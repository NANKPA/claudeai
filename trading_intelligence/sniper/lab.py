"""The sniper lab: run every setup on every market and timeframe, in-sample vs out-of-sample, at two
fee levels, and write the records the scanner and PhilosophyGate use.

    python -m trading_intelligence.sniper lab                      # default grid (crypto majors)
    python -m trading_intelligence.sniper lab --symbols BTCUSDT ETHUSDT --timeframes 15m 1h

Outputs (trading-intelligence/10_sniper-lab/backtests/): summary.csv (one row per setup x timeframe x
fee level, pooled across markets, plus per-market rows), records.json (the gate records) and
backtest-report.md. Every configuration counts as a trial for the deflated-Sharpe check.
"""
from __future__ import annotations

import argparse
import json
from concurrent.futures import ProcessPoolExecutor
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from .._paths import repo_root
from . import records as rec
from .backtest import Costs, run
from .feeds import DUKA_POINT, INTERVAL_SECONDS, binance_history, dukascopy_history
from .setups import SETUPS, prepare

HTF = {"5m": "1h", "15m": "4h", "30m": "4h", "1h": "1D", "4h": "1D"}
# Per-side costs as a fraction of price. Crypto: exchange fees (maker for resting limits, taker plus
# slippage for market orders and stops); the candles are trade prices, so there is no separate spread.
# Forex and gold: the candles are BID prices; buys pay the ask (bid + FX_SPREAD) inside the simulation,
# so each forex cost level is its own simulation and its fees are the commission only.
# See 10_sniper-lab/small-account-venues.md for the sources.
FEES = {
    "std": Costs(maker_fee=0.0008, taker_fee=0.0010, slippage=0.0002),     # typical lowest retail crypto tier
    "low": Costs(maker_fee=0.0000, taker_fee=0.0005, slippage=0.0001),     # zero-maker crypto venue (MEXC spot level)
    "ultra": Costs(maker_fee=0.0000, taker_fee=0.0002, slippage=0.0001),   # the cheapest found (Binance.US spot, US only)
    # forex/gold: the spread is paid in the prices (FX_SPREAD below), so the fees hold only commission
    "fx_std": Costs(maker_fee=0.0, taker_fee=0.0, slippage=0.00002),             # spread-only account (~1.3-1.4 pips)
    "fx_raw": Costs(maker_fee=0.000032, taker_fee=0.000032, slippage=0.00001),   # raw spread + $3.50/lot/side commission
}
FX_SPREAD = {"fx_std": 0.00012, "fx_raw": 0.000015}    # the spread as a fraction of price: ~1.3 pips and ~0.15 pip EUR/USD
FEE_MARKET = {"std": "crypto", "low": "crypto", "ultra": "crypto", "fx_std": "fx", "fx_raw": "fx"}
CRYPTO = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "XRPUSDT"]
FX = ["EURUSD", "GBPUSD", "USDJPY", "XAUUSD"]


def market_of(symbol: str) -> str:
    return "fx" if symbol in DUKA_POINT else "crypto"


def history(symbol: str, tf: str, start: str, end: str | None):
    if market_of(symbol) == "fx":
        return dukascopy_history(symbol, tf, start, end)
    return binance_history(symbol, tf, start, end)


def setups_for(market: str, tf: str):
    for S in SETUPS.values():
        if market not in S.markets:
            continue
        if S.max_tf and INTERVAL_SECONDS[tf] > INTERVAL_SECONDS[S.max_tf]:
            continue
        yield S
OUT = repo_root() / "trading-intelligence" / "10_sniper-lab" / "backtests"


def recost(trades: pd.DataFrame, c: Costs) -> pd.DataFrame:
    t = trades.copy()
    if t.empty:
        return t
    entry_fee = t["order"].map({"limit": c.maker_fee, "market": c.taker_fee + c.slippage}).astype(float)
    exit_fee = (t["exit_reason"] == "target").map({True: c.maker_fee, False: c.taker_fee + c.slippage})
    risk = (t["plan_entry"] - t["stop"]).abs()
    t["cost_r"] = (t["entry"] * entry_fee + t["exit"] * exit_fee) / risk
    t["net_r"] = t["gross_r"] - t["cost_r"]
    return t


