#!/usr/bin/env python3
"""Daily OHLC market data for the evidence lab (tools/philosophy/studies.py).

Source: the public Yahoo Finance chart API (daily bars). Each symbol is
downloaded once and cached as ``tools/philosophy/data/<symbol>.csv`` (the
folder is git-ignored); later calls read the cache. ``--refresh`` (or
``load(symbol, refresh=True)``) downloads it again.

Cleaning (deliberately minimal, so the studies see the data as published):

* rows with a missing, zero or negative open/high/low/close are dropped
  (a price that is not positive cannot be turned into a return);
* duplicate dates keep the last bar; rows are sorted by date;
* dates are the exchange-local trading date of each bar.

Nothing else is changed: no adjustment for dividends or splits, no
back-adjustment of futures rolls, no outlier filter. Quality problems are
reported by :func:`quality_report` instead of being silently fixed.
:func:`bad_print_mask` flags isolated bad prints (a whole bar far away from
both neighbours, e.g. five ``EURUSD=X`` bars in 2008); the loader keeps them
and ``studies.py`` drops them explicitly.

Usage
-----
    python3 tools/philosophy/market_data.py                 # cache the default symbols
    python3 tools/philosophy/market_data.py ^GSPC GC=F      # cache / show these
    python3 tools/philosophy/market_data.py --refresh ^VIX  # re-download

Education, not financial advice.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import requests

DATA_DIR = Path(__file__).resolve().parent / "data"
CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
#: Query window used for every download: from the Unix epoch to a fixed end.
PERIOD1 = 0
PERIOD2 = 1791728465
HEADERS = {"User-Agent": "Mozilla/5.0"}
DEFAULT_SYMBOLS = ["^GSPC", "^NDX", "^VIX", "ES=F", "NQ=F", "CL=F", "GC=F", "EURUSD=X", "BTC-USD"]
COLUMNS = ["open", "high", "low", "close", "volume"]
PRICE_COLUMNS = ["open", "high", "low", "close"]


def cache_path(symbol: str) -> Path:
    """Path of the cached CSV for ``symbol``."""
    return DATA_DIR / f"{symbol}.csv"


def _download(symbol: str, timeout: float = 60.0) -> tuple[pd.DataFrame, dict]:
    """Fetch the raw daily bars of ``symbol``; returns (frame, meta)."""
    resp = requests.get(CHART_URL.format(symbol=requests.utils.quote(symbol, safe="")),
                        params={"period1": PERIOD1, "period2": PERIOD2, "interval": "1d"},
                        headers=HEADERS, timeout=timeout)
    resp.raise_for_status()
    payload = resp.json()
    chart = payload.get("chart") or {}
    if chart.get("error"):
        raise RuntimeError(f"{symbol}: API error {chart['error']}")
    result = (chart.get("result") or [None])[0]
    if not result or not result.get("timestamp"):
        raise RuntimeError(f"{symbol}: no data returned")
    meta = result.get("meta", {})
    quote = result["indicators"]["quote"][0]
    tz = meta.get("exchangeTimezoneName") or "UTC"
    stamps = pd.to_datetime(np.asarray(result["timestamp"], dtype="int64"), unit="s", utc=True)
    dates = stamps.tz_convert(tz).tz_localize(None).normalize()
    frame = pd.DataFrame({c: pd.to_numeric(pd.Series(quote.get(c)), errors="coerce").to_numpy()
                          for c in COLUMNS}, index=pd.DatetimeIndex(dates, name="date"))
    return frame, meta


def clean(frame: pd.DataFrame) -> pd.DataFrame:
    """Apply the documented cleaning rules (see module docstring)."""
    df = frame.copy()
    df = df[~df.index.duplicated(keep="last")].sort_index()
    prices = df[PRICE_COLUMNS]
    ok = prices.notna().all(axis=1) & (prices > 0).all(axis=1)
    df = df[ok].copy()
    df["volume"] = df["volume"].fillna(0.0)
    df.index.name = "date"
    return df[COLUMNS]


def load(symbol: str, refresh: bool = False) -> pd.DataFrame:
    """Daily bars of ``symbol`` as a DataFrame (date index; open/high/low/close/volume).

    Reads ``tools/philosophy/data/<symbol>.csv`` when present; otherwise (or
    with ``refresh=True``) downloads from the Yahoo Finance chart API, writes
    the raw bars to the cache and returns the cleaned frame.
    """
    path = cache_path(symbol)
    if refresh or not path.exists():
        raw, _ = _download(symbol)
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        raw.to_csv(path, float_format="%.6f")
    raw = pd.read_csv(path, index_col="date", parse_dates=["date"])
    return clean(raw)


#: A bar is a bad print when its whole range sits this many robust daily sds away from both neighbours.
BAD_PRINT_K = 5.0
#: Trailing window (bars) of the robust daily sd used by bad_print_mask.
BAD_PRINT_WINDOW = 60


def bad_print_mask(df: pd.DataFrame, k: float = BAD_PRINT_K, window: int = BAD_PRINT_WINDOW) -> pd.Series:
    """Isolated bad prints: True for a bar whose whole range lies far beyond BOTH neighbours' ranges.

    Bar ranges are widened to include open and close. A bar at t is flagged when
    ``log(low[t] / max(high[t-1], high[t+1]))`` (a spike up) or
    ``log(min(low[t-1], low[t+1]) / high[t])`` (a spike down) exceeds ``k``
    robust daily sds, the sd being 1.4826 x the median absolute daily log return
    of the ``window`` bars before t. A genuine shock moves the market to a new
    level, so its neighbour on one side overlaps it; a misprint jumps away and
    straight back. The rule looks at bar t+1, so it is a cleaning step for data
    errors, not something a decision at t could use. On the cached series it flags
    exactly five ``EURUSD=X`` bars in 2008 (closes about 6-15% off, all dated the 8th
    of a month) and nothing else.
    """
    if len(df) < 3:
        return pd.Series(False, index=df.index)
    hi = df[["open", "high", "close"]].max(axis=1)
    lo = df[["open", "low", "close"]].min(axis=1)
    r = np.log(df["close"]).diff()
    sd = r.abs().shift(1).rolling(window, min_periods=20).median() * 1.4826
    nb_hi = np.maximum(hi.shift(1), hi.shift(-1))
    nb_lo = np.minimum(lo.shift(1), lo.shift(-1))
    with np.errstate(invalid="ignore", divide="ignore"):
        up = np.log(lo / nb_hi)
        down = np.log(nb_lo / hi)
    return ((up > k * sd) | (down > k * sd)).fillna(False).astype(bool)


def quality_report(symbol: str) -> dict:
    """Counts of the rows dropped by cleaning and of suspicious bars that were kept."""
    path = cache_path(symbol)
    if not path.exists():
        load(symbol)
    raw = pd.read_csv(path, index_col="date", parse_dates=["date"])
    n_dup = int(raw.index.duplicated(keep="last").sum())
    raw = raw[~raw.index.duplicated(keep="last")]
    df = clean(raw)
    p = raw[PRICE_COLUMNS]
    hi_bad = df["high"] < df[["open", "close"]].max(axis=1) - 1e-9
    lo_bad = df["low"] > df[["open", "close"]].min(axis=1) + 1e-9
    return {
        "symbol": symbol,
        "first": df.index[0].date().isoformat() if len(df) else None,
        "last": df.index[-1].date().isoformat() if len(df) else None,
        "rows_raw": int(len(raw)),
        "rows_clean": int(len(df)),
        "dropped_missing": int(p.isna().any(axis=1).sum()),
        "dropped_nonpositive": int(((p <= 0).any(axis=1) & p.notna().all(axis=1)).sum()),
        "duplicate_dates": n_dup,
        "flat_bars": int((df["high"] == df["low"]).sum()),
        "inconsistent_bars": int((hi_bad | lo_bad).sum()),
        "bad_prints": int(bad_print_mask(df).sum()),
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Download and cache daily OHLC bars (Yahoo Finance chart API).")
    ap.add_argument("symbols", nargs="*", default=DEFAULT_SYMBOLS)
    ap.add_argument("--refresh", action="store_true", help="re-download even when cached")
    args = ap.parse_args(argv)
    for sym in args.symbols:
        try:
            load(sym, refresh=args.refresh)
            q = quality_report(sym)
        except Exception as exc:  # report and continue with the next symbol
            print(f"{sym}: failed: {exc}", file=sys.stderr)
            continue
        print(f"{sym:9s} {q['first']} -> {q['last']}  rows {q['rows_clean']:6d} "
              f"(dropped {q['dropped_missing']} missing, {q['dropped_nonpositive']} non-positive, "
              f"{q['duplicate_dates']} duplicate dates; kept {q['flat_bars']} flat, "
              f"{q['inconsistent_bars']} inconsistent, {q['bad_prints']} bad-print bars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
