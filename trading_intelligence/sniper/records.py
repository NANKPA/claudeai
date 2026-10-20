"""Turn backtest trades into the setup records PhilosophyGate reads.

Discipline (Section XVII: separate developing a hypothesis from evaluating it):
- Trades are split by time: in-sample (IS) up to `split_date`, out-of-sample (OOS) after it.
- Which regimes and sessions the setup is allowed in is decided on IS only (n >= `min_cell` and a
  positive IS mean). OOS trades are then filtered by that IS choice and never used to choose it.
- The record handed to the gate is the OOS trades inside the IS-chosen conditions, as net R
  multiples with their average cost; the gate then applies n >= 30, mean - 1 SE and the rest.
- Every configuration tried is counted, so the report can deflate the best result for the number
  of trials (Bailey & Lopez de Prado).
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

from ..gate import SetupRecord


def choose_conditions(is_trades: pd.DataFrame, min_cell: int = 20) -> tuple[list[str], list[str]]:
    def good(col):
        g = is_trades.groupby(col)["net_r"].agg(["count", "mean"])
        keep = g[(g["count"] >= min_cell) & (g["mean"] > 0)].index.astype(str)
        return sorted(x for x in keep if x != "unclear")            # the gate never trades an unclear regime
    if is_trades.empty:
        return [], []
    return good("regime"), good("session")


def build_record(trades: pd.DataFrame, setup_key: str, split_date: str, min_cell: int = 20) -> dict:
    """Return {'record': SetupRecord kwargs, 'is': stats, 'oos': stats, 'oos_unfiltered': stats}."""
    t = trades.copy()
    if t.empty:
        return {"setup_key": setup_key, "is": {"n": 0}, "oos": {"n": 0}, "oos_unfiltered": {"n": 0}, "record": None}
    cut = pd.Timestamp(split_date, tz="UTC")
    is_t, oos_t = t[t["signal_time"] < cut], t[t["signal_time"] >= cut]
    regimes, sessions = choose_conditions(is_t, min_cell)
    is_f = is_t[is_t["regime"].isin(regimes) & is_t["session"].isin(sessions)]
    oos_f = oos_t[oos_t["regime"].isin(regimes) & oos_t["session"].isin(sessions)]
    rec = None
    if regimes and sessions and len(oos_f):
        st = stats(oos_f)
        rec = {"setup_id": setup_key, "results_r": [round(float(x), 5) for x in oos_f["net_r"]],
               "avg_cost_r": round(float(oos_f["cost_r"].mean()), 5), "out_of_sample": True, "source": "own",
               "valid_regimes": regimes, "valid_sessions": sessions}
        if effective_n(st) < st["n"]:
            rec["effective_n"] = effective_n(st)                                 # design effect of same-day clustering
    oos_end = pd.Timestamp(oos_t["signal_time"].max()).isoformat() if len(oos_t) else None
    return {"setup_key": setup_key, "split_date": split_date, "oos_end": oos_end, "valid_regimes": regimes,
            "valid_sessions": sessions,
            "is": stats(is_f), "is_unfiltered": stats(is_t), "oos": stats(oos_f), "oos_unfiltered": stats(oos_t),
            "record": rec}


def stats(t: pd.DataFrame) -> dict:
    if t.empty:
        return {"n": 0}
    r = t["net_r"].to_numpy(dtype=float)
    n = len(r)
    sd = float(r.std(ddof=1)) if n > 1 else float("nan")
    se = sd / math.sqrt(n) if n > 1 else float("nan")
    days = max((t["exit_time"].max() - t["entry_time"].min()).total_seconds() / 86400, 1.0)
    # trades on the same day (and across correlated coins) are not independent: cluster the SE by day
    dev = pd.Series(r - r.mean(), index=pd.to_datetime(t["signal_time"]).dt.floor("D").to_numpy())
    g = dev.groupby(level=0).sum().to_numpy()
    G = len(g)                                # cluster-robust SE of the mean, with the G/(G-1) small-sample factor
    se_day = float(np.sqrt((g ** 2).sum() * G / (G - 1)) / n) if G > 1 else float("nan")
    return {"n": n, "per_day": round(n / days, 3), "win_rate": round(float((r > 0).mean()), 4),
            "se_day": round(se_day, 4) if math.isfinite(se_day) else None,
            "t_day": round(float(r.mean()) / se_day, 2) if math.isfinite(se_day) and se_day > 0 else None,
            "mean_net_r": round(float(r.mean()), 4), "se": round(se, 4) if math.isfinite(se) else None,
            "t": round(float(r.mean()) / se, 2) if se and math.isfinite(se) and se > 0 else None,
            "mean_gross_r": round(float(t["gross_r"].mean()), 4), "mean_cost_r": round(float(t["cost_r"].mean()), 4),
            "median_stop_pct": round(float(t["stop_pct"].median()), 5), "sum_net_r": round(float(r.sum()), 2),
            "sharpe_per_trade": round(float(r.mean()) / sd, 4) if sd and math.isfinite(sd) and sd > 0 else None}


def to_setup_record(entry: dict) -> SetupRecord | None:
    rec = entry.get("record")
    return SetupRecord(**rec) if rec else None


def save(records: list[dict], path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(records, indent=1, default=str), encoding="utf-8")


def load(path: str | Path) -> dict[str, dict]:
    return {e["setup_key"]: e for e in json.loads(Path(path).read_text(encoding="utf-8"))}


def deflated_best(entries: list[dict], key: str = "oos") -> dict:
    """Probability that the best OOS per-trade Sharpe is real after all the trials.

    Every configuration tried counts as a trial (including those too thin to judge); the spread of
    Sharpe ratios across trials comes from the configurations with at least 30 OOS trades."""
    from .._paths import ensure_tools_on_path
    ensure_tools_on_path()
    import edge_lab as el  # type: ignore
    ok = [e for e in entries if effective_n(e[key]) >= 30 and e[key].get("sharpe_per_trade") is not None]
    srs = [e[key]["sharpe_per_trade"] for e in ok]
    trials = max(len(entries), len(srs))
    if len(srs) < 2:
        return {"trials": trials, "judged": len(srs)}
    best = max(ok, key=lambda e: e[key]["sharpe_per_trade"])
    n_eff = effective_n(best[key])            # same-day trades are not independent observations
    dsr = el.deflated_sharpe_ratio(best[key]["sharpe_per_trade"], n_eff, 0.0, 3.0, trials, float(np.var(srs)))
    return {"trials": trials, "judged": len(srs), "best": best["setup_key"], "best_sharpe_per_trade": best[key]["sharpe_per_trade"],
            "best_n": best[key]["n"], "best_effective_n": n_eff, "deflated_sharpe_prob": round(float(dsr), 4)}


def effective_n(st: dict) -> int:
    """n shrunk by the day clustering: n x (SE per trade / SE clustered by day)^2 when clustering widens the SE."""
    n = int(st.get("n", 0) or 0)
    se, se_day = st.get("se"), st.get("se_day")
    if n and se and se_day and se_day > se:
        return int(n * (se / se_day) ** 2)
    return n
