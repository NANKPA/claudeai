# Hand-off: continue this work on your own computer

Everything built in the cloud session is on GitHub in **NANKPA/claudeai**, branch
**`claude/trading-intelligence-scraper-5ep9cj`**. The only things not in git are the
scraped raw pages, the market-data cache and the built bundles; they are in
`claudeai-local-data.tar.gz` (sent with this hand-off). Steps below work on macOS, Linux and
Windows (use PowerShell or Git Bash).

## 1. Get the code

```bash
git clone https://github.com/NANKPA/claudeai.git
cd claudeai
git checkout claude/trading-intelligence-scraper-5ep9cj
```

## 2. Restore the files that are not in git

Put `claudeai-local-data.tar.gz` in the `claudeai` folder, then:

```bash
tar -xzf claudeai-local-data.tar.gz
```

This restores:
- `trading-intelligence/01_chart-fanatics/raw/playbooks/` (the 47 first-party playbook pages)
- `trading-intelligence/02_podcasts-interviews/raw/` (4,460 podcast episode files)
- `tools/philosophy/data/` (cached Yahoo daily data for the evidence lab)
- `dist/` (the Claude bundles and the explorer page)

They are git-ignored on purpose (third-party text and re-downloadable data); keep them local.

## 3. Install the tools

Python 3.11 or newer:

```bash
python -m pip install -r tools/requirements.txt
python -m pytest -q tools/philosophy/tests      # expect 120 passed
./tools/run_pipeline.sh                         # rebuild tables, graph, explorer, bundles
```

On Windows without bash, run the steps in `tools/run_pipeline.sh` one by one with `python`.

## 4. Open a Claude session on this folder

Any of these, from inside the `claudeai` folder:
- **Claude Desktop app:** open the folder as a Claude Code project.
- **Terminal:** `claude` (install Claude Code first), or `claude remote-control` to run it on
  your computer and drive it from the Claude Code app.

`trading-intelligence/CLAUDE.md` tells Claude to reason through your philosophy first.

## 5. What to do next locally (needs your own internet connection)

These were blocked from the cloud servers and are the reason to run locally:

```bash
# Chart Fanatics: every video + transcript (uses your browser's YouTube login; never share the cookie file)
python tools/scrapers/youtube_channel.py --cookies-from-browser chrome
# Top-100 trading and top-100 math videos, with transcripts
python tools/scrapers/youtube_top_search.py --transcripts
# BabyPips School of Pipsology lessons (Cloudflare blocks cloud servers)
python tools/scrapers/babypips_course.py
# Then rebuild everything
./tools/run_pipeline.sh
```

The sniper lab also does more at home, because the free forex datafeed (Dukascopy) throttles cloud
servers. At home the intraday forex tests can run:

```bash
# Forex and gold on 5m/15m (downloads minute history once, then caches it; takes a while)
python -m trading_intelligence.sniper lab --symbols EURUSD GBPUSD USDJPY XAUUSD --timeframes 5m 15m 1h 4h \
       --out trading-intelligence/10_sniper-lab/backtests/fx
# Paper-trade every setup live through your PhilosophyGate (state: ~/.trading-intelligence/sniper-paper/)
python -m trading_intelligence.sniper scan --equity 20 --risk-pct 1 --fees low
python -m trading_intelligence.sniper scan --report
```

Also open:
- `trading-intelligence/10_sniper-lab/README.md`: the sniper entries, what the backtests found after
  costs, venues for small accounts, and how the scanner hands gated trades to your bot (`--on-take`).
- `trading-intelligence/00_philosophy/README.md`: what was built around your philosophy and
  what it found.
- `trading-intelligence/00_philosophy/research-program.md`: the 12-week plan, starting with
  the journal (`journal-template.csv` + `tools/philosophy/journal_review.py`).
- `trading-intelligence/00_philosophy/extensions.md`: suggested amendments to the philosophy,
  for you to accept or reject.

## A prompt to start the local session with

> Read HANDOFF.md, trading-intelligence/CLAUDE.md and trading-intelligence/00_philosophy/README.md.
> Then run the YouTube and BabyPips scrapers listed in HANDOFF.md step 5, rebuild with
> tools/run_pipeline.sh, re-run tools/philosophy/merge_blueprint.py and centrality.py, and tell
> me what the new transcripts and lessons add to the graph and to my philosophy.

## State at hand-off

- Graph: 1,154 nodes, 5,772 edges, 30 communities; the philosophy is its own community and the
  explorer's start node.
- 836 verified philosophy links (865 proposed, 31 refuted), 47 playbooks graded against the 12
  principles (blind re-grade kappa 0.94), 7 evidence-lab studies, 20 hypotheses, 18 extensions.
- Hosted explorer: https://claude.ai/artifact/87RR4yVQKDBFdQ9GpwheF3 (private to your account).
