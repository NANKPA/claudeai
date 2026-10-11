---
id: framework_math_foundations
type: framework
title: Partition 06 — Mathematics Foundations of Analysis & Execution
partition: 06_mathematics-foundations
layer: L0
related: [formula_sheet, concept_probability_fat_tails, concept_stochastic_processes, concept_time_series_statistics, concept_optimal_execution_market_impact, concept_kelly_criterion_optimal_f, concept_overfitting_validation]
status: synthesized
---

# Partition 06 — Mathematics Foundations

**Goal:** the smallest body of mathematics that makes every trading idea in
this knowledge base *testable* (analysis) and *executable without ruin*
(execution).

## Contents

| File | What |
|---|---|
| `core-formulas.md` | One-page formula sheet organised by layer |
| `math-books.yaml` | Canon of ~45 books and papers in 6 tracks (A–F), levels 1–3 |
| `lectures.yaml` | Courses, talks, and podcast episodes on the math (seed + discovery queries to reach 100) |

## Six tracks and the order to study them

```
A. Probability & Statistics ─┬─► C. Time Series & Econometrics ─► F. Quant Research, ML & Validation
                             └─► B. Stochastic Calculus & Derivatives
E. Risk, Sizing & Portfolio  (start alongside A: Kelly, ruin, drawdown)
D. Microstructure & Execution (after A + C: order books, impact, optimal execution)
```

| Track | Start with (level 1–2) | Then (level 3) | Why a trader needs it |
|---|---|---|---|
| **A** Probability & statistics | Blitzstein & Hwang; Mosteller; Wasserman | Jaynes; Feller; Taleb *Statistical Consequences of Fat Tails* | Estimate edge with honest error bars; respect fat tails |
| **B** Stochastic calculus | Wilmott; Hull | Shreve I & II; Gatheral | Volatility, options, continuous-time intuition (vol drag, OU) |
| **C** Time series | Ruppert & Matteson; Tsay | Hamilton; Campbell–Lo–MacKinlay | Autocorrelation = the math of patterns; GARCH; cointegration |
| **D** Microstructure & execution | Harris; Johnson | O'Hara; Hasbrouck; Bouchaud et al.; Cartea–Jaimungal–Penalva; Guéant; Almgren–Chriss | Fills, slippage, impact; why liquidity pools exist |
| **E** Risk & sizing | Vince; Tharp (top-100) | Kelly (1956); MacLean–Thorp–Ziemba; Cover & Thomas; Grinold & Kahn; McNeil–Frey–Embrechts | Survive and compound |
| **F** Quant research & validation | ISL; Hilpisch; Jansen | ESL; López de Prado (AFML, MLAM); Bailey & López de Prado (DSR) | Don't fool yourself with backtests |

## Where the math touches discretionary playbooks

| Discretionary idea | Mathematical counterpart |
|---|---|
| "Liquidity sweep" | Stop orders as latent market orders; Kyle/impact models ([[concept_market_microstructure]]) |
| "Fair value / POC reversion" | Ornstein–Uhlenbeck mean reversion, half-life ([[concept_stochastic_processes]]) |
| "Trend/imbalance" | Positive autocorrelation, Hurst > 0.5, time-series momentum ([[concept_time_series_statistics]]) |
| "1:20 R:R at 90% win rate" | Expectancy algebra exposes impossibility ([[concept_expectancy]]) |
| "Plan to lose 20 in a row" | Run-length probabilities and drawdown math ([[concept_risk_of_ruin_drawdown]]) |
| "Only trade the London kill zone" | Conditional distributions by time-of-day ([[concept_trading_sessions_killzones]]) |
| "Risk 0.25% per trade" | Fractional Kelly under estimation error ([[concept_kelly_criterion_optimal_f]]) |
