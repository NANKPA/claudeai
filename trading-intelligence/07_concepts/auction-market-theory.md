---
id: concept_auction_market_theory
type: concept
title: Auction Market Theory (balance, imbalance, value)
partition: 07_concepts
layer: L1
aliases: [AMT, market auction theory, balance and imbalance, market profile, TPO]
related: [concept_volume_profile, concept_vwap, concept_order_flow, concept_market_regimes, concept_mean_reversion, concept_breakout_trading]
influenced_by: [person_peter_steidlmayer, person_james_dalton]
derived_from: [concept_market_microstructure]
status: synthesized
---

# Auction Market Theory (AMT)

**Origin.** J. Peter Steidlmayer developed **Market Profile** at the Chicago
Board of Trade in the early-to-mid 1980s. He organised price by *time spent
at price* (TPO letters) and showed that markets behave as a continuous
two-sided auction. James Dalton's *Mind Over Markets* (1990) and *Markets in
Profile* (2007) turned it into a trading discipline.

## Axioms

1. **The market's purpose is to facilitate trade.** Price advertises
   opportunity, time regulates it, and volume measures success.
2. **Price moves to find the other side.** It auctions *up* until sellers
   respond, then *down* until buyers respond.
3. **Markets alternate between two states:**
   - **Balance.** Two-sided trade in a range around accepted value.
     Edges: fade the extremes back toward the **Point of Control**
     ([[concept_mean_reversion]]).
   - **Imbalance.** One-sided, directional search for new value. Edges:
     join the move and trade continuation ([[concept_breakout_trading]],
     [[concept_trend_following]]).
4. **Acceptance vs rejection.** Time and volume at a new price mean
   acceptance (value migrates). A fast excursion with little volume means
   rejection (excess).

## Key structures

- **Value Area** (~70% of volume or TPOs), **POC**, **VAH/VAL**, **single
  prints**, **poor highs/lows** (unfinished auctions that tend to be
  revisited), **initial balance** (first hour range), and day types
  (normal, trend, double-distribution, neutral).

## Chart Fanatics lineage

AMT is the most-featured framework among the channel's futures guests:
- **Fabio Valentini** reads balance vs imbalance, then applies *Direction →
  Location → Aggression*, with a trend model and a POC mean-reversion model
  (`strategy_fabio_valentini_amt_order_flow`).
- **Andrea Cimitan**, **Rajan Dhall** (auction theory), and **Forrest Knight**
  (volume-profile edges) all build on the same axioms.

See [[concept_volume_profile]] for the volume-based implementation.
