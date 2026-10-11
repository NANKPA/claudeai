---
id: concept_leverage_margin
type: concept
title: Leverage, Margin, Pips & Lots
partition: 07_concepts
layer: L1
aliases: [leverage, margin, margin call, pip, pipette, lot, standard lot, mini lot, micro lot, point value, tick value]
related: [concept_position_sizing, concept_risk_of_ruin_drawdown, concept_prop_firm_risk_rules]
part_of: []
status: synthesized
---

# Leverage, Margin, Pips & Lots

**This is the BabyPips Preschool/Kindergarten core, and the root cause of
most blown accounts.**

## Units

- **Pip.** The fourth decimal for most FX pairs (0.0001), the second for JPY
  pairs (0.01). A *pipette* is one tenth of a pip.
- **Lot sizes (FX).** Standard = 100,000 units, mini = 10,000, micro = 1,000.
  For USD-quoted pairs, 1 standard lot ≈ $10 per pip.
- **Futures.** Tick size × tick value. ES = 0.25 pt = $12.50 (so $50/pt).
  NQ = 0.25 pt = $5 ($20/pt). MNQ = $2/pt.

## Leverage vs margin

- **Margin.** The deposit required to open a position, e.g., 2% means 50:1.
- **Leverage.** Notional exposure ÷ equity. *Effective* leverage is what
  matters, not the maximum the broker allows.
- **Margin call / stop-out.** Equity falls below maintenance margin and the
  broker liquidates.

## The rule that ties it together

Leverage does not determine risk. **Stop distance × position size**
determines risk. Choose risk per trade first (e.g., 0.25–1% of equity), then
derive size:

`lots = (equity × risk%) / (stop_pips × pip_value_per_lot)`

See [[concept_position_sizing]]. Fabio Valentini reportedly risks about
0.25% per trade (T3 source), far below the 1–2% retail norm.
