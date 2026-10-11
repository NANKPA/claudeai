#!/usr/bin/env python3
"""Fill the "top 100" media lists from the discovery queries in the registries.

Reads `discovery_queries` from
  * 02_podcasts-interviews/landmark-media.yaml  (top trading interviews/podcast videos)
  * 06_mathematics-foundations/lectures.yaml    (top videos on the math of trading)
runs each query through YouTube search (yt-dlp), drops audiobook/summary uploads and weak title
matches, keeps the 4 most-viewed results per query (for diversity), ranks the union by views, and writes the best N to
<file>.scraped.yaml as media nodes (tagged with concepts and people).
Optionally pulls transcripts for the winners into the partition's raw/ folder.

Examples
  python3 tools/scrapers/youtube_top_search.py                    # both lists, top 100 each
  python3 tools/scrapers/youtube_top_search.py --only landmark --per-query 40 --transcripts
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import KB_ROOT, preflight, write_markdown, write_yaml  # noqa: E402
from concept_tagger import tag  # noqa: E402
from youtube_channel import fetch_transcript, paragraphs  # noqa: E402

TARGETS = {
    "landmark": "02_podcasts-interviews/landmark-media.yaml",
    "lectures": "06_mathematics-foundations/lectures.yaml",
}
MIN_DURATION_S = 8 * 60  # skip shorts / clips: we want interviews and lectures


def search(query: str, n: int) -> list[dict]:
    import yt_dlp
    opts = {"quiet": True, "no_warnings": True, "skip_download": True, "extract_flat": True, "ignoreerrors": True}
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"ytsearch{n}:{query}", download=False) or {}
    return [e for e in info.get("entries") or [] if e and e.get("id")]


def relevance(query: str, title: str) -> float:
    q = {w for w in re.findall(r"[a-z0-9']+", query.lower()) if len(w) > 2}
    t = set(re.findall(r"[a-z0-9']+", (title or "").lower()))
    return (len(q & t) / len(q)) if q else 0.0


EXCLUDE = re.compile(r"audiobook|full book|book summary|#shorts|reaction", re.I)
PER_QUERY_CAP = 4      # keeps the list diverse: no single guest/topic floods it
MIN_RELEVANCE = 0.5    # at least half the query's keywords must appear in the title


def run(target_key: str, args) -> None:
    rel = TARGETS[target_key]
    data = yaml.safe_load((KB_ROOT / rel).read_text(encoding="utf-8")) or {}
    queries = data.get("discovery_queries") or {}
    cache_path = KB_ROOT / rel.replace(".yaml", ".candidates.json")
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if (cache_path.exists() and not args.refresh) else {}
    picked: dict[str, dict] = {}
    for group, qs in queries.items():
        for q in qs:
            if q not in cache:
                cache[q] = [{k: e.get(k) for k in ("id", "title", "channel", "uploader", "view_count", "duration", "description")}
                            for e in search(q, args.per_query)]
                time.sleep(args.sleep)
            pool = []
            for e in cache[q]:
                title = e.get("title") or ""
                dur = e.get("duration") or 0
                if EXCLUDE.search(title) or (dur and dur < MIN_DURATION_S) or relevance(q, title) < MIN_RELEVANCE:
                    continue
                pool.append(e)
            pool.sort(key=lambda e: -(e.get("view_count") or 0))
            for e in pool[:PER_QUERY_CAP]:
                if e["id"] not in picked:
                    picked[e["id"]] = {"entry": e, "query": q, "group": group}
            print(f"  [{target_key}] {group}: '{q}' -> {len(pool)} eligible, {len(picked)} picked so far")
    cache_path.write_text(json.dumps(cache, ensure_ascii=False), encoding="utf-8")
    ranked = sorted(picked.values(), key=lambda r: -(r["entry"].get("view_count") or 0))[: args.top]
    out = []
    raw_dir = KB_ROOT / rel.split("/")[0] / "raw" / "top-videos"
    for rank, r in enumerate(ranked, 1):
        e = r["entry"]
        vid = e["id"]
        node_id = "media_yt_" + re.sub(r"[^a-z0-9_]", "_", vid.lower())
        tags = tag(f"{e.get('title', '')}\n{e.get('description') or ''}", min_hits=1)
        item = {
            "id": node_id, "type": "media", "rank": rank, "title": e.get("title"),
            "url": f"https://www.youtube.com/watch?v={vid}", "youtube_id": vid,
            "channel": e.get("channel") or e.get("uploader"), "views": e.get("view_count"),
            "duration_s": e.get("duration"), "query": r["query"], "query_group": r["group"],
            "covers": tags["covers"], "speaker_ids": tags["speaker_ids"],
            "verification": "scraped", "views_as_of": time.strftime("%Y-%m-%d", time.gmtime()),
        }
        if args.transcripts:
            snippets, src = fetch_transcript(vid, ["en", "en-US", "en-GB"])
            if snippets:
                body_tags = tag(paragraphs(snippets))
                item["covers"] = sorted(set(item["covers"]) | set(body_tags["covers"]))
                item["speaker_ids"] = sorted(set(item["speaker_ids"]) | set(body_tags["speaker_ids"]))
                write_markdown(raw_dir / f"{vid}.md", {**item, "status": "scraped", "transcript_source": src},
                               f"# {item['title']}\n\n{paragraphs(snippets)}")
            time.sleep(args.sleep)
        out.append(item)
    dest = KB_ROOT / rel.replace(".yaml", ".scraped.yaml")
    write_yaml(dest, {"scraped_media": out})
    print(f"wrote {dest.relative_to(KB_ROOT)} ({len(out)} items from {len(picked)} eligible picks)")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", choices=list(TARGETS), default=None)
    ap.add_argument("--per-query", type=int, default=25)
    ap.add_argument("--top", type=int, default=100)
    ap.add_argument("--sleep", type=float, default=1.5)
    ap.add_argument("--transcripts", action="store_true")
    ap.add_argument("--refresh", action="store_true", help="ignore the cached search results and search again")
    args = ap.parse_args()
    preflight("https://www.youtube.com/")
    for key in ([args.only] if args.only else TARGETS):
        run(key, args)


if __name__ == "__main__":
    main()
