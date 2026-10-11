---
id: strategy_fredy_sarmiento_options_flow
type: strategy
title: "Fredy Sarmiento — Institutional Options Flow: Gamma Wall Reversal (index futures/options, day trading/scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [Institutional Options Flow Strategy, gamma wall reversal, options flow gamma reversal, Fredy Sarmiento strategy]
taught_by: [person_fredy_sarmiento]
featured_in: [channel_chart_fanatics]
uses: [concept_options_greeks, concept_volatility, concept_market_microstructure, concept_order_flow, concept_support_resistance, concept_trading_sessions_killzones, concept_scalping, concept_risk_reward_r_multiples, concept_trade_management, concept_position_sizing, concept_trading_psychology]
derived_from: [concept_options_greeks, concept_market_microstructure]
related: [strategy_carmine_rosato_orderflow_masterclass, strategy_jay_awtani_market_dna]
sources:
  - {title: "Chart Fanatics — Institutional Options Flow Strategy", url: "https://www.chartfanatics.com/strategies/institutional-options-flow-gamma-reversal-strategy", tier: T2}
status: verified-t2
---

# Fredy Sarmiento — Institutional Options Flow: Gamma Wall Reversal (index futures/options, day trading/scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/institutional-options-flow-gamma-reversal-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Fredy Sarmiento with this framework. He
reads index options positioning to find levels for trading index futures.
The page gives no biography or track record.

## Built for

- **Instruments:** the page lists index futures and index options; the
  execution examples are futures trades that use index options data as the
  map. The stop examples are on **NQ**. The page stresses that the trader does not
  need to trade options; options data is information for the futures trade.
- **Style:** day trading and scalping.
- **Timeframes:** intraday. No chart timeframe is named.
- **Session:** roughly the **first two hours of the US session**, when
  participation, liquidity and volatility are greater than in quieter parts
  of the day and same-day (0DTE) positioning is actively changing.
- **Frequency:** about **one or two quality opportunities a day**.

## Core idea

Large options positions leave dealers with exposure that they hedge in
futures. As price moves, delta changes (that change is gamma), so the hedge
must be adjusted, and that forced buying and selling can make certain
strikes act as barriers, magnets or accelerators. The trader turns options
positioning (gamma walls, open interest, convexity, with skew as context)
into a map of levels before the session. Then they wait for futures to
reach a level, read how price arrives, and trade the confirmed reaction
toward the next level. In short, the options level says where to look,
and price behaviour at that level decides whether there is a trade.

## Rules

1. **Check the calendar first.** Options expiration, triple witching, VIX
   expiration and large institutional roll or hedging periods can change
   how levels behave. A valid level on one of those days is not
   automatically tradeable.
2. **Build the institutional map before the session.** Mark the levels
   where options positioning is concentrated:
   - **Model 1, gamma:** the maximum-gamma area, the call wall and the put
     wall, with particular weight on 0DTE positioning.
   - **Model 2, open interest:** the largest concentrations of open
     interest over roughly a **90-day lookback**.
   - **Model 3, convexity:** areas of positive and negative convexity. The
     preferred path runs from one favourable positive-convexity area toward
     the next.
   - **Volatility surface and skew:** use them to see where volatility
     positioning is unusually concentrated. Skew is context only, never a
     standalone signal.
   - Do not read a big call or put print as directional sentiment. It may
     be a hedge, spread, volatility trade or part of a larger book.
3. **Wait for a level.** No trade while price sits between meaningful
   levels. If price never reaches one, there may be no trade that day.
4. **Read the approach speed.**
   - *Slow, controlled approach:* look for a direct rejection at the level.
   - *Fast, violent approach:* do not stand in front of it. Let price
     overshoot, then trade the **reclaim**: back above a lower level for a
     long, or back below an upper level for a short.
5. **Confirm the reaction.** Look for price rejecting or reclaiming the
   level, ideally with large futures orders appearing at that same level.
   Options positioning gives location; futures order flow gives
   confirmation.
6. **Enter near the level.** Do not chase once the reaction has travelled.
   A late entry widens the stop and shrinks the reward.
7. **Stop beyond the invalidation area,** meaning where the reaction thesis
   is clearly wrong. The NQ examples use roughly **30 to 50 ticks**
   (our conversion, not on the page: about 7.5 to 12.5 index points at
   NQ's 0.25 tick), depending on setup
   and conditions. The page says the principle matters more than the
   number.
8. **Target the next options-derived level** (the next gamma, OI or
   convexity area). With several contracts, take a partial as the first
   reaction develops, reduce risk once the trade moves favourably, and hold
   the rest for the larger target.
9. **Accept a failed level.** If price breaks a wall with strength and
   holds beyond it, stop fading it. Reassess which level has become
   dominant.
10. **Keep it selective.** Do not trade just because the market is open.

## Risk management

- **Per-trade risk:** defined by the structural stop beyond the level (the
  30 to 50 tick NQ examples). A fixed dollar or % amount is not specified in
  the playbook.
- **Sizing:** contract count must fit the account and a predefined risk.
  Extra contracts are for scaling out, not for adding risk. The aim is to
  control the dollar loss if the level fails.
- **Daily limit:** no number is given. The page says to recognise when a
  loss is affecting your decisions and to stop before one controlled loss
  turns into a bigger one. It names chasing, overtrading, revenge trading,
  sizing up after a loss and ignoring invalidation as the risks.
- **Weekly limit:** not specified in the playbook.
- **No-trade conditions:** OPEX, triple witching, VIX expiry, large
  roll or hedging periods, and price sitting between levels.

## What the playbook leaves unspecified

- Where the gamma, open-interest, volatility-surface and convexity data
  comes from, and how dealer positioning (its sign and size) is estimated.
- How concentrated positioning must be before a strike counts as a level.
- An objective test for a "slow" versus a "fast" approach, and what counts
  as a reclaim (a close back through, a time limit, a retest).
- What size of futures order counts as confirmation, and on what tool.
- Exact session times. The page says only the first two hours or so of the
  US session.
- How the convexity model turns into concrete entries. The page describes
  it mostly in concept.
- How much to scale out at the first partial, and when to move the stop.
- How to handle the options-expiry days, beyond treating them with
  caution.
- Any win rate, R:R figure or sample of trades.

## Evidence & claims

- The page reports **no win rate, R:R figure, P&L or payout**.
- The claim of about one or two quality opportunities a day is
  self-reported (T4).
- The 30 to 50 tick NQ stops are a risk parameter from the examples, not a
  result.
- The edge is described qualitatively, as a small invalidation distance
  against a large distance to the next level. No numbers support it, so no
  expectancy check is possible.

## Concepts & lineage

- Delta, gamma and 0DTE sensitivity driving dealer hedge adjustments →
  [[concept_options_greeks]]
- Dealer hedging as the mechanism that moves futures →
  [[concept_market_microstructure]]
- Volatility surface, skew, buying versus selling volatility →
  [[concept_volatility]]
- Options-derived walls and OI concentrations as reaction levels →
  [[concept_support_resistance]]
- Large futures orders at the level as confirmation →
  [[concept_order_flow]]
- Focus on the first two hours of the US session →
  [[concept_trading_sessions_killzones]]
- Tight-stop intraday execution → [[concept_scalping]]
- Small invalidation against a distant next level →
  [[concept_risk_reward_r_multiples]]
- Partials across multiple contracts and risk reduction →
  [[concept_trade_management]], [[concept_position_sizing]]
- Mindfulness after losses as part of risk control →
  [[concept_trading_psychology]]
