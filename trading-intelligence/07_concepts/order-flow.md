---
id: concept_order_flow
type: concept
title: Order Flow (footprint, delta, CVD, absorption, trapped traders)
partition: 07_concepts
layer: L1
aliases: [footprint chart, cumulative volume delta, CVD, delta, absorption, tape reading, DOM, bookmap, imbalance]
related: [concept_market_microstructure, concept_auction_market_theory, concept_volume_profile, concept_liquidity, concept_scalping, concept_trade_execution]
derived_from: [concept_market_microstructure]
influenced_by: [person_richard_wyckoff, person_humphrey_neill, person_peter_steidlmayer]
sources:
  - {title: "TradeZella — Order Flow Strategy (Trader Yush)", url: "https://www.tradezella.com/strategies/order-flow-strategy", tier: T3}
  - {title: "Chart Fanatics — Yush's Strategy: Trading Trapped Buyers & Sellers with Order Flow", url: "https://www.chartfanatics.com/strategies/order-flow-strategy", tier: T2}
  - {title: "Bookmap — key order flow strategies", url: "https://bookmap.com/en/blog/key-order-flow-strategies-breakouts-trends-trapped-traders-and-stop-runs", tier: T3}
status: synthesized
---

# Order Flow

**Order flow = reading who is aggressive, and whether they are succeeding.**
It is the modern, instrumented descendant of tape reading (Wyckoff's
*Studies in Tape Reading*, 1910; Neill's *Tape Reading and Market Tactics*,
1931).

## Instruments

| Tool | What it shows |
|---|---|
| **Time & sales (tape)** | Every print: price, size, aggressor side |
| **DOM / heatmap (e.g., Bookmap)** | Resting limit liquidity, pulls and stacks |
| **Footprint chart** | Bid vs ask volume traded *at each price inside each bar* |
| **Delta** | Ask-volume minus bid-volume per bar (net aggression) |
| **Cumulative volume delta (CVD)** | Running sum of delta. Divergence from price signals weakening aggression. |
| **Imbalances** | Diagonal bid/ask ratios above a threshold (e.g., 300%) |

## Core reads

1. **Absorption.** Heavy aggressive selling into a level while price does
   *not* fall means passive buyers are absorbing. That signals a potential
   reversal or support.
2. **Exhaustion.** Aggression dries up at the extreme of a move.
3. **Initiative vs responsive** activity (AMT language,
   [[concept_auction_market_theory]]).
4. **Trapped traders.** Aggressive buyers late into a move, followed by a
   failure to continue. Their stop-outs then fuel the reversal. This is the
   order-flow description of a [[concept_liquidity_sweep_reversal]].
5. **Large-lot detection.** Yush's framework flags prints of roughly 75+ lots
   on NQ and 200+ on ES, and needs **at least 2 confirmations** (absorption,
   delta, trapped traders) at a pre-marked zone (T3 source).

## Why futures

Order flow requires real, centralized volume. That is why it is applied to
CME futures (NQ, ES, CL, GC) and rarely to spot FX
([[concept_market_microstructure]]).

## Chart Fanatics usage

Fabio Valentini (volume profile + footprint + CVD inside AMT) and Trader Yush
(absorption and trapped traders) are the channel's main order-flow voices.
Fabio co-founded the order-flow platform Deep Charts.
