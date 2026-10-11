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
