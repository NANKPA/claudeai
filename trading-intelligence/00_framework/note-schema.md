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
