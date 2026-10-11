---
id: strategy_matteo_conti_institutional
type: strategy
title: "Matteo Conti — Institutional Strategy Development Framework (multi-asset, day and swing trading)"
partition: 01_chart-fanatics
layer: L8
aliases: [Institutional Strategy Development Framework, Matteo Conti framework, idea-to-live research process, institutional backtest and validation process]
taught_by: [person_matteo_conti]
featured_in: [channel_chart_fanatics]
uses: [concept_backtesting, concept_overfitting_validation, concept_edge, concept_expectancy, concept_performance_metrics, concept_risk_of_ruin_drawdown, concept_position_sizing, concept_volatility, concept_trading_plan, concept_breakout_trading, concept_vwap, concept_news_trading, concept_trading_sessions_killzones, concept_market_microstructure, concept_optimal_execution_market_impact, concept_random_walk_efficient_markets, concept_market_regimes, concept_correlation_portfolio_risk, concept_probabilistic_thinking]
derived_from: [concept_backtesting, concept_random_walk_efficient_markets]
related: [strategy_naoufel_taief_algorithmic, strategy_pradeep_bonde_episodic_pivot]
sources:
  - {title: "Chart Fanatics — Institutional Strategy Development Framework", url: "https://www.chartfanatics.com/strategies/institutional-strategy-development-framework", tier: T2}
status: verified-t2
---

# Matteo Conti — Institutional Strategy Development Framework (multi-asset, day and swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/institutional-strategy-development-framework. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Matteo Conti explaining how institutional
traders build, test and validate a strategy before risking money on it. The
page gives no further biography.

## Built for

- **Instruments:** multi-asset. The worked examples use US index products
  (QQQ, NQ, ES), crude oil, individual stocks, and small- and mid-cap
  equities for the earnings model, with European equities named as a
  research candidate.
- **Style:** day trading and swing trading. This is a research and
  validation process, not one setup. The four example models are teaching
  vehicles, and the page says not to copy them as-is.
- **Timeframes and windows (by example model):**
  - Opening range breakout: range from **9:30 to 10:00 AM ET**, time exit
    around **3:30 PM ET**.
  - VWAP trend: **1-minute** chart, session VWAP anchored at **9:30 AM ET**.
  - Post-earnings drift: entry at the next trading day's open, held about
    **60 trading days** (chart timeframe not specified in the playbook).
  - Overnight anomaly: long from **4:00 PM ET** to **9:30 AM ET** the next
    trading day.

## Core idea

Institutional traders look for a repeatable strategy that can be tested on
data, not for the next trade. An idea comes from research, gets a reason it
might work, and is turned into objective rules. It is then coded,
backtested, validated out of sample and with Monte Carlo, deployed, and
monitored. The question is never whether the next trade wins but whether the
same rules have a positive expected return over a large sample. Simple
rules with a clear market reason are preferred, because each extra condition
adds another way to overfit.

## Rules

