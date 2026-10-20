"""Market data for the sniper engine: deep history for backtests and live CLOSED candles for scanning.

History: Binance's public data archive (data.binance.vision, monthly zips of 1m/5m/15m/1h... klines,
no account and no API key) - reachable from most places, including where the Binance API is not.
Live: public REST endpoints of Coinbase, Kraken, OKX, KuCoin and Binance's public data API; forex
5-minute bars from Yahoo (last 60 days). Every live call drops the candle that is still forming, so a
detector can never see an unfinished bar.

All frames: UTC DatetimeIndex (bar OPEN time), float columns open, high, low, close, volume.
"""
from __future__ import annotations

import io
import json
import os
import time
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

CACHE = Path(os.environ.get("TI_CANDLE_CACHE", Path.home() / ".cache" / "trading-intelligence" / "candles"))
INTERVAL_SECONDS = {"1m": 60, "3m": 180, "5m": 300, "15m": 900, "30m": 1800, "1h": 3600, "4h": 14400, "1d": 86400}
_UA = {"User-Agent": "Mozilla/5.0 (trading-intelligence research)"}


def _get(url: str, timeout: float = 60) -> bytes:
    req = urllib.request.Request(url, headers=_UA)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (404, 451, 403):
                raise
            time.sleep(2 ** attempt)
        except OSError:
            time.sleep(2 ** attempt)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _frame(rows: list[list], ts_unit: str) -> pd.DataFrame:
    df = pd.DataFrame(rows, columns=["t", "open", "high", "low", "close", "volume"])
    df["t"] = pd.to_datetime(df["t"].astype("int64"), unit=ts_unit, utc=True)
    df = df.set_index("t").astype(float).sort_index()
    df = df[~df.index.duplicated(keep="last")]
    return df[(df[["open", "high", "low", "close"]] > 0).all(axis=1)]


# ── history ─────────────────────────────────────────────────────────────────
def binance_history(symbol: str = "BTCUSDT", interval: str = "5m", start: str = "2023-01",
                    end: str | None = None) -> pd.DataFrame:
    """Monthly klines from data.binance.vision, cached as CSV under TI_CANDLE_CACHE.
    `start`/`end` are "YYYY-MM"; `end` defaults to last month."""
    now = datetime.now(timezone.utc)
    end = end or f"{now.year if now.month > 1 else now.year - 1}-{(now.month - 1) or 12:02d}"
    y, m = map(int, start.split("-"))
    ey, em = map(int, end.split("-"))
    parts = []
    while (y, m) <= (ey, em):
        tag = f"{symbol}-{interval}-{y}-{m:02d}"
        path = CACHE / "binance" / symbol / interval / f"{tag}.csv"
        if not path.exists():
            url = f"https://data.binance.vision/data/spot/monthly/klines/{symbol}/{interval}/{tag}.zip"
            try:
                raw = _get(url, timeout=120)
            except urllib.error.HTTPError:
                raw = None
            if raw:
                with zipfile.ZipFile(io.BytesIO(raw)) as z:
                    text = z.read(z.namelist()[0]).decode()
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)
        if path.exists():
            rows = [line.split(",")[:6] for line in path.read_text().splitlines() if line and line[0].isdigit()]
            if rows:
                ts = int(rows[0][0])
                unit = "us" if ts > 10 ** 14 else "ms"          # the archive switched to microseconds in 2025
                parts.append(_frame([[r[0], r[1], r[2], r[3], r[4], r[5]] for r in rows], unit))
        m += 1
        if m == 13:
            y, m = y + 1, 1
    if not parts:
        raise RuntimeError(f"no history for {symbol} {interval} {start}..{end}")
    df = pd.concat(parts).sort_index()
    return df[~df.index.duplicated(keep="last")]


# Dukascopy's public datafeed: one LZMA file of 1-minute BID candles per day, no account needed.
# Records are big-endian (seconds from midnight, open, close, low, high as integers scaled by the
# point size, volume as float). Months in the URL are 0-based.
DUKA_POINT = {"EURUSD": 1e5, "GBPUSD": 1e5, "AUDUSD": 1e5, "USDCHF": 1e5, "USDCAD": 1e5, "NZDUSD": 1e5,
              "EURGBP": 1e5, "USDJPY": 1e3, "EURJPY": 1e3, "GBPJPY": 1e3, "XAUUSD": 1e3, "XAGUSD": 1e3}


_DUKA_LOCK = __import__("threading").Lock()
_DUKA_LAST = [0.0]
DUKA_MIN_INTERVAL = float(os.environ.get("TI_DUKA_MIN_INTERVAL", "0.35"))   # seconds between requests: be polite


def _duka_get(url: str) -> bytes | None:
    """GET with pacing and patient backoff (the free datafeed answers 429 when hurried). None on 404."""
    for attempt in range(9):
        with _DUKA_LOCK:
            wait = _DUKA_LAST[0] + DUKA_MIN_INTERVAL - time.time()
            if wait > 0:
                time.sleep(wait)
            _DUKA_LAST[0] = time.time()
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=_UA), timeout=60) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            time.sleep(min(5 * 2 ** attempt, 90) if e.code == 429 else min(2 ** attempt, 30))
        except OSError:
            time.sleep(min(2 ** attempt, 30))
    raise RuntimeError(f"dukascopy unreachable: {url}")


