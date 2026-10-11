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


FM_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)


def retag_show(show_dir: Path, hosts: set[str]) -> int:
    """Re-tag one show's saved episodes, ignoring show-note boilerplate (sponsor reads,
    book adverts, link footers: any line repeated across >= 5% of the show's episodes)
    and the show's own hosts, so `covers`/`speaker_ids` reflect each episode's guest/topic."""
    from collections import Counter
    parsed = []
    for f in sorted(show_dir.glob("*.md")):
        m = FM_RE.match(f.read_text(encoding="utf-8"))
        if m:
            parsed.append((f, yaml.safe_load(m.group(1)) or {}, m.group(2)))

    def notes_of(body: str) -> str:
        m = re.search(r"## Show notes\n\n(.*?)(?:\n## Transcript|\Z)", body, re.S)
        return m.group(1) if m else ""

    freq: Counter = Counter()
    for _, _, body in parsed:
        freq.update({ln.strip() for ln in notes_of(body).splitlines() if len(ln.strip()) > 20})
    boiler = {ln for ln, c in freq.items() if c >= max(5, 0.05 * len(parsed))}
    for f, fm, body in parsed:
        clean = "\n".join(ln for ln in notes_of(body).splitlines() if ln.strip() not in boiler)
        transcript = body.split("## Transcript", 1)[1] if "## Transcript" in body else ""
        t = tag(f"{fm.get('title', '')}\n{clean}\n{transcript}", min_hits=1)
        fm["covers"] = t["covers"]
        fm["speaker_ids"] = [x for x in t["speaker_ids"] if x not in hosts]
        write_markdown(f, fm, body)
    return len(boiler)


def main() -> None:
    import feedparser

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", default=None, help="podcast id")
    ap.add_argument("--max-episodes", type=int, default=300)
    ap.add_argument("--transcribe", type=int, default=0, help="newest N episodes per show to transcribe")
    ap.add_argument("--whisper-model", default="small")
    ap.add_argument("--retag-only", action="store_true", help="re-tag saved episodes without fetching feeds")
    args = ap.parse_args()

    registry = yaml.safe_load((PART / "podcasts.yaml").read_text(encoding="utf-8"))
    if args.retag_only:
        for pod in registry["podcasts"]:
            show_dir = PART / "raw" / pod["id"]
            if show_dir.is_dir():
                n = retag_show(show_dir, set(pod.get("hosts", []) + pod.get("founded_by", [])))
                print(f"{pod['id']}: re-tagged ({n} boilerplate lines ignored)")
        rebuild_index()
        return
    preflight("https://itunes.apple.com/")
    session = PoliteSession(delay=1.0, respect_robots=False)  # documented public API
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
        retag_show(PART / "raw" / pod["id"], set(pod.get("hosts", []) + pod.get("founded_by", [])))
        time.sleep(1)
    n = rebuild_index()
    print(f"done: {n} episodes; next: python3 tools/build_graph.py")


def rebuild_index() -> int:
    """Write podcast-episodes.scraped.yaml from the saved (re-tagged) episode files."""
    items = []
    for f in sorted((PART / "raw").glob("podcast_*/*.md")):
        m = FM_RE.match(f.read_text(encoding="utf-8"))
        fm = yaml.safe_load(m.group(1)) if m else {}
        if fm.get("id"):
            items.append({k: fm.get(k) for k in ("id", "type", "title", "published", "featured_in", "covers", "speaker_ids")})
    write_yaml(PART / "podcast-episodes.scraped.yaml", {"scraped_media": items})
    return len(items)


if __name__ == "__main__":
    main()
