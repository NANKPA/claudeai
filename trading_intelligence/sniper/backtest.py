"""Conservative bar-by-bar backtester for sniper setups.

Rules (each chosen to understate results rather than flatter them):
- The decision is taken at the CLOSE of bar i using rows <= i. A market entry fills at the OPEN of
  bar i+1 (plus slippage); if that open is already past the stop or the target, there is no trade.
- A limit entry rests from bar i+1. It fills only when the bar trades THROUGH the limit (a touch is
  not enough), at the limit, or at the open if the bar opens through it. It is cancelled when it
  expires, or when price reaches the target before filling (the move left without us).
- On the fill bar the stop is checked first. If the stop is not hit and the bar CLOSES beyond the
  target, price crossed the target after the fill and the trade exits AT the target. An entry that
  fills beyond the stop (a gap) exits at once at the fill price.
- On later bars, if the stop and the target are both inside one bar, the STOP is assumed first; a bar
  that opens beyond the stop exits at that open.
- Prices from BID candles (forex): buy-side triggers (a long's limit entry, a short's stop and target)
  need the ask, so they trigger only `trigger_spread` (a fraction of price) further.
- Stop and time exits pay taker fees plus slippage; resting entries and target exits pay maker fees.
- One position or pending order per setup per market at a time.
Each trade is returned in R of the PLANNED risk (signal entry to stop), the risk the gate sizes on,
with its costs, regime and session tags.
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from .setups import Setup, Signal, prepare


@dataclass(frozen=True)
class Costs:
    maker_fee: float = 0.0008      # fraction of notional per side
    taker_fee: float = 0.0010
    slippage: float = 0.0002       # fraction of price lost on taker fills (market entries, stops, time exits)


class Book:
    """Orders and the position for ONE setup on ONE market, bar by bar. The backtester and the live paper
    broker both use it, so paper fills follow exactly the backtest's rules.

    Call `on_bar()` with each CLOSED bar in order; it returns the trades that closed on that bar. When the
    book is `flat`, a Signal generated at the close of the bar just processed may be `submit()`ted: a
    market order fills at the next bar's open, a limit rests from the next bar."""

    def __init__(self, costs: Costs = Costs(), symbol: str = "", trigger_spread: float = 0.0):
        self.costs, self.symbol, self.trigger_spread = costs, symbol, trigger_spread
        self.k = -1                    # index of the last bar processed
        self.pending = None            # {"sig", "last_k"}
        self.pos = None
        self.tag = None                # free-form data carried from submit() to the closed trade (paper account)

    @property
    def flat(self) -> bool:
        return self.pending is None and self.pos is None

    def submit(self, sig: Signal, tag: dict | None = None) -> None:
        if not self.flat:
            raise RuntimeError("book already has an order or a position")
        last = self.k + 1 if sig.order == "market" else self.k + max(sig.expiry_bars, 1)
        self.pending, self.tag = {"sig": sig, "last_k": last}, tag

    def cancel(self) -> None:
        if self.pending is not None:
            self.pending, self.tag = None, None

    def _levels(self, s: Signal) -> tuple[int, float, float]:
        """side, and the stop and target levels as the BID must print them (buy-side orders need the ask)."""
        side = 1 if s.side == "long" else -1
        sp = self.trigger_spread
        if side == 1:
            return side, s.stop, s.target
        return side, s.stop * (1 - sp), s.target * (1 - sp)

    def on_bar(self, t, o: float, h: float, l: float, c: float) -> list[dict]:
        self.k += 1
        k, out = self.k, []
        if self.pos is None and self.pending is not None and self.pending["sig"].order == "market":
            s = self.pending["sig"]
            self.pending = None
            side = 1 if s.side == "long" else -1
            if (o - s.stop) * side > 0 and (s.target - o) * side > 0:      # gapped past stop or target: no trade
                self.pos = {"sig": s, "fill_k": k, "entry_time": t, "entry": o, "maker": False, "mae": 0.0, "mfe": 0.0}
            else:
                self.tag = None
        # ── manage the open position on this bar (including the bar it filled on) ──
        if self.pos is not None:
            pos = self.pos
            s = pos["sig"]
            side, stop, target = self._levels(s)
            fill_bar = k == pos["fill_k"]
            exit_px = reason = None
            hit_stop = (l <= stop) if side == 1 else (h >= stop)
            if hit_stop:
                gap = (o < stop) if side == 1 else (o > stop)
                exit_px, reason = (o if gap and not fill_bar else s.stop), "stop"
            elif fill_bar:
                if (c - target) * side >= 0:                       # closed beyond the target after the fill
                    exit_px, reason = s.target, "target"
            else:
                hit_tgt = (h >= target) if side == 1 else (l <= target)
                if hit_tgt:
                    gap = (o > target) if side == 1 else (o < target)
                    exit_px, reason = (o if gap else s.target), "target"
            pos["mae"] = min(pos["mae"], ((l if side == 1 else h) - pos["entry"]) * side)
            pos["mfe"] = max(pos["mfe"], ((h if side == 1 else l) - pos["entry"]) * side)
            if exit_px is None and k - pos["fill_k"] >= s.max_hold_bars:
                exit_px, reason = c, "time"
            if exit_px is not None:
                out.append(self._finish(t, exit_px, reason))
        # ── work the resting limit order on this bar ────────────────────────
        elif self.pending is not None:
            s, last = self.pending["sig"], self.pending["last_k"]
            side, stop, target = self._levels(s)
            trig = s.entry * (1 - self.trigger_spread) if side == 1 else s.entry
            through = (l < trig) if side == 1 else (h > trig)
            if through:
                fill = min(o, s.entry) if side == 1 else max(o, s.entry)
                self.pos = {"sig": s, "fill_k": k, "entry_time": t, "entry": fill, "maker": True,
                            "mae": min(0.0, ((l if side == 1 else h) - fill) * side), "mfe": max(0.0, (c - fill) * side)}
                self.pending = None
                hit_stop = (l <= stop) if side == 1 else (h >= stop)
                beyond = (fill - s.stop) * side <= 0                 # filled at or past the stop (a gap)
                if beyond:
                    out.append(self._finish(t, fill, "stop"))
                elif hit_stop:                                       # filled and stopped in the same bar
                    out.append(self._finish(t, s.stop, "stop"))
                elif (c - target) * side >= 0:                       # filled, then closed beyond the target
                    out.append(self._finish(t, s.target, "target"))
            else:
                ran = (h >= target) if side == 1 else (l <= target)
                if ran or k >= last:
                    self.pending, self.tag = None, None
        return out

    def _finish(self, t, exit_px: float, reason: str) -> dict:
        tr = _close(self.pos, self.k, t, exit_px, reason, self.costs, self.symbol)
        if self.tag is not None:
            tr["tag"] = self.tag
        self.pos, self.tag = None, None
        return tr


