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
- Prices from BID candles (forex): every buy pays the ask = bid x (1 + `trigger_spread`), every sell gets
  the bid. A long enters on the ask and exits on the bid; a short enters on the bid and exits on the ask.
  So the spread is paid inside the prices, once per round trip, and is NOT also charged as a fee.
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

    def _bars(self, side: int, o: float, h: float, l: float, c: float):
        """The bar as the ENTRY sees it and as the EXIT sees it. Candles are bid (forex) or last-trade
        (crypto, spread 0). A buy pays the ask = bid x (1 + spread), a sell gets the bid: a long enters
        on the ask and exits on the bid; a short enters on the bid and exits on the ask."""
        a = 1 + self.trigger_spread
        ask, bid = (o * a, h * a, l * a, c * a), (o, h, l, c)
        return (ask, bid) if side == 1 else (bid, ask)

    def on_bar(self, t, o: float, h: float, l: float, c: float) -> list[dict]:
        self.k += 1
        k, out = self.k, []
        a = 1 + self.trigger_spread
        if self.pos is None and self.pending is not None and self.pending["sig"].order == "market":
            s = self.pending["sig"]
            self.pending = None
            side = 1 if s.side == "long" else -1
            (eo, _, _, _), (xo, _, _, _) = self._bars(side, o, h, l, c)
            if (xo - s.stop) * side > 0 and (s.target - xo) * side > 0:    # gapped past stop or target: no trade
                self.pos = {"sig": s, "fill_k": k, "entry_time": t, "entry": eo, "maker": False, "mae": 0.0, "mfe": 0.0}
            else:
                self.tag = None
        # ── manage the open position on this bar (including the bar it filled on) ──
        if self.pos is not None:
            pos = self.pos
            s = pos["sig"]
            side = 1 if s.side == "long" else -1
            _, (xo, xh, xl, xc) = self._bars(side, o, h, l, c)
            fill_bar = k == pos["fill_k"]
            exit_px = reason = None
            hit_stop = (xl <= s.stop) if side == 1 else (xh >= s.stop)
            if hit_stop:
                gap = (xo < s.stop) if side == 1 else (xo > s.stop)
                exit_px, reason = (xo if gap and not fill_bar else s.stop), "stop"
            elif fill_bar:
                if (xc - s.target) * side >= 0:                    # closed beyond the target after the fill
                    exit_px, reason = s.target, "target"
            else:
                hit_tgt = (xh >= s.target) if side == 1 else (xl <= s.target)
                if hit_tgt:
                    gap = (xo > s.target) if side == 1 else (xo < s.target)
                    exit_px, reason = (xo if gap else s.target), "target"
            pos["mae"] = min(pos["mae"], ((xl if side == 1 else xh) - pos["entry"]) * side)
            pos["mfe"] = max(pos["mfe"], ((xh if side == 1 else xl) - pos["entry"]) * side)
            if exit_px is None and k - pos["fill_k"] >= s.max_hold_bars:
                exit_px, reason = xc, "time"
            if exit_px is not None:
                out.append(self._finish(t, exit_px, reason))
        # ── work the resting limit order on this bar ────────────────────────
        elif self.pending is not None:
            s, last = self.pending["sig"], self.pending["last_k"]
            side = 1 if s.side == "long" else -1
            (eo, eh, el, ec), (xo, xh, xl, xc) = self._bars(side, o, h, l, c)
            through = (el < s.entry) if side == 1 else (eh > s.entry)
            if through:
                fill = min(eo, s.entry) if side == 1 else max(eo, s.entry)
                now = fill / a if side == 1 else fill * a          # what an immediate exit would get at the fill
                self.pos = {"sig": s, "fill_k": k, "entry_time": t, "entry": fill, "maker": True,
                            "mae": min(0.0, ((xl if side == 1 else xh) - fill) * side), "mfe": max(0.0, (xc - fill) * side)}
                self.pending = None
                hit_stop = (xl <= s.stop) if side == 1 else (xh >= s.stop)
                if (now - s.stop) * side <= 0:                     # filled at or past the stop (a gap): out at once
                    out.append(self._finish(t, now, "stop"))
                elif hit_stop:                                     # filled and stopped in the same bar
                    out.append(self._finish(t, s.stop, "stop"))
                elif (xc - s.target) * side >= 0:                  # filled, then closed beyond the target
                    out.append(self._finish(t, s.target, "target"))
            else:
                ran = (xh >= s.target) if side == 1 else (xl <= s.target)
                if ran or k >= last:
                    self.pending, self.tag = None, None
        return out

    def force_exit(self, t, price: float, reason: str) -> dict | None:
        """Close an open position at `price` (a hole in the data: the bars that would have managed it are
        missing). A pending order is simply dropped. Returns the closed trade, if there was one."""
        if self.pos is not None:
            return self._finish(t, price, reason)
        self.pending, self.tag = None, None
        return None

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
