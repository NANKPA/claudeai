---
id: concept_order_blocks_breakers
type: concept
title: Order Blocks, Breaker Blocks & Mitigation
partition: 07_concepts
layer: L3
aliases: [order block, OB, breaker, breaker block, mitigation block, supply and demand zone, point of interest, POI]
related: [concept_smart_money_concepts, concept_fair_value_gap, concept_support_resistance, concept_market_structure, concept_liquidity]
derived_from: [concept_support_resistance, concept_wyckoff_method]
influenced_by: [person_michael_huddleston]
sources:
  - {title: "TradeZella — Structure + OTE (Trader Mayne)", url: "https://www.tradezella.com/strategies/structure-ote", tier: T3}
status: synthesized
---

# Order Blocks & Breakers

## Order block (OB)

The **last opposing candle before a displacement that breaks structure**. A
bullish OB is the last down-close candle before a strong up-move that
creates a BOS. The theory: unfilled institutional orders remain there, so
price reacts on return. Classic "supply/demand zone" traders describe the
same base. The ICT label is newer than the idea.

## Breaker block

A **failed order block**. Price sweeps liquidity, then breaks back through
the OB that should have held. The failed bullish OB becomes a **bearish
breaker** (and vice versa). The sequence *sweep → failure → structure
reclaim* is the breaker setup Trader Mayne uses as his lower-timeframe
confirmation.

## Mitigation block

Like a breaker, but without the liquidity sweep (a failure swing that does
not make a new extreme).

## Trader Mayne's Structure + OTE (T3 summary)

1. HTF (daily/weekly) **clean structure break**.
2. Mark the **POI that caused it**: an order block or breaker.
3. Wait for price to return to the POI (ideally in the
   [[concept_premium_discount_ote]] zone).
4. LTF confirmation: a **breaker**, i.e., a failed move that sweeps
   liquidity and reclaims structure.
5. Stop beyond the sweep. Target the HTF liquidity.

## Caveat

Breaker and OB zones work best as **confluence** (with FVG, structure, and
liquidity), not as standalone triggers. Several indicator authors explicitly
warn against using breakers alone.