TRADE_COLUMNS = ["setup", "symbol", "side", "order", "signal_time", "entry_time", "exit_time", "plan_entry", "entry", "stop",
                 "target", "exit", "exit_reason", "stop_pct", "gross_r", "cost_r", "net_r", "mae_r", "mfe_r", "bars_held",
                 "regime", "session"]


def run(df: pd.DataFrame, setup: Setup, costs: Costs = Costs(), symbol: str = "", prepared: bool = False,
        warmup: int = 300, trigger_spread: float = 0.0) -> pd.DataFrame:
    d = df if prepared else prepare(df)
    o, h, l, c = (d[k].to_numpy() for k in ("open", "high", "low", "close"))
    idx = d.index
    n = len(d)
    book = Book(costs, symbol, trigger_spread)
    book.k = warmup - 1
    trades = []
    for i in range(warmup, n):
        trades += book.on_bar(idx[i], o[i], h[i], l[i], c[i])
        if book.flat and i < n - 1:
            sig = setup.signal_at(d, i)
            if sig is not None:
                book.submit(sig)
    return pd.DataFrame(trades, columns=TRADE_COLUMNS)


def _close(pos, k, t, exit_px, reason, costs: Costs, symbol) -> dict:
    s = pos["sig"]
    side = 1 if s.side == "long" else -1
    entry = pos["entry"]
    risk = abs(s.entry - s.stop)                     # the planned risk: what the gate sized the position on
    entry_fee = costs.maker_fee if pos["maker"] else costs.taker_fee + costs.slippage
    exit_fee = costs.maker_fee if reason == "target" else costs.taker_fee + costs.slippage
    cost = entry * entry_fee + exit_px * exit_fee
    gross = (exit_px - entry) * side / risk
    return {"setup": s.setup_id, "symbol": symbol, "side": s.side, "order": s.order, "signal_time": s.time,
            "entry_time": pos["entry_time"], "exit_time": t, "plan_entry": s.entry, "entry": entry, "stop": s.stop,
            "target": s.target, "exit": exit_px, "exit_reason": reason, "stop_pct": risk / s.entry, "gross_r": gross,
            "cost_r": cost / risk, "net_r": gross - cost / risk, "mae_r": pos["mae"] / risk, "mfe_r": pos["mfe"] / risk,
            "bars_held": k - pos["fill_k"], "regime": s.regime, "session": s.session}


def summarize(trades: pd.DataFrame) -> dict:
    if trades.empty:
        return {"n": 0}
    r = trades["net_r"].to_numpy()
    n = len(r)
    sd = float(r.std(ddof=1)) if n > 1 else float("nan")
    days = max((trades["exit_time"].max() - trades["entry_time"].min()).days, 1)
    return {"n": n, "trades_per_day": n / days, "win_rate": float((r > 0).mean()), "mean_net_r": float(r.mean()),
            "se": sd / np.sqrt(n) if n > 1 else float("nan"), "mean_gross_r": float(trades["gross_r"].mean()),
            "mean_cost_r": float(trades["cost_r"].mean()), "median_stop_pct": float(trades["stop_pct"].median()),
            "sum_net_r": float(r.sum())}
