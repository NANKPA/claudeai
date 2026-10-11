#!/usr/bin/env python3
"""Edge lab: the mathematics of "The Philosophy of the Relationship" as code.

Source text: trading-intelligence/00_philosophy/philosophy-of-the-relationship.md

The philosophy calls mathematics "the trader's sword" (Section VII) and asks
that every belief about an edge be measured, sized and re-tested. This module
holds the small, pure functions that do the measuring:

* Section VI   probability is conditional; the law of large numbers
               -> wilson_interval, beta_posterior, trades_needed, conditional_stats
* Section VII  expected value; maths must serve the decision
               -> expected_value, expectancy_from_results, breakeven_win_rate
* Section XI   is a losing run normal variation or a broken assumption?
               -> prob_losing_streak, consistency_check
* Section XIV  capital preservation and the asymmetry of losses
               -> recovery_required, simulate_equity, kelly_fraction,
                  kelly_under_uncertainty
* Section XVI  the journal as a record of understanding (see journal_review.py)
* Section XVII the scientific method; overfitting
               -> sharpe_ratio, probabilistic_sharpe_ratio,
                  deflated_sharpe_ratio

Conventions
-----------
* Trade results are R-multiples (profit or loss divided by the amount risked).
* A "win" is a result strictly greater than zero; scratches count as non-wins.
* ``reward_risk`` (b) is the average win divided by the average loss, in R.
* ``cost_r`` is a flat per-trade cost in R, subtracted from every outcome.

Education, not financial advice. Every number this module produces is
conditional on the inputs and assumptions supplied to it.

CLI
---
    python3 tools/philosophy/edge_lab.py ev --p 0.6 --win 100 --loss 120 --cost 5
    python3 tools/philosophy/edge_lab.py streak --p-loss 0.5 --streak 6 --trades 100
    python3 tools/philosophy/edge_lab.py ruin --p 0.45 --rr 2 --risk 0.02 --trades 250
    python3 tools/philosophy/edge_lab.py sample --p 0.55 --rr 1.5 --cost 0.05
    python3 tools/philosophy/edge_lab.py kelly --p 0.6 --rr 1 --wins 33 --n 55
"""
from __future__ import annotations

import argparse
import math
import sys
from dataclasses import asdict, dataclass, field
from typing import Any, Iterable, Sequence

import numpy as np
import pandas as pd
from scipy import stats

__all__ = [
    "EULER_GAMMA",
    "VERDICT_WITHIN",
    "VERDICT_UNUSUAL",
    "VERDICT_INCONSISTENT",
    "Expectancy",
    "BetaPosterior",
    "SampleSizePlan",
    "EquitySimulation",
    "KellyUnderUncertainty",
    "ConsistencyReport",
    "expected_value",
    "expectancy_from_results",
    "breakeven_win_rate",
    "wilson_interval",
    "beta_posterior",
    "trades_needed",
    "prob_losing_streak",
    "longest_losing_streak",
    "max_drawdown_r",
    "simulate_equity",
    "recovery_required",
    "kelly_fraction",
    "kelly_under_uncertainty",
    "sharpe_ratio",
    "return_moments",
    "probabilistic_sharpe_ratio",
    "expected_max_sharpe",
    "deflated_sharpe_ratio",
    "consistency_check",
    "conditional_stats",
    "main",
]

#: Euler-Mascheroni constant, used by the expected maximum Sharpe ratio.
EULER_GAMMA = 0.5772156649015329

#: Verdicts returned by :func:`consistency_check` (Section XI).
VERDICT_WITHIN = "within expected variation"
VERDICT_UNUSUAL = "unusual - investigate"
VERDICT_INCONSISTENT = "inconsistent with the reference - assumptions may no longer hold"

NumberSeq = Iterable[float] | np.ndarray | pd.Series


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def _as_array(values: NumberSeq) -> np.ndarray:
    """Return a 1-D float array of the finite values, order preserved."""
    if isinstance(values, pd.Series):
        arr = pd.to_numeric(values, errors="coerce").to_numpy(dtype=float)
    elif isinstance(values, np.ndarray):
        arr = values.astype(float)
    else:
        arr = np.asarray(list(values), dtype=float)
    arr = arr.ravel()
    return arr[np.isfinite(arr)]


def _check_prob(p: float, name: str) -> None:
    if not (0.0 <= float(p) <= 1.0) or math.isnan(float(p)):
        raise ValueError(f"{name} must be a probability in [0, 1], got {p!r}")


def _check_conf(conf: float) -> None:
    if not (0.0 < conf < 1.0):
        raise ValueError(f"conf must be in (0, 1), got {conf!r}")


def _z(conf: float) -> float:
    """Two-sided normal critical value for a central interval of size conf."""
    _check_conf(conf)
    return float(stats.norm.ppf(0.5 + conf / 2.0))


class _DictMixin:
    def to_dict(self) -> dict[str, Any]:
        """Plain-dict view (numpy arrays are left as arrays)."""
        return asdict(self)  # type: ignore[call-overload]


# ---------------------------------------------------------------------------
# Section VII: expected value
# ---------------------------------------------------------------------------
def expected_value(p_win: float, avg_win: float, avg_loss: float, cost: float = 0.0) -> float:
    """Expected value per trade (Section VII, "Expected value").

    EV = p_win * avg_win - (1 - p_win) * avg_loss - cost

    ``avg_loss`` is the size of the average loss; its sign is ignored, so 120
    and -120 mean the same thing. Units are whatever the inputs use (dollars,
    R, points). The philosophy's worked example, p = 0.60, win = 100,
    loss = 120, cost = 5, gives 7.0 per trade on average - under those
    assumptions only.
    """
    _check_prob(p_win, "p_win")
    return float(p_win * avg_win - (1.0 - p_win) * abs(avg_loss) - cost)


