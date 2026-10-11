---
id: concept_market_regimes
type: concept
title: Market Regimes (trend vs range, high vs low volatility)
partition: 07_concepts
layer: L2
aliases: [regime, trending market, ranging market, balance, imbalance, volatility regime, risk-on risk-off]
related: [concept_auction_market_theory, concept_volatility, concept_trend_following, concept_mean_reversion, concept_time_series_statistics, concept_fundamental_macro_analysis]
status: synthesized
---

# Market Regimes

**The most important filter in trading: what *kind* of market is this?** The
same setup has opposite expectancy in different regimes.

## A 2×2 that covers most of it

| | **Low volatility** | **High volatility** |
|---|---|---|
| **Trending / imbalanced** | Grind: pullback entries, trailing stops ([[concept_trend_following]]) | Expansion: breakouts, momentum, wide stops ([[concept_breakout_trading]]) |
| **Ranging / balanced** | Rotation: fade edges to POC/VWAP ([[concept_mean_reversion]]) | Chop: whipsaw; reduce size or stand aside |

## Detectors

- **AMT.** Balance vs imbalance, value migration, day type
  ([[concept_auction_market_theory]]).
- **Structure.** Clean HH/HL vs overlapping swings ([[concept_market_structure]]).
- **Statistics.** ADX, Hurst exponent, variance ratio, efficiency ratio
  (Kaufman), realized-vol percentile ([[concept_time_series_statistics]]).
- **Moving-average alignment.** Stacked, fanning EMAs mean a trend. Tangled
  EMAs mean range. TG Capital's rule: *if the EMAs are crossing or tangled,
  the setup is invalid* (`strategy_tg_capital_trident`).
- **Macro.** Rate-cycle, liquidity and risk-on/off regimes
  ([[concept_fundamental_macro_analysis]]).

## Practitioner notes

- Clement Ang frames system rules around *when he is allowed to be
  aggressive* and which entry styles suit choppy markets (TraderLion Q&A).
  That is regime gating in plain language.
- Fabio Valentini runs **two models**: trend continuation when the market is
  out of balance, mean reversion when breakouts fail back into balance.
