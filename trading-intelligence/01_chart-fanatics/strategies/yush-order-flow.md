---
id: strategy_yush_order_flow
type: strategy
title: "Trader Yush — Trading Trapped Buyers & Sellers with Order Flow (NQ/ES futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Yush strategy, trapped traders order flow, Yush AOI model, range and trend order-flow models]
taught_by: [person_trader_yush]
featured_in: [channel_chart_fanatics]
uses: [concept_order_flow, concept_volume_profile, concept_auction_market_theory, concept_support_resistance, concept_market_regimes, concept_mean_reversion, concept_trend_following, concept_scalping, concept_trade_management, concept_position_sizing, concept_trade_execution]
derived_from: [concept_order_flow, concept_auction_market_theory]
related: [strategy_fabio_valentini_amt_order_flow, strategy_andrea_cimitan_amt, strategy_carmine_rosato_lvn]
sources:
  - {title: "Chart Fanatics — Yush’s Strategy: Trading Trapped Buyers & Sellers with Order Flow", url: "https://www.chartfanatics.com/strategies/order-flow-strategy", tier: T2}
  - {title: "TradeZella — Order Flow Strategy", url: "https://www.tradezella.com/strategies/order-flow-strategy", tier: T3}
status: verified-t2
---

# Trader Yush — Trading Trapped Buyers & Sellers with Order Flow (NQ/ES futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/order-flow-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Trader Yush as a futures day trader who builds levels from market-generated references, volume profile, big trades and delta, then waits for order-flow confirmation before executing. The page gives no other biography.

## Built for

- **Instruments:** futures. The header says NQ; ES appears in the big-trade thresholds and in one worked example.
- **Style:** day trading with a "scalping mindset": quick execution, short holds, typically 2–3 trades per day.
- **Timeframes:** no chart timeframe is given. Execution is read from order-flow tools (DOM, delta, big trades) against session-based levels.
- **Session / time window:** the US session, implied by the references (overnight high and low, previous-day levels, a 32-second opening range). No explicit hours are given.

## Core idea

Every trade starts from an Area of Interest (AOI). An AOI is built from at least two of four objective tools: market-generated levels, volume profile, big trades and delta profile. When price returns to the AOI, the trader waits for order flow to show that one side tried to push and failed, through absorption or trapped traders, and then trades the other way. The market state picks the model. A balanced (range) market uses fades at the value edges. An imbalanced (trend) market uses pullbacks into low-volume nodes. Both models react to what is happening rather than predicting it.

## Rules

1. **Build AOIs.**
   - Market-generated levels: previous-day high and low, overnight high and low, previous-day close, and the opening range (32-second ORB).
   - Volume profile: the value area (where about 70% of volume traded) and low-volume nodes (LVNs).
   - Big trades: NQ 75+ lots and ES 200+ lots (the ES figure is "adjusted based on liquidity").
   - Delta profile: positive delta means buyers lifting the ask; negative delta means sellers hitting the bid.
   - A valid AOI needs **at least 2** of these. **3–4** makes an A+ setup.
2. **Classify the market state.**
   - *Balanced/range:* price inside value, volume concentrated in the middle, breakouts that lack follow-through, repeated reversals at similar levels.
   - *Imbalanced/trend:* strong directional movement, value shifting in one direction, LVNs present, shallow pullbacks.
3. **Wait for price to return to the AOI.** No return means no trade. Never enter directly into strong momentum. Wait for a slowdown, a reaction and confirmation.

**Model 1: Range (balanced market)**

4. **Trade only the edges:** value area high as resistance and value area low as support. The middle of the range is a no-trade zone.
5. **Aggressive entry** at the edge on early rejection: absorption (heavy activity, no price movement), strong delta without continuation, or big trades that fail to push price further. Use smaller size and a tight stop.
6. **Confirmation entry.** Price breaks out of the range, breakout traders chase, then price comes back inside and shows rejection. Enter the fade once price is back in the range (for example, short after a failed break above the top).
7. **Stop:** just outside the range edge.
8. **Targets:** T1 at the range midpoint, T2 at the opposite side of value. Move the stop to break-even as soon as T1 is reached.

**Model 2: Trend (imbalanced market)**

