---
id: concept_risk_of_ruin_drawdown
type: concept
title: Risk of Ruin & Drawdown Math
partition: 07_concepts
layer: L6
aliases: [risk of ruin, drawdown, max drawdown, recovery math, losing streak, gambler's ruin]
related: [concept_position_sizing, concept_kelly_criterion_optimal_f, concept_probability_fat_tails, concept_prop_firm_risk_rules, concept_trading_psychology]
status: synthesized
---

# Risk of Ruin & Drawdown Math

## Recovery asymmetry

`gain needed to recover = 1/(1 − DD) − 1`

| Drawdown | Gain needed |
|---|---|
| 10% | 11.1% |
| 20% | 25% |
| 30% | 42.9% |
| 50% | 100% |
| 75% | 300% |

## Losing streaks are normal

The probability of at least one run of `k` consecutive losses in `N` trades
is high, even with good systems. At a 40% win rate, a streak of 10+ losses
within 500 trades is likely. Marci Silfrain's advice: **plan to lose on every
trade, and plan to lose the next 20 in a row.**

With fixed fractional risk `f`, a streak of `k` losses costs
`1 − (1 − f)^k`: at 1% × 20 losses ≈ 18%, and at 5% × 20 losses ≈ 64%.

## Risk of ruin (gambler's ruin, simplified)

For a per-trade edge with win probability `p > 0.5` at even odds, and capital
of `U` betting units: `RoR ≈ ((1 − p)/p)^U`. Smaller bets (more units) mean
exponentially lower ruin. That is the formal reason for small fractional
risk. In practice, estimate ruin probability by **Monte Carlo resampling of
your R-multiple distribution** ([[concept_backtesting]]).

## Practical guardrails

- Max daily loss (e.g., 2–3R), weekly loss limit, and hard stop on an equity
  drawdown → reduce size by half ([[concept_prop_firm_risk_rules]]).
- JJ Simon: **stop reversion trades after three consecutive losses** (T3).