def _job_key(start, end, only) -> str:
    """Saved job results are reused only for the same period, setups and engine code."""
    import hashlib
    here = Path(__file__).parent
    h = hashlib.sha1(repr((start, end, sorted(only or []))).encode())
    for f in ("setups.py", "backtest.py", "feeds.py"):
        h.update((here / f).read_bytes())
    h.update(repr(sorted(FEES.items())).encode() + repr(sorted(FX_SPREAD.items())).encode())
    return h.hexdigest()[:10]


def _job(args) -> pd.DataFrame:
    """One market x timeframe. Saved under <out>/jobs/ as soon as it finishes, so an interrupted grid
    resumes where it stopped (delete the folder, or pass --fresh, to recompute)."""
    symbol, tf, start, end, only, jobdir = args
    path = Path(jobdir) / f"{symbol}_{tf}_{_job_key(start, end, only)}.csv.gz"
    if path.exists():
        t = pd.read_csv(path, parse_dates=["signal_time", "entry_time", "exit_time"])
        print(f"  {symbol} {tf}: {len(t)} trades (saved)", flush=True)
        return t
    mk = market_of(symbol)
    df = history(symbol, tf, start, end)
    d = prepare(df, htf=HTF[tf], day="fx" if mk == "fx" else "utc")
    base = FEES["fx_std" if mk == "fx" else "std"]
    sims = [(lvl, FEES[lvl], FX_SPREAD[lvl]) for lvl in FX_SPREAD] if mk == "fx" else [("std", base, 0.0)]
    parts = []
    for lvl, costs, spread in sims:
        for S in setups_for(mk, tf):
            if only and S.id not in only:
                continue
            x = run(d, S(tf=tf, htf=HTF[tf], symbol=symbol), costs, symbol, prepared=True, trigger_spread=spread)
            if not x.empty:
                x["sim"] = lvl
                parts.append(x)
    t = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame()
    if not t.empty:
        t["timeframe"] = tf
        t["market"] = mk
        tmp = path.with_suffix(".tmp")
        t.to_csv(tmp, index=False, compression="gzip")
        tmp.replace(path)
    print(f"  {symbol} {tf}: {len(t)} trades", flush=True)
    return t


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="sniper lab")
    ap.add_argument("--symbols", nargs="+", default=CRYPTO + FX)
    ap.add_argument("--timeframes", nargs="+", default=["5m", "15m", "1h", "4h"])
    ap.add_argument("--setups", nargs="+", default=None, help="only these setup ids (default: all)")
    ap.add_argument("--start", default="2022-01")
    ap.add_argument("--end", default=None)
    ap.add_argument("--split", default="2024-01-01", help="in-sample before, out-of-sample from this date")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--fresh", action="store_true", help="discard saved per-job results and recompute everything")
    ap.add_argument("--from-trades", action="store_true", help="rebuild the summary from saved trades without re-simulating")
    ap.add_argument("--inputs", nargs="+", default=None, help="with --from-trades: trade files to combine (default <out>/trades.csv.gz)")
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    if a.from_trades:
        files = [Path(x) for x in a.inputs] if a.inputs else [out / "trades.csv.gz"]
        trades = pd.concat([pd.read_csv(f, parse_dates=["signal_time", "entry_time", "exit_time"]) for f in files],
                           ignore_index=True)
        if a.inputs:
            trades.to_csv(out / "trades.csv.gz", index=False, compression="gzip")
    else:
        jobdir = out / "jobs"
        if a.fresh and jobdir.exists():
            for f in jobdir.glob("*.csv.gz"):
                f.unlink()
        jobdir.mkdir(parents=True, exist_ok=True)
        jobs = [(s, tf, a.start, a.end, a.setups, str(jobdir)) for s in a.symbols for tf in a.timeframes]
        jobs.sort(key=lambda j: INTERVAL_SECONDS[j[1]])          # the long 5m jobs first
        with ProcessPoolExecutor(max_workers=a.workers) as ex:
            frames = [f for f in ex.map(_job, jobs) if f is not None and not f.empty]
        trades = pd.concat(frames, ignore_index=True)
        trades.to_csv(out / "trades.csv.gz", index=False, compression="gzip")
    rows, entries = [], []
    if "market" not in trades.columns:
        trades["market"] = trades["symbol"].map(market_of)
    if "sim" not in trades.columns:
        trades["sim"] = "std"
    trades["sim"] = trades["sim"].fillna("std")
    for fee_name, costs in FEES.items():
        mk = FEE_MARKET[fee_name]
        # crypto levels are re-priced from one simulation; each forex level is its own simulation (its spread)
        sel = (trades["market"] == mk) & ((trades["sim"] == fee_name) if mk == "fx" else True)
        tf_all = recost(trades[sel], costs)
        if tf_all.empty:
            continue
        for (setup, tf), g in tf_all.groupby(["setup", "timeframe"]):
            key = f"{setup}@{tf}@{fee_name}"
            e = rec.build_record(g, key, a.split)
            e.update({"setup": setup, "timeframe": tf, "fees": fee_name, "market": FEE_MARKET[fee_name],
                      "costs": asdict(costs), "symbols": sorted(g["symbol"].unique()),
                      "period": [a.start, a.end or "latest"]})
            entries.append(e)
            rows.append({"key": key, "scope": "pooled", "market": FEE_MARKET[fee_name], "setup": setup, "timeframe": tf,
                         "fees": fee_name,
                         **{f"is_{k}": v for k, v in e["is"].items()}, **{f"oos_{k}": v for k, v in e["oos"].items()},
                         "is_all_n": e["is_unfiltered"].get("n"), "is_all_mean_net_r": e["is_unfiltered"].get("mean_net_r"),
                         "is_all_mean_gross_r": e["is_unfiltered"].get("mean_gross_r"),
                         "oos_all_n": e["oos_unfiltered"].get("n"), "oos_all_mean_net_r": e["oos_unfiltered"].get("mean_net_r"),
                         "oos_all_mean_gross_r": e["oos_unfiltered"].get("mean_gross_r"),
                         "oos_all_mean_cost_r": e["oos_unfiltered"].get("mean_cost_r"),
                         "oos_all_per_day": e["oos_unfiltered"].get("per_day"),
                         "median_stop_pct": e["oos_unfiltered"].get("median_stop_pct"),
                         "valid_regimes": " ".join(e["valid_regimes"]), "valid_sessions": " ".join(e["valid_sessions"]),
                         "conditions_held": bool(e.get("conditions_held_in_sample"))})
            for sym, gs in g.groupby("symbol"):
                es = rec.build_record(gs, f"{key}:{sym}", a.split)
                rows.append({"key": f"{key}:{sym}", "scope": "market", "market": FEE_MARKET[fee_name], "setup": setup,
                             "timeframe": tf, "fees": fee_name,
                             **{f"is_{k}": v for k, v in es["is"].items()}, **{f"oos_{k}": v for k, v in es["oos"].items()}})
    summary = pd.DataFrame(rows)
    summary.to_csv(out / "summary.csv", index=False)
    deflated = rec.deflated_best(entries)
    # Every configuration was chosen from many tried. Unless the best survives the multiple-testing
    # check, the out-of-sample years were used to CHOOSE it and are no longer clean evidence for it:
    # the record is provisional, and only trades after the lab's data (forward) can confirm it.
    survives = (deflated.get("deflated_sharpe_prob") or 0) >= 0.95
    for e in entries:
        e["provisional"] = not survives
        e["deflated_sharpe_prob_best"] = deflated.get("deflated_sharpe_prob")
    rec.save(entries, out / "records.json")
    (out / "deflated.json").write_text(json.dumps(deflated, indent=1))
    write_report(summary, entries, deflated, a, out, trades)
    write_setups_registry(summary, out.parent / "setups.yaml")
    print(summary[summary["scope"] == "pooled"][["key", "is_n", "is_mean_net_r", "oos_n", "oos_mean_net_r", "oos_t",
                                                 "oos_mean_cost_r", "oos_per_day"]].to_string(index=False))
    print("deflated best:", deflated)
    return 0


