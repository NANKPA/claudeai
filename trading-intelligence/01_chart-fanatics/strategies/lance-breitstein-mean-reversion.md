---
id: strategy_lance_breitstein_mean_reversion
type: strategy
title: "Lance Breitstein — Capitulation Mean Reversion (stocks, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Lance Mean Reversion Trading Strategy, capitulation reversal, right-side reversal, blow-off top fade]
taught_by: [person_lance_breitstein]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_expectancy, concept_volatility, concept_bollinger_bands, concept_moving_averages, concept_market_sentiment, concept_multi_timeframe_analysis, concept_market_structure, concept_price_action, concept_trade_management, concept_position_sizing]
derived_from: [concept_mean_reversion, concept_random_walk_efficient_markets]
related: [strategy_marios_stamatoudis_parabolic_short, strategy_kris_verma_shorting, strategy_jj_simon_fair_pricing]
sources:
  - {title: "Chart Fanatics — Lance Mean Reversion Trading Strategy", url: "https://www.chartfanatics.com/strategies/mean-reversion-strategy", tier: T2}
status: verified-t2
---

# Lance Breitstein — Capitulation Mean Reversion (stocks, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/mean-reversion-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Lance Breitstein is presented as the author of a
capitulation-reversal day-trading method for stocks. The playbook gives no
further biography. It teaches the method through two stock examples, OCLR
(October 2016) and KODK.

## Built for

- **Instruments:** stocks.
- **Style:** day trading.
- **Timeframes:** the daily chart judges whether a move is abnormal for that
  stock. The intraday chart (bar length not given) locates the capitulation,
  the reversal signal and the entry.
- **Session / time window:** not specified.

## Core idea

Most of the time markets sit near equilibrium. Panic, forced liquidation or
a sudden swing in sentiment can occasionally throw price far from it, fast.
The trader scores how extreme the move is and waits for proof that it has
turned, trading what the page calls "the right side of the reversal". The
goal is the first retracement toward equilibrium, with the **20-period
moving average** (the Bollinger Band midline) as the reference. Every trade
is judged on expected value, **EV = (win rate × reward) − (loss probability
× risk)**. A good setup raises the odds of a reversal, offers a large
reward because price is far from equilibrium, and has a clearly defined
risk.

## Rules

1. **Scan for extremes.** Look for stocks trading outside the Bollinger
   Bands, moving several days in one direction, expanding in range sharply,
   or trading on unusually high volume. Trade whichever shows the strongest
   setup.
2. **Score the move.** The more of these conditions line up, the stronger
   the setup:
   - a **large** move;
   - a **fast** move, over minutes or hours rather than months;
   - **no fundamental change**. A move without major new information is
     more likely to be temporary, while real news may have shifted
     equilibrium;
   - many **consecutive bars or days** in one direction, on any timeframe;
   - **forced flows**: margin calls, liquidations, short covering,
     redemptions;
   - a **sentiment extreme**, euphoric or despairing;
   - a **normally stable** asset that suddenly turns extremely volatile.
     This is the ideal case;
   - a **quantifiable value anchor**, such as bonds at maturity or cash
     flows, which can make the reversion more reliable.
3. **Confirm capitulation.** Price accelerates, candles grow large compared
   with normal ranges, **volume spikes**, and price stretches far from its
   moving averages. Check the daily chart to confirm the move is abnormal
   for this stock.
4. **Entry trigger: wait for the turn, never the falling knife.**
   - *Long after a decline* that kept respecting the prior bar's highs:
     buy the **break of the prior bar's high**.
   - *Short after a rally* that kept respecting the prior bar's lows: sell
     the **break of the prior bar's low**.
   - *Structure shift:* lower highs and lower lows turn into higher highs
     and higher lows, or the reverse.
   - *Extreme single-candle panic reversal:* you may enter while the candle
     is reversing, but at **smaller size** because the risk is less clearly
     defined.
5. **Stop.** Where the idea is invalid: below the low of the capitulation,
   where the reversal structure fails, or where higher lows break. For a
   short, above the high of the parabolic move.
6. **Target.** The first bounce toward the **20-period MA**. Expect only a
   partial retracement, not a return to the prior highs.
7. **Manage.** Trail the stop under each prior bar's low (longs) or over
   each prior bar's high (shorts).
8. **Size by quality.** Strong setups (extreme displacement, fast
   acceleration, a big volume spike, large distance from equilibrium, clean
   structure, several legs) can be traded larger. Weaker ones go smaller or
   are skipped.

**Worked examples.**
- *OCLR, Oct 27 2016 (long):* a slow decline after the open sped up into a
  capitulation of about 20 to 25%. The stock normally moved about 30 cents
  a day but was now moving about 30 cents a bar, and volume spiked. Entry
  on the prior-bar-high break at about $7.25, stop under the low at about
  $7.00, trailed under bar lows, exit about $7.57 near the 20-period MA.
- *KODK (short):* a news-driven parabolic rally on a government loan
  programme turned into a blow-off. Short on the break of the prior bar's
  low, stop above the parabolic high, trail above bar highs, cover into the
  first pullback. No prices are given.

## Risk management

- **Stop:** always at the structural invalidation point (capitulation low
  or high, or the failed reversal structure).
- **Sizing:** scaled to setup quality. Single-candle panic entries use
  smaller size.
- **Shorts:** need **extra risk management**, because a short's loss is
  theoretically unlimited while a long's is capped at zero.
- **Risk per trade (% or $):** not specified in the playbook.
- **Daily or weekly limits:** not specified in the playbook.

## What the playbook leaves unspecified

- Thresholds for "large", "fast", "high volume" and "far from the MA". No
  ATR multiple, % move, relative volume or Bollinger setting is given
  beyond the 20-period midline.
- How many conditions must line up before a trade is taken, or how they are
  weighted.
- The intraday bar length (the examples suggest a fixed intraday chart but
  never name it).
- When to exit if price stalls before the 20-period MA, and whether to take
  partials.
- How to tell news that changes equilibrium from news that does not. KODK
  was news-driven yet still faded.
- Any rules on stock universe, liquidity, short borrow, or time of day.

## Evidence & claims

- The page gives **no win rate, average R, P&L or payout claim**. It gives
  only the EV formula as a way of thinking.
- The OCLR example implies (my arithmetic from the stated prices) a reward
  of about $0.32 against risk of about $0.25, roughly **1.3R**. It is a
  single self-reported trade (T4), not a statistic.
- With no stated win rate, no expectancy check is possible. The page claims
  a "higher probability" of reversal only qualitatively.

## Concepts & lineage

- Price returning to equilibrium after an overshoot →
  [[concept_mean_reversion]]
- Markets "generally efficient", with temporary dislocations from panic or
  forced flows → [[concept_random_walk_efficient_markets]]
- Choosing trades by expected value (probability, reward, risk) →
  [[concept_expectancy]]
- Volatility expanding against the stock's normal range (30 cents a day
  becoming 30 cents a bar) → [[concept_volatility]]
- Scanning outside the Bands and targeting the 20-period midline →
  [[concept_bollinger_bands]], [[concept_moving_averages]]
- Sentiment extremes and emotional capitulation → [[concept_market_sentiment]]
- Daily context with an intraday trigger → [[concept_multi_timeframe_analysis]]
- Prior-bar breaks and the LH/LL to HH/HL shift as triggers →
  [[concept_market_structure]], [[concept_price_action]]
- Trailing stops on prior bars → [[concept_trade_management]]
- Sizing by setup quality → [[concept_position_sizing]]
