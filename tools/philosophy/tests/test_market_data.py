"""Tests for the data-quality helpers of tools/philosophy/market_data.py (no network)."""
import numpy as np
import pandas as pd

from tools.philosophy import market_data as md


def _bars(close: np.ndarray) -> pd.DataFrame:
    idx = pd.bdate_range("2020-01-01", periods=len(close))
    c = pd.Series(close, index=idx)
    return pd.DataFrame({"open": c.shift(1).fillna(c.iloc[0]), "high": c * 1.002, "low": c * 0.998,
                         "close": c, "volume": 0.0})


def _walk(n: int = 300, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return 100 * np.exp(np.cumsum(rng.normal(0, 0.005, n)))


def test_bad_print_mask_flags_an_isolated_misprint():
    c = _walk()
    df = _bars(c)
    df.iloc[150, :4] = df.iloc[150, :4] * 1.10  # whole bar 10% off, next bar back to normal
    mask = md.bad_print_mask(df)
    assert mask.sum() == 1 and bool(mask.iloc[150])


def test_bad_print_mask_keeps_genuine_shocks():
    c = _walk()
    c[150:] *= 0.85  # a crash to a new level: the next bar overlaps the shocked one
    assert md.bad_print_mask(_bars(c)).sum() == 0
    c2 = _walk(seed=1)
    c2[150] *= 0.90  # one-day crash with a partial (not full) rebound
    c2[151:] *= 0.95
    assert md.bad_print_mask(_bars(c2)).sum() == 0


def test_bad_print_mask_short_input():
    df = _bars(np.array([1.0, 2.0]))
    assert not md.bad_print_mask(df).any()
