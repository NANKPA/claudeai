---
id: concept_market_microstructure
type: concept
title: Market Microstructure (order book, bid/ask, order types)
partition: 07_concepts
layer: L1
aliases: [limit order book, LOB, bid-ask spread, DOM, depth of market, market maker]
related: [concept_liquidity, concept_order_flow, concept_auction_market_theory, concept_optimal_execution_market_impact, concept_trade_execution]
influenced_by: [person_larry_harris, person_maureen_ohara, person_albert_kyle, person_jean_philippe_bouchaud]
status: synthesized
---

# Market Microstructure

**How orders become prices.** Every chart pattern is the visible residue of
order-book events.

## The limit order book

- **Limit orders** rest in the book and *provide* liquidity (bid below,
  ask above).
- **Market orders** *consume* liquidity. They cross the spread and execute
  against resting orders.
- **Price moves** only when aggressive orders exhaust the resting liquidity
  at a level, or when liquidity providers pull or reprice their quotes.
- **Spread** = ask − bid. It is the cost of immediacy. It widens in fast
  markets and around news ([[concept_news_trading]]).
- **Stop orders** are dormant market orders. A cluster of stops is a pool of
  latent aggressive flow that can be triggered ([[concept_liquidity]],
  [[concept_liquidity_sweep_reversal]]).

## Canonical models

| Model | Insight |
|---|---|
| **Kyle (1985)** | Informed traders hide in noise flow; price impact λ ∝ σ_value/σ_noise |
| **Glosten-Milgrom (1985)** | Spread compensates market makers for adverse selection by informed traders |
| **Roll (1984)** | Effective spread can be estimated from negative serial covariance of price changes |
| **Square-root impact law** (Bouchaud et al.) | Impact of a metaorder ≈ `Y·σ·√(Q/V)`, roughly independent of market (see [[concept_optimal_execution_market_impact]]) |

## Market-specific notes

- **Spot FX** is decentralized (OTC). There is no consolidated volume, so
  futures volume (6E, 6B…) or tick volume is used as a proxy. BabyPips teaches
  this structure in its early courses.
- **Futures (ES, NQ, CL, GC)** run on a central limit order book with real
  volume and transparent DOM. This is why order-flow and auction traders
  (Fabio Valentini, Yush, Forrest Knight) focus on futures.
- **Equities** are fragmented across many venues. NBBO, dark pools, and
  payment for order flow change the picture (Harris, *Trading and Exchanges*).
