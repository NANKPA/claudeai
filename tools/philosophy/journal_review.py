#!/usr/bin/env python3
"""Journal review: turn a trading-journal CSV into a markdown review.

Serves Section XVI of "The Philosophy of the Relationship" (the trading
journal as a record of understanding) and the sections it feeds: IX (not
trading is a decision), VI (probability is conditional), VII (expected
value), XI (decision quality vs outcome; is a losing run normal?), XII
(protect the process), XIV (capital preservation) and X (when the evidence
changes).

Usage
-----
    python3 tools/philosophy/journal_review.py JOURNAL.csv
    python3 tools/philosophy/journal_review.py JOURNAL.csv --out /tmp/review.md

The CSV must use the journal-template columns listed in ``EXPECTED_COLUMNS``.
Missing columns are added as empty (and reported); blank cells are fine.

Reading conventions (those of trading-intelligence/00_philosophy/journal-template.md):

* ``decision``: take / skip / wait (synonyms such as enter, pass, watch are
  mapped). Only "take" rows with a numeric ``result_r`` are closed trades.
  A ``result_r`` on a skip or wait row is treated as a counterfactual and is
  never mixed into the statistics.
* ``na`` (also n/a, null, -) in any cell means "not applicable" and is read
  as blank; ``none`` in ``hypothesis_update`` means no update.
* ``result_r`` is the net R result after costs (signed); ``cost_r``,
  ``mae_r`` and ``mfe_r`` are positive magnitudes. A win is result_r > 0.
* ``est_win_prob`` is a decimal 0-1; 55 or 55% are also accepted.
* ``executed_per_plan``: y/yes/true/1 means followed; n/no/false/0/partial
  means deviated; na means no position.
* Emotion fields hold ``;``-separated tags; the template's green / amber /
  red vocabulary is used to group them.
* Gates (Section VIII: understanding + evidence + mathematics) pass when
  understanding_score, evidence_score and math_score are all at or above the
  gate minimum and the estimated EV, when recorded, is positive. The decision
  protocol (trading-intelligence/00_philosophy/decision-protocol.md, Gate 4)
  scores each from 0 to 2 and continues only on 2/2/2, so the default minimum
  is 2; scores on a wider scale (up to 3, 5, 10 or 100) get 60% of that scale.

Education, not financial advice: the review describes the journal's own
records, with their uncertainty; it is not a statement about future results.
"""
from __future__ import annotations

import argparse
import math
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
import pandas as pd

try:  # imported as part of the tools.philosophy package
    from . import edge_lab as el
except ImportError:  # run as a script: python3 tools/philosophy/journal_review.py
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import edge_lab as el  # type: ignore[no-redef]

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = REPO_ROOT / "trading-intelligence" / "00_philosophy" / "journal-review.md"

EXPECTED_COLUMNS: tuple[str, ...] = (
    "trade_id", "decided_at", "instrument", "timeframe", "setup_id", "regime_tag", "session",
    "observation", "interpretation", "hypothesis", "invalidation", "evidence_for",
    "evidence_against", "understanding_score", "evidence_score", "math_score", "est_win_prob",
    "est_avg_win_r", "est_avg_loss_r", "est_cost_r", "est_ev_r", "decision", "planned_entry",
    "planned_stop", "planned_target", "risk_pct", "position_size", "emotional_state_pre",
    "executed_per_plan", "exit_reason", "result_r", "cost_r", "mae_r", "mfe_r",
    "emotional_state_during", "outcome_within_expected", "lesson", "hypothesis_update",
    "reviewed_at",
)
NUMERIC_COLUMNS: tuple[str, ...] = (
    "understanding_score", "evidence_score", "math_score", "est_win_prob", "est_avg_win_r",
    "est_avg_loss_r", "est_cost_r", "est_ev_r", "planned_entry", "planned_stop", "planned_target",
    "risk_pct", "position_size", "result_r", "cost_r", "mae_r", "mfe_r",
)
SCORE_COLUMNS: tuple[str, ...] = ("understanding_score", "evidence_score", "math_score")
PRE_DECISION_FIELDS: tuple[str, ...] = ("observation", "interpretation", "hypothesis", "invalidation",
                                        "est_win_prob")

_DECISION_WORDS = {
    "take": {"take", "taken", "trade", "traded", "enter", "entered", "entry", "long", "short", "buy",
             "sell", "go", "yes", "y"},
    "skip": {"skip", "skipped", "pass", "passed", "no trade", "no-trade", "notrade", "no", "n",
             "reject", "rejected", "stand aside", "stand-aside", "avoid"},
    "wait": {"wait", "waiting", "watch", "watching", "standby", "stand-by", "defer", "deferred"},
}
_YES = {"y", "yes", "true", "1", "followed", "per plan"}
_NO = {"n", "no", "false", "0", "partial", "partly", "deviated"}
SMALL_N = 30
MISSING = "(unspecified)"
#: Cell values read as "not applicable" (the template writes `na` in categorical fields).
NA_TOKENS = {"na", "n/a", "nan", "null", "-"}
#: Emotion tag colours from the journal template's recommended vocabulary.
EMOTION_COLOURS = {
    "green": {"calm", "focused"},
    "amber": {"tired", "distracted", "anxious", "carryover"},
    "red": {"frustrated", "overconfident", "fomo", "revenge"},
}


# ---------------------------------------------------------------------------
# loading and preparation
# ---------------------------------------------------------------------------
def read_journal(path: str | Path) -> pd.DataFrame:
    """Read a journal CSV as text, add any missing template columns as empty.

    Blank cells and the template's "not applicable" markers (``na``, and
    ``none`` in hypothesis_update) become None. ``df.attrs["missing_columns"]``
    and ``df.attrs["extra_columns"]`` record what differed from the template.
    """
    try:
        raw = pd.read_csv(path, dtype=str, keep_default_na=False, skipinitialspace=True)
    except pd.errors.EmptyDataError:
        raw = pd.DataFrame(columns=list(EXPECTED_COLUMNS), dtype=str)
    raw.columns = [str(c).strip() for c in raw.columns]
    missing = [c for c in EXPECTED_COLUMNS if c not in raw.columns]
    extra = [c for c in raw.columns if c not in EXPECTED_COLUMNS]
    data: dict[str, pd.Series] = {}
    for c in EXPECTED_COLUMNS:
        if c in raw.columns:
            s = raw[c].astype(object).map(lambda v: v.strip() if isinstance(v, str) else v)
            blank_words = NA_TOKENS | ({"none"} if c == "hypothesis_update" else set())
            is_blank = s.map(lambda v: not isinstance(v, str) or v == "" or v.lower() in blank_words)
            data[c] = s.mask(is_blank.astype(bool), None)
        else:
            data[c] = pd.Series([None] * len(raw), index=raw.index, dtype=object)
    df = pd.DataFrame(data, index=raw.index)
    df.attrs["missing_columns"] = missing
    df.attrs["extra_columns"] = extra
    return df


