---
id: formula_sheet
type: formula
title: Core Formulas of Analysis & Execution
partition: 06_mathematics-foundations
layer: L0
related: [concept_expectancy, concept_kelly_criterion_optimal_f, concept_position_sizing, concept_risk_of_ruin_drawdown, concept_volatility, concept_stochastic_processes, concept_optimal_execution_market_impact, concept_performance_metrics, concept_overfitting_validation, concept_options_greeks, concept_market_microstructure]
status: synthesized
---

# Core Formulas of Analysis & Execution

One page of mathematics that every layer of the stack uses. Symbols: `p` win
probability, `q = 1−p`, `b` payoff ratio (avg win ÷ avg loss), `R` risk unit,
`σ` volatility, `μ` drift, `f` fraction of equity at risk.

## L0 — Edge & randomness

| Formula | Meaning | Note |
|---|---|---|
| `E[R] = p·b − q` | Expectancy per trade in R | [[concept_expectancy]] |
| `p_BE = 1/(1+b)` | Breakeven win rate for payoff `b` | [[concept_risk_reward_r_multiples]] |
| `SE(p̂) = √(p̂(1−p̂)/n)` | Standard error of an estimated win rate (n = 50, p̂ = 0.5 → ±7%) | [[concept_probabilistic_thinking]] |
| `t ≈ √n · mean(R)/sd(R)` (= SQN) | Is the edge distinguishable from zero? | [[concept_performance_metrics]] |
| `g ≈ μ − σ²/2` | Geometric (compound) growth vs arithmetic mean: volatility drag | [[concept_stochastic_processes]] |
| `σ_T = σ_1·√T` | Square-root-of-time volatility scaling | [[concept_volatility]] |
| `ATR_t = ATR_{t−1} + (TR_t − ATR_{t−1})/n` | Wilder's smoothing of true range | [[concept_volatility]] |
| `Hurst H`: `E[R/S] ∝ n^H` | H > 0.5 trending, H < 0.5 mean-reverting | [[concept_market_regimes]] |
| `half-life = ln 2 / θ` (OU) | Speed of mean reversion | [[concept_mean_reversion]] |

## L5 — Execution

| Formula | Meaning | Note |
|---|---|---|
| `VWAP = ΣPᵢVᵢ / ΣVᵢ` | Volume-weighted fair price / execution benchmark | [[concept_vwap]] |
| `ΔP ≈ Y·σ_daily·√(Q/V_daily)` | Square-root market-impact law | [[concept_optimal_execution_market_impact]] |
| `x(t) = X·sinh(κ(T−t))/sinh(κT)`, `κ ≈ √(λσ²/η)` | Almgren–Chriss optimal liquidation path | [[concept_optimal_execution_market_impact]] |
| `ΔP = λ·(order flow)` | Kyle's lambda: price impact per unit of net order flow | [[concept_market_microstructure]] |
| `cost = ½·spread + commission + slippage` | Per-trade friction to subtract from edge | [[concept_trade_execution]] |

## L6 — Risk & sizing

| Formula | Meaning | Note |
|---|---|---|
| `size = (Equity × f) / (stop_distance × point_value)` | Fixed-fractional sizing | [[concept_position_sizing]] |
| `units = (Equity × 1%) / (N × $/point)` | Turtle volatility unit (N = 20-day ATR) | [[concept_position_sizing]] |
| `f* = p − q/b` | Kelly fraction (binary) | [[concept_kelly_criterion_optimal_f]] |
| `f* = μ/σ²`, `g* = SR²/2` | Continuous Kelly and its max growth rate | [[concept_kelly_criterion_optimal_f]] |
| `loss after k losers = 1 − (1−f)^k` | Streak damage under fixed fractional risk | [[concept_risk_of_ruin_drawdown]] |
| `recovery = 1/(1−DD) − 1` | Gain needed to recover a drawdown | [[concept_risk_of_ruin_drawdown]] |
| `RoR ≈ (q/p)^U` | Gambler's-ruin approximation with U units | [[concept_risk_of_ruin_drawdown]] |
| `σ_p = √(wᵀΣw)` | Portfolio volatility with correlations | [[concept_correlation_portfolio_risk]] |

## L8 — Validation

| Formula | Meaning | Note |
|---|---|---|
| `Sharpe = (μ−r_f)/σ × √periods` | Risk-adjusted return | [[concept_performance_metrics]] |
| `E[max SR_N] ≈ √(2 ln N)` (null, unit variance) | Expected best Sharpe from N skill-less trials | [[concept_overfitting_validation]] |
| `DSR = Φ( (SR̂ − SR₀)·√(T−1) / √(1 − γ₃SR̂ + (γ₄−1)/4·SR̂²) )` | Deflated Sharpe ratio (Bailey & López de Prado) | [[concept_overfitting_validation]] |
| `PF = Σwins / |Σlosses|` | Profit factor | [[concept_performance_metrics]] |

## Options (for context)

`C = S·N(d₁) − K e^{−rT} N(d₂)` · `Δ = N(d₁)` · `Γ = φ(d₁)/(Sσ√T)` ·
`P&L_hedged ≈ ½ΓS²(σ²_real − σ²_impl)dt` ([[concept_options_greeks]]).
