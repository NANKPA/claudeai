---
id: concept_overfitting_validation
type: concept
title: Overfitting & Edge Validation (multiple testing, deflated Sharpe)
partition: 07_concepts
layer: L8
aliases: [overfitting, curve fitting, data snooping, multiple testing, deflated Sharpe ratio, probability of backtest overfitting, PBO, walk-forward, out-of-sample]
related: [concept_backtesting, concept_machine_learning_finance, concept_performance_metrics, concept_random_walk_efficient_markets, concept_edge]
influenced_by: [person_marcos_lopez_de_prado, person_david_aronson]
status: synthesized
---

# Overfitting & Edge Validation

**If you test enough variations, something will look great by chance.**

## The core problem

With N independent strategy trials of zero true skill, the **expected maximum
Sharpe ratio** grows roughly as `√(2·ln N)`. After testing 100 variants, a
Sharpe ≈ 3 (annualised over a short sample) can be pure noise.

## Defences

| Technique | Idea |
|---|---|
| **Hypothesis first** | An economic or microstructural reason for the edge ([[concept_edge]]) |
| **Out-of-sample holdout** | Never touched during design |
| **Walk-forward** | Re-optimise on rolling windows; evaluate only the forward segments |
| **Parameter robustness** | Performance should form a plateau, not a spike, across parameter values |
| **Deflated Sharpe ratio** (Bailey & López de Prado) | Adjust the Sharpe for the number of trials, skew, and kurtosis |
| **PBO / CSCV** | Combinatorially symmetric cross-validation estimates the probability that the in-sample best underperforms out-of-sample |
| **White's Reality Check / SPA** | Data-snooping-robust tests (used in Aronson's *Evidence-Based Technical Analysis*) |
| **Live forward test at small size** | The final arbiter |

## Applied to YouTube strategies

A strategy presented in a video is the **survivor of an invisible selection
process** (of traders, of strategies, of chart examples). Treat every claim
as T4 until you have run your own out-of-sample test
([[concept_backtesting]]).
