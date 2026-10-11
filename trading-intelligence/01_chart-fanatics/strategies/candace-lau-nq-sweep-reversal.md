---
id: strategy_candace_lau_nq_sweep_reversal
type: strategy
title: "Candace Lau — NQ Liquidity Sweep & IFVG Reversal (NQ futures, scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [NQ Liquidity Sweep & IFVG Scalping Strategy, NQ Liquidity Sweep & Reversal Scalping Strategy, Candace Lau strategy, NQ liquidity sweep reversal]
taught_by: [person_candace_lau]
featured_in: [channel_chart_fanatics]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_premium_discount_ote, concept_fair_value_gap, concept_market_structure, concept_multi_timeframe_analysis, concept_amd_power_of_three, concept_trading_sessions_killzones, concept_smt_divergence, concept_scalping, concept_risk_reward_r_multiples, concept_trade_management, concept_position_sizing, concept_prop_firm_risk_rules]
derived_from: [concept_smart_money_concepts, concept_amd_power_of_three]
related: [strategy_marco_trades_liquidity_grab, strategy_trader_kane_lab_model, strategy_tanja_amd_futures]
sources:
  - {title: "Chart Fanatics — NQ Liquidity Sweep & IFVG Scalping Strategy", url: "https://www.chartfanatics.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists NQ Liquidity Sweep & Reversal Scalping Strategy by Candace Lau)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "TradeZella — NQ Liquidity Sweep & Reversal Scalping Strategy", url: "https://www.tradezella.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy", tier: T3}
status: verified-t2
---

# Candace Lau — NQ Liquidity Sweep & IFVG Reversal (NQ futures, scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Candace Lau scalps NQ futures, taking reversals after liquidity
sweeps in the London and New York sessions. The page text itself does not
name her or describe her background (attribution comes from the index
listing); its risk section uses a prop-account example.

## Built for

- **Instruments:** futures, specifically NQ. MNQ is the fallback when the
  structural stop would mean too many dollars at risk. ES is used only as an
  SMT comparison.
- **Style:** scalping.
- **Timeframes:** Daily and 1H for context and targets. **1-minute** for
  execution. 15-second and 3-second charts to judge the speed of
  displacement and to refine aggressive entries. Suggested learning order:
  5-minute, then 1-minute, then seconds charts.
- **Sessions:** **London, about 2:00 to 5:00 AM ET**. Never enter before
  2:00, and watch 2:30, 3:00 and 3:30 for expansion. **New York** uses the
  same model in a faster, more volatile setting, especially around the
  open.

## Core idea

NQ often reverses after it takes a meaningful pool of liquidity. Build
context on the higher timeframes, mark the liquidity price is likely to
target, and wait for the sweep. The sweep itself is not the entry. Enter
only when the reversal is confirmed by an **Inversion Fair Value Gap
(IFVG)** together with **fast, decisive displacement**, then aim for the
next low-resistance liquidity. The page frames the sequence as
accumulation, manipulation (the sweep) and distribution. The Asia-to-London
transition is a prime place to read it.

## Rules

1. **Higher-timeframe context (Daily, 1H).** Mark Daily and 1H highs and
   lows, Daily and 1H FVGs (the **1H FVG** gets special weight), the prior
   session's and prior day's liquidity, and equal highs and lows.
2. **Premium or discount.** Note where price sits in the relevant range.
   This is context only, not a signal.
3. **Find the liquidity pool.** For a long, sell-side liquidity below
   price. For a short, buy-side liquidity above it. In London the Asia
   range high and low are the default. If Asia already trended, use
   earlier highs and lows, Daily or 1H liquidity, FVGs, the Midnight Open,
   or the NDOG and NWOG (new day and new week opening gaps) instead.
4. **Respect the window.** London 2:00 to 5:00 AM ET, with no entries
   before 2:00. In New York, also map the **RTH gap** at its 25%, 50%, 75%
   and 100% levels, and use **NQ against ES SMT divergence** at key highs
   and lows as supporting confluence only.
5. **Wait for the sweep.** Price must actually take the identified
   liquidity. Price can sweep and keep going, so a sweep alone is never an
   entry.
6. **IFVG confirmation.** In a bullish case, price leaves a bearish FVG on
   the way down into sell-side liquidity. After the sweep, it trades back
   up and closes through that gap, which turns it into a bullish IFVG. A
   bearish case is the mirror image.
   - *Conservative:* require a clear candle-body close through the original
     FVG. A slight poke through it does not count.
   - *Aggressive:* use seconds charts to spot displacement and a smaller
     inversion forming before the 1-minute confirmation completes. This
     gives an earlier entry and possibly a tighter stop, with less
     confirmation.
7. **Displacement and speed.** The reaction away from the sweep must be
   fast and decisive. Do not judge it from the finished candle alone,
   because a big candle can still have formed slowly and choppily.
8. **Entry.** On a retracement into the inversion area, on the 1-minute
   chart. A bracket order can set the stop and first target at entry.
9. **Stop.** Beyond the structure that invalidates the setup: the relevant
   swing, the manipulation extreme, or a supporting order block. Size it to
   volatility. Examples given are about **20 to 25 NQ points in London,
   30 to 40 in New York, and about 15 in quieter periods**, described as
   examples rather than fixed values. If a valid entry needs an excessively
   wide stop, rethink the entry. If the stop is correct but the dollar risk
   is too large, cut size or switch to MNQ.
10. **Target.** Low-resistance liquidity in the direction of the trade:
    opposite swing highs or lows, equal highs or lows, 1H FVGs, session
    liquidity, the Midnight Opening Price, NDOG or NWOG, and RTH gap levels
    in New York. **At least 1:2 R:R.** Set the bracket at about 1:2 and
    widen it to 1:3 or 1:4 when the liquidity target allows. Take the
    planned scalp; there is no need to hold for the whole session move.
11. **Manage.** Once price confirms and takes minor liquidity, tighten the
    stop behind the newly formed structure. This need not mean an instant
    move to breakeven. The pattern is entry, confirmation, minor liquidity
    taken, reduced risk, target or partial, then trail the rest. Decide the
    profit-taking method (fixed target, partials or trailing) in advance
    and test which works best.
12. **Size by quality.** A setup with more aligned references (HTF FVGs,
    equal highs or lows, session liquidity, gap levels) can carry more
    conviction. A weaker one, with fewer confluences, nearby unresolved
    liquidity, a late entry or worse R:R, gets smaller size, less scaling
    and more conservative profit-taking.

## Risk management

- **Daily limit:** set it as a maximum dollar or % loss rather than a fixed
  number of trades. In one prop example, an account of about **$160,000**
  (after building a buffer) ran a daily loss limit of about **$3,000**. The
  page says this is an example, not a recommendation.
- **Personal capital:** risk a percentage of the account. The exact % is
  not specified in the playbook.
- **Prop accounts:** set position size with drawdown, consistency rules and
  account size in mind.
- **Per-trade risk:** comes from the structural stop and adjusts with
  volatility. A fixed $ or % per trade is not specified in the playbook.
- **Minimum reward-to-risk:** 1:2.

## What the playbook leaves unspecified

- An objective test for "displacement and speed", such as a time or
  distance threshold.
- How the premium and discount range is drawn (which swing points) and
  whether a trade must sit in discount for longs or premium for shorts.
- New York session hours beyond "around the open", and a cutoff time for
  London after 5:00 AM.
- How many trades are allowed per session, and what to do after a loss.
- How many confluences make a setup "stronger", and how size changes with
  that grade.
- The size of partials and the rules for trailing, which the page leaves
  to the trader's own testing.

## Evidence & claims

- **London bearish example:** about **40 to 50 NQ points in about nine
  minutes**, closed at the planned liquidity target. Self-reported (T4).
- The page gives **no win rate**. The 1:2 minimum, widened to 1:3 or 1:4,
  is a rule, not a reported result. At 1:2 the break-even win rate is
  about 33%. Without a stated win rate, no expectancy check is possible.
- The ~$3,000 daily limit on a ~$160k account describes how risk was
  managed, not a P&L claim.

## Concepts & lineage

- Swing, equal and session highs and lows as liquidity pools; low-resistance
  liquidity as targets → [[concept_liquidity]]
- Sweep, then confirmed reversal → [[concept_liquidity_sweep_reversal]]
- Accumulation, manipulation, distribution; Asia range swept in London →
  [[concept_amd_power_of_three]]
- FVG to IFVG inversion as the entry structure, with 1H FVGs as context and
  targets → [[concept_fair_value_gap]]
- Displacement and closes through structure → [[concept_market_structure]]
- Premium and discount framing → [[concept_premium_discount_ote]]
- Daily and 1H context with 1-minute and seconds-chart execution →
  [[concept_multi_timeframe_analysis]]
- The London 2:00 to 5:00 AM ET window and New York open timing →
  [[concept_trading_sessions_killzones]]
- NQ against ES at key highs and lows → [[concept_smt_divergence]]
- Bracket orders, 1:2 minimum widened to 1:3 or 1:4 →
  [[concept_risk_reward_r_multiples]], [[concept_scalping]]
- Reducing risk behind new structure, partials and trailing →
  [[concept_trade_management]]
- Size by setup quality, MNQ fallback, daily dollar limit →
  [[concept_position_sizing]], [[concept_prop_firm_risk_rules]]
- Lineage: ICT-style smart-money concepts → [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **Five-step rule order confirmed.** The earlier note's sequence (HTF and
  premium/discount, then liquidity pool, then sweep, then IFVG with
  displacement and speed, then lower-timeframe execution) came from T3
  sources. The playbook now confirms it at T2 as six named factors.
- **Name.** The earlier note used the index listing "NQ Liquidity Sweep &
  Reversal Scalping". The page itself is titled **"NQ Liquidity Sweep &
  IFVG Scalping Strategy"**. Both are kept as aliases.
- **"Lower timeframe" made precise.** The earlier note said only "execute on
  the lower timeframe". The playbook names the **1-minute** as the primary
  execution chart, with 15-second and 3-second charts for judging speed.
- **R:R confirmed and extended.** The 1:2 minimum is confirmed. The
  playbook adds widening the bracket to 1:3 or 1:4 when the target allows.
- **Added:** the London window (2:00 to 5:00 AM ET, nothing before 2:00);
  fallback liquidity references when Asia trends (Midnight Open, NDOG,
  NWOG); the New York RTH gap quartiles; NQ against ES SMT as confluence;
  conservative and aggressive IFVG confirmation; stop ranges by session and
  the MNQ fallback; the trade-management sequence; sizing by setup quality;
  and the daily loss limit example.
- **Added `uses`:** AMD/PO3, sessions, SMT, trade management, position
  sizing and prop-firm rules, because the playbook relies on each of them.
