---
id: strategy_alex_temiz_first_red_day
type: strategy
title: "Alex Temiz — First Red Day Strategy (stocks/options, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [First Red Day, FRD short, Alex's First Red Day, red-to-green line short]
taught_by: [person_alex_temiz]
featured_in: [channel_chart_fanatics]
uses: [concept_price_action, concept_support_resistance, concept_mean_reversion, concept_market_sentiment, concept_trade_management, concept_position_sizing]
derived_from: [concept_mean_reversion]
related: [strategy_kyle_williams_first_red_day, strategy_marios_stamatoudis_parabolic_short, strategy_kris_verma_shorting]
sources:
  - {title: "Chart Fanatics — Alex’s First Red Day Trading Strategy", url: "https://www.chartfanatics.com/strategies/first-red-day", tier: T2}
status: verified-t2
---

# Alex Temiz — First Red Day Strategy (stocks/options, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/first-red-day. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook is credited to "Alex" and links to his Chart Academy instructor profile (https://www.chartacademy.com/instructors/alex-temiz). It describes shorting overextended multi-day runners on their first red day, intraday, in stocks or options. The page gives no other biography.

## Built for

- **Instruments:** stocks, and options on the same names when the options are liquid.
- **Style:** day trading. A small runner can be held for further weakness over following days.
- **Timeframes:** daily chart to qualify the multi-day run. Intraday to trigger against the previous day's close.
- **Session / time window:** the open of the First Red Day (gap up or gap down) and the intraday session after it. The page names no exchange, market hours or other window.

## Core idea

Stocks that go parabolic over several days tend to come back down. The first day the stock trades red versus the prior close is when momentum shifts, late buyers get trapped, and the drop can be fast and large. The previous day's close (the "red-to-green line") is the whole trade: below it the setup is live, and a reclaim and hold above it invalidates it. The page says the edge persists because greed and chasing at the top repeat. Extended stocks also often sell new shares in dilutive offerings, which adds supply.

## Rules

1. **Qualify the run.** The stock must be up big for **at least three consecutive days**, ideally each day stronger than the last. The move must be parabolic, extended and hyped, not a slow trend. One or two green days is not enough.
2. **Don't anticipate.** Never short just because it "should" come down. The stock has to go red first.
3. **Mark the previous day's close.** This is the key level. The trade doesn't start until price trades below it.
4. **Scenario A: gap up (the best case).** If the stock pushes higher at the open and then fades, enter when it breaks under the previous close.
5. **Scenario B: gap down.** Watch for a bounce back toward the previous close. Enter when that bounce fails and rejects the level.
6. **Starter and add.**
   - An optional small starter can go on when weakness is building. In the SMCI example, the starter went on an early break below the low of day.
   - Main size goes on only when the break below the previous close confirms.
7. **Stop.** If price reclaims the previous close and holds above it, the setup is invalid. Cut immediately.
8. **Take partial profits** by covering portions into the flush.
9. **Re-entry.** If a bounce comes but stays under the previous close, re-enter or add when the bounce fails.
10. **Hold a runner.** When momentum is clearly broken, keep a small portion for further downside. Rolled-over runners often stay weak for days or weeks.

## Risk management

- **Invalidation:** a reclaim of the previous day's close that holds above it. Exit immediately; don't hold and hope.
- **Sizing:** start small and add main size only on confirmation. Don't go too big too soon, because the edge relies on having room to scale in at the right spot.
- **Risk per trade:** Not specified in the playbook (no $ or % figure, and no tick or price buffer around the prior close).
- **Daily / weekly limits:** Not specified in the playbook.
- **Profit protection:** partial covers into the drop. Only a small portion is held as a runner.

## What the playbook leaves unspecified

- What "up big" means: a minimum % per day or in total, plus price, float, market-cap or volume filters.
- How long, or by how much, price must "hold" above the prior close before the stop is triggered.
- Where partial profits are taken (no targets such as VWAP, gap fill or % levels) and when the runner is finally covered.
- Short-sale practicalities: borrow and locate availability, halts, and squeeze risk.
- Options details: strike, expiry, and how to handle implied-volatility collapse.
- A wording ambiguity. One rule says main size goes on when price confirms "the break below red to green". The setup is consistently described as a break *below the previous close* (the red-to-green line), so that is the reading used here.
- A second wording ambiguity. The overview defines the setup as the first day the stock *closes* red, but the rules and the SMCI example trigger intraday once price trades below the previous close. The page doesn't reconcile the two.

## Evidence & claims

- **SMCI example:** after a gap up following a multi-day run, a starter went on at the break of the low of day and main size at the break of the previous close. Price then fell about $30 per share quickly, and partials were covered into the drop. The reported profit was about $50,000. Self-reported (T4).
- The page gives no win rate, R multiple, position size or risk amount, so no expectancy or R calculation is possible.
- The claims that the setup works in any market condition and is easy to execute are qualitative (T4).
- The page also notes that clean setups can be weeks or months apart, and that gap-down versions sometimes leave less room if you wait too long.

## Concepts & lineage

- The prior close as the red-to-green line, broken from above or rejected on a bounce: [[concept_support_resistance]], [[concept_price_action]]
- Parabolic multi-day extensions reverting once momentum fails: [[concept_mean_reversion]]
- Greed, FOMO, trapped late buyers and panic selling as the driver: [[concept_market_sentiment]]
- Starter-and-add scaling and keeping room to add: [[concept_position_sizing]]
- Partial covers into the flush, re-entries on failed bounces, a small runner: [[concept_trade_management]]
