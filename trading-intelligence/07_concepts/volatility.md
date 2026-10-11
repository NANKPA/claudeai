---
id: concept_volatility
type: concept
title: Volatility (realized, implied, ATR, regimes)
partition: 07_concepts
layer: L0
aliases: [ATR, average true range, implied volatility, realized volatility, VIX]
related: [concept_probability_fat_tails, concept_options_greeks, concept_position_sizing, concept_market_regimes, concept_bollinger_bands, concept_time_series_statistics]
influenced_by: [person_welles_wilder, person_sheldon_natenberg]
status: synthesized
---

# Volatility

**Definition.** The dispersion of returns, usually the annualised standard
deviation of log returns. It is the single most useful number in trading.
It sets stop distance, position size, target realism, and options prices.

## Measures

| Measure | Formula / idea | Use |
|---|---|---|
| **Realized (historical) vol** | `σ_annual = stdev(daily log returns) × √252` | Risk budgeting, vol targeting |
| **ATR** (Wilder, 1978) | EMA of true range = max(H−L, \|H−C₋₁\|, \|L−C₋₁\|) | Stop placement and position sizing in price units |
| **Implied vol** | Vol that equates an option model price to the market price | Market's forecast plus a risk premium; VIX for the S&P 500 |
| **Parkinson / Garman-Klass** | Range-based estimators | More efficient than close-to-close |

## Stylised facts

- **Clustering.** High-vol days follow high-vol days (GARCH, see
  [[concept_time_series_statistics]]).
- **Leverage effect.** Equity vol rises when prices fall (negative
  spot-vol correlation).
- **Implied usually exceeds realized.** That gap is the *variance risk
  premium*, the edge behind short-vol strategies (and their tail risk).
- **Vol mean-reverts.** Compression precedes expansion. This is the basis of
  squeeze and breakout setups ([[concept_breakout_trading]],
  [[concept_bollinger_bands]]).

## Execution & risk rules derived from vol

1. **Size inversely to volatility:** `units = (equity × risk%) / (k × ATR × point value)`.
   This is the Turtle "N" unit rule ([[concept_position_sizing]]).
2. **Stops in ATR multiples** adapt to regime. A fixed-pip stop does not.
3. **Expected daily range ≈ ATR.** A target of 3× ADR on an intraday
   scalp is unrealistic.
