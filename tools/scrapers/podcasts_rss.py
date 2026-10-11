#!/usr/bin/env python3
"""Pull episode catalogs (and optionally audio transcripts) for every podcast in
02_podcasts-interviews/podcasts.yaml.

Feed discovery uses the public iTunes Search API with each show's
`itunes_search_term`, so no feed URLs need to be hard-coded. Every episode's
show notes are saved as markdown in raw/<podcast_id>/ and tagged with concepts
and people. With --transcribe N, the newest N episodes per show are downloaded
and transcribed locally with faster-whisper (pip install faster-whisper).

Examples
  python3 tools/scrapers/podcasts_rss.py                      # all shows, show notes only
  python3 tools/scrapers/podcasts_rss.py --only podcast_chat_with_traders --max-episodes 500
  python3 tools/scrapers/podcasts_rss.py --transcribe 5 --whisper-model small
"""
from __future__ import annotations

import argparse
import re
import sys
import tempfile
import time
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import KB_ROOT, PoliteSession, preflight, slug, write_markdown, write_yaml  # noqa: E402
from concept_tagger import tag  # noqa: E402

PART = KB_ROOT / "02_podcasts-interviews"


def find_feed(session: PoliteSession, term: str) -> str | None:
    resp = session.get("https://itunes.apple.com/search", params={"term": term, "entity": "podcast", "limit": 5})
    if not resp or not resp.ok:
        return None
    results = resp.json().get("results", [])
    term_l = term.lower()
    results.sort(key=lambda r: -sum(w in (r.get("collectionName") or "").lower() for w in term_l.split()))
    return next((r.get("feedUrl") for r in results if r.get("feedUrl")), None)


def strip_html(html: str) -> str:
    text = re.sub(r"<(br|/p|/li)\s*/?>", "\n", html or "", flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def transcribe(audio_url: str, session: PoliteSession, model_name: str) -> str:
    from faster_whisper import WhisperModel  # optional dependency
    resp = session.get(audio_url, stream=True)
    if not resp or not resp.ok:
        return ""
    with tempfile.NamedTemporaryFile(suffix=".mp3") as tmp:
        for chunk in resp.iter_content(1 << 16):
            tmp.write(chunk)
        tmp.flush()
        model = WhisperModel(model_name, compute_type="int8")
        segments, _ = model.transcribe(tmp.name, vad_filter=True)
        return "\n".join(f"[{int(s.start // 60)}:{int(s.start % 60):02d}] {s.text.strip()}" for s in segments)


def main() -> None:
    import feedparser

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", default=None, help="podcast id")
    ap.add_argument("--max-episodes", type=int, default=300)
    ap.add_argument("--transcribe", type=int, default=0, help="newest N episodes per show to transcribe")
    ap.add_argument("--whisper-model", default="small")
    args = ap.parse_args()

    preflight("https://itunes.apple.com/")
    session = PoliteSession(delay=1.0, respect_robots=False)  # documented public API
    registry = yaml.safe_load((PART / "podcasts.yaml").read_text(encoding="utf-8"))
    scraped = []
    for pod in registry["podcasts"]:
        if args.only and pod["id"] != args.only:
            continue
        feed_url = pod.get("rss") or find_feed(session, pod.get("itunes_search_term") or pod["title"])
        if not feed_url:
            print(f"{pod['id']}: no feed found")
            continue
        feed = feedparser.parse(feed_url)
        episodes = feed.entries[: args.max_episodes]
        print(f"{pod['id']}: {len(feed.entries)} episodes in feed ({feed_url}); saving {len(episodes)}")
        for n, ep in enumerate(episodes):
            title = ep.get("title", "untitled")
            ep_slug = slug(title)[:80] or f"episode_{n}"
            node_id = f"media_{pod['id'].removeprefix('podcast_')}_{ep_slug}"[:120]
            notes = strip_html(ep.get("summary") or ep.get("description") or "")
            audio = next((l.get("href") for l in ep.get("links", []) if l.get("rel") == "enclosure"), None)
            transcript = ""
            if args.transcribe and n < args.transcribe and audio:
                try:
                    transcript = transcribe(audio, session, args.whisper_model)
                except ImportError:
                    raise SystemExit("--transcribe needs: pip install faster-whisper")
            tags = tag(f"{title}\n{notes}\n{transcript}", min_hits=1)
            fm = {
                "id": node_id, "type": "media", "title": title, "partition": "02_podcasts-interviews",
                "source_url": ep.get("link"), "audio_url": audio, "published": ep.get("published"),
                "duration": ep.get("itunes_duration"), "featured_in": [pod["id"]],
                "speaker_ids": tags["speaker_ids"], "covers": tags["covers"],
                "status": "scraped", "has_transcript": bool(transcript),
            }
            body = f"# {title}\n\n## Show notes\n\n{notes}"
            if transcript:
                body += f"\n\n## Transcript (faster-whisper {args.whisper_model})\n\n{transcript}"
            write_markdown(PART / "raw" / pod["id"] / f"{ep_slug}.md", fm, body)
            scraped.append({k: fm[k] for k in ("id", "type", "title", "published", "featured_in", "covers", "speaker_ids")})
        time.sleep(1)
    write_yaml(PART / "podcast-episodes.scraped.yaml", {"scraped_media": scraped})
    print(f"done: {len(scraped)} episodes; next: python3 tools/build_graph.py")


if __name__ == "__main__":
    main()
