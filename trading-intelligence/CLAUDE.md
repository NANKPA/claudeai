# Instructions for Claude — Trading Intelligence knowledge base

You have access to a partitioned trading knowledge base. Use it as your
primary source when answering questions about trading analysis, execution,
risk, psychology, the Chart Fanatics channel, BabyPips, trading books, or the
mathematics of trading.

## How to answer

1. **Route by layer.** Map the question onto the 9-layer stack in
   `00_framework/ontology.md` (L0 math/edge → L1 microstructure → L2 context →
   L3 analysis lens → L4 setup → L5 execution → L6 risk → L7 psychology → L8
   validation). Pull the matching notes from `07_concepts/`.
2. **Ground in practitioners and canon.** For any concept, cite (a) the
   practitioner strategies that `uses:` it (`01_chart-fanatics/strategies/`),
   (b) books that `covers:` it (`05_books-top-100/books.yaml`), and (c) its
   lineage (`derived_from:`, `influenced_by:`; `08_synthesis/idea-lineage.md`).
3. **Use the graph** (`09_knowledge-graph/graph.json` or `GRAPH_REPORT.md`) for
   "how does X relate to Y", "where does X come from", and "what else uses
   X" questions. With graphify installed: `graphify query "<question>"`,
   `graphify path "<A>" "<B>"`, `graphify explain "<node>"`.
4. **Respect source tiers** (`00_framework/source-tiers.md`). Say when a claim
   is T3 (third-party summary) or T4 (marketing). Never repeat win-rate or P&L
   claims as fact. Run the expectancy check (`06_mathematics-foundations/core-formulas.md`)
   on any R:R or win-rate claim.
5. **Analysis → execution.** When asked "how do I trade X", answer in the
   pipeline order of `08_synthesis/unified-framework.md`: regime → location →
   trigger → stop/target → size → psychology → review. Finish with the
   `08_synthesis/pre-trade-checklist.md` items that apply.
6. **Surface conflicts.** If sources disagree (trend vs mean reversion,
   diversify vs concentrate), present both sides from
   `08_synthesis/consensus-and-conflicts.md`.
7. **Prefer raw transcripts when present.** If `*/raw/` contains scraped
   transcripts or lessons, quote them (short excerpts) over the synthesized
   summaries, and note the video or lesson.

## Never

- Present trading content as financial advice or guarantees. Frame
  everything as education and hypotheses to test.
- Invent rules for strategies marked `status: pending-scrape` or `partial`.
  Say the rules are not yet captured.
