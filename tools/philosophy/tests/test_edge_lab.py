"""Tests for tools/philosophy/edge_lab.py (the philosophy's mathematics as code)."""
import itertools
import math
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from scipy import stats

from tools.philosophy import edge_lab as el

EDGE_LAB = Path(__file__).resolve().parents[1] / "edge_lab.py"


# --------------------------------------------------------------------------- Section VII
def test_expected_value_reproduces_the_philosophy_example():
    # Section VII: (0.60 x $100) - (0.40 x $120) - $5 = $7 per trade
    assert el.expected_value(0.60, 100, 120, 5) == 7.0  # exactly, not approximately
    assert el.expected_value(0.60, 100, -120, 5) == 7.0


def test_expected_value_ignores_loss_sign_and_validates_probability():
    assert el.expected_value(0.6, 100, -120, 5) == pytest.approx(7.0)
    assert el.expected_value(0.5, 1, 1) == pytest.approx(0.0)
    with pytest.raises(ValueError):
        el.expected_value(1.2, 1, 1)


def test_breakeven_win_rate():
    assert el.breakeven_win_rate(1.0) == pytest.approx(0.5)
    assert el.breakeven_win_rate(2.0) == pytest.approx(1 / 3)
    p = el.breakeven_win_rate(1.5, cost_r=0.1)
    assert el.expected_value(p, 1.5, 1.0, 0.1) == pytest.approx(0.0, abs=1e-12)
    with pytest.raises(ValueError):
        el.breakeven_win_rate(0)


def test_expectancy_from_results_matches_scipy():
    r = [1.0, -1.0, 2.0, -1.0, 0.5, -1.0, 3.0, 0.0]
    ex = el.expectancy_from_results(r)
    arr = np.array(r)
    assert ex.n == 8
    assert ex.mean == pytest.approx(arr.mean())
    assert ex.sd == pytest.approx(arr.std(ddof=1))
    assert ex.se == pytest.approx(arr.std(ddof=1) / math.sqrt(8))
    assert ex.t_stat == pytest.approx(stats.ttest_1samp(arr, 0).statistic)
    assert ex.p_value == pytest.approx(stats.ttest_1samp(arr, 0).pvalue)
    lo, hi = stats.t.interval(0.95, df=7, loc=arr.mean(), scale=stats.sem(arr))
    assert (ex.ci_low, ex.ci_high) == pytest.approx((lo, hi))
    assert ex.win_rate == pytest.approx(4 / 8)  # 0.0 is a scratch, not a win
    assert ex.avg_win == pytest.approx(6.5 / 4)
    assert ex.avg_loss == pytest.approx(3.0 / 4)
    # expectancy identity: p * avg_win - (1 - p) * avg_loss == mean
    assert el.expected_value(ex.win_rate, ex.avg_win, ex.avg_loss) == pytest.approx(ex.mean)


def test_expectancy_from_results_edge_cases():
    empty = el.expectancy_from_results([])
    assert empty.n == 0 and math.isnan(empty.mean)
    one = el.expectancy_from_results([1.5, float("nan")])
    assert one.n == 1 and one.mean == 1.5 and math.isnan(one.sd)
    same = el.expectancy_from_results([1.0, 1.0, 1.0])
    assert same.ci_low == same.ci_high == 1.0


# --------------------------------------------------------------------------- Section VI
def test_wilson_interval_known_value():
    lo, hi = el.wilson_interval(8, 10)
    assert lo == pytest.approx(0.490, abs=1e-3)
    assert hi == pytest.approx(0.943, abs=1e-3)


def test_wilson_interval_properties():
    lo, hi = el.wilson_interval(0, 10)
    assert lo == 0.0 and 0 < hi < 0.35
    a = el.wilson_interval(3, 20)
    b = el.wilson_interval(17, 20)
    assert a[0] == pytest.approx(1 - b[1]) and a[1] == pytest.approx(1 - b[0])
    assert all(math.isnan(x) for x in el.wilson_interval(0, 0))
    # the interval narrows as n grows (law of large numbers)
    w_small = np.subtract(*el.wilson_interval(6, 10)[::-1])
    w_large = np.subtract(*el.wilson_interval(600, 1000)[::-1])
    assert w_large < w_small / 5
    with pytest.raises(ValueError):
        el.wilson_interval(11, 10)


