# Partition 07_concepts


<!-- ===== FILE: trading-intelligence/07_concepts/amd-power-of-three.md ===== -->

---
id: concept_amd_power_of_three
type: concept
title: AMD / Power of Three (accumulation, manipulation, distribution)
partition: 07_concepts
layer: L3
aliases: [AMD, power of three, PO3, Judas swing, accumulation manipulation distribution, daily bias]
related: [concept_wyckoff_method, concept_liquidity, concept_trading_sessions_killzones, concept_smart_money_concepts, concept_liquidity_sweep_reversal]
derived_from: [concept_wyckoff_method, concept_dow_theory]
influenced_by: [person_michael_huddleston, person_richard_wyckoff]
sources:
  - {title: "TradeZella — AMD Model (Tanja Trades)", url: "https://www.tradezella.com/strategies/amd-model", tier: T3}
  - {title: "Chart Fanatics — Tanja's AMD Futures Trading Strategy", url: "https://www.chartfanatics.com/strategies/amd-model", tier: T2}
status: synthesized
---

# AMD / Power of Three

**Each candle (daily, 4H, session) is modelled as three phases:**

1. **Accumulation.** A quiet range (e.g., the Asian session) where positions
   build and liquidity forms on both sides.
2. **Manipulation (Judas swing).** A false move out of the range that sweeps
   stops on one side ([[concept_liquidity]]).
3. **Distribution.** The real directional expansion the other way, confirmed
   by a break of structure.

For a bullish daily candle: open → drop below the open (manipulation, which
forms the low/wick) → rally to the high (distribution) → close near the high.
Hence "power of three": open, high/low, close.

## Execution template (Tanja Trades, T2/T3)

- Futures day trading. **Filter out chop by trading only after a liquidity
  sweep and a confirmed displacement.**
- Best during **major news events**, with clear risk rules.
- Sequence: identify the range → wait for the sweep → enter once the new
  direction is confirmed (BOS/displacement) → target the opposing side of the
  range and beyond.

## Lineage (the clearest in this knowledge base)

Dow's three phases of a primary trend (accumulation → public participation →
distribution) → **Wyckoff's** accumulation/distribution schematics with
*spring* and *upthrust* (the manipulation) → ICT's **Power of Three / Judas
swing** → Chart Fanatics guests' AMD models. See [[concept_wyckoff_method]].


<!-- ===== FILE: trading-intelligence/07_concepts/auction-market-theory.md ===== -->

---
id: concept_auction_market_theory
type: concept
title: Auction Market Theory (balance, imbalance, value)
partition: 07_concepts
layer: L1
aliases: [AMT, market auction theory, balance and imbalance, market profile, TPO]
related: [concept_volume_profile, concept_vwap, concept_order_flow, concept_market_regimes, concept_mean_reversion, concept_breakout_trading]
influenced_by: [person_peter_steidlmayer, person_james_dalton]
derived_from: [concept_market_microstructure]
status: synthesized
---

# Auction Market Theory (AMT)

**Origin.** J. Peter Steidlmayer developed **Market Profile** at the Chicago
Board of Trade in the early-to-mid 1980s. He organised price by *time spent
at price* (TPO letters) and showed that markets behave as a continuous
two-sided auction. James Dalton's *Mind Over Markets* (1990) and *Markets in
Profile* (2007) turned it into a trading discipline.

## Axioms

1. **The market's purpose is to facilitate trade.** Price advertises
   opportunity, time regulates it, and volume measures success.
2. **Price moves to find the other side.** It auctions *up* until sellers
   respond, then *down* until buyers respond.
3. **Markets alternate between two states:**
   - **Balance.** Two-sided trade in a range around accepted value.
     Edges: fade the extremes back toward the **Point of Control**
     ([[concept_mean_reversion]]).
   - **Imbalance.** One-sided, directional search for new value. Edges:
     join the move and trade continuation ([[concept_breakout_trading]],
     [[concept_trend_following]]).
4. **Acceptance vs rejection.** Time and volume at a new price mean
   acceptance (value migrates). A fast excursion with little volume means
   rejection (excess).

## Key structures

- **Value Area** (~70% of volume or TPOs), **POC**, **VAH/VAL**, **single
  prints**, **poor highs/lows** (unfinished auctions that tend to be
  revisited), **initial balance** (first hour range), and day types
  (normal, trend, double-distribution, neutral).

## Chart Fanatics lineage

AMT is the most-featured framework among the channel's futures guests:
- **Fabio Valentini** reads balance vs imbalance, then applies *Direction →
  Location → Aggression*, with a trend model and a POC mean-reversion model
  (`strategy_fabio_valentini_amt_order_flow`).
- **Andrea Cimitan**, **Rajan Dhall** (auction theory), and **Forrest Knight**
  (volume-profile edges) all build on the same axioms.

See [[concept_volume_profile]] for the volume-based implementation.


<!-- ===== FILE: trading-intelligence/07_concepts/backtesting.md ===== -->

---
id: concept_backtesting
type: concept
title: Backtesting (manual & systematic)
partition: 07_concepts
layer: L8
aliases: [backtest, manual backtesting, replay, forward test, paper trading, Monte Carlo, walk forward]
related: [concept_overfitting_validation, concept_performance_metrics, concept_edge, concept_machine_learning_finance, concept_trading_journal_review]
status: synthesized
---

# Backtesting

**Testing a rule set on historical data before risking capital.**

## Manual (discretionary) backtesting

- Bar-replay through history, logging every valid setup by the written rules.
- Marci Silfrain spends hours every day **backtesting, sim trading, and
  paper trading**, more time than she spends live.
- Weakness: hindsight bias and lenient rule interpretation. Write the rules
  down first, and log *every* instance, including the ugly ones.

## Systematic backtesting

1. **Clean data:** survivorship-free; adjusted futures (back-adjusted vs
   ratio); realistic sessions.
2. **Realistic costs:** commissions, spread, slippage (especially on stops and
   around news).
3. **No look-ahead:** signals use only information available at the decision
   time. Beware repainting indicators and synthetic Heikin-Ashi fills.
4. **Out-of-sample and walk-forward tests,** plus Monte Carlo resampling of
   trade order for drawdown distributions ([[concept_risk_of_ruin_drawdown]]).

## Examples in this knowledge base

- **TG Capital Trident reconstruction** (TakeProfit): EURUSD M30, ~20% win
  rate, profitable out-of-sample 2023–24. One self-published test.
- **JJ Simon NQ 1-minute backtest video:** ~52% win rate and 1.66 profit
  factor *after filtering and parameter changes* (note the overfitting risk).

See [[concept_overfitting_validation]] before believing any backtest.


<!-- ===== FILE: trading-intelligence/07_concepts/bollinger-bands.md ===== -->

---
id: concept_bollinger_bands
type: concept
title: Bollinger Bands & Volatility Squeezes
partition: 07_concepts
layer: L3
aliases: [Bollinger Bands, BB, squeeze, Keltner channels, band walk, "%b", bandwidth]
related: [concept_volatility, concept_mean_reversion, concept_breakout_trading, concept_trendlines]
influenced_by: [person_john_bollinger]
status: synthesized
---

# Bollinger Bands

John Bollinger (1980s; *Bollinger on Bollinger Bands*, 2001):
**20-period SMA ± 2 standard deviations.** BabyPips Elementary Grade 5.

## Readings

- **Squeeze.** Bandwidth at a multi-month low means volatility compression,
  which precedes expansion ([[concept_volatility]],
  [[concept_breakout_trading]]).
- **Band walk.** In strong trends price "walks" the outer band. That is *not*
  a reversal signal.
- **Mean reversion.** In ranges, tags of the outer band revert toward the
  mid-band ([[concept_mean_reversion]]).
- **%b and bandwidth** quantify position and compression.

## In this knowledge base

Marci Silfrain uses Bollinger Bands as **context** in her measured-move trend
strategy, helping spot continuations versus possible reversals
(`strategy_marci_silfrain_measured_move`).


<!-- ===== FILE: trading-intelligence/07_concepts/breakout-trading.md ===== -->

---
id: concept_breakout_trading
type: concept
title: Breakout Trading (and fakeouts)
partition: 07_concepts
layer: L4
aliases: [breakout, breakouts and fakeouts, opening range breakout, ORB, range expansion, false breakout, fakeout]
related: [concept_trend_following, concept_volatility, concept_chart_patterns, concept_liquidity_sweep_reversal, concept_auction_market_theory, concept_bollinger_bands]
status: synthesized
---

# Breakout Trading

BabyPips High School covers trading breakouts (and **fakeouts**).

## Valid breakout checklist

1. **Compression before expansion:** a tight range, low ATR, a squeeze
   ([[concept_volatility]]).
2. **Participation:** volume or delta expansion, value migrating (AMT
   acceptance).
3. **Close beyond the level**, then hold or retest (role reversal).
4. **Room to run:** no immediate HTF level ahead.

## Variants

- **Donchian / N-day high** (trend following).
- **Opening range breakout** (Crabel): the first 5–30 minutes of a session.
- **Pattern breakouts:** flags, triangles, VCP pivots
  ([[concept_growth_momentum_canslim]]).

## The fakeout problem

Most breakouts in **ranges** fail (Al Brooks). The failure is itself a
setup: a breakout that traps traders and reverses is a
[[concept_liquidity_sweep_reversal]]. Decide in advance which game you play:
breakout continuation (trend regimes) or failed-breakout fade (range regimes).


<!-- ===== FILE: trading-intelligence/07_concepts/candlestick-patterns.md ===== -->

---
id: concept_candlestick_patterns
type: concept
title: Japanese Candlestick Patterns
partition: 07_concepts
layer: L3
aliases: [candlesticks, doji, hammer, shooting star, engulfing, morning star, evening star, harami, marubozu, heikin ashi]
related: [concept_price_action, concept_support_resistance, concept_chart_patterns]
influenced_by: [person_munehisa_homma, person_steve_nison]
status: synthesized
---

# Japanese Candlestick Patterns

Developed in 18th-century Japanese rice markets (attributed to Munehisa
Homma). Steve Nison brought them to the West (*Japanese Candlestick Charting
Techniques*, 1991). BabyPips teaches them in Elementary Grade 2.

## Anatomy

Body = open→close. Wicks/shadows = high and low. Color/fill = direction. A
long wick shows **rejection**, i.e., a failed auction at that extreme
([[concept_auction_market_theory]]).

## Core patterns

| Type | Patterns | Message |
|---|---|---|
| Indecision | Doji, spinning top | Balance; wait |
| Single-bar reversal | Hammer / hanging man, shooting star / inverted hammer | Rejection of an extreme |
| Two-bar | Bullish/bearish engulfing, harami, tweezer tops/bottoms | Momentum shift |
| Three-bar | Morning/evening star, three white soldiers / three black crows | Reversal / continuation |
| Momentum | Marubozu | One-sided control (displacement) |

## Rules

- **Patterns only matter at a level**, in context ([[concept_price_action]]).
- **Confirmation.** Many playbooks require the *next* candle to confirm,
  e.g., TG Capital's Trident needs a doji wick into the FVG midpoint, *then*
  a confirmation candle.
- **Statistics are weak standalone.** Bulkowski's studies show most patterns
  sit only modestly above chance without context.

**Heikin Ashi** (BabyPips Summer School) averages candles to smooth trend
reading. Its prices are synthetic, so never use them for backtest fills.


<!-- ===== FILE: trading-intelligence/07_concepts/carry-trade.md ===== -->

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


<!-- ===== FILE: trading-intelligence/07_concepts/chart-patterns.md ===== -->

---
id: concept_chart_patterns
type: concept
title: Classical Chart Patterns
partition: 07_concepts
layer: L3
aliases: [head and shoulders, double top, double bottom, triangles, wedges, flags, pennants, cup and handle, rectangles, gaps]
related: [concept_support_resistance, concept_breakout_trading, concept_trendlines, concept_liquidity, concept_price_action]
influenced_by: [person_robert_d_edwards, person_john_magee, person_thomas_bulkowski, person_peter_brandt]
status: synthesized
---

# Classical Chart Patterns

Codified by Schabacker (1930s) and **Edwards & Magee**, *Technical Analysis
of Stock Trends* (1948). Catalogued statistically by **Thomas Bulkowski**,
*Encyclopedia of Chart Patterns*. BabyPips Middle School Grade 7.

| Family | Patterns | Typical rule |
|---|---|---|
| Reversal | Head & shoulders (and inverse), double/triple tops & bottoms, rounding | Break of neckline; target = pattern height |
| Continuation | Flags, pennants, rectangles, ascending/descending triangles, cup & handle | Breakout in trend direction; measured move |
| Bilateral | Symmetrical triangles, wedges | Trade the break, either side |
| Gaps | Breakaway, runaway, exhaustion | Context-dependent continuation or exhaustion |

## Peter Brandt's discipline (classical charting as a business)

Brandt (*Diary of a Professional Commodity Trader*) trades classical
patterns with strict rules: few patterns qualify, risk is predefined, and
most trades fail, but winners pay for the losers. Expect a ~30–40% win rate
with positive expectancy ([[concept_expectancy]]).

## Modern reinterpretation

