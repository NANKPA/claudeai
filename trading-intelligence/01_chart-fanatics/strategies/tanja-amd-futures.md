---
id: strategy_tanja_amd_futures
type: strategy
title: "Tanja Trades — AMD Futures Model: Trade the Distribution Leg (futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Tanja's AMD Futures Trading Strategy", Tanja AMD model, AMD futures strategy, AMD model]
taught_by: [person_tanja_trades]
featured_in: [channel_chart_fanatics]
uses: [concept_amd_power_of_three, concept_liquidity, concept_liquidity_sweep_reversal, concept_market_structure, concept_fair_value_gap, concept_news_trading, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_intermarket_analysis, concept_market_regimes, concept_trade_management]
derived_from: [concept_amd_power_of_three, concept_wyckoff_method]
related: [strategy_marco_trades_liquidity_grab, strategy_candace_lau_nq_sweep_reversal, strategy_trader_kane_lab_model]
sources:
  - {title: "Chart Fanatics — Tanja's AMD Futures Trading Strategy", url: "https://www.chartfanatics.com/strategies/amd-model", tier: T2}
  - {title: "TradeZella — AMD Model", url: "https://www.tradezella.com/strategies/amd-model", tier: T3}
status: verified-t2
---

# Tanja Trades — AMD Futures Model: Trade the Distribution Leg (futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/amd-model. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Tanja Trades day trades futures with a structured AMD
approach. It is built to avoid chop and to trade only clean, news-driven
moves under strict discipline rules.

## Built for

- **Instruments:** futures. The example is Nasdaq (NQ), and Nasdaq and
  S&P are checked against each other for alignment.
- **Style:** day trading.
- **Timeframes:** 1H, 4H and Daily for the draw on liquidity, key levels
  and major FVGs. 1m, 5m and 15m to confirm displacement and refine the
  entry.
- **Time window:** the **New York session after high-impact news**, not
  during the spike. The playbook's "macro windows" are **9:50 to 10:10 and
  10:50 to 11:10 ET**. The CPI example is built around the 8:30 AM ET
  release.

## Core idea

Markets cycle through **Accumulation** (a sideways range that builds
liquidity), **Manipulation** (a sharp sweep of stops above or below the
range) and **Distribution** (the real directional leg). The accumulation
chop is hard to trade, and the manipulation is not traded directly. Tanja
enters only in **distribution**, once a forceful break of a swing leaves a
**fair value gap** and price comes back into it. A daily filter of news,
correlation and a clear draw on liquidity decides whether there is any
trade at all. The page's default when nothing is clear is that the safest
trade is no trade.

## Rules

1. **Classify the day using the economic calendar.**
   - *High probability:* major scheduled news (CPI, NFP, GDP, FOMC, PPI);
     a strong sweep that clears obvious stops; clean displacement and FVGs
     on the higher timeframes.
   - *Low probability:* no major news; bank holidays or the day after one;
     **the day before** CPI, FOMC or NFP; the day after a large move that
     already hit a major target; jagged highs and lows with no direction.
2. **Check correlation.** Nasdaq and S&P should agree. A heavy divergence
   lowers the odds.
3. **Name the draw on liquidity** on 1H, 4H or Daily: equal highs or lows,
   an unfilled FVG, or a clean swing point. **No clear destination, no
   trade.** If the higher timeframe is unclear, do not force a
   lower-timeframe setup.
4. **Read the AMD sequence.** Mark the accumulation range, then wait for
   the manipulation sweep. Do not trade the sweep itself.
5. **Require displacement.** Price breaks a key swing high or low with
   force and leaves an FVG behind, confirmed on 1m, 5m or 15m. If price
   respects that FVG on the retrace, the move is valid.
6. **Entry.** On the retrace into the valid FVG. **If there is no
   retracement, skip it. Never chase.**
7. **Stop.** In the example, above the high of the manipulation spike,
   which is beyond the sweep extreme. The page gives no general stop rule
   beyond the example.
