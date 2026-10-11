---
id: concept_kelly_criterion_optimal_f
type: concept
title: Kelly Criterion & Optimal f
partition: 07_concepts
layer: L6
aliases: [Kelly criterion, Kelly formula, fractional Kelly, optimal f, growth optimal portfolio, geometric growth]
related: [concept_position_sizing, concept_risk_of_ruin_drawdown, concept_expectancy, concept_probability_fat_tails, concept_stochastic_processes]
influenced_by: [person_john_kelly, person_claude_shannon, person_ed_thorp, person_ralph_vince]
sources:
  - {title: "Kelly, J. L. (1956). A New Interpretation of Information Rate. Bell System Technical Journal", url: "https://doi.org/10.1002/j.1538-7305.1956.tb03809.x", tier: T1}
status: synthesized
---

# Kelly Criterion & Optimal f

## Kelly (1956)

John L. Kelly Jr. at Bell Labs, building on Shannon's information theory:
the bet fraction that **maximises the expected logarithm of wealth** (the
long-run geometric growth rate).

- **Binary bet** (win `b` per 1 risked with probability `p`, else lose 1):
  `f* = p − (1 − p)/b = (bp − q)/b`
- **Continuous (Gaussian) approximation:** `f* = μ / σ²` (excess return ÷
  variance). The growth rate at f* is `g* = μ²/(2σ²) = SR²/2`.

Example: p = 0.55, b = 1 → f* = 10% of bankroll per bet.

## Properties

- Betting **more than 2× Kelly gives negative growth**, even with an edge.
- **Full Kelly drawdowns are brutal:** a 50% drawdown happens with ~50%
  probability at some point. Hence **fractional Kelly (¼–½)**. Half Kelly
  gives ~75% of the growth for a fraction of the variance.
- Kelly assumes the probabilities are *known*. With estimation error and fat
  tails, overestimating edge leads to over-betting, so shade down
  ([[concept_probability_fat_tails]]).

## Optimal f (Ralph Vince, 1990–2009)

Find the fraction `f` of the **largest historical loss** that maximises
terminal wealth relative (TWR) over the actual trade list. It is an
empirical, trade-list-driven relative of Kelly. Critiques: it is anchored to
the worst *past* loss (the future can be worse) and produces "tremendous
drawdowns". Position-sizing experts, including Van Tharp, rarely recommend it.

## Lineage

Shannon → **Kelly (1956)** → **Ed Thorp** (blackjack 1962, Princeton-Newport
Partners; *Beat the Dealer*, *A Man for All Markets*) → Vince (*The
Mathematics of Money Management*, 1992) → Tharp (position-sizing models) →
MacLean, Thorp & Ziemba (eds.), *The Kelly Capital Growth Investment
Criterion* (2011). Popular history: Poundstone, *Fortune's Formula* (2005).
