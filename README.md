# claudeai — Trading Intelligence

A partitioned, graph-linked trading knowledge base built for Claude.

- **`trading-intelligence/`**: the knowledge base: 9 partitions (framework, Chart Fanatics,
  podcasts and interviews, legends, BabyPips, top-100 books, mathematics, concepts, synthesis)
  plus the graphify knowledge graph in `09_knowledge-graph/`. Start with
  [`trading-intelligence/README.md`](trading-intelligence/README.md).
- **`tools/`**: the build and scraping toolchain:
  - `render_registries.py`: YAML registries → markdown tables
  - `build_graph.py`: notes + registries → graphify (Leiden communities, report, HTML, wiki)
  - `build_explorer.py`: the interactive Trading Intelligence Map (`explorer.html`)
  - `bundle_for_claude.py`: one-file bundle + per-partition bundles for Claude Projects (`dist/`)
  - `scrapers/`: Chart Fanatics channel + transcripts + written playbooks, top-100 video search, podcast RSS,
    BabyPips course crawler, Open Library book QA
  - `run_pipeline.sh [--scrape]`: run everything end to end

```bash
pip install -r tools/requirements.txt
./tools/run_pipeline.sh            # rebuild tables, graph, explorer, Claude bundle
./tools/run_pipeline.sh --scrape   # also scrape (needs access to youtube.com, babypips.com,
                                   # itunes.apple.com, openlibrary.org)
```
