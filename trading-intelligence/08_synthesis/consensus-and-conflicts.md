---
id: synthesis_consensus_conflicts
type: synthesis
title: Consensus & Conflicts across sources
partition: 08_synthesis
layer: L8
related: [synthesis_unified_framework, synthesis_idea_lineage]
status: synthesized
---

# Where the sources agree, and where they genuinely disagree

## Near-universal consensus (every partition says it)

| Principle | Voices |
|---|---|
| **Cut losses short; risk small and fixed per trade** | Livermore, Loeb, O'Neil (7–8%), Turtles (1%/N), Hite (1%), Fabio (~0.25%), BabyPips Senior, Tharp |
| **Location before trigger: trade at meaningful levels only** | Dalton (value edges), ICT (PD arrays), Brandt (pattern boundaries), Forrest Knight (auction levels), BabyPips G1 |
| **Context/regime decides which setup is valid** | Dalton (balance/imbalance), Fabio (two models), TG Capital (EMA stack gate), Clement Ang (when to be aggressive), Weinstein (stages) |
| **Losing streaks are normal; think in distributions** | Douglas, Silfrain (20 in a row), Seykota, Thorp, Duke |
| **Preparation, backtesting and journaling outweigh live screen time** | Silfrain, Umar Ashraf, Steenbarger, Brandt's trade diary |
| **The big money is in a few big moves** | Livermore, trend followers, Minervini, TG Capital's 1:20 targets |

## Genuine conflicts (pick a side consciously)

| Tension | Side A | Side B | Resolution |
|---|---|---|---|
| **Diversify vs concentrate** | Trend followers, Dalio (15+ uncorrelated streams) | Druckenmiller, Soros ("bet the ranch" on conviction) | Concentration requires skill at *timing conviction*; default to diversification until your journal proves that skill |
| **Trend vs mean reversion** | Turtles, Minervini, momentum | AMT POC reversion, JJ Simon, range traders | Both are right in different regimes. The regime filter is the real edge ([[concept_market_regimes]]) |
| **Indicators vs naked charts** | BabyPips Elementary–Middle School, Wilder, Bollinger | Tori Trades, Fabio ("no lagging oscillators"), Brooks | Indicators are summaries of price/volume. Use them as filters and gates (TG's EMA stack), not as triggers |
| **Anticipation vs confirmation entries** | Limit orders at zones (Yush: early entries, smaller size) | Wait for the signal candle close (Forrest Knight), MSS (Candace Lau) | Trade-off between price and win rate; measure both in the journal |
| **Discretionary vs systematic** | CF guests, Brandt, Brooks | Simons, Carver, López de Prado | Hybrid via meta-labeling: a discretionary setup plus a systematic filter and sizing ([[concept_machine_learning_finance]]) |
| **Markets are efficient vs exploitable** | Fama, Malkiel | Lo, Asness, every trader here | Adaptive markets: edges exist, decay, and must be re-validated |
| **Trade the news vs avoid it** | Tanja (AMD during news), JJ Simon (news resets fair price) | Prop-firm guidance (slippage, spreads) | Depends on execution infrastructure and rules |
| **High R:R vs high win rate** | TG Capital (1:20), trend followers (30–40% WR) | Scalpers (60–80% WR, <1R) | Only expectancy after costs matters ([[concept_expectancy]]) |

## Claims that do NOT survive scrutiny

| Claim | Problem | Note |
|---|---|---|
| "90% win rate at 1:20+ R:R" | Implies +17.9R per trade; an independent re-test found ~20% WR | `strategy_tg_capital_trident` |
| "Smart money is hunting *your* stop" | Stops are liquidity in aggregate; nobody targets an individual retail stop | [[concept_liquidity]] |
| "Fib levels are where price must turn" | Weak standalone evidence; useful as a location filter | [[concept_fibonacci]] |
| Self-reported payout totals ($1.2M–$1.8M+) | Unaudited, vary by source, prop-specific | `strategy_jj_simon_fair_pricing` |
