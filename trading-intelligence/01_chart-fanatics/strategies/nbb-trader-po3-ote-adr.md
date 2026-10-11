---
id: strategy_nbb_trader_po3_ote_adr
type: strategy
title: "NBB Trader — PO3, OTE + ADR: Market Maker Model with Fixed-R Fib Entries (forex, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [PO3 OTE ADR Forex Playbook, Market Maker Model + OTE, Smart Money Reversal OTE, NBB Trader strategy]
taught_by: [person_nbb_trader]
featured_in: [channel_chart_fanatics]
uses: [concept_amd_power_of_three, concept_premium_discount_ote, concept_fibonacci, concept_order_blocks_breakers, concept_fair_value_gap, concept_liquidity, concept_liquidity_sweep_reversal, concept_market_structure, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_risk_reward_r_multiples, concept_trade_management]
derived_from: [concept_smart_money_concepts, concept_amd_power_of_three]
related: [strategy_tg_capital_trident, strategy_trader_mayne_structure_ote, strategy_tanja_amd_futures, strategy_trader_kane_lab_model]
sources:
  - {title: "Chart Fanatics — PO3, OTE + ADR Forex Playbook", url: "https://www.chartfanatics.com/strategies/po3-ote-adr", tier: T2}
status: verified-t2
---

# NBB Trader — PO3, OTE + ADR: Market Maker Model with Fixed-R Fib Entries (forex, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/po3-ote-adr. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits NBB Trader with this forex playbook,
which combines a Market Maker Model with Optimal Trade Entry Fibonacci
levels. The page gives no biography.

## Built for

- **Instruments:** forex.
- **Style:** labelled swing trading. Execution, however, runs inside
  intraday session windows; see the gaps section.
- **Timeframes:** **Daily and 4H** for bias and PD arrays. **15m or 30m**
  to confirm the breaker and displacement. **5m** only to refine an entry
  after confirmation, for example from a 5m FVG. **No 1m charts**; the page
  says to avoid them unless highly experienced.
- **Sessions (New York time):** **London Open 2–5 AM**, **New York Open
  7–10 AM**, **London Close 10 AM–12 PM**. London Close works best when a
  large move has already started earlier in the day.

## Core idea

The Market Maker Model reads each day as **accumulation** (a tight range,
often in Asia), **manipulation** (a break of that range to trap traders,
often at London) and **distribution** (the real move the other way, often
in New York). Trade only distribution in the direction of a pre-set
higher-timeframe bias. Confirm it at a key level with a Smart Money
Reversal: a breaker pattern plus a displacement candle. Then enter on a
Fibonacci pullback into the OTE zone. Because the stop sits at the 1.0
level and the first target at 0.0, the R-multiple is fixed by the entry
level, whatever the size of the range.

## Rules

1. **Set the bias before the day.** Use the weekly and daily charts. If
   they are bearish, look only for shorts. Never trade both directions.
   The bias also tells you which side is accumulation and which is
   distribution.
2. **Price must open near a key level (PD array).** Valid levels:
   previous day high or low; previous week high or low; daily or 4H FVGs;
   daily or 4H order blocks; daily or 4H breaker blocks; mitigation blocks.
   If price opens far from one, skip the trade.
3. **Trade only in the session windows** listed above.
4. **Wait for the manipulation to finish** and distribution to start in
   your direction. In the worked example, London ran above the previous
   day's high and that sweep made the high of the day.
5. **Confirm with a Smart Money Reversal on the 15m or 30m chart.** Both
   parts are required:
   - *Breaker structure:* for a short, a high, a low, a higher high, then
     a lower low. The page notes some traders call this a head and
     shoulders. The page shows only the short version; longs are
     presumably the mirror image.
   - *Displacement:* a strong candle that **closes with its body** (not just
     a wick) beyond the key level.
   - If displacement is weak, or another PD array is in the way, skip that
     entry and wait for a second pullback.
6. **Draw the Fibonacci** from the swing created by the manipulation to the
   swing created by the displacement (high to low for a short).
7. **Enter only on a pullback into 0.50, 0.62 or 0.705**, with 0.79 as an
   optional deeper level. If price does not retrace at least to **0.50**,
   there is no trade. The 5m can be used to refine the entry.
