---
id: concept_moving_averages
type: concept
title: Moving Averages (SMA, EMA, stacks, crossovers)
partition: 07_concepts
layer: L3
aliases: [SMA, EMA, moving average crossover, golden cross, death cross, EMA stack, 200-day moving average, 9 21 EMA]
related: [concept_trend_following, concept_market_regimes, concept_vwap, concept_oscillators_momentum]
influenced_by: [person_richard_donchian, person_gerald_appel]
status: synthesized
---

# Moving Averages

BabyPips Elementary Grade 4. A lagging smoother of price that defines trend
and dynamic support.

| Type | Formula | Note |
|---|---|---|
| SMA(n) | mean of last n closes | Equal weights |
| EMA(n) | `EMA_t = α·P_t + (1−α)·EMA_{t−1}`, `α = 2/(n+1)` | Reacts faster |

## Uses

1. **Trend filter.** Price above the 200-day SMA means long-only. This is a
   classic regime rule, documented to reduce drawdowns in equity indices.
2. **Crossovers.** Fast/slow MA cross (Donchian's era onwards). Simple trend
   following is profitable over long histories in futures, at the cost of
   whipsaw in ranges ([[concept_trend_following]]).
3. **EMA stacks.** Alignment of several EMAs as a trend-quality gate.
   **TG Capital** requires the **5, 9, 13 (or 15), and 21 EMAs stacked**; if
   they are tangled or crossing, *no trade* (`strategy_tg_capital_trident`).
4. **Dynamic support.** The 10/21 EMA in strong growth-stock trends
   (Minervini, Kell), and the 20 EMA in Al Brooks' price action.

## Pitfalls

Lag means late entries and exits. Parameter fishing (finding "the best" MA
length) is a classic overfitting trap ([[concept_overfitting_validation]]).
