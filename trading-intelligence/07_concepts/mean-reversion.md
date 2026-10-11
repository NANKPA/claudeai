---
id: concept_mean_reversion
type: concept
title: Mean Reversion
partition: 07_concepts
layer: L4
aliases: [mean reversion, fade, reversion to fair value, POC reversion, VWAP reversion, pairs trading, statistical arbitrage]
related: [concept_auction_market_theory, concept_volume_profile, concept_vwap, concept_bollinger_bands, concept_oscillators_momentum, concept_stochastic_processes, concept_market_regimes]
contrasts_with: [concept_trend_following]
status: synthesized
---

# Mean Reversion

**Price deviates from a reference "fair value" and tends to return.** The
reference can be POC, VWAP, a moving average, a pair spread, or JJ Simon's
NY-open fair price.

## Where it is valid

- **Balanced markets** (AMT), ranges, low-vol regimes ([[concept_market_regimes]]).
- **Short horizons** for indices (overreaction).
- **Cointegrated spreads** (pairs/stat-arb), modelled as Ornstein-Uhlenbeck
  ([[concept_stochastic_processes]]); trade when the z-score is beyond ±2.

## Chart Fanatics implementations

| Trader | Reference | Rule highlight |
|---|---|---|
| Fabio Valentini | POC | When breakout attempts fail and price returns to balance, revert to POC (T2/T3) |
| JJ Simon | NY open / pre-open fair price | Reversion unless fundamentals change; **stop reversion trades after three consecutive losses** (T3) |
| Forrest Knight | Volume-profile edges | Edge-to-edge rotation through LVNs (T3) |

## Return profile & danger

High win rate and **negative skew**: many small wins, occasional large loss
when the regime flips to trend. Hard stops and regime filters are mandatory.
Never average down without a predefined max risk ([[concept_risk_of_ruin_drawdown]]).
