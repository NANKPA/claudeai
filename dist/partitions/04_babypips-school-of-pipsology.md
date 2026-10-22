# Partition 04_babypips-school-of-pipsology


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/README.md ===== -->

---
id: course_babypips_school_of_pipsology
type: course
title: BabyPips — School of Pipsology (course map)
partition: 04_babypips-school-of-pipsology
layer: L0
aliases: [BabyPips, School of Pipsology, babypips forex course]
related: [concept_leverage_margin, concept_support_resistance, concept_fundamental_macro_analysis, concept_position_sizing]
sources:
  - {title: "School of Pipsology — Babypips.com", url: "https://www.babypips.com/learn/forex", tier: T2}
  - {title: "Summer School — School of Pipsology", url: "https://www.babypips.com/learn/forex/summer-school", tier: T2}
  - {title: "Undergraduate - Senior — School of Pipsology", url: "https://www.babypips.com/learn/forex/undergraduate-senior", tier: T2}
  - {title: "Elementary — School of Pipsology", url: "https://www.babypips.com/learn/forex/elementary", tier: T2}
  - {title: "Finance Magnates — babypips.com updates its forex school", url: "https://www.financemagnates.com/forex/analysis/babypips-com-updates-its-forex-school/", tier: T3}
status: partial — structure from web search; lesson text pending scrape
---

# Partition 04 — BabyPips School of Pipsology

> **Scrape status (2026-10-11):** babypips.com sits behind Cloudflare bot
> protection that answers every automated request (even `robots.txt`) with
> HTTP 403 from cloud servers. The crawler deliberately does not try to get
> around that. To capture the lessons, run `tools/scrapers/babypips_course.py`
> on your own computer (pass `--cookies` with your own login for premium
> lessons). The course **structure** below comes from search results of the
> official pages, and each course note is a concept-level summary written for
> this knowledge base, not BabyPips' text.

## Course map (current layout: 11 courses)

| # | Course | Grades / modules | Access | Concept hubs | Structure confidence |
|---|---|---|---|---|---|
| 1 | **Preschool** | Intro to the forex market | Free | [[concept_market_microstructure]], [[concept_leverage_margin]] | confirmed |
| 2 | **Kindergarten** | Choosing a broker; how to analyse currency markets | Free | [[concept_leverage_margin]] | confirmed |
| 3 | **Elementary** | G1 Support & Resistance · G2 Japanese Candlesticks · G3 Fibonacci · G4 Moving Averages · G5 Popular Chart Indicators | Free | [[concept_support_resistance]], [[concept_candlestick_patterns]], [[concept_fibonacci]], [[concept_moving_averages]], [[concept_oscillators_momentum]] | confirmed |
| 4 | **Middle School** | G6 Oscillators & Momentum · G7 Important Chart Patterns · G8 Pivot Points | Free | [[concept_oscillators_momentum]], [[concept_chart_patterns]], [[concept_pivot_points]] | confirmed |
| 5 | **Summer School** | Heikin Ashi · Elliott Wave Theory · Harmonic Price Patterns · Trading Divergences | Free/mixed | [[concept_elliott_wave]], [[concept_divergence]], [[concept_candlestick_patterns]] | confirmed |
| 6 | **High School** | Price Action (G9) · Trading Breakouts (and fakeouts) · Multiple Time Frame Analysis | Premium | [[concept_price_action]], [[concept_breakout_trading]], [[concept_multi_timeframe_analysis]] | confirmed |
| 7 | **Undergraduate Freshman** | Macro fundamentals behind currency moves | Premium | [[concept_fundamental_macro_analysis]] | confirmed |
| 8 | **Undergraduate Sophomore** | Market sentiment/COT · Trading the news · Carry trade · USD index · Intermarket correlations · Using equities to trade FX | Premium | [[concept_market_sentiment]], [[concept_news_trading]], [[concept_carry_trade]], [[concept_intermarket_analysis]] | inferred (older outline + third-party) |
| 9 | **Undergraduate Junior** | Developing a trading plan · Which type of trader are you · Trading journal | Premium | [[concept_trading_plan]], [[concept_trading_journal_review]] | inferred |
| 10 | **Undergraduate Senior** | Risk Management · Trading With Leverage · Position Sizing · Stop Loss Placement · Scaling In and Out · Currency Correlations · (risk budgets & circuit breakers; drawdown math) | Premium | [[concept_risk_of_ruin_drawdown]], [[concept_position_sizing]], [[concept_trade_management]], [[concept_correlation_portfolio_risk]], [[concept_trading_psychology]] | confirmed |
| 11 | **Graduation / advanced** | (not confirmed by search; third-party reviews mention levels up to "Doctorate") | — | — | unconfirmed |

