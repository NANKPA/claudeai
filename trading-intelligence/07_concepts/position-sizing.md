---
id: concept_position_sizing
type: concept
title: Position Sizing
partition: 07_concepts
layer: L6
aliases: [position sizing, fixed fractional, percent risk, volatility targeting, turtle unit, money management, risk per trade]
related: [concept_kelly_criterion_optimal_f, concept_risk_of_ruin_drawdown, concept_expectancy, concept_volatility, concept_leverage_margin, concept_correlation_portfolio_risk, concept_prop_firm_risk_rules]
influenced_by: [person_van_tharp, person_ralph_vince, person_ed_thorp, person_richard_dennis]
status: synthesized
---

# Position Sizing

**"Position sizing is the part of your system that tells you how much."**
(Van Tharp). It determines whether an edge compounds or ruins you. BabyPips
Senior covers it.

## Models

| Model | Rule | Notes |
|---|---|---|
| **Fixed fractional (% risk)** | `size = equity × f / (stop distance × point value)` | Industry default; f = 0.25–1% for discretionary traders, ~0.5–2% for systematic |
| **Volatility unit (Turtle)** | `units = (equity × 1%) / (N × $ per point)` | Equalises risk across markets ([[concept_volatility]]) |
| **Volatility targeting** | Scale exposure so portfolio vol ≈ target (e.g., 10–20% annual) | Carver, CTAs |
| **Kelly / fractional Kelly** | `f* = p − q/b` (binary bets) | Growth-optimal; use ¼–½ Kelly ([[concept_kelly_criterion_optimal_f]]) |
| **Optimal f (Vince)** | Maximise TWR from the trade list | Aggressive; huge drawdowns |
| **Meta-labeled sizing** | Size ∝ ML-estimated probability of success | ([[concept_machine_learning_finance]]) |

## Rules worth tattooing

1. **Risk is set by stop × size, never by leverage** ([[concept_leverage_margin]]).
2. **Size down in drawdowns and in unfamiliar regimes;** size up only with
   evidence.
3. **Account for correlation:** five correlated positions at 1% each are one
   5% bet ([[concept_correlation_portfolio_risk]]).
4. **Per-trade, per-idea, per-day risk budgets with circuit breakers**
   (BabyPips Senior; prop-firm practice) ([[concept_prop_firm_risk_rules]]).

## In this knowledge base

Fabio Valentini ~0.25% per trade (T3). The Turtles' 1% per N unit. Gianluca
Bruni (Chart Fanatics guest, announced) on building statistical models around
a strategy.