def _to_number(s: pd.Series, percent_to_fraction: bool = False) -> pd.Series:
    text = s.astype(object).map(lambda v: v if isinstance(v, str) else ("" if v is None else str(v)))
    had_pct = text.str.contains("%", regex=False)
    num = pd.to_numeric(text.str.replace("%", "", regex=False).str.replace(",", "", regex=False)
                        .str.strip().replace("", np.nan), errors="coerce").astype(float)
    if percent_to_fraction:
        num = num.where(~(had_pct | (num > 1.0)), num / 100.0)
    return num


def _normalise_decision(v: object) -> str:
    if not isinstance(v, str) or not v.strip():
        return "blank"
    t = re.sub(r"\s+", " ", v.strip().lower())
    for label, words in _DECISION_WORDS.items():
        if t in words:
            return label
    return "other"


def _yes_no(v: object) -> float:
    if not isinstance(v, str) or not v.strip():
        return float("nan")
    t = v.strip().lower()
    if t in _YES:
        return 1.0
    if t in _NO:
        return 0.0
    return float("nan")


def infer_gate_min(df: pd.DataFrame) -> float:
    """Minimum score for a gate to pass, inferred from the recorded scores.

    The decision protocol's Gate 4 scale is 0-2 and only 2/2/2 continues, so
    scores that never exceed 2 (or no scores at all) give 2. Wider scales get
    60% of the scale, rounded up: 1-3 -> 2, 1-5 -> 3, 1-10 -> 6, 0-100 -> 60.
    """
    vals = pd.concat([_to_number(df[c]) for c in SCORE_COLUMNS]).dropna()
    if vals.empty or float(vals.max()) <= 2.0:
        return 2.0
    mx = float(vals.max())
    for scale in (3.0, 5.0, 10.0, 100.0):
        if mx <= scale:
            break
    else:
        scale = mx
    return float(math.ceil(0.6 * scale))


def prepare_journal(df: pd.DataFrame, gate_min: float | None = None) -> pd.DataFrame:
    """Add typed and derived columns (prefixed with "_") used by the review.

    Derived: _decision, _taken, _result, _closed, _win, _est_p, _est_ev,
    _est_ev_computed, _plan (1/0/NaN), _gates (1/0/NaN), _process,
    _when, _reviewed, and numeric copies of the numeric template columns
    (prefixed "_n_").
    """
    out = df.copy()
    for c in EXPECTED_COLUMNS:
        if c not in out.columns:
            out[c] = None
    for c in NUMERIC_COLUMNS:
        out["_n_" + c] = _to_number(out[c], percent_to_fraction=(c == "est_win_prob"))
    out["_decision"] = out["decision"].map(_normalise_decision)
    out["_taken"] = out["_decision"] == "take"
    out["_result"] = out["_n_result_r"]
    out["_closed"] = out["_taken"] & out["_result"].notna()
    out["_win"] = np.where(out["_closed"], (out["_result"] > 0).astype(float), np.nan)
    out["_est_p"] = out["_n_est_win_prob"].where(out["_n_est_win_prob"].between(0, 1))

    est_ev = out["_n_est_ev_r"].copy()
    can = est_ev.isna() & out["_est_p"].notna() & out["_n_est_avg_win_r"].notna() & out["_n_est_avg_loss_r"].notna()
    computed = (out["_est_p"] * out["_n_est_avg_win_r"]
                - (1 - out["_est_p"]) * out["_n_est_avg_loss_r"].abs()
                - out["_n_est_cost_r"].fillna(0.0))
    out["_est_ev"] = est_ev.where(~can, computed)
    out["_est_ev_computed"] = can

    out["_plan"] = out["executed_per_plan"].map(_yes_no).astype(float)
    gmin = infer_gate_min(out) if gate_min is None else float(gate_min)
    scores = out[["_n_" + c for c in SCORE_COLUMNS]]
    assessed = scores.notna().any(axis=1)
    all_pass = (scores >= gmin).all(axis=1)
    ev_ok = out["_est_ev"].isna() | (out["_est_ev"] > 0)
    out["_gates"] = np.where(assessed, (all_pass & ev_ok).astype(float), np.nan)
    followed = (out["_plan"] == 1) & (out["_gates"] == 1)
    not_followed = (out["_plan"] == 0) | (out["_gates"] == 0)
    out["_process"] = np.select([followed, not_followed], ["followed", "not followed"], "unknown")

    out["_when"] = pd.to_datetime(out["decided_at"], errors="coerce", utc=True, format="mixed")
    out["_reviewed"] = pd.to_datetime(out["reviewed_at"], errors="coerce", utc=True, format="mixed")
    out.attrs = dict(df.attrs)
    out.attrs["gate_min"] = gmin
    return out


def load_journal(path: str | Path, gate_min: float | None = None) -> pd.DataFrame:
    """read_journal followed by prepare_journal."""
    return prepare_journal(read_journal(path), gate_min=gate_min)


# ---------------------------------------------------------------------------
# analyses (each returns data; rendering happens in build_review)
# ---------------------------------------------------------------------------
def closed_trades(pj: pd.DataFrame) -> pd.DataFrame:
    """Taken trades with a numeric result, in decision order (stable)."""
    c = pj[pj["_closed"]].copy()
    c["_pos"] = np.arange(len(c))
    return c.sort_values(["_when", "_pos"], na_position="last", kind="mergesort")