def _coverage(trades: pd.DataFrame) -> list[str]:
    """What actually ran, read from the trades (not from the command line)."""
    out = []
    for mk, src in (("crypto", "Binance spot archive"), ("fx", "Dukascopy BID candles")):
        t = trades[trades["market"] == mk]
        if t.empty:
            continue
        per = t.groupby("symbol")["timeframe"].agg(lambda x: "/".join(sorted(set(x), key=lambda v: INTERVAL_SECONDS[v])))
        start, end = t["signal_time"].min(), t["exit_time"].max()
        out.append(f"{'Crypto' if mk == 'crypto' else 'Forex and gold'} ({src}): "
                   + ", ".join(f"{sym} {tfs}" for sym, tfs in per.items())
                   + f"; signals {start:%Y-%m-%d} to {end:%Y-%m-%d}")
    return out


def _breakdown(trades: pd.DataFrame, e: dict) -> list[str]:
    """Per-year and per-market results of a passing record's out-of-sample trades, so a result carried
    by one market or one year is visible."""
    t = trades[(trades["setup"] == e["setup"]) & (trades["timeframe"] == e["timeframe"])
               & (trades["market"] == FEE_MARKET[e["fees"]])]
    if FEE_MARKET[e["fees"]] == "fx":
        t = t[t["sim"] == e["fees"]]
    t = recost(t, FEES[e["fees"]])
    t = t[(t["signal_time"] >= pd.Timestamp(e["split_date"], tz="UTC")) & t["regime"].isin(e["valid_regimes"])
          & t["session"].isin(e["valid_sessions"])]
    if t.empty:
        return []
    rows = []
    for name, g in list(t.groupby(t["signal_time"].dt.year)) + list(t.groupby("symbol")):
        rows.append(f"{name}: {len(g)} trades, {g['net_r'].mean():+.3f}R, total {g['net_r'].sum():+.1f}R")
    top5 = t["net_r"].nlargest(5).sum() / t["net_r"].sum() if t["net_r"].sum() > 0 else float("nan")
    tail = f"; the 5 best trades are {top5:.0%} of the total" if top5 == top5 else ""
    return [f"  - by year and market: " + "; ".join(rows) + tail]


