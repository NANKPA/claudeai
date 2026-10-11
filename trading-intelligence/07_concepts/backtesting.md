---
id: concept_backtesting
type: concept
title: Backtesting (manual & systematic)
partition: 07_concepts
layer: L8
aliases: [backtest, manual backtesting, replay, forward test, paper trading, Monte Carlo, walk forward]
related: [concept_overfitting_validation, concept_performance_metrics, concept_edge, concept_machine_learning_finance, concept_trading_journal_review]
status: synthesized
---

# Backtesting

**Testing a rule set on historical data before risking capital.**

## Manual (discretionary) backtesting

- Bar-replay through history, logging every valid setup by the written rules.
- Marci Silfrain spends hours every day **backtesting, sim trading, and
  paper trading**, more time than she spends live.
- Weakness: hindsight bias and lenient rule interpretation. Write the rules
  down first, and log *every* instance, including the ugly ones.

## Systematic backtesting

1. **Clean data:** survivorship-free; adjusted futures (back-adjusted vs
   ratio); realistic sessions.
2. **Realistic costs:** commissions, spread, slippage (especially on stops and
   around news).
3. **No look-ahead:** signals use only information available at the decision
   time. Beware repainting indicators and synthetic Heikin-Ashi fills.
4. **Out-of-sample and walk-forward tests,** plus Monte Carlo resampling of
   trade order for drawdown distributions ([[concept_risk_of_ruin_drawdown]]).

## Examples in this knowledge base

- **TG Capital Trident reconstruction** (TakeProfit): EURUSD M30, ~20% win
  rate, profitable out-of-sample 2023–24. One self-published test.
- **JJ Simon NQ 1-minute backtest video:** ~52% win rate and 1.66 profit
  factor *after filtering and parameter changes* (note the overfitting risk).

See [[concept_overfitting_validation]] before believing any backtest.
