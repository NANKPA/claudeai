---
id: concept_trade_execution
type: concept
title: Trade Execution (triggers, order types, confirmation)
partition: 07_concepts
layer: L5
aliases: [entry trigger, confirmation entry, limit entry, market entry, stop entry, order types, direction location aggression]
related: [concept_market_microstructure, concept_trade_management, concept_optimal_execution_market_impact, concept_multi_timeframe_analysis, concept_order_flow, concept_trading_plan]
status: synthesized
---

# Trade Execution

**Analysis tells you *where*; execution decides *whether you get filled, at
what price, and with what stop*.**

## Fabio Valentini's three-step model (T2/T3)

1. **Direction:** is the market balanced or imbalanced? Which side is in
   control ([[concept_auction_market_theory]])?
2. **Location:** only act at meaningful levels: value-area edges, POC, LVNs,
   prior-day references ([[concept_volume_profile]]).
3. **Aggression:** enter when order flow shows the expected side becoming
   aggressive (footprint, delta, CVD) ([[concept_order_flow]]).

This is the cleanest general-purpose execution checklist in the knowledge
base: **context → level → trigger**.

## Entry styles

| Style | Order | Pros | Cons |
|---|---|---|---|
| **Anticipatory limit** at the zone | Limit | Best price, tight stop | Fills on trades that run through (adverse selection) |
| **Confirmation** (signal candle close, MSS, breaker) | Stop/market after confirmation | Higher win rate | Worse price, wider stop |
| **Breakout stop-entry** | Buy-stop above level | Catches momentum | Slippage, fakeouts |

Forrest Knight: wait for the **signal candle to close** with a rejecting
wick; don't front-run. Yush: entries are *early*, so size smaller and keep
stops tight.

## Order-type mechanics

Market (certain fill, uncertain price) · Limit (certain price, uncertain
fill) · Stop (becomes market when triggered, so it slips in gaps) ·
Stop-limit (may not fill) · OCO/brackets (automate stop and target).

## Execution costs to log

Spread, commission, slippage vs intended price, and missed fills. These are
the silent killers of scalping edges ([[concept_scalping]]).
