---
id: strategy_rajan_dhall_auction
type: strategy
title: "Rajan Dhall — Auction Market Strategy: Auction-Zone Retest with Trend (stocks/futures, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Rajan Dhall Auction Market Strategy, market auction theory, A+ Simple Trading Strategy, A+ trading playbook, Rajan Dhall strategy]
taught_by: [person_rajan_dhall]
featured_in: [channel_chart_fanatics]
uses: [concept_auction_market_theory, concept_trend_following, concept_moving_averages, concept_multi_timeframe_analysis, concept_support_resistance, concept_candlestick_patterns, concept_market_sentiment, concept_trading_sessions_killzones, concept_risk_reward_r_multiples]
derived_from: [concept_auction_market_theory, concept_trend_following]
related: [strategy_fabio_valentini_amt_order_flow, strategy_andrea_cimitan_amt, strategy_vincent_desiano_break_retest]
sources:
  - {title: "Chart Fanatics — Rajan Dhall Auction Market Strategy", url: "https://www.chartfanatics.com/strategies/market-auction-theory", tier: T2}
  - {title: "Riz Iqbal on X (May 2025) — Rajan Dhall episode announcement", url: "https://x.com/Wordsof_Rizdom/status/1925902141010452612", tier: T4}
status: verified-t2
---

# Rajan Dhall — Auction Market Strategy: Auction-Zone Retest with Trend (stocks/futures, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/market-auction-theory. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Rajan Dhall teaches a free 7-lesson masterclass on Chart
Academy. It covers auction market theory, volume profile, a 21 moving
average trend-following approach across three timeframes, and reading
sentiment before the session. His May 2025 Chart Fanatics episode was
announced as an "A+ Simple Trading Strategy" (T4).

## Built for

- **Instruments:** stocks and futures. The page says it is used mainly on
  stocks but also suits indices and crypto, or any market with a strong
  intraday range. The worked example is SPY.
- **Style:** scalping and day trading.
- **Timeframes:** **daily** for bias, **5-minute** for execution. The page
  calls the method fractal, for example monthly with daily, or daily with
  5-minute.
- **Time window:** the **first hour after the open**. Avoid the middle and
  late session unless conditions clearly line up.

## Core idea

Each day's trading is an auction. The prior day's candle and the daily
trend give the direction. On the 5-minute chart, the **auction zone** is
the congestion or value area where buyers and sellers found temporary
balance. The setup comes when price **returns to that zone and rejects it
in the trend's direction**, usually in the high-volume first hour. Moving
averages only confirm that the two timeframes agree. A rejection candle is
the trigger, and trades target at least **2:1**.

## Rules

1. **Directional bias.** Take it from the **previous day's daily candle**.
   A strongly bearish close means a short bias for the next day; a bullish
   one means long.
2. **Trend alignment on both timeframes.** The daily chart must show a
   clear trend, which the page describes as about 45 degrees. The 5-minute
   chart must trend the same way. For longs, price is **above the moving
   averages** (the page's example is 21/50 MAs) on both timeframes; for
   shorts, below. The MAs only confirm
   alignment visually. They are not signals.
3. **Open and gap context.** At the open, check whether price gapped up or
   down, and whether it opened inside or outside the previous day's range.
4. **Mark the auction zone.** On the 5-minute chart, find the area where
   price consolidated or found balance. In the SPY example this was a
   range that formed right after the open, then broke in the trend
   direction.
5. **Entry.** When price retests the auction zone and prints a **rejection
   candle** (for a short: trades into the zone and closes back below it),
   enter **as soon as that candle closes**.
6. **Stop.** Just beyond the setup candle: **above the rejection candle's
   high** for shorts, **below its low** for longs.
7. **Target.** At least **2:1** reward-to-risk.
8. **Retests.** Later retests that reject the same zone again can be traded
   the same way. The SPY example gave a second short.
9. **No-trade conditions.**
   - The daily and 5-minute charts disagree.
   - The auction structure is messy, or sentiment is unclear (for example,
     conflicting news headlines).
   - Price never retests the zone, or sells off at the open with no
     structure.

## Risk management

- **Stop:** beyond the rejection candle's high or low.
- **Reward-to-risk:** minimum 2:1. The cons note that most trades target
  2:1, so large R multiples are not possible without modifying the method.
- **Risk per trade (% or $), sizing:** not specified in the playbook.
- **Daily or weekly limits, maximum number of trades:** not specified in
  the playbook.
- **Temperament:** being a "good loser" and acting fast are listed as
  requirements, because trades often trigger within seconds of the open.

## What the playbook leaves unspecified

- How strong a prior-day candle must be to set a bias, and what to do after
  an indecisive day.
- An objective test for a "45-degree" daily trend, and the MA type (the
  example uses the 21 EMA; the rules say 21/50 MAs "e.g.").
- How to draw the auction zone (its boundaries and minimum duration), and
  whether volume profile is used. The masterclass covers volume profile,
  but the playbook's rules do not.
- What shape counts as a rejection candle, beyond closing back outside the
  zone.
- How the gap and open-location context should change the trade. It is
  listed as context, without rules.
- Whether to move the stop to breakeven, take partials, or how many retests
  remain valid.

## Evidence & claims

- **SPY example:** two shorts after retests of the auction zone, and both
  reached the 2:1 target. Self-reported (T4), with no prices given.
- The page claims **no win rate, P&L or payout**.
- **Expectancy context:** at a fixed 2:1, the break-even win rate is about
  33%. With no stated win rate, E = p×2 − (1−p) cannot be evaluated.

## Concepts & lineage

- The day as an auction, with a congestion or value area as the zone of
  balance → [[concept_auction_market_theory]]
- Trading only with the daily trend → [[concept_trend_following]]
- 21 and 50 MAs as an alignment filter → [[concept_moving_averages]]
- Daily bias with a 5-minute execution; fractal timeframe pairs →
  [[concept_multi_timeframe_analysis]]
- Retesting a broken balance zone → [[concept_support_resistance]]
- The rejection candle as trigger → [[concept_candlestick_patterns]]
- Gap and headline sentiment as context → [[concept_market_sentiment]]
- The first-hour window → [[concept_trading_sessions_killzones]]
- The fixed 2:1 target → [[concept_risk_reward_r_multiples]]

## Changes vs. earlier note

- **Status upgraded from `pending-scrape`.** The earlier note had no rules,
  only a T4 episode announcement. The playbook now provides the full rule
  set at T2.
- **Name.** The earlier note was titled "A+ Simple Strategy & Market
  Auction Theory", taken from the episode announcement (T4). The page is
  titled **"Rajan Dhall Auction Market Strategy"**. The A+ names are kept
  as aliases only.
- **Lineage confirmed, with a nuance.** The earlier note assumed descent
  from auction market theory, and the playbook confirms the auction
  framing. The execution itself, though, is a trend-aligned retest of a
  5-minute consolidation with an MA filter, so trend following is added as
  a second parent.
- **`concept_volume_profile` removed from `uses`.** The playbook's rules
  define the auction zone from price congestion. Volume profile appears
  only in the masterclass description.
- **Added:** the prior-day-candle bias, dual-timeframe 21/50 MA alignment,
  gap and open context, the rejection-candle entry and stop, the 2:1
  target, the first-hour window and the no-trade conditions.
