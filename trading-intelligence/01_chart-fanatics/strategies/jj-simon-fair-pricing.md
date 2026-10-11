---
id: strategy_jj_simon_fair_pricing
type: strategy
title: "JJ Simon — Fair Pricing Theory: Continuation & Reversion (Nasdaq futures, 1-minute scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [fair pricing theory, fair value theory, JJ Simon strategy, fair price reversion]
taught_by: [person_jj_simon]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_trading_sessions_killzones, concept_news_trading, concept_market_structure, concept_multi_timeframe_analysis, concept_prop_firm_risk_rules, concept_position_sizing, concept_risk_reward_r_multiples, concept_risk_of_ruin_drawdown, concept_backtesting, concept_scalping, concept_market_regimes]
derived_from: [concept_mean_reversion, concept_auction_market_theory]
related: [strategy_fabio_valentini_amt_order_flow, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — JJ Simon’s Fair Pricing Theory Strategy", url: "https://www.chartfanatics.com/strategies/fair-pricing-theory-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists Fair Pricing Theory by JJ Simon)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "SozAI — The Strategy Behind My $1.6M in Prop Firm Payouts (transcript & summary)", url: "https://sozai.app/transcript/strategy-behind-1-6m-prop-firm-payouts/", tier: T3}
  - {title: "SozAI — Backtesting JJ Simon's NQ Strategy | Fair Value Theory", url: "https://sozai.app/transcript/backtesting-jj-simon-nq-strategy/", tier: T3}
status: verified-t2
---

# JJ Simon — Fair Pricing Theory: Continuation & Reversion (Nasdaq futures, 1-minute scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/fair-pricing-theory-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** JJ Simon is a Nasdaq futures scalper whose risk model is built
around prop-firm evaluation and funded accounts. The earlier note's sources
tie him to $1.2M to $1.8M+ in prop payouts (T4, see Evidence).

## Built for

- **Instruments:** futures. The examples that name a market refer to
  Nasdaq (NQ).
- **Style:** scalping.
- **Execution chart:** 1-minute. Context comes from the prior 6 to 12 hours,
  read on the 1-minute or a 5-minute chart.
- **Window:** roughly the first 90 minutes of a major session. In New York
  that is **9:30 to 11:00 AM ET**. The same logic applies to the Asia,
  London and New York afternoon sessions. About 11:00 AM to 2:00 PM ET is
  described as low volume, and fresh participation can arrive around
  2:00 PM ET.
- **Accounts:** mainly prop-firm evaluation and funded accounts. Live
  personal accounts are handled differently (see Rules).

## Core idea

Each event that brings in new volume sets a **fair price**: a session open,
or the price just before a scheduled news release. When new volume arrives,
price displaces away from that level. The trader can first ride the
**continuation** away from fair price. Once the move is stretched, the
trader can trade the **reversion** back toward it, but only after a
confirmed momentum shift. Fair price is not a fixed support or resistance
line. It is reassessed whenever a different event takes over the market.

## Rules

1. **Set the fair price from the event now driving the market.**
   - *Normal session:* the opening price (9:30 AM ET for New York).
   - *Scheduled news* (examples: CPI and PPI at 8:30 AM ET): the price just
     before the release. The market already knew the release was coming and
     had the forecasts. On big news days this pre-news price can stay more
     important than the 9:30 open.
   - *Unexpected news* (a surprise announcement, speech or tweet): do not
     expect a return to the old level. Let the move play out and use the
     next consolidation as the new fair price.
2. **Read the larger context.** Look back about 6 to 12 hours to see the
   prior directional move and whether it may start reverting.
3. **Continuation trade.** If the opening displacement is strong, breaks
   relevant structure and agrees with the bias, enter in its direction. The
   opening candle alone is not enough.
4. **Reversion trade.** Once price is stretched from fair price, stop
   chasing it. Never fade a move just because it looks extended. Wait for
   one of two confirmations pointing back toward fair price:
   - **Displacement Candle (DC):** the body is larger than the previous
     candle's body, it closes beyond the previous candle's wick, and it
     displaces a candle of the opposite colour.
   - **Break of Structure (BOS):** a candle closes through a meaningful
     prior swing high or low. A wick through the level does not count. The
     clearer the structure, the stronger the signal. JJ ranks BOS as
     slightly stronger than DC.
   In both cases, enter only after the confirming candle has closed.
5. **Target.** For reversions, the fair price itself: the 9:30 open or the
   pre-news price.
6. **Unexpected-news continuation.** Fixed targets are optional here. Hold
   while structure keeps going your way, and get out when price closes
   through meaningful structure in the opposite direction.
7. **Stops and targets by account type:**
   - *Evaluation:* mechanical. Example: a **25-point stop with a 38-point
     target** (about 1:1.5). If the opening candle is unusually large, scale
     to **50 points / 76 points** and halve the contracts. Stops used across
     setups and accounts are about **25, 37.5, 50 and 75 points**, chosen
     from the account model and historical testing rather than chart
     invalidation. More valid DC entries are taken in evaluations.
   - *Funded:* more selective, with BOS entries preferred. With no
     restrictive consistency rule, a target of **50, 75, 100+ points** is
     allowed when fair price is that far away. With a consistency rule,
     take smaller and more repeatable wins.
   - *Live personal account:* focus on reversions, BOS entries and
     expected-news reversions, with stops and targets placed on market
     structure.
8. **Three-Loss Rule.** If **three reversion trades in a row fail in the
   same session**, stop taking reversions for that session. The market may
   be trending and setting a new fair value.
9. **Keep reassessing fair price.** Drop an old fair price once value has
   clearly moved. Signs include unexpected news, a new consolidation, a
   strong trend, or repeated failed reversions.
10. **Layering (account management).** Across several prop accounts, put
    different valid entries on different accounts. For example, the first
    DC goes on one account and a later BOS on another. This avoids exposing
    every account to the same single outcome.

## Risk management

- **Per trade:** a fixed point stop for each account model (25, 37.5, 50 or
  75 points). When the stop distance changes, the contract count changes in
  inverse proportion, so the dollar exposure stays roughly constant.
- **Reward-to-risk:** about 1:1.5 in evaluations (25 to 38 points). Funded
  and live targets are larger and depend on structure.
- **Session limit:** the Three-Loss Rule applies to reversion trades. No
  daily dollar loss limit is specified in the playbook.
- **Account rules:** the profit target, drawdown and consistency rules of
  each prop firm shape both sizing and targets.
- **Backtesting the account model:** measure the **evaluation pass rate**
  under the firm's real rules, not just raw P&L. The page's worked example:
  a $100 evaluation that passes 25% of the time costs about $400 per funded
  account ($100 ÷ 25%). Compare that cost with the expected payout. JJ
  suggests running about **50 evaluation backtests** to reduce small-sample
  noise.
- **Dollar risk per contract, or as a % of the account:** not specified in
  the playbook.

## What the playbook leaves unspecified

- What separates a "meaningful" structure from noise for BOS, and what
  "extended" means before a reversion is allowed.
- How exactly the 6 to 12 hour lookback sets the bias, and how a conflict
  between that bias and the opening displacement is settled.
- Stops for reversion entries on live accounts. The page says only that
  they are structure-based.
- How large the "new consolidation" after unexpected news must be, and how
  long it must last.
- Which stop size (25, 37.5, 50 or 75) goes with which setup or account.
  The page says only that it comes from historical testing.
- Rules for the Asia, London and afternoon-session versions, which are
  mentioned but not given in detail.
- Any daily dollar loss limit or rule for continuation-trade losses.

## Evidence & claims

- **On the playbook page:** no win rate or P&L is claimed. The 1:1.5 ratio
  is a risk setting, not a result. The $100 / 25% / $400 figures are a
  worked example of the pass-rate method, not reported results.
- **Payout claims (from the earlier note's sources):** $1.2M to $1.8M+ in
  prop payouts across summaries, and one video is titled "$1.6M in Prop
  Firm Payouts". All self-reported (T4).
- **Independent NQ 1-minute backtest (SozAI, T3):** about **52% win rate,
  1.66 profit factor**, but only *after filtering and parameter changes*,
  which raises overfitting risk ([[concept_overfitting_validation]]).
- **Conflicting third-party summary (T3, unverified):** one summary cited
  about a 20% win rate with R:R up to 1:4. The playbook's funded-account
  targets of 50 to 100+ points would give 1:2 to 1:4 if paired with a
  25-point stop, but the page does not state the funded-account stop and
  gives no win rate.
- **Expectancy check, E = p×RR − (1−p), in R** (illustrative, because the
  win rates and R:R come from different sources):
  - 52% at the evaluation 1:1.5: E = 0.52×1.5 − 0.48 = **+0.30R**.
    Break-even at 1:1.5 needs p = 40%.
  - 20% at 1:4: E = 0.20×4 − 0.80 = **0.00R**, which is break-even before
    costs.

## Concepts & lineage

- Reverting toward the event-defined fair price after a confirmed shift →
  [[concept_mean_reversion]]
- Fair price as the market's current accepted value, which shifts when new
  information arrives. This link is the knowledge base's interpretation;
  the page never names AMT → [[concept_auction_market_theory]]
- Session opens, the 9:30 to 11:00 window and the afternoon lull →
  [[concept_trading_sessions_killzones]]
- Scheduled versus unexpected news, and the pre-news price as fair value →
  [[concept_news_trading]]
- Displacement Candle and Break of Structure confirmations →
  [[concept_market_structure]]
- A 6 to 12 hour context read with a 1-minute trigger →
  [[concept_multi_timeframe_analysis]]
- Three-Loss Rule as a switch that detects trend days →
  [[concept_market_regimes]], [[concept_risk_of_ruin_drawdown]]
- Fixed point stops, halving contracts as stops double, layering →
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]]
- Evaluation, funded and consistency rules, and pass-rate economics →
  [[concept_prop_firm_risk_rules]], [[concept_backtesting]]
