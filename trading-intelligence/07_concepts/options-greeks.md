---
id: concept_options_greeks
type: concept
title: Options & the Greeks
partition: 07_concepts
layer: L0
aliases: [delta, gamma, theta, vega, Black-Scholes, gamma exposure, GEX]
related: [concept_volatility, concept_stochastic_processes, concept_probability_fat_tails, concept_market_sentiment]
influenced_by: [person_fischer_black, person_sheldon_natenberg, person_nassim_taleb]
status: synthesized
---

# Options & the Greeks

**Black-Scholes-Merton (1973)** prices a European option by constructing a
riskless hedge of option and stock. The price depends on volatility, not on
expected return.

`C = S·N(d₁) − K·e^{−rT}·N(d₂)`, with `d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T)` and `d₂ = d₁ − σ√T`.

| Greek | Sensitivity to | Trader meaning |
|---|---|---|
| **Delta (Δ)** | underlying price | Directional exposure; roughly the probability of finishing in the money |
| **Gamma (Γ)** | change in delta | Convexity. Long gamma gains from movement, short gamma loses. |
| **Theta (Θ)** | time | Daily decay. The price of holding gamma. |
| **Vega (ν)** | implied vol | Exposure to the vol level |
| **Rho (ρ)** | rates | Mostly minor, except for long-dated options |

**Core identity:** for a delta-hedged option, P&L ≈ ½Γ·S²·(σ²_realized − σ²_implied)·dt.
You profit from options when realized vol beats the implied vol you paid.

## Why non-options traders care

- **Dealer gamma positioning** (GEX) changes intraday behaviour. When dealers
  are long gamma they dampen moves, which helps mean reversion. When they are
  short gamma they amplify moves, which helps breakouts. This links to
  [[concept_market_regimes]].
- **Options flow** is a sentiment and positioning input
  ([[concept_market_sentiment]]). Chart Fanatics features options-flow traders
  (see `strategy_brando_options_swing`).
- **Short-vol payoffs** resemble high-win-rate strategies: small frequent
  gains and rare huge losses ([[concept_probability_fat_tails]]).

References: Natenberg, *Option Volatility & Pricing*; Hull, *Options, Futures,
and Other Derivatives*; Taleb, *Dynamic Hedging*.