8. **Targets.** Take partials at logical targets (swing levels or the next
   FVG). The example's target was the pre-market lows and the equal lows
   under the range.
9. **Manage.** Trail the stop to protect profit once the move confirms.
10. **Execution limits.** **Two trades per session at most.** **After two
    losses, stop for the day.** Size down on the day before major news and
    during known accumulation. Stand aside when there is no clear bias or
    structure.

## Risk management

- **Session cap:** at most two trades. Two losses end the day.
- **Sizing:** smaller on days before major news and during accumulation.
  The base risk per trade ($ or %) is not specified in the playbook.
- **Stop:** beyond the manipulation extreme, shown only in the example.
- **No chase:** if the price never retraces into the FVG, there is no
  trade.
- **Daily dollar or weekly limit:** not specified in the playbook, beyond
  the two-loss stop.

## What the playbook leaves unspecified

- A general stop rule and the reward-to-risk minimum. Only the example
  shows a stop, and no R:R figure is given.
- How large a displacement must be, and how big or which kind of FVG is
  valid (the first FVG, or the largest).
- Which timeframe the displacement must show on. The overview says the
  higher timeframe, while the timeframe section says 1m, 5m or 15m; the
  page does not reconcile the two.
- How heavy a Nasdaq–S&P divergence must be to skip a day.
- Whether trades outside the macro windows are allowed, and how the 8:30
  release fits with the 9:50 to 10:10 window.
- How large partials should be, and the rules for trailing.
- Whether FOMC afternoons follow the same timing.

## Evidence & claims

- **CPI short example:** about **100 points on NQ within minutes**.
  Self-reported (T4).
- The page claims **no win rate, R:R figure or payout**. No expectancy
  check is possible.

## Concepts & lineage

- The Accumulation, Manipulation, Distribution cycle →
  [[concept_amd_power_of_three]]
- Liquidity built in the range, then swept → [[concept_liquidity]],
  [[concept_liquidity_sweep_reversal]]
- A forceful break of a swing high or low as confirmation →
  [[concept_market_structure]]
- Displacement that leaves an FVG, with the retrace into it as entry →
  [[concept_fair_value_gap]]
- Classifying days by scheduled high-impact news →
  [[concept_news_trading]], [[concept_market_regimes]]
- Nasdaq–S&P alignment check → [[concept_intermarket_analysis]]
- HTF draw on liquidity with an LTF trigger →
  [[concept_multi_timeframe_analysis]]
- The 9:50 to 10:10 and 10:50 to 11:10 ET macro windows →
  [[concept_trading_sessions_killzones]]
- Partials and trailing stops → [[concept_trade_management]]
- Lineage (editorial, not stated on the page): Dow-style phases, then the
  Wyckoff spring and upthrust, then ICT Power of Three →
  [[concept_wyckoff_method]]

## Changes vs. earlier note

- **Confirmed:** the AMD sequence, trading only after a liquidity sweep and
  confirmed displacement, the focus on major news events, and the chop
  filter. The earlier note had these from T3 TradeZella wording; the
  playbook now confirms them at T2.
- **Refined: confirmation is "displacement / BOS".** The earlier note
  said "displacement / BOS" (T3). The playbook defines displacement as a
  forceful break of a swing high or low **that leaves an FVG**, and the
  entry is the **retrace into that FVG**. If price does not retrace, there
  is no trade.
- **Added:** the high and low probability day lists (including skipping
  the day before CPI, FOMC or NFP), the Nasdaq–S&P correlation check, the
  rule requiring a clear draw on liquidity, the timeframe stack, the
  two-trades and two-losses session cap, sizing down before news, the
  9:50 to 10:10 and 10:50 to 11:10 ET macro windows, partials and
  trailing, and the CPI example.
- **Lineage marked as editorial.** The Dow, Wyckoff, ICT PO3 chain from
  the earlier note is kept but does not appear on the page.
- **Sources.** The earlier note already cited this Chart Fanatics page
  (T2), so it stays as the first source, with no duplicate entry added.
  TradeZella (T3) is kept unchanged.
