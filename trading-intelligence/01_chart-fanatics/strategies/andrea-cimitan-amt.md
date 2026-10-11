---
id: strategy_andrea_cimitan_amt
type: strategy
title: "Andrea Cimitan — Liquidity Auction & Order Flow Strategy (futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Liquidity Auction Theory, Andrea Cimitan auction market theory, failed auction strategy, acceptance vs absorption]
taught_by: [person_andrea_cimitan]
featured_in: [channel_chart_fanatics]
uses: [concept_auction_market_theory, concept_order_flow, concept_volume_profile, concept_market_microstructure, concept_optimal_execution_market_impact, concept_liquidity, concept_mean_reversion, concept_breakout_trading, concept_multi_timeframe_analysis]
derived_from: [concept_auction_market_theory, concept_market_microstructure]
related: [strategy_fabio_valentini_amt_order_flow, strategy_rajan_dhall_auction, strategy_yush_order_flow]
sources:
  - {title: "Chart Fanatics — Liquidity Auction & Order Flow Trading Strategy", url: "https://www.chartfanatics.com/strategies/auction-market-theory-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists Auction Market Theory by Andrea Cimitan)", url: "https://www.chartfanatics.com/strategies", tier: T2}
status: verified-t2
---

# Andrea Cimitan — Liquidity Auction & Order Flow Strategy (futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/auction-market-theory-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** According to the page, Andrea Cimitan teaches this approach, which he calls "Liquidity Auction Theory", in a 17-lesson Order Flow Masterclass on Chart Academy. The masterclass covers footprint charts, volume profile, CVD and market-maker mechanics, with live ES and Nasdaq examples.

## Built for

- **Instruments:** futures. The masterclass examples are ES and Nasdaq.
- **Style:** day trading.
- **Timeframes:** a higher-timeframe volume profile and the daily candle for context. Order flow (footprint, absorption) for execution. No chart timeframe is fixed.
- **Session / time window:** no hours are stated. The worked example trades the market open and the opening range.

## Core idea

The market is treated as a continuous double auction. Limit orders provide liquidity, and price moves only when one side becomes aggressive and accepts worse prices to get filled. Urgency moves price, not a larger count of buyers or sellers. Large players split meta-orders and run them through execution algorithms such as VWAP or TWAP, so price travels in search of liquidity rather than to hunt individual stops. Markets cycle from balance (fair value) to imbalance and then to a new balance. The only question is whether the aggressive side is being *accepted* (price follows) or *absorbed* (price stalls). Trade only when the market proves one side is in control.

## Rules

1. **Build a bias.**
   - *Order-flow autocorrelation:* strong buying or selling pressure in one session raises the odds of similar behaviour in the next.
   - *Higher-timeframe context:* a daily candle moving higher suggests longer-term participants are holding positions.
2. **Locate fair value.** Use the volume profile to find where most trading happened (the value area) and whether price is inside or outside it. Then judge whether price is trying to move into imbalance.
3. **Setup 1: Failed auction below value (reversal long).**
   - Price trades below value and sellers turn aggressive, but they fail to push lower and get absorbed.
   - Absorption alone is not an entry. Enter long only once buyers clearly take control.
   - Stop below the area where sellers tried to dominate.
   - Target a return to fair value, possibly the opposite side of the range.
4. **Setup 2: Failed auction above value (reversal short).**
   - The mirror of Setup 1: buyers push above value, fail, and are absorbed by sellers.
   - Enter after seller dominance is confirmed.
   - Stop above the failed auction. Target a return to fair value.
5. **Setup 3: Breakout with acceptance (continuation).**
   - A breakout is tradable only if price holds outside the level, participation continues, and there is no immediate rejection.
   - A break that quickly returns inside is a failed auction, not a breakout.
   - Enter after real participation confirms the move. Stop below the breakout structure. Target continuation.
6. **Decision filter for every setup.** Aggressive buyers whose pushes keep moving price are in control. Aggressive buyers who appear while price doesn't rise are being absorbed. Apply the same test to sellers.
7. **Opening-range integration.** Take an ORB only when buyers dominate and price holds beyond the range. If aggressors are absorbed and price returns into the range, skip it. In the worked example, a first breakout attempt showed aggression mostly in the candle *wick* (effort without acceptance) and was skipped. A second attempt with activity in the candle *body* was taken.
8. **Stop runs.** Stop orders are market orders, so a triggered cluster cascades. Afterwards the book often thins and price often reverses. Treat these as liquidity events, not deliberate stop hunting.
9. **Manage on participation.** Hold while the controlling side stays in control. Exit when the opposite side takes over. In the example, the exit came when buyers began to be absorbed near the highs and sellers gained control.

## Risk management

- **Invalidation:** stops go where the trade idea fails, typically where the opposing side would show control again. They are not placed at arbitrary price distances.
- **Stop size:** confirmation-based entries are said to allow tighter, more efficient stops.
- **Risk per trade:** Not specified in the playbook.
- **Sizing:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.

## What the playbook leaves unspecified

- Which volume profile to use (session, prior day, composite) and the value-area percentage.
- Objective footprint, delta or CVD thresholds for "aggression", "absorption" and "control". The tools are named only in the masterclass blurb.
- How long or how far price must hold outside a level to count as "acceptance".
- The opening-range length and any time-of-day window.
- Profit-taking rules beyond "return to value" or "continuation", R targets, scaling, and trade frequency.
- Position size, risk per trade and loss limits.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- The worked example (a value-area-low reversal that aligned with the previous day's value-area low, followed by an ORB add-on) is described qualitatively, with no prices, size or outcome figures (T4).

## Concepts & lineage

- Balance → imbalance → new balance, fair value and failed auctions: [[concept_auction_market_theory]]
- Value area and value-area low/high as location: [[concept_volume_profile]]
- Aggressive vs passive orders, acceptance vs absorption, footprint and CVD: [[concept_order_flow]]
- Double auction, market makers capturing the spread, retail's small share of volume: [[concept_market_microstructure]]
- Meta-orders and VWAP/TWAP execution algorithms ("execution alpha"): [[concept_optimal_execution_market_impact]]
- Price moving to find liquidity, and stop runs as liquidity events: [[concept_liquidity]]
- Failed-auction rotations back to fair value: [[concept_mean_reversion]]
- Breakouts with acceptance and the ORB filter: [[concept_breakout_trading]]
- Daily-candle context and session-to-session autocorrelation: [[concept_multi_timeframe_analysis]]

## Changes vs. earlier note

- The earlier note (index listing only, `pending-scrape`) titled this "Auction Market Theory" and had no rules. The playbook page is titled **Liquidity Auction & Order Flow Trading Strategy**, and the title now follows it.
- **Confirmed:** auction market theory and volume profile are the foundation.
- **Added:** the microstructure framing (double auction, urgency, meta-orders, VWAP/TWAP execution, market-maker role) and the balance/imbalance cycle.
- **Added:** the three setups (failed auction below value, failed auction above value, breakout with acceptance), each with an entry condition, stop and target.
- **Added:** the acceptance-vs-absorption filter, the opening-range integration, the stop-run explanation, and the order-flow-based exit.
- **Added:** order flow, market microstructure, liquidity and breakout concepts to `uses`.
