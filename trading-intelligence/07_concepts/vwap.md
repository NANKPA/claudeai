---
id: concept_vwap
type: concept
title: VWAP (volume-weighted average price) & anchored VWAP
partition: 07_concepts
layer: L1
aliases: [VWAP, anchored VWAP, AVWAP, VWAP bands]
related: [concept_volume_profile, concept_auction_market_theory, concept_mean_reversion, concept_optimal_execution_market_impact, concept_moving_averages]
influenced_by: [person_brian_shannon]
status: synthesized
---

# VWAP

`VWAP_t = Σ(Pᵢ·Vᵢ) / Σ Vᵢ`, accumulated from an anchor (session open by
default).

## Two worlds, one line

1. **Execution benchmark** (institutional). Large orders are judged against
   VWAP. VWAP algorithms slice orders in proportion to the expected volume
   curve ([[concept_optimal_execution_market_impact]]). Institutional
   participation is one reason VWAP behaves as a real level.
2. **Trading level** (discretionary). Price above VWAP means buyers are in
   control on average for the session; below means sellers. Standard-deviation
   bands give mean-reversion extremes.

## Anchored VWAP

Anchor at a meaningful event (earnings gap, swing low, news candle,
[[concept_episodic_pivot]]) to see the average cost basis of everyone who has
traded since. Brian Shannon popularised AVWAP among swing traders.

## Uses in this knowledge base

- Fair-value anchor alongside POC in AMT-based strategies.
- JJ Simon's **Fair Pricing Theory** treats a reference price at the NY open
  as "fair" and trades reversion toward it. That is conceptually the same
  move as VWAP or POC reversion (`strategy_jj_simon_fair_pricing`).
