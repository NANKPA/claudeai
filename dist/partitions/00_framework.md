# Partition 00_framework


<!-- ===== FILE: trading-intelligence/00_framework/learning-path.md ===== -->

---
id: framework_learning_path
type: framework
title: Learning Path through the partitions
partition: 00_framework
layer: L0
related: [framework_ontology, course_babypips_school_of_pipsology, channel_chart_fanatics, framework_math_foundations, synthesis_unified_framework]
status: synthesized
---

# Learning Path

A sequenced route through the knowledge base. Each phase pairs a **retail
foundation** (BabyPips), a **professional practice** layer (Chart Fanatics
guests), the **canonical books**, and the **mathematics**, so understanding
builds from the ground up.

| Phase | Goal | BabyPips | Concepts (07) | Practitioners (01/03) | Books (05) | Math (06) |
|---|---|---|---|---|---|---|
| **1. Mechanics** (L1) | Know what you are trading | Preschool, Kindergarten | microstructure, leverage/margin, sessions | — | *Trading and Exchanges* | Track A basics: expectancy, variance |
| **2. Reading charts** (L2–L3) | Structure, levels, candles | Elementary, Middle School | market structure, S/R, candlesticks, chart patterns, MAs | Tori Trades, Marci Silfrain | Murphy; Edwards & Magee; Nison | Track C: autocorrelation, volatility |
| **3. Why levels work** (L1–L3) | Auction, liquidity, order flow | Summer School (divergence) | AMT, volume profile, liquidity, order flow, Wyckoff, SMC | Fabio Valentini, Forrest Knight, Yush, Candace Lau, Marco | *Markets and Market Logic*; *Mind Over Markets*; *Studies in Tape Reading*; Weis | Track D: microstructure, impact |
| **4. Setups** (L4) | One playbook, written precisely | High School | sweep reversal, trend pullback, breakout, mean reversion, EP | TG Capital, Mayne, Tanja, JJ Simon, Bonde | Raschke & Connors; Brooks; O'Neil; Minervini | — |
| **5. Execution** (L5) | Trigger, management, costs | High School (MTF) | trade execution, trade management, optimal execution | Fabio (Direction-Location-Aggression), Kane (breakeven) | Harris; Carter | Almgren–Chriss, square-root law |
| **6. Risk** (L6) | Survive and compound | Senior | position sizing, R, expectancy, Kelly, ruin, correlation, prop rules | Silfrain ("20 in a row"), JJ Simon (3-loss stop) | Tharp; Vince; Thorp; *Way of the Turtle* | Track E |
| **7. Psychology** (L7) | Execute the plan | Junior, Senior | psychology, probabilistic thinking, trading plan | Umar Ashraf (5 stages) | Douglas; Hougaard; Steenbarger; Kahneman | Bayesian updating |
| **8. Validation** (L8) | Prove and monitor the edge | — | journal, backtesting, overfitting, metrics | Gianluca Bruni (statistical models) | Aronson; López de Prado; Carver | Track F |
| **9. Macro & context** (L3) | Bigger picture | Freshman, Sophomore | macro, intermarket, sentiment, news, carry, reflexivity | Andy Krieger | Soros; Dalio; Murphy *Intermarket*; Marks | — |

**Capstone:** write your own playbook using `08_synthesis/pre-trade-checklist.md`,
backtest ≥ 100 instances, then forward-test at minimum size.


<!-- ===== FILE: trading-intelligence/00_framework/note-schema.md ===== -->

---
id: framework_note_schema
type: framework
title: Note & Registry Schema
partition: 00_framework
layer: L0
related: [framework_ontology]
---

# Note & Registry Schema

The knowledge graph is compiled from two kinds of files by
`tools/build_graph.py`. Keep to this schema so new material (including scraper
output) slots into the graph automatically.

## 1. Markdown notes (YAML frontmatter)

```yaml
---
id: concept_liquidity          # REQUIRED. lowercase [a-z0-9_]. Globally unique.
type: concept                  # REQUIRED. see ontology node types
title: Liquidity               # REQUIRED. human label
partition: 07_concepts         # folder it lives in
layer: L1                      # L0..L8 (ontology layer)
aliases: [liquidity pool, resting orders]
tags: [ict, smc, order-flow]
# ---- relations: any key below is a list of target ids ----
related: [concept_market_structure]
derived_from: [concept_wyckoff_method]
influenced_by: []
uses: []
covers: []
teaches: []
featured_in: []
part_of: []
contrasts_with: []
validates: []
challenges: []
# ---- provenance ----
sources:
  - {title: "Chart Fanatics liquidity playbook", url: "https://www.chartfanatics.com/playbook/liquidity-playbook", tier: T2}
status: synthesized            # synthesized | scraped | pending-scrape | verified
---
```

