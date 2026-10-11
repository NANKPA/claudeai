---
id: channel_chart_fanatics
type: channel
title: Chart Fanatics (YouTube channel)
partition: 01_chart-fanatics
layer: L4
aliases: [Chart Fanatics, chartfanatics, CF]
hosted_by: [person_riz_iqbal]
related: [channel_chart_fanatics_live, channel_chart_academy, podcast_words_of_rizdom, synthesis_cf_playbook_patterns, concept_smart_money_concepts, concept_auction_market_theory, concept_order_flow, concept_liquidity_sweep_reversal]
sources:
  - {title: "Chart Fanatics official site", url: "https://www.chartfanatics.com/", tier: T2}
  - {title: "Chart Fanatics — Trading Strategies & Playbooks", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "Chart Fanatics YouTube", url: "https://www.youtube.com/@chart-fanatics", tier: T2}
  - {title: "OutlierKit channel analysis (third-party)", url: "https://outlierkit.com/channel/chart-fanatics", tier: T3}
  - {title: "Riz Iqbal on X", url: "https://x.com/Wordsof_Rizdom/status/1925902141010452612", tier: T4}
status: "playbooks captured (T2, 2026-10-11); video transcripts pending a home-machine scrape"
---

# Partition 01 — Chart Fanatics

> **Scrape status (2026-10-11):** all 47 written playbooks were captured from
> `chartfanatics.com/strategies` (T2) into `raw/playbooks/`, and every strategy
> note was rewritten from them. The full upload catalog was also listed:
> 1,029 uploads, made up of 50 long-form masterclasses (about 85 hours) and 979
> shorts, with view counts (`catalog.scraped.yaml`). Video transcripts are still
> pending. YouTube's bot check blocks per-video pages and transcripts from cloud
> servers, so `tools/scrapers/youtube_channel.py` must run on a home machine
> (it supports `--cookies-from-browser`).

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

The 47 first-party playbooks are analysed side by side in
[`playbook-synthesis.md`](playbook-synthesis.md). They fall into eight
families:

- ICT/SMC liquidity models (11)
- auction-market / volume-profile / order-flow models (8)
- classical price action and trend (8)
- stock momentum exhaustion and short selling (6)
- growth stocks, episodic pivots and stage analysis (4)
- options and volatility (4)
- systematic and research frameworks (3)
- psychology and trader development (3)

The typical playbook marks a level in advance and waits for a sweep,
absorption or a candle close to confirm. It puts the stop beyond the
structure that proves the idea wrong (36 of 47) and targets the next liquidity
or a return to value.

**Most-used concepts** (by `uses:` across the current notes; the generated
[`concept-frequency.md`](concept-frequency.md) is recomputed from the
strategy notes on every build): **trade management** (28), **support &
resistance** (27), **multi-timeframe analysis** (26), **position sizing**
(24), **risk:reward / R multiples** (21), **liquidity** (19), then **market
structure** and **sessions & kill zones** (18 each).

**Dominant market:** US index futures. 22 playbooks name them and NQ alone
appears in 19. Most of these are timed around the New York open: 20 playbooks
anchor to 9:30 ET or its first two hours. US stocks come second: 20 trade
shares, split between small-cap shorts and growth-stock longs. FX is a
minority (3 playbooks are built on it, and 2 order-flow traders exclude spot
FX). Options are the main vehicle in 3.

Risk rules are the weak spot. Only 4 playbooks state a per-trade % risk, none
states a weekly limit, and the 5 win-rate claims come without sample sizes
(all self-reported, T4).

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
