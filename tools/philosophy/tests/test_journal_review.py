"""Tests for tools/philosophy/journal_review.py on the synthetic fixture."""
import csv
import subprocess
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from tools.philosophy import edge_lab as el
from tools.philosophy import journal_review as jr

HERE = Path(__file__).resolve().parent
FIXTURE = HERE / "fixtures" / "journal_example.csv"
SCRIPT = HERE.parent / "journal_review.py"
TEMPLATE_CSV = HERE.parents[2] / "trading-intelligence" / "00_philosophy" / "journal-template.csv"
VERDICTS = (el.VERDICT_WITHIN, el.VERDICT_UNUSUAL, el.VERDICT_INCONSISTENT)


@pytest.fixture(scope="module")
def raw_rows():
    with FIXTURE.open(newline="") as fh:
        return list(csv.DictReader(fh))


@pytest.fixture(scope="module")
def pj():
    return jr.load_journal(FIXTURE)


@pytest.fixture(scope="module")
def review(pj):
    return jr.build_review(pj, source=FIXTURE.name, generated_on="2026-01-01")


def _closed(rows):
    return [r for r in rows if r["decision"] == "take" and r["result_r"].strip()]


# --------------------------------------------------------------------------- the fixture
def test_fixture_has_exactly_the_template_columns(raw_rows):
    with FIXTURE.open(newline="") as fh:
        header = next(csv.reader(fh))
    assert tuple(header) == jr.EXPECTED_COLUMNS
    assert len(jr.EXPECTED_COLUMNS) == 39
    assert len(raw_rows) == 60


def test_fixture_is_clearly_synthetic_with_mixed_decisions(raw_rows):
    assert all(r["trade_id"].startswith("SYN-") for r in raw_rows)
    assert all("SYNTHETIC" in r["instrument"] for r in raw_rows)
    assert all("[synthetic]" in r["observation"] for r in raw_rows)
    counts = Counter(r["decision"] for r in raw_rows)
    assert counts["take"] > 0 and counts["skip"] > 0 and counts["wait"] > 0


# --------------------------------------------------------------------------- loading
def test_load_journal_derives_decisions_and_closed_trades(pj, raw_rows):
    assert len(pj) == 60
    assert pj.attrs["missing_columns"] == [] and pj.attrs["extra_columns"] == []
    counts = Counter(r["decision"] for r in raw_rows)
    assert pj["_decision"].value_counts().to_dict() == dict(counts)
    assert int(pj["_closed"].sum()) == len(_closed(raw_rows))
    # counterfactual results on skip rows never count as trades
    cf = [r for r in raw_rows if r["decision"] != "take" and r["result_r"].strip()]
    assert cf and not pj.loc[pj["decision"] != "take", "_closed"].any()
    assert jr.infer_gate_min(pj) == 2.0  # decision protocol: 0-2 scale, 2/2/2 passes


def test_template_not_applicable_markers_are_blank(pj, raw_rows):
    # the template writes `na` in categorical fields and `none` in hypothesis_update
    assert any(r["executed_per_plan"] == "na" for r in raw_rows)
    assert any(r["hypothesis_update"] == "none" for r in raw_rows)
    aside = pj[pj["_decision"].isin(["skip", "wait"])]
    assert aside["executed_per_plan"].isna().all() and aside["exit_reason"].isna().all()
    assert aside["_plan"].isna().all()
    assert pj["hypothesis_update"].dropna().str.contains(":").all()
    assert "na" not in set(jr.tag_stats(pj, "emotional_state_during")["tag"])


def test_percent_win_probabilities_are_normalised(tmp_path):
    df = pd.read_csv(FIXTURE, dtype=str, keep_default_na=False).head(3)
    df.loc[0, "est_win_prob"] = "45%"
    df.loc[1, "est_win_prob"] = "60"
    df.loc[2, "est_win_prob"] = "0.5"
    path = tmp_path / "pct.csv"
    df.to_csv(path, index=False)
    est = jr.load_journal(path)["_est_p"].tolist()
    assert est == pytest.approx([0.45, 0.60, 0.50])


def test_missing_est_ev_is_computed_from_components(pj):
    comp = pj[pj["_est_ev_computed"]]
    assert len(comp) > 0
    for _, r in comp.iterrows():
        expected = el.expected_value(r["_est_p"], r["_n_est_avg_win_r"], r["_n_est_avg_loss_r"],
                                     r["_n_est_cost_r"])
        assert r["_est_ev"] == pytest.approx(expected)


