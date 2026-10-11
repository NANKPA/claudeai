#!/usr/bin/env python3
"""Scrape an entire YouTube channel (default: Chart Fanatics) into the knowledge base.

For every video on the channel's Videos and Live tabs:
  * metadata via yt-dlp (title, date, views, duration, description, chapters, tags)
  * transcript via youtube-transcript-api (falls back to yt-dlp auto-captions)
  * concept + people tags via concept_tagger -> `covers:` / `speaker_ids:` edges
Writes one markdown file per video to <partition>/raw/videos/<id>.md and a
catalog to <partition>/catalog.scraped.yaml, both picked up by build_graph.py.

Examples
  python3 tools/scrapers/youtube_channel.py                       # Chart Fanatics, all videos
  python3 tools/scrapers/youtube_channel.py --limit 20            # quick sample
  python3 tools/scrapers/youtube_channel.py --channel https://www.youtube.com/@chartfanaticslive \
        --channel-node channel_chart_fanatics_live --id-prefix media_cfl_
  python3 tools/scrapers/youtube_channel.py --cookies-from-browser chrome   # if YouTube asks to sign in
"""
from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import KB_ROOT, preflight, write_markdown, write_yaml  # noqa: E402
from concept_tagger import tag  # noqa: E402

DEFAULT_CHANNEL = "https://www.youtube.com/@chart-fanatics"


def ydl_opts(args) -> dict:
    opts = {"quiet": True, "no_warnings": True, "skip_download": True, "ignoreerrors": True}
    if args.cookies_from_browser:
        opts["cookiesfrombrowser"] = (args.cookies_from_browser,)
    if args.cookies:
        opts["cookiefile"] = args.cookies
    return opts


def list_channel_videos(channel: str, args) -> list[dict]:
    import yt_dlp
    entries: dict[str, dict] = {}
    opts = {**ydl_opts(args), "extract_flat": "in_playlist"}
    with yt_dlp.YoutubeDL(opts) as ydl:
        for tab in args.tabs:
            info = ydl.extract_info(f"{channel.rstrip('/')}/{tab}", download=False) or {}
            for e in info.get("entries") or []:
                if e and e.get("id") and len(e["id"]) == 11:
                    entries.setdefault(e["id"], {**e, "_tab": tab})
    return list(entries.values())


def video_metadata(video_id: str, args) -> dict:
    import yt_dlp
    with yt_dlp.YoutubeDL(ydl_opts(args)) as ydl:
        return ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False) or {}


