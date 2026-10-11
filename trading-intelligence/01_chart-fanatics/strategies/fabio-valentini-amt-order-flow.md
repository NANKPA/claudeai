---
id: strategy_fabio_valentini_amt_order_flow
type: strategy
title: "Fabio Valentini — Auction Market Theory + Order-Flow Scalping (NQ/ES futures, scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [Fabio Valentini strategy, auction market strategy, direction location aggression, market state location aggression]
taught_by: [person_fabio_valentini]
featured_in: [channel_chart_fanatics, channel_chart_academy]
uses: [concept_auction_market_theory, concept_volume_profile, concept_order_flow, concept_market_regimes, concept_trend_following, concept_mean_reversion, concept_scalping, concept_trading_sessions_killzones, concept_position_sizing, concept_risk_reward_r_multiples, concept_trade_execution]
derived_from: [concept_auction_market_theory]
related: [strategy_andrea_cimitan_amt, strategy_carmine_rosato_lvn, strategy_yush_order_flow, strategy_forrest_knight_volume_profile]
sources:
  - {title: "Chart Fanatics — Auction Market Theory Trading Strategy by Fabio", url: "https://www.chartfanatics.com/strategies/auction-market-strategy", tier: T2}
  - {title: "Chart Academy — Fabio Valentini instructor page", url: "https://www.chartacademy.com/instructors/fabio-valentini", tier: T2}
  - {title: "Trading LIVE with the #1 Scalper in the WORLD (video summary)", url: "https://videohighlight.com/v/tvERE-Beu2U", tier: T3}
  - {title: "PickMyTrade — Fabio Valentini Scalping Strategy: Settings & Rules (NQ)", url: "https://blog.pickmytrade.trade/fabio-valentini-pro-scalper-nasdaq-scalping-strategy/", tier: T3}
status: verified-t2
---

# Fabio Valentini — Auction Market Theory + Order-Flow Scalping (NQ/ES futures, scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/auction-market-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook names him only as "Fabio" and says he teaches a free five-lesson order-flow masterclass on Chart Academy with live Nasdaq examples. The rest of this biography comes from the earlier search-based note (third-party, T3; not in the playbook): Fabio Valentini is an Italian futures scalper, mostly on Nasdaq (NQ), who co-founded the order-flow platform Deep Charts. He is featured in the channel's most-viewed video, *"Trading LIVE with the #1 Scalper in the WORLD (EXTREME Accuracy)"*, and in an episode with order-flow trader Carmine Rosato (T3).

## Built for

- **Instruments:** futures. The trend model names NASDAQ and ES.
- **Style:** scalping (intraday).
- **Timeframes:** none fixed. The volume profile is drawn on specific legs (the impulse or the reclaim), with the previous day's profile as the balance reference. Execution uses footprint charts, big-print bubbles and CVD.
- **Sessions:**
  - The trend model works best in New York. Avoid the London open because of fake breakouts.
  - The mean-reversion model works best in London or in compressed summer conditions.

## Core idea

The market is an auction that alternates between **balance** (rotation around fair value) and **imbalance** (one side pushing price to find new value). Most traders lose by trading breakouts inside balance. The page claims the market stays stuck there about 70% of the time. A trade needs three things in order: **market state** (balanced or not), **location** (LVNs and POC from the volume profile), and **aggression** (order-flow confirmation at that location). If any one is missing, stay flat. There are two complementary models: trend continuation toward new balance, and mean reversion back into balance after a failed breakout.

## Rules

**Trend model (out of balance, seeking new balance)**

1. **Session:** New York. Avoid the London open.
2. **Market state:** confirm the market is out of balance, with displacement and momentum away from prior value. If price is just rotating, skip.
3. **Location:** apply a volume profile to the impulse leg that broke structure and mark the LVNs inside it. Set alerts just before the LVNs. Don't rest blind limit orders.
4. **Trigger:** when price returns into an LVN, require aggression in the trend direction: big buy bubbles or footprint imbalance for longs, big sell bubbles or imbalance for shorts. No aggression means no trade.
5. **Stop:** just beyond the aggressive print, plus a 1–2 tick buffer before the obvious swing high or low. (The worked long example put the stop just below the LVN.)
6. **Break-even:** move to break-even early if CVD shows strong pressure.
7. **Target:** the previous balance's POC. Close the full position there. Trail beyond it only on rare strong trend days. The page's reason is that price reverses from balance about 70% of the time. In the worked example, the trade was closed early when sellers showed aggression against it.

**Mean-reversion model (failed breakout, back into balance)**

