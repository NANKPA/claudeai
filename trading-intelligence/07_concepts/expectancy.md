---
id: concept_expectancy
type: concept
title: Expectancy (expected value per trade)
partition: 07_concepts
layer: L6
aliases: [expectancy, expected value, EV, SQN, system quality number, profit factor]
related: [concept_edge, concept_risk_reward_r_multiples, concept_position_sizing, concept_performance_metrics, concept_probabilistic_thinking]
influenced_by: [person_van_tharp, person_ed_thorp]
status: synthesized
---

# Expectancy

`E[R] = p·W̄_R − (1 − p)·L̄_R` (in R-multiples)

Example: 40% win rate, average win 2.5R, average loss 1R →
`E = 0.4×2.5 − 0.6×1 = +0.4R per trade`. Over 100 trades at 1% risk that is
roughly +40% before compounding and costs.

## Related statistics

- **Profit factor** = gross profit ÷ gross loss.
- **SQN (Van Tharp)** = `√N · mean(R) / stdev(R)`. It captures expectancy
  *and* consistency. It is essentially a t-statistic of the edge.
- **Expectancy per unit time** = E × trades per period. A small edge traded
  often can beat a large edge traded rarely ([[concept_scalping]]).

## Win rate is not expectancy

| System | Win % | Avg W | Avg L | E (R) |
|---|---|---|---|---|
| Trend follower | 35% | 3.0R | 1R | +0.40 |
| Scalper | 75% | 0.4R | 1R | +0.05 |
| Mean reverter (blowup-prone) | 85% | 0.3R | 2.5R | −0.12 |

The third looks great for months and is a losing system
([[concept_probability_fat_tails]]).

Mark Douglas's insight: once you *think in expectancy*, a single loss carries
no information, so you can execute without fear ([[concept_probabilistic_thinking]]).