9. **Setup sequence:** price moves aggressively one way and leaves an LVN. Price then pulls back into the LVN, the opposite side turns aggressive, and price fails to continue against the trend.
10. **Aggressive entry** inside the pullback zone when opposing aggression appears without follow-through, or absorption is visible. Use a tight stop. **Confirmation entry:** wait for a reclaim of structure and a higher low (bullish) or lower high (bearish) with a shift back in the trend direction. This gives a slightly worse price.
11. **Management:** take partial profits at previous highs or lows, hold the rest for continuation, and trail on structure. Move to break-even after the partial. Add only to winning positions.
12. **Execution discipline:** don't anticipate; react to confirmation. Limit yourself to high-quality setups, typically 2–3 trades per day.

## Risk management

- **Risk per trade:** Not specified in the playbook as a $ or % figure. Define risk before every entry.
- **Stops:**
  - Range model: just outside the range edge.
  - Trend model: tight, with quick invalidation.
  - Trend example (instrument not stated): stop just above the overnight low.
- **Sizing:** smaller size on aggressive entries. Scale into strength, not weakness, and never add to losers.
- **Protecting profit:** never let a winner turn into a loss. Break-even after T1 or the first partial. A break-even stop-out is acceptable.
- **Losses:** accept them quickly.
- **Daily / weekly limits:** Not specified in the playbook beyond the typical 2–3 trades per day.

## What the playbook leaves unspecified

- Numeric thresholds for "strong" delta and for absorption, and how the ES big-trade filter is "adjusted based on liquidity" (and whether the NQ one is too).
- Which volume profile to use (prior day, developing, composite) and the value-area settings.
- An objective rule for calling the market balanced or imbalanced in real time.
- A chart timeframe, stop buffers in ticks, partial sizes, and the trailing method.
- Position size per trade, a daily loss limit, time-of-day restrictions and news handling.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- **Trend example (Model 2; the page doesn't name the instrument):** shortly after the open, a liquidation-driven break below the overnight low left an LVN and a print of about 300 lots near the level. The pullback into the zone showed continued negative delta and more big sell prints. The short was entered just below the level with the stop above the overnight low. Described qualitatively, with no P&L (T4).
- **ES range example:** positive delta built to about 800, 1,800 and 1,900+ at the range highs without price progress, which the page reads as absorption. A sweep of the overnight high then failed. The short was entered around the level, targeting the range midpoint and then the range low. No P&L given (T4).
- The earlier note's third-party summary (TradeZella, T3) reported the same big-trade thresholds and the two-confirmation minimum, and the playbook agrees with it.

## Concepts & lineage

- Delta, big trades, absorption and trapped traders as the confirmation layer: [[concept_order_flow]]
- Value area (about 70% of volume), VAH and VAL edges, LVNs as imbalance zones: [[concept_volume_profile]], [[concept_auction_market_theory]]
- Market-generated reference levels (PDH/PDL, ONH/ONL, prior close, ORB) as AOIs: [[concept_support_resistance]]
- Separate models for balanced vs imbalanced conditions: [[concept_market_regimes]]
- Range model fading back to the midpoint and the opposite side of value: [[concept_mean_reversion]]
- Trend model joining pullbacks into LVNs and scaling into strength: [[concept_trend_following]]
- Two-target exits, break-even after T1, trailing on structure: [[concept_trade_management]]
- Smaller size on aggressive entries, adding only to winners: [[concept_position_sizing]]
- Aggressive vs confirmation entries, and no entries into momentum: [[concept_trade_execution]], [[concept_scalping]]

## Changes vs. earlier note

- **Confirmed:** the big-trade thresholds (about 75+ lots on NQ and about 200+ on ES), the minimum of 2 confirmations per zone, and the absorption, delta and trapped-trader logic. The earlier note had these from a third-party summary (T3).
- **Corrected:** the earlier note said entries are early, so traders should size smaller and keep stops tight (T3). The playbook says that applies only to the *aggressive* entry variant. Each model also has a *confirmation* entry.
- **Corrected:** the earlier title said "ES/NQ scalping". The playbook labels it NQ futures **day trading** with a scalping mindset.
- **Added:** the four AOI tools, including the 32-second ORB and the 70% value area, and the A+ grade for 3–4 confirmations.
- **Added:** the two models (range edges vs trend pullbacks into LVNs), the targets (range midpoint, then the opposite side of value), break-even rules, add-to-winners-only, and the guideline of typically 2–3 trades per day.
- The Chart Fanatics (T2) source is kept as the primary source, and the TradeZella (T3) source is kept as secondary.
