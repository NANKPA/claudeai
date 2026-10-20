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

HTF = {"5m": "1h", "15m": "4h", "1h": "1D", "4h": "1D"}
# Per-side costs as a fraction of price. Crypto: exchange fees (maker for resting limits, taker plus
# slippage for market orders and stops). Forex and gold: half the spread plus commission on every fill
# (no maker rebate), slippage on stops. See 10_sniper-lab/small-account-venues.md for the sources.
FEES = {
    "std": Costs(maker_fee=0.0008, taker_fee=0.0010, slippage=0.0002),     # typical lowest retail crypto tier
    "low": Costs(maker_fee=0.0000, taker_fee=0.0005, slippage=0.0001),     # zero-maker crypto venue (MEXC spot level)
    "ultra": Costs(maker_fee=0.0000, taker_fee=0.0002, slippage=0.0001),   # the cheapest found (Binance.US spot, US only)
    "fx_std": Costs(maker_fee=0.00006, taker_fee=0.00006, slippage=0.00002),   # spread-only, ~1.4 pips EUR/USD round trip
    "fx_raw": Costs(maker_fee=0.00004, taker_fee=0.00004, slippage=0.00001),   # raw spread + commission, ~0.8-0.9 pips
}
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
    risk = (t["entry"] - t["stop"]).abs()
    t["cost_r"] = (t["entry"] * entry_fee + t["exit"] * exit_fee) / risk
    t["net_r"] = t["gross_r"] - t["cost_r"]
    return t


def _job(args) -> pd.DataFrame:
    """One market x timeframe. Saved under <out>/jobs/ as soon as it finishes, so an interrupted grid
    resumes where it stopped (delete the folder, or pass --fresh, to recompute)."""
    symbol, tf, start, end, only, jobdir = args
    path = Path(jobdir) / f"{symbol}_{tf}.csv.gz"
    if path.exists():
        t = pd.read_csv(path, parse_dates=["signal_time", "entry_time", "exit_time"])
        print(f"  {symbol} {tf}: {len(t)} trades (saved)", flush=True)
        return t
    mk = market_of(symbol)
    df = history(symbol, tf, start, end)
    d = prepare(df, htf=HTF[tf], day="fx" if mk == "fx" else "utc")
    base = FEES["fx_std" if mk == "fx" else "std"]
    parts = [run(d, S(tf=tf, htf=HTF[tf], symbol=symbol), base, symbol, prepared=True)
             for S in setups_for(mk, tf) if not only or S.id in only]
    parts = [x for x in parts if not x.empty]
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
    for fee_name, costs in FEES.items():
        tf_all = recost(trades[trades["market"] == FEE_MARKET[fee_name]], costs)
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
                         "valid_regimes": " ".join(e["valid_regimes"]), "valid_sessions": " ".join(e["valid_sessions"])})
            for sym, gs in g.groupby("symbol"):
                es = rec.build_record(gs, f"{key}:{sym}", a.split)
                rows.append({"key": f"{key}:{sym}", "scope": "market", "market": FEE_MARKET[fee_name], "setup": setup,
                             "timeframe": tf, "fees": fee_name,
                             **{f"is_{k}": v for k, v in es["is"].items()}, **{f"oos_{k}": v for k, v in es["oos"].items()}})
    summary = pd.DataFrame(rows)
    summary.to_csv(out / "summary.csv", index=False)
    rec.save(entries, out / "records.json")
    deflated = rec.deflated_best(entries)
    (out / "deflated.json").write_text(json.dumps(deflated, indent=1))
    write_report(summary, entries, deflated, a, out)
    write_setups_registry(summary, out.parent / "setups.yaml")
    print(summary[summary["scope"] == "pooled"][["key", "is_n", "is_mean_net_r", "oos_n", "oos_mean_net_r", "oos_t",
                                                 "oos_mean_cost_r", "oos_per_day"]].to_string(index=False))
    print("deflated best:", deflated)
    return 0


