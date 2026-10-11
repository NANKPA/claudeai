---
id: synthesis_idea_lineage
type: synthesis
title: Idea Lineage Map — where every modern trading idea comes from
partition: 08_synthesis
layer: L8
related: [synthesis_unified_framework, concept_wyckoff_method, concept_dow_theory, concept_auction_market_theory, concept_smart_money_concepts, concept_kelly_criterion_optimal_f, concept_trend_following, concept_growth_momentum_canslim]
status: synthesized
---

# Idea Lineage Map

**Most "new" strategies on YouTube are re-expressions of 6–8 ideas that are
50–120 years old.** Knowing the lineage tells you (a) the original, fuller
source to study and (b) which claims are genuinely new.

```mermaid
flowchart LR
  %% ROOTS
  DOW["Dow Theory<br/>c.1900"]:::root
  WYK["Wyckoff<br/>1910–1930s"]:::root
  LIV["Livermore<br/>1900–1940"]:::root
  BACH["Bachelier<br/>1900"]:::root
  KELLY["Kelly / Shannon<br/>1948–1956"]:::root
  CBOT["Steidlmayer<br/>Market Profile 1980s"]:::root
  ELL["Elliott + Fibonacci<br/>1938"]:::root
  KT["Kahneman & Tversky<br/>1979"]:::root

  %% STRUCTURE / SMC branch
  DOW --> MS["Market structure<br/>HH/HL, BOS, CHoCH"]
  DOW --> SMT["SMT divergence<br/>(confirmation)"]
  DOW --> PH["3 phases"] --> WYK
  WYK --> SPRING["Spring / Upthrust"] --> LIQ["Liquidity sweep<br/>stop hunt"]
  WYK --> CO["Composite operator"] --> SMC["ICT / SMC<br/>2010s"]
  RAS["Raschke & Connors<br/>Turtle Soup 1995"] --> LIQ
  LIQ --> SMC
  ELL --> OTE["OTE 62–79%"] --> SMC
  SMC --> AMD["AMD / Power of 3"]
  SMC --> FVG["FVG / IFVG / OB"]
  SMC --> CF1["CF: Candace Lau, Tanja, Mayne,<br/>Kane, TG Capital, Marco"]:::cf

  %% AUCTION branch
  WYK --> TAPE["Tape reading<br/>(Wyckoff, Neill)"] --> OF["Order flow<br/>footprint, CVD"]
  CBOT --> DAL["Dalton<br/>Mind Over Markets 1990"] --> AMT["Auction Market Theory<br/>volume profile"]
  AMT --> CF2["CF: Fabio Valentini, Andrea Cimitan,<br/>Rajan Dhall, Forrest Knight"]:::cf
  OF --> CF2
  OF --> CF3["CF: Yush (trapped traders)"]:::cf
  AMT --> FP["Fair value reversion"] --> CF4["CF: JJ Simon fair pricing"]:::cf

  %% MOMENTUM branch
  LIV --> LOEB["Loeb 1935"] --> DAR["Darvas boxes 1960"]
  LIV --> ONEIL["O'Neil CANSLIM 1988"]
  LOEB --> ONEIL
  ONEIL --> MIN["Minervini SEPA/VCP"] --> CF5["Kell, Ang, Bonde (EP)"]:::cf

  %% TREND FOLLOWING branch
  LIV --> DON["Donchian channels 1960s"] --> TUR["Turtles 1983"] --> CTA["CTAs, Covel, Carver"]
  DOW --> DON

  %% MATH branch
  BACH --> EMH["Random walk / EMH 1970"]
  BACH --> MAN["Mandelbrot fat tails 1963"] --> TAL["Taleb"]
  KELLY --> THORP["Thorp 1962–"] --> VINCE["Vince optimal f 1992"] --> THARP["Tharp position sizing"]
  THARP --> PROP["Prop-firm risk rules"]
  KYLE["Kyle 1985 / microstructure"] --> AC["Almgren–Chriss 2000"] --> SQRT["Square-root impact law"]

  %% PSYCH branch
  KT --> DOUG["Douglas 1990/2000"] --> HOUG["Hougaard 2022"]
  KT --> DUKE["Annie Duke 2018"]

  classDef root fill:#fde68a,stroke:#92400e,color:#111;
  classDef cf fill:#bfdbfe,stroke:#1e3a8a,color:#111;
```

## The eight root ideas

| Root | Original source | Modern descendants (this KB) |
|---|---|---|
| **Trends are defined by swings and need confirmation** | Dow (WSJ, c.1900); Rhea 1932 | Market structure, BOS/CHoCH, SMT divergence, trend following |
| **Large operators accumulate, manipulate, and distribute** | Wyckoff (1910–1930s) | Liquidity sweeps, AMD/Power of 3, "smart money", order blocks |
| **The market is a two-sided auction seeking value** | Steidlmayer (CBOT, 1980s); Dalton 1990 | Volume profile, POC reversion, Fabio's AMT, fair-pricing theory |
| **Read aggression on the tape** | Wyckoff 1910; Neill 1931 | Footprint, delta/CVD, absorption, trapped traders |
| **Buy strength at pivots; cut losses fast; pyramid winners** | Livermore; Loeb; Darvas | CANSLIM, SEPA/VCP, episodic pivots, Donchian, Turtles |
| **Price changes are random-ish, with fat tails** | Bachelier 1900; Mandelbrot 1963 | EMH debate, adaptive markets, Taleb, risk of ruin |
| **Bet in proportion to edge to maximise growth** | Kelly 1956; Thorp | Optimal f, position sizing, R-multiples, prop-firm risk rules |
| **Humans misjudge probabilities and losses** | Kahneman & Tversky 1979 | Douglas, Steenbarger, Duke, Tendler, Hougaard |

## What is genuinely newer

- **Time-of-day precision** (kill zones, 10 AM 4H anchor). Larry Williams and
  Toby Crabel pioneered it; ICT systematised the vocabulary.
- **Cheap order-flow tooling** (footprints, heatmaps) democratised what pit
  traders read by ear.
- **Prop-firm economics** reshaped risk rules (trailing drawdowns,
  consistency rules) and created a large population of NQ/ES scalpers.
  That is most of the Chart Fanatics guest roster.
- **Formal backtest-overfitting statistics** (deflated Sharpe, PBO, 2014+).
