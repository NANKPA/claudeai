# Partition 02 — Podcasts & Landmark Interviews

| File | What |
|---|---|
| `podcasts.yaml` → `podcast-directory.md` | 16 shows: hosts, focus, rank signals from directories (FeedSpot, MillionPodcasts, CastFox) |
| `landmark-media.yaml` → `landmark-media.md` | Curated seed of landmark interviews, talks, documentaries and episodes, with verification flags, **plus the scraped view-ranked top 100** |
| `landmark-media.scraped.yaml` | The top 100 trading interviews & podcast videos by YouTube views (scraped 2026-10-11) |
| `podcast-episodes.scraped.yaml` | 4,460 episodes from 15 shows (RSS), tagged with concepts and guests |
| `raw/` | Episode show notes, one file per episode (git-ignored) |

**Scrape status (2026-10-11):** RSS catalogs captured for 15 of 16 shows
(SteadyTrade's feed was not found). 270 episodes are linked to a known guest
(show hosts and repeated sponsor/advert lines are ignored when tagging), e.g.
Tom Basso, Jerry Parker, Ray Dalio, Al Brooks, Mark Minervini, Jared Tendler.
The view-ranked top 100 comes from `tools/scrapers/youtube_top_search.py`. It
drops audiobook/summary re-uploads and weak title matches, keeps at most 4 per
query for diversity, and ranks by views. Transcripts of the videos are not
captured: YouTube blocks transcript requests from cloud servers, so run the
scraper with `--transcripts` on a home machine.

**Most consistently top-ranked shows:** Chat With Traders and Top Traders
Unplugged (FeedSpot 2026 top-2). Then Flirting with Models (quant), MacroVoices
(macro), and Words of Rizdom (the Chart Fanatics sister podcast).
