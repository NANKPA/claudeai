#!/usr/bin/env bash
# End-to-end refresh of the trading-intelligence knowledge base.
#   ./tools/run_pipeline.sh            # offline steps only (render, graph, bundle)
#   ./tools/run_pipeline.sh --scrape   # also run every scraper (needs network access to
#                                      # youtube.com, babypips.com, itunes.apple.com, openlibrary.org)
set -euo pipefail
cd "$(dirname "$0")/.."

python3 -m pip install -q -r tools/requirements.txt

if [[ "${1:-}" == "--scrape" ]]; then
  python3 tools/scrapers/youtube_channel.py                                   # Chart Fanatics: every video + transcript
  python3 tools/scrapers/youtube_channel.py --channel https://www.youtube.com/@chartfanaticslive \
          --channel-node channel_chart_fanatics_live --id-prefix media_cfl_ --tabs streams videos
  python3 tools/scrapers/chartfanatics_playbooks.py                          # written strategy playbooks (T2 rules)
  python3 tools/scrapers/youtube_top_search.py --transcripts                  # top-100 trading + top-100 math videos
  python3 tools/scrapers/podcasts_rss.py                                      # podcast episode catalogs
  python3 tools/scrapers/babypips_course.py ${BABYPIPS_COOKIES:+--cookies "$BABYPIPS_COOKIES"}
  python3 tools/scrapers/books_enrich.py                                      # Open Library QA of the book registry
fi

python3 tools/render_registries.py
python3 tools/build_graph.py
python3 tools/build_explorer.py
python3 tools/bundle_for_claude.py ${INCLUDE_RAW:+--include-raw}
echo "Done. Open trading-intelligence/09_knowledge-graph/explorer.html (or graph.html)"