# --------------------------------------------------------------------------- analyses
def test_brier_score():
    assert jr.brier_score([1.0, 0.0], [1, 0]) == 0.0
    assert jr.brier_score([0.5, 0.5], [1, 0]) == pytest.approx(0.25)
    assert np.isnan(jr.brier_score([np.nan], [1]))


def test_calibration_matches_manual_computation(pj, raw_rows, review):
    closed = _closed(raw_rows)
    p, y = [], []
    for r in closed:
        v = r["est_win_prob"]
        if v:
            x = float(v.rstrip("%"))
            p.append(x / 100 if (v.endswith("%") or x > 1) else x)
            y.append(1.0 if float(r["result_r"]) > 0 else 0.0)
    brier = float(np.mean((np.array(p) - np.array(y)) ** 2))
    assert jr.brier_score(pj.loc[pj["_closed"], "_est_p"], pj.loc[pj["_closed"], "_win"]) == pytest.approx(brier)
    assert f"| {brier:.3f} |" in review
    assert jr.calibration_table(pj)["n"].sum() == len(p)


def test_decision_quality_matrix_matches_manual_rule(pj, raw_rows):
    m = jr.decision_quality_matrix(pj)
    closed = _closed(raw_rows)
    assert int(m["total_n"].sum()) == len(closed)

    def est_ev(r):
        if r["est_ev_r"]:
            return float(r["est_ev_r"])
        x = float(r["est_win_prob"].rstrip("%"))
        p = x / 100 if (r["est_win_prob"].endswith("%") or x > 1) else x
        return p * float(r["est_avg_win_r"]) - (1 - p) * abs(float(r["est_avg_loss_r"])) - float(r["est_cost_r"])

    followed = [r for r in closed if r["executed_per_plan"] == "y"
                and all(float(r[c]) >= 2 for c in jr.SCORE_COLUMNS) and est_ev(r) > 0]
    assert int(m.loc["followed", "total_n"]) == len(followed)
    assert int(m.loc["followed", "win_n"]) == sum(float(r["result_r"]) > 0 for r in followed)
    assert int(m.loc["not followed", "total_n"]) == len(closed) - len(followed)


def test_setup_consistency_runs_on_the_largest_setup(pj):
    items = {it["setup_id"]: it for it in jr.setup_consistency(pj, window=20, min_ref=10)}
    big = items["concept_breakout_trading"]
    assert big["report"] is not None and big["report"].n == 20 and big["ref_n"] == big["n"] - 20
    assert big["report"].verdict in VERDICTS
    small = items["concept_liquidity_sweep_reversal"]
    assert small["report"] is None and "needs at least 30" in small["reason"]


def test_tag_stats_split_multi_tags(pj):
    ts = jr.tag_stats(pj, "emotional_state_pre").set_index("tag")
    assert "calm" in ts.index and "focused" in ts.index  # from "calm; focused"
    assert jr.split_tags(" Calm; focused | FOMO ") == ["calm", "focused", "fomo"]
    assert jr.split_tags(None) == []


# --------------------------------------------------------------------------- the review
def test_review_has_every_section(review):
    for heading in ("## 1. Decisions", "## 2. Overall results", "## 3. Results by condition",
                    "### By setup", "### By regime", "### By session", "## 4. Calibration",
                    "## 5. Estimated vs realised expected value", "## 6. Decision quality vs outcome",
                    "## 7. Plan adherence and emotional state", "## 8. Recent results",
                    "## 9. Risk and survival", "## 10. Hypotheses whose evidence has changed",
                    "## 11. Journal hygiene", "Education, not financial advice"):
        assert heading in review, heading
    for setup in ("concept_breakout_trading", "concept_mean_reversion", "concept_liquidity_sweep_reversal"):
        assert setup in review
    assert any(v in review for v in VERDICTS)
    assert "Earned loss" in review and "Lucky" in review and "Variance" in review


def test_review_counts_skip_and_wait_decisions(review, raw_rows):
    counts = Counter(r["decision"] for r in raw_rows)
    assert f"| skip | {counts['skip']} |" in review
    assert f"| wait | {counts['wait']} |" in review
    stood_aside = counts["skip"] + counts["wait"]
    assert f"{stood_aside} of them" in review
    assert "counterfactual" in review


def test_review_overall_expectancy_matches_edge_lab(review, raw_rows):
    r = [float(x["result_r"]) for x in _closed(raw_rows)]
    ex = el.expectancy_from_results(r)
    assert f"| Closed trades | {len(r)} |" in review
    assert f"{ex.mean:+.3f}R" in review


def test_review_lists_changed_hypotheses(review, raw_rows):
    updated = [r["trade_id"] for r in raw_rows if r["hypothesis_update"].strip() not in ("", "none")]
    assert updated
    section = review.split("## 10.")[1].split("## 11.")[0]
    for tid in updated:
        assert tid in section