8. **Stop:** the default is the **1.0 level** (the swing extreme). The
   tighter option is **0.90**.
9. **First take-profit:** always the **0.0 level**.
10. **Break-even:** once price **closes past the 0.20 level**, move the stop
    to break-even.
11. **Let it run if it breaks through:** if price closes through the TP with
    momentum, keep the position, trail the stop, and use the old TP as the
    new stop.
12. **Scaling in:** add a second entry, with new risk, only when the first
    is at break-even or better. Never add while the first position still
    carries full risk.

## Risk management

- **Fixed geometry:** stop at 1.0 (or 0.90), target at 0.0. Risk and reward
  are set by the entry level, not by the size of the range.
- **Break-even** at a close past 0.20, and no scaling while the first
  position is at full risk.
- **Risk per trade ($ or %), position size, maximum trades, and daily or
  weekly loss limits:** Not specified in the playbook.
- **Skip conditions:** price opening far from a PD array, weak
  displacement, an opposing PD array in the way, or no pullback to at
  least 0.50.

## What the playbook leaves unspecified

- **ADR.** The title names it (presumably Average Daily Range), but the
  page never defines it or says how it is used.
- How "close to a key level" is measured at the open.
- How to grade swings and choose the fib anchors when several swings
  qualify. The page admits this takes practice.
- How the swing-trading label fits the session-based entries: how long a
  trade is held, and whether it is closed at session or day end.
- When the optional 0.79 entry should be used, and how the 1.0 versus 0.90
  stop is chosen.
- Whether part of the position is closed at the 0.0 TP or all of it, and
  how the runner's trail is managed beyond using the old TP as a stop.
- How many trades per day or session, and which session takes priority
  when more than one sets up.
- A definition of mitigation blocks, and how to weigh competing PD arrays.

## Evidence & claims

- The page reports **no win rate, P&L or payout**. The worked example
  (London sweep of the previous day's high, breaker and displacement,
  entry in the 0.62–0.705 zone) gives no result.
- **The fixed R-multiples on the page do not match its own geometry**
  (our arithmetic, not stated on the page). The page lists 50% ≈ 1.63R,
  62% ≈ 2.38R and 70.5% ≈ 3.75R. With the stop at 1.0 and the target at
  0.0, the R at an entry level x is x ÷ (1 − x):
  - 0.50 → **1.00R**
  - 0.62 → **1.63R**
  - 0.705 → **2.39R**
  - 0.79 → **3.76R**
  The page's numbers are each one level off; they belong to the next
  deeper entry. With the tighter 0.90 stop the values are 1.25R, 2.21R,
  3.62R and 7.18R.
- Break-even win rates for the corrected stop-at-1.0 values: 50% at 0.50,
  about 38% at 0.62, about 30% at 0.705 and about 21% at 0.79. Without a
  reported win rate, no expectancy check is possible.
- The pros list calls the R levels fixed and the approach consistent.
  These are claims about design, not measured outcomes.

## Concepts & lineage

- Accumulation, manipulation, distribution across Asia, London and New
  York → [[concept_amd_power_of_three]]
- Session windows → [[concept_trading_sessions_killzones]]
- Previous day and week highs and lows as liquidity, and the manipulation
  sweep → [[concept_liquidity]], [[concept_liquidity_sweep_reversal]]
- FVGs as PD arrays and 5m refinement → [[concept_fair_value_gap]]
- Order, breaker and mitigation blocks; the breaker pattern in the Smart
  Money Reversal → [[concept_order_blocks_breakers]]
- Displacement with a body close, structure shift →
  [[concept_market_structure]]
- OTE retracement zone (0.62–0.79) → [[concept_premium_discount_ote]]
- Fibonacci anchors, entries, stop, target and the 0.20 break-even level →
  [[concept_fibonacci]]
- Daily and 4H, then 15m or 30m, then 5m → [[concept_multi_timeframe_analysis]]
- R fixed by entry level → [[concept_risk_reward_r_multiples]]
- Break-even, trailing past TP, scaling only when risk-free →
  [[concept_trade_management]]
- Lineage (our attribution; the page does not name ICT): ICT smart-money
  concepts and the PO3 / Market Maker Model →
  [[concept_smart_money_concepts]], [[concept_amd_power_of_three]]
