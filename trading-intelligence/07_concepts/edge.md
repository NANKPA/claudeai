---
id: concept_edge
type: concept
title: Edge (positive expectancy, repeatable)
partition: 07_concepts
layer: L0
aliases: [trading edge, statistical edge, alpha]
related: [concept_expectancy, concept_probabilistic_thinking, concept_backtesting, concept_overfitting_validation, concept_performance_metrics]
derived_from: [concept_probability_fat_tails]
influenced_by: [person_ed_thorp, person_mark_douglas]
status: synthesized
---

# Edge

**Definition.** An edge is a *repeatable* condition under which the expected
value of a trade, after costs, is positive. It is a property of a
**distribution of outcomes**, never of a single trade.

**Formally:** `E = p·W̄ − (1−p)·L̄ − costs > 0`, where `p` is the win rate,
`W̄` the average win and `L̄` the average loss (see [[concept_expectancy]]).

## What edge is made of

1. **A cause.** Someone is on the other side for a structural reason: forced
   liquidation, hedging flow, stop clusters ([[concept_liquidity]]),
   behavioural bias, a risk premium ([[concept_carry_trade]]), or an
   informational lag.
2. **A detector.** A rule that identifies the condition with acceptable false
   positives (the setup, L4).
3. **An execution path.** A way to capture it without costs and slippage
   eating it ([[concept_optimal_execution_market_impact]]).
4. **A survival layer.** Sizing that lets the law of large numbers play out
   ([[concept_position_sizing]], [[concept_risk_of_ruin_drawdown]]).

## Lineage

Thorp framed edge in casino terms first (card counting gives a measurable
advantage) and carried the same logic to markets, sizing it with the Kelly
criterion. Mark Douglas made the psychological corollary famous: *"anything can
happen"* on one trade, while the edge plays out over a series.

## Pitfalls

- **Edge ≠ win rate.** Trend followers win 30–40% of the time and still have
  an edge. Many 80%-win-rate scalpers have none once costs are counted.
- **Edges decay** as they are crowded. Monitor them with
  [[concept_trading_journal_review]].
- A backtest is a *hypothesis* about edge until it survives
  out-of-sample testing ([[concept_overfitting_validation]]).