def test_beta_posterior():
    post = el.beta_posterior(30, 50, threshold=0.5)
    assert (post.a, post.b) == (31.0, 21.0)
    assert post.mean == pytest.approx(31 / 52)
    assert post.ci_low < post.mean < post.ci_high
    assert post.prob_above_threshold == pytest.approx(stats.beta(31, 21).sf(0.5))
    sym = el.beta_posterior(10, 20, threshold=0.5)
    assert sym.prob_above_threshold == pytest.approx(0.5)
    assert el.beta_posterior(3, 5).prob_above_threshold is None


def test_trades_needed_matches_closed_form():
    plan = el.trades_needed(0.6, 1.0)
    assert plan.expectancy_r == pytest.approx(0.2)
    assert plan.sd_r == pytest.approx(math.sqrt(0.96))
    z, zb = stats.norm.ppf(0.975), stats.norm.ppf(0.8)
    assert plan.n_expectancy_typical == math.ceil((z * math.sqrt(0.96) / 0.2) ** 2) == 93
    assert plan.n_expectancy == math.ceil(((z + zb) * math.sqrt(0.96) / 0.2) ** 2) == 189
    assert plan.n_win_rate == math.ceil(z ** 2 * 0.24 / 0.05 ** 2) == 369


def test_trades_needed_behaviour():
    thin = el.trades_needed(0.52, 1.0, cost_r=0.0)
    thick = el.trades_needed(0.60, 1.0, cost_r=0.0)
    assert thin.n_expectancy > thick.n_expectancy
    with_cost = el.trades_needed(0.60, 1.0, cost_r=0.05)
    assert with_cost.n_expectancy > thick.n_expectancy
    none = el.trades_needed(0.5, 1.0, cost_r=0.05)
    assert math.isinf(none.n_expectancy) and math.isinf(none.n_expectancy_typical)


# --------------------------------------------------------------------------- Section XI
def _brute_force_streak(p_loss, streak, n):
    total = 0.0
    for seq in itertools.product((0, 1), repeat=n):  # 1 = loss
        run = best = 0
        for x in seq:
            run = run + 1 if x else 0
            best = max(best, run)
        if best >= streak:
            k = sum(seq)
            total += p_loss ** k * (1 - p_loss) ** (n - k)
    return total


@pytest.mark.parametrize("p_loss", [0.3, 0.5, 0.65])
@pytest.mark.parametrize("n", [1, 4, 7, 12])
@pytest.mark.parametrize("streak", [1, 2, 3, 5])
def test_prob_losing_streak_matches_brute_force(p_loss, n, streak):
    assert el.prob_losing_streak(p_loss, streak, n) == pytest.approx(_brute_force_streak(p_loss, streak, n),
                                                                     abs=1e-12)


def test_prob_losing_streak_edges():
    assert el.prob_losing_streak(0.5, 0, 10) == 1.0
    assert el.prob_losing_streak(0.5, 11, 10) == 0.0
    assert el.prob_losing_streak(0.0, 3, 10) == 0.0
    assert el.prob_losing_streak(1.0, 3, 10) == 1.0
    # a coin-flip loss rate makes 7 straight losses in 200 trades more likely than not
    assert el.prob_losing_streak(0.5, 7, 200) > 0.5
    # more trades, more chances
    assert el.prob_losing_streak(0.4, 6, 500) > el.prob_losing_streak(0.4, 6, 100)


def test_streak_and_drawdown_helpers():
    r = [1, -1, -1, 0, 2, -1, -1]
    assert el.longest_losing_streak(r) == 3
    assert el.max_drawdown_r(r) == pytest.approx(2.0)
    assert el.max_drawdown_r([-1, -1, 3]) == pytest.approx(2.0)  # starts from 0
    assert el.max_drawdown_r([]) == 0.0


