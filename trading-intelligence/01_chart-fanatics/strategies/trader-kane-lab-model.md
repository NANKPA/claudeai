---
id: strategy_trader_kane_lab_model
type: strategy
title: "Trader Kane — 50% Reversal with SMT Divergence & PO3 (NQ/ES futures and crypto, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Trader Kane’s 50% Reversal Strategy", "SMT Divergence + PO3", Lab Model, Trader Kane strategy]
taught_by: [person_trader_kane]
featured_in: [channel_chart_fanatics]
uses: [concept_smt_divergence, concept_amd_power_of_three, concept_premium_discount_ote, concept_fair_value_gap, concept_liquidity_sweep_reversal, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_trade_management, concept_smart_money_concepts]
derived_from: [concept_smart_money_concepts, concept_amd_power_of_three]
related: [strategy_candace_lau_nq_sweep_reversal, strategy_tanja_amd_futures, strategy_nbb_trader_po3_ote_adr]
sources:
  - {title: "Chart Fanatics — Trader Kane’s 50% Reversal Strategy", url: "https://www.chartfanatics.com/strategies/smt-divergence-po3", tier: T2}
  - {title: "PickMyTrade — Trader Kane Strategy: The Lab Model NQ Trading System Explained", url: "https://blog.pickmytrade.trade/trader-kane-strategy-the-lab-model-nq-trading-system-explained/", tier: T3}
  - {title: "Scribd — Trader Kane's Chart Fanatics Strategy", url: "https://es.scribd.com/document/876819803/Chart-Fanatics-Kane-1", tier: T3}
status: verified-t2
---

# Trader Kane — 50% Reversal with SMT Divergence & PO3 (NQ/ES futures and crypto, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/smt-divergence-po3. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Trader Kane is an NQ futures day trader and co-founder of The
Lab education community (per the earlier note, T3). Do not confuse him
with Kane Trading (kanetrading.com), a separate Fibonacci and ABCD site.

## Built for

- **Instruments:** crypto and futures. The SMT read compares **NQ with
  ES**.
- **Style:** scalping and day trading. The aim is consistent "base hits",
  not full trend moves.
- **Timeframes:** Daily, then 4H, then 1H for bias, then an intraday chart
  for entry (the example executes on the **3-minute**).
- **Time window:** manipulation usually comes around **10:00 AM EST**. The
  example moves to breakeven on the **11:00 AM** hourly candle, and trades
  are often finished before midday. The page says the model also works on
  higher timeframes.

## Core idea

Price often returns to the **50% level** of an earlier range before the
broader trend continues. The model frames market behaviour with the **Power of
Three**: accumulation (a range), manipulation (a sweep of a key high or
low) and distribution (delivery back into the 50% area). When Daily, 4H and
1H all line up around a key 50% level, the trader waits for a sweep at the
key time. **SMT divergence** confirms it, with NQ and ES failing to make
the same high or low. A break of an **inversion zone** then gives the
trigger, and the trade targets only the move back to the 50% level.

## Rules

1. **Daily bias.** Mark the previous day's high and low and the swing high
   and low, then find the **50% midpoint** of the large range. That sets
   the bias and the target area.
2. **4H check.** Find the midpoint of recent swings and look for PO3
   structure. Has a recent high or low been swept?
3. **1H alignment.** The 1H should agree with the Daily and 4H and show
   its own PO3, often with a reversal wick around 10:00 AM. SMT usually
   becomes visible on this timeframe.
4. **Wait for manipulation at the key time** (around 10:00 AM EST): a sweep
   above a prior high for a bearish setup, or below a prior low for a
   bullish one.
5. **Confirm with SMT.** One index makes the new extreme and the other does
   not (for example, NQ makes a new high while ES does not). This signals
   the manipulation may be over.
6. **Find the inversion zone.** After the manipulation, look for a reaction
   at an earlier imbalance or inversion zone, meaning old support now
   acting as resistance or the reverse. Wait for price to break down
   through it or reject it.
7. **Entry.** A breakdown candle closes beyond the inversion zone. Then
   either place a **sell stop under the breakdown candle** or a **limit on
   the retest** of the zone (mirror for longs). In the example, the entry
   was a sell stop on the 3-minute chart.
8. **Stop.** Just beyond the **SMT extreme**: above the SMT high for
   shorts, below the SMT low for longs.