def write_report(summary: pd.DataFrame, entries: list[dict], deflated: dict, a, out: Path,
                 trades: pd.DataFrame | None = None) -> None:
    pooled = summary[summary["scope"] == "pooled"].sort_values(["market", "fees", "timeframe", "setup"])
    passing = [e for e in entries if e.get("record") and rec.effective_n(e["oos"]) >= 30 and e["oos"].get("se")
               and e["oos"]["mean_net_r"] - max(e["oos"]["se"], e["oos"].get("se_day") or 0) > 0]
    when = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    cov = _coverage(trades) if trades is not None else []
    L = ["---", "id: synthesis_sniper_backtests", "type: synthesis",
         'title: "Sniper Lab — backtests of the codified sniper entries (in-sample vs out-of-sample)"',
         "partition: 10_sniper-lab", "layer: L8",
         "related: [synthesis_sniper_entries, synthesis_small_account_venues, synthesis_evidence_lab, framework_decision_protocol, philosophy_relationship]",
         "status: computed", "---", "",
         "# Sniper Lab — backtests", "",
         f"> Generated {when} by `python -m trading_intelligence.sniper lab`. Education and research, not a trading signal.", ""]
    L += ["**What ran.** " + " ".join(f"{c}." for c in cov), "",
          f"**Method.** Allowed regimes and sessions are chosen on signals before {a.split} (in-sample); the trades in a "
          "kept regime AND a kept session must also have been positive in-sample. Everything is then judged on signals "
          f"from {a.split} on (out-of-sample). Each configuration (setup × timeframe × cost level) pools its markets. "
          "The three crypto fee levels are the same trades re-priced; each forex account type is its own simulation.", "",
          "**Fills.** A market entry fills at the next bar's open. A resting limit entry fills only when price trades "
          "THROUGH it (a touch is not a fill). On later bars, when the stop and the target fall in the same bar, the stop "
          "counts; a bar that opens beyond the stop exits at that open. On the fill bar the stop is checked first, and a "
          "bar that closes beyond the target exits at the target. A target fills on a TOUCH at the target price and pays "
          "the maker fee: that assumes queue priority and is the one optimistic rule (see Known limits). R is measured "
          "on the planned risk, the risk the gate sizes on.", "",
          "## Cost levels (fraction of price)", "",
          "| Level | Market | Resting limit (per side) | Market order / stop (per side) | Slippage on market entries, stops, time exits | Spread per round trip (paid in the prices) |",
          "|---|---|---|---|---|---|"]
    for name, c in FEES.items():
        sp = FX_SPREAD.get(name, 0.0)
        L.append(f"| {name} | {FEE_MARKET[name]} | {c.maker_fee:.4%} | {c.taker_fee:.4%} | {c.slippage:.4%} | {sp:.4%} |")
    for mk, title in (("crypto", "Crypto"), ("fx", "Forex and gold")):
        pm = pooled[pooled["market"] == mk]
        if pm.empty:
            continue
        note = ("IS = in-sample (before the split), OOS = out-of-sample. Gross R is before fees; net R is after fees and "
                "slippage at that level." if mk == "crypto" else
                "IS = in-sample (before the split), OOS = out-of-sample. The candles are bid prices and every buy pays the "
                "ask, so **gross R is already after the spread** (it changes with the account type); the cost column is "
                "commission plus slippage only. The ask is modelled as bid × (1 + spread): 0.012% on fx_std (about 1.4 pips "
                "on EUR/USD, 1.8 on USD/JPY, $0.40 on gold) and 0.0015% on fx_raw (about 0.17 pip, 0.23 pip, $0.05), the "
                "same fraction for every market and hour, with no widening at rollover or news.")
        L += ["", f"## {title}: every trade, pooled across markets", "", note, "",
              "| Setup | TF | Costs | OOS trades/day | Stop % | IS gross R | OOS gross R | OOS cost R | OOS net R |",
              "|---|---|---|---|---|---|---|---|---|"]
        for _, r in pm.iterrows():
            L.append(f"| {r['setup']} | {r['timeframe']} | {r['fees']} | {_f(r.get('oos_all_per_day'), 2)} | "
                     f"{_f((r.get('median_stop_pct') or 0) * 100, 2)} | {_f(r.get('is_all_mean_gross_r'))} | "
                     f"{_f(r.get('oos_all_mean_gross_r'))} | {_f(r.get('oos_all_mean_cost_r'))} | {_f(r.get('oos_all_mean_net_r'))} |")
    L += ["", "## Inside the conditions chosen in-sample (the record the gate reads)", "",
          "A regime and a session are each kept when, on their own, they were positive after costs in-sample on at least "
          "20 trades. The trades in both a kept regime and a kept session must then also be positive in-sample on at "
          "least 20 trades (\"held\"); only then is there a record. The out-of-sample trades inside the conditions are "
          "the evidence.", "",
          "| Setup | TF | Costs | Allowed regimes | Allowed sessions | IS n | IS net R | Held | OOS n | OOS net R | OOS t | OOS t (by day) |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    chosen = pooled[pooled["is_n"].fillna(0) > 0]
    for _, r in chosen.iterrows():
        L.append(f"| {r['setup']} | {r['timeframe']} | {r['fees']} | {r.get('valid_regimes') or '-'} | "
                 f"{r.get('valid_sessions') or '-'} | {int(r.get('is_n') or 0)} | {_f(r.get('is_mean_net_r'))} | "
                 f"{'yes' if r.get('conditions_held') else 'no'} | "
                 f"{int(r.get('oos_n') or 0)} | {_f(r.get('oos_mean_net_r'))} | {_f(r.get('oos_t'), 2)} | {_f(r.get('oos_t_day'), 2)} |")
    if chosen.empty:
        L.append("| (none: no regime and session was positive after costs in-sample) | | | | | | | | | | | |")
    L += ["", "## What passes the owner's gate", ""]
    if passing:
        L += [f"{len(passing)} configuration(s) have at least 30 effectively independent out-of-sample trades and mean - 1 SE "
              "> 0 after costs, with the SE clustered by day as well as per trade (Gate 4's math score of 2). The scanner's "
              "gate can take only these:", ""]
        distinct = len({(e["setup"], e["timeframe"], FEE_MARKET[e["fees"]]) for e in passing})
        if distinct < len(passing):
            L += [f"These are {distinct} distinct strategies: the same setup and timeframe at two cost levels shares most "
                  "of its trades, so it counts once.", ""]
        for e in passing:
            L.append(f"- `{e['setup_key']}`: OOS n {e['oos']['n']} (effective {rec.effective_n(e['oos'])}), "
                     f"{e['oos']['mean_net_r']:+.3f}R per trade (SE {max(e['oos']['se'], e['oos'].get('se_day') or 0):.3f}), "
                     f"in-sample inside the same conditions {e['is'].get('mean_net_r', float('nan')):+.3f}R over "
                     f"{e['is'].get('n', 0)} trades, {e['oos']['per_day']:.2f} trades/day, regimes "
                     f"{', '.join(e['valid_regimes'])}, sessions {', '.join(e['valid_sessions'])}")
            if trades is not None:
                L += _breakdown(trades, e)
        L += ["", "Passing Gate 4 is necessary, not sufficient. These were chosen out of every configuration tried, using the "
              "same out-of-sample years that now make them look good; the multiple-testing result below says whether that "
              "choice could be luck."]
        if not ((deflated.get("deflated_sharpe_prob") or 0) >= 0.95):
            L += ["", "**They do not survive it, so every record is marked provisional.** The scanner paper-trades them "
                  "through the gate as usual. It hands a take to the owner's own order code (`--on-take`) only when the "
                  "FULL gate, run on that setup's forward trades alone (signals after the lab's data ended, inside its "
                  "chosen regimes and sessions, day-clustered like the lab), also says take; the size handed over comes "
                  "from that forward-only decision. Forward trades played no part in choosing the setup, so they are the "
                  "clean test. At a few trades a month, 30 of them take many months."]
    else:
        L += ["**None.** No configuration has an out-of-sample record that clears Gate 4 after costs. The gate will skip "
              "every live signal from these setups until a record does; the scanner keeps following them on paper to "
              "build forward evidence."]
    L += ["", "## Multiple testing", "",
          f"{deflated.get('trials', 0)} configurations were tried; {deflated.get('judged', 0)} have a record (conditions held "
          "in-sample) and at least 30 effectively independent out-of-sample trades inside them. "
          + (f"The best of those (`{deflated['best']}`, per-trade Sharpe {deflated['best_sharpe_per_trade']:+.3f} over "
             f"{deflated['best_n']} trades) has a deflated-Sharpe probability of {deflated['deflated_sharpe_prob']:.2f} of being "
             "real once the number of trials is counted (Bailey & López de Prado; 0.95 is the usual bar)."
             if deflated.get("best") else ""), "",
          "## Reading this as the owner's philosophy asks", ""]
    for mk, title in (("crypto", "Crypto"), ("fx", "Forex and gold")):
        pm = pooled[pooled["market"] == mk].dropna(subset=["oos_all_mean_gross_r"])
        if pm.empty:
            continue
        b = pm.sort_values("oos_all_mean_gross_r", ascending=False).iloc[0]
        pos = pm[pm["oos_all_mean_net_r"] > 0]
        what = "before fees" if mk == "crypto" else "after the spread, before commission"
        L.append(f"- **{title}.** Best out-of-sample average {what}: {b['oos_all_mean_gross_r']:+.3f}R per trade "
                 f"({b['setup']} {b['timeframe']} {b['fees']}, {int(b['oos_all_n'])} trades; in-sample "
                 f"{b['is_all_mean_gross_r']:+.3f}R). {len(pos)} of {len(pm)} configurations are positive after costs "
                 "out-of-sample before the in-sample condition filter.")
    L += ["- Crypto: a pattern that does not pay before fees cannot be rescued by a cheaper venue; cheaper fees only "
          "shrink the loss (Section VII: expected value first). Forex: the gross column already includes the spread, so "
          "the account type changes it.",
          "- Cost in R = round-trip cost / stop distance. A 5-minute crypto stop of 0.2-0.3% against a 0.2% round trip "
          "costs most of 1R; the same stop in EUR/USD against a 0.01% round trip costs a few hundredths (Gate 5.6).",
          "- More trades is not more edge: every trade pays the cost, so frequency multiplies a negative expectancy.",
          "- Only the out-of-sample columns are evidence; in-sample numbers chose the conditions (Section XVII).", "",
          "## Known limits of this test", "",
          "- **Target fills on a touch** at the target price (queue priority assumed). This can only flatter results.",
          "- **Forex spread is modelled**, a fixed fraction of price on BID candles, not the recorded ask; real spreads "
          "widen at rollover and on news.",
          "- **Pooled markets are correlated.** The day-clustered SE and the effective n correct for same-day "
          "trades, not for every dependence.",
          "- **The search over regimes and sessions** is not counted as extra trials in the deflated Sharpe, so that "
          "check is, if anything, too kind.",
          "- **Forward evidence must come from comparable data.** The lab used Binance trades and Dukascopy bid candles. "
          "A scanner fed by another source (Yahoo quotes, a broker feed) builds forward records on different prices.",
          "- **Crypto coverage was cut short by the owner:** BNB, XRP and the 1h/4h crypto timeframes were not run. "
          "Intraday forex (5m/15m) needs minute history that throttles cloud servers; run it at home.", ""]
    (out.parent / "backtest-report.md").write_text("\n".join(L), encoding="utf-8")


def write_setups_registry(summary: pd.DataFrame, path: Path) -> None:
    """The codified setups as knowledge-graph nodes, linked to the playbooks and concepts they came from."""
    import yaml
    pooled = summary[summary["scope"] == "pooled"]
    out = []
    for sid, S in SETUPS.items():
        rows = pooled[pooled["setup"] == sid].dropna(subset=["oos_all_mean_net_r"])
        tested = [{"config": r["key"], "oos_trades": int(r["oos_all_n"] or 0),
                   "oos_gross_r": round(float(r["oos_all_mean_gross_r"]), 3), "oos_net_r": round(float(r["oos_all_mean_net_r"]), 3)}
                  for _, r in rows.sort_values("oos_all_mean_net_r", ascending=False).iterrows()]
        best = dict(tested[0]) if tested else None
        verdict = ("not tested" if not best else
                   "positive after costs out-of-sample in its best configuration (check the gate and multiple testing)"
                   if best["oos_net_r"] > 0 else "negative after costs out-of-sample in every configuration tested")
        out.append({"id": sid, "type": "setup", "title": f"{S.name} (codified)", "derived_from": list(S.derived_from),
                    "related": ["synthesis_sniper_backtests", "synthesis_sniper_entries"],
                    "code": f"trading_intelligence/sniper/setups.py:{S.__name__}", "rules": " ".join((S.__doc__ or "").split()),
                    "markets": list(S.markets), "max_timeframe": S.max_tf, "verdict": verdict,
                    "best_config": best, "tested": tested[:6]})
    head = ("# Generated by `python -m trading_intelligence.sniper lab` - do not edit by hand.\n"
            "# The codified sniper setups as graph nodes (kind: setup), each linked to the playbooks and concepts\n"
            "# it was coded from, with its out-of-sample result (net R per trade after costs; best six configs).\n")
    path.write_text(head + yaml.safe_dump({"setups": out}, sort_keys=False, allow_unicode=True, width=160), encoding="utf-8")


def _f(x, nd=3):
    try:
        return "-" if x is None or pd.isna(x) else f"{float(x):+.{nd}f}" if nd == 3 else f"{float(x):.{nd}f}"
    except (TypeError, ValueError):
        return "-"


if __name__ == "__main__":
    raise SystemExit(main())