Inline wikilinks such as `[[concept_fair_value_gap]]` in the body also become
`related` edges.

## 2. YAML registries

Registries hold many small entities (books, people, podcasts, media). Each
entry uses the same keys as frontmatter (`id`, `type`, `title`, relation
lists, `sources`) plus type-specific fields:

| Registry | Extra fields |
|---|---|
| `people.yaml` | `name`, `role`, `era`, `known_for` |
| `books.yaml`, `math-books.yaml` | `author_ids`, `year`, `category`, `key_idea`, `rank` |
| `podcasts.yaml` | `hosts`, `focus`, `url`, `rss` (when known) |
| `landmark-media.yaml`, `lectures.yaml` | `speaker_ids`, `year`, `format`, `url`, `verification` |

## 3. Scraper output

Scrapers write markdown into each partition's `raw/` folder with frontmatter:

```yaml
---
id: media_cf_<youtube_id>
type: media
title: "<video title>"
partition: 01_chart-fanatics
source_url: https://www.youtube.com/watch?v=<id>
captured_at: 2026-10-11T00:00:00Z
author: Chart Fanatics
featured_in: [channel_chart_fanatics]
status: scraped
view_count: 123456
upload_date: 20250101
---
<transcript text>
```

`raw/` is git-ignored by default (full third-party text stays on your machine)
but is still read by `build_graph.py` and `bundle_for_claude.py` locally.

## ID prefixes

`concept_` · `strategy_` · `person_` · `book_` · `mathbook_` · `podcast_` ·
`media_` · `course_` · `lesson_` · `channel_` · `formula_` · `framework_` ·
`synthesis_` · `layer_`


<!-- ===== FILE: trading-intelligence/00_framework/ontology.md ===== -->

---
id: framework_ontology
type: framework
title: Trading Intelligence Ontology (the 9-layer stack)
partition: 00_framework
layer: L0
related: [framework_note_schema, framework_source_tiers, framework_learning_path, synthesis_unified_framework]
---

# Trading Intelligence Ontology

Every note in this knowledge base sits on one **layer** of a single stack that
runs from *why markets move* to *how a trade is executed and reviewed*. The
layers are ordered: each one depends on the ones beneath it. A strategy (L4)
without a sizing rule (L6) is incomplete. An entry trigger (L5) without
context (L2) is a coin flip.

| Layer | Name | Question it answers | Example concept ids |
|---|---|---|---|
| **L0** | Mathematical foundations | What is randomness, edge, and growth? | `concept_probability_fat_tails`, `concept_stochastic_processes`, `concept_time_series_statistics` |
| **L1** | Market mechanics & microstructure | How do orders become prices? | `concept_market_microstructure`, `concept_auction_market_theory`, `concept_liquidity` |
| **L2** | Market structure & context | What state is the market in right now? | `concept_market_structure`, `concept_market_regimes`, `concept_trading_sessions_killzones`, `concept_multi_timeframe_analysis` |
| **L3** | Analysis methods | Which lens reads that state? | `concept_smart_money_concepts`, `concept_volume_profile`, `concept_order_flow`, `concept_wyckoff_method`, `concept_fundamental_macro_analysis` |
| **L4** | Setups & strategy archetypes | What repeatable pattern do I trade? | `concept_liquidity_sweep_reversal`, `concept_trend_following`, `concept_mean_reversion`, `concept_breakout_trading` |
| **L5** | Execution | Exactly when and how do I get in and out? | `concept_trade_execution`, `concept_trade_management`, `concept_optimal_execution_market_impact` |
| **L6** | Risk & money management | How much do I risk, and can I survive? | `concept_position_sizing`, `concept_expectancy`, `concept_kelly_criterion_optimal_f`, `concept_risk_of_ruin_drawdown` |
| **L7** | Psychology & discipline | Will I actually follow the plan? | `concept_trading_psychology`, `concept_probabilistic_thinking`, `concept_trading_plan` |
| **L8** | Review & edge validation | Is the edge real, and is it decaying? | `concept_backtesting`, `concept_overfitting_validation`, `concept_performance_metrics`, `concept_trading_journal_review` |

## Node types

