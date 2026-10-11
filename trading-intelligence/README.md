# Trading Intelligence — partitioned knowledge base

A structured, graph-linked knowledge base on **how markets work and how
trades are analysed and executed**. It combines the Chart Fanatics YouTube
channel, trading podcasts and landmark interviews, the legends of trading,
the BabyPips School of Pipsology, the top-100 trading books, and the
mathematics underneath analysis and execution. It is built to be loaded into
Claude (Projects, Claude Code, or the API) and mapped with
[graphify](https://graphify.com).

## Partitions

| # | Partition | What's inside | Status |
|---|---|---|---|
| 00 | [`00_framework/`](00_framework/) | Ontology (9-layer stack), note schema, source-quality tiers, learning path | complete |
| 01 | [`01_chart-fanatics/`](01_chart-fanatics/) | Channel profile, ecosystem, 21 guest strategies, video catalog seed | synthesized from search; **transcripts pending scrape** |
| 02 | [`02_podcasts-interviews/`](02_podcasts-interviews/) | 16 podcasts, landmark interviews/talks seed + discovery queries for a top-100 | seed; **ranking pending scrape** |
| 03 | [`03_legends-authorities/`](03_legends-authorities/) | ~135 curated people with influence lineage (plus auto-linked authors) | complete (v1) |
| 04 | [`04_babypips-school-of-pipsology/`](04_babypips-school-of-pipsology/) | 11-course map + concept summaries per course | structure confirmed; **lesson text pending scrape** |
| 05 | [`05_books-top-100/`](05_books-top-100/) | Ranked top-100 trading books, lineage links, 13 deep summaries | complete (v1) |
| 06 | [`06_mathematics-foundations/`](06_mathematics-foundations/) | ~45 math books/papers in 6 tracks, lectures seed, formula sheet | complete (v1) |
| 07 | [`07_concepts/`](07_concepts/) | 69 atomic concept notes across layers L0–L8: the graph's backbone | complete (v1) |
| 08 | [`08_synthesis/`](08_synthesis/) | Unified analysis→execution framework, idea-lineage map, consensus & conflicts, pre-trade checklist | complete (v1) |
| 09 | [`09_knowledge-graph/`](09_knowledge-graph/) | graphify output: `graph.html`, `graph.json`, `GRAPH_REPORT.md`, wiki | generated |

## Start here

1. `08_synthesis/unified-framework.md`: the whole system on one page.
2. `00_framework/ontology.md`: how everything is organised.
3. `09_knowledge-graph/explorer.html`: the interactive Trading Intelligence Map (stack, graph,
   lineage tracing). Hosted copy: https://claude.ai/artifact/87RR4yVQKDBFdQ9GpwheF3
4. `00_framework/learning-path.md`: what to study in what order.

## Using it with Claude

- **Claude Projects (claude.ai):** upload `dist/trading-intelligence-bundle.md`
  (built by `tools/bundle_for_claude.py`) as project knowledge, and paste
  `CLAUDE.md` into the project instructions.
- **Claude Code:** open this repo. `CLAUDE.md` tells Claude how to route
  questions through the partitions and the graph. With graphify installed,
  `/graphify query "..."` traverses `09_knowledge-graph/graph.json`.
- **API / RAG:** `09_knowledge-graph/graph.json` is GraphRAG-ready (nodes,
  edges, communities). `wiki/` has one article per community.

## Honesty about sources

Every note carries a source tier (T1 primary → T5 synthesized; see
`00_framework/source-tiers.md`). The build environment could not reach
YouTube, BabyPips, or podcast hosts, so the scraped layers (`raw/`) are
empty until the scrapers run on a machine with access. Nothing in `raw/` has
been fabricated.
