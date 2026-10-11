# Partition 02 — Podcasts & Landmark Interviews

| File | What |
|---|---|
| `podcasts.yaml` → `podcast-directory.md` | 16 shows: hosts, focus, rank signals from directories (FeedSpot, MillionPodcasts, CastFox) |
| `landmark-media.yaml` → `landmark-media.md` | Curated seed of landmark interviews, talks, documentaries and episodes, each with a verification flag, plus `discovery_queries` to grow it into a view-ranked **top 100** |
| `raw/` | Scraper output: episode show notes (RSS) and YouTube transcripts (git-ignored) |

**Why a seed, not a ranking:** this build ran in a sandbox that could not
reach YouTube or podcast hosts, so view counts could not be measured.
`tools/scrapers/youtube_top_search.py` runs the discovery queries, ranks by
views × relevance, and writes `landmark-media.scraped.yaml`. The graph
builder then picks the results up automatically.

**Most consistently top-ranked shows:** Chat With Traders and Top Traders
Unplugged (FeedSpot 2026 top-2). Then Flirting with Models (quant), MacroVoices
(macro), and Words of Rizdom (the Chart Fanatics sister podcast).
