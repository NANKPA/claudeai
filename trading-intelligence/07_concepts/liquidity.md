---
id: concept_liquidity
type: concept
title: Liquidity (resting orders, stop pools, sweeps)
partition: 07_concepts
layer: L1
aliases: [liquidity pool, liquidity sweep, liquidity run, buy-side liquidity, sell-side liquidity, stop hunt, liquidity grab, equal highs, equal lows]
related: [concept_market_microstructure, concept_market_structure, concept_liquidity_sweep_reversal, concept_smart_money_concepts, concept_order_flow, concept_amd_power_of_three]
derived_from: [concept_wyckoff_method, concept_market_microstructure]
influenced_by: [person_michael_huddleston, person_richard_wyckoff]
sources:
  - {title: "Chart Fanatics — Liquidity Grab Trading Strategy (Marco Trades)", url: "https://www.chartfanatics.com/playbook/liquidity-playbook", tier: T2}
  - {title: "TradeZella — NQ Liquidity Sweep & Reversal (Candace Lau)", url: "https://www.tradezella.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy", tier: T3}
status: synthesized
---

# Liquidity

Two meanings that traders often conflate:

1. **Microstructure liquidity.** How much size can trade near the current
   price without moving it (depth, spread, resiliency). See
   [[concept_market_microstructure]].
2. **"Liquidity" in SMC/ICT usage.** *Where resting orders, especially stop
   orders, cluster.* These are the pools that large participants need in
   order to fill size.

## Where liquidity rests (sense 2)

| Pool | Why orders sit there |
|---|---|
| **Above swing highs / below swing lows** | Stops of traders positioned against the move; breakout entry orders |
| **Equal highs / equal lows** ("double tops/bottoms") | Retail traders treat them as strong S/R, so stops stack just beyond |
| **Session extremes** (Asia high/low, London high/low, prior-day high/low, overnight high/low) | Reference levels used by many participants ([[concept_trading_sessions_killzones]]) |
| **Trendline touches** | Stops sit under the "obvious" trendline ([[concept_trendlines]]) |
| **Round numbers** | Order clustering |

**Buy-side liquidity (BSL)** sits above highs (buy stops). **Sell-side
liquidity (SSL)** sits below lows (sell stops).

## The core mechanic

A large seller needs buyers. Triggering the buy stops above a high supplies
those buyers, so the seller can fill while price trades *through* the high
(the **sweep**). If no genuine demand follows, price reverses: a
**liquidity sweep / stop hunt / spring / upthrust**. The important part is
not that price reached the pool, but *what happens after it is taken*
(Candace Lau's framing): displacement and a market-structure shift confirm
the reversal ([[concept_liquidity_sweep_reversal]]).

## Lineage

This is Wyckoff's **spring** and **upthrust** (1930s), re-described by ICT in
the 2010s as liquidity runs ([[concept_wyckoff_method]] →
[[concept_smart_money_concepts]]). Tape readers and order-flow traders
describe the same event as **trapped traders** ([[concept_order_flow]]).

## Pitfalls

- Hindsight bias: every reversal *looks* like a sweep afterwards. Require a
  confirmation rule.
- Liquidity is a **target** as well as a reversal point. In a trending
  market, price often runs a pool and *continues* to the next one.
