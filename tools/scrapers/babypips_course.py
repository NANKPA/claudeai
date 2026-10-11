#!/usr/bin/env python3
"""Crawl the BabyPips School of Pipsology into 04_babypips-school-of-pipsology/raw/.

* Starts at https://www.babypips.com/learn/forex and discovers course pages
  and their lesson links (/learn/forex/<slug>).
* Respects robots.txt and waits --delay seconds between requests.
* Extracts each lesson's main text with trafilatura and saves it as markdown
  with frontmatter (part_of the course node, tagged with concepts).
* Premium lessons need a logged-in session: export your own browser cookies
  to a Netscape cookies.txt and pass --cookies. Without them, paywalled
  lessons are recorded as `status: premium-locked` (title only).

The output is for your personal study corpus. BabyPips content is copyrighted,
so keep raw/ private (it is git-ignored by default).

Examples
  python3 tools/scrapers/babypips_course.py --max-lessons 20      # sample
  python3 tools/scrapers/babypips_course.py --cookies ~/babypips_cookies.txt
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

BASE = "https://www.babypips.com/learn/forex"
PART = KB_ROOT / "04_babypips-school-of-pipsology"
# course slug on babypips -> our course node id
COURSE_NODES = {
    "preschool": "course_babypips_preschool",
    "kindergarten": "course_babypips_kindergarten",
    "elementary": "course_babypips_elementary",
    "middle-school": "course_babypips_middle_school",
    "summer-school": "course_babypips_summer_school",
    "high-school": "course_babypips_high_school",
    "undergraduate-freshman": "course_babypips_freshman",
    "undergraduate-sophomore": "course_babypips_sophomore",
    "undergraduate-junior": "course_babypips_junior",
    "undergraduate-senior": "course_babypips_senior",
}
PAYWALL_MARKERS = ("premium members", "upgrade to premium", "unlock this lesson", "become a premium")


def links_under(html: str, page_url: str) -> list[str]:
    out = []
    for href in re.findall(r'href="([^"#?]+)"', html):
        url = urljoin(page_url, href)
        p = urlparse(url)
        if p.netloc.endswith("babypips.com") and p.path.startswith("/learn/forex/") and p.path.count("/") == 3:
            if url not in out:
                out.append(url)
    return out


def main() -> None:
    import trafilatura

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--delay", type=float, default=3.0)
    ap.add_argument("--max-lessons", type=int, default=0, help="0 = all")
    ap.add_argument("--cookies", default=None, help="Netscape cookies.txt for your own premium login")
    ap.add_argument("--refresh", action="store_true")
    args = ap.parse_args()

    preflight(BASE)
    s = PoliteSession(delay=args.delay, cookies_file=args.cookies)
    index = s.get(BASE)
    if not index or not index.ok:
        raise SystemExit(f"could not load {BASE}")
    course_urls = [u for u in links_under(index.text, BASE) if urlparse(u).path.rsplit("/", 1)[-1] in COURSE_NODES]
    print(f"{len(course_urls)} course pages")
    saved, catalog = 0, []
    for course_url in course_urls:
        course_slug = urlparse(course_url).path.rsplit("/", 1)[-1]
        course_node = COURSE_NODES[course_slug]
        page = s.get(course_url)
        if not page or not page.ok:
            continue
        lessons = [u for u in links_under(page.text, course_url) if urlparse(u).path.rsplit("/", 1)[-1] not in COURSE_NODES]
        print(f"{course_slug}: {len(lessons)} lessons")
        for n, lesson_url in enumerate(lessons, 1):
            if args.max_lessons and saved >= args.max_lessons:
                break
            lesson_slug = urlparse(lesson_url).path.rsplit("/", 1)[-1]
            path = PART / "raw" / course_slug / f"{n:03d}-{lesson_slug}.md"
            if path.exists() and not args.refresh:
                continue
            resp = s.get(lesson_url)
            if not resp or not resp.ok:
                continue
            text = trafilatura.extract(resp.text, output_format="markdown", include_links=False, include_tables=True) or ""
            title_m = re.search(r"<title>(.*?)</title>", resp.text, re.S | re.I)
            title = re.sub(r"\s*[-|]\s*Babypips.*$", "", (title_m.group(1).strip() if title_m else lesson_slug))
            locked = len(text) < 400 or any(m in text.lower() for m in PAYWALL_MARKERS)
            tags = tag(f"{title}\n{text}") if not locked else {"covers": [], "speaker_ids": []}
            fm = {
                "id": f"lesson_babypips_{slug(lesson_slug)}"[:120], "type": "course", "title": title,
                "partition": "04_babypips-school-of-pipsology", "source_url": lesson_url,
                "part_of": [course_node], "covers": tags["covers"], "lesson_number": n,
                "status": "premium-locked" if locked else "scraped",
            }
            write_markdown(path, fm, text if not locked else f"# {title}\n\n_Premium lesson: not captured (no logged-in session)._")
            catalog.append({k: fm[k] for k in ("id", "title", "source_url", "status")} | {"course": course_slug})
            saved += 1
            print(f"  [{course_slug} {n}] {'LOCKED ' if locked else ''}{title[:70]}")
    write_yaml(PART / "lessons.scraped.yaml", {"lessons_index": catalog})
    print(f"done: {saved} lessons; next: python3 tools/build_graph.py")


if __name__ == "__main__":
    main()