Historical note: the 2006 ebook edition used a 14-grade layout (Preschool
"Types of Trading", Kindergarten "Types of Charts" … 12th Grade "Market Hours"
… 14th Grade "Plan Your Trade and Trade Your Plan"). Market hours now sit
earlier in the curriculum. See [[concept_trading_sessions_killzones]].

## How BabyPips maps onto the 9-layer stack

```
Preschool/Kindergarten ─► L1 mechanics (pips, lots, leverage, sessions, brokers)
Elementary/Middle/Summer ─► L2–L3 technical toolset
High School ─────────────► L3–L5 price action, breakouts, MTF
Freshman/Sophomore ──────► L3 fundamentals, sentiment, intermarket, carry
Junior ──────────────────► L7 trading plan & trader type
Senior ──────────────────► L6 risk & money management, L7 psychology
```

**Gap vs Chart Fanatics:** BabyPips gives the *retail TA canon* and FX
fundamentals. It covers little on **auction market theory, order flow,
liquidity sweeps/SMC, or futures microstructure**, which dominate Chart
Fanatics. Use BabyPips for L0–L3 literacy and L6 risk basics, and Chart
Fanatics plus the books for the professional L3–L5 layer.


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/01-preschool.md ===== -->

---
id: course_babypips_preschool
type: course
title: "BabyPips Course 1 — Preschool: what forex is"
partition: 04_babypips-school-of-pipsology
layer: L1
part_of: [course_babypips_school_of_pipsology]
covers: [concept_market_microstructure, concept_leverage_margin, concept_trading_sessions_killzones]
status: synthesized
---

# Preschool — the forex market

**Learning outcomes (concept-level summary):**

- FX is the exchange of one currency for another. It is **decentralised
  (OTC)**, runs 24 hours on weekdays, and is the largest market by turnover.
  See [[concept_market_microstructure]].
- **Currency pairs:** base/quote; majors (EUR/USD, USD/JPY, GBP/USD, USD/CHF,
  AUD/USD, USD/CAD, NZD/USD), crosses, exotics.
- **Bid/ask, spread, pip, lot, leverage, margin**: the arithmetic of a
  position ([[concept_leverage_margin]]).
- **Who trades:** central banks, commercial banks, institutions, corporates,
  retail via brokers. Liquidity concentrates in the London and New York
  sessions ([[concept_trading_sessions_killzones]]).
- **Ways to trade:** spot, futures (CME currency futures), options, and CFDs.

**Bridge to professional practice:** retail spot FX has no consolidated
volume. Futures traders (6E, 6B…) can use real volume and order flow
([[concept_order_flow]]).


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/02-kindergarten.md ===== -->

---
id: course_babypips_kindergarten
type: course
title: "BabyPips Course 2 — Kindergarten: brokers & types of analysis"
partition: 04_babypips-school-of-pipsology
layer: L1
part_of: [course_babypips_school_of_pipsology]
covers: [concept_leverage_margin, concept_fundamental_macro_analysis, concept_market_sentiment, concept_candlestick_patterns]
status: synthesized
---