def fetch_transcript(video_id: str, langs: list[str]) -> tuple[list[tuple[float, str]], str]:
    """Return ([(start_seconds, text)], source)."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=langs)
        return [(s.start, s.text) for s in fetched.snippets], "youtube-transcript-api"
    except Exception as exc:  # noqa: BLE001 - fall back to captions
        err = exc.__class__.__name__
    try:
        return _captions_via_ytdlp(video_id, langs), "yt-dlp-captions"
    except Exception as exc:  # noqa: BLE001
        return [], f"unavailable ({err}; {exc.__class__.__name__})"


def _captions_via_ytdlp(video_id: str, langs: list[str]) -> list[tuple[float, str]]:
    import tempfile
    import yt_dlp
    with tempfile.TemporaryDirectory() as tmp:
        opts = {"quiet": True, "skip_download": True, "writesubtitles": True, "writeautomaticsub": True,
                "subtitleslangs": langs, "subtitlesformat": "vtt", "outtmpl": f"{tmp}/%(id)s.%(ext)s"}
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
        vtts = list(Path(tmp).glob("*.vtt"))
        if not vtts:
            raise FileNotFoundError("no captions")
        return parse_vtt(vtts[0].read_text(encoding="utf-8"))


def parse_vtt(text: str) -> list[tuple[float, str]]:
    out: list[tuple[float, str]] = []
    last = ""
    for block in text.split("\n\n"):
        m = re.search(r"(\d+):(\d+):(\d+)\.(\d+) -->", block)
        if not m:
            continue
        start = int(m[1]) * 3600 + int(m[2]) * 60 + int(m[3])
        lines = [re.sub(r"<[^>]+>", "", ln).strip() for ln in block.splitlines()[1:] if "-->" not in ln]
        line = " ".join(ln for ln in lines if ln)
        if line and line != last:  # auto-captions repeat rolling lines
            out.append((float(start), line))
            last = line
    return out


def paragraphs(snippets: list[tuple[float, str]], every: float = 60.0) -> str:
    out, buf, mark = [], [], 0.0
    for start, text in snippets:
        if start - mark >= every and buf:
            out.append(f"**[{int(mark // 3600):d}:{int(mark % 3600 // 60):02d}:{int(mark % 60):02d}]** " + " ".join(buf))
            buf, mark = [], start
        buf.append(text.replace("\n", " "))
    if buf:
        out.append(f"**[{int(mark // 3600):d}:{int(mark % 3600 // 60):02d}:{int(mark % 60):02d}]** " + " ".join(buf))
    return "\n\n".join(out)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--channel", default=DEFAULT_CHANNEL)
    ap.add_argument("--channel-node", default="channel_chart_fanatics", help="graph id of the channel")
    ap.add_argument("--partition", default="01_chart-fanatics")
    ap.add_argument("--id-prefix", default="media_cf_")
    ap.add_argument("--tabs", nargs="+", default=["videos", "streams"])
    ap.add_argument("--limit", type=int, default=0, help="0 = all videos")
    ap.add_argument("--langs", nargs="+", default=["en", "en-US", "en-GB"])
    ap.add_argument("--sleep", type=float, default=2.0, help="seconds between videos")
    ap.add_argument("--refresh", action="store_true", help="re-scrape videos already on disk")
    ap.add_argument("--no-transcripts", action="store_true")
    ap.add_argument("--catalog-only", action="store_true",
                    help="list videos from the channel tabs only (no per-video requests); works where YouTube bot-checks video pages")
    ap.add_argument("--cookies-from-browser", default=None)
    ap.add_argument("--cookies", default=None, help="Netscape cookies.txt")
    args = ap.parse_args()

    preflight("https://www.youtube.com/")
    part = KB_ROOT / args.partition
    raw_dir = part / "raw" / "videos"
    videos = list_channel_videos(args.channel, args)
    print(f"{len(videos)} videos found on {args.channel}")
    if args.limit:
        videos = videos[: args.limit]
    curated_path = part / "catalog.yaml"
    curated = {}
    if curated_path.exists():  # reuse hand-curated node ids so curated and scraped entries merge
        import yaml
        for m in (yaml.safe_load(curated_path.read_text(encoding="utf-8")) or {}).get("media", []):
            if m.get("youtube_id"):
                curated[m["youtube_id"]] = m["id"]
    if args.catalog_only:
        items = []
        for v in videos:
            vid = v["id"]
            tags = tag(v.get("title") or "", min_hits=1)
            items.append({"id": curated.get(vid) or args.id_prefix + re.sub(r"[^a-z0-9_]", "_", vid.lower()), "type": "media",
                          "title": v.get("title"), "youtube_id": vid, "url": f"https://www.youtube.com/watch?v={vid}",
                          "view_count": v.get("view_count"), "duration_s": v.get("duration"), "tab": v.get("_tab"),
                          "featured_in": [args.channel_node], "covers": tags["covers"], "speaker_ids": tags["speaker_ids"],
                          "status": "catalog-only"})
        write_yaml(part / "catalog.scraped.yaml", {"scraped_media": items})
        print(f"catalog-only: {len(items)} videos -> {args.partition}/catalog.scraped.yaml")
        return

    catalog = []
    for i, v in enumerate(videos, 1):
        vid = v["id"]
        node_id = curated.get(vid) or args.id_prefix + re.sub(r"[^a-z0-9_]", "_", vid.lower())
        path = raw_dir / f"{vid}.md"
        if path.exists() and not args.refresh:
            print(f"[{i}/{len(videos)}] {vid} cached")
            catalog.append({"id": node_id, "youtube_id": vid, "title": v.get("title"), "cached": True})
            continue
        meta = video_metadata(vid, args)
        title = meta.get("title") or v.get("title") or vid
        snippets, t_source = ([], "skipped") if args.no_transcripts else fetch_transcript(vid, args.langs)
        transcript = paragraphs(snippets)
        description = meta.get("description") or ""
        tags = tag(f"{title}\n{description}\n{transcript}")
        chapters = meta.get("chapters") or []
        fm = {
            "id": node_id,
            "type": "media",
            "title": title,
            "partition": args.partition,
            "source_url": f"https://www.youtube.com/watch?v={vid}",
            "youtube_id": vid,
            "captured_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "author": meta.get("channel") or meta.get("uploader"),
            "upload_date": meta.get("upload_date"),
            "view_count": meta.get("view_count"),
            "like_count": meta.get("like_count"),
            "duration_s": meta.get("duration"),
            "tab": v.get("_tab"),
            "transcript_source": t_source,
            "featured_in": [args.channel_node],
            "speaker_ids": tags["speaker_ids"],
            "covers": tags["covers"],
            "status": "scraped",
        }
        body = [f"# {title}\n", f"Source: https://www.youtube.com/watch?v={vid}\n"]
        if chapters:
            body.append("## Chapters\n" + "\n".join(f"- {int(c['start_time'] // 60)}:{int(c['start_time'] % 60):02d} {c.get('title', '')}" for c in chapters))
        if description:
            body.append("## Description\n" + description)
        body.append("## Transcript\n" + (transcript or f"_No transcript available ({t_source})._"))
        write_markdown(path, fm, "\n\n".join(body))
        catalog.append({k: fm[k] for k in ("id", "youtube_id", "title", "upload_date", "view_count", "duration_s", "covers", "speaker_ids")})
        print(f"[{i}/{len(videos)}] {vid} {fm['view_count'] or '?'} views · {len(snippets)} caption lines · {title[:70]}")
        time.sleep(args.sleep)

    write_yaml(part / "catalog.scraped.yaml", {"scraped_media": [{**c, "type": "media", "featured_in": [args.channel_node]} for c in catalog]})
    print(f"done: {len(catalog)} videos -> {raw_dir.relative_to(KB_ROOT)}; next: python3 tools/build_graph.py")


if __name__ == "__main__":
    main()
