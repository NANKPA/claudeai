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

from .feeds import resample


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
def prepare(df: pd.DataFrame, htf: str = "1h", vol_window_days: int = 30) -> pd.DataFrame:
    d = df.copy()
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
    d = d.join(hv.reindex(d.index, method="ffill"))
    # prior UTC day high / low / midpoint (known from the start of the day)
    day = resample(df, "1D")
    pdv = pd.DataFrame({"pdh": day["high"], "pdl": day["low"]})
    pdv.index = pdv.index + pd.Timedelta("1D")
    d = d.join(pdv.reindex(d.index, method="ffill"))
    d["pdm"] = (d["pdh"] + d["pdl"]) / 2
    # session VWAP (UTC day) and the dispersion around it, cumulative up to and including each bar
    tp = (d["high"] + d["low"] + d["close"]) / 3
    key = d.index.normalize()
    vol = d["volume"].where(d["volume"] > 0, 1e-12)
    cpv = (tp * vol).groupby(key).cumsum()
    cv = vol.groupby(key).cumsum()
    d["vwap"] = cpv / cv
    dev2 = ((tp - d["vwap"]) ** 2 * vol).groupby(key).cumsum() / cv
    d["vwap_sd"] = np.sqrt(dev2)
    # regime: HTF trend x volatility (ATR% above / below its trailing median)
    bars_per_day = int(round(pd.Timedelta("1D") / (d.index[1] - d.index[0]))) if len(d) > 1 else 288
    atr_pct = d["atr"] / d["close"]
    med = atr_pct.rolling(bars_per_day * vol_window_days, min_periods=bars_per_day * 5).median()
    up = (d["htf_ema20"] > d["htf_ema50"]) & (d["close"] > d["htf_ema50"])
    down = (d["htf_ema20"] < d["htf_ema50"]) & (d["close"] < d["htf_ema50"])
    d["htf_dir"] = np.where(up, 1, np.where(down, -1, 0))
    vol_tag = np.where(atr_pct > med, "high_vol", "low_vol")
    d["regime"] = np.where(d["htf_dir"] != 0, "trend_", "range_") + vol_tag
    d.loc[med.isna() | d["htf_ema50"].isna(), "regime"] = "unclear"
    hour = (d.index + (d.index[1] - d.index[0] if len(d) > 1 else pd.Timedelta("5min"))).hour
    d["session"] = np.select([hour < 7, hour < 13, hour < 21], ["asia", "london", "ny"], "late")
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

    def __init__(self, tf: str = "5m", htf: str = "1h", **overrides):
        self.tf, self.htf = tf, htf            # labels for the level the hypothesis is about (Gate 2)
        self.p = {**self.params, **overrides}

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
    """New York opening range (13:30-14:00 UTC): after a 5m close beyond the range, rest a LIMIT at the
    range edge for the retest; stop at the range midpoint; target `rr` R. One signal per day."""
    id = "sniper_orb_retest"
    name = "Opening-range breakout and retest (New York open)"
    derived_from = ("strategy_vincent_desiano_break_retest", "strategy_okala_80_20_nasdaq", "concept_breakout_trading",
                    "concept_trading_sessions_killzones", "concept_support_resistance")
    params = {"or_start": "13:30", "or_minutes": 30, "last_entry_hour": 16, "rr": 2.0, "expiry": 12, "hold": 48}

    def signal_at(self, d, i):
        p = self.p
        t = d.index[i]
        start = t.normalize() + pd.Timedelta(p["or_start"] + ":00")
        end = start + pd.Timedelta(minutes=p["or_minutes"])
        close_time = t + (d.index[1] - d.index[0])
        if not (end < close_time <= t.normalize() + pd.Timedelta(hours=p["last_entry_hour"])):
            return None
        rng = d.loc[start:end - pd.Timedelta(seconds=1)]
        if len(rng) == 0:
            return None
        orh, orl = rng["high"].max(), rng["low"].min()
        mid = (orh + orl) / 2
        after = d.loc[end:t]
        prev = after.iloc[:-1]
        close = d["close"].iat[i]
        # first close beyond the range today
        if close > orh and not (prev["close"] > orh).any() and not (prev["close"] < orl).any():
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
        if close < orl and not (prev["close"] < orl).any() and not (prev["close"] > orh).any():
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


SETUPS: dict[str, type[Setup]] = {s.id: s for s in (SweepReclaim, FVGRetrace, OTERetrace, ORBRetest, EMAPullback, VWAPReversion)}
