---
id: strategy_dhesi_liquidity_inversion
type: strategy
title: "Dhesi — Liquidity Inversion Model: Sweep, FVG Inversion & LTF Confirmation (NQ/ES futures, day trading/swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Liquidity Inversion Model, Dhesi Trades model, FVG inversion model, Dhesi liquidity inversion]
taught_by: [person_dhesi]
featured_in: [channel_chart_fanatics]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_fair_value_gap, concept_order_blocks_breakers, concept_market_structure, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_volatility, concept_smt_divergence, concept_trendlines, concept_trade_management, concept_position_sizing, concept_risk_reward_r_multiples, concept_trading_psychology]
derived_from: [concept_smart_money_concepts, concept_fair_value_gap]
related: [strategy_candace_lau_nq_sweep_reversal, strategy_jadecap_liquidity_volatility, strategy_marco_trades_liquidity_grab]
sources:
  - {title: "Chart Fanatics — Dhesi - Liquidity Inversion Model", url: "https://www.chartfanatics.com/strategies/liquidity-inversion-model", tier: T2}
status: verified-t2
---

# Dhesi — Liquidity Inversion Model: Sweep, FVG Inversion & LTF Confirmation (NQ/ES futures, day trading/swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/liquidity-inversion-model. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Dhesi (Dhesi Trades) trades NQ and ES futures and prefers NQ
for its intraday range. He uses one ICT-style model for day trades, swings
and longer-dated positions.

## Built for

- **Instruments:** the page header says futures and forex. The body is
  built around **NQ and ES**, with NQ preferred. Other liquid markets are
  allowed in principle, but the page advises proving the model before
  watching many tickers.
- **Style:** day trading and swing trading. The page also mentions scalps
  and long-dated option (LEAPS) positions built from the same logic.
- **Timeframes:** monthly, daily, 4H, 1H, 15m, 5m and 1m. Day-trade entries
  are refined on the **15m, 5m or 1m**. Swing entries need **1H or higher**
  confirmation, preferably 4H and daily.
- **Session:** New York, built around the **10:00 a.m. ET four-hour candle
  open**. Moves before 10:00 are treated as noisy.
- **Skill level:** assumes the trader already knows ICT-style tools: draws
  on liquidity, FVGs, inversion FVGs, PD arrays, order blocks, balanced
  price ranges, and session, monthly and equal highs and lows.

## Core idea

Start from where liquidity sits. Wait for price to sweep or tap it, then
require a **fair value gap inversion**: the gap that supported the move
into the liquidity gets violated and starts acting from the other side.
That higher-timeframe inversion defines the setup. A day-trade entry also
needs a pullback into a PD array from the new move, followed by a
lower-timeframe inversion in the trade direction. Take a technical partial
and let a runner work when volatility expands.

## Rules

1. **Mark the draws on liquidity.** Monthly highs and lows come first
   because they tend to give the strongest reactions. Then session highs
   and lows, equal highs and lows, the new week opening gap, unfilled FVGs,
   and easy-to-reach pools such as a cluster of trendline lows.
2. **Stay reactive.** Do not fix a bias before price reaches the area.
   React to what it does there.
3. **Check volatility.** The full model is for expanded volatility, when
   liquidity is being hit with force. Downside NQ moves are singled out as
   the best case. In dead volatility, do not trade it aggressively; base
   hits are fine.
4. **Time it (day trades).** Let the 10:00 a.m. ET four-hour candle
   reveal what price is doing at the key area (a sweep, a gap tap, or a
   rejection from a higher-timeframe PD array) before committing.
5. **Sweep and fast inversion.** After the sweep, price should react fast
   and violate the relevant FVG within the next few candles, **often two or
   three**. Bearish: a bullish FVG breaks and turns into resistance.
   Bullish: a bearish FVG breaks and turns into support. If price lingers
   inside the gap, the setup loses urgency. If price respects the gap and
   continues, there is no reversal.
6. **Lower-timeframe confirmation (day trades).** Wait for a retracement
   into a PD array (FVG or order block) created by the new move. The
   retracement is not the entry. The entry comes when the counter-direction
   lower-timeframe structures formed during that retracement are broken and
   inverted. If an order block and an FVG are stacked, wait for both to be
   violated.
7. **Swing entries use 1H or higher.** Never enter a swing from the 15m, 5m
   or 1m chart.
8. **Do not chase.** The big displacement candle shows the idea; the
   pullback and inversion give the risk. A bare 4H FVG tap is not a
   day-trade entry when the resulting stop is too large for your account;
   wait for confirmation.
9. **Optional SMT.** ES against NQ divergence adds confidence but is not
   required.
10. **Stop where the chart is wrong.** For a bearish day trade, above the
    current 15-minute high or the lower-timeframe high that formed before
    the inversion. For a bullish continuation, below the low that should
    hold if the FVG reaction is real.
11. **Targets come from the chart.** Use local highs and lows, session
    highs and lows, unfilled hourly or daily FVGs, daily or weekly gaps,
    equal highs and lows, and stacked liquidity. Never set targets from
    dollar goals or arbitrary point counts.
