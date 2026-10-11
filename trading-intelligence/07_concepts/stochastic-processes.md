---
id: concept_stochastic_processes
type: concept
title: Stochastic Processes (Brownian motion, Itô, mean-reverting OU)
partition: 07_concepts
layer: L0
aliases: [Brownian motion, geometric Brownian motion, Ornstein-Uhlenbeck, Ito calculus]
related: [concept_random_walk_efficient_markets, concept_options_greeks, concept_volatility, concept_mean_reversion, concept_optimal_execution_market_impact]
influenced_by: [person_louis_bachelier, person_kiyosi_ito, person_steven_shreve]
status: synthesized
---

# Stochastic Processes

The mathematical language for prices that evolve randomly through time.

| Process | SDE | Use in trading |
|---|---|---|
| **Arithmetic Brownian motion** | `dS = μ dt + σ dW` | Bachelier's 1900 model; short-horizon price approximations, the Almgren-Chriss execution model |
| **Geometric Brownian motion** | `dS = μS dt + σS dW` | Black-Scholes-Merton; log-normal prices |
| **Ornstein-Uhlenbeck** | `dX = θ(μ − X) dt + σ dW` | Mean-reverting spreads, pairs trading, the half-life of reversion ([[concept_mean_reversion]]) |
| **Jump-diffusion** | GBM + Poisson jumps | Gap risk, earnings, news shocks ([[concept_news_trading]]) |
| **Stochastic volatility (Heston)** | variance follows its own mean-reverting process | Volatility smile, [[concept_volatility]] |

## Itô's lemma (the one formula to know)

For `f(S,t)`: `df = (∂f/∂t + μS ∂f/∂S + ½σ²S² ∂²f/∂S²) dt + σS ∂f/∂S dW`.
The `½σ²` term is why volatility drags on compounded growth: the geometric
mean return is about `μ − σ²/2`. That is the same mathematics behind
volatility drag in leveraged positions and behind the Kelly growth-rate
formula ([[concept_kelly_criterion_optimal_f]]).

## Practical takeaways

- **Half-life of mean reversion** = `ln(2)/θ`. Estimate it before trading a
  reversion setup.
- **The square-root-of-time rule** (`σ√t`) scales volatility across
  timeframes. It underlies ATR-based stops across
  [[concept_multi_timeframe_analysis]].

Standard references: Shreve, *Stochastic Calculus for Finance I & II*; MIT
18.S096 lectures (see `06_mathematics-foundations`).