# --------------------------------------------------------------------------- Section XIV
def test_simulate_equity_is_deterministic_with_a_seed():
    a = el.simulate_equity(0.45, 2.0, 0.02, 300, 2000, cost_r=0.05, seed=42)
    b = el.simulate_equity(0.45, 2.0, 0.02, 300, 2000, cost_r=0.05, seed=42)
    c = el.simulate_equity(0.45, 2.0, 0.02, 300, 2000, cost_r=0.05, seed=43)
    np.testing.assert_array_equal(a.final_equity, b.final_equity)
    np.testing.assert_array_equal(a.max_drawdown, b.max_drawdown)
    np.testing.assert_array_equal(a.longest_losing_streak, b.longest_losing_streak)
    assert a.prob_ruin == b.prob_ruin
    assert not np.array_equal(a.final_equity, c.final_equity)
    assert a.final_equity.shape == (2000,) and a.longest_losing_streak.dtype.kind == "i"
    s = a.summary()
    assert s["final_equity_p05"] <= s["final_equity_median"] <= s["final_equity_p95"]
    assert 0.0 <= s["prob_ruin"] <= 1.0


def test_simulate_equity_degenerate_paths_are_exact():
    f, n = 0.1, 10
    allwin = el.simulate_equity(1.0, 2.0, f, n, 5)
    np.testing.assert_allclose(allwin.final_equity, (1 + f * 2.0) ** n)
    assert allwin.max_drawdown.max() == 0.0 and allwin.longest_losing_streak.max() == 0
    allloss = el.simulate_equity(0.0, 2.0, f, n, 5, ruin_drawdown=0.5)
    np.testing.assert_allclose(allloss.final_equity, (1 - f) ** n)
    np.testing.assert_allclose(allloss.max_drawdown, 1 - (1 - f) ** n)
    assert (allloss.longest_losing_streak == n).all()
    assert allloss.prob_ruin == 1.0  # 1 - 0.9^10 = 65% drawdown >= 50%


def test_simulate_equity_streaks_match_exact_probability():
    sim = el.simulate_equity(0.5, 1.0, 0.01, 50, 40_000, seed=1)
    exact = el.prob_losing_streak(0.5, 6, 50)
    assert np.mean(sim.longest_losing_streak >= 6) == pytest.approx(exact, abs=0.01)


def test_more_risk_means_more_ruin():
    low = el.simulate_equity(0.5, 1.5, 0.01, 300, 3000, seed=3)
    high = el.simulate_equity(0.5, 1.5, 0.10, 300, 3000, seed=3)
    assert high.prob_ruin > low.prob_ruin
    assert np.median(high.max_drawdown) > np.median(low.max_drawdown)


def test_recovery_required():
    assert el.recovery_required(0.5) == 1.0  # Section XIV: $1,000 -> $500 needs +100%
    assert el.recovery_required(0.0) == 0.0
    assert el.recovery_required(0.2) == pytest.approx(0.25)
    assert math.isinf(el.recovery_required(1.0))
    with pytest.raises(ValueError):
        el.recovery_required(1.5)


def test_kelly_fraction():
    assert el.kelly_fraction(0.6, 1.0) == pytest.approx(0.2)
    assert el.kelly_fraction(0.5, 2.0) == pytest.approx(0.25)
    assert el.kelly_fraction(0.4, 1.0) < 0


def test_kelly_fraction_with_cost_maximises_log_growth():
    p, b, c = 0.55, 1.5, 0.05
    f_star = el.kelly_fraction(p, b, c)
    grid = np.linspace(0.001, 0.6, 20_000)
    growth = p * np.log1p(grid * (b - c)) + (1 - p) * np.log1p(-grid * (1 + c))
    assert f_star == pytest.approx(grid[np.argmax(growth)], abs=1e-3)


def test_kelly_under_uncertainty_shrinks_with_little_evidence():
    small = el.kelly_under_uncertainty(6, 10, 1.0)
    large = el.kelly_under_uncertainty(600, 1000, 1.0)
    assert small.kelly_point == pytest.approx(0.2) and large.kelly_point == pytest.approx(0.2)
    assert small.p_quantile == pytest.approx(stats.beta.ppf(0.05, 7, 5))
    assert small.kelly_conservative == 0.0
    assert 0 < large.kelly_conservative < large.kelly_point
    assert large.half_kelly_conservative == pytest.approx(large.kelly_conservative / 2)


# --------------------------------------------------------------------------- Section XVII
def test_sharpe_ratio():
    r = np.array([0.01, -0.005, 0.007, 0.002, -0.001, 0.004])
    per = r.mean() / r.std(ddof=1)
    assert el.sharpe_ratio(r, periods_per_year=None) == pytest.approx(per)
    assert el.sharpe_ratio(r) == pytest.approx(per * math.sqrt(252))
    assert math.isnan(el.sharpe_ratio([0.01]))
    assert math.isnan(el.sharpe_ratio([0.01, 0.01, 0.01]))


