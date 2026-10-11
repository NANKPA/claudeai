---
id: strategy_marios_stamatoudis_parabolic_short
type: strategy
title: "Marios Stamatoudis — Parabolic Short: Exhaustion-Day VWAP Failure (stocks, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Parabolic Short Strategy, parabolic exhaustion short, exhaustion day VWAP rejection, Marios parabolic short]
taught_by: [person_marios_stamatoudis]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_vwap, concept_market_structure, concept_moving_averages, concept_market_sentiment, concept_support_resistance, concept_volatility, concept_trade_management]
derived_from: [concept_mean_reversion]
related: [strategy_alex_temiz_first_red_day, strategy_kyle_williams_first_red_day, strategy_kris_verma_shorting, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — Parabolic Short Strategy", url: "https://www.chartfanatics.com/strategies/parabolic-short-strategy", tier: T2}
status: verified-t2
---

# Marios Stamatoudis — Parabolic Short: Exhaustion-Day VWAP Failure (stocks, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/parabolic-short-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Marios Stamatoudis with this stock day
trading setup for shorting the collapse of an exhausted parabolic run. The
page gives no biography.

## Built for

- **Instruments:** stocks, from small caps to large caps, including
  theme-driven names and recent IPOs.
- **Style:** day trading. Positions are closed before the end of the day.
  The same read can also be used to exit longs into strength.
- **Timeframes:** daily chart to qualify the run (size of the move, the
  20-day moving average base, acceleration). Intraday chart with **VWAP**
  for execution; no intraday timeframe is named.
- **Window:** the exhaustion day is usually the day of the final push or
  the next day. If nothing triggers within **two days**, drop the idea.
- **Frequency:** not a daily setup. It needs patience.

## Core idea

A fast run attracts early buyers, then momentum traders, then late chasers.
Once nearly everyone who wants in is in, demand is spent and the trend is
held up only by existing holders. A small trigger can then cause a sharp,
same-day collapse. Do not call the top. Qualify the run by its size and
acceleration, then wait for an **exhaustion day** when price breaks its
intraday structure, loses VWAP and fails to win it back. Short that
failure with the stop at the high of the day.

## Rules

1. **Filter 1: size of the move.** Measure it from the **latest base**
   rather than the lowest point of the chart. The base is the last touch of the **20-day moving
   average** before the run.
   - Small cap: about **200% or more**.
   - Mid cap: about **100%**.
   - Large cap: about **50%**.
   - Moves far beyond these are an extreme zone, where a sharp reversal is
     more likely and the drop can be more violent.
2. **Filter 2: structure of the move.** The run must accelerate: larger
   candles, a steeper slope, sometimes gaps between sessions. Slow,
   controlled trends with small candles, or trends with regular pullbacks
   that release pressure, do not qualify. The strongest case is a steady
   climb that suddenly turns into a fast, aggressive phase, which traps
   both early holders and late chasers.
3. **Optional strengtheners:** volume at the highest level in recent
   history (the last wave of buyers), and a first touch of a round number
   such as 100, 300 or 500 after the run.
4. **Estimate the expected move before entering.**
   - Established, long-trending stocks: about **10% to 20%**, sometimes
     more after an extreme run.
   - Hype or theme stocks: about **20% to 40% or more** in a day.
   - IPOs: usually in between, and less predictable.
   - Skip it when a large share of the expected drop is already done, such
     as after a big gap down.
5. **Require the exhaustion day.** Price stops making higher highs, prints
   lower highs and then lower lows, and **moves below VWAP without
   reclaiming it**. A weak bounce toward VWAP that gets rejected confirms
   it. If price holds above VWAP and keeps climbing, the setup is not
   active.
6. **Entry, from earliest to best:**
   1. Upward intraday structure breaks into lower highs and lower lows.
      This is the earliest entry and the riskiest.
   2. A structure break and a VWAP loss together. This is stronger.
   3. A **failed attempt to reclaim VWAP**. This is the best entry.
7. **Invalidation.** A strong VWAP reclaim followed by continuation higher
   cancels the setup.
8. **Stop** at the **day's high**, or at the latest lower high.
9. **Take partial profits** once the trade moves in your favour, then move
   the stop to **break-even**.
10. **Risk-free add.** With the stop at break-even, a second VWAP test that
    fails again is a place to add size. If it fails, the earlier profits cover the
    added piece.
11. **Close before the end of the day.** No overnight holds.
12. **Two attempts at most.** If the setup fails once, one more try is
    allowed. If it fails again, move on.

## Risk management

- **Stop:** the day's high, or the latest lower high.
- **Break-even:** after the first partial.
- **Adding:** only after the stop is at break-even (the "risk-free add").
- **Attempts:** a maximum of two per setup.
- **Overnight:** not allowed.
- **Risk per trade ($ or %), position size, and daily or weekly loss
  limits:** Not specified in the playbook.
- **Short-specific risks** (borrow availability, short-sale restriction,
  halts, squeezes): Not specified in the playbook.

## What the playbook leaves unspecified

- Market-cap cut-offs for small, mid and large caps.
- An objective measure of acceleration, such as slope, candle size or gap
  count.
- The intraday chart timeframe used for structure and VWAP.
- How much to take at the first partial and where, and the final profit
  target. The expected-move ranges are the only guide.
- What counts as a "strong" VWAP reclaim, for example a close above it or
  holding for a set time.
- How far back "highest volume in recent history" looks.
- How the two-day window is counted when the final push spans more than
  one session.
- Practical short-selling constraints.

## Evidence & claims

- **SMCI example (early 2024):** the page says the run ticked every box: a
  big prior advance, wide-range candles, heavy volume and a nearby key
  level. The short came at the VWAP rejection, with the stop at the day's
  high.
  The stock fell about **23% to 24% in one day**, which the page says
  matched expectations and ended the larger uptrend. Self-reported (T4).
- **Quantum computing stocks, late 2024:** used as an illustration of
  crowded runs collapsing on negative news. No trade result is given.
- **Typical drop sizes** (10–20% for established names, 20–40% or more for
  hype names, IPOs in between) are self-reported expectations (T4).
- The page calls the setup very high-probability but gives **no win rate,
  R:R or trade sample**, so no expectancy check is possible.

## Concepts & lineage

- Fading an overextended, crowded run back toward value →
  [[concept_mean_reversion]]
- VWAP loss, failed reclaim and rejection as the trigger →
  [[concept_vwap]]
- Lower highs and lower lows confirming the turn →
  [[concept_market_structure]]
- The 20-day moving average as the base for measuring the run →
  [[concept_moving_averages]]
- FOMO buying, crowded trades and exhausted demand →
  [[concept_market_sentiment]]
- Round-number psychological levels → [[concept_support_resistance]]
- Expected move by stock type and extreme extensions →
  [[concept_volatility]]
- Partials, break-even and the risk-free add →
  [[concept_trade_management]]
