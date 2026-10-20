"""Sniper setups: mechanical, causal versions of the precise entries taught in the knowledge base's
playbooks (liquidity sweeps, fair value gaps, OTE retracements, opening-range retests, trend
pullbacks, VWAP reversion).

Causality contract: `signal_at(df, i)` may read rows 0..i only, and every indicator column is built so
that row i depends on bars <= i (higher-timeframe values are shifted to become available only after
their own bar has CLOSED). The decision is taken at the close of bar i; a market entry fills at the
open of bar i+1; a limit entry rests from bar i+1 until it fills, expires, or its stop trades first.

Every signal carries the text Gates 1-2 of the owner's protocol ask for (observation, interpretation,
alternative, hypothesis, horizon, invalidation, explanation, what undermines it), so it can go
straight into PhilosophyGate.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

from .feeds import INTERVAL_SECONDS, resample


@dataclass
class Signal:
    setup_id: str
    i: int
    time: pd.Timestamp
    side: str                  # "long" / "short"
    entry: float
    stop: float
    target: float
    order: str                 # "limit" or "market"
    expiry_bars: int
    max_hold_bars: int
    regime: str
    session: str
    text: dict = field(default_factory=dict)
    conditions: dict = field(default_factory=dict)


# ── indicators (all causal) ─────────────────────────────────────────────────
NY = "America/New_York"


def _by_day(values: pd.Series, key: np.ndarray, how: str) -> pd.Series:
    return values.groupby(key).agg(how)


def prepare(df: pd.DataFrame, htf: str = "1h", vol_window_days: int = 30, day: str = "utc") -> pd.DataFrame:
    """Indicator columns; row i depends only on bars <= i.

    day="utc" (crypto: the 00:00 UTC daily candle) or "fx" (the forex day that starts at 17:00 New York).
    """
    d = df.copy()
    step = (d.index[1] - d.index[0]) if len(d) > 1 else pd.Timedelta("5min")
    step = min(step, pd.Series(d.index).diff().dropna().mode().iloc[0]) if len(d) > 2 else step
    prev_close = d["close"].shift(1)
    tr = pd.concat([d["high"] - d["low"], (d["high"] - prev_close).abs(), (d["low"] - prev_close).abs()], axis=1).max(axis=1)
    d["atr"] = tr.rolling(14, min_periods=14).mean()
    d["ema20"] = d["close"].ewm(span=20, adjust=False).mean()
    d["ema50"] = d["close"].ewm(span=50, adjust=False).mean()
    # higher timeframe: value of an HTF bar becomes usable only once that bar has closed
    h = resample(df, htf)
    hc = h["close"]
    hv = pd.DataFrame({"htf_ema20": hc.ewm(span=20, adjust=False).mean(), "htf_ema50": hc.ewm(span=50, adjust=False).mean(),
                       "htf_close": hc})
    hv.index = hv.index + pd.Timedelta(htf)                       # available from the HTF bar's close
    # last confirmed HTF pivots (fractal k = 3): a pivot at HTF bar j is known at the close of bar j + 3
    left_h, left_l = h["high"].shift(1).rolling(3).max(), h["low"].shift(1).rolling(3).min()
    right_h = h["high"][::-1].shift(1).rolling(3).max()[::-1]
    right_l = h["low"][::-1].shift(1).rolling(3).min()[::-1]
    piv = pd.DataFrame({"htf_pivot_high": h["high"].where((h["high"] > left_h) & (h["high"] >= right_h)),
                        "htf_pivot_low": h["low"].where((h["low"] < left_l) & (h["low"] <= right_l))})
    # known at the CLOSE of the third HTF bar after the pivot (the actual bar: weekends and outages skip bins)
    piv.index = (pd.Series(h.index, index=h.index).shift(-3) + pd.Timedelta(htf)).to_numpy()
    piv = piv[piv.index.notna()].dropna(how="all").groupby(level=0).last().ffill()
    d = d.join(hv.reindex(d.index, method="ffill"))
    d = d.join(piv.reindex(d.index, method="ffill"))
    # the trading day, New York clock
    ny = d.index.tz_convert(NY)
    d["ny_min"] = ny.hour * 60 + ny.minute                      # bar OPEN time, minutes after New York midnight
    nydate = ny.normalize().tz_localize(None)
    if day == "fx":
        dkey = (ny + pd.Timedelta(hours=7)).normalize().tz_localize(None)
    else:
        dkey = d.index.normalize().tz_localize(None)
    dkey = np.asarray(dkey)
    # prior day high / low / midpoint and the 10-day average daily range (known from the day's start)
    hi, lo = _by_day(d["high"], dkey, "max"), _by_day(d["low"], dkey, "min")
    d["pdh"] = hi.shift(1).reindex(dkey).to_numpy()
    d["pdl"] = lo.shift(1).reindex(dkey).to_numpy()
    d["pdm"] = (d["pdh"] + d["pdl"]) / 2
    d["adr10"] = (hi - lo).shift(1).rolling(10, min_periods=10).mean().reindex(dkey).to_numpy()
    # session VWAP for the trading day and the dispersion around it, cumulative up to each bar
    tp = (d["high"] + d["low"] + d["close"]) / 3
    vol = d["volume"].where(d["volume"] > 0, 1e-12)
    cpv = (tp * vol).groupby(dkey).cumsum()
    cv = vol.groupby(dkey).cumsum()
    d["vwap"] = cpv / cv
    dev2 = ((tp - d["vwap"]) ** 2 * vol).groupby(dkey).cumsum() / cv
    d["vwap_sd"] = np.sqrt(dev2)
    # Asia range: bars opening 20:00-24:00 New York, usable on the next New York date before 20:00
    in_asia = ny.hour >= 20
    akey = np.asarray(nydate + pd.Timedelta(days=1))
    ahi = d["high"][in_asia].groupby(akey[in_asia]).max()
    alo = d["low"][in_asia].groupby(akey[in_asia]).min()
    use = ~in_asia
    nd = np.asarray(nydate)
    d["asia_hi"] = np.where(use, ahi.reindex(nd).to_numpy(), np.nan)
    d["asia_lo"] = np.where(use, alo.reindex(nd).to_numpy(), np.nan)
    # New York opening range 09:30-10:00 (needs bars of 30 minutes or less), usable from 10:00
    in_or = (d["ny_min"] >= 570) & (d["ny_min"] < 600)
    if step <= pd.Timedelta("30min"):
        orh = d["high"][in_or].groupby(nd[in_or]).max()
        orl = d["low"][in_or].groupby(nd[in_or]).min()
        after = d["ny_min"] >= 600
        d["or_hi"] = np.where(after, orh.reindex(nd).to_numpy(), np.nan)
        d["or_lo"] = np.where(after, orl.reindex(nd).to_numpy(), np.nan)
        above = (after & (d["close"] > d["or_hi"])).astype(int)
        below = (after & (d["close"] < d["or_lo"])).astype(int)
        d["or_closed_above_before"] = above.groupby(nd).cumsum().groupby(nd).shift(1).fillna(0).to_numpy() > 0
        d["or_closed_below_before"] = below.groupby(nd).cumsum().groupby(nd).shift(1).fillna(0).to_numpy() > 0
    else:
        d["or_hi"] = d["or_lo"] = np.nan
        d["or_closed_above_before"] = d["or_closed_below_before"] = False
    # last confirmed pivots on the entry timeframe (k = 3): a pivot at bar j is known at the close of bar j + 3
    lh, ll = d["high"].shift(1).rolling(3).max(), d["low"].shift(1).rolling(3).min()
    rh = d["high"][::-1].shift(1).rolling(3).max()[::-1]
    rl = d["low"][::-1].shift(1).rolling(3).min()[::-1]
    d["piv_hi"] = d["high"].where((d["high"] > lh) & (d["high"] >= rh)).shift(3).ffill()
    d["piv_lo"] = d["low"].where((d["low"] < ll) & (d["low"] <= rl)).shift(3).ffill()
    # Donchian channel of the previous 20 bars; first UTC half-hour return (intraday momentum)
    d["dc20_hi"] = d["high"].shift(1).rolling(20, min_periods=20).max()
    d["dc20_lo"] = d["low"].shift(1).rolling(20, min_periods=20).min()
    umin = d.index.hour * 60 + d.index.minute
    udate = np.asarray(d.index.normalize().tz_localize(None))
    first = umin < 30
    if step <= pd.Timedelta("30min") and first.any():
        o1 = d["open"][first].groupby(udate[first]).first()
        c1 = d["close"][first].groupby(udate[first]).last()
        r1 = (c1 / o1 - 1).reindex(udate).to_numpy()
        d["first_half_hour_r"] = np.where(umin + step.total_seconds() / 60 >= 30, r1, np.nan)
    else:
        d["first_half_hour_r"] = np.nan
    # regime: HTF trend x volatility (ATR% above / below its trailing median)
    bars_per_day = max(int(round(pd.Timedelta("1D") / step)), 1)
    atr_pct = d["atr"] / d["close"]
    med = atr_pct.rolling(bars_per_day * vol_window_days, min_periods=bars_per_day * 5).median()
    up = (d["htf_ema20"] > d["htf_ema50"]) & (d["close"] > d["htf_ema50"])
    down = (d["htf_ema20"] < d["htf_ema50"]) & (d["close"] < d["htf_ema50"])
    d["htf_dir"] = np.where(up, 1, np.where(down, -1, 0))
    vol_tag = np.where(atr_pct > med, "high_vol", "low_vol")
    d["regime"] = np.where(d["htf_dir"] != 0, "trend_", "range_") + vol_tag
    d.loc[med.isna() | d["htf_ema50"].isna(), "regime"] = "unclear"
    hour = (d.index + step).hour
    d["session"] = np.select([hour < 7, hour < 13, hour < 21], ["asia", "london", "ny"], "late")
    d.attrs["step"] = step
    return d


def _texts(**kw) -> dict:
    keys = ("observation", "interpretation", "alternative_interpretation", "hypothesis", "horizon", "invalidation",
            "explanation", "undermined_by")
    return {k: kw[k] for k in keys}


class Setup:
    id = "base"
    name = ""
    derived_from: tuple[str, ...] = ()
    params: dict = {}
    symbol_params: dict = {}                   # per-market parameter overrides, e.g. a round-number grid
    max_tf: str | None = None                  # the coarsest timeframe the rules make sense on
    markets: tuple[str, ...] = ("crypto", "fx")

    def __init__(self, tf: str = "5m", htf: str = "1h", symbol: str = "", **overrides):
        self.tf, self.htf, self.symbol = tf, htf, symbol    # tf/htf label the level of the hypothesis (Gate 2)
        self.p = {**self.params, **self.symbol_params.get(symbol, {}), **overrides}
        self.step_min = INTERVAL_SECONDS.get(tf, 300) // 60

    def signal_at(self, d: pd.DataFrame, i: int) -> Signal | None:   # pragma: no cover - interface
        raise NotImplementedError

    def _sig(self, d, i, side, entry, stop, target, order, expiry, hold, text, conditions) -> Signal | None:
        if not (np.isfinite([entry, stop, target]).all()):
            return None
        if side == "long" and not (stop < entry < target):
            return None
        if side == "short" and not (target < entry < stop):
            return None
        return Signal(self.id, i, d.index[i], side, float(entry), float(stop), float(target), order, expiry, hold,
                      str(d["regime"].iat[i]), str(d["session"].iat[i]), text, conditions)


class SweepReclaim(Setup):
    """Prior-day low (high) swept by at least `min_sweep_atr` x ATR, and the bar closes back inside:
    stops below an obvious level were run and absorbed. Enter at market on the next open, stop beyond
    the sweep extreme, target `rr` R."""
    id = "sniper_sweep_reclaim"
    name = "Prior-day liquidity sweep + reclaim"
    derived_from = ("strategy_candace_lau_nq_sweep_reversal", "strategy_marco_trades_liquidity_grab",
                    "strategy_dhesi_liquidity_inversion", "concept_liquidity_sweep_reversal", "concept_liquidity")
    params = {"min_sweep_atr": 0.1, "stop_buffer_atr": 0.1, "rr": 2.0, "hold": 48}

    def signal_at(self, d, i):
        p = self.p
        atr, low, high, close = d["atr"].iat[i], d["low"].iat[i], d["high"].iat[i], d["close"].iat[i]
        pdl, pdh = d["pdl"].iat[i], d["pdh"].iat[i]
        if not np.isfinite([atr, pdl, pdh]).all():
            return None
        if low < pdl - p["min_sweep_atr"] * atr and close > pdl:
            stop = low - p["stop_buffer_atr"] * atr
            r = close - stop
            t = _texts(observation=f"Price traded below the prior-day low {pdl:.6g} (to {low:.6g}) and closed back above it at {close:.6g}.",
                       interpretation="Sell stops resting under the prior-day low were triggered and absorbed by buyers.",
                       alternative_interpretation="A stop run that is the first leg of a breakdown below the prior day.",
                       hypothesis=f"{self.tf}: price travels {p['rr']:g}R above entry before trading below the sweep low.",
                       horizon=f"within {p['hold']} bars", invalidation=f"price trades below the sweep low {low:.6g}",
                       explanation="An obvious low collects stops; when they are absorbed and price closes back inside, the "
                                   "sellers who drove the sweep are trapped.",
                       undermined_by="A trend day down where the reclaim fails and the prior-day low becomes resistance.")
            return self._sig(d, i, "long", close, stop, close + p["rr"] * r, "market", 0, p["hold"], t,
                             {"sweep": True, "reclaim": True})
        if high > pdh + p["min_sweep_atr"] * atr and close < pdh:
            stop = high + p["stop_buffer_atr"] * atr
            r = stop - close
            t = _texts(observation=f"Price traded above the prior-day high {pdh:.6g} (to {high:.6g}) and closed back below it at {close:.6g}.",
                       interpretation="Buy stops above the prior-day high were triggered and absorbed by sellers.",
                       alternative_interpretation="A stop run that is the first leg of a breakout above the prior day.",
                       hypothesis=f"{self.tf}: price travels {p['rr']:g}R below entry before trading above the sweep high.",
                       horizon=f"within {p['hold']} bars", invalidation=f"price trades above the sweep high {high:.6g}",
                       explanation="An obvious high collects stops; when they are absorbed and price closes back inside, the "
                                   "buyers who drove the sweep are trapped.",
                       undermined_by="A trend day up where the reclaim fails and the prior-day high becomes support.")
            return self._sig(d, i, "short", close, stop, close - p["rr"] * r, "market", 0, p["hold"], t,
                             {"sweep": True, "reclaim": True})
        return None


class FVGRetrace(Setup):
    """A displacement candle (body >= `disp_atr` x ATR) in the direction of the HTF trend leaves a
    three-candle fair value gap; rest a LIMIT at the gap's midpoint; stop beyond the displacement
    candle; target `rr` R."""
    id = "sniper_fvg_retrace"
    name = "Fair value gap retrace in the HTF trend"
    derived_from = ("strategy_trader_mayne_structure_ote", "strategy_abraham_perez_ict_orderflow",
                    "strategy_nbb_trader_po3_ote_adr", "concept_fair_value_gap", "concept_smart_money_concepts")
    params = {"disp_atr": 1.5, "stop_buffer_atr": 0.1, "rr": 2.0, "expiry": 12, "hold": 48}

    def signal_at(self, d, i):
        if i < 3:
            return None
        p = self.p
        atr, dirn = d["atr"].iat[i], d["htf_dir"].iat[i]
        o1, c1 = d["open"].iat[i - 1], d["close"].iat[i - 1]
        if not np.isfinite(atr) or abs(c1 - o1) < p["disp_atr"] * atr:
            return None
        if dirn == 1 and c1 > o1 and d["low"].iat[i] > d["high"].iat[i - 2]:
            top, bot = d["low"].iat[i], d["high"].iat[i - 2]
            entry = (top + bot) / 2
            stop = d["low"].iat[i - 1] - p["stop_buffer_atr"] * atr
            t = _texts(observation=f"A bullish displacement candle left a gap between {bot:.6g} and {top:.6g} in a {self.htf} uptrend.",
                       interpretation="Aggressive buyers moved price faster than sellers could fill; the gap is unfinished business.",
                       alternative_interpretation="An exhaustion spike that fully retraces the displacement.",
                       hypothesis=f"{self.tf}: a retrace into the gap holds and price travels {p['rr']:g}R above the entry.",
                       horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                       invalidation=f"price trades below the displacement low {stop:.6g}",
                       explanation="Displacement shows initiative; the first return to the imbalance is where late buyers "
                                   "and the initiators defend their average price.",
                       undermined_by=f"The {self.htf} trend turning, or the gap being run through on the first touch.")
            return self._sig(d, i, "long", entry, stop, entry + p["rr"] * (entry - stop), "limit", p["expiry"], p["hold"], t,
                             {"displacement": True, "fvg": True, "htf_trend": True})
        if dirn == -1 and c1 < o1 and d["high"].iat[i] < d["low"].iat[i - 2]:
            bot, top = d["high"].iat[i], d["low"].iat[i - 2]
            entry = (top + bot) / 2
            stop = d["high"].iat[i - 1] + p["stop_buffer_atr"] * atr
            t = _texts(observation=f"A bearish displacement candle left a gap between {bot:.6g} and {top:.6g} in a {self.htf} downtrend.",
                       interpretation="Aggressive sellers moved price faster than buyers could fill.",
                       alternative_interpretation="A capitulation spike that fully retraces.",
                       hypothesis=f"{self.tf}: a retrace into the gap holds and price travels {p['rr']:g}R below the entry.",
                       horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                       invalidation=f"price trades above the displacement high {stop:.6g}",
                       explanation="The first return to a bearish imbalance is where initiators defend their average price.",
                       undermined_by=f"The {self.htf} trend turning, or the gap being run through on the first touch.")
            return self._sig(d, i, "short", entry, stop, entry - p["rr"] * (stop - entry), "limit", p["expiry"], p["hold"], t,
                             {"displacement": True, "fvg": True, "htf_trend": True})
        return None


class OTERetrace(Setup):
    """In an HTF uptrend, a fresh 5m swing high above a leg of >= `leg_atr` x ATR: rest a LIMIT at the
    `fib` (0.705) retracement of the leg (the optimal trade entry zone), stop below the leg's origin,
    target the swing high."""
    id = "sniper_ote_retrace"
    name = "Optimal trade entry (62-79% retracement) after a break of structure"
    derived_from = ("strategy_trader_mayne_structure_ote", "strategy_nbb_trader_po3_ote_adr",
                    "concept_premium_discount_ote", "concept_fibonacci", "concept_market_structure")
    params = {"lookback": 36, "leg_atr": 4.0, "fib": 0.705, "stop_buffer_atr": 0.1, "expiry": 24, "hold": 72}

    def signal_at(self, d, i):
        p = self.p
        lb = p["lookback"]
        if i < lb + 2:
            return None
        atr, dirn = d["atr"].iat[i], d["htf_dir"].iat[i]
        if not np.isfinite(atr) or dirn == 0:
            return None
        hi = d["high"].iloc[i - lb + 1:i + 1].to_numpy()
        lo = d["low"].iloc[i - lb + 1:i + 1].to_numpy()
        if dirn == 1:
            h_idx = int(hi.argmax())
            if h_idx != lb - 1:                               # signal only on the bar that makes the new high
                return None
            l_idx = int(lo[:h_idx + 1].argmin())
            H, L = hi[h_idx], lo[l_idx]
            if H - L < p["leg_atr"] * atr:
                return None
            entry = H - p["fib"] * (H - L)
            stop = L - p["stop_buffer_atr"] * atr
            t = _texts(observation=f"A {H - L:.6g} leg from {L:.6g} broke to a new high {H:.6g} in a {self.htf} uptrend.",
                       interpretation="Structure shifted up; buyers are in control of this leg.",
                       alternative_interpretation="A liquidity grab above the prior high before a deeper reversal.",
                       hypothesis=f"{self.tf}: a retrace to the {p['fib']:.1%} level holds and price revisits the high {H:.6g}.",
                       horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                       invalidation=f"price trades below the leg origin {L:.6g}",
                       explanation="After a break of structure, the discount part of the leg is where the initiating buyers "
                                   "add; the prior high is the next pool of liquidity.",
                       undermined_by="A failed breakout: price falls back through the 79% level and the leg origin.")
            return self._sig(d, i, "long", entry, stop, H, "limit", p["expiry"], p["hold"], t,
                             {"bos": True, "leg_size": True, "htf_trend": True})
        l_idx = int(lo.argmin())
        if l_idx != lb - 1:
            return None
        h_idx = int(hi[:l_idx + 1].argmax())
        L, H = lo[l_idx], hi[h_idx]
        if H - L < p["leg_atr"] * atr:
            return None
        entry = L + p["fib"] * (H - L)
        stop = H + p["stop_buffer_atr"] * atr
        t = _texts(observation=f"A {H - L:.6g} leg from {H:.6g} broke to a new low {L:.6g} in a {self.htf} downtrend.",
                   interpretation="Structure shifted down; sellers are in control of this leg.",
                   alternative_interpretation="A liquidity grab below the prior low before a reversal up.",
                   hypothesis=f"{self.tf}: a retrace to the {p['fib']:.1%} level holds and price revisits the low {L:.6g}.",
                   horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                   invalidation=f"price trades above the leg origin {H:.6g}",
                   explanation="After a break of structure, the premium part of the leg is where the initiating sellers add.",
                   undermined_by="A failed breakdown: price rises back through the 79% level and the leg origin.")
        return self._sig(d, i, "short", entry, stop, L, "limit", p["expiry"], p["hold"], t,
                         {"bos": True, "leg_size": True, "htf_trend": True})


class ORBRetest(Setup):
    """New York opening range (09:30-10:00 New York time, daylight saving included): after the first
    close beyond the range, rest a LIMIT at the range edge for the retest; stop at the range
    midpoint; target `rr` R. Entries until `last_entry` New York; timeframes of 30 minutes or less."""
    id = "sniper_orb_retest"
    name = "Opening-range breakout and retest (New York open)"
    derived_from = ("strategy_vincent_desiano_break_retest", "strategy_okala_80_20_nasdaq", "concept_breakout_trading",
                    "concept_trading_sessions_killzones", "concept_support_resistance")
    params = {"last_entry_min": 12 * 60, "rr": 2.0, "expiry": 12, "hold": 48}
    max_tf = "30m"

    def signal_at(self, d, i):
        p = self.p
        orh, orl = d["or_hi"].iat[i], d["or_lo"].iat[i]
        if not np.isfinite([orh, orl]).all() or d["ny_min"].iat[i] >= p["last_entry_min"]:
            return None
        if d["or_closed_above_before"].iat[i] or d["or_closed_below_before"].iat[i]:
            return None
        mid = (orh + orl) / 2
        close = d["close"].iat[i]
        if close > orh:
            tx = _texts(observation=f"The first {self.tf} close above the New York opening range high {orh:.6g} (range {orl:.6g}-{orh:.6g}).",
                        interpretation="Buyers accepted prices above the opening auction.",
                        alternative_interpretation="A failed breakout that traps late buyers back inside the range.",
                        hypothesis=f"{self.tf}: a retest of {orh:.6g} holds and price travels {p['rr']:g}R above it.",
                        horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                        invalidation=f"a trade below the range midpoint {mid:.6g}",
                        explanation="The opening range is the session's first agreed value; acceptance outside it after a "
                                    "retest shows initiative.", undermined_by="Price returning inside the range and through its middle.")
            return self._sig(d, i, "long", orh, mid, orh + p["rr"] * (orh - mid), "limit", p["expiry"], p["hold"], tx,
                             {"range_defined": True, "breakout_close": True})
        if close < orl:
            tx = _texts(observation=f"The first {self.tf} close below the New York opening range low {orl:.6g} (range {orl:.6g}-{orh:.6g}).",
                        interpretation="Sellers accepted prices below the opening auction.",
                        alternative_interpretation="A failed breakdown that traps late sellers back inside the range.",
                        hypothesis=f"{self.tf}: a retest of {orl:.6g} holds and price travels {p['rr']:g}R below it.",
                        horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                        invalidation=f"a trade above the range midpoint {mid:.6g}",
                        explanation="Acceptance below the opening range after a retest shows initiative selling.",
                        undermined_by="Price returning inside the range and through its middle.")
            return self._sig(d, i, "short", orl, mid, orl - p["rr"] * (mid - orl), "limit", p["expiry"], p["hold"], tx,
                             {"range_defined": True, "breakout_close": True})
        return None


class EMAPullback(Setup):
    """HTF trend; a 5m bar dips to the 20 EMA and closes back in the trend direction as a rejection
    candle: enter at market on the next open, stop beyond the bar, target `rr` R."""
    id = "sniper_ema_pullback"
    name = "Trend pullback to the 20 EMA with a rejection close"
    derived_from = ("strategy_marci_silfrain_measured_move", "strategy_tori_trendline_4h", "strategy_anthony_crudele_futures_trend",
                    "concept_trend_following", "concept_moving_averages", "concept_multi_timeframe_analysis")
    params = {"stop_buffer_atr": 0.2, "rr": 2.0, "hold": 48}

    def signal_at(self, d, i):
        p = self.p
        atr, dirn = d["atr"].iat[i], d["htf_dir"].iat[i]
        o, h, l, c, e20, e50 = (d[k].iat[i] for k in ("open", "high", "low", "close", "ema20", "ema50"))
        if not np.isfinite([atr, e20, e50]).all():
            return None
        if dirn == 1 and c > e50 and l <= e20 < c and c > o:
            stop = l - p["stop_buffer_atr"] * atr
            tx = _texts(observation=f"In a {self.htf} uptrend, a {self.tf} bar dipped to the 20 EMA ({e20:.6g}) and closed up at {c:.6g}.",
                        interpretation="The pullback found buyers at the moving average.",
                        alternative_interpretation="The first leg of a deeper correction through the 50 EMA.",
                        hypothesis=f"{self.tf}: the trend resumes and price travels {p['rr']:g}R above entry.",
                        horizon=f"within {p['hold']} bars", invalidation=f"a trade below the pullback low {l:.6g}",
                        explanation="In an established trend, shallow pullbacks are bought by participants who missed the move.",
                        undermined_by=f"The {self.htf} trend rolling over, or a close below the 50 EMA.")
            return self._sig(d, i, "long", c, stop, c + p["rr"] * (c - stop), "market", 0, p["hold"], tx,
                             {"htf_trend": True, "ema_touch": True, "rejection": True})
        if dirn == -1 and c < e50 and h >= e20 > c and c < o:
            stop = h + p["stop_buffer_atr"] * atr
            tx = _texts(observation=f"In a {self.htf} downtrend, a {self.tf} bar rallied to the 20 EMA ({e20:.6g}) and closed down at {c:.6g}.",
                        interpretation="The rally found sellers at the moving average.",
                        alternative_interpretation="The first leg of a deeper correction through the 50 EMA.",
                        hypothesis=f"{self.tf}: the trend resumes and price travels {p['rr']:g}R below entry.",
                        horizon=f"within {p['hold']} bars", invalidation=f"a trade above the pullback high {h:.6g}",
                        explanation="In an established downtrend, shallow rallies are sold.",
                        undermined_by=f"The {self.htf} trend turning up, or a close above the 50 EMA.")
            return self._sig(d, i, "short", c, stop, c - p["rr"] * (stop - c), "market", 0, p["hold"], tx,
                             {"htf_trend": True, "ema_touch": True, "rejection": True})
        return None


class VWAPReversion(Setup):
    """In a range regime, a close back inside the VWAP - `k` sd band after a close outside it: enter at
    market, stop beyond the 3-bar extreme, target the session VWAP."""
    id = "sniper_vwap_reversion"
    name = "VWAP band re-entry in a range"
    derived_from = ("strategy_lance_breitstein_mean_reversion", "strategy_jj_simon_fair_pricing",
                    "concept_vwap", "concept_mean_reversion", "concept_auction_market_theory")
    params = {"k": 2.0, "stop_buffer_atr": 0.1, "hold": 36, "min_rr": 1.0}

    def signal_at(self, d, i):
        if i < 4:
            return None
        p = self.p
        if not str(d["regime"].iat[i]).startswith("range"):
            return None
        atr, vw, sd = d["atr"].iat[i], d["vwap"].iat[i], d["vwap_sd"].iat[i]
        c, cp = d["close"].iat[i], d["close"].iat[i - 1]
        if not np.isfinite([atr, vw, sd]).all() or sd <= 0:
            return None
        lo3, hi3 = d["low"].iloc[i - 2:i + 1].min(), d["high"].iloc[i - 2:i + 1].max()
        if cp < vw - p["k"] * sd <= c:
            stop = lo3 - p["stop_buffer_atr"] * atr
            if (vw - c) < p["min_rr"] * (c - stop):
                return None
            tx = _texts(observation=f"In a range, price closed below VWAP - {p['k']:g} sd and then back inside at {c:.6g} (VWAP {vw:.6g}).",
                        interpretation="The excursion below value was rejected.",
                        alternative_interpretation="The start of a range breakdown with value migrating lower.",
                        hypothesis=f"{self.tf}: price returns to the session VWAP {vw:.6g} before trading below {stop:.6g}.",
                        horizon=f"within {p['hold']} bars", invalidation=f"a trade below the 3-bar low {lo3:.6g}",
                        explanation="In balance, prices far from value attract responsive buyers back toward value.",
                        undermined_by="A shift from balance to trend: value migrating with price.")
            return self._sig(d, i, "long", c, stop, vw, "market", 0, p["hold"], tx,
                             {"range_regime": True, "band_reentry": True})
        if cp > vw + p["k"] * sd >= c:
            stop = hi3 + p["stop_buffer_atr"] * atr
            if (c - vw) < p["min_rr"] * (stop - c):
                return None
            tx = _texts(observation=f"In a range, price closed above VWAP + {p['k']:g} sd and then back inside at {c:.6g} (VWAP {vw:.6g}).",
                        interpretation="The excursion above value was rejected.",
                        alternative_interpretation="The start of a range breakout with value migrating higher.",
                        hypothesis=f"{self.tf}: price returns to the session VWAP {vw:.6g} before trading above {stop:.6g}.",
                        horizon=f"within {p['hold']} bars", invalidation=f"a trade above the 3-bar high {hi3:.6g}",
                        explanation="In balance, prices far from value attract responsive sellers back toward value.",
                        undermined_by="A shift from balance to trend: value migrating with price.")
            return self._sig(d, i, "short", c, stop, vw, "market", 0, p["hold"], tx,
                             {"range_regime": True, "band_reentry": True})
        return None


class BreakRetest(Setup):
    """Research spec S5. A momentum close through the prior-day high (low) or the last confirmed HTF
    pivot, after a close on the other side: rest a LIMIT just beyond the level for the retest; stop
    0.5 ATR back through the level; target 2R. 03:00-12:00 New York."""
    id = "sniper_break_retest"
    name = "Break and retest of a key level"
    derived_from = ("strategy_vincent_desiano_break_retest", "strategy_gala_trades_price_action",
                    "strategy_abraham_perez_ict_orderflow", "concept_support_resistance", "concept_breakout_trading")
    params = {"break_buffer_atr": 0.2, "break_body_atr": 0.6, "entry_offset_atr": 0.1, "stop_atr": 0.5, "rr": 2.0,
              "expiry": 12, "hold": 48, "window": (180, 720)}

    def signal_at(self, d, i):
        if i < 1:
            return None
        p = self.p
        if not (p["window"][0] <= d["ny_min"].iat[i] < p["window"][1]):
            return None
        atr, o, c, cp = d["atr"].iat[i], d["open"].iat[i], d["close"].iat[i], d["close"].iat[i - 1]
        if not np.isfinite(atr) or abs(c - o) < p["break_body_atr"] * atr:
            return None
        names = {"pdh": "prior-day high", "htf_pivot_high": f"last {self.htf} swing high",
                 "pdl": "prior-day low", "htf_pivot_low": f"last {self.htf} swing low"}
        if c > o:
            for col in ("pdh", "htf_pivot_high"):
                lv = d[col].iat[i]
                if np.isfinite(lv) and cp <= lv and c > lv + p["break_buffer_atr"] * atr:
                    entry, stop = lv + p["entry_offset_atr"] * atr, lv - p["stop_atr"] * atr
                    tx = _texts(observation=f"A {self.tf} momentum close at {c:.6g} broke the {names[col]} {lv:.6g}.",
                                interpretation="Sellers who defended the level are trapped; it may now act as support.",
                                alternative_interpretation="A failed breakout that falls back below the level.",
                                hypothesis=f"{self.tf}: a retest of {lv:.6g} holds and price travels {p['rr']:g}R above entry.",
                                horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                                invalidation=f"a trade below {stop:.6g}, back through the level",
                                explanation="A broken level changes role; stop orders clustered beyond it fuel the move "
                                            "(Osler, round-number and S/R order clustering).",
                                undermined_by="No retest (no trade), or a retest that closes back below the level.")
                    return self._sig(d, i, "long", entry, stop, entry + p["rr"] * (entry - stop), "limit", p["expiry"],
                                     p["hold"], tx, {"level_break": True, "momentum_body": True, "window": True})
        else:
            for col in ("pdl", "htf_pivot_low"):
                lv = d[col].iat[i]
                if np.isfinite(lv) and cp >= lv and c < lv - p["break_buffer_atr"] * atr:
                    entry, stop = lv - p["entry_offset_atr"] * atr, lv + p["stop_atr"] * atr
                    tx = _texts(observation=f"A {self.tf} momentum close at {c:.6g} broke the {names[col]} {lv:.6g}.",
                                interpretation="Buyers who defended the level are trapped; it may now act as resistance.",
                                alternative_interpretation="A failed breakdown that rises back above the level.",
                                hypothesis=f"{self.tf}: a retest of {lv:.6g} holds and price travels {p['rr']:g}R below entry.",
                                horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                                invalidation=f"a trade above {stop:.6g}, back through the level",
                                explanation="A broken level changes role; stops clustered beyond it fuel the move.",
                                undermined_by="No retest (no trade), or a retest that closes back above the level.")
                    return self._sig(d, i, "short", entry, stop, entry - p["rr"] * (stop - entry), "limit", p["expiry"],
                                     p["hold"], tx, {"level_break": True, "momentum_body": True, "window": True})
        return None


class AsiaLondonJudas(Setup):
    """Research spec S8. A compressed Asia range (20:00-24:00 New York, at most 0.5 x the 10-day average
    daily range) is swept in the London window (02:00-05:00 New York) and price closes back inside within
    6 bars: rest a LIMIT at the swept Asia extreme; stop beyond the sweep; target the opposite Asia
    extreme (at least 1.5R); flat by 11:00 New York."""
    id = "sniper_asia_london_judas"
    name = "Asia range, London sweep, return (session liquidity model)"
    derived_from = ("strategy_candace_lau_nq_sweep_reversal", "strategy_nbb_trader_po3_ote_adr",
                    "strategy_jadecap_liquidity_volatility", "concept_amd_power_of_three", "concept_trading_sessions_killzones")
    params = {"max_range_adr": 0.5, "london": (120, 300), "sweep_atr": 0.05, "return_bars": 6, "return_atr": 0.1,
              "stop_buffer_atr": 0.1, "min_r": 1.5, "expiry": 12, "flat_by": 660}
    max_tf = "15m"

    def signal_at(self, d, i):
        p = self.p
        nb = p["return_bars"]
        m = d["ny_min"].iat[i]
        if i < nb or not (p["london"][0] <= m < p["london"][1] + nb * self.step_min):
            return None
        ahi, alo, adr, atr = d["asia_hi"].iat[i], d["asia_lo"].iat[i], d["adr10"].iat[i], d["atr"].iat[i]
        if not np.isfinite([ahi, alo, adr, atr]).all() or ahi - alo > p["max_range_adr"] * adr:
            return None
        c, cp = d["close"].iat[i], d["close"].iat[i - 1]
        lows = d["low"].iloc[i - nb + 1:i + 1].to_numpy()
        highs = d["high"].iloc[i - nb + 1:i + 1].to_numpy()
        mins = d["ny_min"].iloc[i - nb + 1:i + 1].to_numpy()
        expiry = max(min(p["expiry"], int((p["london"][1] - m) // self.step_min)), 1)
        # the hold counts from the fill, which can come up to `expiry` bars later: flat by 11:00 at the latest
        hold = max(int((p["flat_by"] - m) // self.step_min) - expiry, 1)
        j = int(lows.argmin())
        if (lows[j] < alo - p["sweep_atr"] * atr and p["london"][0] <= mins[j] < p["london"][1]
                and c > alo + p["return_atr"] * atr and cp <= alo + p["return_atr"] * atr):
            stop = lows[j] - p["stop_buffer_atr"] * atr
            if (ahi - alo) < p["min_r"] * (alo - stop):
                return None
            tx = _texts(observation=f"London swept the Asia low {alo:.6g} (to {lows[j]:.6g}) and {self.tf} closed back above it at {c:.6g}.",
                        interpretation="Sell stops under the Asia range were run in the London open and absorbed.",
                        alternative_interpretation="The start of a London trend day down that will leave the range behind.",
                        hypothesis=f"{self.tf}: a retest of {alo:.6g} holds and price reaches the Asia high {ahi:.6g} by 11:00 New York.",
                        horizon="fill before 05:00 New York, flat by 11:00 New York",
                        invalidation=f"a trade below the sweep low {lows[j]:.6g}",
                        explanation="Asia's compressed range leaves stops on both sides; London volume runs one side, and when "
                                    "the run is absorbed price distributes toward the other side.",
                        undermined_by="A London breakout that keeps going (the opposite reading lost money in vendor tests).")
            return self._sig(d, i, "long", alo, stop, ahi, "limit", expiry, hold, tx,
                             {"compressed_asia": True, "london_sweep": True, "return_inside": True})
        j = int(highs.argmax())
        if (highs[j] > ahi + p["sweep_atr"] * atr and p["london"][0] <= mins[j] < p["london"][1]
                and c < ahi - p["return_atr"] * atr and cp >= ahi - p["return_atr"] * atr):
            stop = highs[j] + p["stop_buffer_atr"] * atr
            if (ahi - alo) < p["min_r"] * (stop - ahi):
                return None
            tx = _texts(observation=f"London swept the Asia high {ahi:.6g} (to {highs[j]:.6g}) and {self.tf} closed back below it at {c:.6g}.",
                        interpretation="Buy stops above the Asia range were run in the London open and absorbed.",
                        alternative_interpretation="The start of a London trend day up that will leave the range behind.",
                        hypothesis=f"{self.tf}: a retest of {ahi:.6g} holds and price reaches the Asia low {alo:.6g} by 11:00 New York.",
                        horizon="fill before 05:00 New York, flat by 11:00 New York",
                        invalidation=f"a trade above the sweep high {highs[j]:.6g}",
                        explanation="London volume runs one side of the Asia range; when the run is absorbed price distributes "
                                    "toward the other side.",
                        undermined_by="A London breakout that keeps going.")
            return self._sig(d, i, "short", ahi, stop, alo, "limit", expiry, hold, tx,
                             {"compressed_asia": True, "london_sweep": True, "return_inside": True})
        return None


class RoundNumberSweep(Setup):
    """Research spec S9. Price approached a round number from one side for 12 closes, poked through it by
    0.05-1.0 ATR and closed back: rest a LIMIT at the round number; stop beyond the poke; target 2R.
    02:00-16:00 New York. The grid is per market (BTC $1,000, ETH $100, EUR/USD 0.0050, gold $10)."""
    id = "sniper_round_number_sweep"
    name = "Round-number stop run and reclaim"
    derived_from = ("strategy_okala_80_20_nasdaq", "strategy_marco_trades_liquidity_grab", "concept_support_resistance",
                    "concept_liquidity_sweep_reversal")
    params = {"grid": None, "approach_bars": 12, "min_poke_atr": 0.05, "max_poke_atr": 1.0, "stop_buffer_atr": 0.1,
              "rr": 2.0, "expiry": 6, "hold": 48, "window": (120, 960)}
    symbol_params = {"BTCUSDT": {"grid": 1000.0}, "ETHUSDT": {"grid": 100.0}, "SOLUSDT": {"grid": 5.0},
                     "BNBUSDT": {"grid": 10.0}, "XRPUSDT": {"grid": 0.05}, "EURUSD": {"grid": 0.005},
                     "GBPUSD": {"grid": 0.005}, "USDJPY": {"grid": 0.5}, "XAUUSD": {"grid": 10.0}}

    def signal_at(self, d, i):
        p = self.p
        n = p["approach_bars"]
        if i < n + 1 or not (p["window"][0] <= d["ny_min"].iat[i] < p["window"][1]):
            return None
        atr, lo, hi, c = (d[k].iat[i] for k in ("atr", "low", "high", "close"))
        cp = d["close"].iat[i - 1]
        if not np.isfinite(atr) or atr <= 0:
            return None
        g = p["grid"] or 10 ** (np.floor(np.log10(cp)) - 1)
        prev = d["close"].iloc[i - n:i].to_numpy()
        lv = np.floor(cp / g) * g
        if (prev > lv).all() and lv - p["max_poke_atr"] * atr <= lo <= lv - p["min_poke_atr"] * atr and c > lv:
            stop = lo - p["stop_buffer_atr"] * atr
            tx = _texts(observation=f"After {n} closes above {lv:.6g}, a {self.tf} bar poked to {lo:.6g} and closed back above at {c:.6g}.",
                        interpretation="Stops parked under the round number fired without follow-through.",
                        alternative_interpretation="The first test of a level that will break on the next attempt.",
                        hypothesis=f"{self.tf}: a retest of {lv:.6g} holds and price travels {p['rr']:g}R above it.",
                        horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                        invalidation=f"a trade below {stop:.6g}",
                        explanation="Take-profit orders sit at round numbers and stop-losses just beyond them (Osler); a poke "
                                    "and close back means the stops fired and were absorbed.",
                        undermined_by="Crypto evidence: prices cluster at round numbers but returns after them show no pattern "
                                      "(Urquhart 2017).")
            return self._sig(d, i, "long", lv, stop, lv + p["rr"] * (lv - stop), "limit", p["expiry"], p["hold"], tx,
                             {"approach": True, "poke": True, "reclaim": True})
        lv = np.ceil(cp / g) * g
        if (prev < lv).all() and lv + p["min_poke_atr"] * atr <= hi <= lv + p["max_poke_atr"] * atr and c < lv:
            stop = hi + p["stop_buffer_atr"] * atr
            tx = _texts(observation=f"After {n} closes below {lv:.6g}, a {self.tf} bar poked to {hi:.6g} and closed back below at {c:.6g}.",
                        interpretation="Stops parked above the round number fired without follow-through.",
                        alternative_interpretation="The first test of a level that will break on the next attempt.",
                        hypothesis=f"{self.tf}: a retest of {lv:.6g} holds and price travels {p['rr']:g}R below it.",
                        horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                        invalidation=f"a trade above {stop:.6g}",
                        explanation="Stops just beyond a round number fired and were absorbed.",
                        undermined_by="Prices cluster at round numbers without a reliable reversal after them (Urquhart 2017).")
            return self._sig(d, i, "short", lv, stop, lv - p["rr"] * (stop - lv), "limit", p["expiry"], p["hold"], tx,
                             {"approach": True, "poke": True, "reclaim": True})
        return None


class OrderBlockMT(Setup):
    """Research spec S10 on one timeframe. A momentum close through the last confirmed pivot (body >= 0.8
    ATR); the order block is the last opposite candle in the 8 bars before the break; if its 50% (mean
    threshold) is in the discount half of the dealing range, rest a LIMIT there; stop beyond the block;
    target the dealing-range extreme (at least 1.5R)."""
    id = "sniper_ob_mean_threshold"
    name = "Order-block retest at the 50% after a break of structure"
    derived_from = ("strategy_trader_mayne_structure_ote", "concept_order_blocks_breakers", "concept_market_structure",
                    "concept_premium_discount_ote")
    params = {"bos_body_atr": 0.8, "range_lookback": 21, "ob_lookback": 8, "discount_max": 0.5, "stop_buffer_atr": 0.1,
              "min_r": 1.5, "expiry": 16, "hold": 32}

    def signal_at(self, d, i):
        p = self.p
        nl, nb = p["range_lookback"], p["ob_lookback"]
        if i < max(nl, nb) + 1:
            return None
        atr, o, c, cp = d["atr"].iat[i], d["open"].iat[i], d["close"].iat[i], d["close"].iat[i - 1]
        ph, pl = d["piv_hi"].iat[i - 1], d["piv_lo"].iat[i - 1]
        if not np.isfinite(atr) or abs(c - o) < p["bos_body_atr"] * atr:
            return None
        O = d["open"].iloc[i - nb:i].to_numpy()
        C = d["close"].iloc[i - nb:i].to_numpy()
        H = d["high"].iloc[i - nb:i].to_numpy()
        Lw = d["low"].iloc[i - nb:i].to_numpy()
        if np.isfinite(ph) and c > o and c > ph >= cp:
            lo_rng, hi_rng = d["low"].iloc[i - nl + 1:i + 1].min(), d["high"].iat[i]
            downs = np.where(C < O)[0]
            if not len(downs):
                return None
            k = downs[-1]
            mt = (H[k] + Lw[k]) / 2
            if mt > lo_rng + p["discount_max"] * (hi_rng - lo_rng):
                return None
            stop = Lw[k] - p["stop_buffer_atr"] * atr
            if hi_rng - mt < p["min_r"] * (mt - stop):
                return None
            tx = _texts(observation=f"A {self.tf} momentum close at {c:.6g} broke the swing high {ph:.6g}; the last down candle "
                                    f"before it spans {Lw[k]:.6g}-{H[k]:.6g}.",
                        interpretation="The side that broke structure added size in that block; its 50% is in the discount half.",
                        alternative_interpretation="A liquidity grab above the swing high before a reversal.",
                        hypothesis=f"{self.tf}: a retrace to {mt:.6g} holds and price returns to the range high {hi_rng:.6g}.",
                        horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                        invalidation=f"a trade below the order block {stop:.6g}",
                        explanation="The order block marks where the initiators last added; they defend their average price.",
                        undermined_by="Order blocks are confluence, not triggers; a vendor test of OB retests lost money (T4).")
            return self._sig(d, i, "long", mt, stop, hi_rng, "limit", p["expiry"], p["hold"], tx,
                             {"bos": True, "order_block": True, "discount": True})
        if np.isfinite(pl) and c < o and c < pl <= cp:
            hi_rng, lo_rng = d["high"].iloc[i - nl + 1:i + 1].max(), d["low"].iat[i]
            ups = np.where(C > O)[0]
            if not len(ups):
                return None
            k = ups[-1]
            mt = (H[k] + Lw[k]) / 2
            if mt < hi_rng - p["discount_max"] * (hi_rng - lo_rng):
                return None
            stop = H[k] + p["stop_buffer_atr"] * atr
            if mt - lo_rng < p["min_r"] * (stop - mt):
                return None
            tx = _texts(observation=f"A {self.tf} momentum close at {c:.6g} broke the swing low {pl:.6g}; the last up candle "
                                    f"before it spans {Lw[k]:.6g}-{H[k]:.6g}.",
                        interpretation="The side that broke structure added size in that block; its 50% is in the premium half.",
                        alternative_interpretation="A liquidity grab below the swing low before a reversal.",
                        hypothesis=f"{self.tf}: a retrace to {mt:.6g} holds and price returns to the range low {lo_rng:.6g}.",
                        horizon=f"fill within {p['expiry']} bars, target within {p['hold']} bars",
                        invalidation=f"a trade above the order block {stop:.6g}",
                        explanation="The order block marks where the initiators last added.",
                        undermined_by="Order blocks are confluence, not triggers.")
            return self._sig(d, i, "short", mt, stop, lo_rng, "limit", p["expiry"], p["hold"], tx,
                             {"bos": True, "order_block": True, "premium": True})
        return None


class SweepReclaimRetest(Setup):
    """Research spec S1, the maker version of the prior-day sweep: after the sweep and reclaim inside the
    London or New York morning window, rest a LIMIT at the reclaimed level (the retest) instead of buying
    the next open; stop beyond the sweep; target 2R."""
    id = "sniper_sweep_reclaim_limit"
    name = "Prior-day sweep + reclaim, retest entry (limit)"
    derived_from = SweepReclaim.derived_from
    params = {"min_sweep_atr": 0.1, "stop_buffer_atr": 0.1, "rr": 2.0, "expiry": 6, "hold": 48,
              "windows": ((120, 300), (480, 660))}           # spec S1: 02:00-05:00 and 08:00-11:00 New York

    def signal_at(self, d, i):
        m = d["ny_min"].iat[i]
        if not any(a <= m < b for a, b in self.p["windows"]):
            return None
        s = SweepReclaim(tf=self.tf, htf=self.htf, **{k: v for k, v in self.p.items() if k in SweepReclaim.params}).signal_at(d, i)
        if s is None:
            return None
        lvl = d["pdl"].iat[i] if s.side == "long" else d["pdh"].iat[i]
        target = lvl + (1 if s.side == "long" else -1) * self.p["rr"] * abs(lvl - s.stop)
        s.text["hypothesis"] = s.text["hypothesis"].replace("above entry", "above the retest").replace("below entry", "below the retest")
        s.text["horizon"] = f"fill within {self.p['expiry']} bars, target within {self.p['hold']} bars"
        return self._sig(d, i, s.side, lvl, s.stop, target, "limit", self.p["expiry"], self.p["hold"], s.text, s.conditions)


class EMAPullbackLimit(Setup):
    """Maker version of the EMA pullback: rest a LIMIT at the rejection bar's close for 2 bars instead of
    buying the next open (it fills only if price comes back to it)."""
    id = "sniper_ema_pullback_limit"
    name = "Trend pullback to the 20 EMA, limit entry"
    derived_from = EMAPullback.derived_from
    params = {"stop_buffer_atr": 0.2, "rr": 2.0, "expiry": 2, "hold": 48}

    def signal_at(self, d, i):
        s = EMAPullback(tf=self.tf, htf=self.htf, **{k: v for k, v in self.p.items() if k in EMAPullback.params}).signal_at(d, i)
        if s is None:
            return None
        return self._sig(d, i, s.side, s.entry, s.stop, s.target, "limit", self.p["expiry"], self.p["hold"], s.text, s.conditions)


class DonchianTrend(Setup):
    """Trend model (not a sniper entry): a fresh close beyond the previous 20-bar high (low), market
    entry, 2 ATR stop, 3R target, time exit after 60 bars. The Turtle rule set simplified to a bracket."""
    id = "trend_donchian_breakout"
    name = "Donchian 20-bar breakout (Turtle-style trend model)"
    derived_from = ("person_richard_donchian", "person_richard_dennis", "book_way_of_the_turtle", "book_complete_turtletrader",
                    "book_trend_following_covel", "concept_trend_following", "concept_breakout_trading")
    params = {"stop_atr": 2.0, "rr": 3.0, "hold": 60}

    def signal_at(self, d, i):
        if i < 1:
            return None
        p = self.p
        atr, c, cp = d["atr"].iat[i], d["close"].iat[i], d["close"].iat[i - 1]
        hi, lo, hip, lop = d["dc20_hi"].iat[i], d["dc20_lo"].iat[i], d["dc20_hi"].iat[i - 1], d["dc20_lo"].iat[i - 1]
        if not np.isfinite([atr, hi, lo, hip, lop]).all():
            return None
        for side, fresh in (("long", c > hi and cp <= hip), ("short", c < lo and cp >= lop)):
            if not fresh:
                continue
            sgn = 1 if side == "long" else -1
            stop = c - sgn * p["stop_atr"] * atr
            word = "high" if side == "long" else "low"
            tx = _texts(observation=f"A {self.tf} close at {c:.6g} beyond the previous 20-bar {word} {hi if side == 'long' else lo:.6g}.",
                        interpretation="Price left its recent range: the balance shifted.",
                        alternative_interpretation="A false breakout that returns into the range.",
                        hypothesis=f"{self.tf}: the move extends {p['rr']:g}R before it retraces {p['stop_atr']:g} ATR.",
                        horizon=f"within {p['hold']} bars", invalidation=f"a trade through {stop:.6g}",
                        explanation="Trends persist more often than chance in many markets (time-series momentum); a "
                                    "breakout is the simplest way to be on board.",
                        undermined_by="Range-bound markets where most breakouts fail (trend following wins rarely and big).")
            return self._sig(d, i, side, c, stop, c + sgn * p["rr"] * p["stop_atr"] * atr, "market", 0, p["hold"], tx,
                             {"breakout": True})
        return None


class IntradayMomentum(Setup):
    """Published effect (Gao, Han, Li & Zhou 2018 for the S&P 500; Shen, Urquhart & Wang 2022 for
    Bitcoin): the first half-hour's return predicts the last half-hour's. At 23:30 UTC, trade the last
    half-hour of the UTC day in the direction of the 00:00-00:30 return; protective stop 3 ATR; time exit
    at 24:00. Crypto only (a 24-hour market with a UTC day)."""
    id = "lit_intraday_momentum"
    name = "Intraday momentum: first half-hour predicts the last half-hour"
    derived_from = ("concept_trend_following", "concept_trading_sessions_killzones")
    params = {"stop_atr": 3.0, "min_abs_r": 0.0}
    max_tf = "30m"
    markets = ("crypto",)

    def signal_at(self, d, i):
        p = self.p
        t = d.index[i]
        if (t.hour * 60 + t.minute + self.step_min) != 23 * 60 + 30:
            return None
        r1, atr, c = d["first_half_hour_r"].iat[i], d["atr"].iat[i], d["close"].iat[i]
        if not np.isfinite([r1, atr]).all() or abs(r1) <= p["min_abs_r"] or r1 == 0:
            return None
        side, sgn = ("long", 1) if r1 > 0 else ("short", -1)
        hold = max(30 // self.step_min - 1, 0)
        stop = c - sgn * p["stop_atr"] * atr
        tx = _texts(observation=f"Today's first UTC half-hour returned {r1:+.3%}.",
                    interpretation="Early flows set the day's direction; late traders rebalance in the same direction.",
                    alternative_interpretation="Noise: the first half-hour says nothing about the last.",
                    hypothesis=f"{self.tf}: the last half-hour of the UTC day moves {'up' if sgn > 0 else 'down'}.",
                    horizon="23:30 to 24:00 UTC", invalidation=f"a trade through {stop:.6g}",
                    explanation="Published intraday momentum: informed early trading and late hedging/rebalancing flows "
                                "(Gao et al. 2018; Shen, Urquhart & Wang 2022 in Bitcoin).",
                    undermined_by="Effects found in-sample in academic data that weaken once known, or that are smaller than costs.")
        return self._sig(d, i, side, c, stop, c + sgn * 10 * p["stop_atr"] * atr, "market", 0, hold, tx,
                         {"time_window": True, "first_half_hour_signal": True})


SETUPS: dict[str, type[Setup]] = {s.id: s for s in (SweepReclaim, FVGRetrace, OTERetrace, ORBRetest, EMAPullback,
                                                    VWAPReversion, BreakRetest, AsiaLondonJudas, RoundNumberSweep,
                                                    OrderBlockMT, SweepReclaimRetest, EMAPullbackLimit, DonchianTrend,
                                                    IntradayMomentum)}