def brier_score(est_p: Iterable[float], outcome: Iterable[float]) -> float:
    """Mean squared error of probability estimates against 0/1 outcomes (Section XVI)."""
    p = np.asarray(list(est_p), dtype=float)
    y = np.asarray(list(outcome), dtype=float)
    ok = np.isfinite(p) & np.isfinite(y)
    if not ok.any():
        return float("nan")
    return float(np.mean((p[ok] - y[ok]) ** 2))


CAL_EDGES = (0.0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0 + 1e-9)


def calibration_table(pj: pd.DataFrame, conf: float = 0.95) -> pd.DataFrame:
    """Estimated vs realised win rate by band of est_win_prob (closed trades)."""
    c = pj[pj["_closed"] & pj["_est_p"].notna()]
    cols = ["band", "n", "mean_est", "realised", "ci_low", "ci_high", "gap"]
    if c.empty:
        return pd.DataFrame(columns=cols)
    bands = pd.cut(c["_est_p"], bins=list(CAL_EDGES), right=False)
    rows = []
    for interval, g in c.groupby(bands, observed=True):
        n = len(g)
        w = int(g["_win"].sum())
        lo, hi = el.wilson_interval(w, n, conf)
        hi_edge = min(1.0, interval.right)
        rows.append({"band": f"{interval.left:.2f}-{hi_edge:.2f}", "n": n, "mean_est": g["_est_p"].mean(),
                     "realised": w / n, "ci_low": lo, "ci_high": hi, "gap": w / n - g["_est_p"].mean()})
    return pd.DataFrame(rows, columns=cols)


def decision_quality_matrix(pj: pd.DataFrame) -> pd.DataFrame:
    """Process (followed / not followed / unknown) x outcome (win / loss) on closed trades (Section XI)."""
    c = pj[pj["_closed"]]
    rows = []
    for proc in ("followed", "not followed", "unknown"):
        g = c[c["_process"] == proc]
        wins = g[g["_win"] == 1]["_result"]
        losses = g[g["_win"] == 0]["_result"]
        rows.append({"process": proc, "win_n": len(wins), "win_mean_r": wins.mean() if len(wins) else np.nan,
                     "loss_n": len(losses), "loss_mean_r": losses.mean() if len(losses) else np.nan,
                     "total_n": len(g), "mean_r": g["_result"].mean() if len(g) else np.nan})
    return pd.DataFrame(rows).set_index("process")


def split_tags(v: object) -> list[str]:
    """Split an emotion field such as "calm; focused" into lower-case tags."""
    if not isinstance(v, str) or not v.strip():
        return []
    return [t.strip().lower() for t in re.split(r"[;,|/]+", v) if t.strip()]


def emotion_colour(v: object) -> str | None:
    """Colour band of an emotion field: the worst of its tags (red > amber > green), or "other"."""
    tags = split_tags(v)
    if not tags:
        return None
    for colour in ("red", "amber", "green"):
        if any(t in EMOTION_COLOURS[colour] for t in tags):
            return colour
    return "other"


def tag_stats(pj: pd.DataFrame, column: str) -> pd.DataFrame:
    """Per-tag n, win rate, mean R and plan adherence for an emotion column (Section XII)."""
    c = pj[pj["_closed"]]
    rows = []
    exploded = [(t, i) for i, v in c[column].items() for t in split_tags(v)]
    if not exploded:
        return pd.DataFrame(columns=["tag", "n", "win_rate", "mean_r", "plan_followed"])
    tags = pd.DataFrame(exploded, columns=["tag", "idx"])
    for tag, g in tags.groupby("tag"):
        sub = c.loc[g["idx"].unique()]
        plan = sub["_plan"].dropna()
        rows.append({"tag": tag, "n": len(sub), "win_rate": sub["_win"].mean(), "mean_r": sub["_result"].mean(),
                     "plan_followed": plan.mean() if len(plan) else np.nan})
    return pd.DataFrame(rows).sort_values(["n", "tag"], ascending=[False, True], kind="mergesort")


def setup_consistency(pj: pd.DataFrame, window: int = 20, min_ref: int = 10,
                      seed: int = 0) -> list[dict[str, object]]:
    """consistency_check of each setup's latest ``window`` trades against its earlier ones (Section XI)."""
    c = closed_trades(pj)
    keys = c["setup_id"].fillna(MISSING)
    out: list[dict[str, object]] = []
    for setup in sorted(keys.unique()):
        r = c.loc[keys == setup, "_result"].to_numpy(dtype=float)
        item: dict[str, object] = {"setup_id": setup, "n": int(r.size)}
        if r.size < window + min_ref:
            item["report"] = None
            item["reason"] = (f"needs at least {window + min_ref} closed trades "
                              f"({window} recent + {min_ref} reference); has {r.size}")
        else:
            ref, recent = r[:-window], r[-window:]
            ref_sd = float(ref.std(ddof=1)) if ref.size > 1 else float("nan")
            item["ref_n"] = int(ref.size)
            item["ref_p_win"] = float((ref > 0).mean())
            item["ref_mean_r"] = float(ref.mean())
            item["report"] = el.consistency_check(recent, item["ref_p_win"], item["ref_mean_r"], ref_sd,
                                                  ref_results=ref, seed=seed)
        out.append(item)
    return out


# ---------------------------------------------------------------------------
# rendering helpers
# ---------------------------------------------------------------------------
def _finite(x: object) -> bool:
    try:
        return x is not None and math.isfinite(float(x))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return False


def _pct(x: object, nd: int = 1) -> str:
    return f"{100 * float(x):.{nd}f}%" if _finite(x) else "n/a"


def _r(x: object, nd: int = 2) -> str:
    return f"{float(x):+.{nd}f}R" if _finite(x) else "n/a"


def _num(x: object, nd: int = 3) -> str:
    return f"{float(x):.{nd}f}" if _finite(x) else "n/a"


def _ci_pct(lo: object, hi: object) -> str:
    return f"[{_pct(lo)}, {_pct(hi)}]" if _finite(lo) and _finite(hi) else ""


def _ci_r(lo: object, hi: object) -> str:
    return f"[{_r(lo)}, {_r(hi)}]" if _finite(lo) and _finite(hi) else ""


def _cell(v: object, limit: int = 160) -> str:
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return ""
    s = re.sub(r"\s+", " ", str(v)).strip().replace("|", "\\|")
    return s if len(s) <= limit else s[: limit - 1].rstrip() + "…"


