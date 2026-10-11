---
id: concept_volume_profile
type: concept
title: Volume Profile (POC, value area, HVN/LVN)
partition: 07_concepts
layer: L1
aliases: [POC, point of control, value area, VAH, VAL, HVN, LVN, high volume node, low volume node]
related: [concept_auction_market_theory, concept_vwap, concept_order_flow, concept_support_resistance, concept_mean_reversion]
derived_from: [concept_auction_market_theory]
influenced_by: [person_peter_steidlmayer, person_james_dalton]
sources:
  - {title: "TradeZella — Volume Profile Strategy (Forrest Knight)", url: "https://www.tradezella.com/strategies/volume-profile-strategy", tier: T3}
status: synthesized
---

# Volume Profile

A horizontal histogram of **volume traded at each price** over a chosen
window: session, composite, or anchored.

## Anatomy

- **POC (Point of Control).** The price with the most volume. It is the
  "fairest" price, and price is magnetically drawn to it in balance.
- **Value Area (VA).** The range holding ~70% of volume, bounded by **VAH**
  and **VAL**.
- **HVN (high-volume node).** Price was accepted there. It acts as
  support/resistance and price slows in it.
- **LVN (low-volume node).** Price was rejected there. Price travels fast
  through it, and it often marks the edge between two distributions.

## Canonical plays

| Play | Logic |
|---|---|
| **Fade the edge back to POC** | In balance, rejection at VAH/VAL targets POC ([[concept_mean_reversion]]) |
| **80% rule** (Dalton/Market Profile lore) | If price opens outside value and re-enters it, holding for two TPO periods, it often traverses to the other side of value |
| **Edge-to-edge through LVN** | Forrest Knight: trade the reaction at the edge of an HVN at key auction levels (PDH/PDL, ONH/ONL), targeting the next node through the low-volume gap. Wait for the **signal candle to close** with a rejecting wick (T3). |
| **Breakout acceptance** | Value migrating beyond prior VAH, with volume building, confirms imbalance ([[concept_breakout_trading]]) |

## Relation to VWAP

VWAP is the *volume-weighted mean* price. POC is the *volume mode*. Both
estimate fair value and both are used as mean-reversion anchors
([[concept_vwap]]).
