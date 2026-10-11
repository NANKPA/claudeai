---
id: concept_trading_journal_review
type: concept
title: Trading Journal & Performance Review
partition: 07_concepts
layer: L8
aliases: [trading journal, trade log, review, MAE, MFE, playbook review, tradezella]
related: [concept_performance_metrics, concept_trading_plan, concept_trading_psychology, concept_backtesting, concept_expectancy]
influenced_by: [person_brett_steenbarger]
status: synthesized
---

# Trading Journal & Review

**The feedback loop that turns trades into data.** Tools such as TradeZella
host public "playbooks" of many Chart Fanatics guests' strategies.

## Fields that matter

| Field | Why |
|---|---|
| Setup tag / grade (A+, A, B) | Expectancy *per setup* ([[concept_expectancy]]) |
| Planned entry, stop, target; actual fills | Execution slippage ([[concept_trade_execution]]) |
| R result, MAE, MFE | Stop and target optimisation |
| Session / time | Time-of-day edge ([[concept_trading_sessions_killzones]]) |
| Regime label | When the setup works ([[concept_market_regimes]]) |
| Rule adherence (Y/N), emotion tags | Psychology leaks ([[concept_trading_psychology]]) |
| Screenshot before and after | Pattern-recognition training |

## Review cadence

- **Daily:** adherence, mistakes, one lesson.
- **Weekly:** stats by setup and session; cut the worst-performing context.
- **Monthly/quarterly:** edge decay check; compare to backtest expectations
  ([[concept_overfitting_validation]]).

Steenbarger's approach: review what you do *well* as rigorously as your
mistakes, and do more of it.