def _table(headers: Sequence[str], rows: Iterable[Sequence[object]]) -> list[str]:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(v) for v in row) + " |")
    return lines


def _small(n: int) -> str:
    return " †" if n < SMALL_N else ""


# ---------------------------------------------------------------------------
# review sections
# ---------------------------------------------------------------------------
def _section_decisions(pj: pd.DataFrame) -> list[str]:
    n = len(pj)
    counts = pj["_decision"].value_counts()
    lines = ["## 1. Decisions: not trading is a decision (Section IX)", ""]
    if n == 0:
        return lines + ["The journal has no rows yet.", ""]
    order = ["take", "skip", "wait", "other", "blank"]
    labels = {"take": "take", "skip": "skip", "wait": "wait", "other": "other (unrecognised value)",
              "blank": "decision not recorded"}
    lines += _table(["Decision", "Rows", "Share"],
                    [(labels[k], int(counts.get(k, 0)), _pct(counts.get(k, 0) / n))
                     for k in order if counts.get(k, 0)])
    taken = int(pj["_taken"].sum())
    closed = int(pj["_closed"].sum())
    stood_aside = int(counts.get("skip", 0) + counts.get("wait", 0))
    lines += ["", f"- {n} recorded decisions; {stood_aside} of them ({_pct(stood_aside / n)}) were to skip or "
                  f"wait. Standing aside is logged as a decision, not as an absence of one.",
              f"- {taken} taken: {closed} with a recorded result, {taken - closed} still open or not yet reviewed."]
    cf = pj[~pj["_taken"] & pj["_result"].notna()]
    if len(cf):
        lines.append(f"- {len(cf)} skip/wait rows carry a `result_r` (a counterfactual: what the idea would have "
                     f"done). Mean {_r(cf['_result'].mean())}. They are excluded from every statistic below.")
    lines.append("")
    return lines


def _section_overall(pj: pd.DataFrame) -> list[str]:
    c = pj[pj["_closed"]]
    lines = ["## 2. Overall results (Sections VI and VII)", ""]
    if c.empty:
        return lines + ["No closed trades with a numeric `result_r` yet.", ""]
    ex = el.expectancy_from_results(c["_result"].to_numpy())
    wins = int((c["_result"] > 0).sum())
    lo, hi = el.wilson_interval(wins, ex.n)
    payoff = ex.avg_win / ex.avg_loss if ex.avg_loss > 0 else float("nan")
    rows: list[tuple[str, str]] = [
        ("Closed trades", f"{ex.n}{_small(ex.n)}"),
        ("Win rate (95% Wilson CI)", f"{_pct(ex.win_rate)} {_ci_pct(lo, hi)}"),
        ("Expectancy, mean R (95% t CI)", f"{_r(ex.mean, 3)} {_ci_r(ex.ci_low, ex.ci_high)}"),
        ("SD of R / t-stat / p-value", f"{_num(ex.sd, 2)} / {_num(ex.t_stat, 2)} / {_num(ex.p_value, 3)}"),
        ("Average win / average loss", f"{_r(ex.avg_win) if wins else 'n/a'} / "
                                       f"{_r(-ex.avg_loss) if wins < ex.n else 'n/a'}"),
        ("Total R", _r(ex.total)),
    ]
    cost = c["_n_cost_r"].dropna()
    if len(cost):
        rows.append(("Mean recorded cost per trade (already inside result_r)", f"{cost.mean():.3f}R"))
    if _finite(payoff) and payoff > 0:
        be = el.breakeven_win_rate(payoff)
        post = el.beta_posterior(wins, ex.n, threshold=min(be, 1.0))
        rows.append(("Breakeven win rate at the observed payoff", _pct(be)))
        rows.append(("P(true win rate > breakeven), Beta(1,1) posterior", _num(post.prob_above_threshold)))
        p_obs = min(max(ex.win_rate, 1e-9), 1 - 1e-9)
        plan = el.trades_needed(p_obs, payoff)
        rows.append(("Trades needed for a 95% CI on expectancy to exclude 0 (80% power), if the observed "
                     "p and payoff were true", "not reachable (no edge at these values)"
                     if not math.isfinite(plan.n_expectancy) else f"{int(plan.n_expectancy)}"))
    lines += _table(["Measure", "Value"], rows)
    lines.append("")
    if not (_finite(ex.ci_low) and _finite(ex.ci_high)):
        lines.append("Reading: too few trades for an interval. One or two outcomes say almost nothing about an "
                     "edge (Section VI, the law of large numbers).")
    elif ex.ci_low > 0:
        lines.append("Reading: the expectancy interval sits above zero on this sample. That is evidence, not "
                     "proof; it holds only for the conditions these trades were taken in (Section VI).")
    elif ex.ci_high < 0:
        lines.append("Reading: the expectancy interval sits below zero. On this evidence the method, as "
                     "executed, loses on average; investigate before risking more (Sections X and XVII).")
    else:
        lines.append("Reading: the expectancy interval includes zero. On this sample an edge cannot yet be "
                     "told apart from noise (Section VI, the law of large numbers).")
    mae, mfe = c["_n_mae_r"].abs(), c["_n_mfe_r"].abs()  # the template records magnitudes
    has_exc = mae.notna() | mfe.notna()
    if has_exc.any():
        parts = []
        for lab, mask in (("winners", c["_win"] == 1), ("losers", c["_win"] == 0)):
            m = mask & has_exc
            if m.any():
                parts.append(f"{lab}: MAE {_num(mae[m].median(), 2)}R, MFE {_num(mfe[m].median(), 2)}R (n={int(m.sum())})")
        lines += ["", "Path (median excursions, as magnitudes in R; protocol Gate 2 uses winners' MAE as the normal "
                      "C-band): " + "; ".join(parts)]
        lost_after_1r = int(((c["_win"] == 0) & (mfe >= 1.0)).sum())
        if lost_after_1r:
            lines.append(f"- Losing trades that first moved at least 1R in favour: {lost_after_1r} "
                         f"(a management and target question, not an entry question).")
    big_losses = c[c["_result"] < -1.0]["_result"]
    if len(big_losses):
        lines.append(f"- Losses larger than 1R net of costs: {len(big_losses)} (largest {_r(big_losses.min())}). "
                     "Slippage, costs or a moved stop?")
    lines.append("")
    return lines


