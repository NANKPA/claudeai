"""The sniper scanner: watch live CLOSED candles, turn each setup signal into a TradeProposal, run it
through PhilosophyGate, journal the decision, and paper-trade it with the backtester's own fill rules.

    python -m trading_intelligence.sniper scan                        # loop forever, BTC/ETH/SOL 15m + 1h
    python -m trading_intelligence.sniper scan --once                 # one pass (for cron / Task Scheduler)
    python -m trading_intelligence.sniper scan --equity 20 --risk-pct 1 --min-notional 5 --max-leverage 1
    python -m trading_intelligence.sniper scan --report               # forward results so far

Two books are kept, so the evidence grows whatever the gate decides:
- shadow: EVERY signal is followed with the same fill rules (one order or position per setup and
  market). These results are new out-of-sample evidence; they are added to the setup's record (inside
  the regimes and sessions chosen in-sample) the next time the gate looks at that setup.
- account: only the gate's "take" decisions, sized by Gate 6 for the paper equity (any amount).
  Outcomes are written back into the journal row of the decision.

Nothing here sends an order to a venue. `--on-take "command"` hands each gated TAKE (and only those) to
your own execution code as JSON on stdin, after its journal row is written. The operator's state for Gate 0 is read from `state.txt` in the
scanner's home folder on every pass (default "calm"): write "tired" there and risk halves, write
"frustrated" and the gate stands aside.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import os
import time
from dataclasses import asdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from .. import gate as G
from ..journal import Journal
from . import records as rec
from .backtest import Book, Costs
from .feeds import INTERVAL_SECONDS, latest, recent
from .lab import FEE_MARKET, FEES, FX_SPREAD, HTF, OUT as LAB_OUT, market_of, setups_for
from .setups import SETUPS, Signal, prepare

HOME = Path(os.environ.get("TI_SNIPER_HOME", Path.home() / ".trading-intelligence" / "sniper-paper"))
HISTORY_DAYS = {"5m": 35, "15m": 60, "1h": 150}
FORWARD_COLS = ["uid", "key", "trade_id", "account", "timeframe", "setup", "symbol", "side", "order", "signal_time",
                "entry_time", "exit_time", "plan_entry", "entry", "stop", "target", "exit", "exit_reason", "stop_pct", "gross_r",
                "cost_r", "net_r", "mae_r", "mfe_r", "bars_held", "regime", "session"]
ACCOUNT_COLS = ["exit_time", "trade_id", "key", "symbol", "session", "net_r", "risk_pct", "size", "pnl", "equity"]


def _venue_symbol(venue: str, sym: str) -> str:
    """BTCUSDT / EURUSD -> the venue's spelling."""
    if venue == "yahoo":
        return {"XAUUSD": "GC=F", "XAGUSD": "SI=F"}.get(sym, f"{sym}=X")
    base, quote = sym[:-4], sym[-4:]
    return {"coinbase": f"{base}-{'USD' if quote == 'USDT' else quote}", "okx": f"{base}-{quote}",
            "kucoin": f"{base}-{quote}"}.get(venue, sym)


def _csv_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _append(path: Path, cols: list[str], row: dict) -> None:
    if path.exists():
        with path.open(newline="", encoding="utf-8") as f:
            header = next(csv.reader(f), [])
        if header and header != cols:          # written by an older version: keep it aside, start a new file
            path.rename(path.with_name(f"{path.stem}.old-{int(time.time())}{path.suffix}"))
    new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        if new:
            w.writeheader()
        w.writerow(row)
        f.flush()
        os.fsync(f.fileno())


def point_value(symbol: str, price: float) -> float:
    """Account currency (USD) per 1.0 price move per unit. USD-base pairs (USDJPY ...) pay in the quote
    currency, so one unit is worth 1/price dollars per 1.0 move. Crosses (EURJPY, EURGBP ...) need a
    second rate and are refused."""
    if market_of(symbol) != "fx":
        if symbol.upper().replace("-", "").endswith(("USDT", "USDC", "FDUSD", "USD")):
            return 1.0
        raise ValueError(f"{symbol}: only crypto pairs quoted in USD or a USD stablecoin can be sized in a USD account")
    if symbol.endswith("USD"):
        return 1.0
    if symbol.startswith("USD"):
        return 1.0 / price
    raise ValueError(f"{symbol}: only pairs quoted in USD, or with USD as the base, can be sized in a USD account")


