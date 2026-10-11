---
id: concept_scalping
type: concept
title: Scalping
partition: 07_concepts
layer: L4
aliases: [scalping, scalper, intraday, 1-minute chart, tick chart]
related: [concept_order_flow, concept_market_microstructure, concept_trading_sessions_killzones, concept_trade_execution, concept_probability_fat_tails, concept_prop_firm_risk_rules]
status: synthesized
---

# Scalping

**Holding periods of seconds to minutes, targeting small moves, with many
trades.** It is the style of several Chart Fanatics headliners: Fabio
Valentini, billed as the "#1 scalper in the world", whose live-trading
episode is the channel's most-viewed video (~3.7M views per an aggregator);
Candace Lau (NQ sweep reversals); JJ Simon (NQ 1-minute).

## What makes or breaks scalping

| Factor | Why |
|---|---|
| **Costs** | Commissions and spread are a large fraction of each target. Edge must exceed cost per trade by a margin. |
| **Execution quality** | Slippage on stops; queue position on limits ([[concept_trade_execution]]) |
| **Order flow** | The only "fundamentals" at this horizon ([[concept_order_flow]]) |
| **Time-of-day** | Only trade the liquid windows ([[concept_trading_sessions_killzones]]) |
| **Risk per trade** | Small (Fabio ≈ 0.25%/trade per a T3 source) with daily loss limits |

## Competition evidence

Fabio Valentini placed in the top three of the **Robbins World Cup Trading
Championship** futures division. Sources cite returns from 218% to 500%+ in
a single year depending on the edition, which makes this one of the few
audited data points in this partition (T1/T2, numbers vary by source).

## Warnings

High win rates with small targets can mask negative skew
([[concept_probability_fat_tails]]). Many prop-firm-funded scalpers pass
evaluations and then fail in live markets: prop-firm conditions differ from
live trading ([[concept_prop_firm_risk_rules]]).