def _conditional_table(pj: pd.DataFrame, by: str | list[str]) -> list[str]:
    c = pj[pj["_closed"]]
    stats = el.conditional_stats(c, "_result", by)
    if stats.empty:
        return ["No closed trades.", ""]
    keys = [by] if isinstance(by, str) else by
    rows = []
    for _, s in stats.iterrows():
        n = int(s["n"])
        rows.append([" / ".join(str(s[k]) for k in keys), f"{n}{_small(n)}",
                     f"{_pct(s['win_rate'])} {_ci_pct(s['win_ci_low'], s['win_ci_high'])}",
                     f"{_r(s['mean_r'])} {_ci_r(s['mean_ci_low'], s['mean_ci_high'])}",
                     _r(s["expectancy_r"]), _r(s["total_r"])])
    return _table([" / ".join(keys), "n", "Win rate [95% CI]", "Mean R [95% CI]", "Expectancy", "Total R"],
                  rows) + [""]


def _section_conditional(pj: pd.DataFrame) -> list[str]:
    lines = ["## 3. Results by condition: probability is conditional (Section VI)", "",
             "Each estimate below applies only to the condition it was measured in. "
             "† marks fewer than 30 trades: read those rows as anecdotes, not estimates.", ""]
    for col, title in (("setup_id", "By setup"), ("regime_tag", "By regime"), ("session", "By session")):
        lines += [f"### {title} (`{col}`)", ""] + _conditional_table(pj, col)
        if col == "setup_id":
            lines += _sample_test_table(pj)
    lines += ["### By setup and regime", ""] + _conditional_table(pj, ["setup_id", "regime_tag"])
    return lines


def _sample_test_table(pj: pd.DataFrame) -> list[str]:
    """Decision protocol Gate 5.4 on the journal's own live record, per setup."""
    c = pj[pj["_closed"]]
    if c.empty:
        return []
    rows = []
    for setup, g in c.groupby(c["setup_id"].fillna(MISSING)):
        ex = el.expectancy_from_results(g["_result"].to_numpy())
        one = ex.mean - ex.se if _finite(ex.se) else float("nan")
        two = ex.mean - 2 * ex.se if _finite(ex.se) else float("nan")
        if ex.n < SMALL_N:
            reading = "below the n >= 30 floor: anecdote"
        elif _finite(two) and two > 0:
            reading = "mean - 2 SE > 0"
        elif _finite(one) and one > 0:
            reading = "mean - 1 SE > 0 only"
        else:
            reading = "conservative estimate <= 0"
        rows.append((setup, ex.n, _r(ex.mean, 3), _r(one, 3), _r(two, 3), reading))
    return (["Conservative estimates on this journal's live record (decision protocol, Gate 5.4: n >= 30 and "
             "mean R - 1 SE > 0 for `math_score` 2; mean R - 2 SE > 0 for full risk). Live trades are only one "
             "of the record types the protocol accepts.", ""]
            + _table(["Setup", "n", "Mean R", "Mean - 1 SE", "Mean - 2 SE", "Reading"], rows) + [""])


def _section_calibration(pj: pd.DataFrame) -> list[str]:
    lines = ["## 4. Calibration of probability estimates (Section XVI)", ""]
    c = pj[pj["_closed"] & pj["_est_p"].notna()]
    if c.empty:
        return lines + ["No closed trade has an `est_win_prob`; calibration cannot be measured yet.", ""]
    brier = brier_score(c["_est_p"], c["_win"])
    base = float(c["_win"].mean())
    ref = base * (1 - base)
    skill = 1 - brier / ref if ref > 0 else float("nan")
    lines += _table(["Measure", "Value"], [
        ("Closed trades with an estimate", f"{len(c)}{_small(len(c))}"),
        ("Mean estimated win probability", _pct(c["_est_p"].mean())),
        ("Realised win rate", _pct(base)),
        ("Brier score (0 = perfect; 0.25 = always saying 50%)", _num(brier)),
        ("Brier score of the base rate", _num(ref)),
        ("Skill vs base rate (1 - Brier / base-rate Brier)", _num(skill)),
    ])
    cal = calibration_table(pj)
    lines += ["", "By estimated band:", ""]
    lines += _table(["Estimated band", "n", "Mean estimate", "Realised [95% CI]", "Realised - estimate"],
                    [(r.band, f"{r.n}{_small(r.n)}", _pct(r.mean_est), f"{_pct(r.realised)} {_ci_pct(r.ci_low, r.ci_high)}",
                      f"{100 * r.gap:+.1f} pts") for r in cal.itertuples()])
    lo, hi = el.wilson_interval(int(c["_win"].sum()), len(c))
    mean_est = float(c["_est_p"].mean())
    lines.append("")
    if hi < mean_est:
        lines.append("Reading: estimates run above what happened, beyond sampling noise - the pattern Section XVI "
                     "warns about (calling a setup high-probability without the evidence for it).")
    elif lo > mean_est:
        lines.append("Reading: estimates run below what happened, beyond sampling noise (under-confidence).")
    else:
        lines.append("Reading: the average estimate is inside the realised win rate's interval; no "
                     "miscalibration is visible at this sample size.")
    lines.append("")
    return lines