# ── the paper account ───────────────────────────────────────────────────────
class PaperAccount:
    def __init__(self, home: Path, equity0: float):
        self.path = home / "account.csv"
        self.equity0 = equity0

    def rows(self) -> list[dict]:
        return _csv_rows(self.path)

    def equity(self) -> float:
        r = self.rows()
        return float(r[-1]["equity"]) if r else self.equity0

    def state(self, key: str, session: str, now: datetime, open_risk_pct: float, emotional_state: str,
              base_risk_pct: float, lot_step: float, min_notional: float, style: str,
              point_value: float = 1.0) -> G.AccountState:
        rows = self.rows()
        eq = [self.equity0] + [float(r["equity"]) for r in rows]
        peak = max(eq)
        today = now.date()
        week = now.isocalendar()[:2]
        t_rows = [(pd.Timestamp(r["exit_time"]).to_pydatetime(), r) for r in rows]
        today_rows = [(t, r) for t, r in t_rows if t.date() == today]
        realized_today = sum(float(r["net_r"]) for _, r in today_rows)
        realized_week = sum(float(r["net_r"]) for t, r in t_rows if t.isocalendar()[:2] == week)
        streak = 0
        for _, r in reversed(today_rows):
            if r["key"] != key or r["session"] != session:
                continue
            if float(r["net_r"]) < 0:
                streak += 1
            else:
                break
        losses = [t for t, r in today_rows if float(r["net_r"]) < 0]
        mins = (now - max(losses)).total_seconds() / 60 if losses else None
        return G.AccountState(equity=eq[-1], emotional_state=emotional_state, point_value=point_value, lot_step=lot_step,
                              min_order_notional=min_notional, base_risk_pct=base_risk_pct, trading_style=style,
                              realized_today_r=realized_today, realized_week_r=realized_week,
                              consecutive_losses_setup_session=streak,
                              drawdown_from_peak_pct=(peak - eq[-1]) / peak * 100 if peak > 0 else 0.0,
                              open_risk_pct=open_risk_pct, minutes_since_last_loss=mins,
                              loss_this_session=any(float(r["net_r"]) < 0 and r["session"] == session for _, r in today_rows))

    def book_trade(self, tr: dict, tag: dict, closed_at) -> dict | None:
        """Book a closed gated trade once (a restart after a crash must not book it twice)."""
        if any(r["trade_id"] == tag["trade_id"] for r in self.rows()):
            return None
        risk_per_unit = abs(tr["plan_entry"] - tr["stop"])
        pnl = tag["size"] * risk_per_unit * tr["net_r"] * tag.get("point_value", 1.0)
        row = {"exit_time": pd.Timestamp(closed_at).isoformat(), "trade_id": tag["trade_id"], "key": tag["key"],
               "symbol": tr["symbol"], "session": tr["session"], "net_r": round(tr["net_r"], 5),
               "risk_pct": tag["risk_pct"], "size": tag["size"], "pnl": round(pnl, 6), "equity": round(self.equity() + pnl, 6)}
        _append(self.path, ACCOUNT_COLS, row)
        return row


# ── book persistence ────────────────────────────────────────────────────────
def _dump_book(b: Book) -> dict:
    def sig(s):
        d = asdict(s)
        d["time"] = pd.Timestamp(s.time).isoformat()
        return d
    pend = None if b.pending is None else {"sig": sig(b.pending["sig"]), "last_k": b.pending["last_k"]}
    pos = None
    if b.pos is not None:
        pos = {**b.pos, "sig": sig(b.pos["sig"]), "entry_time": pd.Timestamp(b.pos["entry_time"]).isoformat()}
    return {"k": b.k, "pending": pend, "pos": pos, "tag": b.tag}