8. **Session:** London, or compressed summer conditions.
9. **Market state:** the market is in balance or consolidation. The previous day's profile can serve as the balance reference. Watch for price to push out of balance and fail.
10. **Location:** don't take the first move back. Wait for (a) a clear reclaim inside balance and (b) a pullback into the reclaim leg. Apply a volume profile to the reclaim leg and mark its LVNs.
11. **Trigger:** on the pullback into the LVN, require aggression in the snap-back direction: big buy prints for longs after a reclaim, big sell prints for shorts after a failed upside break.
12. **Stop:** just beyond the aggressive print with a 1–2 tick buffer before obvious highs or lows. Never widen it. If you're wrong, you should be wrong immediately.
13. **Target:** the balance POC. Exit the full position there. Don't reach for the other side of the range unless conditions are exceptional.

## Risk management

- **Risk per trade:** 0.25%–0.5% of the account (both models).
- **Stops:** just beyond the aggressive print plus a 1–2 tick buffer. Never widen. Move to break-even early on strong CVD (trend model).
- **Exits:** full exit at the POC target (no scaling out in the playbook rules).
- **Expected drawdown pattern:** several small stop-outs in a row are common, and the strike rate drops on choppy or compressed days.
- **Daily / weekly limits:** Not specified in the playbook.
- **Maximum trades per session:** Not specified in the playbook.

## What the playbook leaves unspecified

- Size thresholds for "big" bubbles or prints, footprint imbalance ratios, and what counts as "strong" CVD pressure.
- An objective test for balanced vs out of balance, beyond displacement or rotation.
- Which LVN to use when a leg has several, and how far before the LVN to set alerts.
- Exact session hours, and how to recognise "compressed summer conditions".
- Daily loss limit, trade count, and any rule for scaling into winners. The Chart Academy blurb on the page mentions scaling into winners, but the playbook rules don't define it.
- Footprint and profile settings (row size, aggregation).

## Evidence & claims

- **"About 70% of the time" claims:** the market stays stuck in balance about 70% of the time, and price reverses from balance about 70% of the time. Self-reported (T4); no data.
- **R:R claim:** normal trades deliver 1:2.5 to 1:5 reward-to-risk, with much larger ratios on strong days. Self-reported (T4). The page states no win rate, so a full expectancy check isn't possible. Break-even win rates before costs are 28.6% at 1:2.5 and 16.7% at 1:5.
- **Acknowledged drawbacks:** consecutive small losses, a lower win rate in chop, and stress when managing large size intraday.
- **Competition results (earlier note, T3 search summaries, not re-verified here):** top 3 in the Robbins World Cup Trading Championship futures/scalping division, with audited returns reported at 218% to 500%+ depending on source and edition.
- **Earlier risk figure (T3):** a third-party guide gave about 0.25% risk per trade. The playbook's 0.25%–0.5% range now supersedes it.

## Concepts & lineage

- Balance vs imbalance, fair value, failed breakouts back to POC: [[concept_auction_market_theory]]
- LVNs inside the impulse or reclaim leg as location, POC as target: [[concept_volume_profile]]
- Big prints, footprint imbalance and CVD as the aggression trigger: [[concept_order_flow]]
- Separate models for trending and ranging conditions: [[concept_market_regimes]], [[concept_trend_following]], [[concept_mean_reversion]]
- New York for trend, London or summer for mean reversion, avoid the London open: [[concept_trading_sessions_killzones]]
- 0.25–0.5% risk per trade: [[concept_position_sizing]]; 1:2.5–1:5 targets: [[concept_risk_reward_r_multiples]]
- Alerts instead of blind limits, enter only on aggression: [[concept_trade_execution]], [[concept_scalping]]
- Lineage (earlier note, T3; not stated in the playbook): Steidlmayer's Market Profile (CBOT, 1980s) → Dalton's *Mind Over Markets* → order-flow tooling (footprint, DOM) → Fabio's state/location/aggression model.

## Changes vs. earlier note

- **Corrected:** the earlier note (T3, Chart Academy) called the three filters "Direction → Location → Aggression". The playbook calls them **Market State → Location → Aggression**. The Chart Academy blurb on the same page still uses "Direction, Location, and Aggression", so both names are kept as aliases.
- **Corrected:** the earlier note described the trend model as joining aggression *after acceptance beyond value* (T3). The playbook enters on a **pullback into an LVN of the impulse leg** with aggression, and targets the **previous balance POC** with a full exit.
- **Corrected:** the earlier note listed VWAP as a tool and said "no lagging oscillators" (T3). The playbook mentions neither, so VWAP was removed from `uses`.
- **Corrected:** risk was about 0.25% per trade (T3). The playbook says **0.25%–0.5%** (T2).
- **Answered:** two of the earlier open questions. Stop rule: beyond the aggressive print plus 1–2 ticks, never widen. Targets: the POC in both models. Daily loss limit and trade count are still not in the playbook.
- **Added:** session preferences per model, mean-reversion entry only after a reclaim plus pullback (not the first move back), alerts rather than blind limits, early break-even on strong CVD, and the claimed 1:2.5–1:5 R:R.
- Dropped the empty `teaches` key and moved the earlier lineage line into Concepts & lineage. Kept all earlier sources and the extra `featured_in` entry.