# Kindergarten — brokers and the three types of analysis

- **Choosing a broker:** regulation, execution model (dealing desk vs
  ECN/STP), spreads/commissions, margin rules. Execution quality matters
  ([[concept_trade_execution]]).
- **Three lenses:** **technical** (price/volume history), **fundamental**
  (macro, rates, [[concept_fundamental_macro_analysis]]) and **sentiment**
  (positioning, [[concept_market_sentiment]]). Professionals combine all three
  with a primary lens.
- **Chart types:** line, bar (OHLC), candlestick ([[concept_candlestick_patterns]]).
- **Demo trading** as practice. Its limits: no slippage and no emotional cost
  ([[concept_trading_psychology]]).


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/03-elementary.md ===== -->

---
id: course_babypips_elementary
type: course
title: "BabyPips Course 3 — Elementary (Grades 1–5): the core technical toolkit"
partition: 04_babypips-school-of-pipsology
layer: L3
part_of: [course_babypips_school_of_pipsology]
covers: [concept_support_resistance, concept_trendlines, concept_candlestick_patterns, concept_fibonacci, concept_moving_averages, concept_bollinger_bands, concept_oscillators_momentum]
sources:
  - {title: "Elementary — School of Pipsology", url: "https://www.babypips.com/learn/forex/elementary", tier: T2}
status: synthesized
---

# Elementary — Grades 1–5

| Grade | Topic | Key takeaways | Concept note |
|---|---|---|---|
| **1** | Support & Resistance levels | S/R as zones; role reversal; trendlines and channels; trade the bounce or the break | [[concept_support_resistance]], [[concept_trendlines]] |
| **2** | Japanese Candlesticks | Body and wick anatomy; single, dual, and triple-candle patterns; context matters | [[concept_candlestick_patterns]] |
| **3** | Fibonacci | Retracements (38.2/50/61.8) and extensions; confluence with S/R; stops beyond the next level | [[concept_fibonacci]] |
| **4** | Moving Averages | SMA vs EMA; crossovers; dynamic S/R; lag trade-off | [[concept_moving_averages]] |
| **5** | Popular Chart Indicators | Bollinger Bands, MACD, Parabolic SAR, Stochastic, RSI, ADX, Ichimoku Kinko Hyo; combine trend and momentum tools | [[concept_bollinger_bands]], [[concept_oscillators_momentum]] |

**Professional upgrade path:** Grade 1 S/R becomes auction-based levels
(POC, VAH/VAL, prior-day H/L) in [[concept_volume_profile]] and liquidity
pools in [[concept_liquidity]]. Grade 3 Fibonacci becomes ICT's OTE in
[[concept_premium_discount_ote]].


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/04-middle-school.md ===== -->

---
id: course_babypips_middle_school
type: course
title: "BabyPips Course 4 — Middle School (Grades 6–8): momentum, patterns, pivots"
partition: 04_babypips-school-of-pipsology
layer: L3
part_of: [course_babypips_school_of_pipsology]
covers: [concept_oscillators_momentum, concept_chart_patterns, concept_pivot_points, concept_breakout_trading, concept_mean_reversion]
status: synthesized
---

# Middle School — Grades 6–8

| Grade | Topic | Key takeaways | Concept note |
|---|---|---|---|
| **6** | Oscillators & momentum indicators | Leading (oscillators) vs lagging (trend) indicators; using MACD to confirm trend; avoid oscillator signals against strong trends | [[concept_oscillators_momentum]] |
| **7** | Important chart patterns | Double tops/bottoms, head & shoulders, wedges, rectangles, triangles; measured targets | [[concept_chart_patterns]] |
| **8** | Pivot points | Calculate pivots (P, R1–R3, S1–S3); range trading vs breakouts at pivots | [[concept_pivot_points]] |