def _load_book(d: dict, costs: Costs, symbol: str, trigger_spread: float = 0.0) -> Book:
    def sig(x):
        x = dict(x)
        x["time"] = pd.Timestamp(x["time"])
        return Signal(**x)
    b = Book(costs, symbol, trigger_spread)
    b.k, b.tag = d.get("k", -1), d.get("tag")
    if d.get("pending"):
        b.pending = {"sig": sig(d["pending"]["sig"]), "last_k": d["pending"]["last_k"]}
    if d.get("pos"):
        p = dict(d["pos"])
        p["sig"], p["entry_time"] = sig(p["sig"]), pd.Timestamp(p["entry_time"])
        b.pos = p
    return b


# ── records: backtest OOS + forward shadow trades ───────────────────────────
def setup_record(key: str, lab: dict, forward: list[dict]) -> G.SetupRecord | None:
    e = lab.get(key)
    if not e or not e.get("record"):
        return None
    r = dict(e["record"])
    regimes, sessions = set(r["valid_regimes"]), set(r["valid_sessions"])
    end = pd.Timestamp(e["oos_end"]) if e.get("oos_end") else None       # a re-run lab may already contain them
    fwd = [x for x in forward if x["key"] == key and x["regime"] in regimes and x["session"] in sessions
           and (end is None or pd.Timestamp(x["signal_time"]) > end)]
    if fwd:
        n0 = len(r["results_r"])
        r["results_r"] = r["results_r"] + [float(x["net_r"]) for x in fwd]
        r["avg_cost_r"] = (r["avg_cost_r"] * n0 + sum(float(x["cost_r"]) for x in fwd)) / (n0 + len(fwd))
        if r.get("effective_n") is not None and n0:                 # forward trades are clustered alike
            r["effective_n"] = int(r["effective_n"] + len(fwd) * r["effective_n"] / n0)
    return G.SetupRecord(**r)


def trade_id_for(key: str, symbol: str, sig: Signal) -> str:
    return f"{key}-{symbol}-{pd.Timestamp(sig.time):%Y%m%dT%H%M}"


def proposal(sig: Signal, key: str, symbol: str, tf: str, costs: Costs, derived_from,
             spread: float = 0.0) -> G.TradeProposal:
    entry_fee = costs.maker_fee if sig.order == "limit" else costs.taker_fee + costs.slippage
    exit_fee = costs.taker_fee + costs.slippage                          # the stop exit: the dear case
    t = sig.text
    return G.TradeProposal(
        setup_id=key, instrument=symbol, side=sig.side, entry=sig.entry, stop=sig.stop, target=sig.target,
        cost_price=sig.entry * entry_fee + sig.stop * exit_fee + sig.entry * spread,   # forex: one spread per round trip
        timeframe=f"{HTF[tf]}/{tf}", regime_tag=sig.regime,
        session=sig.session, observation=t["observation"], interpretation=t["interpretation"],
        alternative_interpretation=t["alternative_interpretation"], hypothesis=t["hypothesis"], horizon=t["horizon"],
        invalidation=t["invalidation"], explanation=t["explanation"], undermined_by=t["undermined_by"],
        required_conditions=list(sig.conditions), conditions_present=dict(sig.conditions),
        evidence_for=[f"signal at the close of the {tf} bar opened {pd.Timestamp(sig.time):%Y-%m-%d %H:%M} UTC",
                      f"codified from {', '.join(derived_from)}"],
        trade_id=trade_id_for(key, symbol, sig))                                 # one decision per signal, restart-safe


