---
id: concept_random_walk_efficient_markets
type: concept
title: Random Walk & Efficient Market Hypothesis
partition: 07_concepts
layer: L0
aliases: [EMH, random walk hypothesis, adaptive markets]
related: [concept_probability_fat_tails, concept_stochastic_processes, concept_edge, concept_time_series_statistics]
contrasts_with: [concept_trend_following, concept_price_action]
influenced_by: [person_louis_bachelier, person_eugene_fama, person_andrew_lo, person_burton_malkiel]
status: synthesized
---

# Random Walk & the Efficient Market Hypothesis

**Claim.** If prices fully reflect available information, future price changes
are unpredictable. Excess returns then exist only as compensation for risk.

## Three forms (Fama, 1970)

1. **Weak:** past prices are not predictive, so technical analysis cannot earn
   excess returns.
2. **Semi-strong:** public information is priced, so fundamental analysis
   cannot either.
3. **Strong:** even private information is priced.

## The counter-evidence traders rely on

- **Time-series momentum and trend premia** are documented across a century
  of futures data (Hurst, Ooi & Pedersen). This is the empirical basis for
  [[concept_trend_following]].
- **Short-horizon mean reversion** and **post-earnings drift** (the basis for
  [[concept_episodic_pivot]]).
- **Variance-ratio tests** reject the random walk for weekly US equity returns
  (Lo & MacKinlay, *A Non-Random Walk Down Wall Street*).
- **Microstructure frictions** (inventory, order-flow imbalance) create
  predictable, very short-lived dynamics (see [[concept_order_flow]]).

## Synthesis: the Adaptive Markets Hypothesis (Lo)

Markets are efficient *on average*, but efficiency varies with the ecology of
participants. Edges appear, get crowded, and decay. This is the most useful
working model for a discretionary trader: assume most patterns are noise, and
demand evidence ([[concept_backtesting]], [[concept_overfitting_validation]]).