def _duka_decode(raw: bytes, symbol: str, t0: pd.Timestamp) -> pd.DataFrame | None:
    import lzma
    import struct
    if not raw:
        return None
    data = lzma.decompress(raw)
    rows = [struct.unpack(">5if", data[k:k + 24]) for k in range(0, len(data) - len(data) % 24, 24)]
    df = pd.DataFrame(rows, columns=["s", "open", "close", "low", "high", "volume"])
    df = df[df["volume"] > 0]                                  # weekend and holiday filler rows
    if df.empty:
        return None
    df.index = t0 + pd.to_timedelta(df["s"], unit="s")
    out = df[["open", "high", "low", "close"]] / DUKA_POINT[symbol]
    out["volume"] = df["volume"]
    return out


def _duka_day(symbol: str, day: pd.Timestamp) -> pd.DataFrame | None:
    url = (f"https://datafeed.dukascopy.com/datafeed/{symbol}/{day.year}/{day.month - 1:02d}/{day.day:02d}/"
           "BID_candles_min_1.bi5")
    return _duka_decode(_duka_get(url), symbol, day)


def _duka_month_hours(symbol: str, mth: pd.Period) -> pd.DataFrame | None:
    url = f"https://datafeed.dukascopy.com/datafeed/{symbol}/{mth.year}/{mth.month - 1:02d}/BID_candles_hour_1.bi5"
    return _duka_decode(_duka_get(url), symbol, pd.Timestamp(mth.start_time, tz="UTC"))


def dukascopy_history(symbol: str = "EURUSD", interval: str = "15m", start: str = "2022-01", end: str | None = None,
                      workers: int = 3) -> pd.DataFrame:
    """Forex and metals history from Dukascopy (BID candles), cached per month under TI_CANDLE_CACHE."""
    from concurrent.futures import ThreadPoolExecutor
    now = datetime.now(timezone.utc)
    end = end or f"{now.year if now.month > 1 else now.year - 1}-{(now.month - 1) or 12:02d}"
    months = pd.period_range(start, end, freq="M")
    hourly = INTERVAL_SECONDS.get(interval, 86400) >= 3600         # 1h and above: one file per month
    base = "1h" if hourly else "1m"
    parts = []
    for mth in months:
        path = CACHE / "dukascopy" / symbol / base / f"{symbol}-{base}-{mth}.csv.gz"
        if not path.exists():
            if hourly:
                frames = [f for f in [_duka_month_hours(symbol, mth)] if f is not None]
            else:
                days = [d for d in pd.date_range(mth.start_time, mth.end_time.normalize(), freq="D", tz="UTC")
                        if d.weekday() != 5]
                with ThreadPoolExecutor(max_workers=workers) as ex:
                    frames = [f for f in ex.map(lambda d: _duka_day(symbol, d), days) if f is not None]
            if not frames:
                continue
            m = pd.concat(frames).sort_index()
            path.parent.mkdir(parents=True, exist_ok=True)
            m.to_csv(path, compression="gzip")
        m = pd.read_csv(path, index_col=0, parse_dates=True)
        if m.index.tz is None:
            m.index = m.index.tz_localize("UTC")
        parts.append(m)
    if not parts:
        raise RuntimeError(f"no dukascopy history for {symbol} {start}..{end}")
    df = pd.concat(parts).sort_index()
    df = df[~df.index.duplicated(keep="last")]
    if interval == base:
        return df
    return resample(df, {"5m": "5min", "15m": "15min", "30m": "30min"}.get(interval, interval))


# ── live (closed candles only) ──────────────────────────────────────────────
def _closed(df: pd.DataFrame, interval: str) -> pd.DataFrame:
    now = pd.Timestamp.now(tz="UTC")
    return df[df.index + pd.Timedelta(seconds=INTERVAL_SECONDS[interval]) <= now]


