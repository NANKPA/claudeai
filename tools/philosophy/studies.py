#!/usr/bin/env python3
"""Evidence lab: the Philosophy of the Relationship tested on real daily market data.

Runs seven pre-registered studies (S1-S7), each tied to a section of
trading-intelligence/00_philosophy/philosophy-of-the-relationship.md, and
writes the report trading-intelligence/00_philosophy/evidence-lab.md plus one
PNG chart per study in trading-intelligence/00_philosophy/figures/.

    python3 tools/philosophy/studies.py            # cached data (downloaded if missing)
    python3 tools/philosophy/studies.py --refresh  # re-download the data first

Every rule and parameter lives in the PARAMS block below. It was fixed before
any result was computed and is printed verbatim into the report. Every number
in the report is computed by this script. Seeds are fixed, so a re-run on the
same cached data reproduces the report (apart from the runtime line).

Education, not financial advice. Not a trading signal.
"""
from __future__ import annotations

import argparse
import math
import sys
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.ticker  # noqa: E402,F401
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from numpy.lib.stride_tricks import sliding_window_view  # noqa: E402
from scipy import stats  # noqa: E402

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import edge_lab as el  # noqa: E402
import market_data as md  # noqa: E402

# --- PARAMS (pre-registered: fixed before any result was computed) ---
PARAMS = {
    "data_end": "2026-09-30",            # last bar used (complete months only)
    "is_end": "2012-12-31",              # in-sample: every bar up to this date
    "oos_start": "2013-01-01",           # out-of-sample: every bar from this date
    "purge": "an in-sample observation counts only if its whole outcome window ends by is_end",
    "bars": "high = max(open, high, close), low = min(open, low, close); nothing else changed",
    "atr_len": 14,                       # Wilder ATR (exponential, alpha = 1/14) of true range
    "sma_fast": 50,
    "sma_slow": 200,
    "trend_rule": "uptrend at t: close > SMA200 and SMA50 > SMA200 (data up to t); else 'other'",
    "seed": 20261011,
    "n_boot": 2000,                      # block-bootstrap replicates
    "ci": 0.95,
    "S1": {
        "symbols": ["^GSPC", "^NDX", "GC=F", "EURUSD=X", "CL=F"],
        "entries": "every day t with SMA200 and ATR14 defined; A = close[t]",
        "target_atr": 3.0,               # B = A + 3 * ATR14[t]
        "horizon": 60,                   # bars t+1 .. t+60
        "depths_atr": [0.5, 1.0, 1.5, 2.0, 3.0],  # C_k = A - k * ATR14[t]
        "event": "C_k touched before B: first bar with low <= C_k comes no later than first bar with high >= B",
        "tie_rule": "C_k and B on the same bar: adverse move first, and that bar does not count as reaching B",
        "block_calendar_days": 182,      # dependence: non-overlapping calendar blocks, all symbols together
        "null_paths": 20000,             # memoryless null per symbol x regime x period
        "null_model": "i.i.d. resampled days (close, high, low change / previous ATR) from the same symbol, "
                      "period and previous-day regime; same B, C_k and tie rule",
        "structural_change_rule": "depth k behaves like structural change in a regime if the 95% CI of "
                                  "P(B | C_k) lies entirely below the null value in BOTH IS and OOS",
    },
    "S2": {
        "symbols": ["^GSPC", "^NDX", "EURUSD=X", "GC=F"],
        "horizon": 5,                    # outcome: log(close[t+5] / close[t])
        "vol_window": 20,                # realised vol of daily log returns t-19..t
        "vol_terciles": "per symbol, 1/3 and 2/3 quantiles of in-sample realised vol",
        "pattern": "3 consecutive lower closes: close[t] < close[t-1] < close[t-2] < close[t-3]",
        "block_calendar_days": 91,
        "found_rule": "IS 95% CI of (cell - unconditional) excludes 0",
        "held_rule": "held: same sign OOS and OOS CI excludes 0; weakened: same sign, CI includes 0; "
                     "vanished: opposite sign, CI includes 0; reversed: opposite sign, CI excludes 0",
    },
    "S3": {
        "p_win": 0.55, "reward_risk": 1.0, "cost_r": 0.05,
        "n_trades": [10, 30, 100, 300, 1000],
        "n_samples": 100000,
        "looks_like_loser": "observed expectancy after costs <= 0",
        "looks_like_star": "observed win rate >= 0.70",
        "empirical_cell": "the S7 cell (best S2 cell chosen in-sample), non-overlapping 5-day trades",
    },
    "S4": {
        "strategies": [[0.35, 2.5], [0.50, 1.5], [0.60, 1.0]],   # [p_win, reward:risk]
        "cost_r": 0.05,
        "risk_per_trade": [0.005, 0.01, 0.02, 0.05, 0.10],
        "n_trades": 250, "n_paths": 10000, "ruin_drawdown": 0.50,
        "streaks": [6, 10],
        "recovery_losses": [0.10, 0.20, 0.30, 0.50, 0.75, 0.90],
    },
    "S5": {
        "symbol": "^GSPC",
        "cost_bp_per_side": 1.0,
        "position": "decided at close t from closes up to t; earns close-to-close return t -> t+1; flat earns 0",
        "ma_cross_fast": [5, 10, 15, 20, 25, 30, 40, 50, 60, 80, 100],
        "ma_cross_slow": [50, 75, 100, 125, 150, 200, 250, 300],
        "price_vs_ma": [10, 20, 50, 100, 150, 200, 250, 300],
        "momentum_lookback": [10, 20, 40, 60, 90, 120, 180, 250],
        "donchian_entry": [10, 20, 40, 55, 80, 100, 150, 200, 250],   # close > max of prior N closes
        "donchian_exit": [5, 10, 20, 40, 60],                         # close < min of prior M closes (M < N)
        "modes": ["long/flat", "long/short"],   # Donchian: long/flat with exit M; long/short stop-and-reverse on N
        "selection": "highest in-sample annualised Sharpe (252 days), net of costs",
        "n_shuffles": 20,                # in-sample daily returns permuted: no signal left
        "warmup_bars": 301,
    },
    "S6": {
        "p_win": 0.60, "win": 100.0, "loss": 120.0, "cost": 5.0,
        "twin_p_win": 0.55,
        "n_trades": [1, 10, 20, 50, 100, 500],
        "n_sims": 100000,
    },
    "S7": {
        "selection": "largest in-sample mean 5-day log return among the non-baseline S2 cells "
                     "(all symbols) with at least 150 in-sample observations",
        "min_is_obs": 150,
        "trades": "long, enter at close t when the cell holds, exit at close t+5, no overlapping trades",
        "costs_bp_per_side": [0, 1, 2, 5, 10],
    },
    "figures_dpi": 110,
}
# --- end PARAMS ---

#: Changes made after the first results were seen. Kept empty unless something had to change.
DEVIATIONS: list[str] = [
    "Data (added in review): isolated bad prints are dropped before any study runs "
    "(`market_data.bad_print_mask`: a bar whose whole range sits more than 5 robust daily sds beyond BOTH "
    "neighbours' ranges; the bars removed are listed under *Data and caveats*). Kept, they inflated the ATR "
    "and realised volatility of the affected market for weeks, moved the first touches of B and C in S1, and "
    "put large outliers into S2's 5-day returns. Every number on this page was recomputed after the change.",
    "S2: a cell whose observations fall in fewer than 10 distinct bootstrap blocks in either period is "
    "reported as 'too few to judge' instead of being classified. Added after the first run, where a cell "
    "with 4 out-of-sample observations (all in one or two blocks) received a 95% CI under 6 points wide and "
    "a 'reversed' label: with so few blocks the block bootstrap cannot see the uncertainty. The cut-off of "
    "10 blocks was set once, from that reasoning, and not tuned; S7's candidate rule is unchanged.",
]
S2_MIN_BLOCKS = 10  # see DEVIATIONS

P = PARAMS
REPO = HERE.parents[1]
OUT_DIR = REPO / "trading-intelligence" / "00_philosophy"
FIG_DIR = OUT_DIR / "figures"
REPORT = OUT_DIR / "evidence-lab.md"

# chart palette (reference light palette of the dataviz method)
C_SURF, C_TEXT, C_TEXT2, C_GRID, C_MUTED = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df", "#a9a8a2"
C_SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
MARKERS = ["o", "s", "^", "D"]


def log(msg: str) -> None:
    print(msg, flush=True)


# ---------------------------------------------------------------------------
# formatting
# ---------------------------------------------------------------------------
def pct(x: float, d: int = 1) -> str:
    return "n/a" if x is None or not np.isfinite(x) else f"{100 * x:.{d}f}%"


def pp(x: float, d: int = 1, signed: bool = False) -> str:
    if x is None or not np.isfinite(x):
        return "n/a"
    v = 100 * x
    if abs(v) < 0.5 * 10 ** -d:
        return f"{0:.{d}f}"
    return f"{v:+.{d}f}" if signed else f"{v:.{d}f}"


def ci_pct(lo: float, hi: float, d: int = 1, signed: bool = False) -> str:
    return f"[{pp(lo, d, signed)}, {pp(hi, d, signed)}]"


def bp(x: float, d: int = 0, signed: bool = True) -> str:
    if x is None or not np.isfinite(x):
        return "n/a"
    if 0 < abs(1e4 * x) < 0.5 * 10 ** -d:  # would print as "-0"/"+0": show one more decimal
        d += 1
    return f"{1e4 * x:+.{d}f}" if signed else f"{1e4 * x:.{d}f}"


def share(x: float, n: int, d: int = 1) -> str:
    """A simulated share of n paths; shares that would print as 0% or 100% are given as counts."""
    if x is None or not np.isfinite(x):
        return "n/a"
    k = int(round(x * n))
    if k == n:
        return f"all {n:,}"
    if round(100 * x, d) == 0 or round(100 * x, d) == 100:
        return f"{k:,} of {n:,}"
    return pct(x, d)


def prob(x: float, d: int = 1) -> str:
    """An exact probability; values that would round to 0% or 100% are shown as bounds."""
    if x is None or not np.isfinite(x):
        return "n/a"
    lim = 0.5 * 10 ** -(d + 2)
    if 0 < x < lim:
        return f"<{pct(lim * 2, d)}"
    if 1 - lim < x < 1:
        return f">{pct(1 - lim * 2, d)}"
    return pct(x, d)


def ci_bp(lo: float, hi: float, d: int = 0) -> str:
    return f"[{bp(lo, d)}, {bp(hi, d)}]"


def num(x: float, d: int = 2) -> str:
    return "n/a" if x is None or not np.isfinite(x) else f"{x:.{d}f}"


def table(header: list[str], rows: list[list[str]], align: str | None = None) -> list[str]:
    al = align or ("l" + "r" * (len(header) - 1))
    sep = ["---:" if a == "r" else ":---:" if a == "c" else "---" for a in al]
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(sep) + " |"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out + [""]


# ---------------------------------------------------------------------------
# charts
# ---------------------------------------------------------------------------
plt.rcParams.update({
    "font.size": 8.5, "axes.titlesize": 9.5, "axes.labelsize": 8.5, "legend.fontsize": 8,
    "axes.edgecolor": C_GRID, "axes.labelcolor": C_TEXT2, "xtick.color": C_TEXT2, "ytick.color": C_TEXT2,
    "text.color": C_TEXT, "axes.titlecolor": C_TEXT, "axes.grid": True, "grid.color": C_GRID,
    "grid.linewidth": 0.6, "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": C_SURF, "axes.facecolor": C_SURF, "savefig.facecolor": C_SURF,
    "legend.frameon": False, "lines.linewidth": 2.0,
})


def new_fig(ncols: int = 1, w: float = 7.6, h: float = 3.7):
    fig, axes = plt.subplots(1, ncols, figsize=(w, h), squeeze=False)
    return fig, axes.ravel()


def save_fig(fig, name: str) -> str:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(FIG_DIR / name, dpi=P["figures_dpi"], metadata={"Software": None})
    plt.close(fig)
    return f"figures/{name}"


# ---------------------------------------------------------------------------
# data and shared helpers
# ---------------------------------------------------------------------------
_DATA: dict[str, pd.DataFrame] = {}
REFRESH = False


def prepare(raw: pd.DataFrame) -> pd.DataFrame:
    """Cut at data_end, drop isolated bad prints, make bars consistent, add ATR, SMAs, regime and
    realised vol (causal: each value at t uses bars up to t)."""
    df = raw.loc[: P["data_end"]].copy()
    bad = md.bad_print_mask(df)  # see DEVIATIONS; a data-error filter, it looks at bar t+1
    df = df[~bad.to_numpy()].copy()
    df["high"] = df[["open", "high", "close"]].max(axis=1)
    df["low"] = df[["open", "low", "close"]].min(axis=1)
    c = df["close"]
    prev = c.shift(1)
    tr = pd.concat([df["high"] - df["low"], (df["high"] - prev).abs(), (df["low"] - prev).abs()],
                   axis=1).max(axis=1)
    df["atr"] = tr.ewm(alpha=1.0 / P["atr_len"], adjust=False, min_periods=P["atr_len"]).mean()
    df["sma_fast"] = c.rolling(P["sma_fast"]).mean()
    df["sma_slow"] = c.rolling(P["sma_slow"]).mean()
    df["uptrend"] = (c > df["sma_slow"]) & (df["sma_fast"] > df["sma_slow"])
    lr = np.log(c).diff()
    df["lr"] = lr
    df["rv"] = lr.rolling(P["S2"]["vol_window"]).std() * math.sqrt(252)
    df["ctx_ok"] = df["sma_slow"].notna() & df["atr"].notna() & (df["atr"] > 0)
    return df


def get(symbol: str) -> pd.DataFrame:
    if symbol not in _DATA:
        _DATA[symbol] = prepare(md.load(symbol, refresh=REFRESH))
    return _DATA[symbol]


def period_masks(df: pd.DataFrame, horizon: int) -> tuple[np.ndarray, np.ndarray]:
    """IS / OOS entry masks with the outcome window fully inside its period (purged)."""
    n = len(df)
    pos = np.arange(n)
    is_last = int(np.searchsorted(df.index.values, np.datetime64(P["is_end"]), side="right")) - 1
    is_ok = pos + horizon <= is_last
    oos_ok = (df.index >= pd.Timestamp(P["oos_start"])) & (pos + horizon <= n - 1)
    return is_ok, np.asarray(oos_ok)