- Execution on a 1-minute chart → [[concept_scalping]]

## Changes vs. earlier note

- **Fair price definition.** The earlier note said fair price is "usually
  the New York open or pre-open" (T3). The playbook says it is the **9:30 AM ET
  open** in normal sessions and the **price just before** a scheduled
  release on news days, and that the pre-news price can override the 9:30
  open.
- **News handling, corrected.** The earlier note said news releases
  "reset" fair price (T3). The playbook separates **scheduled** news, where
  the pre-news price stays fair and price is expected to revert to it, from
  **unexpected** news, where a new consolidation becomes the new fair price.
- **Setup grading dropped.** The earlier note's "HTF mean reversion + LTF
  continuation" framing with A+/A/B grades (T3) does not appear on the
  page. The page uses two entry models (DC and BOS, with BOS slightly
  stronger) and a 6 to 12 hour context window.
- **R:R conflict narrowed.** The playbook confirms **about 1:1.5** (25 to
  38 points) for evaluations, and allows 50 to 100+ point targets on funded
  accounts without consistency rules. The ~20% / 1:4 figure is still
  unconfirmed and now appears only under Evidence.
- **Three-loss rule confirmed and narrowed.** It covers **three
  consecutive failed reversion trades in the same session**, and it stops
  only reversions for that session.
- **"Less effective on live accounts", reframed.** The playbook does not
  say this. It says the fixed stops and targets are designed around prop
  rules. On a live account JJ would favour reversions, BOS entries and
  expected-news reversions, with stops and targets set by structure.
- **Added:** the exact DC and BOS definitions, session timing, the ladder of
  stop sizes, halving contracts when stops double, layering across
  accounts, and pass-rate backtesting (about 50 runs).
- **VWAP removed from `uses`.** The playbook never mentions VWAP. The
  earlier "POC/VWAP reversion" cross-link was editorial.