The process (the page's 13 steps, grouped):

1. **Find an idea in research.** Sources include academic work (for example
   papers on SSRN) and industry research from funds and practitioners. Take
   the market behaviour the paper found, not its exact recipe: "Do not copy
   the research paper directly."
2. **Explain why the edge should exist.** Each example model is tied to a
   cause: early-session order imbalance, institutional VWAP execution, slow
   absorption of earnings news, and an overnight risk premium or thin
   overnight liquidity. Knowing the cause also helps you notice when it
   stops applying.
3. **Define three objective components.** An **entry** with no room for
   interpretation (for example, a 1-minute candle closing above VWAP, not
   "price looks strong"). An **exit**: stop, target, time exit, or a price
   or indicator condition. A **position size**: start with **one fixed
   contract** while developing.
4. **Encode one rule at a time.** Code the entry and check it fires where
   expected. Then add the exit and test again, then the sizing, until the
   code behaves exactly like the written rules. AI and LLMs may help
   translate rules into code, but the trader must understand and check
   every part.
5. **Backtest** the exact rules on historical data. Review net profit, win
   rate, average trade, average winner and loser, maximum drawdown and
   losing streaks.
6. **Develop in sample, then freeze.** Split history, for example **80% in
   sample and 20% out of sample**. Add, remove or tune rules only on the
   in-sample part. Freeze the rules before looking at the unseen data.
7. **Test out of sample.** If results hold up in development but collapse
   on unseen data, suspect overfitting.
8. **Run Monte Carlo.** *Shuffle*: keep every trade but randomise the
   order thousands of times to see how much drawdown and losing
   streaks depend on sequence. *Resampling*: draw trades with replacement
   to estimate expected return, potential drawdown, the longest losing
   streak and the chance of a given loss. Tight clusters of equity curves
   point to a sturdier edge, and a wide spread points to a fragile one.
9. **Finalise sizing** with volatility targeting: fix the money at risk and
   size from current volatility (fewer contracts when volatility is high,
   more when it is low), so that a few wild sessions do not dominate
   results.
10. **Deploy** in one of three modes: research only (backtest, then trade by
    hand), as confirmation for a discretionary setup, or fully automated.
11. **Monitor live results** against the Monte Carlo ranges. A breach is a
    warning to review the strategy, not automatic proof it is broken.
12. **Build a portfolio.** Develop further *uncorrelated* strategies (for
    example momentum alongside mean reversion). The page suggests about
    **3 to 4 strategies** at once for a retail trader.

The four example models, as starting hypotheses to test:

- **Opening range breakout (long).** Mark the high and low from 9:30 to
  10:00 AM ET. Go long on a **close** above the range high, not a touch.
  Stop at the range low. Test targets of **1R to 2R**. Exit around 3:30 PM
  ET if neither has been hit. The short version (close below the range low,
  stop on the other side of the range) must be tested separately. In
  Matteo's experience the long side has worked better, because buyers tend
  to step into downside breaks.
- **VWAP trend.** Use session VWAP from 9:30 AM ET on the 1-minute chart.
  Go long on a candle close above VWAP and short on a close below it. Exit
  when price crosses back through VWAP; there is no separate target. The
  research used QQQ, and the page suggests testing NQ, ES, crude oil and
  individual stocks. Variants such as previous-day VWAP need their own
  validation.
- **Post-earnings announcement drift (long).** Requires a positive price
  reaction to earnings **and** actual EPS above the analyst estimate. Enter
  at the next trading day's open and exit after about **60 trading days**.
  Stops (a percentage, the pre-earnings close or others) are research
  options, not part of the base model. Size at **1 to 2% of the portfolio
  per stock**, a fixed dollar amount, or scaled to surprise, reaction or
  volatility. Small and mid caps are the main candidates. The short side
  may be weaker because companies often warn ahead of bad numbers.
- **Overnight anomaly.** Go long at 4:00 PM ET and exit at 9:30 AM ET the
  next trading day. This mainly tests whether the effect exists. It is not
  a finished strategy, and the page gives no stop or target. It can seed
  new ideas, such as an overnight breakout or momentum model.

## Risk management

- **Per-trade risk:** for development, one fixed contract. For live
  trading, volatility-adjusted sizing to a fixed money-at-risk figure. The
  page's illustration uses a target risk of $10,000; that is an example,
  not a recommended level. For the earnings model, 1 to 2% of the portfolio
  per stock or a fixed dollar amount.
- **Stops:** opening range low for the ORB long; a VWAP recross for the
  VWAP model; a time exit for the earnings drift model (stops are left to
  research); none for the overnight baseline.
- **Daily or weekly loss limits:** not specified in the playbook.
- **Strategy-level risk:** Monte Carlo drawdown and losing-streak ranges
  act as reference limits during live trading. A live drawdown beyond the
  simulated range triggers a review.
- **Portfolio risk:** run several uncorrelated strategies rather than one.

## What the playbook leaves unspecified

- How many trades or how many years of data are needed before a backtest
  counts as meaningful, and which markets and date ranges the examples
  used.
- Pass and fail thresholds for out-of-sample and Monte Carlo results: how
  much out-of-sample decay is acceptable, and what counts as a "tight"
  versus "wide" spread of equity curves.
- Transaction costs, slippage, borrow and commissions in the backtests.
- How volatility is measured for volatility targeting (ATR, range width,
  standard deviation) and over what lookback.
- How large a positive price reaction must be for the earnings model, and
  which EPS consensus source to use.
- Whether the ORB stop should be at the range low when the range is very
  wide, and whether to skip trades on wide-range days.
- How "uncorrelated" is measured when building the 3 to 4 strategy
  portfolio, and how capital is split between them.
- What happens to a live strategy after a review: pause, cut size or
  retire it.

## Evidence & claims

- The page gives **no win rate, R:R result, P&L or payout** for any of the
  four models or for Matteo's own trading. No expectancy check is possible.
- **Research claims cited, not quantified on the page:** a large share of
  historical equity-index returns came overnight rather than during regular
  hours; Matteo says he has seen similar behaviour in recent Nasdaq futures
  data. Treat this as self-reported (T4) until checked against the
  underlying studies.
- **Self-reported (T4):** Matteo's experience is that the opening range
  imbalance has worked better on the long side than the short side. No
  figures are given.
- The "70% win rate can still lose the next trade" line and the $10,000
  drawdown and target-risk figures are illustrations, not results.
- The 1R to 2R ORB target is a range to test, not a claimed outcome.

## Concepts & lineage

- Research → rules → code → backtest pipeline →
  [[concept_backtesting]], [[concept_trading_plan]]
- In-sample and out-of-sample split, frozen rules, overfitting warning →
  [[concept_overfitting_validation]]
- Monte Carlo shuffle and resampling of the trade list, drawdown and
  losing-streak ranges → [[concept_risk_of_ruin_drawdown]],
  [[concept_probabilistic_thinking]]
- Positive expected return across a large sample, not single-trade
  outcomes → [[concept_expectancy]], [[concept_edge]]
- Backtest statistics (net profit, win rate, average trade, max drawdown)
  → [[concept_performance_metrics]]
- One-contract development sizing, then volatility targeting →
  [[concept_position_sizing]], [[concept_volatility]]
- Opening range breakout from 9:30 to 10:00 AM ET, and RTH versus
  overnight returns → [[concept_breakout_trading]],
  [[concept_trading_sessions_killzones]]
- VWAP trend model, with VWAP as an institutional execution benchmark →
  [[concept_vwap]], [[concept_optimal_execution_market_impact]]
- Post-earnings announcement drift on an EPS surprise →
  [[concept_news_trading]]
- Anomalies explained by slow information flow and thin overnight
  liquidity → [[concept_random_walk_efficient_markets]],
  [[concept_market_microstructure]]
- Momentum and mean-reversion strategies doing well in different
  conditions → [[concept_market_regimes]]
- A portfolio of 3 to 4 uncorrelated strategies →
  [[concept_correlation_portfolio_risk]]