**Upgrade path:** double tops/bottoms = equal highs/lows = **liquidity**. The
failed pattern is often the better trade ([[concept_liquidity_sweep_reversal]]).


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/05-summer-school.md ===== -->

---
id: course_babypips_summer_school
type: course
title: "BabyPips Course 5 — Summer School: Heikin Ashi, Elliott, harmonics, divergence"
partition: 04_babypips-school-of-pipsology
layer: L3
part_of: [course_babypips_school_of_pipsology]
covers: [concept_candlestick_patterns, concept_elliott_wave, concept_fibonacci, concept_divergence]
sources:
  - {title: "Summer School — School of Pipsology", url: "https://www.babypips.com/learn/forex/summer-school", tier: T2}
status: synthesized
---

# Summer School — advanced chart reading

| Module | Key takeaways | Concept note |
|---|---|---|
| **Heikin Ashi** | Averaged candles that smooth trend reading. Not real prices, so never use them for backtest fills. | [[concept_candlestick_patterns]] |
| **Elliott Wave Theory** | 5-wave impulse, 3-wave correction, wave rules, and Fibonacci relationships | [[concept_elliott_wave]] |
| **Harmonic price patterns** | ABCD, Gartley, Butterfly, Crab, Bat: Fibonacci-ratio swing geometry with defined invalidation | [[concept_fibonacci]] |
| **Trading divergences** | Regular (reversal) vs hidden (continuation) divergence | [[concept_divergence]] |

**Evidence note:** harmonic and wave methods are highly parameterised.
Validate them with out-of-sample testing ([[concept_overfitting_validation]]).


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/06-high-school.md ===== -->

---
id: course_babypips_high_school
type: course
title: "BabyPips Course 6 — High School: price action, breakouts, multiple time frames"
partition: 04_babypips-school-of-pipsology
layer: L4
part_of: [course_babypips_school_of_pipsology]
covers: [concept_price_action, concept_breakout_trading, concept_multi_timeframe_analysis, concept_market_structure]
status: synthesized
---

# High School (premium) — price action, breakouts, MTF

- **Price action trading (Grade 9):** reading raw candles, structure, and
  levels with few indicators ([[concept_price_action]],
  [[concept_market_structure]]).
- **Trading breakouts (and fakeouts):** volatility compression → expansion;
  continuation vs failed breakouts ([[concept_breakout_trading]]).
- **Multiple time frame analysis:** HTF bias, setup TF, trigger TF; choose the
  combination that matches your style ([[concept_multi_timeframe_analysis]]).

**Upgrade path:** the fakeout chapter is the doorway to the
[[concept_liquidity_sweep_reversal]] playbooks that dominate Chart Fanatics.


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/07-undergraduate-freshman.md ===== -->

---
id: course_babypips_freshman
type: course
title: "BabyPips Course 7 — Undergraduate Freshman: macro fundamentals behind currency moves"
partition: 04_babypips-school-of-pipsology
layer: L3
part_of: [course_babypips_school_of_pipsology]
covers: [concept_fundamental_macro_analysis, concept_news_trading, concept_carry_trade]
status: synthesized
---

# Undergraduate Freshman (premium) — fundamentals

- **Interest rates rule FX:** relative policy-rate expectations, central-bank
  guidance, QE/QT ([[concept_fundamental_macro_analysis]]).
- **Economic indicators:** GDP, CPI/PCE, employment (NFP), PMIs, retail
  sales, trade balance. Markets trade the **surprise vs consensus**
  ([[concept_news_trading]]).
- **Monetary vs fiscal policy;** capital flows; risk-on/off and safe havens.
- **Interest-rate differentials** as the basis of [[concept_carry_trade]].


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/08-undergraduate-sophomore.md ===== -->

---
id: course_babypips_sophomore
type: course
title: "BabyPips Course 8 — Undergraduate Sophomore: sentiment, news, carry, intermarket"
partition: 04_babypips-school-of-pipsology
layer: L3
part_of: [course_babypips_school_of_pipsology]
covers: [concept_market_sentiment, concept_news_trading, concept_carry_trade, concept_intermarket_analysis]
status: synthesized — structure inferred
---

