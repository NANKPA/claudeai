---
id: concept_performance_metrics
type: concept
title: Performance Metrics (Sharpe, Sortino, MAR, profit factor)
partition: 07_concepts
layer: L8
aliases: [Sharpe ratio, Sortino ratio, Calmar, MAR, profit factor, win rate, average R, ulcer index, CAGR]
related: [concept_expectancy, concept_overfitting_validation, concept_risk_of_ruin_drawdown, concept_trading_journal_review]
influenced_by: [person_william_sharpe]
status: synthesized
---

# Performance Metrics

| Metric | Formula | Read |
|---|---|---|
| **CAGR** | `(End/Start)^(1/years) − 1` | Growth |
| **Sharpe** | `(R − R_f)/σ` (annualise: × √periods) | Return per unit of total vol; assumes roughly normal returns |
| **Sortino** | `(R − R_f)/σ_downside` | Penalises only downside vol |
| **Max drawdown** | Largest peak-to-trough decline | Pain / survivability |
| **MAR / Calmar** | CAGR / MaxDD | Classic CTA metric |
| **Profit factor** | Gross profit / gross loss | >1.5 is solid for discretionary trading |
| **Expectancy (R)** | `p·W̄ − q·L̄` | Edge per trade ([[concept_expectancy]]) |
| **SQN** | `√N·mean(R)/sd(R)` | Edge consistency |
| **Skew & kurtosis** | 3rd and 4th moments | Hidden tail risk ([[concept_probability_fat_tails]]) |

## Interpretation rules

- A **Sharpe > 3** on a short sample is more likely luck, error, or hidden
  tail risk than genius ([[concept_overfitting_validation]]).
- Compare strategies on **the same risk** (vol-normalised).
- Negative skew plus a high Sharpe is the signature of short-vol and
  martingale-like systems.
