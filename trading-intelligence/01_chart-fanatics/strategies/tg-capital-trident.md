---
id: strategy_tg_capital_trident
type: strategy
title: "TG Capital — London Session Trident Strategy (forex, gold and futures, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Trident Pattern, TG Capital Trident, unique high RR, London session swing strategy, "1:20 RR strategy"]
taught_by: [person_tg_capital]
featured_in: [channel_chart_fanatics]
uses: [concept_trading_sessions_killzones, concept_fair_value_gap, concept_moving_averages, concept_multi_timeframe_analysis, concept_candlestick_patterns, concept_trend_following, concept_market_regimes, concept_trade_management, concept_risk_reward_r_multiples, concept_prop_firm_risk_rules]
derived_from: [concept_smart_money_concepts]
related: [strategy_nbb_trader_po3_ote_adr, strategy_jadecap_liquidity_volatility]
sources:
  - {title: "Chart Fanatics — TG's Capital London Session Swing Trading Strategy", url: "https://www.chartfanatics.com/strategies/unique-high-rr", tier: T2}
  - {title: "TradeZella — TG Capital London Session Strategy", url: "https://www.tradezella.com/strategies/unique-high-rr", tier: T3}
  - {title: "TradingView — TG Capital Trident Strategy [Long + Short] (third-party script)", url: "https://www.tradingview.com/script/nFdphVub-TG-Capital-Trident-Strategy-Long-Short/", tier: T3}
  - {title: "TakeProfit — Reverse-Engineering a Public 1:20 RR Strategy: Chart Fanatics & TG Capital", url: "https://takeprofit.com/posts/reverse-engineering-a-public-1-20-rr-strategy-chart-fanatics-tg-capital-51", tier: T3}
status: verified-t2
---

# TG Capital — London Session Trident Strategy (forex, gold and futures, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/unique-high-rr. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** According to the earlier search-based note (T3; not in the playbook), TG Capital is the trader in the Chart Fanatics video *"STEAL This INSANE Simple 90% Win Rate Trading Strategy (1:20+ RR)"*. The numbers in that title are T4. The playbook gives no biography.

## Built for

- **Instruments:** futures and forex.
  - Valid pairs: USDJPY, EURUSD, GBPUSD, NZDUSD, USDCAD and gold (XAUUSD).
  - The page says it is especially strong on gold and Nasdaq, and favours longs on naturally bullish assets, but the model works in both directions.
- **Style:** swing trading. Entries are intraday, and trades are held as long as the daily trend lasts.
- **Timeframes:** the 30-minute chart is the only chart used for entries. The daily chart sets bias and take-profit levels.
- **Session / time window:** the London kill zone, **3:00–6:30 AM New York time**. All entries must fall inside it. The FVG itself must form between **2:30 and 4:00 AM**.

## Core idea

The trader waits in a narrow London window for the "Trident" pattern, and only when trend filters agree. The pattern has three parts:

1. a clean 3-candle fair value gap on the 30-minute chart;
2. a small-bodied doji whose wick reaches the gap's 50% level (consequent encroachment);
3. a confirmation candle.

The filters are a 200 EMA directional bias and a clean 5/9/13(15)/21 EMA stack. The trade is then held for daily-chart trend continuation, aiming for a large reward relative to a tight stop. The page favours quality over quantity, and setups can be rare.

## Rules

1. **Bias.** Above the 200 EMA, longs only. Below it, shorts only. Daily structure must agree. A "Bull Trading Candle Strength" indicator on the daily chart confirms momentum: green is strong bullish, blue mild bullish, red strong bearish, black mild bearish.
2. **Trend filter.** The 5, 9, 13 (or 15) and 21 EMAs must be clearly stacked in the trade direction. If they cross or tangle, the setup is invalid.
3. **Time filter.** Only consider entries between 3:00 and 6:30 AM New York time.
4. **Fair value gap.** A clean 3-candle FVG must form on the 30-minute chart between 2:30 and 4:00 AM. Ignore FVGs outside the window.
5. **Mark the 50% level** of the FVG (consequent encroachment).
6. **Trident candle.** The next candle must be a small-bodied doji whose wick reaches into the 50% zone, showing that a push into the gap was rejected.
7. **Confirmation candle.** As written on the page, the candle after the doji must close *below* the doji high; a close above it invalidates the trade. (See the gaps section.)
8. **Entry.** Enter at market on the confirmation candle (the example entered right after it closed). If early, place a limit at the FVG's 50% level instead.
9. **Stop.** Below the low of the candle that forms the FVG. **Gold exception:** no hard stop. A closing-candle filter is used instead, because, according to the page's backtests, gold often makes deep liquidity wicks before running.
10. **Take profit.** Use daily structure to guide take-profit levels and ride the trend while it lasts.
11. **Early exit.** Consider closing if the EMAs start to reverse, or if a significant opposing candle invalidates the structure.

## Risk management

