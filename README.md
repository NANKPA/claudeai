# claudeai — Trading Intelligence

A partitioned, graph-linked trading knowledge base built for Claude.

- **`trading-intelligence/`**: the knowledge base. Its foundation is the owner's philosophy,
  [`00_philosophy/`](trading-intelligence/00_philosophy/) ("The Philosophy of the Relationship"),
  linked to 10 partitions (framework, Chart Fanatics, podcasts and interviews, legends, BabyPips,
  top-100 books, mathematics, concepts, synthesis) and the graphify knowledge graph in
  `09_knowledge-graph/`. Start with
  [`trading-intelligence/README.md`](trading-intelligence/README.md).
- **`trading_intelligence/`**: the bot plug-in (see [`BOT_INTEGRATION.md`](BOT_INTEGRATION.md)): an MCP
  server that gives a Claude session the philosophy, the knowledge graph and the maths as tools, and a
  Python package whose `PhilosophyGate` runs the owner's decision protocol before every order.
  Install: `pip install "trading-intelligence[mcp] @ git+https://github.com/NANKPA/claudeai.git"`.
- **`tools/`**: the build and scraping toolchain:
  - `render_registries.py`: YAML registries → markdown tables
  - `build_graph.py`: notes + registries → graphify (Leiden communities, report, HTML, wiki)
  - `build_explorer.py`: the interactive Trading Intelligence Map (`explorer.html`)
  - `bundle_for_claude.py`: one-file bundle + per-partition bundles for Claude Projects (`dist/`)
  - `philosophy/`: the evidence lab (`edge_lab.py`, `studies.py`, `market_data.py`, 120 tests),
    the journal review (`journal_review.py`), the blueprint merge and the centrality analysis
  - `scrapers/`: Chart Fanatics channel + transcripts + written playbooks, top-100 video search, podcast RSS,
    BabyPips course crawler, Open Library book QA
  - `run_pipeline.sh [--scrape]`: run everything end to end

```bash
pip install -r tools/requirements.txt
./tools/run_pipeline.sh            # rebuild tables, graph, explorer, Claude bundle
./tools/run_pipeline.sh --scrape   # also scrape (needs access to youtube.com, babypips.com,
                                   # itunes.apple.com, openlibrary.org)
```