Double tops/bottoms = **equal highs/lows = liquidity** ([[concept_liquidity]]).
The "failed pattern" is often the better trade (Brandt: "failed signals are
among the most reliable"). That is the same insight as SMC's sweep-and-reverse.


<!-- ===== FILE: trading-intelligence/07_concepts/correlation-portfolio-risk.md ===== -->

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


<!-- ===== FILE: trading-intelligence/07_concepts/divergence.md ===== -->

---
id: concept_divergence
type: concept
title: Divergence (regular & hidden)
partition: 07_concepts
layer: L3
aliases: [RSI divergence, MACD divergence, hidden divergence, regular divergence, delta divergence]
related: [concept_oscillators_momentum, concept_smt_divergence, concept_order_flow, concept_mean_reversion]
status: synthesized
---

# Divergence

**Price and a momentum measure disagree.** BabyPips covers trading
divergences in Summer School.

| Type | Price | Indicator | Implies |
|---|---|---|---|
| Regular bullish | Lower low | Higher low | Possible reversal up |
| Regular bearish | Higher high | Lower high | Possible reversal down |
| Hidden bullish | Higher low | Lower low | Trend continuation up |
| Hidden bearish | Lower high | Higher high | Trend continuation down |

## Three flavours of the same idea

1. **Oscillator divergence** (RSI/MACD): momentum fading.
2. **Order-flow divergence** (CVD vs price): aggression fading or being
   absorbed ([[concept_order_flow]]).
3. **Intermarket / SMT divergence:** correlated assets fail to confirm
   ([[concept_smt_divergence]]).

All three say *the push is losing participation*. None says *when* it
reverses, so pair them with a structure trigger ([[concept_market_structure]]).


<!-- ===== FILE: trading-intelligence/07_concepts/dow-theory.md ===== -->

---
id: concept_dow_theory
type: concept
title: Dow Theory
partition: 07_concepts
layer: L2
aliases: [Dow theory, primary trend, secondary reaction, confirmation]
related: [concept_market_structure, concept_trend_following, concept_intermarket_analysis]
influenced_by: [person_charles_dow]
status: synthesized
---

# Dow Theory

Developed from Charles Dow's *Wall Street Journal* editorials (c. 1900–1902).
William Hamilton (*The Stock Market Barometer*, 1922) and Robert Rhea
(*The Dow Theory*, 1932) formalised it. It is the **root of modern technical
analysis**.

## Six tenets

1. **The market discounts everything.**
2. **Three trends:** primary (months–years), secondary (weeks–months), minor
   (days). This is the original [[concept_multi_timeframe_analysis]].
3. **Primary trends have three phases:** accumulation, public participation,
   distribution. This anticipates Wyckoff and ICT's AMD
   ([[concept_wyckoff_method]], [[concept_amd_power_of_three]]).
4. **Averages must confirm each other** (Industrials and Rails/Transports),
   the root of [[concept_intermarket_analysis]] and SMT divergence
   ([[concept_smt_divergence]]).
5. **Volume must confirm the trend.**
6. **A trend persists until a definitive reversal signal.** Defined by
   successive peaks and troughs, it is the origin of
   [[concept_market_structure]] (HH/HL) and the philosophy of
   [[concept_trend_following]].

## Descendants

Market structure (BOS/CHoCH) · SMT divergence (correlated-index
non-confirmation) · Wyckoff phases · Elliott Wave (impulse/correction) ·
trend following.


<!-- ===== FILE: trading-intelligence/07_concepts/edge.md ===== -->

---
id: concept_edge
type: concept
title: Edge (positive expectancy, repeatable)
partition: 07_concepts
layer: L0
aliases: [trading edge, statistical edge, alpha]
related: [concept_expectancy, concept_probabilistic_thinking, concept_backtesting, concept_overfitting_validation, concept_performance_metrics]
derived_from: [concept_probability_fat_tails]
influenced_by: [person_ed_thorp, person_mark_douglas]
status: synthesized
---

# Edge

**Definition.** An edge is a *repeatable* condition under which the expected
value of a trade, after costs, is positive. It is a property of a
**distribution of outcomes**, never of a single trade.

**Formally:** `E = p·W̄ − (1−p)·L̄ − costs > 0`, where `p` is the win rate,
`W̄` the average win and `L̄` the average loss (see [[concept_expectancy]]).

## What edge is made of

1. **A cause.** Someone is on the other side for a structural reason: forced
   liquidation, hedging flow, stop clusters ([[concept_liquidity]]),
   behavioural bias, a risk premium ([[concept_carry_trade]]), or an
   informational lag.
2. **A detector.** A rule that identifies the condition with acceptable false
   positives (the setup, L4).
3. **An execution path.** A way to capture it without costs and slippage
   eating it ([[concept_optimal_execution_market_impact]]).
4. **A survival layer.** Sizing that lets the law of large numbers play out
   ([[concept_position_sizing]], [[concept_risk_of_ruin_drawdown]]).

## Lineage

Thorp framed edge in casino terms first (card counting gives a measurable
advantage) and carried the same logic to markets, sizing it with the Kelly
criterion. Mark Douglas made the psychological corollary famous: *"anything can
happen"* on one trade, while the edge plays out over a series.

## Pitfalls

- **Edge ≠ win rate.** Trend followers win 30–40% of the time and still have
  an edge. Many 80%-win-rate scalpers have none once costs are counted.
- **Edges decay** as they are crowded. Monitor them with
  [[concept_trading_journal_review]].
- A backtest is a *hypothesis* about edge until it survives
  out-of-sample testing ([[concept_overfitting_validation]]).


<!-- ===== FILE: trading-intelligence/07_concepts/elliott-wave.md ===== -->

---
id: concept_elliott_wave
type: concept
title: Elliott Wave Theory
partition: 07_concepts
layer: L3
aliases: [Elliott wave, impulse wave, corrective wave, ABC correction, wave count]
related: [concept_fibonacci, concept_market_structure, concept_dow_theory, concept_market_sentiment]
derived_from: [concept_dow_theory]
influenced_by: [person_ralph_elliott, person_robert_prechter]
status: synthesized
---

# Elliott Wave Theory

Ralph Nelson Elliott (1930s; *The Wave Principle*, 1938). Popularised by
Frost & Prechter, *Elliott Wave Principle* (1978). BabyPips Summer School.

## Structure

- **Impulse:** 5 waves in the trend direction (1-2-3-4-5).
  Rules: wave 2 never retraces beyond the start of wave 1; wave 3 is never the
  shortest; wave 4 does not overlap wave 1's territory (in standard impulses).
- **Correction:** 3 waves against the trend (A-B-C), plus flats, triangles,
  and combinations.
- **Fractal:** waves nest within waves of higher degree.
- **Fibonacci relationships** between wave lengths ([[concept_fibonacci]]).

## Assessment

It is a useful *vocabulary* for trend/correction rhythm, and it gives the
classic "wave 3 is the strongest" intuition behind trading the first pullback
after a structure break. But counts are highly subjective and revisable,
which makes them hard to falsify. Use the rules as invalidation levels, not
as forecasts.


<!-- ===== FILE: trading-intelligence/07_concepts/episodic-pivot.md ===== -->

---
id: concept_episodic_pivot
type: concept
title: Episodic Pivot (EP)
partition: 07_concepts
layer: L4
aliases: [episodic pivot, EP, earnings gap, catalyst gap, neglected stock gap-up]
related: [concept_growth_momentum_canslim, concept_news_trading, concept_breakout_trading, concept_vwap]
derived_from: [concept_growth_momentum_canslim]
influenced_by: [person_pradeep_bonde]
status: synthesized
---

# Episodic Pivot (EP)

Coined and taught by **Pradeep Bonde (Stockbee)**. He has appeared on Words
of Rizdom and Chart Fanatics discussions of what separates profitable
traders. The episode's exact air date is unconfirmed.

## Definition

A **catalyst** (earnings surprise, guidance raise, FDA approval, contract,
regulatory change) causes a **large gap on huge volume** in a stock that the
market had **neglected**. The event forces a repricing. Because institutions
cannot build positions in one day, the move can trend for weeks or months.

## Typical criteria (practitioner heuristics; verify against Bonde's material)

- Gap ≥ ~10% on volume far above average (often 3×+).
- Little prior run-up: the stock was *not* already a momentum leader
  (the "neglect" factor).
- A genuine fundamental change, not a sympathy move.
- Entry on day 1 (opening range high, or holding above the open/AVWAP),
  stop below the day's low ([[concept_vwap]]).

## Why it can work

It is a behavioural and microstructure edge: underreaction to news
(post-earnings announcement drift is a well-documented anomaly) plus slow
institutional accumulation.

**Source note:** the rules above are a synthesis. Specific secondhand claims
(e.g., "Bonde relied on just one strategy") come from social posts and are
T4. Scrape the Chart Fanatics/Words of Rizdom episode to upgrade them.


<!-- ===== FILE: trading-intelligence/07_concepts/expectancy.md ===== -->

---
id: concept_expectancy
type: concept
title: Expectancy (expected value per trade)
partition: 07_concepts
layer: L6
aliases: [expectancy, expected value, EV, SQN, system quality number, profit factor]
related: [concept_edge, concept_risk_reward_r_multiples, concept_position_sizing, concept_performance_metrics, concept_probabilistic_thinking]
influenced_by: [person_van_tharp, person_ed_thorp]
status: synthesized
---

# Expectancy

`E[R] = p·W̄_R − (1 − p)·L̄_R` (in R-multiples)

Example: 40% win rate, average win 2.5R, average loss 1R →
`E = 0.4×2.5 − 0.6×1 = +0.4R per trade`. Over 100 trades at 1% risk that is
roughly +40% before compounding and costs.

## Related statistics

- **Profit factor** = gross profit ÷ gross loss.
- **SQN (Van Tharp)** = `√N · mean(R) / stdev(R)`. It captures expectancy
  *and* consistency. It is essentially a t-statistic of the edge.
- **Expectancy per unit time** = E × trades per period. A small edge traded
  often can beat a large edge traded rarely ([[concept_scalping]]).

## Win rate is not expectancy

| System | Win % | Avg W | Avg L | E (R) |
|---|---|---|---|---|
| Trend follower | 35% | 3.0R | 1R | +0.40 |
| Scalper | 75% | 0.4R | 1R | +0.05 |
| Mean reverter (blowup-prone) | 85% | 0.3R | 2.5R | −0.12 |

The third looks great for months and is a losing system
([[concept_probability_fat_tails]]).

Mark Douglas's insight: once you *think in expectancy*, a single loss carries
no information, so you can execute without fear ([[concept_probabilistic_thinking]]).


<!-- ===== FILE: trading-intelligence/07_concepts/fair-value-gap.md ===== -->

---
id: concept_fair_value_gap
type: concept
title: Fair Value Gap (FVG), Inversion FVG, Imbalance
partition: 07_concepts
layer: L3
aliases: [FVG, fair value gap, imbalance, inefficiency, IFVG, inversion fair value gap, BPR, balanced price range, consequent encroachment]
related: [concept_smart_money_concepts, concept_market_structure, concept_order_blocks_breakers, concept_volume_profile, concept_trade_execution]
derived_from: [concept_chart_patterns]
influenced_by: [person_michael_huddleston]
status: synthesized
---

# Fair Value Gap (FVG)

**Definition (3-candle).** In a bullish FVG, candle 1's high is below
candle 3's low. The middle candle moved so fast that a price range traded
only one-sided. Bearish is the mirror image.

```
bullish FVG = [high(c1), low(c3)]  when low(c3) > high(c1)
```

## Interpretation

- Represents **one-sided, inefficient delivery** (displacement). It is the
  candlestick analogue of a **low-volume node** ([[concept_volume_profile]])
  and of classic **gaps** in Edwards & Magee.
- Price often **revisits** the gap to rebalance before continuing. Entries at
  the gap or its midpoint (**consequent encroachment, 50%**) offer a tight
  stop.
- **Inversion FVG (IFVG).** An FVG that price closes *through* flips polarity.
  A failed bullish gap becomes resistance. Candace Lau and Trader Kane use
  IFVGs as reversal confirmation.
- **Balanced Price Range (BPR).** Overlapping bullish and bearish FVGs.

## Rules of thumb

1. Only FVGs **created by displacement that broke structure** matter.
   Random gaps in chop do not.
2. Context first: in a discount zone in an uptrend, a bullish FVG is a
   candidate entry ([[concept_premium_discount_ote]]).
3. **TG Capital's "Trident":** FVG + a doji wick into its midpoint + a
   confirmation candle, inside the London kill zone with stacked EMAs
   (`strategy_tg_capital_trident`).

## Evidence note

FVG "fills" are common partly by construction: price frequently retraces
into any recent range. Measure the fill rate *and* the post-fill
continuation rate in your market before relying on it.


<!-- ===== FILE: trading-intelligence/07_concepts/fibonacci.md ===== -->

---
id: concept_fibonacci
type: concept
title: Fibonacci Retracements & Extensions
partition: 07_concepts
layer: L3
aliases: [fibonacci, fib, 38.2, 50, 61.8, golden ratio, extensions, 1.272, 1.618]
related: [concept_premium_discount_ote, concept_elliott_wave, concept_support_resistance, concept_trade_management]
influenced_by: [person_ralph_elliott]
status: synthesized
---

# Fibonacci Retracements & Extensions

Ratios from the Fibonacci sequence: **23.6%, 38.2%, 50%** (not Fibonacci,
but universal), **61.8%, 78.6%**, and extensions **127.2%, 161.8%, 261.8%**.
BabyPips Elementary Grade 3.

## Use

- **Retracement.** Draw from swing low to swing high (in an uptrend). Look
  for pullbacks to hold 38.2–61.8% in healthy trends.
- **Extensions.** Profit targets beyond the prior swing.
- **Confluence.** A Fib level coinciding with S/R, an order block, or a
  trendline is the only version worth using.

## Lineage & evidence

Ralph Nelson Elliott tied wave proportions to Fibonacci ratios (1930s) →
mainstream TA → ICT's OTE band (62–79%) ([[concept_premium_discount_ote]]).

**Evidence:** independent studies find little predictive power in Fib levels
*per se*. Their value is mostly **self-reinforcing attention** plus a
**disciplined location filter** that improves R:R. Treat them as zones.


<!-- ===== FILE: trading-intelligence/07_concepts/fundamental-macro-analysis.md ===== -->

---
id: concept_fundamental_macro_analysis
type: concept
title: Fundamental & Macro Analysis (rates, central banks, growth, inflation)
partition: 07_concepts
layer: L3
aliases: [fundamental analysis, macro, interest rates, central banks, monetary policy, inflation, GDP, NFP, CPI, economic machine, debt cycle]
related: [concept_intermarket_analysis, concept_news_trading, concept_carry_trade, concept_market_sentiment, concept_reflexivity, concept_market_regimes]
influenced_by: [person_ray_dalio, person_stanley_druckenmiller, person_george_soros]
status: synthesized
---

# Fundamental & Macro Analysis

BabyPips Undergraduate Freshman covers the macro fundamentals behind currency
moves. For FX, **relative interest-rate expectations** dominate everything
else.

## The macro stack

1. **Monetary policy.** Policy rates, forward guidance, QE/QT. A currency
   appreciates when its central bank is expected to be *more hawkish than
   priced*.
2. **Growth & inflation data.** GDP, PMIs, employment (NFP), CPI/PCE, retail
   sales. Markets trade the *surprise versus consensus*, not the level
   ([[concept_news_trading]]).
3. **Liquidity.** Central-bank balance sheets and credit conditions.
   Druckenmiller: "Earnings don't move the overall market; it's the Federal
   Reserve Board... focus on the central banks and the movement of liquidity."
4. **Debt cycles.** Dalio's *How the Economic Machine Works*: productivity
   growth + short-term debt cycle (~5–8 yrs) + long-term debt cycle (~50–75 yrs).
5. **Positioning & sentiment** ([[concept_market_sentiment]]).

## For short-term technical traders

- Know the calendar. Many Chart Fanatics guests trade *around* news (Tanja's
  AMD model favours major news events; JJ Simon notes that news resets fair
  price), while prop-firm guidance often avoids news because of slippage.
- Macro defines the **regime** inside which technical setups fire
  ([[concept_market_regimes]]).

## Lineage

Classical economics → Keynes (expectations and the "beauty contest") →
Soros (reflexivity) → Druckenmiller (liquidity + concentration) → Dalio
(economic machine, risk parity).


<!-- ===== FILE: trading-intelligence/07_concepts/growth-momentum-canslim.md ===== -->

---
id: concept_growth_momentum_canslim
type: concept
title: Growth-Stock Momentum (CANSLIM, SEPA, VCP)
partition: 07_concepts
layer: L4
aliases: [CANSLIM, SEPA, VCP, volatility contraction pattern, stage analysis, pivot buy point, relative strength, superperformance]
related: [concept_breakout_trading, concept_episodic_pivot, concept_trend_following, concept_moving_averages, concept_position_sizing]
derived_from: [concept_trend_following]
influenced_by: [person_william_oneil, person_mark_minervini, person_nicolas_darvas, person_jesse_livermore, person_stan_weinstein]
status: synthesized
---

# Growth-Stock Momentum (CANSLIM → SEPA → VCP)

## CANSLIM (William O'Neil, *How to Make Money in Stocks*, 1988)

**C**urrent quarterly earnings · **A**nnual earnings growth · **N**ew
product/high · **S**upply & demand (shares, volume) · **L**eader vs laggard
(relative strength) · **I**nstitutional sponsorship · **M**arket direction.
Buy proper bases (cup-with-handle) at the pivot. **Cut every loss at 7–8%.**

## Stage analysis (Stan Weinstein, 1988)

Stage 1 basing → **Stage 2 advancing** (buy) → Stage 3 topping → Stage 4
declining. Uses the 30-week MA.

## SEPA & VCP (Mark Minervini)

- **Trend template:** price above the rising 150/200-day MAs, and above the
  50-day, near 52-week highs, with high RS.
- **Volatility Contraction Pattern:** successive pullbacks contract
  (e.g., 25% → 12% → 6%) with drying volume. Buy the pivot breakout. The
  stop sits just under the last contraction, so risk is tiny relative to
  upside.
- **Risk:** small losses, a high average-gain-to-loss ratio, and progressive
  exposure as the market confirms.

## Lineage

Livermore (pivotal points, pyramiding) → Darvas (box theory, *How I Made
$2,000,000 in the Stock Market*, 1960) → O'Neil (CANSLIM, IBD) → Minervini
(SEPA, US Investing Champion) → Oliver Kell, **Clement Ang** (US Investing
Championship 2024–25; TraderLion community) and **Pradeep Bonde's**
episodic pivots ([[concept_episodic_pivot]]).


<!-- ===== FILE: trading-intelligence/07_concepts/intermarket-analysis.md ===== -->

---
id: concept_intermarket_analysis
type: concept
title: Intermarket Analysis & Correlations
partition: 07_concepts
layer: L3
aliases: [intermarket, correlations, DXY, bonds stocks commodities, currency correlations, risk on risk off]
related: [concept_fundamental_macro_analysis, concept_smt_divergence, concept_correlation_portfolio_risk, concept_dow_theory]
influenced_by: [person_john_murphy]
status: synthesized
---

# Intermarket Analysis

John Murphy, *Intermarket Technical Analysis* (1991) and *Intermarket
Analysis* (2004): **bonds, stocks, commodities, and currencies move in linked
cycles.** BabyPips Sophomore covers the US Dollar Index, intermarket
correlations, and using equities to trade FX.

## Classic relationships (regime-dependent!)

| Relationship | Typical sign | Mechanism |
|---|---|---|
| USD vs commodities (gold, oil) | Negative | Commodity pricing in USD |
| Bonds (prices) vs commodities | Negative | Inflation expectations |
| Stocks vs bonds (prices) | Positive in deflationary regimes, negative in inflationary | Discount rate vs growth |
| AUD, NZD, CAD vs commodities | Positive | Terms of trade |
| JPY, CHF vs risk assets | Negative | Safe-haven / funding currencies ([[concept_carry_trade]]) |
| EURUSD vs GBPUSD | Strongly positive | Shared USD leg, the basis of [[concept_smt_divergence]] |

## Uses

1. **Confirmation / non-confirmation** (Dow's principle).
2. **Hidden risk.** Long EURUSD + long GBPUSD + short USDCHF is one trade, not
   three ([[concept_correlation_portfolio_risk]]).
3. **Lead-lag.** Bonds often turn before stocks; the dollar drives commodities.

Correlations are unstable. Recompute them on rolling windows.


<!-- ===== FILE: trading-intelligence/07_concepts/kelly-criterion-optimal-f.md ===== -->

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


<!-- ===== FILE: trading-intelligence/07_concepts/leverage-margin.md ===== -->

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


<!-- ===== FILE: trading-intelligence/07_concepts/liquidity-sweep-reversal.md ===== -->

---
id: concept_liquidity_sweep_reversal
type: concept
title: Liquidity Sweep Reversal (stop-hunt reversal)
partition: 07_concepts
layer: L4
aliases: [liquidity sweep reversal, stop hunt reversal, liquidity grab, turtle soup, spring, upthrust, failed breakout, Judas swing]
related: [concept_liquidity, concept_market_structure, concept_fair_value_gap, concept_amd_power_of_three, concept_order_flow, concept_breakout_trading, concept_smt_divergence]
derived_from: [concept_wyckoff_method, concept_liquidity]
influenced_by: [person_richard_wyckoff, person_linda_raschke, person_michael_huddleston]
sources:
  - {title: "Chart Fanatics — Liquidity Grab Trading Strategy (Marco Trades)", url: "https://www.chartfanatics.com/playbook/liquidity-playbook", tier: T2}
  - {title: "TradeZella — NQ Liquidity Sweep & Reversal Scalping Strategy (Candace Lau)", url: "https://www.tradezella.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy", tier: T3}
  - {title: "STEAL This EASY Liquidity TRAP Trading Strategy (Chart Fanatics video, transcript summary)", url: "https://my.infocaptor.com/hub/summaries/chart-fanatics/steal-this-easy-liquidity-trap-trading-strategy-$500k+-perfect-sniper-entries-DAnXM7C16h0", tier: T3}
status: synthesized
---

# Liquidity Sweep Reversal

**The single most repeated setup across Chart Fanatics' futures and FX
guests.** Price runs a pool of stops beyond an obvious high or low, fails to
continue, and reverses.

## Generic rule set

1. **Mark liquidity:** swing highs/lows, equal highs/lows, session extremes
   (Asia, London, PDH/PDL) ([[concept_liquidity]]).
2. **Wait for the sweep:** price trades *through* the level, ideally in a
   kill zone and against HTF bias ([[concept_trading_sessions_killzones]]).
3. **Confirm the failure:** displacement back inside, plus a market structure
   shift ([[concept_market_structure]]). Optional: an IFVG
   ([[concept_fair_value_gap]]), SMT divergence ([[concept_smt_divergence]]),
   or order-flow absorption/trapped traders ([[concept_order_flow]]).
4. **Enter:** on the retrace into the FVG/OB created by the displacement, or
   on the LTF break.
5. **Stop:** beyond the sweep extreme. **Target:** the opposing liquidity
   pool. Minimum **1:2 R:R** (Candace Lau).

## Variants in this knowledge base

| Trader | Twist |
|---|---|
| **Marco Trades** (CF playbook, T2) | For buys: wait for price to trade *below a low*, look for confirmation, buy, stop under that low. Sells mirror this at highs. |
| **Candace Lau** (T3) | NQ scalps; HTF context + premium/discount + IFVG + strong displacement with speed |
| **Liquidity TRAP video** (T3) | Whiteboard of spiked liquidity above/below swing points; sell or buy after the sweep |
| **Tanja Trades AMD** | The sweep is the "manipulation" leg ([[concept_amd_power_of_three]]) |
| **Trader Yush** | Order-flow version: trapped buyers/sellers |

## Lineage

Wyckoff **spring/upthrust** (1930s) → Linda Raschke & Larry Connors'
**"Turtle Soup"** (*Street Smarts*, 1995): fading 20-day breakouts that fail,
an explicit stop-hunt reversal named after the Turtles' breakout rule → ICT
liquidity runs and the Judas swing → today's sweep-reversal scalps.


<!-- ===== FILE: trading-intelligence/07_concepts/liquidity.md ===== -->

---
id: concept_liquidity
type: concept
title: Liquidity (resting orders, stop pools, sweeps)
partition: 07_concepts
layer: L1
aliases: [liquidity pool, liquidity sweep, liquidity run, buy-side liquidity, sell-side liquidity, stop hunt, liquidity grab, equal highs, equal lows]
related: [concept_market_microstructure, concept_market_structure, concept_liquidity_sweep_reversal, concept_smart_money_concepts, concept_order_flow, concept_amd_power_of_three]
derived_from: [concept_wyckoff_method, concept_market_microstructure]
influenced_by: [person_michael_huddleston, person_richard_wyckoff]
sources:
  - {title: "Chart Fanatics — Liquidity Grab Trading Strategy (Marco Trades)", url: "https://www.chartfanatics.com/playbook/liquidity-playbook", tier: T2}
  - {title: "TradeZella — NQ Liquidity Sweep & Reversal (Candace Lau)", url: "https://www.tradezella.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy", tier: T3}
status: synthesized
---

# Liquidity

Two meanings that traders often conflate:

1. **Microstructure liquidity.** How much size can trade near the current
   price without moving it (depth, spread, resiliency). See
   [[concept_market_microstructure]].
2. **"Liquidity" in SMC/ICT usage.** *Where resting orders, especially stop
   orders, cluster.* These are the pools that large participants need in
   order to fill size.

## Where liquidity rests (sense 2)

| Pool | Why orders sit there |
|---|---|
| **Above swing highs / below swing lows** | Stops of traders positioned against the move; breakout entry orders |
| **Equal highs / equal lows** ("double tops/bottoms") | Retail traders treat them as strong S/R, so stops stack just beyond |
| **Session extremes** (Asia high/low, London high/low, prior-day high/low, overnight high/low) | Reference levels used by many participants ([[concept_trading_sessions_killzones]]) |
| **Trendline touches** | Stops sit under the "obvious" trendline ([[concept_trendlines]]) |
| **Round numbers** | Order clustering |

**Buy-side liquidity (BSL)** sits above highs (buy stops). **Sell-side
liquidity (SSL)** sits below lows (sell stops).

## The core mechanic

A large seller needs buyers. Triggering the buy stops above a high supplies
those buyers, so the seller can fill while price trades *through* the high
(the **sweep**). If no genuine demand follows, price reverses: a
**liquidity sweep / stop hunt / spring / upthrust**. The important part is
not that price reached the pool, but *what happens after it is taken*
(Candace Lau's framing): displacement and a market-structure shift confirm
the reversal ([[concept_liquidity_sweep_reversal]]).

## Lineage

This is Wyckoff's **spring** and **upthrust** (1930s), re-described by ICT in
the 2010s as liquidity runs ([[concept_wyckoff_method]] →
[[concept_smart_money_concepts]]). Tape readers and order-flow traders
describe the same event as **trapped traders** ([[concept_order_flow]]).

## Pitfalls

- Hindsight bias: every reversal *looks* like a sweep afterwards. Require a
  confirmation rule.
- Liquidity is a **target** as well as a reversal point. In a trending
  market, price often runs a pool and *continues* to the next one.


<!-- ===== FILE: trading-intelligence/07_concepts/machine-learning-finance.md ===== -->

---
id: concept_machine_learning_finance
type: concept
title: Machine Learning in Finance (labels, leakage, meta-labeling)
partition: 07_concepts
layer: L0
aliases: [financial machine learning, triple barrier, meta-labeling, purged cross-validation]
related: [concept_backtesting, concept_overfitting_validation, concept_time_series_statistics, concept_performance_metrics]
influenced_by: [person_marcos_lopez_de_prado]
status: synthesized
---

# Machine Learning in Finance

Financial data has a low signal-to-noise ratio, is non-stationary, and is
autocorrelated. Off-the-shelf ML overfits it badly. The core corrections
come from López de Prado, *Advances in Financial Machine Learning* (2018):

1. **Better bars.** Sample by information (dollar, volume, or tick-imbalance
   bars) instead of time. The returns come out closer to i.i.d.
2. **Triple-barrier labeling.** Label each event by which barrier is hit
   first: profit-take, stop-loss, or time limit. The label then matches how a
   trade actually resolves ([[concept_trade_management]]).
3. **Meta-labeling.** A primary model (it can be a discretionary setup!)
   decides *side*. A secondary ML model decides *whether to take the trade and
   how big*. This is the most practical bridge between a discretionary
   playbook and ML ([[concept_position_sizing]]).
4. **Purged and embargoed K-fold CV.** Remove training samples whose labels
   overlap the test window, to prevent leakage.
5. **Feature importance** (MDI, MDA, SFI) instead of chasing in-sample accuracy.
6. **Deflated Sharpe ratio** and the probability of backtest overfitting
   correct for the number of trials ([[concept_overfitting_validation]]).

## Practitioner warning

Most ML funds fail for process reasons: siloed researchers, backtest
overfitting, and non-stationary features. They rarely fail for model-choice
reasons. Start with a sound economic hypothesis ([[concept_edge]]) and use ML
to *filter and size*, not to discover the whole strategy.


<!-- ===== FILE: trading-intelligence/07_concepts/market-microstructure.md ===== -->

---
id: concept_market_microstructure
type: concept
title: Market Microstructure (order book, bid/ask, order types)
partition: 07_concepts
layer: L1
aliases: [limit order book, LOB, bid-ask spread, DOM, depth of market, market maker]
related: [concept_liquidity, concept_order_flow, concept_auction_market_theory, concept_optimal_execution_market_impact, concept_trade_execution]
influenced_by: [person_larry_harris, person_maureen_ohara, person_albert_kyle, person_jean_philippe_bouchaud]
status: synthesized
---

# Market Microstructure

**How orders become prices.** Every chart pattern is the visible residue of
order-book events.

## The limit order book

- **Limit orders** rest in the book and *provide* liquidity (bid below,
  ask above).
- **Market orders** *consume* liquidity. They cross the spread and execute
  against resting orders.
- **Price moves** only when aggressive orders exhaust the resting liquidity
  at a level, or when liquidity providers pull or reprice their quotes.
- **Spread** = ask − bid. It is the cost of immediacy. It widens in fast
  markets and around news ([[concept_news_trading]]).
- **Stop orders** are dormant market orders. A cluster of stops is a pool of
  latent aggressive flow that can be triggered ([[concept_liquidity]],
  [[concept_liquidity_sweep_reversal]]).

## Canonical models

| Model | Insight |
|---|---|
| **Kyle (1985)** | Informed traders hide in noise flow; price impact λ ∝ σ_value/σ_noise |
| **Glosten-Milgrom (1985)** | Spread compensates market makers for adverse selection by informed traders |
| **Roll (1984)** | Effective spread can be estimated from negative serial covariance of price changes |
| **Square-root impact law** (Bouchaud et al.) | Impact of a metaorder ≈ `Y·σ·√(Q/V)`, roughly independent of market (see [[concept_optimal_execution_market_impact]]) |

## Market-specific notes

- **Spot FX** is decentralized (OTC). There is no consolidated volume, so
  futures volume (6E, 6B…) or tick volume is used as a proxy. BabyPips teaches
  this structure in its early courses.
- **Futures (ES, NQ, CL, GC)** run on a central limit order book with real
  volume and transparent DOM. This is why order-flow and auction traders
  (Fabio Valentini, Yush, Forrest Knight) focus on futures.
- **Equities** are fragmented across many venues. NBBO, dark pools, and
  payment for order flow change the picture (Harris, *Trading and Exchanges*).


<!-- ===== FILE: trading-intelligence/07_concepts/market-regimes.md ===== -->

---
id: concept_market_regimes
type: concept
title: Market Regimes (trend vs range, high vs low volatility)
partition: 07_concepts
layer: L2
aliases: [regime, trending market, ranging market, balance, imbalance, volatility regime, risk-on risk-off]
related: [concept_auction_market_theory, concept_volatility, concept_trend_following, concept_mean_reversion, concept_time_series_statistics, concept_fundamental_macro_analysis]
status: synthesized
---

# Market Regimes

**The most important filter in trading: what *kind* of market is this?** The
same setup has opposite expectancy in different regimes.

## A 2×2 that covers most of it

| | **Low volatility** | **High volatility** |
|---|---|---|
| **Trending / imbalanced** | Grind: pullback entries, trailing stops ([[concept_trend_following]]) | Expansion: breakouts, momentum, wide stops ([[concept_breakout_trading]]) |
| **Ranging / balanced** | Rotation: fade edges to POC/VWAP ([[concept_mean_reversion]]) | Chop: whipsaw; reduce size or stand aside |

## Detectors

- **AMT.** Balance vs imbalance, value migration, day type
  ([[concept_auction_market_theory]]).
- **Structure.** Clean HH/HL vs overlapping swings ([[concept_market_structure]]).
- **Statistics.** ADX, Hurst exponent, variance ratio, efficiency ratio
  (Kaufman), realized-vol percentile ([[concept_time_series_statistics]]).
- **Moving-average alignment.** Stacked, fanning EMAs mean a trend. Tangled
  EMAs mean range. TG Capital's rule: *if the EMAs are crossing or tangled,
  the setup is invalid* (`strategy_tg_capital_trident`).
- **Macro.** Rate-cycle, liquidity and risk-on/off regimes
  ([[concept_fundamental_macro_analysis]]).

## Practitioner notes

- Clement Ang frames system rules around *when he is allowed to be
  aggressive* and which entry styles suit choppy markets (TraderLion Q&A).
  That is regime gating in plain language.
- Fabio Valentini runs **two models**: trend continuation when the market is
  out of balance, mean reversion when breakouts fail back into balance.


<!-- ===== FILE: trading-intelligence/07_concepts/market-sentiment.md ===== -->

---
id: concept_market_sentiment
type: concept
title: Market Sentiment & Positioning (COT, contrarian signals)
partition: 07_concepts
layer: L3
aliases: [sentiment, COT report, commitments of traders, put call ratio, positioning, contrarian, crowd psychology]
related: [concept_fundamental_macro_analysis, concept_reflexivity, concept_options_greeks, concept_trading_psychology]
influenced_by: [person_humphrey_neill, person_charles_mackay]
status: synthesized
---

# Market Sentiment & Positioning

BabyPips Sophomore covers market sentiment and the **Commitments of Traders
(COT)** report.

## Gauges

- **CFTC COT** (weekly): commercials (hedgers), large speculators, small
  traders. Extreme speculator positioning is a contrarian warning.
- **Retail broker sentiment** (% long/short): retail crowding is commonly
  faded.
- **Options:** put/call ratio, skew, VIX term structure, dealer gamma
  ([[concept_options_greeks]]).
- **Surveys** (AAII, fund manager surveys) and **flows** (ETF in/out).

## Principles

- **Contrarian at extremes, trend-following in between.** Humphrey Neill,
  *The Art of Contrary Thinking* (1954): "When everyone thinks alike,
  everyone is likely to be wrong."
- **Crowds and manias:** Mackay, *Extraordinary Popular Delusions and the
  Madness of Crowds* (1841).
- Positioning creates **fuel**: crowded longs are future sellers. This links
  sentiment to liquidity ([[concept_liquidity]]) and to
  [[concept_reflexivity]].


<!-- ===== FILE: trading-intelligence/07_concepts/market-structure.md ===== -->

---
id: concept_market_structure
type: concept
title: Market Structure (swings, BOS, CHoCH / MSS)
partition: 07_concepts
layer: L2
aliases: [higher highs higher lows, break of structure, BOS, change of character, CHoCH, market structure shift, MSS, swing points]
related: [concept_dow_theory, concept_liquidity, concept_smart_money_concepts, concept_multi_timeframe_analysis, concept_trend_following, concept_price_action]
derived_from: [concept_dow_theory]
status: synthesized
---

# Market Structure

**The skeleton of price.** Swing highs and lows define trend, and the way
they break defines change.

## Vocabulary

| Term | Definition |
|---|---|
| **Uptrend** | Higher highs (HH) and higher lows (HL) |
| **Downtrend** | Lower highs (LH) and lower lows (LL) |
| **Range** | Neither: overlapping swings inside boundaries |
| **BOS (break of structure)** | Price breaks the last swing *in the trend's direction*: continuation |
| **CHoCH / MSS (change of character / market structure shift)** | Price breaks the last swing *against* the trend: first sign of reversal |
| **Displacement** | An impulsive, large-range move that breaks structure, often leaving a [[concept_fair_value_gap]] |
| **Internal vs external structure** | Minor swings inside the major (higher-timeframe) swing range |

## Rules that make structure tradable

1. **Define a swing objectively** (e.g., a fractal: a high with N lower highs
   on each side). Otherwise structure is subjective.
2. **Body close vs wick break.** Many playbooks require a candle-body close
   beyond the swing for a valid BOS. A wick-only break is treated as a
   possible sweep ([[concept_liquidity]]).
3. **Timeframe hierarchy.** A 5-minute CHoCH inside a daily uptrend is
   usually a pullback, not a reversal ([[concept_multi_timeframe_analysis]]).

## Lineage

Dow Theory (c. 1900–1930: trends defined by successive peaks and troughs,
confirmation) → Edwards & Magee → modern price action → SMC/ICT's BOS/CHoCH
labels. The idea is a century old; the vocabulary is new.

## Used by

Trader Mayne's Structure + OTE (HTF break → POI → LTF breaker confirmation),
Candace Lau's sweep reversal (needs a structure shift after the sweep), and
JJ Simon's A+/A/B grading (displacement + BOS).


<!-- ===== FILE: trading-intelligence/07_concepts/mean-reversion.md ===== -->

---
id: concept_mean_reversion
type: concept
title: Mean Reversion
partition: 07_concepts
layer: L4
aliases: [mean reversion, fade, reversion to fair value, POC reversion, VWAP reversion, pairs trading, statistical arbitrage]
related: [concept_auction_market_theory, concept_volume_profile, concept_vwap, concept_bollinger_bands, concept_oscillators_momentum, concept_stochastic_processes, concept_market_regimes]
contrasts_with: [concept_trend_following]
status: synthesized
---

# Mean Reversion

**Price deviates from a reference "fair value" and tends to return.** The
reference can be POC, VWAP, a moving average, a pair spread, or JJ Simon's
NY-open fair price.

## Where it is valid

- **Balanced markets** (AMT), ranges, low-vol regimes ([[concept_market_regimes]]).
- **Short horizons** for indices (overreaction).
- **Cointegrated spreads** (pairs/stat-arb), modelled as Ornstein-Uhlenbeck
  ([[concept_stochastic_processes]]); trade when the z-score is beyond ±2.

## Chart Fanatics implementations

| Trader | Reference | Rule highlight |
|---|---|---|
| Fabio Valentini | POC | When breakout attempts fail and price returns to balance, revert to POC (T2/T3) |
| JJ Simon | NY open / pre-open fair price | Reversion unless fundamentals change; **stop reversion trades after three consecutive losses** (T3) |
| Forrest Knight | Volume-profile edges | Edge-to-edge rotation through LVNs (T3) |

## Return profile & danger

High win rate and **negative skew**: many small wins, occasional large loss
when the regime flips to trend. Hard stops and regime filters are mandatory.
Never average down without a predefined max risk ([[concept_risk_of_ruin_drawdown]]).


<!-- ===== FILE: trading-intelligence/07_concepts/moving-averages.md ===== -->

---
id: concept_moving_averages
type: concept
title: Moving Averages (SMA, EMA, stacks, crossovers)
partition: 07_concepts
layer: L3
aliases: [SMA, EMA, moving average crossover, golden cross, death cross, EMA stack, 200-day moving average, 9 21 EMA]
related: [concept_trend_following, concept_market_regimes, concept_vwap, concept_oscillators_momentum]
influenced_by: [person_richard_donchian, person_gerald_appel]
status: synthesized
---

# Moving Averages

BabyPips Elementary Grade 4. A lagging smoother of price that defines trend
and dynamic support.

| Type | Formula | Note |
|---|---|---|
| SMA(n) | mean of last n closes | Equal weights |
| EMA(n) | `EMA_t = α·P_t + (1−α)·EMA_{t−1}`, `α = 2/(n+1)` | Reacts faster |

## Uses

1. **Trend filter.** Price above the 200-day SMA means long-only. This is a
   classic regime rule, documented to reduce drawdowns in equity indices.
2. **Crossovers.** Fast/slow MA cross (Donchian's era onwards). Simple trend
   following is profitable over long histories in futures, at the cost of
   whipsaw in ranges ([[concept_trend_following]]).
3. **EMA stacks.** Alignment of several EMAs as a trend-quality gate.
   **TG Capital** requires the **5, 9, 13 (or 15), and 21 EMAs stacked**; if
   they are tangled or crossing, *no trade* (`strategy_tg_capital_trident`).
4. **Dynamic support.** The 10/21 EMA in strong growth-stock trends
   (Minervini, Kell), and the 20 EMA in Al Brooks' price action.

## Pitfalls

Lag means late entries and exits. Parameter fishing (finding "the best" MA
length) is a classic overfitting trap ([[concept_overfitting_validation]]).


<!-- ===== FILE: trading-intelligence/07_concepts/multi-timeframe-analysis.md ===== -->

---
id: concept_multi_timeframe_analysis
type: concept
title: Multi-Timeframe Analysis (top-down)
partition: 07_concepts
layer: L2
aliases: [MTF, top-down analysis, HTF, LTF, timeframe alignment, fractal markets]
related: [concept_market_structure, concept_support_resistance, concept_trade_execution, concept_premium_discount_ote]
influenced_by: [person_alexander_elder]
status: synthesized
---

# Multi-Timeframe Analysis

**Higher timeframe (HTF) for bias and location; lower timeframe (LTF) for the
trigger and risk.** BabyPips covers this in High School.

## A standard three-tier stack

| Tier | Ratio | Job | Example (day trade NQ) |
|---|---|---|---|
| **Bias** | ×4–6 above the setup TF | Trend direction, key levels, draw on liquidity | Daily / 4H |
| **Setup** | — | Pattern, zone, POI | 15m / 1H |
| **Trigger** | ÷4–6 below | Entry, tight stop | 1m / 5m |

Elder's **Triple Screen** (1986) formalised this. Trade in the direction of
the long-term tide and enter on short-term waves against it.

## Why it works mechanically

- Larger timeframes aggregate more participants and capital. Their levels
  hold more resting liquidity.
- An LTF trigger gives a **smaller stop at the same HTF location**, so the
  R:R multiplies ([[concept_risk_reward_r_multiples]]). This is how
  "1:20 RR" claims arise: a 30m/5m trigger aimed at a daily target.

## In Chart Fanatics playbooks

TG Capital (daily bias and targets, 30m entries), Trader Mayne (HTF structure
break, then LTF breaker confirmation), Candace Lau (HTF context, LTF
execution).

## Pitfall

Too many timeframes produce conflicting signals and paralysis. Fix the
stack in the trading plan ([[concept_trading_plan]]).


<!-- ===== FILE: trading-intelligence/07_concepts/news-trading.md ===== -->

---
id: concept_news_trading
type: concept
title: News & Event Trading
partition: 07_concepts
layer: L3
aliases: [news trading, economic calendar, NFP, CPI, FOMC, earnings, event risk, slippage]
related: [concept_fundamental_macro_analysis, concept_volatility, concept_episodic_pivot, concept_trade_execution, concept_market_microstructure]
status: synthesized
---

# News & Event Trading

BabyPips Sophomore covers trading the news.

## Two approaches

1. **Directional:** trade the *surprise* (actual − consensus) and the
   subsequent repricing. Requires speed, or a post-release structure setup.
2. **Non-directional / volatility:** straddle-like breakouts of the
   pre-release range, or options volatility trades.

## Microstructure reality

- **Spreads widen and liquidity vanishes** seconds before and after major
  releases. Stops slip, sometimes by many pips/points
  ([[concept_market_microstructure]]).
- Prop-firm guidance often restricts trading around high-impact news because
  of these hidden costs.

## In this knowledge base

- **Tanja Trades' AMD model** targets clean moves *during* major news events
  (T3).
- **JJ Simon's fair pricing theory:** news releases **reset** the fair price
  and start continuation trades (T3).
- **Episodic pivots** (Pradeep Bonde) are *equity* news events: earnings or
  catalysts that reprice a neglected stock ([[concept_episodic_pivot]]).


<!-- ===== FILE: trading-intelligence/07_concepts/optimal-execution-market-impact.md ===== -->

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


<!-- ===== FILE: trading-intelligence/07_concepts/options-greeks.md ===== -->

---
id: concept_options_greeks
type: concept
title: Options & the Greeks
partition: 07_concepts
layer: L0
aliases: [delta, gamma, theta, vega, Black-Scholes, gamma exposure, GEX]
related: [concept_volatility, concept_stochastic_processes, concept_probability_fat_tails, concept_market_sentiment]
influenced_by: [person_fischer_black, person_sheldon_natenberg, person_nassim_taleb]
status: synthesized
---

# Options & the Greeks

**Black-Scholes-Merton (1973)** prices a European option by constructing a
riskless hedge of option and stock. The price depends on volatility, not on
expected return.

`C = S·N(d₁) − K·e^{−rT}·N(d₂)`, with `d₁ = [ln(S/K) + (r + σ²/2)T] / (σ√T)` and `d₂ = d₁ − σ√T`.

| Greek | Sensitivity to | Trader meaning |
|---|---|---|
| **Delta (Δ)** | underlying price | Directional exposure; roughly the probability of finishing in the money |
| **Gamma (Γ)** | change in delta | Convexity. Long gamma gains from movement, short gamma loses. |
| **Theta (Θ)** | time | Daily decay. The price of holding gamma. |
| **Vega (ν)** | implied vol | Exposure to the vol level |
| **Rho (ρ)** | rates | Mostly minor, except for long-dated options |

**Core identity:** for a delta-hedged option, P&L ≈ ½Γ·S²·(σ²_realized − σ²_implied)·dt.
You profit from options when realized vol beats the implied vol you paid.

## Why non-options traders care

- **Dealer gamma positioning** (GEX) changes intraday behaviour. When dealers
  are long gamma they dampen moves, which helps mean reversion. When they are
  short gamma they amplify moves, which helps breakouts. This links to
  [[concept_market_regimes]].
- **Options flow** is a sentiment and positioning input
  ([[concept_market_sentiment]]). Chart Fanatics features options-flow traders
  (see `strategy_brando_options_swing`).
- **Short-vol payoffs** resemble high-win-rate strategies: small frequent
  gains and rare huge losses ([[concept_probability_fat_tails]]).

References: Natenberg, *Option Volatility & Pricing*; Hull, *Options, Futures,
and Other Derivatives*; Taleb, *Dynamic Hedging*.


<!-- ===== FILE: trading-intelligence/07_concepts/order-blocks-breakers.md ===== -->

---
id: concept_order_blocks_breakers
type: concept
title: Order Blocks, Breaker Blocks & Mitigation
partition: 07_concepts
layer: L3
aliases: [order block, OB, breaker, breaker block, mitigation block, supply and demand zone, point of interest, POI]
related: [concept_smart_money_concepts, concept_fair_value_gap, concept_support_resistance, concept_market_structure, concept_liquidity]
derived_from: [concept_support_resistance, concept_wyckoff_method]
influenced_by: [person_michael_huddleston]
sources:
  - {title: "TradeZella — Structure + OTE (Trader Mayne)", url: "https://www.tradezella.com/strategies/structure-ote", tier: T3}
status: synthesized
---

# Order Blocks & Breakers

## Order block (OB)

The **last opposing candle before a displacement that breaks structure**. A
bullish OB is the last down-close candle before a strong up-move that
creates a BOS. The theory: unfilled institutional orders remain there, so
price reacts on return. Classic "supply/demand zone" traders describe the
same base. The ICT label is newer than the idea.

## Breaker block

A **failed order block**. Price sweeps liquidity, then breaks back through
the OB that should have held. The failed bullish OB becomes a **bearish
breaker** (and vice versa). The sequence *sweep → failure → structure
reclaim* is the breaker setup Trader Mayne uses as his lower-timeframe
confirmation.

## Mitigation block

Like a breaker, but without the liquidity sweep (a failure swing that does
not make a new extreme).

## Trader Mayne's Structure + OTE (T3 summary)

1. HTF (daily/weekly) **clean structure break**.
2. Mark the **POI that caused it**: an order block or breaker.
3. Wait for price to return to the POI (ideally in the
   [[concept_premium_discount_ote]] zone).
4. LTF confirmation: a **breaker**, i.e., a failed move that sweeps
   liquidity and reclaims structure.
5. Stop beyond the sweep. Target the HTF liquidity.

## Caveat

Breaker and OB zones work best as **confluence** (with FVG, structure, and
liquidity), not as standalone triggers. Several indicator authors explicitly
warn against using breakers alone.


<!-- ===== FILE: trading-intelligence/07_concepts/order-flow.md ===== -->

---
id: concept_order_flow
type: concept
title: Order Flow (footprint, delta, CVD, absorption, trapped traders)
partition: 07_concepts
layer: L1
aliases: [footprint chart, cumulative volume delta, CVD, delta, absorption, tape reading, DOM, bookmap, imbalance]
related: [concept_market_microstructure, concept_auction_market_theory, concept_volume_profile, concept_liquidity, concept_scalping, concept_trade_execution]
derived_from: [concept_market_microstructure]
influenced_by: [person_richard_wyckoff, person_humphrey_neill, person_peter_steidlmayer]
sources:
  - {title: "TradeZella — Order Flow Strategy (Trader Yush)", url: "https://www.tradezella.com/strategies/order-flow-strategy", tier: T3}
  - {title: "Chart Fanatics — Yush's Strategy: Trading Trapped Buyers & Sellers with Order Flow", url: "https://www.chartfanatics.com/strategies/order-flow-strategy", tier: T2}
  - {title: "Bookmap — key order flow strategies", url: "https://bookmap.com/en/blog/key-order-flow-strategies-breakouts-trends-trapped-traders-and-stop-runs", tier: T3}
status: synthesized
---

# Order Flow

**Order flow = reading who is aggressive, and whether they are succeeding.**
It is the modern, instrumented descendant of tape reading (Wyckoff's
*Studies in Tape Reading*, 1910; Neill's *Tape Reading and Market Tactics*,
1931).

## Instruments

| Tool | What it shows |
|---|---|
| **Time & sales (tape)** | Every print: price, size, aggressor side |
| **DOM / heatmap (e.g., Bookmap)** | Resting limit liquidity, pulls and stacks |
| **Footprint chart** | Bid vs ask volume traded *at each price inside each bar* |
| **Delta** | Ask-volume minus bid-volume per bar (net aggression) |
| **Cumulative volume delta (CVD)** | Running sum of delta. Divergence from price signals weakening aggression. |
| **Imbalances** | Diagonal bid/ask ratios above a threshold (e.g., 300%) |

## Core reads

1. **Absorption.** Heavy aggressive selling into a level while price does
   *not* fall means passive buyers are absorbing. That signals a potential
   reversal or support.
2. **Exhaustion.** Aggression dries up at the extreme of a move.
3. **Initiative vs responsive** activity (AMT language,
   [[concept_auction_market_theory]]).
4. **Trapped traders.** Aggressive buyers late into a move, followed by a
   failure to continue. Their stop-outs then fuel the reversal. This is the
   order-flow description of a [[concept_liquidity_sweep_reversal]].
5. **Large-lot detection.** Yush's framework flags prints of roughly 75+ lots
   on NQ and 200+ on ES, and needs **at least 2 confirmations** (absorption,
   delta, trapped traders) at a pre-marked zone (T3 source).

## Why futures

Order flow requires real, centralized volume. That is why it is applied to
CME futures (NQ, ES, CL, GC) and rarely to spot FX
([[concept_market_microstructure]]).

## Chart Fanatics usage

Fabio Valentini (volume profile + footprint + CVD inside AMT) and Trader Yush
(absorption and trapped traders) are the channel's main order-flow voices.
Fabio co-founded the order-flow platform Deep Charts.


<!-- ===== FILE: trading-intelligence/07_concepts/oscillators-momentum.md ===== -->

---
id: concept_oscillators_momentum
type: concept
title: Oscillators & Momentum Indicators (RSI, MACD, Stochastic, ADX)
partition: 07_concepts
layer: L3
aliases: [RSI, relative strength index, MACD, stochastic, ADX, parabolic SAR, momentum indicators, leading indicators, lagging indicators]
related: [concept_divergence, concept_moving_averages, concept_market_regimes, concept_mean_reversion]
influenced_by: [person_welles_wilder, person_gerald_appel, person_george_lane]
status: synthesized
---

# Oscillators & Momentum Indicators

BabyPips Elementary Grade 5 and Middle School Grade 6 (leading vs lagging,
using MACD to confirm trend).

| Indicator | Creator | Formula idea | Primary use |
|---|---|---|---|
| **RSI(14)** | J. Welles Wilder (1978) | 100 − 100/(1+RS), RS = avg gain/avg loss | Overbought/oversold in ranges; momentum regime (40–80 bull range) |
| **MACD (12,26,9)** | Gerald Appel (late 1970s) | EMA12 − EMA26; signal = EMA9 | Trend momentum, crossovers, divergence |
| **Stochastic** | George Lane (1950s) | Close position within N-period range | Range turns |
| **ADX** | Wilder (1978) | Directional movement strength | Trend vs range filter ([[concept_market_regimes]]) |
| **Parabolic SAR / ATR** | Wilder (1978) | — | Trailing stops, volatility ([[concept_volatility]]) |

## Rules

- **Oscillators are regime-dependent.** "Overbought" in a strong trend stays
  overbought. Use them in ranges or as momentum confirmation, never as
  standalone reversal calls.
- **Leading vs lagging.** Oscillators "lead" but give false signals. Trend
  indicators "lag" but confirm.
- Most elite discretionary traders in this knowledge base (Chart Fanatics
  futures guests, Tori Trades) use few or no oscillators. Order flow, levels,
  and structure carry the information.


<!-- ===== FILE: trading-intelligence/07_concepts/overfitting-validation.md ===== -->

---
id: concept_overfitting_validation
type: concept
title: Overfitting & Edge Validation (multiple testing, deflated Sharpe)
partition: 07_concepts
layer: L8
aliases: [overfitting, curve fitting, data snooping, multiple testing, deflated Sharpe ratio, probability of backtest overfitting, PBO, walk-forward, out-of-sample]
related: [concept_backtesting, concept_machine_learning_finance, concept_performance_metrics, concept_random_walk_efficient_markets, concept_edge]
influenced_by: [person_marcos_lopez_de_prado, person_david_aronson]
status: synthesized
---

# Overfitting & Edge Validation

**If you test enough variations, something will look great by chance.**

## The core problem

With N independent strategy trials of zero true skill, the **expected maximum
Sharpe ratio** grows roughly as `√(2·ln N)`. After testing 100 variants, a
Sharpe ≈ 3 (annualised over a short sample) can be pure noise.

## Defences

| Technique | Idea |
|---|---|
| **Hypothesis first** | An economic or microstructural reason for the edge ([[concept_edge]]) |
| **Out-of-sample holdout** | Never touched during design |
| **Walk-forward** | Re-optimise on rolling windows; evaluate only the forward segments |
| **Parameter robustness** | Performance should form a plateau, not a spike, across parameter values |
| **Deflated Sharpe ratio** (Bailey & López de Prado) | Adjust the Sharpe for the number of trials, skew, and kurtosis |
| **PBO / CSCV** | Combinatorially symmetric cross-validation estimates the probability that the in-sample best underperforms out-of-sample |
| **White's Reality Check / SPA** | Data-snooping-robust tests (used in Aronson's *Evidence-Based Technical Analysis*) |
| **Live forward test at small size** | The final arbiter |

## Applied to YouTube strategies

A strategy presented in a video is the **survivor of an invisible selection
process** (of traders, of strategies, of chart examples). Treat every claim
as T4 until you have run your own out-of-sample test
([[concept_backtesting]]).


<!-- ===== FILE: trading-intelligence/07_concepts/performance-metrics.md ===== -->

---
id: concept_performance_metrics
type: concept
title: Performance Metrics (Sharpe, Sortino, MAR, profit factor)
partition: 07_concepts
layer: L8
aliases: [Sharpe ratio, Sortino ratio, Calmar, MAR, profit factor, win rate, average R, ulcer index, CAGR]
related: [concept_expectancy, concept_overfitting_validation, concept_risk_of_ruin_drawdown, concept_trading_journal_review]
influenced_by: [person_william_sharpe]
status: synthesized
---

# Performance Metrics

| Metric | Formula | Read |
|---|---|---|
| **CAGR** | `(End/Start)^(1/years) − 1` | Growth |
| **Sharpe** | `(R − R_f)/σ` (annualise: × √periods) | Return per unit of total vol; assumes roughly normal returns |
| **Sortino** | `(R − R_f)/σ_downside` | Penalises only downside vol |
| **Max drawdown** | Largest peak-to-trough decline | Pain / survivability |
| **MAR / Calmar** | CAGR / MaxDD | Classic CTA metric |
| **Profit factor** | Gross profit / gross loss | >1.5 is solid for discretionary trading |
| **Expectancy (R)** | `p·W̄ − q·L̄` | Edge per trade ([[concept_expectancy]]) |
| **SQN** | `√N·mean(R)/sd(R)` | Edge consistency |
| **Skew & kurtosis** | 3rd and 4th moments | Hidden tail risk ([[concept_probability_fat_tails]]) |

## Interpretation rules

- A **Sharpe > 3** on a short sample is more likely luck, error, or hidden
  tail risk than genius ([[concept_overfitting_validation]]).
- Compare strategies on **the same risk** (vol-normalised).
- Negative skew plus a high Sharpe is the signature of short-vol and
  martingale-like systems.


<!-- ===== FILE: trading-intelligence/07_concepts/pivot-points.md ===== -->

---
id: concept_pivot_points
type: concept
title: Pivot Points
partition: 07_concepts
layer: L3
aliases: [floor pivots, standard pivots, camarilla, woodie, R1 S1, daily pivot]
related: [concept_support_resistance, concept_trading_sessions_killzones, concept_mean_reversion, concept_breakout_trading]
status: synthesized
---

# Pivot Points

BabyPips Middle School Grade 8: computing pivot points and using them for
**range trading** and **breakouts**.

## Standard (floor) pivots from the prior period's H, L, C

```
P  = (H + L + C) / 3
R1 = 2P − L        S1 = 2P − H
R2 = P + (H − L)   S2 = P − (H − L)
R3 = H + 2(P − L)  S3 = L − 2(H − P)
```

Variants: Woodie, Camarilla, Fibonacci pivots.

## Use

- **Range days:** fade R1/S1 back toward P.
- **Trend days:** a break-and-hold beyond R1/S1 targets R2/S2.
- They work largely because floor traders and algorithms watch the same
  prior-day H/L/C references, which are themselves liquidity levels
  ([[concept_liquidity]]).


<!-- ===== FILE: trading-intelligence/07_concepts/position-sizing.md ===== -->

---
id: concept_position_sizing
type: concept
title: Position Sizing
partition: 07_concepts
layer: L6
aliases: [position sizing, fixed fractional, percent risk, volatility targeting, turtle unit, money management, risk per trade]
related: [concept_kelly_criterion_optimal_f, concept_risk_of_ruin_drawdown, concept_expectancy, concept_volatility, concept_leverage_margin, concept_correlation_portfolio_risk, concept_prop_firm_risk_rules]
influenced_by: [person_van_tharp, person_ralph_vince, person_ed_thorp, person_richard_dennis]
status: synthesized
---

# Position Sizing

**"Position sizing is the part of your system that tells you how much."**
(Van Tharp). It determines whether an edge compounds or ruins you. BabyPips
Senior covers it.

## Models

| Model | Rule | Notes |
|---|---|---|
| **Fixed fractional (% risk)** | `size = equity × f / (stop distance × point value)` | Industry default; f = 0.25–1% for discretionary traders, ~0.5–2% for systematic |
| **Volatility unit (Turtle)** | `units = (equity × 1%) / (N × $ per point)` | Equalises risk across markets ([[concept_volatility]]) |
| **Volatility targeting** | Scale exposure so portfolio vol ≈ target (e.g., 10–20% annual) | Carver, CTAs |
| **Kelly / fractional Kelly** | `f* = p − q/b` (binary bets) | Growth-optimal; use ¼–½ Kelly ([[concept_kelly_criterion_optimal_f]]) |
| **Optimal f (Vince)** | Maximise TWR from the trade list | Aggressive; huge drawdowns |
| **Meta-labeled sizing** | Size ∝ ML-estimated probability of success | ([[concept_machine_learning_finance]]) |

## Rules worth tattooing

1. **Risk is set by stop × size, never by leverage** ([[concept_leverage_margin]]).
2. **Size down in drawdowns and in unfamiliar regimes;** size up only with
   evidence.
3. **Account for correlation:** five correlated positions at 1% each are one
   5% bet ([[concept_correlation_portfolio_risk]]).
4. **Per-trade, per-idea, per-day risk budgets with circuit breakers**
   (BabyPips Senior; prop-firm practice) ([[concept_prop_firm_risk_rules]]).

## In this knowledge base

Fabio Valentini ~0.25% per trade (T3). The Turtles' 1% per N unit. Gianluca
Bruni (Chart Fanatics guest, announced) on building statistical models around
a strategy.


<!-- ===== FILE: trading-intelligence/07_concepts/premium-discount-ote.md ===== -->

---
id: concept_premium_discount_ote
type: concept
title: Premium / Discount & Optimal Trade Entry (OTE)
partition: 07_concepts
layer: L3
aliases: [premium, discount, equilibrium, OTE, optimal trade entry, 62% 70.5% 79% retracement]
related: [concept_fibonacci, concept_smart_money_concepts, concept_order_blocks_breakers, concept_multi_timeframe_analysis, concept_mean_reversion]
derived_from: [concept_fibonacci]
influenced_by: [person_michael_huddleston]
status: synthesized
---

# Premium / Discount & OTE

**Premium/discount.** Take a dealing range (swing low → swing high). Above
50% (*equilibrium*) is **premium**; below is **discount**. Buy in discount,
sell in premium, within the HTF bias. This is value investing logic applied to
a swing.

**OTE (Optimal Trade Entry).** ICT's name for a pullback into the **62%–79%**
retracement band of the impulse leg (sweet spot ≈ 70.5%). It sits inside
discount for longs and premium for shorts.

## Why it can work

- It forces **location discipline**: no chasing after displacement.
- A deep retracement gives a **small stop relative to the target** (the
  impulse extreme and beyond), so it improves R:R
  ([[concept_risk_reward_r_multiples]]).

## Lineage

Fibonacci retracement practice (38.2/50/61.8%), popularised in trading by
Elliott-wave practitioners from the 1930s onward ([[concept_fibonacci]]) →
ICT's OTE band → Trader Mayne's **Structure + OTE** playbook and the
Tradezella "PO3 + OTE + ADR" playbook.

## Caveat

Fibonacci levels have weak standalone statistical support. Treat OTE as a
*location filter* that improves R:R, not as a predictive level.


<!-- ===== FILE: trading-intelligence/07_concepts/price-action.md ===== -->

---
id: concept_price_action
type: concept
title: Price Action Trading (naked charts)
partition: 07_concepts
layer: L3
aliases: [price action, naked trading, bar by bar, pin bar, inside bar, engulfing, two-legged pullback]
related: [concept_candlestick_patterns, concept_market_structure, concept_support_resistance, concept_trendlines, concept_chart_patterns, concept_smart_money_concepts]
influenced_by: [person_al_brooks, person_steve_nison]
status: synthesized
---

# Price Action Trading

**Trading the bars themselves**, with few or no indicators. Structure,
levels, candle behaviour and context carry the information. BabyPips
dedicates a High School grade to it.

## Families

| School | Key ideas |
|---|---|
| **Al Brooks** (*Reading Price Charts Bar by Bar*, Trends/Ranges/Reversals trilogy) | Every bar is a trend or trading-range bar. Signal bars, entry bars, two-legged pullbacks (H2/L2), "always in" direction. Most breakouts fail in ranges and most reversals fail in trends. |
| **Candlestick price action** (Nison) | Pin bars, engulfing bars, inside bars, read at levels |
| **Supply/demand & SMC** | Zones, liquidity, displacement ([[concept_smart_money_concepts]]) |
| **Wyckoff / VSA** | Bars plus volume, effort vs result |

## Universal rules

1. **Location before pattern.** A pin bar in the middle of a range means
   nothing; at HTF support after a sweep it means a lot.
2. **Context decides.** The trend or range state comes first
   ([[concept_market_regimes]]).
3. **Trigger ≠ signal.** Wait for the bar to close, then enter on a break of
   the signal bar (Forrest Knight's "wait for the signal candle to close").

Tori Trades' no-indicator 4H trendline approach and Marci Silfrain's
measured-move method are price-action strategies at heart.


<!-- ===== FILE: trading-intelligence/07_concepts/probabilistic-thinking.md ===== -->

---
id: concept_probabilistic_thinking
type: concept
title: Probabilistic Thinking (thinking in bets)
partition: 07_concepts
layer: L7
aliases: [thinking in probabilities, five fundamental truths, thinking in bets, process over outcome, resulting]
related: [concept_trading_psychology, concept_expectancy, concept_edge, concept_probability_fat_tails, concept_reflexivity]
influenced_by: [person_mark_douglas, person_annie_duke, person_ed_thorp]
status: synthesized
---

# Probabilistic Thinking

**Mark Douglas's five fundamental truths** (*Trading in the Zone*, 2000):

1. Anything can happen.
2. You don't need to know what is going to happen next to make money.
3. There is a random distribution between wins and losses for any given set
   of variables that define an edge.
4. An edge is nothing more than an indication of a higher probability of one
   thing happening over another.
5. Every moment in the market is unique.

## Consequences

- **A single trade's outcome is not feedback on the decision.** Judge the
  process. Annie Duke calls the error **"resulting"** (*Thinking in Bets*).
- Execute every valid setup. Skipping trades after losses destroys the
  sample the edge depends on ([[concept_expectancy]]).
- Express views as **probabilities with sizes**, not certainties. This is
  Thorp's casino mindset and Soros's fallibilism ([[concept_reflexivity]]).

## Bridge to mathematics

Bayesian updating of your edge estimate ([[concept_probability_fat_tails]])
is the formal version of "the market can prove me wrong". Your win-rate
estimate after 30 trades has a wide confidence interval. Respect it.


<!-- ===== FILE: trading-intelligence/07_concepts/probability-fat-tails.md ===== -->

---
id: concept_probability_fat_tails
type: concept
title: Probability, Distributions & Fat Tails
partition: 07_concepts
layer: L0
aliases: [fat tails, kurtosis, black swans, power laws]
related: [concept_random_walk_efficient_markets, concept_volatility, concept_risk_of_ruin_drawdown, concept_kelly_criterion_optimal_f, concept_edge]
influenced_by: [person_benoit_mandelbrot, person_nassim_taleb, person_et_jaynes]
covers: []
status: synthesized
---

# Probability, Distributions & Fat Tails

**Core idea.** Returns are *not* normally distributed. They have fat tails
(excess kurtosis), volatility clustering, and skew. Extreme moves happen orders
of magnitude more often than a Gaussian model predicts.

## Key facts every trader should hold

- **Daily equity-index returns** routinely show 5–10σ days that a normal
  distribution would place once in thousands of years. October 1987 was
  roughly a −20σ day under a Gaussian model.
- **Power laws.** Mandelbrot (1963, cotton prices) showed price changes follow
  stable Paretian or power-law tails. The variance may be unstable or, in the
  extreme, undefined.
- **Sample statistics lie in fat-tailed worlds.** The sample mean and
  variance converge slowly. A strategy's historical Sharpe ratio can be
  dominated by a few observations (Taleb, *Statistical Consequences of Fat
  Tails*).
- **Bayesian updating** (Jaynes) is the right frame for edge estimation.
  Your win rate is a posterior belief, not a constant.

## Trading implications

| Implication | Where it lands |
|---|---|
| Size for the tail, not the average | [[concept_position_sizing]], [[concept_risk_of_ruin_drawdown]] |
| Short-volatility and high-win-rate strategies hide tail risk ("picking up pennies in front of a steamroller") | [[concept_options_greeks]], [[concept_scalping]] |
| Stops do not guarantee max loss (gaps, limit moves) | [[concept_trade_management]] |
| Use full Kelly only with a known distribution; use fractional Kelly in practice | [[concept_kelly_criterion_optimal_f]] |

## Lineage

Bachelier (1900, Gaussian random walk) → Mandelbrot (1963, fat tails) →
Fama (1965, documents leptokurtosis) → Taleb (2001–2020, operational
consequences). See [[concept_random_walk_efficient_markets]].


<!-- ===== FILE: trading-intelligence/07_concepts/prop-firm-risk-rules.md ===== -->

---
id: concept_prop_firm_risk_rules
type: concept
title: Prop-Firm Evaluations & Risk Rules
partition: 07_concepts
layer: L6
aliases: [prop firm, funded account, evaluation, challenge, trailing drawdown, daily loss limit, consistency rule, payouts]
related: [concept_risk_of_ruin_drawdown, concept_position_sizing, concept_scalping, concept_trading_psychology]
sources:
  - {title: "BabyPips — Risk Management: How to Increase Your Odds of Passing Prop Firm Challenges", url: "https://www.babypips.com/learn/forex/prop-firm-risk-management", tier: T2}
status: synthesized
---

# Prop-Firm Evaluations & Risk Rules

Most Chart Fanatics guests are futures prop-firm traders, and payout totals
are a common credential (e.g., JJ Simon's claims of $1.2M–$1.8M in payouts;
the numbers vary by source, so they are T4).

## Typical rules

| Rule | Effect on strategy |
|---|---|
| **Max (trailing) drawdown** | Path-dependence: early losses can end the account. Favours small risk early. |
| **Daily loss limit** | Caps tail days; forces a stop-trading rule |
| **Profit target** | Encourages over-aggression near deadlines |
| **Consistency rule** | No single day can exceed X% of profits |
| **News restrictions** | No trading around high-impact releases ([[concept_news_trading]]) |

## Sizing math for evaluations

Treat the drawdown limit as the **bankroll**. With a $2,500 trailing limit,
risking $250/trade (10% of the buffer) gives a material chance of failure
after a normal losing streak ([[concept_risk_of_ruin_drawdown]]). BabyPips'
prop guidance: apply `(Account × Risk%) ÷ Stop` consistently, budget risk per
trade, per idea, and per day, and stop after a set number of daily losses.

## Caveat

Evaluation success ≠ live edge. Several sources note prop-optimised
strategies behave differently on live accounts (fills, size, psychology).
Umar Ashraf's framework warns: *"The goal is NOT to make money"* early on;
it is to collect data and build process.


<!-- ===== FILE: trading-intelligence/07_concepts/random-walk-efficient-markets.md ===== -->

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


<!-- ===== FILE: trading-intelligence/07_concepts/reflexivity.md ===== -->

---
id: concept_reflexivity
type: concept
title: Reflexivity (Soros)
partition: 07_concepts
layer: L3
aliases: [reflexivity, boom bust, feedback loop, self-reinforcing trends]
related: [concept_market_sentiment, concept_fundamental_macro_analysis, concept_trend_following, concept_probabilistic_thinking]
influenced_by: [person_george_soros, person_karl_popper]
status: synthesized
---

# Reflexivity

George Soros, *The Alchemy of Finance* (1987), building on Karl Popper's
fallibilism.

**Thesis.** Market participants' biased perceptions *change the
fundamentals* they are trying to price, and those changed fundamentals feed
back into perceptions. Prices do not passively reflect reality; they help
create it.

## Boom-bust sequence

1. An unrecognised trend begins.
2. A prevailing bias forms and reinforces the trend (self-reinforcing).
3. The trend is tested, survives, and conviction grows.
4. A **gap** opens between perception and reality.
5. A moment of truth; the trend becomes unsustainable.
6. Reversal and a self-reinforcing collapse.

## Why traders care

- It explains why **trends overshoot** any "fair value"
  ([[concept_trend_following]]).
- It justifies **concentration at inflection points**. Soros and
  Druckenmiller on sterling in 1992: when conviction is high, go for the
  jugular. Druckenmiller recounted that Soros pushed the position from 100%
  to 200% exposure.
- **Fallibilism as risk management:** assume your thesis is flawed, and look
  for the flaw ([[concept_probabilistic_thinking]]).


<!-- ===== FILE: trading-intelligence/07_concepts/risk-of-ruin-drawdown.md ===== -->

---
id: concept_risk_of_ruin_drawdown
type: concept
title: Risk of Ruin & Drawdown Math
partition: 07_concepts
layer: L6
aliases: [risk of ruin, drawdown, max drawdown, recovery math, losing streak, gambler's ruin]
related: [concept_position_sizing, concept_kelly_criterion_optimal_f, concept_probability_fat_tails, concept_prop_firm_risk_rules, concept_trading_psychology]
status: synthesized
---

# Risk of Ruin & Drawdown Math

## Recovery asymmetry

`gain needed to recover = 1/(1 − DD) − 1`

| Drawdown | Gain needed |
|---|---|
| 10% | 11.1% |
| 20% | 25% |
| 30% | 42.9% |
| 50% | 100% |
| 75% | 300% |

## Losing streaks are normal

The probability of at least one run of `k` consecutive losses in `N` trades
is high, even with good systems. At a 40% win rate, a streak of 10+ losses
within 500 trades is likely. Marci Silfrain's advice: **plan to lose on every
trade, and plan to lose the next 20 in a row.**

With fixed fractional risk `f`, a streak of `k` losses costs
`1 − (1 − f)^k`: at 1% × 20 losses ≈ 18%, and at 5% × 20 losses ≈ 64%.

## Risk of ruin (gambler's ruin, simplified)

For a per-trade edge with win probability `p > 0.5` at even odds, and capital
of `U` betting units: `RoR ≈ ((1 − p)/p)^U`. Smaller bets (more units) mean
exponentially lower ruin. That is the formal reason for small fractional
risk. In practice, estimate ruin probability by **Monte Carlo resampling of
your R-multiple distribution** ([[concept_backtesting]]).

## Practical guardrails

- Max daily loss (e.g., 2–3R), weekly loss limit, and hard stop on an equity
  drawdown → reduce size by half ([[concept_prop_firm_risk_rules]]).
- JJ Simon: **stop reversion trades after three consecutive losses** (T3).


<!-- ===== FILE: trading-intelligence/07_concepts/risk-reward-r-multiples.md ===== -->

---
id: concept_risk_reward_r_multiples
type: concept
title: Risk:Reward & R-Multiples
partition: 07_concepts
layer: L6
aliases: [risk reward, R multiple, RR, 1R, reward to risk, breakeven win rate]
related: [concept_expectancy, concept_position_sizing, concept_trade_management, concept_multi_timeframe_analysis]
influenced_by: [person_van_tharp]
status: synthesized
---

# Risk:Reward & R-Multiples

**1R = the amount you risk on a trade** (entry to stop × size). Every outcome
is expressed as a multiple of R (Van Tharp).

## Breakeven win rate

`p_breakeven = 1 / (1 + RR)`

| R:R | Breakeven win rate |
|---|---|
| 1:1 | 50% |
| 1:1.5 | 40% |
| 1:2 | 33.3% |
| 1:3 | 25% |
| 1:5 | 16.7% |
| 1:20 | 4.8% |

## Sanity check on marketing claims

A video titled "90% win rate … (1:20+ RR)" (TG Capital on Chart Fanatics)
implies an expectancy of `0.9×20 − 0.1×1 = +17.9R per trade`. That is
implausible for any real strategy. An independent EA reconstruction tested
on EURUSD M30 found a **~20% win rate** with large winners, still profitable
out-of-sample for 2023–24 (T3, single self-published backtest). **The
strategy may be real; the headline is not** ([[concept_expectancy]]).

## Planned vs realised R

Planned R:R is a hypothesis. Realised R depends on how often the target is
reached before the stop. Track MAE/MFE (max adverse/favourable excursion) in
the journal to tune stops and targets ([[concept_trading_journal_review]]).


<!-- ===== FILE: trading-intelligence/07_concepts/scalping.md ===== -->

---
id: concept_scalping
type: concept
title: Scalping
partition: 07_concepts
layer: L4
aliases: [scalping, scalper, intraday, 1-minute chart, tick chart]
related: [concept_order_flow, concept_market_microstructure, concept_trading_sessions_killzones, concept_trade_execution, concept_probability_fat_tails, concept_prop_firm_risk_rules]
status: synthesized
---

# Scalping

**Holding periods of seconds to minutes, targeting small moves, with many
trades.** It is the style of several Chart Fanatics headliners: Fabio
Valentini, billed as the "#1 scalper in the world", whose live-trading
episode is the channel's most-viewed video (~3.7M views per an aggregator);
Candace Lau (NQ sweep reversals); JJ Simon (NQ 1-minute).

## What makes or breaks scalping

| Factor | Why |
|---|---|
| **Costs** | Commissions and spread are a large fraction of each target. Edge must exceed cost per trade by a margin. |
| **Execution quality** | Slippage on stops; queue position on limits ([[concept_trade_execution]]) |
| **Order flow** | The only "fundamentals" at this horizon ([[concept_order_flow]]) |
| **Time-of-day** | Only trade the liquid windows ([[concept_trading_sessions_killzones]]) |
| **Risk per trade** | Small (Fabio ≈ 0.25%/trade per a T3 source) with daily loss limits |

## Competition evidence

Fabio Valentini placed in the top three of the **Robbins World Cup Trading
Championship** futures division. Sources cite returns from 218% to 500%+ in
a single year depending on the edition, which makes this one of the few
audited data points in this partition (T1/T2, numbers vary by source).

## Warnings

High win rates with small targets can mask negative skew
([[concept_probability_fat_tails]]). Many prop-firm-funded scalpers pass
evaluations and then fail in live markets: prop-firm conditions differ from
live trading ([[concept_prop_firm_risk_rules]]).


<!-- ===== FILE: trading-intelligence/07_concepts/smart-money-concepts.md ===== -->

---
id: concept_smart_money_concepts
type: concept
title: Smart Money Concepts / ICT (umbrella)
partition: 07_concepts
layer: L3
aliases: [SMC, ICT, Inner Circle Trader, smart money, institutional order flow, PD arrays]
related: [concept_liquidity, concept_fair_value_gap, concept_order_blocks_breakers, concept_premium_discount_ote, concept_amd_power_of_three, concept_smt_divergence, concept_market_structure, concept_trading_sessions_killzones]
derived_from: [concept_wyckoff_method, concept_dow_theory, concept_fibonacci, concept_support_resistance]
influenced_by: [person_michael_huddleston, person_richard_wyckoff]
status: synthesized
---

# Smart Money Concepts (SMC) / ICT

**A vocabulary for reading price as the footprint of large participants
seeking liquidity.** It was popularised by Michael J. Huddleston ("The Inner
Circle Trader") through free YouTube mentorships (notably the *2022 ICT
Mentorship* series). Retail educators later repackaged it as "SMC". It is the
dominant framework among Chart Fanatics' futures and FX guests.

## Building blocks (each has its own note)

| Block | Note |
|---|---|
| Liquidity pools (BSL/SSL), sweeps, runs | [[concept_liquidity]] |
| Market structure: BOS, CHoCH/MSS, displacement | [[concept_market_structure]] |
| Fair value gaps, inversion FVGs, BPR | [[concept_fair_value_gap]] |
| Order blocks, breakers, mitigation blocks | [[concept_order_blocks_breakers]] |
| Premium/discount, OTE (62–79% retracement) | [[concept_premium_discount_ote]] |
| Power of Three / AMD, daily bias | [[concept_amd_power_of_three]] |
| Kill zones, session ranges, "macros" | [[concept_trading_sessions_killzones]] |
| SMT divergence (ES vs NQ, EURUSD vs GBPUSD) | [[concept_smt_divergence]] |

## The canonical SMC sequence

1. **HTF bias / draw on liquidity.** Where is price likely to go next
   (an untaken high or low, or an unfilled FVG)?
2. **Wait for a sweep** of opposing liquidity in a kill zone.
3. **Displacement + MSS** confirm the sweep was a turn.
4. **Enter on the retrace** into an FVG, OB, or OTE zone.
5. **Stop** beyond the sweep extreme. **Target** the opposing liquidity pool.

## Honest assessment (lineage & evidence)

- Almost every component has older roots: Wyckoff's springs/upthrusts and
  composite operator, Dow's phases, Fibonacci retracements, classic
  supply/demand and gap theory. ICT's contribution is the *integration*,
  time-of-day emphasis, and precise vocabulary.
- **"Smart money hunts your stops" is a narrative.** The mechanical truth is
  simpler: stop clusters are liquidity, and large orders need liquidity
  ([[concept_market_microstructure]]).
- Rules are often taught discretionarily. Every "mechanical" ICT system
  online is a third-party reconstruction (e.g., the Trader Kane Lab Model
  write-up states that no first-person rulebook exists). Backtest before
  trusting ([[concept_backtesting]]).


<!-- ===== FILE: trading-intelligence/07_concepts/smt-divergence.md ===== -->

---
id: concept_smt_divergence
type: concept
title: SMT Divergence (correlated-market non-confirmation)
partition: 07_concepts
layer: L3
aliases: [SMT, smart money technique, correlation divergence, ES NQ divergence, intermarket divergence]
related: [concept_dow_theory, concept_intermarket_analysis, concept_divergence, concept_liquidity_sweep_reversal, concept_smart_money_concepts]
derived_from: [concept_dow_theory, concept_intermarket_analysis]
influenced_by: [person_michael_huddleston, person_charles_dow]
status: synthesized
---

# SMT Divergence

**Two normally correlated instruments disagree at a swing.** One makes a new
high or low and the other does not. The failure to confirm suggests the move
in the leader is a liquidity grab rather than genuine strength.

| Pair | Typical use |
|---|---|
| **ES vs NQ (vs YM)** | Index futures reversals at the NY open |
| **EURUSD vs GBPUSD** | FX majors at the London open |
| **EURUSD vs DXY** (inverse) | Dollar confirmation |

## Lineage

This is Dow Theory's **confirmation principle** (Industrials and Rails must
confirm each other), applied intraday to highly correlated futures. ICT
renamed it SMT ("smart money technique").

## In practice

Trader Kane's "Lab Model" (T3 reconstruction) executes on **NQ** and uses
**ES as the divergence reference**, combined with IFVGs and premium/discount.
Pair SMT with a sweep and a structure shift. Alone it fires too often in
noisy tape.


<!-- ===== FILE: trading-intelligence/07_concepts/stochastic-processes.md ===== -->

---
id: concept_stochastic_processes
type: concept
title: Stochastic Processes (Brownian motion, Itô, mean-reverting OU)
partition: 07_concepts
layer: L0
aliases: [Brownian motion, geometric Brownian motion, Ornstein-Uhlenbeck, Ito calculus]
related: [concept_random_walk_efficient_markets, concept_options_greeks, concept_volatility, concept_mean_reversion, concept_optimal_execution_market_impact]
influenced_by: [person_louis_bachelier, person_kiyosi_ito, person_steven_shreve]
status: synthesized
---

# Stochastic Processes

The mathematical language for prices that evolve randomly through time.

| Process | SDE | Use in trading |
|---|---|---|
| **Arithmetic Brownian motion** | `dS = μ dt + σ dW` | Bachelier's 1900 model; short-horizon price approximations, the Almgren-Chriss execution model |
| **Geometric Brownian motion** | `dS = μS dt + σS dW` | Black-Scholes-Merton; log-normal prices |
| **Ornstein-Uhlenbeck** | `dX = θ(μ − X) dt + σ dW` | Mean-reverting spreads, pairs trading, the half-life of reversion ([[concept_mean_reversion]]) |
| **Jump-diffusion** | GBM + Poisson jumps | Gap risk, earnings, news shocks ([[concept_news_trading]]) |
| **Stochastic volatility (Heston)** | variance follows its own mean-reverting process | Volatility smile, [[concept_volatility]] |

## Itô's lemma (the one formula to know)

For `f(S,t)`: `df = (∂f/∂t + μS ∂f/∂S + ½σ²S² ∂²f/∂S²) dt + σS ∂f/∂S dW`.
The `½σ²` term is why volatility drags on compounded growth: the geometric
mean return is about `μ − σ²/2`. That is the same mathematics behind
volatility drag in leveraged positions and behind the Kelly growth-rate
formula ([[concept_kelly_criterion_optimal_f]]).

## Practical takeaways

- **Half-life of mean reversion** = `ln(2)/θ`. Estimate it before trading a
  reversion setup.
- **The square-root-of-time rule** (`σ√t`) scales volatility across
  timeframes. It underlies ATR-based stops across
  [[concept_multi_timeframe_analysis]].

Standard references: Shreve, *Stochastic Calculus for Finance I & II*; MIT
18.S096 lectures (see `06_mathematics-foundations`).


<!-- ===== FILE: trading-intelligence/07_concepts/support-resistance.md ===== -->

---
id: concept_support_resistance
type: concept
title: Support & Resistance
partition: 07_concepts
layer: L2
aliases: [support, resistance, key levels, horizontal levels, role reversal, polarity, supply and demand zones]
related: [concept_market_structure, concept_volume_profile, concept_pivot_points, concept_fibonacci, concept_liquidity, concept_order_blocks_breakers]
status: synthesized
---

# Support & Resistance

**A price where a large enough imbalance of resting or responsive orders has
previously stopped price, and may again.** It is BabyPips Elementary Grade 1.

## Where real levels come from

1. **Prior swing highs and lows**, especially multi-touch ones.
2. **High-volume nodes and POC** (acceptance), see [[concept_volume_profile]].
3. **Session and period references**: prior day/week high, low, close; opens
   ([[concept_trading_sessions_killzones]], [[concept_pivot_points]]).
4. **Origin of displacement**: supply/demand zones and order blocks
   ([[concept_order_blocks_breakers]]).
5. **Round numbers** and option strikes with large open interest.

## Principles

- **Zones, not lines.** Use a range, typically sized by ATR.
- **Role reversal (polarity).** Broken resistance becomes support, and vice
  versa. This is the basis of the "break-and-retest" entry.
- **The more a level is tested, the weaker it gets** for continuation-against
  purposes: each test consumes resting orders. Meanwhile stops build beyond
  it, making it a liquidity target ([[concept_liquidity]]).
- **Higher timeframe levels dominate** ([[concept_multi_timeframe_analysis]]).

## Used by

Brando Elite's options swing playbook builds on higher-timeframe levels plus
news catalysts. Forrest Knight trades reactions at auction levels (PDH/PDL,
ONH/ONL).


<!-- ===== FILE: trading-intelligence/07_concepts/time-series-statistics.md ===== -->

---
id: concept_time_series_statistics
type: concept
title: Time-Series Statistics (stationarity, autocorrelation, cointegration)
partition: 07_concepts
layer: L0
aliases: [stationarity, autocorrelation, cointegration, GARCH, ARIMA]
related: [concept_stochastic_processes, concept_volatility, concept_mean_reversion, concept_backtesting, concept_machine_learning_finance]
influenced_by: [person_robert_engle, person_ruey_tsay]
status: synthesized
---

# Time-Series Statistics

**Why it matters.** Almost every "pattern" is a claim about the
autocorrelation structure of returns. You cannot evaluate a pattern without
these tools.

## Toolkit

- **Stationarity.** Prices are non-stationary (unit root). Returns are
  roughly stationary in mean, but not in variance. Test with ADF or KPSS.
- **Autocorrelation (ACF/PACF).** Positive autocorrelation of returns means
  momentum; negative means mean reversion. Daily index returns have near-zero
  autocorrelation. *Squared* returns are strongly autocorrelated: volatility
  clusters.
- **Volatility models.** ARCH (Engle, 1982), GARCH(1,1) (Bollerslev, 1986).
  Forecasting volatility is far easier than forecasting direction, and it
  drives position sizing ([[concept_position_sizing]]).
- **Cointegration** (Engle-Granger, Johansen). Two non-stationary series
  whose linear combination is stationary is the basis of pairs and spread
  trading ([[concept_mean_reversion]]).
- **Hurst exponent / variance ratio.** H > 0.5 means trending, H < 0.5 means
  mean-reverting. Use it as a regime diagnostic ([[concept_market_regimes]]).
- **Structural breaks.** Relationships change. Test for them, and prefer
  rolling or walk-forward estimates ([[concept_overfitting_validation]]).

## Pitfall: fractional differentiation

Integer differencing (returns) makes a series stationary but erases memory.
López de Prado proposes fractional differentiation to keep memory while
achieving stationarity, a useful idea for ML features
([[concept_machine_learning_finance]]).


<!-- ===== FILE: trading-intelligence/07_concepts/trade-execution.md ===== -->

---
id: concept_trade_execution
type: concept
title: Trade Execution (triggers, order types, confirmation)
partition: 07_concepts
layer: L5
aliases: [entry trigger, confirmation entry, limit entry, market entry, stop entry, order types, direction location aggression]
related: [concept_market_microstructure, concept_trade_management, concept_optimal_execution_market_impact, concept_multi_timeframe_analysis, concept_order_flow, concept_trading_plan]
status: synthesized
---

# Trade Execution

**Analysis tells you *where*; execution decides *whether you get filled, at
what price, and with what stop*.**

## Fabio Valentini's three-step model (T2/T3)

1. **Direction:** is the market balanced or imbalanced? Which side is in
   control ([[concept_auction_market_theory]])?
2. **Location:** only act at meaningful levels: value-area edges, POC, LVNs,
   prior-day references ([[concept_volume_profile]]).
3. **Aggression:** enter when order flow shows the expected side becoming
   aggressive (footprint, delta, CVD) ([[concept_order_flow]]).

This is the cleanest general-purpose execution checklist in the knowledge
base: **context → level → trigger**.

## Entry styles

| Style | Order | Pros | Cons |
|---|---|---|---|
| **Anticipatory limit** at the zone | Limit | Best price, tight stop | Fills on trades that run through (adverse selection) |
| **Confirmation** (signal candle close, MSS, breaker) | Stop/market after confirmation | Higher win rate | Worse price, wider stop |
| **Breakout stop-entry** | Buy-stop above level | Catches momentum | Slippage, fakeouts |

Forrest Knight: wait for the **signal candle to close** with a rejecting
wick; don't front-run. Yush: entries are *early*, so size smaller and keep
stops tight.

## Order-type mechanics

Market (certain fill, uncertain price) · Limit (certain price, uncertain
fill) · Stop (becomes market when triggered, so it slips in gaps) ·
Stop-limit (may not fill) · OCO/brackets (automate stop and target).

## Execution costs to log

Spread, commission, slippage vs intended price, and missed fills. These are
the silent killers of scalping edges ([[concept_scalping]]).


<!-- ===== FILE: trading-intelligence/07_concepts/trade-management.md ===== -->

---
id: concept_trade_management
type: concept
title: Trade Management (stops, targets, breakeven, scaling, trailing)
partition: 07_concepts
layer: L5
aliases: [stop loss, take profit, breakeven, scaling in, scaling out, pyramiding, trailing stop, partials, time stop]
related: [concept_trade_execution, concept_risk_reward_r_multiples, concept_position_sizing, concept_volatility, concept_expectancy]
influenced_by: [person_jesse_livermore, person_van_tharp]
status: synthesized
---

# Trade Management

BabyPips Senior covers stop-loss placement and scaling in and out.

## Stops

- **Structural:** beyond the level that invalidates the idea (the sweep
  extreme, the swing low). Preferred in SMC/AMT playbooks.
- **Volatility:** k × ATR ([[concept_volatility]]).
- **Time stop:** exit if the expected move hasn't happened within N bars
  (also one barrier of triple-barrier labelling).
- **Stops are not guarantees.** Gaps and fast markets slip
  ([[concept_probability_fat_tails]]).

## Targets

- The **opposing liquidity pool** or HTF level (SMC).
- The **other side of value / POC** (AMT).
- **Measured move** (patterns, Marci Silfrain).
- **R-multiple** targets (2R, 3R) or a trailing exit (trend following).

## Breakeven

Moving the stop to entry early cuts losers to scratches *and* cuts winners
that retest. Trader Kane's model uses **aggressive breakeven management**
(T3). This changes the win/loss distribution, so measure its net effect in
your journal ([[concept_trading_journal_review]]).

## Scaling

- **Pyramiding into winners** (Livermore; Turtles added units every ½N).
- **Scaling out** (partials) smooths equity but lowers average R.
- Never **average into losers** without a predefined total risk.

## Case: TG Capital (T2/T3)

Minimum target **1:20 R:R** from entry vs stop. Exit early if the EMA stack
breaks or price closes through the stop level. One trade at a time; new FVG
setups are ignored until the position closes.


<!-- ===== FILE: trading-intelligence/07_concepts/trading-journal-review.md ===== -->

---
id: concept_trading_journal_review
type: concept
title: Trading Journal & Performance Review
partition: 07_concepts
layer: L8
aliases: [trading journal, trade log, review, MAE, MFE, playbook review, tradezella]
related: [concept_performance_metrics, concept_trading_plan, concept_trading_psychology, concept_backtesting, concept_expectancy]
influenced_by: [person_brett_steenbarger]
status: synthesized
---

# Trading Journal & Review

**The feedback loop that turns trades into data.** Tools such as TradeZella
host public "playbooks" of many Chart Fanatics guests' strategies.

## Fields that matter

| Field | Why |
|---|---|
| Setup tag / grade (A+, A, B) | Expectancy *per setup* ([[concept_expectancy]]) |
| Planned entry, stop, target; actual fills | Execution slippage ([[concept_trade_execution]]) |
| R result, MAE, MFE | Stop and target optimisation |
| Session / time | Time-of-day edge ([[concept_trading_sessions_killzones]]) |
| Regime label | When the setup works ([[concept_market_regimes]]) |
| Rule adherence (Y/N), emotion tags | Psychology leaks ([[concept_trading_psychology]]) |
| Screenshot before and after | Pattern-recognition training |

## Review cadence

- **Daily:** adherence, mistakes, one lesson.
- **Weekly:** stats by setup and session; cut the worst-performing context.
- **Monthly/quarterly:** edge decay check; compare to backtest expectations
  ([[concept_overfitting_validation]]).

Steenbarger's approach: review what you do *well* as rigorously as your
mistakes, and do more of it.


<!-- ===== FILE: trading-intelligence/07_concepts/trading-plan.md ===== -->

---
id: concept_trading_plan
type: concept
title: Trading Plan (rules written before the trade)
partition: 07_concepts
layer: L7
aliases: [trading plan, playbook, rules, checklist, pre-market routine, plan your trade trade your plan]
related: [concept_trading_psychology, concept_trade_execution, concept_position_sizing, concept_trading_journal_review, concept_multi_timeframe_analysis]
status: synthesized
---

# Trading Plan

BabyPips Junior: develop your own trading plan, decide which type of trader
you are, and "plan your trade and trade your plan".

## Minimum viable plan

1. **Markets & sessions:** what, and when (e.g., NQ, 09:30–11:00 ET).
2. **Regime filter:** when the playbook is ON or OFF ([[concept_market_regimes]]).
3. **Setups:** precise, testable definitions with screenshots (an A+/A/B
   grading like JJ Simon's).
4. **Execution:** trigger, order type, stop, target, management
   ([[concept_trade_execution]], [[concept_trade_management]]).
5. **Risk:** per trade, per day, per week; drawdown actions
   ([[concept_position_sizing]]).
6. **Psychology rules:** max trades, a break after N losses, no revenge trades.
7. **Review loop:** journal fields and a weekly review cadence
   ([[concept_trading_journal_review]]).

## Framework for developing traders (Umar Ashraf, 5 stages; stages 1–2 confirmed)

1. **Novice:** education, paper trading, choose a market and style.
2. **Developing:** data collection and early strategy; avoid ego and revenge
   trades.
3–5. *(Not retrieved. Scrape the Chart Fanatics/Tradezella playbook to
   complete.)*

You cannot skip stages.


<!-- ===== FILE: trading-intelligence/07_concepts/trading-psychology.md ===== -->

---
id: concept_trading_psychology
type: concept
title: Trading Psychology & Discipline
partition: 07_concepts
layer: L7
aliases: [trading psychology, discipline, tilt, revenge trading, FOMO, fear and greed, loss aversion, best loser wins, mental game]
related: [concept_probabilistic_thinking, concept_trading_plan, concept_trading_journal_review, concept_risk_of_ruin_drawdown]
influenced_by: [person_mark_douglas, person_brett_steenbarger, person_tom_hougaard, person_daniel_kahneman, person_jared_tendler]
status: synthesized
---

# Trading Psychology & Discipline

BabyPips Senior covers trading psychology. Every legend in this knowledge
base ranks it at or near the top.

## Behavioural roots (Kahneman & Tversky, prospect theory, 1979)

- **Loss aversion:** losses hurt ~2× as much as equal gains please. So traders
  **cut winners early and hold losers** (the disposition effect), exactly
  backwards.
- **Overconfidence, recency, and confirmation bias** feed over-trading and
  ignoring stops.

## Practitioner frameworks

| Author | Core idea |
|---|---|
| **Mark Douglas** (*The Disciplined Trader*, *Trading in the Zone*) | Think in probabilities. Accept risk fully *before* entry. Five fundamental truths ([[concept_probabilistic_thinking]]). |
| **Brett Steenbarger** (*The Psychology of Trading*, *The Daily Trading Coach*) | Be your own coach; build on strengths; solution-focused self-review |
| **Tom Hougaard** (*Best Loser Wins*) | The winner is the trader who loses best. Train behaviour that is uncomfortable (adding to winners, taking small losses instantly). |
| **Jared Tendler** (*The Mental Game of Trading*) | Map tilt, fear, and greed patterns, then fix the underlying flaw |
| **Ed Seykota** | "Win or lose, everybody gets what they want out of the market." |

## Chart Fanatics & Words of Rizdom voices

- **Marci Silfrain:** spends far more time backtesting, sim, and paper
  trading than live; plans to lose every trade and the next 20 in a row.
- **Umar Ashraf's 5-stage framework:** "Trading is hard", "the goal is NOT
  to make money" at first, you can't skip stages, and avoid ego and revenge
  trades in the developing stage.
- Words of Rizdom also hosts trading psychologists (e.g., "Here's How I MAKE
  Traders Profitable Long Term").

## Operational guardrails

Pre-defined daily loss limit · mandatory break after N losses · pre-market
routine · post-session journal ([[concept_trading_journal_review]]) · size
reduction after a drawdown ([[concept_risk_of_ruin_drawdown]]).


<!-- ===== FILE: trading-intelligence/07_concepts/trading-sessions-killzones.md ===== -->

---
id: concept_trading_sessions_killzones
type: concept
title: Trading Sessions & Kill Zones (time-of-day edge)
partition: 07_concepts
layer: L2
aliases: [market hours, kill zone, killzone, Asian session, London session, New York session, kill zones, London open, NY open, opening range, initial balance, macro times]
related: [concept_liquidity, concept_amd_power_of_three, concept_smart_money_concepts, concept_volatility, concept_news_trading, concept_scalping]
influenced_by: [person_michael_huddleston, person_larry_williams]
status: synthesized
---

# Trading Sessions & Kill Zones

**Volatility and liquidity are not uniform through the day.** Time is a
filter as important as price. BabyPips teaches market hours early because FX
trades 24/5 across overlapping sessions.

## The FX/futures clock (New York time, approximate)

| Window | Character |
|---|---|
| **Asian session** (~19:00–03:00) | Lower range; builds the Asian high/low (often the "accumulation" range) |
| **London open / London kill zone** (~02:00–05:00) | First major expansion; frequently sweeps the Asian range |
| **NY pre-market & US data** (08:30) | News shocks ([[concept_news_trading]]) |
| **NY open / NY AM kill zone** (~09:30–11:00 for indices; 07:00–10:00 FX) | Highest volume overlap with London; main reversals and trends |
| **London close** (~10:00–12:00) | Profit-taking reversals in FX |
| **NY PM / power hour** (15:00–16:00) | Index rebalancing flows |

## How playbooks use time

- **TG Capital (Chart Fanatics):** trades *only* the London kill zone,
  **3:00–6:30 AM NY time**, on the 30-minute chart (T2).
- **Trader Kane, "The Lab Model":** uses the **10:00 AM ET four-hour candle**
  as a timing anchor on NQ (T3 reconstruction).
- **JJ Simon:** treats the NY open/pre-open price as the session's *fair
  price* (`strategy_jj_simon_fair_pricing`).
- **AMT:** the **initial balance** (first hour) frames day type
  ([[concept_auction_market_theory]]).

## Lineage

Larry Williams (day-of-week and time-of-day studies) → Toby Crabel (opening
range breakout, 1990) → ICT kill zones and "macro" windows → session-based
prop-firm scalping. See also [[concept_amd_power_of_three]].


<!-- ===== FILE: trading-intelligence/07_concepts/trend-following.md ===== -->

---
id: concept_trend_following
type: concept
title: Trend Following
partition: 07_concepts
layer: L4
aliases: [trend following, CTA, managed futures, turtle trading, time-series momentum, Donchian breakout]
related: [concept_breakout_trading, concept_moving_averages, concept_market_structure, concept_position_sizing, concept_market_regimes, concept_dow_theory]
contrasts_with: [concept_mean_reversion]
derived_from: [concept_dow_theory]
influenced_by: [person_richard_donchian, person_richard_dennis, person_ed_seykota, person_jesse_livermore, person_michael_covel]
status: synthesized
---

# Trend Following

**Cut losses short, let profits run, and follow price, not predictions.**

## Mechanics

- **Entry:** breakout of an N-day high/low (Donchian channel), MA crossover,
  or a structure break ([[concept_breakout_trading]]).
- **Exit:** a shorter opposite channel, a trailing stop (ATR multiple), or an
  MA cross.
- **Sizing:** volatility-normalised. The Turtle unit: risk ~1% of equity per
  1 N (N = 20-day ATR) ([[concept_position_sizing]]).
- **Diversification:** dozens of uncorrelated futures markets. A few outlier
  trends pay for many small losses.

## Return profile

Win rate ~30–40%, large average win/loss ratio, **positive skew**, long flat
or drawdown periods, and crisis alpha (it often profits in sustained
selloffs). It is the opposite profile of mean reversion and short vol.

## Lineage

Livermore ("the big money is in the big swing", "line of least resistance")
→ Donchian (1960s channel rules, the "father of trend following") →
**Richard Dennis & William Eckhardt's Turtle experiment (1983–84)**: trading
can be taught (Faith, *Way of the Turtle*; Covel, *The Complete TurtleTrader*)
→ Seykota, Parker (Chesapeake), Basso, Hite → modern CTAs. Systematic
descendants: Carver (*Systematic Trading*), Clenow (*Following the Trend*).

## Evidence

Time-series momentum is documented across asset classes over a century of
data. It is one of the best-supported anomalies, but returns are lumpy and
crowded in some periods.


<!-- ===== FILE: trading-intelligence/07_concepts/trendlines.md ===== -->

---
id: concept_trendlines
type: concept
title: Trendlines & Channels
partition: 07_concepts
layer: L2
aliases: [trendline, trend channel, measured move, trendline break]
related: [concept_market_structure, concept_support_resistance, concept_trend_following, concept_liquidity, concept_chart_patterns]
sources:
  - {title: "Chart Fanatics — Tori's Trendline Trading Playbook", url: "https://www.chartfanatics.com/playbook/trendline-strategy", tier: T2}
  - {title: "Chart Fanatics — Measured Move Trend Strategy (Marci Silfrain)", url: "https://www.chartfanatics.com/strategies/measured-move-trend-strategy", tier: T2}
status: synthesized
---

# Trendlines & Channels

A line connecting two or more swing lows (uptrend) or highs (downtrend). It
gives the trend's *rate* and a dynamic support/resistance.

## Construction rules (to reduce subjectivity)

- Use **swing points**, not arbitrary wicks. Pick bodies or wicks and stay
  consistent.
- **Two points draw it, the third touch validates it.**
- **Slope matters.** Very steep lines break quickly (blow-off). Shallow lines
  persist.
- **Channel:** a parallel line through the opposite swings projects targets.

## Two Chart Fanatics trendline playbooks

| Playbook | Core |
|---|---|
| **Tori Trades (T2)** | Swing trading on the **4-hour** chart with trendlines and **no indicators** |
| **Marci Silfrain, Measured Move / "Little RZY" (T2/T3)** | Confirm trend → strong impulse → pullback; draw a trendline across the pullback; enter on the break or rejection; project a **measured move** equal to the prior impulse. Bollinger Bands give context. Third-party write-ups add a filter favouring the first two touches. |

## Caveat

Obvious trendlines collect stops beneath them, so a "trendline break" is
frequently a liquidity grab before continuation ([[concept_liquidity]]). Pair
trendline signals with structure and volume confirmation.


<!-- ===== FILE: trading-intelligence/07_concepts/volatility.md ===== -->

---
id: concept_volatility
type: concept
title: Volatility (realized, implied, ATR, regimes)
partition: 07_concepts
layer: L0
aliases: [ATR, average true range, implied volatility, realized volatility, VIX]
related: [concept_probability_fat_tails, concept_options_greeks, concept_position_sizing, concept_market_regimes, concept_bollinger_bands, concept_time_series_statistics]
influenced_by: [person_welles_wilder, person_sheldon_natenberg]
status: synthesized
---

# Volatility

**Definition.** The dispersion of returns, usually the annualised standard
deviation of log returns. It is the single most useful number in trading.
It sets stop distance, position size, target realism, and options prices.

## Measures

| Measure | Formula / idea | Use |
|---|---|---|
| **Realized (historical) vol** | `σ_annual = stdev(daily log returns) × √252` | Risk budgeting, vol targeting |
| **ATR** (Wilder, 1978) | EMA of true range = max(H−L, \|H−C₋₁\|, \|L−C₋₁\|) | Stop placement and position sizing in price units |
| **Implied vol** | Vol that equates an option model price to the market price | Market's forecast plus a risk premium; VIX for the S&P 500 |
| **Parkinson / Garman-Klass** | Range-based estimators | More efficient than close-to-close |

## Stylised facts

- **Clustering.** High-vol days follow high-vol days (GARCH, see
  [[concept_time_series_statistics]]).
- **Leverage effect.** Equity vol rises when prices fall (negative
  spot-vol correlation).
- **Implied usually exceeds realized.** That gap is the *variance risk
  premium*, the edge behind short-vol strategies (and their tail risk).
- **Vol mean-reverts.** Compression precedes expansion. This is the basis of
  squeeze and breakout setups ([[concept_breakout_trading]],
  [[concept_bollinger_bands]]).

## Execution & risk rules derived from vol

1. **Size inversely to volatility:** `units = (equity × risk%) / (k × ATR × point value)`.
   This is the Turtle "N" unit rule ([[concept_position_sizing]]).
2. **Stops in ATR multiples** adapt to regime. A fixed-pip stop does not.
3. **Expected daily range ≈ ATR.** A target of 3× ADR on an intraday
   scalp is unrealistic.


<!-- ===== FILE: trading-intelligence/07_concepts/volume-profile.md ===== -->

---
id: concept_volume_profile
type: concept
title: Volume Profile (POC, value area, HVN/LVN)
partition: 07_concepts
layer: L1
aliases: [POC, point of control, value area, VAH, VAL, HVN, LVN, high volume node, low volume node]
related: [concept_auction_market_theory, concept_vwap, concept_order_flow, concept_support_resistance, concept_mean_reversion]
derived_from: [concept_auction_market_theory]
influenced_by: [person_peter_steidlmayer, person_james_dalton]
sources:
  - {title: "TradeZella — Volume Profile Strategy (Forrest Knight)", url: "https://www.tradezella.com/strategies/volume-profile-strategy", tier: T3}
status: synthesized
---

# Volume Profile

A horizontal histogram of **volume traded at each price** over a chosen
window: session, composite, or anchored.

## Anatomy

- **POC (Point of Control).** The price with the most volume. It is the
  "fairest" price, and price is magnetically drawn to it in balance.
- **Value Area (VA).** The range holding ~70% of volume, bounded by **VAH**
  and **VAL**.
- **HVN (high-volume node).** Price was accepted there. It acts as
  support/resistance and price slows in it.
- **LVN (low-volume node).** Price was rejected there. Price travels fast
  through it, and it often marks the edge between two distributions.

## Canonical plays

| Play | Logic |
|---|---|
| **Fade the edge back to POC** | In balance, rejection at VAH/VAL targets POC ([[concept_mean_reversion]]) |
| **80% rule** (Dalton/Market Profile lore) | If price opens outside value and re-enters it, holding for two TPO periods, it often traverses to the other side of value |
| **Edge-to-edge through LVN** | Forrest Knight: trade the reaction at the edge of an HVN at key auction levels (PDH/PDL, ONH/ONL), targeting the next node through the low-volume gap. Wait for the **signal candle to close** with a rejecting wick (T3). |
| **Breakout acceptance** | Value migrating beyond prior VAH, with volume building, confirms imbalance ([[concept_breakout_trading]]) |

## Relation to VWAP

VWAP is the *volume-weighted mean* price. POC is the *volume mode*. Both
estimate fair value and both are used as mean-reversion anchors
([[concept_vwap]]).


<!-- ===== FILE: trading-intelligence/07_concepts/vwap.md ===== -->

---
id: concept_vwap
type: concept
title: VWAP (volume-weighted average price) & anchored VWAP
partition: 07_concepts
layer: L1
aliases: [VWAP, anchored VWAP, AVWAP, VWAP bands]
related: [concept_volume_profile, concept_auction_market_theory, concept_mean_reversion, concept_optimal_execution_market_impact, concept_moving_averages]
influenced_by: [person_brian_shannon]
status: synthesized
---

# VWAP

`VWAP_t = Σ(Pᵢ·Vᵢ) / Σ Vᵢ`, accumulated from an anchor (session open by
default).

## Two worlds, one line

1. **Execution benchmark** (institutional). Large orders are judged against
   VWAP. VWAP algorithms slice orders in proportion to the expected volume
   curve ([[concept_optimal_execution_market_impact]]). Institutional
   participation is one reason VWAP behaves as a real level.
2. **Trading level** (discretionary). Price above VWAP means buyers are in
   control on average for the session; below means sellers. Standard-deviation
   bands give mean-reversion extremes.

## Anchored VWAP

Anchor at a meaningful event (earnings gap, swing low, news candle,
[[concept_episodic_pivot]]) to see the average cost basis of everyone who has
traded since. Brian Shannon popularised AVWAP among swing traders.

## Uses in this knowledge base

- Fair-value anchor alongside POC in AMT-based strategies.
- JJ Simon's **Fair Pricing Theory** treats a reference price at the NY open
  as "fair" and trades reversion toward it. That is conceptually the same
  move as VWAP or POC reversion (`strategy_jj_simon_fair_pricing`).


<!-- ===== FILE: trading-intelligence/07_concepts/wyckoff-method.md ===== -->

---
id: concept_wyckoff_method
type: concept
title: Wyckoff Method (accumulation, distribution, composite operator)
partition: 07_concepts
layer: L3
aliases: [Wyckoff, composite man, composite operator, spring, upthrust, UTAD, effort vs result, accumulation schematic, distribution schematic]
related: [concept_amd_power_of_three, concept_liquidity, concept_smart_money_concepts, concept_order_flow, concept_auction_market_theory, concept_market_structure]
derived_from: [concept_dow_theory]
influenced_by: [person_richard_wyckoff]
status: synthesized
---

# Wyckoff Method

Richard D. Wyckoff (1873–1934) studied the operators of his era (Livermore,
Keene, Morgan) and codified their methods. Key works: *Studies in Tape
Reading* (1910, as "Rollo Tape") and his 1930s stock-market course. David
Weis (*Trades About to Happen*) and Tom Williams (VSA) carried it forward.

## Three laws

1. **Supply & demand.** Price rises when demand exceeds supply.
2. **Cause & effect.** The size of the range (cause) projects the size of
   the subsequent trend (effect). This is the origin of point-and-figure
   counts and of "measured move" thinking.
3. **Effort vs result.** Volume (effort) should match price movement
   (result). Divergence signals absorption, the ancestor of order-flow
   absorption ([[concept_order_flow]]).

## The composite operator

Imagine **one large operator** behind the market who accumulates quietly,
marks price up, distributes, then marks down. This is the conceptual ancestor
of "smart money" in SMC/ICT ([[concept_smart_money_concepts]]).

## Schematics (phases A–E)

- **Accumulation:** PS → SC (selling climax) → AR → ST → **Spring** (false
  break below support that sweeps stops) → test → SOS → LPS → markup.
- **Distribution:** PSY → BC (buying climax) → AR → ST → **UTAD / Upthrust**
  (false break above resistance) → SOW → LPSY → markdown.

## Lineage map

`Wyckoff spring/upthrust` = `liquidity sweep / stop hunt` ([[concept_liquidity]])
`Wyckoff accumulation → spring → markup` = `AMD / Power of Three` ([[concept_amd_power_of_three]])
`Composite operator` = `smart money`
`Effort vs result` = `absorption / delta divergence`
`Cause & effect` = `measured move`, range projection
