# Book registry fact-check (Open Library, 2026-10-11)

`tools/scrapers/books_enrich.py` looked up every book in `books.yaml` and
`../06_mathematics-foundations/math-books.yaml` on Open Library. Raw flags are in
`books.qa.txt`; enrichment (ISBNs, subjects, covers) is in `books.enriched.yaml`.

**Verdict: no wrong years or authors in the registry. Two edition notes added.**

| Flag type | Count | Review |
|---|---|---|
| YEAR mismatch | 24 | 22 are false alarms: Open Library's `first_publish_year` comes from the record with the most editions, which is often a reprint (e.g. *Market Wizards* 2012 reissue vs 1989 original; *Technical Analysis of Stock Trends* 1992 vs 1948; *The Black Swan* 2005 is a mis-match). Two were real edition nuances and are now annotated: *Trading Systems and Methods* (1978 as *Commodity Trading Systems and Methods*; current title from 1998) and Kathy Lien's book (2005 as *Day Trading the Currency Market*; current title from 2008, so the registry year is now 2008). |
| NOT FOUND | 15 | Search misses for long or subtitle-heavy titles, specialist monographs, and edited volumes. These are not evidence the books are wrong. |

Re-run with `python3 tools/scrapers/books_enrich.py`.
