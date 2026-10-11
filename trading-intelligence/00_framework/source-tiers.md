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