def latest(venue: str, symbol: str, interval: str = "5m", limit: int = 300) -> pd.DataFrame:
    """The most recent CLOSED candles from a venue's public API.
    Symbols: coinbase "BTC-USD", kraken "XBTUSD", okx/kucoin "BTC-USDT", binance "BTCUSDT", yahoo "EURUSD=X"."""
    sec = INTERVAL_SECONDS[interval]
    v = venue.lower()
    if v == "coinbase":
        data = json.loads(_get(f"https://api.exchange.coinbase.com/products/{symbol}/candles?granularity={sec}"))
        df = _frame([[r[0], r[3], r[2], r[1], r[4], r[5]] for r in data], "s")
    elif v == "kraken":
        data = json.loads(_get(f"https://api.kraken.com/0/public/OHLC?pair={symbol}&interval={sec // 60}"))["result"]
        key = next(k for k in data if k != "last")
        df = _frame([[r[0], r[1], r[2], r[3], r[4], r[6]] for r in data[key]], "s")
    elif v == "okx":
        bar = {"1h": "1H", "4h": "4H", "1d": "1D"}.get(interval, interval)
        data = json.loads(_get(f"https://www.okx.com/api/v5/market/candles?instId={symbol}&bar={bar}&limit={min(limit, 300)}"))["data"]
        df = _frame([[r[0], r[1], r[2], r[3], r[4], r[5]] for r in data if r[8] == "1"], "ms")
    elif v == "kucoin":
        typ = {"1m": "1min", "5m": "5min", "15m": "15min", "30m": "30min", "1h": "1hour", "4h": "4hour", "1d": "1day"}[interval]
        data = json.loads(_get(f"https://api.kucoin.com/api/v1/market/candles?type={typ}&symbol={symbol}"))["data"]
        df = _frame([[r[0], r[1], r[3], r[4], r[2], r[5]] for r in data], "s")
    elif v == "binance":
        data = json.loads(_get(f"https://data-api.binance.vision/api/v3/klines?symbol={symbol}&interval={interval}&limit={min(limit, 1000)}"))
        df = _frame([[r[0], r[1], r[2], r[3], r[4], r[5]] for r in data], "ms")
    elif v == "csv":
        folder = Path(os.environ.get("TI_CSV_DIR", "."))
        raw = pd.read_csv(folder / f"{symbol}_{interval}.csv")
        tcol = raw.columns[0]
        t = pd.to_datetime(raw[tcol], utc=True)
        df = pd.DataFrame({"open": raw["open"], "high": raw["high"], "low": raw["low"], "close": raw["close"],
                           "volume": raw["volume"] if "volume" in raw else 0.0}).astype(float)
        df.index = t
        df = df[~df.index.duplicated(keep="last")].sort_index()
        return _closed(df[(df[["open", "high", "low", "close"]] > 0).all(axis=1)], interval).tail(limit)
    elif v == "yahoo":
        if interval == "4h":                                   # Yahoo has no 4h bars: build them from 1h
            return _closed(resample(latest("yahoo", symbol, "1h", limit=100000), "4h"), "4h").tail(limit)
        rng = "7d" if sec < 300 else "60d" if sec < 3600 else "730d"
        res = json.loads(_get(f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?interval={interval}&range={rng}"))
        r = res["chart"]["result"][0]
        q = r["indicators"]["quote"][0]
        rows = [[t, o, h, lo, c, vol or 0] for t, o, h, lo, c, vol in
                zip(r["timestamp"], q["open"], q["high"], q["low"], q["close"], q["volume"]) if None not in (o, h, lo, c)]
        df = _frame(rows, "s")
    else:
        raise ValueError(f"unknown venue {venue!r}")
    return _closed(df, interval).tail(limit)


def recent(venue: str, symbol: str, interval: str = "5m", days: float = 35) -> pd.DataFrame:
    """The last `days` of CLOSED candles, paging through the venue's API (Binance's public data API and
    Coinbase page; other venues return what one call gives, which may be too short to tag the regime:
    the gate then reads "unclear" and stands aside)."""
    sec = INTERVAL_SECONDS[interval]
    v = venue.lower()
    now = int(time.time())
    start = now - int(days * 86400)
    parts = []
    if v == "binance":
        t = start * 1000
        while t < now * 1000:
            data = json.loads(_get(f"https://data-api.binance.vision/api/v3/klines?symbol={symbol}&interval={interval}"
                                   f"&startTime={t}&limit=1000"))
            if not data:
                break
            parts.append(_frame([[r[0], r[1], r[2], r[3], r[4], r[5]] for r in data], "ms"))
            nxt = int(data[-1][0]) + sec * 1000
            if nxt <= t or len(data) < 1000:
                break
            t = nxt
    elif v == "coinbase":
        t = start
        while t < now:
            end = min(t + 300 * sec, now)
            a = datetime.fromtimestamp(t, timezone.utc).isoformat()
            b = datetime.fromtimestamp(end, timezone.utc).isoformat()
            data = json.loads(_get(f"https://api.exchange.coinbase.com/products/{symbol}/candles?granularity={sec}"
                                   f"&start={a}&end={b}"))
            if data:
                parts.append(_frame([[r[0], r[3], r[2], r[1], r[4], r[5]] for r in data], "s"))
            t = end
            time.sleep(0.15)                                       # public rate limit
    elif v == "csv":
        return latest("csv", symbol, interval, limit=int(days * 86400 // sec) + 1)
    else:
        return latest(venue, symbol, interval, limit=1000)
    if not parts:
        raise RuntimeError(f"no recent candles for {venue} {symbol} {interval}")
    df = pd.concat(parts).sort_index()
    return _closed(df[~df.index.duplicated(keep="last")], interval)


def resample(df: pd.DataFrame, rule: str) -> pd.DataFrame:
    """Higher-timeframe bars (labelled by their OPEN time)."""
    agg = {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
    return df.resample(rule, label="left", closed="left").agg(agg).dropna()