def test_return_moments_normal_sample():
    rng = np.random.default_rng(0)
    m = el.return_moments(rng.normal(0.001, 0.01, 20_000))
    assert m["n"] == 20_000
    assert m["skew"] == pytest.approx(0.0, abs=0.1)
    assert m["kurt"] == pytest.approx(3.0, abs=0.15)


def test_psr_sanity():
    assert el.probabilistic_sharpe_ratio(0.0, 100, 0.0, 3.0) == pytest.approx(0.5)
    assert el.probabilistic_sharpe_ratio(0.1, 1000, 0.0, 3.0) > el.probabilistic_sharpe_ratio(0.1, 100, 0.0, 3.0)
    # negative skew and fat tails lower confidence in the same Sharpe
    assert el.probabilistic_sharpe_ratio(0.1, 250, -2.0, 9.0) < el.probabilistic_sharpe_ratio(0.1, 250, 0.0, 3.0)


def test_dsr_sanity():
    sr, n, sk, ku, v = 0.08, 750, -0.5, 5.0, 0.002
    psr = el.probabilistic_sharpe_ratio(sr, n, sk, ku)
    dsrs = [el.deflated_sharpe_ratio(sr, n, sk, ku, k, v) for k in (1, 2, 10, 100, 1000)]
    assert dsrs[0] == pytest.approx(psr)  # one trial: nothing was selected
    assert all(d <= psr + 1e-12 for d in dsrs)
    assert all(a > b for a, b in zip(dsrs, dsrs[1:]))  # more trials, higher bar
    assert el.expected_max_sharpe(100, v) > el.expected_max_sharpe(10, v) > 0


def test_dsr_numerical_example_from_bailey_lopez_de_prado_2014():
    # Paper's example: annualised SR 2.5, 1,250 daily obs (250/yr), skew -3, kurtosis 10,
    # 100 trials, annualised variance of trial SRs 0.5 -> DSR about 0.90.
    sr = 2.5 / math.sqrt(250)
    v = 0.5 / 250
    assert el.expected_max_sharpe(100, v) * math.sqrt(250) == pytest.approx(1.79, abs=0.01)
    assert el.deflated_sharpe_ratio(sr, 1250, -3.0, 10.0, 100, v) == pytest.approx(0.9004, abs=1e-3)


# --------------------------------------------------------------------------- Section XI
def test_consistency_check_clearly_consistent():
    recent = [2.0, -1.0] * 10  # exactly the reference: p = 0.5, b = 2
    rep = el.consistency_check(recent, ref_p_win=0.5, ref_mean_r=0.5, ref_sd_r=1.5,
                               ref_results=[2.0, -1.0] * 50)
    assert rep.verdict == el.VERDICT_WITHIN == "within expected variation"
    assert rep.wins == 10 and rep.longest_losing_streak == 1
    assert rep.drawdown_percentile is not None and rep.drawdown_percentile < 60


def test_consistency_check_clearly_inconsistent():
    recent = [-1.0] * 20
    rep = el.consistency_check(recent, ref_p_win=0.5, ref_mean_r=0.5, ref_sd_r=1.5,
                               ref_results=[2.0, -1.0] * 50)
    assert rep.verdict == el.VERDICT_INCONSISTENT
    assert rep.verdict == "inconsistent with the reference - assumptions may no longer hold"
    assert rep.direction == "below reference"
    assert rep.p_value_wins < 1e-4 and rep.p_value_streak < 1e-4
    assert rep.drawdown_percentile == pytest.approx(100.0, abs=0.5)


