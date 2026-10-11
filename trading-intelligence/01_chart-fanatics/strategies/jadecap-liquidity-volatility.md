---
id: strategy_jadecap_liquidity_volatility
type: strategy
title: "JadeCap — Intraday Liquidity & Volatility Model: New York Session Liquidity Raids (futures/forex, day trading/swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [JadeCap Liquidity Trading Strategy, Intraday Liquidity Volatility Model, session liquidity raid model, JadeCap model]
taught_by: [person_jadecap]
featured_in: [channel_chart_fanatics]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_fair_value_gap, concept_market_structure, concept_order_blocks_breakers, concept_trading_sessions_killzones, concept_multi_timeframe_analysis, concept_smt_divergence, concept_trading_journal_review]
derived_from: [concept_smart_money_concepts, concept_liquidity]
related: [strategy_tg_capital_trident, strategy_dhesi_liquidity_inversion, strategy_marco_trades_liquidity_grab, strategy_candace_lau_nq_sweep_reversal]
sources:
  - {title: "Chart Fanatics — JadeCap Liquidity Trading Strategy", url: "https://www.chartfanatics.com/strategies/intraday-liquidity-volatility-model", tier: T2}
status: verified-t2
---

# JadeCap — Intraday Liquidity & Volatility Model: New York Session Liquidity Raids (futures/forex, day trading/swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/intraday-liquidity-volatility-model. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits JadeCap with this intraday model. It
trades New York session raids on overnight and prior-day liquidity, and
both worked examples are NQ shorts. The page gives no biography.

## Built for

- **Instruments:** futures and forex. The pros list says crypto also works
  with slight adjustments. Both examples are **NQ**.
- **Style:** day trading first. Swing trades are possible when the higher
  timeframe agrees.
- **Timeframes:** **daily** for bias. **15m and 5m** for confirmation. One
  example enters from a **1H** FVG.
- **Session:** New York. The page's ideal window for setups is
  **9:30–11:30 AM EST**, listed among the conditions for a trade. Intraday trades may be closed around midday; one example exits
  near 12:15 PM.

## Core idea

Stop orders cluster just above recent highs and below recent lows. Price
often runs into those pools and then either reverses sharply or continues.
Start each day with a daily bias. Mark the prior day's and the Asian and
London session highs and lows. Wait for New York to take one of them, then
enter only after lower-timeframe confirmation: an FVG, a market structure
shift, a turtle soup (failed breakout), a breaker block, or divergence
between related markets. Target the opposite liquidity, and respect time
of day.

## Rules

1. **Set a daily bias** from the daily chart, using recent highs and lows,
   inefficiencies and where price is likely to go next.
2. **Mark session liquidity:** the previous day's high and low, the Asian
   session high and low, and the London session high and low.
3. **Wait for a liquidity raid in the New York session.** One of those
   levels must be taken out.
4. **Confirm on the 15m or 5m.** After the raid, require one of: a fair
   value gap, a market structure shift, a turtle soup (false breakout and
   reversal), or a breaker block. The overview also lists divergence
   between markets as a confirmation.
5. **Time window:** setups should form in the **9:30–11:30 AM EST**
   window, which the page calls the ideal window and lists among the
   conditions for a trade.
6. **Entry** (from the examples):
   - *Immediate:* short right after the sweep (here, of the previous day's
     high) once price fails to continue higher.
   - *Second chance:* short on a retracement into a fresh bearish FVG (15m
     or 1H) that rejects.
   - The page shows no long example; longs are presumably the mirror
     image.
7. **Stop:** beyond the sweep extreme, which is above the sweep high in
   both short examples.
8. **Targets:**
   - *Intraday:* opposite-side session liquidity, FVGs, or equal highs and
     lows. In the first example the target was the untouched Asian session
     low.
   - *Swing:* higher-timeframe liquidity (daily or weekly highs and lows),
     imbalances or major structure. Hold for days while the bias and
     structure still support it.
9. **Time-based exit:** if an intraday trade slows near midday, consider
   closing before the full target to avoid afternoon chop. Whether to stay
   in is a judgement call based on the clock, how price is behaving and
   your own risk tolerance.

## Risk management

- **Stop:** beyond the high or low of the liquidity sweep.
- **Time stop:** discretionary exit around midday if momentum fades.
- **Risk per trade ($ or %), position size, minimum R:R, daily or weekly
  loss limits:** Not specified in the playbook.
- **Partials:** mentioned as a skill that takes practice, with no rule
  given.
- **Record-keeping:** the page says confidence in the model comes from
  tracking outcomes and journaling.

## What the playbook leaves unspecified

- How to set the daily bias in concrete terms.
- The hours of the Asian and London sessions used to mark their highs and
  lows.
- Whether the raid itself must occur inside 9:30–11:30 AM, or only the
  entry.
- How to rank the five confirmation types, and what counts as "divergence
  between markets" (which instruments).
- Any minimum reward-to-risk, partial-profit or break-even rule.
- How forex traders should adapt a window built around the 9:30 AM
  equity open.
- How "volatility" is measured or used. It appears in the model's name
  but is never operationalised.
- A long-side worked example.

## Evidence & claims

- The page reports **no win rate, R:R, P&L or payout**.
- **NQ short, 15m:** a previous-day-high sweep failed. There were two
  entries, an immediate short and a later 15m FVG retest, both with stops
  above the sweep high. The exit came when price tagged the Asian low at
  roughly 12:15 PM EST. Self-reported (T4), with no R or
  dollar result.
- **NQ short from a 1H FVG:** an Asian-high sweep at the start of the
  session, entry inside the 1H bearish FVG, and the page says target was
  hit within the session. Self-reported (T4), with no R or dollar result.
- With no win rate or R:R, no expectancy check is possible.

## Concepts & lineage

- Stops above highs and below lows; previous-day and session highs and
  lows as pools → [[concept_liquidity]]
- Raid, then confirmed reversal or continuation; turtle soup →
  [[concept_liquidity_sweep_reversal]]
- FVG confirmation and FVG retest entries → [[concept_fair_value_gap]]
- Market structure shift → [[concept_market_structure]]
- Breaker block confirmation → [[concept_order_blocks_breakers]]
- Asian and London ranges, the 9:30–11:30 AM EST window and midday exits →
  [[concept_trading_sessions_killzones]]
- Daily bias with 15m, 5m or 1H execution →
  [[concept_multi_timeframe_analysis]]
- Divergence between related markets as confirmation →
  [[concept_smt_divergence]]
- Tracking outcomes and journaling to build confidence →
  [[concept_trading_journal_review]]
- Lineage (our attribution; the page speaks of institutional traders
  seeking stops but does not name ICT): ICT-style smart-money liquidity
  concepts →
  [[concept_smart_money_concepts]]