def _section_ev(pj: pd.DataFrame) -> list[str]:
    lines = ["## 5. Estimated vs realised expected value (Section VII)", ""]
    c = pj[pj["_closed"] & pj["_est_ev"].notna()]
    if c.empty:
        return lines + ["No closed trade has an estimated EV (`est_ev_r`, or the estimates needed to compute "
                        "it).", ""]
    n_comp = int(c["_est_ev_computed"].sum())
    gap = el.expectancy_from_results((c["_result"] - c["_est_ev"]).to_numpy())
    real = el.expectancy_from_results(c["_result"].to_numpy())
    lines += _table(["Measure", "Value"], [
        ("Closed trades with an estimated EV", f"{len(c)}{_small(len(c))}"
         + (f" ({n_comp} computed from est_win_prob, est_avg_win_r, est_avg_loss_r, est_cost_r)" if n_comp else "")),
        ("Mean estimated EV", _r(c["_est_ev"].mean(), 3)),
        ("Mean realised R [95% CI]", f"{_r(real.mean, 3)} {_ci_r(real.ci_low, real.ci_high)}"),
        ("Realised minus estimated [95% CI]", f"{_r(gap.mean, 3)} {_ci_r(gap.ci_low, gap.ci_high)}"),
    ])
    cst = c[c["_n_cost_r"].notna() & c["_n_est_cost_r"].notna()]
    if len(cst):
        drift = cst["_n_cost_r"].mean() - cst["_n_est_cost_r"].mean()
        lines += ["", f"Costs: mean realised `cost_r` {cst['_n_cost_r'].mean():.3f}R against mean `est_cost_r` "
                      f"{cst['_n_est_cost_r'].mean():.3f}R (difference {drift:+.3f}R, n={len(cst)})."
                      + (" Realised costs run above the estimate." if drift > 0.005 else "")]
    lines += ["", "By setup:", ""]
    rows = []
    for setup, g in c.groupby(c["setup_id"].fillna(MISSING)):
        gx = el.expectancy_from_results((g["_result"] - g["_est_ev"]).to_numpy())
        if _finite(gx.ci_high) and gx.ci_high < 0:
            reading = "realised below estimate"
        elif _finite(gx.ci_low) and gx.ci_low > 0:
            reading = "realised above estimate"
        else:
            reading = "no clear gap at this n"
        rows.append((setup, f"{len(g)}{_small(len(g))}", _r(g["_est_ev"].mean()), _r(g["_result"].mean()),
                     f"{_r(gx.mean)} {_ci_r(gx.ci_low, gx.ci_high)}", reading))
    lines += _table(["Setup", "n", "Mean est. EV", "Mean realised R", "Gap [95% CI]", "Reading"], rows)
    lines += ["", "`result_r` is read as the net result after costs, so the gap includes any cost the "
                  "estimate left out.", ""]
    return lines


def _section_decision_quality(pj: pd.DataFrame) -> list[str]:
    gmin = pj.attrs.get("gate_min", float("nan"))
    lines = ["## 6. Decision quality vs outcome (Section XI)", "",
             f"Process followed = `executed_per_plan` is yes **and** the gates passed (understanding, evidence "
             f"and math scores all >= {gmin:g}, and the estimated EV positive when recorded). "
             "A loss after a sound process is not, by itself, a bad decision; a win after a broken one is not a "
             "good one. Cell names follow the decision protocol's Gate 8.2.", ""]
    c = pj[pj["_closed"]]
    if c.empty:
        return lines + ["No closed trades yet.", ""]
    m = decision_quality_matrix(pj)
    lines += _table(["Process", "Wins (mean R)", "Losses or scratches (mean R)", "All (mean R)"],
                    [(proc, f"{int(r.win_n)} ({_r(r.win_mean_r)})", f"{int(r.loss_n)} ({_r(r.loss_mean_r)})",
                      f"{int(r.total_n)} ({_r(r.mean_r)})") for proc, r in m.iterrows() if r.total_n])
    q = {
        "Earned (good decision, favourable outcome): repeat the process": m.loc["followed", "win_n"],
        "Variance (good decision, unfavourable outcome): accept it, no rule change": m.loc["followed", "loss_n"],
        "Lucky (poor decision, favourable outcome): treat as a mistake": m.loc["not followed", "win_n"],
        "Earned loss (poor decision, unfavourable outcome): fix the gate that was bent":
            m.loc["not followed", "loss_n"],
    }
    lines += [""] + [f"- {k}: {int(v)}" for k, v in q.items()]
    gate_fail = []
    for col in SCORE_COLUMNS:
        s = c["_n_" + col]
        gate_fail.append(f"{col.replace('_score', '')} {int((s < gmin).sum())}")
    neg_ev = int((c["_est_ev"] <= 0).sum())
    lines.append(f"- gate shortfalls on closed trades: {', '.join(gate_fail)}; estimated EV <= 0: {neg_ev}")
    unknown = int(m.loc["unknown", "total_n"])
    if unknown:
        lines.append(f"- {unknown} closed trades lack `executed_per_plan` or gate scores, so their process "
                     "cannot be judged.")
    lines.append("")
    return lines


def _section_process(pj: pd.DataFrame) -> list[str]:
    lines = ["## 7. Plan adherence and emotional state (Section XII)", ""]
    c = pj[pj["_closed"]]
    if c.empty:
        return lines + ["No closed trades yet.", ""]
    rows = []
    for lab, mask in (("followed the plan", c["_plan"] == 1), ("deviated", c["_plan"] == 0),
                      ("not recorded", c["_plan"].isna())):
        g = c[mask]
        if len(g):
            ex = el.expectancy_from_results(g["_result"].to_numpy())
            rows.append((lab, f"{len(g)}{_small(len(g))}", _pct(ex.win_rate),
                         f"{_r(ex.mean)} {_ci_r(ex.ci_low, ex.ci_high)}"))
    lines += ["### Executed per plan", ""] + _table(["Execution", "n", "Win rate", "Mean R [95% CI]"], rows) + [""]
    for col, title in (("emotional_state_pre", "Emotional state before the decision"),
                       ("emotional_state_during", "Emotional state during the trade")):
        ts = tag_stats(pj, col)
        lines += [f"### {title} (`{col}`)", ""]
        if ts.empty:
            lines += ["Not recorded.", ""]
            continue
        lines += _table(["Tag", "n", "Win rate", "Mean R", "Followed plan"],
                        [(r.tag, f"{r.n}{_small(r.n)}", _pct(r.win_rate), _r(r.mean_r), _pct(r.plan_followed))
                         for r in ts.itertuples()]) + [""]
    colour = c["emotional_state_pre"].map(emotion_colour)
    if colour.notna().any():
        rows = []
        for col_name in ("green", "amber", "red", "other"):
            g = c[colour == col_name]
            if len(g):
                plan = g["_plan"].dropna()
                rows.append((col_name, f"{len(g)}{_small(len(g))}", _pct(g["_win"].mean()), _r(g["_result"].mean()),
                             _pct(plan.mean()) if len(plan) else "n/a"))
        lines += ["### Pre-trade state by colour (worst tag wins; template vocabulary)", ""]
        lines += _table(["State", "n", "Win rate", "Mean R", "Followed plan"], rows) + [""]
    seq = closed_trades(pj)
    prev = seq["_win"].shift(1)
    rows = []
    for lab, mask in (("after a win", prev == 1), ("after a loss or scratch", prev == 0)):
        g = seq[mask]
        if len(g):
            plan = g["_plan"].dropna()
            rows.append((lab, f"{len(g)}{_small(len(g))}", _pct(g["_win"].mean()), _r(g["_result"].mean()),
                         _pct(plan.mean()) if len(plan) else "n/a"))
    if rows:
        lines += ["### Trades taken just after a win or a loss", ""]
        lines += _table(["Previous trade", "n", "Win rate", "Mean R", "Followed plan"], rows) + [""]
    ex_rows = []
    for reason, g in c.groupby(c["exit_reason"].fillna(MISSING)):
        ex_rows.append((reason, len(g), _r(g["_result"].mean())))
    lines += ["### Exit reasons", ""] + _table(["Exit reason", "n", "Mean R"],
                                               sorted(ex_rows, key=lambda t: -t[1])) + [""]
    owe = c["outcome_within_expected"].map(_yes_no)
    if owe.notna().any():
        lines.append(f"Outcome within the expected range (`outcome_within_expected`): yes {int((owe == 1).sum())}, "
                     f"no {int((owe == 0).sum())}, not recorded {int(owe.isna().sum())}.")
        lines.append("")
    return lines


