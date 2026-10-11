---
id: concept_correlation_portfolio_risk
type: concept
title: Correlation & Portfolio Risk
partition: 07_concepts
layer: L6
aliases: [correlation risk, portfolio heat, currency correlations, diversification, risk parity, VaR]
related: [concept_intermarket_analysis, concept_position_sizing, concept_trend_following, concept_risk_of_ruin_drawdown]
influenced_by: [person_harry_markowitz, person_ray_dalio]
status: synthesized
---

# Correlation & Portfolio Risk

BabyPips Senior covers currency correlations. Correlated positions **compound
your risk invisibly**.

## Core math

Portfolio variance: `σ_p² = Σᵢ Σⱼ wᵢ wⱼ σᵢ σⱼ ρᵢⱼ`. For N equal-risk positions
with average correlation ρ, portfolio vol ≈ `σ·√(ρ + (1 − ρ)/N)`. As N grows,
risk falls only to `σ·√ρ`. **Correlation, not count, limits diversification.**

## Practice

- **Portfolio heat:** the sum of open risk across all positions, capped
  (e.g., 3–6% of equity).
- **Cluster limits:** cap exposure per theme (USD, tech, metals).
- **Stress correlations go to 1** in crises ([[concept_probability_fat_tails]]).

## Lineage

Markowitz (*Portfolio Selection*, 1952) → Sharpe (CAPM) → risk parity
(Dalio's *All Weather*, balance risk not capital) → CTA volatility targeting
([[concept_trend_following]]). Dalio's "Holy Grail": 15+ good, uncorrelated
return streams can cut risk by ~80% without cutting return.