def write_report(summary: pd.DataFrame, entries: list[dict], deflated: dict, a, out: Path) -> None:
    pooled = summary[summary["scope"] == "pooled"].sort_values(["market", "fees", "timeframe", "setup"])
    passing = [e for e in entries if e["oos"].get("n", 0) >= 30 and e["oos"].get("se")
               and e["oos"]["mean_net_r"] - e["oos"]["se"] > 0]
    when = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    syms = sorted(set(summary.get("key", pd.Series(dtype=str)).str.split(":").str[1].dropna()))
    L = ["---", "id: synthesis_sniper_backtests", "type: synthesis",
         'title: "Sniper Lab — backtests of the codified sniper entries (in-sample vs out-of-sample)"',
         "partition: 10_sniper-lab", "layer: L8",
         "related: [synthesis_sniper_entries, synthesis_small_account_venues, synthesis_evidence_lab, framework_decision_protocol, philosophy_relationship]",
         "status: computed", "---", "",
         "# Sniper Lab — backtests", "",
         f"> Generated {when} by `python -m trading_intelligence.sniper lab`. Markets: {', '.join(syms)} (crypto: Binance spot "
         "archive; forex and gold: Dukascopy BID candles). "
         f"Timeframes: {', '.join(a.timeframes)}. Period {a.start} to {a.end or 'last full month'}. Rules and the allowed "
         f"regimes/sessions are chosen on data before {a.split} and judged only on data after it. Fills are conservative "
         "(a limit fills only when price trades at or through it; when stop and target share a bar the stop counts). "
         "Education and research, not a trading signal.", "",
         "## Cost levels (per side, fraction of price)", "",
         "| Level | Market | Resting limit | Market order / stop | Extra slippage on stops |", "|---|---|---|---|---|"]
    for name, c in FEES.items():
        L.append(f"| {name} | {FEE_MARKET[name]} | {c.maker_fee:.4%} | {c.taker_fee:.4%} | {c.slippage:.4%} |")
    for mk, title in (("crypto", "Crypto"), ("fx", "Forex and gold")):
        pm = pooled[pooled["market"] == mk]
        if pm.empty:
            continue
        L += ["", f"## {title}: every trade, pooled across markets", "",
              "IS = in-sample (before the split), OOS = out-of-sample. Gross R is before costs; net R after costs at that level.", "",
              "| Setup | TF | Costs | OOS trades/day | Stop % | IS gross R | OOS gross R | OOS cost R | OOS net R |",
              "|---|---|---|---|---|---|---|---|---|"]
        for _, r in pm.iterrows():
            L.append(f"| {r['setup']} | {r['timeframe']} | {r['fees']} | {_f(r.get('oos_all_per_day'), 2)} | "
                     f"{_f((r.get('median_stop_pct') or 0) * 100, 2)} | {_f(r.get('is_all_mean_gross_r'))} | "
                     f"{_f(r.get('oos_all_mean_gross_r'))} | {_f(r.get('oos_all_mean_cost_r'))} | {_f(r.get('oos_all_mean_net_r'))} |")
    L += ["", "## Inside the conditions chosen in-sample (the record the gate reads)", "",
          "Only regimes and sessions that were positive after costs in-sample (at least 20 trades each) are kept; the "
          "out-of-sample trades inside them are the evidence.", "",
          "| Setup | TF | Costs | Allowed regimes | Allowed sessions | IS n | IS net R | OOS n | OOS net R | OOS t |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    chosen = pooled[pooled["is_n"].fillna(0) > 0]
    for _, r in chosen.iterrows():
        L.append(f"| {r['setup']} | {r['timeframe']} | {r['fees']} | {r.get('valid_regimes') or '-'} | "
                 f"{r.get('valid_sessions') or '-'} | {int(r.get('is_n') or 0)} | {_f(r.get('is_mean_net_r'))} | "
                 f"{int(r.get('oos_n') or 0)} | {_f(r.get('oos_mean_net_r'))} | {_f(r.get('oos_t'), 2)} |")
    if chosen.empty:
        L.append("| (none: no regime and session was positive after costs in-sample) | | | | | | | | | |")
    L += ["", "## What passes the owner's gate", ""]
    if passing:
        L += [f"{len(passing)} configuration(s) have n >= 30 out-of-sample trades and mean - 1 SE > 0 after costs "
              "(Gate 4's math score of 2). The scanner's gate can take only these:", ""]
        L += [f"- `{e['setup_key']}`: OOS n {e['oos']['n']}, {e['oos']['mean_net_r']:+.3f}R per trade (SE {e['oos']['se']:.3f}), "
              f"{e['oos']['per_day']:.2f} trades/day, regimes {', '.join(e['valid_regimes'])}, sessions "
              f"{', '.join(e['valid_sessions'])}" for e in passing]
        L += ["", "Passing Gate 4 is necessary, not sufficient: read it together with the multiple-testing result below."]
    else:
        L += ["**None.** No configuration has an out-of-sample record that clears Gate 4 after costs. The gate will skip "
              "every live signal from these setups until a record does; the scanner keeps following them on paper to "
              "build forward evidence."]
    L += ["", "## Multiple testing", "",
          f"{deflated.get('trials', 0)} configurations were tried; {deflated.get('judged', 0)} had at least 30 out-of-sample "
          "trades inside their chosen conditions. "
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
        L.append(f"- **{title}.** Best out-of-sample average before costs: {b['oos_all_mean_gross_r']:+.3f}R per trade "
                 f"({b['setup']} {b['timeframe']}). {len(pos)} of {len(pm)} configurations are positive after costs "
                 "out-of-sample (before the in-sample condition filter).")
    L += ["- A pattern that does not pay before costs cannot be rescued by a cheaper venue; cheaper costs only shrink the "
          "loss (Section VII: expected value first).",
          "- Cost in R = round-trip cost / stop distance. A 5-minute crypto stop of 0.2-0.3% against a 0.2% round trip "
          "costs most of 1R; the same stop in EUR/USD against a 0.01% round trip costs a few hundredths (Gate 5.6).",
          "- More trades is not more edge: every trade pays the cost, so frequency multiplies a negative expectancy.",
          "- Only the out-of-sample columns are evidence; in-sample numbers chose the conditions (Section XVII).", ""]
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
        best = tested[0] if tested else None
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