# ── the scan ────────────────────────────────────────────────────────────────
class Scanner:
    def __init__(self, a):
        self.a = a
        self.home = Path(a.home)
        self.home.mkdir(parents=True, exist_ok=True)
        self.costs = FEES[a.fees] if a.fees in FEES else Costs()
        if a.maker is not None or a.taker is not None or a.slippage is not None:
            self.costs = Costs(maker_fee=a.maker if a.maker is not None else self.costs.maker_fee,
                               taker_fee=a.taker if a.taker is not None else self.costs.taker_fee,
                               slippage=a.slippage if a.slippage is not None else self.costs.slippage)
        if a.maker is not None or a.taker is not None or a.slippage is not None:
            print(f"note: costs overridden for pricing; the gate still reads the '{a.fees}' backtest records")
        wrong = [x for x in a.symbols if a.fees in FEE_MARKET and market_of(x) != FEE_MARKET[a.fees]]
        if wrong:
            raise SystemExit(f"--fees {a.fees} is a {FEE_MARKET[a.fees]} cost level, but {wrong} are not {FEE_MARKET[a.fees]} "
                             "markets; scan them separately with their own --fees")
        for x in a.symbols:
            point_value(x, 1.0)                                  # refuse crosses up front
        self.spread = FX_SPREAD.get(a.fees, 0.0) if a.fees in FEE_MARKET and FEE_MARKET[a.fees] == "fx" else 0.0
        self.lab = rec.load(a.records) if Path(a.records).exists() else {}
        limits_file = os.environ.get("TI_LIMITS_FILE")
        base = G.Limits(**json.loads(Path(limits_file).read_text(encoding="utf-8"))) if limits_file else G.Limits()
        self.limits, _ = base.tightened({"max_leverage": a.max_leverage} if a.max_leverage is not None else None)
        self.gate = G.PhilosophyGate(self.limits)
        self.journal = Journal(self.home / "journal.csv")
        self.account = PaperAccount(self.home, a.equity)
        self.state_path = self.home / "books.json"
        self.state = json.loads(self.state_path.read_text()) if self.state_path.exists() else {}
        self.frames: dict[tuple[str, str], pd.DataFrame] = {}
        self.seen = {r.get("uid") for r in _csv_rows(self.home / "forward.csv")}

    def save(self) -> None:
        tmp = self.state_path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.state, indent=1, default=str))
        os.replace(tmp, self.state_path)

    def operator_state(self) -> str:
        p = self.home / "state.txt"
        return p.read_text(encoding="utf-8").strip() if p.exists() else self.a.state

    def candles(self, sym: str, tf: str) -> pd.DataFrame:
        vs = _venue_symbol(self.a.venue, sym)
        key = (sym, tf)
        if key not in self.frames:
            self.frames[key] = recent(self.a.venue, vs, tf, HISTORY_DAYS.get(tf, 60))
        else:
            new = latest(self.a.venue, vs, tf, limit=300)
            step = pd.Timedelta(seconds=INTERVAL_SECONDS[tf])
            if len(new) and new.index[0] > self.frames[key].index[-1] + step:      # a hole (sleep, outage): refetch
                new = recent(self.a.venue, vs, tf, HISTORY_DAYS.get(tf, 60))
            df = pd.concat([self.frames[key], new]).sort_index()
            df = df[~df.index.duplicated(keep="last")]
            keep = pd.Timedelta(days=HISTORY_DAYS.get(tf, 60))
            self.frames[key] = df[df.index >= df.index[-1] - keep]
        return self.frames[key]

    def open_risk(self, exclude: str | None = None) -> float:
        """Risk still open in OTHER books (the book being decided is flat by construction)."""
        return sum(float(b["tag"]["risk_pct"]) for k, b in self.state.items()
                   if k != exclude and isinstance(b, dict) and b.get("tag") and b["tag"].get("account")
                   and (b.get("pos") or b.get("pending")))

    def journaled(self, trade_id: str) -> dict | None:
        return next((r for r in self.journal.rows() if r["trade_id"] == trade_id), None)

    def restored_tag(self, row: dict, key: str, pv: float) -> dict:
        take = row["decision"] == "take"
        return {"trade_id": row["trade_id"], "key": key, "account": take, "size": float(row["position_size"] or 0),
                "risk_pct": float(row["risk_pct"] or 0), "point_value": pv}

    def pass_once(self) -> list[str]:
        log = []
        forward = _csv_rows(self.home / "forward.csv")
        for sym in self.a.symbols:
            for tf in self.a.timeframes:
                try:
                    df = self.candles(sym, tf)
                except Exception as e:  # noqa: BLE001 - one market's outage must not stop the others
                    log.append(f"{sym} {tf}: data error {e}")
                    continue
                mk = market_of(sym)
                d = prepare(df, htf=HTF[tf], day="fx" if mk == "fx" else "utc")
                allowed = {S.id for S in setups_for(mk, tf)}
                for setup_id in self.a.setups:
                    if setup_id in allowed:
                        log += self.step(d, sym, tf, setup_id, forward)
                        self.save()                      # after every book: a crash loses at most one step
        return log

    def step(self, d: pd.DataFrame, sym: str, tf: str, setup_id: str, forward: list[dict]) -> list[str]:
        """Process every closed bar not seen yet, in order, with the backtest's rules: manage the book on
        each bar, and when it is flat follow any signal on that bar (shadow). Only a signal on the LATEST
        bar is live: it goes through the gate and the journal, and a take can be handed off."""
        out = []
        skey = f"{setup_id}|{sym}|{tf}"
        st = self.state.get(skey, {})
        mk = market_of(sym)
        book = _load_book(st, self.costs, sym, self.spread if mk == "fx" else 0.0)
        last = pd.Timestamp(st["last_time"]) if st.get("last_time") else None
        idx = d.index
        new_i = [i for i in range(len(d)) if last is None or idx[i] > last]
        if last is None:
            new_i = new_i[-1:]                            # first sight of this market: start from the latest bar
        o, h, l, c = (d[k].to_numpy() for k in ("open", "high", "low", "close"))
        key = f"{setup_id}@{tf}@{self.a.fees}"
        S = SETUPS[setup_id]
        setup = S(tf=tf, htf=HTF[tf], symbol=sym)
        step = pd.Timedelta(seconds=INTERVAL_SECONDS[tf])
        prev = last
        for n, i in enumerate(new_i):
            # a hole in 24/7 crypto data: the bars that would have managed the position are missing, so it is
            # closed at the first bar after the hole (forex closes at weekends; its gaps are real market gaps)
            if mk == "crypto" and prev is not None and idx[i] - prev > step * 1.5 and not book.flat:
                tag = book.tag
                tr = book.force_exit(idx[i], o[i], "data_gap")
                if tr is not None:
                    out.append(self.closed(tr, key, tf, skey, idx[i]))
                elif tag:
                    out.append(self.unfilled(tag, key, sym, idx[i]))
            prev = idx[i]
            tag = book.tag
            closed = book.on_bar(idx[i], o[i], h[i], l[i], c[i])
            for tr in closed:
                out.append(self.closed(tr, key, tf, skey, idx[i] + step))
            if tag and book.tag is None and not closed and book.pos is None:
                out.append(self.unfilled(tag, key, sym, idx[i]))
            if book.flat:
                sig = setup.signal_at(d, i)
                if sig is not None:
                    if n == len(new_i) - 1:
                        out.append(self.decide(sig, book, key, sym, tf, S.derived_from, forward, skey))
                    else:                                  # a missed bar: follow it on paper, never trade it now
                        tid = trade_id_for(key, sym, sig)
                        row = self.journaled(tid)          # unless it was decided live before a crash: restore that
                        tag = (self.restored_tag(row, key, point_value(sym, sig.entry)) if row is not None else
                               {"trade_id": "", "key": key, "account": False, "size": 0, "risk_pct": 0,
                                "point_value": 1.0, "shadow_only": True})
                        book.submit(sig, tag=tag)
        st = _dump_book(book)
        st["last_time"] = idx[new_i[-1]].isoformat() if new_i else (last.isoformat() if last is not None else None)
        self.state[skey] = st
        return [x for x in out if x]

    def decide(self, sig: Signal, book: Book, key: str, sym: str, tf: str, derived_from, forward,
               skey: str | None = None) -> str:
        now = datetime.now(timezone.utc)
        mk = market_of(sym)
        t = proposal(sig, key, sym, tf, self.costs, derived_from, spread=self.spread if mk == "fx" else 0.0)
        pv = point_value(sym, sig.entry)
        prior = self.journaled(t.trade_id)
        if prior is not None:                     # decided before a crash: restore the order, never hand off twice
            book.submit(sig, tag=self.restored_tag(prior, key, pv))
            return f"{sig.time:%Y-%m-%d %H:%M} {key} {sym}: decision already journaled ({prior['decision']}), order restored"
        setup = setup_record(key, self.lab, forward)
        acct = self.account.state(key, sig.session, now, self.open_risk(exclude=skey), self.operator_state(),
                                  self.a.risk_pct, self.a.lot_step, self.a.min_notional, self.a.style, point_value=pv)
        d = self.gate.evaluate(t, setup, acct)
        tid = self.journal.record_decision(d)
        take = d.action == "take"
        book.submit(sig, tag={"trade_id": tid, "key": key, "account": take, "size": d.position_size if take else 0,
                              "risk_pct": d.risk_pct if take else 0, "point_value": pv})
        if take and self.a.on_take:
            self.hand_off(sig, tid, key, sym, tf, d)
        why = next((g.detail for g in d.gates if g.status == "fail"), d.gates[-1].detail if d.gates else "")
        size = f" size {d.position_size:g} risk {d.risk_pct:.2f}%" if take else ""
        return (f"{sig.time:%Y-%m-%d %H:%M} {key} {sym} {sig.side} {sig.order} @ {sig.entry:.6g} stop {sig.stop:.6g} "
                f"target {sig.target:.6g} [{sig.regime}/{sig.session}] -> {d.action.upper()}{size}: {why}")

    def hand_off(self, sig: Signal, tid: str, key: str, sym: str, tf: str, d: G.Decision) -> None:
        """Pass a gated TAKE to the owner's own execution code (`--on-take "command"`): the trade as JSON
        on stdin. Called only after the journal row is written (Section XVI). A failure is journaled."""
        import shlex
        import subprocess
        payload = {"trade_id": tid, "setup": key, "symbol": sym, "timeframe": tf, "side": sig.side, "order": sig.order,
                   "entry": sig.entry, "stop": sig.stop, "target": sig.target, "size": d.position_size,
                   "risk_pct": d.risk_pct, "expiry_bars": sig.expiry_bars, "max_hold_bars": sig.max_hold_bars,
                   "est_ev_r": d.est_ev_r, "decided_at": d.journal_row.get("decided_at"), "paper": False}
        try:
            r = subprocess.run(shlex.split(self.a.on_take), input=json.dumps(payload), text=True, capture_output=True,
                               timeout=60)
            if r.returncode != 0:
                raise RuntimeError(f"exit {r.returncode}: {r.stderr.strip()[:300]}")
        except Exception as e:  # noqa: BLE001 - never crash the scan; record it
            self.journal.record_outcome(tid, lesson=f"on-take hand-off failed: {e}")

    def unfilled(self, tag: dict, key: str, sym: str, t) -> str:
        """The order expired, price left without it, or a market order's open gapped past the stop."""
        if tag.get("account"):
            self.journal.record_outcome(tag["trade_id"], executed_per_plan="no: order not filled (expired, or price "
                                        "left first)", exit_reason="not_filled", result_r=0, cost_r=0)
            return f"{pd.Timestamp(t):%Y-%m-%d %H:%M} {key} {sym}: gated order not filled, cancelled"
        return ""

    def closed(self, tr: dict, key: str, tf: str, skey: str, closed_at) -> str:
        tag = tr.pop("tag", None) or {}
        uid = f"{skey}|{pd.Timestamp(tr['signal_time']).isoformat()}"
        row = {**tr, "uid": uid, "key": key, "trade_id": tag.get("trade_id", ""), "account": bool(tag.get("account")),
               "timeframe": tf}
        for k in ("signal_time", "entry_time", "exit_time"):
            row[k] = pd.Timestamp(row[k]).isoformat()
        if uid not in self.seen:                  # a restart after a crash must not count a trade twice
            _append(self.home / "forward.csv", FORWARD_COLS, row)
            self.seen.add(uid)
        msg = f"{pd.Timestamp(tr['exit_time']):%Y-%m-%d %H:%M} closed {key} {tr['symbol']} {tr['exit_reason']} {tr['net_r']:+.2f}R"
        if tag.get("account"):
            acc = self.account.book_trade(tr, tag, closed_at)
            self.journal.record_outcome(tag["trade_id"], executed_per_plan="yes (paper)", exit_reason=tr["exit_reason"],
                                        result_r=round(tr["net_r"], 4), cost_r=round(tr["cost_r"], 4),
                                        mae_r=round(tr["mae_r"], 4), mfe_r=round(tr["mfe_r"], 4),
                                        outcome_within_expected="yes" if tr["exit_reason"] in ("stop", "target") else
                                        "data gap: closed at the first bar after missing data" if tr["exit_reason"] == "data_gap"
                                        else "time exit")
            msg += (" (already booked)" if acc is None else f" | account pnl {acc['pnl']:+.4f} equity {acc['equity']:.4f}")
        return msg