| `type` | What it is | Lives in |
|---|---|---|
| `concept` | An idea, mechanism, or principle (atomic, reusable) | `07_concepts/` |
| `strategy` | A named, rule-based playbook from a specific trader | `01_chart-fanatics/strategies/` |
| `person` | Trader, author, researcher, or host | `03_legends-authorities/people.yaml` |
| `book` | Book (trading or mathematics) | `05_books-top-100/books.yaml`, `06_mathematics-foundations/math-books.yaml` |
| `podcast` | A show (feed) | `02_podcasts-interviews/podcasts.yaml` |
| `media` | A specific episode, talk, lecture, documentary, or video | `02_podcasts-interviews/landmark-media.yaml`, `06_mathematics-foundations/lectures.yaml` |
| `course` | A structured curriculum or course module | `04_babypips-school-of-pipsology/` |
| `channel` | A YouTube channel or education brand | `01_chart-fanatics/` |
| `formula` | A quantitative rule with an equation | `06_mathematics-foundations/core-formulas.md` |
| `framework` / `synthesis` | Meta notes that organise everything else | `00_framework/`, `08_synthesis/` |

## Edge types (relations)

Relations are directional (`source → target`), stored in frontmatter and in
the YAML registries, and preserved in the knowledge graph.

| Relation | Meaning | Example |
|---|---|---|
| `related` | Conceptually adjacent; no lineage implied | liquidity ↔ market structure |
| `derived_from` | The idea descends from an earlier idea or person | ICT AMD → Wyckoff method |
| `influenced_by` | Person-to-person intellectual lineage | Minervini → O'Neil → Livermore |
| `uses` | A strategy or method relies on a concept or tool | Fabio's model → volume profile, CVD |
| `teaches` / `authored` | A person or source teaches or wrote something | Mark Douglas → *Trading in the Zone* |
| `covers` | A book, course, or media item covers a concept | BabyPips Grade 8 → pivot points |
| `featured_in` | A person appears in a channel or episode | Fabio Valentini → Chart Fanatics |
| `hosted_by` | A show is hosted by a person | Chart Fanatics → Riz Iqbal |
| `part_of` | Membership in a larger unit | Grade 3 → Elementary course |
| `contrasts_with` | A real disagreement between ideas | trend following ↔ mean reversion |
| `validates` / `challenges` | Evidence for or against a claim | independent backtest → TG Capital claim |

## Design rules

1. **Atomic concepts.** One idea per concept note. Strategies *compose*
   concepts; they never redefine them.
2. **Lineage over lists.** Every concept states where it came from
   (`derived_from`), so the graph can answer "where did this idea originate?"
3. **Evidence is tiered.** Every factual claim carries a source tier (see
   `framework_source_tiers`). Marketing claims stay labelled as marketing.
4. **Analysis → Execution is the spine.** The synthesis in
   `08_synthesis/unified-framework.md` walks L0 → L8 as one pipeline.


<!-- ===== FILE: trading-intelligence/00_framework/source-tiers.md ===== -->

---
id: framework_source_tiers
type: framework
title: Source Quality Tiers
partition: 00_framework
layer: L8
related: [framework_ontology, concept_overfitting_validation]
---

# Source Quality Tiers

Trading content is full of survivorship bias and marketing. Every claim in this
knowledge base is tagged with the tier of its best source, and Claude should
weigh claims by tier when answering.

| Tier | Definition | Examples | How to use |
|---|---|---|---|
| **T1 — Primary / peer-reviewed / audited** | Original books, academic papers, exchange documentation, audited competition results | Kelly (1956), Almgren & Chriss (2000), Schwager's interviews, Robbins World Cup published results | Treat as ground truth for *what was said or proven*. |
| **T2 — First-party practitioner material** | The trader's own video, course, or playbook; the channel's own strategy page | Chart Fanatics episode or strategy page, Chart Academy masterclass, BabyPips lessons | Accurate about *the method*. Performance claims are still self-reported. |
| **T3 — Third-party summaries** | Journaling-platform playbooks, transcript sites, blog breakdowns, AI summaries | TradeZella playbooks, transcript aggregators, PickMyTrade blog posts | Useful for structure. Verify the rules against T2 before trading them. |
| **T4 — Marketing & social claims** | Titles, thumbnails, tweets, "90% win rate" claims | Video titles, X or TikTok promos | **Never** treat as evidence. Record it only as "claimed". |
| **T5 — Synthesized** | Claude's own synthesis from established domain knowledge | Concept notes, lineage map, unified framework | A starting map. Upgrade it by attaching T1/T2 sources as scrapes land. |

## Rules of evidence

- **Win-rate claims require a sample size and an R:R.** A 90% win rate at
  1:20 R:R is mathematically implausible for a discretionary system. An
  independent re-test of one such claim found about a 20% win rate, but with
  large winners (see `strategy_tg_capital_trident`).
- **Self-reported P&L is T4** unless it is audited or competition-verified.
- **Backtests are evidence of a hypothesis, not of an edge,** until they are
  checked out-of-sample (see `concept_overfitting_validation`).
- When sources conflict, record both and link them with `contrasts_with`.