def _section_consistency(pj: pd.DataFrame, window: int, min_ref: int) -> list[str]:
    lines = ["## 8. Recent results vs each setup's own history (Section XI)", "",
             f"The latest {window} closed trades of each setup are tested against that setup's earlier trades: "
             "binomial test on wins, z-test on mean R, exact losing-streak probability and a bootstrap "
             "percentile of the drawdown. The question is Section XI's: ordinary variation, or evidence that "
             "the assumptions no longer hold?", ""]
    items = setup_consistency(pj, window=window, min_ref=min_ref)
    if not items:
        return lines + ["No closed trades yet.", ""]
    rows = []
    notes = []
    for it in items:
        rep = it.get("report")
        if rep is None:
            notes.append(f"- `{it['setup_id']}`: {it['reason']}.")
            continue
        assert isinstance(rep, el.ConsistencyReport)
        dd = f"{rep.max_drawdown_r:.1f}R" + (f" (p{rep.drawdown_percentile:.0f})" if rep.drawdown_percentile is not None else "")
        rows.append((it["setup_id"], f"{rep.n} vs {it['ref_n']}",
                     f"{_pct(rep.win_rate)} vs {_pct(rep.ref_p_win)} (p={rep.p_value_wins:.3f})",
                     f"{_r(rep.mean_r)} vs {_r(rep.ref_mean_r)} (p={_num(rep.p_value_mean)})",
                     dd, f"{rep.longest_losing_streak} (p={rep.p_value_streak:.3f})",
                     rep.verdict if rep.verdict == el.VERDICT_WITHIN else f"{rep.verdict} ({rep.direction})"))
    if rows:
        lines += _table(["Setup", "Recent vs ref n", "Win rate (p)", "Mean R (p)", "Max DD (percentile)",
                         "Longest losing run (p)", "Verdict"], rows) + [""]
    lines += notes + ([""] if notes else [])
    return lines


def _section_risk(pj: pd.DataFrame) -> list[str]:
    lines = ["## 9. Risk and survival (Section XIV)", ""]
    c = pj[pj["_closed"]]
    risk = pj.loc[pj["_taken"], "_n_risk_pct"].dropna()
    if risk.empty and c.empty:
        return lines + ["No taken trades yet.", ""]
    if len(risk):
        f_max = float(risk.max()) / 100.0
        dmg = 1 - (1 - f_max) ** 10 if 0 < f_max < 1 else float("nan")
        lines.append(f"- Risk per trade (`risk_pct`): mean {risk.mean():.2f}%, max {risk.max():.2f}%; "
                     f"trades above 2%: {int((risk > 2).sum())}.")
        if _finite(dmg):
            lines.append(f"- Ten consecutive losses at the maximum risk would cost {_pct(dmg)} of equity and need "
                         f"a {_pct(el.recovery_required(dmg))} gain to recover.")
    if len(c) >= 2:
        r = closed_trades(pj)["_result"].to_numpy()
        streak = el.longest_losing_streak(r)
        p_loss = float((r <= 0).mean())
        if streak > 0 and 0 < p_loss < 1:
            p_now = el.prob_losing_streak(p_loss, streak, len(r))
            p_200 = el.prob_losing_streak(p_loss, streak, 200)
            lines.append(f"- Longest losing run so far: {streak} trades. With the observed loss rate "
                         f"({_pct(p_loss)}), a run at least that long has probability {p_now:.2f} in {len(r)} "
                         f"independent trades and {p_200:.2f} in 200: plan for it rather than be surprised by it.")
        lines.append(f"- Largest drawdown of the cumulative R curve: {el.max_drawdown_r(r):.1f}R.")
    lines.append("")
    return lines


def _section_hypotheses(pj: pd.DataFrame) -> list[str]:
    lines = ["## 10. Hypotheses whose evidence has changed (Sections X and XVI)", ""]
    h = pj[pj["hypothesis_update"].notna()]
    if h.empty:
        return lines + ["No `hypothesis_update` recorded.", ""]
    h = h.assign(_pos=np.arange(len(h))).sort_values(["_when", "_pos"], na_position="last", kind="mergesort")
    lines += _table(["Trade", "Decided", "Setup", "Decision", "Hypothesis", "Update"],
                    [(r["trade_id"], r["decided_at"], r["setup_id"], r["_decision"], _cell(r["hypothesis"], 120),
                      _cell(r["hypothesis_update"], 160)) for _, r in h.iterrows()])
    lines.append("")
    return lines


