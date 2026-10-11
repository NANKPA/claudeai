---
id: strategy_kris_verma_shorting
type: strategy
title: "Kris Verma — Small-Cap Shorting: Gap Fades, Backside Parabolics & Halt Exhaustion (small-cap stocks, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Kris Verma’s Small-Cap Shorting Strategy", small-cap gap fade, backside parabolic short, multi-halt exhaustion short, share recycling]
taught_by: [person_kris_verma]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_market_microstructure, concept_liquidity, concept_trading_sessions_killzones, concept_support_resistance, concept_trade_management, concept_position_sizing, concept_probability_fat_tails, concept_performance_metrics, concept_backtesting]
derived_from: [concept_mean_reversion]
related: [strategy_steven_dux_small_cap_short, strategy_marios_stamatoudis_parabolic_short, strategy_alex_temiz_first_red_day, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — Kris Verma’s Small-Cap Shorting Strategy", url: "https://www.chartfanatics.com/strategies/shorting-strategy", tier: T2}
status: verified-t2
---

# Kris Verma — Small-Cap Shorting: Gap Fades, Backside Parabolics & Halt Exhaustion (small-cap stocks, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/shorting-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Kris Verma shorts small-cap stocks. His playbook combines a
data-driven base with time-of-day rules, behaviour checks and share
recycling. The page gives no further biography.

## Built for

- **Instruments:** small-cap stocks that gap up sharply, typically driven
  by promotion, hype or thin pre-market trading instead of any genuine
  improvement in the business.
- **Style:** scalping and day trading, short side only.
- **Time window:** pre-market through early morning, **4:00 to 10:00 AM**,
  is preferred. The edge fades after about **12:00 PM**, and trading is
  usually cut back or stopped after midday.
- **Timeframe:** no chart timeframe is specified.

## Core idea

Weak small-caps often use sudden spikes in liquidity to sell stock, so
their gaps tend to fade. The page notes that more volume and more traders
in recent years mean failed fades now often squeeze hard before the stock
finally drops. The playbook therefore refuses to guess front-side tops. It
waits for behavioural proof that the move is failing, uses **wide
fixed-percentage stops** to survive manipulation, and **recycles shares**
through ranges. It judges results by overall profit factor rather than
textbook R:R.

## Rules

1. **Filter the universe.**
   - Market cap: **under $100M preferred, about $200M maximum**.
   - Institutional ownership: **under about 40% preferred**.
   - Gap strength: large percentage gaps only. Avoid smaller moves of
     **about 20 to 40%**, which are less reliable now that volatility and
     ranges have expanded.
2. **Setup A: gap-up short with fade validation** (the page labels this
   "ADF behavior" without defining it).
   - No pre-market entries. Wait for the open.
   - The stock must start fading and trade weak relative to its open.
   - **10:00 AM check:** below the open, with volume falling as price
     drops, means the setup is confirmed.
   - Short into pops or bounces. Never short the low of a flush.
   - *Invalidation:* if the stock is holding above the open at 10:00,
     reduce or remove the risk.
3. **Setup B: backside parabolic short** (the page calls it the primary
   edge).
   - A large move has already happened, and topping signs appear: upper
     wicks, failed pushes, slowing momentum, volume falling as price fades.
   - Skip the first wobble. Act only once the stock has clearly rolled
     over from front side to backside.
   - Enter on bounces during the fade, never at the lows.
   - Expected downside, based on historical pullbacks: **about 30 to
     40%**. The goal is consistency, not catching every move. This setup
     works best earlier in the day.
4. **Setup C: multi-halt exhaustion short.**
   - No entries during the early up-halts. Consider a short only after
     **several up-halts (commonly 4 to 5)**, when resumption candles show
     brief dips followed by pushes (forced covering) and the extension is
     historically extreme.
   - Base the entry on how far the stock has already run, not on a guess
     about the next halt. Keep size conservative, because these names are
     volatile and illiquid.
5. **Stops.**
   - **Do not use pre-market highs as stops.** A break above them often
     sets off short covering before the reversal.
   - Use a **fixed-percentage wide stop** from the entry, so manipulation
     does not shake you out. Staying in the trade matters more than a tight
     stop.
6. **Time-based management.**
   - *10:00 AM rule:* below the open, downside continuation is more likely.
     Above the open, reduce risk or consider exiting.
   - *30-minute rule:* if the trade is working after about 30 minutes, keep
     holding. If price is reclaiming or stalling, reassess.
   - *Ongoing checks:* volume behaviour, signs of manipulation, the overall
     strength of small caps, and sympathy moves in other gappers.
7. **Recycling.**
   - When a stock ranges instead of fading cleanly, take partial profits
     into sharp drops near support.
   - Re-short bounces into prior support that has turned into resistance,
     and repeat within the range.
   - Use recycling when the stock grinds against you. The aim then shifts
     from directional conviction to limiting the damage.

**Worked example: CRCL multi-day backside short.** CRCL was in an extended
multi-day run. The short came only after the move stalled, red candles
appeared and selling pressure became visible. The position was held
through the first push down. Partials were taken at the prior day's close,
a level where a bounce was likely. The bounce was re-shorted into
resistance, and the cycle was repeated.

## Risk management

- **Stops:** wide, at a **fixed percentage** from entry, never at
  pre-market highs. **The percentage is not specified in the playbook.**
- **Accepted trade-off:** a higher win rate in exchange for larger single
  losses. Judge the method by overall profit factor.
- **Sizing:** kept controlled. Conservative on multi-halt shorts. No single
  trade may put the account at risk.
- **Outlier risk:** thin liquidity and halts can push price beyond expected
  levels.
- **Costs:** hard-to-borrow fees and locate costs eat into profit.
  Recycling reuses located shares, and the choice of broker matters.
- **Risk per trade, daily or weekly loss limit:** not specified in the
  playbook.

## What the playbook leaves unspecified

- The stop percentage, and how it varies by setup or stock price.
- The minimum gap size. The page says only to avoid moves of roughly 20 to
  40%.
- What "ADF behavior" means.
- How many consecutive red candles or failed pushes confirm a backside
  move, and on which chart timeframe.
- A conflict in timing: the preferred window starts at **4:00 AM**
  pre-market, yet Setup A forbids pre-market entries. The page never says
  which setups, if any, may be entered pre-market.
- The size of partials and re-entries in recycling, and how far a range may
  stretch before recycling stops.
- The data behind the "data-backed edge" (sample, period, metrics).

## Evidence & claims

- The pros claim a **"Proven, data-backed edge"**. Self-reported (T4); the
  page shows no statistics.
- The stops are described as producing a **higher win rate with larger
  individual losses**. This is qualitative and self-reported (T4), with no
  figures.
- **About 30 to 40% downside targets** come from the trader's own read of
  historical pullbacks. Self-reported (T4).
- The CRCL example is called profitable but gives no prices or P&L (T4).
- With no win rate or R:R given, no expectancy check is possible. Note that
  with wide stops and a high win rate, the outcome depends on how large the
  tail losses are, so profit factor should be measured directly.

## Concepts & lineage

- Fading hype gaps back toward value → [[concept_mean_reversion]]
- Halts, thin floats, locates and borrow costs, forced covering →
  [[concept_market_microstructure]], [[concept_liquidity]]
- The 4:00 to 10:00 AM window, the 10:00 AM check, the 30-minute check, the
  midday cutoff → [[concept_trading_sessions_killzones]]
- Prior support turning into resistance in recycling; the prior day's close
  as a bounce level → [[concept_support_resistance]]
- Partials, re-entries, reducing risk when the stock holds above the open →
  [[concept_trade_management]]
- Conservative size and no single account-threatening trade →
  [[concept_position_sizing]]
- Squeeze and outlier risk from wide stops →
  [[concept_probability_fat_tails]]
- Profit factor over R:R, plus regular backtesting and review →
  [[concept_performance_metrics]], [[concept_backtesting]]