def report(home: Path, equity0: float) -> str:
    fwd = _csv_rows(home / "forward.csv")
    acc = _csv_rows(home / "account.csv")
    lines = [f"Sniper paper scanner - {home}", ""]
    if not fwd:
        lines.append("No closed shadow trades yet.")
    else:
        df = pd.DataFrame(fwd)
        df["net_r"] = df["net_r"].astype(float)
        g = df.groupby("key")["net_r"].agg(["count", "mean", lambda s: (s > 0).mean(), "sum"])
        g.columns = ["n", "mean_net_r", "win_rate", "sum_r"]
        lines += ["Shadow (every signal, forward):", g.round(3).to_string(), ""]
    if acc:
        eq = float(acc[-1]["equity"])
        lines.append(f"Account: {len(acc)} trades, equity {equity0:g} -> {eq:.4f} ({(eq / equity0 - 1) * 100:+.2f}%)")
    else:
        lines.append("Account: no gated trades taken yet (the gate takes only setups whose record clears Gates 4-6).")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="sniper scan")
    ap.add_argument("--venue", default="binance", help="candle source: binance (public data API), coinbase, kraken, okx, "
                                                       "kucoin; yahoo for forex and gold (EURUSD, XAUUSD ...)")
    ap.add_argument("--symbols", nargs="+", default=["BTCUSDT", "ETHUSDT", "SOLUSDT"])
    ap.add_argument("--timeframes", nargs="+", default=["15m", "1h"])
    ap.add_argument("--setups", nargs="+", default=sorted(SETUPS))
    ap.add_argument("--fees", default="std", help="cost level whose backtest records the gate reads: std / low (crypto), "
                                                   "fx_std / fx_raw (forex and gold)")
    ap.add_argument("--maker", type=float, default=None, help="override maker fee (fraction, e.g. 0.0002)")
    ap.add_argument("--taker", type=float, default=None)
    ap.add_argument("--slippage", type=float, default=None)
    ap.add_argument("--equity", type=float, default=20.0, help="paper starting equity, any amount")
    ap.add_argument("--risk-pct", type=float, default=0.5, help="base risk per trade, percent of equity")
    ap.add_argument("--lot-step", type=float, default=0.00001, help="the venue's quantity step for these markets")
    ap.add_argument("--min-notional", type=float, default=5.0, help="the venue's smallest order value")
    ap.add_argument("--max-leverage", type=float, default=1.0, help="1 = spot (no leverage)")
    ap.add_argument("--style", default="intraday", choices=["intraday", "swing"])
    ap.add_argument("--state", default="calm", help="operator state for Gate 0 if state.txt is absent")
    ap.add_argument("--records", default=str(LAB_OUT / "records.json"))
    ap.add_argument("--home", default=None, help=f"state folder (default {HOME}/<fees>, one per cost level, so a "
                                                 "crypto and a forex scanner never share books)")
    ap.add_argument("--on-take", default=None, help="command that receives each gated TAKE as JSON on stdin "
                                                     "(your bot's own order code); never called for skips or waits")
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args(argv)
    a.home = a.home or str(HOME / a.fees)
    if a.report:
        print(report(Path(a.home), a.equity))
        return 0
    unknown = [s for s in a.setups if s not in SETUPS]
    if unknown:
        ap.error(f"unknown setups {unknown}; choose from {sorted(SETUPS)}")
    sc = Scanner(a)
    if not sc.lab:
        print(f"warning: no backtest records at {a.records}; the gate will skip every signal (run `sniper lab` first)")
    step = min(INTERVAL_SECONDS[tf] for tf in a.timeframes)
    while True:
        for line in sc.pass_once():
            print(line, flush=True)
        if a.once:
            return 0
        now = time.time()
        time.sleep(step - now % step + 5)                   # just after the next bar closes


if __name__ == "__main__":
    raise SystemExit(main())
