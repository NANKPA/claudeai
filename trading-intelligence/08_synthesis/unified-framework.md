---
id: synthesis_unified_framework
type: synthesis
title: The Unified Trading Intelligence Framework (analysis → execution)
partition: 08_synthesis
layer: L8
related: [framework_ontology, synthesis_idea_lineage, synthesis_consensus_conflicts, synthesis_pre_trade_checklist, channel_chart_fanatics, course_babypips_school_of_pipsology]
uses: [concept_edge, concept_market_regimes, concept_auction_market_theory, concept_liquidity, concept_market_structure, concept_trade_execution, concept_position_sizing, concept_trading_psychology, concept_overfitting_validation]
status: synthesized
---

# The Unified Trading Intelligence Framework

All the sources in this knowledge base (Chart Fanatics guests, BabyPips, the
top-100 books, the legends, and the mathematics) collapse into **one
pipeline**. Each stage has a question, the tools that answer it, the sources
that teach it best, and the failure it prevents.

```
 ┌─────────────── ANALYSIS ───────────────┐   ┌────────────── EXECUTION ──────────────┐
 L0 Edge? → L1 Mechanics → L2 Context → L3 Lens → L4 Setup → L5 Trigger → L6 Size → L7 Discipline → L8 Review
     ▲                                                                                              │
     └──────────────────────────────── feedback: is the edge still real? ◄──────────────────────────┘
```

## Stage by stage

### L0 — Is there an edge at all?
- **Question:** Why should this pattern pay? Who is on the other side, and why?
- **Tools:** expectancy algebra, fat-tail awareness, adaptive-markets mindset.
- **Best sources:** Thorp (*Beat the Dealer*, *A Man for All Markets*);
  Taleb; Lo (*Adaptive Markets*); math track A.
- **Prevents:** trading noise; believing marketing win rates.
- Notes: [[concept_edge]], [[concept_probability_fat_tails]], [[concept_random_walk_efficient_markets]].

### L1 — How do orders become prices here?
- **Question:** What is the instrument's microstructure (central book? real
  volume? session liquidity?)
- **Tools:** order book, auction logic, liquidity pools, order flow.
- **Best sources:** Harris; Steidlmayer/Dalton; Wyckoff tape reading;
  Fabio Valentini / Yush (CF); BabyPips Preschool–Kindergarten for FX basics.
- **Prevents:** misreading why levels hold or break.
- Notes: [[concept_market_microstructure]], [[concept_auction_market_theory]], [[concept_liquidity]], [[concept_order_flow]].

### L2 — What state is the market in?
- **Question:** Balanced or imbalanced? Trending or ranging? High or low
  vol? Which session?
- **Tools:** AMT day types, structure (HH/HL), ATR percentile, EMA alignment,
  session clock.
- **Best sources:** Dalton; Dow/Rhea; Al Brooks; TG Capital's EMA-stack gate;
  Fabio's two models.
- **Prevents:** running a mean-reversion setup in a trend (and vice versa),
  the most common cause of a strategy "stopping working".
- Notes: [[concept_market_regimes]], [[concept_market_structure]], [[concept_trading_sessions_killzones]], [[concept_multi_timeframe_analysis]].

### L3 — Which lens reads it best?
Pick **one primary lens** and at most two confirmations:

| Lens | Best for | Teachers |
|---|---|---|
| AMT / volume profile / order flow | Futures intraday | Steidlmayer, Dalton, Fabio, Forrest Knight, Yush |
| SMC / ICT (liquidity, FVG, OB, AMD) | FX and index futures intraday | ICT; CF guests Candace Lau, Tanja, Mayne, Kane, TG Capital, Marco |
| Classical TA / price action | Swing, any market | Edwards & Magee, Brandt, Brooks, Nison, BabyPips Elementary–High School |
| Growth-stock momentum | US equities swing/position | Livermore → Darvas → O'Neil → Minervini → Kell, Bonde, Ang |
| Trend following (systematic) | Diversified futures | Donchian, Dennis, Seykota, Covel, Carver |
| Macro / fundamentals / sentiment | FX, rates, multi-week | Soros, Druckenmiller, Dalio, BabyPips Freshman–Sophomore |

### L4 — What is the exact setup?
The recurring archetypes across all sources (see `synthesis_consensus_conflicts`):
1. **Liquidity sweep → reversal** ([[concept_liquidity_sweep_reversal]])
2. **Trend pullback to value/structure** ([[concept_trend_following]], [[concept_premium_discount_ote]])
3. **Compression → breakout with acceptance** ([[concept_breakout_trading]])
4. **Reversion to fair value** (POC/VWAP/fair price) ([[concept_mean_reversion]])
5. **Catalyst repricing** ([[concept_episodic_pivot]], [[concept_news_trading]])

### L5 — When exactly, and how?
- **Direction → Location → Aggression** (Fabio): context, level, trigger.
- Confirmation styles: candle close (Forrest Knight), structure shift
  (Candace Lau), breaker (Mayne), order-flow absorption (Yush), FVG retrace
  (TG Capital).
- Account for costs and slippage. For size, respect impact (Almgren–Chriss,
  square-root law).
- Notes: [[concept_trade_execution]], [[concept_trade_management]], [[concept_optimal_execution_market_impact]].

### L6 — How much?
- Fixed-fractional 0.25–1% per trade (Fabio ~0.25%); volatility-normalised
  units (Turtles); fractional Kelly as the theoretical ceiling.
- Daily, weekly, and drawdown circuit breakers (BabyPips Senior, prop rules,
  JJ Simon's 3-loss stop).
- Notes: [[concept_position_sizing]], [[concept_kelly_criterion_optimal_f]], [[concept_risk_of_ruin_drawdown]], [[concept_correlation_portfolio_risk]].

### L7 — Will I follow it?
- Think in probabilities (Douglas); lose well (Hougaard); plan for 20 losses
  in a row (Silfrain); stages you can't skip (Umar Ashraf).
- Notes: [[concept_trading_psychology]], [[concept_probabilistic_thinking]], [[concept_trading_plan]].

### L8 — Is it still working?
- Journal per setup, regime, and session; compare live vs backtest; deflate
  Sharpe for the number of trials; walk-forward.
- Notes: [[concept_trading_journal_review]], [[concept_backtesting]], [[concept_overfitting_validation]], [[concept_performance_metrics]].

## The one-sentence version

> **Trade a structurally motivated edge (L0–L1), only in the regime where it
> exists (L2), through one lens (L3) and one setup (L4), triggered at a
> location with confirmation (L5), sized to survive the worst streak (L6),
> executed without hesitation (L7), and audited relentlessly (L8).**
