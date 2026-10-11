---
id: strategy_jj_simon_fair_pricing
type: strategy
title: JJ Simon — Fair Pricing Theory (NQ reversion + continuation)
partition: 01_chart-fanatics
layer: L4
aliases: [fair pricing theory, fair value theory, JJ Simon strategy]
taught_by: [person_jj_simon]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_vwap, concept_trading_sessions_killzones, concept_news_trading, concept_market_structure, concept_risk_of_ruin_drawdown, concept_prop_firm_risk_rules, concept_scalping]
derived_from: [concept_auction_market_theory, concept_mean_reversion]
related: [strategy_fabio_valentini_amt_order_flow]
sources:
  - {title: "Chart Fanatics strategies index (lists Fair Pricing Theory by JJ Simon)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "SozAI — The Strategy Behind My $1.6M in Prop Firm Payouts (transcript & summary)", url: "https://sozai.app/transcript/strategy-behind-1-6m-prop-firm-payouts/", tier: T3}
  - {title: "SozAI — Backtesting JJ Simon's NQ Strategy | Fair Value Theory", url: "https://sozai.app/transcript/backtesting-jj-simon-nq-strategy/", tier: T3}
status: synthesized
---

# JJ Simon — Fair Pricing Theory

## Core idea (T3)

The price at a **reference point, usually the New York open or pre-open**,
is "fair". Without new information, price **drifts back toward fair**.
**News releases reset** the fair price ([[concept_news_trading]]).

## Two trade types

| Type | When | Logic |
|---|---|---|
| **Reversion** | Price stretched from fair, no new information | Target a return to fair ([[concept_mean_reversion]]) |
| **Continuation** | After session opens or news releases | Trade the repricing |

Framing variant: **HTF mean reversion + LTF continuation**, with setups
**graded A+, A, B** by displacement and break of structure.

## Risk

- R:R cited as 1:1.5 in one summary. Another cites a ~20% win rate with R:R up
  to 1:4. The sources disagree, so verify against the video.
- **Stop reversion trades after three consecutive losses** (a regime
  circuit-breaker, [[concept_risk_of_ruin_drawdown]]).

## Evidence

- Payout claims range from **$1.2M to $1.8M+** across summaries (T4).
- An independent NQ 1-minute backtest reported **~52% win rate, 1.66 PF**
  *after filtering and parameter changes* (overfitting risk:
  [[concept_overfitting_validation]]).
- Prop-firm focused; one source says it is less effective on live accounts.

## Cross-link

Conceptually equivalent to **POC/VWAP reversion** in AMT. Fair price is an
anchor of value.
