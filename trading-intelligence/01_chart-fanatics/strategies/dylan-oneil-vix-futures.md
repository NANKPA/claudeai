---
id: strategy_dylan_oneil_vix_futures
type: strategy
title: "Dylan O’Neil — VIX Futures Strategy: VIX Pressure as Confirmation for ES and NQ (index and VIX futures, day and swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["VIX Futures Strategy: Volatility-Based Edge", Dylan O'Neil VIX strategy, VIX confirmation at previous-day levels, VIX 1% rule]
taught_by: [person_dylan_oneil]
featured_in: [channel_chart_fanatics]
uses: [concept_volatility, concept_market_sentiment, concept_intermarket_analysis, concept_divergence, concept_smt_divergence, concept_support_resistance, concept_breakout_trading, concept_liquidity_sweep_reversal, concept_chart_patterns, concept_market_microstructure, concept_market_regimes, concept_risk_reward_r_multiples]
derived_from: [concept_intermarket_analysis, concept_volatility]
related: [strategy_trader_kane_lab_model, strategy_tanja_amd_futures]
sources:
  - {title: "Chart Fanatics — VIX Futures Strategy: Volatility-Based Edge", url: "https://www.chartfanatics.com/strategies/the-vix-futures-strategy", tier: T2}
status: verified-t2
---

# Dylan O’Neil — VIX Futures Strategy: VIX Pressure as Confirmation for ES and NQ (index and VIX futures, day and swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/the-vix-futures-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Dylan O’Neil trades futures using the VIX as a live gauge of
pressure on the S&P 500. He uses it to judge whether ES and NQ moves have
real force behind them. The page gives no further biography.

## Built for

- **Instruments:** futures: **ES** (the main target), **NQ** as a second
  confirmation, and **VIX futures**, which the trade example goes long.
- **Style:** day trading and swing trading. The page presents it mainly as
  a **confirmation layer** to add to an existing strategy, plus some
  stand-alone turning-point trades.
- **Timeframes:** the page says it works on all timeframes. ES, NQ and the
  VIX must be watched on **matching timeframes**.
- **Key reference:** each instrument's **previous day high and low**.
- **Session:** no specific time window. The example mentions a "clean
  time-of-day alignment" without saying what it was.

## Core idea

The VIX is priced from SPX options, mostly put demand, so it shows how much
fear or hedging pressure sits on the S&P. More put demand lifts the VIX and
weighs on ES. Less put demand lowers the VIX and takes weight off. The page
claims most ES volume is algorithmic and that VIX moves trigger sell or buy
programs. On that basis, the VIX tells you whether an ES or NQ break of a
key level is real or likely to fail. Dylan's analogy: with a low VIX, ES
climbs a mountain carrying no weight; with a high VIX, it climbs carrying a
heavy backpack.

## Rules

1. **Read the VIX backdrop.** A weak or falling VIX makes it easier for ES
   to hold support and rise. A strong or rising VIX makes rallies more
   likely to fail.
2. **Mark previous-day levels** on ES, NQ and the VIX, using matching
   timeframes.
3. **Confirmed breakdown (continuation):** ES breaks its previous day low,
   **and** the VIX is rising and at or above its previous day high. If NQ
   **also** breaks its previous day low, all three agree and further
   downside is more likely.
4. **Unconfirmed breakdown (failure or squeeze):** ES breaks its previous
   day low, but the VIX is **not** at its previous day high or is making a
   lower high. That alone means the break lacks pressure and has a good
   chance of failing. If NQ also holds above its own low or makes a higher
   low, the relative strength adds to the case. **Do not short it.** Once
   ES gets back above the previous day low, it often snaps back and
   squeezes higher, trapping shorts.
5. **VIX moves first:** if the VIX reaches its previous day high *before*
   ES or NQ break their lows, pressure is building early. When ES does
   break, the move is more likely to continue.
6. **Pair support and resistance across the two charts.** VIX at support
   (likely to bounce) with ES at resistance points to an ES turn lower. VIX
   at resistance (likely to turn down) with ES at support points to ES
   holding or rising. These pairings mark the strongest turning points.
