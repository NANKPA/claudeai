---
id: concept_trade_management
type: concept
title: Trade Management (stops, targets, breakeven, scaling, trailing)
partition: 07_concepts
layer: L5
aliases: [stop loss, take profit, breakeven, scaling in, scaling out, pyramiding, trailing stop, partials, time stop]
related: [concept_trade_execution, concept_risk_reward_r_multiples, concept_position_sizing, concept_volatility, concept_expectancy]
influenced_by: [person_jesse_livermore, person_van_tharp]
status: synthesized
---

# Trade Management

BabyPips Senior covers stop-loss placement and scaling in and out.

## Stops

- **Structural:** beyond the level that invalidates the idea (the sweep
  extreme, the swing low). Preferred in SMC/AMT playbooks.
- **Volatility:** k × ATR ([[concept_volatility]]).
- **Time stop:** exit if the expected move hasn't happened within N bars
  (also one barrier of triple-barrier labelling).
- **Stops are not guarantees.** Gaps and fast markets slip
  ([[concept_probability_fat_tails]]).

## Targets

- The **opposing liquidity pool** or HTF level (SMC).
- The **other side of value / POC** (AMT).
- **Measured move** (patterns, Marci Silfrain).
- **R-multiple** targets (2R, 3R) or a trailing exit (trend following).

## Breakeven

Moving the stop to entry early cuts losers to scratches *and* cuts winners
that retest. Trader Kane's model uses **aggressive breakeven management**
(T3). This changes the win/loss distribution, so measure its net effect in
your journal ([[concept_trading_journal_review]]).

## Scaling

- **Pyramiding into winners** (Livermore; Turtles added units every ½N).
- **Scaling out** (partials) smooths equity but lowers average R.
- Never **average into losers** without a predefined total risk.

## Case: TG Capital (T2/T3)

Minimum target **1:20 R:R** from entry vs stop. Exit early if the EMA stack
breaks or price closes through the stop level. One trade at a time; new FVG
setups are ignored until the position closes.
