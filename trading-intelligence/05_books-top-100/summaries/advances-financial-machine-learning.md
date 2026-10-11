---
id: book_advances_financial_ml
type: book
title: "Advances in Financial Machine Learning (López de Prado, 2018) — summary"
partition: 05_books-top-100
layer: L8
status: synthesized
---

# Advances in Financial Machine Learning — summary

See [[concept_machine_learning_finance]] and [[concept_overfitting_validation]].

| Part | Key tools |
|---|---|
| Data analysis | Dollar/volume/imbalance bars; fractional differentiation; CUSUM event sampling |
| Modelling | Triple-barrier labeling; **meta-labeling**; sample weights for overlapping labels; sequential bootstrap |
| Backtesting | Purged and embargoed CV; combinatorial purged CV; dangers of backtesting; synthetic data |
| Useful features | Structural breaks, entropy, microstructural features |
| HPC | Parallelisation recipes |

**Most transferable idea for discretionary traders:** meta-labeling. Keep
your setup as the "primary model" and learn *when to take it and how big*.
