---
id: channel_chart_fanatics
type: channel
title: Chart Fanatics (YouTube channel)
partition: 01_chart-fanatics
layer: L4
aliases: [Chart Fanatics, chartfanatics, CF]
hosted_by: [person_riz_iqbal]
related: [channel_chart_fanatics_live, channel_chart_academy, podcast_words_of_rizdom, concept_smart_money_concepts, concept_auction_market_theory, concept_order_flow, concept_liquidity_sweep_reversal]
sources:
  - {title: "Chart Fanatics official site", url: "https://www.chartfanatics.com/", tier: T2}
  - {title: "Chart Fanatics — Trading Strategies & Playbooks", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "Chart Fanatics YouTube", url: "https://www.youtube.com/@chart-fanatics", tier: T2}
  - {title: "OutlierKit channel analysis (third-party)", url: "https://outlierkit.com/channel/chart-fanatics", tier: T3}
  - {title: "Riz Iqbal on X", url: "https://x.com/Wordsof_Rizdom/status/1925902141010452612", tier: T4}
status: partial — synthesized from web search; transcripts pending scrape
---

# Partition 01 — Chart Fanatics

> **Scrape status:** the container that built this partition could not reach
> `youtube.com` or `chartfanatics.com` (network policy). Everything here was
> assembled from web-search results and is tiered accordingly. Run
> `tools/scrapers/youtube_channel.py` on a machine with access to pull every
> video's metadata and transcript into `raw/`, then rebuild the graph.

## Channel profile

| Field | Value | Tier |
|---|---|---|
| Format | Weekly long-form **strategy masterclasses** with guest traders; whiteboard breakdowns, live trading, Q&A | T2 |
| Positioning | "Taught by verified, consistently profitable traders"; only features traders with verified results | T2 (self-described) |
| Host | **Riz Iqbal**, also host of the *Words of Rizdom* trading podcast | T4→T2 |
| Subscribers | ~473K (third-party snapshot, date unknown) | T3 |
| Average video length | ~1h41m (third-party) | T3 |
| Topic clusters | Day trading & futures strategy masterclasses; elite guest interviews & case studies; prop-firm strategies; live-trading proof | T3 |
| Sister channel | **Chart Fanatics Live**, live-streams from guest traders (e.g., NY session with MarcoTrades) | T2 |
| Education arm | **Chart Academy**: practice, learning paths, tools (e.g., Fabio Valentini's free 5-lesson order-flow masterclass, ~1.4h) | T2 |
| Most-viewed video | "Trading LIVE with the #1 Scalper in the WORLD (EXTREME Accuracy)" with Fabio Valentini, ~3.7M views | T3 |

## What the channel teaches

See the generated [`concept-frequency.md`](concept-frequency.md) (recomputed
from the strategy notes on every build). In v1 the most-used concepts are
**market structure** (7 strategies), **multi-timeframe analysis** (5), then
**auction market theory / volume profile**, **liquidity**, **support &
resistance**, **news trading**, **scalping** and **trade execution** (4 each).
Next come liquidity sweep reversals, premium/discount/OTE and fair value gaps
(3 each).

**Dominant market:** CME index futures (NQ, ES), mostly traded through prop
firms. Secondary: FX (London session), options swing trading, US growth
stocks.

## Files

- `video-catalog.md`: known videos and episodes (seed list; the scraper
  replaces it with the full catalog).
- `strategies/`: one note per guest playbook, linked to concepts.
- `ecosystem.md`: Chart Fanatics Live, Chart Academy, Words of Rizdom.
- `raw/`: scraper output (transcripts), git-ignored.

## How to read this channel critically

1. Separate **method** (T2: usually well explained) from **performance
   claims** (T4: titles like "90% win rate", "$500K+").
2. Prefer audited results: Robbins World Cup (Fabio Valentini top-3, futures
   division), US Investing Championship (Clement Ang).
3. Re-test the rules: see `strategy_tg_capital_trident` for a case where an
   independent re-test contradicts the headline but still finds an edge.
