---
id: concept_probability_fat_tails
type: concept
title: Probability, Distributions & Fat Tails
partition: 07_concepts
layer: L0
aliases: [fat tails, kurtosis, black swans, power laws]
related: [concept_random_walk_efficient_markets, concept_volatility, concept_risk_of_ruin_drawdown, concept_kelly_criterion_optimal_f, concept_edge]
influenced_by: [person_benoit_mandelbrot, person_nassim_taleb, person_et_jaynes]
covers: []
status: synthesized
---

# Probability, Distributions & Fat Tails

**Core idea.** Returns are *not* normally distributed. They have fat tails
(excess kurtosis), volatility clustering, and skew. Extreme moves happen orders
of magnitude more often than a Gaussian model predicts.

## Key facts every trader should hold

- **Daily equity-index returns** routinely show 5–10σ days that a normal
  distribution would place once in thousands of years. October 1987 was
  roughly a −20σ day under a Gaussian model.
- **Power laws.** Mandelbrot (1963, cotton prices) showed price changes follow
  stable Paretian or power-law tails. The variance may be unstable or, in the
  extreme, undefined.
- **Sample statistics lie in fat-tailed worlds.** The sample mean and
  variance converge slowly. A strategy's historical Sharpe ratio can be
  dominated by a few observations (Taleb, *Statistical Consequences of Fat
  Tails*).
- **Bayesian updating** (Jaynes) is the right frame for edge estimation.
  Your win rate is a posterior belief, not a constant.

## Trading implications

| Implication | Where it lands |
|---|---|
| Size for the tail, not the average | [[concept_position_sizing]], [[concept_risk_of_ruin_drawdown]] |
| Short-volatility and high-win-rate strategies hide tail risk ("picking up pennies in front of a steamroller") | [[concept_options_greeks]], [[concept_scalping]] |
| Stops do not guarantee max loss (gaps, limit moves) | [[concept_trade_management]] |
| Use full Kelly only with a known distribution; use fractional Kelly in practice | [[concept_kelly_criterion_optimal_f]] |

## Lineage

Bachelier (1900, Gaussian random walk) → Mandelbrot (1963, fat tails) →
Fama (1965, documents leptokurtosis) → Taleb (2001–2020, operational
consequences). See [[concept_random_walk_efficient_markets]].