12. **Manage.** Typically trim **50%** at the first technical target and move the
    stop to **breakeven**. Let the runner work toward the higher-timeframe
    draw. A runner stopped at breakeven still counts as a successful trade.
13. **One clean attempt.** A missed entry is not chased; the next chance
    comes with a later session or a fresh four-hour candle. No averaging or compounding
    into trades, except in rare high-conviction higher-timeframe setups.
14. **Daily stop rule.** Two losses end the day. One win and one loss allow
    a third attempt, but only if the setup appears again.

**Entry variants on the page**

- *Bearish reversal after a buy-side sweep:* price runs buy-side liquidity
  (monthly high, session high or equal highs), rejects and inverts the supporting
  FVG or PD array. Then enter on the lower-timeframe pullback and
  inversion. Stop above the protected high. First target is the nearest
  sell-side liquidity, with runners toward larger stacked liquidity.
- *Bullish continuation into equal highs:* the market is already expanding
  higher with an open higher-timeframe FVG below. Wait for the tap, a
  bullish reaction and a lower-timeframe inversion. In the NQ example the
  target pool was a set of **relative equal highs at 26,100**; entry came
  from a 4H FVG tap and a 1-minute inversion.
- *Higher-timeframe reversal for swings and LEAPS:* identical steps,
  applied to monthly and daily charts. The example is NQ reacting from a monthly FVG
  and order block during the tariff-driven pullback. The monthly gap
  inverted back up, which confirmed longer-term longs and gave a clear
  bias for day trades.

## Risk management

- **Per-trade risk:** a fixed dollar or % figure is not specified in the
  playbook. Hold the same dollar risk and change the size: when high
  volatility puts the structural stop **40–50 NQ points** from entry, cut
  contracts rather than pull the stop to an arbitrary level.
- **Stop placement:** structural, beyond the protected high or low.
  Discomfort with the dollar amount is not a reason to move it.
- **Daily limit:** **two losses end the day**. A win followed by a loss
  allows one more attempt.
- **Weekly limit:** not specified in the playbook.
- **Scaling:** no adding or averaging, apart from rare high-conviction
  higher-timeframe trades.
- **Swing versus day risk:** swings can carry wider stops because their
  objective is larger. Day trades need confirmation that tightens the
  stop.

## What the playbook leaves unspecified

- A dollar or % risk per trade, and a maximum number of trades beyond the
  two-loss rule.
- Which timeframe the "two or three candles" inversion window is counted
  on.
- An objective test for "expanded" versus "dead" volatility.
- How to choose between the 15m, 5m and 1m for a given entry.
- How to grade competing PD arrays, or which one counts as "the" relevant
  FVG.
- How to manage the runner after breakeven (trail or fixed target), and
  whether day trades must close by a set time.
- Forex specifics such as pairs or sessions. The header lists forex, but
  every example is NQ or ES.
- A minimum R:R. The page mentions 1:1.5 and 1:2 ideas that runners can
  extend, but sets no floor.
- Any win rate or trade sample.

## Evidence & claims

- **No win rate, P&L or payout** is reported.
- On volatile NQ down-moves, the page says "a 50-point idea can become a
  200-point opportunity". Self-reported (T4).
- Runners are said to stretch a 1:1.5 or 1:2 trade into a far bigger
  multiple. Self-reported (T4). Both describe trade design, not measured
  results.
- **Worked examples** (no R or dollar results given): the November NQ
  reversal (a swing short from the daily-FVG inversion with an hourly
  entry, and a New York day short after a 10:00 a.m. sweep of equal highs,
  targeting the 9:30 a.m. session low); the 26,100 equal-highs
  continuation; and the monthly-FVG reversal during the tariff pullback.
- Without a win rate, no expectancy check is possible. By simple
  arithmetic (not stated on the page), the break-even win rate would be
  40% at 1:1.5 and about 33% at 1:2.

## Concepts & lineage

- Monthly, session and equal highs and lows, NWOG and unfilled gaps as
  draws → [[concept_liquidity]]
- Stacked trendline lows as low-resistance liquidity →
  [[concept_trendlines]]
- Sweep, rejection, then confirmed reversal →
  [[concept_liquidity_sweep_reversal]]
- FVG inversion as the trigger at both higher and lower timeframes →
  [[concept_fair_value_gap]]
- Order blocks as PD arrays in the retracement →
  [[concept_order_blocks_breakers]]
- Displacement and violation of protected highs and lows →
  [[concept_market_structure]]
- Monthly-to-1-minute stack, with swing versus day-trade timeframe rules →
  [[concept_multi_timeframe_analysis]]
- The 10:00 a.m. ET four-hour candle in New York →
  [[concept_trading_sessions_killzones]]
- Volatility as a quality filter → [[concept_volatility]]
- ES against NQ as optional confluence → [[concept_smt_divergence]]
- 50% at the first technical target, breakeven, runner →
  [[concept_trade_management]], [[concept_risk_reward_r_multiples]]
- Size down to keep a structural stop → [[concept_position_sizing]]
- Two-loss rule to stop revenge trading → [[concept_trading_psychology]]
- Lineage: ICT-style smart-money concepts → [[concept_smart_money_concepts]]
