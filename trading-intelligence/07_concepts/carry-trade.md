---
id: concept_carry_trade
type: concept
title: Carry Trade
partition: 07_concepts
layer: L4
aliases: [carry trade, interest rate differential, rollover, swap, funding currency]
related: [concept_fundamental_macro_analysis, concept_intermarket_analysis, concept_probability_fat_tails, concept_volatility]
status: synthesized
---

# Carry Trade

BabyPips Sophomore. **Borrow (sell) a low-yielding currency and buy a
high-yielding one**, collecting the interest-rate differential (rollover or
swap) daily.

## Profile

- Steady positive accrual while volatility is low.
- **"Up the stairs, down the elevator":** carry unwinds are violent in
  risk-off shocks (e.g., the 2008 JPY carry unwind). The returns are
  negatively skewed ([[concept_probability_fat_tails]]).
- Works best in **low-vol, risk-on** regimes. Combine it with a trend or
  volatility filter.

## Theory

Uncovered interest parity predicts the high-yielder should depreciate by the
rate gap. Empirically it often doesn't (the *forward premium puzzle*). The
carry return is compensation for crash risk, i.e., a risk premium, which
makes it a textbook example of an edge with a structural cause
([[concept_edge]]).