# Undergraduate Sophomore (premium) — beyond the chart

*(Module list inferred from the older outline and third-party listings;
confirm on scrape.)*

| Module | Key takeaways | Concept |
|---|---|---|
| Market sentiment & COT report | Positioning extremes as contrarian signals | [[concept_market_sentiment]] |
| Trading the news | Directional vs non-directional approaches; spreads and slippage at release | [[concept_news_trading]] |
| Carry trade | Earn the rate differential; crash risk in risk-off | [[concept_carry_trade]] |
| U.S. Dollar Index | The USD as the common leg of the majors | [[concept_intermarket_analysis]] |
| Intermarket correlations & using equities | Bonds, stocks, commodities, and their FX links | [[concept_intermarket_analysis]] |


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/09-undergraduate-junior.md ===== -->

---
id: course_babypips_junior
type: course
title: "BabyPips Course 9 — Undergraduate Junior: trading plan & trader type"
partition: 04_babypips-school-of-pipsology
layer: L7
part_of: [course_babypips_school_of_pipsology]
covers: [concept_trading_plan, concept_trading_journal_review, concept_trading_psychology]
status: synthesized — structure inferred
---

# Undergraduate Junior (premium) — build the plan

- **Which type of trader are you?** Match holding period and style
  (scalper, day, swing, position) to personality, schedule, and capital.
  Schwager's wizards stress *fit* ([[concept_trading_psychology]]).
- **Develop a trading plan:** markets, setups, entry/exit, risk, routine
  ([[concept_trading_plan]]).
- **Keep a journal** and review it ([[concept_trading_journal_review]]).


<!-- ===== FILE: trading-intelligence/04_babypips-school-of-pipsology/courses/10-undergraduate-senior.md ===== -->

---
id: course_babypips_senior
type: course
title: "BabyPips Course 10 — Undergraduate Senior: risk management"
partition: 04_babypips-school-of-pipsology
layer: L6
part_of: [course_babypips_school_of_pipsology]
covers: [concept_risk_of_ruin_drawdown, concept_leverage_margin, concept_position_sizing, concept_trade_management, concept_correlation_portfolio_risk, concept_trading_psychology, concept_prop_firm_risk_rules]
sources:
  - {title: "Undergraduate - Senior — School of Pipsology", url: "https://www.babypips.com/learn/forex/undergraduate-senior", tier: T2}
  - {title: "BabyPips — The Risk Management Plan Most Prop Traders Are Missing", url: "https://www.babypips.com/learn/forex/risk-management-plan-prop-traders", tier: T2}
status: synthesized
---

# Undergraduate Senior (premium) — risk

The course warns that **most new traders lose all their money**, and frames
risk as the antidote.

| Module | Key takeaways | Concept |
|---|---|---|
| Risk management | **Drawdown math** (losses need larger gains to recover); risk budgets per trade, per idea, per day; circuit breakers | [[concept_risk_of_ruin_drawdown]] |
| Trading with leverage | Effective vs maximum leverage | [[concept_leverage_margin]] |
| Position sizing | `(Account × Risk%) ÷ (Stop × pip value)`, applied consistently | [[concept_position_sizing]] |
| Stop-loss placement | Structural, volatility, time, and percentage stops | [[concept_trade_management]] |
| Scaling in and out | Adding to winners vs averaging losers | [[concept_trade_management]] |
| Currency correlations | Correlated positions compound risk invisibly | [[concept_correlation_portfolio_risk]] |
| Psychology (revenge trading) | No size-up to win it back; stop after N losses in a day | [[concept_trading_psychology]] |

BabyPips has extended this with prop-firm risk guides
([[concept_prop_firm_risk_rules]]).
