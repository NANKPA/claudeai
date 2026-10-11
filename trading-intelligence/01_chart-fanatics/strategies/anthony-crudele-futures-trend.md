---
id: strategy_anthony_crudele_futures_trend
type: strategy
title: "Anthony Crudele — Futures Trend Trading Strategy: Bollinger Band Environments (index futures, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Anthony Crudele’s Futures Trend Trading Strategy", Crudele Bollinger environment model, consolidation-expansion-mean reversion framework, Beacon mean-reversion levels]
taught_by: [person_anthony_crudele]
featured_in: [channel_chart_fanatics]
uses: [concept_bollinger_bands, concept_volatility, concept_market_regimes, concept_trend_following, concept_breakout_trading, concept_mean_reversion, concept_support_resistance, concept_liquidity_sweep_reversal, concept_fibonacci, concept_multi_timeframe_analysis, concept_moving_averages, concept_vwap, concept_oscillators_momentum, concept_options_greeks, concept_position_sizing, concept_trade_management]
derived_from: [concept_bollinger_bands, concept_market_regimes]
related: [strategy_ted_zhang_stage_analysis, strategy_brando_options_swing]
sources:
  - {title: "Chart Fanatics — Anthony Crudele’s Futures Trend Trading Strategy", url: "https://www.chartfanatics.com/strategies/futures-trading-strategy", tier: T2}
status: verified-t2
---

# Anthony Crudele — Futures Trend Trading Strategy: Bollinger Band Environments (index futures, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/futures-trading-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Anthony Crudele swing trades index futures, often through options
on futures. He starts every day by classifying the market environment on
the daily chart, using Bollinger Bands and his own "Beacon" levels tool.

## Built for

- **Instruments:** futures, mainly index markets (**S&P, Nasdaq,
  Russell**). **Options on futures** are often the position vehicle.
- **Style:** swing trading, with a **1 to 5 trading day** hold. Intraday
  execution is sometimes used to refine entries.
- **Timeframes:** the **daily** chart comes first and defines everything.
  **60-minute and 30-minute** charts, and sometimes **3-minute**, are used
  only to refine entries, mainly in consolidation.
- **Indicators:** **Bollinger Bands (20, 3 standard deviations)** are
  required. **Beacon** is Anthony's tool that auto-draws mean-reversion
  Fibonacci levels between Bollinger Band peaks. **8/21/34 moving
  averages** give trend and exit context. **RSI** is optional, only to
  confirm overbought or oversold during mean reversion. **Anchored VWAP**
  is used in extreme volatility. The page lists the moving averages, RSI
  and anchored VWAP as tools not used for entries.
- **Session or time window:** not specified.

## Core idea

Identify the environment before looking for any setup. On the daily chart,
Bollinger Bands set to 3 standard deviations sort the market into
**consolidation** (bands contracting, two-way tape), **expansion** (bands
turning outward, one-directional trend) or **mean reversion** (bands
contracting after a peak, a pullback against the main trend). Each
environment sets a posture. In consolidation, trade the edges and avoid the
middle. In expansion, trade one direction only. In mean reversion, trade
the pullback to a defined 50% target, with smaller size against the main
trend. Only then drop to lower timeframes for execution.

## Rules

1. **Daily process (stated as non-negotiable).** Open the daily chart and
   read the 20-period, 3-standard-deviation Bollinger Bands:
   - **Contracting** → consolidation.
   - **Expanding** → trend or expansion.
   - **Contracting after a peak, with Beacon levels drawn** → mean
     reversion.
   Set the posture, and only then go to a lower timeframe.
2. **Consolidation (two-way tape).** The bands narrow and price becomes
   range-bound, often after a meaningful high or low. Expect false
   breakouts and stop runs past recent highs and lows that snap back into
   the range.
   - Go long or short **at the range edges only**. Never trade the middle.
   - Drop to **60-minute, 30-minute or 3-minute** charts, because
     short-term technicals matter more here.
   - Be selective. This environment chops up swing traders most.
3. **Expansion (one direction only).** The bands turn from flat to
   outward, price touches the upper band (uptrend) or lower band
   (downtrend), and the move usually begins with a breakout from the prior
   range.
   - **Bullish expansion:** long only, with no fading rallies.
   - **Bearish expansion:** short only, with no buying dips.
   - **Entry:** after the breakout or confirmation. Manage it as trend
     continuation.
   - **Targets:** larger-timeframe levels (weekly highs and lows, major
     reference points) and **"unfinished business"**: a prior Bollinger
     Band peak becomes the objective in the next directional move.
   - **Vehicle:** usually **options on futures**, calls or puts about **3
     to 5 days out**, scaled out into targets.