9. **Target.** The **50% level** of the impulse or dealing range (the H1
   dealing range in the example). This is the base hit. Do not aim for the
   full move unless momentum is unusually strong.
10. **Manage.** As soon as the trade moves your way and confirms, **move
    the stop to breakeven**. In the example, the trigger was the 11:00 AM
    hourly candle turning bearish. If price climbs back past the
    manipulation candle's high or low, you are probably wrong and should
    be out.

## Risk management

- **Stop:** structural, just beyond the SMT high or low.
- **Breakeven rule:** strict and early. The page admits it causes a **high
  break-even rate**, with many trades closing flat.
- **Exit if wrong:** when price returns past the manipulation candle's
  extreme.
- **Risk per trade (% or $), position size:** not specified in the
  playbook.
- **Daily or weekly limits, maximum number of trades:** not specified in
  the playbook.

## What the playbook leaves unspecified

- Which swing defines the daily "large range" and the "dealing range" whose
  50% is the target.
- How "around 10:00 AM" is bounded: the earliest and latest valid time for
  the manipulation.
- What counts as an inversion zone, for example whether it means an
  inverted FVG specifically or any flipped support or resistance.
- An objective trigger for "confirms" before moving to breakeven, beyond
  the single 11:00 AM candle example.
- Which instrument is traded when NQ and ES diverge (the one that swept, or
  the other), and how the setup carries over to crypto, where no NQ/ES SMT
  pair exists.
- Position sizing, risk per trade and daily loss rules.

## Evidence & claims

- The playbook page makes **no win-rate, R:R, P&L or payout claim**. Its
  pros are qualitative: entries near the high or low of the day, setups
  described as high-probability and high-confluence, quick trades.
  Self-reported (T4).
- **From the earlier note:** his Chart Fanatics episode is billed "$2M+"
  (T4 marketing figure, unverified).
- No expectancy check is possible. The admitted high break-even rate means
  any real test should log breakeven exits as their own outcome.

## Concepts & lineage

- NQ against ES failure to confirm a new extreme →
  [[concept_smt_divergence]]
- Accumulation, manipulation, distribution on 4H and 1H →
  [[concept_amd_power_of_three]]
- The 50% midpoint of the range as target, and premium-zone rejection →
  [[concept_premium_discount_ote]]
- Inversion zone and earlier imbalance as the trigger area →
  [[concept_fair_value_gap]]
- A sweep of a prior high or low, then reversal →
  [[concept_liquidity_sweep_reversal]]
- Daily, 4H and 1H bias with a 3-minute execution →
  [[concept_multi_timeframe_analysis]]
- The 10:00 AM manipulation window and 11:00 AM breakeven check →
  [[concept_trading_sessions_killzones]]
- Early breakeven, base-hit exits → [[concept_trade_management]]
- Lineage: ICT-style smart-money framework → [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **First-person rulebook now exists.** The earlier note said there was no
  public first-person rulebook and that every mechanical version was a T3
  reconstruction. The Chart Fanatics playbook now provides the rules at
  T2.
- **Name.** The page calls the method **"Trader Kane's 50% Reversal
  Strategy"** (URL slug `smt-divergence-po3`) and never says "Lab Model".
  That label comes only from the earlier T3 sources and is kept as an alias.
- **Timing anchor, corrected.** The earlier note made the 10:00 AM ET
  **four-hour candle** the timing anchor (T3). The playbook places the
  manipulation **around 10:00 AM EST**, read on the **1H**, often as a
  wick. The 4H is used for PO3 and swing midpoints, and the 11:00 AM hourly
  candle triggers breakeven. The "10 AM 4H anchor" wording is dropped from
  the title.
- **Instrument scope, corrected.** The earlier note said NQ-only execution
  with ES as the SMT reference (T3). The playbook lists **crypto and
  futures**, uses NQ and ES for SMT, and does not limit execution to NQ.
- **Confirmed:** SMT divergence, inversion zones, premium and discount,
  and aggressive breakeven management. The playbook adds that this
  produces a high break-even rate.
- **Added:** the 50% level as the core target, top-down Daily, 4H and 1H
  PO3 alignment, the entry mechanics (sell stop under the breakdown candle,
  or a limit on the retest), the stop beyond the SMT extreme, and the
  manipulation-candle exit.
- **Added `uses`:** AMD/PO3, liquidity sweep reversal and multi-timeframe
  analysis.