7. **The 1% rule:** if ES is up 1% or more **and** the VIX is also up 1% or
   more, ES strength is fragile and pushes into resistance tend to fail. If
   ES is down 1% or more **and** the VIX is down 1% or more, the weakness is
   fragile and support tends to hold. Use this to avoid chasing extended
   moves.
8. **Natural floor at major highs:** near all-time or multi-year highs,
   puts are cheap and funds hedge more, so the VIX can rise while ES holds.
   A rising VIX there is **not** a reliable breakdown signal on its own.
   Lean on ES levels instead.
9. **Stand-alone VIX trade (the page's example):** go long VIX futures at a
   clear **contract low** (about **16.8**) where a **double bottom** forms,
   while ES **fails to break out at all-time highs**. Extra context in the
   example: the S&P had sold off on four of the previous five Fridays, and
   the VIX bounce came on a Thursday.
10. **No duplicate exposure.** Do not take the same trade on several
    instruments at once (for example, short ES, short NQ and long VIX).

## Risk management

- **Avoid duplicated risk:** do not express one idea on several
  correlated instruments at the same time.
- **Stop placement, targets, position size, risk per trade and daily or
  weekly limits:** not specified in the playbook. The VIX example gives a
  6R result but no stop or target level.
- **Invalidation:** implied only. For example, a "confirmed" breakdown
  stops being confirmed if the VIX falls back below its previous day high,
  but the page gives no explicit exit rule.

## What the playbook leaves unspecified

- Entry triggers, stops and targets for ES and NQ trades. The page reads as
  a filter, not a full system.
- Upside mirror rules (ES breaking its previous day high with the VIX at or
  below its previous day low). The page only explains the downside cases,
  though it says previous-day highs are used too.
- What timeframe(s) to use, and what "matching timeframes" means in
  practice.
- Whether the previous day's levels are from the regular session or the
  full overnight session, given VIX and ES trading hours.
- How to identify "important" VIX support and resistance beyond previous
  day levels and contract lows.
- Whether the 1% rule uses VIX percentage change or point change, and
  measured from what reference (prior close).
- How "natural floor" VIX levels are defined, and how to trade near
  all-time highs.
- Handling VIX futures roll, contango and contract choice for the
  stand-alone VIX trades.
- The "clean time-of-day alignment" in the example.

## Evidence & claims

- **Long VIX futures example:** a **6:1 R** outcome. Self-reported (T4).
  It is a single trade, and there is no win rate, so no expectancy check is
  possible.
- **"About 90% of ES volume is algorithms"**, and VIX moves trigger
  sell or buy programs. A market-structure claim from the page, not
  independently sourced. Treat as self-reported (T4).
- **Four of five prior Fridays sold off:** context in the example, not a
  tested statistic. Self-reported (T4).
- The page's pros (filters fakeouts, confirms strength, works on all
  timeframes) are qualitative claims, not measured results. It also admits
  false signals near all-time highs.

## Concepts & lineage

- VIX as SPX-options implied volatility and a fear gauge →
  [[concept_volatility]], [[concept_market_sentiment]]
- Using the VIX and NQ to confirm or reject ES moves →
  [[concept_intermarket_analysis]]
- Non-confirmation between ES, NQ and the VIX at previous-day levels.
  Editorial: the ES-versus-NQ part matches ICT-style SMT divergence →
  [[concept_divergence]], [[concept_smt_divergence]]
- Previous day highs and lows, and VIX support and resistance →
  [[concept_support_resistance]]
- Telling real breakdowns from fake ones, and the snap-back squeeze after
  an unconfirmed break → [[concept_breakout_trading]],
  [[concept_liquidity_sweep_reversal]]
- Double bottom at a VIX contract low → [[concept_chart_patterns]]
- Algorithmic sell and buy programs keyed to the VIX →
  [[concept_market_microstructure]]
- The VIX's natural floor at major highs, where signals change →
  [[concept_market_regimes]]
- 6R outcome reported on the VIX trade →
  [[concept_risk_reward_r_multiples]]