def test_review_flags_hygiene_problems(review, pj):
    early = pj[pj["_reviewed"] < pj["_when"]]["trade_id"].tolist()
    assert early
    section = review.split("## 11.")[1]
    assert all(t in section for t in early)


def test_template_row_checks_match_manual_rules(pj, raw_rows):
    checks = jr.template_row_checks(pj)
    impulse = [r["trade_id"] for r in raw_rows if r["decision"] == "take" and not (
        all(r[c] == "2" for c in jr.SCORE_COLUMNS))]
    key = next(k for k in checks if "impulse" in k)
    assert sorted(pj.loc[checks[key], "trade_id"]) == sorted(impulse)
    assert impulse  # the fixture contains impulse entries on purpose
    zero_not_skip = [r for r in raw_rows if "0" in (r["understanding_score"], r["evidence_score"], r["math_score"])
                     and r["decision"] != "skip"]
    assert int(checks[next(k for k in checks if "score of 0" in k)].sum()) == len(zero_not_skip)
    assert int(checks[next(k for k in checks if "differs from the formula" in k)].sum()) == 0


def test_emotion_colour_uses_worst_tag():
    assert jr.emotion_colour("calm;focused") == "green"
    assert jr.emotion_colour("calm;anxious") == "amber"
    assert jr.emotion_colour("focused;fomo") == "red"
    assert jr.emotion_colour("curious") == "other"
    assert jr.emotion_colour(None) is None


def test_excursions_are_read_as_magnitudes(review):
    path_line = next(line for line in review.splitlines() if line.startswith("Path (median excursions"))
    assert "MAE -" not in path_line and "MFE -" not in path_line


@pytest.mark.skipif(not TEMPLATE_CSV.exists(), reason="journal template not present")
def test_reads_the_real_journal_template(tmp_path):
    with TEMPLATE_CSV.open(newline="") as fh:
        assert tuple(next(csv.reader(fh))) == jr.EXPECTED_COLUMNS
    pj = jr.load_journal(TEMPLATE_CSV)
    assert pj.attrs["missing_columns"] == [] and pj.attrs["extra_columns"] == []
    text = jr.build_review(pj, source=TEMPLATE_CSV.name)
    assert "## 11. Journal hygiene" in text


# --------------------------------------------------------------------------- robustness
def test_review_handles_empty_and_missing_columns(tmp_path):
    df = pd.read_csv(FIXTURE, dtype=str, keep_default_na=False)
    for col in ("est_win_prob", "est_ev_r", "emotional_state_pre", "emotional_state_during", "hypothesis_update",
                "executed_per_plan", "understanding_score", "evidence_score", "math_score", "regime_tag",
                "mae_r", "mfe_r", "risk_pct"):
        df[col] = ""
    df = df.drop(columns=["session", "lesson"]).assign(extra_note="x")
    path = tmp_path / "blank.csv"
    df.to_csv(path, index=False)
    pj = jr.load_journal(path)
    assert pj.attrs["missing_columns"] == ["session", "lesson"]
    assert pj.attrs["extra_columns"] == ["extra_note"]
    text = jr.build_review(pj, source=path.name)
    assert "Columns missing from the CSV" in text and "`extra_note`" in text
    assert "calibration cannot be measured yet" in text
    assert "No `hypothesis_update` recorded." in text
    assert "Not recorded." in text
    assert "(unspecified)" in text  # blank regime and missing session
    assert "process cannot be judged" in text


def test_review_of_header_only_journal(tmp_path):
    path = tmp_path / "empty.csv"
    path.write_text(",".join(jr.EXPECTED_COLUMNS) + "\n")
    text = jr.build_review(jr.load_journal(path), source=path.name)
    assert "The journal has no rows yet." in text
    assert "No closed trades with a numeric `result_r` yet." in text


def test_write_review_and_cli(tmp_path):
    out = tmp_path / "review.md"
    assert jr.write_review(FIXTURE, out, generated_on="2026-01-01") == out
    assert out.read_text().startswith("# Trading journal review")
    out2 = tmp_path / "cli.md"
    assert jr.main([str(FIXTURE), "--out", str(out2)]) == 0
    assert out2.exists()
    # run as a script (exercises the non-package import path)
    out3 = tmp_path / "script.md"
    proc = subprocess.run([sys.executable, str(SCRIPT), str(FIXTURE), "--out", str(out3), "--window", "15"],
                          capture_output=True, text=True, check=True)
    assert "wrote" in proc.stdout and out3.exists()
    assert "latest 15 closed trades" in out3.read_text()
