---
id: strategy_carmine_rosato_orderflow_masterclass
type: strategy
title: "Carmine Rosato — Order Flow Masterclass: Absorption & Stop-Run Reclaim (futures, intraday order-flow trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Order Flow Masterclass by Camrine, Carmine order flow, absorption short, stop run and reclaim long]
taught_by: [person_carmine_rosato]
featured_in: [channel_chart_fanatics]
uses: [concept_order_flow, concept_auction_market_theory, concept_market_microstructure, concept_liquidity, concept_liquidity_sweep_reversal, concept_support_resistance, concept_volume_profile]
derived_from: [concept_auction_market_theory, concept_order_flow]
related: [strategy_carmine_rosato_lvn, strategy_yush_order_flow, strategy_fabio_valentini_amt_order_flow, strategy_jay_awtani_market_dna]
sources:
  - {title: "Chart Fanatics — Order Flow Masterclass by Camrine", url: "https://www.chartfanatics.com/strategies/orderflow-trading-masterclass", tier: T2}
status: verified-t2
---

# Carmine Rosato — Order Flow Masterclass: Absorption & Stop-Run Reclaim (futures, intraday order-flow trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/orderflow-trading-masterclass. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Carmine Rosato teaches order flow in free masterclasses on Chart
Academy. Per the page, they cover futures fundamentals, risk management and
scaling, Level 2 walls, and reversal and breakout-retest setups. (The page
title spells his name "Camrine".)

## Built for

- **Instruments:** the page has no Built For block. The masterclass it
  promotes is about futures, and the two case studies quote prices of 5710
  and 5844. The page never names the contract.
- **Style:** intraday order-flow reading with three tools: the DOM, the
  liquidity heatmap and the footprint chart.
- **Timeframe / session:** not stated. The second case study refers to the
  previous day's low and to earlier tests of a level within the same session.

## Core idea

The market is a continuous auction. Resting limit orders supply liquidity
and do not move price; aggressive market orders consume it and do. The page
says price moves because one side is more aggressive, not because there are
"more buyers than sellers". Support and resistance are places where
aggressive orders keep failing to get through passive liquidity. The trader
reads three signals live: **absorption**, **liquidity walls** and **stop
runs**. Delta (and, on paper, the volume profile, which the page only
defines) is the next layer of reading, and a trade is taken only once one
side has visibly taken control.

## Rules

The page teaches concepts plus two worked case studies. It gives no single
rulebook, so the steps below are drawn from those case studies.

1. **Context and location.** Mark levels where liquidity sits: resistance
   with a visible sell wall, support with a visible bid wall, and obvious
   prior highs and lows (such as the previous day's low) where stops pile
   up. The page closes by naming three steps, Context, Location and
   Confirmation, but does not define them.
2. **Read the signals at the level:**
   - *Absorption:* heavy aggressive volume and a strong delta in one
     direction, but price barely moves. The passive side is soaking up the
     pressure.
   - *Liquidity wall:* a large cluster of resting orders on the book or
     heatmap that price repeatedly hits and cannot clear.
   - *Stop run:* a sharp push through an obvious high or low that triggers
     stops, after which the market often snaps back.
3. **Confirm with delta.** Look at how price responds to delta, not just the
   number. If delta is strongly positive and price does not rise, buyers are
   being absorbed. If delta is strongly negative and price does not fall,
   sellers are being absorbed.
4. **Setup A, absorption short at resistance.** Price rallies into a sell
   wall (about 111 contracts at 5710 in the example). Buyers keep lifting
   the offer in 70 to 80 lot clips and delta prints positive, but price
   stalls. Go short when buying fades, the bids below thin out and sellers
   start hitting aggressively. The page does not give a stop or a target for
   this case.
5. **Setup B, stop run and reclaim long.** Price flushes below the previous
   day's low on heavy negative delta, then stops going lower (absorption).
   The footprint shows aggressive selling with no follow-through, and the
   heatmap shows liquidity building beneath price. **Enter long when price
   reclaims the level** (about 5844 in the example). That level had already
   held as support four or five times earlier in the session.
6. **Stop.** In Setup B, the stop goes just below the low of the flush.
7. **Exit.** Not specified. Both case studies only describe price
   moving away from the level after the shift in control.

## Risk management

- **Risk per trade:** not specified in the playbook.
- **Stop:** structural. In the reclaim long it sits just below the flush
  low. The absorption short has no stop rule.
- **Daily or weekly limits, sizing:** not specified in the playbook. Risk
  management and scaling are listed as masterclass topics but not taught on
  this page.

## What the playbook leaves unspecified

- Which contract, session and time window the setups are meant for.
- How large a wall must be, or how many absorbed lots or how much delta,
  before it counts. The 111-lot wall and 70 to 80 lot clips describe one
  example and are not thresholds.
- Stops and targets for the absorption short, and targets for the reclaim
  long.
- What "Context, Location, and Confirmation" means as a checklist.
- How the volume profile is used. The page defines it in a single sentence.
- Trade management (partials, trailing, breakeven) and any risk limits.
- How to deal with spoofed or pulled liquidity on the heatmap. The page
  notes that resting orders can be withdrawn but gives no rule for it.

## Evidence & claims

- The page contains **no win-rate, R:R, P&L or payout claims**. The only
  numbers are example prices and lot sizes from the two case studies.
- With no stated win rate or reward-to-risk, no expectancy check is
  possible. The setups would need to be journaled or backtested from
  scratch.

## Concepts & lineage

- The market as a two-sided auction of passive limit orders against
  aggressive market orders → [[concept_auction_market_theory]],
  [[concept_market_microstructure]]
- Absorption, delta, DOM, heatmap and footprint reading →
  [[concept_order_flow]]
- Liquidity walls and stop pools above highs and below lows →
  [[concept_liquidity]]
- Stop run followed by reclaim of the swept level →
  [[concept_liquidity_sweep_reversal]]
- Support and resistance explained as passive liquidity outlasting
  aggression → [[concept_support_resistance]]
- Where value was accepted or rejected → [[concept_volume_profile]]
