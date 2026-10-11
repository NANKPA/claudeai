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
