---
id: strategy_pavel_first_principles
type: strategy
title: "Pavel — First-Principles Trading Framework (multi-asset, strategy-design framework)"
partition: 01_chart-fanatics
layer: L8
aliases: [first-principles trading framework, playground vs approach, Pavel framework, three directional approaches]
taught_by: [person_pavel]
featured_in: [channel_chart_fanatics]
uses: [concept_edge, concept_expectancy, concept_performance_metrics, concept_market_microstructure, concept_random_walk_efficient_markets, concept_liquidity, concept_volatility, concept_breakout_trading, concept_oscillators_momentum, concept_mean_reversion, concept_moving_averages, concept_trend_following, concept_support_resistance, concept_backtesting, concept_correlation_portfolio_risk]
derived_from: [concept_edge, concept_random_walk_efficient_markets]
related: [strategy_matteo_conti_institutional, strategy_ted_zhang_stage_analysis, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — First-Principles Trading Framework by Pavel", url: "https://www.chartfanatics.com/strategies/trading-first-principles-framework", tier: T2}
status: verified-t2
---

# Pavel — First-Principles Trading Framework (multi-asset, strategy-design framework)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/trading-first-principles-framework. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Pavel as the author of this framework. The page gives no biography and no track record.

## Built for

- **Instruments:** "Multi Assets". The page discusses forex, commodities, stocks and ETFs (large caps, broad indexes and small caps) and crypto.
- **Style:** no label. This is a strategy-design framework. Its worked rules use daily data, with holding periods of about 1–5 days for short-term momentum and mean reversion. Trend-following trades are held until the 10-day MA exit triggers; the page gives no typical duration.
- **Timeframes:** the parameter examples are daily. The 1-hour and 1-minute timeframes appear only as contrasts. Holding period matters as much as chart timeframe: a 5-minute entry held for three days counts as a longer-horizon trade.
- **Session / time window:** not specified.

## Core idea

The framework says an indicator or pattern is only a measuring tool. In its words, "a trading tool is not the same thing as a trading edge." A trader first chooses the *playground* (asset class plus timeframe) and then the *approach*. The best playgrounds for a small trader have less institutional competition and a large enough expected move per trade relative to costs. The edge there also needs enough capacity to survive. The page points to smaller, less liquid markets, and to higher timeframes or longer holds as liquidity rises. It also warns against simply picking the most volatile market. The trader then picks one of three directional behaviours: short-term momentum, mean reversion, or long-term momentum. Once more than one strategy is profitable, the trader combines less-correlated strategies and rebalances between them.

## Rules

1. **Assess the playground before any setup.** Rate the asset class and timeframe for liquidity, volatility, efficiency and professional competition. Avoid the most competitive mix, which is very high liquidity on a very low timeframe. In more liquid markets, prefer higher timeframes or longer holds.
2. **Check expectancy against costs.** The expected move per trade has to be large next to fees, spread and slippage. The page's example is a 1-hour breakout earning about 0.4% per trade against about 0.2% in round-trip costs. Costs eat half of that edge.
3. **Match the approach to the asset class:**
   - *Large stocks and indexes:* long-side trend following and long-side mean reversion.
   - *Small caps:* less liquid and less efficient, so short-term momentum and even short-side mean reversion can work. The page doesn't say whether the large-cap approaches also apply.
   - *Commodities:* all three directional approaches.
   - *Forex:* the framework favours long-term momentum and mean reversion.
   - *Crypto:* all three. Some less-liquid venues also allow arbitrage and market making.
   - *Beginners:* simple long-term momentum across several assets.
4. **Short-term momentum (breakout), entry.** Measure normal recent movement, then enter when it expands sharply. In the page's example, the previous five daily candles averaged about 1% and the next candle moved about 2%, a roughly 2× volatility expansion. RSI, CCI or another momentum gauge can measure this. Research the exact threshold for each market.
5. **Short-term momentum, exit.** Either use a time exit (the page says daily-chart momentum lasts about 2–5 days; set N by research) or hold while momentum persists and exit when it fades.
6. **Mean reversion, entry.** Pick a mean, for example the 5-day simple moving average. Measure how far the close normally sits from it (about 2% in the example). Enter toward the mean when the gap becomes abnormally large (6–7% in the example). Short-period RSI or price-action measures are alternatives. Price must be stretched relative to its normal behaviour; a move in one direction alone is not a signal.
7. **Mean reversion, exit.** Either use a time exit (the page says about 1–4 days on daily data) or exit when price returns to the mean.
8. **Long-term momentum (trend following), entry.** Go long when price breaks above the highest high of the last 100 days. Longer lookbacks such as 200 days can also be used. An all-time-high break is a bigger resistance break and one of the strongest forms of long-term momentum. The page says the downside can be traded the same way "where appropriate".
9. **Long-term momentum, exit.** Stay in while price closes above the 10-day moving average. Exit on a close below it. Don't let a small correction close the position.
10. **Combined entry.** After a 100-day-high breakout, a pullback can be bought as a mean-reversion trade inside the trend. Enter when the mean-reversion condition appears rather than waiting for price to turn back up, because waiting for confirmation gives up part of the edge.
11. **Portfolio.** Add strategies that are less correlated, uncorrelated or negatively correlated with each other. Allocate capital across them, for example 50/50, and rebalance to the target weights on a schedule (daily, weekly, monthly or another interval).
12. **Keep researching.** Edges decay as more capital trades them, and lower-timeframe edges decay fastest. Research is a continuing job.

## Risk management

- **Risk per trade:** Not specified in the playbook.
- **Stop-loss:** Not specified. Exits are time-based, momentum-based, return-to-mean or a 10-day MA close. The page gives no protective stop rule for any approach.
- **Daily / weekly limits:** Not specified in the playbook.
- **Sizing:** Not specified per trade. At portfolio level, capital is split across strategies and rebalanced to target weights.
- **Structural risk control:** pick playgrounds with less competition and less cost drag. Lower portfolio volatility, and so raise the Sharpe ratio, by combining less-correlated edges rather than chasing smooth returns at very short timeframes.

## What the playbook leaves unspecified

- Numeric thresholds for a "meaningful" volatility expansion and an "abnormally large" deviation. The 2× and 6–7% figures are examples only. The page also doesn't say how to measure "normal" movement (ATR, average absolute deviation, lookback length).
- RSI and CCI lengths and trigger levels.
- Protective stops, per-trade sizing, and handling of overnight gaps for all three approaches.
- Concrete short-side trend-following rules ("where appropriate").
- Universe selection: liquidity minimums, which small caps or crypto venues, and cost assumptions by market.
- How deep a counter-trend pullback must go before the trend-following entry in rule 10, and what invalidates it.
- How to measure correlation between strategies, how to set target weights, how often to rebalance once costs are counted, and how to detect that an edge has decayed (metric, sample size).

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims about Pavel's own trading.
- **Illustrative expectancy:** a crypto breakout earns about 1.5% per trade on the daily chart and about 0.4% on the 1-hour chart. Self-reported (T4), and the page itself calls these examples. Cost arithmetic: 0.2% in round-trip costs takes 50% of a 0.4% edge but only about 13% of a 1.5% edge.
- **Duration claims:** daily short-term momentum lasts about 2–5 days, and daily mean reversion plays out over about 1–4 days. Self-reported (T4); no data shown.
- **Rebalancing example:** $20,000 split 50/50 between two strategies that return +100% and −50%, then the reverse. Without rebalancing the account ends at $20,000; with one annual rebalance it ends at $31,250. The arithmetic checks out, but the case is built on perfectly alternating returns. Real gains depend on actual correlation and relative mean reversion, minus rebalancing costs.
- The claims that long-term momentum is the most robust approach across asset classes, and that lower-timeframe edges decay faster, are argued from first principles with no backtest shown (T4).

## Concepts & lineage

- Edge as a statistically positive expected outcome over a large sample: [[concept_edge]], [[concept_expectancy]]
- Sharpe ratio and why institutions pay for stable return streams: [[concept_performance_metrics]]
- Competition from market makers and arbitrageurs, plus spread, fees and slippage as cost drag: [[concept_market_microstructure]]
- Edge decay and the move from immature to mature markets as inefficiencies are arbitraged away: [[concept_random_walk_efficient_markets]]
- The liquidity–volatility trade-off and small size as a retail advantage: [[concept_liquidity]], [[concept_volatility]]
- Short-term momentum measured as a volatility expansion, optionally with RSI or CCI: [[concept_breakout_trading]], [[concept_oscillators_momentum]]
- Mean reversion measured as distance from a 5-day SMA: [[concept_mean_reversion]], [[concept_moving_averages]]
- Trend entry on a 100-day-high break with a 10-day MA exit: [[concept_trend_following]], [[concept_support_resistance]]
- Researching thresholds and time exits for each market: [[concept_backtesting]]
- Combining less-correlated strategies and rebalancing: [[concept_correlation_portfolio_risk]]
