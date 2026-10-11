---
id: strategy_trader_mayne_structure_ote
type: strategy
title: "Trader Mayne — Structure + OTE: HTF Break, POI Pullback & LTF Breaker Entry (forex/futures/crypto, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Structure + OTE Playbook, Structure OTE, Trader Mayne strategy, Structure + OTE Swing Playbook]
taught_by: [person_trader_mayne]
featured_in: [channel_chart_fanatics]
uses: [concept_market_structure, concept_order_blocks_breakers, concept_fair_value_gap, concept_premium_discount_ote, concept_liquidity, concept_liquidity_sweep_reversal, concept_multi_timeframe_analysis, concept_trend_following, concept_risk_reward_r_multiples, concept_position_sizing]
derived_from: [concept_smart_money_concepts]
related: [strategy_marci_silfrain_measured_move, strategy_nbb_trader_po3_ote_adr]
sources:
  - {title: "Chart Fanatics — Structure + OTE Playbook", url: "https://www.chartfanatics.com/strategies/structure-ote", tier: T2}
  - {title: "TradeZella — Structure + OTE", url: "https://www.tradezella.com/strategies/structure-ote", tier: T3}
status: verified-t2
---

# Trader Mayne — Structure + OTE: HTF Break, POI Pullback & LTF Breaker Entry (forex/futures/crypto, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/structure-ote. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Trader Mayne teaches this top-down swing framework for crypto,
forex and futures. The page notes he also has a seven-lesson crypto
masterclass on Chart Academy.

## Built for

- **Instruments:** forex, futures and crypto. The pros list adds
  commodities. Both worked examples are crypto (Bitcoin and Solana).
- **Style:** swing trading.
- **Timeframes:** two timeframes. **HTF** (weekly, daily, H12 or H4) for
  trend, bias and range. **LTF** (H1, M15 or M5) for the entry. Suggested
  pairs: **Daily → H1** and **H4 → M15**. The examples use 1D → 30m and
  Weekly → H12.
- **Session:** not specified. The page says the method scales across
  markets and timeframes.

## Core idea

Price moves in swings. After a clean higher-timeframe break of structure,
price often pulls back into the zone that caused the break, the **point of
interest (POI)**. That is where the next higher low (uptrend) or lower high
(downtrend) is expected to form. Mark the POI and the premium/discount
split of the new range. When price returns to the POI, drop to the lower
timeframe and wait for a **breaker setup**: engineered liquidity, a stop
run, then a structure break the other way. Enter on the breaker, put the
stop beyond the swept extreme, and target the next higher-timeframe
external liquidity. Every condition must be present for the setup to be
valid.

## Rules

1. **Pick the timeframe pair:** an HTF from weekly, daily, H12 or H4, and
   an LTF from H1, M15 or M5.
2. **Define the HTF trend.** Use swing structure, and require a **clear
   market structure break (MSB)** that sets up a new trading range.
3. **Mark the HTF range.** In an uptrend, from the last significant swing
   low to the new swing high. In a downtrend, from swing high to swing low.
   Draw the **50% line**: buy only in the discount (lower half) of an
   uptrend, and sell only in the premium (upper half) of a downtrend.
4. **Mark the POI on the HTF.** This is the zone that caused the break: an
   **order block** (in the examples, the last opposite-colour candle before
   the breaking move), or a **breaker block** or **fair value gap**.
5. **Wait for the pullback into the POI,** ideally inside the correct half
   of the range.
6. **LTF breaker setup inside the POI.** All three are needed:
   - engineered liquidity: a swing low (for longs) or swing high (for
     shorts) forming inside the zone;
   - a stop run that sweeps that liquidity;
   - a market structure break in the opposite direction.
7. **Entry:** on the breaker block after the LTF MSB. In both examples,
   entry came on the retest.
8. **Stop:** below the swept low (longs) or above the swept high (shorts).
9. **Target:** the next **HTF external liquidity**: the prior swing high
   on a long, the prior swing low on a short.
10. **R:R filter:** take the setup only if it offers **at least 2:1**.
11. **Size:** adjust dynamically with confidence and confluence.

## Risk management

- **Minimum reward-to-risk:** 2:1. Setups below that are skipped.
- **Invalidation:** beyond the low or high that was swept on the LTF.
- **Sizing:** varies with confidence and confluence. No base risk is
  given.
