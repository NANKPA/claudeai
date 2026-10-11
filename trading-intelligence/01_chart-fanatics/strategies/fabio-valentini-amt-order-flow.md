---
id: strategy_fabio_valentini_amt_order_flow
type: strategy
title: Fabio Valentini — Auction Market Theory + Order-Flow Scalping (NQ)
partition: 01_chart-fanatics
layer: L4
aliases: [Fabio Valentini strategy, auction market strategy, direction location aggression]
teaches: []
taught_by: [person_fabio_valentini]
featured_in: [channel_chart_fanatics, channel_chart_academy]
uses: [concept_auction_market_theory, concept_volume_profile, concept_vwap, concept_order_flow, concept_mean_reversion, concept_trend_following, concept_scalping, concept_trade_execution, concept_market_regimes]
derived_from: [concept_auction_market_theory]
related: [strategy_forrest_knight_volume_profile, strategy_yush_order_flow, strategy_rajan_dhall_auction]
sources:
  - {title: "Chart Fanatics — Auction Market Theory Trading Strategy by Fabio", url: "https://www.chartfanatics.com/strategies/auction-market-strategy", tier: T2}
  - {title: "Chart Academy — Fabio Valentini instructor page", url: "https://www.chartacademy.com/instructors/fabio-valentini", tier: T2}
  - {title: "Trading LIVE with the #1 Scalper in the WORLD (video summary)", url: "https://videohighlight.com/v/tvERE-Beu2U", tier: T3}
  - {title: "PickMyTrade — Fabio Valentini Scalping Strategy: Settings & Rules (NQ)", url: "https://blog.pickmytrade.trade/fabio-valentini-pro-scalper-nasdaq-scalping-strategy/", tier: T3}
status: synthesized
---

# Fabio Valentini — AMT + Order-Flow Scalping

**Trader.** Italian futures scalper, mostly Nasdaq (NQ). Top-3 in the
**Robbins World Cup Trading Championship** futures/scalping division, with
audited returns reported between 218% and 500%+ depending on source and
edition. Co-founder of the order-flow platform **Deep Charts**. Teaches a free
5-lesson order-flow masterclass on Chart Academy (~1.4h).

**Featured in:** the channel's most-viewed video, *"Trading LIVE with the #1
Scalper in the WORLD (EXTREME Accuracy)"* (~3.7M views), with live NY-session
calls; also an episode with fellow order-flow trader **Carmine Rosato**.

## Framework

1. **Read the auction state:** balanced or imbalanced?
   ([[concept_auction_market_theory]])
2. **Direction → Location → Aggression** ([[concept_trade_execution]]):
   - *Direction:* which side controls the auction (value migration,
     initiative activity).
   - *Location:* trade only at meaningful volume-profile locations: value
     edges, POC, LVNs, prior references ([[concept_volume_profile]]).
   - *Aggression:* enter when footprint/delta/CVD show the expected side
     stepping in ([[concept_order_flow]]).

## Two models

| Model | Market state | Logic |
|---|---|---|
| **Trend / continuation** | Out of balance, breaking out and seeking new value | Join aggression after acceptance beyond value ([[concept_trend_following]]) |
| **Mean reversion** | Breakout attempts fail; price returns into balance | Fade back to the **Point of Control** ([[concept_mean_reversion]]) |

## Tools

Volume profile, VWAP, footprint charts, CVD. **No lagging oscillators.**

## Risk

About **0.25% risk per trade** per a third-party guide (not the 1% default
in that guide's script). Treat it as T3.

## Lineage

Steidlmayer's Market Profile (CBOT, 1980s) → Dalton's *Mind Over Markets* →
order-flow tooling (footprint/DOM) → Fabio's Direction-Location-Aggression.

## Open questions (fill from transcript)

- Exact entry trigger on the footprint (imbalance thresholds? absorption
  definition?)
- Stop placement rule and target selection in each model
- Daily loss limit and trade count