4. **Mean reversion (the pullback phase).** After an expansion, price stops
   extending and the bands start contracting. The method does not try to
   catch the exact top or bottom. Posture changes: after an up-expansion,
   **you are no longer long**. Trading against the main trend is allowed,
   but at **smaller size**.
   - **Levels:** Beacon applies Fibonacci-style levels to the
     **Bollinger Band peak-to-peak move** (a "fib on volatility", not on
     price) at **30%, 50% and 70%**.
   - **Bearish trigger:** a **daily close below the 30% line**. The target
     becomes the **50% line**.
   - **Action:** buy puts or short futures, and stay in until a daily
     close back above the relevant level.
   - **Exit:** once **50%** is hit, the mean-reversion objective is done.
5. **After 50% is hit: "hands in pocket."** Price may chop and consolidate
   or start a new expansion. Wait until the environment is clear again.
6. **Execution refinements.** Entries are not one-candle signals. Use
   lower-timeframe structure or order-flow tools to improve fills after
   the environment and direction are set. RSI may confirm an overbought or
   oversold condition in mean reversion but never triggers a trade.
7. **Exits and management.** The page says targets, exits and stops are
   the hardest part. Use the **8/21/34 moving averages** for exit context.
   In extreme volatility, **anchor VWAP** to the candle or level where the
   tape turned (a key high or low), and use **VWAP ±1, 2 and 3 standard
   deviation** bands as trim and exit guides. The bear-case question is
   whether price can stay below VWAP.

## Risk management

- **Sizing:** risk is managed **in dollars**, not one fixed contract. A
  wider stop means a smaller position. Sizing is called the biggest area of
  discretion.
- **Counter-trend trades:** mean-reversion trades against the main trend
  use smaller size.
- **Futures versus options:** if the correct stop (for example, above a key
  high after a gap) is too wide for futures, use **options** instead,
  often **out-of-the-money** calls or puts, so the premium caps the risk.
- **Stops:** at the structural level (above a key high or below a key low),
  or for mean-reversion futures shorts, a daily close back above the
  relevant Beacon level.
- **No-trade:** after the 50% target, or whenever the environment is
  unclear, stand aside. The page says that sometimes the correct trade is
  no trade.
- **Risk per trade ($ or % of account) and daily or weekly loss limits:**
  not specified in the playbook.

## What the playbook leaves unspecified

- An objective test for "contracting" versus "expanding" bands (bandwidth
  thresholds or slope rules) and for when consolidation turns into
  expansion.
- How Beacon chooses the two Bollinger peaks, and which band (upper,
  lower, or both) the peak-to-peak move uses. The tool is proprietary.
- The bullish mean-reversion mirror (after a down-expansion). Only the
  bearish trigger and target are written out.
- What role the **70%** level plays. It is listed but never used in a rule.
- Exact entry triggers in expansion ("after breakout or confirmation") and
  at consolidation edges.
- Options specifics beyond 3 to 5 days out and OTM: strike choice, sizing
  in premium, and when to roll or exit on time.
- Account-level risk limits and how many index markets to hold at once.
- How news and gaps are handled, beyond switching to options. The page
  lists news and volatility disrupting structure as a con.

## Evidence & claims

- The page gives **no win rate, R:R, P&L or payout**. No expectancy check is
  possible.
- The listed pros (easy to understand, less overtrading, avoids fading
  strong trends, works in bull and bear markets) are qualitative claims.
  Self-reported (T4).
- **Trade breakdown (bearish expansion into mean reversion):** a year-long
  downtrend, a band contraction, then a downside expansion that made the
  trade short-only. A gap and an extreme range made the proper stop above
  the key high too wide for futures, so out-of-the-money puts were bought.
  The page reports no outcome figure.

## Concepts & lineage

- 20-period, 3-standard-deviation Bollinger Bands to classify the
  environment → [[concept_bollinger_bands]], [[concept_volatility]]
- Consolidation, expansion and mean reversion as distinct regimes with
  their own posture → [[concept_market_regimes]]
- One-direction-only trading in expansion, launched from a range breakout
  → [[concept_trend_following]], [[concept_breakout_trading]]
- Fading range edges, and stop runs that snap back into the range →
  [[concept_support_resistance]], [[concept_liquidity_sweep_reversal]]
- Mean-reversion pullback to the 50% Beacon level →
  [[concept_mean_reversion]], [[concept_fibonacci]]
- Daily environment with 60, 30 and 3-minute execution →
  [[concept_multi_timeframe_analysis]]
- 8/21/34 moving averages for exit context → [[concept_moving_averages]]
- Anchored VWAP with standard-deviation bands for trims in high
  volatility → [[concept_vwap]]
- RSI only as an overbought or oversold confirmation →
  [[concept_oscillators_momentum]]
- Short-dated OTM options on futures as a defined-risk vehicle →
  [[concept_options_greeks]]
- Dollar-risk sizing, smaller counter-trend size, scaling out →
  [[concept_position_sizing]], [[concept_trade_management]]
