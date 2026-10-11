---
id: concept_risk_reward_r_multiples
type: concept
title: Risk:Reward & R-Multiples
partition: 07_concepts
layer: L6
aliases: [risk reward, R multiple, RR, 1R, reward to risk, breakeven win rate]
related: [concept_expectancy, concept_position_sizing, concept_trade_management, concept_multi_timeframe_analysis]
influenced_by: [person_van_tharp]
status: synthesized
---

# Risk:Reward & R-Multiples

**1R = the amount you risk on a trade** (entry to stop × size). Every outcome
is expressed as a multiple of R (Van Tharp).

## Breakeven win rate

`p_breakeven = 1 / (1 + RR)`

| R:R | Breakeven win rate |
|---|---|
| 1:1 | 50% |
| 1:1.5 | 40% |
| 1:2 | 33.3% |
| 1:3 | 25% |
| 1:5 | 16.7% |
| 1:20 | 4.8% |

## Sanity check on marketing claims

A video titled "90% win rate … (1:20+ RR)" (TG Capital on Chart Fanatics)
implies an expectancy of `0.9×20 − 0.1×1 = +17.9R per trade`. That is
implausible for any real strategy. An independent EA reconstruction tested
on EURUSD M30 found a **~20% win rate** with large winners, still profitable
out-of-sample for 2023–24 (T3, single self-published backtest). **The
strategy may be real; the headline is not** ([[concept_expectancy]]).

## Planned vs realised R

Planned R:R is a hypothesis. Realised R depends on how often the target is
reached before the stop. Track MAE/MFE (max adverse/favourable excursion) in
the journal to tune stops and targets ([[concept_trading_journal_review]]).
