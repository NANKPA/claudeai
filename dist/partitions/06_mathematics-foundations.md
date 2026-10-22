# Partition 06_mathematics-foundations


<!-- ===== FILE: trading-intelligence/06_mathematics-foundations/README.md ===== -->

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
| `lectures.yaml` → `lectures.md` | Courses, talks and episodes on the math: curated seed + the **scraped view-ranked top 100** (`lectures.scraped.yaml`) |

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


<!-- ===== FILE: trading-intelligence/06_mathematics-foundations/core-formulas.md ===== -->

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


<!-- ===== FILE: trading-intelligence/06_mathematics-foundations/lectures.md ===== -->

<!-- generated by tools/render_registries.py from the YAML registries; do not edit by hand -->

# Math-of-Trading Lectures, Courses & Talks (seed)

| Title | Speakers | Year | Format | Verification | Concepts | Link |
|---|---|---|---|---|---|---|
| **Chat With Traders EP 109 — The man who beat the dealer, and later, beat the market (Edward Thorp)** | Edward O. Thorp |  | podcast | verified | `concept_edge`, `concept_kelly_criterion_optimal_f` | [link](https://chatwithtraders.com/?p=1508) |
| **Jim Simons — Mathematics, Common Sense, and Good Luck: My Life and Careers (MIT, 2010)** | Jim Simons | 2010 | talk | verified | `concept_edge`, `concept_machine_learning_finance` | [link](https://simonsfoundation.org/2024/05/10/remembering-the-life-and-careers-of-jim-simons) |
| **Jim Simons — Numberphile interview ('Billionaire Mathematician', full and short versions)** | Jim Simons | 2015 | interview | verified | `concept_machine_learning_finance`, `concept_edge` |  |
| **MIT 18.642 Topics in Mathematics with Applications in Finance (Fall 2024) — successor course with recordings** |  | 2024 | university course | verified | `concept_stochastic_processes`, `concept_time_series_statistics` | [link](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/syllabus) |
| **MIT 18.S096 Topics in Mathematics with Applications in Finance (Fall 2013) — full lecture series** | Peter Kempthorne | 2013 | university course (video lectures + notes) | verified | `concept_stochastic_processes`, `concept_time_series_statistics`, `concept_options_greeks`, `concept_correlation_portfolio_risk`, `concept_volatility` | [link](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/) |
| **TIP128 — Edward Thorp: A Man for All Markets (The Investor's Podcast)** | Edward O. Thorp |  | podcast | verified | `concept_kelly_criterion_optimal_f`, `concept_position_sizing` | [link](https://www.theinvestorspodcast.com/episodes/edward-thorp-a-man-for-all-markets/) |
| **3Blue1Brown — Bayes theorem, the geometry of changing beliefs** | Grant Sanderson |  | explainer | known | `concept_probabilistic_thinking`, `concept_probability_fat_tails` |  |
| **3Blue1Brown — But what is the Central Limit Theorem?** | Grant Sanderson | 2023 | explainer | known | `concept_probability_fat_tails` |  |
| **EconTalk — Nassim Taleb episodes (Black Swan, fat tails, skin in the game)** | Nassim Nicholas Taleb, Russ Roberts |  | podcast series | known | `concept_probability_fat_tails`, `concept_risk_of_ruin_drawdown` |  |
| **Financial Engineering and Risk Management (Columbia, Coursera) — Martin Haugh & Garud Iyengar** | Martin Haugh, Garud Iyengar |  | online course | known | `concept_options_greeks`, `concept_stochastic_processes`, `concept_correlation_portfolio_risk` |  |
| **Harvard Stat 110: Probability — Joe Blitzstein** | Joe Blitzstein |  | university course | known | `concept_probability_fat_tails`, `concept_expectancy`, `concept_probabilistic_thinking` |  |
| **Jim Simons — The mathematician who cracked Wall Street (TED 2015)** | Jim Simons | 2015 | talk | known | `concept_machine_learning_finance`, `concept_edge` |  |
| **MIT 15.401 Finance Theory I — Andrew Lo (Fall 2008)** | Andrew W. Lo | 2008 | university course | known | `concept_random_walk_efficient_markets`, `concept_correlation_portfolio_risk`, `concept_options_greeks` |  |
| **MIT 15.S50 Poker Theory and Analytics (decision-making under uncertainty)** |  |  | university course | known | `concept_probabilistic_thinking`, `concept_kelly_criterion_optimal_f`, `concept_expectancy` |  |
| **MIT 18.06 Linear Algebra — Gilbert Strang** | Gilbert Strang |  | university course | known | `concept_correlation_portfolio_risk`, `concept_machine_learning_finance` |  |
| **MIT 18.650 Statistics for Applications (Fall 2016) — Philippe Rigollet** | Philippe Rigollet | 2016 | university course | known | `concept_overfitting_validation`, `concept_backtesting` |  |
| **MIT 6.041 Probabilistic Systems Analysis / RES.6-012 Introduction to Probability — John Tsitsiklis** | John Tsitsiklis |  | university course | known | `concept_probability_fat_tails`, `concept_stochastic_processes` |  |
| **Marcos López de Prado — The 7 Reasons Most Machine Learning Funds Fail (QuantCon)** | Marcos López de Prado |  | talk | known | `concept_machine_learning_finance`, `concept_overfitting_validation`, `concept_backtesting` |  |
| **Veritasium — The Trillion Dollar Equation (Black–Scholes, Bachelier, Thorp, Simons)** | Derek Muller | 2024 | explainer | known | `concept_options_greeks`, `concept_stochastic_processes`, `concept_random_walk_efficient_markets` |  |
| **Yale ECON 252 Financial Markets — Robert Shiller (Open Yale Courses)** | Robert Shiller |  | university course | known | `concept_random_walk_efficient_markets`, `concept_market_sentiment`, `concept_correlation_portfolio_risk` |  |

## Discovery queries (scraper fills the ranked top-100 from these)

- **probability_statistics**: `Kelly criterion explained`; `risk of ruin trading explained`; `expected value trading math`; `law of large numbers trading edge`; `fat tails Taleb lecture`; `Bayesian probability lecture`
- **stochastic_derivatives**: `stochastic calculus for finance lecture`; `Ito's lemma explained`; `Black Scholes derivation lecture`; `Brownian motion finance lecture`; `volatility surface lecture Gatheral`
- **time_series**: `GARCH volatility model lecture`; `cointegration pairs trading lecture`; `time series analysis finance lecture`
- **microstructure_execution**: `Almgren Chriss optimal execution lecture`; `market microstructure lecture limit order book`; `square root law market impact Bouchaud`; `high frequency trading market making lecture Cartea Jaimungal`; `VWAP TWAP execution algorithms explained`
- **quant_validation**: `backtest overfitting deflated Sharpe ratio`; `Marcos Lopez de Prado lecture`; `Ernest Chan quantitative trading interview`; `Robert Carver systematic trading`; `quantitative trading podcast`
- **foundations_more**: `MIT 18.S096 topics in mathematics finance lecture`; `Black Scholes model explained`; `options greeks explained delta gamma`; `volatility smile explained`; `Jim Simons lecture mathematics`; `Ed Thorp interview Kelly`; `Taleb fat tails lecture`; `Mandelbrot fractals markets`; `Ito calculus lecture`; `random walk hypothesis explained`; `Monte Carlo simulation trading`; `Sharpe ratio explained`; `limit order book explained`; `market making explained`; `optimal execution explained`; `statistical arbitrage explained`; `probability theory lecture`; `expected value explained`

## Top math-of-trading videos (scraped)

Ranked by YouTube views (as of 2026-10-11) after filtering: no audiobook/summary re-uploads, title must match the query, at most 4 picks per query. Generated by `tools/scrapers/youtube_top_search.py` (T3: discovery list).

| # | Title | Channel | Views | Concepts |
|---|---|---|---|---|
| 1 | [Option Greeks Explained - Theta Delta Gamma Vega RHO \| Stock Market Trading Knowledge \| Share Market](https://www.youtube.com/watch?v=Ca66fN3oP1U) | Pushkar Raj Thakur: Stock Market Educator 📈 | 3,927,626 | `concept_options_greeks`, `concept_order_flow` |
| 2 | [The mathematician who cracked Wall Street \| Jim Simons](https://www.youtube.com/watch?v=U5kIdtMJGc8) | TED | 2,900,075 |  |
| 3 | [Lecture 1: Probability and Counting \| Statistics 110](https://www.youtube.com/watch?v=KbB0FjPg0mw) | Harvard University | 1,775,418 |  |
| 4 | [Jim Simons (full length interview) - Numberphile](https://www.youtube.com/watch?v=QNznD9hMEh0) | Numberphile2 | 1,358,228 |  |
| 5 | [Stock Market Order Types (Market Order, Limit Order, Stop Loss, Stop Limit)](https://www.youtube.com/watch?v=p9YndmEoJn0) | Arvabelle | 1,269,319 | `concept_trade_execution`, `concept_trade_management` |
| 6 | [Option Greeks Delta, Gamma, Theta, Vega Explained \| Learn Share Market Trading](https://www.youtube.com/watch?v=TfHjCtyKPHo) | Pushkar Raj Thakur: Stock Market Educator 📈 | 1,174,457 | `concept_options_greeks`, `concept_order_flow` |
| 7 | [Introduction to the Black-Scholes formula \| Finance & Capital Markets \| Khan Academy](https://www.youtube.com/watch?v=pr-u4LCFYEY) | Khan Academy | 1,158,247 | `concept_options_greeks` |
| 8 | [Jim Simons: A Short Story of My Life and Mathematics (2022)](https://www.youtube.com/watch?v=CTQcLi6SpX8) | The Abel Prize | 803,322 |  |
| 9 | [The Sharpe Ratio Explained (by a quant trader)](https://www.youtube.com/watch?v=9HD6xo2iO1g) | Wall Street Quants | 789,950 | `concept_performance_metrics` |
| 10 | [La formule qui a radicalement transformé la finance mondiale [Black-Scholes]](https://www.youtube.com/watch?v=XE7FKLfZzBA) | ScienceEtonnante | 729,603 | `concept_options_greeks` |
| 11 | [Jim Simons Trading Secrets 1.1 MARKOV Process](https://www.youtube.com/watch?v=gA0egjZcRB0) | QuantProgram | 711,674 |  |
| 12 | [Statistics Lecture 4.2: Introduction to Probability](https://www.youtube.com/watch?v=_EpXHuPnaK0) | Professor Leonard | 639,655 |  |
| 13 | [Benoit Mandelbrot: Fractals and the art of roughness](https://www.youtube.com/watch?v=ay8OMOsf6AQ) | TED | 492,889 |  |
| 14 | [3. Probability Theory](https://www.youtube.com/watch?v=f9XFM8YLccg) | MIT OpenCourseWare | 470,817 |  |
| 15 | [8. Time Series Analysis I](https://www.youtube.com/watch?v=uBeM1FUk4Ps) | MIT OpenCourseWare | 463,073 |  |
| 16 | [Black-Scholes Option Pricing Model -- Intro and Call Example](https://www.youtube.com/watch?v=i0sGAds8ztI) | Kevin Bracker | 441,784 | `concept_options_greeks` |
| 17 | [The Math of Winning in Trading](https://www.youtube.com/watch?v=BAfRVpKIxZ4) | Mulham Trading | 424,767 |  |
| 18 | [The Expected Value and Variance of Discrete Random Variables](https://www.youtube.com/watch?v=Vyk8HQOckIE) | jbstatistics | 415,904 | `concept_expectancy` |
| 19 | ["Basic Statistical Arbitrage: Understanding the Math Behind Pairs Trading" by Max Margenot](https://www.youtube.com/watch?v=g-qvFjvyqcs) | Quantopian | 405,115 | `concept_mean_reversion` |
| 20 | [TIME SERIES ANALYSIS THE BEST EXAMPLE](https://www.youtube.com/watch?v=HIWXdHlDSFs) | Adhir Hurjunlal | 399,631 |  |
| 21 | [Time Series Analysis \| Time Series Forecasting \| Time Series Analysis in R \| Ph.D. (Stanford)](https://www.youtube.com/watch?v=FPM6it4v8MY) | Great Learning | 375,457 |  |
| 22 | [How to Trade with the Black-Scholes Model](https://www.youtube.com/watch?v=0x-Pc-Z3wu4) | Roman Paolucci | 366,207 | `concept_options_greeks` |
| 23 | [Lecture 13   Time Series Analysis](https://www.youtube.com/watch?v=Prpu_U5tKkE) | Jordan Kern | 350,854 |  |
| 24 | [[#1] Theory of Probability \|\| Quantitative Techniques calicut university in Malayalam](https://www.youtube.com/watch?v=BPFemUnsHwI) | Zydemic Education  | 345,097 |  |
| 25 | [What is a Random Walk? \| Infinite Series](https://www.youtube.com/watch?v=stgYW6M5o4k) | PBS Infinite Series | 304,621 | `concept_support_resistance` |
| 26 | [19. Black-Scholes Formula, Risk-neutral Valuation](https://www.youtube.com/watch?v=TnS8kI_KuJc) | MIT OpenCourseWare | 288,523 | `concept_options_greeks` |
| 27 | [Mathematics of Maximizing Profit in Gambling/Investing \| Kelly Criterion](https://www.youtube.com/watch?v=-X9u9oYvGYk) | EpsilonDelta | 285,027 | `concept_kelly_criterion_optimal_f` |
| 28 | [Lecture 4: Conditional Probability \| Statistics 110](https://www.youtube.com/watch?v=P7NE4WF8j-Q) | Harvard University | 282,614 | `concept_trading_plan` |
| 29 | [Warren Buffett: Black-Scholes Formula Is Total Nonsense](https://www.youtube.com/watch?v=H4X-4e7fPgI) | The Long-Term Investor | 240,152 | `concept_options_greeks` |
| 30 | [Monte Carlo Simulation of a Stock Portfolio with Python](https://www.youtube.com/watch?v=6-dhdMDiYWQ) | QuantPy | 217,955 | `concept_backtesting` |
| 31 | [ICT Market Maker Model - Explained In-depth!](https://www.youtube.com/watch?v=uSFxr4jT230) | DanDowdTrading | 210,310 | `concept_market_microstructure`, `concept_smart_money_concepts` |
| 32 | [GARCH Model : Time Series Talk](https://www.youtube.com/watch?v=inoBpq1UEn4) | ritvikmath | 207,086 | `concept_time_series_statistics` |
| 33 | [Option Greeks (Telugu)  Explained  Delta, Gamma, Theta, Vega , Rho](https://www.youtube.com/watch?v=YdTRF4d9KvE) | DAY TRADER తెలుగు | 202,534 | `concept_options_greeks`, `concept_order_flow` |
| 34 | [Getting data from expected value \| Probability and Statistics \| Khan Academy](https://www.youtube.com/watch?v=gHpl5UcgRkI) | Khan Academy | 196,480 | `concept_expectancy` |
| 35 | [15 Years of Trading Risk Management in 20 Minutes](https://www.youtube.com/watch?v=gb7nNveNBjg) | TheOneLanceB | 189,279 |  |
| 36 | [How Does Leverage Affect Trading Returns? The Kelly Criterion \| Coffeezilla Follow-up](https://www.youtube.com/watch?v=UjsC2sk7vVg) | Patrick Boyle | 188,511 | `concept_kelly_criterion_optimal_f`, `concept_leverage_margin` |
| 37 | [KELLY CRITERION \| Ed Thorp \| Optimal Position Sizing For Stock Trading](https://www.youtube.com/watch?v=THYLv5_0Vm8) | Financial Wisdom | 185,306 | `concept_position_sizing`, `concept_kelly_criterion_optimal_f` |
| 38 | [How Markets Actually Work — Retail vs Institutions vs Market Makers Explained (Video 1)](https://www.youtube.com/watch?v=jb6Odrq6alA) | Smart Money Decode X | 184,713 | `concept_market_microstructure` |
| 39 | [Efficient Market Hypothesis - EMH Explained Simply](https://www.youtube.com/watch?v=UTHvfI9awBk) | Learn to Invest - Investors Grow | 171,557 | `concept_random_walk_efficient_markets` |
| 40 | [The Kelly Criterion](https://www.youtube.com/watch?v=-9JM9suCIHs) | Mutual Information | 162,831 | `concept_kelly_criterion_optimal_f` |
| 41 | [Brownian Motion (Wiener process)](https://www.youtube.com/watch?v=BVYVeaPojY4) | profbillbyrne | 159,615 | `concept_stochastic_processes` |
| 42 | [A RANDOM WALK DOWN WALL STREET SUMMARY (BY BURTON MALKIEL)](https://www.youtube.com/watch?v=7TCVoB6Vorg) | The Swedish Investor | 153,404 | `concept_support_resistance` |
| 43 | [Statistics 101: What is Expected Value?](https://www.youtube.com/watch?v=u5svtXcKXEk) | Brandon Foltz | 147,030 | `concept_expectancy` |
| 44 | [The 7 Reasons Most Machine Learning Funds Fail Marcos Lopez de Prado from QuantCon 2018](https://www.youtube.com/watch?v=BRUlSm4gdQ4) | Quantopian | 143,249 |  |
| 45 | [Calculating Options Greeks That Matter: Delta, Gamma, Theta - Raj Malhotra](https://www.youtube.com/watch?v=Qs0jNUtHnVc) | InstituteofTrading | 138,860 | `concept_options_greeks`, `concept_order_flow` |
| 46 | [QUANT FINANCE 1 - Why We Never Use the Black Scholes Equation, 1](https://www.youtube.com/watch?v=UoGlUZPNouM) | N N Taleb's Probability Questions  | 132,960 |  |
| 47 | [Brownian Motion-I](https://www.youtube.com/watch?v=4-Tas6Uw_OQ) | Probability and Stochastics for finance | 125,164 | `concept_stochastic_processes`, `concept_oscillators_momentum` |
| 48 | [Stochastic Calculus for Quants \| Understanding Geometric Brownian Motion using Itô Calculus](https://www.youtube.com/watch?v=Devm4ElEhGc) | QuantPy | 123,730 | `concept_stochastic_processes`, `concept_oscillators_momentum` |
| 49 | [Volatility Skew Explained \| Options Trading Concepts](https://www.youtube.com/watch?v=cVQudesBUcA) | tastylive | 115,342 |  |
| 50 | [A 20-Year Veteran Reveals the World of Options Market Making](https://www.youtube.com/watch?v=7UY6Yg53R2Q) | QuantPy | 111,393 |  |
| 51 | [Quant Strategy: Pairs Trading Algorithm (Mean Reversion)](https://www.youtube.com/watch?v=f73ItMWO4z8) | Spencer Pao | 103,751 | `concept_mean_reversion` |
| 52 | [SQL Execution Plans (Visually Explained) \| SQL Hints \| #SQL Course 40](https://www.youtube.com/watch?v=O7AzUDogXsw) | Data with Baraa | 103,411 |  |
| 53 | [Statistical Rethinking 2022 Lecture 02 - Bayesian Inference](https://www.youtube.com/watch?v=guTdrfycW2Q) | Richard McElreath | 93,825 |  |
| 54 | [Introduction to Pairs Trading](https://www.youtube.com/watch?v=JTucMRYMOyY) | Quantopian | 93,396 | `concept_mean_reversion`, `concept_time_series_statistics` |
| 55 | [Must-Watch: Dr. Ernest Chan’s Ultimate Guide to Mean Reversion Trading!](https://www.youtube.com/watch?v=sFwyS-L-aDE) | QuantInsti Quantitative Learning | 92,306 | `concept_mean_reversion` |
| 56 | [Simplicity in Systematic Trading \| Robert Carver](https://www.youtube.com/watch?v=klwnw3iSRuM) | Top Traders Unplugged | 89,343 |  |
| 57 | [Sharpe Ratio, Treynor Ratio and Jensen's Alpha (Calculations for CFA® and FRM® Exams)](https://www.youtube.com/watch?v=9NJqujK5v5g) | AnalystPrep | 81,310 | `concept_edge`, `concept_performance_metrics` |
| 58 | [How To Calculate Expected Move for Stocks \| Trading Tutorials](https://www.youtube.com/watch?v=Lhv3wiPv6Ok) | Trade Brigade | 80,817 |  |
| 59 | [Discrete Random Variables (1 of 3: Expected value & median)](https://www.youtube.com/watch?v=a9vcTvaBqfs) | Eddie Woo | 80,410 | `concept_expectancy` |
| 60 | [Statistical Rethinking 2026 - Lecture A01 - Introduction to Bayesian Workflow](https://www.youtube.com/watch?v=ztbYkBPDOgU) | Richard McElreath | 71,147 |  |
| 61 | [The First Step in Every Winning Trade (How to Find Expected Value)](https://www.youtube.com/watch?v=F-ZktuFvk0E) | TheOneLanceB | 67,846 | `concept_expectancy` |
| 62 | [Expected Value Explained Intuitively](https://www.youtube.com/watch?v=nKBun2JmqlE) | Galak Breaks It Down | 66,603 | `concept_expectancy` |
| 63 | [⁠Greed Makes Markets: Market Making From First Principles With an HFT Quant](https://www.youtube.com/watch?v=iqEFMb1aKNU) | Odds on Open | 60,118 |  |
| 64 | [Stochastic Process, Filtration \| Part 1 Stochastic Calculus for Quantitative Finance](https://www.youtube.com/watch?v=ocnhBnL-DBc) | Stochastip | 58,641 | `concept_oscillators_momentum`, `concept_stochastic_processes` |
| 65 | [Fractals and the Hidden Hierarchy in Stock prices, Forex, and other Markets - Fractals and Finance](https://www.youtube.com/watch?v=EeViIO66f9I) | Fractal Manhattan | 53,843 |  |
| 66 | [Axioms of Brownian Motion](https://www.youtube.com/watch?v=VNTfgqJQlnk) | Maths Partner | 53,255 | `concept_stochastic_processes` |
| 67 | [Paul Wilmott on Quantitative Finance, Chapter 4.6, Brownian motion](https://www.youtube.com/watch?v=1GeqzM6aPuk) | Amber Whitehead | 51,292 | `concept_stochastic_processes` |
| 68 | [Derivation of Ito's Lemma](https://www.youtube.com/watch?v=aLq2MKr9E4U) | Maths Partner | 50,840 | `concept_oscillators_momentum` |
| 69 | ["Trading Strategies that are Designed, Not Fitted" by Robert Carver from QuantCon NYC 2017](https://www.youtube.com/watch?v=-aT55uRJI8Q) | Quantopian | 50,318 |  |
| 70 | [Fractals and the art of roughness - Benoit Mandelbrot](https://www.youtube.com/watch?v=wQTnVEXAtBY) | TED-Ed | 49,562 |  |
| 71 | [Stanford CS109 I Conditional Probability and Bayes I 2022 I Lecture 4](https://www.youtube.com/watch?v=NHRoXvPaZqY) | Stanford Online | 48,618 |  |
| 72 | [Benoit B. Mandelbrot, MIT 2001 - Fractals in Science, Engineering and Finance (Roughness and Beauty)](https://www.youtube.com/watch?v=ock9Gk_aqw4) | MIT Video Productions | 45,941 |  |
| 73 | [Brownian Motion \| Part 3 Stochastic Calculus for Quantitative Finance](https://www.youtube.com/watch?v=IBw5a8ByyzY) | Stochastip | 42,324 | `concept_oscillators_momentum`, `concept_stochastic_processes` |
| 74 | [The Volatility Smile - Options Trading Lessons](https://www.youtube.com/watch?v=ruFWFUkpbQk) | Patrick Boyle | 40,367 |  |
| 75 | [Why Random Walks and the Efficient Market Hypothesis Fail](https://www.youtube.com/watch?v=vo8q5AqIKlA) | Fractal Manhattan | 39,841 |  |
| 76 | [Lecture 15 - ARIMA & GARCH Models](https://www.youtube.com/watch?v=pspVn0OopME) | Steven Skiena | 37,414 | `concept_time_series_statistics` |
| 77 | [Pairs Trading: The Cointegration Approach and Minimum Profit Optimization](https://www.youtube.com/watch?v=1zz91G0nR14) | Hudson & Thames | 37,230 | `concept_mean_reversion`, `concept_time_series_statistics` |
| 78 | [Ito's Lemma -- Some intuitive explanations on the solution of stochastic differential equations](https://www.youtube.com/watch?v=_4zyAFpJ_Z4) | He Ha | 34,743 | `concept_oscillators_momentum` |
| 79 | [Secrets From A Profitable Systematic Trader - Robert Carver \| Trader Interview](https://www.youtube.com/watch?v=lMY9n1c3tFU) | Etienne Crete - Desire To TRADE | 34,004 |  |
| 80 | [1.2 Ito's Lemma](https://www.youtube.com/watch?v=m7ElHjYTSk0) | UChicago Online | 33,952 | `concept_oscillators_momentum` |
| 81 | [3 PROVEN Ways To Avoid RISK OF RUIN (Risk Management Trading)](https://www.youtube.com/watch?v=_Gy6ZltWxPw) | Trade With Trend - Raunak A | 32,829 | `concept_growth_momentum_canslim`, `concept_risk_of_ruin_drawdown` |
| 82 | [Limit Order Books](https://www.youtube.com/watch?v=Iaiw5iGjXbw) | Richard Holowczak | 32,716 | `concept_market_microstructure` |
| 83 | [Why Monte Carlo Simulation Works](https://www.youtube.com/watch?v=-4sf43SLL3A) | Roman Paolucci | 31,249 | `concept_backtesting` |
| 84 | [Master Volatility with ARCH & GARCH Models](https://www.youtube.com/watch?v=iImtlBRcczA) | Roman Paolucci | 30,425 | `concept_time_series_statistics` |
| 85 | [Machine Learning for Quantitative Trading Webinar with Dr. Ernie Chan](https://www.youtube.com/watch?v=72aEDjwGMr8) | Quantiacs | 29,421 |  |
| 86 | [Stochastic Market Microstructure Models of Limit Order Books](https://www.youtube.com/watch?v=XoBjQqMmKoM) | INFORMS | 28,376 | `concept_market_microstructure`, `concept_oscillators_momentum` |
| 87 | [Lecture 24: Stochastic Calculus](https://www.youtube.com/watch?v=5cruqmIF6l0) | MIT OpenCourseWare | 24,597 | `concept_oscillators_momentum` |
| 88 | [How To: Monte Carlo Simulation](https://www.youtube.com/watch?v=jGhk-uSrtII) | DeltaTrend Trading | 24,527 | `concept_backtesting`, `concept_oscillators_momentum` |
| 89 | [Ito Calculus-I](https://www.youtube.com/watch?v=6Ao6uGACt3w) | Probability and Stochastics for finance | 24,037 | `concept_stochastic_processes` |
| 90 | [Lecture 6: Modelling Volatility and Economic Forecasting](https://www.youtube.com/watch?v=n2GXY4JWgNQ) | Hanomics | 23,873 |  |
| 91 | [Systematic Trading – Build Your First Strategy!](https://www.youtube.com/watch?v=TDadFMS9R5g) | Peak Trading Research | 23,658 |  |
| 92 | [External Data Conference \| Ten Financial Applications of Machine Learning \| Marcos Lopez de Prado](https://www.youtube.com/watch?v=3gxx0QBuznI) | External Data Conference | 21,670 |  |
| 93 | [Risk Management: Risk to Reward Ratio, Expectancy and Risk of Ruin](https://www.youtube.com/watch?v=fZSAvprJusA) | Koroush AK | 21,250 | `concept_expectancy`, `concept_risk_of_ruin_drawdown` |
| 94 | [AI For Trading Forex (What You Can & Can't Do!) - Ernest Chan](https://www.youtube.com/watch?v=pLslJHWpIiQ) | Etienne Crete - Desire To TRADE | 21,132 |  |
| 95 | [Rough volatility: An overview by Jim Gatheral](https://www.youtube.com/watch?v=gW073Tnx7CE) | LSE Statistics | 20,863 | `concept_oscillators_momentum` |
| 96 | [Basic Statistical Arbitrage: Understanding the Math Behind Pairs Trading](https://www.youtube.com/watch?v=C6j45b26b34) | Quantopian | 20,688 | `concept_mean_reversion` |
| 97 | [Design A Limit Order Book \| Google SWE Teaches Low Level Design Episode 5](https://www.youtube.com/watch?v=nmYx6tQxtSs) | Jordan has no life | 19,969 | `concept_market_microstructure` |
| 98 | [Ito's Lemma Clearly and Visually Explained](https://www.youtube.com/watch?v=TgBzqdN24fo) | Roman Paolucci | 19,800 |  |
| 99 | [Machine Learning for Asset Managers with Marcos Lopez de Prado](https://www.youtube.com/watch?v=tODXAJDZtow) | NorQuant Kapitalforvaltning | 19,767 |  |
| 100 | [Volatility Surface & Volatility Smile Explained](https://www.youtube.com/watch?v=G7gf-oXptxE) | Outlier Trading | 18,842 |  |


<!-- ===== FILE: trading-intelligence/06_mathematics-foundations/math-books.md ===== -->

<!-- generated by tools/render_registries.py from the YAML registries; do not edit by hand -->

# Mathematics Canon for Analysis & Execution

Levels: 1 = accessible · 2 = undergraduate · 3 = graduate/research.


## Track D — Microstructure & Optimal Execution

| Level | Title | Author | Year | Key idea | Concepts |
|---|---|---|---|---|---|
| 2 | **Optimal Trading Strategies** | Robert Kissell & Morton Glantz | 2003 | Transaction-cost analysis and quantitative execution strategies. | `concept_optimal_execution_market_impact` |
| 2 | **Algorithmic Trading and DMA** | Barry Johnson | 2010 | Execution algorithms (VWAP, TWAP, IS, POV) and order-routing mechanics. | `concept_optimal_execution_market_impact`, `concept_vwap`, `concept_trade_execution` |
| 3 | **Continuous Auctions and Insider Trading (paper, Econometrica)** | Albert S. Kyle | 1985 | Informed trading, noise traders, and price impact lambda. | `concept_market_microstructure`, `concept_optimal_execution_market_impact` |
| 3 | **Market Microstructure Theory** | Maureen O'Hara | 1995 | Inventory and information models (Kyle, Glosten–Milgrom) of price formation. | `concept_market_microstructure`, `concept_liquidity` |
| 3 | **Optimal Execution of Portfolio Transactions (paper, Journal of Risk)** | Robert Almgren & Neil Chriss | 2000 | Mean-variance optimal liquidation trajectory under temporary/permanent impact. | `concept_optimal_execution_market_impact` |
| 3 | **Empirical Market Microstructure** | Joel Hasbrouck | 2007 | Econometrics of trades and quotes: Roll model, price discovery, information shares. | `concept_market_microstructure`, `concept_order_flow` |
| 3 | **Algorithmic and High-Frequency Trading** | Álvaro Cartea, Sebastian Jaimungal & José Penalva | 2015 | Stochastic control for optimal execution, market making, and statistical arbitrage. | `concept_optimal_execution_market_impact`, `concept_market_microstructure` |
| 3 | **The Financial Mathematics of Market Liquidity** | Olivier Guéant | 2016 | From Almgren–Chriss optimal execution to market making, block pricing, and buybacks. | `concept_optimal_execution_market_impact`, `concept_liquidity` |
| 3 | **Trades, Quotes and Prices** | Jean-Philippe Bouchaud, Julius Bonart, Jonathan Donier & Martin Gould | 2018 | Financial markets under the microscope: order-book dynamics and the square-root impact law. | `concept_optimal_execution_market_impact`, `concept_market_microstructure`, `concept_order_flow` |

## Track A — Probability & Statistics

| Level | Title | Author | Year | Key idea | Concepts |
|---|---|---|---|---|---|
| 1 | **Fifty Challenging Problems in Probability with Solutions** | Frederick Mosteller | 1965 | Classic puzzles that build probabilistic intuition (gambler's ruin, waiting times). | `concept_risk_of_ruin_drawdown`, `concept_probabilistic_thinking` |
| 1 | **Introduction to Probability** | Joseph K. Blitzstein & Jessica Hwang | 2014 | Intuition-first probability (Harvard Stat 110 companion): conditioning, expectation, distributions. | `concept_probability_fat_tails`, `concept_expectancy` |
| 2 | **Heard on the Street** | Timothy Falcon Crack | 1995 | Quantitative interview questions in probability and finance. | `concept_probabilistic_thinking` |
| 2 | **All of Statistics** | Larry Wasserman | 2004 | Concise modern statistics: inference, bootstrap, hypothesis testing, multiple testing. | `concept_overfitting_validation`, `concept_backtesting` |
| 2 | **A Practical Guide to Quantitative Finance Interviews** | Xinfeng Zhou | 2008 | Brain teasers, probability, stochastic calculus, and finance problems with solutions. | `concept_probabilistic_thinking`, `concept_stochastic_processes` |
| 3 | **An Introduction to Probability Theory and Its Applications (Vol. I)** | William Feller | 1950 | The classic treatment of random walks, ruin problems, and limit theorems. | `concept_random_walk_efficient_markets`, `concept_risk_of_ruin_drawdown` |
| 3 | **Statistical Inference** | George Casella & Roger L. Berger | 1990 | Rigorous estimation and hypothesis-testing theory. | `concept_overfitting_validation` |
| 3 | **Probability Theory: The Logic of Science** | E. T. Jaynes | 2003 | Probability as extended logic; Bayesian inference and maximum entropy. | `concept_probabilistic_thinking`, `concept_edge` |
| 3 | **Statistical Consequences of Fat Tails** | Nassim Nicholas Taleb | 2020 | Why sample statistics, the LLN, and standard risk metrics fail under fat tails. | `concept_probability_fat_tails`, `concept_performance_metrics` |

## Track F — Quant Research, ML & Validation

| Level | Title | Author | Year | Key idea | Concepts |
|---|---|---|---|---|---|
| 1 | **An Introduction to Statistical Learning** | James, Witten, Hastie & Tibshirani | 2013 | Accessible ML: regression, classification, resampling, regularisation, trees. | `concept_machine_learning_finance`, `concept_overfitting_validation` |
| 1 | **Python for Finance** | Yves Hilpisch | 2014 | Python tooling for financial analytics, simulation, and derivatives. | `concept_backtesting`, `concept_stochastic_processes` |
| 2 | **Finding Alphas** | Igor Tulchinsky et al. | 2015 | WorldQuant's practical guide to designing and testing alpha signals. | `concept_edge`, `concept_overfitting_validation` |
| 2 | **Machine Learning for Asset Managers** | Marcos López de Prado | 2020 | Denoising covariance matrices, clustering, feature importance, and backtest-overfitting tests. | `concept_machine_learning_finance`, `concept_overfitting_validation`, `concept_correlation_portfolio_risk` |
| 2 | **Machine Learning for Algorithmic Trading** | Stefan Jansen | 2020 | End-to-end Python workflow: data, alpha factors, models, backtests. | `concept_machine_learning_finance`, `concept_backtesting` |
| 3 | **The Elements of Statistical Learning** | Hastie, Tibshirani & Friedman | 2001 | The graduate reference for statistical learning; bias-variance and model selection. | `concept_machine_learning_finance`, `concept_overfitting_validation` |
| 3 | **The Deflated Sharpe Ratio (paper, Journal of Portfolio Management)** | David H. Bailey & Marcos López de Prado | 2014 | Correct the Sharpe ratio for selection bias across many trials and non-normal returns. | `concept_overfitting_validation`, `concept_performance_metrics` |

## Track E — Risk, Sizing & Portfolio Mathematics

| Level | Title | Author | Year | Key idea | Concepts |
|---|---|---|---|---|---|
| 2 | **A New Interpretation of Information Rate (paper, Bell System Technical Journal)** | J. L. Kelly Jr. | 1956 | Maximise expected log wealth: the Kelly criterion. | `concept_kelly_criterion_optimal_f` |
| 2 | **Portfolio Selection: Efficient Diversification of Investments** | Harry Markowitz | 1959 | Mean-variance optimisation and the efficient frontier. | `concept_correlation_portfolio_risk` |
| 2 | **Value at Risk** | Philippe Jorion | 1996 | VaR methodologies, backtesting VaR, and stress testing. | `concept_risk_of_ruin_drawdown`, `concept_correlation_portfolio_risk` |
| 3 | **Elements of Information Theory** | Thomas M. Cover & Joy A. Thomas | 1991 | Entropy, gambling and data compression, universal portfolios: the information-theory roots of Kelly. | `concept_kelly_criterion_optimal_f` |
| 3 | **Active Portfolio Management** | Richard C. Grinold & Ronald N. Kahn | 1995 | Fundamental law of active management: IR ≈ IC × √breadth. | `concept_edge`, `concept_performance_metrics`, `concept_position_sizing` |
| 3 | **Fractals and Scaling in Finance** | Benoit B. Mandelbrot | 1997 | Mandelbrot's technical papers on discontinuity, concentration, and scaling. | `concept_probability_fat_tails` |
| 3 | **Convex Optimization** | Stephen Boyd & Lieven Vandenberghe | 2004 | The optimisation toolkit behind portfolio construction and execution scheduling. | `concept_correlation_portfolio_risk`, `concept_optimal_execution_market_impact` |
| 3 | **Quantitative Risk Management** | Alexander J. McNeil, Rüdiger Frey & Paul Embrechts | 2005 | Extreme value theory, copulas, and risk measures (ES/VaR). | `concept_probability_fat_tails`, `concept_correlation_portfolio_risk` |
| 3 | **The Kelly Capital Growth Investment Criterion** | Leonard C. MacLean, Edward O. Thorp & William T. Ziemba (eds.) | 2011 | Collected theory and practice of growth-optimal betting, including fractional Kelly. | `concept_kelly_criterion_optimal_f`, `concept_position_sizing` |

## Track B — Stochastic Calculus & Derivatives

| Level | Title | Author | Year | Key idea | Concepts |
|---|---|---|---|---|---|
| 1 | **Paul Wilmott Introduces Quantitative Finance** | Paul Wilmott | 2001 | Accessible derivation of Black–Scholes and practical quant finance. | `concept_options_greeks`, `concept_stochastic_processes` |
| 3 | **Brownian Motion and Stochastic Calculus** | Ioannis Karatzas & Steven E. Shreve | 1988 | Rigorous graduate reference for stochastic calculus. | `concept_stochastic_processes` |
| 3 | **Arbitrage Theory in Continuous Time** | Tomas Björk | 1998 | Martingale pricing, PDEs, and interest-rate theory with economic intuition. | `concept_stochastic_processes` |
| 3 | **Stochastic Calculus for Finance I & II** | Steven E. Shreve | 2004 | Binomial to continuous-time: Brownian motion, Itô, risk-neutral pricing, change of measure. | `concept_stochastic_processes`, `concept_options_greeks` |
| 3 | **The Volatility Surface** | Jim Gatheral | 2006 | Stochastic and local volatility models; fitting and trading the implied-vol surface. | `concept_volatility`, `concept_options_greeks` |

## Track C — Time Series & Financial Econometrics

| Level | Title | Author | Year | Key idea | Concepts |
|---|---|---|---|---|---|
| 2 | **Analysis of Financial Time Series** | Ruey S. Tsay | 2002 | ARMA, GARCH, high-frequency data, VaR: the practitioner's time-series text. | `concept_time_series_statistics`, `concept_volatility` |
| 2 | **Statistics and Data Analysis for Financial Engineering** | David Ruppert & David S. Matteson | 2015 | Applied statistics in R: returns, heavy tails, copulas, GARCH, regression. | `concept_time_series_statistics`, `concept_probability_fat_tails` |
| 3 | **Time Series Analysis** | James D. Hamilton | 1994 | Definitive graduate text: unit roots, cointegration, regime-switching models. | `concept_time_series_statistics`, `concept_market_regimes` |
| 3 | **The Econometrics of Financial Markets** | John Y. Campbell, Andrew W. Lo & A. Craig MacKinlay | 1997 | Return predictability, event studies, microstructure, and asset-pricing tests. | `concept_random_walk_efficient_markets`, `concept_time_series_statistics`, `concept_market_microstructure` |