@dataclass(frozen=True)
class Expectancy(_DictMixin):
    """Sample expectancy with its uncertainty (see expectancy_from_results)."""

    n: int
    mean: float
    sd: float
    se: float
    t_stat: float
    p_value: float
    ci_low: float
    ci_high: float
    conf: float
    win_rate: float
    avg_win: float
    avg_loss: float
    total: float


def expectancy_from_results(results: NumberSeq, conf: float = 0.95) -> Expectancy:
    """Expectancy of observed results with a Student-t interval (Sections VI-VII).

    Returns n, mean, sample sd (ddof=1), standard error, t-statistic against a
    true mean of zero, its two-sided p-value and a ``conf`` confidence interval
    for the mean. Also reports the win rate (result > 0), the average win and
    the average loss magnitude (results <= 0). Non-finite values are dropped.
    A positive mean whose interval still contains zero is a story, not yet an
    edge (Section VI, the law of large numbers).
    """
    _check_conf(conf)
    r = _as_array(results)
    n = int(r.size)
    nan = float("nan")
    if n == 0:
        return Expectancy(0, nan, nan, nan, nan, nan, nan, nan, conf, nan, nan, nan, 0.0)
    mean = float(r.mean())
    wins = r[r > 0]
    losses = r[r <= 0]
    win_rate = float(wins.size / n)
    avg_win = float(wins.mean()) if wins.size else 0.0
    avg_loss = float(-losses.mean()) if losses.size else 0.0
    if n < 2:
        return Expectancy(n, mean, nan, nan, nan, nan, nan, nan, conf, win_rate, avg_win, avg_loss, float(r.sum()))
    sd = float(r.std(ddof=1))
    se = sd / math.sqrt(n)
    if se > 0:
        t_stat = mean / se
        p_value = float(2.0 * stats.t.sf(abs(t_stat), df=n - 1))
        tcrit = float(stats.t.ppf(0.5 + conf / 2.0, df=n - 1))
        lo, hi = mean - tcrit * se, mean + tcrit * se
    else:  # every result identical: no sampling spread is visible
        t_stat = math.copysign(math.inf, mean) if mean != 0 else nan
        p_value = 0.0 if mean != 0 else 1.0
        lo = hi = mean
    return Expectancy(n, mean, sd, se, float(t_stat), p_value, float(lo), float(hi), conf,
                      win_rate, avg_win, avg_loss, float(r.sum()))


def breakeven_win_rate(reward_risk: float, cost_r: float = 0.0) -> float:
    """Win rate at which a fixed payoff ratio breaks even (Section VII).

    Solves p * b - (1 - p) - cost_r = 0, giving p = (1 + cost_r) / (1 + b).
    A value above 1 means no win rate can pay for that cost at that payoff.
    """
    if reward_risk <= 0:
        raise ValueError("reward_risk must be > 0")
    return float((1.0 + cost_r) / (1.0 + reward_risk))