def calendar_blocks(dates: pd.DatetimeIndex | np.ndarray, days: int) -> np.ndarray:
    d = pd.DatetimeIndex(dates)
    return ((d - pd.Timestamp("1970-01-01")).days // days).to_numpy()


def block_bootstrap(nums: np.ndarray, dens: np.ndarray, blocks: np.ndarray, rng: np.random.Generator,
                    n_boot: int) -> tuple[np.ndarray, np.ndarray]:
    """Ratio statistics sum(num)/sum(den) per column, and their block-bootstrap replicates.

    Non-overlapping blocks are resampled with replacement (same blocks for every
    column, so differences between columns are bootstrapped jointly).
    """
    nums = np.asarray(nums, dtype=float)
    dens = np.asarray(dens, dtype=float)
    if nums.ndim == 1:
        nums, dens = nums[:, None], dens[:, None]
    ub, inv = np.unique(blocks, return_inverse=True)
    nb = len(ub)
    N = np.zeros((nb, nums.shape[1]))
    D = np.zeros((nb, nums.shape[1]))
    np.add.at(N, inv, nums)
    np.add.at(D, inv, dens)
    idx = rng.integers(0, nb, size=(n_boot, nb))
    W = np.zeros((n_boot, nb))
    np.add.at(W, (np.repeat(np.arange(n_boot), nb), idx.ravel()), 1.0)
    with np.errstate(invalid="ignore", divide="ignore"):
        point = N.sum(0) / D.sum(0)
        reps = (W @ N) / (W @ D)
    return point, reps


def ci_of(reps: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    a = (1 - P["ci"]) / 2
    with np.errstate(invalid="ignore"):
        lo, hi = np.nanpercentile(reps, [100 * a, 100 * (1 - a)], axis=0)
    return lo, hi


def data_section_rows() -> list[list[str]]:
    rows = []
    used = {s: [] for s in md.DEFAULT_SYMBOLS}
    for k in ["S1", "S2"]:
        for s in P[k]["symbols"]:
            used[s].append(k)
    used[P["S5"]["symbol"]].append("S5")
    for s in used:
        if not used[s]:
            continue
        df = get(s)
        raw = pd.read_csv(md.cache_path(s), index_col="date", parse_dates=["date"]).sort_index()
        raw = raw.loc[: P["data_end"]]
        dups = int(raw.index.duplicated(keep="last").sum())
        raw = raw[~raw.index.duplicated(keep="last")]
        pr = raw[md.PRICE_COLUMNS]
        missing = int(pr.isna().any(axis=1).sum())
        nonpos = int(((pr <= 0).any(axis=1) & pr.notna().all(axis=1)).sum())
        cl = md.clean(raw)
        spikes = int(md.bad_print_mask(cl).sum())
        oc_hi, oc_lo = cl[["open", "close"]].max(axis=1), cl[["open", "close"]].min(axis=1)
        flat = int((cl["high"] == cl["low"]).sum())
        bad = int(((cl["high"] < oc_hi - 1e-9) | (cl["low"] > oc_lo + 1e-9)).sum())
        rows.append([f"`{s}`", df.index[0].date().isoformat(), df.index[-1].date().isoformat(), f"{len(df):,}",
                     str(missing), str(nonpos), str(dups), str(spikes), str(flat), str(bad),
                     ", ".join(sorted(set(used[s])))])
    return rows


def flat_share(symbol: str, start: str | None = None, end: str | None = None) -> float:
    """Share of bars with high == low (no intraday range recorded) in a date window."""
    df = get(symbol).loc[start:end]
    return float((df["high"] == df["low"]).mean()) if len(df) else float("nan")


# ---------------------------------------------------------------------------
# S1: A -> C -> B
# ---------------------------------------------------------------------------
def first_passage(HW: np.ndarray, LW: np.ndarray, A: np.ndarray, R: np.ndarray, target: float,
                  depths: list[float]) -> tuple[dict, dict]:
    """Reach-B and touched-C-before-B events for windows of future highs/lows (rows = entries)."""
    H = HW.shape[1]
    hitB = HW >= (A + target * R)[:, None]
    anyB = hitB.any(axis=1)
    tB = np.where(anyB, hitB.argmax(axis=1), H)
    lastB = np.where(anyB, H - 1 - hitB[:, ::-1].argmax(axis=1), -1)
    res: dict = {"B": anyB}
    ties: dict = {}
    for k in depths:
        hitC = LW <= (A - k * R)[:, None]
        anyC = hitC.any(axis=1)
        tC = np.where(anyC, hitC.argmax(axis=1), H)
        E = anyC & (tC <= tB)
        res[("E", k)] = E
        res[("BC", k)] = E & (lastB > tC)
        ties[k] = int((anyC & (tC == tB)).sum())
    return res, ties


def s1_symbol(sym: str, rng: np.random.Generator) -> tuple[pd.DataFrame, dict, dict]:
    p1 = P["S1"]
    H, tgt, depths = p1["horizon"], p1["target_atr"], p1["depths_atr"]
    df = get(sym)
    n = len(df)
    hi, lo, cl, atr = (df[c].to_numpy(float) for c in ["high", "low", "close", "atr"])
    m = n - H
    HW = sliding_window_view(hi[1:], H)[:m]
    LW = sliding_window_view(lo[1:], H)[:m]
    is_ok, oos_ok = period_masks(df, H)
    ok = df["ctx_ok"].to_numpy()[:m] & (is_ok[:m] | oos_ok[:m])
    idx = np.flatnonzero(ok)
    res, ties = first_passage(HW[idx], LW[idx], cl[idx], atr[idx], tgt, depths)
    obs = pd.DataFrame({"date": df.index[idx], "symbol": sym,
                        "period": np.where(is_ok[idx], "IS", "OOS"),
                        "regime": np.where(df["uptrend"].to_numpy()[idx], "uptrend", "other"),
                        "B": res["B"]})
    for k in depths:
        obs[f"E{k}"] = res[("E", k)]
        obs[f"BC{k}"] = res[("BC", k)]
    # memoryless null: i.i.d. days, normalised by the previous day's ATR
    prevc, prevatr = cl[:-1], atr[:-1]
    with np.errstate(invalid="ignore", divide="ignore"):
        d = (cl[1:] - prevc) / prevatr
        h = (hi[1:] - prevc) / prevatr
        lw = (lo[1:] - prevc) / prevatr
    ctx_prev = df["ctx_ok"].to_numpy()[:-1]
    up_prev = df["uptrend"].to_numpy()[:-1]
    dates_j = df.index[1:]
    in_is = np.asarray(dates_j <= pd.Timestamp(P["is_end"]))
    in_oos = np.asarray(dates_j >= pd.Timestamp(P["oos_start"]))
    null: dict = {}
    for period, pmask in [("IS", in_is), ("OOS", in_oos)]:
        for regime, rmask in [("uptrend", up_prev), ("other", ~up_prev)]:
            pool = np.flatnonzero(ctx_prev & rmask & pmask & np.isfinite(d))
            if len(pool) < 50:
                continue
            draw = pool[rng.integers(0, len(pool), size=(p1["null_paths"], H))]
            cp = np.cumsum(d[draw], axis=1)
            base = np.concatenate([np.zeros((cp.shape[0], 1)), cp[:, :-1]], axis=1)
            z = np.zeros(cp.shape[0])
            nres, _ = first_passage(base + h[draw], base + lw[draw], z, np.ones_like(z), tgt, depths)
            null[(period, regime)] = {"B": float(nres["B"].mean()),
                                      **{("E", k): float(nres[("E", k)].mean()) for k in depths},
                                      **{("BC", k): float(nres[("BC", k)].mean()) for k in depths}}
    return obs, null, ties


def s1_pooled(sub: pd.DataFrame, nulls: dict, symbols: list[str], period: str,
              rng: np.random.Generator) -> dict:
    """Pooled P(B), P(B | C_k), touch shares and exclusive bins for one period, with block-bootstrap CIs,
    the entry-weighted memoryless null, and the uptrend-minus-other differences (same resamples)."""
    p1 = P["S1"]
    depths = p1["depths_atr"]
    regimes = ["uptrend", "other"]
    bins = [(0.0, depths[0])] + [(depths[i], depths[i + 1]) for i in range(len(depths) - 1)] + [(depths[-1], np.inf)]
    blocks = calendar_blocks(sub["date"], p1["block_calendar_days"])
    cols, nums, dens = [], [], []
    for r in regimes:
        rm = (sub["regime"] == r).to_numpy()
        cols.append((r, "PB", 0.0)); nums.append(sub["B"].to_numpy() & rm); dens.append(rm)
        for k in depths:
            E = sub[f"E{k}"].to_numpy() & rm
            cols.append((r, "PBC", k)); nums.append(sub[f"BC{k}"].to_numpy() & rm); dens.append(E)
            cols.append((r, "share", k)); nums.append(E); dens.append(rm)
        for (a, b) in bins:
            if a == 0.0:
                mask = rm & ~sub[f"E{b}"].to_numpy()
                hit = sub["B"].to_numpy() & mask
            elif np.isinf(b):
                mask = rm & sub[f"E{a}"].to_numpy()
                hit = sub[f"BC{a}"].to_numpy() & mask
            else:
                mask = rm & sub[f"E{a}"].to_numpy() & ~sub[f"E{b}"].to_numpy()
                hit = sub[f"BC{a}"].to_numpy() & mask
            cols.append((r, "bin", (a, b))); nums.append(hit); dens.append(mask)
    point, reps = block_bootstrap(np.column_stack(nums), np.column_stack(dens), blocks, rng, P["n_boot"])
    lo, hi = ci_of(reps)
    dsum = np.column_stack(dens).sum(0)
    out: dict = {}
    for j, key in enumerate(cols):
        out[(period,) + key] = (point[j], lo[j], hi[j], int(dsum[j]))
    # uptrend minus other, from the same block resamples
    col_ix = {key: j for j, key in enumerate(cols)}
    for key, k in [("PB", 0.0)] + [("PBC", k) for k in depths]:
        ju, jo = col_ix[("uptrend", key, k)], col_ix[("other", key, k)]
        dl, dh = ci_of(reps[:, ju] - reps[:, jo])
        out[(period, "diff", key, k)] = (point[ju] - point[jo], float(dl), float(dh))
    # pooled memoryless null, weighting symbols by their entry counts in the cell
    for r in regimes:
        w = {s: int(((sub["symbol"] == s) & (sub["regime"] == r)).sum()) for s in symbols}
        nb = sum(w[s] * nulls[s][(period, r)]["B"] for s in w if (period, r) in nulls[s])
        nd = sum(w[s] for s in w if (period, r) in nulls[s])
        out[(period, r, "null", 0.0)] = nb / nd if nd else np.nan
        for k in depths:
            a = sum(w[s] * nulls[s][(period, r)][("BC", k)] for s in w if (period, r) in nulls[s])
            b = sum(w[s] * nulls[s][(period, r)][("E", k)] for s in w if (period, r) in nulls[s])
            out[(period, r, "null", k)] = a / b if b else np.nan
    return out


def s1_calls(pooled: dict) -> tuple[dict, dict, str]:
    """Observed-vs-null call per (period, regime, depth), breakdown-like depth per regime, and the verdict."""
    depths = P["S1"]["depths_atr"]
    regimes = ["uptrend", "other"]
    calls = {}
    for period in ["IS", "OOS"]:
        for r in regimes:
            for k in depths:
                v, lo_, hi_, _n = pooled[(period, r, "PBC", k)]
                nv = pooled[(period, r, "null", k)]
                calls[(period, r, k)] = ("below null" if hi_ < nv else "above null" if lo_ > nv else "at null")
    sc_depth = {}
    for r in regimes:
        ks = [k for k in depths if calls[("IS", r, k)] == "below null" and calls[("OOS", r, k)] == "below null"]
        sc_depth[r] = min(ks) if ks else None
    # verdict (pre-registered rule)
    shallow_all_below = all(calls[(pd_, r, depths[0])] == "below null" for pd_ in ["IS", "OOS"] for r in regimes)
    if shallow_all_below:
        verdict = "contradicts"
    elif any(v is not None for v in sc_depth.values()):
        verdict = "qualifies"
    else:
        verdict = "supports"
    return calls, sc_depth, verdict


#: S1 sensitivity (added in review): the futures series carry unadjusted roll gaps in their ATR and paths.
S1_FUTURES = ["GC=F", "CL=F"]


def s1_run() -> dict:
    log("S1: A -> C -> B ...")
    p1 = P["S1"]
    depths = p1["depths_atr"]
    rng = np.random.default_rng(P["seed"] + 1)
    frames, nulls, ties = [], {}, {}
    for sym in p1["symbols"]:
        obs, null, t = s1_symbol(sym, rng)
        frames.append(obs)
        nulls[sym] = null
        ties[sym] = t
    obs = pd.concat(frames, ignore_index=True)
    out: dict = {"obs": obs, "pooled": {}, "per_symbol": {}, "bins": {}, "ties": ties}
    regimes = ["uptrend", "other"]
    for period in ["IS", "OOS"]:
        sub = obs[obs["period"] == period]
        out["pooled"].update(s1_pooled(sub, nulls, p1["symbols"], period, rng))
        # per symbol, all regimes
        for s in p1["symbols"]:
            ss = sub[sub["symbol"] == s]
            if ss.empty:
                continue
            bl = calendar_blocks(ss["date"], p1["block_calendar_days"])
            all1 = np.ones(len(ss), bool)
            cn = [ss["B"].to_numpy(), ss["BC1.0"].to_numpy(), ss["BC2.0"].to_numpy()]
            cd = [all1, ss["E1.0"].to_numpy(), ss["E2.0"].to_numpy()]
            pt, rp = block_bootstrap(np.column_stack(cn), np.column_stack(cd), bl, rng, P["n_boot"])
            l2, h2 = ci_of(rp)
            out["per_symbol"][(s, period)] = {
                "n": len(ss), "first": ss["date"].min().date().isoformat(), "last": ss["date"].max().date().isoformat(),
                "up_share": float((ss["regime"] == "uptrend").mean()),
                "PB": (pt[0], l2[0], h2[0]), "PBC1": (pt[1], l2[1], h2[1], int(cd[1].sum())),
                "PBC2": (pt[2], l2[2], h2[2], int(cd[2].sum()))}
    # classification against the null
    calls, sc_depth, verdict = s1_calls(out["pooled"])
    out["calls"] = calls
    out["sc_depth"] = sc_depth
    out["bins_def"] = ([(0.0, depths[0])] + [(depths[i], depths[i + 1]) for i in range(len(depths) - 1)]
                       + [(depths[-1], np.inf)])
    out["n"] = {(pd_, r): int(((obs["period"] == pd_) & (obs["regime"] == r)).sum())
                for pd_ in ["IS", "OOS"] for r in regimes}
    out["nulls"] = nulls
    out["n_blocks"] = {pd_: int(len(np.unique(calendar_blocks(obs.loc[obs["period"] == pd_, "date"],
                                                                p1["block_calendar_days"]))))
                       for pd_ in ["IS", "OOS"]}
    out["verdict"] = verdict
    # sensitivity (added in review, own seed so the main numbers are unchanged): without the futures
    rng_s = np.random.default_rng(P["seed"] + 11)
    keep = [s for s in p1["symbols"] if s not in S1_FUTURES]
    sens: dict = {}
    for period in ["IS", "OOS"]:
        sub = obs[(obs["period"] == period) & obs["symbol"].isin(keep)]
        sens.update(s1_pooled(sub, nulls, keep, period, rng_s))
    s_calls, s_sc, s_verdict = s1_calls(sens)
    out["sens"] = {"symbols": keep, "pooled": sens, "calls": s_calls, "sc_depth": s_sc, "verdict": s_verdict}
    s1_chart(out)
    return out


def s1_chart(out: dict) -> None:
    depths = [0.0] + P["S1"]["depths_atr"]
    fig, axes = new_fig(2, h=3.6)
    for ax, period in zip(axes, ["IS", "OOS"]):
        for i, r in enumerate(["uptrend", "other"]):
            ys, los, his, nulls = [], [], [], []
            for k in depths:
                key = (period, r, "PB", 0.0) if k == 0 else (period, r, "PBC", k)
                v, lo, hi, _ = out["pooled"][key]
                ys.append(v); los.append(lo); his.append(hi)
                nulls.append(out["pooled"][(period, r, "null", k)])
            col = C_SERIES[i]
            ax.fill_between(depths, np.array(los) * 100, np.array(his) * 100, color=col, alpha=0.15, lw=0)
            ax.plot(depths, np.array(ys) * 100, color=col, marker="o", ms=4.5, label=f"{r}: observed")
            ax.plot(depths, np.array(nulls) * 100, color=col, ls="--", lw=1.4, label=f"{r}: memoryless null")
        span = "to 2012" if period == "IS" else "2013 on"
        ax.set_title(f"{'In-sample' if period == 'IS' else 'Out-of-sample'} ({span})")
        ax.set_xlabel("depth of the adverse move C below A (ATR)")
        ax.set_xticks(depths)
        ax.set_ylim(0, 100)
    axes[0].set_ylabel("P(reach B = A + 3 ATR within 60 days)  %")
    axes[1].legend(loc="upper right")
    return save_fig(fig, "s1_detour_curve.png")


# ---------------------------------------------------------------------------
# S2: recurrence is conditional
# ---------------------------------------------------------------------------
def s2_cells(df: pd.DataFrame, is_rows: np.ndarray) -> tuple[list[tuple[str, np.ndarray]], tuple[float, float]]:
    c = df["close"]
    rv = df["rv"]
    q1, q2 = rv[is_rows].quantile([1 / 3, 2 / 3]).to_numpy()
    vol = np.where(rv <= q1, "low vol", np.where(rv <= q2, "mid vol", "high vol"))
    reg = np.where(df["uptrend"].to_numpy(), "uptrend", "other")
    down3 = ((c < c.shift(1)) & (c.shift(1) < c.shift(2)) & (c.shift(2) < c.shift(3))).to_numpy()
    n = len(df)
    cells: list[tuple[str, np.ndarray]] = [("all days (baseline)", np.ones(n, bool))]
    ctx = []
    for r in ["uptrend", "other"]:
        for v in ["low vol", "mid vol", "high vol"]:
            ctx.append((f"{r} · {v}", (reg == r) & (vol == v)))
    cells += ctx
    cells.append(("3-down (no context)", down3))
    cells += [(f"3-down · {name}", down3 & m) for name, m in ctx]
    return cells, (float(q1), float(q2))


def classify(is_lo: float, is_hi: float, is_pt: float, o_lo: float, o_hi: float, o_pt: float) -> str:
    found = is_lo > 0 or is_hi < 0
    o_sig = o_lo > 0 or o_hi < 0
    if not found:
        return "not found IS" + (" (sig. OOS)" if o_sig else "")
    same = np.sign(o_pt) == np.sign(is_pt) and o_pt != 0
    if same:
        return "held" if o_sig else "weakened"
    return "reversed" if o_sig else "vanished"


def s2_run() -> dict:
    log("S2: conditional recurrence ...")
    p2 = P["S2"]
    H = p2["horizon"]
    rng = np.random.default_rng(P["seed"] + 2)
    res: dict = {"symbols": {}, "rows": []}
    for sym in p2["symbols"]:
        df = get(sym)
        c = df["close"]
        fwd = np.log(c.shift(-H) / c).to_numpy()
        is_ok, oos_ok = period_masks(df, H)
        valid = df["ctx_ok"].to_numpy() & df["rv"].notna().to_numpy() & np.isfinite(fwd)
        is_rows, oos_rows = valid & is_ok, valid & oos_ok
        cells, (q1, q2) = s2_cells(df, is_rows)
        stats_p: dict = {}
        for period, rows in [("IS", is_rows), ("OOS", oos_rows)]:
            r = np.where(rows, fwd, 0.0)
            blocks = calendar_blocks(df.index[rows], p2["block_calendar_days"])
            nums, dens = [], []
            for _, m in cells:
                mm = (m & rows)[rows]
                nums += [((r > 0) & m)[rows], (r * m)[rows]]
                dens += [mm, mm]
            point, reps = block_bootstrap(np.column_stack(nums), np.column_stack(dens), blocks, rng, P["n_boot"])
            nc = len(cells)
            up_pt, mean_pt = point[0::2], point[1::2]
            up_rep, mean_rep = reps[:, 0::2], reps[:, 1::2]
            d_up = up_rep - up_rep[:, [0]]
            d_mean = mean_rep - mean_rep[:, [0]]
            ul, uh = ci_of(up_rep)
            ml, mh = ci_of(mean_rep)
            dul, duh = ci_of(d_up)
            dml, dmh = ci_of(d_mean)
            stats_p[period] = {
                "n": [int((m & rows).sum()) for _, m in cells],
                "nblk": [int(len(np.unique(blocks[(m & rows)[rows]]))) for _, m in cells],
                "up": up_pt, "up_ci": (ul, uh), "mean": mean_pt, "mean_ci": (ml, mh),
                "d_up": up_pt - up_pt[0], "d_up_ci": (dul, duh),
                "d_mean": mean_pt - mean_pt[0], "d_mean_ci": (dml, dmh),
                "first": df.index[rows][0].date().isoformat(), "last": df.index[rows][-1].date().isoformat(),
                "base_up_rep": up_rep[:, 0].copy(), "base_mean_rep": mean_rep[:, 0].copy(),
            }
            assert len(stats_p[period]["n"]) == nc
        res["symbols"][sym] = {"cells": cells, "stats": stats_p, "q": (q1, q2), "fwd": fwd,
                               "is_rows": is_rows, "oos_rows": oos_rows}
        for j, (name, _) in enumerate(cells):
            if j == 0:
                continue
            si, so = stats_p["IS"], stats_p["OOS"]
            few = min(si["nblk"][j], so["nblk"][j]) < S2_MIN_BLOCKS
            res["rows"].append({
                "too_few": few,
                "symbol": sym, "cell": name, "j": j, "is_n": si["n"][j], "oos_n": so["n"][j],
                "is_mean": si["mean"][j],
                "cls_up": classify(si["d_up_ci"][0][j], si["d_up_ci"][1][j], si["d_up"][j],
                                   so["d_up_ci"][0][j], so["d_up_ci"][1][j], so["d_up"][j]),
                "cls_mean": classify(si["d_mean_ci"][0][j], si["d_mean_ci"][1][j], si["d_mean"][j],
                                     so["d_mean_ci"][0][j], so["d_mean_ci"][1][j], so["d_mean"][j]),
                "is_d_mean": si["d_mean"][j], "oos_d_mean": so["d_mean"][j],
                "is_sig_mean": si["d_mean_ci"][0][j] > 0 or si["d_mean_ci"][1][j] < 0,
            })
    # counts and verdict
    cnt = {}
    for metric in ["cls_up", "cls_mean"]:
        vals = [r[metric] for r in res["rows"] if not r["too_few"]]
        cnt[metric] = {k: sum(v == k for v in vals) for k in
                       ["held", "weakened", "vanished", "reversed", "not found IS", "not found IS (sig. OOS)"]}
        cnt[metric]["tested"] = len(vals)
        cnt[metric]["too_few"] = sum(r["too_few"] for r in res["rows"])
        cnt[metric]["found"] = sum(v in ("held", "weakened", "vanished", "reversed") for v in vals)
    res["counts"] = cnt
    found = cnt["cls_up"]["found"] + cnt["cls_mean"]["found"]
    held = cnt["cls_up"]["held"] + cnt["cls_mean"]["held"]
    lost = found - held
    if found == 0:
        verdict = "contradicts"
    elif held > 0 and lost > 0:
        verdict = "supports"
    else:
        verdict = "qualifies"
    res["verdict"] = verdict
    s2_chart(res)
    return res


def s2_chart(res: dict) -> None:
    fig, axes = new_fig(1, w=6.4, h=4.4)
    ax = axes[0]
    allv = []
    for i, sym in enumerate(P["S2"]["symbols"]):
        rows = [r for r in res["rows"] if r["symbol"] == sym and not r["too_few"]]
        x = np.array([r["is_d_mean"] for r in rows]) * 1e4
        y = np.array([r["oos_d_mean"] for r in rows]) * 1e4
        sig = np.array([r["is_sig_mean"] for r in rows])
        allv += list(x) + list(y)
        col = C_SERIES[i]
        ax.scatter(x[sig], y[sig], s=34, color=col, marker=MARKERS[i], edgecolor=C_SURF, linewidth=0.8,
                   label=f"{sym} (filled = found in-sample)", zorder=3)
        ax.scatter(x[~sig], y[~sig], s=30, facecolor="none", edgecolor=col, marker=MARKERS[i], linewidth=1.1,
                   zorder=3)
    lim = max(abs(np.nanmin(allv)), abs(np.nanmax(allv))) * 1.08
    ax.plot([-lim, lim], [-lim, lim], color=C_MUTED, ls="--", lw=1, zorder=1)
    ax.axhline(0, color=C_TEXT2, lw=0.8, zorder=1)
    ax.axvline(0, color=C_TEXT2, lw=0.8, zorder=1)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_xlabel("in-sample: cell minus baseline, mean 5-day return (bp)")
    ax.set_ylabel("out-of-sample: same difference (bp)")
    ax.set_title("Conditional differences: in-sample vs out-of-sample")
    ax.plot([], [], color=C_MUTED, ls="--", lw=1, label="difference repeated exactly")
    ax.legend(loc="upper left", fontsize=7.5)
    save_fig(fig, "s2_conditional_is_vs_oos.png")


# ---------------------------------------------------------------------------
# S7: does the best conditional cell survive costs?  (run before S3, which reuses its trades)
# ---------------------------------------------------------------------------
def nonoverlap_trades(close: np.ndarray, mask: np.ndarray, H: int, return_index: bool = False):
    out, idx, next_ok = [], [], -1
    for i in np.flatnonzero(mask):
        if i >= next_ok:
            out.append(close[i + H] / close[i] - 1.0)
            idx.append(i)
            next_ok = i + H
    return (np.array(out), np.array(idx, dtype=int)) if return_index else np.array(out)


def s7_run(s2: dict) -> dict:
    log("S7: costs ...")
    p7 = P["S7"]
    H = P["S2"]["horizon"]
    cand = [r for r in s2["rows"] if r["is_n"] >= p7["min_is_obs"]]
    best = max(cand, key=lambda r: r["is_mean"])
    sym, j = best["symbol"], best["j"]
    info = s2["symbols"][sym]
    df = get(sym)
    close = df["close"].to_numpy(float)
    name, m = info["cells"][j]
    trades, skipped = {}, {}
    for period, rows_ in [("IS", info["is_rows"]), ("OOS", info["oos_rows"])]:
        tr, ix = nonoverlap_trades(close, m & rows_, H, return_index=True)
        trades[period] = tr
        sk = np.setdiff1d(np.flatnonzero(m & rows_), ix)
        skipped[period] = close[sk + H] / close[sk] - 1.0
    bench = {"IS": nonoverlap_trades(close, info["is_rows"], H),
             "OOS": nonoverlap_trades(close, info["oos_rows"], H)}
    rows = {}
    for period in ["IS", "OOS"]:
        for cst in p7["costs_bp_per_side"]:
            net = trades[period] - 2 * cst * 1e-4
            ex = el.expectancy_from_results(net, conf=P["ci"])
            rows[(period, cst)] = ex
    be = {p: float(trades[p].mean() / 2.0) for p in trades}
    bench_ex = {p: el.expectancy_from_results(bench[p], conf=P["ci"]) for p in bench}
    ex2 = rows[("OOS", 2)]
    oos_gross = rows[("OOS", 0)]
    if oos_gross.mean <= 0 or ex2.ci_low <= 0 or be["OOS"] < 5e-4:
        verdict = "supports"
    else:
        verdict = "qualifies"
    out = {"symbol": sym, "cell": name, "j": j, "trades": trades, "skipped": skipped, "bench": bench, "rows": rows,
           "breakeven": be, "bench_ex": bench_ex, "verdict": verdict, "best": best,
           "n_candidates": len(cand)}
    s7_chart(out)
    return out


def s7_chart(out: dict) -> None:
    fig, axes = new_fig(1, w=6.4, h=3.6)
    ax = axes[0]
    xs = np.linspace(0, max(P["S7"]["costs_bp_per_side"]), 101)
    for i, period in enumerate(["IS", "OOS"]):
        tr = out["trades"][period]
        n = len(tr)
        mean, sd = tr.mean(), tr.std(ddof=1)
        tcrit = stats.t.ppf(0.5 + P["ci"] / 2, n - 1)
        ys = (mean - 2 * xs * 1e-4) * 1e4
        half = tcrit * sd / math.sqrt(n) * 1e4
        col = C_SERIES[i]
        ax.fill_between(xs, ys - half, ys + half, color=col, alpha=0.13, lw=0)
        ax.plot(xs, ys, color=col, ls="-" if period == "OOS" else "--",
                label=f"{'out-of-sample' if period == 'OOS' else 'in-sample (selection data)'}, n = {n}")
        pts = np.array(P["S7"]["costs_bp_per_side"])
        ax.plot(pts, (mean - 2 * pts * 1e-4) * 1e4, ls="none", marker="o", ms=4.5, color=col)
    ax.axhline(0, color=C_TEXT2, lw=0.9)
    ax.set_xlabel("cost per side (bp); a round trip pays it twice")
    ax.set_ylabel("expectancy per 5-day trade (bp)")
    ax.set_title(f"Best in-sample cell: {out['symbol']} · {out['cell']}")
    ax.legend(loc="upper right")
    save_fig(fig, "s7_costs.png")


# ---------------------------------------------------------------------------
# S3: the law of large numbers
# ---------------------------------------------------------------------------
def s3_run(s7: dict) -> dict:
    log("S3: law of large numbers ...")
    p3 = P["S3"]
    p, b, c = p3["p_win"], p3["reward_risk"], p3["cost_r"]
    rng = np.random.default_rng(P["seed"] + 3)
    rows = []
    sims = {}
    for n in p3["n_trades"]:
        W = rng.binomial(n, p, size=p3["n_samples"])
        wr = W / n
        exp_r = wr * b - (1 - wr) - c
        thr_loser = math.floor(n * (1 + c) / (1 + b) + 1e-9)       # expectancy <= 0  <=>  W <= thr
        thr_star = math.ceil(0.70 * n - 1e-9)                      # win rate >= 70%
        rows.append({
            "n": n, "wr_q": np.percentile(wr, [2.5, 50, 97.5]), "exp_q": np.percentile(exp_r, [2.5, 50, 97.5]),
            "loser_sim": float(np.mean(exp_r <= 1e-12)), "loser_exact": float(stats.binom.cdf(thr_loser, n, p)),
            "star_sim": float(np.mean(wr >= 0.70 - 1e-12)), "star_exact": float(stats.binom.sf(thr_star - 1, n, p)),
        })
        sims[n] = wr
    plan = el.trades_needed(p, b, c, conf=P["ci"], power=0.8)
    true_ev = el.expected_value(p, b, 1.0, c)
    # empirical cell (S7 selection)
    emp = {}
    for period in ["IS", "OOS"]:
        tr = s7["trades"][period]
        n = len(tr)
        wins = int((tr > 0).sum())
        lo, hi = el.wilson_interval(wins, n, P["ci"])
        post = el.beta_posterior(wins, n, threshold=0.5, conf=P["ci"])
        ex = el.expectancy_from_results(tr, conf=P["ci"])
        z_a, z_b = stats.norm.ppf(0.5 + P["ci"] / 2), stats.norm.ppf(0.8)
        n_need = math.ceil(((z_a + z_b) * ex.sd / ex.mean) ** 2) if ex.mean > 0 else math.inf
        emp[period] = {"n": n, "wins": wins, "wr": wins / n if n else np.nan, "wilson": (lo, hi), "post": post,
                       "ex": ex, "n_need": n_need}
    small = [r for r in rows if r["n"] <= 100]
    verdict = "supports" if (min(r["loser_exact"] for r in small) >= 0.10 and plan.n_expectancy > 100) \
        else "qualifies"
    out = {"rows": rows, "plan": plan, "true_ev": true_ev, "emp": emp, "verdict": verdict}
    s3_chart(out, sims)
    return out


def s3_chart(out: dict, sims: dict) -> None:
    fig, axes = new_fig(1, w=6.4, h=3.6)
    ax = axes[0]
    ns = list(sims)
    xs = np.arange(len(ns))
    for i, n in enumerate(ns):
        q = np.percentile(sims[n], [2.5, 25, 50, 75, 97.5]) * 100
        ax.plot([i, i], [q[0], q[4]], color=C_SERIES[0], lw=2, solid_capstyle="round")
        ax.plot([i, i], [q[1], q[3]], color=C_SERIES[0], lw=7, solid_capstyle="butt", alpha=0.55)
        ax.plot(i, q[2], marker="o", color=C_SERIES[0], ms=5, markeredgecolor=C_SURF)
    p3 = P["S3"]
    be = (1 + p3["cost_r"]) / (1 + p3["reward_risk"]) * 100
    ax.axhline(p3["p_win"] * 100, color=C_SERIES[2], lw=1.4, label=f"true win rate {p3['p_win']:.0%}")
    ax.axhline(be, color=C_SERIES[1], lw=1.4, ls="--", label=f"breakeven after costs {be:.1f}%")
    ax.axhline(70, color=C_TEXT2, lw=1, ls=":", label="70%: 'looks like a star'")
    ax.set_xticks(xs, [str(n) for n in ns])
    ax.set_xlabel("number of trades in the sample")
    ax.set_ylabel("observed win rate (%)")
    ax.set_title("Same true edge, different samples: middle 50% (thick) and 95% (thin)")
    ax.legend(loc="upper right")
    save_fig(fig, "s3_law_of_large_numbers.png")


# ---------------------------------------------------------------------------
# S4: streaks and ruin
# ---------------------------------------------------------------------------
def s4_run() -> dict:
    log("S4: streaks and ruin ...")
    p4 = P["S4"]
    out: dict = {"sims": {}, "streaks": {}, "kelly": {}, "ev": {}}
    k = 0
    for p, b in p4["strategies"]:
        out["ev"][(p, b)] = p * b - (1 - p) - p4["cost_r"]
        out["kelly"][(p, b)] = el.kelly_fraction(p, b, p4["cost_r"])
        for s in p4["streaks"]:
            out["streaks"][(p, b, s)] = el.prob_losing_streak(1 - p, s, p4["n_trades"])
        for f in p4["risk_per_trade"]:
            sim = el.simulate_equity(p, b, f, p4["n_trades"], p4["n_paths"], cost_r=p4["cost_r"],
                                     ruin_drawdown=p4["ruin_drawdown"], seed=P["seed"] + 400 + k)
            k += 1
            out["sims"][(p, b, f)] = sim.summary()
    out["recovery"] = {L: el.recovery_required(L) for L in p4["recovery_losses"]}
    hi_f, one = max(p4["risk_per_trade"]), 0.01
    ok = [(p, b) for p, b in p4["strategies"]
          if out["sims"][(p, b, hi_f)]["prob_ruin"] >= 0.25 and out["sims"][(p, b, one)]["prob_ruin"] <= 0.01]
    out["verdict"] = "supports" if ok else "qualifies"
    s4_chart(out)
    return out


def s4_chart(out: dict) -> None:
    p4 = P["S4"]
    fig, axes = new_fig(2, h=3.5)
    fs = np.array(p4["risk_per_trade"]) * 100
    for i, (p, b) in enumerate(p4["strategies"]):
        col = C_SERIES[i]
        lab = f"p = {p:.2f}, {b:g}R (EV {out['ev'][(p, b)]:+.3f}R)"
        ruin = [out["sims"][(p, b, f)]["prob_ruin"] * 100 for f in p4["risk_per_trade"]]
        med = [out["sims"][(p, b, f)]["final_equity_median"] for f in p4["risk_per_trade"]]
        axes[0].plot(fs, ruin, color=col, marker=MARKERS[i], ms=5, label=lab)
        axes[1].plot(fs, med, color=col, marker=MARKERS[i], ms=5, label=lab)
    for ax in axes:
        ax.set_xscale("log")
        ax.set_xticks(fs, [f"{x:g}%" for x in fs])
        ax.minorticks_off()
        ax.set_xlabel("risk per trade (% of equity)")
    axes[0].set_ylabel("P(drawdown ≥ 50%) in 250 trades  (%)")
    axes[0].set_title("Same positive-EV edges, different bet sizes")
    axes[1].set_yscale("log")
    axes[1].axhline(1.0, color=C_TEXT2, lw=0.9)
    axes[1].set_ylabel("median final equity (start = 1)")
    axes[1].set_title("Median outcome after 250 trades")
    axes[0].legend(loc="upper left")
    save_fig(fig, "s4_ruin.png")


# ---------------------------------------------------------------------------
# S5: overfitting
# ---------------------------------------------------------------------------
def s5_variants() -> list[tuple]:
    p5 = P["S5"]
    v: list[tuple] = []
    for mode in p5["modes"]:
        for s in p5["ma_cross_slow"]:
            for f in p5["ma_cross_fast"]:
                if f < s:
                    v.append(("SMA cross", f, s, mode))
        for n in p5["price_vs_ma"]:
            v.append(("close vs SMA", n, None, mode))
        for L in p5["momentum_lookback"]:
            v.append(("momentum", L, None, mode))
    for N in p5["donchian_entry"]:
        for M in p5["donchian_exit"]:
            if M < N:
                v.append(("Donchian", N, M, "long/flat"))
    for N in p5["donchian_entry"]:
        v.append(("Donchian", N, None, "long/short"))
    return v


def s5_name(v: tuple) -> str:
    kind, a, b, mode = v
    if kind == "SMA cross":
        return f"SMA {a}/{b} cross, {mode}"
    if kind == "close vs SMA":
        return f"close vs SMA {a}, {mode}"
    if kind == "momentum":
        return f"{a}-day momentum, {mode}"
    if b is None:
        return f"Donchian {a}-day stop-and-reverse, {mode}"
    return f"Donchian {a}-day entry / {b}-day exit, {mode}"


def s5_positions(c: np.ndarray, variants: list[tuple]) -> np.ndarray:
    s = pd.Series(c)
    p5 = P["S5"]
    sma = {w: s.rolling(w).mean().to_numpy() for w in set(p5["ma_cross_fast"]) | set(p5["ma_cross_slow"])
           | set(p5["price_vs_ma"])}
    prior = s.shift(1)
    pmax = {N: prior.rolling(N).max().to_numpy() for N in p5["donchian_entry"]}
    pmin = {M: prior.rolling(M).min().to_numpy() for M in set(p5["donchian_exit"]) | set(p5["donchian_entry"])}
    lag = {L: s.shift(L).to_numpy() for L in p5["momentum_lookback"]}
    out = np.zeros((len(variants), len(c)))
    for i, (kind, a, b, mode) in enumerate(variants):
        if kind == "Donchian":
            up = c > pmax[a]
            if b is None:
                ev = np.where(up, 1.0, np.where(c < pmin[a], -1.0, np.nan))
            else:
                ev = np.where(up, 1.0, np.where(c < pmin[b], 0.0, np.nan))
            out[i] = pd.Series(ev).ffill().fillna(0.0).to_numpy()
            continue
        if kind == "SMA cross":
            ref, x = sma[b], sma[a]
        elif kind == "close vs SMA":
            ref, x = sma[a], c
        else:
            ref, x = lag[a], c
        defined = np.isfinite(ref) & np.isfinite(x)
        up = np.where(defined, x > ref, False)
        pos = np.where(up, 1.0, 0.0 if mode == "long/flat" else -1.0)
        out[i] = np.where(defined, pos, 0.0)
    return out


def s5_net(pos: np.ndarray, r: np.ndarray, cost: float) -> np.ndarray:
    dpos = np.abs(np.diff(pos, axis=1, prepend=0.0))
    net = np.zeros_like(pos)
    net[:, 1:] = pos[:, :-1] * r[None, 1:] - cost * dpos[:, :-1]
    return net


def sr_rows(x: np.ndarray) -> np.ndarray:
    with np.errstate(invalid="ignore", divide="ignore"):
        return x.mean(axis=1) / x.std(axis=1, ddof=1)


def s5_run() -> dict:
    log("S5: overfitting ...")
    p5 = P["S5"]
    df = get(p5["symbol"])
    c = df["close"].to_numpy(float)
    dates = df.index
    n = len(c)
    r = np.zeros(n)
    r[1:] = c[1:] / c[:-1] - 1
    i_is_end = int(np.searchsorted(dates.values, np.datetime64(P["is_end"]), side="right")) - 1
    i_oos0 = int(np.searchsorted(dates.values, np.datetime64(P["oos_start"]), side="left"))
    w0 = p5["warmup_bars"]
    is_sl, oos_sl = slice(w0, i_is_end + 1), slice(i_oos0, n)
    cost = p5["cost_bp_per_side"] * 1e-4
    variants = s5_variants()
    nv = len(variants)
    pos = s5_positions(c, variants)
    net = s5_net(pos, r, cost)
    sr_is = sr_rows(net[:, is_sl])
    sr_oos = sr_rows(net[:, oos_sl])
    ann = math.sqrt(252)
    win = int(np.nanargmax(sr_is))
    m = el.return_moments(net[win, is_sl])
    sr_var = float(np.nanvar(sr_is, ddof=1))
    dsr = el.deflated_sharpe_ratio(m["sr"], int(m["n"]), m["skew"], m["kurt"], nv, sr_var)
    psr = el.probabilistic_sharpe_ratio(m["sr"], int(m["n"]), m["skew"], m["kurt"])
    sr0 = el.expected_max_sharpe(nv, sr_var)
    bh_is = el.sharpe_ratio(r[is_sl], 252)
    bh_oos = el.sharpe_ratio(r[oos_sl], 252)
    oos_rank = int((sr_oos > sr_oos[win]).sum()) + 1
    rho = float(stats.spearmanr(sr_is, sr_oos, nan_policy="omit").statistic)
    top = np.argsort(-sr_is)[:5]
    # shuffled copies: in-sample returns permuted (no serial structure, same distribution)
    rng = np.random.default_rng(P["seed"] + 5)
    shuf = []
    for k in range(p5["n_shuffles"]):
        rs = r.copy()
        rs[1:i_is_end + 1] = rng.permutation(r[1:i_is_end + 1])
        cs = c[0] * np.cumprod(1 + rs)
        ps = s5_positions(cs[: i_is_end + 1], variants)
        ns = s5_net(ps, rs[: i_is_end + 1], cost)
        s_is = sr_rows(ns[:, is_sl])
        bw = int(np.nanargmax(s_is))
        ms = el.return_moments(ns[bw, is_sl])
        sv = float(np.nanvar(s_is, ddof=1))
        shuf.append({"best": float(s_is[bw] * ann), "rule": s5_name(variants[bw]),
                     "median": float(np.nanmedian(s_is) * ann),
                     "bh": el.sharpe_ratio(rs[is_sl], 252),
                     "dsr": el.deflated_sharpe_ratio(ms["sr"], int(ms["n"]), ms["skew"], ms["kurt"], nv, sv),
                     "psr": el.probabilistic_sharpe_ratio(ms["sr"], int(ms["n"]), ms["skew"], ms["kurt"])})
    best_shuf = np.array([s["best"] for s in shuf])
    perm_p = (1 + int((best_shuf >= sr_is[win] * ann).sum())) / (1 + len(shuf))
    out = {
        "n_variants": nv, "winner": s5_name(variants[win]), "sr_is": sr_is * ann, "sr_oos": sr_oos * ann,
        "win": win, "win_is": float(sr_is[win] * ann), "win_oos": float(sr_oos[win] * ann),
        "dsr": dsr, "psr": psr, "sr0_ann": sr0 * ann, "bh_is": bh_is, "bh_oos": bh_oos, "oos_rank": oos_rank,
        "rho": rho, "top": [(s5_name(variants[t]), float(sr_is[t] * ann), float(sr_oos[t] * ann)) for t in top],
        "median_is": float(np.nanmedian(sr_is) * ann), "median_oos": float(np.nanmedian(sr_oos) * ann),
        "share_oos_beat_bh": float(np.nanmean(sr_oos * ann > bh_oos)),
        "shuf": shuf, "perm_p": perm_p, "is_span": (dates[w0].date(), dates[i_is_end].date()),
        "oos_span": (dates[i_oos0].date(), dates[n - 1].date()), "n_is": i_is_end + 1 - w0, "n_oos": n - i_oos0,
        "win_moments": m,
    }
    a = out["win_oos"] < 0.5 * out["win_is"]
    bdsr = dsr < 0.95
    cperm = perm_p >= 0.05
    out["verdict_parts"] = {"oos_below_half": a, "dsr_below_95": bdsr, "perm_p_ge_05": cperm}
    out["verdict"] = "supports" if (a or bdsr or cperm) else "qualifies"
    s5_chart(out)
    return out


def s5_chart(out: dict) -> None:
    fig, axes = new_fig(2, h=3.6)
    ax = axes[0]
    ax.hist(out["sr_is"], bins=30, color=C_SERIES[0], alpha=0.75, edgecolor=C_SURF, linewidth=0.6,
            label=f"{out['n_variants']} rule variants (real data)")
    best_sh = [s["best"] for s in out["shuf"]]
    ymax = ax.get_ylim()[1]
    ax.plot(best_sh, np.full(len(best_sh), ymax * 0.06), ls="none", marker="|", ms=14, mew=1.6,
            color=C_SERIES[1], label="best rule on each shuffled copy")
    ax.axvline(out["win_is"], color=C_TEXT, lw=1.4, label="best rule on real data")
    ax.axvline(out["bh_is"], color=C_SERIES[2], lw=1.4, ls="--", label="buy and hold")
    ax.set_xlabel("in-sample Sharpe (annualised, net of 1 bp per side)")
    ax.set_ylabel("number of variants")
    ax.yaxis.set_major_locator(matplotlib.ticker.MaxNLocator(integer=True))
    ax.set_title("Selection: the best of many")
    ax.legend(loc="upper left", fontsize=7)
    ax = axes[1]
    ax.scatter(out["sr_is"], out["sr_oos"], s=14, color=C_MUTED, edgecolor="none", label="each variant")
    ax.scatter([out["win_is"]], [out["win_oos"]], s=60, color=C_SERIES[0], edgecolor=C_SURF, zorder=3,
               label="in-sample winner")
    ax.scatter([out["bh_is"]], [out["bh_oos"]], s=50, marker="D", color=C_SERIES[2], edgecolor=C_SURF, zorder=3,
               label="buy and hold")
    ax.axhline(0, color=C_TEXT2, lw=0.8)
    ax.set_xlabel("in-sample Sharpe")
    ax.set_ylabel("out-of-sample Sharpe")
    ax.set_title("Does in-sample rank carry over?")
    ax.legend(loc="lower right", fontsize=7)
    save_fig(fig, "s5_overfitting.png")


# ---------------------------------------------------------------------------
# S6: decision quality vs outcome
# ---------------------------------------------------------------------------
def s6_probs(p: float, win: float, loss: float, cost: float, n: int) -> tuple[float, float]:
    """Exact P(total < 0) and P(total > 0) after n independent trades."""
    w = np.arange(n + 1)
    total = w * (win - cost) - (n - w) * (loss + cost)
    pmf = stats.binom.pmf(w, n, p)
    return float(pmf[total < 0].sum()), float(pmf[total > 0].sum())


def s6_run() -> dict:
    log("S6: decision vs outcome ...")
    p6 = P["S6"]
    p, win, loss, cost, q = p6["p_win"], p6["win"], p6["loss"], p6["cost"], p6["twin_p_win"]
    rng = np.random.default_rng(P["seed"] + 6)
    rows = []
    for n in p6["n_trades"]:
        down, _ = s6_probs(p, win, loss, cost, n)
        _, up_twin = s6_probs(q, win, loss, cost, n)
        W = rng.binomial(n, p, p6["n_sims"])
        Wt = rng.binomial(n, q, p6["n_sims"])
        tot = W * (win - cost) - (n - W) * (loss + cost)
        tott = Wt * (win - cost) - (n - Wt) * (loss + cost)
        rows.append({"n": n, "down": down, "down_sim": float(np.mean(tot < 0)), "up_twin": up_twin,
                     "up_twin_sim": float(np.mean(tott > 0))})
    curve_n = np.unique(np.round(np.logspace(0, math.log10(2000), 120)).astype(int))
    curve = [(int(n), *s6_probs(p, win, loss, cost, int(n))[:1], s6_probs(q, win, loss, cost, int(n))[1])
             for n in curve_n]

    def first_below(fn, level):
        for n in range(1, 5001):
            if fn(n) < level:
                return n
        return None

    def stays_below(fn, level, n_max=5000):
        """Smallest n from which fn stays below level up to n_max (the curves zigzag)."""
        last = None
        for n in range(1, n_max + 1):
            if fn(n) >= level:
                last = n
        return None if last is None else (last + 1 if last < n_max else None)

    f_down = lambda n: s6_probs(p, win, loss, cost, n)[0]  # noqa: E731
    f_up = lambda n: s6_probs(q, win, loss, cost, n)[1]  # noqa: E731
    n_down5, n_up5 = first_below(f_down, 0.05), first_below(f_up, 0.05)
    out = {"rows": rows, "ev": el.expected_value(p, win, loss, cost), "ev_twin": el.expected_value(q, win, loss, cost),
           "n_down5": n_down5, "n_up5": n_up5, "n_down5_stay": stays_below(f_down, 0.05),
           "n_up5_stay": stays_below(f_up, 0.05), "curve": curve}
    r20 = [r for r in rows if r["n"] == 20][0]
    out["verdict"] = "supports" if (r20["down"] >= 0.2 and r20["up_twin"] >= 0.2) else "qualifies"
    s6_chart(out)
    return out


def s6_chart(out: dict) -> None:
    fig, axes = new_fig(1, w=6.4, h=3.6)
    ax = axes[0]
    n = np.array([c[0] for c in out["curve"]])
    ax.plot(n, np.array([c[1] for c in out["curve"]]) * 100, color=C_SERIES[0], lw=1.5,
            label=f"+EV strategy (EV {out['ev']:+.0f} $/trade): P(behind)")
    ax.plot(n, np.array([c[2] for c in out["curve"]]) * 100, color=C_SERIES[1], lw=1.5,
            label=f"−EV twin (EV {out['ev_twin']:+.0f} $/trade): P(ahead)")
    ax.axhline(5, color=C_TEXT2, lw=0.9, ls=":")
    ax.set_xscale("log")
    ax.set_xlabel("number of trades")
    ax.set_ylabel("probability (%)")
    ax.set_ylim(0, 65)
    ax.set_title("Outcomes mislead for a long time (exact binomial)")
    ax.legend(loc="upper right")
    save_fig(fig, "s6_decision_vs_outcome.png")


# ---------------------------------------------------------------------------
# report
# ---------------------------------------------------------------------------
FRONTMATTER = """---
id: synthesis_evidence_lab
type: synthesis
title: "Evidence Lab — testing the Philosophy of the Relationship on real market data"
partition: 00_philosophy
layer: L8
related: [philosophy_relationship, philo_conditional_probability, philo_acb_principle, philo_capital_preservation, philo_scientific_method, philo_being_wrong, philo_open_questions]
uses: [concept_expectancy, concept_probabilistic_thinking, concept_market_regimes, concept_overfitting_validation, concept_risk_of_ruin_drawdown, concept_backtesting, concept_volatility]
status: computed
---
"""


def params_source() -> str:
    lines = Path(__file__).read_text(encoding="utf-8").splitlines()
    a = next(i for i, ln in enumerate(lines) if ln.startswith("# --- PARAMS"))
    b = next(i for i, ln in enumerate(lines) if ln.startswith("# --- end PARAMS"))
    return "\n".join(lines[a:b + 1])


def verdict_word(v: str) -> str:
    return {"supports": "Supports", "qualifies": "Qualifies", "contradicts": "Contradicts"}[v]


def report_s1(s1: dict, fig: str) -> tuple[list[str], str]:
    p1 = P["S1"]
    depths = p1["depths_atr"]
    L: list[str] = []
    L += ["## S1 — A → C → B: is an adverse move a detour or a breakdown?", ""]
    L += ["**Claim tested.** Section III ([[philo_acb_principle]]) says price may travel from A to C, against "
          "the hypothesis, before reaching B; the intermediate move *may* be consistent with the larger "
          "hypothesis, yet B is only a hypothesis and not every adverse move is a detour. Principles 2 and 3 "
          "([[principle_02_context_before_movement]], [[principle_03_future_is_uncertain]]) turn this into "
          "practice: read a move in its context, and treat the destination as uncertain. Testable form: "
          "(a) touching C should lower, not erase, the chance of reaching B; (b) the context at A (here, the "
          "trend regime) should shape the curve; and the question the study must answer, (c): at what depth, "
          "if any, does the adverse move carry information of its own, i.e. behave like a change in structure "
          "rather than a detour?", ""]
    L += [f"**Design.** Every trading day t is an entry A = close[t]. B = A + {p1['target_atr']:g} × ATR14[t] "
          f"(Wilder's ATR, [[person_welles_wilder]]; [[concept_volatility]]); horizon {p1['horizon']} trading "
          f"days. C_k = A − k × ATR14[t] for k = {', '.join(f'{k:g}' for k in depths)}. The conditional "
          "probability is the one a trader can use in real time: *given that price has touched C_k before "
          "touching B, how often was B still reached within the original horizon?* If C_k and B fall on the "
          "same daily bar, the adverse move is assumed to come first and that bar does not count as reaching "
          "B (conservative against the claim). Regime at A ([[concept_market_regimes]]): *uptrend* = close > "
          "SMA200 and SMA50 > SMA200, otherwise *other*. Uncertainty: entries overlap heavily, so 95% CIs come "
          f"from a block bootstrap that resamples {p1['block_calendar_days']}-day calendar blocks of all five "
          "markets together (preserving the overlap and the cross-market correlation).", ""]
    L += ["**The yardstick.** P(B) falls with depth for pure geometry: from C_k the target is (3 + k) ATR "
          "away and less time is left. So a falling curve alone says nothing about a change in structure. "
          f"Each curve is compared with a *memoryless null*: {p1['horizon']}-day paths built from the same market's own "
          "days (close, high and low changes divided by the prior ATR), drawn at random from the same "
          "period and regime. The null keeps each market's drift, volatility and fat tails but has no memory, "
          "so in it an adverse move carries no information about what follows. Observed below the null = the "
          "detour carried bad news beyond geometry (breakdown-like); at the null = geometry only; above = "
          "adverse moves were followed by more recovery than chance (detour-like).", ""]
    rows = []
    for s in p1["symbols"]:
        for period in ["IS", "OOS"]:
            d = s1["per_symbol"].get((s, period))
            if d:
                rows.append([f"`{s}`", period, f"{d['first']} → {d['last']}", f"{d['n']:,}", pct(d["up_share"], 0)])
    L += [f"**Data.** Entries per market and period (the IS window ends {p1['horizon']} trading days before "
          "2013 so no in-sample outcome uses 2013 data):", ""]
    L += table(["market", "period", "entries", "n", "share in uptrend"], rows)
    for period, title in [("IS", "In-sample"), ("OOS", "Out-of-sample")]:
        nu, no = s1["n"][(period, "uptrend")], s1["n"][(period, "other")]
        L += [f"**{title}, five markets pooled** (uptrend n = {nu:,}; other n = {no:,}). "
              "*Touched* = share of entries whose path touched C_k before B. P(B | C_k) with 95% block-bootstrap "
              "CI, the memoryless null, and the comparison.", ""]
        rows = []
        for k in [0.0] + depths:
            row = ["unconditional" if k == 0 else f"C at −{k:g} ATR"]
            for r in ["uptrend", "other"]:
                if k == 0:
                    v, lo, hi, _ = s1["pooled"][(period, r, "PB", 0.0)]
                    row += ["—", f"{pct(v)} {ci_pct(lo, hi)}", pct(s1["pooled"][(period, r, "null", 0.0)]), ""]
                else:
                    sh = s1["pooled"][(period, r, "share", k)][0]
                    v, lo, hi, nE = s1["pooled"][(period, r, "PBC", k)]
                    row += [pct(sh), f"{pct(v)} {ci_pct(lo, hi)}", pct(s1["pooled"][(period, r, "null", k)]),
                            s1["calls"][(period, r, k)]]
            rows.append(row)
        L += table(["depth", "up: touched", "up: P(B) [95% CI]", "up: null", "up: vs null",
                    "other: touched", "other: P(B) [95% CI]", "other: null", "other: vs null"], rows)
    L += [f"![S1 detour curve]({fig})", ""]
    # bins
    L += ["**The hindsight trap (exclusive bins).** The same entries cut by the *deepest* excursion reached "
          "before B (for paths that never reach B, the deepest point of the whole window). Read this way, "
          "detours look almost harmless until 2 ATR, but the reading is circular: a path that never reaches B "
          f"has {p1['horizon']} days to sink, so it almost always lands in the deepest bin, and the shallow bins are left "
          "with the winners. The deepest point is known only afterwards. The real-time tables above are the "
          "ones a decision can use; this one shows how hindsight flatters a hypothesis.", ""]
    rows = []
    for (a, b) in s1["bins_def"]:
        lab = f"{a:g}–{b:g} ATR" if np.isfinite(b) else f"≥ {a:g} ATR"
        row = [lab]
        for period in ["IS", "OOS"]:
            for r in ["uptrend", "other"]:
                v, lo, hi, nn = s1["pooled"][(period, r, "bin", (a, b))]
                row.append(f"{pct(v, 0)} (n {nn:,})")
        rows.append(row)
    L += table(["deepest excursion before B", "IS uptrend", "IS other", "OOS uptrend", "OOS other"], rows)
    rows = []
    for s in p1["symbols"]:
        for period in ["IS", "OOS"]:
            d = s1["per_symbol"].get((s, period))
            if not d:
                continue
            rows.append([f"`{s}`", period, f"{pct(d['PB'][0])} {ci_pct(d['PB'][1], d['PB'][2])}",
                         f"{pct(d['PBC1'][0])} {ci_pct(d['PBC1'][1], d['PBC1'][2])} (n {d['PBC1'][3]:,})",
                         f"{pct(d['PBC2'][0])} {ci_pct(d['PBC2'][1], d['PBC2'][2])} (n {d['PBC2'][3]:,})"])
    L += ["**Per market (both regimes together).**", ""]
    L += table(["market", "period", "P(B) [95% CI]", "P(B \\| C at −1 ATR) [95% CI]",
                "P(B \\| C at −2 ATR) [95% CI]"], rows)
    tie_total = sum(sum(t.values()) for t in s1["ties"].values())
    L += [f"Same-bar ties (C_k and B on one bar), all depths and markets: {tie_total:,}; they were resolved "
          "against the claim as stated above.", ""]
    # verdict
    sc = s1["sc_depth"]
    parts = []
    for r in ["uptrend", "other"]:
        if sc[r] is None:
            parts.append(f"in the *{r}* regime no tested depth (up to {depths[-1]:g} ATR) fell below the "
                         "memoryless null in both periods")
        else:
            parts.append(f"in the *{r}* regime, excursions of {sc[r]:g} ATR or more fell below the memoryless "
                         "null in both periods")
    u1 = s1["pooled"][("OOS", "uptrend", "PBC", 1.0)][0]
    u0 = s1["pooled"][("OOS", "uptrend", "PB", 0.0)][0]
    o1 = s1["pooled"][("OOS", "other", "PBC", 1.0)][0]
    o0 = s1["pooled"][("OOS", "other", "PB", 0.0)][0]
    kd = depths[-1]
    u3 = s1["pooled"][("OOS", "uptrend", "PBC", kd)][0]
    o3 = s1["pooled"][("OOS", "other", "PBC", kd)][0]

    def gap(period: str, r: str) -> tuple[float, float]:
        g = [s1["pooled"][(period, r, "PBC", k)][0] - s1["pooled"][(period, r, "null", k)] for k in depths]
        return min(g), max(g)

    above = [f"{pd_} {r} at {k:g} ATR" for (pd_, r, k), c in s1["calls"].items() if c == "above null"]
    below = [f"{pd_} {r} at {k:g} ATR" for (pd_, r, k), c in s1["calls"].items() if c == "below null"]
    n_cmp = len(s1["calls"])
    go_is, go_oos, gu_oos = gap("IS", "other"), gap("OOS", "other"), gap("OOS", "uptrend")
    ctx_all = all(s1["pooled"][(pd_, "uptrend", key, k)][0] > s1["pooled"][(pd_, "other", key, k)][0]
                  for pd_ in ["IS", "OOS"] for key, k in [("PB", 0.0)] + [("PBC", k) for k in depths])
    pooled = s1["pooled"]
    d0, dk = pooled[("OOS", "diff", "PB", 0.0)], pooled[("OOS", "diff", "PBC", kd)]
    n0 = pooled[("OOS", "uptrend", "null", 0.0)] - pooled[("OOS", "other", "null", 0.0)]
    nk = pooled[("OOS", "uptrend", "null", kd)] - pooled[("OOS", "other", "null", kd)]
    diff_clear = [f"{pd_} {'unconditional' if k == 0 else f'{k:g} ATR'}"
                  for pd_ in ["IS", "OOS"] for key, k in [("PB", 0.0)] + [("PBC", k) for k in depths]
                  if pooled[(pd_, "diff", key, k)][1] > 0]
    sens = s1["sens"]
    s_above = [f"{pd_} {r} at {k:g} ATR" for (pd_, r, k), c in sens["calls"].items() if c == "above null"]
    s_below = [f"{pd_} {r} at {k:g} ATR" for (pd_, r, k), c in sens["calls"].items() if c == "below null"]
    if all(v is None for v in sc.values()):
        depth_txt = ("**No depth behaved like structural change** in either regime: up to "
                     f"{kd:g} ATR, the observed curve never sat clearly below (in both periods) what a memoryless "
                     "market with the same drift and volatility produces. The decline of P(B) with depth is, "
                     "within the precision of these data, geometry: farther to go and less time to get there.")
    else:
        depth_txt = "Breakdown-like depths (below the null in both periods): " + "; ".join(
            f"{r} from {sc[r]:g} ATR" for r in sc if sc[r] is not None) + "."
    L += [f"**Verdict: {verdict_word(s1['verdict'])}** (pre-registered rule: " + "; ".join(parts) + "). "
          f"An adverse move weakens the hypothesis without settling it. Out-of-sample, a 1-ATR detour took "
          f"P(B) from {pct(u0)} to {pct(u1)} in uptrends and from {pct(o0)} to {pct(o1)} otherwise; even after "
          f"a {kd:g}-ATR detour, B was still reached {pct(u3)} of the time in uptrends ({pct(o3)} otherwise). "
          + depth_txt + " "
          + ("The regime at A shifts the whole curve: at every depth and in both periods the uptrend point "
             "estimate sits above the other-regime one, " if ctx_all else "The regime curves differ but cross at "
             "some depth; ")
          + f"out-of-sample by {pp(d0[0], 0)} points {ci_pct(d0[1], d0[2], 0, True)} unconditionally and "
          f"{pp(dk[0], 0)} points {ci_pct(dk[1], dk[2], 0, True)} at {kd:g} ATR (95% CIs of the difference, "
          "same block resamples; "
          + (f"the interval excludes zero at {len(diff_clear)} of {2 * (len(depths) + 1)} period-depth points). "
             if diff_clear else "no interval excludes zero). ")
          + f"The memoryless nulls differ by {pp(n0, 0)} and {pp(nk, 0)} points at the same two places, so "
          + ("most of that gap is what the different drift and volatility of uptrend and other-regime days "
             "produce, not extra information carried by the detour. "
             if min(n0 / d0[0], nk / dk[0]) >= 2 / 3 else
             f"unconditionally {n0 / d0[0]:.0%} of the gap is what the different drift and volatility of the "
             f"two regimes' days produce, but at {kd:g} ATR only {nk / dk[0]:.0%}; the remainder comes from "
             "uptrend paths running above their null after deep detours and other-regime paths running below "
             "theirs, which is suggestive only (see the next sentences). ")
          + "Softer signals, mostly inside the CIs: observed "
          f"minus null ranged from {pp(go_is[0], 0, True)} to {pp(go_is[1], 0, True)} points in-sample and from "
          f"{pp(go_oos[0], 0, True)} to {pp(go_oos[1], 0, True)} out-of-sample in the *other* regime"
          + (" (adverse moves there leaned towards bad news, but these ten numbers are nested and strongly "
             "correlated, not ten independent signs)" if max(go_is[1], go_oos[1]) < 0 else "")
          + f", and from {pp(gu_oos[0], 0, True)} to "
          f"{pp(gu_oos[1], 0, True)} for out-of-sample uptrends"
          + (f"; single-period CIs clear of the null: above at {', '.join(above)}" if above else "")
          + (f"; below at {', '.join(below)}" if below else "") + ". "
          + (f"That is {len(above) + len(below)} of {n_cmp} period × regime × depth comparisons, about the "
             f"{0.05 * n_cmp:.0f} a 95% interval would give by chance alone, so it is not read as a finding. "
             if (above or below) else "")
          + f"Sensitivity (added in review): without the two futures series ({', '.join(S1_FUTURES)}), whose ATR "
          "and paths include unadjusted roll gaps, the pre-registered rule gives "
          f"*{sens['verdict']}*"
          + (f", with {len(s_above) + len(s_below)} of {len(sens['calls'])} single-period CIs clear of the null"
             if (s_above or s_below) else ", with no single-period CI clear of the null")
          + (f" (above at {', '.join(s_above)})" if s_above else "")
          + (f" (below at {', '.join(s_below)})" if s_below else "") + ". "
          "For Section III this means the distinction between a detour and a breakdown cannot be read from "
          "the size of the adverse move alone; the depth of a detour, on its own, carried no information "
          "beyond geometry here. Whether richer context can tell the two apart, as Principle 2 asks, is "
          "not something this test of one trend filter can settle.", ""]
    L += ["**What this does NOT show.** It does not show that B = A + 3 ATR is a sensible target, or that "
          "buying every day is a strategy (most entries are not trades anyone would take). It uses daily "
          "bars, so the order of events within a day is unknown. It conditions on one context variable "
          "(trend); the philosophy's *structure* is richer than a moving-average test, and a richer context "
          "might find the breakdown signal that depth alone does not carry. The memoryless null removes "
          "volatility clustering: after a sharp fall volatility usually rises, so real paths, measured in "
          "ATR at entry, swing wider in both directions than the null's. The null is also held in one regime "
          f"for all {p1['horizon']} days, and its value is treated as fixed: its own estimation error (it is "
          "built from the same finite sample of days) is not in the CIs, so single-period 'above' or 'below' "
          f"calls are, if anything, too easy to get. The block bootstrap uses {p1['block_calendar_days']}-day "
          f"blocks for {p1['horizon']}-trading-day outcomes (about {p1['horizon'] * 365.25 / 252:.0f} calendar "
          "days), so neighbouring blocks still share some outcome windows, and the out-of-sample period holds "
          f"only {s1['n_blocks']['OOS']} blocks ({s1['n_blocks']['IS']} in-sample): the CIs are approximate. It "
          "says nothing about the short side.", ""]
    if all(v is None for v in sc.values()):
        sc_txt = f"no depth up to {kd:g} ATR beat a memoryless null as a breakdown signal"
    else:
        sc_txt = "breakdown-like from " + ", ".join(f"{sc[r]:g} ATR ({r})" for r in sc if sc[r] is not None)
    finding = (f"OOS, a 1-ATR detour cut P(B) from {pct(u0, 0)} to {pct(u1, 0)} (uptrend) and "
               f"{pct(o0, 0)} to {pct(o1, 0)} (other); {sc_txt} (also without the futures: "
               f"{sens['verdict']}); the regime at A shifted the whole curve (OOS gap {pp(d0[0], 0)} points "
               f"unconditionally, {pp(n0, 0)} of them reproduced by the memoryless null).")
    return L, finding


def report_s2(s2: dict, fig: str) -> tuple[list[str], str]:
    p2 = P["S2"]
    L = ["## S2 — Recurrence is conditional", ""]
    L += ["**Claim tested.** Sections V and VI ([[philo_recurring_storyline]], "
          "[[philo_conditional_probability]]) and Principle 4 ([[principle_04_conditional_probability]]): a "
          "recurring tendency is a conditional probability, not a law. The same pattern can mean different "
          "things in different conditions, and an estimate holds only while conditions resemble those it was "
          "measured in. Testable form: conditional cells should differ from the unconditional baseline, and "
          "some of the differences found on one period should fail on the next.", ""]
    L += [f"**Design.** Outcome: {p2['horizon']}-day forward log return from the close of day t; P(up) = share "
          "of positive outcomes. Conditions at t (data up to t only): trend regime (as in S1) × realised-vol "
          f"tercile ({p2['vol_window']}-day realised volatility; tercile cut-offs estimated per market on "
          "in-sample data only, then frozen), and one simple recurring pattern, three consecutive lower "
          "closes (*3-down*), alone and inside each of the six contexts. Each cell is compared with the "
          "baseline (all days) of the same market and period. Overlapping 5-day windows are handled with a "
          f"block bootstrap over {p2['block_calendar_days']}-day calendar blocks; the cell-minus-baseline "
          "difference is bootstrapped jointly. A difference is *found* in-sample when its 95% CI excludes "
          "zero; out-of-sample it *held* (same sign, CI excludes zero), *weakened* (same sign, CI includes "
          "zero), *vanished* (opposite sign, CI includes zero) or *reversed* (opposite sign, CI excludes "
          f"zero). A cell whose observations fall in fewer than {S2_MIN_BLOCKS} bootstrap blocks in either "
          "period is marked *too few to judge* (see the deviation note above) and left out of the scorecard "
          "and the chart.", ""]
    rows = []
    for sym in p2["symbols"]:
        info = s2["symbols"][sym]
        si, so = info["stats"]["IS"], info["stats"]["OOS"]
        q1, q2 = info["q"]
        rows.append([f"`{sym}`", f"{si['first']} → {si['last']}", f"{si['n'][0]:,}", f"{so['first']} → {so['last']}",
                     f"{so['n'][0]:,}", f"{q1:.1%} / {q2:.1%}"])
    L += ["**Data.**", ""]
    L += table(["market", "in-sample", "IS days", "out-of-sample", "OOS days", "vol tercile cut-offs (annualised)"], rows)
    for sym in p2["symbols"]:
        info = s2["symbols"][sym]
        si, so = info["stats"]["IS"], info["stats"]["OOS"]
        L += [f"**`{sym}`.** Baseline in-sample: P(up) {pct(si['up'][0])} {ci_pct(*[x[0] for x in si['up_ci']])}, "
              f"mean {bp(si['mean'][0])} bp {ci_bp(*[x[0] for x in si['mean_ci']])}. Out-of-sample: P(up) "
              f"{pct(so['up'][0])} {ci_pct(*[x[0] for x in so['up_ci']])}, mean {bp(so['mean'][0])} bp "
              f"{ci_bp(*[x[0] for x in so['mean_ci']])}. Cells show the difference from that baseline.", ""]
        rows = []
        srows = {r["cell"]: r for r in s2["rows"] if r["symbol"] == sym}
        for j, (name, _) in enumerate(info["cells"]):
            if j == 0:
                continue
            rr = srows[name]
            rows.append([name, f"{si['n'][j]:,}",
                         f"{pp(si['d_up'][j], 1, True)} {ci_pct(si['d_up_ci'][0][j], si['d_up_ci'][1][j], 1, True)}",
                         f"{bp(si['d_mean'][j])} {ci_bp(si['d_mean_ci'][0][j], si['d_mean_ci'][1][j])}",
                         f"{so['n'][j]:,}",
                         f"{pp(so['d_up'][j], 1, True)} {ci_pct(so['d_up_ci'][0][j], so['d_up_ci'][1][j], 1, True)}",
                         f"{bp(so['d_mean'][j])} {ci_bp(so['d_mean_ci'][0][j], so['d_mean_ci'][1][j])}",
                         "too few to judge" if rr["too_few"] else rr["cls_up"],
                         "too few to judge" if rr["too_few"] else rr["cls_mean"]])
        L += table(["cell", "IS n", "IS ΔP(up), pp", "IS Δmean, bp", "OOS n", "OOS ΔP(up), pp", "OOS Δmean, bp",
                    "P(up): fate", "mean: fate"], rows)
    cnt = s2["counts"]
    rows = []
    for metric, lab in [("cls_up", "P(up)"), ("cls_mean", "mean 5-day return")]:
        c = cnt[metric]
        rows.append([lab, str(c["tested"]), str(c["found"]), str(c["held"]), str(c["weakened"]), str(c["vanished"]),
                     str(c["reversed"]), str(c["not found IS (sig. OOS)"])])
    n_cells = len(s2["rows"])
    L += [f"**Scorecard.** {n_cells} cells per metric ({len(s2['symbols'][p2['symbols'][0]]['cells']) - 1} × "
          f"{len(p2['symbols'])} markets); {cnt['cls_mean']['too_few']} were too "
          "few to judge, the rest are counted below.", ""]
    L += table(["metric", "cells judged", "found IS", "held", "weakened", "vanished", "reversed",
                "appeared only OOS"], rows)
    exp_fp = 0.05 * cnt["cls_mean"]["tested"]
    L += [f"With {cnt['cls_mean']['tested']} cells per metric, about {exp_fp:.1f} would clear a 95% interval by "
          "chance alone even if no condition mattered (and as many again out-of-sample); the cells also "
          "overlap (the 3-down cells are subsets of the context cells), so they are not independent tests. "
          f"In-sample, {cnt['cls_up']['found']} (P(up)) and {cnt['cls_mean']['found']} (mean) cleared it.", ""]
    L += [f"![S2 in-sample vs out-of-sample]({fig})", ""]
    held = [f"`{r['symbol']}` {r['cell']}" for r in s2["rows"] if r["cls_mean"] == "held" and not r["too_few"]]
    held_up = [f"`{r['symbol']}` {r['cell']}" for r in s2["rows"] if r["cls_up"] == "held" and not r["too_few"]]
    found = cnt["cls_up"]["found"] + cnt["cls_mean"]["found"]
    heldn = cnt["cls_up"]["held"] + cnt["cls_mean"]["held"]
    base_parts, moved = [], []
    for sym in p2["symbols"]:
        st_ = s2["symbols"][sym]["stats"]
        # IS and OOS resamples are independent, so pairing them bootstraps the difference
        dl, dh = ci_of(st_["OOS"]["base_up_rep"] - st_["IS"]["base_up_rep"])
        dv = st_["OOS"]["up"][0] - st_["IS"]["up"][0]
        base_parts.append(f"`{sym}` {pct(st_['IS']['up'][0])} → {pct(st_['OOS']['up'][0])} "
                          f"({pp(dv, 1, True)} points {ci_pct(dl, dh, 1, True)})")
        if dl > 0 or dh < 0:
            moved.append(f"`{sym}`")
    base = "; ".join(base_parts)
    tested2 = cnt["cls_up"]["tested"] + cnt["cls_mean"]["tested"]
    p_chance = float(stats.binom.sf(found - 1, tested2, 0.05)) if found else 1.0
    L += [f"**Verdict: {verdict_word(s2['verdict'])}** (pre-registered rule: some in-sample differences held "
          "and some did not). The support is mostly for the cautious half of Sections V–VI. Across both "
          f"metrics, {found} of {tested2} judged cells differed from their baseline in-sample, where about "
          f"{0.05 * tested2:.0f} would by chance; if the {tested2} tests were independent, {found} or more would "
          f"happen by chance with probability {p_chance:.2g}, but they are not (nested cells, and two strongly "
          "correlated metrics on the same cells), so the true chance is larger and the excess is suggestive, "
          f"not established. {heldn} held out-of-sample and {found - heldn} weakened, "
          f"vanished or reversed. Held (mean): {', '.join(held) if held else 'none'}. Held (P(up)): "
          f"{', '.join(held_up) if held_up else 'none'}. "
          + (f"A single held cell out of {tested2} tests is itself weak evidence. " if heldn == 1 else "")
          + f"The unconditional baselines also differed between periods (P(up), in-sample → out-of-sample, "
          f"with a 95% CI of the change: {base}); "
          + (f"for {', '.join(moved)} the change is beyond sampling noise, so even the 'unconditional' "
             "probability was conditional on the period, while for the others it is within noise. "
             if moved else "none of these changes is beyond sampling noise. ")
          + "Conditioning can matter, but with these simple conditions most apparent "
          "differences were within noise, and a difference that looked real on one period usually did not "
          "survive to the next: a conditional estimate has to be re-earned, not assumed.", ""]
    L += ["**What this does NOT show.** These are statistical tendencies of index, gold and EUR/USD closes, "
          "not setups. A cell that held is not a trading edge: S7 shows what costs do to the best one. Two "
          "periods are a thin test of persistence; a cell can hold across 2013–2026 and still fail later. "
          "The regime and volatility definitions are one simple choice among many; other definitions would "
          "give other cells. The in-sample volatility terciles are cut on the whole in-sample period, so the "
          "in-sample classification of a day uses later in-sample data (a fitted, not a real-time, split); "
          "only the out-of-sample classification is real-time. No p-value or interval here is corrected for "
          "the number of cells scanned. Equity index levels exclude dividends.", ""]
    finding = (f"{found} of {tested2} conditional cells differed in-sample (≈{0.05 * tested2:.0f} expected by "
               f"chance, before allowing for dependence); {heldn} held OOS, {found - heldn} weakened, vanished "
               "or reversed.")
    return L, finding


def report_s3(s3: dict, s7: dict, fig: str) -> tuple[list[str], str]:
    p3 = P["S3"]
    L = ["## S3 — The law of large numbers: what a sample can and cannot establish", ""]
    L += ["**Claim tested.** Section VI ([[philo_conditional_probability]], *the importance of the law of large "
          "numbers*): a few successful trades do not establish an advantage, and observed frequencies approach "
          "the underlying probability only as relevant observations accumulate. Open question 3 "
          "([[question_estimate_reliability]]) asks how reliable the estimates are. See also "
          "[[concept_probabilistic_thinking]] and [[concept_expectancy]].", ""]
    L += [f"**Design.** A hypothetical strategy with a real but small edge: win rate {p3['p_win']:.0%}, "
          f"payoff {p3['reward_risk']:g}:1, cost {p3['cost_r']:g}R per trade, so the true expectancy is "
          f"{s3['true_ev']:+.3f}R per trade (breakeven win rate "
          f"{el.breakeven_win_rate(p3['reward_risk'], p3['cost_r']):.1%}). For each sample size, "
          f"{p3['n_samples']:,} independent samples are simulated (seeded binomial draws); the exact binomial "
          "probability is shown next to each simulated share as a check. *Looks like a loser* = observed "
          "expectancy ≤ 0 after costs; *looks like a star* = observed win rate ≥ 70%.", ""]
    rows = []
    for r in s3["rows"]:
        rows.append([str(r["n"]), pct(r["wr_q"][1]), f"{pct(r['wr_q'][0])} – {pct(r['wr_q'][2])}",
                     f"{r['exp_q'][0]:+.2f}R – {r['exp_q'][2]:+.2f}R",
                     f"{pct(r['loser_sim'])} ({prob(r['loser_exact'])})",
                     f"{share(r['star_sim'], p3['n_samples'], 2)} ({prob(r['star_exact'], 2)})"])
    L += ["**Results (hypothetical, simulated).**", ""]
    L += table(["trades", "median win rate", "95% of samples: win rate", "95% of samples: expectancy",
                "looks like a loser: sim (exact)", "looks like a star: sim (exact)"], rows)
    pl = s3["plan"]
    L += [f"`trades_needed` for the true parameters: per-trade expectancy {pl.expectancy_r:+.3f}R with sd "
          f"{pl.sd_r:.3f}R, so a 95% interval on expectancy excludes zero on an average sample only after "
          f"about **{pl.n_expectancy_typical:,.0f} trades**, and with 80% power after about "
          f"**{pl.n_expectancy:,.0f} trades**; pinning the win rate to ±5 points takes about "
          f"{pl.n_win_rate:,.0f} trades.", ""]
    L += [f"![S3 law of large numbers]({fig})", ""]
    e = s3["emp"]
    L += [f"**One empirical cell.** The cell chosen in S7 (`{s7['symbol']}` · {s7['cell']}), as "
          "non-overlapping 5-day long trades so that the trades are close to independent, checked with "
          "`wilson_interval`, `beta_posterior` (uniform prior) and `expectancy_from_results` from "
          "`edge_lab.py`. A *win* is a positive 5-day return before costs.", ""]
    rows = []
    for period in ["IS", "OOS"]:
        d = e[period]
        ex = d["ex"]
        rows.append([period, str(d["n"]), str(d["wins"]), pct(d["wr"]), ci_pct(*d["wilson"]),
                     f"{pct(d['post'].mean)} {ci_pct(d['post'].ci_low, d['post'].ci_high)}",
                     pct(d["post"].prob_above_threshold), f"{bp(ex.mean)} {ci_bp(ex.ci_low, ex.ci_high)}",
                     f"{d['n_need']:,}" if np.isfinite(d["n_need"]) else "∞ (mean ≤ 0)"])
    L += table(["period", "trades", "wins", "win rate", "Wilson 95% CI", "Beta posterior mean [95% CrI]",
                "P(true win rate > 50%)", "mean bp [95% CI]", "trades for 80% power"], rows)
    di = e["IS"]
    L += [f"The in-sample row is also the *best of {s7['n_candidates']} cells*, so its numbers carry selection "
          "bias on top of sampling error: the interval describes sampling noise only, not the luck of being "
          f"picked. Even so, an interval of {ci_pct(*di['wilson'])} on {di['n']} trades is the honest size of "
          "what the sample knows.", ""]
    L += [f"**Verdict: {verdict_word(s3['verdict'])}.** With a genuine edge of {s3['true_ev']:+.2f}R, "
          f"{pct(s3['rows'][1]['loser_exact'], 1)} of 30-trade samples and {pct(s3['rows'][2]['loser_exact'], 1)} "
          f"of 100-trade samples still look like losing strategies, and about {pl.n_expectancy:,.0f} trades are "
          "needed before the evidence reliably separates the edge from zero.", ""]
    L += ["**What this does NOT show.** The simulated trades are independent and identically distributed; "
          "real trades are not (regimes change, S2), which makes the real problem harder, not easier. The "
          "empirical row describes one cell of one study, not a strategy anyone trades.", ""]
    finding = (f"A true {s3['true_ev']:+.2f}R edge looks like a loser in {pct(s3['rows'][1]['loser_exact'], 1)} "
               f"of 30-trade samples; ≈{pl.n_expectancy:,.0f} trades needed for 80% power.")
    return L, finding


def report_s4(s4: dict, fig: str) -> tuple[list[str], str]:
    p4 = P["S4"]
    L = ["## S4 — Capital preservation: streaks, drawdowns and ruin", ""]
    L += ["**Claim tested.** Section XIV ([[philo_capital_preservation]]) and Principle 9 "
          "([[principle_09_protect_capital]]): even a strategy with a genuine positive expectancy meets "
          "unfavourable sequences, losses are asymmetric, and sizing must keep a bad sequence from ending "
          "participation. See [[concept_risk_of_ruin_drawdown]], [[concept_position_sizing]], "
          "[[concept_kelly_criterion_optimal_f]].", ""]
    L += [f"**Design.** Three hypothetical positive-EV strategies after a {p4['cost_r']:g}R cost per trade, each "
          f"run at five fixed-fractional risk levels: {p4['n_trades']} trades × {p4['n_paths']:,} seeded paths "
          "(`simulate_equity`), compounding on current equity. Streak probabilities are exact (Markov chain, "
          "`prob_losing_streak`). *Ruin* here = a peak-to-trough drawdown of 50% or more at any point.", ""]
    rows = []
    for p, b in p4["strategies"]:
        rows.append([f"p = {p:.2f}, {b:g}R", f"{s4['ev'][(p, b)]:+.3f}R", f"{s4['kelly'][(p, b)]:.1%}",
                     prob(s4["streaks"][(p, b, p4['streaks'][0])]), prob(s4["streaks"][(p, b, p4['streaks'][1])])])
    L += ["**The strategies.**", ""]
    L += table(["strategy", "EV per trade", "full Kelly fraction", f"P({p4['streaks'][0]}+ loss streak in "
                f"{p4['n_trades']})", f"P({p4['streaks'][1]}+ loss streak in {p4['n_trades']})"], rows)
    rows = []
    for p, b in p4["strategies"]:
        for f in p4["risk_per_trade"]:
            s = s4["sims"][(p, b, f)]
            rows.append([f"p = {p:.2f}, {b:g}R", f"{f:.1%}", pct(s["max_drawdown_median"]), pct(s["max_drawdown_p95"]),
                         share(s["prob_ruin"], p4["n_paths"]), num(s["final_equity_median"], 2),
                         share(s["prob_final_below_start"], p4["n_paths"])])
    L += ["**Results (hypothetical, simulated).**", ""]
    L += table(["strategy", "risk per trade", "median max DD", "95th pct max DD", "P(DD ≥ 50%)",
                "median final equity (start 1.00)", "P(end below start)"], rows)
    rows = [[f"{L_:.0%}", f"{g:.1%}"] for L_, g in s4["recovery"].items()]
    L += ["**The asymmetry of losses** (`recovery_required`): the gain needed to get back to the start.", ""]
    L += table(["loss", "gain required"], rows)
    L += [f"![S4 ruin]({fig})", ""]
    hi_f = max(p4["risk_per_trade"])
    worst = tuple(max(p4["strategies"], key=lambda s: s4["sims"][(s[0], s[1], hi_f)]["prob_ruin"]))
    sw = s4["sims"][(worst[0], worst[1], hi_f)]
    s1p = s4["sims"][(worst[0], worst[1], 0.01)]
    over = [(p, b) for p, b in p4["strategies"] if s4["kelly"][(p, b)] < hi_f]
    under = [(p, b) for p, b in p4["strategies"] if s4["kelly"][(p, b)] >= hi_f]
    parts = []
    for p, b in over:
        lo_f = max(f for f in p4["risk_per_trade"] if f <= s4["kelly"][(p, b)])
        parts.append(f"for p = {p:.2f}, {b:g}R (full Kelly {s4['kelly'][(p, b)]:.1%}), going from {lo_f:.0%} to "
                     f"{hi_f:.0%} risk lowered the median final equity from "
                     f"{num(s4['sims'][(p, b, lo_f)]['final_equity_median'])} to "
                     f"{num(s4['sims'][(p, b, hi_f)]['final_equity_median'])}: past Kelly, more risk is worse "
                     "even for the typical path")
    for p, b in under:
        parts.append(f"for p = {p:.2f}, {b:g}R (Kelly {s4['kelly'][(p, b)]:.1%}) the median kept rising to "
                     f"{num(s4['sims'][(p, b, hi_f)]['final_equity_median'])} at {hi_f:.0%} while P(DD ≥ 50%) "
                     f"reached {share(s4['sims'][(p, b, hi_f)]['prob_ruin'], p4['n_paths'])}")
    kelly_txt = ("The median hides the path: " + "; ".join(parts) + ". The simulation cannot measure how a "
                 "person trades through a 50% drawdown; Principle 9's point is that the process should never "
                 "have to find out.") if parts else ""
    L += [f"**Verdict: {verdict_word(s4['verdict'])}.** The same edge (p = {worst[0]:.2f}, {worst[1]:g}R, EV "
          f"{s4['ev'][worst]:+.3f}R) reached a 50% drawdown in {share(s1p['prob_ruin'], p4['n_paths'])} "
          f"simulated paths at 1% risk per trade and in {share(sw['prob_ruin'], p4['n_paths'])} at "
          f"{hi_f:.0%}. A positive expectancy does not protect an account from its own bet size. " + kelly_txt, ""]
    L += ["**What this does NOT show.** The win rates and payoffs are assumed known and constant; in "
          "practice they are estimates (S3), which argues for sizing below these levels. Trades are "
          "independent here; correlated losses (several positions in one regime) make streaks and "
          "drawdowns worse. No real account or strategy is described.", ""]
    finding = (f"Same +EV edge (p = {worst[0]:.2f}, {worst[1]:g}R): a 50% drawdown in "
               f"{share(s1p['prob_ruin'], p4['n_paths'])} simulated paths at 1% risk vs "
               f"{share(sw['prob_ruin'], p4['n_paths'])} at {hi_f:.0%}; a 50% loss needs +100%.")
    return L, finding


def report_s5(s5: dict, fig: str) -> tuple[list[str], str]:
    p5 = P["S5"]
    L = ["## S5 — Overfitting: the best of many rules", ""]
    L += ["**Claim tested.** Section XVII ([[philo_scientific_method]]) warns that rules adjusted until they "
          "fit the past can learn the noise of the sample; Section XX.4 ([[philo_research_foundations]]) "
          "points to the research on backtest overfitting; Principle 5 "
          "([[principle_05_mathematical_justification]]) asks for mathematical justification, not a "
          "convincing backtest. See [[concept_overfitting_validation]], [[concept_backtesting]], "
          "[[paper_deflated_sharpe_2014]] ([[person_marcos_lopez_de_prado]]).", ""]
    L += [f"**Design.** `{p5['symbol']}` daily closes. {s5['n_variants']} rule variants "
          "([[concept_moving_averages]], [[concept_trend_following]], [[concept_breakout_trading]]): "
          "SMA crossovers, close vs SMA, time-series momentum and Donchian breakouts, each long/flat and "
          "long/short. Position decided at the close from data up to that close, held to the next close; "
          f"{p5['cost_bp_per_side']:g} bp per side on every change of position; flat earns nothing. "
          f"In-sample {s5['is_span'][0]} → {s5['is_span'][1]} ({s5['n_is']:,} days), out-of-sample "
          f"{s5['oos_span'][0]} → {s5['oos_span'][1]} ({s5['n_oos']:,} days). The winner is the highest "
          "in-sample Sharpe. Its Deflated Sharpe Ratio uses the number of variants tried and the variance of "
          f"their Sharpe ratios. The whole search is then repeated on {p5['n_shuffles']} copies of the "
          "in-sample series whose daily returns were randomly permuted: same returns, same drift, nearly the "
          "same buy-and-hold Sharpe, no serial structure for any rule to find.", ""]
    m = s5["win_moments"]
    rows = [
        ["variants searched", f"{s5['n_variants']}"],
        ["in-sample winner", s5["winner"]],
        ["winner: in-sample Sharpe", num(s5["win_is"])],
        ["winner: out-of-sample Sharpe", num(s5["win_oos"])],
        ["winner: out-of-sample rank", f"{s5['oos_rank']} of {s5['n_variants']}"],
        ["buy and hold: in-sample / out-of-sample Sharpe", f"{num(s5['bh_is'])} / {num(s5['bh_oos'])}"],
        ["median variant: in-sample / out-of-sample Sharpe", f"{num(s5['median_is'])} / {num(s5['median_oos'])}"],
        ["share of variants beating buy and hold out-of-sample", pct(s5["share_oos_beat_bh"])],
        ["Spearman rank correlation, IS vs OOS Sharpe", num(s5["rho"])],
        ["winner: skew / kurtosis of daily returns (IS)", f"{num(m['skew'])} / {num(m['kurt'])}"],
        ["winner: PSR vs 0 (no deflation)", num(s5["psr"], 3)],
        ["expected best Sharpe of the variants by luck alone (SR0, annualised)", num(s5["sr0_ann"])],
        ["winner: Deflated Sharpe Ratio", num(s5["dsr"], 3)],
    ]
    L += ["**Results.**", ""]
    L += table(["quantity", "value"], rows)
    rows = [[name, num(a), num(b)] for name, a, b in s5["top"]]
    L += ["Top five in-sample variants:", ""]
    L += table(["variant", "IS Sharpe", "OOS Sharpe"], rows)
    best = np.array([s["best"] for s in s5["shuf"]])
    dsrs = np.array([s["dsr"] for s in s5["shuf"]])
    bh_sh = np.array([s["bh"] for s in s5["shuf"]])
    med_sh = np.array([s["median"] for s in s5["shuf"]])
    rows = [
        ["best in-sample Sharpe: mean [min, max]", f"{num(best.mean())} [{num(best.min())}, {num(best.max())}]"],
        ["buy and hold Sharpe on the shuffled copies (mean)", num(bh_sh.mean())],
        ["median variant Sharpe (mean over copies)", num(med_sh.mean())],
        ["copies whose best rule beats the real winner's in-sample Sharpe",
         f"{int((best >= s5['win_is']).sum())} of {len(best)}"],
        ["permutation p-value of the real winner", num(s5["perm_p"], 3)],
        ["Deflated Sharpe of the shuffled winners: median [min, max]",
         f"{num(np.median(dsrs), 3)} [{num(dsrs.min(), 3)}, {num(dsrs.max(), 3)}]"],
    ]
    L += [f"**The same search on {len(best)} no-signal copies.**", ""]
    L += table(["quantity", "value"], rows)
    L += [f"![S5 overfitting]({fig})", ""]
    vp = s5["verdict_parts"]
    reasons = []
    if vp["oos_below_half"]:
        reasons.append("the winner kept less than half of its in-sample Sharpe out-of-sample")
    if vp["dsr_below_95"]:
        reasons.append("its Deflated Sharpe Ratio is below 0.95")
    if vp["perm_p_ge_05"]:
        reasons.append(f"the best rule on no-signal copies matched or beat it in "
                       f"{int((best >= s5['win_is']).sum())} of {len(best)} copies (permutation p = "
                       f"{num(s5['perm_p'], 2)} ≥ 0.05)")
    L += [f"**Verdict: {verdict_word(s5['verdict'])}.** Pre-registered triggers met: "
          f"{'; '.join(reasons) if reasons else 'none'}. "
          f"The winner, {s5['winner']}, did not collapse: in-sample Sharpe {num(s5['win_is'])}, out-of-sample "
          f"{num(s5['win_oos'])}. But what the search was selecting for, an advantage over simply holding, did "
          f"not carry over: {num(s5['win_is'] - s5['bh_is'], 2)} Sharpe over buy and hold in-sample, "
          f"{num(s5['win_oos'] - s5['bh_oos'], 2)} out-of-sample, and only {pct(s5['share_oos_beat_bh'])} of "
          "all variants beat buy and hold out-of-sample. On series with no signal at all, the best of "
          f"{s5['n_variants']} rules reached a mean in-sample Sharpe of {num(best.mean())} against "
          f"{num(bh_sh.mean())} for holding, an advantage of up to {num((best - bh_sh).max(), 2)} produced by "
          f"selection alone; the real winner's in-sample advantage ({num(s5['win_is'] - s5['bh_is'], 2)}) "
          + ("sits inside that range. " if (best - bh_sh).max() >= s5['win_is'] - s5['bh_is'] else
             "is larger than any of them. ")
          + f"The high IS-OOS rank correlation "
          f"({num(s5['rho'])}) is consistent with the rules differing persistently in *how much* market "
          "exposure they carry rather than in timing skill (exposure itself was not measured here).", ""]
    L += ["**What this does NOT show.** It does not show that trend rules never work: one market, one "
          "family of rules and one split are tested. The variants are highly correlated, so the effective "
          "number of independent trials is smaller than the count, which makes the deflation conservative. "
          "The index excludes dividends (understating every long position) and flat periods earn no "
          "interest (understating the long/flat rules); the two biases partly offset. The DSR assumes skill-less trials centre on zero "
          "Sharpe; with a drifting index, long-biased rules do not, so the shuffled winners' DSR also "
          "measures the drift, not timing skill.", ""]
    finding = (f"Best of {s5['n_variants']} rules: Sharpe {num(s5['win_is'])} IS → {num(s5['win_oos'])} OOS, "
               f"but its edge over buy and hold went {num(s5['win_is'] - s5['bh_is'], 2)} → "
               f"{num(s5['win_oos'] - s5['bh_oos'], 2)}; DSR {num(s5['dsr'], 2)}; no-signal winners averaged "
               f"{num(best.mean())} vs {num(bh_sh.mean())} for holding.")
    return L, finding


def report_s6(s6: dict, fig: str) -> tuple[list[str], str]:
    p6 = P["S6"]
    L = ["## S6 — Decision quality is not the outcome", ""]
    L += ["**Claim tested.** Section XI ([[philo_being_wrong]]): a loss does not prove the decision wrong and "
          "a profit does not prove it right. Section XIII ([[philo_decisions_not_money]]): follow the process "
          "that has shown an advantage, not the money. Principle 8 "
          "([[principle_08_decision_quality_not_outcome]]). The numbers are the philosophy's own $7 example "
          "from Section VII ([[philo_mathematics_sword]]).", ""]
    L += [f"**Design.** Exact binomial probabilities (checked against {p6['n_sims']:,} seeded simulations) for "
          f"the Section VII strategy: win rate {p6['p_win']:.0%}, average win ${p6['win']:.0f}, average loss "
          f"${p6['loss']:.0f}, cost ${p6['cost']:.0f} per trade, EV {s6['ev']:+.0f} $/trade; and a negative-EV "
          f"twin with the same payoffs and a {p6['twin_p_win']:.0%} win rate (EV {s6['ev_twin']:+.0f} $/trade).", ""]
    rows = []
    for r in s6["rows"]:
        rows.append([str(r["n"]), f"{pct(r['down'])} ({pct(r['down_sim'])})",
                     f"{pct(r['up_twin'])} ({pct(r['up_twin_sim'])})"])
    L += ["**Results (hypothetical).** Exact, with the simulation in brackets.", ""]
    L += table(["trades", f"+EV strategy (EV +${s6['ev']:.0f}): P(behind)",
                f"−EV twin (EV −${abs(s6['ev_twin']):.0f}): P(ahead)"], rows)
    L += [f"The +EV strategy loses any single trade with probability {1 - p6['p_win']:.0%}. Its chance of being "
          f"behind first dips below 5% at {s6['n_down5']:,} trades and stays below from **{s6['n_down5_stay']:,} "
          f"trades**; the −EV twin's chance of being ahead first dips below 5% at {s6['n_up5']:,} trades and stays "
          f"below from **{s6['n_up5_stay']:,} trades**. (The zigzag in the chart is real: the total moves in whole "
          "trades, so the break-even number of wins jumps as n grows.)", ""]
    L += [f"![S6 decision vs outcome]({fig})", ""]
    r20 = [r for r in s6["rows"] if r["n"] == 20][0]
    L += [f"**Verdict: {verdict_word(s6['verdict'])}.** After 20 trades the sound strategy is behind "
          f"{pct(r20['down'], 0)} of the time and the unsound one is ahead {pct(r20['up_twin'], 0)} of the time. "
          "Over the horizon most traders judge themselves on, the result says little about the decision.", ""]
    L += ["**What this does NOT show.** The probabilities assume the win rate and payoffs are known and "
          "stable, which is exactly what a real trader does not know (S3). The point is narrower: even "
          "when the edge is known, short-run results are a weak verdict.", ""]
    finding = (f"After 20 trades the +$7 strategy is behind {pct(r20['down'], 0)} of the time; the −$4 twin is "
               f"ahead {pct(r20['up_twin'], 0)}.")
    return L, finding


def report_s7(s7: dict, s2: dict, fig: str) -> tuple[list[str], str]:
    p7 = P["S7"]
    L = ["## S7 — Does the edge survive costs?", ""]
    L += ["**Claim tested.** Open question 4 ([[question_survives_costs]]) and Principle 5 "
          "([[principle_05_mathematical_justification]]): spreads, commissions and slippage can turn an "
          "apparent advantage into a loss; question 5 ([[question_survives_regime_change]]) asks whether it "
          "survives a change of period. See [[concept_expectancy]].", ""]
    best = s7["best"]
    L += [f"**Design.** The cell was chosen on in-sample data only: {p7['selection']}. Chosen: "
          f"**`{s7['symbol']}` · {s7['cell']}** (in-sample mean {bp(best['is_mean'])} bp over "
          f"{best['is_n']:,} overlapping days; {s7['n_candidates']} candidate cells). Trades: "
          f"{p7['trades']}. Expectancy per trade is net of the cost per side paid twice; 95% CIs are Student-t "
          "on the non-overlapping trades.", ""]
    rows = []
    for cst in p7["costs_bp_per_side"]:
        ri, ro = s7["rows"][("IS", cst)], s7["rows"][("OOS", cst)]
        rows.append([f"{cst:g}", f"{bp(ri.mean)} {ci_bp(ri.ci_low, ri.ci_high)}", pct(ri.win_rate),
                     f"{bp(ro.mean)} {ci_bp(ro.ci_low, ro.ci_high)}", pct(ro.win_rate)])
    ni, no = len(s7["trades"]["IS"]), len(s7["trades"]["OOS"])
    L += [f"**Results.** In-sample {ni} trades, out-of-sample {no} trades.", ""]
    L += table(["cost per side (bp)", "IS expectancy, bp [95% CI]", "IS win rate", "OOS expectancy, bp [95% CI]",
                "OOS win rate"], rows)
    bo, bi = s7["bench_ex"]["OOS"], s7["bench_ex"]["IS"]

    def be_txt(period: str) -> str:
        v = s7["breakeven"][period]
        return f"{bp(v, 1, False)} bp" if v > 0 else "none (the gross expectancy is already ≤ 0)"

    so = s2["symbols"][s7["symbol"]]["stats"]["OOS"]
    si = s2["symbols"][s7["symbol"]]["stats"]["IS"]
    j = s7["j"]
    L += [f"Break-even cost per side: **{be_txt('IS')} in-sample, {be_txt('OOS')} out-of-sample**. For comparison, a 5-day long trade taken "
          f"on every eligible day (non-overlapping) averaged {bp(bi.mean)} bp {ci_bp(bi.ci_low, bi.ci_high)} "
          f"in-sample and {bp(bo.mean)} bp {ci_bp(bo.ci_low, bo.ci_high)} out-of-sample before costs: that part "
          "of any long cell's return is the market's drift, not the condition.", ""]
    L += [f"![S7 costs]({fig})", ""]
    ro2 = s7["rows"][("OOS", 2)]
    g_oos = s7["rows"][("OOS", 0)].mean
    L += [f"**Two averages of one cell.** In S2 the cell's out-of-sample mean was {bp(so['mean'][j])} bp over "
          f"{so['n'][j]} overlapping days; the {no} non-overlapping trades a trader could actually take "
          f"averaged {bp(g_oos)} bp. Signals in this cell come in clusters (sell-offs), and a one-position-at-"
          "a-time rule takes the first signal of each cluster and skips the rest: out-of-sample the "
          f"{len(s7['skipped']['OOS'])} skipped signal days averaged {bp(s7['skipped']['OOS'].mean())} bp "
          "(simple return). In-sample the cell mean was "
          f"{bp(si['mean'][j])} bp, the trades {bp(s7['rows'][('IS', 0)].mean)} bp and the skipped days "
          f"{bp(s7['skipped']['IS'].mean())} bp. A conditional frequency and a tradable expectancy are "
          "different objects.", ""]
    L += [f"**Verdict: {verdict_word(s7['verdict'])}.** The cell chosen as best in-sample "
          f"({bp(s7['rows'][('IS', 0)].mean)} bp per trade gross, break-even "
          f"{be_txt('IS')} per side) earned {bp(g_oos)} bp per trade out-of-sample before costs and "
          f"{bp(ro2.mean)} bp {ci_bp(ro2.ci_low, ro2.ci_high)} at 2 bp per side; break-even out-of-sample: "
          f"{be_txt('OOS')}. "
          + ("Here the out-of-sample period, not the costs, removed the apparent edge; costs only deepened "
             "the loss. " if g_oos <= 0 else
             f"The gross edge survived out-of-sample, and costs above {be_txt('OOS')} per side would erase it. ")
          + f"With {no} trades the interval is wide either way: the evidence cannot say the cell is bad, only that "
          "it never earned the confidence its in-sample numbers suggested. "
          + ("Scope of the verdict: the pre-registered rule counts an out-of-sample loss before costs as "
             "support, but this cell does not test the narrower claim that costs turn a real advantage into a "
             "loss; what it shows is the decay from the selection period to the next (question 5). "
             if g_oos <= 0 else "")
          + f"Its in-sample numbers are also the best of {s7['n_candidates']} candidate cells, so they are "
          "biased upward by the selection itself (S5's lesson), on top of sampling error.", ""]
    L += ["**What this does NOT show.** The costs are flat assumptions, not measured spreads or slippage, "
          "and an index cannot be traded directly (futures or ETFs add their own costs and tracking). The "
          "trades are long only, so the result mixes the condition with the market's drift. The Student-t "
          "intervals treat the non-overlapping trades as independent; trades taken in the same sell-off are "
          "not fully independent, so the true intervals are somewhat wider. Nothing here is a recommendation "
          "to trade the cell.", ""]
    finding = (f"Best IS cell ({s7['symbol']} · {s7['cell']}): {bp(s7['rows'][('IS', 0)].mean)} bp/trade IS "
               f"→ {bp(s7['rows'][('OOS', 0)].mean)} bp OOS before costs; break-even OOS: {be_txt('OOS')}"
               + ("; the edge fell away before costs, so costs themselves were not the test." if
                  s7["rows"][("OOS", 0)].mean <= 0 else "."))
    return L, finding


def write_report(s1, s2, s3, s4, s5, s6, s7, runtime: float) -> None:
    L: list[str] = [FRONTMATTER, "# Evidence Lab — testing the Philosophy of the Relationship on real market data", ""]
    L += ["> **Education, not financial advice. Not a trading signal.** Every number on this page was computed "
          "by `tools/philosophy/studies.py` from public daily data, under the definitions stated here, and "
          "comes with its uncertainty. None of it is the win rate or P&L of a real strategy, account or "
          "trader. The hypothetical strategies in S3, S4 and S6 are labelled as such.", ""]
    L += ["The philosophy ([[philosophy_relationship]]) asks to be tested. Section XVII "
          "([[philo_scientific_method]]) says a theory becomes a method only when its claims meet actual "
          "outcomes, and Section XIX ([[philo_open_questions]]) lists what it still has to prove. This page "
          "takes seven of its claims to real market data (and, where the claim is about mathematics rather "
          "than markets, to exact calculation and simulation), with the rules fixed in advance and an "
          "out-of-sample period kept apart. It is layer L8 of the ontology ([[framework_ontology]]): "
          "review and validation. The functions used are in `tools/philosophy/edge_lab.py`; the formulas are "
          "in [[formula_sheet]].", ""]
    L += ["## How to re-run", "",
          "```bash",
          "python3 tools/philosophy/market_data.py           # download and cache the daily bars (once)",
          "python3 tools/philosophy/studies.py               # run S1-S7, rewrite this page and figures/",
          "python3 tools/philosophy/studies.py --refresh     # re-download the data first",
          "```", "",
          "Data are cached in `tools/philosophy/data/` (git-ignored). Seeds are fixed: the same cache gives the "
          f"same page. This run took {runtime:.0f} s.", ""]
    gc_flat_is, gc_flat_oos = flat_share("GC=F", None, "2007-12-31"), flat_share("GC=F", "2008-01-01", None)
    bad_txt = []
    for sym in md.DEFAULT_SYMBOLS:
        if not any(sym in P[k]["symbols"] for k in ("S1", "S2")) and sym != P["S5"]["symbol"]:
            continue
        cl = md.clean(pd.read_csv(md.cache_path(sym), index_col="date", parse_dates=["date"])).loc[: P["data_end"]]
        m = md.bad_print_mask(cl).to_numpy()
        if m.any():
            c_ = cl["close"].to_numpy()
            ix = np.flatnonzero(m)
            off = [abs(math.log(c_[i] / math.sqrt(c_[i - 1] * c_[i + 1]))) for i in ix]
            bad_txt.append(f"`{sym}`: {len(ix)} bars ({', '.join(cl.index[i].date().isoformat() for i in ix)}), "
                           f"closes {pct(min(off), 0)}–{pct(max(off), 0)} away from their neighbours")
    bad_line = ("Bad prints dropped by the studies: " + "; ".join(bad_txt) + "." if bad_txt
                else "No bad prints were found.")
    L += ["## Data and caveats", "",
          "Daily bars from the public Yahoo Finance chart API, cut at the pre-registered end date. "
          "Columns: rows dropped by the loader for a missing price or a non-positive price, duplicate dates "
          "(the last bar is kept), isolated bad prints dropped by the studies (see the deviations), and bars "
          "kept but suspicious (a high equal to the low, or a high/low inside the open-close range, which the "
          "studies widen to the open and close).", ""]
    L += table(["symbol", "first", "last", "rows used", "dropped: missing", "dropped: ≤ 0", "duplicate dates",
                "dropped: bad prints", "flat bars", "inconsistent bars", "studies"], data_section_rows())
    L += ["- **Yahoo data quality.** Free daily data has gaps and errors. "
          f"{pct(gc_flat_is, 0)} of `GC=F` bars up to 2007 have no intraday range at all (open = high = low = "
          f"close; {pct(gc_flat_oos, 0)} from 2008), so ATR and intraday excursions there come from close-to-close "
          "moves only and are understated; the same days feed S1's null, which keeps the comparison like for "
          "like but makes the gold in-sample rows a close-only test. `EURUSD=X` bars are a 24-hour quote, not "
          "an exchange print, with occasional bad highs/lows. " + bad_line,
          "- **Futures roll gaps.** `GC=F` and `CL=F` are front-month continuous series with no "
          "back-adjustment: each roll can add a jump that no position earned, which inflates ATR and the path "
          "excursions in S1 (only S1 uses `CL=F`; S2 uses `GC=F`, where the jump lands in a 5-day return). "
          "They are not corrected; S1 reports a sensitivity run without the two futures series. `CL=F`'s "
          "negative settlement of April 2020 and the next day are dropped by the loader (a non-positive price "
          "has no return), so the following bar's range and return span three sessions.",
          "- **Index levels.** `^GSPC` and `^NDX` are index levels: they have no survivorship bias of their own "
          "(the index is what it was), but they are not tradable instruments, and they exclude dividends, "
          "so long-side returns are understated (by roughly the dividend yield).",
          "- **Execution.** Signals and entries use the same close (a market-on-close assumption), which is "
          "optimistic. Costs are flat assumptions. No interest is earned when flat.",
          "- **Dependence.** Daily entries with multi-day outcomes overlap. S1 and S2 use every day and report "
          "block-bootstrap CIs (non-overlapping calendar blocks resampled with replacement). S3's empirical "
          "cell and S7 use non-overlapping trades. S5 uses daily returns.",
          "- **Look-ahead.** Every condition at day t uses bars up to and including t, and outcomes start at "
          "t+1; in-sample outcome windows end by 2012-12-31, and every selection (S5's best rule, S7's best "
          "cell) uses in-sample data only. Two disclosed exceptions, neither of which reaches the out-of-sample "
          "tests: S2's volatility tercile cut-offs are fitted on the whole in-sample period, so the "
          "*in-sample* tercile of a day uses later in-sample data (the out-of-sample classification uses the "
          "frozen in-sample cut-offs, so it is real-time); and the bad-print filter looks at the next bar, "
          "as a cleaning step for data errors. S1's memoryless null is built from the same period's days; it "
          "is a yardstick, not a rule anyone could have traded.",
          ""]
    L += ["## Pre-registration", "",
          "The block below is copied from the top of `studies.py`. It was written before any study was run "
          "and is the full set of rules and parameters. The verdict rules are in the code next to each study "
          "and were also fixed in advance; the prose around the numbers was written after.", "",
          "```python", params_source(), "```", ""]
    if DEVIATIONS:
        L += ["**Deviations from the pre-registration**, made after results were seen:", ""]
        L += [f"- {d}" for d in DEVIATIONS] + [""]
    else:
        L += ["No parameter or rule was changed after the results were seen.", ""]
    findings = []
    for fn, args, sec in [
        (report_s1, (s1, "figures/s1_detour_curve.png"), "III; P2–P3"),
        (report_s2, (s2, "figures/s2_conditional_is_vs_oos.png"), "V, VI; P4"),
        (report_s3, (s3, s7, "figures/s3_law_of_large_numbers.png"), "VI (LLN); Q3"),
        (report_s4, (s4, "figures/s4_ruin.png"), "XIV; P9"),
        (report_s5, (s5, "figures/s5_overfitting.png"), "XVII, XX.4; P5"),
        (report_s6, (s6, "figures/s6_decision_vs_outcome.png"), "XI, XIII; P8"),
        (report_s7, (s7, s2, "figures/s7_costs.png"), "XIX Q4; P5"),
    ]:
        lines, finding = fn(*args)
        L += lines
        findings.append((sec, finding))
    verdicts = [s1["verdict"], s2["verdict"], s3["verdict"], s4["verdict"], s5["verdict"], s6["verdict"], s7["verdict"]]
    L += ["## Summary", ""]
    rows = []
    for i, ((sec, finding), v) in enumerate(zip(findings, verdicts), start=1):
        rows.append([f"S{i}", sec, v, finding])
    L += table(["study", "section", "verdict", "one-line finding"], rows, align="llll")
    L += ["*Supports* = the data behave as the section says; *qualifies* = they agree in part, or only under "
          "conditions the section does not state; *contradicts* = they behave otherwise. Verdict rules were "
          "fixed in advance (see the code). S3, S4 and S6 are mathematics about hypothetical strategies; "
          "S1, S2, S5 and S7 use market data.", ""]
    L += ["**What the lab as a whole does not show.** That any strategy is profitable. The studies test the "
          "philosophy's claims about evidence and method; they leave open questions 1, 2, 5 and 6 "
          "([[question_repeatable_behaviors]], [[question_define_conditions]], "
          "[[question_survives_regime_change]], [[question_consistent_execution]]) mostly open, with two "
          "periods and a handful of markets as the only evidence on persistence. Not a trading signal.", ""]
    REPORT.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    summary = list(zip([f"S{i}" for i in range(1, 8)], verdicts, [f for _, f in findings]))
    return summary


def main(argv: list[str] | None = None) -> int:
    global REFRESH
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--refresh", action="store_true", help="re-download the market data before running")
    args = ap.parse_args(argv)
    REFRESH = args.refresh
    t0 = time.time()
    s1 = s1_run()
    s2 = s2_run()
    s7 = s7_run(s2)
    s3 = s3_run(s7)
    s4 = s4_run()
    s5 = s5_run()
    s6 = s6_run()
    runtime = time.time() - t0
    summary = write_report(s1, s2, s3, s4, s5, s6, s7, runtime)
    log(f"wrote {REPORT.relative_to(REPO)} and {FIG_DIR.relative_to(REPO)}/ in {runtime:.1f} s")
    for sid, v, f in summary:
        log(f"  {sid} | {v} | {f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
