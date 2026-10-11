---
id: strategy_tg_capital_trident
type: strategy
title: TG Capital — London Session "Trident" (FVG + EMA stack, 1:20 R:R)
partition: 01_chart-fanatics
layer: L4
aliases: [TG Capital strategy, Trident, unique high RR, London session swing strategy, 1:20 RR strategy]
taught_by: [person_tg_capital]
featured_in: [channel_chart_fanatics]
uses: [concept_trading_sessions_killzones, concept_fair_value_gap, concept_moving_averages, concept_multi_timeframe_analysis, concept_candlestick_patterns, concept_risk_reward_r_multiples, concept_trade_management, concept_market_regimes]
derived_from: [concept_smart_money_concepts]
validates: []
challenges: []
related: [concept_backtesting, concept_overfitting_validation]
sources:
  - {title: "Chart Fanatics — TG's Capital London Session Swing Trading Strategy", url: "https://www.chartfanatics.com/strategies/unique-high-rr", tier: T2}
  - {title: "TradeZella — TG Capital London Session Strategy", url: "https://www.tradezella.com/strategies/unique-high-rr", tier: T3}
  - {title: "TradingView — TG Capital Trident Strategy [Long + Short] (third-party script)", url: "https://www.tradingview.com/script/nFdphVub-TG-Capital-Trident-Strategy-Long-Short/", tier: T3}
  - {title: "TakeProfit — Reverse-Engineering a Public 1:20 RR Strategy: Chart Fanatics & TG Capital", url: "https://takeprofit.com/posts/reverse-engineering-a-public-1-20-rr-strategy-chart-fanatics-tg-capital-51", tier: T3}
status: synthesized
---

# TG Capital — London Session "Trident"

**Video:** *"STEAL This INSANE Simple 90% Win Rate Trading Strategy (1:20+ RR)
— TG Capital"*. The title's numbers are T4.

## Published rules (Chart Fanatics strategy page, T2)

| Element | Rule |
|---|---|
| **Session** | London kill zone only, **3:00–6:30 AM New York time** ([[concept_trading_sessions_killzones]]) |
| **Timeframes** | **Daily** = bias and take-profit targets; **30-minute** = entries ([[concept_multi_timeframe_analysis]]) |
| **Trend filter** | **5, 9, 13 (or 15), 21 EMAs stacked** in order. If crossing or tangled, the setup is invalid ([[concept_moving_averages]], [[concept_market_regimes]]) |
| **Entry pattern: "Trident"** | A **fair value gap** + a **doji wick into its midpoint** + a **confirmation candle** ([[concept_fair_value_gap]], [[concept_candlestick_patterns]]) |

## Management (third-party script, T3)

- Minimum target **1:20 R:R** from entry vs stop.
- Exit early if the EMA stack breaks or price fully closes through the stop.
- **One position at a time;** new FVGs are ignored until it closes.

## Evidence check

| Claim | Source | Finding |
|---|---|---|
| "90% win rate at 1:20+ RR" | Video title (T4) | Implies +17.9R per trade, which is implausible ([[concept_risk_reward_r_multiples]]) |
| Independent EA re-test | TakeProfit, EURUSD M30 (T3) | **~20% win rate, many large winners, profitable out-of-sample 2023–24** |

**Verdict.** The structure (session + trend filter + FVG retrace + daily
targets) is coherent and *may* carry a positive-skew edge. The headline win
rate does not survive. This is a model example of separating method from
marketing ([[concept_overfitting_validation]]).
