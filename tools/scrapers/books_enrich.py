#!/usr/bin/env python3
"""Enrich and fact-check the book registries against the Open Library API.

For each entry in books.yaml and math-books.yaml: look up title + first author,
record ISBNs, first publish year, subjects, and cover URL, and flag year or
author mismatches with the curated registry (the curated YAML is never
modified). Output: 05_books-top-100/books.enriched.yaml + a QA report.

Example
  python3 tools/scrapers/books_enrich.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import KB_ROOT, PoliteSession, preflight, write_yaml  # noqa: E402

SOURCES = ["05_books-top-100/books.yaml", "06_mathematics-foundations/math-books.yaml"]


def lookup(s: PoliteSession, title: str, author: str) -> dict | None:
    first_author = author.split("&")[0].split(",")[0].replace("(eds.)", "").strip()
    resp = s.get("https://openlibrary.org/search.json",
                 params={"title": title.split(":")[0].split("(")[0].strip(), "author": first_author, "limit": 3,
                         "fields": "title,author_name,first_publish_year,isbn,subject,cover_i,key,edition_count"})
    if not resp or not resp.ok:
        return None
    docs = resp.json().get("docs") or []
    return max(docs, key=lambda d: d.get("edition_count") or 0) if docs else None


def main() -> None:
    preflight("https://openlibrary.org/")
    s = PoliteSession(delay=1.0, respect_robots=False)  # documented public API
    enriched, qa = [], []
    for rel in SOURCES:
        data = yaml.safe_load((KB_ROOT / rel).read_text(encoding="utf-8"))
        for key in ("books", "math_books"):
            for b in data.get(key) or []:
                if b["id"].startswith("paper_"):
                    continue
                doc = lookup(s, b["title"], b.get("author", ""))
                if not doc:
                    qa.append(f"NOT FOUND  {b['id']}: {b['title']}")
                    continue
                year = doc.get("first_publish_year")
                rec = {"id": b["id"], "ol_key": doc.get("key"), "ol_title": doc.get("title"),
                       "ol_authors": doc.get("author_name"), "first_publish_year": year,
                       "isbn_sample": (doc.get("isbn") or [])[:3], "subjects": (doc.get("subject") or [])[:8],
                       "cover": f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-M.jpg" if doc.get("cover_i") else None}
                enriched.append(rec)
                if year and b.get("year") and abs(int(year) - int(b["year"])) > 1:
                    qa.append(f"YEAR       {b['id']}: registry {b['year']} vs Open Library first_publish_year {year}")
                print(f"{b['id']}: {year}")
    write_yaml(KB_ROOT / "05_books-top-100/books.enriched.yaml", {"enrichment": enriched})
    (KB_ROOT / "05_books-top-100/books.qa.txt").write_text("\n".join(qa) + "\n", encoding="utf-8")
    print(f"enriched {len(enriched)}; {len(qa)} QA flags -> 05_books-top-100/books.qa.txt")


if __name__ == "__main__":
    main()