# ---------------------------------------------------------------------------
# Section VI: probability is conditional; the law of large numbers
# ---------------------------------------------------------------------------
def wilson_interval(wins: int, n: int, conf: float = 0.95) -> tuple[float, float]:
    """Wilson score interval for a win rate (Section VI, law of large numbers).

    Better behaved than the textbook p +- z*SE for small samples and for rates
    near 0 or 1. Example: 8 wins in 10 trades gives roughly (0.490, 0.943) -
    a "high-probability" setup on ten trades is still compatible with a coin.
    Returns (nan, nan) when n == 0.
    """
    if n < 0 or wins < 0 or wins > n:
        raise ValueError(f"need 0 <= wins <= n, got wins={wins}, n={n}")
    if n == 0:
        return (float("nan"), float("nan"))
    z = _z(conf)
    p = wins / n
    z2 = z * z
    denom = 1.0 + z2 / n
    centre = (p + z2 / (2.0 * n)) / denom
    half = z * math.sqrt(p * (1.0 - p) / n + z2 / (4.0 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


@dataclass(frozen=True)
class BetaPosterior(_DictMixin):
    """Beta posterior for a win probability (see beta_posterior)."""

    a: float
    b: float
    mean: float
    ci_low: float
    ci_high: float
    conf: float
    threshold: float | None
    prob_above_threshold: float | None


def beta_posterior(wins: int, n: int, prior_a: float = 1.0, prior_b: float = 1.0,
                   threshold: float | None = None, conf: float = 0.95) -> BetaPosterior:
    """Bayesian view of a win rate: Beta(prior_a + wins, prior_b + losses) (Section VI).

    Returns the posterior mean, a central ``conf`` credible interval and, when
    ``threshold`` is given, P(p > threshold). A natural threshold is the
    breakeven win rate of the setup's payoff (see breakeven_win_rate): the
    probability that the true win rate clears breakeven, given the evidence.
    The default Beta(1, 1) prior is uniform.
    """
    if n < 0 or wins < 0 or wins > n:
        raise ValueError(f"need 0 <= wins <= n, got wins={wins}, n={n}")
    if prior_a <= 0 or prior_b <= 0:
        raise ValueError("prior_a and prior_b must be > 0")
    _check_conf(conf)
    a = float(prior_a + wins)
    b = float(prior_b + n - wins)
    dist = stats.beta(a, b)
    lo, hi = dist.ppf([(1 - conf) / 2, (1 + conf) / 2])
    p_above = None
    if threshold is not None:
        _check_prob(threshold, "threshold")
        p_above = float(dist.sf(threshold))
    return BetaPosterior(a, b, float(a / (a + b)), float(lo), float(hi), conf,
                         None if threshold is None else float(threshold), p_above)


@dataclass(frozen=True)
class SampleSizePlan(_DictMixin):
    """How many trades the law of large numbers asks for (see trades_needed)."""

    expectancy_r: float
    sd_r: float
    n_expectancy: float           # trades so a conf-CI excludes 0 with probability `power`
    n_expectancy_typical: float   # trades so the *expected* CI just excludes 0 (power 0.5)
    n_win_rate: float             # trades so the win-rate CI half-width <= win_rate_half_width
    win_rate_half_width: float
    conf: float
    power: float


def trades_needed(p_win: float, reward_risk: float, cost_r: float = 0.0, conf: float = 0.95,
                  power: float = 0.8, win_rate_half_width: float = 0.05) -> SampleSizePlan:
    """Approximate sample size before the evidence can separate an edge from zero (Section VI).

    For a two-outcome trade (+b with probability p, -1 otherwise, minus cost_r)
    the true expectancy is mu = p*b - (1 - p) - cost_r and the per-trade standard
    deviation is sigma = (b + 1) * sqrt(p * (1 - p)). Using the normal
    approximation:

    * n_expectancy         = ((z_conf + z_power) * sigma / mu)^2 - trades for a
                             ``conf`` interval on expectancy to exclude zero with
                             probability ``power``;
    * n_expectancy_typical = (z_conf * sigma / mu)^2 - trades for the interval
                             to exclude zero on an average sample;
    * n_win_rate           = z_conf^2 * p * (1 - p) / h^2 - trades for the
                             win-rate interval half-width to fall to h (5 points
                             by default).

    Values are rounded up. When mu <= 0 the expectancy counts are infinite:
    no amount of data can show an edge that is not there.
    """
    _check_prob(p_win, "p_win")
    if not (0 < power < 1):
        raise ValueError("power must be in (0, 1)")
    if reward_risk <= 0:
        raise ValueError("reward_risk must be > 0")
    if not (0 < win_rate_half_width < 1):
        raise ValueError("win_rate_half_width must be in (0, 1)")
    z_a = _z(conf)
    z_b = float(stats.norm.ppf(power))
    mu = p_win * reward_risk - (1.0 - p_win) - cost_r
    sigma = (reward_risk + 1.0) * math.sqrt(p_win * (1.0 - p_win))
    if mu <= 0:
        n_pow = n_typ = math.inf
    elif sigma == 0:  # a certain outcome: one observation settles it
        n_pow = n_typ = 1.0
    else:
        n_pow = float(math.ceil(max(0.0, z_a + z_b) ** 2 * (sigma / mu) ** 2))
        n_typ = float(math.ceil((z_a * sigma / mu) ** 2))
    n_wr = float(math.ceil(z_a ** 2 * p_win * (1.0 - p_win) / win_rate_half_width ** 2))
    return SampleSizePlan(float(mu), float(sigma), max(n_pow, 1.0), max(n_typ, 1.0), max(n_wr, 1.0),
                          win_rate_half_width, conf, power)


# ---------------------------------------------------------------------------
# Section XI: streaks and drawdowns are part of the system
# ---------------------------------------------------------------------------
def prob_losing_streak(p_loss: float, streak: int, n_trades: int) -> float:
    """Exact P(at least one run of >= ``streak`` consecutive losses in ``n_trades``) (Section XI).

    Trades are independent with loss probability ``p_loss``. Computed with a
    Markov chain over the current run length (states 0 .. streak-1 plus an
    absorbing "streak reached" state), not by simulation. It answers the
    Section XI question "is this losing run normal?" for a given loss rate:
    a positive-expectancy strategy that loses 50% of the time has a better
    than even chance of 7 straight losses somewhere in 200 trades.
    """
    _check_prob(p_loss, "p_loss")
    if n_trades < 0:
        raise ValueError("n_trades must be >= 0")
    if streak <= 0:
        return 1.0
    if streak > n_trades or p_loss == 0.0:
        return 0.0
    if p_loss == 1.0:
        return 1.0
    p_win = 1.0 - p_loss
    state = np.zeros(streak, dtype=float)  # state[k]: current run of k losses, never reached `streak`
    state[0] = 1.0
    absorbed = 0.0
    for _ in range(n_trades):
        absorbed += state[-1] * p_loss
        total = state.sum()
        state[1:] = state[:-1] * p_loss
        state[0] = total * p_win
    return float(min(1.0, max(0.0, absorbed)))


def longest_losing_streak(results: NumberSeq) -> int:
    """Longest run of consecutive non-winning results (result <= 0) (Section XI)."""
    r = _as_array(results)
    best = cur = 0
    for x in r:
        if x <= 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return int(best)


def max_drawdown_r(results: NumberSeq) -> float:
    """Largest peak-to-trough fall of the cumulative R curve, in R (Sections XI, XIV).

    The curve starts at 0 before the first trade, so an opening loss counts.
    """
    r = _as_array(results)
    if r.size == 0:
        return 0.0
    curve = np.concatenate([[0.0], np.cumsum(r)])
    peak = np.maximum.accumulate(curve)
    return float((peak - curve).max())


def _max_drawdown_rows(paths: np.ndarray) -> np.ndarray:
    """Row-wise max drawdown in R of a 2-D array of R results."""
    curve = np.cumsum(paths, axis=1)
    curve = np.concatenate([np.zeros((paths.shape[0], 1)), curve], axis=1)
    peak = np.maximum.accumulate(curve, axis=1)
    return (peak - curve).max(axis=1)


# ---------------------------------------------------------------------------
# Section XIV: capital preservation and survival
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class EquitySimulation(_DictMixin):
    """Monte Carlo of fixed-fractional compounding (see simulate_equity)."""

    final_equity: np.ndarray = field(repr=False)
    max_drawdown: np.ndarray = field(repr=False)
    longest_losing_streak: np.ndarray = field(repr=False)
    prob_ruin: float
    ruin_drawdown: float
    p_win: float
    reward_risk: float
    risk_fraction: float
    n_trades: int
    n_paths: int
    cost_r: float
    seed: int

    def summary(self) -> dict[str, float]:
        """Percentiles of final equity (start = 1.0), drawdown and streaks."""
        fe, dd, ls = self.final_equity, self.max_drawdown, self.longest_losing_streak
        return {
            "expectancy_r_per_trade": self.p_win * self.reward_risk - (1 - self.p_win) - self.cost_r,
            "final_equity_p05": float(np.percentile(fe, 5)),
            "final_equity_median": float(np.median(fe)),
            "final_equity_p95": float(np.percentile(fe, 95)),
            "prob_final_below_start": float(np.mean(fe < 1.0)),
            "max_drawdown_median": float(np.median(dd)),
            "max_drawdown_p95": float(np.percentile(dd, 95)),
            "longest_losing_streak_median": float(np.median(ls)),
            "longest_losing_streak_p95": float(np.percentile(ls, 95)),
            "prob_ruin": self.prob_ruin,
        }


def simulate_equity(p_win: float, reward_risk: float, risk_fraction: float, n_trades: int,
                    n_paths: int, cost_r: float = 0.0, ruin_drawdown: float = 0.5,
                    seed: int = 0) -> EquitySimulation:
    """Simulate fixed-fractional compounding over many equity paths (Section XIV).

    Each trade risks ``risk_fraction`` of current equity: a win multiplies
    equity by 1 + f*(b - cost_r), a loss by 1 - f*(1 + cost_r); equity cannot
    fall below zero. Starting equity is 1.0. Returns per-path final equity,
    maximum drawdown (fraction of the running peak), longest losing streak and
    P(max drawdown >= ruin_drawdown). Vectorised with numpy and processed in
    chunks so memory stays bounded; the same ``seed`` gives the same paths.
    The point is Section XIV's: a genuine edge can still deliver a sequence
    that ends participation if too much is risked per trade.
    """
    _check_prob(p_win, "p_win")
    if reward_risk <= 0:
        raise ValueError("reward_risk must be > 0")
    if not (0 < risk_fraction <= 1):
        raise ValueError("risk_fraction must be in (0, 1]")
    if n_trades < 1 or n_paths < 1:
        raise ValueError("n_trades and n_paths must be >= 1")
    if not (0 < ruin_drawdown <= 1):
        raise ValueError("ruin_drawdown must be in (0, 1]")
    rng = np.random.default_rng(seed)
    final = np.empty(n_paths)
    mdd = np.empty(n_paths)
    streaks = np.empty(n_paths, dtype=np.int64)
    chunk = max(1, min(n_paths, 2_000_000 // n_trades))
    win_mult = 1.0 + risk_fraction * (reward_risk - cost_r)
    loss_mult = max(0.0, 1.0 - risk_fraction * (1.0 + cost_r))
    for start in range(0, n_paths, chunk):
        m = min(chunk, n_paths - start)
        win = rng.random((m, n_trades)) < p_win
        factors = np.where(win, win_mult, loss_mult)
        np.maximum(factors, 0.0, out=factors)
        eq = np.cumprod(factors, axis=1)
        peak = np.maximum(np.maximum.accumulate(eq, axis=1), 1.0)
        dd = 1.0 - eq / peak
        final[start:start + m] = eq[:, -1]
        mdd[start:start + m] = dd.max(axis=1)
        lost = ~win
        c = np.cumsum(lost, axis=1)
        reset = np.maximum.accumulate(np.where(lost, 0, c), axis=1)
        streaks[start:start + m] = (c - reset).max(axis=1)
    prob_ruin = float(np.mean(mdd >= ruin_drawdown - 1e-12))
    return EquitySimulation(final, mdd, streaks, prob_ruin, float(ruin_drawdown), float(p_win),
                            float(reward_risk), float(risk_fraction), int(n_trades), int(n_paths),
                            float(cost_r), int(seed))


def recovery_required(loss_fraction: float) -> float:
    """Gain needed to recover a loss: 1 / (1 - L) - 1 (Section XIV).

    The philosophy's example: losing 50% of a $1,000 account needs a 100%
    return on the remaining $500, so recovery_required(0.5) == 1.0. A total
    loss (L = 1) cannot be recovered and returns infinity.
    """
    if not (0.0 <= loss_fraction <= 1.0):
        raise ValueError("loss_fraction must be in [0, 1]")
    if loss_fraction == 1.0:
        return math.inf
    return float(1.0 / (1.0 - loss_fraction) - 1.0)


def kelly_fraction(p_win: float, reward_risk: float, cost_r: float = 0.0) -> float:
    """Growth-optimal fraction of equity to risk per trade (Sections XIV, VII).

    For a binary trade paying b R with probability p and losing 1 R otherwise,
    f* = p - (1 - p) / b. With a flat cost c (in R) the outcomes become b - c
    and -(1 + c), and f* = p / (1 + c) - (1 - p) / (b - c). A negative value
    means the bet has no positive expectancy and the growth-optimal size is
    zero. Full Kelly assumes p and b are known exactly; they never are, which
    is why kelly_under_uncertainty exists.
    """
    _check_prob(p_win, "p_win")
    if reward_risk <= 0:
        raise ValueError("reward_risk must be > 0")
    if cost_r == 0.0:
        return float(p_win - (1.0 - p_win) / reward_risk)
    if reward_risk - cost_r <= 0:
        return -math.inf
    return float(p_win / (1.0 + cost_r) - (1.0 - p_win) / (reward_risk - cost_r))


@dataclass(frozen=True)
class KellyUnderUncertainty(_DictMixin):
    """Kelly sizing that respects estimation error (see kelly_under_uncertainty)."""

    p_hat: float
    p_quantile: float
    quantile: float
    posterior_a: float
    posterior_b: float
    kelly_point: float
    kelly_conservative: float
    half_kelly_conservative: float


def kelly_under_uncertainty(wins: int, n: int, reward_risk: float, quantile: float = 0.05,
                            prior_a: float = 1.0, prior_b: float = 1.0,
                            cost_r: float = 0.0) -> KellyUnderUncertainty:
    """Kelly fraction evaluated at a pessimistic quantile of the win rate (Sections XIV, VI).

    The win rate is uncertain, so instead of plugging in wins / n the function
    uses the ``quantile`` of the Beta(prior_a + wins, prior_b + losses)
    posterior (5% by default). With few trades this quantile sits well below
    the observed rate and the conservative fraction shrinks, often to zero:
    size follows evidence. ``kelly_point`` is the naive plug-in value for
    comparison; ``kelly_conservative`` is floored at zero.
    """
    if n <= 0 or wins < 0 or wins > n:
        raise ValueError(f"need 0 <= wins <= n and n > 0, got wins={wins}, n={n}")
    if not (0 < quantile < 1):
        raise ValueError("quantile must be in (0, 1)")
    a = float(prior_a + wins)
    b = float(prior_b + n - wins)
    p_q = float(stats.beta.ppf(quantile, a, b))
    p_hat = wins / n
    k_point = kelly_fraction(p_hat, reward_risk, cost_r)
    k_cons = max(0.0, kelly_fraction(p_q, reward_risk, cost_r))
    return KellyUnderUncertainty(float(p_hat), p_q, float(quantile), a, b, float(k_point),
                                 float(k_cons), float(k_cons / 2.0))


# ---------------------------------------------------------------------------
# Section XVII: the scientific method and overfitting
# ---------------------------------------------------------------------------
def sharpe_ratio(returns: NumberSeq, periods_per_year: float | None = 252) -> float:
    """Sharpe ratio mean / sd (ddof=1), annualised by sqrt(periods_per_year) (Section XVII).

    Pass periods_per_year=None (or 1) for the per-period ratio, which is the
    input that probabilistic_sharpe_ratio and deflated_sharpe_ratio expect.
    Returns are assumed to be in excess of any benchmark rate already.
    """
    r = _as_array(returns)
    if r.size < 2:
        return float("nan")
    sd = float(r.std(ddof=1))
    if sd == 0:
        return float("nan")
    sr = float(r.mean()) / sd
    if periods_per_year:
        sr *= math.sqrt(periods_per_year)
    return float(sr)


def return_moments(returns: NumberSeq) -> dict[str, float]:
    """Per-period Sharpe, n, skewness and (non-excess) kurtosis of a return series.

    Convenience wrapper that produces the inputs of the PSR and DSR in the
    units those formulas expect (Section XVII). A normal distribution has
    skew 0 and kurtosis 3.
    """
    r = _as_array(returns)
    if r.size < 4:
        raise ValueError("need at least 4 returns for skewness and kurtosis")
    return {
        "sr": sharpe_ratio(r, periods_per_year=None),
        "n": float(r.size),
        "skew": float(stats.skew(r, bias=False)),
        "kurt": float(stats.kurtosis(r, fisher=False, bias=False)),
    }


def probabilistic_sharpe_ratio(sr: float, n: int, skew: float, kurt: float,
                               sr_benchmark: float = 0.0) -> float:
    """Probabilistic Sharpe Ratio, P(true SR > sr_benchmark) (Section XVII).

    Bailey & Lopez de Prado: PSR = Phi((SR - SR*) * sqrt(n - 1) /
    sqrt(1 - skew * SR + (kurt - 1) / 4 * SR^2)). ``sr`` and ``sr_benchmark``
    are per-period (not annualised) and ``n`` is the number of return
    observations; ``kurt`` is the ordinary kurtosis (3 for a normal).
    Negative skew and fat tails widen the uncertainty around SR.
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    denom = 1.0 - skew * sr + (kurt - 1.0) / 4.0 * sr ** 2
    if denom <= 0:
        return float("nan")
    z = (sr - sr_benchmark) * math.sqrt(n - 1.0) / math.sqrt(denom)
    return float(stats.norm.cdf(z))


def expected_max_sharpe(n_trials: int, sr_variance: float) -> float:
    """Expected maximum per-period SR among n_trials skill-less trials (Section XVII).

    SR0 = sqrt(V[SR]) * ((1 - g) * Phi^-1(1 - 1/N) + g * Phi^-1(1 - 1/(N e))),
    g = Euler-Mascheroni constant (Bailey & Lopez de Prado, 2014). With one
    trial nothing was selected and SR0 = 0.
    """
    if n_trials < 1:
        raise ValueError("n_trials must be >= 1")
    if sr_variance < 0:
        raise ValueError("sr_variance must be >= 0")
    if n_trials == 1 or sr_variance == 0:
        return 0.0
    g = EULER_GAMMA
    term = (1 - g) * stats.norm.ppf(1 - 1.0 / n_trials) + g * stats.norm.ppf(1 - 1.0 / (n_trials * math.e))
    return float(math.sqrt(sr_variance) * term)


def deflated_sharpe_ratio(sr: float, n: int, skew: float, kurt: float, n_trials: int,
                          sr_variance: float) -> float:
    """Deflated Sharpe Ratio (Bailey & Lopez de Prado, 2014) (Section XVII, overfitting).

    The PSR evaluated against SR0, the Sharpe ratio the best of ``n_trials``
    skill-less strategies would be expected to show by luck alone
    (expected_max_sharpe). ``sr_variance`` is the variance of the per-period
    Sharpe ratios across the trials that were tried. The more variants were
    tested before this one was chosen, the higher the bar - the cost of
    "adjusting the rules until they fit the past" that Section XVII warns about.
    """
    sr0 = expected_max_sharpe(n_trials, sr_variance)
    return probabilistic_sharpe_ratio(sr, n, skew, kurt, sr_benchmark=sr0)


# ---------------------------------------------------------------------------
# Section XI: normal variation or changed assumptions?
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class ConsistencyReport(_DictMixin):
    """Result of consistency_check (Section XI)."""

    verdict: str
    n: int
    wins: int
    win_rate: float
    ref_p_win: float
    p_value_wins: float
    mean_r: float
    ref_mean_r: float
    z_mean: float
    p_value_mean: float
    t_stat_mean: float
    p_value_mean_t: float
    max_drawdown_r: float
    drawdown_percentile: float | None
    p_value_drawdown: float | None
    longest_losing_streak: int
    p_value_streak: float
    min_p_value: float
    min_p_value_adjusted: float
    direction: str
    notes: list[str]


def consistency_check(recent_results: NumberSeq, ref_p_win: float, ref_mean_r: float,
                      ref_sd_r: float, ref_results: NumberSeq | None = None,
                      n_boot: int = 5000, seed: int = 0, alpha_investigate: float = 0.05,
                      alpha_inconsistent: float = 0.01) -> ConsistencyReport:
    """Are recent results inside the strategy's expected range? (Section XI)

    Section XI asks whether a losing run is ordinary variation or evidence that
    the assumptions behind a strategy no longer hold. Tests against the
    reference behaviour (win rate, mean R and sd R from earlier trades or a
    backtest):

    1. exact binomial test of the recent win count (two-sided);
    2. z-test of the recent mean R using the reference sd (two-sided); a
       one-sample t-test using the recent sd is reported alongside;
    3. exact probability of a losing streak at least as long as the observed
       one (prob_losing_streak, one-sided);
    4. if ``ref_results`` is given: the percentile of the observed max
       drawdown (in R) among ``n_boot`` bootstrap samples of the same length
       drawn from the reference trades, and the matching one-sided p-value.

    Verdict, using the smallest p-value of the tests that could be run:
    ``VERDICT_INCONSISTENT`` if it stays below ``alpha_inconsistent`` after a
    Bonferroni adjustment for the number of tests; else ``VERDICT_UNUSUAL`` if
    the raw value is below ``alpha_investigate`` (deliberately sensitive:
    investigating is cheap - Section X says manage risk first, then
    investigate); else ``VERDICT_WITHIN``. Results far *better* than the
    reference are also flagged: the reference no longer describes them.
    """
    _check_prob(ref_p_win, "ref_p_win")
    r = _as_array(recent_results)
    n = int(r.size)
    notes: list[str] = []
    nan = float("nan")
    if n == 0:
        return ConsistencyReport(VERDICT_WITHIN, 0, 0, nan, float(ref_p_win), nan, nan, float(ref_mean_r),
                                 nan, nan, nan, nan, 0.0, None, None, 0, nan, nan, nan, "n/a",
                                 ["no recent results: nothing to test"])
    if n < 10:
        notes.append(f"only {n} recent trades: every test has little power")
    wins = int((r > 0).sum())
    win_rate = wins / n
    p_vals: dict[str, float] = {}

    p_wins = float(stats.binomtest(wins, n, ref_p_win, alternative="two-sided").pvalue)
    p_vals["wins"] = p_wins

    mean_r = float(r.mean())
    if ref_sd_r and ref_sd_r > 0 and math.isfinite(ref_sd_r):
        z_mean = (mean_r - ref_mean_r) / (ref_sd_r / math.sqrt(n))
        p_mean = float(2.0 * stats.norm.sf(abs(z_mean)))
        p_vals["mean"] = p_mean
    else:
        z_mean, p_mean = nan, nan
        notes.append("reference sd missing or zero: z-test on mean R skipped")
    if n >= 2 and r.std(ddof=1) > 0:
        tt = stats.ttest_1samp(r, ref_mean_r)
        t_stat, p_t = float(tt.statistic), float(tt.pvalue)
    else:
        t_stat, p_t = nan, nan

    streak = longest_losing_streak(r)
    p_streak = prob_losing_streak(1.0 - ref_p_win, streak, n) if streak > 0 else 1.0
    p_vals["streak"] = p_streak

    mdd = max_drawdown_r(r)
    dd_pct: float | None = None
    p_dd: float | None = None
    if ref_results is not None:
        ref = _as_array(ref_results)
        if ref.size >= 2:
            rng = np.random.default_rng(seed)
            boot = ref[rng.integers(0, ref.size, size=(n_boot, n))]
            boot_dd = _max_drawdown_rows(boot)
            dd_pct = float(100.0 * (np.mean(boot_dd < mdd) + 0.5 * np.mean(boot_dd == mdd)))
            p_dd = float((np.sum(boot_dd >= mdd) + 1) / (n_boot + 1))
            p_vals["drawdown"] = p_dd
        else:
            notes.append("reference results too few for a drawdown bootstrap")

    finite = [p for p in p_vals.values() if math.isfinite(p)]
    min_p = min(finite) if finite else nan
    min_p_adj = min(1.0, min_p * len(finite)) if finite else nan
    if not finite:
        verdict = VERDICT_WITHIN
    elif min_p_adj < alpha_inconsistent:
        verdict = VERDICT_INCONSISTENT
    elif min_p < alpha_investigate:
        verdict = VERDICT_UNUSUAL
    else:
        verdict = VERDICT_WITHIN

    if mean_r < ref_mean_r:
        direction = "below reference"
    elif mean_r > ref_mean_r:
        direction = "above reference"
    else:
        direction = "in line"
    return ConsistencyReport(verdict, n, wins, float(win_rate), float(ref_p_win), p_wins, mean_r,
                             float(ref_mean_r), float(z_mean), p_mean, t_stat, p_t, float(mdd), dd_pct, p_dd,
                             int(streak), float(p_streak), float(min_p), float(min_p_adj), direction, notes)


# ---------------------------------------------------------------------------
# Section VI: probability is conditional
# ---------------------------------------------------------------------------
UNSPECIFIED = "(unspecified)"


def conditional_stats(df: pd.DataFrame, outcome_col: str, by: str | Sequence[str],
                      conf: float = 0.95) -> pd.DataFrame:
    """Per-condition statistics of an R outcome column (Section VI: probability is conditional).

    Groups ``df`` by ``by`` (one column name or several) and returns, for each
    condition: n, wins, win rate with a Wilson interval, mean R with a Student-t
    interval, sd, average win, average loss, expectancy (p * avg_win -
    (1 - p) * avg_loss, which equals the mean R) and total R. Rows with a
    missing outcome are dropped; missing or blank condition values are grouped
    as "(unspecified)". Sorted by n (largest first).
    """
    keys = [by] if isinstance(by, str) else list(by)
    missing = [c for c in keys + [outcome_col] if c not in df.columns]
    if missing:
        raise KeyError(f"columns not found: {missing}")
    cols = ["n", "wins", "win_rate", "win_ci_low", "win_ci_high", "mean_r", "mean_ci_low",
            "mean_ci_high", "sd_r", "avg_win_r", "avg_loss_r", "expectancy_r", "total_r"]
    data = df[keys].copy()
    for k in keys:
        s = data[k].astype("string").str.strip()
        data[k] = s.mask(s.isna() | (s == ""), UNSPECIFIED).astype(str)
    data["_r"] = pd.to_numeric(df[outcome_col], errors="coerce")
    data = data[np.isfinite(data["_r"].astype(float))]
    if data.empty:
        return pd.DataFrame(columns=keys + cols)
    rows = []
    for key, grp in data.groupby(keys, sort=True):
        key_t = key if isinstance(key, tuple) else (key,)
        ex = expectancy_from_results(grp["_r"].to_numpy(), conf=conf)
        lo, hi = wilson_interval(int(round(ex.win_rate * ex.n)), ex.n, conf)
        rows.append(dict(zip(keys, key_t)) | {
            "n": ex.n,
            "wins": int(round(ex.win_rate * ex.n)),
            "win_rate": ex.win_rate,
            "win_ci_low": lo,
            "win_ci_high": hi,
            "mean_r": ex.mean,
            "mean_ci_low": ex.ci_low,
            "mean_ci_high": ex.ci_high,
            "sd_r": ex.sd,
            "avg_win_r": ex.avg_win,
            "avg_loss_r": ex.avg_loss,
            "expectancy_r": expected_value(ex.win_rate, ex.avg_win, ex.avg_loss),
            "total_r": ex.total,
        })
    out = pd.DataFrame(rows, columns=keys + cols)
    return out.sort_values(["n"] + keys, ascending=[False] + [True] * len(keys), kind="mergesort") \
              .reset_index(drop=True)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
DISCLAIMER = "Education, not financial advice: conditional on the inputs above, not a forecast."


def _fmt_n(x: float) -> str:
    return "inf" if not math.isfinite(x) else f"{int(x):,}"


def _cmd_ev(a: argparse.Namespace) -> None:
    ev = expected_value(a.p, a.win, a.loss, a.cost)
    q = 1.0 - a.p
    print(f"Expected value per trade: {ev:.2f}")
    print(f"  = ({a.p:.2f} x {a.win:g}) - ({q:.2f} x {abs(a.loss):g}) - {a.cost:g}"
          f" = {a.p * a.win:.2f} - {q * abs(a.loss):.2f} - {a.cost:.2f}")
    if a.loss:
        b = a.win / abs(a.loss)
        cost_r = a.cost / abs(a.loss)
        print(f"  payoff ratio b = {b:.3f}; breakeven win rate incl. cost = "
              f"{breakeven_win_rate(b, cost_r):.1%}")
    print(DISCLAIMER)


def _cmd_breakeven(a: argparse.Namespace) -> None:
    print(f"Breakeven win rate at b = {a.rr:g}, cost = {a.cost:g}R: {breakeven_win_rate(a.rr, a.cost):.2%}")


def _cmd_wilson(a: argparse.Namespace) -> None:
    lo, hi = wilson_interval(a.wins, a.n, a.conf)
    post = beta_posterior(a.wins, a.n, threshold=a.threshold)
    print(f"Win rate {a.wins}/{a.n} = {a.wins / a.n:.1%}; Wilson {a.conf:.0%} CI: {lo:.3f} - {hi:.3f}")
    if post.prob_above_threshold is not None:
        print(f"Beta(1,1) posterior: P(p > {a.threshold:g}) = {post.prob_above_threshold:.3f}")


def _cmd_streak(a: argparse.Namespace) -> None:
    p = prob_losing_streak(a.p_loss, a.streak, a.trades)
    print(f"P(at least one run of >= {a.streak} losses in {a.trades} trades | p_loss = {a.p_loss:g}) = {p:.4f}")


def _cmd_ruin(a: argparse.Namespace) -> None:
    sim = simulate_equity(a.p, a.rr, a.risk, a.trades, a.paths, a.cost, a.ruin_dd, a.seed)
    s = sim.summary()
    print(f"Fixed-fractional simulation: p = {a.p:g}, b = {a.rr:g}, risk = {a.risk:.2%} per trade, "
          f"cost = {a.cost:g}R, {a.trades} trades x {a.paths} paths (seed {a.seed})")
    print(f"  expectancy per trade:            {s['expectancy_r_per_trade']:+.3f} R")
    print(f"  final equity (start 1.0) p5/p50/p95: {s['final_equity_p05']:.3f} / "
          f"{s['final_equity_median']:.3f} / {s['final_equity_p95']:.3f}")
    print(f"  P(final equity below start):     {s['prob_final_below_start']:.3f}")
    print(f"  max drawdown median / p95:       {s['max_drawdown_median']:.1%} / {s['max_drawdown_p95']:.1%}")
    print(f"  longest losing streak median / p95: {s['longest_losing_streak_median']:.0f} / "
          f"{s['longest_losing_streak_p95']:.0f}")
    print(f"  P(drawdown >= {a.ruin_dd:.0%}):            {s['prob_ruin']:.4f}")
    print(DISCLAIMER)


def _cmd_sample(a: argparse.Namespace) -> None:
    plan = trades_needed(a.p, a.rr, a.cost, a.conf, a.power)
    print(f"True expectancy {plan.expectancy_r:+.3f} R, sd {plan.sd_r:.3f} R per trade")
    print(f"  trades for a {a.conf:.0%} CI on expectancy to exclude 0 (power {a.power:.0%}): "
          f"{_fmt_n(plan.n_expectancy)}")
    print(f"  ... on an average sample (power 50%): {_fmt_n(plan.n_expectancy_typical)}")
    print(f"  trades for the win-rate CI to be within +-{plan.win_rate_half_width:.0%}: "
          f"{_fmt_n(plan.n_win_rate)}")


def _cmd_kelly(a: argparse.Namespace) -> None:
    f = kelly_fraction(a.p, a.rr, a.cost)
    print(f"Kelly fraction (p = {a.p:g}, b = {a.rr:g}, cost = {a.cost:g}R): {f:.4f}"
          + ("  (no positive edge: size 0)" if f <= 0 else ""))
    if a.wins is not None and a.n is not None:
        k = kelly_under_uncertainty(a.wins, a.n, a.rr, a.quantile, cost_r=a.cost)
        print(f"With {a.wins}/{a.n} wins: p_hat = {k.p_hat:.3f}, {a.quantile:.0%} posterior quantile = "
              f"{k.p_quantile:.3f}")
        print(f"  plug-in Kelly {k.kelly_point:.4f}; conservative Kelly {k.kelly_conservative:.4f}; "
              f"half of that {k.half_kelly_conservative:.4f}")
    print(DISCLAIMER)


def _cmd_recover(a: argparse.Namespace) -> None:
    print(f"A {a.loss:.0%} loss needs a {recovery_required(a.loss):.1%} gain to recover")


def build_parser() -> argparse.ArgumentParser:
    """Argument parser for the edge_lab command line."""
    p = argparse.ArgumentParser(prog="edge_lab", description=__doc__.split("\n\n")[0],
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("ev", help="expected value per trade (Section VII)")
    s.add_argument("--p", type=float, required=True, help="probability of winning")
    s.add_argument("--win", type=float, required=True, help="average win")
    s.add_argument("--loss", type=float, required=True, help="average loss (magnitude)")
    s.add_argument("--cost", type=float, default=0.0, help="average cost per trade")
    s.set_defaults(func=_cmd_ev)

    s = sub.add_parser("breakeven", help="breakeven win rate for a payoff ratio")
    s.add_argument("--rr", type=float, required=True)
    s.add_argument("--cost", type=float, default=0.0, help="cost per trade in R")
    s.set_defaults(func=_cmd_breakeven)

    s = sub.add_parser("wilson", help="Wilson interval and Beta posterior for a win rate (Section VI)")
    s.add_argument("--wins", type=int, required=True)
    s.add_argument("--n", type=int, required=True)
    s.add_argument("--conf", type=float, default=0.95)
    s.add_argument("--threshold", type=float, default=None, help="report P(p > threshold)")
    s.set_defaults(func=_cmd_wilson)

    s = sub.add_parser("streak", help="exact probability of a losing streak (Section XI)")
    s.add_argument("--p-loss", type=float, required=True)
    s.add_argument("--streak", type=int, required=True)
    s.add_argument("--trades", type=int, required=True)
    s.set_defaults(func=_cmd_streak)

    s = sub.add_parser("ruin", help="simulate fixed-fractional equity paths (Section XIV)")
    s.add_argument("--p", type=float, required=True)
    s.add_argument("--rr", type=float, required=True)
    s.add_argument("--risk", type=float, required=True, help="fraction of equity risked per trade")
    s.add_argument("--trades", type=int, default=250)
    s.add_argument("--paths", type=int, default=10_000)
    s.add_argument("--cost", type=float, default=0.0)
    s.add_argument("--ruin-dd", type=float, default=0.5, help="drawdown counted as ruin")
    s.add_argument("--seed", type=int, default=0)
    s.set_defaults(func=_cmd_ruin)

    s = sub.add_parser("sample", help="trades needed before the evidence separates edge from zero (Section VI)")
    s.add_argument("--p", type=float, required=True)
    s.add_argument("--rr", type=float, required=True)
    s.add_argument("--cost", type=float, default=0.0)
    s.add_argument("--conf", type=float, default=0.95)
    s.add_argument("--power", type=float, default=0.8)
    s.set_defaults(func=_cmd_sample)

    s = sub.add_parser("kelly", help="Kelly fraction, optionally under win-rate uncertainty (Section XIV)")
    s.add_argument("--p", type=float, required=True)
    s.add_argument("--rr", type=float, required=True)
    s.add_argument("--cost", type=float, default=0.0)
    s.add_argument("--wins", type=int, default=None)
    s.add_argument("--n", type=int, default=None)
    s.add_argument("--quantile", type=float, default=0.05)
    s.set_defaults(func=_cmd_kelly)

    s = sub.add_parser("recover", help="gain needed to recover a loss (Section XIV)")
    s.add_argument("--loss", type=float, required=True, help="loss as a fraction, e.g. 0.5")
    s.set_defaults(func=_cmd_recover)
    return p


def main(argv: Sequence[str] | None = None) -> int:
    """Run the edge_lab CLI; returns a process exit code."""
    args = build_parser().parse_args(argv)
    try:
        args.func(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
