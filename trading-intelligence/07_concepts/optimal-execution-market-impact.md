---
id: concept_optimal_execution_market_impact
type: concept
title: Optimal Execution & Market Impact (Almgren-Chriss, square-root law)
partition: 07_concepts
layer: L5
aliases: [optimal execution, market impact, Almgren-Chriss, implementation shortfall, square-root law, TWAP, VWAP algorithm, slippage, transaction cost analysis, TCA]
related: [concept_market_microstructure, concept_vwap, concept_trade_execution, concept_stochastic_processes, concept_liquidity]
influenced_by: [person_robert_almgren, person_jean_philippe_bouchaud, person_albert_kyle]
status: synthesized
---

# Optimal Execution & Market Impact

**The mathematics of getting size done.** It is the institutional half of
"execution".

## Almgren & Chriss (2000), "Optimal Execution of Portfolio Transactions"

Liquidate `X` shares over horizon `T`:
- **Temporary impact** (cost of trading fast): `h(v) = ε·sgn(v) + η·v`.
- **Permanent impact** (information leakage): `g(v) = γ·v`.
- **Price risk** while holding inventory: variance `σ²·∫x(t)²dt`.

Minimise `E[cost] + λ·Var[cost]`. The optimal trajectory is
`x(t) = X·sinh(κ(T−t))/sinh(κT)`, with `κ ≈ √(λσ²/η)`.
- λ → 0 (risk-neutral): **linear (TWAP)** schedule.
- λ large: **front-loaded** selling to cut risk.
This yields an *efficient frontier* of execution strategies.

## The square-root impact law (empirical, very robust)

Impact of a metaorder of size `Q`: `ΔP ≈ Y·σ_daily·√(Q / V_daily)`, with `Y ~ O(1)`.
Doubling size raises impact by ~41%, not 100%. It is documented across
equities, futures, FX, and crypto (Bouchaud et al., *Trades, Quotes and
Prices*).

## Algorithms

| Algo | Objective |
|---|---|
| **TWAP** | Even slices over time |
| **VWAP** | Track the volume curve; benchmark = VWAP ([[concept_vwap]]) |
| **POV** | Fixed % of market volume |
| **Implementation shortfall (arrival price)** | Minimise cost vs decision price (Almgren-Chriss) |

## Relevance to discretionary traders

1. Your stop orders are other people's liquidity ([[concept_liquidity]]).
2. Slippage scales with *speed* and *size relative to volume*. Size down in
   thin markets and around news.
3. **Kyle's λ** (impact per unit of order flow) is why informed flow hides,
   and why order-flow traders hunt for large prints ([[concept_order_flow]]).

Further reading: Cartea, Jaimungal & Penalva, *Algorithmic and High-Frequency
Trading* (2015); Guéant, *The Financial Mathematics of Market Liquidity*
(2016); Harris, *Trading and Exchanges* (2003).