- **Risk per trade ($ or %):** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.
- **Trade management** (break-even, partials, trailing): Not specified in
  the playbook.

## What the playbook leaves unspecified

- What makes a market structure break "clean" (a body close or a wick, and
  how far beyond the swing).
- Which "last significant" swing anchors the range when several qualify.
- How to choose between an order block, breaker or FVG when more than one
  POI sits in the pullback path.
- Despite the name, **no OTE Fibonacci levels** (such as 0.62–0.79) are
  given. The only location filter is the 50% premium/discount split.
- How much engineered liquidity is enough, and how the LTF MSB is
  measured.
- Any management after entry: break-even, partials or trailing.
- How size changes with confluence, and from what base risk.
- What to do if price runs through the POI without an LTF setup.
- Trade frequency and holding period.

## Evidence & claims

- **Bitcoin short (1D HTF, 30m LTF):** bearish MSB, entry in a bearish
  order block in premium after a 30m swing-high sweep, stop above the swept
  high. The page says it reached the target (the next HTF lower low) with
  a large bearish FVG on the way. Self-reported (T4). No R figure is given.
- **Solana long (weekly HTF, H12 LTF):** bullish MSB, entry in a bullish
  order block in discount after several H12 lows built up and the last one
  was swept. The page says price rallied back to its all-time high, the
  target. Self-reported (T4). No R figure is given.
- The page reports **no win rate or P&L**. The 2:1 minimum is a filter,
  not a result; by simple arithmetic (not on the page), the break-even win
  rate at 2:1 is about 33%. No expectancy check is possible.
- The earlier note's TradeZella source (T3) is kept. The earlier note
  recorded no independent test or result from it.
- The page's own cons: entries need discretion around breakers and
  confirmation, the method needs backtesting and live practice, and
  traders must adapt it to their own style.

## Concepts & lineage

- HTF swing structure, MSB and the new range →
  [[concept_market_structure]]
- Trading pullbacks in the direction of the HTF trend →
  [[concept_trend_following]]
- 50% premium/discount split of the range →
  [[concept_premium_discount_ote]]
- Order blocks and breaker blocks as POIs; the LTF breaker entry →
  [[concept_order_blocks_breakers]]
- FVG as an alternative POI → [[concept_fair_value_gap]]
- Engineered liquidity inside the POI and HTF external liquidity as the
  target → [[concept_liquidity]]
- Stop run, then a structure break the other way →
  [[concept_liquidity_sweep_reversal]]
- HTF and LTF pairing → [[concept_multi_timeframe_analysis]]
- Minimum 2:1 → [[concept_risk_reward_r_multiples]]
- Size scaled by confidence and confluence → [[concept_position_sizing]]
- Lineage: smart-money concepts (the page refers to "smart money"; the
  ICT-style label is our attribution) → [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **Status:** upgraded from `synthesized` to `verified-t2` against the
  Chart Fanatics page text.
- **Confirmed:** the earlier workflow. That means a clean HTF structure
  break, a POI that is an order block or breaker, a pullback into it, an
  LTF breaker setup (a failed move that sweeps liquidity and reclaims
  structure), and a stop beyond the sweep.
- **Corrected, location filter:** the earlier note said the pullback should
  ideally land "inside the OTE band". The playbook gives no OTE Fibonacci
  levels. The location rule is the **50% midpoint** of the HTF range:
  discount for longs, premium for shorts.
- **Corrected, target:** the earlier note said only "target in the HTF
  trend direction". The playbook names the **next HTF external liquidity**,
  the previous swing high or low.
- **Expanded, timeframes:** the earlier note said HTF daily or weekly. The
  playbook allows weekly, daily, H12 or H4 for HTF and H1, M15 or M5 for
  LTF, suggesting Daily → H1 and H4 → M15 pairs.
- **Added:** FVG as a third POI type; the 50% range line; a minimum 2:1
  R:R; sizing by confidence and confluence; the rule that every condition
  must be met; and the Bitcoin and Solana examples.
- **Added `uses`:** FVG, sweep reversal, R-multiples and position sizing.
  Added NBB Trader's PO3/OTE note to `related` for its breaker and OTE
  mechanics.
