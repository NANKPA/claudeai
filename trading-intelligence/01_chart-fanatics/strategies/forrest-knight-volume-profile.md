---
id: strategy_forrest_knight_volume_profile
type: strategy
title: "Forrest Knight — Volume Profile Edge-to-Edge Strategy (options/futures, day trading / swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Forrest Knight volume profile strategy, edge-to-edge volume profile, volume edge signal candle, previous day POC retest]
taught_by: [person_forrest_knight]
featured_in: [channel_chart_fanatics]
uses: [concept_volume_profile, concept_auction_market_theory, concept_support_resistance, concept_liquidity, concept_price_action, concept_candlestick_patterns, concept_multi_timeframe_analysis, concept_trade_execution]
derived_from: [concept_auction_market_theory]
related: [strategy_fabio_valentini_amt_order_flow, strategy_yush_order_flow, strategy_carmine_rosato_lvn]
sources:
  - {title: "Chart Fanatics — Volume Profile Trading Strategy By Forrest Knight", url: "https://www.chartfanatics.com/strategies/volume-profile-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists Volume Profile Strategy by Forrest Knight)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "TradeZella — Volume Profile Strategy", url: "https://www.tradezella.com/strategies/volume-profile-strategy", tier: T3}
  - {title: "DamnPropFirms — volume profile strategies (quotes Knight)", url: "https://damnpropfirms.com/trading-guides/volume-profile-strategies-high-probability-trades/", tier: T3}
status: verified-t2
---

# Forrest Knight — Volume Profile Edge-to-Edge Strategy (options/futures, day trading / swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/volume-profile-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Forrest Knight as a volume-profile trader working options and futures on day-trading and swing horizons, and gives no further biography.

## Built for

- **Instruments:** options and futures. The worked example is NQ futures.
  - It needs centralized, reliable volume data.
  - The page says it is **not viable in decentralized markets such as spot forex**.
- **Style:** day trading and swing trading.
- **Timeframes:**
  - Weekly and daily to find long-term value areas, edges and directional bias.
  - **4H and 1H** as the main execution charts for signal candles. Lower timeframes are allowed for entries under the higher-timeframe bias.
  - Keep bias and execution timeframes separate, and filter down to 2–3 main profiles.
- **Tools:** session volume profile and visible-range volume profile.
- **Session / time window:** not specified beyond the overnight and prior-day reference levels.

## Core idea

Volume *at price* shows where participants are positioned. High-value areas (HVAs), where heavy volume traded, are "sticky" and price tends to consolidate there. Price tends to travel quickly through low-value areas (LVAs). The sharp drop-off between the two (a **volume edge** or **shelf**) is where price reacts, stalls or breaks away. The trade is taken at a volume edge that lines up with one of four daily liquidity levels, only after a high-volume signal candle closes rejecting it. The target is the next shelf ("edge-to-edge"), and the middle of low-volume zones is avoided.

## Rules

1. **Set directional bias from higher timeframes.** Example: a weekly close with a high-volume, bottom-wick reversal candle at a volume edge makes the bias long. Then favour long trades on the 4H, 1H or lower timeframes. The weekly candle is not traded itself.
2. **Mark the four daily levels:** overnight high, overnight low, prior-day high and prior-day low. Trapped traders tend to act aggressively at these liquidity zones.
3. **Map volume edges and shelves.** Find the transitions between HVA and LVA on the chosen profiles.
4. **Qualify the setup.** All three must be present:
   - price is touching a volume-profile edge;
   - the edge lines up with ONH, ONL, PDH or PDL;
   - a **high-volume signal candle** with a visible rejection wick **closes in the trade direction**.
5. **Wait for the candle to close.** Don't front-run the signal candle, because its last few minutes can flip it.
6. **Entry:** after the signal candle closes at the volume edge. **Alternative (volatility retest):** if the signal candle has a long wick, expect a 50–80% retrace of the wick before continuation and place a limit order in that zone. Estimate the zone visually, not with Fibonacci tools. The page says this suits NQ and other volatile markets.
7. **Stop:** just beyond the signal candle's wick, or beyond the edge of the high-value node.
8. **Target:** the next shelf (edge-to-edge). Trade through the low-volume zone toward the next high-volume area.
9. **No mid-zone trades.** Low-volume interiors are unpredictable. Wait for price to reach an edge.
10. **Previous-day POC retest (core setup).** After a breakout or trend day, price often returns to the prior day's POC before resuming. Look for a signal candle at that POC and target a new high or low.

## Risk management

- **Stop:** beyond the signal-candle wick or the high-value-node edge.
- **Risk per trade:** Not specified in the playbook.
- **Sizing:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.
- **Built-in filter:** sit out when no valid edge signal appears. Some days produce none, and trading inside chop zones is lower probability.

## What the playbook leaves unspecified

- What counts as a "high-volume" signal candle (relative-volume threshold) and how long the wick must be.
- Profile settings: row size, value-area %, which session or range each profile covers, and how to resolve conflicting nodes.
- Overnight-session hours used for ONH and ONL.
- How bias is set when the weekly chart gives no reversal candle, or when weekly and daily disagree.
- Partial exits, break-even or trailing rules, and what to do if price stalls before the next shelf.
- Options specifics (strike, expiry, greeks) despite options being listed as an instrument.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- **NQ 1H example:** price swept above PDH at the upper shelf edge, then closed back below it on a long-upper-wick, high-volume candle. The short went on at the close with the stop above the wick high, targeting ONL at the lower shelf, which was hit. No prices or P&L given (T4).
- The claim that the method works across asset classes is limited by the page's own caveat that it needs centralized volume data (T4).

## Concepts & lineage

- Volume at price, HVAs and LVAs, volume edges and shelves, POC: [[concept_volume_profile]]
- Price consolidating in high-value areas and moving fast through low-value areas, edge-to-edge rotation: [[concept_auction_market_theory]]
- ONH/ONL/PDH/PDL as trapped-trader liquidity levels: [[concept_liquidity]], [[concept_support_resistance]]
- High-volume rejection-wick signal candle, wait for the close: [[concept_candlestick_patterns]], [[concept_price_action]]
- Weekly or daily bias with 4H or 1H execution: [[concept_multi_timeframe_analysis]]
- Entry on candle close or a 50–80% wick-retrace limit: [[concept_trade_execution]]

## Changes vs. earlier note

- **Confirmed:** location at the edge of a high-volume node on PDH/PDL/ONH/ONL, a wick-rejection signal candle that closes in the trade direction (wait for the close), and edge-to-edge targets through low-volume areas. The earlier note had these from T3 summaries.
- **Clarified:** the earlier note called bias only "a higher-timeframe directional filter". The playbook gives a concrete example: a weekly high-volume bottom-wick reversal candle at a volume edge means long bias.
- **Added:** 4H/1H execution timeframes, the stop rule (beyond the wick or the HVN edge), the 50–80% wick-retrace limit entry, the previous-day POC retest setup, the no-mid-zone rule, and the "2–3 profiles" guidance.
- **Added:** the limitation that it is not viable on spot forex because that market has no centralized volume.
- **Added:** `concept_liquidity` and `concept_candlestick_patterns` to `uses`, and two more related strategies.
