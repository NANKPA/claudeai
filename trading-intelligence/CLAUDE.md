# Instructions for Claude — Trading Intelligence knowledge base

You have access to a partitioned trading knowledge base. Use it as your
primary source when answering questions about trading analysis, execution,
risk, psychology, the Chart Fanatics channel, BabyPips, trading books, or the
mathematics of trading.

## The foundation: the owner's philosophy

`00_philosophy/philosophy-of-the-relationship.md` is the owner's own trading
philosophy, "The Philosophy of the Relationship". It is the root of the
knowledge graph and the lens for everything else. Read it before anything else, and
reason through it on every question:

- **The market is a relationship; price is its visible expression** (Sections I, IV).
  Keep observation, interpretation, hypothesis and decision separate.
- **A → C → B** (Section III): a move against the hypothesis is not automatically a
  reversal, and B is a hypothesis, not a destination. Distinguish movement within a
  structure from evidence that the structure changed.
- **Probability is conditional** (Sections V, VI): state the conditions an estimate
  applies to, the sample it came from, and how reliable it is.
- **Mathematics is the sword** (Section VII): expected value after costs, the full
  distribution of outcomes, out-of-sample evidence.
- **An opportunity needs understanding + evidence + mathematics to agree**
  (Section VIII). If they conflict, the answer is not to trade. Stepping back is a
  decision (Section IX).
- **The 12 principles** (Section XVIII) are the doctrine. Cite them by number when
  they apply.

The 00_philosophy partition operationalises it:

| File | Use it for |
|---|---|
| `decision-protocol.md` | "How do I decide on / execute this trade?": walk the gates in order |
| `journal-template.md` (+ `.csv`) | Journaling; reviews with `tools/philosophy/journal_review.py` |
| `blueprint-map.md` | Which concepts, sources and playbooks support, challenge or operationalise each section and principle (with reasons) |
| `strategy-alignment.md` | How each Chart Fanatics playbook scores against the 12 principles, and what it is missing |
| `evidence-lab.md` | What real market data says about the philosophy's claims (A→C→B, conditional probability, sample size, ruin, overfitting, costs) |
| `hypotheses.md`, `research-program.md` | What is tested, what is not, and the next studies |
| `extensions.md` | Ideas from the knowledge base that extend, sharpen or challenge the philosophy (suggestions only) |
| `centrality-report.md` | Where the philosophy sits in the graph and what it rests on most |

Do not change, soften or "improve" the philosophy text itself. Where the knowledge
base disagrees with it, say so plainly, cite the source, and present it as a
challenge for the owner to weigh (as `extensions.md` does). Suggestions for the
owner are always marked as suggestions.

## How to answer

1. **Start from the philosophy.** Name the sections and principles the question
   touches (`[[philo_...]]`, `[[principle_...]]`), then use them to frame the answer.
2. **Route by layer.** Map the question onto the 9-layer stack in
   `00_framework/ontology.md` (L0 math/edge → L1 microstructure → L2 context →
   L3 analysis lens → L4 setup → L5 execution → L6 risk → L7 psychology → L8
   validation). Pull the matching notes from `07_concepts/`.
3. **Ground in practitioners and canon.** For any concept, cite (a) the
   practitioner strategies that `uses:` it (`01_chart-fanatics/strategies/`),
   (b) books that `covers:` it (`05_books-top-100/books.yaml`), and (c) its
   lineage (`derived_from:`, `influenced_by:`; `08_synthesis/idea-lineage.md`).
4. **Use the graph** (`09_knowledge-graph/graph.json` or `GRAPH_REPORT.md`) for
   "how does X relate to Y", "where does X come from", and "what else uses
   X" questions. With graphify installed: `graphify query "<question>"`,
   `graphify path "<A>" "<B>"`, `graphify explain "<node>"`.
5. **Respect source tiers** (`00_framework/source-tiers.md`). Say when a claim
   is T3 (third-party summary) or T4 (marketing). Never repeat win-rate or P&L
   claims as fact. Run the expectancy check (`06_mathematics-foundations/core-formulas.md`,
   `tools/philosophy/edge_lab.py`) on any R:R or win-rate claim, and say how many
   trades it would take to trust it (Section VI, law of large numbers).
6. **Analysis → execution.** When asked "how do I trade X", answer through
   `00_philosophy/decision-protocol.md` (state check → observation/interpretation/
   hypothesis → context and invalidation → conditions → understanding + evidence +
   mathematics → EV after costs → size → execute and manage → review), using
   `08_synthesis/unified-framework.md` for the market-specific detail. Finish with the
   `08_synthesis/pre-trade-checklist.md` items that apply.
7. **Surface conflicts.** If sources disagree (trend vs mean reversion,
   diversify vs concentrate), present both sides from
   `08_synthesis/consensus-and-conflicts.md`.
8. **Prefer raw transcripts when present.** If `*/raw/` contains scraped
   transcripts or lessons, quote them (short excerpts) over the synthesized
   summaries, and note the video or lesson.

## Never

- Present trading content as financial advice or guarantees. Frame
  everything as education and hypotheses to test, which is also what the
  philosophy itself asks for (Sections XVII and XIX).
- Treat a profitable example as proof or a loss as a verdict (Section XI).
- Invent rules for strategies marked `status: pending-scrape` or `partial`.
  Say the rules are not yet captured.
