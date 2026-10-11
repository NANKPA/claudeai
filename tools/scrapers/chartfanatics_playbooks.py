#!/usr/bin/env python3
"""Capture the written strategy playbooks from chartfanatics.com.

Crawls https://www.chartfanatics.com/strategies (and /playbook/* pages it links
to), extracts each playbook's main text with trafilatura, and saves it to
01_chart-fanatics/raw/playbooks/<slug>.md. When a page matches an existing
strategy note (via its source URL), the scraped file reuses that strategy's id,
so the graph merges the first-party rules into the existing node.
Respects robots.txt and waits --delay seconds between requests.

Example
  python3 tools/scrapers/chartfanatics_playbooks.py
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import KB_ROOT, PoliteSession, preflight, slug, write_markdown, write_yaml  # noqa: E402
from concept_tagger import tag  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ti_lib import load_kb  # noqa: E402

INDEX = "https://www.chartfanatics.com/strategies"
PART = KB_ROOT / "01_chart-fanatics"


def known_strategy_urls() -> dict[str, str]:
    """Map playbook URL path -> existing strategy id (from the strategy notes' sources)."""
    out = {}
    for node in load_kb(include_raw=False).nodes.values():
        if node.kind != "strategy":
            continue
        for src in node.attrs.get("sources") or []:
            url = (src or {}).get("url", "") if isinstance(src, dict) else ""
            path = urlparse(url).path.rstrip("/")
            if "chartfanatics.com" in url and re.match(r"^/(strategies|playbook)/[^/]+$", path):
                out[path] = node.id
    return out


def main() -> None:
    import trafilatura

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--delay", type=float, default=3.0)
    args = ap.parse_args()

    preflight(INDEX)
    s = PoliteSession(delay=args.delay)
    index = s.get(INDEX)
    if not index or not index.ok:
        raise SystemExit(f"could not load {INDEX}")
    links = []
    for href in re.findall(r'href="([^"#?]+)"', index.text):
        url = urljoin(INDEX, href)
        path = urlparse(url).path.rstrip("/")
        if urlparse(url).netloc.endswith("chartfanatics.com") and re.match(r"^/(strategies|playbook)/[^/]+$", path) and url not in links:
            links.append(url)
    known = known_strategy_urls()
    print(f"{len(links)} playbook pages; {len(known)} already linked to strategy notes")
    catalog = []
    for url in links:
        resp = s.get(url)
        if not resp or not resp.ok:
            continue
        text = trafilatura.extract(resp.text, output_format="markdown", include_tables=True) or ""
        title_m = re.search(r"<title>(.*?)</title>", resp.text, re.S | re.I)
        title = (title_m.group(1).strip() if title_m else url).split("|")[0].strip()
        path = urlparse(url).path.rstrip("/")
        page_slug = path.rsplit("/", 1)[-1]
        node_id = known.get(path) or f"strategy_cf_{slug(page_slug)}"
        tags = tag(f"{title}\n{text}")
        fm = {"id": node_id, "type": "strategy", "title": title, "partition": "01_chart-fanatics",
              "source_url": url, "featured_in": ["channel_chart_fanatics"], "uses": tags["covers"],
              "taught_by": tags["speaker_ids"], "status": "scraped",
              "sources": [{"title": f"Chart Fanatics — {title}", "url": url, "tier": "T2"}]}
        write_markdown(PART / "raw" / "playbooks" / f"{page_slug}.md", fm, f"# {title}\n\n{text}")
        catalog.append({"id": node_id, "title": title, "url": url, "matched_existing": path in known})
        print(f"  {'merged ' if path in known else 'new    '}{node_id}: {title[:70]}")
    write_yaml(PART / "playbooks.scraped.yaml", {"playbooks_index": catalog})
    print(f"done: {len(catalog)} playbooks; next: python3 tools/build_graph.py")


if __name__ == "__main__":
    main()