def _section_hygiene(pj: pd.DataFrame) -> list[str]:
    lines = ["## 11. Journal hygiene (Section XVI)", "",
             "Reasoning is only evidence if it was written before the outcome was known.", ""]
    t = pj[pj["_taken"]]
    if t.empty:
        return lines + ["No taken trades yet.", ""]
    rows = []
    for col in PRE_DECISION_FIELDS:
        missing = int(t[col].isna().sum())
        rows.append((f"`{col}` blank on taken trades", f"{missing} of {len(t)}"))
    early = pj[pj["_reviewed"].notna() & pj["_when"].notna() & (pj["_reviewed"] < pj["_when"])]
    rows.append(("`reviewed_at` earlier than `decided_at`",
                 f"{len(early)}" + (f" ({', '.join(map(str, early['trade_id'].fillna('?')))})" if len(early) else "")))
    c = pj[pj["_closed"]]
    rows.append(("Closed trades without `reviewed_at`", f"{int(c['reviewed_at'].isna().sum())} of {len(c)}"))
    rows.append(("Closed trades with a `lesson`", f"{int(c['lesson'].notna().sum())} of {len(c)}"))
    for label, mask in template_row_checks(pj).items():
        ids = pj.loc[mask, "trade_id"].fillna("?").astype(str).tolist()
        shown = ", ".join(ids[:8]) + (", ..." if len(ids) > 8 else "")
        rows.append((label, f"{len(ids)}" + (f" ({shown})" if ids else "")))
    lines += _table(["Check", "Count"], rows) + [""]
    return lines


def template_row_checks(pj: pd.DataFrame) -> dict[str, pd.Series]:
    """The journal template's per-row checks, as boolean masks of offending rows."""
    scores = pj[["_n_" + c for c in SCORE_COLUMNS]]
    est = pj["_n_est_ev_r"]
    formula = (pj["_est_p"] * pj["_n_est_avg_win_r"] - (1 - pj["_est_p"]) * pj["_n_est_avg_loss_r"].abs()
               - pj["_n_est_cost_r"].fillna(0.0))
    full = (scores == 2).all(axis=1)
    has_zero = (scores == 0).any(axis=1)
    pos_fields = ["_n_cost_r", "_n_mae_r", "_n_mfe_r", "_n_risk_pct", "_n_position_size"]
    stood_aside = pj["_decision"].isin(["skip", "wait"])
    return {
        "`est_ev_r` differs from the formula by more than 0.01": (est.notna() & formula.notna()
                                                               & ((est - formula).abs() > 0.01 + 1e-9)),
        "`take` without 2/2/2 scores and `est_ev_r` > 0 (impulse entries)": pj["_taken"] & ~(
            full & (pj["_est_ev"] > 0)),
        "a score of 0 but `decision` is not `skip`": has_zero & (pj["_decision"] != "skip"),
        "`skip`/`wait` rows carrying position fields": stood_aside & pj[pos_fields].notna().any(axis=1),
    }


def build_review(pj: pd.DataFrame, source: str = "journal.csv", window: int = 20, min_ref: int = 10,
                 generated_on: str | None = None) -> str:
    """Render the full markdown review of a prepared journal (see prepare_journal)."""
    date = generated_on or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lines = [
        "# Trading journal review",
        "",
        f"_Generated by `tools/philosophy/journal_review.py` from `{source}` on {date}._",
        "",
        "> Education, not financial advice. Every figure below describes this journal's own records, with its "
        "uncertainty; none of it is a statement about future results. Read it through *The Philosophy of the "
        "Relationship* (`trading-intelligence/00_philosophy/philosophy-of-the-relationship.md`): the purpose "
        "is not to prove the trader right but to find where understanding is accurate, where it is incomplete, "
        "and what evidence should change it (Section XVI).",
        "",
    ]
    missing = pj.attrs.get("missing_columns") or []
    extra = pj.attrs.get("extra_columns") or []
    if missing or extra:
        if missing:
            lines.append(f"- Columns missing from the CSV (treated as empty): {', '.join(f'`{c}`' for c in missing)}")
        if extra:
            lines.append(f"- Extra columns ignored: {', '.join(f'`{c}`' for c in extra)}")
        lines.append("")
    lines += _section_decisions(pj)
    lines += _section_overall(pj)
    lines += _section_conditional(pj)
    lines += _section_calibration(pj)
    lines += _section_ev(pj)
    lines += _section_decision_quality(pj)
    lines += _section_process(pj)
    lines += _section_consistency(pj, window, min_ref)
    lines += _section_risk(pj)
    lines += _section_hypotheses(pj)
    lines += _section_hygiene(pj)
    lines += [
        "## Method notes",
        "",
        "- Win = `result_r` > 0; only `decision` = take rows with a numeric `result_r` are counted as trades.",
        "- Win-rate intervals are Wilson score intervals; mean-R intervals use Student's t. "
        "Both assume trades are independent draws from one unchanging process - the very assumption "
        "sections 3 and 8 exist to question.",
        "- Calibration uses the Brier score; the base-rate Brier is the score of always forecasting the "
        "realised win rate.",
        "- Section 8 flags *unusual - investigate* when any test has p < 0.05 and *inconsistent* when the "
        "smallest p-value stays below 0.01 after a Bonferroni adjustment; better-than-reference runs are "
        "flagged too.",
        "- Functions: `tools/philosophy/edge_lab.py`.",
        "",
    ]
    return "\n".join(lines)


def write_review(journal: str | Path, out: str | Path | None = None, window: int = 20, min_ref: int = 10,
                 gate_min: float | None = None, generated_on: str | None = None) -> Path:
    """Read ``journal``, build the review and write it to ``out`` (default: DEFAULT_OUT)."""
    pj = load_journal(journal, gate_min=gate_min)
    text = build_review(pj, source=Path(journal).name, window=window, min_ref=min_ref,
                        generated_on=generated_on)
    out_path = Path(out) if out else DEFAULT_OUT
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    return out_path


def main(argv: Sequence[str] | None = None) -> int:
    """Command-line entry point."""
    ap = argparse.ArgumentParser(prog="journal_review", description=__doc__.split("\n\n")[0])
    ap.add_argument("journal", help="trading-journal CSV (journal-template columns)")
    ap.add_argument("--out", default=None, help=f"markdown output (default: {DEFAULT_OUT.relative_to(REPO_ROOT)})")
    ap.add_argument("--window", type=int, default=20, help="recent trades per setup for the consistency check")
    ap.add_argument("--min-ref", type=int, default=10, help="minimum earlier trades for a reference")
    ap.add_argument("--gate-min", type=float, default=None,
                    help="minimum understanding/evidence/math score for a gate to pass (default: inferred)")
    args = ap.parse_args(argv)
    path = write_review(args.journal, args.out, args.window, args.min_ref, args.gate_min)
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
