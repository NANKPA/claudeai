---
id: concept_time_series_statistics
type: concept
title: Time-Series Statistics (stationarity, autocorrelation, cointegration)
partition: 07_concepts
layer: L0
aliases: [stationarity, autocorrelation, cointegration, GARCH, ARIMA]
related: [concept_stochastic_processes, concept_volatility, concept_mean_reversion, concept_backtesting, concept_machine_learning_finance]
influenced_by: [person_robert_engle, person_ruey_tsay]
status: synthesized
---

# Time-Series Statistics

**Why it matters.** Almost every "pattern" is a claim about the
autocorrelation structure of returns. You cannot evaluate a pattern without
these tools.

## Toolkit

- **Stationarity.** Prices are non-stationary (unit root). Returns are
  roughly stationary in mean, but not in variance. Test with ADF or KPSS.
- **Autocorrelation (ACF/PACF).** Positive autocorrelation of returns means
  momentum; negative means mean reversion. Daily index returns have near-zero
  autocorrelation. *Squared* returns are strongly autocorrelated: volatility
  clusters.
- **Volatility models.** ARCH (Engle, 1982), GARCH(1,1) (Bollerslev, 1986).
  Forecasting volatility is far easier than forecasting direction, and it
  drives position sizing ([[concept_position_sizing]]).
- **Cointegration** (Engle-Granger, Johansen). Two non-stationary series
  whose linear combination is stationary is the basis of pairs and spread
  trading ([[concept_mean_reversion]]).
- **Hurst exponent / variance ratio.** H > 0.5 means trending, H < 0.5 means
  mean-reverting. Use it as a regime diagnostic ([[concept_market_regimes]]).
- **Structural breaks.** Relationships change. Test for them, and prefer
  rolling or walk-forward estimates ([[concept_overfitting_validation]]).

## Pitfall: fractional differentiation

Integer differencing (returns) makes a series stationary but erases memory.
López de Prado proposes fractional differentiation to keep memory while
achieving stationarity, a useful idea for ML features
([[concept_machine_learning_finance]]).