def test_consistency_check_unusual():
    # 5 wins in 20 against a 50% reference, wins spread out (no long losing run)
    recent = [2.0 if (i * 5) // 20 != ((i + 1) * 5) // 20 else -1.0 for i in range(20)]
    rep = el.consistency_check(recent, ref_p_win=0.5, ref_mean_r=0.5, ref_sd_r=1.5)
    assert rep.verdict == el.VERDICT_UNUSUAL == "unusual - investigate"


def test_consistency_check_same_wins_clustered_is_worse():
    spread = [2.0 if (i * 7) // 20 != ((i + 1) * 7) // 20 else -1.0 for i in range(20)]
    clustered = [-1.0] * 13 + [2.0] * 7
    assert el.consistency_check(spread, 0.5, 0.5, 1.5).verdict == el.VERDICT_WITHIN
    assert el.consistency_check(clustered, 0.5, 0.5, 1.5).verdict == el.VERDICT_INCONSISTENT


def test_consistency_check_flags_too_good_as_well():
    rep = el.consistency_check([2.0] * 20, 0.5, 0.5, 1.5)
    assert rep.verdict == el.VERDICT_INCONSISTENT and rep.direction == "above reference"


def test_consistency_check_empty_and_bootstrap_determinism():
    assert el.consistency_check([], 0.5, 0.5, 1.5).verdict == el.VERDICT_WITHIN
    ref = np.random.default_rng(5).choice([2.0, -1.0], 200)
    recent = [-1, -1, 2, -1, -1, -1, 2, -1, 2, -1]
    a = el.consistency_check(recent, 0.5, 0.5, 1.5, ref_results=ref, seed=9)
    b = el.consistency_check(recent, 0.5, 0.5, 1.5, ref_results=ref, seed=9)
    assert a.drawdown_percentile == b.drawdown_percentile


# --------------------------------------------------------------------------- Section VI
def test_conditional_stats():
    df = pd.DataFrame({
        "regime": ["trend"] * 6 + ["range"] * 4 + [None, ""],
        "r": [2.0, -1.0, 2.0, -1.0, 2.0, np.nan, -1.0, -1.0, 1.0, -1.0, 0.5, -0.5],
    })
    out = el.conditional_stats(df, "r", "regime")
    by = out.set_index("regime")
    assert list(out["regime"]) == ["trend", "range", el.UNSPECIFIED]  # sorted by n
    t = by.loc["trend"]
    assert t["n"] == 5 and t["wins"] == 3
    assert t["win_rate"] == pytest.approx(0.6)
    assert (t["win_ci_low"], t["win_ci_high"]) == pytest.approx(el.wilson_interval(3, 5))
    assert t["mean_r"] == pytest.approx(0.8)
    assert t["expectancy_r"] == pytest.approx(t["mean_r"])
    lo, hi = stats.t.interval(0.95, df=4, loc=0.8, scale=stats.sem([2, -1, 2, -1, 2]))
    assert (t["mean_ci_low"], t["mean_ci_high"]) == pytest.approx((lo, hi))
    assert by.loc[el.UNSPECIFIED, "n"] == 2
    multi = el.conditional_stats(df.assign(s=["a", "b"] * 6), "r", ["regime", "s"])
    assert set(multi.columns[:2]) == {"regime", "s"} and multi["n"].sum() == 11


def test_conditional_stats_empty():
    out = el.conditional_stats(pd.DataFrame({"k": ["a"], "r": [np.nan]}), "r", "k")
    assert out.empty and "win_rate" in out.columns


# --------------------------------------------------------------------------- CLI
def test_cli_ev_prints_the_worked_example():
    proc = subprocess.run([sys.executable, str(EDGE_LAB), "ev", "--p", "0.6", "--win", "100", "--loss", "120",
                           "--cost", "5"], capture_output=True, text=True, check=True)
    assert "Expected value per trade: 7.00" in proc.stdout


@pytest.mark.parametrize("argv, expected", [
    (["streak", "--p-loss", "0.5", "--streak", "7", "--trades", "200"], "P(at least one run of >= 7 losses"),
    (["ruin", "--p", "0.45", "--rr", "2", "--risk", "0.02", "--trades", "100", "--paths", "500"], "P(drawdown >="),
    (["sample", "--p", "0.6", "--rr", "1"], "189"),
    (["kelly", "--p", "0.6", "--rr", "1", "--wins", "60", "--n", "100"], "Kelly fraction"),
    (["breakeven", "--rr", "2"], "33.33%"),
    (["wilson", "--wins", "8", "--n", "10"], "0.490 - 0.943"),
    (["recover", "--loss", "0.5"], "100.0% gain"),
])
def test_cli_subcommands(capsys, argv, expected):
    assert el.main(argv) == 0
    assert expected in capsys.readouterr().out


def test_cli_reports_bad_input(capsys):
    assert el.main(["ev", "--p", "1.5", "--win", "1", "--loss", "1"]) == 2
    assert "error" in capsys.readouterr().err