- **Stop:** below the FVG-candle low. Gold uses a close-based stop instead of a hard stop.
- **Risk per trade:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook. Exposure is limited by time instead: at most 3.5 hours of trading per day, and setups may come only a handful of times per year.
- **Prop-firm caveat:** the page says the model needs a fully balance-based prop-firm drawdown model. A hybrid or equity-based drawdown can end trades, because open P&L swings widely (for example +10R falling back to +5R).
- **Psychology:** you must be able to sit through long gaps between setups and through large open-profit swings.

## What the playbook leaves unspecified

- **EMA timeframe:** which timeframe the 200 EMA and the EMA stack are read on (30-minute or daily). The worked example doesn't say.
- **Internal inconsistencies:**
  - The FVG window starts at 2:30 AM, before the 3:00 AM kill zone opens.
  - For a long, the confirmation rule (close below the doji high, or the trade is invalid) reads as inverted relative to the bullish story it describes. It needs clarifying before any test.
- **Pattern definitions:** minimum FVG size, how small a doji's body must be, and how far into the 50% zone the wick must reach.
- **Indicator:** the formula behind the "Bull Trading Candle Strength" indicator.
- **Gold stop:** which timeframe's close triggers it, and the maximum loss allowed.
- **Exits:** no fixed R target. The 1:20 figure comes from the video title and third-party material, not the playbook. "Daily structure" exits aren't defined.
- **Other mechanics:** position limits (for example one trade at a time), short-side mirror details, risk per trade.

## Evidence & claims

- **Win rate:** about 90% "when all rules are followed". Self-reported (T4), on the T2 page.
- **Reward size:** described as high risk-to-reward, with open P&L swings such as +10R back to +5R. Self-reported (T4).
- **Kill-zone choice:** said to rest on years of backtesting. No data shown (T4).
- **Video title:** claims a 90% win rate at 1:20+ RR (T4).
  - Expectancy check: E = 0.9 × 20 − 0.1 = **+17.9R per trade**, which is implausible.
  - Even at 1:5, E = 0.9 × 5 − 0.1 = +4.4R.
  - Win rate and R:R that high almost never coexist.
- **Independent EA re-test** (TakeProfit, EURUSD M30, T3): about a **20% win rate** with many large winners, profitable out-of-sample in 2023–24. At a 20% win rate, break-even R:R is 4:1. This contradicts the 90% headline but is consistent with a positive-skew trend edge.
- **Third-party TradingView script** (T3): uses a 1:20 minimum target, exits if the EMA stack breaks or price closes through the stop, and holds one position at a time. These are that script's choices, not playbook rules.
- **Sample size:** only a handful of setups per year means a 90% win rate can't be verified from any realistic personal sample.

## Concepts & lineage

- London kill zone (3:00–6:30 AM NY) and FVG formation window: [[concept_trading_sessions_killzones]]
- 3-candle FVG and its 50% consequent encroachment: [[concept_fair_value_gap]]
- Doji "Trident" plus confirmation candle: [[concept_candlestick_patterns]]
- 200 EMA bias and 5/9/13(15)/21 EMA stack: [[concept_moving_averages]], [[concept_trend_following]]
- Tangled EMAs mean no trend, so no trade: [[concept_market_regimes]]
- 30-minute entries with daily bias and targets: [[concept_multi_timeframe_analysis]]
- Holding winners for large R, and EMA-reversal exits: [[concept_trade_management]], [[concept_risk_reward_r_multiples]]
- Balance-based vs equity-based prop drawdown rules: [[concept_prop_firm_risk_rules]]
- The FVG and kill-zone vocabulary comes from ICT / smart-money concepts: [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **Confirmed:**
  - the London kill zone of 3:00–6:30 AM New York time;
  - daily bias and targets with 30-minute entries;
  - the 5/9/13(15)/21 EMA stack, invalid when tangled;
  - the Trident definition (FVG + doji wick into its midpoint + confirmation candle).
- **Added:** the 200 EMA long-only/short-only filter, the daily candle-strength indicator, the 2:30–4:00 AM FVG window, the confirmation-candle rule as written, entry options (market on confirmation, or a limit at 50%), the stop below the FVG-candle low, the gold no-hard-stop exception, the valid-pairs list, and the prop-firm drawdown caveat.
- **Corrected:** the earlier note's 1:20 minimum R:R came from a third-party script and the video title (T3/T4). **The playbook states no fixed R:R.** The playbook's exits are daily-structure targets, plus early exits on EMA reversal or a significant opposing candle.
- **New on the T2 page:** the about-90% win rate now appears on the page itself, not just in the video title. It is still a self-reported claim (T4).
- **Cleanup:**
  - `related` had held concept ids (`concept_backtesting`, `concept_overfitting_validation`); it now lists strategy ids only.
  - The empty `validates` and `challenges` keys were dropped.
  - All earlier sources are kept, including the independent re-test.
