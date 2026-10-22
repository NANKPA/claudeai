# Partition 01_chart-fanatics


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/README.md ===== -->

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


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/catalog.yaml ===== -->

```yaml
# Chart Fanatics catalog — seed list assembled from web search (2026-10-11).
# The YouTube scraper (tools/scrapers/youtube_channel.py) writes the full catalog
# to raw/ and catalog.scraped.yaml; this file stays as the curated seed.
# verification: confirmed = title+channel seen in a primary or first-party listing
#               third-party = seen only on an aggregator / summary site
#               announced  = seen in a host's social post announcing the episode

channels:
  - id: channel_chart_fanatics_live
    type: channel
    title: Chart Fanatics Live (YouTube)
    url: https://www.youtube.com/@chartfanaticslive
    related: [channel_chart_fanatics]
    sources:
      - {title: "Chart Fanatics Live — YouTube", url: "https://www.youtube.com/@chartfanaticslive", tier: T2}
  - id: channel_chart_academy
    type: channel
    title: Chart Academy (education platform)
    url: https://www.chartacademy.com
    related: [channel_chart_fanatics]
    sources:
      - {title: "Chart Academy — Fabio Valentini", url: "https://www.chartacademy.com/instructors/fabio-valentini", tier: T2}

media:
  - id: media_cf_fabio_live_scalper
    type: media
    title: "Trading LIVE with the #1 Scalper in the WORLD (EXTREME Accuracy)"
    youtube_id: tvERE-Beu2U
    url: https://www.youtube.com/watch?v=tvERE-Beu2U
    speaker_ids: [person_fabio_valentini]
    featured_in: [channel_chart_fanatics]
    covers: [strategy_fabio_valentini_amt_order_flow, concept_auction_market_theory, concept_order_flow, concept_scalping]
    views_approx: 4700000
    verification: confirmed
    sources:
      - {title: "videohighlight summary", url: "https://videohighlight.com/v/tvERE-Beu2U", tier: T3}
  - id: media_cf_liquidity_trap
    type: media
    title: "STEAL This EASY Liquidity TRAP Trading Strategy - $500K+ (PERFECT Sniper Entries)"
    youtube_id: DAnXM7C16h0
    url: https://www.youtube.com/watch?v=DAnXM7C16h0
    featured_in: [channel_chart_fanatics]
    covers: [concept_liquidity, concept_liquidity_sweep_reversal, concept_multi_timeframe_analysis]
    views_approx: 1300000
    verification: confirmed
    sources:
      - {title: "InfoCaptor transcript summary", url: "https://my.infocaptor.com/hub/summaries/chart-fanatics/steal-this-easy-liquidity-trap-trading-strategy-$500k+-perfect-sniper-entries-DAnXM7C16h0", tier: T3}
      - {title: "GitHub — youtube-liquidity-trap-analysis", url: "https://github.com/zitiao236-dev/youtube-liquidity-trap-analysis", tier: T3}
  - id: media_cf_marci_silfrain
    type: media
    title: "Marci Silfrain — Chart Fanatics strategy episode (World #2 futures trader)"
    youtube_id: AVVM-FyewLg
    url: https://www.youtube.com/watch?v=AVVM-FyewLg
    speaker_ids: [person_marci_silfrain]
    featured_in: [channel_chart_fanatics]
    covers: [strategy_marci_silfrain_measured_move]
    views_approx: 1100000
    verification: confirmed
    sources:
      - {title: "OutlierKit outlier videos", url: "https://outlierkit.com/channel/chart-fanatics", tier: T3}
  - id: media_cf_tg_capital
    type: media
    title: "STEAL This INSANE Simple 90% Win Rate Trading Strategy (1:20+ RR) - TG Capital"
    youtube_id: ADnslyKOwFE
    url: https://www.youtube.com/watch?v=ADnslyKOwFE
    speaker_ids: [person_tg_capital]
    featured_in: [channel_chart_fanatics]
    covers: [strategy_tg_capital_trident]
    verification: third-party
    sources:
      - {title: "TakeProfit reverse-engineering post", url: "https://takeprofit.com/posts/reverse-engineering-a-public-1-20-rr-strategy-chart-fanatics-tg-capital-51", tier: T3}
  - id: media_cf_live_marcotrades_ny
    type: media
    title: "Chart Fanatics Live Trading: New York Session With MarcoTrades"
    youtube_id: -8KwnNEPuzU
    url: https://www.youtube.com/watch?v=-8KwnNEPuzU
    speaker_ids: [person_marco_trades]
    featured_in: [channel_chart_fanatics_live]
    covers: [strategy_marco_trades_liquidity_grab]
    verification: confirmed
    sources:
      - {title: "YouTube", url: "https://www.youtube.com/watch?v=-8KwnNEPuzU", tier: T2}
  - id: media_cf_fabio_carmine_orderflow
    type: media
    title: "Order-flow traders Fabio Valentini & Carmine Rosato (Chart Fanatics episode)"
    speaker_ids: [person_fabio_valentini, person_carmine_rosato]
    featured_in: [channel_chart_fanatics]
    covers: [concept_order_flow]
    verification: third-party
  - id: media_cf_rajan_dhall
    type: media
    title: "Rajan Dhall — A+ Simple Trading Strategy & Market Auction Theory (May 2025)"
    speaker_ids: [person_rajan_dhall]
    featured_in: [channel_chart_fanatics]
    covers: [strategy_rajan_dhall_auction]
    year: 2025
    verification: announced
    sources:
      - {title: "Riz Iqbal on X", url: "https://x.com/Wordsof_Rizdom/status/1925902141010452612", tier: T4}
  - id: media_cf_gianluca_bruni
    type: media
    title: "Gianluca Bruni (2x World Trading Champion) — building statistical models around your strategy; prop-firm mastery"
    speaker_ids: [person_gianluca_bruni]
    featured_in: [channel_chart_fanatics]
    covers: [concept_backtesting, concept_position_sizing, concept_prop_firm_risk_rules]
    verification: announced
    sources:
      - {title: "Riz Iqbal on X", url: "https://x.com/Wordsofrizdom/status/2093722771998032076", tier: T4}
  - id: media_cf_andy_krieger
    type: media
    title: "Andy Krieger — the $300 Million Trade"
    speaker_ids: [person_andy_krieger]
    featured_in: [channel_chart_fanatics]
    covers: [concept_fundamental_macro_analysis, concept_position_sizing, concept_options_greeks]
    verification: third-party
  - id: media_cf_trader_kane
    type: media
    title: "Trader Kane ($2M+) — episode"
    speaker_ids: [person_trader_kane]
    featured_in: [channel_chart_fanatics]
    covers: [strategy_trader_kane_lab_model]
    verification: third-party
  - id: media_cf_ted_zhang
    type: media
    title: "Ted Zhang — managing $25 million at a young age (Nov 2025)"
    speaker_ids: [person_ted_zhang]
    featured_in: [channel_chart_fanatics, podcast_words_of_rizdom]
    year: 2025
    verification: third-party
  - id: media_cf_first_systematic_trader
    type: media
    title: "First systematic trader on Chart Fanatics & Words of Rizdom (Oct 2025)"
    featured_in: [channel_chart_fanatics, podcast_words_of_rizdom]
    covers: [concept_backtesting, concept_trend_following]
    year: 2025
    verification: announced
    sources:
      - {title: "Riz Iqbal on X", url: "https://x.com/Wordsof_Rizdom/status/1978571268598140966", tier: T4}
  - id: media_wor_50m_trader
    type: media
    title: "BEST Trading Podcast: From Losing To Consistent Profitable Trader Managing $50 Million"
    youtube_id: j2KsCD2tlcE
    url: https://www.youtube.com/watch?v=j2KsCD2tlcE
    featured_in: [podcast_words_of_rizdom]
    covers: [concept_trading_psychology]
    verification: third-party
  - id: media_wor_marci_world_2
    type: media
    title: "The World's #2 Trader | Futures Trading World Champion Marci Silfrain (Words of Rizdom)"
    speaker_ids: [person_marci_silfrain]
    featured_in: [podcast_words_of_rizdom]
    covers: [strategy_marci_silfrain_measured_move, concept_trading_psychology]
    verification: third-party
    sources:
      - {title: "Recapio digest", url: "https://recapio.com/digest/the-world-s-2-trader-futures-trading-world-champion-marci-silfrain-by-words-of-rizdom", tier: T3}
  - id: media_wor_trading_psychologist
    type: media
    title: "Trading Psychologist: Here's How I MAKE Traders Profitable Long Term (Words of Rizdom)"
    featured_in: [podcast_words_of_rizdom]
    covers: [concept_trading_psychology]
    verification: confirmed
    sources:
      - {title: "Spotify for Creators", url: "https://creators.spotify.com/pod/profile/wordsofrizdom/episodes/Trading-Psychologist-Heres-How-I-MAKE-Traders-Profitable-Long-Term-e2vb2bq", tier: T2}
```


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/concept-frequency.md ===== -->

<!-- generated by tools/render_registries.py from the YAML registries; do not edit by hand -->

# Chart Fanatics — concept frequency across guest strategies

How many Chart Fanatics strategy notes `uses:` each concept. This is a proxy for what the channel teaches most.

| Concept | # strategies | Strategies |
|---|---|---|
| Trade Management (stops, targets, breakeven, scaling, trailing) (`concept_trade_management`) | 28 | Alex Temiz, Anthony Crudele, Ariel Hernandez, Candace Lau, Clement Ang, Dhesi, Fredy Sarmiento, Gala Trades, Jay Awtani, Jeff Holden, Kris Verma, Kyle Williams, Lance Breitstein, Marci Silfrain, Marco Trades, Marios Stamatoudis, NBB Trader, Okala, Pradeep Bonde, Steven Dux, TG Capital, Tanja Trades, Ted Zhang, Tori Trades, Trader Kane, Trader Yush, Traveling Trader, Vincent Desiano |
| Support & Resistance (`concept_support_resistance`) | 27 | Alex Temiz, Ali Crooks, Anthony Crudele, Brando Elite, Carmine Rosato, Carmine Rosato, Clement Ang, Dylan O’Neil, Forrest Knight, Fredy Sarmiento, Gala Trades, Jay Awtani, Jeff Holden, Kris Verma, Kyle Williams, Marci Silfrain, Marios Stamatoudis, Okala, Pavel, Pradeep Bonde, Rajan Dhall, Steven Dux, Ted Zhang, Tori Trades, Trader Yush, Traveling Trader, Vincent Desiano |
| Multi-Timeframe Analysis (top-down) (`concept_multi_timeframe_analysis`) | 26 | Abraham Perez, Ali Crooks, Andrea Cimitan, Anthony Crudele, Ariel Hernandez, Brando Elite, Candace Lau, Clement Ang, Dhesi, Forrest Knight, Gala Trades, JJ Simon, JadeCap, Lance Breitstein, Marci Silfrain, Marco Trades, NBB Trader, Okala, Rajan Dhall, TG Capital, Tanja Trades, Ted Zhang, Tori Trades, Trader Kane, Trader Mayne, Traveling Trader |
| Position Sizing (`concept_position_sizing`) | 24 | Alex Temiz, Anthony Crudele, Ariel Hernandez, Brando Elite, Candace Lau, Carmine Rosato, Dhesi, Fabio Valentini, Fredy Sarmiento, Gala Trades, JJ Simon, Jeff Holden, Kris Verma, Kyle Williams, Lance Breitstein, Matteo Conti, Naoufel Taief, Pradeep Bonde, Steven Dux, Ted Zhang, Trader Mayne, Trader Yush, Umar Ashraf, Usman Ashraf |
| Risk:Reward & R-Multiples (`concept_risk_reward_r_multiples`) | 21 | Abraham Perez, Ali Crooks, Brando Elite, Candace Lau, Carmine Rosato, Clement Ang, Dhesi, Dylan O’Neil, Fabio Valentini, Fredy Sarmiento, Gala Trades, JJ Simon, Jay Awtani, Kyle Williams, NBB Trader, Naoufel Taief, Okala, Rajan Dhall, Steven Dux, TG Capital, Trader Mayne |
| Liquidity (resting orders, stop pools, sweeps) (`concept_liquidity`) | 19 | Abraham Perez, Andrea Cimitan, Candace Lau, Carmine Rosato, Carmine Rosato, Clement Ang, Dhesi, Forrest Knight, JadeCap, Jay Awtani, Kris Verma, Marco Trades, NBB Trader, Pavel, Steven Dux, Tanja Trades, Trader Mayne, Traveling Trader, Usman Ashraf |
| Market Structure (swings, BOS, CHoCH / MSS) (`concept_market_structure`) | 18 | Abraham Perez, Ali Crooks, Candace Lau, Clement Ang, Dhesi, Gala Trades, JJ Simon, JadeCap, Lance Breitstein, Marci Silfrain, Marco Trades, Marios Stamatoudis, NBB Trader, Tanja Trades, Ted Zhang, Tori Trades, Trader Mayne, Traveling Trader |
| Trading Sessions & Kill Zones (time-of-day edge) (`concept_trading_sessions_killzones`) | 18 | Abraham Perez, Candace Lau, Dhesi, Fabio Valentini, Fredy Sarmiento, JJ Simon, JadeCap, Kris Verma, Marco Trades, Matteo Conti, NBB Trader, Okala, Rajan Dhall, Steven Dux, TG Capital, Tanja Trades, Trader Kane, Vincent Desiano |
| Mean Reversion (`concept_mean_reversion`) | 16 | Alex Temiz, Andrea Cimitan, Anthony Crudele, Fabio Valentini, JJ Simon, Kris Verma, Kyle Williams, Lance Breitstein, Marci Silfrain, Marios Stamatoudis, Naoufel Taief, Okala, Pavel, Steven Dux, Ted Zhang, Trader Yush |
| Liquidity Sweep Reversal (stop-hunt reversal) (`concept_liquidity_sweep_reversal`) | 14 | Abraham Perez, Anthony Crudele, Ariel Hernandez, Candace Lau, Carmine Rosato, Dhesi, Dylan O’Neil, JadeCap, Marco Trades, NBB Trader, Tanja Trades, Trader Kane, Trader Mayne, Traveling Trader |
| Breakout Trading (and fakeouts) (`concept_breakout_trading`) | 14 | Ali Crooks, Andrea Cimitan, Anthony Crudele, Ariel Hernandez, Clement Ang, Dylan O’Neil, Gala Trades, Matteo Conti, Naoufel Taief, Pavel, Pradeep Bonde, Ted Zhang, Tori Trades, Vincent Desiano |
| Volatility (realized, implied, ATR, regimes) (`concept_volatility`) | 13 | Anthony Crudele, Clement Ang, Dhesi, Dylan O’Neil, Fredy Sarmiento, Kyle Williams, Lance Breitstein, Marios Stamatoudis, Matteo Conti, Naoufel Taief, Okala, Pavel, Usman Ashraf |
| Market Regimes (trend vs range, high vs low volatility) (`concept_market_regimes`) | 13 | Anthony Crudele, Ariel Hernandez, Clement Ang, Dylan O’Neil, Fabio Valentini, JJ Simon, Matteo Conti, Naoufel Taief, Okala, TG Capital, Tanja Trades, Ted Zhang, Trader Yush |
| Price Action Trading (naked charts) (`concept_price_action`) | 12 | Alex Temiz, Clement Ang, Forrest Knight, Gala Trades, Kyle Williams, Lance Breitstein, Marco Trades, Okala, Steven Dux, Tori Trades, Traveling Trader, Vincent Desiano |
| Moving Averages (SMA, EMA, stacks, crossovers) (`concept_moving_averages`) | 12 | Ali Crooks, Anthony Crudele, Ariel Hernandez, Clement Ang, Jeff Holden, Lance Breitstein, Marios Stamatoudis, Pavel, Rajan Dhall, TG Capital, Ted Zhang, Traveling Trader |
| Trend Following (`concept_trend_following`) | 12 | Anthony Crudele, Clement Ang, Fabio Valentini, Gala Trades, Marci Silfrain, Pavel, Rajan Dhall, TG Capital, Ted Zhang, Tori Trades, Trader Mayne, Trader Yush |
| Fair Value Gap (FVG), Inversion FVG, Imbalance (`concept_fair_value_gap`) | 10 | Abraham Perez, Candace Lau, Dhesi, JadeCap, NBB Trader, TG Capital, Tanja Trades, Trader Kane, Trader Mayne, Traveling Trader |
| Market Microstructure (order book, bid/ask, order types) (`concept_market_microstructure`) | 10 | Andrea Cimitan, Carmine Rosato, Dylan O’Neil, Fredy Sarmiento, Jay Awtani, Kris Verma, Kyle Williams, Matteo Conti, Pavel, Steven Dux |
| Trading Psychology & Discipline (`concept_trading_psychology`) | 10 | Brando Elite, Clement Ang, Dhesi, Fredy Sarmiento, Gala Trades, Jared Tendler, Jeff Holden, Kyle Williams, Marci Silfrain, Umar Ashraf |
| Order Flow (footprint, delta, CVD, absorption, trapped traders) (`concept_order_flow`) | 9 | Abraham Perez, Andrea Cimitan, Carmine Rosato, Carmine Rosato, Fabio Valentini, Fredy Sarmiento, Gala Trades, Jay Awtani, Trader Yush |
| Market Sentiment & Positioning (COT, contrarian signals) (`concept_market_sentiment`) | 9 | Alex Temiz, Ali Crooks, Dylan O’Neil, Kyle Williams, Lance Breitstein, Marios Stamatoudis, Rajan Dhall, Steven Dux, Ted Zhang |
| Volume Profile (POC, value area, HVN/LVN) (`concept_volume_profile`) | 8 | Abraham Perez, Andrea Cimitan, Carmine Rosato, Carmine Rosato, Fabio Valentini, Forrest Knight, Steven Dux, Trader Yush |
| News & Event Trading (`concept_news_trading`) | 8 | Brando Elite, Clement Ang, JJ Simon, Jay Awtani, Matteo Conti, Pradeep Bonde, Tanja Trades, Ted Zhang |
| VWAP (volume-weighted average price) & anchored VWAP (`concept_vwap`) | 7 | Abraham Perez, Anthony Crudele, Clement Ang, Jeff Holden, Kyle Williams, Marios Stamatoudis, Matteo Conti |
| Scalping (`concept_scalping`) | 7 | Abraham Perez, Candace Lau, Carmine Rosato, Fabio Valentini, Fredy Sarmiento, JJ Simon, Trader Yush |
| Trading Journal & Performance Review (`concept_trading_journal_review`) | 7 | Gala Trades, JadeCap, Jared Tendler, Jeff Holden, Kyle Williams, Tori Trades, Umar Ashraf |
| Auction Market Theory (balance, imbalance, value) (`concept_auction_market_theory`) | 6 | Andrea Cimitan, Carmine Rosato, Fabio Valentini, Forrest Knight, Rajan Dhall, Trader Yush |
| Trading Plan (rules written before the trade) (`concept_trading_plan`) | 6 | Gala Trades, Jared Tendler, Jeff Holden, Matteo Conti, Umar Ashraf, Vincent Desiano |
| Backtesting (manual & systematic) (`concept_backtesting`) | 6 | JJ Simon, Kris Verma, Marci Silfrain, Matteo Conti, Naoufel Taief, Pavel |
| Performance Metrics (Sharpe, Sortino, MAR, profit factor) (`concept_performance_metrics`) | 6 | Kris Verma, Matteo Conti, Naoufel Taief, Pavel, Steven Dux, Umar Ashraf |
| Trendlines & Channels (`concept_trendlines`) | 5 | Ali Crooks, Dhesi, Marci Silfrain, Tori Trades, Traveling Trader |
| Options & the Greeks (`concept_options_greeks`) | 5 | Anthony Crudele, Brando Elite, Fredy Sarmiento, Gala Trades, Usman Ashraf |
| Classical Chart Patterns (`concept_chart_patterns`) | 5 | Ariel Hernandez, Clement Ang, Dylan O’Neil, Marci Silfrain, Ted Zhang |
| SMT Divergence (correlated-market non-confirmation) (`concept_smt_divergence`) | 5 | Candace Lau, Dhesi, Dylan O’Neil, JadeCap, Trader Kane |
| Order Blocks, Breaker Blocks & Mitigation (`concept_order_blocks_breakers`) | 5 | Dhesi, JadeCap, NBB Trader, Trader Mayne, Traveling Trader |
| Japanese Candlestick Patterns (`concept_candlestick_patterns`) | 5 | Forrest Knight, Okala, Rajan Dhall, TG Capital, Vincent Desiano |
| Expectancy (expected value per trade) (`concept_expectancy`) | 5 | Jared Tendler, Lance Breitstein, Matteo Conti, Naoufel Taief, Pavel |
| Oscillators & Momentum Indicators (RSI, MACD, Stochastic, ADX) (`concept_oscillators_momentum`) | 4 | Ali Crooks, Anthony Crudele, Clement Ang, Pavel |
| Correlation & Portfolio Risk (`concept_correlation_portfolio_risk`) | 4 | Ali Crooks, Matteo Conti, Naoufel Taief, Pavel |
| Growth-Stock Momentum (CANSLIM, SEPA, VCP) (`concept_growth_momentum_canslim`) | 4 | Ariel Hernandez, Clement Ang, Pradeep Bonde, Ted Zhang |
| Premium / Discount & Optimal Trade Entry (OTE) (`concept_premium_discount_ote`) | 4 | Candace Lau, NBB Trader, Trader Kane, Trader Mayne |
| AMD / Power of Three (accumulation, manipulation, distribution) (`concept_amd_power_of_three`) | 4 | Candace Lau, NBB Trader, Tanja Trades, Trader Kane |
| Trade Execution (triggers, order types, confirmation) (`concept_trade_execution`) | 4 | Fabio Valentini, Forrest Knight, Marco Trades, Trader Yush |
| Risk of Ruin & Drawdown Math (`concept_risk_of_ruin_drawdown`) | 4 | JJ Simon, Marci Silfrain, Matteo Conti, Naoufel Taief |
| Edge (positive expectancy, repeatable) (`concept_edge`) | 4 | Matteo Conti, Pavel, Steven Dux, Umar Ashraf |
| Divergence (regular & hidden) (`concept_divergence`) | 3 | Ali Crooks, Dylan O’Neil, Traveling Trader |
| Bollinger Bands & Volatility Squeezes (`concept_bollinger_bands`) | 3 | Anthony Crudele, Lance Breitstein, Marci Silfrain |
| Fibonacci Retracements & Extensions (`concept_fibonacci`) | 3 | Anthony Crudele, Marci Silfrain, NBB Trader |
| Prop-Firm Evaluations & Risk Rules (`concept_prop_firm_risk_rules`) | 3 | Candace Lau, JJ Simon, TG Capital |
| Smart Money Concepts / ICT (umbrella) (`concept_smart_money_concepts`) | 2 | Abraham Perez, Trader Kane |
| Optimal Execution & Market Impact (Almgren-Chriss, square-root law) (`concept_optimal_execution_market_impact`) | 2 | Andrea Cimitan, Matteo Conti |
| Episodic Pivot (EP) (`concept_episodic_pivot`) | 2 | Ariel Hernandez, Pradeep Bonde |
| Fundamental & Macro Analysis (rates, central banks, growth, inflation) (`concept_fundamental_macro_analysis`) | 2 | Brando Elite, Traveling Trader |
| Intermarket Analysis & Correlations (`concept_intermarket_analysis`) | 2 | Dylan O’Neil, Tanja Trades |
| Leverage, Margin, Pips & Lots (`concept_leverage_margin`) | 2 | Jay Awtani, Usman Ashraf |
| Overfitting & Edge Validation (multiple testing, deflated Sharpe) (`concept_overfitting_validation`) | 2 | Matteo Conti, Naoufel Taief |
| Random Walk & Efficient Market Hypothesis (`concept_random_walk_efficient_markets`) | 2 | Matteo Conti, Pavel |
| Probabilistic Thinking (thinking in bets) (`concept_probabilistic_thinking`) | 2 | Matteo Conti, Steven Dux |
| Dow Theory (`concept_dow_theory`) | 1 | Abraham Perez |
| Probability, Distributions & Fat Tails (`concept_probability_fat_tails`) | 1 | Kris Verma |
| Machine Learning in Finance (labels, leakage, meta-labeling) (`concept_machine_learning_finance`) | 1 | Naoufel Taief |


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/ecosystem.md ===== -->

---
id: synthesis_chart_fanatics_ecosystem
type: synthesis
title: Chart Fanatics ecosystem (Live, Chart Academy, Words of Rizdom)
partition: 01_chart-fanatics
layer: L4
related: [channel_chart_fanatics, channel_chart_fanatics_live, channel_chart_academy, podcast_words_of_rizdom]
status: synthesized
---

# The Chart Fanatics Ecosystem

| Property | Role | Evidence |
|---|---|---|
| **Chart Fanatics** (YouTube, `@chart-fanatics`) | Flagship weekly strategy masterclasses | chartfanatics.com (T2) |
| **Chart Fanatics Live** (YouTube, `@chartfanaticslive`) | "Dedicated channel for live-streaming from the best traders in the world" | YouTube channel description (T2) |
| **chartfanatics.com/strategies** | Free written playbooks per guest | T2 |
| **Chart Academy** (chartacademy.com) | Courses, practice tools, instructor masterclasses (e.g., Fabio Valentini) | T2 |
| **Words of Rizdom** podcast (Riz Iqbal) | Long-form trader interviews; ~191 episodes since Nov 2022 per an aggregator; "only interviews verified traders" | T3 |
| **Social:** X `@chartfanatics`, Instagram, TikTok `@chartfanatics` | Clips and promos; large P&L claims here are **T4** | T4 |

## Guest roster known so far (from search)

Fabio Valentini · Carmine Rosato · Marci Silfrain · TG Capital · Marco Trades ·
Candace Lau · JJ Simon · Tanja Trades · Trader Mayne · Umar Ashraf · Tori
Trades · Brando Elite · Trader Yush · Forrest Knight · Trader Kane · Pradeep
Bonde · Andrea Cimitan · Rajan Dhall · Andy Krieger · Gianluca Bruni · Ted
Zhang · Clement Ang · Matteo Conti · Fredy Sarmiento · "Pavel" (Trading First
Principles).

See `03_legends-authorities/people.yaml` for each person's node.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/playbook-synthesis.md ===== -->

---
id: synthesis_cf_playbook_patterns
type: synthesis
title: "Chart Fanatics — Cross-Playbook Patterns (47 first-party playbooks)"
partition: 01_chart-fanatics
layer: L4
related: [channel_chart_fanatics, synthesis_unified_framework, synthesis_consensus_conflicts]
uses: [concept_trade_management, concept_support_resistance, concept_multi_timeframe_analysis, concept_position_sizing, concept_risk_reward_r_multiples, concept_liquidity, concept_market_structure, concept_trading_sessions_killzones, concept_mean_reversion, concept_liquidity_sweep_reversal, concept_breakout_trading, concept_volatility, concept_market_regimes]
status: synthesized
---

# Chart Fanatics — cross-playbook patterns (47 first-party playbooks)

**In one paragraph.** The 47 playbooks fall into eight families. The two largest are
ICT/SMC liquidity models (11) and auction-market / order-flow models (8).
Together with the intraday price-action models, they make the channel mainly a
**US index futures, New York open** school: 22 playbooks name US index
futures (18 build their rules or examples on them), NQ is named in 19, and
20 anchor their timing to the 9:30 ET cash open or its first two hours. A typical playbook marks a level in advance, waits
for price to reach it, and asks for confirmation before entering. That
confirmation is a sweep then a reversal, order-flow absorption or aggression, or
a candle close. The stop sits beyond the structure that would prove the idea
wrong (36 of 47), and the target is the next pool of liquidity or a return to
value. On risk, the playbooks are thin. Only 4 give a per-trade risk as a % of
the account, and none gives a weekly limit. Only 5 report a win rate, and none
of those comes with a sample size. Where both a win rate and an R:R are stated,
the claims range from plausible (+0.2R to +0.7R per trade) to arithmetically
implausible (+3.8R to +17.9R).

## 1. Method

- **What was analysed.** All 47 strategy notes in [`strategies/`](strategies/),
  covering 46 traders (Carmine Rosato has two pages). Every note carries
  `status: verified-t2` and was rewritten on 2026-10-11 from the trader's own
  playbook page on chartfanatics.com/strategies. Those pages are captured locally
  in `raw/playbooks/`, which is git-ignored.
- **Source tiers.** The rules in each playbook are **T2**: the trader's own
  published method. Every performance figure is **self-reported and labelled
  T4**. That covers win rates, achieved R multiples, P&L, payouts and account
  returns. Material carried over from the earlier notes, such as independent
  backtests and competition results, stays **T3** and is marked where it
  appears. Across the 47 notes the cited sources are 56 T2, 19 T3 and 2 T4.
- **How the counts were made.** Concept counts come from a script over each
  note's `uses:` and `derived_from:` frontmatter: 496 `uses` links, about 10.6
  per note. The other dimensions were coded by reading each note's *Built for*,
  *Rules*, *Risk management*, *Evidence & claims* and *What the playbook leaves
  unspecified* sections: markets, timeframes, sessions, entry triggers, stops,
  targets, risk rules and claims. A keyword pass over the same sections served as
  a cross-check. Single-label tables (family, horizon, trigger, stop, target)
  sum to 47. Multi-label counts (markets, timeframes, sessions) do not.
- **Caveat.** The performance numbers are self-reported, mostly come from
  hand-picked winning examples, and never include a sample size or test period.
  Read §8 as a list of claims to test. This note is educational analysis, not
  trading advice.

## 2. Strategy families

| Family | n | Strategies | Shared mechanics |
|---|---|---|---|
| **ICT / SMC liquidity models** | 11 | [[strategy_abraham_perez_ict_orderflow]], [[strategy_candace_lau_nq_sweep_reversal]], [[strategy_dhesi_liquidity_inversion]], [[strategy_jadecap_liquidity_volatility]], [[strategy_marco_trades_liquidity_grab]], [[strategy_nbb_trader_po3_ote_adr]], [[strategy_tanja_amd_futures]], [[strategy_tg_capital_trident]], [[strategy_trader_kane_lab_model]], [[strategy_trader_mayne_structure_ote]], [[strategy_traveling_trader_universal]] | Mark resting liquidity in advance: prior-day and session highs and lows, equal highs and lows, opening gaps. Wait for a sweep (the "manipulation" leg in the AMD/PO3 framing of 4 of them). Confirm with displacement plus an FVG, inverted FVG, breaker or structure shift. Enter on the retrace, stop beyond the swept extreme, target the opposite liquidity. Strict clock windows (London 2–5 AM ET, New York 9:30–11:30, 10:00 AM). SMT divergence between NQ and ES appears as optional confluence. |
| **Auction market theory / volume profile / order flow** | 8 | [[strategy_andrea_cimitan_amt]], [[strategy_carmine_rosato_lvn]], [[strategy_carmine_rosato_orderflow_masterclass]], [[strategy_fabio_valentini_amt_order_flow]], [[strategy_forrest_knight_volume_profile]], [[strategy_jay_awtani_market_dna]], [[strategy_rajan_dhall_auction]], [[strategy_yush_order_flow]] | Markets alternate between balance and imbalance. The volume profile supplies location: value area, POC, LVNs and volume edges. The trigger is aggression versus absorption at that location, read on the footprint, DOM, heatmap, tape or big prints. Targets are a return to value (POC, value edge) or the next node. These playbooks prefer centralised-volume markets: 7 of the 8 are intraday index futures or stocks. [[strategy_abraham_perez_ict_orderflow]] borrows this layer (Bookmap confirmation is required). |
| **Classical price action, levels & trend** | 8 | [[strategy_ali_crooks_trendline_pocket]], [[strategy_anthony_crudele_futures_trend]], [[strategy_gala_trades_price_action]], [[strategy_jj_simon_fair_pricing]], [[strategy_marci_silfrain_measured_move]], [[strategy_okala_80_20_nasdaq]], [[strategy_tori_trendline_4h]], [[strategy_vincent_desiano_break_retest]] | Hand-drawn levels, trendlines, moving averages or Bollinger environments. Confirmation is a candle close at the level: break-and-retest, bounce, rejection, or a close through a line. Targets are a fixed R or a projected move. Two NQ intraday variants use fixed point stops (JJ Simon, Okala). The swing variants (Ali, Anthony, Marci, Tori) trade daily or 4H trends. |
| **Stock momentum exhaustion & short selling** | 6 | [[strategy_alex_temiz_first_red_day]], [[strategy_kris_verma_shorting]], [[strategy_kyle_williams_first_red_day]], [[strategy_lance_breitstein_mean_reversion]], [[strategy_marios_stamatoudis_parabolic_short]], [[strategy_steven_dux_small_cap_short]] | Qualify an abnormal run with numbers (2–3+ green days; 80–100%+ for Kyle Williams, ~300% for Dux, 200/100/50% by market cap for Stamatoudis). Never short the front side. Wait for proof of failure: a break of the prior close, a VWAP loss, a lower high or a momentum shift. Stops go at the high of day, the run high or the consolidation high. Targets are an expected % fade or VWAP. Attempt caps (Kyle Williams, Marios Stamatoudis) and borrow, halt and squeeze risks recur. Lance Breitstein is the two-sided capitulation version. |
| **Growth stocks, episodic pivots & stage analysis** | 4 | [[strategy_ariel_hernandez_real_simple]], [[strategy_clement_ang_price_cycle]], [[strategy_pradeep_bonde_episodic_pivot]], [[strategy_ted_zhang_stage_analysis]] | Daily and weekly charts. Trend is defined by moving averages (10/20-day EMAs, 10–40-week SMAs). Entries come from catalyst gaps (EPs) and volume-confirmed base breakouts, with tight structural stops (low of day, prior day's low). Partials go into strength and the rest trails on a moving average. Relative strength plus market and group alignment act as filters. |
| **Options & volatility** | 4 | [[strategy_brando_options_swing]], [[strategy_dylan_oneil_vix_futures]], [[strategy_fredy_sarmiento_options_flow]], [[strategy_usman_ashraf_options]] | Options serve either as the vehicle (premium as the maximum loss, size for zero) or as information (gamma and open-interest walls as futures levels; VIX put-demand pressure as confirmation for ES). The calendar matters: FOMC, CPI, OPEX and IV crush. [[strategy_anthony_crudele_futures_trend]] also uses options on futures as its main vehicle. |
| **Systematic / algorithmic & research frameworks** | 3 | [[strategy_matteo_conti_institutional]], [[strategy_naoufel_taief_algorithmic]], [[strategy_pavel_first_principles]] | Start from a hypothesis with an economic reason, turn it into objective rules, backtest, then run out-of-sample and Monte Carlo tests. Run a portfolio of uncorrelated strategies. Keep rules few to limit overfitting, and check the expected move against costs. |
| **Psychology & trader development** | 3 | [[strategy_jared_tendler_psychology]], [[strategy_jeff_holden_momentum_model]], [[strategy_umar_ashraf_5_stage]] | Journaling as the core loop. Build one baseline playbook before adding more. Size by grade or by development stage. Behavioural stop rules (a reset limit; risk mistakes fixed before exit mistakes). |

**Concept footprint (from `uses:`).** The most-used concepts are
[[concept_trade_management]] (28), [[concept_support_resistance]] (27),
[[concept_multi_timeframe_analysis]] (26), [[concept_position_sizing]] (24),
[[concept_risk_reward_r_multiples]] (21), [[concept_liquidity]] (19),
[[concept_market_structure]] (18), [[concept_trading_sessions_killzones]] (18),
[[concept_mean_reversion]] (16), [[concept_liquidity_sweep_reversal]] (14),
[[concept_breakout_trading]] (14), [[concept_volatility]] (13) and
[[concept_market_regimes]] (13). The most common lineage roots in
`derived_from:` are [[concept_smart_money_concepts]] (9),
[[concept_auction_market_theory]] (8) and [[concept_mean_reversion]] (7). No
playbook `uses` carry trade, Elliott wave, Kelly/optimal f, pivot points,
reflexivity, stochastic processes or time-series statistics.
[[concept_wyckoff_method]] appears only as lineage, in 2 notes.

## 3. Markets & instruments

| Market | Notes naming it | Built around it (rules or worked examples) | Notes |
|---|---|---|---|
| **US index futures** (NQ, ES, S&P/Nasdaq/Russell) | 22 | 18 | 20 name the contract; in 4 (Jay Awtani, Matteo Conti, Naoufel Taief, TG Capital) they are listed but the worked examples use other markets. Carmine Rosato's two pages use index-style prices without naming one. **NQ is named in 19**, ES/S&P futures in 12. Four designs are NQ-specific: [[strategy_abraham_perez_ict_orderflow]], [[strategy_candace_lau_nq_sweep_reversal]], [[strategy_jj_simon_fair_pricing]], [[strategy_okala_80_20_nasdaq]]. |
| Futures of any kind | 32 | — | Includes header-only listings (e.g. [[strategy_steven_dux_small_cap_short]] lists futures but gives no futures rules). |
| **Single stocks (shares)** | 20 | 14 | US small caps are the core universe in 3 ([[strategy_kris_verma_shorting]], [[strategy_kyle_williams_first_red_day]], [[strategy_steven_dux_small_cap_short]]) and are included in 4 more. Growth leaders are the core universe in 4 (§2). |
| **Options** | 11 | 4 | The main vehicle in [[strategy_brando_options_swing]] (SPX), [[strategy_gala_trades_price_action]] (single-stock, short-dated) and [[strategy_usman_ashraf_options]] (education). Options on futures in [[strategy_anthony_crudele_futures_trend]]. [[strategy_fredy_sarmiento_options_flow]] uses options positioning only as a map for futures trades. |
| **FX** | 11 | 3 | Built on FX: [[strategy_ali_crooks_trendline_pocket]], [[strategy_nbb_trader_po3_ote_adr]], [[strategy_tg_capital_trident]]. Two pages explicitly **exclude** spot FX because its volume is not centralised: [[strategy_forrest_knight_volume_profile]], [[strategy_jay_awtani_market_dna]]. |
| Crypto | 10 | 1 | Usually listed as compatible. Only [[strategy_trader_mayne_structure_ote]]'s examples (BTC, SOL) are crypto. |
| Gold | 1 | 1 | [[strategy_tg_capital_trident]], which has a gold-specific close-based stop. Marci Silfrain's gold use is a T3 third-party application. |
| Other commodities (crude, platinum, metals) | 6 | 1 | Only [[strategy_tori_trendline_4h]] works examples (platinum, crude). [[strategy_matteo_conti_institutional]] suggests crude as a market to test. |
| ETFs traded | 4 | 3 | QQQ, SPY, and generic ETFs in stage analysis. |
| VIX futures | 1 | 1 | [[strategy_dylan_oneil_vix_futures]] |
| No market (frameworks) | 2 | — | [[strategy_jared_tendler_psychology]], [[strategy_umar_ashraf_5_stage]] |

**Reading.** US index futures, NQ above all, are the centre of gravity. US
equities come second, split between small-cap shorts and growth-stock longs. FX
is a minority (3 playbooks built on it), and two order-flow traders reject spot
FX on data grounds.

## 4. Timeframes and sessions

**Holding horizon (single label):**

| Horizon | n | Strategies |
|---|---|---|
| Intraday only (scalping / day trading) | 24 | All 6 exhaustion/short playbooks; 7 of 8 AMT/order-flow; 5 ICT models; JJ Simon, Okala, Gala, Vincent; Fredy; Jeff Holden |
| Intraday or swing | 7 | Dhesi, Dylan O'Neil, Forrest Knight, JadeCap, Matteo Conti, Pradeep Bonde, Traveling Trader |
| Swing / position | 11 | Ali Crooks, Anthony Crudele, Ariel Hernandez, Brando, Clement Ang, Marci Silfrain, NBB Trader, Ted Zhang, TG Capital, Tori Trades, Trader Mayne |
| Systematic (automated) | 1 | Naoufel Taief |
| Frameworks without a holding period | 4 | Jared Tendler, Pavel, Umar Ashraf, Usman Ashraf |

NBB Trader and TG Capital are labelled swing, but their entries must happen
inside intraday kill-zone windows.

**Chart timeframes named (multi-label):** Daily 25 · 5-minute 12 · 1-hour 11 ·
4-hour 9 · Weekly 8 · 15-minute 7 · 1-minute 6 · 30-minute 6 · 3-minute or
200-second 3 · seconds charts 2 · 2-minute 1 · 10-minute 1 · Monthly 1. Seventeen
notes name **no chart timeframe**. Of those, 11 are trading methods, mostly
order-flow reads (both Carmine pages, Fabio, Fredy, Jay, Kris, Yush) plus
Jeff Holden, Naoufel, Pradeep and Vincent. Three are any-timeframe methods
(Dylan, Marci, Traveling Trader) and three are non-trading frameworks. The
typical pair is a daily (sometimes 4H/1H) bias with execution on 1–5 minute
charts. That fits [[concept_multi_timeframe_analysis]] being the third most-used
concept.

**Where the entry is taken (single label):** seconds to 1-minute 6 · 2–5 minute
8 · 15–30 minute 2 · 1H–4H 3 · daily or higher 5 · order-flow tools with no chart
named 8 · intraday chart unnamed 8 · any timeframe 3 · not applicable 4.

**Sessions and time windows:**

- **20** playbooks are anchored to the **US cash open (9:30 ET) or its first one
  to two hours**. **11** state explicit clock windows.
- **6** key on **about 10:00 AM ET**: Dhesi's 10:00 four-hour candle, Trader
  Kane's 10:00 manipulation, Kris Verma's 10:00 check, Steven Dux's 10:00–11:00
  trigger, Matteo Conti's 9:30–10:00 opening range, and Tanja's 9:50–10:10 macro
  window.
- **6** avoid lunch and the afternoon, or close by midday: JadeCap, JJ Simon,
  Kris Verma, Okala, Trader Kane, Rajan Dhall.
- **4** use **London** as an entry window: Candace Lau (2:00–5:00 AM ET), NBB
  Trader (London Open 2–5 AM NY time, plus NY Open 7–10 AM and London Close
  10 AM–12 PM), TG Capital (3:00–6:30 AM NY time), and Fabio Valentini's
  mean-reversion model. Abraham Perez prefers **Asia** and New York, and rates
  London least attractive.
- Other common windows: New York 9:30–11:00 (JJ Simon) or 9:30–11:30 (JadeCap,
  Steven Dux). Kris Verma uses 4:00–10:00 AM, with the edge fading after noon.
  Matteo Conti's overnight study runs from 4:00 PM to 9:30 AM.
- **20** trading methods state **no** session window. These are mostly the swing,
  stock-exhaustion and growth playbooks. Their timing comes from catalysts or the
  daily bar instead.

## 5. Entry-trigger families

| Trigger family (primary) | n | Examples |
|---|---|---|
| **Sweep / stop-run, then reversal confirmation** (structure shift, FVG inversion, breaker, SMT, reclaim) | 9 | Candace Lau's IFVG after a London sweep; Dhesi's FVG inversion within 2–3 candles; NBB Trader's breaker + displacement, then a 0.50–0.79 retrace; Trader Kane's SMT + inversion break at 10:00; Marco Trades buying below a respected low |
| **Candle confirmation at a pre-marked level** (break-retest, bounce, rejection, signal candle) | 8 | Gala Trades' 5-minute breaking retest; Vincent Desiano's battle-zone retest; Rajan Dhall's rejection candle at the auction zone; Forrest Knight's high-volume wick at a volume edge; Okala's Fork or H at 20/80 prices; TG Capital's FVG + doji + confirmation candle; Fredy Sarmiento's rejection or reclaim at a gamma level; Traveling Trader's retrace after displacement |
| **Order-flow confirmation at a level** (absorption, aggression, big prints, tape) | 6 | Fabio Valentini's big prints at an LVN; Andrea Cimitan's failed auction plus control shift; Carmine Rosato's absorption at an LVN and stop-run reclaim; Jay Awtani's aggression overwhelming a passive wall; Trader Yush's trapped traders at an AOI |
| **Exhaustion short on an extended stock** | 5 | Alex Temiz and Kyle Williams on the break below the prior close; Marios Stamatoudis on a failed VWAP reclaim; Kris Verma shorting pops once a gap fades below the open; Steven Dux shorting the consolidation breakdown at 10:00–11:00 |
| **Base, gap or catalyst breakout** | 4 | Ariel Hernandez's first-5-minute ORB on EP days; Pradeep Bonde's market-on-open Day-1 EP; Clement Ang's 5-minute break of base resistance; Ted Zhang's Stage 2 breakout |
| **Trend pullback or trendline trigger** | 3 | Ali Crooks' 21 EMA pullback in the trendline-break pocket; Tori Trades' Action Line bounce or close-through; Marci Silfrain's Little RZY pullback |
| **Reversion to a defined mean or fair value after a turn** | 3 | Lance Breitstein's prior-bar break toward the 20-period MA; JJ Simon's displacement candle or BOS back toward fair price; Anthony Crudele's daily close below the 30% Beacon line toward 50% |
| **Systematic rule signals** | 3 | Matteo Conti's ORB close and VWAP cross; Pavel's 2× volatility expansion and 100-day high; Naoufel Taief's generated rules |
| **Filter or confirmation only (no full trigger)** | 2 | Dylan O'Neil's VIX-at-previous-day-high confirmation; Brando's level + catalyst + multi-day hold |
| **No entry model** | 4 | Jared Tendler, Umar Ashraf, Usman Ashraf, Jeff Holden (chart examples illustrate the review loop) |

Cross-cutting counts (multi-label):

- **18** name a sweep, stop run or failed breakout as an ingredient. That is the 9
  above plus Carmine Rosato (order flow), Trader Yush, Forrest Knight, Traveling
  Trader, Andrea Cimitan, Ariel Hernandez (undercut & rally), Fabio Valentini
  (mean-reversion model), Fredy Sarmiento (overshoot and reclaim) and Dylan
  O'Neil (unconfirmed breakdown).
- **13** require a **candle close** before entry. A wick or touch is not enough.
- **9** `use` [[concept_order_flow]]. Abraham Perez makes it mandatory inside an
  ICT model. Gala Trades treats Bookmap as optional.
- **13** explicitly forbid chasing. If price does not come back to the level,
  there is no trade.

## 6. Stop placement and target logic

**Stop placement (primary method):**

| Method | n | Examples |
|---|---|---|
| Beyond the level, zone, swing or setup candle that defines the trade | 16 | Beyond the LVN or aggressive print + 1–2 ticks (Fabio); beyond the DNA zone (Jay); beyond the signal-candle wick (Forrest); beyond the retest wick (Gala, Vincent); beyond the rejection candle (Rajan); below the FVG candle (TG Capital); 30–50 NQ ticks beyond an options level (Fredy) |
| Beyond the swept or manipulation extreme | 10 | Swept high or low (Abraham, Marco, JadeCap, Mayne); SMT extreme (Kane); manipulation spike (Tanja); protected high (Dhesi); fib 1.0 at the manipulation swing (NBB); flush low (Carmine Rosato) |
| Day or range reference (LOD/HOD, prior-day low, opening range, prior close) | 7 | Opening-range or Day-1 low (Pradeep, Ariel); HOD + $0.10–0.20 on shorts (Clement); high of day or run high (Kyle, Marios); a reclaim of the prior close (Alex); ORB range low (Matteo) |
| Close-based invalidation through a line or level | 3 | Daily close back above a Beacon level (Anthony); close through the trendline (Marci); close through the Safety Line (Tori) |
| Fixed distance, percentage or geometry | 5 | 10 NQ points (Okala); 25/37.5/50/75 points by account type (JJ Simon); a wide fixed % (Kris Verma); %/ATR/indicator stops (Naoufel); half the target distance (Ali, a fixed 2R) |
| Premium as the risk (no hard stop) | 2 | Size for zero (Brando); premium or level stop (Usman) |
| None given | 4 | Dylan O'Neil, Pavel (exits only by time, MA or mean), Jared Tendler, Umar Ashraf |

So **36 of 47** tie the stop to chart structure (the first four rows). Several
add that size should change rather than the stop: Dhesi, Candace (MNQ
fallback), Steven Dux (stop first, size second) and Anthony (switch to options
when the stop is too wide).

**Target logic (primary method):**

| Method | n | Examples |
|---|---|---|
| Opposing liquidity or the next level | 12 | Session or prior-day high/low and equal highs/lows (Candace, Dhesi, JadeCap, Marco, Tanja, Abraham); HTF external liquidity (Mayne); the next volume shelf (Forrest); the next options level (Fredy); HOD or the next zone (Carmine LVN); the prior intraday low (Vincent) |
| Fixed R, points or geometry | 7 | 2R (Ali); ≥2:1 (Rajan); ≥3:1 (Jay); 1.5–2R (Gala); +15 points then breakeven (Okala); fib 0.0 (NBB); mandatory system targets (Naoufel) |
| Return to value, mean or fair price | 7 | POC (Fabio); fair value (Andrea); fair price (JJ Simon); 20-period MA (Lance); 50% of the dealing range (Kane); 50% Beacon (Anthony); range midpoint and then the opposite value edge (Yush) |
| Trail or let it run (no fixed target) | 8 | Trail under daily lows (Pradeep); 10/20-day MA (Ariel); rising weekly MAs (Ted); the Safety Line (Tori); daily trend (TG); 9 EMA (Jeff); 5×–10× aim with no exit rule (Brando); partials into the flush plus a runner (Alex) |
| Projected move or expected % | 6 | Measured move (Marci); ≥−10% day for small caps (Kyle); 10–40% expected drop (Marios); 30–40% downside (Kris); 24–26% average fade (Steven Dux); 2× ADR and 8–10 ATR above the 50-day (Clement) |
| Time exits | 2 | Matteo Conti (3:30 PM, 60 days, 9:30 AM); Pavel (N-day exits) |
| None given | 5 | Carmine Rosato (order-flow masterclass), Dylan O'Neil, and the three non-trading frameworks |

**Management:** 19 take partial profits by rule, and 2 more allow them
optionally. 12 move the stop to breakeven, 2 more say only "reduce risk". 5
state an explicit minimum R:R (Candace 1:2, Ali 2R, Rajan 2:1, Mayne 2:1, Jay
3:1).

## 7. Stated risk rules

This table lists only rules the notes state. Everything else is "not specified in
the playbook".

| Trader | Risk per trade | Daily and other limits |
|---|---|---|
| Ariel Hernandez ([[strategy_ariel_hernandez_real_simple]]) | **0.5–1% of total equity**, sized from the stop distance | Exposure added only as trades and the market confirm |
| Fabio Valentini ([[strategy_fabio_valentini_amt_order_flow]]) | **0.25–0.5% of the account** | Never widen the stop; break-even early on strong CVD |
| Naoufel Taief ([[strategy_naoufel_taief_algorithmic]]) | Average loss **≤ about 0.5% of the capital allocated to each strategy** (about 0.025–0.125% of the account, derived) | 5–25% of the account per strategy; bench a strategy when its drawdown nears the Monte Carlo maximum |
| Matteo Conti ([[strategy_matteo_conti_institutional]]) | One fixed contract while developing. Live: fixed money at risk with volatility targeting. Earnings-drift model: **1–2% of the portfolio per stock** | Monte Carlo ranges trigger a review; 3–4 uncorrelated strategies |
| Jeff Holden ([[strategy_jeff_holden_momentum_model]]) | A share of the daily stop by grade: A+ ≤80%, A ≤30%, B ≤15%, C ≤5% | The daily stop is the budget; its size is not stated |
| Candace Lau ([[strategy_candace_lau_nq_sweep_reversal]]) | From the structural stop (about 20–25 NQ points in London, 30–40 in New York); MNQ when dollar risk is too high | Daily loss limit as $ or %. Example: about $3,000 on a ~$160k prop account (≈1.9%), given as an example only. Minimum 1:2 |
| Dhesi ([[strategy_dhesi_liquidity_inversion]]) | Constant dollar risk; cut contracts when the stop is 40–50 NQ points | **Two losses end the day**; a win then a loss allows a third attempt; no averaging |
| Tanja Trades ([[strategy_tanja_amd_futures]]) | Base not stated; smaller before major news and during accumulation | **Two trades per session; two losses end the day** |
| JJ Simon ([[strategy_jj_simon_fair_pricing]]) | Fixed 25/37.5/50/75-point stops, with contracts scaled inversely | Three-Loss Rule: three failed reversions end reversions for the session |
| Gala Trades ([[strategy_gala_trades_price_action]]) | A maximum dollar loss set before the order | About 2–3 trades a day; at most 2 attempts per setup; flat by the close |
| Trader Yush ([[strategy_yush_order_flow]]) | Defined before entry; smaller on aggressive entries | About 2–3 trades a day; never add to losers |
| Okala ([[strategy_okala_80_20_nasdaq]]) | Fixed 10 NQ points | Skip any setup needing a wider stop |
| Steven Dux ([[strategy_steven_dux_small_cap_short]]) | Stop first, then size down to an acceptable risk | Bounce shorts under 10% of the float and 1% of volume; first red days start at ¼ size |
| Clement Ang ([[strategy_clement_ang_price_cycle]]) | Not stated | About 3 attempts per ticker at most; no new positions into earnings without a cushion |
| Kyle Williams ([[strategy_kyle_williams_first_red_day]]) | Scaled by setup grade | 3–5 attempts at most on parabolic shorts; no new positions late in the day |
| Marios Stamatoudis ([[strategy_marios_stamatoudis_parabolic_short]]) | Not stated | 2 attempts at most; add only once the stop is at break-even; no overnight holds |
| TG Capital ([[strategy_tg_capital_trident]]) | Not stated | Trading limited to a 3.5-hour window; needs a balance-based prop drawdown |
| Brando Elite ([[strategy_brando_options_swing]]) | The whole premium is the risk ("size for zero") | No stop |
| Anthony Crudele ([[strategy_anthony_crudele_futures_trend]]) | Managed in dollars; smaller counter-trend; OTM options when the correct stop is too wide | — |
| Carmine Rosato ([[strategy_carmine_rosato_lvn]]) | Fixed dollar risk per trade (amount not stated) | — |
| Dylan O'Neil ([[strategy_dylan_oneil_vix_futures]]) | Not stated | No duplicate exposure across ES, NQ and VIX |
| Jared Tendler ([[strategy_jared_tendler_psychology]]) | No financial rule | A mid-session reset limit; breaking it ends the session |
| Umar Ashraf ([[strategy_umar_ashraf_5_stage]]) | Staged: extremely low in Stage 1, full size only in Stage 5 | — |

**Totals.**

- **4 of 47** give a per-trade risk as a % of capital (Ariel, Fabio, Naoufel,
  Matteo).
- **1** gives a daily dollar or % loss limit, and only as an example (Candace).
- **8** use loss-count, trade-count, time or behavioural daily caps.
- **5** cap re-attempts per ticker or setup.
- **0** give a weekly limit.
- Two more patterns are common: **12** size from the stop distance (constant
  dollar risk), and **12** scale size with setup quality, grade or
  conditions (for example smaller before news or against the trend).

## 8. Performance claims (T4)

Every figure in this section is self-reported (T4) unless marked T3. The
expectancy check is E = p × RR − (1 − p), in R, before costs.

| Trader | Claim | Expectancy check |
|---|---|---|
| Ali Crooks ([[strategy_ali_crooks_trendline_pocket]]) | About **58% win rate at a fixed 2:1**, from personal tracking; no sample size or period | E = 0.58 × 2 − 0.42 = **+0.74R**. Break-even is 33.3% |
| Naoufel Taief ([[strategy_naoufel_taief_algorithmic]]) | Breakout systems are typically about **40% win rate at about 2:1** (design inputs) | E = **+0.20R**. A thin margin over the 33% break-even |
| Clement Ang ([[strategy_clement_ang_price_cycle]]) | About **30% win rate**; the Affirm example moved ~20% on ~4% risk (≈5R) | Positive only if the average winner is **above 2.33R**, so the runners must carry the edge |
| JJ Simon ([[strategy_jj_simon_fair_pricing]]) | Prop payouts of $1.2M–1.8M+ (T4, from the earlier note's sources; none on the page). Third-party NQ backtest: 52% win rate and PF 1.66 after filtering (T3). A conflicting third-party figure: 20% at up to 1:4 (T3) | **+0.30R** at 52% and 1.5R; **0.00R** at 20% and 4R. The tiers and sources do not agree |
| Brando Elite ([[strategy_brando_options_swing]]) | **80% win rate** when level and catalyst align; aims for 5×–10×; one SPX call trade was said to return "seven figures" | If both held: **+3.8R to +7.8R**, which is implausible. Only a few setups a year, so the sample is tiny |
| TG Capital ([[strategy_tg_capital_trident]]) | About **90% win rate** with all rules followed; open profit swings such as +10R back to +5R; a video title claims 1:20+ | 0.9 × 20 − 0.1 = **+17.9R**, which is implausible. An independent EA re-test (T3) found about a 20% win rate, which needs an average win above 4R |
| Fabio Valentini ([[strategy_fabio_valentini_amt_order_flow]]) | Normal trades return **1:2.5 to 1:5**; the market is in balance about 70% of the time. Top-3 in the Robbins World Cup (T3) | No win rate. Break-even is 28.6% at 2.5R and 16.7% at 5R |
| Steven Dux ([[strategy_steven_dux_small_cap_short]]) | Gap-up shorts: average risk about 7%, average fade about 24–26% (described as 1:3.5–1:4) | 24–26 ÷ 7 = **3.4–3.7R** by arithmetic. Break-even is about 20–22%. No win rate given |
| Jay Awtani ([[strategy_jay_awtani_market_dna]]) | Most setups offer **4–5:1+** | No win rate. Break-even is 25% at the 3:1 minimum and 17–20% at 4–5:1 |
| NBB Trader ([[strategy_nbb_trader_po3_ote_adr]]) | The page lists ≈1.63R, 2.38R and 3.75R for entries at 50%, 62% and 70.5% | The geometry gives **1.00R, 1.63R and 2.39R** (and 3.76R at 0.79). Each listed figure belongs to the next deeper level |
| Okala ([[strategy_okala_80_20_nasdaq]]) | A built-in +15 points against a 10-point stop | 1.5R on the first scale, so break-even is 40% if everything exits there |
| Gala Trades ([[strategy_gala_trades_price_action]]) | Tesla call: about $2,400 at risk, closed for a little over $5,000 | ≈ **2.1R** on one trade; no win rate |
| Dylan O'Neil ([[strategy_dylan_oneil_vix_futures]]) | One long-VIX trade made **6R** | One trade; no stop, target or win rate given |
| Lance Breitstein ([[strategy_lance_breitstein_mean_reversion]]) | OCLR long: entry ≈ $7.25, stop ≈ $7.00, exit ≈ $7.57 | ≈ **1.3R** (derived); one trade |
| Alex Temiz ([[strategy_alex_temiz_first_red_day]]) | SMCI short: about **$50,000** on a ~$30 per share drop | No size or risk given, so no R can be computed |
| Candace Lau, Tanja Trades, Dhesi | About 40–50 NQ points in about 9 minutes (Candace); about 100 NQ points within minutes on CPI (Tanja); a 50-point idea becoming 200 points (Dhesi) | Point moves on single trades or trade designs; no win rate |
| Pradeep Bonde, Marios Stamatoudis, Kyle Williams, Ted Zhang | Stock moves: SMCI +189% in 28 days and ROOT +358% (Pradeep); SMCI −23–24% in a day (Marios); BYND +1,400% before the short (Kyle); a rare-earth ETF +25–30% (Ted) | These are moves in the stock, not the trader's P&L. Only winners are shown |
| Kris Verma ([[strategy_kris_verma_shorting]]) | A data-backed edge; a higher win rate in exchange for larger single losses; 30–40% downside targets | No statistics. Profit factor would have to be measured directly because of tail losses |
| Marci Silfrain, Trader Kane | A 320% competition return (T3) and an episode billed "$2M+" (T4), both from the earlier notes | Not on the playbook pages |

**Pattern.** **27 of 47** pages make no quantitative performance claim at all.
Only **5** pages state a win rate (Ali, Brando, Clement, TG Capital, Naoufel),
and none gives a sample size or period. The two highest win-rate claims (80%,
90%) come paired with the largest R targets (5×–20×), which is the combination
that fails the expectancy check. The one independent re-test on file (TG
Capital, T3) points the opposite way: a low win rate with large winners.

## 9. Consensus and genuine disagreements

**Consensus across the playbooks:**

| Principle | Evidence (counts from §§2–7) |
|---|---|
| **Location before trigger.** Trade only at levels marked in advance; skip the middle | [[concept_support_resistance]] in 27, [[concept_liquidity]] in 19. Explicit no-trade middles or zones: Anthony (range middle), Forrest (inside low-volume zones), Yush (mid-range), Fredy (between levels), Vincent (No Trade Zone) |
| **Confirmation over anticipation.** The sweep, the absorption, the trendline break or the first impulse is not the entry | 13 require a candle close; 18 build on a sweep or failed breakout and still wait for a reaction; 13 forbid chasing |
| **The stop goes where the idea is wrong**, and size adjusts to fit it | 36 structural stops; 12 size from the stop distance |
| **Time of day matters** | 18 `use` [[concept_trading_sessions_killzones]]; 20 anchor to the US open; 6 avoid midday |
| **Top-down context** | [[concept_multi_timeframe_analysis]] in 26; daily is the most-named chart (25) |
| **Size by quality, and cap attempts** | 12 scale size by quality, grade or conditions; 5 attempt caps; 8 daily loss or trade-count caps |
| **Bank part, protect the rest** | 19 take partials; 12 move to breakeven |
| **Regime decides the model** | [[concept_market_regimes]] in 13. Examples: Fabio's balance vs imbalance, Yush's range vs trend, Anthony's three Bollinger environments, Ted's four stages, TG Capital's EMA-stack gate |

**Genuine disagreements:**

| Question | One side | Other side |
|---|---|---|
| **Where should the stop go?** | Structure only, never comfort: Traveling Trader, Steven Dux, Jeff Holden, Dhesi | Fixed distances chosen from testing or to survive noise: JJ Simon (points by account type), Okala (10 points), Kris Verma (wide fixed %, never at the pre-market high). No hard stop at all: Brando (premium), TG Capital on gold (close filter) |
| **Win rate or payoff?** | A high win rate with larger losses accepted: Kris Verma, Kyle Williams; 80–90% claims from Brando and TG Capital | A low win rate with big winners: Clement Ang (~30%), Fabio (1:2.5–1:5), Naoufel (~40% at 2:1), and TG Capital's own T3 re-test (~20%) |
| **Manage or leave alone?** | Hands-off: Ali's fixed 2R with no trailing; Fabio's full exit at the POC | Scale and protect: Dhesi (50% plus breakeven), Gala (half), Vincent (25–50%), Okala, Clement (thirds). Breakeven timing also splits. Kane moves early and accepts many scratches. Marco never moves to breakeven before a partial. Candace tightens behind new structure rather than going straight to breakeven |
| **Is the ICT toolkit useful?** | Built on FVGs, order blocks and breakers: Candace, Dhesi, NBB, Mayne, TG Capital | Marco Trades calls BOS, order blocks and FVGs retail habits and trades raw highs, lows and time only |
| **Why do sweeps happen?** | Deliberate manipulation by a market maker (the AMD/PO3 framing in NBB, Tanja, Kane, Candace) | Mechanical liquidity events: triggered stops are market orders that cascade, so this is not intentional hunting (Andrea Cimitan) |
| **Is spot FX tradable with these tools?** | FX is the home market for Ali, NBB and TG Capital, and Pavel favours FX for long-term momentum and mean reversion | Forrest Knight and Jay Awtani exclude spot FX: its volume and depth are not centralised |
| **Indicators?** | Required tools: Anthony (Bollinger 20/3 plus a proprietary tool), TG Capital (EMA stack plus a proprietary indicator), Ted (four weekly SMAs), Clement (10/20 EMAs), Ali (21 EMA) | Price only: Marco, Okala, Tori. Jay says indicators only reflect what already happened. Pavel says a tool is not an edge |
| **Fix a bias or react?** | Set the bias before the day and trade one direction only: NBB (weekly/daily), Rajan (the prior daily candle), TG Capital (200 EMA) | Stay reactive until price reaches the area: Dhesi, Trader Yush |
| **Is news a requirement or a hazard?** | A catalyst is required: Brando, Jay, Pradeep. Tanja treats no-news days as low probability | Lance prefers extremes *without* a fundamental change. Fredy avoids OPEX, triple-witching and VIX-expiry days. Tanja herself avoids the day *before* CPI, FOMC or NFP |
| **Trade the breakout?** | Buy the break: Ariel, Pradeep, Clement, Ted; Matteo's ORB (the long side worked better) | Fabio says most breakouts inside balance fail. Andrea takes a breakout only with acceptance. Vincent never trades the break itself, only the retest |
| **Which session?** | London: Candace, NBB, TG Capital, Fabio's mean-reversion model | Abraham rates London least attractive; Fabio avoids the London open for trend trades |
| **When does psychology matter?** | Early and always: Jared Tendler (most discipline problems are emotional); Brando (mindset first) | Umar Ashraf: psychology is overrated early, and emotional overload means the size is too big |
| **Discretion or rules?** | Fully systematic with no overrides: Naoufel; objective, coded rules: Matteo | Most discretionary pages admit their patterns need judgment or are clearer in hindsight (Mayne, Tori, Marci, Okala) |

## 10. What the playbooks collectively leave unspecified

- **Sample sizes and test periods.** None of the 5 on-page win rates comes with a
  sample size, date range or instrument list.
  - Matteo Conti and Naoufel Taief describe in-sample and out-of-sample splits
    and Monte Carlo testing. Neither gives a data length, a Monte Carlo
    percentile or pass/fail thresholds.
  - Steven Dux says each setup has a known approximate win rate and frequency,
    but gives none. Kris Verma, Tori Trades and TG Capital refer to data or years
    of backtesting without showing any.
  - The only numeric sample guidance in the corpus is JJ Simon's suggestion of
    about 50 evaluation backtests.
- **Costs.** Only Pavel puts a number on costs: 0.2% round-trip against a
  0.4% or 1.5% expected move. Matteo Conti and Naoufel Taief leave slippage and
  commission assumptions open. Seven stock playbooks flag borrow, locate, SSR or
  halt handling as missing: Alex, Clement, Kyle, Lance, Marios, Pradeep, Steven.
- **Account risk.**
  - 43 give no per-trade % of capital.
  - 46 give no daily dollar or % loss limit; Candace's is an example only.
  - None gives a weekly limit.
  - Portfolio heat and the maximum number of open positions are missing from
    the multi-position stock playbooks (Ariel, Clement, Pradeep, Ted).
- **Objective thresholds.** All 47 gap lists include at least one discretionary
  term left undefined. The most common are:
  - "displacement" (Abraham, Candace, Dhesi, NBB, Tanja, Traveling Trader);
  - "absorption" or "aggression", meaning lot size, delta or print size
    (Andrea, both Carmine pages, Fabio, Jay, Yush);
  - balanced versus imbalanced (Fabio, Yush);
  - "extended" or "large" moves (JJ, Lance, Marios, Kris);
  - a "clean" or "significant" level or structure (Gala, Vincent, Mayne,
    Ted).
- **Exit management.** Most notes leave open the partial size, the trailing
  method, the runner's exit and time stops. Only Ali's fixed, hands-off 2R defines
  the exit completely. The other fixed-geometry designs (NBB, Okala, JJ Simon's
  evaluation model) still leave the partial size or the runner open.
- **Session hours.** 15 gap lists flag missing session hours, cut-off times or
  Asia/London definitions.
- **Mirror cases.** Several pages show only one side:
  - no long example: JadeCap, NBB Trader;
  - only the downside rules: Dylan O'Neil;
  - only the bearish mean-reversion trigger: Anthony Crudele;
  - short-side details missing: TG Capital, Ted Zhang.
- **Internal inconsistencies found on the pages:**
  - TG Capital: the FVG window opens before the kill zone, and the long
    confirmation rule reads inverted.
  - NBB Trader: the R table is off by one level, and the "ADR" in the title is
    never defined.
  - Okala: "four components", but five are listed.
  - Kris Verma: a window that starts at 4:00 AM, yet no pre-market entries.
  - Tanja: two different timeframes given for displacement.
  - Alex Temiz: the setup is defined by a red close but triggered intraday.
  - Trader Mayne: "OTE" in the title, but no OTE fib levels in the rules.
  - Dhesi and Steven Dux: forex or futures in the header, with no rules for
    them.
  - Ali Crooks: 21 MA and 21 EMA both used.
  - Gala Trades: a chart-level stop, but a percentage-of-premium stop is also
    mentioned.

**Implication for this knowledge base.** Treat the playbooks as well-specified
on *location* and *trigger* and under-specified on *risk*, *exits* and
*evidence*. Before relying on any of them, fill those gaps from the risk and
validation layers: [[concept_position_sizing]], [[concept_risk_of_ruin_drawdown]],
[[concept_expectancy]], [[concept_backtesting]] and
[[concept_overfitting_validation]].


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/abraham-perez-ict-orderflow.md ===== -->

---
id: strategy_abraham_perez_ict_orderflow
type: strategy
title: "Abraham Perez — Nasdaq ICT & Order Flow Scalping Strategy (NQ futures, scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [Nasdaq ICT order flow scalping, NQ ICT + Bookmap scalping, Abraham Perez NQ strategy, IFVG order-flow scalp]
taught_by: [person_abraham_perez]
featured_in: [channel_chart_fanatics]
uses: [concept_smart_money_concepts, concept_liquidity, concept_liquidity_sweep_reversal, concept_fair_value_gap, concept_market_structure, concept_dow_theory, concept_order_flow, concept_volume_profile, concept_vwap, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_risk_reward_r_multiples, concept_scalping]
derived_from: [concept_smart_money_concepts, concept_order_flow]
related: [strategy_candace_lau_nq_sweep_reversal, strategy_marco_trades_liquidity_grab, strategy_yush_order_flow]
sources:
  - {title: "Chart Fanatics — Nasdaq ICT & Order Flow Scalping Strategy (NQ)", url: "https://www.chartfanatics.com/strategies/nasdaq-ict-and-order-flow-scalping-strategy", tier: T2}
status: verified-t2
---

# Abraham Perez — Nasdaq ICT & Order Flow Scalping Strategy (NQ futures, scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/nasdaq-ict-and-order-flow-scalping-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Abraham as a discretionary Nasdaq futures scalper who combines ICT liquidity concepts, Dow Theory structure, volume analysis and Bookmap order flow. The page text uses only his first name; the surname Perez comes from this knowledge base's catalogue entry, not the playbook. The page gives no other biography.

## Built for

- **Instruments:** Nasdaq futures (NQ).
- **Style:** scalping. Discretionary, and it needs the ability to read structure, liquidity, volume and Bookmap.
- **Timeframes:**
  - Daily and 4-hour for context.
  - 1-hour and 15-minute to confirm structure.
  - 1-minute and seconds charts to refine the entry.
- **Sessions:**
  - Asia and New York are the main sessions. Asia on Nasdaq can be cleaner when everything lines up.
  - New York can be more manipulated, balanced or choppy, so it needs more patience.
  - London is usually less attractive for this approach.

## Core idea

The entry pattern is not the edge. The edge comes from knowing where liquidity is likely to be targeted, how price reacts once it is taken, and whether buyers or sellers are actually in control. The process has three steps: find the bias on higher timeframes, wait for liquidity to be taken, then enter only when structure, volume and Bookmap order flow all confirm. In the playbook's words, "liquidity can attract price, but aggression moves price."

## Rules

1. **Higher-timeframe context (Daily, 4H).** Establish the likely direction and whether price is trending or rotating. Find external liquidity (above major highs, below major lows) and the next reaction area. Ask where price is most likely to raid liquidity first. An uptrend can still raid downside liquidity before continuing, and a downtrend can raid upside liquidity. After external liquidity is taken, look for a pullback into internal liquidity or the next reaction zone.
2. **Secondary structure (1H, 15M).** Lower-timeframe structure must support the higher-timeframe idea. Look for:
   - displacement in the intended direction;
   - a strong close, not just a wick;
   - volume that shows real intent.
3. **Liquidity first.** Wait for price to take a pool rather than front-running it. Pools include prior highs and lows, equal highs and lows, obvious liquidity pools, and prior support and resistance. A sweep alone is *not* a signal: price can take liquidity and keep going.
4. **Confirmation checklist.** Before any entry, all five must be true:
   - liquidity was taken;
   - structure shifted;
   - volume supports the move;
   - order flow supports the direction;
   - Bookmap shows aggression on the correct side.

   POC or VWAP should also act as support or resistance in favour of the trade. If Bookmap looks balanced, wait.
5. **Entry model (1M or seconds chart). Pick one:**
   - **IFVG.** *Short:* liquidity is taken above, price sells off aggressively and closes below the IFVG, and order flow confirms. *Long:* sell-side liquidity is taken, price reclaims with volume and closes above the IFVG, and order flow confirms. An IFVG without order-flow support is skipped, because these fail often.
   - **Change in State of Delivery.** Price reacts at a key area and appears to continue the old direction. It then manipulates with volume, breaks the other way, and retests the broken area: failed support becomes resistance for shorts, broken resistance becomes support for longs. Enter once volume and order flow confirm the control shift.
   - **Break and retest continuation.** Price breaks a prior high or low with displacement, and a fair value gap carries the move. The retest of the broken area must close back in the continuation direction, with order flow supporting.
6. **Stop.** *Shorts:* above the swept high or the structure that invalidates the bearish idea. *Longs:* below the swept low or the invalidating structure. If POC or VWAP is reclaimed against the trade, the thesis is weakening.
7. **Targets.**
   - In choppy or uncertain conditions, such as a manipulated New York session, use a conservative target of about 1:2.
   - In clean conditions with strong order flow, hold toward the next liquidity pool or reaction area: opposing liquidity, prior highs and lows, or fair value zones.
8. **Management.** Give the trade room while POC and VWAP keep supporting it and the session is clean. Cut or reduce if aggressive volume flips against the position or the controlling side loses control.
9. **No-trade conditions.** Don't trade if any of these apply:
   - higher-timeframe context and lower-timeframe structure disagree;
   - the market is balanced with no side in control;
   - no meaningful liquidity has been taken;
   - the pattern appears without order-flow confirmation;
   - the entry would be late;
   - risk can't be clearly defined;
   - POC or VWAP works against the idea;
   - volume doesn't support the direction.

## Risk management

- **Risk per trade:** Not specified in the playbook beyond keeping risk "tight enough for a scalp".
- **Sizing:** match position size to the stop distance. No fixed % or contract count is given.
- **Invalidation:** the structure that proves the idea wrong (the swept high or low). POC or VWAP reclaiming against the trade is a warning sign.
- **Chasing:** don't enter late. If the move has run too far, the risk-to-reward no longer works.
- **Daily / weekly limits:** Not specified in the playbook.

## What the playbook leaves unspecified

- Exact Asia and New York session times, and any news filter.
- Objective thresholds for "displacement", volume that "shows intent", and Bookmap aggression (dot or print size), plus a definition of a "balanced" heatmap.
- Which POC (session, developing or composite) and which VWAP anchor.
- IFVG geometry: which timeframe's gap, and how a close "below/above the IFVG area" is measured.
- How to choose between the three entry models in real time.
- When to move to break-even, partial-profit rules, a daily loss limit, and a maximum trade count.

## Evidence & claims

- The page makes no win-rate, P&L or payout claims.
- The "~1:2" figure is a target rule for choppy conditions, not a reported result. For reference, a strict 1:2 needs a win rate above 33.3% to break even before costs.
- The two worked examples are a bearish pullback short, discussed for both Asia and New York (closer to 1:2 in New York), and an Asia continuation short. Both are described qualitatively, with no prices or numeric outcomes (T4).

## Concepts & lineage

- External vs internal liquidity, equal highs and lows, liquidity pools: [[concept_liquidity]]
- A sweep is not an automatic reversal; wait for confirmation after the raid: [[concept_liquidity_sweep_reversal]]
- IFVG and FVG-driven continuation: [[concept_fair_value_gap]]
- ICT framework, including Change in State of Delivery: [[concept_smart_money_concepts]]
- Displacement, structure shifts, break and retest: [[concept_market_structure]], [[concept_dow_theory]]
- Bookmap heatmap (passive liquidity) vs tape and dots (aggressive orders), absorption: [[concept_order_flow]]
- POC as a support or resistance filter: [[concept_volume_profile]]; VWAP as a filter: [[concept_vwap]]
- Daily/4H → 1H/15M → 1M/seconds top-down process: [[concept_multi_timeframe_analysis]]
- Asia vs New York vs London session quality: [[concept_trading_sessions_killzones]]
- Conservative 1:2 targets vs holding toward the next liquidity pool: [[concept_risk_reward_r_multiples]]
- Short-holding-period execution: [[concept_scalping]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/alex-temiz-first-red-day.md ===== -->

---
id: strategy_alex_temiz_first_red_day
type: strategy
title: "Alex Temiz — First Red Day Strategy (stocks/options, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [First Red Day, FRD short, Alex's First Red Day, red-to-green line short]
taught_by: [person_alex_temiz]
featured_in: [channel_chart_fanatics]
uses: [concept_price_action, concept_support_resistance, concept_mean_reversion, concept_market_sentiment, concept_trade_management, concept_position_sizing]
derived_from: [concept_mean_reversion]
related: [strategy_kyle_williams_first_red_day, strategy_marios_stamatoudis_parabolic_short, strategy_kris_verma_shorting]
sources:
  - {title: "Chart Fanatics — Alex’s First Red Day Trading Strategy", url: "https://www.chartfanatics.com/strategies/first-red-day", tier: T2}
status: verified-t2
---

# Alex Temiz — First Red Day Strategy (stocks/options, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/first-red-day. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook is credited to "Alex" and links to his Chart Academy instructor profile (https://www.chartacademy.com/instructors/alex-temiz). It describes shorting overextended multi-day runners on their first red day, intraday, in stocks or options. The page gives no other biography.

## Built for

- **Instruments:** stocks, and options on the same names when the options are liquid.
- **Style:** day trading. A small runner can be held for further weakness over following days.
- **Timeframes:** daily chart to qualify the multi-day run. Intraday to trigger against the previous day's close.
- **Session / time window:** the open of the First Red Day (gap up or gap down) and the intraday session after it. The page names no exchange, market hours or other window.

## Core idea

Stocks that go parabolic over several days tend to come back down. The first day the stock trades red versus the prior close is when momentum shifts, late buyers get trapped, and the drop can be fast and large. The previous day's close (the "red-to-green line") is the whole trade: below it the setup is live, and a reclaim and hold above it invalidates it. The page says the edge persists because greed and chasing at the top repeat. Extended stocks also often sell new shares in dilutive offerings, which adds supply.

## Rules

1. **Qualify the run.** The stock must be up big for **at least three consecutive days**, ideally each day stronger than the last. The move must be parabolic, extended and hyped, not a slow trend. One or two green days is not enough.
2. **Don't anticipate.** Never short just because it "should" come down. The stock has to go red first.
3. **Mark the previous day's close.** This is the key level. The trade doesn't start until price trades below it.
4. **Scenario A: gap up (the best case).** If the stock pushes higher at the open and then fades, enter when it breaks under the previous close.
5. **Scenario B: gap down.** Watch for a bounce back toward the previous close. Enter when that bounce fails and rejects the level.
6. **Starter and add.**
   - An optional small starter can go on when weakness is building. In the SMCI example, the starter went on an early break below the low of day.
   - Main size goes on only when the break below the previous close confirms.
7. **Stop.** If price reclaims the previous close and holds above it, the setup is invalid. Cut immediately.
8. **Take partial profits** by covering portions into the flush.
9. **Re-entry.** If a bounce comes but stays under the previous close, re-enter or add when the bounce fails.
10. **Hold a runner.** When momentum is clearly broken, keep a small portion for further downside. Rolled-over runners often stay weak for days or weeks.

## Risk management

- **Invalidation:** a reclaim of the previous day's close that holds above it. Exit immediately; don't hold and hope.
- **Sizing:** start small and add main size only on confirmation. Don't go too big too soon, because the edge relies on having room to scale in at the right spot.
- **Risk per trade:** Not specified in the playbook (no $ or % figure, and no tick or price buffer around the prior close).
- **Daily / weekly limits:** Not specified in the playbook.
- **Profit protection:** partial covers into the drop. Only a small portion is held as a runner.

## What the playbook leaves unspecified

- What "up big" means: a minimum % per day or in total, plus price, float, market-cap or volume filters.
- How long, or by how much, price must "hold" above the prior close before the stop is triggered.
- Where partial profits are taken (no targets such as VWAP, gap fill or % levels) and when the runner is finally covered.
- Short-sale practicalities: borrow and locate availability, halts, and squeeze risk.
- Options details: strike, expiry, and how to handle implied-volatility collapse.
- A wording ambiguity. One rule says main size goes on when price confirms "the break below red to green". The setup is consistently described as a break *below the previous close* (the red-to-green line), so that is the reading used here.
- A second wording ambiguity. The overview defines the setup as the first day the stock *closes* red, but the rules and the SMCI example trigger intraday once price trades below the previous close. The page doesn't reconcile the two.

## Evidence & claims

- **SMCI example:** after a gap up following a multi-day run, a starter went on at the break of the low of day and main size at the break of the previous close. Price then fell about $30 per share quickly, and partials were covered into the drop. The reported profit was about $50,000. Self-reported (T4).
- The page gives no win rate, R multiple, position size or risk amount, so no expectancy or R calculation is possible.
- The claims that the setup works in any market condition and is easy to execute are qualitative (T4).
- The page also notes that clean setups can be weeks or months apart, and that gap-down versions sometimes leave less room if you wait too long.

## Concepts & lineage

- The prior close as the red-to-green line, broken from above or rejected on a bounce: [[concept_support_resistance]], [[concept_price_action]]
- Parabolic multi-day extensions reverting once momentum fails: [[concept_mean_reversion]]
- Greed, FOMO, trapped late buyers and panic selling as the driver: [[concept_market_sentiment]]
- Starter-and-add scaling and keeping room to add: [[concept_position_sizing]]
- Partial covers into the flush, re-entries on failed bounces, a small runner: [[concept_trade_management]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/ali-crooks-trendline-pocket.md ===== -->

---
id: strategy_ali_crooks_trendline_pocket
type: strategy
title: "Ali Crooks — Trendline Break Pocket (forex, daily swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Trendline Break Pocket Playbook, the Pocket, trendline break pocket, Frequency & Proximity levels]
taught_by: [person_ali_crooks]
featured_in: [channel_chart_fanatics]
uses: [concept_trendlines, concept_support_resistance, concept_market_structure, concept_moving_averages, concept_breakout_trading, concept_risk_reward_r_multiples, concept_multi_timeframe_analysis, concept_divergence, concept_oscillators_momentum, concept_market_sentiment, concept_correlation_portfolio_risk]
derived_from: [concept_trendlines, concept_market_structure]
related: [strategy_tori_trendline_4h, strategy_vincent_desiano_break_retest]
sources:
  - {title: "Chart Fanatics — Trendline Break Pocket Playbook", url: "https://www.chartfanatics.com/strategies/trendline-break-pocket-strategy", tier: T2}
status: verified-t2
---

# Ali Crooks — Trendline Break Pocket (forex, daily swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/trendline-break-pocket-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Ali Crooks is a discretionary forex swing trader. He teaches an
11-lesson free masterclass on Chart Academy covering market conditions,
entries, testing, journaling and risk management. This pocket setup is one
piece of that wider system.

## Built for

- **Instruments:** forex. The pros say it works in any market with clean
  structure.
- **Style:** swing trading with minimal screen time, independent of news or
  intraday noise.
- **Analysis timeframes:** daily, plus weekly if needed, for key levels and
  trendlines.
- **Trigger timeframe:** daily by default. 4H is an optional advanced
  trigger but must still use the daily trendline and daily levels.
- **Session / time window:** not specified in the playbook.

## Core idea

Ali sorts the market into three conditions: **against the trend**
(counter-trend trades off extended levels), **with the trend** (classic
continuation) and the **Trendline Break Pocket**. The playbook trades only
the Pocket. That is the short window after price reacts from a
higher-timeframe key level, breaks a properly drawn trendline, and breaks
the last swing of the old trend. Momentum has visibly shifted at that
point, but the new trend is not yet obvious. Entry comes on a pullback to
the **21 EMA** or a breakout from a small consolidation, with a fixed
**2R** target.

## Rules

1. **Build key levels with Frequency & Proximity** on the daily or weekly
   chart.
   - *Frequency:* how often the area has been respected recently, judged by
     repeated rejecting highs or holding lows.
   - *Proximity:* what happened there most recently. If price tagged and
     respected it, the level is strong and active. If price broke through
     and chopped, it is messy.
   - **Key level** = good frequency and recently respected, the main
     location for this setup. **Proceed with caution** = only one clean
     reaction, or recent breaks; usable but with less confidence. Ignore
     mid-range areas that have been broken repeatedly.
2. **Identify the market condition.** Trade only the Pocket. Skip both the
   against-the-trend and the with-the-trend conditions.
3. **Price must reach the key level.** One overshoot (a deeper wick or
   push) is allowed. **A second overshoot voids the setup.**
4. **Draw the trendline correctly.** Anchor it at the **Price Action
   Momentum Point**, the swing that made the most recent higher high or
   lower low. If price steepens, ignore the older swing and use the more
   recent one. **A trendline break is not an entry.** It only moves the
   market into the Pocket.
5. **Confirm the momentum shift.** After the trendline breaks, price must
   break the **last lower high** (when leaving a downtrend) or the **last
   higher low** (when leaving an uptrend). No swing break, no trade.
6. **Take one of two entries only:**
   - **Entry 1, the core entry: pullback to the 21 EMA.** Price pulls back
     and touches the EMA, and the entry order sits at the EMA.
   - **Entry 2: breakout from consolidation**, used when price never comes
     fully back to the EMA. The consolidation forms after the swing break,
     on the correct side (below the broken structure for shorts, above it
     for longs), with **at least two highs and two lows**. Enter on the
     breakout.
   If any requirement is missing, skip the trade.
7. **Target and stop.** The target is the high or low that formed after the
   momentum break. The stop is placed at **half the target distance**, so
   the trade is a fixed 2R.
8. **Clean air.** Look left. If any major level, zone or structure sits
   between entry and the 2R target, skip the trade.
9. **Manage hands-off.** For standard 2R trades: no micromanagement, no
   trailing, no early exits.
10. **Optional filters to extend past 2R** (for after the base model is
    mastered). These signal that a winner may run further; they do not
    raise the win rate.
    - *MACD divergence:* for a short, price makes higher highs while MACD
      makes lower highs.
    - *Retail sentiment:* go long when retail is heavily short, short when
      retail is heavily long. An early sentiment extreme inside the Pocket
      suggests the move can run.

## Risk management

- **Reward-to-risk:** fixed **2:1**, with the stop at half the distance to
  the structural target.
- **Invalidation filters:** two overshoots of the level, no swing break, a
  consolidation with fewer than two highs and two lows, or no clean air to
  2R.
- **Risk per trade (% or $):** not specified in the playbook.
- **Daily, weekly or portfolio limits:** not specified in the playbook. The
  cons warn that **several correlated markets can trigger together**, but
  no exposure cap is given.

## What the playbook leaves unspecified

- How much risk to put on each trade, and how to handle correlated pairs
  that trigger at the same time.
- How wide a key-level zone is, and how many touches count as good
  frequency.
- The page says "21-period moving average" in one place and "21 EMA" in the
  rules. It treats them as the same thing; the rules use the EMA.
- How the 4H trigger works in practice (which consolidation, which EMA).
- Rules for extending targets past 2R when the MACD or sentiment filters
  agree: where the new target goes, and whether trailing is then allowed.
- Which retail sentiment tool to use, and what "heavily" short or long
  means.
- How long to wait for a pullback before the setup expires.

## Evidence & claims

- **"~58% win rate at 2:1"** from the trader's historical tracking of the
  setup. Self-reported (T4). No sample size, period or instruments are
  given.
- **Expectancy check:** E = p×RR − (1−p) = 0.58×2 − 0.42 = **+0.74R per
  trade** before costs, if the claim holds. Break-even at 2R needs p ≈
  33.3%.
- The swing-break rule is said to remove "90% of the fake trendline breaks"
  that trap retail traders. Self-reported (T4), with no data shown.
- The two worked examples (shorts at the 21 EMA after resistance) each
  reached the full 2R. Self-reported (T4), with no prices given.

## Concepts & lineage

- A trendline anchored at the swing that created the latest HH or LL, whose
  break signals momentum failure → [[concept_trendlines]]
- Frequency & Proximity key levels → [[concept_support_resistance]]
- Breaking the last lower high or higher low as the momentum-shift check →
  [[concept_market_structure]]
- Pullback to the 21 EMA as the core entry → [[concept_moving_averages]]
- Consolidation breakout as the second entry → [[concept_breakout_trading]]
- Fixed 2R with the stop at half the target distance →
  [[concept_risk_reward_r_multiples]]
- Daily or weekly analysis with a daily or 4H trigger →
  [[concept_multi_timeframe_analysis]]
- The MACD divergence filter → [[concept_divergence]],
  [[concept_oscillators_momentum]]
- The contrarian retail-sentiment filter → [[concept_market_sentiment]]
- Correlated pairs triggering together → [[concept_correlation_portfolio_risk]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/andrea-cimitan-amt.md ===== -->

---
id: strategy_andrea_cimitan_amt
type: strategy
title: "Andrea Cimitan — Liquidity Auction & Order Flow Strategy (futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Liquidity Auction Theory, Andrea Cimitan auction market theory, failed auction strategy, acceptance vs absorption]
taught_by: [person_andrea_cimitan]
featured_in: [channel_chart_fanatics]
uses: [concept_auction_market_theory, concept_order_flow, concept_volume_profile, concept_market_microstructure, concept_optimal_execution_market_impact, concept_liquidity, concept_mean_reversion, concept_breakout_trading, concept_multi_timeframe_analysis]
derived_from: [concept_auction_market_theory, concept_market_microstructure]
related: [strategy_fabio_valentini_amt_order_flow, strategy_rajan_dhall_auction, strategy_yush_order_flow]
sources:
  - {title: "Chart Fanatics — Liquidity Auction & Order Flow Trading Strategy", url: "https://www.chartfanatics.com/strategies/auction-market-theory-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists Auction Market Theory by Andrea Cimitan)", url: "https://www.chartfanatics.com/strategies", tier: T2}
status: verified-t2
---

# Andrea Cimitan — Liquidity Auction & Order Flow Strategy (futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/auction-market-theory-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** According to the page, Andrea Cimitan teaches this approach, which he calls "Liquidity Auction Theory", in a 17-lesson Order Flow Masterclass on Chart Academy. The masterclass covers footprint charts, volume profile, CVD and market-maker mechanics, with live ES and Nasdaq examples.

## Built for

- **Instruments:** futures. The masterclass examples are ES and Nasdaq.
- **Style:** day trading.
- **Timeframes:** a higher-timeframe volume profile and the daily candle for context. Order flow (footprint, absorption) for execution. No chart timeframe is fixed.
- **Session / time window:** no hours are stated. The worked example trades the market open and the opening range.

## Core idea

The market is treated as a continuous double auction. Limit orders provide liquidity, and price moves only when one side becomes aggressive and accepts worse prices to get filled. Urgency moves price, not a larger count of buyers or sellers. Large players split meta-orders and run them through execution algorithms such as VWAP or TWAP, so price travels in search of liquidity rather than to hunt individual stops. Markets cycle from balance (fair value) to imbalance and then to a new balance. The only question is whether the aggressive side is being *accepted* (price follows) or *absorbed* (price stalls). Trade only when the market proves one side is in control.

## Rules

1. **Build a bias.**
   - *Order-flow autocorrelation:* strong buying or selling pressure in one session raises the odds of similar behaviour in the next.
   - *Higher-timeframe context:* a daily candle moving higher suggests longer-term participants are holding positions.
2. **Locate fair value.** Use the volume profile to find where most trading happened (the value area) and whether price is inside or outside it. Then judge whether price is trying to move into imbalance.
3. **Setup 1: Failed auction below value (reversal long).**
   - Price trades below value and sellers turn aggressive, but they fail to push lower and get absorbed.
   - Absorption alone is not an entry. Enter long only once buyers clearly take control.
   - Stop below the area where sellers tried to dominate.
   - Target a return to fair value, possibly the opposite side of the range.
4. **Setup 2: Failed auction above value (reversal short).**
   - The mirror of Setup 1: buyers push above value, fail, and are absorbed by sellers.
   - Enter after seller dominance is confirmed.
   - Stop above the failed auction. Target a return to fair value.
5. **Setup 3: Breakout with acceptance (continuation).**
   - A breakout is tradable only if price holds outside the level, participation continues, and there is no immediate rejection.
   - A break that quickly returns inside is a failed auction, not a breakout.
   - Enter after real participation confirms the move. Stop below the breakout structure. Target continuation.
6. **Decision filter for every setup.** Aggressive buyers whose pushes keep moving price are in control. Aggressive buyers who appear while price doesn't rise are being absorbed. Apply the same test to sellers.
7. **Opening-range integration.** Take an ORB only when buyers dominate and price holds beyond the range. If aggressors are absorbed and price returns into the range, skip it. In the worked example, a first breakout attempt showed aggression mostly in the candle *wick* (effort without acceptance) and was skipped. A second attempt with activity in the candle *body* was taken.
8. **Stop runs.** Stop orders are market orders, so a triggered cluster cascades. Afterwards the book often thins and price often reverses. Treat these as liquidity events, not deliberate stop hunting.
9. **Manage on participation.** Hold while the controlling side stays in control. Exit when the opposite side takes over. In the example, the exit came when buyers began to be absorbed near the highs and sellers gained control.

## Risk management

- **Invalidation:** stops go where the trade idea fails, typically where the opposing side would show control again. They are not placed at arbitrary price distances.
- **Stop size:** confirmation-based entries are said to allow tighter, more efficient stops.
- **Risk per trade:** Not specified in the playbook.
- **Sizing:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.

## What the playbook leaves unspecified

- Which volume profile to use (session, prior day, composite) and the value-area percentage.
- Objective footprint, delta or CVD thresholds for "aggression", "absorption" and "control". The tools are named only in the masterclass blurb.
- How long or how far price must hold outside a level to count as "acceptance".
- The opening-range length and any time-of-day window.
- Profit-taking rules beyond "return to value" or "continuation", R targets, scaling, and trade frequency.
- Position size, risk per trade and loss limits.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- The worked example (a value-area-low reversal that aligned with the previous day's value-area low, followed by an ORB add-on) is described qualitatively, with no prices, size or outcome figures (T4).

## Concepts & lineage

- Balance → imbalance → new balance, fair value and failed auctions: [[concept_auction_market_theory]]
- Value area and value-area low/high as location: [[concept_volume_profile]]
- Aggressive vs passive orders, acceptance vs absorption, footprint and CVD: [[concept_order_flow]]
- Double auction, market makers capturing the spread, retail's small share of volume: [[concept_market_microstructure]]
- Meta-orders and VWAP/TWAP execution algorithms ("execution alpha"): [[concept_optimal_execution_market_impact]]
- Price moving to find liquidity, and stop runs as liquidity events: [[concept_liquidity]]
- Failed-auction rotations back to fair value: [[concept_mean_reversion]]
- Breakouts with acceptance and the ORB filter: [[concept_breakout_trading]]
- Daily-candle context and session-to-session autocorrelation: [[concept_multi_timeframe_analysis]]

## Changes vs. earlier note

- The earlier note (index listing only, `pending-scrape`) titled this "Auction Market Theory" and had no rules. The playbook page is titled **Liquidity Auction & Order Flow Trading Strategy**, and the title now follows it.
- **Confirmed:** auction market theory and volume profile are the foundation.
- **Added:** the microstructure framing (double auction, urgency, meta-orders, VWAP/TWAP execution, market-maker role) and the balance/imbalance cycle.
- **Added:** the three setups (failed auction below value, failed auction above value, breakout with acceptance), each with an entry condition, stop and target.
- **Added:** the acceptance-vs-absorption filter, the opening-range integration, the stop-run explanation, and the order-flow-based exit.
- **Added:** order flow, market microstructure, liquidity and breakout concepts to `uses`.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/anthony-crudele-futures-trend.md ===== -->

---
id: strategy_anthony_crudele_futures_trend
type: strategy
title: "Anthony Crudele — Futures Trend Trading Strategy: Bollinger Band Environments (index futures, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Anthony Crudele’s Futures Trend Trading Strategy", Crudele Bollinger environment model, consolidation-expansion-mean reversion framework, Beacon mean-reversion levels]
taught_by: [person_anthony_crudele]
featured_in: [channel_chart_fanatics]
uses: [concept_bollinger_bands, concept_volatility, concept_market_regimes, concept_trend_following, concept_breakout_trading, concept_mean_reversion, concept_support_resistance, concept_liquidity_sweep_reversal, concept_fibonacci, concept_multi_timeframe_analysis, concept_moving_averages, concept_vwap, concept_oscillators_momentum, concept_options_greeks, concept_position_sizing, concept_trade_management]
derived_from: [concept_bollinger_bands, concept_market_regimes]
related: [strategy_ted_zhang_stage_analysis, strategy_brando_options_swing]
sources:
  - {title: "Chart Fanatics — Anthony Crudele’s Futures Trend Trading Strategy", url: "https://www.chartfanatics.com/strategies/futures-trading-strategy", tier: T2}
status: verified-t2
---

# Anthony Crudele — Futures Trend Trading Strategy: Bollinger Band Environments (index futures, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/futures-trading-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Anthony Crudele swing trades index futures, often through options
on futures. He starts every day by classifying the market environment on
the daily chart, using Bollinger Bands and his own "Beacon" levels tool.

## Built for

- **Instruments:** futures, mainly index markets (**S&P, Nasdaq,
  Russell**). **Options on futures** are often the position vehicle.
- **Style:** swing trading, with a **1 to 5 trading day** hold. Intraday
  execution is sometimes used to refine entries.
- **Timeframes:** the **daily** chart comes first and defines everything.
  **60-minute and 30-minute** charts, and sometimes **3-minute**, are used
  only to refine entries, mainly in consolidation.
- **Indicators:** **Bollinger Bands (20, 3 standard deviations)** are
  required. **Beacon** is Anthony's tool that auto-draws mean-reversion
  Fibonacci levels between Bollinger Band peaks. **8/21/34 moving
  averages** give trend and exit context. **RSI** is optional, only to
  confirm overbought or oversold during mean reversion. **Anchored VWAP**
  is used in extreme volatility. The page lists the moving averages, RSI
  and anchored VWAP as tools not used for entries.
- **Session or time window:** not specified.

## Core idea

Identify the environment before looking for any setup. On the daily chart,
Bollinger Bands set to 3 standard deviations sort the market into
**consolidation** (bands contracting, two-way tape), **expansion** (bands
turning outward, one-directional trend) or **mean reversion** (bands
contracting after a peak, a pullback against the main trend). Each
environment sets a posture. In consolidation, trade the edges and avoid the
middle. In expansion, trade one direction only. In mean reversion, trade
the pullback to a defined 50% target, with smaller size against the main
trend. Only then drop to lower timeframes for execution.

## Rules

1. **Daily process (stated as non-negotiable).** Open the daily chart and
   read the 20-period, 3-standard-deviation Bollinger Bands:
   - **Contracting** → consolidation.
   - **Expanding** → trend or expansion.
   - **Contracting after a peak, with Beacon levels drawn** → mean
     reversion.
   Set the posture, and only then go to a lower timeframe.
2. **Consolidation (two-way tape).** The bands narrow and price becomes
   range-bound, often after a meaningful high or low. Expect false
   breakouts and stop runs past recent highs and lows that snap back into
   the range.
   - Go long or short **at the range edges only**. Never trade the middle.
   - Drop to **60-minute, 30-minute or 3-minute** charts, because
     short-term technicals matter more here.
   - Be selective. This environment chops up swing traders most.
3. **Expansion (one direction only).** The bands turn from flat to
   outward, price touches the upper band (uptrend) or lower band
   (downtrend), and the move usually begins with a breakout from the prior
   range.
   - **Bullish expansion:** long only, with no fading rallies.
   - **Bearish expansion:** short only, with no buying dips.
   - **Entry:** after the breakout or confirmation. Manage it as trend
     continuation.
   - **Targets:** larger-timeframe levels (weekly highs and lows, major
     reference points) and **"unfinished business"**: a prior Bollinger
     Band peak becomes the objective in the next directional move.
   - **Vehicle:** usually **options on futures**, calls or puts about **3
     to 5 days out**, scaled out into targets.
4. **Mean reversion (the pullback phase).** After an expansion, price stops
   extending and the bands start contracting. The method does not try to
   catch the exact top or bottom. Posture changes: after an up-expansion,
   **you are no longer long**. Trading against the main trend is allowed,
   but at **smaller size**.
   - **Levels:** Beacon applies Fibonacci-style levels to the
     **Bollinger Band peak-to-peak move** (a "fib on volatility", not on
     price) at **30%, 50% and 70%**.
   - **Bearish trigger:** a **daily close below the 30% line**. The target
     becomes the **50% line**.
   - **Action:** buy puts or short futures, and stay in until a daily
     close back above the relevant level.
   - **Exit:** once **50%** is hit, the mean-reversion objective is done.
5. **After 50% is hit: "hands in pocket."** Price may chop and consolidate
   or start a new expansion. Wait until the environment is clear again.
6. **Execution refinements.** Entries are not one-candle signals. Use
   lower-timeframe structure or order-flow tools to improve fills after
   the environment and direction are set. RSI may confirm an overbought or
   oversold condition in mean reversion but never triggers a trade.
7. **Exits and management.** The page says targets, exits and stops are
   the hardest part. Use the **8/21/34 moving averages** for exit context.
   In extreme volatility, **anchor VWAP** to the candle or level where the
   tape turned (a key high or low), and use **VWAP ±1, 2 and 3 standard
   deviation** bands as trim and exit guides. The bear-case question is
   whether price can stay below VWAP.

## Risk management

- **Sizing:** risk is managed **in dollars**, not one fixed contract. A
  wider stop means a smaller position. Sizing is called the biggest area of
  discretion.
- **Counter-trend trades:** mean-reversion trades against the main trend
  use smaller size.
- **Futures versus options:** if the correct stop (for example, above a key
  high after a gap) is too wide for futures, use **options** instead,
  often **out-of-the-money** calls or puts, so the premium caps the risk.
- **Stops:** at the structural level (above a key high or below a key low),
  or for mean-reversion futures shorts, a daily close back above the
  relevant Beacon level.
- **No-trade:** after the 50% target, or whenever the environment is
  unclear, stand aside. The page says that sometimes the correct trade is
  no trade.
- **Risk per trade ($ or % of account) and daily or weekly loss limits:**
  not specified in the playbook.

## What the playbook leaves unspecified

- An objective test for "contracting" versus "expanding" bands (bandwidth
  thresholds or slope rules) and for when consolidation turns into
  expansion.
- How Beacon chooses the two Bollinger peaks, and which band (upper,
  lower, or both) the peak-to-peak move uses. The tool is proprietary.
- The bullish mean-reversion mirror (after a down-expansion). Only the
  bearish trigger and target are written out.
- What role the **70%** level plays. It is listed but never used in a rule.
- Exact entry triggers in expansion ("after breakout or confirmation") and
  at consolidation edges.
- Options specifics beyond 3 to 5 days out and OTM: strike choice, sizing
  in premium, and when to roll or exit on time.
- Account-level risk limits and how many index markets to hold at once.
- How news and gaps are handled, beyond switching to options. The page
  lists news and volatility disrupting structure as a con.

## Evidence & claims

- The page gives **no win rate, R:R, P&L or payout**. No expectancy check is
  possible.
- The listed pros (easy to understand, less overtrading, avoids fading
  strong trends, works in bull and bear markets) are qualitative claims.
  Self-reported (T4).
- **Trade breakdown (bearish expansion into mean reversion):** a year-long
  downtrend, a band contraction, then a downside expansion that made the
  trade short-only. A gap and an extreme range made the proper stop above
  the key high too wide for futures, so out-of-the-money puts were bought.
  The page reports no outcome figure.

## Concepts & lineage

- 20-period, 3-standard-deviation Bollinger Bands to classify the
  environment → [[concept_bollinger_bands]], [[concept_volatility]]
- Consolidation, expansion and mean reversion as distinct regimes with
  their own posture → [[concept_market_regimes]]
- One-direction-only trading in expansion, launched from a range breakout
  → [[concept_trend_following]], [[concept_breakout_trading]]
- Fading range edges, and stop runs that snap back into the range →
  [[concept_support_resistance]], [[concept_liquidity_sweep_reversal]]
- Mean-reversion pullback to the 50% Beacon level →
  [[concept_mean_reversion]], [[concept_fibonacci]]
- Daily environment with 60, 30 and 3-minute execution →
  [[concept_multi_timeframe_analysis]]
- 8/21/34 moving averages for exit context → [[concept_moving_averages]]
- Anchored VWAP with standard-deviation bands for trims in high
  volatility → [[concept_vwap]]
- RSI only as an overbought or oversold confirmation →
  [[concept_oscillators_momentum]]
- Short-dated OTM options on futures as a defined-risk vehicle →
  [[concept_options_greeks]]
- Dollar-risk sizing, smaller counter-trend size, scaling out →
  [[concept_position_sizing]], [[concept_trade_management]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/ariel-hernandez-real-simple.md ===== -->

---
id: strategy_ariel_hernandez_real_simple
type: strategy
title: "Ariel Hernandez — Real Simple Swing Setups: EP, HVC, Flat Base, U&R, High Tight Flag (stocks, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Ariel’s Swing Trading Strategy", Real Simple Strategy, Ariel swing setups, "EP / HVC / flat base playbook"]
taught_by: [person_ariel_hernandez]
featured_in: [channel_chart_fanatics]
uses: [concept_episodic_pivot, concept_breakout_trading, concept_growth_momentum_canslim, concept_chart_patterns, concept_moving_averages, concept_liquidity_sweep_reversal, concept_market_regimes, concept_position_sizing, concept_trade_management, concept_multi_timeframe_analysis]
derived_from: [concept_growth_momentum_canslim, concept_episodic_pivot]
related: [strategy_pradeep_bonde_episodic_pivot, strategy_ted_zhang_stage_analysis]
sources:
  - {title: "Chart Fanatics — Ariel’s Swing Trading Strategy", url: "https://www.chartfanatics.com/strategies/real-simple-strategy", tier: T2}
status: verified-t2
---

# Ariel Hernandez — Real Simple Swing Setups: EP, HVC, Flat Base, U&R, High Tight Flag (stocks, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/real-simple-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Ariel Hernandez is a swing trader of stocks. He teaches this
system in his free "Building the Foundation" masterclass on Chart Academy,
which uses examples such as Nvidia, Palantir, Coinbase and ExxonMobil.

## Built for

- **Instruments:** stocks, and specifically leaders in strong sectors or
  groups that show signs of institutional accumulation.
- **Style:** swing trading.
- **Timeframes:** the **daily chart** makes every trade decision. The
  **5-minute chart** only refines execution, for example an opening-range
  break or a clean reclaim.
- **Market condition:** a healthy, trending broad market, plus a supportive
  sector or group.

## Core idea

Trade with the footprints of institutions: high-volume breakouts, relative
strength, and repeated strong closes near the highs. Use a small set of
repeatable price-action setups built around earnings gaps, high-volume
closes and breakout bases. Each setup has a predefined structural stop.
Position size follows the stop distance and is built up gradually, only
when the market, the group and the setup all agree. The page frames
patience as the answer to FOMO: if a move is missed, wait for the next
setup.

## Rules

**Context (every setup)**

1. On the daily chart, confirm accumulation or a valid base, a strong
   group, and a supportive market. Mark the entry and stop **in advance**.

**The six setups**

2. **Episodic Pivot (EP).** A trending stock gaps up on unexpected news or
   earnings, on volume several times its daily average.
   *Entry:* an opening range break above the high of the **first 5-minute
   bar**. *Stop:* the low of the day. *Size:* set from the entry-to-stop
   distance relative to the stock's typical daily move. Act quickly in a
   healthy market, because the strongest EP gaps often never retest.
3. **Delayed High-Volume Close (HVC).** A second chance after an EP that
   was missed. Draw a line at the close of the high-volume gap day. *Entry:*
   intraday, on any later day, as price breaks back through that close. Do
   not wait for a daily close. *Stop:* the low of the trigger day. It works
   best after several days of consolidation near the HVC.
4. **Flat Base Breakout.** A tight horizontal range lasting several weeks,
   often after a strong prior trend. The 10-day or 20-day MA tightens up to
   price, and daily ranges shrink near the breakout level. *Entry:* above
   the prior day's high, where that also clears base resistance. *Stop:*
   the prior day's low if that candle was very tight, or the low of the
   breakout day if the candle was wide or wicky.
5. **Undercut & Rally (U&R).** Price dips quickly below a clear prior low
   that holds stops, then reclaims it. *Entry:* on the reclaim. *Stop:* the
   new swing low made by the undercut. This setup is useful in corrections
   or as the market stabilises.
6. **Moving Average U&R.** Price falls below a key daily MA (10, 20 or 50
   day), then reclaims it with strength, ideally on rising volume. *Entry:*
   as price rallies back through the MA. *Stop:* the low of the reclaim
   day.
7. **High Tight Flag.** Price rises **50 to 100%** in a short time, then
   forms a tight flag near the highs for **two to five weeks** while volume
   contracts. *Entry:* a break through the upper half of the tight range.
   *Stop:* the low of the breakout day.

**Execution and management**

8. **Size.** Choose position size so a stopped-out trade costs only
   **0.5 to 1% of total equity**.
9. **Monitor.** Look for strong closes, rising volume on breakout days, and
   relative strength against the market.
10. **Take partials** into strength, especially after **three to five
    strong days**.
11. **Trail** the rest with the rising **10-day or 20-day MA**.
12. **Exit without hesitation** if the trailing stop is violated or price
    closes below key levels on high volume. In the NVDA example, the final
    exit came on a bearish reversal candle.
13. **Progressive exposure.** Add size only as trades work and the market
    trend confirms. When a group starts moving, layer into other names in
    it.

## Risk management

- **Risk per trade:** 0.5 to 1% of total equity.
- **Stops:** always structural: the low of day, the prior day's low, the
  swing low of the undercut, or the reclaim-day low, depending on the
  setup.
- **Sizing:** set from the stop distance (a tighter stop allows a larger
  position), and on EPs also relative to the stock's typical daily move.
- **Exposure:** built up gradually as trades and the market confirm.
- **Daily, weekly or portfolio heat limits:** not specified in the
  playbook.
- **Known drawback:** many small losses ("paper cuts") from tight stops, and
  weak or choppy markets produce more false breakouts.

## What the playbook leaves unspecified

- What counts as a healthy market and a strong group. No index, breadth or
  relative-strength rule is given.
- The minimum gap size and relative-volume multiple for an EP (the page
  says only "multiple times" average).
- How many weeks a flat base needs, or how tight the range must be.
- A precise definition of the upper-half breakout point for the high
  tight flag.
- What share of the position to sell as partials, and whether the trail
  uses the 10-day or the 20-day MA, or an intraday break versus a close.
- The steps of progressive exposure: how much to add, and after how many
  winners.
- The page promises five to six setups and lists six. It does not say how
  to choose when several trigger at once.

## Evidence & claims

- The page claims **no win rate, R:R, P&L or payout**. Its pros are
  qualitative: scalable, repeatable, aligned with strength, "FOMO-proof".
  All self-reported (T4).
- The NVDA flat-base example has no prices, so its outcome is only
  described in words: most of the breakout was captured.
- No expectancy check is possible.

## Concepts & lineage

- Earnings or news gap on heavy volume with an opening-range-break entry →
  [[concept_episodic_pivot]]
- Flat base, high tight flag and HVC breakouts →
  [[concept_breakout_trading]], [[concept_chart_patterns]]
- Leaders in leading groups, institutional accumulation, relative strength
  → [[concept_growth_momentum_canslim]]
- Undercut & rally shakeouts below a prior low or an MA →
  [[concept_liquidity_sweep_reversal]]
- 10, 20 and 50-day MAs for setups and trailing →
  [[concept_moving_averages]]
- Trading only in a healthy, trending market → [[concept_market_regimes]]
- Daily decisions with 5-minute execution →
  [[concept_multi_timeframe_analysis]]
- 0.5 to 1% risk, sizing by stop distance, progressive exposure →
  [[concept_position_sizing]]
- Partials after 3 to 5 strong days, MA trailing →
  [[concept_trade_management]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/brando-options-swing.md ===== -->

---
id: strategy_brando_options_swing
type: strategy
title: "Brando Elite — Options Swing Trading on HTF Levels + News Catalysts (options, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Brando's options swing strategy, Brando Elite, size for zero, level plus catalyst options swing]
taught_by: [person_brando_elite]
featured_in: [channel_chart_fanatics]
uses: [concept_support_resistance, concept_news_trading, concept_fundamental_macro_analysis, concept_multi_timeframe_analysis, concept_options_greeks, concept_position_sizing, concept_risk_reward_r_multiples, concept_trading_psychology]
derived_from: [concept_support_resistance, concept_news_trading]
related: []
sources:
  - {title: "Chart Fanatics — Brando’s Options Swing Trading Strategy", url: "https://www.chartfanatics.com/strategies/support-and-resistance", tier: T2}
status: verified-t2
---

# Brando Elite — Options Swing Trading on HTF Levels + News Catalysts (options, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/support-and-resistance. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook is credited to "Brando"; the "Brando Elite" name comes from this knowledge base's catalogue entry, not the page. He swing-trades options, and both worked examples are SPX calls. The playbook pitches the approach to options traders trying to grow smaller accounts through a few high-conviction trades.

## Built for

- **Instruments:** options, using weekly or monthly contracts. The examples are on the S&P 500 (SPX).
- **Style:** swing trading.
- **Timeframes:** weekly and daily charts for key levels. Confirmation can take several days ("multi-day hold or reclaim").
- **Session / time window:** not specified. Timing is driven by scheduled or major catalysts: FOMC, CPI/NFP, big-tech earnings, geopolitical events.

## Core idea

The largest opportunities come when price reaches a major higher-timeframe support or resistance level at the same moment a news or data catalyst supplies the volatility for a big move. Trade only when level and catalyst align, and only after the market confirms the idea. Instead of a tight stop, size the whole options position at an amount you could lose entirely ("size for zero"). That lets you hold through volatility and aim for large R multiples. The playbook puts mindset first: emotional neutrality, accepting that not every day is a trading day, and putting learning ahead of fast profits.

## Rules

1. **Mindset first.** Stay emotionally stable through wins and losses, accept that not every day is a trade day, and put learning ahead of quick money.
2. **Mark key levels on weekly and daily charts:**
   - major support and resistance from past highs, lows and reactions;
   - round psychological numbers, such as 5000, 6000 or 7000 on SPX, which act as magnets.
3. **Require a catalyst at the level.** Examples:
   - FOMC meetings;
   - CPI or NFP releases;
   - earnings, especially Nvidia or Apple;
   - geopolitical events such as tariffs or elections.

   Don't trade a level without a strong catalyst; those setups tend to fail or chop.
4. **Wait for confirmation.** At least one of:
   - a strong bounce or rejection from the level;
   - a multi-day hold or reclaim of the level;
   - a clear shift in sentiment after the catalyst.

   Even a perfect level needs the market to validate it.
5. **Instrument choice.** Weekly or monthly options. Both examples bought calls after confirmation. Example 2 entered after the election. For Example 1, the page doesn't say whether the entry came before or after the Nvidia earnings report.
6. **Size for zero.** Size the total position at what you're comfortable losing in full, instead of using a tight stop. In the page's example, rather than risking $5,000 with a 20% stop, put on a $1,000 position whose total loss is acceptable.
7. **Targets.** Hold through volatility and aim for large R multiples (5×, 10×+). The page gives no explicit exit rule.

*Example 1 (SPX long, May 2024).* After a multi-week consolidation, SPX pulled back to the psychological 5000 weekly support. It then formed two higher weekly lows. The catalysts were a large Nvidia earnings beat (the stock jumped over 25%), cooling inflation data and a stabilising labour market. Calls were bought in the 5150–5160 area after confirmation.

*Example 2 (SPX breakout, November 2024).* SPX spent months capped below 5700. After the election, it gapped up and held above 5700. Calls were bought once price reclaimed and stabilised above the level.

## Risk management

- **Sizing:** "size for zero". The maximum loss is the full premium paid, and the position is sized so that loss is acceptable.
- **Stop-loss:** no tight stop. The position is sized so it can go to zero, and the page says this avoids premature exits. No other stop rule is given.
- **Risk per trade as % of account:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.
- **Trade filtering:** no level-without-catalyst trades. The page accepts that some years have only a few ideal setups.

## What the playbook leaves unspecified

- Strike and delta selection, the choice between weekly and monthly expiry, and handling theta decay and post-event IV crush.
- Exit and profit-taking rules: when to take 5× or 10×, partials, time stops, and what to do if the level fails after entry.
- How many days of "multi-day hold" count as confirmation, and an objective definition of a "key level".
- The maximum premium per trade as a % of account, and how many concurrent positions to hold.
- Whether entries can come before a catalyst. Example 2 entered after the election; Example 1's entry timing relative to the Nvidia report isn't stated.

## Evidence & claims

- **Win rate:** 80% when technicals and news align. Self-reported (T4).
- **Target R multiples:** 5× and 10×+ are stated as aims, not as realized averages.
  - If an 80% win rate and 5R winners held at the same time: E = 0.8 × 5 − 0.2 = **+3.8R per trade**.
  - At 10R: E = 0.8 × 10 − 0.2 = **+7.8R**.
  - Both figures are implausibly high. The two claims very likely don't apply together, since a "win" may be any profit rather than a 5R+ result.
- **Example 1:** SPX rallied over 200 points in two weeks, and the position "returned over seven figures in gains". Self-reported (T4); no position size or cost given.
- **Example 2:** SPX rallied over 400 points within a month, peaking near 6147. That is the index move, not a reported P&L (T4).
- **Frequency:** only a few ideal setups a year, so any win-rate figure rests on a small sample.

## Concepts & lineage

- Weekly and daily support/resistance and round psychological numbers: [[concept_support_resistance]], [[concept_multi_timeframe_analysis]]
- FOMC, CPI/NFP, earnings and elections as the volatility trigger: [[concept_news_trading]], [[concept_fundamental_macro_analysis]]
- Long calls with weekly or monthly expiries; theta decay, gamma and IV crush around catalysts are risks the trader must manage, though the playbook doesn't discuss them: [[concept_options_greeks]]
- "Size for zero" (premium at risk instead of a stop): [[concept_position_sizing]]
- Targeting 5×–10×+ R multiples: [[concept_risk_reward_r_multiples]]
- Emotional neutrality and patience as foundations: [[concept_trading_psychology]]

## Changes vs. earlier note

- **Confirmed:** options swing trading built on higher-timeframe support/resistance plus news catalysts (the earlier T2 summary).
- **Added:**
  - weekly or monthly contracts;
  - round-number levels (SPX 5000/6000/7000);
  - the catalyst list (FOMC, CPI/NFP, earnings, geopolitics);
  - the three confirmation conditions;
  - the "size for zero" sizing rule in place of stops;
  - the 5×–10×+ R targets;
  - the two SPX trade examples;
  - the self-reported 80% win rate.
- **Still open:** the earlier note marked strike, expiry, delta targets and exits as pending. The playbook now gives weekly or monthly expiries, but strike, delta and exit rules **remain unspecified**.
- **Kept:** the earlier note's warning about theta decay vs gamma and IV crush. It is kept as an analyst caveat under Concepts, not as a playbook rule.
- **Kept:** the earlier note's single Chart Fanatics T2 source. Added `derived_from` and an empty `related` list.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/candace-lau-nq-sweep-reversal.md ===== -->

---
id: strategy_candace_lau_nq_sweep_reversal
type: strategy
title: "Candace Lau — NQ Liquidity Sweep & IFVG Reversal (NQ futures, scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [NQ Liquidity Sweep & IFVG Scalping Strategy, NQ Liquidity Sweep & Reversal Scalping Strategy, Candace Lau strategy, NQ liquidity sweep reversal]
taught_by: [person_candace_lau]
featured_in: [channel_chart_fanatics]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_premium_discount_ote, concept_fair_value_gap, concept_market_structure, concept_multi_timeframe_analysis, concept_amd_power_of_three, concept_trading_sessions_killzones, concept_smt_divergence, concept_scalping, concept_risk_reward_r_multiples, concept_trade_management, concept_position_sizing, concept_prop_firm_risk_rules]
derived_from: [concept_smart_money_concepts, concept_amd_power_of_three]
related: [strategy_marco_trades_liquidity_grab, strategy_trader_kane_lab_model, strategy_tanja_amd_futures]
sources:
  - {title: "Chart Fanatics — NQ Liquidity Sweep & IFVG Scalping Strategy", url: "https://www.chartfanatics.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists NQ Liquidity Sweep & Reversal Scalping Strategy by Candace Lau)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "TradeZella — NQ Liquidity Sweep & Reversal Scalping Strategy", url: "https://www.tradezella.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy", tier: T3}
status: verified-t2
---

# Candace Lau — NQ Liquidity Sweep & IFVG Reversal (NQ futures, scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/nq-liquidity-sweep-reversal-scalping-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Candace Lau scalps NQ futures, taking reversals after liquidity
sweeps in the London and New York sessions. The page text itself does not
name her or describe her background (attribution comes from the index
listing); its risk section uses a prop-account example.

## Built for

- **Instruments:** futures, specifically NQ. MNQ is the fallback when the
  structural stop would mean too many dollars at risk. ES is used only as an
  SMT comparison.
- **Style:** scalping.
- **Timeframes:** Daily and 1H for context and targets. **1-minute** for
  execution. 15-second and 3-second charts to judge the speed of
  displacement and to refine aggressive entries. Suggested learning order:
  5-minute, then 1-minute, then seconds charts.
- **Sessions:** **London, about 2:00 to 5:00 AM ET**. Never enter before
  2:00, and watch 2:30, 3:00 and 3:30 for expansion. **New York** uses the
  same model in a faster, more volatile setting, especially around the
  open.

## Core idea

NQ often reverses after it takes a meaningful pool of liquidity. Build
context on the higher timeframes, mark the liquidity price is likely to
target, and wait for the sweep. The sweep itself is not the entry. Enter
only when the reversal is confirmed by an **Inversion Fair Value Gap
(IFVG)** together with **fast, decisive displacement**, then aim for the
next low-resistance liquidity. The page frames the sequence as
accumulation, manipulation (the sweep) and distribution. The Asia-to-London
transition is a prime place to read it.

## Rules

1. **Higher-timeframe context (Daily, 1H).** Mark Daily and 1H highs and
   lows, Daily and 1H FVGs (the **1H FVG** gets special weight), the prior
   session's and prior day's liquidity, and equal highs and lows.
2. **Premium or discount.** Note where price sits in the relevant range.
   This is context only, not a signal.
3. **Find the liquidity pool.** For a long, sell-side liquidity below
   price. For a short, buy-side liquidity above it. In London the Asia
   range high and low are the default. If Asia already trended, use
   earlier highs and lows, Daily or 1H liquidity, FVGs, the Midnight Open,
   or the NDOG and NWOG (new day and new week opening gaps) instead.
4. **Respect the window.** London 2:00 to 5:00 AM ET, with no entries
   before 2:00. In New York, also map the **RTH gap** at its 25%, 50%, 75%
   and 100% levels, and use **NQ against ES SMT divergence** at key highs
   and lows as supporting confluence only.
5. **Wait for the sweep.** Price must actually take the identified
   liquidity. Price can sweep and keep going, so a sweep alone is never an
   entry.
6. **IFVG confirmation.** In a bullish case, price leaves a bearish FVG on
   the way down into sell-side liquidity. After the sweep, it trades back
   up and closes through that gap, which turns it into a bullish IFVG. A
   bearish case is the mirror image.
   - *Conservative:* require a clear candle-body close through the original
     FVG. A slight poke through it does not count.
   - *Aggressive:* use seconds charts to spot displacement and a smaller
     inversion forming before the 1-minute confirmation completes. This
     gives an earlier entry and possibly a tighter stop, with less
     confirmation.
7. **Displacement and speed.** The reaction away from the sweep must be
   fast and decisive. Do not judge it from the finished candle alone,
   because a big candle can still have formed slowly and choppily.
8. **Entry.** On a retracement into the inversion area, on the 1-minute
   chart. A bracket order can set the stop and first target at entry.
9. **Stop.** Beyond the structure that invalidates the setup: the relevant
   swing, the manipulation extreme, or a supporting order block. Size it to
   volatility. Examples given are about **20 to 25 NQ points in London,
   30 to 40 in New York, and about 15 in quieter periods**, described as
   examples rather than fixed values. If a valid entry needs an excessively
   wide stop, rethink the entry. If the stop is correct but the dollar risk
   is too large, cut size or switch to MNQ.
10. **Target.** Low-resistance liquidity in the direction of the trade:
    opposite swing highs or lows, equal highs or lows, 1H FVGs, session
    liquidity, the Midnight Opening Price, NDOG or NWOG, and RTH gap levels
    in New York. **At least 1:2 R:R.** Set the bracket at about 1:2 and
    widen it to 1:3 or 1:4 when the liquidity target allows. Take the
    planned scalp; there is no need to hold for the whole session move.
11. **Manage.** Once price confirms and takes minor liquidity, tighten the
    stop behind the newly formed structure. This need not mean an instant
    move to breakeven. The pattern is entry, confirmation, minor liquidity
    taken, reduced risk, target or partial, then trail the rest. Decide the
    profit-taking method (fixed target, partials or trailing) in advance
    and test which works best.
12. **Size by quality.** A setup with more aligned references (HTF FVGs,
    equal highs or lows, session liquidity, gap levels) can carry more
    conviction. A weaker one, with fewer confluences, nearby unresolved
    liquidity, a late entry or worse R:R, gets smaller size, less scaling
    and more conservative profit-taking.

## Risk management

- **Daily limit:** set it as a maximum dollar or % loss rather than a fixed
  number of trades. In one prop example, an account of about **$160,000**
  (after building a buffer) ran a daily loss limit of about **$3,000**. The
  page says this is an example, not a recommendation.
- **Personal capital:** risk a percentage of the account. The exact % is
  not specified in the playbook.
- **Prop accounts:** set position size with drawdown, consistency rules and
  account size in mind.
- **Per-trade risk:** comes from the structural stop and adjusts with
  volatility. A fixed $ or % per trade is not specified in the playbook.
- **Minimum reward-to-risk:** 1:2.

## What the playbook leaves unspecified

- An objective test for "displacement and speed", such as a time or
  distance threshold.
- How the premium and discount range is drawn (which swing points) and
  whether a trade must sit in discount for longs or premium for shorts.
- New York session hours beyond "around the open", and a cutoff time for
  London after 5:00 AM.
- How many trades are allowed per session, and what to do after a loss.
- How many confluences make a setup "stronger", and how size changes with
  that grade.
- The size of partials and the rules for trailing, which the page leaves
  to the trader's own testing.

## Evidence & claims

- **London bearish example:** about **40 to 50 NQ points in about nine
  minutes**, closed at the planned liquidity target. Self-reported (T4).
- The page gives **no win rate**. The 1:2 minimum, widened to 1:3 or 1:4,
  is a rule, not a reported result. At 1:2 the break-even win rate is
  about 33%. Without a stated win rate, no expectancy check is possible.
- The ~$3,000 daily limit on a ~$160k account describes how risk was
  managed, not a P&L claim.

## Concepts & lineage

- Swing, equal and session highs and lows as liquidity pools; low-resistance
  liquidity as targets → [[concept_liquidity]]
- Sweep, then confirmed reversal → [[concept_liquidity_sweep_reversal]]
- Accumulation, manipulation, distribution; Asia range swept in London →
  [[concept_amd_power_of_three]]
- FVG to IFVG inversion as the entry structure, with 1H FVGs as context and
  targets → [[concept_fair_value_gap]]
- Displacement and closes through structure → [[concept_market_structure]]
- Premium and discount framing → [[concept_premium_discount_ote]]
- Daily and 1H context with 1-minute and seconds-chart execution →
  [[concept_multi_timeframe_analysis]]
- The London 2:00 to 5:00 AM ET window and New York open timing →
  [[concept_trading_sessions_killzones]]
- NQ against ES at key highs and lows → [[concept_smt_divergence]]
- Bracket orders, 1:2 minimum widened to 1:3 or 1:4 →
  [[concept_risk_reward_r_multiples]], [[concept_scalping]]
- Reducing risk behind new structure, partials and trailing →
  [[concept_trade_management]]
- Size by setup quality, MNQ fallback, daily dollar limit →
  [[concept_position_sizing]], [[concept_prop_firm_risk_rules]]
- Lineage: ICT-style smart-money concepts → [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **Five-step rule order confirmed.** The earlier note's sequence (HTF and
  premium/discount, then liquidity pool, then sweep, then IFVG with
  displacement and speed, then lower-timeframe execution) came from T3
  sources. The playbook now confirms it at T2 as six named factors.
- **Name.** The earlier note used the index listing "NQ Liquidity Sweep &
  Reversal Scalping". The page itself is titled **"NQ Liquidity Sweep &
  IFVG Scalping Strategy"**. Both are kept as aliases.
- **"Lower timeframe" made precise.** The earlier note said only "execute on
  the lower timeframe". The playbook names the **1-minute** as the primary
  execution chart, with 15-second and 3-second charts for judging speed.
- **R:R confirmed and extended.** The 1:2 minimum is confirmed. The
  playbook adds widening the bracket to 1:3 or 1:4 when the target allows.
- **Added:** the London window (2:00 to 5:00 AM ET, nothing before 2:00);
  fallback liquidity references when Asia trends (Midnight Open, NDOG,
  NWOG); the New York RTH gap quartiles; NQ against ES SMT as confluence;
  conservative and aggressive IFVG confirmation; stop ranges by session and
  the MNQ fallback; the trade-management sequence; sizing by setup quality;
  and the daily loss limit example.
- **Added `uses`:** AMD/PO3, sessions, SMT, trade management, position
  sizing and prop-firm rules, because the playbook relies on each of them.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/carmine-rosato-lvn.md ===== -->

---
id: strategy_carmine_rosato_lvn
type: strategy
title: "Carmine Rosato — Low Volume Node (LVN) Pullback Strategy (futures/indices, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Carmine LVN Trading Strategy, LVN pullback, low volume node strategy, Carmine LVN]
taught_by: [person_carmine_rosato]
featured_in: [channel_chart_fanatics]
uses: [concept_volume_profile, concept_order_flow, concept_support_resistance, concept_liquidity, concept_scalping, concept_position_sizing, concept_risk_reward_r_multiples]
derived_from: [concept_volume_profile, concept_auction_market_theory]
related: [strategy_carmine_rosato_orderflow_masterclass, strategy_forrest_knight_volume_profile, strategy_fabio_valentini_amt_order_flow]
sources:
  - {title: "Chart Fanatics — Carmine LVN Trading Strategy", url: "https://www.chartfanatics.com/strategies/low-volume-node", tier: T2}
status: verified-t2
---

# Carmine Rosato — Low Volume Node (LVN) Pullback Strategy (futures/indices, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/low-volume-node. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Carmine Rosato teaches order flow, Level 2 walls, and reversal
and breakout-retest setups in free masterclasses on Chart Academy. This LVN
setup is described as using the same order-flow method.

## Built for

- **Instruments:** futures and indices.
- **Style:** scalping and day trading.
- **Timeframe / session:** no chart timeframe is named. The worked example
  starts at the open and plays out later in the same session.
- **Tools:** volume-by-price profile, liquidity heatmap, footprint chart and
  delta.

## Core idea

A strong push away from a key level runs fast and leaves little traded
volume behind. That thin pocket is a **low volume node (LVN)**, and the
playbook reads it as a sign that large participants were active. Price
often comes back to the LVN, where those participants reload or defend
their positions. The trader waits for that return, gets order-flow proof
that the level is being defended again, and enters with a tight stop for a
high reward-to-risk trade.

## Rules

1. **Mark a level of interest.** Find a clear supply, demand, support or
   resistance level. Price should have consolidated there and then moved
   impulsively away, which shows strong buyers or sellers.
2. **Let price leave.** The first move away is not an entry. Wait for the
   rally or drop that confirms large participants stepped in.
3. **Find the LVN.** On a volume-by-price profile, locate the area that
   price crossed quickly on little or no volume. Treat it as a **zone**,
   not a single price.
4. **Wait for the revisit.** Let price pull back into the LVN.
5. **Confirm the defence.** Use the heatmap, footprint, delta or order flow
   to see large buyers or sellers defending the zone. In the example, this
   meant passive bids held while sell orders hit them, aggressive selling
   was absorbed, and every new low was bought straight back.
6. **Enter.** Go long when price bounces from demand or support, short when
   it rejects supply or resistance.
7. **Stop.** Just beyond the LVN, or beyond the recent low (for longs) or
   high (for shorts).
8. **Size.** Set position size from the stop distance so the dollar risk is
   the same on every trade.
9. **Target.** A logical level: high or low of the day, another supply or
   demand zone, another LVN, or a support or resistance level. Scale out or
   take the whole profit depending on context and volatility.

**Worked example (long).** The market sold off at the open into a marked
demand zone and bounced hard. The rally left two LVNs, one at 5563 and a
deeper one in the 5550s. Later, price pulled back into the 5563 LVN and
showed absorption. The long went in at 5561 with a tight stop just below
the zone, and price reached the target, the high of the day.

## Risk management

- **Risk per trade:** fix the dollar risk before every entry. The amount
  itself is not specified in the playbook.
- **Sizing:** from the stop distance, so dollar risk stays constant.
- **Invalidation:** a move through the LVN zone or the recent swing, where
  the stop sits.
- **Daily or weekly limits:** not specified in the playbook.
- **Mindset:** accept that some trades will lose, and stay disciplined.

## What the playbook leaves unspecified

- Which chart timeframe and which profile lookback to use when finding LVNs.
- How to choose among several LVNs. The page admits this takes experience;
  its example had two candidates and used the shallower one.
- What exactly counts as confirmation: how much absorption, which delta
  reading, how many failed breaks.
- How tight the stop is in ticks or points. The example says only that it
  sat "just below the zone".
- The minimum reward-to-risk, and the rules for scaling out.
- Whether to trade only at certain times or sessions, and any daily loss
  limit.

## Evidence & claims

- The page claims **no win rate, R:R figure, P&L or payout**. Among the pros
  it lists a qualitative "High reward-to-risk potential" (self-reported,
  T4).
- The example gives an entry (5561) and a target (high of day) but no stop
  price, so its R multiple cannot be worked out. No expectancy check is
  possible.

## Concepts & lineage

- Finding thin-volume zones on a volume-by-price profile →
  [[concept_volume_profile]]
- An LVN as a pocket the auction moved through quickly on thin volume →
  [[concept_auction_market_theory]]
- Confirming the defence with heatmap, footprint and delta absorption →
  [[concept_order_flow]], [[concept_liquidity]]
- Supply, demand, support and resistance as the origin of the move →
  [[concept_support_resistance]]
- Tight-stop intraday execution → [[concept_scalping]]
- Constant dollar risk set by stop distance →
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/carmine-rosato-orderflow-masterclass.md ===== -->

---
id: strategy_carmine_rosato_orderflow_masterclass
type: strategy
title: "Carmine Rosato — Order Flow Masterclass: Absorption & Stop-Run Reclaim (futures, intraday order-flow trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Order Flow Masterclass by Camrine, Carmine order flow, absorption short, stop run and reclaim long]
taught_by: [person_carmine_rosato]
featured_in: [channel_chart_fanatics]
uses: [concept_order_flow, concept_auction_market_theory, concept_market_microstructure, concept_liquidity, concept_liquidity_sweep_reversal, concept_support_resistance, concept_volume_profile]
derived_from: [concept_auction_market_theory, concept_order_flow]
related: [strategy_carmine_rosato_lvn, strategy_yush_order_flow, strategy_fabio_valentini_amt_order_flow, strategy_jay_awtani_market_dna]
sources:
  - {title: "Chart Fanatics — Order Flow Masterclass by Camrine", url: "https://www.chartfanatics.com/strategies/orderflow-trading-masterclass", tier: T2}
status: verified-t2
---

# Carmine Rosato — Order Flow Masterclass: Absorption & Stop-Run Reclaim (futures, intraday order-flow trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/orderflow-trading-masterclass. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Carmine Rosato teaches order flow in free masterclasses on Chart
Academy. Per the page, they cover futures fundamentals, risk management and
scaling, Level 2 walls, and reversal and breakout-retest setups. (The page
title spells his name "Camrine".)

## Built for

- **Instruments:** the page has no Built For block. The masterclass it
  promotes is about futures, and the two case studies quote prices of 5710
  and 5844. The page never names the contract.
- **Style:** intraday order-flow reading with three tools: the DOM, the
  liquidity heatmap and the footprint chart.
- **Timeframe / session:** not stated. The second case study refers to the
  previous day's low and to earlier tests of a level within the same session.

## Core idea

The market is a continuous auction. Resting limit orders supply liquidity
and do not move price; aggressive market orders consume it and do. The page
says price moves because one side is more aggressive, not because there are
"more buyers than sellers". Support and resistance are places where
aggressive orders keep failing to get through passive liquidity. The trader
reads three signals live: **absorption**, **liquidity walls** and **stop
runs**. Delta (and, on paper, the volume profile, which the page only
defines) is the next layer of reading, and a trade is taken only once one
side has visibly taken control.

## Rules

The page teaches concepts plus two worked case studies. It gives no single
rulebook, so the steps below are drawn from those case studies.

1. **Context and location.** Mark levels where liquidity sits: resistance
   with a visible sell wall, support with a visible bid wall, and obvious
   prior highs and lows (such as the previous day's low) where stops pile
   up. The page closes by naming three steps, Context, Location and
   Confirmation, but does not define them.
2. **Read the signals at the level:**
   - *Absorption:* heavy aggressive volume and a strong delta in one
     direction, but price barely moves. The passive side is soaking up the
     pressure.
   - *Liquidity wall:* a large cluster of resting orders on the book or
     heatmap that price repeatedly hits and cannot clear.
   - *Stop run:* a sharp push through an obvious high or low that triggers
     stops, after which the market often snaps back.
3. **Confirm with delta.** Look at how price responds to delta, not just the
   number. If delta is strongly positive and price does not rise, buyers are
   being absorbed. If delta is strongly negative and price does not fall,
   sellers are being absorbed.
4. **Setup A, absorption short at resistance.** Price rallies into a sell
   wall (about 111 contracts at 5710 in the example). Buyers keep lifting
   the offer in 70 to 80 lot clips and delta prints positive, but price
   stalls. Go short when buying fades, the bids below thin out and sellers
   start hitting aggressively. The page does not give a stop or a target for
   this case.
5. **Setup B, stop run and reclaim long.** Price flushes below the previous
   day's low on heavy negative delta, then stops going lower (absorption).
   The footprint shows aggressive selling with no follow-through, and the
   heatmap shows liquidity building beneath price. **Enter long when price
   reclaims the level** (about 5844 in the example). That level had already
   held as support four or five times earlier in the session.
6. **Stop.** In Setup B, the stop goes just below the low of the flush.
7. **Exit.** Not specified. Both case studies only describe price
   moving away from the level after the shift in control.

## Risk management

- **Risk per trade:** not specified in the playbook.
- **Stop:** structural. In the reclaim long it sits just below the flush
  low. The absorption short has no stop rule.
- **Daily or weekly limits, sizing:** not specified in the playbook. Risk
  management and scaling are listed as masterclass topics but not taught on
  this page.

## What the playbook leaves unspecified

- Which contract, session and time window the setups are meant for.
- How large a wall must be, or how many absorbed lots or how much delta,
  before it counts. The 111-lot wall and 70 to 80 lot clips describe one
  example and are not thresholds.
- Stops and targets for the absorption short, and targets for the reclaim
  long.
- What "Context, Location, and Confirmation" means as a checklist.
- How the volume profile is used. The page defines it in a single sentence.
- Trade management (partials, trailing, breakeven) and any risk limits.
- How to deal with spoofed or pulled liquidity on the heatmap. The page
  notes that resting orders can be withdrawn but gives no rule for it.

## Evidence & claims

- The page contains **no win-rate, R:R, P&L or payout claims**. The only
  numbers are example prices and lot sizes from the two case studies.
- With no stated win rate or reward-to-risk, no expectancy check is
  possible. The setups would need to be journaled or backtested from
  scratch.

## Concepts & lineage

- The market as a two-sided auction of passive limit orders against
  aggressive market orders → [[concept_auction_market_theory]],
  [[concept_market_microstructure]]
- Absorption, delta, DOM, heatmap and footprint reading →
  [[concept_order_flow]]
- Liquidity walls and stop pools above highs and below lows →
  [[concept_liquidity]]
- Stop run followed by reclaim of the swept level →
  [[concept_liquidity_sweep_reversal]]
- Support and resistance explained as passive liquidity outlasting
  aggression → [[concept_support_resistance]]
- Where value was accepted or rejected → [[concept_volume_profile]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/clement-ang-price-cycle.md ===== -->

---
id: strategy_clement_ang_price_cycle
type: strategy
title: "Clement Ang — Price Cycle Strategy: Continuation Base and Late-Stage Failed Base (US stocks, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Clement’s Price Cycle Trading Strategy", Clement Ang price cycle, wedge pop continuation, late-stage failed base short]
taught_by: [person_clement_ang]
featured_in: [channel_chart_fanatics]
uses: [concept_moving_averages, concept_trend_following, concept_growth_momentum_canslim, concept_breakout_trading, concept_chart_patterns, concept_volatility, concept_support_resistance, concept_price_action, concept_market_structure, concept_multi_timeframe_analysis, concept_vwap, concept_oscillators_momentum, concept_market_regimes, concept_news_trading, concept_liquidity, concept_trade_management, concept_risk_reward_r_multiples, concept_trading_psychology]
derived_from: [concept_growth_momentum_canslim, concept_trend_following]
related: [strategy_ted_zhang_stage_analysis, strategy_ariel_hernandez_real_simple, strategy_pradeep_bonde_episodic_pivot]
sources:
  - {title: "Chart Fanatics — Clement’s Price Cycle Trading Strategy", url: "https://www.chartfanatics.com/strategies/price-cycle-continuation-failed-base-strategy", tier: T2}
status: verified-t2
---

# Clement Ang — Price Cycle Strategy: Continuation Base and Late-Stage Failed Base (US stocks, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/price-cycle-continuation-failed-base-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Clement Ang swing trades stocks by reading where a leader sits in
its price cycle. The playbook says he moved from a chart full of indicators
(RSI, stochastics, Money Flow Index, MACD) to a stripped-down process,
because the signals conflicted and caused analysis paralysis.

## Built for

- **Instruments:** stocks. The examples are US names (Affirm), with QQQ as
  the market reference.
- **Style:** swing trading, long and short.
- **Timeframes:** the **daily** chart defines the setup, using the 10-day
  and 20-day EMAs, with the 50-day and 200-day moving averages for context.
  The **5-minute** chart is used for execution. **Weekly** bases of about
  six weeks or more are noted for larger continuation moves.
- **Session:** entries happen during regular hours on the 5-minute chart.
  No fixed time window is given.

## Core idea

A stock moves through a cycle, not a single pattern. On the bullish side
the sequence is uptrend, pullback, wedge pop, cross back, base, breakout
and continuation. On the bearish side it is failed breakout, 20 EMA
violation, weak rally, breakdown and downtrend. Longs buy relative-strength
leaders as volatility contracts around the 10 and 20 EMAs. Shorts sell
former leaders after the base fails and a weak, low-volume rally rolls over
at the moving averages. With a historical win rate of about 30% (self-reported,
T4), the edge comes from tight, defined stops and letting winners run to several times
the risk. Clement describes the process as about 70% reaction and 30%
anticipation.

## Rules

**Stock selection (both sides)**

1. Average daily dollar volume of about **$50M or more**.
2. **ADR above about 3%**.
3. **Strong relative strength** against the market: holding sideways or
   rising while the index falls. Prefer names whose **industry group** is
   also strong.
4. **Market context:** many of the best bases form during market
   corrections. Watch leaders that hold their moving averages while the
   index declines, ready for when the market turns.

**Long: continuation setup**

5. **Uptrend:** higher highs and higher lows, above the longer-term
   averages. The 200-day gives the broad trend.
6. **Wedge pop:** after a correction, price pushes back through the
   **10 and 20 EMAs**, ideally on rising volume. This is a clue, not
   necessarily the entry.
7. **Cross back and base:** a controlled pullback to the 10 and 20 EMAs
   that turns into a sideways base rather than a breakdown.
8. **Volatility contraction:** tight daily candles, volume drying up,
   relative strength holding, price at or above the 10 and 20 EMAs, and
   clear resistance overhead. That resistance is the breakout level.
9. **Entry 1, buying strength:** buy through the base resistance on the
   5-minute chart, ideally with improving volume. **Stop:** below the
   current day's low or the prior day's low, with a small buffer.
10. **Entry 2, buying weakness** (useful in choppy markets where breakouts
    fade): the daily structure must still be bullish. Price fades intraday
    toward the daily 10 EMA or another support and starts turning up. Buy
    the turn. VWAP, short-term moving averages, the 5-minute opening range
    and MACD can confirm, but they only support the setup. **Stop:** below
    the low of day or below the moving-average support used. Risk is
    usually tighter than on Entry 1.
11. **Earnings:** the Affirm example skipped a setup that was still
    developing, because earnings were close and there was no profit cushion.
12. **Scale-out 1:** at about **2× ADR** from entry (for example, about 10%
    on a 5%-ADR stock), sell about **one-third** and move the stop toward
    breakeven after a strong move.
13. **Scale-out 2:** when price is very extended, at about **8 to 10 ATR
    multiples above the 50-day moving average**, sell another **one-third**
    into strength.
14. **Final third:** trail on a **daily close below the 10 EMA**, or below
    the **20 EMA** if that is the average the stock has historically
    respected.
15. **Re-entry:** only from a fresh consolidation or base, not by chasing
    the same leg. Weekly bases of **six weeks or more** can carry larger
    multi-week moves.

**Short: late-stage failed base**

16. **Failed breakout:** a former leader seems to set up for another
    breakout, but the pattern fails.
17. **20 EMA break:** price breaks the **20-day EMA**, ideally on higher
    volume. The stock moves to a breakdown watchlist. Do not chase this
    first break.
18. **Weak recovery:** wait for a low-volume wedge or rally back toward the
    moving averages.
19. **Uppercut and fail** (preferred): price pokes briefly above the 10 or
    20 EMA, then rolls back below it.
20. **Entry:** on the 5-minute chart, short when the rally into the daily
    moving averages turns down. A **loss of intraday VWAP** is one possible
    trigger.
21. **Stop:** just above the **high of day plus $0.10 to $0.20**.
22. **Market confirmation:** better when QQQ or the relevant index is also
    falling, so the market is behind the trade.
23. **Invalidation:** a close back above the moving average that was
    supposed to cap price. Honour the stop.
24. **Cover 1:** at prior lows on the left side of the daily chart. If
    price undercuts an old low and starts reclaiming it, cover about
    **50%**. Shorts take more off at the first target than longs, because
    downside moves reverse sharply.
25. **Cover 2:** cover the rest when price reclaims the **10 EMA** or the
    relevant short-term moving-average structure.
26. **Re-short:** once the 20 EMA slopes down and acts as resistance,
    repeat breakdown, rally into the EMA, failure, re-short for later legs.
27. **Re-entry limit:** after a tight stop-out, re-enter only if the setup
    forms again, with **about three attempts at most per ticker**. Then
    stop trading the name.

## Risk management

- **Stop placement:** longs below the day's low or prior day's low (Entry
  1) or below the low of day or moving-average support (Entry 2). Shorts
  at high of day plus $0.10 to $0.20.
- **Pre-trade questions:** where is the trade invalid, how much is at risk,
  and is the potential reward large enough to justify it.
- **Scaling:** longs out in thirds (2× ADR, 8 to 10 ATR above the 50-day,
  then a trail). Shorts out by halves (prior-low undercut and reclaim, then
  a 10 EMA reclaim).
- **Event risk:** avoid opening new positions just before earnings without
  a profit cushion (from the Affirm example).
- **Tilt control:** at most about three attempts per ticker.
- **Risk per trade ($ or % of account), position size, and daily or weekly
  loss limits:** not specified in the playbook.

## What the playbook leaves unspecified

- Account risk per trade and how share size is set from the stop distance.
- The lookback periods for ADR and ATR, and how relative strength is
  measured (RS line, percentage versus index, or a ranking).
- How tight a contraction must be, and how much volume must dry up, before
  a base counts.
- Exactly when to move the stop to breakeven, and what counts as a "strong
  move in favour".
- How large the stop buffer is on longs ("a small buffer").
- How much volume expansion a wedge pop or 20 EMA break needs.
- Whether shorts have their own liquidity or ADR filters, and how borrow
  is handled.
- Whether the 50% short cover needs a full reclaim of the prior low or
  only an intraday move back above it.
- How many positions to hold at once, and portfolio heat limits.

## Evidence & claims

- **Win rate:** about **30%** historically, as discussed in the episode.
  Self-reported (T4).
- **Affirm example (2023):** initial risk about **4%**, ADR about **7%**,
  and price up about **20%** within three days, a move of roughly 5R (20 / 4)
  on that one trade. The realized result after scale-outs is not given.
  Self-reported (T4).
- No average reward-to-risk is claimed, so a full expectancy check is not
  possible. As a reference: with p = 0.30, E = 0.30×RR − 0.70 is positive
  only if the **average winner exceeds about 2.33R** after costs. The
  scale-out plan (one-third at 2× ADR, which is often under 2R when the
  stop is near one ADR) means the runners must carry most of the
  expectancy.

## Concepts & lineage

- Uptrend, pullback, base and continuation, and the reverse cycle into a
  downtrend → [[concept_trend_following]], [[concept_market_structure]]
- 10 and 20 EMAs for setup and trailing, 50 and 200 for context →
  [[concept_moving_averages]]
- Relative-strength leaders, strong industry groups, bases formed during
  market corrections → [[concept_growth_momentum_canslim]],
  [[concept_market_regimes]]
- Tight candles and drying volume before a breakout through base
  resistance → [[concept_volatility]], [[concept_breakout_trading]],
  [[concept_chart_patterns]]
- Wedge pop, uppercut and fail, and undercut and reclaim of prior lows →
  [[concept_price_action]], [[concept_support_resistance]]
- Daily setup with a 5-minute trigger (VWAP loss, opening range, MACD as
  support) → [[concept_multi_timeframe_analysis]], [[concept_vwap]],
  [[concept_oscillators_momentum]]
- The $50M dollar-volume filter → [[concept_liquidity]]
- Skipping setups right before earnings → [[concept_news_trading]]
- Scale-outs at 2× ADR and 8 to 10 ATR from the 50-day, then a moving
  average trail → [[concept_trade_management]]
- A low win rate offset by large R multiples →
  [[concept_risk_reward_r_multiples]]
- The three-attempt limit against revenge trading and tilt →
  [[concept_trading_psychology]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/dhesi-liquidity-inversion.md ===== -->

---
id: strategy_dhesi_liquidity_inversion
type: strategy
title: "Dhesi — Liquidity Inversion Model: Sweep, FVG Inversion & LTF Confirmation (NQ/ES futures, day trading/swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Liquidity Inversion Model, Dhesi Trades model, FVG inversion model, Dhesi liquidity inversion]
taught_by: [person_dhesi]
featured_in: [channel_chart_fanatics]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_fair_value_gap, concept_order_blocks_breakers, concept_market_structure, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_volatility, concept_smt_divergence, concept_trendlines, concept_trade_management, concept_position_sizing, concept_risk_reward_r_multiples, concept_trading_psychology]
derived_from: [concept_smart_money_concepts, concept_fair_value_gap]
related: [strategy_candace_lau_nq_sweep_reversal, strategy_jadecap_liquidity_volatility, strategy_marco_trades_liquidity_grab]
sources:
  - {title: "Chart Fanatics — Dhesi - Liquidity Inversion Model", url: "https://www.chartfanatics.com/strategies/liquidity-inversion-model", tier: T2}
status: verified-t2
---

# Dhesi — Liquidity Inversion Model: Sweep, FVG Inversion & LTF Confirmation (NQ/ES futures, day trading/swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/liquidity-inversion-model. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Dhesi (Dhesi Trades) trades NQ and ES futures and prefers NQ
for its intraday range. He uses one ICT-style model for day trades, swings
and longer-dated positions.

## Built for

- **Instruments:** the page header says futures and forex. The body is
  built around **NQ and ES**, with NQ preferred. Other liquid markets are
  allowed in principle, but the page advises proving the model before
  watching many tickers.
- **Style:** day trading and swing trading. The page also mentions scalps
  and long-dated option (LEAPS) positions built from the same logic.
- **Timeframes:** monthly, daily, 4H, 1H, 15m, 5m and 1m. Day-trade entries
  are refined on the **15m, 5m or 1m**. Swing entries need **1H or higher**
  confirmation, preferably 4H and daily.
- **Session:** New York, built around the **10:00 a.m. ET four-hour candle
  open**. Moves before 10:00 are treated as noisy.
- **Skill level:** assumes the trader already knows ICT-style tools: draws
  on liquidity, FVGs, inversion FVGs, PD arrays, order blocks, balanced
  price ranges, and session, monthly and equal highs and lows.

## Core idea

Start from where liquidity sits. Wait for price to sweep or tap it, then
require a **fair value gap inversion**: the gap that supported the move
into the liquidity gets violated and starts acting from the other side.
That higher-timeframe inversion defines the setup. A day-trade entry also
needs a pullback into a PD array from the new move, followed by a
lower-timeframe inversion in the trade direction. Take a technical partial
and let a runner work when volatility expands.

## Rules

1. **Mark the draws on liquidity.** Monthly highs and lows come first
   because they tend to give the strongest reactions. Then session highs
   and lows, equal highs and lows, the new week opening gap, unfilled FVGs,
   and easy-to-reach pools such as a cluster of trendline lows.
2. **Stay reactive.** Do not fix a bias before price reaches the area.
   React to what it does there.
3. **Check volatility.** The full model is for expanded volatility, when
   liquidity is being hit with force. Downside NQ moves are singled out as
   the best case. In dead volatility, do not trade it aggressively; base
   hits are fine.
4. **Time it (day trades).** Let the 10:00 a.m. ET four-hour candle
   reveal what price is doing at the key area (a sweep, a gap tap, or a
   rejection from a higher-timeframe PD array) before committing.
5. **Sweep and fast inversion.** After the sweep, price should react fast
   and violate the relevant FVG within the next few candles, **often two or
   three**. Bearish: a bullish FVG breaks and turns into resistance.
   Bullish: a bearish FVG breaks and turns into support. If price lingers
   inside the gap, the setup loses urgency. If price respects the gap and
   continues, there is no reversal.
6. **Lower-timeframe confirmation (day trades).** Wait for a retracement
   into a PD array (FVG or order block) created by the new move. The
   retracement is not the entry. The entry comes when the counter-direction
   lower-timeframe structures formed during that retracement are broken and
   inverted. If an order block and an FVG are stacked, wait for both to be
   violated.
7. **Swing entries use 1H or higher.** Never enter a swing from the 15m, 5m
   or 1m chart.
8. **Do not chase.** The big displacement candle shows the idea; the
   pullback and inversion give the risk. A bare 4H FVG tap is not a
   day-trade entry when the resulting stop is too large for your account;
   wait for confirmation.
9. **Optional SMT.** ES against NQ divergence adds confidence but is not
   required.
10. **Stop where the chart is wrong.** For a bearish day trade, above the
    current 15-minute high or the lower-timeframe high that formed before
    the inversion. For a bullish continuation, below the low that should
    hold if the FVG reaction is real.
11. **Targets come from the chart.** Use local highs and lows, session
    highs and lows, unfilled hourly or daily FVGs, daily or weekly gaps,
    equal highs and lows, and stacked liquidity. Never set targets from
    dollar goals or arbitrary point counts.
12. **Manage.** Typically trim **50%** at the first technical target and move the
    stop to **breakeven**. Let the runner work toward the higher-timeframe
    draw. A runner stopped at breakeven still counts as a successful trade.
13. **One clean attempt.** A missed entry is not chased; the next chance
    comes with a later session or a fresh four-hour candle. No averaging or compounding
    into trades, except in rare high-conviction higher-timeframe setups.
14. **Daily stop rule.** Two losses end the day. One win and one loss allow
    a third attempt, but only if the setup appears again.

**Entry variants on the page**

- *Bearish reversal after a buy-side sweep:* price runs buy-side liquidity
  (monthly high, session high or equal highs), rejects and inverts the supporting
  FVG or PD array. Then enter on the lower-timeframe pullback and
  inversion. Stop above the protected high. First target is the nearest
  sell-side liquidity, with runners toward larger stacked liquidity.
- *Bullish continuation into equal highs:* the market is already expanding
  higher with an open higher-timeframe FVG below. Wait for the tap, a
  bullish reaction and a lower-timeframe inversion. In the NQ example the
  target pool was a set of **relative equal highs at 26,100**; entry came
  from a 4H FVG tap and a 1-minute inversion.
- *Higher-timeframe reversal for swings and LEAPS:* identical steps,
  applied to monthly and daily charts. The example is NQ reacting from a monthly FVG
  and order block during the tariff-driven pullback. The monthly gap
  inverted back up, which confirmed longer-term longs and gave a clear
  bias for day trades.

## Risk management

- **Per-trade risk:** a fixed dollar or % figure is not specified in the
  playbook. Hold the same dollar risk and change the size: when high
  volatility puts the structural stop **40–50 NQ points** from entry, cut
  contracts rather than pull the stop to an arbitrary level.
- **Stop placement:** structural, beyond the protected high or low.
  Discomfort with the dollar amount is not a reason to move it.
- **Daily limit:** **two losses end the day**. A win followed by a loss
  allows one more attempt.
- **Weekly limit:** not specified in the playbook.
- **Scaling:** no adding or averaging, apart from rare high-conviction
  higher-timeframe trades.
- **Swing versus day risk:** swings can carry wider stops because their
  objective is larger. Day trades need confirmation that tightens the
  stop.

## What the playbook leaves unspecified

- A dollar or % risk per trade, and a maximum number of trades beyond the
  two-loss rule.
- Which timeframe the "two or three candles" inversion window is counted
  on.
- An objective test for "expanded" versus "dead" volatility.
- How to choose between the 15m, 5m and 1m for a given entry.
- How to grade competing PD arrays, or which one counts as "the" relevant
  FVG.
- How to manage the runner after breakeven (trail or fixed target), and
  whether day trades must close by a set time.
- Forex specifics such as pairs or sessions. The header lists forex, but
  every example is NQ or ES.
- A minimum R:R. The page mentions 1:1.5 and 1:2 ideas that runners can
  extend, but sets no floor.
- Any win rate or trade sample.

## Evidence & claims

- **No win rate, P&L or payout** is reported.
- On volatile NQ down-moves, the page says "a 50-point idea can become a
  200-point opportunity". Self-reported (T4).
- Runners are said to stretch a 1:1.5 or 1:2 trade into a far bigger
  multiple. Self-reported (T4). Both describe trade design, not measured
  results.
- **Worked examples** (no R or dollar results given): the November NQ
  reversal (a swing short from the daily-FVG inversion with an hourly
  entry, and a New York day short after a 10:00 a.m. sweep of equal highs,
  targeting the 9:30 a.m. session low); the 26,100 equal-highs
  continuation; and the monthly-FVG reversal during the tariff pullback.
- Without a win rate, no expectancy check is possible. By simple
  arithmetic (not stated on the page), the break-even win rate would be
  40% at 1:1.5 and about 33% at 1:2.

## Concepts & lineage

- Monthly, session and equal highs and lows, NWOG and unfilled gaps as
  draws → [[concept_liquidity]]
- Stacked trendline lows as low-resistance liquidity →
  [[concept_trendlines]]
- Sweep, rejection, then confirmed reversal →
  [[concept_liquidity_sweep_reversal]]
- FVG inversion as the trigger at both higher and lower timeframes →
  [[concept_fair_value_gap]]
- Order blocks as PD arrays in the retracement →
  [[concept_order_blocks_breakers]]
- Displacement and violation of protected highs and lows →
  [[concept_market_structure]]
- Monthly-to-1-minute stack, with swing versus day-trade timeframe rules →
  [[concept_multi_timeframe_analysis]]
- The 10:00 a.m. ET four-hour candle in New York →
  [[concept_trading_sessions_killzones]]
- Volatility as a quality filter → [[concept_volatility]]
- ES against NQ as optional confluence → [[concept_smt_divergence]]
- 50% at the first technical target, breakeven, runner →
  [[concept_trade_management]], [[concept_risk_reward_r_multiples]]
- Size down to keep a structural stop → [[concept_position_sizing]]
- Two-loss rule to stop revenge trading → [[concept_trading_psychology]]
- Lineage: ICT-style smart-money concepts → [[concept_smart_money_concepts]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/dylan-oneil-vix-futures.md ===== -->

---
id: strategy_dylan_oneil_vix_futures
type: strategy
title: "Dylan O’Neil — VIX Futures Strategy: VIX Pressure as Confirmation for ES and NQ (index and VIX futures, day and swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["VIX Futures Strategy: Volatility-Based Edge", Dylan O'Neil VIX strategy, VIX confirmation at previous-day levels, VIX 1% rule]
taught_by: [person_dylan_oneil]
featured_in: [channel_chart_fanatics]
uses: [concept_volatility, concept_market_sentiment, concept_intermarket_analysis, concept_divergence, concept_smt_divergence, concept_support_resistance, concept_breakout_trading, concept_liquidity_sweep_reversal, concept_chart_patterns, concept_market_microstructure, concept_market_regimes, concept_risk_reward_r_multiples]
derived_from: [concept_intermarket_analysis, concept_volatility]
related: [strategy_trader_kane_lab_model, strategy_tanja_amd_futures]
sources:
  - {title: "Chart Fanatics — VIX Futures Strategy: Volatility-Based Edge", url: "https://www.chartfanatics.com/strategies/the-vix-futures-strategy", tier: T2}
status: verified-t2
---

# Dylan O’Neil — VIX Futures Strategy: VIX Pressure as Confirmation for ES and NQ (index and VIX futures, day and swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/the-vix-futures-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Dylan O’Neil trades futures using the VIX as a live gauge of
pressure on the S&P 500. He uses it to judge whether ES and NQ moves have
real force behind them. The page gives no further biography.

## Built for

- **Instruments:** futures: **ES** (the main target), **NQ** as a second
  confirmation, and **VIX futures**, which the trade example goes long.
- **Style:** day trading and swing trading. The page presents it mainly as
  a **confirmation layer** to add to an existing strategy, plus some
  stand-alone turning-point trades.
- **Timeframes:** the page says it works on all timeframes. ES, NQ and the
  VIX must be watched on **matching timeframes**.
- **Key reference:** each instrument's **previous day high and low**.
- **Session:** no specific time window. The example mentions a "clean
  time-of-day alignment" without saying what it was.

## Core idea

The VIX is priced from SPX options, mostly put demand, so it shows how much
fear or hedging pressure sits on the S&P. More put demand lifts the VIX and
weighs on ES. Less put demand lowers the VIX and takes weight off. The page
claims most ES volume is algorithmic and that VIX moves trigger sell or buy
programs. On that basis, the VIX tells you whether an ES or NQ break of a
key level is real or likely to fail. Dylan's analogy: with a low VIX, ES
climbs a mountain carrying no weight; with a high VIX, it climbs carrying a
heavy backpack.

## Rules

1. **Read the VIX backdrop.** A weak or falling VIX makes it easier for ES
   to hold support and rise. A strong or rising VIX makes rallies more
   likely to fail.
2. **Mark previous-day levels** on ES, NQ and the VIX, using matching
   timeframes.
3. **Confirmed breakdown (continuation):** ES breaks its previous day low,
   **and** the VIX is rising and at or above its previous day high. If NQ
   **also** breaks its previous day low, all three agree and further
   downside is more likely.
4. **Unconfirmed breakdown (failure or squeeze):** ES breaks its previous
   day low, but the VIX is **not** at its previous day high or is making a
   lower high. That alone means the break lacks pressure and has a good
   chance of failing. If NQ also holds above its own low or makes a higher
   low, the relative strength adds to the case. **Do not short it.** Once
   ES gets back above the previous day low, it often snaps back and
   squeezes higher, trapping shorts.
5. **VIX moves first:** if the VIX reaches its previous day high *before*
   ES or NQ break their lows, pressure is building early. When ES does
   break, the move is more likely to continue.
6. **Pair support and resistance across the two charts.** VIX at support
   (likely to bounce) with ES at resistance points to an ES turn lower. VIX
   at resistance (likely to turn down) with ES at support points to ES
   holding or rising. These pairings mark the strongest turning points.
7. **The 1% rule:** if ES is up 1% or more **and** the VIX is also up 1% or
   more, ES strength is fragile and pushes into resistance tend to fail. If
   ES is down 1% or more **and** the VIX is down 1% or more, the weakness is
   fragile and support tends to hold. Use this to avoid chasing extended
   moves.
8. **Natural floor at major highs:** near all-time or multi-year highs,
   puts are cheap and funds hedge more, so the VIX can rise while ES holds.
   A rising VIX there is **not** a reliable breakdown signal on its own.
   Lean on ES levels instead.
9. **Stand-alone VIX trade (the page's example):** go long VIX futures at a
   clear **contract low** (about **16.8**) where a **double bottom** forms,
   while ES **fails to break out at all-time highs**. Extra context in the
   example: the S&P had sold off on four of the previous five Fridays, and
   the VIX bounce came on a Thursday.
10. **No duplicate exposure.** Do not take the same trade on several
    instruments at once (for example, short ES, short NQ and long VIX).

## Risk management

- **Avoid duplicated risk:** do not express one idea on several
  correlated instruments at the same time.
- **Stop placement, targets, position size, risk per trade and daily or
  weekly limits:** not specified in the playbook. The VIX example gives a
  6R result but no stop or target level.
- **Invalidation:** implied only. For example, a "confirmed" breakdown
  stops being confirmed if the VIX falls back below its previous day high,
  but the page gives no explicit exit rule.

## What the playbook leaves unspecified

- Entry triggers, stops and targets for ES and NQ trades. The page reads as
  a filter, not a full system.
- Upside mirror rules (ES breaking its previous day high with the VIX at or
  below its previous day low). The page only explains the downside cases,
  though it says previous-day highs are used too.
- What timeframe(s) to use, and what "matching timeframes" means in
  practice.
- Whether the previous day's levels are from the regular session or the
  full overnight session, given VIX and ES trading hours.
- How to identify "important" VIX support and resistance beyond previous
  day levels and contract lows.
- Whether the 1% rule uses VIX percentage change or point change, and
  measured from what reference (prior close).
- How "natural floor" VIX levels are defined, and how to trade near
  all-time highs.
- Handling VIX futures roll, contango and contract choice for the
  stand-alone VIX trades.
- The "clean time-of-day alignment" in the example.

## Evidence & claims

- **Long VIX futures example:** a **6:1 R** outcome. Self-reported (T4).
  It is a single trade, and there is no win rate, so no expectancy check is
  possible.
- **"About 90% of ES volume is algorithms"**, and VIX moves trigger
  sell or buy programs. A market-structure claim from the page, not
  independently sourced. Treat as self-reported (T4).
- **Four of five prior Fridays sold off:** context in the example, not a
  tested statistic. Self-reported (T4).
- The page's pros (filters fakeouts, confirms strength, works on all
  timeframes) are qualitative claims, not measured results. It also admits
  false signals near all-time highs.

## Concepts & lineage

- VIX as SPX-options implied volatility and a fear gauge →
  [[concept_volatility]], [[concept_market_sentiment]]
- Using the VIX and NQ to confirm or reject ES moves →
  [[concept_intermarket_analysis]]
- Non-confirmation between ES, NQ and the VIX at previous-day levels.
  Editorial: the ES-versus-NQ part matches ICT-style SMT divergence →
  [[concept_divergence]], [[concept_smt_divergence]]
- Previous day highs and lows, and VIX support and resistance →
  [[concept_support_resistance]]
- Telling real breakdowns from fake ones, and the snap-back squeeze after
  an unconfirmed break → [[concept_breakout_trading]],
  [[concept_liquidity_sweep_reversal]]
- Double bottom at a VIX contract low → [[concept_chart_patterns]]
- Algorithmic sell and buy programs keyed to the VIX →
  [[concept_market_microstructure]]
- The VIX's natural floor at major highs, where signals change →
  [[concept_market_regimes]]
- 6R outcome reported on the VIX trade →
  [[concept_risk_reward_r_multiples]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/fabio-valentini-amt-order-flow.md ===== -->

---
id: strategy_fabio_valentini_amt_order_flow
type: strategy
title: "Fabio Valentini — Auction Market Theory + Order-Flow Scalping (NQ/ES futures, scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [Fabio Valentini strategy, auction market strategy, direction location aggression, market state location aggression]
taught_by: [person_fabio_valentini]
featured_in: [channel_chart_fanatics, channel_chart_academy]
uses: [concept_auction_market_theory, concept_volume_profile, concept_order_flow, concept_market_regimes, concept_trend_following, concept_mean_reversion, concept_scalping, concept_trading_sessions_killzones, concept_position_sizing, concept_risk_reward_r_multiples, concept_trade_execution]
derived_from: [concept_auction_market_theory]
related: [strategy_andrea_cimitan_amt, strategy_carmine_rosato_lvn, strategy_yush_order_flow, strategy_forrest_knight_volume_profile]
sources:
  - {title: "Chart Fanatics — Auction Market Theory Trading Strategy by Fabio", url: "https://www.chartfanatics.com/strategies/auction-market-strategy", tier: T2}
  - {title: "Chart Academy — Fabio Valentini instructor page", url: "https://www.chartacademy.com/instructors/fabio-valentini", tier: T2}
  - {title: "Trading LIVE with the #1 Scalper in the WORLD (video summary)", url: "https://videohighlight.com/v/tvERE-Beu2U", tier: T3}
  - {title: "PickMyTrade — Fabio Valentini Scalping Strategy: Settings & Rules (NQ)", url: "https://blog.pickmytrade.trade/fabio-valentini-pro-scalper-nasdaq-scalping-strategy/", tier: T3}
status: verified-t2
---

# Fabio Valentini — Auction Market Theory + Order-Flow Scalping (NQ/ES futures, scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/auction-market-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook names him only as "Fabio" and says he teaches a free five-lesson order-flow masterclass on Chart Academy with live Nasdaq examples. The rest of this biography comes from the earlier search-based note (third-party, T3; not in the playbook): Fabio Valentini is an Italian futures scalper, mostly on Nasdaq (NQ), who co-founded the order-flow platform Deep Charts. He is featured in the channel's most-viewed video, *"Trading LIVE with the #1 Scalper in the WORLD (EXTREME Accuracy)"*, and in an episode with order-flow trader Carmine Rosato (T3).

## Built for

- **Instruments:** futures. The trend model names NASDAQ and ES.
- **Style:** scalping (intraday).
- **Timeframes:** none fixed. The volume profile is drawn on specific legs (the impulse or the reclaim), with the previous day's profile as the balance reference. Execution uses footprint charts, big-print bubbles and CVD.
- **Sessions:**
  - The trend model works best in New York. Avoid the London open because of fake breakouts.
  - The mean-reversion model works best in London or in compressed summer conditions.

## Core idea

The market is an auction that alternates between **balance** (rotation around fair value) and **imbalance** (one side pushing price to find new value). Most traders lose by trading breakouts inside balance. The page claims the market stays stuck there about 70% of the time. A trade needs three things in order: **market state** (balanced or not), **location** (LVNs and POC from the volume profile), and **aggression** (order-flow confirmation at that location). If any one is missing, stay flat. There are two complementary models: trend continuation toward new balance, and mean reversion back into balance after a failed breakout.

## Rules

**Trend model (out of balance, seeking new balance)**

1. **Session:** New York. Avoid the London open.
2. **Market state:** confirm the market is out of balance, with displacement and momentum away from prior value. If price is just rotating, skip.
3. **Location:** apply a volume profile to the impulse leg that broke structure and mark the LVNs inside it. Set alerts just before the LVNs. Don't rest blind limit orders.
4. **Trigger:** when price returns into an LVN, require aggression in the trend direction: big buy bubbles or footprint imbalance for longs, big sell bubbles or imbalance for shorts. No aggression means no trade.
5. **Stop:** just beyond the aggressive print, plus a 1–2 tick buffer before the obvious swing high or low. (The worked long example put the stop just below the LVN.)
6. **Break-even:** move to break-even early if CVD shows strong pressure.
7. **Target:** the previous balance's POC. Close the full position there. Trail beyond it only on rare strong trend days. The page's reason is that price reverses from balance about 70% of the time. In the worked example, the trade was closed early when sellers showed aggression against it.

**Mean-reversion model (failed breakout, back into balance)**

8. **Session:** London, or compressed summer conditions.
9. **Market state:** the market is in balance or consolidation. The previous day's profile can serve as the balance reference. Watch for price to push out of balance and fail.
10. **Location:** don't take the first move back. Wait for (a) a clear reclaim inside balance and (b) a pullback into the reclaim leg. Apply a volume profile to the reclaim leg and mark its LVNs.
11. **Trigger:** on the pullback into the LVN, require aggression in the snap-back direction: big buy prints for longs after a reclaim, big sell prints for shorts after a failed upside break.
12. **Stop:** just beyond the aggressive print with a 1–2 tick buffer before obvious highs or lows. Never widen it. If you're wrong, you should be wrong immediately.
13. **Target:** the balance POC. Exit the full position there. Don't reach for the other side of the range unless conditions are exceptional.

## Risk management

- **Risk per trade:** 0.25%–0.5% of the account (both models).
- **Stops:** just beyond the aggressive print plus a 1–2 tick buffer. Never widen. Move to break-even early on strong CVD (trend model).
- **Exits:** full exit at the POC target (no scaling out in the playbook rules).
- **Expected drawdown pattern:** several small stop-outs in a row are common, and the strike rate drops on choppy or compressed days.
- **Daily / weekly limits:** Not specified in the playbook.
- **Maximum trades per session:** Not specified in the playbook.

## What the playbook leaves unspecified

- Size thresholds for "big" bubbles or prints, footprint imbalance ratios, and what counts as "strong" CVD pressure.
- An objective test for balanced vs out of balance, beyond displacement or rotation.
- Which LVN to use when a leg has several, and how far before the LVN to set alerts.
- Exact session hours, and how to recognise "compressed summer conditions".
- Daily loss limit, trade count, and any rule for scaling into winners. The Chart Academy blurb on the page mentions scaling into winners, but the playbook rules don't define it.
- Footprint and profile settings (row size, aggregation).

## Evidence & claims

- **"About 70% of the time" claims:** the market stays stuck in balance about 70% of the time, and price reverses from balance about 70% of the time. Self-reported (T4); no data.
- **R:R claim:** normal trades deliver 1:2.5 to 1:5 reward-to-risk, with much larger ratios on strong days. Self-reported (T4). The page states no win rate, so a full expectancy check isn't possible. Break-even win rates before costs are 28.6% at 1:2.5 and 16.7% at 1:5.
- **Acknowledged drawbacks:** consecutive small losses, a lower win rate in chop, and stress when managing large size intraday.
- **Competition results (earlier note, T3 search summaries, not re-verified here):** top 3 in the Robbins World Cup Trading Championship futures/scalping division, with audited returns reported at 218% to 500%+ depending on source and edition.
- **Earlier risk figure (T3):** a third-party guide gave about 0.25% risk per trade. The playbook's 0.25%–0.5% range now supersedes it.

## Concepts & lineage

- Balance vs imbalance, fair value, failed breakouts back to POC: [[concept_auction_market_theory]]
- LVNs inside the impulse or reclaim leg as location, POC as target: [[concept_volume_profile]]
- Big prints, footprint imbalance and CVD as the aggression trigger: [[concept_order_flow]]
- Separate models for trending and ranging conditions: [[concept_market_regimes]], [[concept_trend_following]], [[concept_mean_reversion]]
- New York for trend, London or summer for mean reversion, avoid the London open: [[concept_trading_sessions_killzones]]
- 0.25–0.5% risk per trade: [[concept_position_sizing]]; 1:2.5–1:5 targets: [[concept_risk_reward_r_multiples]]
- Alerts instead of blind limits, enter only on aggression: [[concept_trade_execution]], [[concept_scalping]]
- Lineage (earlier note, T3; not stated in the playbook): Steidlmayer's Market Profile (CBOT, 1980s) → Dalton's *Mind Over Markets* → order-flow tooling (footprint, DOM) → Fabio's state/location/aggression model.

## Changes vs. earlier note

- **Corrected:** the earlier note (T3, Chart Academy) called the three filters "Direction → Location → Aggression". The playbook calls them **Market State → Location → Aggression**. The Chart Academy blurb on the same page still uses "Direction, Location, and Aggression", so both names are kept as aliases.
- **Corrected:** the earlier note described the trend model as joining aggression *after acceptance beyond value* (T3). The playbook enters on a **pullback into an LVN of the impulse leg** with aggression, and targets the **previous balance POC** with a full exit.
- **Corrected:** the earlier note listed VWAP as a tool and said "no lagging oscillators" (T3). The playbook mentions neither, so VWAP was removed from `uses`.
- **Corrected:** risk was about 0.25% per trade (T3). The playbook says **0.25%–0.5%** (T2).
- **Answered:** two of the earlier open questions. Stop rule: beyond the aggressive print plus 1–2 ticks, never widen. Targets: the POC in both models. Daily loss limit and trade count are still not in the playbook.
- **Added:** session preferences per model, mean-reversion entry only after a reclaim plus pullback (not the first move back), alerts rather than blind limits, early break-even on strong CVD, and the claimed 1:2.5–1:5 R:R.
- Dropped the empty `teaches` key and moved the earlier lineage line into Concepts & lineage. Kept all earlier sources and the extra `featured_in` entry.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/forrest-knight-volume-profile.md ===== -->

---
id: strategy_forrest_knight_volume_profile
type: strategy
title: "Forrest Knight — Volume Profile Edge-to-Edge Strategy (options/futures, day trading / swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Forrest Knight volume profile strategy, edge-to-edge volume profile, volume edge signal candle, previous day POC retest]
taught_by: [person_forrest_knight]
featured_in: [channel_chart_fanatics]
uses: [concept_volume_profile, concept_auction_market_theory, concept_support_resistance, concept_liquidity, concept_price_action, concept_candlestick_patterns, concept_multi_timeframe_analysis, concept_trade_execution]
derived_from: [concept_auction_market_theory]
related: [strategy_fabio_valentini_amt_order_flow, strategy_yush_order_flow, strategy_carmine_rosato_lvn]
sources:
  - {title: "Chart Fanatics — Volume Profile Trading Strategy By Forrest Knight", url: "https://www.chartfanatics.com/strategies/volume-profile-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists Volume Profile Strategy by Forrest Knight)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "TradeZella — Volume Profile Strategy", url: "https://www.tradezella.com/strategies/volume-profile-strategy", tier: T3}
  - {title: "DamnPropFirms — volume profile strategies (quotes Knight)", url: "https://damnpropfirms.com/trading-guides/volume-profile-strategies-high-probability-trades/", tier: T3}
status: verified-t2
---

# Forrest Knight — Volume Profile Edge-to-Edge Strategy (options/futures, day trading / swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/volume-profile-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Forrest Knight as a volume-profile trader working options and futures on day-trading and swing horizons, and gives no further biography.

## Built for

- **Instruments:** options and futures. The worked example is NQ futures.
  - It needs centralized, reliable volume data.
  - The page says it is **not viable in decentralized markets such as spot forex**.
- **Style:** day trading and swing trading.
- **Timeframes:**
  - Weekly and daily to find long-term value areas, edges and directional bias.
  - **4H and 1H** as the main execution charts for signal candles. Lower timeframes are allowed for entries under the higher-timeframe bias.
  - Keep bias and execution timeframes separate, and filter down to 2–3 main profiles.
- **Tools:** session volume profile and visible-range volume profile.
- **Session / time window:** not specified beyond the overnight and prior-day reference levels.

## Core idea

Volume *at price* shows where participants are positioned. High-value areas (HVAs), where heavy volume traded, are "sticky" and price tends to consolidate there. Price tends to travel quickly through low-value areas (LVAs). The sharp drop-off between the two (a **volume edge** or **shelf**) is where price reacts, stalls or breaks away. The trade is taken at a volume edge that lines up with one of four daily liquidity levels, only after a high-volume signal candle closes rejecting it. The target is the next shelf ("edge-to-edge"), and the middle of low-volume zones is avoided.

## Rules

1. **Set directional bias from higher timeframes.** Example: a weekly close with a high-volume, bottom-wick reversal candle at a volume edge makes the bias long. Then favour long trades on the 4H, 1H or lower timeframes. The weekly candle is not traded itself.
2. **Mark the four daily levels:** overnight high, overnight low, prior-day high and prior-day low. Trapped traders tend to act aggressively at these liquidity zones.
3. **Map volume edges and shelves.** Find the transitions between HVA and LVA on the chosen profiles.
4. **Qualify the setup.** All three must be present:
   - price is touching a volume-profile edge;
   - the edge lines up with ONH, ONL, PDH or PDL;
   - a **high-volume signal candle** with a visible rejection wick **closes in the trade direction**.
5. **Wait for the candle to close.** Don't front-run the signal candle, because its last few minutes can flip it.
6. **Entry:** after the signal candle closes at the volume edge. **Alternative (volatility retest):** if the signal candle has a long wick, expect a 50–80% retrace of the wick before continuation and place a limit order in that zone. Estimate the zone visually, not with Fibonacci tools. The page says this suits NQ and other volatile markets.
7. **Stop:** just beyond the signal candle's wick, or beyond the edge of the high-value node.
8. **Target:** the next shelf (edge-to-edge). Trade through the low-volume zone toward the next high-volume area.
9. **No mid-zone trades.** Low-volume interiors are unpredictable. Wait for price to reach an edge.
10. **Previous-day POC retest (core setup).** After a breakout or trend day, price often returns to the prior day's POC before resuming. Look for a signal candle at that POC and target a new high or low.

## Risk management

- **Stop:** beyond the signal-candle wick or the high-value-node edge.
- **Risk per trade:** Not specified in the playbook.
- **Sizing:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.
- **Built-in filter:** sit out when no valid edge signal appears. Some days produce none, and trading inside chop zones is lower probability.

## What the playbook leaves unspecified

- What counts as a "high-volume" signal candle (relative-volume threshold) and how long the wick must be.
- Profile settings: row size, value-area %, which session or range each profile covers, and how to resolve conflicting nodes.
- Overnight-session hours used for ONH and ONL.
- How bias is set when the weekly chart gives no reversal candle, or when weekly and daily disagree.
- Partial exits, break-even or trailing rules, and what to do if price stalls before the next shelf.
- Options specifics (strike, expiry, greeks) despite options being listed as an instrument.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- **NQ 1H example:** price swept above PDH at the upper shelf edge, then closed back below it on a long-upper-wick, high-volume candle. The short went on at the close with the stop above the wick high, targeting ONL at the lower shelf, which was hit. No prices or P&L given (T4).
- The claim that the method works across asset classes is limited by the page's own caveat that it needs centralized volume data (T4).

## Concepts & lineage

- Volume at price, HVAs and LVAs, volume edges and shelves, POC: [[concept_volume_profile]]
- Price consolidating in high-value areas and moving fast through low-value areas, edge-to-edge rotation: [[concept_auction_market_theory]]
- ONH/ONL/PDH/PDL as trapped-trader liquidity levels: [[concept_liquidity]], [[concept_support_resistance]]
- High-volume rejection-wick signal candle, wait for the close: [[concept_candlestick_patterns]], [[concept_price_action]]
- Weekly or daily bias with 4H or 1H execution: [[concept_multi_timeframe_analysis]]
- Entry on candle close or a 50–80% wick-retrace limit: [[concept_trade_execution]]

## Changes vs. earlier note

- **Confirmed:** location at the edge of a high-volume node on PDH/PDL/ONH/ONL, a wick-rejection signal candle that closes in the trade direction (wait for the close), and edge-to-edge targets through low-volume areas. The earlier note had these from T3 summaries.
- **Clarified:** the earlier note called bias only "a higher-timeframe directional filter". The playbook gives a concrete example: a weekly high-volume bottom-wick reversal candle at a volume edge means long bias.
- **Added:** 4H/1H execution timeframes, the stop rule (beyond the wick or the HVN edge), the 50–80% wick-retrace limit entry, the previous-day POC retest setup, the no-mid-zone rule, and the "2–3 profiles" guidance.
- **Added:** the limitation that it is not viable on spot forex because that market has no centralized volume.
- **Added:** `concept_liquidity` and `concept_candlestick_patterns` to `uses`, and two more related strategies.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/fredy-sarmiento-options-flow.md ===== -->

---
id: strategy_fredy_sarmiento_options_flow
type: strategy
title: "Fredy Sarmiento — Institutional Options Flow: Gamma Wall Reversal (index futures/options, day trading/scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [Institutional Options Flow Strategy, gamma wall reversal, options flow gamma reversal, Fredy Sarmiento strategy]
taught_by: [person_fredy_sarmiento]
featured_in: [channel_chart_fanatics]
uses: [concept_options_greeks, concept_volatility, concept_market_microstructure, concept_order_flow, concept_support_resistance, concept_trading_sessions_killzones, concept_scalping, concept_risk_reward_r_multiples, concept_trade_management, concept_position_sizing, concept_trading_psychology]
derived_from: [concept_options_greeks, concept_market_microstructure]
related: [strategy_carmine_rosato_orderflow_masterclass, strategy_jay_awtani_market_dna]
sources:
  - {title: "Chart Fanatics — Institutional Options Flow Strategy", url: "https://www.chartfanatics.com/strategies/institutional-options-flow-gamma-reversal-strategy", tier: T2}
status: verified-t2
---

# Fredy Sarmiento — Institutional Options Flow: Gamma Wall Reversal (index futures/options, day trading/scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/institutional-options-flow-gamma-reversal-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Fredy Sarmiento with this framework. He
reads index options positioning to find levels for trading index futures.
The page gives no biography or track record.

## Built for

- **Instruments:** the page lists index futures and index options; the
  execution examples are futures trades that use index options data as the
  map. The stop examples are on **NQ**. The page stresses that the trader does not
  need to trade options; options data is information for the futures trade.
- **Style:** day trading and scalping.
- **Timeframes:** intraday. No chart timeframe is named.
- **Session:** roughly the **first two hours of the US session**, when
  participation, liquidity and volatility are greater than in quieter parts
  of the day and same-day (0DTE) positioning is actively changing.
- **Frequency:** about **one or two quality opportunities a day**.

## Core idea

Large options positions leave dealers with exposure that they hedge in
futures. As price moves, delta changes (that change is gamma), so the hedge
must be adjusted, and that forced buying and selling can make certain
strikes act as barriers, magnets or accelerators. The trader turns options
positioning (gamma walls, open interest, convexity, with skew as context)
into a map of levels before the session. Then they wait for futures to
reach a level, read how price arrives, and trade the confirmed reaction
toward the next level. In short, the options level says where to look,
and price behaviour at that level decides whether there is a trade.

## Rules

1. **Check the calendar first.** Options expiration, triple witching, VIX
   expiration and large institutional roll or hedging periods can change
   how levels behave. A valid level on one of those days is not
   automatically tradeable.
2. **Build the institutional map before the session.** Mark the levels
   where options positioning is concentrated:
   - **Model 1, gamma:** the maximum-gamma area, the call wall and the put
     wall, with particular weight on 0DTE positioning.
   - **Model 2, open interest:** the largest concentrations of open
     interest over roughly a **90-day lookback**.
   - **Model 3, convexity:** areas of positive and negative convexity. The
     preferred path runs from one favourable positive-convexity area toward
     the next.
   - **Volatility surface and skew:** use them to see where volatility
     positioning is unusually concentrated. Skew is context only, never a
     standalone signal.
   - Do not read a big call or put print as directional sentiment. It may
     be a hedge, spread, volatility trade or part of a larger book.
3. **Wait for a level.** No trade while price sits between meaningful
   levels. If price never reaches one, there may be no trade that day.
4. **Read the approach speed.**
   - *Slow, controlled approach:* look for a direct rejection at the level.
   - *Fast, violent approach:* do not stand in front of it. Let price
     overshoot, then trade the **reclaim**: back above a lower level for a
     long, or back below an upper level for a short.
5. **Confirm the reaction.** Look for price rejecting or reclaiming the
   level, ideally with large futures orders appearing at that same level.
   Options positioning gives location; futures order flow gives
   confirmation.
6. **Enter near the level.** Do not chase once the reaction has travelled.
   A late entry widens the stop and shrinks the reward.
7. **Stop beyond the invalidation area,** meaning where the reaction thesis
   is clearly wrong. The NQ examples use roughly **30 to 50 ticks**
   (our conversion, not on the page: about 7.5 to 12.5 index points at
   NQ's 0.25 tick), depending on setup
   and conditions. The page says the principle matters more than the
   number.
8. **Target the next options-derived level** (the next gamma, OI or
   convexity area). With several contracts, take a partial as the first
   reaction develops, reduce risk once the trade moves favourably, and hold
   the rest for the larger target.
9. **Accept a failed level.** If price breaks a wall with strength and
   holds beyond it, stop fading it. Reassess which level has become
   dominant.
10. **Keep it selective.** Do not trade just because the market is open.

## Risk management

- **Per-trade risk:** defined by the structural stop beyond the level (the
  30 to 50 tick NQ examples). A fixed dollar or % amount is not specified in
  the playbook.
- **Sizing:** contract count must fit the account and a predefined risk.
  Extra contracts are for scaling out, not for adding risk. The aim is to
  control the dollar loss if the level fails.
- **Daily limit:** no number is given. The page says to recognise when a
  loss is affecting your decisions and to stop before one controlled loss
  turns into a bigger one. It names chasing, overtrading, revenge trading,
  sizing up after a loss and ignoring invalidation as the risks.
- **Weekly limit:** not specified in the playbook.
- **No-trade conditions:** OPEX, triple witching, VIX expiry, large
  roll or hedging periods, and price sitting between levels.

## What the playbook leaves unspecified

- Where the gamma, open-interest, volatility-surface and convexity data
  comes from, and how dealer positioning (its sign and size) is estimated.
- How concentrated positioning must be before a strike counts as a level.
- An objective test for a "slow" versus a "fast" approach, and what counts
  as a reclaim (a close back through, a time limit, a retest).
- What size of futures order counts as confirmation, and on what tool.
- Exact session times. The page says only the first two hours or so of the
  US session.
- How the convexity model turns into concrete entries. The page describes
  it mostly in concept.
- How much to scale out at the first partial, and when to move the stop.
- How to handle the options-expiry days, beyond treating them with
  caution.
- Any win rate, R:R figure or sample of trades.

## Evidence & claims

- The page reports **no win rate, R:R figure, P&L or payout**.
- The claim of about one or two quality opportunities a day is
  self-reported (T4).
- The 30 to 50 tick NQ stops are a risk parameter from the examples, not a
  result.
- The edge is described qualitatively, as a small invalidation distance
  against a large distance to the next level. No numbers support it, so no
  expectancy check is possible.

## Concepts & lineage

- Delta, gamma and 0DTE sensitivity driving dealer hedge adjustments →
  [[concept_options_greeks]]
- Dealer hedging as the mechanism that moves futures →
  [[concept_market_microstructure]]
- Volatility surface, skew, buying versus selling volatility →
  [[concept_volatility]]
- Options-derived walls and OI concentrations as reaction levels →
  [[concept_support_resistance]]
- Large futures orders at the level as confirmation →
  [[concept_order_flow]]
- Focus on the first two hours of the US session →
  [[concept_trading_sessions_killzones]]
- Tight-stop intraday execution → [[concept_scalping]]
- Small invalidation against a distant next level →
  [[concept_risk_reward_r_multiples]]
- Partials across multiple contracts and risk reduction →
  [[concept_trade_management]], [[concept_position_sizing]]
- Mindfulness after losses as part of risk control →
  [[concept_trading_psychology]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/gala-trades-price-action.md ===== -->

---
id: strategy_gala_trades_price_action
type: strategy
title: "Gala Trades — Price Action Strategy: Hourly Levels with Breaking Retest, Bounce & Rejection (stock options, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Gala Trade Price Action Strategy, Gala Trades price action, hourly level breaking retest, bounce and rejection setups]
taught_by: [person_gala_trades]
featured_in: [channel_chart_fanatics]
uses: [concept_price_action, concept_market_structure, concept_trend_following, concept_support_resistance, concept_multi_timeframe_analysis, concept_breakout_trading, concept_trading_plan, concept_order_flow, concept_options_greeks, concept_risk_reward_r_multiples, concept_position_sizing, concept_trade_management, concept_trading_journal_review, concept_trading_psychology]
derived_from: [concept_price_action, concept_dow_theory]
related: [strategy_vincent_desiano_break_retest, strategy_rajan_dhall_auction, strategy_brando_options_swing]
sources:
  - {title: "Chart Fanatics — Gala Trade Price Action Strategy", url: "https://www.chartfanatics.com/strategies/price-action-strategy", tier: T2}
status: verified-t2
---

# Gala Trades — Price Action Strategy: Hourly Levels with Breaking Retest, Bounce & Rejection (stock options, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/price-action-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Gala day trades short-dated options on individual stocks such as
Tesla and Palantir, using a plain price-action framework. The page notes he
cut his post-open waiting period over time, from 30 minutes down to one
five-minute candle.

## Built for

- **Instruments:** options, mainly short-dated contracts on single stocks
  (Tesla and Palantir in the examples). The page says the same chart
  framework also works on futures. Bookmap is used mainly for SPY, QQQ,
  ES and NQ; single stocks such as Tesla are usually traded without it.
- **Style:** day trading. Every position is closed the same day.
- **Timeframes:** **1-hour** for trend, levels and the pre-market plan.
  **5-minute** as the main confirmation and execution chart. **2-minute**
  to fine-tune timing.
- **Session:** the US cash session. Plans are built before the opening
  bell, and he normally takes no entry until the **first five-minute
  candle has closed**.

## Core idea

The 1-hour chart sets the direction, and a few clean hourly levels mark
where to act. Before the open, write out scenarios: which stock, which
level, which direction, which setup. Then wait for price to reach a
planned level and react on the 5-minute chart through one of three setups:
a breaking retest, a bounce or a rejection. All three join the next leg
of the existing trend. Entering close to the level keeps the stop small,
and the usual objective is about 1.5R to 2R.

## Rules

1. **Hourly trend.** Read the 1-hour structure, not trendlines. Higher
   highs and higher lows mean focus on calls. Lower highs and lower lows
   mean focus on puts. Small pullbacks are fine. If the trend is hard to read, drop
   the chart from the watchlist.
2. **Mark the hourly levels.** Keep only significant hourly pivots where
   price reversed or moved away with strong momentum. Favour candle bodies
   and the **open of a strong impulse candle** over wick extremes.
   High-confidence levels show a strong rejection or breakout, a clear
   pivot, little prior testing and clean structure. Remove a level once
   price keeps trading through it without reacting.
3. **Pre-market plan.** Review many charts but keep a small watchlist of
   the cleanest ones. For each idea, write the stock, the level, the
   direction and the setup that must appear, for example "Tesla puts on a
   rejection of hourly resistance". Check the economic calendar (inflation
   data, Fed announcements and other major releases), because these change
   how aggressively trades are managed.
4. **Wait out the open.** Normally take nothing until the first
   five-minute candle closes; even if a 2-minute setup appears earlier, he
   generally prefers to wait. Then check which
   prepared plans are still valid. Do not invent new ones on the spot.
5. **Timeframe agreement.** The 5-minute chart outranks the 2-minute. If
   the 2-minute looks ready but the 5-minute does not, wait until both
   agree.
6. **Market alignment.** For calls, prefer the major indices steady or
   rising. For puts, prefer them weak. Avoid longs while the indices sell
   off hard. A stock holding up while the indices fall shows relative
   strength, which adds confidence but never replaces the setup.
7. **Optional Bookmap check** (mainly SPY, QQQ, ES, NQ). Large resting orders
   sitting on a pre-marked hourly level add confidence. Bookmap alone never
   justifies an entry.
8. **Setup A: breaking retest.** In the trend direction, price breaks a key
   hourly level and a **5-minute candle closes beyond it**. Wait for the
   pullback to the level. The retest candle can wick back through but must
   close on the correct side. Enter near the level. If price never comes
   back, skip it rather than chase.
   - *Stop:* beyond the most extreme retest wick.
9. **Setup B: bounce.** In an hourly uptrend, price pulls back into hourly
   support. The best version has several candles testing the level, bodies
   holding above it and small wicks below. One rejection candle can do, but
   two or three holding candles are stronger confirmation. Enter once
   support has clearly held, not after a big move away from it.
   - *Stop:* slightly below the lowest wick of the bounce. If that stop is
     large relative to the reward, cut size or skip the trade.
10. **Setup C: rejection.** This is the bounce in reverse, for an hourly
    downtrend. Price rallies into hourly resistance, bodies stay below and
    wicks poke above. Enter as close to resistance as possible.
    - *Stop:* just above the highest rejection wick.
11. **Targets.** The first target is about **1.5R to 2R** in all three
    setups. The next hourly level is a secondary target. If that level is
    far away, close most of the position at the first target and leave a
    small runner. Anything past 2R is a bonus.
12. **Contract selection.** Use short-dated options with strikes near where
    the stock is expected to move during the session. Prefer tight bid-ask
    spreads. A slightly later expiry can give a smoother contract. In the
    Tesla example he chose that Friday's expiration over the nearest one,
    which damped some of the extra volatility.
13. **Manage the trade.**
    - On a normal trade, close about **half** near the first target. Keep
      more on if momentum is strong. Take more off if conditions turn
      uncertain.
    - Read momentum from the candles. Consecutive strong candles with
      little pullback mean stay in. Smaller candles, longer wicks or a
      rejection at the next level mean get defensive.
    - Trail the stop behind recent 5-minute swing highs or lows, not so
      tight that normal noise takes you out. Work it past entry so the
      remainder can no longer lose.
    - Hide the running P&L and manage from the chart.
14. **Close by the end of the day.** A failed setup is closed, never held
    overnight in hope. Time decay and implied volatility keep working
    against a held option.
15. **Frequency and re-entries.** Most days have **two or three trades**.
    If the first entry stops out and the setup is still valid, **one** more
    attempt is allowed. There is never a third attempt on the same setup.
    Stopping after one good winner is fine.
16. **Planned versus unplanned.** Most trades come from the plan. A clear
    unplanned setup can be taken at reduced size. Do not flip between calls
    and puts against the plan unless conditions change in a major way.
17. **Journal every trade** while it is fresh: entry, exit, stop, target,
    size, partials, setup type, whether it was planned, mistakes, emotional
    state and a trade grade. Grade the process, not the P&L.

## Risk management

- **Per-trade risk:** set the maximum acceptable dollar loss before placing
  the order, then size so the total dollar risk stays inside it. Options
  can slip past the planned stop; the page's example is a stop meant to
  lose 5% that loses more. A fixed % of account per trade is not specified
  in the playbook.
- **Comfort test:** a position whose planned loss you would not be at ease
  taking is oversized.
- **Sizing by quality:** size depends on confidence in the level, setup
  quality, stop distance, whether the trade was planned, market conditions
  and emotional state. A high-quality planned setup can get full size.
  Unplanned trades, weaker levels and uncertain conditions get less. In the
  recorded Tesla trade he also traded smaller because he was away from his
  usual setup.
- **Invalidation:** beyond the extreme retest, bounce or rejection wick.
- **Daily limit:** no dollar limit is given. Behavioural caps are about two
  or three trades a day, at most two attempts per setup, and being willing
  to stop after one good winner.
- **Weekly limit:** not specified in the playbook.

## What the playbook leaves unspecified

- A dollar or % risk per trade, or a daily loss limit.
- How "significant" an hourly pivot has to be, and how far back to look
  for levels.
- How to estimate the session's expected move when picking a strike, and
  which delta or days to expiry to use.
- Whether the stop is set on the underlying's chart (the wick) or on the
  option premium. The page treats the stop as a chart level and controls
  dollars through size, but also mentions a percentage stop.
- The exact confirmation candle for each setup, including how many holding
  candles a bounce or rejection needs.
- The size of the runner (only "a small percentage") and how far the trail
  sits behind structure.
- A latest entry time in the session.
- How news days change management. The page only says major releases
  affect how aggressively trades are managed.
- Any win rate or sample of trades.

## Evidence & claims

- **Target design:** about 1.5R to 2R per trade, with more than 2R treated
  as a bonus. This is a rule, not a reported result. By simple arithmetic
  (not stated on the page), break-even win rates would be 40% at 1.5R and
  about 33% at 2R.
- **Tesla call trade:** initial risk of about **$2,400** against a planned
  target of about **$4,800** (2R). The trade closed for a little over
  **$5,000**. Self-reported (T4). He graded it only three stars, citing a
  late entry above the support level, a trade outside the pre-market plan
  (the plan had been Tesla puts at 424 resistance), and closing everything
  at target instead of keeping a runner.
- The page gives **no win rate**, so no expectancy check is possible.

## Concepts & lineage

- 1-hour higher highs and lows to set the call or put bias →
  [[concept_market_structure]], [[concept_trend_following]]
- Reading candle bodies, wicks and closes at levels →
  [[concept_price_action]]
- Hourly pivots and impulse-candle opens as support and resistance →
  [[concept_support_resistance]]
- Breaking retest of an hourly level → [[concept_breakout_trading]]
- 1H for direction, 5m to confirm, 2m to time →
  [[concept_multi_timeframe_analysis]]
- Pre-market scenarios and the small watchlist → [[concept_trading_plan]]
- Bookmap resting liquidity as secondary confirmation →
  [[concept_order_flow]]
- Strike and expiry choice with theta and IV in mind →
  [[concept_options_greeks]]
- 1.5R to 2R objective → [[concept_risk_reward_r_multiples]]
- Dollar-risk sizing graded by setup quality → [[concept_position_sizing]]
- Partials, trailing behind 5-minute swings and runners →
  [[concept_trade_management]]
- Journal and process-based grading → [[concept_trading_journal_review]]
- Hiding P&L and the comfort test → [[concept_trading_psychology]]
- Lineage: classical trend structure read from swing highs and lows →
  [[concept_dow_theory]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/jadecap-liquidity-volatility.md ===== -->

---
id: strategy_jadecap_liquidity_volatility
type: strategy
title: "JadeCap — Intraday Liquidity & Volatility Model: New York Session Liquidity Raids (futures/forex, day trading/swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [JadeCap Liquidity Trading Strategy, Intraday Liquidity Volatility Model, session liquidity raid model, JadeCap model]
taught_by: [person_jadecap]
featured_in: [channel_chart_fanatics]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_fair_value_gap, concept_market_structure, concept_order_blocks_breakers, concept_trading_sessions_killzones, concept_multi_timeframe_analysis, concept_smt_divergence, concept_trading_journal_review]
derived_from: [concept_smart_money_concepts, concept_liquidity]
related: [strategy_tg_capital_trident, strategy_dhesi_liquidity_inversion, strategy_marco_trades_liquidity_grab, strategy_candace_lau_nq_sweep_reversal]
sources:
  - {title: "Chart Fanatics — JadeCap Liquidity Trading Strategy", url: "https://www.chartfanatics.com/strategies/intraday-liquidity-volatility-model", tier: T2}
status: verified-t2
---

# JadeCap — Intraday Liquidity & Volatility Model: New York Session Liquidity Raids (futures/forex, day trading/swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/intraday-liquidity-volatility-model. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits JadeCap with this intraday model. It
trades New York session raids on overnight and prior-day liquidity, and
both worked examples are NQ shorts. The page gives no biography.

## Built for

- **Instruments:** futures and forex. The pros list says crypto also works
  with slight adjustments. Both examples are **NQ**.
- **Style:** day trading first. Swing trades are possible when the higher
  timeframe agrees.
- **Timeframes:** **daily** for bias. **15m and 5m** for confirmation. One
  example enters from a **1H** FVG.
- **Session:** New York. The page's ideal window for setups is
  **9:30–11:30 AM EST**, listed among the conditions for a trade. Intraday trades may be closed around midday; one example exits
  near 12:15 PM.

## Core idea

Stop orders cluster just above recent highs and below recent lows. Price
often runs into those pools and then either reverses sharply or continues.
Start each day with a daily bias. Mark the prior day's and the Asian and
London session highs and lows. Wait for New York to take one of them, then
enter only after lower-timeframe confirmation: an FVG, a market structure
shift, a turtle soup (failed breakout), a breaker block, or divergence
between related markets. Target the opposite liquidity, and respect time
of day.

## Rules

1. **Set a daily bias** from the daily chart, using recent highs and lows,
   inefficiencies and where price is likely to go next.
2. **Mark session liquidity:** the previous day's high and low, the Asian
   session high and low, and the London session high and low.
3. **Wait for a liquidity raid in the New York session.** One of those
   levels must be taken out.
4. **Confirm on the 15m or 5m.** After the raid, require one of: a fair
   value gap, a market structure shift, a turtle soup (false breakout and
   reversal), or a breaker block. The overview also lists divergence
   between markets as a confirmation.
5. **Time window:** setups should form in the **9:30–11:30 AM EST**
   window, which the page calls the ideal window and lists among the
   conditions for a trade.
6. **Entry** (from the examples):
   - *Immediate:* short right after the sweep (here, of the previous day's
     high) once price fails to continue higher.
   - *Second chance:* short on a retracement into a fresh bearish FVG (15m
     or 1H) that rejects.
   - The page shows no long example; longs are presumably the mirror
     image.
7. **Stop:** beyond the sweep extreme, which is above the sweep high in
   both short examples.
8. **Targets:**
   - *Intraday:* opposite-side session liquidity, FVGs, or equal highs and
     lows. In the first example the target was the untouched Asian session
     low.
   - *Swing:* higher-timeframe liquidity (daily or weekly highs and lows),
     imbalances or major structure. Hold for days while the bias and
     structure still support it.
9. **Time-based exit:** if an intraday trade slows near midday, consider
   closing before the full target to avoid afternoon chop. Whether to stay
   in is a judgement call based on the clock, how price is behaving and
   your own risk tolerance.

## Risk management

- **Stop:** beyond the high or low of the liquidity sweep.
- **Time stop:** discretionary exit around midday if momentum fades.
- **Risk per trade ($ or %), position size, minimum R:R, daily or weekly
  loss limits:** Not specified in the playbook.
- **Partials:** mentioned as a skill that takes practice, with no rule
  given.
- **Record-keeping:** the page says confidence in the model comes from
  tracking outcomes and journaling.

## What the playbook leaves unspecified

- How to set the daily bias in concrete terms.
- The hours of the Asian and London sessions used to mark their highs and
  lows.
- Whether the raid itself must occur inside 9:30–11:30 AM, or only the
  entry.
- How to rank the five confirmation types, and what counts as "divergence
  between markets" (which instruments).
- Any minimum reward-to-risk, partial-profit or break-even rule.
- How forex traders should adapt a window built around the 9:30 AM
  equity open.
- How "volatility" is measured or used. It appears in the model's name
  but is never operationalised.
- A long-side worked example.

## Evidence & claims

- The page reports **no win rate, R:R, P&L or payout**.
- **NQ short, 15m:** a previous-day-high sweep failed. There were two
  entries, an immediate short and a later 15m FVG retest, both with stops
  above the sweep high. The exit came when price tagged the Asian low at
  roughly 12:15 PM EST. Self-reported (T4), with no R or
  dollar result.
- **NQ short from a 1H FVG:** an Asian-high sweep at the start of the
  session, entry inside the 1H bearish FVG, and the page says target was
  hit within the session. Self-reported (T4), with no R or dollar result.
- With no win rate or R:R, no expectancy check is possible.

## Concepts & lineage

- Stops above highs and below lows; previous-day and session highs and
  lows as pools → [[concept_liquidity]]
- Raid, then confirmed reversal or continuation; turtle soup →
  [[concept_liquidity_sweep_reversal]]
- FVG confirmation and FVG retest entries → [[concept_fair_value_gap]]
- Market structure shift → [[concept_market_structure]]
- Breaker block confirmation → [[concept_order_blocks_breakers]]
- Asian and London ranges, the 9:30–11:30 AM EST window and midday exits →
  [[concept_trading_sessions_killzones]]
- Daily bias with 15m, 5m or 1H execution →
  [[concept_multi_timeframe_analysis]]
- Divergence between related markets as confirmation →
  [[concept_smt_divergence]]
- Tracking outcomes and journaling to build confidence →
  [[concept_trading_journal_review]]
- Lineage (our attribution; the page speaks of institutional traders
  seeking stops but does not name ICT): ICT-style smart-money liquidity
  concepts →
  [[concept_smart_money_concepts]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/jared-tendler-psychology.md ===== -->

---
id: strategy_jared_tendler_psychology
type: strategy
title: "Jared Tendler — Trading Psychology Playbook: Emotion, Performance & the Mental Game (any market, trading psychology)"
partition: 01_chart-fanatics
layer: L7
aliases: [The Jared Tendler Trading Psychology Playbook, Full Psychology Masterclass, Mental Game of Trading, Jared Tendler psychology, zone map]
taught_by: [person_jared_tendler]
featured_in: [channel_chart_fanatics]
uses: [concept_trading_psychology, concept_trading_journal_review, concept_trading_plan, concept_expectancy]
derived_from: [concept_trading_psychology]
related: [strategy_umar_ashraf_5_stage, strategy_jeff_holden_momentum_model]
sources:
  - {title: "Chart Fanatics — The Jared Tendler Trading Psychology Playbook", url: "https://www.chartfanatics.com/strategies/full-psychology-masterclass", tier: T2}
status: verified-t2
---

# Jared Tendler — Trading Psychology Playbook: Emotion, Performance & the Mental Game (any market, trading psychology)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/full-psychology-masterclass. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Jared Tendler is a trading psychologist and the author of *The
Mental Game of Trading*. This Chart Fanatics page summarises his
masterclass on emotion and performance. It is a mental-game framework, not
an entry setup.

## Built for

- **Instruments / markets:** not specified. The framework applies to any
  market.
- **Style:** not specified. It is aimed at active traders managing their
  state during sessions.
- **Timeframes / sessions:** organised around a single trading session:
  before, during and after.
- **Audience:** traders whose results suffer from tilt, hesitation,
  discipline lapses or emotional carryover.

## Core idea

Emotion is not the enemy. It is the energy that lets the brain focus and
decide. Performance follows an inverted U, the **Yerkes–Dodson curve**: too
little emotion makes you flat and hesitant, too much makes your thinking
malfunction, and the middle is "the zone". Under rising emotion the
thinking brain shuts down **progressively**, and working memory shrinks.
That is why traders can see a mistake and still make it. Most "discipline
problems" are really emotional problems, so the work is to map your zone,
spot early warning signs, reset before the slide goes too far, and journal
so emotion does not carry into the next day.

## Rules

1. **Aim for the middle, not for zero emotion.** Learn which side you
   drift to. Too much energy needs calming down. Too little needs lifting,
   for example by reconnecting with your goals. Do not rely on market
   excitement for motivation, because it disappears when the market goes
   quiet.
2. **Write a Zone Map.** Describe your best state: how your body feels
   (breathing, posture, tension), how your focus feels, what your thinking
   sounds like, and the habits or conditions that usually get you there.
3. **Collect data on your warning signs for a few weeks.** Track each one
   during or after the session:
   - *Triggers*, such as being stopped by one tick, missing a trade, or
     boredom.
   - *Thoughts*, such as needing to win the loss back or not being able
     to miss another setup.
   - *Physical clues*, such as a tight grip, tense shoulders, leaning in, or
     shallow breathing.
   - *Perception shifts*, such as seeing setups that are not there,
     ignoring conflicting signals, or promoting average setups to A+.
   Jared offers a free Data Collection Worksheet for this.
4. **Separate correlation from causation** when studying your routines.
   Work out what a habit actually does to your state before building it
   into your pre-market process.
5. **Before the session (about 5 minutes):** check your physical,
   mental and emotional state. Consider your fuel mix, which the page says
   to adjust daily: physical energy
   (sleep, food, exercise), motivational energy (goals, growth and mastery
   rather than money alone), and emotional energy. Set one process goal,
   for example staying patient for the first 30 minutes.
6. **Treat carryover as leftover risk.** Yesterday's frustration raises
   today's baseline even when you feel fine. If you feel slightly off, note
   it.
7. **During the session:** notice energy and emotion rising or falling, and
   write one short note when something changes. Act early. On the page's
   scale, about 60% emotion can still be reset. Around 80% you know what is
   happening but cannot stop it. At 100% control is gone.
8. **Reset mid-session when you are slipping:**
   1. Name it: tell yourself plainly that you are frustrated.
   2. Move: stand up, stretch, and breathe deeply for about two minutes.
   3. Refocus on what the market is actually doing, not what you want it to
      do.
   4. Set a limit: one small trade at most, or a 15-minute break.
   **If you break that limit, the session is over.**
9. **When you are not in the zone,** trade less, be more selective and slow
   down. Weigh the **emotional expected value** of the next trade. When you
   are off your game, the upside of one more win is small and the downside,
   a spiral of revenge trades, is large. Sometimes the best trade is no
   trade.
10. **After the session: journal as a mental cool-down** (even 5 minutes).
    Record what you felt, when focus or control started to slip, and what
    helped or did not. List your top three emotional moments or lessons.
    Finish with an If–Then plan for tomorrow, for example: if I feel FOMO,
    take three deep breaths and wait for confirmation. Feeling too tired to
    journal usually means mental overload, which is a reason to do it.

## Risk management

- **Financial risk per trade, daily and weekly loss limits, sizing:** Not
  specified in the playbook. The page assumes the trader already has a
  strategy and risk plan.
- **Behavioural stop rule:** the mid-session reset sets a limit (one small
  trade at most, or a 15-minute break). Breaking it ends the session.
- **Emotional risk:** treat mental capital like account capital. When your
  state is poor, the emotional expected value of another trade is poor, so
  reduce activity or stop.
- **Carryover:** unresolved emotion from earlier sessions is treated as
  risk that compounds if it is not cleared through journaling.

## What the playbook leaves unspecified

- How to measure the 60%, 80% and 100% emotion levels. They are an
  illustrative scale with no scoring method.
- Financial limits that should go with the behavioural rules, such as a
  daily loss cap that ends the session.
- How long data collection should run before the Zone Map and warning
  signs are considered reliable. The page says only a few weeks.
- How to turn journal findings into rule changes, beyond the daily If–Then
  plan.
- What the Data Collection Worksheet contains. The page only links to it.
- How the framework connects to a specific strategy or to position sizing.

## Evidence & claims

- The page makes **no win-rate, R:R, P&L or payout claims**.
- It cites the **Yerkes–Dodson law** for the emotion–performance curve, and
  puts typical working-memory capacity at roughly seven items. Both are general psychology claims given without
  citations on the page. Their application to trading is the author's view
  (T4).
- The 60%, 80% and 100% thresholds and the claim that discipline problems
  are usually emotional problems are practitioner heuristics with no data
  (T4).

## Concepts & lineage

- Inverted-U emotion–performance curve, progressive shutdown, working
  memory, tilt and carryover → [[concept_trading_psychology]]
- Post-session journaling as a cool-down, warning-sign data collection and
  the top-three review → [[concept_trading_journal_review]]
- Pre-session check-in, one process goal and If–Then plans →
  [[concept_trading_plan]]
- Emotional EV: weighing small upside against large downside before the
  next trade → [[concept_expectancy]]
- Lineage: performance-psychology framing of trading discipline →
  [[concept_trading_psychology]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/jay-awtani-market-dna.md ===== -->

---
id: strategy_jay_awtani_market_dna
type: strategy
title: "Jay Awtani — Market DNA: Tape & Level II at DNA Zones (large-cap stocks/options and NQ/ES futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Market DNA Playbook, Market DNA strategy, DNA levels, DNA zones]
taught_by: [person_jay_awtani]
featured_in: [channel_chart_fanatics]
uses: [concept_order_flow, concept_market_microstructure, concept_liquidity, concept_support_resistance, concept_news_trading, concept_risk_reward_r_multiples, concept_trade_management, concept_leverage_margin]
derived_from: [concept_order_flow, concept_market_microstructure]
related: [strategy_carmine_rosato_orderflow_masterclass, strategy_yush_order_flow, strategy_fabio_valentini_amt_order_flow, strategy_carmine_rosato_lvn]
sources:
  - {title: "Chart Fanatics — Market DNA Playbook", url: "https://www.chartfanatics.com/strategies/market-dna-strategy", tier: T2}
status: verified-t2
---

# Jay Awtani — Market DNA: Tape & Level II at DNA Zones (large-cap stocks/options and NQ/ES futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/market-dna-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Jay Awtani teaches a free six-lesson masterclass on volume and
order flow on Chart Academy. Its topics include volume analysis, grading
setups, journaling, building playbooks, and his indicators (ATR, relative
volume, Camarilla pivots and moving averages).

## Built for

- **Instruments:** large-cap stocks with strong catalysts, stock options
  for leverage, and **NQ and ES futures**, since centralized exchanges
  report reliable order-flow data. **Forex is excluded**: with no central
  exchange, its volume and depth cannot be trusted. The page puts it bluntly:
  "you're getting lied to."
- **Style:** day trading by reading the tape and Level II (market depth).
- **When:** stocks during catalysts (earnings, news, political events,
  sector shifts). Futures during macro sessions (FOMC, CPI, NFP). **No
  trades in flat or range-bound sessions.**
- **Chart timeframe:** not specified.

## Core idea

Only buyers and sellers move price. Indicators, Fibonacci levels and
patterns just reflect what has already happened. The method finds **DNA
zones**, price areas that once launched huge directional moves. It then
watches the tape and order book there for the moment **aggressive orders
overwhelm passive liquidity walls**, the point where control flips. Entering
right at that flip lets the stop sit just past the zone, a few ticks away,
which makes asymmetric reward-to-risk possible. The page states the risk
lever directly: risk is cut by shrinking the stop distance, not by aiming
for bigger profits.

## Rules

1. **Choose the instrument.** A high-volume large-cap stock with a live
   catalyst (examples: NVDA on AI earnings, ARM on IPO momentum, ORCL on
   news), or NQ or ES during a macro-driven session. No forex.
2. **Mark the DNA zones.** These are price areas that once produced huge
   directional moves (**swings of 20 to 30%**) or explosive momentum.
   Treat them as **zones with a range**, not exact lines.
3. **Confirm the catalyst.** News or earnings are drawing participants in,
   with heavy relative volume showing the name is in play.
4. **Read passive against aggressive flow at the zone.** Identify the
   passive walls on the book that absorb flow, and watch how aggressive
   market orders hit them. The setup is valid when **aggression overwhelms
   absorption** at a major level.
5. **Long trigger.** At a support or DNA zone, aggressive buyers absorb the
   sell orders, the tape shows repeated market buys lifting the offer, and
   the passive sellers' wall fails.
6. **Short trigger.** At a resistance or DNA zone, aggressive sellers hit
   the bid again and again, the buyers at the level are absorbed, and
   sellers keep pressing.
7. **Entry.** As close as possible to the point where aggression confirms
   and control flips.
8. **Stop.** Just beyond the liquidity zone that defines the DNA level.
9. **Minimum reward-to-risk.** At least **3:1**.
10. **Exits.**
    - Take partials at the first strong reaction or intraday pivot.
    - Keep the remainder until aggression on the tape flips against you (for a
      short, buyers suddenly take over).
    - Trail the stop behind newly formed aggressive zones.
    - Never let a trade run past the DNA zone once the zone is
      invalidated.

**Worked example: NVDA long.** Earnings beat with bullish AI guidance, and
volume surged. A prior demand zone, where aggressive buyers had once driven
a major rally, became the DNA zone. On the tape, buyers kept lifting
offers and the passive sellers were absorbed. Entry came as buyers took
control at the zone, with the stop just below it. Partials were scaled at
intraday reaction points, and the rest rode the momentum continuation.

## Risk management

- **Reward-to-risk:** at least 3:1.
- **Stop:** tight and structural, just past the DNA zone's liquidity.
- **Invalidation:** if the DNA zone fails, exit. Never hold past it.
- **Risk per trade ($ or %), position size, options sizing:** not specified
  in the playbook.
- **Daily or weekly limits:** not specified in the playbook.
- **Liquidity caveat:** small caps and thin options chains can cause
  slippage, so stick to very liquid names.

## What the playbook leaves unspecified

- How far back to look for DNA zones, how wide a zone is, and whether a
  "20 to 30% swing" applies to futures as well as stocks.
- Objective thresholds for "aggression overwhelms absorption", such as
  prints per second, lot size or delta. The masterclass topics suggest
  tools like relative volume and ATR, but none is given here.
- How to size or structure options trades (strike, expiry), when options
  are used for leverage.
- How a stop only a few ticks wide is reconciled with "just beyond the
  zone" when the zone itself has a range.
- Session times for stocks (open only, or all day) and for futures (around
  the release, or the whole session).
- How setups are graded, which the masterclass mentions.

## Evidence & claims

- **"Most setups naturally provide 4–5:1+"** reward-to-risk. Self-reported
  (T4).
- The **NVDA example**: per the page, price never came back to the stop
  and the trade paid well relative to its risk. Self-reported (T4), with no
  prices given.
- The pros call these high-conviction trades where the odds are stacked in
  your favour. Qualitative and self-reported (T4).
- **No win rate is stated**, so E = p×RR − (1−p) cannot be computed. For
  reference, the break-even win rate is 25% at 3:1 and about 17 to 20% at
  4 to 5:1.

## Concepts & lineage

- Tape reading and Level II, aggressive against passive orders, absorption
  → [[concept_order_flow]]
- Centralized against decentralized markets; why forex depth is
  unreliable → [[concept_market_microstructure]]
- Liquidity walls on the book → [[concept_liquidity]]
- DNA zones as past launch points that price reacts to again →
  [[concept_support_resistance]]
- Earnings, IPO and macro releases as catalysts →
  [[concept_news_trading]]
- A 3:1 minimum and tight stops for asymmetric R →
  [[concept_risk_reward_r_multiples]]
- Partials at pivots, trailing behind new aggressive zones, exit when the
  tape flips → [[concept_trade_management]]
- Stock options as a leverage vehicle → [[concept_leverage_margin]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/jeff-holden-momentum-model.md ===== -->

---
id: strategy_jeff_holden_momentum_model
type: strategy
title: "Jeff Holden — Momentum Model Performance Development (stocks/futures, day-trading development loop)"
partition: 01_chart-fanatics
layer: L7
aliases: [Momentum Model, Momentum Model Performance Development Playbook, SMB Momentum Model, five whys trade review]
taught_by: [person_jeff_holden]
featured_in: [channel_chart_fanatics]
uses: [concept_trading_journal_review, concept_trading_psychology, concept_trading_plan, concept_position_sizing, concept_trade_management, concept_moving_averages, concept_vwap, concept_support_resistance]
derived_from: [concept_trading_journal_review, concept_trading_plan]
related: [strategy_jared_tendler_psychology]
sources:
  - {title: "Chart Fanatics — Jeff Holden - Momentum Model Performance Development Playbook", url: "https://www.chartfanatics.com/strategies/momentum-model-performance-development", tier: T2}
status: verified-t2
---

# Jeff Holden — Momentum Model Performance Development (stocks/futures, day-trading development loop)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/momentum-model-performance-development. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Jeff Holden is described as SMB's development and recruiting
lead. The playbook draws on the SMB desk's practice of grading trades,
reviewing them and sizing them by quality.

## Built for

- **Instruments:** stocks and futures. It is built around active intraday
  equities trading and can be adapted to futures, forex, crypto or metals,
  but only after studying how that product behaves.
- **Style:** day trading. This is a **performance-development framework**,
  not a single entry pattern.
- **Cadence:** log mistakes daily, review weekly, and repeat the loop
  whenever new friction appears. The chart examples are intraday: a
  backside VWAP reclaim and a 9 EMA continuation in Microsoft.
- **Tools:** a daily report card, chart review, trade grading, a playbook
  template, VWAP, the 9 EMA, volume and key levels.
- **Who it suits:** traders still building consistency, or rebuilding
  baseline execution after market conditions change.

## Core idea

Repeated mistakes become fuel for improvement through one loop that never
gets restarted. Log mistakes, let a week of data show the pattern, find the
root cause of the most important one with the **five whys**, turn the
diagnosis into a specific playbook fix, and treat friction during
implementation as the next piece of data. The edge comes from **stacking
small wins** instead of hunting for one big breakthrough. Pair it with one
well-built **baseline playbook** and a separate **A+ playbook** for rare
events, so that size always matches trade quality.

## Rules

**The development loop**

1. **Log mistakes without judgment (one week).** Every meaningful mistake
   goes in the daily report card: selling too early, ignoring a stop, a
   badly placed stop, entering with no defined structure. A mistake is
   information, not grounds for self-attack.
2. **Pick one mistake.** After a week, choose the recurring mistake whose
   fix would bring the most progress. If both stop-loss and profit-taking
   mistakes show up, **fix the stop-loss (risk) mistake first**.
3. **Diagnose with the five whys** (from Toyota's production process). Keep
   asking why until the real cause appears, usually around the fourth or
   fifth answer. *Invalidation:* a diagnosis that gets no further than
   "I messed up" is incomplete.
4. **Turn the diagnosis into a specific, measurable fix.** Example: if the
   stop was never tied to structure, define structure, invalidation and
   risk before entry. If the setup only works when the broad market is
   aligned, write a separate playbook variant for that condition. "Be more
   disciplined" is not a fix.
5. **Test it next session and work through friction.** Fast markets,
   hesitation and old habits will push back. That does not mean the fix
   failed; it is the next input to the loop. Aim for the next small win:
   one correct stop, one partial held longer, one marginal trade skipped,
   one B trade sized correctly. Then repeat.

**Playbook and sizing rules**

6. **Build one baseline playbook first.** Define the setup, its conditions
   and its risk, and get feedback until it is repeatable and scalable. Only
   then add more. One playbook often grows into variants as conditions
   change.
7. **Keep baseline and A+ apart.** The page frames a career as baseline
   plus A+. Baseline trades keep execution sharp. A+ trades are rare, sit
   in the tail of the distribution, and get their own playbook. Never force
   A+ treatment onto an A, B or C trade.
8. **Grade the trade before you size it** (SMB, as a share of the daily
   stop):
   - A+: up to **80%** of the daily stop
   - A: up to **30%**
   - B: up to **15%**
   - C: up to **5%**

**Chart examples used to illustrate the loop**

9. **Backside VWAP long (diagnosing a stop mistake).** After a selloff,
   price puts in a low, then a higher low, consolidates, and pushes back
   toward VWAP as shorts cover and buyers step in. The stop goes below the
   higher low, the point of maximum pain that invalidates the trade. It
   should not be a tight stop placed where it merely feels comfortable.
10. **MSFT 9 EMA continuation (diagnosing an early exit).** A stock coming
    out of a downtrend pushes into resistance (455). The first test is
    sold, but buyers reclaim it quickly along the 9 EMA, which shows
    urgency. *Trigger:* a break back through the key area and the
    consolidation high, with volume and visible buyer urgency. *Stop:* below the wick or support
    where buyers stepped in. *Management:* hold while price respects the 9
    EMA and buyers stay urgent. Trail with the 9 EMA and exit on a
    meaningful close below it or a clear change in buyer behaviour.

## Risk management

- **Allocation by grade:** A+ ≤80%, A ≤30%, B ≤15%, C ≤5% of the daily
  stop. The page stresses that the discipline of matching risk to quality
  matters more than the exact percentages.
- **Daily stop:** it serves as the risk budget, but its **size is not
  specified in the playbook**.
- **Stops:** structural only, below the higher low or the defended wick or
  support. Never placed just to make the position size feel easier.
- **Priority:** fix risk mistakes before exit-optimisation mistakes.
- **No-trade rules:** do not trade a mistake you have not diagnosed. Do not
  size above the grade (the page says a C trade with A+ risk is "hope with
  leverage"). Do not apply an A+ playbook to a baseline trade. Do not carry
  a playbook into a new product without studying it. Do not drop the
  process because of friction.

## What the playbook leaves unspecified

- How big the daily stop is, as a dollar amount or % of the account, and
  what happens after it is hit.
- Objective criteria for grading a trade A+, A, B or C.
- How to define a "meaningful" mistake, and what a report card should
  contain.
- A measurable test of whether a fix has worked: how many sessions, and
  which metric.
- Targets for the VWAP and 9 EMA examples, beyond trailing.
- The five-whys ChatGPT resource the page mentions. Its link is missing
  from the scraped text.

## Evidence & claims

- The page makes **no win-rate, R:R, P&L or payout claims**. Its claims are
  qualitative: that small wins compound into momentum, and that traders who
  process mistakes grow faster. Both are self-reported (T4).
- With no outcome statistics, no expectancy check is possible. The model is
  a review process to be judged with your own journal data.

## Concepts & lineage

- Daily report card, weekly review, five-whys root-cause analysis →
  [[concept_trading_journal_review]]
- Treating mistakes as information, friction as feedback, and small wins as
  a source of confidence → [[concept_trading_psychology]]
- Baseline and A+ playbooks, and playbook variants →
  [[concept_trading_plan]]
- Allocating the daily stop by trade grade → [[concept_position_sizing]]
- Defining the reason to exit beforehand, trailing with the 9 EMA →
  [[concept_trade_management]], [[concept_moving_averages]]
- Backside reclaim toward VWAP → [[concept_vwap]]
- Key resistance (MSFT 455) and structural invalidation →
  [[concept_support_resistance]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/jj-simon-fair-pricing.md ===== -->

---
id: strategy_jj_simon_fair_pricing
type: strategy
title: "JJ Simon — Fair Pricing Theory: Continuation & Reversion (Nasdaq futures, 1-minute scalping)"
partition: 01_chart-fanatics
layer: L4
aliases: [fair pricing theory, fair value theory, JJ Simon strategy, fair price reversion]
taught_by: [person_jj_simon]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_trading_sessions_killzones, concept_news_trading, concept_market_structure, concept_multi_timeframe_analysis, concept_prop_firm_risk_rules, concept_position_sizing, concept_risk_reward_r_multiples, concept_risk_of_ruin_drawdown, concept_backtesting, concept_scalping, concept_market_regimes]
derived_from: [concept_mean_reversion, concept_auction_market_theory]
related: [strategy_fabio_valentini_amt_order_flow, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — JJ Simon’s Fair Pricing Theory Strategy", url: "https://www.chartfanatics.com/strategies/fair-pricing-theory-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists Fair Pricing Theory by JJ Simon)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "SozAI — The Strategy Behind My $1.6M in Prop Firm Payouts (transcript & summary)", url: "https://sozai.app/transcript/strategy-behind-1-6m-prop-firm-payouts/", tier: T3}
  - {title: "SozAI — Backtesting JJ Simon's NQ Strategy | Fair Value Theory", url: "https://sozai.app/transcript/backtesting-jj-simon-nq-strategy/", tier: T3}
status: verified-t2
---

# JJ Simon — Fair Pricing Theory: Continuation & Reversion (Nasdaq futures, 1-minute scalping)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/fair-pricing-theory-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** JJ Simon is a Nasdaq futures scalper whose risk model is built
around prop-firm evaluation and funded accounts. The earlier note's sources
tie him to $1.2M to $1.8M+ in prop payouts (T4, see Evidence).

## Built for

- **Instruments:** futures. The examples that name a market refer to
  Nasdaq (NQ).
- **Style:** scalping.
- **Execution chart:** 1-minute. Context comes from the prior 6 to 12 hours,
  read on the 1-minute or a 5-minute chart.
- **Window:** roughly the first 90 minutes of a major session. In New York
  that is **9:30 to 11:00 AM ET**. The same logic applies to the Asia,
  London and New York afternoon sessions. About 11:00 AM to 2:00 PM ET is
  described as low volume, and fresh participation can arrive around
  2:00 PM ET.
- **Accounts:** mainly prop-firm evaluation and funded accounts. Live
  personal accounts are handled differently (see Rules).

## Core idea

Each event that brings in new volume sets a **fair price**: a session open,
or the price just before a scheduled news release. When new volume arrives,
price displaces away from that level. The trader can first ride the
**continuation** away from fair price. Once the move is stretched, the
trader can trade the **reversion** back toward it, but only after a
confirmed momentum shift. Fair price is not a fixed support or resistance
line. It is reassessed whenever a different event takes over the market.

## Rules

1. **Set the fair price from the event now driving the market.**
   - *Normal session:* the opening price (9:30 AM ET for New York).
   - *Scheduled news* (examples: CPI and PPI at 8:30 AM ET): the price just
     before the release. The market already knew the release was coming and
     had the forecasts. On big news days this pre-news price can stay more
     important than the 9:30 open.
   - *Unexpected news* (a surprise announcement, speech or tweet): do not
     expect a return to the old level. Let the move play out and use the
     next consolidation as the new fair price.
2. **Read the larger context.** Look back about 6 to 12 hours to see the
   prior directional move and whether it may start reverting.
3. **Continuation trade.** If the opening displacement is strong, breaks
   relevant structure and agrees with the bias, enter in its direction. The
   opening candle alone is not enough.
4. **Reversion trade.** Once price is stretched from fair price, stop
   chasing it. Never fade a move just because it looks extended. Wait for
   one of two confirmations pointing back toward fair price:
   - **Displacement Candle (DC):** the body is larger than the previous
     candle's body, it closes beyond the previous candle's wick, and it
     displaces a candle of the opposite colour.
   - **Break of Structure (BOS):** a candle closes through a meaningful
     prior swing high or low. A wick through the level does not count. The
     clearer the structure, the stronger the signal. JJ ranks BOS as
     slightly stronger than DC.
   In both cases, enter only after the confirming candle has closed.
5. **Target.** For reversions, the fair price itself: the 9:30 open or the
   pre-news price.
6. **Unexpected-news continuation.** Fixed targets are optional here. Hold
   while structure keeps going your way, and get out when price closes
   through meaningful structure in the opposite direction.
7. **Stops and targets by account type:**
   - *Evaluation:* mechanical. Example: a **25-point stop with a 38-point
     target** (about 1:1.5). If the opening candle is unusually large, scale
     to **50 points / 76 points** and halve the contracts. Stops used across
     setups and accounts are about **25, 37.5, 50 and 75 points**, chosen
     from the account model and historical testing rather than chart
     invalidation. More valid DC entries are taken in evaluations.
   - *Funded:* more selective, with BOS entries preferred. With no
     restrictive consistency rule, a target of **50, 75, 100+ points** is
     allowed when fair price is that far away. With a consistency rule,
     take smaller and more repeatable wins.
   - *Live personal account:* focus on reversions, BOS entries and
     expected-news reversions, with stops and targets placed on market
     structure.
8. **Three-Loss Rule.** If **three reversion trades in a row fail in the
   same session**, stop taking reversions for that session. The market may
   be trending and setting a new fair value.
9. **Keep reassessing fair price.** Drop an old fair price once value has
   clearly moved. Signs include unexpected news, a new consolidation, a
   strong trend, or repeated failed reversions.
10. **Layering (account management).** Across several prop accounts, put
    different valid entries on different accounts. For example, the first
    DC goes on one account and a later BOS on another. This avoids exposing
    every account to the same single outcome.

## Risk management

- **Per trade:** a fixed point stop for each account model (25, 37.5, 50 or
  75 points). When the stop distance changes, the contract count changes in
  inverse proportion, so the dollar exposure stays roughly constant.
- **Reward-to-risk:** about 1:1.5 in evaluations (25 to 38 points). Funded
  and live targets are larger and depend on structure.
- **Session limit:** the Three-Loss Rule applies to reversion trades. No
  daily dollar loss limit is specified in the playbook.
- **Account rules:** the profit target, drawdown and consistency rules of
  each prop firm shape both sizing and targets.
- **Backtesting the account model:** measure the **evaluation pass rate**
  under the firm's real rules, not just raw P&L. The page's worked example:
  a $100 evaluation that passes 25% of the time costs about $400 per funded
  account ($100 ÷ 25%). Compare that cost with the expected payout. JJ
  suggests running about **50 evaluation backtests** to reduce small-sample
  noise.
- **Dollar risk per contract, or as a % of the account:** not specified in
  the playbook.

## What the playbook leaves unspecified

- What separates a "meaningful" structure from noise for BOS, and what
  "extended" means before a reversion is allowed.
- How exactly the 6 to 12 hour lookback sets the bias, and how a conflict
  between that bias and the opening displacement is settled.
- Stops for reversion entries on live accounts. The page says only that
  they are structure-based.
- How large the "new consolidation" after unexpected news must be, and how
  long it must last.
- Which stop size (25, 37.5, 50 or 75) goes with which setup or account.
  The page says only that it comes from historical testing.
- Rules for the Asia, London and afternoon-session versions, which are
  mentioned but not given in detail.
- Any daily dollar loss limit or rule for continuation-trade losses.

## Evidence & claims

- **On the playbook page:** no win rate or P&L is claimed. The 1:1.5 ratio
  is a risk setting, not a result. The $100 / 25% / $400 figures are a
  worked example of the pass-rate method, not reported results.
- **Payout claims (from the earlier note's sources):** $1.2M to $1.8M+ in
  prop payouts across summaries, and one video is titled "$1.6M in Prop
  Firm Payouts". All self-reported (T4).
- **Independent NQ 1-minute backtest (SozAI, T3):** about **52% win rate,
  1.66 profit factor**, but only *after filtering and parameter changes*,
  which raises overfitting risk ([[concept_overfitting_validation]]).
- **Conflicting third-party summary (T3, unverified):** one summary cited
  about a 20% win rate with R:R up to 1:4. The playbook's funded-account
  targets of 50 to 100+ points would give 1:2 to 1:4 if paired with a
  25-point stop, but the page does not state the funded-account stop and
  gives no win rate.
- **Expectancy check, E = p×RR − (1−p), in R** (illustrative, because the
  win rates and R:R come from different sources):
  - 52% at the evaluation 1:1.5: E = 0.52×1.5 − 0.48 = **+0.30R**.
    Break-even at 1:1.5 needs p = 40%.
  - 20% at 1:4: E = 0.20×4 − 0.80 = **0.00R**, which is break-even before
    costs.

## Concepts & lineage

- Reverting toward the event-defined fair price after a confirmed shift →
  [[concept_mean_reversion]]
- Fair price as the market's current accepted value, which shifts when new
  information arrives. This link is the knowledge base's interpretation;
  the page never names AMT → [[concept_auction_market_theory]]
- Session opens, the 9:30 to 11:00 window and the afternoon lull →
  [[concept_trading_sessions_killzones]]
- Scheduled versus unexpected news, and the pre-news price as fair value →
  [[concept_news_trading]]
- Displacement Candle and Break of Structure confirmations →
  [[concept_market_structure]]
- A 6 to 12 hour context read with a 1-minute trigger →
  [[concept_multi_timeframe_analysis]]
- Three-Loss Rule as a switch that detects trend days →
  [[concept_market_regimes]], [[concept_risk_of_ruin_drawdown]]
- Fixed point stops, halving contracts as stops double, layering →
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]]
- Evaluation, funded and consistency rules, and pass-rate economics →
  [[concept_prop_firm_risk_rules]], [[concept_backtesting]]
- Execution on a 1-minute chart → [[concept_scalping]]

## Changes vs. earlier note

- **Fair price definition.** The earlier note said fair price is "usually
  the New York open or pre-open" (T3). The playbook says it is the **9:30 AM ET
  open** in normal sessions and the **price just before** a scheduled
  release on news days, and that the pre-news price can override the 9:30
  open.
- **News handling, corrected.** The earlier note said news releases
  "reset" fair price (T3). The playbook separates **scheduled** news, where
  the pre-news price stays fair and price is expected to revert to it, from
  **unexpected** news, where a new consolidation becomes the new fair price.
- **Setup grading dropped.** The earlier note's "HTF mean reversion + LTF
  continuation" framing with A+/A/B grades (T3) does not appear on the
  page. The page uses two entry models (DC and BOS, with BOS slightly
  stronger) and a 6 to 12 hour context window.
- **R:R conflict narrowed.** The playbook confirms **about 1:1.5** (25 to
  38 points) for evaluations, and allows 50 to 100+ point targets on funded
  accounts without consistency rules. The ~20% / 1:4 figure is still
  unconfirmed and now appears only under Evidence.
- **Three-loss rule confirmed and narrowed.** It covers **three
  consecutive failed reversion trades in the same session**, and it stops
  only reversions for that session.
- **"Less effective on live accounts", reframed.** The playbook does not
  say this. It says the fixed stops and targets are designed around prop
  rules. On a live account JJ would favour reversions, BOS entries and
  expected-news reversions, with stops and targets set by structure.
- **Added:** the exact DC and BOS definitions, session timing, the ladder of
  stop sizes, halving contracts when stops double, layering across
  accounts, and pass-rate backtesting (about 50 runs).
- **VWAP removed from `uses`.** The playbook never mentions VWAP. The
  earlier "POC/VWAP reversion" cross-link was editorial.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/kris-verma-shorting.md ===== -->

---
id: strategy_kris_verma_shorting
type: strategy
title: "Kris Verma — Small-Cap Shorting: Gap Fades, Backside Parabolics & Halt Exhaustion (small-cap stocks, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Kris Verma’s Small-Cap Shorting Strategy", small-cap gap fade, backside parabolic short, multi-halt exhaustion short, share recycling]
taught_by: [person_kris_verma]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_market_microstructure, concept_liquidity, concept_trading_sessions_killzones, concept_support_resistance, concept_trade_management, concept_position_sizing, concept_probability_fat_tails, concept_performance_metrics, concept_backtesting]
derived_from: [concept_mean_reversion]
related: [strategy_steven_dux_small_cap_short, strategy_marios_stamatoudis_parabolic_short, strategy_alex_temiz_first_red_day, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — Kris Verma’s Small-Cap Shorting Strategy", url: "https://www.chartfanatics.com/strategies/shorting-strategy", tier: T2}
status: verified-t2
---

# Kris Verma — Small-Cap Shorting: Gap Fades, Backside Parabolics & Halt Exhaustion (small-cap stocks, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/shorting-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Kris Verma shorts small-cap stocks. His playbook combines a
data-driven base with time-of-day rules, behaviour checks and share
recycling. The page gives no further biography.

## Built for

- **Instruments:** small-cap stocks that gap up sharply, typically driven
  by promotion, hype or thin pre-market trading instead of any genuine
  improvement in the business.
- **Style:** scalping and day trading, short side only.
- **Time window:** pre-market through early morning, **4:00 to 10:00 AM**,
  is preferred. The edge fades after about **12:00 PM**, and trading is
  usually cut back or stopped after midday.
- **Timeframe:** no chart timeframe is specified.

## Core idea

Weak small-caps often use sudden spikes in liquidity to sell stock, so
their gaps tend to fade. The page notes that more volume and more traders
in recent years mean failed fades now often squeeze hard before the stock
finally drops. The playbook therefore refuses to guess front-side tops. It
waits for behavioural proof that the move is failing, uses **wide
fixed-percentage stops** to survive manipulation, and **recycles shares**
through ranges. It judges results by overall profit factor rather than
textbook R:R.

## Rules

1. **Filter the universe.**
   - Market cap: **under $100M preferred, about $200M maximum**.
   - Institutional ownership: **under about 40% preferred**.
   - Gap strength: large percentage gaps only. Avoid smaller moves of
     **about 20 to 40%**, which are less reliable now that volatility and
     ranges have expanded.
2. **Setup A: gap-up short with fade validation** (the page labels this
   "ADF behavior" without defining it).
   - No pre-market entries. Wait for the open.
   - The stock must start fading and trade weak relative to its open.
   - **10:00 AM check:** below the open, with volume falling as price
     drops, means the setup is confirmed.
   - Short into pops or bounces. Never short the low of a flush.
   - *Invalidation:* if the stock is holding above the open at 10:00,
     reduce or remove the risk.
3. **Setup B: backside parabolic short** (the page calls it the primary
   edge).
   - A large move has already happened, and topping signs appear: upper
     wicks, failed pushes, slowing momentum, volume falling as price fades.
   - Skip the first wobble. Act only once the stock has clearly rolled
     over from front side to backside.
   - Enter on bounces during the fade, never at the lows.
   - Expected downside, based on historical pullbacks: **about 30 to
     40%**. The goal is consistency, not catching every move. This setup
     works best earlier in the day.
4. **Setup C: multi-halt exhaustion short.**
   - No entries during the early up-halts. Consider a short only after
     **several up-halts (commonly 4 to 5)**, when resumption candles show
     brief dips followed by pushes (forced covering) and the extension is
     historically extreme.
   - Base the entry on how far the stock has already run, not on a guess
     about the next halt. Keep size conservative, because these names are
     volatile and illiquid.
5. **Stops.**
   - **Do not use pre-market highs as stops.** A break above them often
     sets off short covering before the reversal.
   - Use a **fixed-percentage wide stop** from the entry, so manipulation
     does not shake you out. Staying in the trade matters more than a tight
     stop.
6. **Time-based management.**
   - *10:00 AM rule:* below the open, downside continuation is more likely.
     Above the open, reduce risk or consider exiting.
   - *30-minute rule:* if the trade is working after about 30 minutes, keep
     holding. If price is reclaiming or stalling, reassess.
   - *Ongoing checks:* volume behaviour, signs of manipulation, the overall
     strength of small caps, and sympathy moves in other gappers.
7. **Recycling.**
   - When a stock ranges instead of fading cleanly, take partial profits
     into sharp drops near support.
   - Re-short bounces into prior support that has turned into resistance,
     and repeat within the range.
   - Use recycling when the stock grinds against you. The aim then shifts
     from directional conviction to limiting the damage.

**Worked example: CRCL multi-day backside short.** CRCL was in an extended
multi-day run. The short came only after the move stalled, red candles
appeared and selling pressure became visible. The position was held
through the first push down. Partials were taken at the prior day's close,
a level where a bounce was likely. The bounce was re-shorted into
resistance, and the cycle was repeated.

## Risk management

- **Stops:** wide, at a **fixed percentage** from entry, never at
  pre-market highs. **The percentage is not specified in the playbook.**
- **Accepted trade-off:** a higher win rate in exchange for larger single
  losses. Judge the method by overall profit factor.
- **Sizing:** kept controlled. Conservative on multi-halt shorts. No single
  trade may put the account at risk.
- **Outlier risk:** thin liquidity and halts can push price beyond expected
  levels.
- **Costs:** hard-to-borrow fees and locate costs eat into profit.
  Recycling reuses located shares, and the choice of broker matters.
- **Risk per trade, daily or weekly loss limit:** not specified in the
  playbook.

## What the playbook leaves unspecified

- The stop percentage, and how it varies by setup or stock price.
- The minimum gap size. The page says only to avoid moves of roughly 20 to
  40%.
- What "ADF behavior" means.
- How many consecutive red candles or failed pushes confirm a backside
  move, and on which chart timeframe.
- A conflict in timing: the preferred window starts at **4:00 AM**
  pre-market, yet Setup A forbids pre-market entries. The page never says
  which setups, if any, may be entered pre-market.
- The size of partials and re-entries in recycling, and how far a range may
  stretch before recycling stops.
- The data behind the "data-backed edge" (sample, period, metrics).

## Evidence & claims

- The pros claim a **"Proven, data-backed edge"**. Self-reported (T4); the
  page shows no statistics.
- The stops are described as producing a **higher win rate with larger
  individual losses**. This is qualitative and self-reported (T4), with no
  figures.
- **About 30 to 40% downside targets** come from the trader's own read of
  historical pullbacks. Self-reported (T4).
- The CRCL example is called profitable but gives no prices or P&L (T4).
- With no win rate or R:R given, no expectancy check is possible. Note that
  with wide stops and a high win rate, the outcome depends on how large the
  tail losses are, so profit factor should be measured directly.

## Concepts & lineage

- Fading hype gaps back toward value → [[concept_mean_reversion]]
- Halts, thin floats, locates and borrow costs, forced covering →
  [[concept_market_microstructure]], [[concept_liquidity]]
- The 4:00 to 10:00 AM window, the 10:00 AM check, the 30-minute check, the
  midday cutoff → [[concept_trading_sessions_killzones]]
- Prior support turning into resistance in recycling; the prior day's close
  as a bounce level → [[concept_support_resistance]]
- Partials, re-entries, reducing risk when the stock holds above the open →
  [[concept_trade_management]]
- Conservative size and no single account-threatening trade →
  [[concept_position_sizing]]
- Squeeze and outlier risk from wide stops →
  [[concept_probability_fat_tails]]
- Profit factor over R:R, plus regular backtesting and review →
  [[concept_performance_metrics]], [[concept_backtesting]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/kyle-williams-first-red-day.md ===== -->

---
id: strategy_kyle_williams_first_red_day
type: strategy
title: "Kyle Williams — Small Cap Short Selling Playbook: First Red Day and Parabolic Short (US small-cap stocks, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Kyle Williams Small Cap Short Selling Playbook, Kyle Williams First Red Day, FRD short, mini-bubble short, intraday parabolic short]
taught_by: [person_kyle_williams]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_market_sentiment, concept_support_resistance, concept_price_action, concept_vwap, concept_volatility, concept_market_microstructure, concept_risk_reward_r_multiples, concept_position_sizing, concept_trade_management, concept_trading_journal_review, concept_trading_psychology]
derived_from: [concept_mean_reversion, concept_market_sentiment]
related: [strategy_alex_temiz_first_red_day, strategy_steven_dux_small_cap_short, strategy_marios_stamatoudis_parabolic_short, strategy_kris_verma_shorting]
sources:
  - {title: "Chart Fanatics — Kyle Williams Small Cap Short Selling Playbook", url: "https://www.chartfanatics.com/strategies/first-red-day-strategy", tier: T2}
status: verified-t2
---

# Kyle Williams — Small Cap Short Selling Playbook: First Red Day and Parabolic Short (US small-cap stocks, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/first-red-day-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Kyle Williams day trades the short side of euphoric small-cap
runners, shorting "mini bubbles" as they exhaust. The playbook gives no
further biography.

## Built for

- **Instruments:** stocks, mainly small caps. The exit rules also give a
  target for "larger assets".
- **Style:** day trading, short only.
- **Timeframes:** the **daily** chart qualifies the multi-day run.
  Intraday charts and the tape are used to time entries. An optional trail
  uses the **15-minute high**.
- **Time window:** not specified in the playbook, but **avoid opening new
  positions late in the day** because of gap risk.
- **Setups:** First Red Day (primary), the intraday Parabolic Short
  (secondary), and the Overextended Gap Down (a variation).

## Core idea

Small caps produce short-lived bubbles almost every week. The page's
compact version: the best sign a stock is ready to fall is that it can no
longer go up. After several green days, more longs have bought at elevated
prices, and retail traders judge profit or loss against the **previous
day's close**. When price breaks below it, many
holders go underwater at once and fear replaces euphoria. SSR also kicks in
after a 10% drop. The playbook trades that shift. Unlike long breakouts
(low win rate, high R:R), it aims for a **higher win rate**, with clear
structural invalidation and position size scaled to setup quality.

## Rules

**Setup 1: First Red Day (FRD)**

1. **Qualify the bubble (all required):**
   - **2 to 3+ consecutive green days**;
   - **80 to 100%+** gain from the start of the run;
   - **expanding daily volume**;
   - **expanding daily range** (acceleration).
   If any is missing, it is not the setup.
2. **Grade it.**
   - *A-grade traits:* candles growing as price rises, volume building into
     the top, no red days during the run, parabolic curvature, a blow-off
     top day with an oversized range, a big upper wick on the top day, and
     clean structure.
   - *Downgrades:* shrinking candles into the highs, falling volume, choppy
     structure with several red days, frequent halts, and slow
     accumulation instead of an explosive run.
3. **Key level.** The **previous day's close** is the most important level,
   not the open. A stock can gap up, sell off hard and still be green. The
   real psychological trigger is the break below the prior close.
4. **Entry (choose by risk appetite):**
   - **Pre-red (aggressive):** short before the prior close breaks, on a
     failure to make new highs. **Stop: the high of the run.** It has the
     best R:R and the most stop-outs.
   - **Standard:** short the crack below the prior close and add on failed
     bounces. **Stop: today's high of day.** The page calls this the most
     balanced option.
   - **Lower-high confirmation (conservative):** wait for the breakdown,
     then the first bounce, then short the failed lower high. It has a
     higher win rate and a worse R:R.
5. **Exits.** Cover into weakness and do not wait for the exact bottom.
   Scale out instead of all-or-nothing. **Target at least −10% on the day
   for small caps** (2 to 3% for larger assets). Use **VWAP** as a general
   magnet. Trailing on the **15-minute high** is optional.

**Setup 2: Parabolic Short (intraday)**

6. **A real parabola:** a gradual build, several green candles, shrinking
   pullbacks, volume rising into the top, and a curved shape. **Not a
   parabola:** a one-candle news spike, no build, a random volume pop, or a
   sideways range that suddenly goes vertical.
7. **Entry:**
   - **Aggressive:** read the tape for a slowdown in velocity and the first
     big volume contraction. **Stop: high of day.**
   - **Safer:** wait for a pullback and short the first lower high.
     **Stop: the all-time high of the move.**
8. **Target:** VWAP is the main magnet. Cover before the perfect bottom.
9. **Attempts:** a hard cap of **3 to 5 attempts**. Over-trying burns both
   mental and financial capital.

**Setup 3: Overextended Gap Down**

10. After several gap-ups in a row, the **first gap down** matters. **Do not
    short if the stock is already down 10% or more.** Wait for a bounce to
    improve R:R. **Stop: the prior close.**

## Risk management

- **Primary invalidation:** the **all-time high of the run**. New highs
  kill the thesis. Tighter stops (high of day, or prior close for gap
  downs) can be used after confirmation, but they get hit more often.
- **Sizing:** scale size by setup grade. Add on failed bounces once the
  trade is working. Avoid overtrading C-grade setups, and do not use up
  your energy before an A+ setup appears.
- **Attempt cap:** at most 3 to 5 attempts on parabolic shorts.
- **Timing:** no new positions late in the day, because of gap risk.
- **Review:** track performance by setup grade.
- **Risk per trade ($ or %), share size limits, and daily or weekly loss
  limits:** not specified in the playbook.

## What the playbook leaves unspecified

- Liquidity and size filters: float, market cap, price floor, minimum
  volume.
- How "expanding volume" and "expanding range" are measured (how many days
  and what increase).
- How to grade setups (A+, A, B, C) in detail, and how much size each
  grade gets.
- The intraday chart timeframe for entries and for "failed bounce" or
  "lower high" triggers.
- Borrow, locate and halt handling, and how SSR changes execution beyond
  being a trigger.
- How far below the prior close the "crack" must go before the standard
  entry triggers.
- What "late in the day" means as a clock time.
- A rule for when the −10% small-cap target and the VWAP magnet point to
  different levels.
- Whether the 3 to 5 attempt cap also applies to FRD trades.

## Evidence & claims

- **BYND (A+ FRD example):** ran from about **$0.50 to $7.70**, a gain of
  **over 1,400%**. A short on the break below the prior close, with risk
  against the run high, produced a "significant profit". No figure is
  given. Self-reported (T4).
- **"Higher win rate"** than long breakouts, and the win-rate versus R:R
  ranking of the three entry methods, are qualitative, with no numbers.
  Self-reported (T4).
- **"Small caps produce these bubbles weekly":** a frequency claim with no
  data. Self-reported (T4).
- No win rate or average R:R is stated, so no expectancy check is
  possible.

## Concepts & lineage

- Shorting the unwind of euphoric multi-day and intraday bubbles →
  [[concept_mean_reversion]], [[concept_market_sentiment]]
- The previous day's close as the psychological pivot, and failed bounces
  under resistance → [[concept_support_resistance]],
  [[concept_price_action]]
- Expanding range and volume to qualify a parabola, then velocity
  slowdown and volume contraction as the turn →
  [[concept_volatility]]
- SSR after −10%, halts as a downgrade, and tape-reading the top →
  [[concept_market_microstructure]]
- VWAP as the cover magnet → [[concept_vwap]]
- Three entry styles trading win rate against R:R →
  [[concept_risk_reward_r_multiples]]
- Size by grade, add on failed bounces, scale out, 15-minute high trail →
  [[concept_position_sizing]], [[concept_trade_management]]
- Tracking results by setup grade → [[concept_trading_journal_review]]
- The 3 to 5 attempt cap to protect mental capital →
  [[concept_trading_psychology]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/lance-breitstein-mean-reversion.md ===== -->

---
id: strategy_lance_breitstein_mean_reversion
type: strategy
title: "Lance Breitstein — Capitulation Mean Reversion (stocks, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Lance Mean Reversion Trading Strategy, capitulation reversal, right-side reversal, blow-off top fade]
taught_by: [person_lance_breitstein]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_expectancy, concept_volatility, concept_bollinger_bands, concept_moving_averages, concept_market_sentiment, concept_multi_timeframe_analysis, concept_market_structure, concept_price_action, concept_trade_management, concept_position_sizing]
derived_from: [concept_mean_reversion, concept_random_walk_efficient_markets]
related: [strategy_marios_stamatoudis_parabolic_short, strategy_kris_verma_shorting, strategy_jj_simon_fair_pricing]
sources:
  - {title: "Chart Fanatics — Lance Mean Reversion Trading Strategy", url: "https://www.chartfanatics.com/strategies/mean-reversion-strategy", tier: T2}
status: verified-t2
---

# Lance Breitstein — Capitulation Mean Reversion (stocks, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/mean-reversion-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Lance Breitstein is presented as the author of a
capitulation-reversal day-trading method for stocks. The playbook gives no
further biography. It teaches the method through two stock examples, OCLR
(October 2016) and KODK.

## Built for

- **Instruments:** stocks.
- **Style:** day trading.
- **Timeframes:** the daily chart judges whether a move is abnormal for that
  stock. The intraday chart (bar length not given) locates the capitulation,
  the reversal signal and the entry.
- **Session / time window:** not specified.

## Core idea

Most of the time markets sit near equilibrium. Panic, forced liquidation or
a sudden swing in sentiment can occasionally throw price far from it, fast.
The trader scores how extreme the move is and waits for proof that it has
turned, trading what the page calls "the right side of the reversal". The
goal is the first retracement toward equilibrium, with the **20-period
moving average** (the Bollinger Band midline) as the reference. Every trade
is judged on expected value, **EV = (win rate × reward) − (loss probability
× risk)**. A good setup raises the odds of a reversal, offers a large
reward because price is far from equilibrium, and has a clearly defined
risk.

## Rules

1. **Scan for extremes.** Look for stocks trading outside the Bollinger
   Bands, moving several days in one direction, expanding in range sharply,
   or trading on unusually high volume. Trade whichever shows the strongest
   setup.
2. **Score the move.** The more of these conditions line up, the stronger
   the setup:
   - a **large** move;
   - a **fast** move, over minutes or hours rather than months;
   - **no fundamental change**. A move without major new information is
     more likely to be temporary, while real news may have shifted
     equilibrium;
   - many **consecutive bars or days** in one direction, on any timeframe;
   - **forced flows**: margin calls, liquidations, short covering,
     redemptions;
   - a **sentiment extreme**, euphoric or despairing;
   - a **normally stable** asset that suddenly turns extremely volatile.
     This is the ideal case;
   - a **quantifiable value anchor**, such as bonds at maturity or cash
     flows, which can make the reversion more reliable.
3. **Confirm capitulation.** Price accelerates, candles grow large compared
   with normal ranges, **volume spikes**, and price stretches far from its
   moving averages. Check the daily chart to confirm the move is abnormal
   for this stock.
4. **Entry trigger: wait for the turn, never the falling knife.**
   - *Long after a decline* that kept respecting the prior bar's highs:
     buy the **break of the prior bar's high**.
   - *Short after a rally* that kept respecting the prior bar's lows: sell
     the **break of the prior bar's low**.
   - *Structure shift:* lower highs and lower lows turn into higher highs
     and higher lows, or the reverse.
   - *Extreme single-candle panic reversal:* you may enter while the candle
     is reversing, but at **smaller size** because the risk is less clearly
     defined.
5. **Stop.** Where the idea is invalid: below the low of the capitulation,
   where the reversal structure fails, or where higher lows break. For a
   short, above the high of the parabolic move.
6. **Target.** The first bounce toward the **20-period MA**. Expect only a
   partial retracement, not a return to the prior highs.
7. **Manage.** Trail the stop under each prior bar's low (longs) or over
   each prior bar's high (shorts).
8. **Size by quality.** Strong setups (extreme displacement, fast
   acceleration, a big volume spike, large distance from equilibrium, clean
   structure, several legs) can be traded larger. Weaker ones go smaller or
   are skipped.

**Worked examples.**
- *OCLR, Oct 27 2016 (long):* a slow decline after the open sped up into a
  capitulation of about 20 to 25%. The stock normally moved about 30 cents
  a day but was now moving about 30 cents a bar, and volume spiked. Entry
  on the prior-bar-high break at about $7.25, stop under the low at about
  $7.00, trailed under bar lows, exit about $7.57 near the 20-period MA.
- *KODK (short):* a news-driven parabolic rally on a government loan
  programme turned into a blow-off. Short on the break of the prior bar's
  low, stop above the parabolic high, trail above bar highs, cover into the
  first pullback. No prices are given.

## Risk management

- **Stop:** always at the structural invalidation point (capitulation low
  or high, or the failed reversal structure).
- **Sizing:** scaled to setup quality. Single-candle panic entries use
  smaller size.
- **Shorts:** need **extra risk management**, because a short's loss is
  theoretically unlimited while a long's is capped at zero.
- **Risk per trade (% or $):** not specified in the playbook.
- **Daily or weekly limits:** not specified in the playbook.

## What the playbook leaves unspecified

- Thresholds for "large", "fast", "high volume" and "far from the MA". No
  ATR multiple, % move, relative volume or Bollinger setting is given
  beyond the 20-period midline.
- How many conditions must line up before a trade is taken, or how they are
  weighted.
- The intraday bar length (the examples suggest a fixed intraday chart but
  never name it).
- When to exit if price stalls before the 20-period MA, and whether to take
  partials.
- How to tell news that changes equilibrium from news that does not. KODK
  was news-driven yet still faded.
- Any rules on stock universe, liquidity, short borrow, or time of day.

## Evidence & claims

- The page gives **no win rate, average R, P&L or payout claim**. It gives
  only the EV formula as a way of thinking.
- The OCLR example implies (my arithmetic from the stated prices) a reward
  of about $0.32 against risk of about $0.25, roughly **1.3R**. It is a
  single self-reported trade (T4), not a statistic.
- With no stated win rate, no expectancy check is possible. The page claims
  a "higher probability" of reversal only qualitatively.

## Concepts & lineage

- Price returning to equilibrium after an overshoot →
  [[concept_mean_reversion]]
- Markets "generally efficient", with temporary dislocations from panic or
  forced flows → [[concept_random_walk_efficient_markets]]
- Choosing trades by expected value (probability, reward, risk) →
  [[concept_expectancy]]
- Volatility expanding against the stock's normal range (30 cents a day
  becoming 30 cents a bar) → [[concept_volatility]]
- Scanning outside the Bands and targeting the 20-period midline →
  [[concept_bollinger_bands]], [[concept_moving_averages]]
- Sentiment extremes and emotional capitulation → [[concept_market_sentiment]]
- Daily context with an intraday trigger → [[concept_multi_timeframe_analysis]]
- Prior-bar breaks and the LH/LL to HH/HL shift as triggers →
  [[concept_market_structure]], [[concept_price_action]]
- Trailing stops on prior bars → [[concept_trade_management]]
- Sizing by setup quality → [[concept_position_sizing]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/marci-silfrain-measured-move.md ===== -->

---
id: strategy_marci_silfrain_measured_move
type: strategy
title: "Marci Silfrain — Measured Move Trend Strategy: Little RZY (stocks, futures and crypto, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Little RZY, measured move trend strategy, Marci Silfrain strategy, Little RZY measured move]
taught_by: [person_marci_silfrain]
featured_in: [channel_chart_fanatics, podcast_words_of_rizdom]
uses: [concept_trendlines, concept_market_structure, concept_trend_following, concept_chart_patterns, concept_fibonacci, concept_bollinger_bands, concept_mean_reversion, concept_support_resistance, concept_multi_timeframe_analysis, concept_trade_management, concept_backtesting, concept_risk_of_ruin_drawdown, concept_trading_psychology]
derived_from: [concept_fibonacci, concept_chart_patterns]
related: [strategy_tori_trendline_4h, strategy_trader_mayne_structure_ote, strategy_ali_crooks_trendline_pocket]
sources:
  - {title: "Chart Fanatics — Measured Move Trend Strategy (Little RZY) – Marci Silfrain Playbook", url: "https://www.chartfanatics.com/strategies/measured-move-trend-strategy", tier: T2}
  - {title: "TradeZella — Measured Move Trend Strategy (Little RZY)", url: "https://www.tradezella.com/strategies/measured-move-trend-strategy", tier: T3}
  - {title: "The World's #2 Trader — Futures Trading World Champion Marci Silfrain (Words of Rizdom, recap)", url: "https://recapio.com/digest/the-world-s-2-trader-futures-trading-world-champion-marci-silfrain-by-words-of-rizdom", tier: T3}
  - {title: "PickMyTrade — Marci Silfrain Strategy (Gold)", url: "https://blog.pickmytrade.trade/marci-silfrain-strategy-gold/", tier: T3}
status: verified-t2
---

# Marci Silfrain — Measured Move Trend Strategy: Little RZY (stocks, futures and crypto, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/measured-move-trend-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Third-party coverage describes Marci Silfrain as a futures
trader and bills her as the world's #2 futures trader, from a trading
championship result (T3). The playbook gives no biography. The playbook presents her trend method as built on one repeating,
measurable pullback structure rather than a stack of indicators.

## Built for

- **Instruments:** stocks, futures and crypto. A third-party write-up
  applies it to gold (T3).
- **Style:** swing trading, with trend continuation as the main use and
  spotting major bottoms as a secondary one.
- **Timeframes:** all timeframes. **Higher timeframes** give more reliable
  structures and are better for major tops, bottoms and longer-term
  entries. **Lower timeframes** give more setups but need faster decisions
  and more experience. A common approach is to read direction on a higher
  timeframe and execute on a lower one.
- **Session or time window:** not specified.
- **Tools:** trendlines and Bollinger Bands. The band settings are not
  given.

## Core idea

Trends move in repeating, measurable steps: an impulse, a pullback, then
continuation. In each pullback, called a **Little RZY**, you draw a
trendline across the pullback and measure from its extreme candle to the
line. That same distance, projected from the extreme, gives the next
target. Marci links this to the logic of Fibonacci retracements and
extensions, without drawing every level. Bollinger Bands show whether
price is in a "normal" range or stretched. The first one or two
structures in a fresh trend are the strongest. By the fourth or fifth,
the trend is usually tiring.

## Rules

1. **Confirm a trend.** Lower highs and lower lows, with Little RZYs
   forming one after another, for a downtrend. Higher highs and higher
   lows for an uptrend, where the structure is inverted. If price goes
   sideways and the structures stop forming, the trend may be ending.
2. **Wait for an impulse, then a pullback.** Never enter during the
   initial drop or rally.
3. **Draw the trendline** across the **pullback highs** in a downtrend, or
   the **pullback lows** in an uptrend. Each Little RZY gets **its own**
   trendline and measured move. It is not one long trendline across the
   whole trend.
4. **Measure.** Find the candle in the structure with the **lowest low**
   (for shorts) or **highest high** (for longs). Measure vertically from it
   to the trendline directly above or below.
5. **Check context with Bollinger Bands.** The middle band is the "normal"
   price and the outer bands are extremes. Early structures that form near
   the **upper band in a downtrend**, or the **lower band in an uptrend**,
   carry higher odds. The further price sits toward an extreme in the trend
   direction, the weaker the trend.
6. **Prefer early structures.** The first or second Little RZY in a fresh
   trend is strongest. By the fourth or fifth, expect exhaustion. Shrinking
   structures, extreme band readings or sideways drift warn the trend may
   be ending.
7. **Entry.** For a short, wait for the pullback to form and begin
   rejecting the trendline, then enter as price turns back down with the
   trend. For a long, wait for the pullback to finish and enter as price
   starts pushing up again.
8. **Stop.** For a short, above the trendline or the recent swing high.
   Ideally, treat the trade as invalid only on a **confirmed close** above
   the trendline. For a long, below the trendline or the recent swing low.
   Do not set stops too tight, because price may retest the line before
   continuing.
9. **Target.** The measured move: the same distance, projected from the
   extreme candle in the trend direction. Partial exits are allowed, but
   the core idea is to let the full move complete.
10. **Invalidation.** The setup is void if price closes beyond the
    trendline, if the structure is too extended or irregular, or if price
    collapses with no proper pullback. Then wait for a new structure.
11. **Bottom-finding variant (crashes).** As price falls, several
    structures each project lower. A bottom zone is likely when one
    projection lines up with key support or broader context, price is
    stretched outside the Bollinger range, and the market starts to stall
    or consolidate. A move back above the **Bollinger midline** can confirm
    it.
12. **If unclear, zoom in.** Price that looks sideways on one timeframe
    may show a clear Little RZY on a lower one.

## Risk management

- **Stop:** structural, beyond the trendline or the recent swing. A close
  through the line is the cleanest invalidation.
- **Target:** the measured move. Partials are optional.
- **Mindset (from the earlier note, a T3 podcast recap, not on the
  playbook):** plan to lose on every trade, and plan for the next 20 trades
  to be losers in a row.
- **Risk per trade, position sizing, and daily or weekly limits:** not
  specified in the playbook.

## What the playbook leaves unspecified

- Bollinger Band settings (length and standard deviations) and how far
  "near the band" or "beyond the band" is.
- How big or how fast the first impulse must be, and how many candles a
  valid pullback needs.
- An exact entry trigger: what candle or event shows the pullback
  "rejecting" the trendline.
- Stop buffer, and how to choose between "above the trendline" and "above
  the swing high".
- Minimum reward-to-risk, given that the target is fixed by the
  measurement.
- How to size and when to take partials.
- Which timeframe pairs to use for higher-timeframe direction and
  lower-timeframe execution.
- Specific instruments. The page lists stocks, futures and crypto in
  general, and the gold application comes only from a T3 source.
- The page admits these patterns are easier to see in hindsight, and that
  recognising them live takes repeated chart time.

## Evidence & claims

- The playbook gives **no win rate, R:R or P&L**. Its trade example ends
  with the measured move being reached, which is qualitative and
  self-reported (T4).
- The playbook says the strategy "assumes that price tends to complete
  these moves". That is an assumption, not a measured statistic.
- **From the earlier note:** billed as the world's #2 futures trader in a
  trading championship, with one video citing a **320% return** (T3, a
  competition result, not verified here). Her Chart Fanatics episode was
  reported at about **772K views** by an aggregator (T3). That is a
  popularity figure, not a performance one.
- No independent test of the Little RZY is cited. No expectancy check is
  possible.

## Concepts & lineage

- A trendline across each pullback defines the structure →
  [[concept_trendlines]]
- Higher highs and higher lows or lower highs and lower lows to confirm the
  trend; continuation in the trend direction → [[concept_market_structure]],
  [[concept_trend_following]]
- Measured-move projection from the pullback extreme to the line →
  [[concept_chart_patterns]]
- Marci's framing of the measured move as seeing Fibonacci retracement and
  extension relationships without drawing them → [[concept_fibonacci]]
- Bollinger Bands for "normal" versus stretched price, and the midline
  reclaim to confirm a bottom → [[concept_bollinger_bands]],
  [[concept_mean_reversion]]
- A bottom when a projection meets key support →
  [[concept_support_resistance]]
- Higher-timeframe direction with lower-timeframe execution, and zooming in
  to see the structure → [[concept_multi_timeframe_analysis]]
- Optional partials while letting the full move complete →
  [[concept_trade_management]]
- From the earlier note (T3): hours of backtesting, sim and paper trading,
  and expecting long losing streaks → [[concept_backtesting]],
  [[concept_risk_of_ruin_drawdown]], [[concept_trading_psychology]]
- Editorial lineage kept from the earlier note: Wyckoff "cause and effect"
  as a cousin of the measured move. It is not stated on the page →
  [[concept_wyckoff_method]]

## Changes vs. earlier note

- **Corrected: how the target is measured.** The earlier note said the
  next leg is projected to equal the prior impulse (T3). The playbook
  measures from the **lowest low (or highest high) candle inside the
  pullback structure to the trendline directly above (or below) it**, and
  projects that distance from the extreme. It is not the length of the
  prior impulse.
- **Corrected: entry.** The earlier note said to enter on "rejection at,
  or break of, the line" (T3). The playbook enters as the pullback
  **rejects** the trendline and price turns back with the trend. A close
  **through** the line against the trend invalidates the setup.
- **Refined: the early-structure filter.** The earlier note had "favour the
  first two trendline touches" (T3). The playbook says the first one or
  two **Little RZY structures** in a fresh trend are strongest, with
  exhaustion by the fourth or fifth. It also says each structure gets its
  own trendline.
- **Added:** the stop rule (beyond the trendline or swing, ideally on a
  confirmed close, not too tight), the invalidation list, the Bollinger
  Band context (early structures near the opposite band, extremes meaning
  exhaustion), the crash bottom-finding variant with the midline reclaim,
  timeframe guidance, and instruments (stocks, futures, crypto).
- **Lineage changed.** The playbook ties the pattern to Fibonacci
  retracements and extensions, so `derived_from` is now Fibonacci and
  chart patterns. The earlier Wyckoff "cause and effect" link is kept only
  as an editorial note.
- **Answered open questions:** the stop rule is now covered. Position
  sizing is still not given. Instruments are now stated at T2. The gold
  variant remains T3 only.
- **Kept:** the T3 trader billing (world's #2, 320% return), the
  view-count figure and the T3 mindset notes (backtesting habit, planning
  for 20 straight losses). The playbook does not mention them, but does
  not contradict them either.
- **Sources.** The earlier note already cited this Chart Fanatics URL. It
  stays first, retitled to the page title, with no duplicate entry. The
  TradeZella, Words of Rizdom recap and PickMyTrade sources (T3) are kept.
  The status moves from `synthesized` to `verified-t2`.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/marco-trades-liquidity-grab.md ===== -->

---
id: strategy_marco_trades_liquidity_grab
type: strategy
title: "Marco Trades — Liquidity Grab Trading Strategy (futures, forex and crypto, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Marco Trades liquidity playbook, liquidity grab strategy, MarcoTrades, buy below lows sell above highs]
taught_by: [person_marco_trades]
featured_in: [channel_chart_fanatics, channel_chart_fanatics_live]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_market_structure, concept_price_action, concept_trade_execution, concept_trading_sessions_killzones, concept_multi_timeframe_analysis, concept_trade_management]
derived_from: [concept_liquidity_sweep_reversal, concept_liquidity]
related: [strategy_candace_lau_nq_sweep_reversal, strategy_tanja_amd_futures, strategy_yush_order_flow]
sources:
  - {title: "Chart Fanatics — Liquidity Grab Trading Strategy", url: "https://www.chartfanatics.com/strategies/liquidity-strategy", tier: T2}
  - {title: "Chart Fanatics — Liquidity Grab Trading Strategy", url: "https://www.chartfanatics.com/playbook/liquidity-playbook", tier: T2}
  - {title: "Chart Fanatics Live Trading: New York Session With MarcoTrades", url: "https://www.youtube.com/watch?v=-8KwnNEPuzU", tier: T2}
status: verified-t2
---

# Marco Trades — Liquidity Grab Trading Strategy (futures, forex and crypto, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/liquidity-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Marco Trades' day-trading method for
reversals after the market runs stops at key highs and lows, and says he
teaches a free liquidity and counter-trend masterclass on Chart Academy. A
Chart Fanatics Live video kept from the earlier note shows him trading a
New York session; that is not part of the playbook text.

## Built for

- **Instruments:** futures, forex and crypto. The page calls the model
  asset-agnostic.
- **Style:** day trading, counter-trap reversals.
- **Timeframes:** fractal, the same model from 1-minute to daily. The
  worked example uses the **30-minute** chart for context and targets and
  the **5-minute** chart for the setup and entry.
- **Time window:** pick one fixed session window (the example is the **New
  York open**). If the setup does not form inside it, there is no trade.
- **Tools:** raw highs, lows and time. No indicators. The page frames BOS,
  order blocks and FVGs as "retail" concepts that traders find hard to
  unlearn.

## Core idea

Price seeks liquidity, and retail traders get trapped at obvious highs and
lows. A high or low that was **respected** (price reacted and moved away
from it) leaves resting stops and breakout orders beyond it. Rather than
trading ahead of that level, wait for price to run it, confirm the trap,
then trade the reversal. **Buy below lows, sell above highs**, and never
the other way round. Liquidity sets the bias, the entry, the invalidation
and the target.

## Rules

1. **Bias from liquidity.** A respected high, with price moving away from
   it, means liquidity sits above and price may return to it. The same
   applies below a respected low. Mark respected highs and lows. In the
   example, equal lows on the 30-minute chart marked
   the sell-side target.
2. **No liquidity, no trade.** Plan a trade only once liquidity is built
   and price has taken it or formed an inducement. If a big move has already happened and
   left no clear highs or lows, stand aside.
3. **Session filter.** Watch only your chosen window, for example the New
   York open. Ignore price action outside it. No setup inside the window
   means no trade.
4. **Buy setup.** Price returns to a respected low and **trades below it**.
   Look for confirmation: internal structure, a false reaction, the trap.
   **Buy below the low, never above it.**
5. **Sell setup (mirror).** Price returns to a respected high and **trades
   above it**. Confirm the trap. **Sell above the high, never below it.**
   In the example, price ran the pre-NY swing high on the 5-minute chart,
   failed to hold and fell back below it. The short came right after.
6. **Execution.** Enter **only after** the liquidity is taken, never
   before. Use a **market order** once the trap is confirmed. Keep entries
   simple and do not over-refine.
7. **Stop.** Always beyond the high or low that was just taken: below the
   swept low for buys, above the swept high for sells.
8. **Targets.** The opposing liquidity: respected highs for buys, and
   respected or equal lows for sells (internal or external liquidity).
9. **Management.**
   - Trail the stop **only** after price moves your way and forms a new
     higher low (longs) or lower high (shorts).
   - **No break-even stop unless partials have been taken.**
   - Take partials **only at real liquidity targets**, never at arbitrary
     R multiples.
   - Let trades reach meaningful areas. Do not cut early unless the system
     says so.

## Risk management

- **Stop:** beyond the swept high or low. Moving back past it invalidates
  the idea.
- **Stop moves:** only on new structure in your favour. Break-even only
  after a partial.
- **Partials:** only at liquidity targets.
- **Session discipline:** no trade outside the window.
- **Risk per trade ($ or %), position size, maximum trades per day, and
  daily or weekly loss limits:** not specified in the playbook.

## What the playbook leaves unspecified

- An exact confirmation trigger. The page lists "internal structure, false
  reaction, trap" and, in the example, a move back below the swept level,
  but does not define a candle close, a timeframe or a structure-shift
  rule.
- How far beyond the level price may run before the setup counts as a real
  breakout rather than a grab.
- How to judge which highs and lows "have liquidity". The page says context
  matters and structure alone is not enough, but gives no test.
- The stop buffer beyond the swept extreme.
- Minimum reward-to-risk to the liquidity target.
- What "inducement" means in practice. It is mentioned but not defined.
- Which session window to use for each market, and its exact hours.
- Pairing of timeframes for markets other than the example's 30-minute and
  5-minute.

## Evidence & claims

- The page gives **no win rate, R:R, P&L or payout**. No expectancy check is
  possible.
- The pros (clear direction, eliminates noise, fits any asset, strict
  rules) are qualitative claims. Self-reported (T4).
- The worked example (a pre-NY high run on the 5-minute chart, a short
  targeting 30-minute equal lows) gives no prices or result.

## Concepts & lineage

- Respected highs and lows, and equal lows, as resting liquidity pools,
  with liquidity setting the bias and targets → [[concept_liquidity]]
- Run the stops, confirm the trap, trade the reversal →
  [[concept_liquidity_sweep_reversal]]
- Internal structure for confirmation; trailing only on new higher lows or
  lower highs → [[concept_market_structure]]
- Raw price, no indicators → [[concept_price_action]]
- Market-order entry once the trap is confirmed, with no
  over-refinement → [[concept_trade_execution]]
- A fixed session window, such as the New York open →
  [[concept_trading_sessions_killzones]]
- 30-minute context and 5-minute execution →
  [[concept_multi_timeframe_analysis]]
- Partials only at liquidity, break-even only after partials →
  [[concept_trade_management]]

## Changes vs. earlier note

- **Confirmed:** reversals after a stop-hunt of a key high or low; buy
  below the low with a stop below it, and the mirror for sells. The earlier
  note already had these at T2.
- **Answered: confirmation trigger.** The earlier note asked whether it
  was an MSS, a close back inside, or order flow. The playbook names
  internal structure, a false reaction and the trap. Execution is a
  **market order** once price is back on the other side of the swept
  level. No order-flow tool is mentioned, and BOS, OB and FVG are framed as
  retail concepts to unlearn.
- **Answered: target logic.** The target is opposing liquidity: respected
  highs or lows. The example uses equal lows on the 30-minute chart.
- **Corrected: instrument.** The earlier note guessed "likely index
  futures". The playbook lists **futures, forex and crypto** and calls the
  model fractal across timeframes.
- **Added:** the "only respected levels hold liquidity" filter, the
  no-trade rule after big moves that left no levels, the single session
  window, trailing only on new structure, no break-even before partials,
  partials only at liquidity, and the 30-minute and 5-minute example.
- **Sources.** The earlier note cited the playbook at
  `/playbook/liquidity-playbook`. The scraped page at
  `/strategies/liquidity-strategy` is now listed first. The old entry and
  the Chart Fanatics Live video (T2) are kept unchanged. `featured_in`
  keeps `channel_chart_fanatics_live`. The status moves from `synthesized`
  to `verified-t2`.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/marios-stamatoudis-parabolic-short.md ===== -->

---
id: strategy_marios_stamatoudis_parabolic_short
type: strategy
title: "Marios Stamatoudis — Parabolic Short: Exhaustion-Day VWAP Failure (stocks, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Parabolic Short Strategy, parabolic exhaustion short, exhaustion day VWAP rejection, Marios parabolic short]
taught_by: [person_marios_stamatoudis]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_vwap, concept_market_structure, concept_moving_averages, concept_market_sentiment, concept_support_resistance, concept_volatility, concept_trade_management]
derived_from: [concept_mean_reversion]
related: [strategy_alex_temiz_first_red_day, strategy_kyle_williams_first_red_day, strategy_kris_verma_shorting, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — Parabolic Short Strategy", url: "https://www.chartfanatics.com/strategies/parabolic-short-strategy", tier: T2}
status: verified-t2
---

# Marios Stamatoudis — Parabolic Short: Exhaustion-Day VWAP Failure (stocks, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/parabolic-short-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Marios Stamatoudis with this stock day
trading setup for shorting the collapse of an exhausted parabolic run. The
page gives no biography.

## Built for

- **Instruments:** stocks, from small caps to large caps, including
  theme-driven names and recent IPOs.
- **Style:** day trading. Positions are closed before the end of the day.
  The same read can also be used to exit longs into strength.
- **Timeframes:** daily chart to qualify the run (size of the move, the
  20-day moving average base, acceleration). Intraday chart with **VWAP**
  for execution; no intraday timeframe is named.
- **Window:** the exhaustion day is usually the day of the final push or
  the next day. If nothing triggers within **two days**, drop the idea.
- **Frequency:** not a daily setup. It needs patience.

## Core idea

A fast run attracts early buyers, then momentum traders, then late chasers.
Once nearly everyone who wants in is in, demand is spent and the trend is
held up only by existing holders. A small trigger can then cause a sharp,
same-day collapse. Do not call the top. Qualify the run by its size and
acceleration, then wait for an **exhaustion day** when price breaks its
intraday structure, loses VWAP and fails to win it back. Short that
failure with the stop at the high of the day.

## Rules

1. **Filter 1: size of the move.** Measure it from the **latest base**
   rather than the lowest point of the chart. The base is the last touch of the **20-day moving
   average** before the run.
   - Small cap: about **200% or more**.
   - Mid cap: about **100%**.
   - Large cap: about **50%**.
   - Moves far beyond these are an extreme zone, where a sharp reversal is
     more likely and the drop can be more violent.
2. **Filter 2: structure of the move.** The run must accelerate: larger
   candles, a steeper slope, sometimes gaps between sessions. Slow,
   controlled trends with small candles, or trends with regular pullbacks
   that release pressure, do not qualify. The strongest case is a steady
   climb that suddenly turns into a fast, aggressive phase, which traps
   both early holders and late chasers.
3. **Optional strengtheners:** volume at the highest level in recent
   history (the last wave of buyers), and a first touch of a round number
   such as 100, 300 or 500 after the run.
4. **Estimate the expected move before entering.**
   - Established, long-trending stocks: about **10% to 20%**, sometimes
     more after an extreme run.
   - Hype or theme stocks: about **20% to 40% or more** in a day.
   - IPOs: usually in between, and less predictable.
   - Skip it when a large share of the expected drop is already done, such
     as after a big gap down.
5. **Require the exhaustion day.** Price stops making higher highs, prints
   lower highs and then lower lows, and **moves below VWAP without
   reclaiming it**. A weak bounce toward VWAP that gets rejected confirms
   it. If price holds above VWAP and keeps climbing, the setup is not
   active.
6. **Entry, from earliest to best:**
   1. Upward intraday structure breaks into lower highs and lower lows.
      This is the earliest entry and the riskiest.
   2. A structure break and a VWAP loss together. This is stronger.
   3. A **failed attempt to reclaim VWAP**. This is the best entry.
7. **Invalidation.** A strong VWAP reclaim followed by continuation higher
   cancels the setup.
8. **Stop** at the **day's high**, or at the latest lower high.
9. **Take partial profits** once the trade moves in your favour, then move
   the stop to **break-even**.
10. **Risk-free add.** With the stop at break-even, a second VWAP test that
    fails again is a place to add size. If it fails, the earlier profits cover the
    added piece.
11. **Close before the end of the day.** No overnight holds.
12. **Two attempts at most.** If the setup fails once, one more try is
    allowed. If it fails again, move on.

## Risk management

- **Stop:** the day's high, or the latest lower high.
- **Break-even:** after the first partial.
- **Adding:** only after the stop is at break-even (the "risk-free add").
- **Attempts:** a maximum of two per setup.
- **Overnight:** not allowed.
- **Risk per trade ($ or %), position size, and daily or weekly loss
  limits:** Not specified in the playbook.
- **Short-specific risks** (borrow availability, short-sale restriction,
  halts, squeezes): Not specified in the playbook.

## What the playbook leaves unspecified

- Market-cap cut-offs for small, mid and large caps.
- An objective measure of acceleration, such as slope, candle size or gap
  count.
- The intraday chart timeframe used for structure and VWAP.
- How much to take at the first partial and where, and the final profit
  target. The expected-move ranges are the only guide.
- What counts as a "strong" VWAP reclaim, for example a close above it or
  holding for a set time.
- How far back "highest volume in recent history" looks.
- How the two-day window is counted when the final push spans more than
  one session.
- Practical short-selling constraints.

## Evidence & claims

- **SMCI example (early 2024):** the page says the run ticked every box: a
  big prior advance, wide-range candles, heavy volume and a nearby key
  level. The short came at the VWAP rejection, with the stop at the day's
  high.
  The stock fell about **23% to 24% in one day**, which the page says
  matched expectations and ended the larger uptrend. Self-reported (T4).
- **Quantum computing stocks, late 2024:** used as an illustration of
  crowded runs collapsing on negative news. No trade result is given.
- **Typical drop sizes** (10–20% for established names, 20–40% or more for
  hype names, IPOs in between) are self-reported expectations (T4).
- The page calls the setup very high-probability but gives **no win rate,
  R:R or trade sample**, so no expectancy check is possible.

## Concepts & lineage

- Fading an overextended, crowded run back toward value →
  [[concept_mean_reversion]]
- VWAP loss, failed reclaim and rejection as the trigger →
  [[concept_vwap]]
- Lower highs and lower lows confirming the turn →
  [[concept_market_structure]]
- The 20-day moving average as the base for measuring the run →
  [[concept_moving_averages]]
- FOMO buying, crowded trades and exhausted demand →
  [[concept_market_sentiment]]
- Round-number psychological levels → [[concept_support_resistance]]
- Expected move by stock type and extreme extensions →
  [[concept_volatility]]
- Partials, break-even and the risk-free add →
  [[concept_trade_management]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/matteo-conti-institutional.md ===== -->

---
id: strategy_matteo_conti_institutional
type: strategy
title: "Matteo Conti — Institutional Strategy Development Framework (multi-asset, day and swing trading)"
partition: 01_chart-fanatics
layer: L8
aliases: [Institutional Strategy Development Framework, Matteo Conti framework, idea-to-live research process, institutional backtest and validation process]
taught_by: [person_matteo_conti]
featured_in: [channel_chart_fanatics]
uses: [concept_backtesting, concept_overfitting_validation, concept_edge, concept_expectancy, concept_performance_metrics, concept_risk_of_ruin_drawdown, concept_position_sizing, concept_volatility, concept_trading_plan, concept_breakout_trading, concept_vwap, concept_news_trading, concept_trading_sessions_killzones, concept_market_microstructure, concept_optimal_execution_market_impact, concept_random_walk_efficient_markets, concept_market_regimes, concept_correlation_portfolio_risk, concept_probabilistic_thinking]
derived_from: [concept_backtesting, concept_random_walk_efficient_markets]
related: [strategy_naoufel_taief_algorithmic, strategy_pradeep_bonde_episodic_pivot]
sources:
  - {title: "Chart Fanatics — Institutional Strategy Development Framework", url: "https://www.chartfanatics.com/strategies/institutional-strategy-development-framework", tier: T2}
status: verified-t2
---

# Matteo Conti — Institutional Strategy Development Framework (multi-asset, day and swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/institutional-strategy-development-framework. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Matteo Conti explaining how institutional
traders build, test and validate a strategy before risking money on it. The
page gives no further biography.

## Built for

- **Instruments:** multi-asset. The worked examples use US index products
  (QQQ, NQ, ES), crude oil, individual stocks, and small- and mid-cap
  equities for the earnings model, with European equities named as a
  research candidate.
- **Style:** day trading and swing trading. This is a research and
  validation process, not one setup. The four example models are teaching
  vehicles, and the page says not to copy them as-is.
- **Timeframes and windows (by example model):**
  - Opening range breakout: range from **9:30 to 10:00 AM ET**, time exit
    around **3:30 PM ET**.
  - VWAP trend: **1-minute** chart, session VWAP anchored at **9:30 AM ET**.
  - Post-earnings drift: entry at the next trading day's open, held about
    **60 trading days** (chart timeframe not specified in the playbook).
  - Overnight anomaly: long from **4:00 PM ET** to **9:30 AM ET** the next
    trading day.

## Core idea

Institutional traders look for a repeatable strategy that can be tested on
data, not for the next trade. An idea comes from research, gets a reason it
might work, and is turned into objective rules. It is then coded,
backtested, validated out of sample and with Monte Carlo, deployed, and
monitored. The question is never whether the next trade wins but whether the
same rules have a positive expected return over a large sample. Simple
rules with a clear market reason are preferred, because each extra condition
adds another way to overfit.

## Rules

The process (the page's 13 steps, grouped):

1. **Find an idea in research.** Sources include academic work (for example
   papers on SSRN) and industry research from funds and practitioners. Take
   the market behaviour the paper found, not its exact recipe: "Do not copy
   the research paper directly."
2. **Explain why the edge should exist.** Each example model is tied to a
   cause: early-session order imbalance, institutional VWAP execution, slow
   absorption of earnings news, and an overnight risk premium or thin
   overnight liquidity. Knowing the cause also helps you notice when it
   stops applying.
3. **Define three objective components.** An **entry** with no room for
   interpretation (for example, a 1-minute candle closing above VWAP, not
   "price looks strong"). An **exit**: stop, target, time exit, or a price
   or indicator condition. A **position size**: start with **one fixed
   contract** while developing.
4. **Encode one rule at a time.** Code the entry and check it fires where
   expected. Then add the exit and test again, then the sizing, until the
   code behaves exactly like the written rules. AI and LLMs may help
   translate rules into code, but the trader must understand and check
   every part.
5. **Backtest** the exact rules on historical data. Review net profit, win
   rate, average trade, average winner and loser, maximum drawdown and
   losing streaks.
6. **Develop in sample, then freeze.** Split history, for example **80% in
   sample and 20% out of sample**. Add, remove or tune rules only on the
   in-sample part. Freeze the rules before looking at the unseen data.
7. **Test out of sample.** If results hold up in development but collapse
   on unseen data, suspect overfitting.
8. **Run Monte Carlo.** *Shuffle*: keep every trade but randomise the
   order thousands of times to see how much drawdown and losing
   streaks depend on sequence. *Resampling*: draw trades with replacement
   to estimate expected return, potential drawdown, the longest losing
   streak and the chance of a given loss. Tight clusters of equity curves
   point to a sturdier edge, and a wide spread points to a fragile one.
9. **Finalise sizing** with volatility targeting: fix the money at risk and
   size from current volatility (fewer contracts when volatility is high,
   more when it is low), so that a few wild sessions do not dominate
   results.
10. **Deploy** in one of three modes: research only (backtest, then trade by
    hand), as confirmation for a discretionary setup, or fully automated.
11. **Monitor live results** against the Monte Carlo ranges. A breach is a
    warning to review the strategy, not automatic proof it is broken.
12. **Build a portfolio.** Develop further *uncorrelated* strategies (for
    example momentum alongside mean reversion). The page suggests about
    **3 to 4 strategies** at once for a retail trader.

The four example models, as starting hypotheses to test:

- **Opening range breakout (long).** Mark the high and low from 9:30 to
  10:00 AM ET. Go long on a **close** above the range high, not a touch.
  Stop at the range low. Test targets of **1R to 2R**. Exit around 3:30 PM
  ET if neither has been hit. The short version (close below the range low,
  stop on the other side of the range) must be tested separately. In
  Matteo's experience the long side has worked better, because buyers tend
  to step into downside breaks.
- **VWAP trend.** Use session VWAP from 9:30 AM ET on the 1-minute chart.
  Go long on a candle close above VWAP and short on a close below it. Exit
  when price crosses back through VWAP; there is no separate target. The
  research used QQQ, and the page suggests testing NQ, ES, crude oil and
  individual stocks. Variants such as previous-day VWAP need their own
  validation.
- **Post-earnings announcement drift (long).** Requires a positive price
  reaction to earnings **and** actual EPS above the analyst estimate. Enter
  at the next trading day's open and exit after about **60 trading days**.
  Stops (a percentage, the pre-earnings close or others) are research
  options, not part of the base model. Size at **1 to 2% of the portfolio
  per stock**, a fixed dollar amount, or scaled to surprise, reaction or
  volatility. Small and mid caps are the main candidates. The short side
  may be weaker because companies often warn ahead of bad numbers.
- **Overnight anomaly.** Go long at 4:00 PM ET and exit at 9:30 AM ET the
  next trading day. This mainly tests whether the effect exists. It is not
  a finished strategy, and the page gives no stop or target. It can seed
  new ideas, such as an overnight breakout or momentum model.

## Risk management

- **Per-trade risk:** for development, one fixed contract. For live
  trading, volatility-adjusted sizing to a fixed money-at-risk figure. The
  page's illustration uses a target risk of $10,000; that is an example,
  not a recommended level. For the earnings model, 1 to 2% of the portfolio
  per stock or a fixed dollar amount.
- **Stops:** opening range low for the ORB long; a VWAP recross for the
  VWAP model; a time exit for the earnings drift model (stops are left to
  research); none for the overnight baseline.
- **Daily or weekly loss limits:** not specified in the playbook.
- **Strategy-level risk:** Monte Carlo drawdown and losing-streak ranges
  act as reference limits during live trading. A live drawdown beyond the
  simulated range triggers a review.
- **Portfolio risk:** run several uncorrelated strategies rather than one.

## What the playbook leaves unspecified

- How many trades or how many years of data are needed before a backtest
  counts as meaningful, and which markets and date ranges the examples
  used.
- Pass and fail thresholds for out-of-sample and Monte Carlo results: how
  much out-of-sample decay is acceptable, and what counts as a "tight"
  versus "wide" spread of equity curves.
- Transaction costs, slippage, borrow and commissions in the backtests.
- How volatility is measured for volatility targeting (ATR, range width,
  standard deviation) and over what lookback.
- How large a positive price reaction must be for the earnings model, and
  which EPS consensus source to use.
- Whether the ORB stop should be at the range low when the range is very
  wide, and whether to skip trades on wide-range days.
- How "uncorrelated" is measured when building the 3 to 4 strategy
  portfolio, and how capital is split between them.
- What happens to a live strategy after a review: pause, cut size or
  retire it.

## Evidence & claims

- The page gives **no win rate, R:R result, P&L or payout** for any of the
  four models or for Matteo's own trading. No expectancy check is possible.
- **Research claims cited, not quantified on the page:** a large share of
  historical equity-index returns came overnight rather than during regular
  hours; Matteo says he has seen similar behaviour in recent Nasdaq futures
  data. Treat this as self-reported (T4) until checked against the
  underlying studies.
- **Self-reported (T4):** Matteo's experience is that the opening range
  imbalance has worked better on the long side than the short side. No
  figures are given.
- The "70% win rate can still lose the next trade" line and the $10,000
  drawdown and target-risk figures are illustrations, not results.
- The 1R to 2R ORB target is a range to test, not a claimed outcome.

## Concepts & lineage

- Research → rules → code → backtest pipeline →
  [[concept_backtesting]], [[concept_trading_plan]]
- In-sample and out-of-sample split, frozen rules, overfitting warning →
  [[concept_overfitting_validation]]
- Monte Carlo shuffle and resampling of the trade list, drawdown and
  losing-streak ranges → [[concept_risk_of_ruin_drawdown]],
  [[concept_probabilistic_thinking]]
- Positive expected return across a large sample, not single-trade
  outcomes → [[concept_expectancy]], [[concept_edge]]
- Backtest statistics (net profit, win rate, average trade, max drawdown)
  → [[concept_performance_metrics]]
- One-contract development sizing, then volatility targeting →
  [[concept_position_sizing]], [[concept_volatility]]
- Opening range breakout from 9:30 to 10:00 AM ET, and RTH versus
  overnight returns → [[concept_breakout_trading]],
  [[concept_trading_sessions_killzones]]
- VWAP trend model, with VWAP as an institutional execution benchmark →
  [[concept_vwap]], [[concept_optimal_execution_market_impact]]
- Post-earnings announcement drift on an EPS surprise →
  [[concept_news_trading]]
- Anomalies explained by slow information flow and thin overnight
  liquidity → [[concept_random_walk_efficient_markets]],
  [[concept_market_microstructure]]
- Momentum and mean-reversion strategies doing well in different
  conditions → [[concept_market_regimes]]
- A portfolio of 3 to 4 uncorrelated strategies →
  [[concept_correlation_portfolio_risk]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/naoufel-taief-algorithmic.md ===== -->

---
id: strategy_naoufel_taief_algorithmic
type: strategy
title: "Naoufel Taief — No-Code Algorithmic Strategy Portfolio: Generate, Stress-Test & Rotate (stocks/futures, systematic trading)"
partition: 01_chart-fanatics
layer: L8
aliases: [No-Code Algorithmic Trading Strategy, SQX strategy portfolio, Naoufel Taief algo framework, algorithmic strategy incubation and rotation]
taught_by: [person_naoufel_taief]
featured_in: [channel_chart_fanatics]
uses: [concept_backtesting, concept_overfitting_validation, concept_performance_metrics, concept_risk_of_ruin_drawdown, concept_position_sizing, concept_correlation_portfolio_risk, concept_breakout_trading, concept_mean_reversion, concept_market_regimes, concept_volatility, concept_expectancy, concept_risk_reward_r_multiples, concept_machine_learning_finance]
derived_from: [concept_backtesting, concept_overfitting_validation]
related: [strategy_pavel_first_principles, strategy_matteo_conti_institutional]
sources:
  - {title: "Chart Fanatics — No-Code Algorithmic Trading Strategy", url: "https://www.chartfanatics.com/strategies/algorithmic-strategy", tier: T2}
status: verified-t2
---

# Naoufel Taief — No-Code Algorithmic Strategy Portfolio: Generate, Stress-Test & Rotate (stocks/futures, systematic trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/algorithmic-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Naoufel Taief with this framework for
building and running a portfolio of automated strategies without writing
code. The page gives no biography or track record.

## Built for

- **Instruments:** individual stocks (Apple is the example), futures (ES),
  or a universe of stocks selected by filters and ranking (S&P 100 or S&P
  500 style).
- **Style:** fully automated, systematic trading with no discretion.
  Breakout and directional systems are the main focus. Mean reversion,
  volume-based and price-action logic are also used.
- **Timeframes / sessions:** not specified. Strategies are tested across
  timeframes as part of robustness checks.
- **Tooling:** a no-code builder, SQX. The page spells it "Strategic Quant
  X"; the product is usually called StrategyQuant X (editor's note, not
  from the page). It generates,
  backtests and stress-tests strategies, then exports code for
  MultiCharts, TradeStation or MetaTrader. Your own indicators can be
  added as extra building blocks.

## Core idea

Generating strategies is easy, but most are curve-fitted and fail live.
So generate many, then try to **break** them with robustness tests, and
trade only the few that survive. Judge them on risk-adjusted performance
and drawdown, not raw return. Run them as a diversified portfolio that is
managed like a sports team: live strategies play, failing ones are
benched, and an incubation pool in simulation supplies replacements. The
page sums up the philosophy as process over prediction.

## Rules

1. **Set your risk tolerance first.** Decide acceptable drawdown, sizing
   parameters and capital per strategy. Limits for personal money can
   differ from limits for investor capital.
2. **Define the build.** Choose long-only, short-only or both. A **stop
   loss and a profit target are mandatory**. Keep it simple: usually **two
   or three entry rules** and **one exit rule** (sometimes two). More rules
   mean more curve-fitting.
3. **Use building blocks.** Combine predefined conditions such as RSI,
   volatility measures, price patterns and volume.
4. **Set stops and targets.** Stops can be percentage-based, ATR-based or
   indicator-based (for example a channel exit). ATR stops are used to
   adapt risk to calm versus volatile markets. Targets can be
   percentage, ATR or indicator-level based.
5. **Generate for quantity.** Use random rule generation plus genetic
   evolution of parameters. The page notes that optimisation explores
   possibilities but easily produces curve-fitted results.
6. **Apply baseline filters,** deliberately not too strict (the page gives
   these values as examples):
   - return-to-drawdown ratio of at least **4**;
   - profit factor of at least **1.3 to 1.5**;
   - at least **two trades a month**;
   - acceptable Sharpe ratio and UPI.
   Forcing extreme targets, such as very high annual returns, pushes
   results toward curve-fitting.
7. **Robustness tests** (the aim is to break the strategy):
   - *Parameter robustness:* profitable across a range of values, not one
     tuned setting. If it works only at one RSI level, reject it.
   - *In-sample / out-of-sample:* test on held-out data. Both periods
     should include different regimes (bull, bear, high and low
     volatility).
   - *Monte Carlo:* reshuffle the trade sequence to estimate realistic
     maximum drawdown and worst losing streaks. **Monte Carlo drawdown
     outranks backtest drawdown** for setting expectations.
   - *Cross-market and cross-timeframe:* check that the logic does not
     depend on one environment.
8. **Automate the pipeline.** Run tests in sequence so that thousands of
   generated strategies shrink to a few dozen live candidates.
9. **Deploy.** Export, compile and run each strategy automatically with no
   discretionary overrides.
10. **Allocate capital per strategy:** **5% to 25%** of the account each.
    Risk is calculated on each strategy's allocation, not on the whole
    account. Target an average loss of about **0.5% (or less) of the
    allocated capital**.
11. **Keep an incubation pool.** Many strategies keep running in simulation
    to find those doing well on new data.
12. **Bench, do not panic.** Do not pull a strategy for short-term
    underperformance. Act when drawdown nears its expected maximum, or when
    underperformance lasts a long time. Then cut size sharply or move it
    back to simulation. Benched strategies are kept, not deleted, and may
    return.
13. **Replace.** Fill the slot with an incubation strategy that is
    currently performing well.
14. **Ensemble scaling.** When independent strategies using different logic
    (volume, price action, mean reversion, breakout) signal the same
    direction, overall exposure may be increased.
15. **Universe variant.** Filter the universe (trend, price and volume
    thresholds), shortlist, rank with a score such as rate of change over a
    fixed period, and trade only the top-ranked names within position
    limits.

## Risk management

- **Per-trade risk:** average loss of about **0.5% or less of the capital
  allocated to that strategy**. With 5% to 25% allocations, that works out
  to roughly 0.025% to 0.125% of the total account per average loss
  (derived arithmetic, not stated on the page).
- **Allocation:** 5% to 25% of the account per strategy.
- **Sizing basis:** risk of ruin, using win rate, R:R and average loss as
  inputs, not confidence.
- **Drawdown:** the main constraint. The page notes that a 50% drawdown
  needs a 100% gain to recover. Monte Carlo drawdown sets the expected
  maximum.
- **Exposure:** prefer strategies with less time in the market for the
  same return, to reduce exposure to extreme events and free capital.
- **Benching:** cut size or return to simulation when drawdown nears the
  expected maximum or underperformance persists.
- **Daily / weekly limits:** Not specified in the playbook.
- **Portfolio-level drawdown cap:** Not specified in the playbook.

## What the playbook leaves unspecified

- How much historical data to use, and how to split in-sample and
  out-of-sample periods.
- Monte Carlo settings: number of runs and which percentile counts as the
  expected maximum drawdown.
- How wide a parameter range a strategy must survive.
- How long "extended" underperformance is before benching, and how long
  incubation lasts before promotion.
- Correlation limits between live strategies, and how many run at once.
- How much to increase exposure when the ensemble agrees.
- Transaction cost and slippage assumptions in testing.
- Bar timeframes for the strategies.
- A total portfolio risk or drawdown limit.

## Evidence & claims

- The page reports **no P&L, returns or payouts** for the portfolio.
- **Typical breakout-system inputs:** win rate around **40%**, R:R around
  **2:1** (sometimes higher). Self-reported (T4). These are stated as
  typical design inputs, not measured results.
  - Expectancy check (our arithmetic, not on the page): E = 0.40 × 2 −
    0.60 = **+0.20R per trade**. The break-even win rate at 2:1 is about
    33%, so the margin is thin if the real win rate slips toward that.
- The claim that thousands of generated strategies typically shrink to a
  few dozen viable ones is self-reported (T4).
- The page offers no independent test of the portfolio.

## Concepts & lineage

- Long-history backtests across regimes → [[concept_backtesting]]
- Parameter robustness, out-of-sample holdout, Monte Carlo, cross-market
  checks, few rules → [[concept_overfitting_validation]]
- Sharpe, UPI, profit factor, return-to-drawdown, exposure →
  [[concept_performance_metrics]]
- Drawdown asymmetry and sizing by risk of ruin →
  [[concept_risk_of_ruin_drawdown]]
- 5% to 25% allocation and 0.5% average loss per strategy →
  [[concept_position_sizing]]
- Uncorrelated strategy portfolio and ensemble agreement →
  [[concept_correlation_portfolio_risk]]
- Breakout systems as the core, mean reversion as a complement →
  [[concept_breakout_trading]], [[concept_mean_reversion]]
- Testing across bull, bear and high and low volatility periods →
  [[concept_market_regimes]]
- ATR-based stops and targets → [[concept_volatility]]
- Low win rate offset by about 2:1 payoff → [[concept_expectancy]],
  [[concept_risk_reward_r_multiples]]
- Genetic evolution of rules and parameters →
  [[concept_machine_learning_finance]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/nbb-trader-po3-ote-adr.md ===== -->

---
id: strategy_nbb_trader_po3_ote_adr
type: strategy
title: "NBB Trader — PO3, OTE + ADR: Market Maker Model with Fixed-R Fib Entries (forex, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [PO3 OTE ADR Forex Playbook, Market Maker Model + OTE, Smart Money Reversal OTE, NBB Trader strategy]
taught_by: [person_nbb_trader]
featured_in: [channel_chart_fanatics]
uses: [concept_amd_power_of_three, concept_premium_discount_ote, concept_fibonacci, concept_order_blocks_breakers, concept_fair_value_gap, concept_liquidity, concept_liquidity_sweep_reversal, concept_market_structure, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_risk_reward_r_multiples, concept_trade_management]
derived_from: [concept_smart_money_concepts, concept_amd_power_of_three]
related: [strategy_tg_capital_trident, strategy_trader_mayne_structure_ote, strategy_tanja_amd_futures, strategy_trader_kane_lab_model]
sources:
  - {title: "Chart Fanatics — PO3, OTE + ADR Forex Playbook", url: "https://www.chartfanatics.com/strategies/po3-ote-adr", tier: T2}
status: verified-t2
---

# NBB Trader — PO3, OTE + ADR: Market Maker Model with Fixed-R Fib Entries (forex, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/po3-ote-adr. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits NBB Trader with this forex playbook,
which combines a Market Maker Model with Optimal Trade Entry Fibonacci
levels. The page gives no biography.

## Built for

- **Instruments:** forex.
- **Style:** labelled swing trading. Execution, however, runs inside
  intraday session windows; see the gaps section.
- **Timeframes:** **Daily and 4H** for bias and PD arrays. **15m or 30m**
  to confirm the breaker and displacement. **5m** only to refine an entry
  after confirmation, for example from a 5m FVG. **No 1m charts**; the page
  says to avoid them unless highly experienced.
- **Sessions (New York time):** **London Open 2–5 AM**, **New York Open
  7–10 AM**, **London Close 10 AM–12 PM**. London Close works best when a
  large move has already started earlier in the day.

## Core idea

The Market Maker Model reads each day as **accumulation** (a tight range,
often in Asia), **manipulation** (a break of that range to trap traders,
often at London) and **distribution** (the real move the other way, often
in New York). Trade only distribution in the direction of a pre-set
higher-timeframe bias. Confirm it at a key level with a Smart Money
Reversal: a breaker pattern plus a displacement candle. Then enter on a
Fibonacci pullback into the OTE zone. Because the stop sits at the 1.0
level and the first target at 0.0, the R-multiple is fixed by the entry
level, whatever the size of the range.

## Rules

1. **Set the bias before the day.** Use the weekly and daily charts. If
   they are bearish, look only for shorts. Never trade both directions.
   The bias also tells you which side is accumulation and which is
   distribution.
2. **Price must open near a key level (PD array).** Valid levels:
   previous day high or low; previous week high or low; daily or 4H FVGs;
   daily or 4H order blocks; daily or 4H breaker blocks; mitigation blocks.
   If price opens far from one, skip the trade.
3. **Trade only in the session windows** listed above.
4. **Wait for the manipulation to finish** and distribution to start in
   your direction. In the worked example, London ran above the previous
   day's high and that sweep made the high of the day.
5. **Confirm with a Smart Money Reversal on the 15m or 30m chart.** Both
   parts are required:
   - *Breaker structure:* for a short, a high, a low, a higher high, then
     a lower low. The page notes some traders call this a head and
     shoulders. The page shows only the short version; longs are
     presumably the mirror image.
   - *Displacement:* a strong candle that **closes with its body** (not just
     a wick) beyond the key level.
   - If displacement is weak, or another PD array is in the way, skip that
     entry and wait for a second pullback.
6. **Draw the Fibonacci** from the swing created by the manipulation to the
   swing created by the displacement (high to low for a short).
7. **Enter only on a pullback into 0.50, 0.62 or 0.705**, with 0.79 as an
   optional deeper level. If price does not retrace at least to **0.50**,
   there is no trade. The 5m can be used to refine the entry.
8. **Stop:** the default is the **1.0 level** (the swing extreme). The
   tighter option is **0.90**.
9. **First take-profit:** always the **0.0 level**.
10. **Break-even:** once price **closes past the 0.20 level**, move the stop
    to break-even.
11. **Let it run if it breaks through:** if price closes through the TP with
    momentum, keep the position, trail the stop, and use the old TP as the
    new stop.
12. **Scaling in:** add a second entry, with new risk, only when the first
    is at break-even or better. Never add while the first position still
    carries full risk.

## Risk management

- **Fixed geometry:** stop at 1.0 (or 0.90), target at 0.0. Risk and reward
  are set by the entry level, not by the size of the range.
- **Break-even** at a close past 0.20, and no scaling while the first
  position is at full risk.
- **Risk per trade ($ or %), position size, maximum trades, and daily or
  weekly loss limits:** Not specified in the playbook.
- **Skip conditions:** price opening far from a PD array, weak
  displacement, an opposing PD array in the way, or no pullback to at
  least 0.50.

## What the playbook leaves unspecified

- **ADR.** The title names it (presumably Average Daily Range), but the
  page never defines it or says how it is used.
- How "close to a key level" is measured at the open.
- How to grade swings and choose the fib anchors when several swings
  qualify. The page admits this takes practice.
- How the swing-trading label fits the session-based entries: how long a
  trade is held, and whether it is closed at session or day end.
- When the optional 0.79 entry should be used, and how the 1.0 versus 0.90
  stop is chosen.
- Whether part of the position is closed at the 0.0 TP or all of it, and
  how the runner's trail is managed beyond using the old TP as a stop.
- How many trades per day or session, and which session takes priority
  when more than one sets up.
- A definition of mitigation blocks, and how to weigh competing PD arrays.

## Evidence & claims

- The page reports **no win rate, P&L or payout**. The worked example
  (London sweep of the previous day's high, breaker and displacement,
  entry in the 0.62–0.705 zone) gives no result.
- **The fixed R-multiples on the page do not match its own geometry**
  (our arithmetic, not stated on the page). The page lists 50% ≈ 1.63R,
  62% ≈ 2.38R and 70.5% ≈ 3.75R. With the stop at 1.0 and the target at
  0.0, the R at an entry level x is x ÷ (1 − x):
  - 0.50 → **1.00R**
  - 0.62 → **1.63R**
  - 0.705 → **2.39R**
  - 0.79 → **3.76R**
  The page's numbers are each one level off; they belong to the next
  deeper entry. With the tighter 0.90 stop the values are 1.25R, 2.21R,
  3.62R and 7.18R.
- Break-even win rates for the corrected stop-at-1.0 values: 50% at 0.50,
  about 38% at 0.62, about 30% at 0.705 and about 21% at 0.79. Without a
  reported win rate, no expectancy check is possible.
- The pros list calls the R levels fixed and the approach consistent.
  These are claims about design, not measured outcomes.

## Concepts & lineage

- Accumulation, manipulation, distribution across Asia, London and New
  York → [[concept_amd_power_of_three]]
- Session windows → [[concept_trading_sessions_killzones]]
- Previous day and week highs and lows as liquidity, and the manipulation
  sweep → [[concept_liquidity]], [[concept_liquidity_sweep_reversal]]
- FVGs as PD arrays and 5m refinement → [[concept_fair_value_gap]]
- Order, breaker and mitigation blocks; the breaker pattern in the Smart
  Money Reversal → [[concept_order_blocks_breakers]]
- Displacement with a body close, structure shift →
  [[concept_market_structure]]
- OTE retracement zone (0.62–0.79) → [[concept_premium_discount_ote]]
- Fibonacci anchors, entries, stop, target and the 0.20 break-even level →
  [[concept_fibonacci]]
- Daily and 4H, then 15m or 30m, then 5m → [[concept_multi_timeframe_analysis]]
- R fixed by entry level → [[concept_risk_reward_r_multiples]]
- Break-even, trailing past TP, scaling only when risk-free →
  [[concept_trade_management]]
- Lineage (our attribution; the page does not name ICT): ICT smart-money
  concepts and the PO3 / Market Maker Model →
  [[concept_smart_money_concepts]], [[concept_amd_power_of_three]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/okala-80-20-nasdaq.md ===== -->

---
id: strategy_okala_80_20_nasdaq
type: strategy
title: "Okala — 80/20 Nasdaq Strategy: Reactions at 20 and 80 Price Endings (NQ futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [80/20 Strategy, 80/20 Nasdaq strategy, Okala 80/20, Fork and H pattern model]
taught_by: [person_okala]
featured_in: [channel_chart_fanatics]
uses: [concept_support_resistance, concept_price_action, concept_candlestick_patterns, concept_mean_reversion, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_market_regimes, concept_volatility, concept_risk_reward_r_multiples, concept_trade_management]
derived_from: [concept_support_resistance, concept_price_action]
related: [strategy_jj_simon_fair_pricing, strategy_candace_lau_nq_sweep_reversal]
sources:
  - {title: "Chart Fanatics — 80/20 Trading Strategy Explained (NASDAQ Day Trading Guide)", url: "https://www.chartfanatics.com/strategies/80-20-nasdaq-strategy", tier: T2}
status: verified-t2
---

# Okala — 80/20 Nasdaq Strategy: Reactions at 20 and 80 Price Endings (NQ futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/80-20-nasdaq-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents a price-only model for day trading Nasdaq
futures based on how NQ reacts at prices ending in 20 and 80. It is
attributed to Okala in the Chart Fanatics playbook listing; the page text
itself does not name the trader and gives no biography.

## Built for

- **Instruments:** Nasdaq futures (NQ). The level logic is built only for
  Nasdaq behaviour. The structure ideas may show up on other charts, but
  the 20/80 part is NQ-specific.
- **Style:** intraday day trading with precise entries and quick first
  scales. It is not a trend-chasing or large-move model.
- **Timeframes:** a **10-minute** chart for structure and context, and a
  **200-second** chart for execution.
- **Time window:** best around the **New York open**, when volatility is
  high. Slow periods, especially **lunch**, reduce the edge.
- **Tools:** price only. No indicators and no order-flow tools.

## Core idea

Prices ending in **20** and **80** (for example 25,620 and 25,680) are spots
where NQ tends to pause, reject, revert or overshoot briefly before
rotating back. The level gives the **location**. A recognisable
**structure** gives the reason to enter: the Fork (a long reversal), the H
pattern (a short continuation), and the Cross-Section (a precision
entry). The **Repair**, a candle with no wick on one side, acts as a magnet
and target. The best trades stack all of these and still fit a fixed
10-point stop.

## Rules

1. **Context.** Trade when the market is active and moving with intent,
   ideally the New York open. Choppy markets are fine if the chop produces
   clear reactions and structure. Avoid slow, aimless drift such as the
   lunch hour.
2. **Location.** Watch the nearest price ending in 20 or 80. The reaction
   can come a little before or after the exact level; behaviour matters
   more than precision. **If price turns before reaching the level, the
   trade is missed. Do not chase.**
3. **Map the magnets (Repairs).** A bearish candle with no upper wick
   leaves a magnet above price. A bullish candle with no lower wick leaves
   one below. Untouched Repairs are used mostly as targets, not entries.
4. **Setup: pick the structure.**
   - **Fork (long reversal):** after a sharp move lower, a rejection candle
     forms, often with a long lower wick and a small body. The next candle
     tests that low **but fails to break it**. The setup is valid once
     price starts pushing back up. Ideally there is a 20/80 level nearby
     and room to revert into a target or Repair.
   - **H pattern (short continuation):** after a move lower, a bounce
     fails and rolls over into a lowercase "h" shape. It is strongest when
     the bounce spikes into an **80** level and is rejected. The H is the
     structural condition, not the trigger.
   - **Cross-Section (precision entry):** the overlap zone between two
     important candles. When price returns to it and reacts, it gives a
     tight entry. It can refine an H or any clear continuation or
     reversion setup, and it is stronger when it lines up with a 20 or 80.
5. **Entry trigger.** Enter on a clear reaction, not on anticipation
   alone. The best entries combine a key level, a clean structure, a
   refined entry point and an obvious target. Examples from the page:
   - long as price lifts off the Fork's failed low;
   - short on the retest of the 80 level after the H forms;
   - long when price touches the Cross-Section and the 20 level and
     reacts.
6. **Stop.** A **fixed 10-point stop**, beyond the level or the low or
   high. **If the setup cannot take a clean 10-point stop, skip it.**
7. **First target.** Scale out at **+15 points** to cover risk.
8. **Manage the runner.** After the first scale, move the stop to
   **break-even**. Hold the rest only while momentum and structure stay
   clean, often toward a Repair magnet. Reduce or close it if price stalls,
   chops or loses structure. The runner is a bonus; the base hit is the
   point.
9. **Filter.** Skip partial setups: a pattern away from a level, a level
   reaction without clean structure, or a trade that needs more than the
   standard stop. Overtrading is the main danger, because NQ offers many
   reactions in a session.

## Risk management

- **Stop:** fixed **10 points** on NQ for every trade. A setup that needs
  more is not a playbook trade.
- **First scale:** **+15 points**, then stop to break-even, so the rest of
  the trade carries no downside risk.
- **Runner:** kept only while momentum continues.
- **Contracts per trade, account risk ($ or %), daily loss limit, maximum
  trades per session:** not specified in the playbook.

## What the playbook leaves unspecified

- How big the first scale is (what fraction comes off at +15 points).
- The exact definition of the Cross-Section ("two important candles"):
  which candles, and whether the zone is wicks, bodies or their overlap.
- What counts as a "strong move" or "aggressive selling" before a Fork,
  and how long the Fork's lower wick must be.
- How close to a 20/80 level is close enough. The page allows reactions
  slightly before or after but sets no tolerance.
- Rules for the runner: a trail method, a final target if no Repair is
  nearby, and a time stop.
- Which way to trade at each level (long at 20s, short at 80s, or both
  directions at either). The examples include longs at 620 and 20 and a
  short at 80, but no general rule is given.
- Exact session hours ("New York open", "lunch") and any news-event
  filter.
- The page says there are "four main components" but lists five (level,
  Fork, H, Cross-Section, Repair).
- Daily risk limits or a stop-trading rule after losses.

## Evidence & claims

- The page gives **no win rate, payout or P&L**. The trade examples are
  qualitative (for example "very little drawdown" on the Cross-Section
  long). Self-reported (T4).
- **Built-in reward-to-risk:** the first scale is 15 points against a
  10-point stop, so **1.5R**, with the rest at break-even. No win rate is
  claimed, so a full expectancy check is not possible. As a reference: if
  a whole position were closed at 1.5R, E = p×1.5 − (1−p) breaks even at
  **p = 40%**. Runners add upside, and break-even stops add outcomes near
  zero.

## Concepts & lineage

- Round-number price endings (20 and 80) as reaction levels →
  [[concept_support_resistance]]
- Fork rejection wick, failed lows, H-shaped failed bounce →
  [[concept_price_action]], [[concept_candlestick_patterns]]
- Reverting from overshoots at a level back into a Repair →
  [[concept_mean_reversion]]
- Repair candles (no wick on one side) as magnets for unfilled price.
  Editorial note: this resembles the idea of revisiting inefficient price,
  but the page does not use FVG terms → [[concept_fair_value_gap]]
- 10-minute context with a 200-second trigger →
  [[concept_multi_timeframe_analysis]]
- New York open preferred, lunch avoided, active versus slow conditions →
  [[concept_trading_sessions_killzones]], [[concept_market_regimes]],
  [[concept_volatility]]
- Fixed 10-point stop and 15-point first scale (1.5R) →
  [[concept_risk_reward_r_multiples]]
- Scale out, stop to break-even, runner only on momentum →
  [[concept_trade_management]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/pavel-first-principles.md ===== -->

---
id: strategy_pavel_first_principles
type: strategy
title: "Pavel — First-Principles Trading Framework (multi-asset, strategy-design framework)"
partition: 01_chart-fanatics
layer: L8
aliases: [first-principles trading framework, playground vs approach, Pavel framework, three directional approaches]
taught_by: [person_pavel]
featured_in: [channel_chart_fanatics]
uses: [concept_edge, concept_expectancy, concept_performance_metrics, concept_market_microstructure, concept_random_walk_efficient_markets, concept_liquidity, concept_volatility, concept_breakout_trading, concept_oscillators_momentum, concept_mean_reversion, concept_moving_averages, concept_trend_following, concept_support_resistance, concept_backtesting, concept_correlation_portfolio_risk]
derived_from: [concept_edge, concept_random_walk_efficient_markets]
related: [strategy_matteo_conti_institutional, strategy_ted_zhang_stage_analysis, strategy_lance_breitstein_mean_reversion]
sources:
  - {title: "Chart Fanatics — First-Principles Trading Framework by Pavel", url: "https://www.chartfanatics.com/strategies/trading-first-principles-framework", tier: T2}
status: verified-t2
---

# Pavel — First-Principles Trading Framework (multi-asset, strategy-design framework)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/trading-first-principles-framework. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Pavel as the author of this framework. The page gives no biography and no track record.

## Built for

- **Instruments:** "Multi Assets". The page discusses forex, commodities, stocks and ETFs (large caps, broad indexes and small caps) and crypto.
- **Style:** no label. This is a strategy-design framework. Its worked rules use daily data, with holding periods of about 1–5 days for short-term momentum and mean reversion. Trend-following trades are held until the 10-day MA exit triggers; the page gives no typical duration.
- **Timeframes:** the parameter examples are daily. The 1-hour and 1-minute timeframes appear only as contrasts. Holding period matters as much as chart timeframe: a 5-minute entry held for three days counts as a longer-horizon trade.
- **Session / time window:** not specified.

## Core idea

The framework says an indicator or pattern is only a measuring tool. In its words, "a trading tool is not the same thing as a trading edge." A trader first chooses the *playground* (asset class plus timeframe) and then the *approach*. The best playgrounds for a small trader have less institutional competition and a large enough expected move per trade relative to costs. The edge there also needs enough capacity to survive. The page points to smaller, less liquid markets, and to higher timeframes or longer holds as liquidity rises. It also warns against simply picking the most volatile market. The trader then picks one of three directional behaviours: short-term momentum, mean reversion, or long-term momentum. Once more than one strategy is profitable, the trader combines less-correlated strategies and rebalances between them.

## Rules

1. **Assess the playground before any setup.** Rate the asset class and timeframe for liquidity, volatility, efficiency and professional competition. Avoid the most competitive mix, which is very high liquidity on a very low timeframe. In more liquid markets, prefer higher timeframes or longer holds.
2. **Check expectancy against costs.** The expected move per trade has to be large next to fees, spread and slippage. The page's example is a 1-hour breakout earning about 0.4% per trade against about 0.2% in round-trip costs. Costs eat half of that edge.
3. **Match the approach to the asset class:**
   - *Large stocks and indexes:* long-side trend following and long-side mean reversion.
   - *Small caps:* less liquid and less efficient, so short-term momentum and even short-side mean reversion can work. The page doesn't say whether the large-cap approaches also apply.
   - *Commodities:* all three directional approaches.
   - *Forex:* the framework favours long-term momentum and mean reversion.
   - *Crypto:* all three. Some less-liquid venues also allow arbitrage and market making.
   - *Beginners:* simple long-term momentum across several assets.
4. **Short-term momentum (breakout), entry.** Measure normal recent movement, then enter when it expands sharply. In the page's example, the previous five daily candles averaged about 1% and the next candle moved about 2%, a roughly 2× volatility expansion. RSI, CCI or another momentum gauge can measure this. Research the exact threshold for each market.
5. **Short-term momentum, exit.** Either use a time exit (the page says daily-chart momentum lasts about 2–5 days; set N by research) or hold while momentum persists and exit when it fades.
6. **Mean reversion, entry.** Pick a mean, for example the 5-day simple moving average. Measure how far the close normally sits from it (about 2% in the example). Enter toward the mean when the gap becomes abnormally large (6–7% in the example). Short-period RSI or price-action measures are alternatives. Price must be stretched relative to its normal behaviour; a move in one direction alone is not a signal.
7. **Mean reversion, exit.** Either use a time exit (the page says about 1–4 days on daily data) or exit when price returns to the mean.
8. **Long-term momentum (trend following), entry.** Go long when price breaks above the highest high of the last 100 days. Longer lookbacks such as 200 days can also be used. An all-time-high break is a bigger resistance break and one of the strongest forms of long-term momentum. The page says the downside can be traded the same way "where appropriate".
9. **Long-term momentum, exit.** Stay in while price closes above the 10-day moving average. Exit on a close below it. Don't let a small correction close the position.
10. **Combined entry.** After a 100-day-high breakout, a pullback can be bought as a mean-reversion trade inside the trend. Enter when the mean-reversion condition appears rather than waiting for price to turn back up, because waiting for confirmation gives up part of the edge.
11. **Portfolio.** Add strategies that are less correlated, uncorrelated or negatively correlated with each other. Allocate capital across them, for example 50/50, and rebalance to the target weights on a schedule (daily, weekly, monthly or another interval).
12. **Keep researching.** Edges decay as more capital trades them, and lower-timeframe edges decay fastest. Research is a continuing job.

## Risk management

- **Risk per trade:** Not specified in the playbook.
- **Stop-loss:** Not specified. Exits are time-based, momentum-based, return-to-mean or a 10-day MA close. The page gives no protective stop rule for any approach.
- **Daily / weekly limits:** Not specified in the playbook.
- **Sizing:** Not specified per trade. At portfolio level, capital is split across strategies and rebalanced to target weights.
- **Structural risk control:** pick playgrounds with less competition and less cost drag. Lower portfolio volatility, and so raise the Sharpe ratio, by combining less-correlated edges rather than chasing smooth returns at very short timeframes.

## What the playbook leaves unspecified

- Numeric thresholds for a "meaningful" volatility expansion and an "abnormally large" deviation. The 2× and 6–7% figures are examples only. The page also doesn't say how to measure "normal" movement (ATR, average absolute deviation, lookback length).
- RSI and CCI lengths and trigger levels.
- Protective stops, per-trade sizing, and handling of overnight gaps for all three approaches.
- Concrete short-side trend-following rules ("where appropriate").
- Universe selection: liquidity minimums, which small caps or crypto venues, and cost assumptions by market.
- How deep a counter-trend pullback must go before the trend-following entry in rule 10, and what invalidates it.
- How to measure correlation between strategies, how to set target weights, how often to rebalance once costs are counted, and how to detect that an edge has decayed (metric, sample size).

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims about Pavel's own trading.
- **Illustrative expectancy:** a crypto breakout earns about 1.5% per trade on the daily chart and about 0.4% on the 1-hour chart. Self-reported (T4), and the page itself calls these examples. Cost arithmetic: 0.2% in round-trip costs takes 50% of a 0.4% edge but only about 13% of a 1.5% edge.
- **Duration claims:** daily short-term momentum lasts about 2–5 days, and daily mean reversion plays out over about 1–4 days. Self-reported (T4); no data shown.
- **Rebalancing example:** $20,000 split 50/50 between two strategies that return +100% and −50%, then the reverse. Without rebalancing the account ends at $20,000; with one annual rebalance it ends at $31,250. The arithmetic checks out, but the case is built on perfectly alternating returns. Real gains depend on actual correlation and relative mean reversion, minus rebalancing costs.
- The claims that long-term momentum is the most robust approach across asset classes, and that lower-timeframe edges decay faster, are argued from first principles with no backtest shown (T4).

## Concepts & lineage

- Edge as a statistically positive expected outcome over a large sample: [[concept_edge]], [[concept_expectancy]]
- Sharpe ratio and why institutions pay for stable return streams: [[concept_performance_metrics]]
- Competition from market makers and arbitrageurs, plus spread, fees and slippage as cost drag: [[concept_market_microstructure]]
- Edge decay and the move from immature to mature markets as inefficiencies are arbitraged away: [[concept_random_walk_efficient_markets]]
- The liquidity–volatility trade-off and small size as a retail advantage: [[concept_liquidity]], [[concept_volatility]]
- Short-term momentum measured as a volatility expansion, optionally with RSI or CCI: [[concept_breakout_trading]], [[concept_oscillators_momentum]]
- Mean reversion measured as distance from a 5-day SMA: [[concept_mean_reversion]], [[concept_moving_averages]]
- Trend entry on a 100-day-high break with a 10-day MA exit: [[concept_trend_following]], [[concept_support_resistance]]
- Researching thresholds and time exits for each market: [[concept_backtesting]]
- Combining less-correlated strategies and rebalancing: [[concept_correlation_portfolio_risk]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/pradeep-bonde-episodic-pivot.md ===== -->

---
id: strategy_pradeep_bonde_episodic_pivot
type: strategy
title: "Pradeep Bonde — Episodic Pivot (EP) Strategy (stocks, day trading / swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [episodic pivot strategy, Stockbee EP, EP family, "EP 9M", delayed reaction EP]
taught_by: [person_pradeep_bonde]
featured_in: [channel_chart_fanatics, podcast_words_of_rizdom]
uses: [concept_episodic_pivot, concept_news_trading, concept_growth_momentum_canslim, concept_breakout_trading, concept_support_resistance, concept_trade_management, concept_position_sizing]
derived_from: [concept_growth_momentum_canslim]
related: [strategy_ariel_hernandez_real_simple, strategy_matteo_conti_institutional]
sources:
  - {title: "Chart Fanatics — Pradeep Bonde’s Episodic Pivot (EP) Strategy", url: "https://www.chartfanatics.com/strategies/episodic-pivot-strategy", tier: T2}
  - {title: "Chart Fanatics strategies index (lists Episodic Pivot Strategy by Pradeep Bonde)", url: "https://www.chartfanatics.com/strategies", tier: T2}
  - {title: "Words of Rizdom episode with Pradeep Bonde (StockBee)", url: "https://x.com/Wordsofrizdom/status/1920133277584699473", tier: T4}
status: verified-t2
---

# Pradeep Bonde — Episodic Pivot (EP) Strategy (stocks, day trading / swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/episodic-pivot-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits Pradeep Bonde with the Episodic Pivot method, which the playbook says has grown into a whole family of EP setups. The page gives no biography. The earlier note's "Stockbee" handle and his *Words of Rizdom* podcast interview come from that podcast source, not the playbook (T4).

## Built for

- **Instruments:** stocks; the page names no exchange or market. The examples are SMCI, ROOT, ANF, HIMS and OKLO. Of these, the page describes only ROOT (about $100–200M market cap) and OKLO (small cap) by size.
- **Style:** day trading and swing trading. Entries are mostly on Day 1 or within days to about a month of a catalyst. Positions are then trailed for days to months.
- **Timeframes:** no chart timeframe is named. The rules imply daily bars for context, trend and trailing stops, and intraday action for Day-1 entries: opening print, the first 5–10 minutes, the opening range, and red-to-green turns.
- **Session / time window:** the market open for Day-1 entries (market-on-open order or the first 5–10 minutes). Nothing else is specified.

## Core idea

An Episodic Pivot happens when a long-neglected stock gets a catalyst that changes its story, and the market reprices it fast on a big gap and a surge in volume. The playbook names three ingredients: months of neglect, a news catalyst, and rapid repricing. The aim is to get in at the start of that re-rating, use the catalyst and volume as confirmation, keep risk tight, and size up when conviction is high. Beyond the classical earnings EP, the variants (turnaround, story, 9M volume, delayed reaction, "sugar babies") raise the number of setups from a handful a year to dozens or more.

## Rules

1. **Context: neglect.** The stock has done little for months. It sits near lows or in a dead range, with no strong narrative and little interest.
2. **Qualify the catalyst and pick the EP type:**
   - *Classical growth EP:* earnings or a pre-announcement shows very strong sales growth, ideally triple-digit (100%+), with guidance that high growth should last several quarters. The company is small or mid-sized, and the stock gaps up substantially on heavy volume.
   - *Turnaround EP:* a beaten-down company (falling sales, management or product problems, a bad cycle) shows a clear, credible turnaround in earnings or profitability, with a strong gap, trend and heavy volume.
   - *Story / thematic EP:* a simple hot theme the market can easily talk about (examples: AI, crypto or Bitcoin treasuries, quantum computing, robotics, weight-loss drugs). Volume and price moves are very strong, and the stock often moves with a group of theme names. Fundamentals may be weak.
   - *EP 9M (volume EP):* a daily scan for stocks trading 9 million or more shares in a day, far above their normal volume, above a minimum price (for example $3). Look for volume many times normal plus a strong gap or intraday trend. Abnormal volume counts as the catalyst.
   - *Delayed reaction EP (long):* the catalyst day is messy, with a gap that fades or a weak close. Log the stock on a dedicated watchlist and monitor it for up to a month.
   - *Delayed reaction EP (short):* a negative catalyst (guidance cut, very poor earnings, a serious problem) gaps the stock down. Don't short Day 1. Wait for the dip-buyers' bounce.
   - *Sugar babies:* a curated basket (for example 25 names) of habitual runners that have repeatedly made 40–50% bursts in 5–6 days.
3. **Entry trigger by type:**
   - Classical: market-on-open order on Day 1, or within the first 5–10 minutes if strength confirms.
   - Turnaround: Day 1 once the catalyst is confirmed, or the first clean pullback in the new trend.
   - Story: Day 1 if the theme is strong, or a Day 2–3 breakout from consolidation on volume.
   - EP 9M: intraday once the 9M+ volume lines up with a clear trend, or the next day after a strong close.
   - Delayed long: a strong red-to-green day after consolidation, a breakout from the tight range built after the catalyst, or a reclaim of a key level on strong volume.
   - Delayed short: a bounce into resistance that fails (lower high or failed rally).
   - Sugar babies: a strong volume breakout, or a clean pullback into support followed by renewed strength.
4. **Stop placement:**
   - Classical: below the opening-range low (the SMCI example used the Day-1 low).
   - Turnaround: below the nearest logical swing low.
   - Story: tight, below the breakout level or the consolidation low.
   - EP 9M: under intraday support (OKLO example: below the breakout day's low).
   - Delayed long: the entry day's low or the low of the structure being traded against.
   - Delayed short: above the bounce high or the key resistance.
   - Sugar babies: tight, beneath the breakout level or the pullback low.
5. **Exits:**
   - Classical: exit if the trend breaks or the catalyst loses strength.
   - Turnaround: exit only on a clear break of the larger trend.
   - Story: exit on weakness, loss of momentum or fading volume, since theme moves can reverse fast.
   - EP 9M: exit when volume collapses, momentum fades or the structure breaks.
   - Sugar babies: exit quickly once momentum slows, since these are short 5–6 day bursts.
   - Delayed reaction (long and short): Not specified in the playbook. In the HIMS example the stop stayed at the entry-day low and was then trailed under developing swing lows.
6. **Trade management:**
   - In the examples, the stop moves to break-even once the trade has moved strongly in favour.
   - The stop is then trailed under daily swing lows (ROOT example: under each day's low).
   - Turnaround trades are trailed loosely under significant swing lows, because their runway can last several quarters.

## Risk management

- **Risk per trade:** Not specified in the playbook (no % or $ figure).
- **Stops:** defined per EP type (rule 4). Delayed-reaction entries allow tighter stops than Day-1 entries, and modern Day-1 gaps of 20–40% or more can need wide stops.
- **Sizing:** scale size with conviction, which comes from understanding the catalyst. High-conviction delayed EPs can take *larger* positions because the stops are tighter. The page notes that sizing big on story EPs is emotionally hard because the companies are often weak.
- **Daily / weekly limits:** Not specified in the playbook.
- **Invalidation:** the trend breaks, the catalyst loses strength, or volume and momentum fade.

## What the playbook leaves unspecified

- How long "neglect" must last (the ROOT example says 6–7 months), plus market-cap, float and liquidity filters other than the $3 example.
- What counts as "far above normal" volume (relative-volume multiple) and a minimum gap size.
- The opening-range length and what "strength confirms" means in the first 5–10 minutes.
- The exact break-even trigger and the swing-low definition for trailing.
- A position-size formula, maximum risk per trade, total portfolio heat, and how many EPs to hold at once.
- Short-side mechanics for delayed short EPs (borrow, squeeze risk).
- Any market-regime filter. How sugar-baby lists are built and refreshed beyond the 40–50% in 5–6 days description.

## Evidence & claims

All figures below are self-reported (T4). Most describe how far the stock moved, not the trader's realized P&L. The page gives no win rate or average R, so no expectancy check is possible. Only winning examples are shown.

- **Typical EP size:** EPs can reprice by 50–300% or more, and the move can unfold in as little as 10–20 trading days.
- **Account impact:** a single EP can move an account 20–50% or even 100%+.
- **Frequency:** classical earnings/sales EPs give only about 5–10 trades a year. Adding the variants gives dozens to hundreds.
- **SMCI (growth EP):** +35% on Day 1, then +189% over 28 trading days.
- **ROOT (growth EP):** +358% in about 16–17 days. The stock rose another +55% after the trailing stop was hit.
- **ANF (turnaround EP):** +240% from the EP day, and about 700–800% over the multi-month trend (low $20s to about $200).
- **HIMS (delayed reaction EP):** catalyst-day volume of 152 million shares, a company record, after a roughly 62% decline. Entry came days later on a red-to-green turn.
- **OKLO (9M EP):** the breakout day traded more than 15 million shares, and a second 9M breakout later started another leg.

## Concepts & lineage

- Neglect → catalyst → rapid repricing on a volume surge: [[concept_episodic_pivot]]
- Earnings, guidance, theme and FDA/partnership news as catalysts: [[concept_news_trading]]
- Triple-digit sales growth and re-rating of growth stocks: [[concept_growth_momentum_canslim]]
- Day 2–3 consolidation breakouts, 9M breakouts and opening-range stops: [[concept_breakout_trading]], [[concept_support_resistance]]
- Break-even stops and trailing under daily swing lows: [[concept_trade_management]]
- Conviction-based sizing and larger size on tighter delayed entries: [[concept_position_sizing]]

## Changes vs. earlier note

- The earlier note (index listing T2 plus podcast T4) only defined an EP as a catalyst-driven, high-volume gap in a neglected stock, and marked screening, entry and stop rules as "pending scrape". The playbook **confirms** that definition and now **supplies** the full rules.
- **Added:** the seven-member EP family (classical growth, turnaround, story/thematic, EP 9M, delayed reaction long and short, sugar babies), each with its own entry, stop and exit.
- **Added:** concrete thresholds: triple-digit sales growth for classical EPs, 9 million shares above a minimum price (for example $3) for EP 9M, a watchlist window of up to one month for delayed EPs, and 40–50% bursts in 5–6 days for sugar babies.
- **Added:** execution and management rules: market-on-open or first 5–10 minute entries, opening-range-low stops, break-even then trailing under daily swing lows, and looser trailing for turnarounds.
- Nothing in the earlier note is contradicted. The Words of Rizdom source is kept at T4.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/rajan-dhall-auction.md ===== -->

---
id: strategy_rajan_dhall_auction
type: strategy
title: "Rajan Dhall — Auction Market Strategy: Auction-Zone Retest with Trend (stocks/futures, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Rajan Dhall Auction Market Strategy, market auction theory, A+ Simple Trading Strategy, A+ trading playbook, Rajan Dhall strategy]
taught_by: [person_rajan_dhall]
featured_in: [channel_chart_fanatics]
uses: [concept_auction_market_theory, concept_trend_following, concept_moving_averages, concept_multi_timeframe_analysis, concept_support_resistance, concept_candlestick_patterns, concept_market_sentiment, concept_trading_sessions_killzones, concept_risk_reward_r_multiples]
derived_from: [concept_auction_market_theory, concept_trend_following]
related: [strategy_fabio_valentini_amt_order_flow, strategy_andrea_cimitan_amt, strategy_vincent_desiano_break_retest]
sources:
  - {title: "Chart Fanatics — Rajan Dhall Auction Market Strategy", url: "https://www.chartfanatics.com/strategies/market-auction-theory", tier: T2}
  - {title: "Riz Iqbal on X (May 2025) — Rajan Dhall episode announcement", url: "https://x.com/Wordsof_Rizdom/status/1925902141010452612", tier: T4}
status: verified-t2
---

# Rajan Dhall — Auction Market Strategy: Auction-Zone Retest with Trend (stocks/futures, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/market-auction-theory. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Rajan Dhall teaches a free 7-lesson masterclass on Chart
Academy. It covers auction market theory, volume profile, a 21 moving
average trend-following approach across three timeframes, and reading
sentiment before the session. His May 2025 Chart Fanatics episode was
announced as an "A+ Simple Trading Strategy" (T4).

## Built for

- **Instruments:** stocks and futures. The page says it is used mainly on
  stocks but also suits indices and crypto, or any market with a strong
  intraday range. The worked example is SPY.
- **Style:** scalping and day trading.
- **Timeframes:** **daily** for bias, **5-minute** for execution. The page
  calls the method fractal, for example monthly with daily, or daily with
  5-minute.
- **Time window:** the **first hour after the open**. Avoid the middle and
  late session unless conditions clearly line up.

## Core idea

Each day's trading is an auction. The prior day's candle and the daily
trend give the direction. On the 5-minute chart, the **auction zone** is
the congestion or value area where buyers and sellers found temporary
balance. The setup comes when price **returns to that zone and rejects it
in the trend's direction**, usually in the high-volume first hour. Moving
averages only confirm that the two timeframes agree. A rejection candle is
the trigger, and trades target at least **2:1**.

## Rules

1. **Directional bias.** Take it from the **previous day's daily candle**.
   A strongly bearish close means a short bias for the next day; a bullish
   one means long.
2. **Trend alignment on both timeframes.** The daily chart must show a
   clear trend, which the page describes as about 45 degrees. The 5-minute
   chart must trend the same way. For longs, price is **above the moving
   averages** (the page's example is 21/50 MAs) on both timeframes; for
   shorts, below. The MAs only confirm
   alignment visually. They are not signals.
3. **Open and gap context.** At the open, check whether price gapped up or
   down, and whether it opened inside or outside the previous day's range.
4. **Mark the auction zone.** On the 5-minute chart, find the area where
   price consolidated or found balance. In the SPY example this was a
   range that formed right after the open, then broke in the trend
   direction.
5. **Entry.** When price retests the auction zone and prints a **rejection
   candle** (for a short: trades into the zone and closes back below it),
   enter **as soon as that candle closes**.
6. **Stop.** Just beyond the setup candle: **above the rejection candle's
   high** for shorts, **below its low** for longs.
7. **Target.** At least **2:1** reward-to-risk.
8. **Retests.** Later retests that reject the same zone again can be traded
   the same way. The SPY example gave a second short.
9. **No-trade conditions.**
   - The daily and 5-minute charts disagree.
   - The auction structure is messy, or sentiment is unclear (for example,
     conflicting news headlines).
   - Price never retests the zone, or sells off at the open with no
     structure.

## Risk management

- **Stop:** beyond the rejection candle's high or low.
- **Reward-to-risk:** minimum 2:1. The cons note that most trades target
  2:1, so large R multiples are not possible without modifying the method.
- **Risk per trade (% or $), sizing:** not specified in the playbook.
- **Daily or weekly limits, maximum number of trades:** not specified in
  the playbook.
- **Temperament:** being a "good loser" and acting fast are listed as
  requirements, because trades often trigger within seconds of the open.

## What the playbook leaves unspecified

- How strong a prior-day candle must be to set a bias, and what to do after
  an indecisive day.
- An objective test for a "45-degree" daily trend, and the MA type (the
  example uses the 21 EMA; the rules say 21/50 MAs "e.g.").
- How to draw the auction zone (its boundaries and minimum duration), and
  whether volume profile is used. The masterclass covers volume profile,
  but the playbook's rules do not.
- What shape counts as a rejection candle, beyond closing back outside the
  zone.
- How the gap and open-location context should change the trade. It is
  listed as context, without rules.
- Whether to move the stop to breakeven, take partials, or how many retests
  remain valid.

## Evidence & claims

- **SPY example:** two shorts after retests of the auction zone, and both
  reached the 2:1 target. Self-reported (T4), with no prices given.
- The page claims **no win rate, P&L or payout**.
- **Expectancy context:** at a fixed 2:1, the break-even win rate is about
  33%. With no stated win rate, E = p×2 − (1−p) cannot be evaluated.

## Concepts & lineage

- The day as an auction, with a congestion or value area as the zone of
  balance → [[concept_auction_market_theory]]
- Trading only with the daily trend → [[concept_trend_following]]
- 21 and 50 MAs as an alignment filter → [[concept_moving_averages]]
- Daily bias with a 5-minute execution; fractal timeframe pairs →
  [[concept_multi_timeframe_analysis]]
- Retesting a broken balance zone → [[concept_support_resistance]]
- The rejection candle as trigger → [[concept_candlestick_patterns]]
- Gap and headline sentiment as context → [[concept_market_sentiment]]
- The first-hour window → [[concept_trading_sessions_killzones]]
- The fixed 2:1 target → [[concept_risk_reward_r_multiples]]

## Changes vs. earlier note

- **Status upgraded from `pending-scrape`.** The earlier note had no rules,
  only a T4 episode announcement. The playbook now provides the full rule
  set at T2.
- **Name.** The earlier note was titled "A+ Simple Strategy & Market
  Auction Theory", taken from the episode announcement (T4). The page is
  titled **"Rajan Dhall Auction Market Strategy"**. The A+ names are kept
  as aliases only.
- **Lineage confirmed, with a nuance.** The earlier note assumed descent
  from auction market theory, and the playbook confirms the auction
  framing. The execution itself, though, is a trend-aligned retest of a
  5-minute consolidation with an MA filter, so trend following is added as
  a second parent.
- **`concept_volume_profile` removed from `uses`.** The playbook's rules
  define the auction zone from price congestion. Volume profile appears
  only in the masterclass description.
- **Added:** the prior-day-candle bias, dual-timeframe 21/50 MA alignment,
  gap and open context, the rejection-candle entry and stop, the 2:1
  target, the first-hour window and the no-trade conditions.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/steven-dux-small-cap-short.md ===== -->

---
id: strategy_steven_dux_small_cap_short
type: strategy
title: "Steven Dux — Small-Cap Short Statistics Playbook (US small-cap stocks, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Small-Cap Short Statistics Playbook, Steven Dux small-cap short, Dux gap-up short, Dux bounce short, Dux first red day]
taught_by: [person_steven_dux]
featured_in: [channel_chart_fanatics]
uses: [concept_mean_reversion, concept_support_resistance, concept_volume_profile, concept_liquidity, concept_market_sentiment, concept_market_microstructure, concept_price_action, concept_trading_sessions_killzones, concept_position_sizing, concept_risk_reward_r_multiples, concept_trade_management, concept_performance_metrics, concept_probabilistic_thinking, concept_edge]
derived_from: [concept_mean_reversion, concept_market_sentiment]
related: [strategy_kyle_williams_first_red_day, strategy_alex_temiz_first_red_day, strategy_kris_verma_shorting, strategy_marios_stamatoudis_parabolic_short]
sources:
  - {title: "Chart Fanatics — Steven Dux - Small-Cap Short Statistics Playbook", url: "https://www.chartfanatics.com/strategies/small-cap-short-statistics", tier: T2}
status: verified-t2
---

# Steven Dux — Small-Cap Short Statistics Playbook (US small-cap stocks, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/small-cap-short-statistics. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Steven Dux as a statistics-first short
seller of low-float US small-cap runners. He waits for the data to qualify a
setup before the chart pattern matters.

## Built for

- **Instruments:** the page header lists stocks and futures, but every rule
  and example concerns **US small-cap equities**: low market cap, low
  float, big percentage moves and heavy retail participation. It works best
  with borrow access.
- **Style:** short-biased day trading. Bounce shorts and first red days are
  next-day or multi-day setups; whether positions are held overnight is not
  specified in the playbook.
- **Timeframes:** the daily chart for history and multi-day runs, and 1-hour
  or 30-minute charts for volume-at-price context. Intraday execution charts
  are not named.
- **Time window:** gap-up shorts focus on **9:30 to 11:30 ET**, when much of
  the day's volume trades. The cleaner trigger comes at about **10:00 to
  11:00**.
- **Tools and level:** a scanner, float and market-cap data, pre-market and
  intraday volume, and a way to estimate full-day volume. The page says it
  is **not a beginner system**: you need to handle halts, locates,
  slippage and squeezes.

## Core idea

Short a small-cap runner only when the numbers show likely selling pressure
outweighing likely buying power. There are three variants of that
imbalance. The **gap-up short** fades a stock up more than 100% once early
volume is spent and it starts losing momentum. The **bounce short** sells
into a prior high-volume consolidation where trapped holders wait to get
out near break-even. The **first red day** shorts a parabolic multi-day
runner after the first red day confirms exhaustion. Filters, crowding
reads, timing and size all come from Dux's statistics. Their purpose is to
avoid being right but too early.

## Rules

**A. Qualify the universe (all variants)**

1. **Market cap:** initial market cap under **$100M** for gap-up shorts.
   Bounce shorts and many first red day candidates can go up to about
   **$200M**.
2. **Float:** under **50M shares**. Dux's bands: 1 to 2M is very low float,
   2 to 5M is mid float, 5 to 10M is larger but still in the universe.
3. **Price:** above **$3**. Lower-priced names distort the statistics.
4. **Sector exclusions:** remove **biotech** and **energy** unless there is
   an extreme outlier reason. Avoid **thin Chinese tickers**, especially
   with intraday volume under about **30M shares** and a thin level 2,
   because of halt risk.

**B. Read volume and crowding**

5. **Estimate full-day volume** from pre-market volume, using a rough
   **1:5 to 1:10** ratio.
6. **Crowding limits for a same-day short:**
   - **More than 50M shares pre-market** means caution. The stock can stay
     crowded and squeeze through the setup. The better trade may be the
     next day, if it gaps down and volume dries up.
   - **Float rotation above about 15x**, especially in very low floats,
     means cutting size and waiting for a clear momentum shift.

**C. Gap-up short (intraday)**

7. **Setup:** the stock is up more than **100%**, with initial market cap
   under $100M and float under 50M. Expect an opening push. Dux's averages
   are **30 to 35%** on 1 to 2M floats and **20 to 25%** on 5 to 10M
   floats.
8. **Timing:** do not short the open. Let it push and **consolidate for
   about an hour**. Look for the first meaningful weakness between about
   **10:00 and 11:00**, once roughly **30 to 35% of expected daily volume**
   has traded.
9. **Entry:** start building size during the consolidation and go to full
   size on the breakdown.
   - *Ultra-low float (under about 2M) with heavy rotation:* wait for a
     clear momentum shift, such as a big drop from the high followed by a
     bounce to short.
   - *Higher float (about 7 to 8M):* shorting against the **pre-market
     high** is more acceptable.
10. **Stop:** above the **consolidation high**.
11. **Target:** based on the average fade (see Evidence) and the intraday
    structure. The first objective is continuation of the breakdown from
    the consolidation. Manage by whether volume keeps drying up and trapped
    buyers start leaving.

**D. Bounce short (next-day or multi-day)**

12. **Find trapped supply:** look back about **one year** on the daily
    chart. Find a day where the stock spiked on heavy volume, consolidated
    around a clear price, then dumped. Measure the trapped block, for
    example 25M shares around $5, about **$125M** trapped.
13. **Compare demand with supply:** estimate the current day's volume from
    pre-market (adjusted for a weak open). The trapped-to-current ratio
    should favour the trapped supply, for example **2:1** (current volume of
    about 10 to 15M against 25M trapped). Size up when the ratio is much
    stronger.
    Skip if current volume can match or overwhelm the trapped block.
14. **Entry:** as close as possible to the old consolidation or resistance,
    for the tightest risk.
    - *Gap straight into the zone on light pre-market volume:* it can fail
      fast after the open.
    - *Climb into the zone during regular hours:* expect more patience and
      possibly a bounce before it rolls over.
15. **Stop:** built around the prior resistance or consolidation. Size so
    that a small push through the level is still survivable.
16. **Target:** depends on how price came back. A direct gap into the zone
    tends to fade faster and deeper than a climb from the lows.

**E. First red day (multi-day runner)**

17. **Qualify the run:** at least **three consecutive green days**, with
    rising (or dollar-adjusted rising) volume and about **300% range** from
    the initial breakout. A two-day run needs about **1,000%**. A **red or
    flat day in the middle resets the count.**
18. **Exhaustion check:** estimate whether the day is likely to reach the
    dollar-volume exhaustion zone, using initial market cap, expected day
    range and estimated volume. If it is not likely, leave it alone.
19. **Wait for the first red day**, then trade the **following session**
    when it opens weak or stays red. The second day of weakness is the main
    trade, not the first guess at the top.
20. **Entry:** about **one-quarter size** near the open, adding if price
    bounces into resistance.
21. **Stop:** around the consolidation or spike area of the red-day failure
    zone.
22. **Reward filter:** skip if the first red day has already erased more
    than **about 50% of the whole run**. The remaining reward is too small.
23. **Manage:** ride the unwind as demand fades. With large size, cover
    along the way so the position gives liquidity back instead of trapping
    itself.

## Risk management

- **Stop first, size second:** place the stop at the real invalidation
  point (consolidation high, prior resistance, or spike area), then size
  down until the risk is acceptable. Do not pick a stop to suit a size.
- **Size caps (bounce shorts):** stay under about **10% of the float** and
  about **1% of the volume**. Oversizing can break the supply-demand
  balance the trade depends on.
- **Size down** for very low floats, crowded names, prices just above $3,
  or setups that only barely qualify. **Size up** when the volume ratio is
  strong and trapped supply is obvious.
- **Scaling:** build into gap-up shorts during the consolidation. Start
  first red days at about one-quarter size.
- **Catastrophe rules:** no thin stocks where a halt could block the exit.
  Do not treat ultra-low-float crowding as a normal fade. Do not size a
  first red day as if the top were guaranteed. Do not short into the
  heaviest volume of a squeeze without a momentum shift. The account has to
  survive being early.
- **Risk per trade in $ or % of account, and daily or weekly loss
  limits:** not specified in the playbook.

## What the playbook leaves unspecified

- The actual win rates. The page says each setup has a known approximate
  win rate and frequency per year but gives no numbers.
- The execution chart and the exact definition of a "meaningful"
  breakdown or "momentum shift" (candle close, VWAP loss, prior low).
- How to calculate the first red day's "dollar-volume exhaustion zone" from
  market cap, range and volume. The method is described, but no formula is
  given.
- How deep a consolidation must be, and how to tell it has formed, beyond
  "about an hour".
- Bounce-short size caps beyond the 10% float and 1% volume limits, and
  whether those caps also apply to gap-up shorts and first red days.
- Concrete profit-taking rules: how much to cover at each stage, and
  whether to use time stops.
- Borrow cost, locate availability and short-sale restriction (SSR) effects
  on the entries.
- What counts as an "extreme outlier" that allows a biotech or energy
  trade.
- How the futures listed in the header fit in. No futures rules are given.

## Evidence & claims

All figures are Dux's own statistics as reported on the page,
self-reported (T4):

- **Gap-up short:** average risk about **7%**, average fade about **24 to
  26%** (about 26% from the intraday high, closer to 24 to 25% from a
  confirmed entry), described as roughly **1:3.5 to 1:4** reward-to-risk
  on clean setups. As arithmetic, 24 to 26% over 7% is about 3.4 to 3.7R,
  so the 1:4 end is slightly above the stated averages.
- **Opening push:** averages of 30 to 35% (1 to 2M floats) and 20 to 25%
  (5 to 10M floats).
- **Bounce short:** one approach type faded about **75%** of the move from
  the top, and another about **50%**.
- **Biotech:** Dux's tracking showed a "meaningful drop" in win rate. No
  figure is given.
- **No win rate** is stated, so a full expectancy check is not possible. As
  a reference only: at 1:3.5 the breakeven win rate is 1/4.5 ≈ 22%, and at
  1:4 it is 1/5 = 20%. With E = p×RR − (1−p), the setup needs a win rate
  above those levels, net of slippage and borrow costs, to be positive.

## Concepts & lineage

- Fading emotional, overextended runners back toward value →
  [[concept_mean_reversion]], [[concept_market_sentiment]]
- Trapped volume at a prior consolidation acting as overhead supply →
  [[concept_support_resistance]], [[concept_volume_profile]]
- Pre-market volume, float rotation and crowding as demand measures; halts,
  thin level 2 and locates → [[concept_liquidity]],
  [[concept_market_microstructure]]
- The 9:30 to 11:30 window and the 10:00 to 11:00 trigger →
  [[concept_trading_sessions_killzones]]
- Consolidation, breakdown and bounce-into-resistance triggers →
  [[concept_price_action]]
- Stop at invalidation, then size to float, volume and setup quality →
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]]
- Scaling in, quarter-size starts and covering into the unwind →
  [[concept_trade_management]]
- Setup frequency, average fade and filters from tracked statistics →
  [[concept_performance_metrics]], [[concept_probabilistic_thinking]],
  [[concept_edge]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/tanja-amd-futures.md ===== -->

---
id: strategy_tanja_amd_futures
type: strategy
title: "Tanja Trades — AMD Futures Model: Trade the Distribution Leg (futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Tanja's AMD Futures Trading Strategy", Tanja AMD model, AMD futures strategy, AMD model]
taught_by: [person_tanja_trades]
featured_in: [channel_chart_fanatics]
uses: [concept_amd_power_of_three, concept_liquidity, concept_liquidity_sweep_reversal, concept_market_structure, concept_fair_value_gap, concept_news_trading, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_intermarket_analysis, concept_market_regimes, concept_trade_management]
derived_from: [concept_amd_power_of_three, concept_wyckoff_method]
related: [strategy_marco_trades_liquidity_grab, strategy_candace_lau_nq_sweep_reversal, strategy_trader_kane_lab_model]
sources:
  - {title: "Chart Fanatics — Tanja's AMD Futures Trading Strategy", url: "https://www.chartfanatics.com/strategies/amd-model", tier: T2}
  - {title: "TradeZella — AMD Model", url: "https://www.tradezella.com/strategies/amd-model", tier: T3}
status: verified-t2
---

# Tanja Trades — AMD Futures Model: Trade the Distribution Leg (futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/amd-model. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Tanja Trades day trades futures with a structured AMD
approach. It is built to avoid chop and to trade only clean, news-driven
moves under strict discipline rules.

## Built for

- **Instruments:** futures. The example is Nasdaq (NQ), and Nasdaq and
  S&P are checked against each other for alignment.
- **Style:** day trading.
- **Timeframes:** 1H, 4H and Daily for the draw on liquidity, key levels
  and major FVGs. 1m, 5m and 15m to confirm displacement and refine the
  entry.
- **Time window:** the **New York session after high-impact news**, not
  during the spike. The playbook's "macro windows" are **9:50 to 10:10 and
  10:50 to 11:10 ET**. The CPI example is built around the 8:30 AM ET
  release.

## Core idea

Markets cycle through **Accumulation** (a sideways range that builds
liquidity), **Manipulation** (a sharp sweep of stops above or below the
range) and **Distribution** (the real directional leg). The accumulation
chop is hard to trade, and the manipulation is not traded directly. Tanja
enters only in **distribution**, once a forceful break of a swing leaves a
**fair value gap** and price comes back into it. A daily filter of news,
correlation and a clear draw on liquidity decides whether there is any
trade at all. The page's default when nothing is clear is that the safest
trade is no trade.

## Rules

1. **Classify the day using the economic calendar.**
   - *High probability:* major scheduled news (CPI, NFP, GDP, FOMC, PPI);
     a strong sweep that clears obvious stops; clean displacement and FVGs
     on the higher timeframes.
   - *Low probability:* no major news; bank holidays or the day after one;
     **the day before** CPI, FOMC or NFP; the day after a large move that
     already hit a major target; jagged highs and lows with no direction.
2. **Check correlation.** Nasdaq and S&P should agree. A heavy divergence
   lowers the odds.
3. **Name the draw on liquidity** on 1H, 4H or Daily: equal highs or lows,
   an unfilled FVG, or a clean swing point. **No clear destination, no
   trade.** If the higher timeframe is unclear, do not force a
   lower-timeframe setup.
4. **Read the AMD sequence.** Mark the accumulation range, then wait for
   the manipulation sweep. Do not trade the sweep itself.
5. **Require displacement.** Price breaks a key swing high or low with
   force and leaves an FVG behind, confirmed on 1m, 5m or 15m. If price
   respects that FVG on the retrace, the move is valid.
6. **Entry.** On the retrace into the valid FVG. **If there is no
   retracement, skip it. Never chase.**
7. **Stop.** In the example, above the high of the manipulation spike,
   which is beyond the sweep extreme. The page gives no general stop rule
   beyond the example.
8. **Targets.** Take partials at logical targets (swing levels or the next
   FVG). The example's target was the pre-market lows and the equal lows
   under the range.
9. **Manage.** Trail the stop to protect profit once the move confirms.
10. **Execution limits.** **Two trades per session at most.** **After two
    losses, stop for the day.** Size down on the day before major news and
    during known accumulation. Stand aside when there is no clear bias or
    structure.

## Risk management

- **Session cap:** at most two trades. Two losses end the day.
- **Sizing:** smaller on days before major news and during accumulation.
  The base risk per trade ($ or %) is not specified in the playbook.
- **Stop:** beyond the manipulation extreme, shown only in the example.
- **No chase:** if the price never retraces into the FVG, there is no
  trade.
- **Daily dollar or weekly limit:** not specified in the playbook, beyond
  the two-loss stop.

## What the playbook leaves unspecified

- A general stop rule and the reward-to-risk minimum. Only the example
  shows a stop, and no R:R figure is given.
- How large a displacement must be, and how big or which kind of FVG is
  valid (the first FVG, or the largest).
- Which timeframe the displacement must show on. The overview says the
  higher timeframe, while the timeframe section says 1m, 5m or 15m; the
  page does not reconcile the two.
- How heavy a Nasdaq–S&P divergence must be to skip a day.
- Whether trades outside the macro windows are allowed, and how the 8:30
  release fits with the 9:50 to 10:10 window.
- How large partials should be, and the rules for trailing.
- Whether FOMC afternoons follow the same timing.

## Evidence & claims

- **CPI short example:** about **100 points on NQ within minutes**.
  Self-reported (T4).
- The page claims **no win rate, R:R figure or payout**. No expectancy
  check is possible.

## Concepts & lineage

- The Accumulation, Manipulation, Distribution cycle →
  [[concept_amd_power_of_three]]
- Liquidity built in the range, then swept → [[concept_liquidity]],
  [[concept_liquidity_sweep_reversal]]
- A forceful break of a swing high or low as confirmation →
  [[concept_market_structure]]
- Displacement that leaves an FVG, with the retrace into it as entry →
  [[concept_fair_value_gap]]
- Classifying days by scheduled high-impact news →
  [[concept_news_trading]], [[concept_market_regimes]]
- Nasdaq–S&P alignment check → [[concept_intermarket_analysis]]
- HTF draw on liquidity with an LTF trigger →
  [[concept_multi_timeframe_analysis]]
- The 9:50 to 10:10 and 10:50 to 11:10 ET macro windows →
  [[concept_trading_sessions_killzones]]
- Partials and trailing stops → [[concept_trade_management]]
- Lineage (editorial, not stated on the page): Dow-style phases, then the
  Wyckoff spring and upthrust, then ICT Power of Three →
  [[concept_wyckoff_method]]

## Changes vs. earlier note

- **Confirmed:** the AMD sequence, trading only after a liquidity sweep and
  confirmed displacement, the focus on major news events, and the chop
  filter. The earlier note had these from T3 TradeZella wording; the
  playbook now confirms them at T2.
- **Refined: confirmation is "displacement / BOS".** The earlier note
  said "displacement / BOS" (T3). The playbook defines displacement as a
  forceful break of a swing high or low **that leaves an FVG**, and the
  entry is the **retrace into that FVG**. If price does not retrace, there
  is no trade.
- **Added:** the high and low probability day lists (including skipping
  the day before CPI, FOMC or NFP), the Nasdaq–S&P correlation check, the
  rule requiring a clear draw on liquidity, the timeframe stack, the
  two-trades and two-losses session cap, sizing down before news, the
  9:50 to 10:10 and 10:50 to 11:10 ET macro windows, partials and
  trailing, and the CPI example.
- **Lineage marked as editorial.** The Dow, Wyckoff, ICT PO3 chain from
  the earlier note is kept but does not appear on the page.
- **Sources.** The earlier note already cited this Chart Fanatics page
  (T2), so it stays as the first source, with no duplicate entry added.
  TradeZella (T3) is kept unchanged.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/ted-zhang-stage-analysis.md ===== -->

---
id: strategy_ted_zhang_stage_analysis
type: strategy
title: "Ted Zhang — Stage Analysis Strategy (multi-asset, swing and position trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Ted Zhang’s Stage Analysis Strategy", Ted Zhang stage analysis, Weinstein-style stage analysis, four-stage cycle, first multi-month base]
taught_by: [person_ted_zhang]
featured_in: [channel_chart_fanatics]
uses: [concept_moving_averages, concept_market_structure, concept_trend_following, concept_market_regimes, concept_multi_timeframe_analysis, concept_breakout_trading, concept_chart_patterns, concept_growth_momentum_canslim, concept_mean_reversion, concept_news_trading, concept_market_sentiment, concept_support_resistance, concept_position_sizing, concept_trade_management]
derived_from: [concept_wyckoff_method, concept_trend_following]
related: [strategy_clement_ang_price_cycle, strategy_ariel_hernandez_real_simple]
sources:
  - {title: "Chart Fanatics — Ted Zhang’s Stage Analysis Strategy", url: "https://www.chartfanatics.com/strategies/stage-analysis-strategy", tier: T2}
status: verified-t2
---

# Ted Zhang — Stage Analysis Strategy (multi-asset, swing and position trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/stage-analysis-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Ted Zhang uses Stan Weinstein-style stage analysis to classify
whether an asset is basing, rising, topping or falling before he commits
capital. The playbook describes him taking long setups in Stage 2, and in
one example he used a failed earnings reaction as a personal short signal.

## Built for

- **Instruments:** multi-asset. The page names liquid stocks, ETFs, crypto,
  commodities, fixed income, futures, forex and currencies.
- **Style:** swing and position trading.
- **Timeframes:** the **weekly** chart classifies the stage and the
  **daily** chart refines the entry. The page calls the method fractal:
  faster traders can apply it to lower timeframes after studying how the
  stages behave there.
- **Tools:** the **10-, 20-, 30- and 40-week simple moving averages**,
  price structure and volume. Relative-strength scans and stage-breadth
  data are optional extras.
- **Session or time window:** not specified in the playbook. It is a
  higher-timeframe method.

## Core idea

Markets move through four repeating stages. **Stage 1** is a base after a
decline. **Stage 2** is the uptrend where longs are favoured. **Stage 3**
is a top where exposure should come down. **Stage 4** is a downtrend where
longs are avoided. The edge is not a moving-average crossover. It comes
from knowing which stage is active, trading with it, and standing aside
in the choppy transition stages, so that you catch the cleaner middle of a
move. Price has to confirm any story: do not buy because something looks
cheap or hold because the news still sounds good.

## Rules

1. **Classify the weekly stage** with four questions. Is price above or
   below the key averages? Are the averages rising, falling or flat? Is
   price trending cleanly or slicing back and forth through them? Is
   structure making higher highs and higher lows, or lower highs and lower
   lows?
   - **Stage 1 (basing):** follows a Stage 4 decline. The decline flattens,
     the 10-week catches up to price, the slower averages converge, and
     price swings above and below them. Bad news stops pushing it lower.
     **A possible base is not yet a trade.**
   - **Stage 2 (markup):** price is above all four averages, with higher
     highs and higher lows. The 10-week is above the 20- and 30-week, the
     slower averages turn up beneath price, and pullbacks hold near rising
     weekly support.
   - **Stage 3 (distribution):** after a long advance, price turns wide,
     loose and sideways. The averages flatten and slice through price,
     breakouts fail, and **good news gets a poor reaction**.
   - **Stage 4 (markdown):** price is below the key averages, with lower
     highs and lower lows. The 10-week is below the 30-week, which is below
     the 40-week. A bounce here is not a new uptrend.
2. **Set the bias.** Go long when the asset is entering or already in
   Stage 2. Avoid longs in a clean Stage 4. Use Stage 1 and Stage 3 to
   watch, reduce and prepare. If breadth shows more and more stocks moving
   into Stages 3 and 4, lower your confidence in new longs. Narrative,
   fundamentals or a catalyst can add conviction only if price confirms
   them.
3. **Qualify the base** (long continuation). The asset must be in Stage 2
   and the base must be clean, not loose. The page singles out the
   **first multi-month base after a strong first Stage 2 leg** as especially
   attractive. Ideally:
   support near the 10- or 20-week average, a shakeout followed by a
   reclaim of the lows, higher lows, tightening on the right side, and a
   clearly defined breakout area.
4. **Entry models (the trigger comes from the daily chart):**
   - *Stage 2 transition:* price leaves a Stage 1 base and reclaims all
     four weekly averages, with the 10-week above the 20- and 30-week.
     Enter on a defined daily breakout as the weekly trend turns up.
   - *First multi-month base continuation:* enter when price clears the
     breakout area with confirmation, ideally on volume.
   - *First consolidation above the 40-week* (investor-style): price
     leaves Stage 1 and holds above the 40-week. Enter on the breakout
     from its first constructive consolidation.
   - *Stage 4 mean reversion* (tactical, separate): price is very
     stretched below the 30- and 40-week and forms a tight shelf around the
     10-week. Take a daily-chart entry back toward the slower averages,
     with clear invalidation. It is not a sign that Stage 2 has begun.
5. **Stop.** Set invalidation before entry: below the base, or below the
   level whose loss proves the breakout failed. If price loses Stage 2
   structure and falls back below the key averages, cut risk or exit.
6. **Targets.** Prior highs and previous all-time highs are reference
   points, but Stage 2 has no fixed target. Let the trend run while price
   respects the rising 10- and 20-week averages. Stage 4 mean-reversion
   trades target the slower moving averages.
7. **Manage.** Sell into strength when price goes unusually vertical.
   Reduce or exit when price turns wide and loose, slices through the
   averages repeatedly, or fails to rally on good news. You need not hold
   every Stage 2 position through the whole cycle. Rotate capital into
   cleaner Stage 2 bases when a position is extended or stuck in a long
   consolidation.
8. **No-trade list.** Skip a clean Stage 4 decline, a possible Stage 1
   that has not broken out, a visible loose Stage 3 range, an extended
   breakout you would be chasing, bullish news without Stage 2 structure,
   and any base too messy to define invalidation.

## Risk management

- **Sizing:** match position size to the stop distance, allowing for the
  wider stops of weekly-chart setups.
- **Invalidation:** below the base or the breakout-failure level. Exit
  when Stage 2 structure is lost. The Moderna example shows a valid
  flat-base breakout above all four averages that failed and fell back into
  Stage 4. The right response was to exit, and the stock later fell much
  further.
- **Portfolio exposure:** cut overall exposure when breadth shows more
  assets moving into Stages 3 and 4. Do not ride out a deep drawdown
  because the long-term story still looks good.
- **Risk per trade ($ or %), maximum positions, and daily or weekly
  limits:** not specified in the playbook.

## What the playbook leaves unspecified

- A precise way to decide the stage: how flat counts as "flat", or how
  many slices through the averages mark a transition.
- The daily-chart trigger: what "confirmation" and "with volume" mean as
  numbers (closing basis, volume multiple).
- Base dimensions: minimum length for "multi-month", depth limits, and how
  tight the right side must be.
- Account risk per trade and how wide a weekly stop can be before the
  trade is skipped.
- How to measure stage breadth and what level should trigger cuts in
  exposure.
- Exit rules for the trend: whether a close below the 10-week or 20-week
  is the exit, and on which timeframe.
- The short-side rules for Stage 3 and Stage 4 beyond the Abercrombie
  example and the Stage 4 mean-reversion bounce.
- What counts as "extremely stretched" for the Stage 4 mean-reversion
  setup.

## Evidence & claims

- **Rare-earth ETF example:** after the first multi-month base, with the
  breakout near 75, the move ran about **25 to 30%**. Self-reported (T4).
- **Abercrombie & Fitch:** a gap down on better-than-expected earnings
  inside a loose Stage 3 structure, which Zhang used as a personal short
  signal. No result is given.
- **Moderna:** a failed Stage 1 to Stage 2 breakout, shown as a lesson in
  taking the loss. No figures are given.
- The page claims **no win rate, R:R or P&L**. No expectancy check is
  possible.

## Concepts & lineage

- The four-stage cycle (accumulation, markup, distribution, markdown).
  The page calls it Weinstein-style; the Wyckoff phase vocabulary link is
  editorial → [[concept_wyckoff_method]], [[concept_market_regimes]]
- Higher highs and higher lows versus lower highs and lower lows to read
  trend direction → [[concept_market_structure]],
  [[concept_trend_following]]
- 10-, 20-, 30- and 40-week SMA slope and alignment →
  [[concept_moving_averages]]
- Weekly stage with a daily entry → [[concept_multi_timeframe_analysis]]
- First multi-month base, shakeout and reclaim, right-side tightening,
  breakout → [[concept_chart_patterns]], [[concept_breakout_trading]],
  [[concept_growth_momentum_canslim]]
- Good news failing to lift price as a sign of distribution →
  [[concept_news_trading]], [[concept_market_sentiment]]
- Stage 4 shelf bounce toward the slower averages →
  [[concept_mean_reversion]]
- Prior highs and all-time highs as references →
  [[concept_support_resistance]]
- Size to stop distance, sell into vertical moves, rotate into cleaner
  bases → [[concept_position_sizing]], [[concept_trade_management]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/tg-capital-trident.md ===== -->

---
id: strategy_tg_capital_trident
type: strategy
title: "TG Capital — London Session Trident Strategy (forex, gold and futures, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Trident Pattern, TG Capital Trident, unique high RR, London session swing strategy, "1:20 RR strategy"]
taught_by: [person_tg_capital]
featured_in: [channel_chart_fanatics]
uses: [concept_trading_sessions_killzones, concept_fair_value_gap, concept_moving_averages, concept_multi_timeframe_analysis, concept_candlestick_patterns, concept_trend_following, concept_market_regimes, concept_trade_management, concept_risk_reward_r_multiples, concept_prop_firm_risk_rules]
derived_from: [concept_smart_money_concepts]
related: [strategy_nbb_trader_po3_ote_adr, strategy_jadecap_liquidity_volatility]
sources:
  - {title: "Chart Fanatics — TG's Capital London Session Swing Trading Strategy", url: "https://www.chartfanatics.com/strategies/unique-high-rr", tier: T2}
  - {title: "TradeZella — TG Capital London Session Strategy", url: "https://www.tradezella.com/strategies/unique-high-rr", tier: T3}
  - {title: "TradingView — TG Capital Trident Strategy [Long + Short] (third-party script)", url: "https://www.tradingview.com/script/nFdphVub-TG-Capital-Trident-Strategy-Long-Short/", tier: T3}
  - {title: "TakeProfit — Reverse-Engineering a Public 1:20 RR Strategy: Chart Fanatics & TG Capital", url: "https://takeprofit.com/posts/reverse-engineering-a-public-1-20-rr-strategy-chart-fanatics-tg-capital-51", tier: T3}
status: verified-t2
---

# TG Capital — London Session Trident Strategy (forex, gold and futures, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/unique-high-rr. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** According to the earlier search-based note (T3; not in the playbook), TG Capital is the trader in the Chart Fanatics video *"STEAL This INSANE Simple 90% Win Rate Trading Strategy (1:20+ RR)"*. The numbers in that title are T4. The playbook gives no biography.

## Built for

- **Instruments:** futures and forex.
  - Valid pairs: USDJPY, EURUSD, GBPUSD, NZDUSD, USDCAD and gold (XAUUSD).
  - The page says it is especially strong on gold and Nasdaq, and favours longs on naturally bullish assets, but the model works in both directions.
- **Style:** swing trading. Entries are intraday, and trades are held as long as the daily trend lasts.
- **Timeframes:** the 30-minute chart is the only chart used for entries. The daily chart sets bias and take-profit levels.
- **Session / time window:** the London kill zone, **3:00–6:30 AM New York time**. All entries must fall inside it. The FVG itself must form between **2:30 and 4:00 AM**.

## Core idea

The trader waits in a narrow London window for the "Trident" pattern, and only when trend filters agree. The pattern has three parts:

1. a clean 3-candle fair value gap on the 30-minute chart;
2. a small-bodied doji whose wick reaches the gap's 50% level (consequent encroachment);
3. a confirmation candle.

The filters are a 200 EMA directional bias and a clean 5/9/13(15)/21 EMA stack. The trade is then held for daily-chart trend continuation, aiming for a large reward relative to a tight stop. The page favours quality over quantity, and setups can be rare.

## Rules

1. **Bias.** Above the 200 EMA, longs only. Below it, shorts only. Daily structure must agree. A "Bull Trading Candle Strength" indicator on the daily chart confirms momentum: green is strong bullish, blue mild bullish, red strong bearish, black mild bearish.
2. **Trend filter.** The 5, 9, 13 (or 15) and 21 EMAs must be clearly stacked in the trade direction. If they cross or tangle, the setup is invalid.
3. **Time filter.** Only consider entries between 3:00 and 6:30 AM New York time.
4. **Fair value gap.** A clean 3-candle FVG must form on the 30-minute chart between 2:30 and 4:00 AM. Ignore FVGs outside the window.
5. **Mark the 50% level** of the FVG (consequent encroachment).
6. **Trident candle.** The next candle must be a small-bodied doji whose wick reaches into the 50% zone, showing that a push into the gap was rejected.
7. **Confirmation candle.** As written on the page, the candle after the doji must close *below* the doji high; a close above it invalidates the trade. (See the gaps section.)
8. **Entry.** Enter at market on the confirmation candle (the example entered right after it closed). If early, place a limit at the FVG's 50% level instead.
9. **Stop.** Below the low of the candle that forms the FVG. **Gold exception:** no hard stop. A closing-candle filter is used instead, because, according to the page's backtests, gold often makes deep liquidity wicks before running.
10. **Take profit.** Use daily structure to guide take-profit levels and ride the trend while it lasts.
11. **Early exit.** Consider closing if the EMAs start to reverse, or if a significant opposing candle invalidates the structure.

## Risk management

- **Stop:** below the FVG-candle low. Gold uses a close-based stop instead of a hard stop.
- **Risk per trade:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook. Exposure is limited by time instead: at most 3.5 hours of trading per day, and setups may come only a handful of times per year.
- **Prop-firm caveat:** the page says the model needs a fully balance-based prop-firm drawdown model. A hybrid or equity-based drawdown can end trades, because open P&L swings widely (for example +10R falling back to +5R).
- **Psychology:** you must be able to sit through long gaps between setups and through large open-profit swings.

## What the playbook leaves unspecified

- **EMA timeframe:** which timeframe the 200 EMA and the EMA stack are read on (30-minute or daily). The worked example doesn't say.
- **Internal inconsistencies:**
  - The FVG window starts at 2:30 AM, before the 3:00 AM kill zone opens.
  - For a long, the confirmation rule (close below the doji high, or the trade is invalid) reads as inverted relative to the bullish story it describes. It needs clarifying before any test.
- **Pattern definitions:** minimum FVG size, how small a doji's body must be, and how far into the 50% zone the wick must reach.
- **Indicator:** the formula behind the "Bull Trading Candle Strength" indicator.
- **Gold stop:** which timeframe's close triggers it, and the maximum loss allowed.
- **Exits:** no fixed R target. The 1:20 figure comes from the video title and third-party material, not the playbook. "Daily structure" exits aren't defined.
- **Other mechanics:** position limits (for example one trade at a time), short-side mirror details, risk per trade.

## Evidence & claims

- **Win rate:** about 90% "when all rules are followed". Self-reported (T4), on the T2 page.
- **Reward size:** described as high risk-to-reward, with open P&L swings such as +10R back to +5R. Self-reported (T4).
- **Kill-zone choice:** said to rest on years of backtesting. No data shown (T4).
- **Video title:** claims a 90% win rate at 1:20+ RR (T4).
  - Expectancy check: E = 0.9 × 20 − 0.1 = **+17.9R per trade**, which is implausible.
  - Even at 1:5, E = 0.9 × 5 − 0.1 = +4.4R.
  - Win rate and R:R that high almost never coexist.
- **Independent EA re-test** (TakeProfit, EURUSD M30, T3): about a **20% win rate** with many large winners, profitable out-of-sample in 2023–24. At a 20% win rate, break-even R:R is 4:1. This contradicts the 90% headline but is consistent with a positive-skew trend edge.
- **Third-party TradingView script** (T3): uses a 1:20 minimum target, exits if the EMA stack breaks or price closes through the stop, and holds one position at a time. These are that script's choices, not playbook rules.
- **Sample size:** only a handful of setups per year means a 90% win rate can't be verified from any realistic personal sample.

## Concepts & lineage

- London kill zone (3:00–6:30 AM NY) and FVG formation window: [[concept_trading_sessions_killzones]]
- 3-candle FVG and its 50% consequent encroachment: [[concept_fair_value_gap]]
- Doji "Trident" plus confirmation candle: [[concept_candlestick_patterns]]
- 200 EMA bias and 5/9/13(15)/21 EMA stack: [[concept_moving_averages]], [[concept_trend_following]]
- Tangled EMAs mean no trend, so no trade: [[concept_market_regimes]]
- 30-minute entries with daily bias and targets: [[concept_multi_timeframe_analysis]]
- Holding winners for large R, and EMA-reversal exits: [[concept_trade_management]], [[concept_risk_reward_r_multiples]]
- Balance-based vs equity-based prop drawdown rules: [[concept_prop_firm_risk_rules]]
- The FVG and kill-zone vocabulary comes from ICT / smart-money concepts: [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **Confirmed:**
  - the London kill zone of 3:00–6:30 AM New York time;
  - daily bias and targets with 30-minute entries;
  - the 5/9/13(15)/21 EMA stack, invalid when tangled;
  - the Trident definition (FVG + doji wick into its midpoint + confirmation candle).
- **Added:** the 200 EMA long-only/short-only filter, the daily candle-strength indicator, the 2:30–4:00 AM FVG window, the confirmation-candle rule as written, entry options (market on confirmation, or a limit at 50%), the stop below the FVG-candle low, the gold no-hard-stop exception, the valid-pairs list, and the prop-firm drawdown caveat.
- **Corrected:** the earlier note's 1:20 minimum R:R came from a third-party script and the video title (T3/T4). **The playbook states no fixed R:R.** The playbook's exits are daily-structure targets, plus early exits on EMA reversal or a significant opposing candle.
- **New on the T2 page:** the about-90% win rate now appears on the page itself, not just in the video title. It is still a self-reported claim (T4).
- **Cleanup:**
  - `related` had held concept ids (`concept_backtesting`, `concept_overfitting_validation`); it now lists strategy ids only.
  - The empty `validates` and `challenges` keys were dropped.
  - All earlier sources are kept, including the independent re-test.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/tori-trendline-4h.md ===== -->

---
id: strategy_tori_trendline_4h
type: strategy
title: "Tori Trades — Trendline Trading Playbook: Action Line and Safety Line (stocks, futures and forex, 4H swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Tori's trendline playbook", Tori Trades strategy, Action Line and Safety Line, 4H trendline bounce and break]
taught_by: [person_tori_trades]
featured_in: [channel_chart_fanatics]
uses: [concept_trendlines, concept_price_action, concept_market_structure, concept_support_resistance, concept_breakout_trading, concept_trend_following, concept_multi_timeframe_analysis, concept_trade_management, concept_trading_journal_review]
derived_from: [concept_trendlines, concept_price_action]
related: [strategy_marci_silfrain_measured_move, strategy_ali_crooks_trendline_pocket]
sources:
  - {title: "Chart Fanatics — Tori’s Trendline Trading Playbook", url: "https://www.chartfanatics.com/strategies/trendline-strategy", tier: T2}
  - {title: "Chart Fanatics — Tori's Trendline Trading Playbook", url: "https://www.chartfanatics.com/playbook/trendline-strategy", tier: T2}
status: verified-t2
---

# Tori Trades — Trendline Trading Playbook: Action Line and Safety Line (stocks, futures and forex, 4H swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/trendline-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Tori Trades swing trades with hand-drawn trendlines and price
structure only, with no indicators. The playbook gives no further
biography.

## Built for

- **Instruments:** stocks, futures and forex. The examples are platinum
  and crude oil. It works best on instruments that consistently respect
  trendlines; the page names certain strongly trending commodities and
  metals as suitable.
- **Style:** swing trading. Setups can take days or weeks to appear.
- **Timeframes:** the **4-hour** chart for drawing lines, finding
  touchpoints and planning entries and exits. A top-down check on the
  **daily or weekly** confirms the main trend.
- **Session or time window:** not specified.
- **Tools:** trendlines and price structure only.

## Core idea

Price often respects trendlines: it either bounces off them or breaks
through them to signal a change of trend. Every trade has two lines. The
**Action Line** is where you enter: the line that holds for a bounce, or
the line that breaks for a break trade. The **Safety Line** is where you
exit if wrong. For a bounce it is the same line. For a break it is a new,
opposing trendline. The distance from entry to the Safety Line is the
trade's risk, and the Safety Line is trailed as structure develops.

## Rules

1. **Top-down bias.** Confirm the main trend on the daily or weekly, then
   work on the 4-hour chart.
2. **Pick suitable instruments.** Favour markets that consistently respect
   trendlines (certain commodities and metals). Avoid those that throw
   frequent false breaks. Ranging markets give few valid trades.
3. **Trendline Bounce (with trend).**
   - *Setup:* the line has at least **two or three clear touchpoints**,
     and **at least one week of price data** runs from the first touch to
     the planned entry.
   - *Entry:* when price reaches or tests the line. In the platinum
     example, the long was opened at the third touch of a rising
     trendline.
   - *Stop:* the same line is the Safety Line. **A close through the line
     ends the trade at once.** Leave enough room that normal wicks do not
     stop you out; do not set the stop right at entry.
   - *Management:* trail the stop along the trendline, below each new
     valid swing low in an uptrend.
   - The page calls this the lowest-risk setup, because invalidation is
     immediate.
4. **Trendline Break (reversal), 2-touch version.**
   - *Setup:* the Action Line has **exactly two clear touchpoints**, and
     about **one week of 4-hour data** runs from the first touch to the
     break.
   - *Safety Line:* draw an opposing trendline. If none exists at the
     break, **wait** until price forms a clear high or low to draw one.
   - *Entry:* on a break and **close** through the Action Line, with a
     clear Safety Line in place. The break must happen **close to the
     Safety Line** so risk stays tight. If it is too far, skip it.
   - *Stop:* the Safety Line. A close back beyond it ends the trade.
     Move it by hand as new structure forms.
   - The page says this version gives more trades but can produce bigger
     losses.
5. **Trendline Break (reversal), 3-touch version.** The same as the 2-touch
   version, except the Action Line needs **three or more** clear
   touchpoints and **at least one week** of 4-hour data before the break.
   The page treats more touches as a more reliable break. Trail the Safety
   Line as price makes new highs or lows.
6. **Adding.** In the 2-touch platinum example, positions were added as
   the trend continued in the trade's favour.
7. **Exit.** No profit target is given in the playbook. The only exit
   described is a close through the Safety Line, which is trailed to lock
   in profit.
8. **Record-keeping.** Log 2-touch breaks **separately** from 3-touch
   breaks.

## Risk management

- **Risk per trade:** defined by the distance from entry to the Safety
  Line. Skip break trades where that distance is too large.
- **Stop rule:** a **close** through the Safety Line (the trendline for
  bounces, the opposing line for breaks), not an intraday touch. Leave room
  for normal wicks.
- **Trailing:** move the stop along the trendline or Safety Line as new
  swing points form.
- **Capital:** some futures contracts need enough capital to trade.
- **Account risk in $ or %, position size, maximum positions, daily or
  weekly limits:** not specified in the playbook.

## What the playbook leaves unspecified

- How close is "close to the Safety Line". There is no maximum stop
  distance in points, percentage or ATR.
- What counts as a "clear touchpoint": how near price must come, and
  whether wicks or closes count.
- For bounces, whether to enter on a touch, a limit order at the line, or
  a confirmation candle. The page says "reaches or tests" and admits
  timing takes discretion.
- How much buffer to give the stop beyond the line.
- Whether there are profit targets or partials, beyond trailing and
  adding.
- Rules for adding to a position: how much, and where the combined stop
  sits.
- Whether the bounce needs "two or three" touches as a minimum, given that
  the platinum example entered on the third touch.
- How the daily or weekly trend must align with a counter-trend break
  setup.

## Evidence & claims

- The page gives **no win rate, R:R, P&L or payout**. No expectancy check is
  possible.
- The pros say the method is repeatable and "can be backed by real data",
  but no data is shown. Self-reported (T4).
- The page notes that more touches make a break **more reliable**, which is
  qualitative. It also admits that fake-outs and losses are part of the
  system.
- The examples (platinum bounce, platinum 2-touch break, crude oil 3-touch
  break) give no prices or results.

## Concepts & lineage

- Hand-drawn trendlines with touch counts, and Action and Safety lines →
  [[concept_trendlines]]
- No-indicator reading of swings, wicks and closes →
  [[concept_price_action]]
- Swing highs and lows used to trail and to draw the opposing Safety Line
  → [[concept_market_structure]], [[concept_support_resistance]]
- Bounce entries with the trend → [[concept_trend_following]]
- A close through the line as a reversal entry →
  [[concept_breakout_trading]]
- Daily or weekly trend check, with 4-hour execution →
  [[concept_multi_timeframe_analysis]]
- Trailing along the line and adding as the trend extends →
  [[concept_trade_management]]
- Logging 2-touch and 3-touch breaks separately →
  [[concept_trading_journal_review]]

## Changes vs. earlier note

- **Status upgraded.** The earlier note was `partial`, with touch count,
  entry trigger, stop and target marked "pending scrape". All of these are
  now captured from the playbook (T2).
- **Confirmed:** swing trading on the **4-hour** chart using trendlines and
  no indicators.
- **Added:** instruments (stocks, futures, forex, with commodity and metal
  examples), the daily or weekly top-down check, the Action Line and
  Safety Line framework, the bounce setup (2 to 3 touches, one week of
  data, close-through exit), the 2-touch and 3-touch break setups (an
  opposing Safety Line, a break close to it, skip if far), trailing,
  adding, the trailed Safety Line as the only described exit, and logging 2-touch and 3-touch breaks
  separately.
- **Targets clarified.** The earlier note listed the target as unknown.
  The playbook still gives **no profit target**; the only exit it describes
  is a close through the trailed Safety Line.
- **Sources.** The earlier note cited the page at `/playbook/trendline-strategy`.
  The scraped page lives at `/strategies/trendline-strategy`, which is now
  listed first. The old entry is kept unchanged after it.
- **Graph fields.** `derived_from` was added (trendlines, price action),
  and `related` now includes Ali Crooks' trendline-break pocket.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/trader-kane-lab-model.md ===== -->

---
id: strategy_trader_kane_lab_model
type: strategy
title: "Trader Kane — 50% Reversal with SMT Divergence & PO3 (NQ/ES futures and crypto, scalping/day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: ["Trader Kane’s 50% Reversal Strategy", "SMT Divergence + PO3", Lab Model, Trader Kane strategy]
taught_by: [person_trader_kane]
featured_in: [channel_chart_fanatics]
uses: [concept_smt_divergence, concept_amd_power_of_three, concept_premium_discount_ote, concept_fair_value_gap, concept_liquidity_sweep_reversal, concept_multi_timeframe_analysis, concept_trading_sessions_killzones, concept_trade_management, concept_smart_money_concepts]
derived_from: [concept_smart_money_concepts, concept_amd_power_of_three]
related: [strategy_candace_lau_nq_sweep_reversal, strategy_tanja_amd_futures, strategy_nbb_trader_po3_ote_adr]
sources:
  - {title: "Chart Fanatics — Trader Kane’s 50% Reversal Strategy", url: "https://www.chartfanatics.com/strategies/smt-divergence-po3", tier: T2}
  - {title: "PickMyTrade — Trader Kane Strategy: The Lab Model NQ Trading System Explained", url: "https://blog.pickmytrade.trade/trader-kane-strategy-the-lab-model-nq-trading-system-explained/", tier: T3}
  - {title: "Scribd — Trader Kane's Chart Fanatics Strategy", url: "https://es.scribd.com/document/876819803/Chart-Fanatics-Kane-1", tier: T3}
status: verified-t2
---

# Trader Kane — 50% Reversal with SMT Divergence & PO3 (NQ/ES futures and crypto, scalping/day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/smt-divergence-po3. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Trader Kane is an NQ futures day trader and co-founder of The
Lab education community (per the earlier note, T3). Do not confuse him
with Kane Trading (kanetrading.com), a separate Fibonacci and ABCD site.

## Built for

- **Instruments:** crypto and futures. The SMT read compares **NQ with
  ES**.
- **Style:** scalping and day trading. The aim is consistent "base hits",
  not full trend moves.
- **Timeframes:** Daily, then 4H, then 1H for bias, then an intraday chart
  for entry (the example executes on the **3-minute**).
- **Time window:** manipulation usually comes around **10:00 AM EST**. The
  example moves to breakeven on the **11:00 AM** hourly candle, and trades
  are often finished before midday. The page says the model also works on
  higher timeframes.

## Core idea

Price often returns to the **50% level** of an earlier range before the
broader trend continues. The model frames market behaviour with the **Power of
Three**: accumulation (a range), manipulation (a sweep of a key high or
low) and distribution (delivery back into the 50% area). When Daily, 4H and
1H all line up around a key 50% level, the trader waits for a sweep at the
key time. **SMT divergence** confirms it, with NQ and ES failing to make
the same high or low. A break of an **inversion zone** then gives the
trigger, and the trade targets only the move back to the 50% level.

## Rules

1. **Daily bias.** Mark the previous day's high and low and the swing high
   and low, then find the **50% midpoint** of the large range. That sets
   the bias and the target area.
2. **4H check.** Find the midpoint of recent swings and look for PO3
   structure. Has a recent high or low been swept?
3. **1H alignment.** The 1H should agree with the Daily and 4H and show
   its own PO3, often with a reversal wick around 10:00 AM. SMT usually
   becomes visible on this timeframe.
4. **Wait for manipulation at the key time** (around 10:00 AM EST): a sweep
   above a prior high for a bearish setup, or below a prior low for a
   bullish one.
5. **Confirm with SMT.** One index makes the new extreme and the other does
   not (for example, NQ makes a new high while ES does not). This signals
   the manipulation may be over.
6. **Find the inversion zone.** After the manipulation, look for a reaction
   at an earlier imbalance or inversion zone, meaning old support now
   acting as resistance or the reverse. Wait for price to break down
   through it or reject it.
7. **Entry.** A breakdown candle closes beyond the inversion zone. Then
   either place a **sell stop under the breakdown candle** or a **limit on
   the retest** of the zone (mirror for longs). In the example, the entry
   was a sell stop on the 3-minute chart.
8. **Stop.** Just beyond the **SMT extreme**: above the SMT high for
   shorts, below the SMT low for longs.
9. **Target.** The **50% level** of the impulse or dealing range (the H1
   dealing range in the example). This is the base hit. Do not aim for the
   full move unless momentum is unusually strong.
10. **Manage.** As soon as the trade moves your way and confirms, **move
    the stop to breakeven**. In the example, the trigger was the 11:00 AM
    hourly candle turning bearish. If price climbs back past the
    manipulation candle's high or low, you are probably wrong and should
    be out.

## Risk management

- **Stop:** structural, just beyond the SMT high or low.
- **Breakeven rule:** strict and early. The page admits it causes a **high
  break-even rate**, with many trades closing flat.
- **Exit if wrong:** when price returns past the manipulation candle's
  extreme.
- **Risk per trade (% or $), position size:** not specified in the
  playbook.
- **Daily or weekly limits, maximum number of trades:** not specified in
  the playbook.

## What the playbook leaves unspecified

- Which swing defines the daily "large range" and the "dealing range" whose
  50% is the target.
- How "around 10:00 AM" is bounded: the earliest and latest valid time for
  the manipulation.
- What counts as an inversion zone, for example whether it means an
  inverted FVG specifically or any flipped support or resistance.
- An objective trigger for "confirms" before moving to breakeven, beyond
  the single 11:00 AM candle example.
- Which instrument is traded when NQ and ES diverge (the one that swept, or
  the other), and how the setup carries over to crypto, where no NQ/ES SMT
  pair exists.
- Position sizing, risk per trade and daily loss rules.

## Evidence & claims

- The playbook page makes **no win-rate, R:R, P&L or payout claim**. Its
  pros are qualitative: entries near the high or low of the day, setups
  described as high-probability and high-confluence, quick trades.
  Self-reported (T4).
- **From the earlier note:** his Chart Fanatics episode is billed "$2M+"
  (T4 marketing figure, unverified).
- No expectancy check is possible. The admitted high break-even rate means
  any real test should log breakeven exits as their own outcome.

## Concepts & lineage

- NQ against ES failure to confirm a new extreme →
  [[concept_smt_divergence]]
- Accumulation, manipulation, distribution on 4H and 1H →
  [[concept_amd_power_of_three]]
- The 50% midpoint of the range as target, and premium-zone rejection →
  [[concept_premium_discount_ote]]
- Inversion zone and earlier imbalance as the trigger area →
  [[concept_fair_value_gap]]
- A sweep of a prior high or low, then reversal →
  [[concept_liquidity_sweep_reversal]]
- Daily, 4H and 1H bias with a 3-minute execution →
  [[concept_multi_timeframe_analysis]]
- The 10:00 AM manipulation window and 11:00 AM breakeven check →
  [[concept_trading_sessions_killzones]]
- Early breakeven, base-hit exits → [[concept_trade_management]]
- Lineage: ICT-style smart-money framework → [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **First-person rulebook now exists.** The earlier note said there was no
  public first-person rulebook and that every mechanical version was a T3
  reconstruction. The Chart Fanatics playbook now provides the rules at
  T2.
- **Name.** The page calls the method **"Trader Kane's 50% Reversal
  Strategy"** (URL slug `smt-divergence-po3`) and never says "Lab Model".
  That label comes only from the earlier T3 sources and is kept as an alias.
- **Timing anchor, corrected.** The earlier note made the 10:00 AM ET
  **four-hour candle** the timing anchor (T3). The playbook places the
  manipulation **around 10:00 AM EST**, read on the **1H**, often as a
  wick. The 4H is used for PO3 and swing midpoints, and the 11:00 AM hourly
  candle triggers breakeven. The "10 AM 4H anchor" wording is dropped from
  the title.
- **Instrument scope, corrected.** The earlier note said NQ-only execution
  with ES as the SMT reference (T3). The playbook lists **crypto and
  futures**, uses NQ and ES for SMT, and does not limit execution to NQ.
- **Confirmed:** SMT divergence, inversion zones, premium and discount,
  and aggressive breakeven management. The playbook adds that this
  produces a high break-even rate.
- **Added:** the 50% level as the core target, top-down Daily, 4H and 1H
  PO3 alignment, the entry mechanics (sell stop under the breakdown candle,
  or a limit on the retest), the stop beyond the SMT extreme, and the
  manipulation-candle exit.
- **Added `uses`:** AMD/PO3, liquidity sweep reversal and multi-timeframe
  analysis.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/trader-mayne-structure-ote.md ===== -->

---
id: strategy_trader_mayne_structure_ote
type: strategy
title: "Trader Mayne — Structure + OTE: HTF Break, POI Pullback & LTF Breaker Entry (forex/futures/crypto, swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Structure + OTE Playbook, Structure OTE, Trader Mayne strategy, Structure + OTE Swing Playbook]
taught_by: [person_trader_mayne]
featured_in: [channel_chart_fanatics]
uses: [concept_market_structure, concept_order_blocks_breakers, concept_fair_value_gap, concept_premium_discount_ote, concept_liquidity, concept_liquidity_sweep_reversal, concept_multi_timeframe_analysis, concept_trend_following, concept_risk_reward_r_multiples, concept_position_sizing]
derived_from: [concept_smart_money_concepts]
related: [strategy_marci_silfrain_measured_move, strategy_nbb_trader_po3_ote_adr]
sources:
  - {title: "Chart Fanatics — Structure + OTE Playbook", url: "https://www.chartfanatics.com/strategies/structure-ote", tier: T2}
  - {title: "TradeZella — Structure + OTE", url: "https://www.tradezella.com/strategies/structure-ote", tier: T3}
status: verified-t2
---

# Trader Mayne — Structure + OTE: HTF Break, POI Pullback & LTF Breaker Entry (forex/futures/crypto, swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/structure-ote. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Trader Mayne teaches this top-down swing framework for crypto,
forex and futures. The page notes he also has a seven-lesson crypto
masterclass on Chart Academy.

## Built for

- **Instruments:** forex, futures and crypto. The pros list adds
  commodities. Both worked examples are crypto (Bitcoin and Solana).
- **Style:** swing trading.
- **Timeframes:** two timeframes. **HTF** (weekly, daily, H12 or H4) for
  trend, bias and range. **LTF** (H1, M15 or M5) for the entry. Suggested
  pairs: **Daily → H1** and **H4 → M15**. The examples use 1D → 30m and
  Weekly → H12.
- **Session:** not specified. The page says the method scales across
  markets and timeframes.

## Core idea

Price moves in swings. After a clean higher-timeframe break of structure,
price often pulls back into the zone that caused the break, the **point of
interest (POI)**. That is where the next higher low (uptrend) or lower high
(downtrend) is expected to form. Mark the POI and the premium/discount
split of the new range. When price returns to the POI, drop to the lower
timeframe and wait for a **breaker setup**: engineered liquidity, a stop
run, then a structure break the other way. Enter on the breaker, put the
stop beyond the swept extreme, and target the next higher-timeframe
external liquidity. Every condition must be present for the setup to be
valid.

## Rules

1. **Pick the timeframe pair:** an HTF from weekly, daily, H12 or H4, and
   an LTF from H1, M15 or M5.
2. **Define the HTF trend.** Use swing structure, and require a **clear
   market structure break (MSB)** that sets up a new trading range.
3. **Mark the HTF range.** In an uptrend, from the last significant swing
   low to the new swing high. In a downtrend, from swing high to swing low.
   Draw the **50% line**: buy only in the discount (lower half) of an
   uptrend, and sell only in the premium (upper half) of a downtrend.
4. **Mark the POI on the HTF.** This is the zone that caused the break: an
   **order block** (in the examples, the last opposite-colour candle before
   the breaking move), or a **breaker block** or **fair value gap**.
5. **Wait for the pullback into the POI,** ideally inside the correct half
   of the range.
6. **LTF breaker setup inside the POI.** All three are needed:
   - engineered liquidity: a swing low (for longs) or swing high (for
     shorts) forming inside the zone;
   - a stop run that sweeps that liquidity;
   - a market structure break in the opposite direction.
7. **Entry:** on the breaker block after the LTF MSB. In both examples,
   entry came on the retest.
8. **Stop:** below the swept low (longs) or above the swept high (shorts).
9. **Target:** the next **HTF external liquidity**: the prior swing high
   on a long, the prior swing low on a short.
10. **R:R filter:** take the setup only if it offers **at least 2:1**.
11. **Size:** adjust dynamically with confidence and confluence.

## Risk management

- **Minimum reward-to-risk:** 2:1. Setups below that are skipped.
- **Invalidation:** beyond the low or high that was swept on the LTF.
- **Sizing:** varies with confidence and confluence. No base risk is
  given.
- **Risk per trade ($ or %):** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.
- **Trade management** (break-even, partials, trailing): Not specified in
  the playbook.

## What the playbook leaves unspecified

- What makes a market structure break "clean" (a body close or a wick, and
  how far beyond the swing).
- Which "last significant" swing anchors the range when several qualify.
- How to choose between an order block, breaker or FVG when more than one
  POI sits in the pullback path.
- Despite the name, **no OTE Fibonacci levels** (such as 0.62–0.79) are
  given. The only location filter is the 50% premium/discount split.
- How much engineered liquidity is enough, and how the LTF MSB is
  measured.
- Any management after entry: break-even, partials or trailing.
- How size changes with confluence, and from what base risk.
- What to do if price runs through the POI without an LTF setup.
- Trade frequency and holding period.

## Evidence & claims

- **Bitcoin short (1D HTF, 30m LTF):** bearish MSB, entry in a bearish
  order block in premium after a 30m swing-high sweep, stop above the swept
  high. The page says it reached the target (the next HTF lower low) with
  a large bearish FVG on the way. Self-reported (T4). No R figure is given.
- **Solana long (weekly HTF, H12 LTF):** bullish MSB, entry in a bullish
  order block in discount after several H12 lows built up and the last one
  was swept. The page says price rallied back to its all-time high, the
  target. Self-reported (T4). No R figure is given.
- The page reports **no win rate or P&L**. The 2:1 minimum is a filter,
  not a result; by simple arithmetic (not on the page), the break-even win
  rate at 2:1 is about 33%. No expectancy check is possible.
- The earlier note's TradeZella source (T3) is kept. The earlier note
  recorded no independent test or result from it.
- The page's own cons: entries need discretion around breakers and
  confirmation, the method needs backtesting and live practice, and
  traders must adapt it to their own style.

## Concepts & lineage

- HTF swing structure, MSB and the new range →
  [[concept_market_structure]]
- Trading pullbacks in the direction of the HTF trend →
  [[concept_trend_following]]
- 50% premium/discount split of the range →
  [[concept_premium_discount_ote]]
- Order blocks and breaker blocks as POIs; the LTF breaker entry →
  [[concept_order_blocks_breakers]]
- FVG as an alternative POI → [[concept_fair_value_gap]]
- Engineered liquidity inside the POI and HTF external liquidity as the
  target → [[concept_liquidity]]
- Stop run, then a structure break the other way →
  [[concept_liquidity_sweep_reversal]]
- HTF and LTF pairing → [[concept_multi_timeframe_analysis]]
- Minimum 2:1 → [[concept_risk_reward_r_multiples]]
- Size scaled by confidence and confluence → [[concept_position_sizing]]
- Lineage: smart-money concepts (the page refers to "smart money"; the
  ICT-style label is our attribution) → [[concept_smart_money_concepts]]

## Changes vs. earlier note

- **Status:** upgraded from `synthesized` to `verified-t2` against the
  Chart Fanatics page text.
- **Confirmed:** the earlier workflow. That means a clean HTF structure
  break, a POI that is an order block or breaker, a pullback into it, an
  LTF breaker setup (a failed move that sweeps liquidity and reclaims
  structure), and a stop beyond the sweep.
- **Corrected, location filter:** the earlier note said the pullback should
  ideally land "inside the OTE band". The playbook gives no OTE Fibonacci
  levels. The location rule is the **50% midpoint** of the HTF range:
  discount for longs, premium for shorts.
- **Corrected, target:** the earlier note said only "target in the HTF
  trend direction". The playbook names the **next HTF external liquidity**,
  the previous swing high or low.
- **Expanded, timeframes:** the earlier note said HTF daily or weekly. The
  playbook allows weekly, daily, H12 or H4 for HTF and H1, M15 or M5 for
  LTF, suggesting Daily → H1 and H4 → M15 pairs.
- **Added:** FVG as a third POI type; the 50% range line; a minimum 2:1
  R:R; sizing by confidence and confluence; the rule that every condition
  must be met; and the Bitcoin and Solana examples.
- **Added `uses`:** FVG, sweep reversal, R-multiples and position sizing.
  Added NBB Trader's PO3/OTE note to `related` for its breaker and OTE
  mechanics.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/traveling-trader-universal.md ===== -->

---
id: strategy_traveling_trader_universal
type: strategy
title: "Traveling Trader — Universal Trading Strategy (stocks/options/futures/forex, scalping to swing trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Universal Playbook, universal strategy, liquidity catalyst displacement retracement, The Traveling Trader strategy]
taught_by: [person_traveling_trader]
featured_in: [channel_chart_fanatics]
uses: [concept_liquidity, concept_liquidity_sweep_reversal, concept_market_structure, concept_support_resistance, concept_trendlines, concept_fair_value_gap, concept_order_blocks_breakers, concept_moving_averages, concept_divergence, concept_multi_timeframe_analysis, concept_fundamental_macro_analysis, concept_price_action, concept_trade_management]
derived_from: [concept_smart_money_concepts, concept_price_action]
related: [strategy_vincent_desiano_break_retest, strategy_trader_mayne_structure_ote, strategy_marco_trades_liquidity_grab, strategy_tori_trendline_4h]
sources:
  - {title: "Chart Fanatics — Universal Trading Strategy by The Traveling Trader", url: "https://www.chartfanatics.com/strategies/universal-strategy", tier: T2}
status: verified-t2
---

# Traveling Trader — Universal Trading Strategy (stocks/options/futures/forex, scalping to swing trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/universal-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook is credited to The Traveling Trader and gives no biography. It does discuss options trading directly, warning against stops or targets based on option premium.

## Built for

- **Instruments:** stocks, options, futures and forex according to the page header. The overview also mentions crypto.
- **Style:** scalping, day trading and swing trading. The page lists separate pros and cons for swing and day use.
- **Timeframes:** any. The page stresses higher-timeframe context, because lower-timeframe setups without it often fail.
- **Session / time window:** not specified.

## Core idea

A trade is valid only when it tells a clear, logical "story" in three parts:

1. A **liquidity catalyst**: the market interacts meaningfully with a major level and changes behaviour.
2. **Displacement**: a decisive move away from that level, which shows the interaction mattered.
3. A **retracement** into a logical area, where the entry is actually taken.

The first impulse is treated as a reaction, not an entry. Waiting for the pullback gives a controlled stop, clear invalidation and better reward-to-risk. Targets follow the same story: markets move from one liquidity pool to the next.

## Rules

1. **Map liquidity and context.** Mark major support and resistance, equal highs and lows, well-respected trendlines, the trend's prior swing high or low, and significant levels. Note higher-timeframe direction and any macro, seasonal or news backdrop. While the market moves quietly with no catalyst, there is no trade.
2. **Require a liquidity catalyst.** Any one of these counts:
   - a sweep of equal highs or lows;
   - a break of a major support or resistance zone;
   - a break of a well-respected trendline;
   - a market-structure shift (breaking the trend's prior high or low);
   - a sharp rejection from a significant level.
3. **Require displacement.** There must be clear follow-through: a decisive move, a visible change in price behaviour, and a break of the prior swing structure. Without that reaction, the story is incomplete.
4. **Require confluence.** Never trade a single signal. Supporting factors can include:
   - key support or resistance, a structure shift, a trendline break;
   - divergence;
   - higher-timeframe alignment;
   - macro conditions, seasonality or significant news.
5. **Enter only on the retracement.** Valid zones are a broken support or resistance level, a trendline retest, a fair value gap, an order block, a previous swing level, or a moving average acting as dynamic support or resistance. Never enter during the first impulse. If price never pulls back, the setup doesn't qualify. Don't chase, and don't move the entry because of FOMO.
6. **Stop beyond the level that proves the story wrong.** Stops are set by price structure only. No wide stops out of fear, no arbitrary "breathing room", and no stops based on option pricing. Exit without hesitation if that level breaks.
7. **Targets follow the narrative:** liquidity pools, prior highs and lows, imbalance fills, and areas where traders are trapped or forced to act.
8. **Manage by the story, not by emotion.** Let the move play out, and exit when the narrative says it's complete, not early to "protect" profit. For options, base the stop and target on the underlying chart, not the premium.

*Worked example (S&P 500, short).* In a post-election uptrend, price broke the trendline that had acted as support. The catalyst was then confirmed by bearish follow-through and the loss of the latest higher low. Price retraced to the broken trendline, which lined up with the 21 EMA. The short was taken there. The trade was invalid if price reclaimed the trendline and held above the 21 EMA. Targets were prior internal lows and lower liquidity.

## Risk management

- **Invalidation:** the structural level beyond which the story fails. The stop is defined by price structure and nothing else.
- **Risk per trade:** Not specified in the playbook.
- **Sizing:** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.
- **Swing-trade risks acknowledged:** overnight gaps can open beyond the stop. Greeks, implied volatility and time decay distort option P&L. Macro headlines can disrupt a technically valid story.
- **Day-trade risks acknowledged:** mistakes compound quickly within a session, and fast markets raise the risk of panic exits, revenge trades and overtrading.

## What the playbook leaves unspecified

- Objective measures of "displacement" and "decisive" follow-through, such as range or volume multiples.
- How many confluence factors are enough, and which timeframes to pair for the catalyst versus the entry.
- How deep a retracement must go, for example how far into a fair value gap, and which order type to use.
- Moving-average lengths (only the 21 EMA appears, in the example).
- Partial exits, trailing, and how to tell when "the narrative says the move is complete".
- Risk per trade, position sizing, R targets, trade frequency, and option strike or expiry selection.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- The S&P 500 example is descriptive only, with no prices or outcome (T4).
- The claim that the playbook works on any market and timeframe is a design assertion, not a tested result (T4).

## Concepts & lineage

- Liquidity levels (equal highs and lows, major levels) as the catalyst: [[concept_liquidity]], [[concept_liquidity_sweep_reversal]]
- Market-structure shifts and breaks of the prior swing: [[concept_market_structure]]
- Support/resistance and trendline breaks and retests: [[concept_support_resistance]], [[concept_trendlines]]
- Retracement entries into fair value gaps and order blocks: [[concept_fair_value_gap]], [[concept_order_blocks_breakers]]
- Moving averages (21 EMA in the example) as dynamic support or resistance: [[concept_moving_averages]]
- Divergence and higher-timeframe alignment as confluence: [[concept_divergence]], [[concept_multi_timeframe_analysis]]
- Macro conditions, seasonality and news as fundamental confluence: [[concept_fundamental_macro_analysis]]
- Story-driven targets at the next liquidity pool, with structure-only stops: [[concept_trade_management]], [[concept_price_action]]
- The catalyst, displacement, retracement vocabulary (with FVG and order-block entries) parallels smart-money concepts. This is an editorial link; the page itself doesn't name SMC or ICT: [[concept_smart_money_concepts]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/umar-ashraf-5-stage.md ===== -->

---
id: strategy_umar_ashraf_5_stage
type: strategy
title: "Umar Ashraf — 5-Stage Trader Development Framework (any market, trader development)"
partition: 01_chart-fanatics
layer: L7
aliases: [5 stage trading framework, Umar Ashraf framework, five stages of a trader, novice to pro framework]
taught_by: [person_umar_ashraf]
featured_in: [channel_chart_fanatics, podcast_words_of_rizdom]
uses: [concept_trading_plan, concept_trading_journal_review, concept_trading_psychology, concept_position_sizing, concept_performance_metrics, concept_edge]
derived_from: []
related: [strategy_jeff_holden_momentum_model, strategy_jared_tendler_psychology]
sources:
  - {title: "Chart Fanatics — Umar Ashraf 5-Stage Trader Framework", url: "https://www.chartfanatics.com/strategies/5-stage-trading-framework", tier: T2}
  - {title: "TradeZella — 5 stage trading framework", url: "https://www.tradezella.com/strategies/5-stage-trading-framework", tier: T3}
status: verified-t2
---

# Umar Ashraf — 5-Stage Trader Development Framework (any market, trader development)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/5-stage-trading-framework. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Chart Fanatics credits this framework to Umar Ashraf; the page gives no biography. The earlier note's description of him as founder of Stock Market Lab is not in the playbook (third-party, T3, unverified). This page is a framework for trader development, not an entry setup.

## Built for

- **Instruments / markets:** not specified. The framework is market-agnostic.
- **Style:** not specified. Stage 1 mentions being at your desk an hour before the market opens, which implies active intraday trading, but no style is named.
- **Timeframes / sessions:** not specified.
- **Audience:** traders at every level. The page calls it a "mirror" for honest self-assessment, not only a beginner's map.

## Core idea

Every trader goes through five stages: Novice, Developing, Intermediate, Advanced and Pro. Stages can't be skipped or faked. Each one has a purpose, a set of tasks and typical traps. The goal is a repeatable process, and money is treated as a by-product. Early struggles usually come from missing strategy, risk management and structure rather than from psychology. Psychology starts to matter in Stage 3 and later, once real size and consistency are at stake. Position size grows only stage by stage.

## Rules

1. **Accept the foundational principles first.**
   - Trading is hard.
   - The goal is not to make X dollars but to build a repeatable process.
   - Control what you can: what you trade, how much you risk, how well you execute.
   - There is no "aha" moment; one green month doesn't mean you've figured it out.
   - Psychology is overrated early. If emotions take over, you're trading too big.
2. **Diagnose your current stage honestly.** Then do the work that stage requires.
3. **Stage 1: Novice (about 2–4 weeks of daily work).**
   - Observe price action and start trade notes and a journal.
   - Set cut-off rules, for example being at your desk an hour before the market opens.
   - Keep risk extremely low.
   - Expect to make mistakes, and aim for a repeatable process rather than being right.
4. **Stage 2: Developing (a few weeks more; Stages 1 and 2 together about 4–6 weeks).**
   - Apply the Stage 1 structure live at small size.
   - Track the setups you think may be your edge.
   - Collect data: win rate, performance by setup, time of day.
   - Journal and review daily. Keep strict risk controls and don't size up.
5. **Stage 3: Intermediate (often the longest and hardest; months or years).**
   - Narrow to **1–2 main setups**.
   - Write their rules, context and invalidation in a playbook.
   - Cut every trade outside the plan, even ones that work.
   - Critically review each trade for plan adherence and risk handling.
   - Tighten the routine: premarket prep, execution plan, post-market journal.
6. **Stage 4: Advanced (can last a year or more).**
   - Increase size **gradually and only on your best setups**.
   - Follow the playbook strictly, with no random trades.
   - Use journal data only for small refinements.
   - Track consistency week over week, judging execution rather than outcome.
7. **Stage 5: Pro.**
   - Trade proven setups at full size with full conviction.
   - Focus on long-term consistency.
   - Make only small adjustments, and track performance across market conditions so you can adapt.
   - Handle drawdowns without panic.
8. **At every stage:** journaling is mandatory, simple systems work best, trade quality drives the result, and execution is everything.

## Risk management

- **Risk per trade:** Not specified as a number. Risk is staged instead: extremely low in Stage 1, strict and small in Stage 2, gradual increases on the best setups only in Stage 4, full size in Stage 5.
- **Emotion check:** feeling overwhelmed by emotion means the size is too high.
- **Common sizing traps named:** scaling too soon or too aggressively (Stages 2–4), and revenge trading or forcing trades after a loss (Stage 4).
- **Daily / weekly limits:** Not specified in the playbook.
- **Invalidation:** each setup's invalidation must be written into the playbook (Stage 3). No values are given.

## What the playbook leaves unspecified

- Objective criteria for moving to the next stage, such as sample size, win rate, expectancy, drawdown or consistency thresholds.
- How much to increase size, and how fast, in Stage 4.
- Whether Stage 1 or 2 should use simulated or live trading. Stage 2 says "live conditions" with small size.
- Any markets, setups or instruments. The framework expects the trader to supply their own playbook.
- What to do after regressing, for example how a drawdown should move you back a stage.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- The stage durations are the author's estimates, unverified (T4): Stage 1 takes 2–4 weeks, Stages 1–2 together take 4–6 weeks, Stage 3 can take months or years, and Stage 4 can take a year or more.
- The claims that most traders never get past Stage 2 or 3, and that early "psychology" problems are really process problems, are opinion with no data (T4).

## Concepts & lineage

- Building, then narrowing to, a written playbook of 1–2 setups with rules, context and invalidation: [[concept_trading_plan]]
- Daily journaling and critical trade review at every stage: [[concept_trading_journal_review]]
- Psychology matters later, under real size and performance pressure: [[concept_trading_psychology]]
- Stage-gated position sizing: tiny, then small, then gradual, then full: [[concept_position_sizing]]
- Collecting win rate and per-setup and time-of-day statistics: [[concept_performance_metrics]]
- Finding and then trusting your edge over short-term results: [[concept_edge]]

## Changes vs. earlier note

- **Corrected:** the earlier note (T3) described Stage 1 as education, paper trading, learning markets and choosing a style (day vs swing). The playbook's Stage 1 is observing price action, starting a journal, setting cut-off rules and keeping risk extremely low. It doesn't mention paper trading or choosing a market or style, so those items were dropped.
- **Corrected:** the earlier note put "avoid ego-driven and revenge trades" in Stage 2. In the playbook, revenge trading is a Stage 4 temptation. Stage 2's traps are overconfidence after a few wins, skipping review, and sizing up too early. Data collection in Stage 2 is **confirmed**.
- **Corrected:** the earlier note said the goal is "NOT (initially)" to make money. The playbook doesn't limit this to the start: the goal is always a repeatable process, with money as a by-product.
- **Confirmed:** "trading is hard" and "you can't skip stages". The page says everyone wants to skip ahead and it doesn't work.
- **Added:** the other foundational principles (control what you can, no aha moment, psychology is overrated early) and full content for Stages 3–5, which the earlier note listed as not retrieved.
- **Removed:** `concept_backtesting` and `concept_prop_firm_risk_rules` from `uses`, because the playbook mentions neither. Removed the concept id `concept_trading_plan` from `related`, which takes strategy ids only.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/usman-ashraf-options.md ===== -->

---
id: strategy_usman_ashraf_options
type: strategy
title: "Usman Ashraf — Options Trading Masterclass: Options Fundamentals for Beginners (stock options, options education)"
partition: 01_chart-fanatics
layer: L7
aliases: [Options Trading Masterclass, Usman Ashraf options basics, options fundamentals masterclass, Usman Ashraf options]
taught_by: [person_usman_ashraf]
featured_in: [channel_chart_fanatics]
uses: [concept_options_greeks, concept_volatility, concept_leverage_margin, concept_liquidity, concept_position_sizing]
derived_from: [concept_options_greeks]
related: [strategy_brando_options_swing, strategy_gala_trades_price_action]
sources:
  - {title: "Chart Fanatics — Options Trading Masterclass by Usman Ashraf", url: "https://www.chartfanatics.com/strategies/options-trading-masterclass", tier: T2}
status: verified-t2
---

# Usman Ashraf — Options Trading Masterclass: Options Fundamentals for Beginners (stock options, options education)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/options-trading-masterclass. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Usman Ashraf teaches options to beginners. The page says it is
the foundation of his free six-lesson Options Masterclass on Chart Academy.
This page is an education primer on how options work, not a trade setup.

## Built for

- **Instruments:** options on stocks. The examples use AMD.
- **Style:** not a single style. The page links expiry choice to style:
  day traders may prefer weekly or zero-day (0DTE) contracts, and swing
  traders expirations weeks or months away. Longer-dated options (monthlies
  or LEAPS) are described as slower but less exposed to decay.
- **Timeframes / sessions:** not specified.
- **Audience:** beginners. The page recommends buying options rather than
  selling them while learning, because a buyer's risk is defined.

## Core idea

An option is a contract giving the right, but not the obligation, to buy
(call) or sell (put) 100 shares at a strike price before expiration, for a
premium that is the buyer's maximum loss. Most retail traders trade the
premium rather than exercising. The premium is made of intrinsic and
extrinsic (time) value. It is shaped by moneyness, time decay, implied
volatility and the Greeks, and liquidity decides whether you can get in and
out cleanly. Leverage is the attraction, so sizing and expiry must match
the trader's style.

## Rules

This is the decision checklist the page implies, in order. It is not an
entry model.

1. **Know the contract.** One contract covers **100 shares**. The three
   parts are expiration date, strike price and premium. For a buyer, the
   premium is the most you can lose.
2. **Pick a side you can handle.** Buyers pay the premium and have capped
   risk. Sellers (writers) collect it but carry much larger risk. The page
   says buying is usually safer and simpler for beginners.
3. **Pick the direction.** Buy calls if you expect the stock to rise and
   puts if you expect it to fall. The page gives no method for deciding
   direction.
4. **Plan to trade the premium, not exercise.** The page's example: AMD at
   $95, a $97 call bought for $0.50 ($50 per contract) might be worth $1.50
   if AMD reaches $98, so selling it returns $150 without touching the
   shares.
5. **Choose moneyness.** ITM options already have intrinsic value. ATM
   strikes sit near the current price. OTM strikes are cheaper but need a
   bigger move to pay.
6. **Respect time.** Extrinsic value falls as expiration approaches, and at
   expiry only intrinsic value is left. You are trading direction within a
   limited time.
7. **Check implied volatility.** Higher IV makes premiums more expensive,
   and lower IV makes them cheaper. Before earnings IV usually rises, then
   often collapses after the release (volatility crush), pulling option
   prices down with it.
8. **Read the Greeks.**
   - *Delta:* price change per $1 move in the stock. 0.50 means about $0.50.
     Calls have positive delta and puts negative.
   - *Gamma:* how fast delta changes. It is high for short-dated and 0DTE
     options.
   - *Theta:* daily time decay. The page's example is −0.10, about $0.10 lost
     per day.
   - *Vega:* change per 1% move in IV. The example is 0.20, about $0.20 per
     1%.
9. **Check liquidity.** Volume is today's contracts traded and resets at
   the open. Open interest is all contracts still open. In the page's
   example, wanting 70 contracts at a strike with only 100 OI may fill
   slowly, while 10,000 OI is no problem.
10. **Match expiry and size to style.** Short-dated contracts can move
    explosively but decay fast, and a sideways move can erase much of the
    premium. Longer-dated ones move slower but cushion decay.
11. **Choose a risk method.** Either treat the whole premium as the risk
    ("sizing to zero"), or use a stop based on premium value or price
    levels. The page says both can work.

## Risk management

- **Max loss for a buyer:** the premium paid.
- **Risk per trade:** Not specified in the playbook (no % or $ figure).
- **Sizing:** match position size and expiry to style. Two approaches are
  given: size to zero, or a premium-based or price-level stop. No numbers.
- **Daily / weekly limits:** Not specified in the playbook.
- **Seller risk:** described as far greater than buyer risk. No limits or
  margin rules are given.
- **Warning:** leverage makes losses compound as fast as gains without
  discipline.

## What the playbook leaves unspecified

- Any trade setup: how to choose direction, when to enter, where to take
  profit or when to exit.
- Which delta, strike distance or days to expiry to choose for day trades
  versus swings.
- IV thresholds, such as when an option is too expensive to buy.
- A stop level for premium-based stops, such as a percentage of premium.
- Unit conventions. Editor's note from general options knowledge, not from
  the page: the Greek examples are per share, so a contract of 100 shares
  moves about 100 times those amounts, and theta changes as expiry nears
  rather than staying fixed.
- Assignment risk, market hours, 0DTE mechanics and strategy selection.
  The page says these are covered in the full Chart Academy course, not
  here.

## Evidence & claims

- The page makes **no win-rate, R:R, P&L or payout claims**.
- The AMD premium example ($50 to $150, tripling) and the house and car
  deposit analogies are **hypothetical illustrations**, not trade results.
- Two statements are the author's guidance, not tested claims (T4): that
  buying options is usually safer and simpler for beginners, and that
  options can become "one of the most effective tools in your trading
  arsenal".

## Concepts & lineage

- Delta, gamma, theta and vega, and how they move the premium →
  [[concept_options_greeks]]
- Implied volatility, volatility crush around earnings →
  [[concept_volatility]]
- Controlling 100 shares for a fraction of their cost →
  [[concept_leverage_margin]]
- Volume and open interest as fill-quality measures →
  [[concept_liquidity]]
- Matching expiry and size to style, sizing to zero or premium stops →
  [[concept_position_sizing]]
- Lineage: standard options pricing sensitivities →
  [[concept_options_greeks]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/vincent-desiano-break-retest.md ===== -->

---
id: strategy_vincent_desiano_break_retest
type: strategy
title: "Vincent Desiano — Break & Retest with a No-Trade Zone (stocks/options/futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Break & Retest Strategy, battle zone retest, No Trade Zone NTZ, Vincent Desiano break and retest]
taught_by: [person_vincent_desiano]
featured_in: [channel_chart_fanatics]
uses: [concept_support_resistance, concept_breakout_trading, concept_price_action, concept_candlestick_patterns, concept_trading_sessions_killzones, concept_trading_plan, concept_trade_management]
derived_from: [concept_breakout_trading, concept_support_resistance]
related: [strategy_gala_trades_price_action, strategy_rajan_dhall_auction, strategy_ali_crooks_trendline_pocket]
sources:
  - {title: "Chart Fanatics — Break & Retest Strategy", url: "https://www.chartfanatics.com/strategies/break-retest", tier: T2}
status: verified-t2
---

# Vincent Desiano — Break & Retest with a No-Trade Zone (stocks/options/futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/break-retest. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** Vincent Desiano day trades a break-and-retest model off key
levels. The page says he teaches the full method, including premarket
planning, supply and demand, and his 10-2-2 position sizing rule, in a
five-lesson Chart Academy masterclass.

## Built for

- **Instruments:** stocks, options and futures. The worked example is an
  **NQ** short.
- **Style:** day trading. The pros list says the same logic also works for
  swing trades.
- **Timeframes:** not specified.
- **Session:** the previous day's high and low are marked before the open,
  and the premarket high and low once that range is clear. In the NQ
  example, no trade is taken while price consolidates after the open; the
  trade comes only once price breaks out of the no-trade zone and retests.
  No session window or cut-off time is given.

## Core idea

When price breaks a major level, such as the previous day's high or low,
it often comes back to test that level before continuing. Never trade the
break itself. Trade the retest, in what the page calls the **battle
zone**, and only after a confirming candle. Before the open, also mark a
**No Trade Zone (NTZ)**, the range where price is likely to chop. Most
often it spans from the premarket low up to the previous day's high. Stay out
until price breaks cleanly out of that range and retests.

## Rules

1. **Mark the key levels before the open:** the previous day's high and
   low, the premarket high and low, and any supply or demand zone.
2. **Define the NTZ.** Usually it runs from the previous day's high to the
   premarket low, but read the chart for wherever price is likely to be
   indecisive. Take no trades inside it.
3. **Wait for a clean break** of a level, with strong momentum in the
   example. **Do not enter during the break.**
4. **Wait for the retest (battle zone)** and watch how price behaves there.
   - *Longs:* bullish wicks into the level and strong closes above it.
   - *Shorts:* rejections and failed pushes back through the level, with
     no closes back on the wrong side.
5. **Enter on a confirmation candle:** it probes the level with a wick,
   then closes on your side of it (above for longs, below for shorts). The NQ example names rejection candles and bearish engulfing
   candles.
6. **Stop just beyond the invalidation point.** Below the level for longs,
   above it for shorts. In the example, the stop went just above the wick
   high of the retest structure, and a close above it voided the setup.
7. **TP1:** the prior high for longs, or the prior (most recent intraday)
   low for shorts.
8. **At TP1:** take **25% to 50%** off, reduce risk, and hold the rest as a
   runner while the move continues.
9. **No retest, no trade.** Accept missing breaks that never come back.
   Don't chase late entries, which spoil the risk-to-reward.

## Risk management

- **Stop:** just beyond the retest level or wick. The page calls this "no
  guessing, no wide stops".
- **Partials:** 25% to 50% at TP1, then reduce risk on the rest.
- **Position sizing:** the page mentions fixed risk and a **10-2-2 position
  sizing rule** but does not explain either. The details are in the
  masterclass, not this page.
- **Risk per trade ($ or %):** Not specified in the playbook.
- **Daily / weekly limits:** Not specified in the playbook.
- **No-trade filter:** nothing inside the NTZ.

## What the playbook leaves unspecified

- What the 10-2-2 sizing rule is.
- The chart timeframe for the break, retest and confirmation candle.
- What makes a break "clean": a candle close beyond the level, a minimum
  distance, or volume.
- How long to wait for a retest before abandoning the idea.
- How to draw the NTZ when it is not the previous day's high to the
  premarket low.
- What "reduce risk" means after TP1 (break-even or a partial stop move),
  and how the runner is exited or trailed.
- How many trades per day, and a cut-off time.
- How supply and demand zones are drawn.

## Evidence & claims

- The page reports **no win rate, R:R, P&L or payout**.
- The pros list calls it a "High Probability Setup". This is an
  unsupported claim (T4).
- The NQ short example gives the sequence (premarket low broken with
  momentum, retest rejected, short with the stop above the retest wick,
  TP1 at the most recent intraday low) but no result. No expectancy check
  is possible.

## Concepts & lineage

- Previous day and premarket highs and lows, supply and demand zones →
  [[concept_support_resistance]]
- Waiting for the retest of a broken level instead of buying the break →
  [[concept_breakout_trading]]
- Reading wicks and closes in the battle zone → [[concept_price_action]]
- Rejection and engulfing confirmation candles →
  [[concept_candlestick_patterns]]
- Premarket range levels and the NTZ framed by session levels →
  [[concept_trading_sessions_killzones]]
- Marking levels and the NTZ before the open → [[concept_trading_plan]]
- 25–50% partial at TP1 and holding a runner →
  [[concept_trade_management]]


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/strategies/yush-order-flow.md ===== -->

---
id: strategy_yush_order_flow
type: strategy
title: "Trader Yush — Trading Trapped Buyers & Sellers with Order Flow (NQ/ES futures, day trading)"
partition: 01_chart-fanatics
layer: L4
aliases: [Yush strategy, trapped traders order flow, Yush AOI model, range and trend order-flow models]
taught_by: [person_trader_yush]
featured_in: [channel_chart_fanatics]
uses: [concept_order_flow, concept_volume_profile, concept_auction_market_theory, concept_support_resistance, concept_market_regimes, concept_mean_reversion, concept_trend_following, concept_scalping, concept_trade_management, concept_position_sizing, concept_trade_execution]
derived_from: [concept_order_flow, concept_auction_market_theory]
related: [strategy_fabio_valentini_amt_order_flow, strategy_andrea_cimitan_amt, strategy_carmine_rosato_lvn]
sources:
  - {title: "Chart Fanatics — Yush’s Strategy: Trading Trapped Buyers & Sellers with Order Flow", url: "https://www.chartfanatics.com/strategies/order-flow-strategy", tier: T2}
  - {title: "TradeZella — Order Flow Strategy", url: "https://www.tradezella.com/strategies/order-flow-strategy", tier: T3}
status: verified-t2
---

# Trader Yush — Trading Trapped Buyers & Sellers with Order Flow (NQ/ES futures, day trading)

> Source: Chart Fanatics playbook (T2): https://www.chartfanatics.com/strategies/order-flow-strategy. Rules are paraphrased; performance figures are self-reported (T4).

**Trader.** The playbook presents Trader Yush as a futures day trader who builds levels from market-generated references, volume profile, big trades and delta, then waits for order-flow confirmation before executing. The page gives no other biography.

## Built for

- **Instruments:** futures. The header says NQ; ES appears in the big-trade thresholds and in one worked example.
- **Style:** day trading with a "scalping mindset": quick execution, short holds, typically 2–3 trades per day.
- **Timeframes:** no chart timeframe is given. Execution is read from order-flow tools (DOM, delta, big trades) against session-based levels.
- **Session / time window:** the US session, implied by the references (overnight high and low, previous-day levels, a 32-second opening range). No explicit hours are given.

## Core idea

Every trade starts from an Area of Interest (AOI). An AOI is built from at least two of four objective tools: market-generated levels, volume profile, big trades and delta profile. When price returns to the AOI, the trader waits for order flow to show that one side tried to push and failed, through absorption or trapped traders, and then trades the other way. The market state picks the model. A balanced (range) market uses fades at the value edges. An imbalanced (trend) market uses pullbacks into low-volume nodes. Both models react to what is happening rather than predicting it.

## Rules

1. **Build AOIs.**
   - Market-generated levels: previous-day high and low, overnight high and low, previous-day close, and the opening range (32-second ORB).
   - Volume profile: the value area (where about 70% of volume traded) and low-volume nodes (LVNs).
   - Big trades: NQ 75+ lots and ES 200+ lots (the ES figure is "adjusted based on liquidity").
   - Delta profile: positive delta means buyers lifting the ask; negative delta means sellers hitting the bid.
   - A valid AOI needs **at least 2** of these. **3–4** makes an A+ setup.
2. **Classify the market state.**
   - *Balanced/range:* price inside value, volume concentrated in the middle, breakouts that lack follow-through, repeated reversals at similar levels.
   - *Imbalanced/trend:* strong directional movement, value shifting in one direction, LVNs present, shallow pullbacks.
3. **Wait for price to return to the AOI.** No return means no trade. Never enter directly into strong momentum. Wait for a slowdown, a reaction and confirmation.

**Model 1: Range (balanced market)**

4. **Trade only the edges:** value area high as resistance and value area low as support. The middle of the range is a no-trade zone.
5. **Aggressive entry** at the edge on early rejection: absorption (heavy activity, no price movement), strong delta without continuation, or big trades that fail to push price further. Use smaller size and a tight stop.
6. **Confirmation entry.** Price breaks out of the range, breakout traders chase, then price comes back inside and shows rejection. Enter the fade once price is back in the range (for example, short after a failed break above the top).
7. **Stop:** just outside the range edge.
8. **Targets:** T1 at the range midpoint, T2 at the opposite side of value. Move the stop to break-even as soon as T1 is reached.

**Model 2: Trend (imbalanced market)**

9. **Setup sequence:** price moves aggressively one way and leaves an LVN. Price then pulls back into the LVN, the opposite side turns aggressive, and price fails to continue against the trend.
10. **Aggressive entry** inside the pullback zone when opposing aggression appears without follow-through, or absorption is visible. Use a tight stop. **Confirmation entry:** wait for a reclaim of structure and a higher low (bullish) or lower high (bearish) with a shift back in the trend direction. This gives a slightly worse price.
11. **Management:** take partial profits at previous highs or lows, hold the rest for continuation, and trail on structure. Move to break-even after the partial. Add only to winning positions.
12. **Execution discipline:** don't anticipate; react to confirmation. Limit yourself to high-quality setups, typically 2–3 trades per day.

## Risk management

- **Risk per trade:** Not specified in the playbook as a $ or % figure. Define risk before every entry.
- **Stops:**
  - Range model: just outside the range edge.
  - Trend model: tight, with quick invalidation.
  - Trend example (instrument not stated): stop just above the overnight low.
- **Sizing:** smaller size on aggressive entries. Scale into strength, not weakness, and never add to losers.
- **Protecting profit:** never let a winner turn into a loss. Break-even after T1 or the first partial. A break-even stop-out is acceptable.
- **Losses:** accept them quickly.
- **Daily / weekly limits:** Not specified in the playbook beyond the typical 2–3 trades per day.

## What the playbook leaves unspecified

- Numeric thresholds for "strong" delta and for absorption, and how the ES big-trade filter is "adjusted based on liquidity" (and whether the NQ one is too).
- Which volume profile to use (prior day, developing, composite) and the value-area settings.
- An objective rule for calling the market balanced or imbalanced in real time.
- A chart timeframe, stop buffers in ticks, partial sizes, and the trailing method.
- Position size per trade, a daily loss limit, time-of-day restrictions and news handling.

## Evidence & claims

- The page makes no win-rate, R:R, P&L or payout claims.
- **Trend example (Model 2; the page doesn't name the instrument):** shortly after the open, a liquidation-driven break below the overnight low left an LVN and a print of about 300 lots near the level. The pullback into the zone showed continued negative delta and more big sell prints. The short was entered just below the level with the stop above the overnight low. Described qualitatively, with no P&L (T4).
- **ES range example:** positive delta built to about 800, 1,800 and 1,900+ at the range highs without price progress, which the page reads as absorption. A sweep of the overnight high then failed. The short was entered around the level, targeting the range midpoint and then the range low. No P&L given (T4).
- The earlier note's third-party summary (TradeZella, T3) reported the same big-trade thresholds and the two-confirmation minimum, and the playbook agrees with it.

## Concepts & lineage

- Delta, big trades, absorption and trapped traders as the confirmation layer: [[concept_order_flow]]
- Value area (about 70% of volume), VAH and VAL edges, LVNs as imbalance zones: [[concept_volume_profile]], [[concept_auction_market_theory]]
- Market-generated reference levels (PDH/PDL, ONH/ONL, prior close, ORB) as AOIs: [[concept_support_resistance]]
- Separate models for balanced vs imbalanced conditions: [[concept_market_regimes]]
- Range model fading back to the midpoint and the opposite side of value: [[concept_mean_reversion]]
- Trend model joining pullbacks into LVNs and scaling into strength: [[concept_trend_following]]
- Two-target exits, break-even after T1, trailing on structure: [[concept_trade_management]]
- Smaller size on aggressive entries, adding only to winners: [[concept_position_sizing]]
- Aggressive vs confirmation entries, and no entries into momentum: [[concept_trade_execution]], [[concept_scalping]]

## Changes vs. earlier note

- **Confirmed:** the big-trade thresholds (about 75+ lots on NQ and about 200+ on ES), the minimum of 2 confirmations per zone, and the absorption, delta and trapped-trader logic. The earlier note had these from a third-party summary (T3).
- **Corrected:** the earlier note said entries are early, so traders should size smaller and keep stops tight (T3). The playbook says that applies only to the *aggressive* entry variant. Each model also has a *confirmation* entry.
- **Corrected:** the earlier title said "ES/NQ scalping". The playbook labels it NQ futures **day trading** with a scalping mindset.
- **Added:** the four AOI tools, including the 32-second ORB and the 70% value area, and the A+ grade for 3–4 confirmations.
- **Added:** the two models (range edges vs trend pullbacks into LVNs), the targets (range midpoint, then the opposite side of value), break-even rules, add-to-winners-only, and the guideline of typically 2–3 trades per day.
- The Chart Fanatics (T2) source is kept as the primary source, and the TradeZella (T3) source is kept as secondary.


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/video-catalog.md ===== -->

<!-- generated by tools/render_registries.py from the YAML registries; do not edit by hand -->

# Chart Fanatics — Strategy & Video Catalog (seed)

## Strategies / playbooks

| Strategy | Trader | Status | Uses concepts |
|---|---|---|---|
| **Abraham Perez — Nasdaq ICT & Order Flow Scalping Strategy (NQ futures, scalping)** | Abraham Perez | verified-t2 | `concept_smart_money_concepts`, `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_fair_value_gap`, `concept_market_structure`, `concept_dow_theory`, `concept_order_flow`, `concept_volume_profile`, `concept_vwap`, `concept_multi_timeframe_analysis`, `concept_trading_sessions_killzones`, `concept_risk_reward_r_multiples`, `concept_scalping` |
| **Alex Temiz — First Red Day Strategy (stocks/options, day trading)** | Alex Temiz | verified-t2 | `concept_price_action`, `concept_support_resistance`, `concept_mean_reversion`, `concept_market_sentiment`, `concept_trade_management`, `concept_position_sizing` |
| **Ali Crooks — Trendline Break Pocket (forex, daily swing trading)** | Ali Crooks | verified-t2 | `concept_trendlines`, `concept_support_resistance`, `concept_market_structure`, `concept_moving_averages`, `concept_breakout_trading`, `concept_risk_reward_r_multiples`, `concept_multi_timeframe_analysis`, `concept_divergence`, `concept_oscillators_momentum`, `concept_market_sentiment`, `concept_correlation_portfolio_risk` |
| **Andrea Cimitan — Liquidity Auction & Order Flow Strategy (futures, day trading)** | Andrea Cimitan | verified-t2 | `concept_auction_market_theory`, `concept_order_flow`, `concept_volume_profile`, `concept_market_microstructure`, `concept_optimal_execution_market_impact`, `concept_liquidity`, `concept_mean_reversion`, `concept_breakout_trading`, `concept_multi_timeframe_analysis` |
| **Anthony Crudele — Futures Trend Trading Strategy: Bollinger Band Environments (index futures, swing trading)** | Anthony Crudele | verified-t2 | `concept_bollinger_bands`, `concept_volatility`, `concept_market_regimes`, `concept_trend_following`, `concept_breakout_trading`, `concept_mean_reversion`, `concept_support_resistance`, `concept_liquidity_sweep_reversal`, `concept_fibonacci`, `concept_multi_timeframe_analysis`, `concept_moving_averages`, `concept_vwap`, `concept_oscillators_momentum`, `concept_options_greeks`, `concept_position_sizing`, `concept_trade_management` |
| **Ariel Hernandez — Real Simple Swing Setups: EP, HVC, Flat Base, U&R, High Tight Flag (stocks, swing trading)** | Ariel Hernandez | verified-t2 | `concept_episodic_pivot`, `concept_breakout_trading`, `concept_growth_momentum_canslim`, `concept_chart_patterns`, `concept_moving_averages`, `concept_liquidity_sweep_reversal`, `concept_market_regimes`, `concept_position_sizing`, `concept_trade_management`, `concept_multi_timeframe_analysis` |
| **Brando Elite — Options Swing Trading on HTF Levels + News Catalysts (options, swing trading)** | Brando Elite | verified-t2 | `concept_support_resistance`, `concept_news_trading`, `concept_fundamental_macro_analysis`, `concept_multi_timeframe_analysis`, `concept_options_greeks`, `concept_position_sizing`, `concept_risk_reward_r_multiples`, `concept_trading_psychology` |
| **Candace Lau — NQ Liquidity Sweep & IFVG Reversal (NQ futures, scalping)** | Candace Lau | verified-t2 | `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_premium_discount_ote`, `concept_fair_value_gap`, `concept_market_structure`, `concept_multi_timeframe_analysis`, `concept_amd_power_of_three`, `concept_trading_sessions_killzones`, `concept_smt_divergence`, `concept_scalping`, `concept_risk_reward_r_multiples`, `concept_trade_management`, `concept_position_sizing`, `concept_prop_firm_risk_rules` |
| **Carmine Rosato — Low Volume Node (LVN) Pullback Strategy (futures/indices, scalping/day trading)** | Carmine Rosato | verified-t2 | `concept_volume_profile`, `concept_order_flow`, `concept_support_resistance`, `concept_liquidity`, `concept_scalping`, `concept_position_sizing`, `concept_risk_reward_r_multiples` |
| **Carmine Rosato — Order Flow Masterclass: Absorption & Stop-Run Reclaim (futures, intraday order-flow trading)** | Carmine Rosato | verified-t2 | `concept_order_flow`, `concept_auction_market_theory`, `concept_market_microstructure`, `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_support_resistance`, `concept_volume_profile` |
| **Clement Ang — Price Cycle Strategy: Continuation Base and Late-Stage Failed Base (US stocks, swing trading)** | Clement Ang | verified-t2 | `concept_moving_averages`, `concept_trend_following`, `concept_growth_momentum_canslim`, `concept_breakout_trading`, `concept_chart_patterns`, `concept_volatility`, `concept_support_resistance`, `concept_price_action`, `concept_market_structure`, `concept_multi_timeframe_analysis`, `concept_vwap`, `concept_oscillators_momentum`, `concept_market_regimes`, `concept_news_trading`, `concept_liquidity`, `concept_trade_management`, `concept_risk_reward_r_multiples`, `concept_trading_psychology` |
| **Dhesi — Liquidity Inversion Model: Sweep, FVG Inversion & LTF Confirmation (NQ/ES futures, day trading/swing trading)** | Dhesi | verified-t2 | `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_fair_value_gap`, `concept_order_blocks_breakers`, `concept_market_structure`, `concept_multi_timeframe_analysis`, `concept_trading_sessions_killzones`, `concept_volatility`, `concept_smt_divergence`, `concept_trendlines`, `concept_trade_management`, `concept_position_sizing`, `concept_risk_reward_r_multiples`, `concept_trading_psychology` |
| **Dylan O’Neil — VIX Futures Strategy: VIX Pressure as Confirmation for ES and NQ (index and VIX futures, day and swing trading)** | Dylan O’Neil | verified-t2 | `concept_volatility`, `concept_market_sentiment`, `concept_intermarket_analysis`, `concept_divergence`, `concept_smt_divergence`, `concept_support_resistance`, `concept_breakout_trading`, `concept_liquidity_sweep_reversal`, `concept_chart_patterns`, `concept_market_microstructure`, `concept_market_regimes`, `concept_risk_reward_r_multiples` |
| **Fabio Valentini — Auction Market Theory + Order-Flow Scalping (NQ/ES futures, scalping)** | Fabio Valentini | verified-t2 | `concept_auction_market_theory`, `concept_volume_profile`, `concept_order_flow`, `concept_market_regimes`, `concept_trend_following`, `concept_mean_reversion`, `concept_scalping`, `concept_trading_sessions_killzones`, `concept_position_sizing`, `concept_risk_reward_r_multiples`, `concept_trade_execution` |
| **Forrest Knight — Volume Profile Edge-to-Edge Strategy (options/futures, day trading / swing trading)** | Forrest Knight | verified-t2 | `concept_volume_profile`, `concept_auction_market_theory`, `concept_support_resistance`, `concept_liquidity`, `concept_price_action`, `concept_candlestick_patterns`, `concept_multi_timeframe_analysis`, `concept_trade_execution` |
| **Fredy Sarmiento — Institutional Options Flow: Gamma Wall Reversal (index futures/options, day trading/scalping)** | Fredy Sarmiento | verified-t2 | `concept_options_greeks`, `concept_volatility`, `concept_market_microstructure`, `concept_order_flow`, `concept_support_resistance`, `concept_trading_sessions_killzones`, `concept_scalping`, `concept_risk_reward_r_multiples`, `concept_trade_management`, `concept_position_sizing`, `concept_trading_psychology` |
| **Gala Trades — Price Action Strategy: Hourly Levels with Breaking Retest, Bounce & Rejection (stock options, day trading)** | Gala Trades | verified-t2 | `concept_price_action`, `concept_market_structure`, `concept_trend_following`, `concept_support_resistance`, `concept_multi_timeframe_analysis`, `concept_breakout_trading`, `concept_trading_plan`, `concept_order_flow`, `concept_options_greeks`, `concept_risk_reward_r_multiples`, `concept_position_sizing`, `concept_trade_management`, `concept_trading_journal_review`, `concept_trading_psychology` |
| **JJ Simon — Fair Pricing Theory: Continuation & Reversion (Nasdaq futures, 1-minute scalping)** | JJ Simon | verified-t2 | `concept_mean_reversion`, `concept_trading_sessions_killzones`, `concept_news_trading`, `concept_market_structure`, `concept_multi_timeframe_analysis`, `concept_prop_firm_risk_rules`, `concept_position_sizing`, `concept_risk_reward_r_multiples`, `concept_risk_of_ruin_drawdown`, `concept_backtesting`, `concept_scalping`, `concept_market_regimes` |
| **JadeCap — Intraday Liquidity & Volatility Model: New York Session Liquidity Raids (futures/forex, day trading/swing trading)** | JadeCap | verified-t2 | `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_fair_value_gap`, `concept_market_structure`, `concept_order_blocks_breakers`, `concept_trading_sessions_killzones`, `concept_multi_timeframe_analysis`, `concept_smt_divergence`, `concept_trading_journal_review` |
| **Jared Tendler — Trading Psychology Playbook: Emotion, Performance & the Mental Game (any market, trading psychology)** | Jared Tendler | verified-t2 | `concept_trading_psychology`, `concept_trading_journal_review`, `concept_trading_plan`, `concept_expectancy` |
| **Jay Awtani — Market DNA: Tape & Level II at DNA Zones (large-cap stocks/options and NQ/ES futures, day trading)** | Jay Awtani | verified-t2 | `concept_order_flow`, `concept_market_microstructure`, `concept_liquidity`, `concept_support_resistance`, `concept_news_trading`, `concept_risk_reward_r_multiples`, `concept_trade_management`, `concept_leverage_margin` |
| **Jeff Holden — Momentum Model Performance Development (stocks/futures, day-trading development loop)** | Jeff Holden | verified-t2 | `concept_trading_journal_review`, `concept_trading_psychology`, `concept_trading_plan`, `concept_position_sizing`, `concept_trade_management`, `concept_moving_averages`, `concept_vwap`, `concept_support_resistance` |
| **Kris Verma — Small-Cap Shorting: Gap Fades, Backside Parabolics & Halt Exhaustion (small-cap stocks, scalping/day trading)** | Kris Verma | verified-t2 | `concept_mean_reversion`, `concept_market_microstructure`, `concept_liquidity`, `concept_trading_sessions_killzones`, `concept_support_resistance`, `concept_trade_management`, `concept_position_sizing`, `concept_probability_fat_tails`, `concept_performance_metrics`, `concept_backtesting` |
| **Kyle Williams — Small Cap Short Selling Playbook: First Red Day and Parabolic Short (US small-cap stocks, day trading)** | Kyle Williams | verified-t2 | `concept_mean_reversion`, `concept_market_sentiment`, `concept_support_resistance`, `concept_price_action`, `concept_vwap`, `concept_volatility`, `concept_market_microstructure`, `concept_risk_reward_r_multiples`, `concept_position_sizing`, `concept_trade_management`, `concept_trading_journal_review`, `concept_trading_psychology` |
| **Lance Breitstein — Capitulation Mean Reversion (stocks, day trading)** | Lance Breitstein | verified-t2 | `concept_mean_reversion`, `concept_expectancy`, `concept_volatility`, `concept_bollinger_bands`, `concept_moving_averages`, `concept_market_sentiment`, `concept_multi_timeframe_analysis`, `concept_market_structure`, `concept_price_action`, `concept_trade_management`, `concept_position_sizing` |
| **Marci Silfrain — Measured Move Trend Strategy: Little RZY (stocks, futures and crypto, swing trading)** | Marci Silfrain | verified-t2 | `concept_trendlines`, `concept_market_structure`, `concept_trend_following`, `concept_chart_patterns`, `concept_fibonacci`, `concept_bollinger_bands`, `concept_mean_reversion`, `concept_support_resistance`, `concept_multi_timeframe_analysis`, `concept_trade_management`, `concept_backtesting`, `concept_risk_of_ruin_drawdown`, `concept_trading_psychology` |
| **Marco Trades — Liquidity Grab Trading Strategy (futures, forex and crypto, day trading)** | Marco Trades | verified-t2 | `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_market_structure`, `concept_price_action`, `concept_trade_execution`, `concept_trading_sessions_killzones`, `concept_multi_timeframe_analysis`, `concept_trade_management` |
| **Marios Stamatoudis — Parabolic Short: Exhaustion-Day VWAP Failure (stocks, day trading)** | Marios Stamatoudis | verified-t2 | `concept_mean_reversion`, `concept_vwap`, `concept_market_structure`, `concept_moving_averages`, `concept_market_sentiment`, `concept_support_resistance`, `concept_volatility`, `concept_trade_management` |
| **Matteo Conti — Institutional Strategy Development Framework (multi-asset, day and swing trading)** | Matteo Conti | verified-t2 | `concept_backtesting`, `concept_overfitting_validation`, `concept_edge`, `concept_expectancy`, `concept_performance_metrics`, `concept_risk_of_ruin_drawdown`, `concept_position_sizing`, `concept_volatility`, `concept_trading_plan`, `concept_breakout_trading`, `concept_vwap`, `concept_news_trading`, `concept_trading_sessions_killzones`, `concept_market_microstructure`, `concept_optimal_execution_market_impact`, `concept_random_walk_efficient_markets`, `concept_market_regimes`, `concept_correlation_portfolio_risk`, `concept_probabilistic_thinking` |
| **NBB Trader — PO3, OTE + ADR: Market Maker Model with Fixed-R Fib Entries (forex, swing trading)** | NBB Trader | verified-t2 | `concept_amd_power_of_three`, `concept_premium_discount_ote`, `concept_fibonacci`, `concept_order_blocks_breakers`, `concept_fair_value_gap`, `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_market_structure`, `concept_multi_timeframe_analysis`, `concept_trading_sessions_killzones`, `concept_risk_reward_r_multiples`, `concept_trade_management` |
| **Naoufel Taief — No-Code Algorithmic Strategy Portfolio: Generate, Stress-Test & Rotate (stocks/futures, systematic trading)** | Naoufel Taief | verified-t2 | `concept_backtesting`, `concept_overfitting_validation`, `concept_performance_metrics`, `concept_risk_of_ruin_drawdown`, `concept_position_sizing`, `concept_correlation_portfolio_risk`, `concept_breakout_trading`, `concept_mean_reversion`, `concept_market_regimes`, `concept_volatility`, `concept_expectancy`, `concept_risk_reward_r_multiples`, `concept_machine_learning_finance` |
| **Okala — 80/20 Nasdaq Strategy: Reactions at 20 and 80 Price Endings (NQ futures, day trading)** | Okala | verified-t2 | `concept_support_resistance`, `concept_price_action`, `concept_candlestick_patterns`, `concept_mean_reversion`, `concept_multi_timeframe_analysis`, `concept_trading_sessions_killzones`, `concept_market_regimes`, `concept_volatility`, `concept_risk_reward_r_multiples`, `concept_trade_management` |
| **Pavel — First-Principles Trading Framework (multi-asset, strategy-design framework)** | Pavel (Trading First Principles) | verified-t2 | `concept_edge`, `concept_expectancy`, `concept_performance_metrics`, `concept_market_microstructure`, `concept_random_walk_efficient_markets`, `concept_liquidity`, `concept_volatility`, `concept_breakout_trading`, `concept_oscillators_momentum`, `concept_mean_reversion`, `concept_moving_averages`, `concept_trend_following`, `concept_support_resistance`, `concept_backtesting`, `concept_correlation_portfolio_risk` |
| **Pradeep Bonde — Episodic Pivot (EP) Strategy (stocks, day trading / swing trading)** | Pradeep Bonde (Stockbee) | verified-t2 | `concept_episodic_pivot`, `concept_news_trading`, `concept_growth_momentum_canslim`, `concept_breakout_trading`, `concept_support_resistance`, `concept_trade_management`, `concept_position_sizing` |
| **Rajan Dhall — Auction Market Strategy: Auction-Zone Retest with Trend (stocks/futures, scalping/day trading)** | Rajan Dhall | verified-t2 | `concept_auction_market_theory`, `concept_trend_following`, `concept_moving_averages`, `concept_multi_timeframe_analysis`, `concept_support_resistance`, `concept_candlestick_patterns`, `concept_market_sentiment`, `concept_trading_sessions_killzones`, `concept_risk_reward_r_multiples` |
| **Steven Dux — Small-Cap Short Statistics Playbook (US small-cap stocks, day trading)** | Steven Dux | verified-t2 | `concept_mean_reversion`, `concept_support_resistance`, `concept_volume_profile`, `concept_liquidity`, `concept_market_sentiment`, `concept_market_microstructure`, `concept_price_action`, `concept_trading_sessions_killzones`, `concept_position_sizing`, `concept_risk_reward_r_multiples`, `concept_trade_management`, `concept_performance_metrics`, `concept_probabilistic_thinking`, `concept_edge` |
| **TG Capital — London Session Trident Strategy (forex, gold and futures, swing trading)** | TG Capital | verified-t2 | `concept_trading_sessions_killzones`, `concept_fair_value_gap`, `concept_moving_averages`, `concept_multi_timeframe_analysis`, `concept_candlestick_patterns`, `concept_trend_following`, `concept_market_regimes`, `concept_trade_management`, `concept_risk_reward_r_multiples`, `concept_prop_firm_risk_rules` |
| **Tanja Trades — AMD Futures Model: Trade the Distribution Leg (futures, day trading)** | Tanja Trades | verified-t2 | `concept_amd_power_of_three`, `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_market_structure`, `concept_fair_value_gap`, `concept_news_trading`, `concept_multi_timeframe_analysis`, `concept_trading_sessions_killzones`, `concept_intermarket_analysis`, `concept_market_regimes`, `concept_trade_management` |
| **Ted Zhang — Stage Analysis Strategy (multi-asset, swing and position trading)** | Ted Zhang | verified-t2 | `concept_moving_averages`, `concept_market_structure`, `concept_trend_following`, `concept_market_regimes`, `concept_multi_timeframe_analysis`, `concept_breakout_trading`, `concept_chart_patterns`, `concept_growth_momentum_canslim`, `concept_mean_reversion`, `concept_news_trading`, `concept_market_sentiment`, `concept_support_resistance`, `concept_position_sizing`, `concept_trade_management` |
| **Tori Trades — Trendline Trading Playbook: Action Line and Safety Line (stocks, futures and forex, 4H swing trading)** | Tori Trades | verified-t2 | `concept_trendlines`, `concept_price_action`, `concept_market_structure`, `concept_support_resistance`, `concept_breakout_trading`, `concept_trend_following`, `concept_multi_timeframe_analysis`, `concept_trade_management`, `concept_trading_journal_review` |
| **Trader Kane — 50% Reversal with SMT Divergence & PO3 (NQ/ES futures and crypto, scalping/day trading)** | Trader Kane | verified-t2 | `concept_smt_divergence`, `concept_amd_power_of_three`, `concept_premium_discount_ote`, `concept_fair_value_gap`, `concept_liquidity_sweep_reversal`, `concept_multi_timeframe_analysis`, `concept_trading_sessions_killzones`, `concept_trade_management`, `concept_smart_money_concepts` |
| **Trader Mayne — Structure + OTE: HTF Break, POI Pullback & LTF Breaker Entry (forex/futures/crypto, swing trading)** | Trader Mayne | verified-t2 | `concept_market_structure`, `concept_order_blocks_breakers`, `concept_fair_value_gap`, `concept_premium_discount_ote`, `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_multi_timeframe_analysis`, `concept_trend_following`, `concept_risk_reward_r_multiples`, `concept_position_sizing` |
| **Trader Yush — Trading Trapped Buyers & Sellers with Order Flow (NQ/ES futures, day trading)** | Trader Yush | verified-t2 | `concept_order_flow`, `concept_volume_profile`, `concept_auction_market_theory`, `concept_support_resistance`, `concept_market_regimes`, `concept_mean_reversion`, `concept_trend_following`, `concept_scalping`, `concept_trade_management`, `concept_position_sizing`, `concept_trade_execution` |
| **Traveling Trader — Universal Trading Strategy (stocks/options/futures/forex, scalping to swing trading)** | Traveling Trader | verified-t2 | `concept_liquidity`, `concept_liquidity_sweep_reversal`, `concept_market_structure`, `concept_support_resistance`, `concept_trendlines`, `concept_fair_value_gap`, `concept_order_blocks_breakers`, `concept_moving_averages`, `concept_divergence`, `concept_multi_timeframe_analysis`, `concept_fundamental_macro_analysis`, `concept_price_action`, `concept_trade_management` |
| **Umar Ashraf — 5-Stage Trader Development Framework (any market, trader development)** | Umar Ashraf | verified-t2 | `concept_trading_plan`, `concept_trading_journal_review`, `concept_trading_psychology`, `concept_position_sizing`, `concept_performance_metrics`, `concept_edge` |
| **Usman Ashraf — Options Trading Masterclass: Options Fundamentals for Beginners (stock options, options education)** | Usman Ashraf | verified-t2 | `concept_options_greeks`, `concept_volatility`, `concept_leverage_margin`, `concept_liquidity`, `concept_position_sizing` |
| **Vincent Desiano — Break & Retest with a No-Trade Zone (stocks/options/futures, day trading)** | Vincent Desiano | verified-t2 | `concept_support_resistance`, `concept_breakout_trading`, `concept_price_action`, `concept_candlestick_patterns`, `concept_trading_sessions_killzones`, `concept_trading_plan`, `concept_trade_management` |

## Known videos & episodes

| Title | Channel | Speakers | ~Views | Verification |
|---|---|---|---|---|
| **Chart Fanatics Live Trading: New York Session With MarcoTrades** | Chart Fanatics Live (YouTube) | Marco Trades |  | confirmed |
| **Order-flow traders Fabio Valentini & Carmine Rosato (Chart Fanatics episode)** | Chart Fanatics (YouTube channel) | Fabio Valentini, Carmine Rosato |  | third-party |
| **Rajan Dhall — A+ Simple Trading Strategy & Market Auction Theory (May 2025)** | Chart Fanatics (YouTube channel) | Rajan Dhall |  | announced |
| **Gianluca Bruni (2x World Trading Champion) — building statistical models around your strategy; prop-firm mastery** | Chart Fanatics (YouTube channel) | Gianluca Bruni |  | announced |
| **Andy Krieger — the $300 Million Trade** | Chart Fanatics (YouTube channel) | Andrew (Andy) Krieger |  | third-party |
| **Trader Kane ($2M+) — episode** | Chart Fanatics (YouTube channel) | Trader Kane |  | third-party |
| **Ted Zhang — managing $25 million at a young age (Nov 2025)** | Chart Fanatics (YouTube channel), Words of Rizdom | Ted Zhang |  | third-party |
| **First systematic trader on Chart Fanatics & Words of Rizdom (Oct 2025)** | Chart Fanatics (YouTube channel), Words of Rizdom |  |  | announced |
| **BEST Trading Podcast: From Losing To Consistent Profitable Trader Managing $50 Million** | Words of Rizdom |  |  | third-party |
| **The World's #2 Trader \| Futures Trading World Champion Marci Silfrain (Words of Rizdom)** | Words of Rizdom | Marci Silfrain |  | third-party |
| **Trading Psychologist: Here's How I MAKE Traders Profitable Long Term (Words of Rizdom)** | Words of Rizdom |  |  | confirmed |

## Full channel catalog (scraped)

1,029 uploads: **50 long-form masterclasses (~85 hours)** and 979 shorts (shorts are listed in `catalog.scraped.yaml`). View counts are as listed on the channel at scrape time.

| # | Title | Views | Length | Concepts (from title) |
|---|---|---|---|---|
| 1 | [Trading LIVE with a World TOP Ranked Scalper (EXTREME Accuracy)](https://www.youtube.com/watch?v=tvERE-Beu2U) | 4,700,000 | 3:34:10 | `concept_scalping` |
| 2 | [STEAL This EASY Liquidity TRAP Trading Strategy - $500K+ (PERFECT Sniper Entries)](https://www.youtube.com/watch?v=DAnXM7C16h0) | 1,300,000 | 1:49:37 |  |
| 3 | [STEAL This SIMPLE Trading Strategy from The WORLD's #2 Futures Trader - Marci Silfrain](https://www.youtube.com/watch?v=AVVM-FyewLg) | 1,100,000 | 1:23:30 | `strategy_marci_silfrain_measured_move` |
| 4 | [The SIMPLE $10 Million ICT Blueprint They Don’t Want You To See (Forex Trading Strategy) ](https://www.youtube.com/watch?v=coBMd1vk2Lo) | 1,000,000 | 1:00:28 | `concept_smart_money_concepts` |
| 5 | [Making $500,000 Using This SIMPLE Futures Strategy - Tori Trades (Simple Breakdown)](https://www.youtube.com/watch?v=VTEQ2fhGLqE) | 872,000 | 1:11:24 | `strategy_tori_trendline_4h` |
| 6 | [STEAL This INSANE Simple 90% Win Rate Trading Strategy (1:20+ RR) - TG Capital](https://www.youtube.com/watch?v=ADnslyKOwFE) | 735,000 | 48:16 | `concept_performance_metrics`, `strategy_tg_capital_trident` |
| 7 | [Worlds BEST NQ Scalper Reveals His A+ Trading Strategy](https://www.youtube.com/watch?v=HNuRp9Z1bMs) | 715,000 | 1:14:44 | `concept_scalping` |
| 8 | [12 Years of Trading Knowledge in 2 Hours - Umar Ashraf](https://www.youtube.com/watch?v=IUo5AwmsE9A) | 674,000 | 1:59:05 | `strategy_umar_ashraf_5_stage` |
| 9 | [The ONE Trading Indicator That Will EXPOSE The Truth About The Markets (PASS Prop Firms)](https://www.youtube.com/watch?v=q_MdVlZ1SH4) | 639,000 | 1:23:03 | `concept_prop_firm_risk_rules` |
| 10 | [LIVE TRADING - How He Made $40,000+ Trading using OrderFlow (Full Masterclass)](https://www.youtube.com/watch?v=UhkRRqO1gQM) | 486,000 | 3:42:20 |  |
| 11 | [The ONE Liquidity Trading Pattern That Actually Works (Precise Entries)](https://www.youtube.com/watch?v=T_djSNBmV00) | 472,000 | 1:11:22 |  |
| 12 | [Worlds BEST Prop Firm Trader Reveals SIMPLE Trading Strategy - Jadecap (Full Breakdown)](https://www.youtube.com/watch?v=8OX-mcSHWhg) | 466,000 | 1:28:23 | `concept_prop_firm_risk_rules`, `strategy_jadecap_liquidity_volatility` |
| 13 | [Options Trading for Beginners: Super Simple - 2 Hour FREE Course](https://www.youtube.com/watch?v=6Bdv-_YUQ0s) | 435,000 | 1:59:54 |  |
| 14 | [STEAL The 1-Minute Strategy That Made Him $1.8M+ (Works EVERY Session)](https://www.youtube.com/watch?v=KHEQ5g55dQ4) | 419,000 | 1:42:25 |  |
| 15 | [74% Win Rate Trader Shares His EXACT OrderFlow Strategy ($2M+ Payouts)](https://www.youtube.com/watch?v=hvyf6frvCcA) | 405,000 | 1:33:10 | `concept_performance_metrics`, `concept_prop_firm_risk_rules` |
| 16 | [Trading $6,000 to OVER $10+ Million Using This Strategy](https://www.youtube.com/watch?v=yLuH8YZXORQ) | 396,000 | 1:06:50 |  |
| 17 | [TAKE This EASY ICT Trading Strategy For Prop Firms (INSANE Entries)](https://www.youtube.com/watch?v=IB-fyWI5j8w) | 346,000 | 1:21:53 | `concept_prop_firm_risk_rules`, `concept_smart_money_concepts` |
| 18 | [COPY This Prop Firm Simple Trading Strategy with 65% Win Rate ($5+ Million Payouts)](https://www.youtube.com/watch?v=jsUTbjwpFVk) | 305,000 | 1:13:14 | `concept_prop_firm_risk_rules`, `concept_performance_metrics` |
| 19 | [The ONLY Break And Retest Trading Strategy You’ll EVER Need (Step By Step)](https://www.youtube.com/watch?v=SMSqQTBxjc0) | 277,000 | 1:28:07 |  |
| 20 | [LIVE Trading with a $1M+ Order Flow Trader (INSANE RESULTS)](https://www.youtube.com/watch?v=SQEtBHOJW6I) | 267,000 | 2:51:38 | `concept_order_flow` |
| 21 | [If You Only Watch One Trading Strategy Video, Make It This](https://www.youtube.com/watch?v=52ZsDmFHqyY) | 250,000 | 1:07:43 |  |
| 22 | [This SIMPLE ICT Futures Trading Strategy Made Her Over $100,000 - Tanja Trades (Copy This)](https://www.youtube.com/watch?v=PZDWQgtqt2I) | 245,000 | 1:10:18 | `concept_smart_money_concepts`, `strategy_tanja_amd_futures` |
| 23 | [COPY This CRAZY Simple 98% Win Rate Trading Strategy](https://www.youtube.com/watch?v=Jx5cJ_qb31U) | 243,000 | 1:12:19 | `concept_performance_metrics` |
| 24 | [$100+ Million Trader: His BEST Trading Strategy (Market Wizard)](https://www.youtube.com/watch?v=_qeFh1ADss8) | 241,000 | 1:31:11 |  |
| 25 | [How To Trade Real Fair Value Gaps with Extreme Accuracy - Carmine Rosato (Full Strategy)](https://www.youtube.com/watch?v=jHsD2-2K_Kk) | 229,000 | 1:14:45 | `concept_fair_value_gap`, `concept_chart_patterns`, `strategy_carmine_rosato_lvn`, `strategy_carmine_rosato_orderflow_masterclass` |
| 26 | [Master The Mental Game of Trading In 60 Minutes (STOP TILT/FOMO)](https://www.youtube.com/watch?v=8HxT9WQ-uD0) | 221,000 | 1:00:54 | `concept_trading_psychology` |
| 27 | [COPY This EXACT Entry System to Become a Millionaire Trader](https://www.youtube.com/watch?v=YzYDUEUOZ4k) | 221,000 | 1:06:30 |  |
| 28 | [PRO Trader Reveals Super Simple Trading Strategy (How The Markets Really Move)](https://www.youtube.com/watch?v=yZpzG8R3Ayk) | 220,000 | 1:20:39 |  |
| 29 | [Trading $50M At 25 Using One SIMPLE Market Cycle Strategy (4 Stages) - Ted Zhang](https://www.youtube.com/watch?v=VDK200OHNSo) | 209,000 | 1:40:26 | `strategy_ted_zhang_stage_analysis` |
| 30 | [STEAL This INSANE 1-Minute Market Maker Trading Strategy (75% Win Rate)](https://www.youtube.com/watch?v=35cyqDz-ej8) | 193,000 | 2:29:41 | `concept_market_microstructure`, `concept_performance_metrics` |
| 31 | [If You Only Watch One ICT Trading Video, Make It This (LIVE Trading)](https://www.youtube.com/watch?v=UIGZtoGGPH4) | 185,000 | 1:13:29 | `concept_smart_money_concepts` |
| 32 | [STEAL This $100 Million Dollar Trading Strategy (Used by Market Wizards)](https://www.youtube.com/watch?v=mDNcx2Dhhms) | 178,000 | 57:14 |  |
| 33 | [STEAL This 7 Figure Liquidity HACK for Your Trading (Any Asset & Timeframe)](https://www.youtube.com/watch?v=nMhywubR2xc) | 172,000 | 1:22:07 |  |
| 34 | [Master ALGO Trading In Less Than 90 Minutes (NO Coding) \| $1M+ Profits](https://www.youtube.com/watch?v=TyHTEtArsS4) | 167,000 | 1:25:00 |  |
| 35 | [20 Years Of Institutional Trading Knowledge In 70 Minutes ($20M+ AUM)](https://www.youtube.com/watch?v=_wpg45NdMkM) | 149,000 | 1:11:55 |  |
| 36 | [Verified $5M+ Trader: LIVE Trading Using His EXACT Strategy](https://www.youtube.com/watch?v=70UtrLU6RAg) | 128,000 | 2:09:41 |  |
| 37 | [Trading Made SIMPLE - Use These 3 Specific Steps To Master Any Market](https://www.youtube.com/watch?v=9D9ck-ZI6V0) | 128,000 | 1:06:40 |  |
| 38 | [If You Only Watch ONE Market Cycle Trading Video, Make It This (500%+ Champion)](https://www.youtube.com/watch?v=0_NSmOWVbpA) | 115,000 | 48:43 |  |
| 39 | [COPY These 3 Simple Steps To Master The TREND Trading Futures - Anthony Crudele](https://www.youtube.com/watch?v=EZ_L7zovyrw) | 101,000 | 46:28 | `strategy_anthony_crudele_futures_trend` |
| 40 | [Wall Street's EXACT Formula To Measure FEAR In The Markets (Trade This NOW)](https://www.youtube.com/watch?v=4BgkLlwgpvo) | 96,000 | 1:38:39 |  |
| 41 | [Simple ONE Candle Trading Strategy Thats Profited Millions (80%+ Win Rate) ](https://www.youtube.com/watch?v=2Ug0jyDvoek) | 80,000 | 2:05:41 | `concept_performance_metrics` |
| 42 | [Copy this Complete In-Depth 85%+ Win Rate Short Trading Strategy - US Investing Champion](https://www.youtube.com/watch?v=SInAfwX3X3A) | 77,000 | 2:17:11 | `concept_performance_metrics` |
| 43 | [Pass Prop Firms Using This ICT & Orderflow Futures Trading Strategy ($600k+)](https://www.youtube.com/watch?v=KkTTCKr-3Ew) | 71,000 | 1:45:07 | `concept_prop_firm_risk_rules`, `concept_smart_money_concepts` |
| 44 | [COPY The BEST Gap Up Short Trading Strategy That Has Made Millions (Proven Results)](https://www.youtube.com/watch?v=EcTRlLYvhXU) | 51,000 | 1:12:14 |  |
| 45 | [Trading LIVE With The World’s #1 Prop Firm Scalper ($2.5M+ Payouts)](https://www.youtube.com/watch?v=-kGVL93XfyE) |  | 2:04:00 | `concept_prop_firm_risk_rules`, `concept_scalping` |
| 46 | [4 Institutional Scalping Strategies Market Makers Keep SECRET (Automate Prop Firm Trading)](https://www.youtube.com/watch?v=yW6c0K8uGvw) |  | 1:38:53 | `concept_scalping`, `concept_market_microstructure`, `concept_prop_firm_risk_rules` |
| 47 | [STEAL This Trading Champion’s Exact Strategy - Math Based Models for Prop Firms](https://www.youtube.com/watch?v=xl4QHqlBCfk) |  | 2:42:09 | `concept_prop_firm_risk_rules` |
| 48 | [If You Only Watch One Trading Process Video, Make It This](https://www.youtube.com/watch?v=WDdvnd9vLbM) |  | 1:24:45 |  |
| 49 | [Trading LIVE with TWO World Class Order Flow Scalpers (FT Fabio Valentini & Carmine Rosato)](https://www.youtube.com/watch?v=xUyqIjCfZzg) |  | 3:49:38 | `concept_order_flow`, `concept_scalping`, `strategy_carmine_rosato_lvn`, `strategy_carmine_rosato_orderflow_masterclass`, `strategy_fabio_valentini_amt_order_flow` |
| 50 | [Trading LIVE with One of the World's BEST Scalpers (PERFECT Sniper Entries)](https://www.youtube.com/watch?v=TvoQr6ObjnU) |  | 5:41:15 | `concept_scalping` |


<!-- ===== FILE: trading-intelligence/01_chart-fanatics/video-title-links.yaml ===== -->

```yaml
# Chart Fanatics videos linked to concepts and playbooks from their TITLES (transcripts are not
# available from the cloud). Each link was proposed by one reader and kept only if an independent
# skeptic, reading the same title, could not refute it: 310 proposed, 245 kept (2026-10-20).
# Links are INFERRED (trailing '?'); the reason quotes the title words that justify each one.
# Curated file: re-running the catalog scraper does not touch it. When transcripts arrive, the
# scraper's own tagging adds content links on top.
video_title_links:
- id: media_cf_0juaispfqje
  covers:
  - concept_liquidity?
  link_reason: '"How To AVOID Getting Swept Out" refers to liquidity sweeps of stops.'
- id: media_cf_0m7eqqj4rta
  covers:
  - concept_auction_market_theory?
  link_reason: '"How To Trade The Market Auction" names auction market theory.'
- id: media_cf_0p1zichzzc8
  covers:
  - concept_trade_execution?
  link_reason: '"MOST Traders Enter TOO Early" is about entry timing/confirmation.'
- id: media_cf_1anqlvizao8
  covers:
  - concept_trade_execution?
  link_reason: '"WHY Confirmation Matters MORE Than BIAS" is about waiting for confirmation before entering.'
- id: media_cf_1fzsup8mony
  covers:
  - concept_price_action?
  link_reason: '"Price Is All That MATTERS" states the price-action (naked chart) view.'
- id: media_cf_1h108qwrpom
  covers:
  - concept_multi_timeframe_analysis?
  link_reason: '"Higher Time Frames Are The WAY" names the higher timeframes (HTF), part of multi-timeframe analysis.'
- id: media_cf_1stdgr87mqq
  covers:
  - strategy_ted_zhang_stage_analysis?
  link_reason: '"Managing Over $30M Using Stage Analysis" names Ted Zhang''s distinctive Stage Analysis method.'
- id: media_cf_1x4tohhptjw
  covers:
  - concept_order_flow?
  link_reason: '"The ONE Trading Indicator That Exposes ALL Market Orders" describes an order-flow tool (footprint/delta) that shows market orders.'
- id: media_cf_2_6ivzjtbgy
  covers:
  - concept_risk_reward_r_multiples?
  - concept_trade_execution?
  link_reason: '"The Entry TRICK That Can TRANSFORM Your RR" names entry technique and RR (risk:reward).'
- id: media_cf_2venfw7lea8
  covers:
  - concept_trade_execution?
  link_reason: '"How 7 Figure Traders Time Entries" is about entry timing and triggers.'
- id: media_cf_35cyqdz_ej8
  covers:
  - concept_scalping?
  link_reason: '"1-Minute Market Maker Trading Strategy" names a 1-minute scalping approach.'
- id: media_cf_3_9nf2ulfyg
  covers:
  - concept_liquidity?
  link_reason: '"2 Liquidity Points Is ALL You NEED" names liquidity points directly.'
- id: media_cf_3et_vvqbcee
  covers:
  - concept_trade_execution?
  link_reason: Title names a "Simple Entry Trading Technique", which is about entries (trade execution).
- id: media_cf_3w6f_nlggvk
  covers:
  - concept_edge?
  link_reason: '"How To BUILD An Edge" names building a trading edge.'
- id: media_cf_48b7etwqqra
  covers:
  - concept_trade_execution?
  link_reason: '"The Confirmation Traders NEED To WAIT FOR" refers to waiting for a confirmation entry.'
- id: media_cf_4bgkllwgpvo
  covers:
  - concept_volatility?
  - concept_market_sentiment?
  link_reason: '"Wall Street''s EXACT Formula To Measure FEAR" refers to the VIX fear gauge, which covers both volatility and market sentiment.'
- id: media_cf_4ec7p3plxcs
  covers:
  - concept_fundamental_macro_analysis?
  link_reason: '"as markets price Iran risk" is about markets pricing geopolitical and macro risk.'
- id: media_cf_4sgqkgb010m
  covers:
  - concept_options_greeks?
  link_reason: Title says "Options Trading Strategy", which names options.
- id: media_cf_4tpy07kqvuu
  covers:
  - concept_order_flow?
  link_reason: '"How Trap Buyers Get Caught" names trapped traders, an order-flow concept.'
- id: media_cf_59_a2svzfwy
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"PRINTS High RR Trades" names RR (risk:reward).'
- id: media_cf_5_ffuf378jw
  covers:
  - concept_trade_management?
  link_reason: '"Get Stopped Out BEFORE The Move" is about stop-loss placement and stops being hunted before the real move.'
- id: media_cf_5ama76mguf8
  covers:
  - concept_breakout_trading?
  - concept_trade_execution?
  link_reason: '"How PRO Traders Enter Trendline Breaks" is about entries (execution) on breaks.'
- id: media_cf_5dxdg8l75zw
  covers:
  - concept_probabilistic_thinking?
  link_reason: '"One BAD Trade Can Teach You The WRONG Lesson" is about judging by outcome rather than process (resulting).'
- id: media_cf_5vwy54lt3k8
  covers:
  - concept_order_flow?
  link_reason: '"WHY Orderflow Trading Is The BEST" names order flow directly.'
- id: media_cf_5xgp0iiwj0w
  covers:
  - concept_trade_management?
  link_reason: '"WHY Taking PROFIT Early WINS" is about take-profit decisions, a trade management topic.'
- id: media_cf_5zzhh7id3nu
  covers:
  - concept_breakout_trading?
  link_reason: '"Why Breakdowns Trap Retail Traders" is about false breakdowns/breakouts.'
- id: media_cf_6bdv__yuq0s
  covers:
  - concept_options_greeks?
  link_reason: '"Options Trading for Beginners ... FREE Course" names options and matches Usman Ashraf''s "Options Fundamentals for Beginners" playbook.'
- id: media_cf_6jynzcxzlfs
  covers:
  - concept_trade_execution?
  link_reason: '"Most Traders Enter TOO Early" is about entry timing and confirmation.'
- id: media_cf_747acils69o
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"Catch 9R Trades" names an R-multiple outcome.'
- id: media_cf_7nssobxtgg0
  covers:
  - concept_liquidity?
  link_reason: '"Your Stop Loss Is EXACTLY Where They Want It" refers to resting stops being targeted as liquidity.'
- id: media_cf_7q7_ei1xqoi
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"DON''T Trade Pre Market" is about which market hours/session to trade.'
- id: media_cf_7wrkfjwpntu
  covers:
  - concept_scalping?
  link_reason: '"How To Profitably Scalp Trade" names scalping.'
- id: media_cf_8cmxz5rqiui
  covers:
  - concept_liquidity?
  link_reason: '"The Liquidity Model EVERY Trader SHOULD Understand" names liquidity explicitly.'
- id: media_cf_8hxt9wq_ud0
  covers:
  - strategy_jared_tendler_psychology?
  link_reason: '"Master The Mental Game of Trading" is Jared Tendler''s signature method and book title, and his playbook is the Mental Game playbook.'
- id: media_cf_8omtuiixr0u
  covers:
  - concept_trade_management?
  link_reason: '"MOST Traders GUESS Their Exits... PROS Plan Them" is about planning exits (trade management) ahead of time (trading plan).'
- id: media_cf_8wn8pfzvoge
  covers:
  - concept_edge?
  link_reason: '"Actually Having An Edge" names trading edge.'
- id: media_cf_9e9abbupwka
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"The 1:10 RR Model" names a risk:reward ratio.'
- id: media_cf_9vzecobh38m
  covers:
  - concept_liquidity_sweep_reversal?
  link_reason: '"The BEST Entries Happen BELOW The LOWS" describes buying after lows are swept, i.e. a liquidity sweep / stop-hunt reversal.'
- id: media_cf_9zxqnk2lbwe
  covers:
  - concept_breakout_trading?
  - concept_support_resistance?
  - strategy_vincent_desiano_break_retest?
  link_reason: '"Break & Retest Trading Masterclass with Scarface Trades" names the break-and-retest method and Scarface Trades, Vincent Desiano''s handle.'
- id: media_cf__6kwbvurm3k
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"The 1:12 RR Setup" names a risk:reward ratio.'
- id: media_cf__axxol2jvhw
  covers:
  - concept_trade_execution?
  link_reason: '"THIS Confirmation SIGNAL" refers to confirmation entries.'
- id: media_cf__n1tggewlbk
  covers:
  - concept_trade_execution?
  link_reason: '"ELITE Execution Strategy" names trade execution.'
- id: media_cf__n6uqhszdqi
  covers:
  - concept_trade_management?
  link_reason: '"RUIN A Winning Trade" is about mismanaging an open winner, i.e. trade management.'
- id: media_cf__nrsoaiyqhm
  covers:
  - concept_chart_patterns?
  link_reason: '"Make MILLIONS Using THIS Chart Pattern" names a chart pattern.'
- id: media_cf__o03cnliblo
  covers:
  - concept_auction_market_theory?
  link_reason: '"Use Simple Market Averages to Trade the Auction" names moving averages and auction market theory.'
- id: media_cf__o8_gjvsvo4
  covers:
  - concept_trade_execution?
  link_reason: Title is about a specific "Entry That Trading Institutions LOVE", which is an entry and execution topic.
- id: media_cf__vrj_tvq7mw
  covers:
  - concept_trade_management?
  link_reason: '"Before Placing Your TP" names take-profit placement, a trade management topic.'
- id: media_cf__xeenvtizoq
  covers:
  - concept_trading_psychology?
  link_reason: '"The MORE You Trade The WORSE You Become" is about overtrading, a discipline and psychology issue.'
- id: media_cf_a9_5n3rllve
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"THIS High RR Strategy" names high risk:reward.'
- id: media_cf_aaq3iqha3uq
  covers:
  - concept_edge?
  link_reason: '"THIS Is The REAL Edge In Trading" names trading edge.'
- id: media_cf_adknlqoghki
  covers:
  - concept_trade_execution?
  link_reason: Title says "His Secret Entry Trick", which is about entry execution.
- id: media_cf_adx8px7ymew
  covers:
  - concept_news_trading?
  link_reason: '"Trade This Simple Method Next Time There''s News" is explicitly about news trading.'
- id: media_cf_agt_cwfawuk
  covers:
  - concept_trade_execution?
  link_reason: Title says "REVEALS His Entry Method", which is about entry execution.
- id: media_cf_ajdwq8dmcx0
  covers:
  - concept_trading_psychology?
  link_reason: '"MOST Traders Chase But Professionals Wait" is about FOMO versus patience and discipline.'
- id: media_cf_aohcksurxbw
  covers:
  - concept_amd_power_of_three?
  link_reason: '"The AMD ICT Trading Strategy" names AMD (accumulation, manipulation, distribution / Power of Three).'
- id: media_cf_aqt6ognyh90
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"Why Price Reverses After The Open" is about time-of-day behavior at the session open.'
- id: media_cf_asyfr4eoogm
  covers:
  - concept_liquidity?
  link_reason: '"Liquidity Cheat Code" names liquidity.'
- id: media_cf_azqrkca24vk
  covers:
  - concept_market_regimes?
  link_reason: '"Trades CHOP" refers to trading a choppy / ranging market regime.'
- id: media_cf_b3btthhknlg
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"They Trade At The WRONG Time" is about the time of day you trade.'
- id: media_cf_b4ggj6stzws
  covers:
  - concept_liquidity?
  link_reason: '"The Market ISN''T Hunting Your STOP LOSS" is about stop hunts, which is the stop-pool liquidity concept.'
- id: media_cf_bb7y5cyqaxu
  covers:
  - concept_trend_following?
  link_reason: '"Momentum Traders Stay on the RIGHT Side of the Move" is about trading with the trend or momentum.'
- id: media_cf_bchjnasgmms
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"The BEST Time To Trade The Market" is about the time of day you trade.'
- id: media_cf_bkt6svtxmo0
  covers:
  - concept_liquidity?
  link_reason: '"The Liquidity Concept MOST Traders Are MISSING" names liquidity explicitly.'
- id: media_cf_bkziqdled6u
  covers:
  - concept_trade_execution?
  link_reason: '"The Entry Strategy That Made MILLIONS" names an entry strategy (trade execution).'
- id: media_cf_bu4kshfqyyw
  covers:
  - concept_trade_execution?
  link_reason: '"Overcomplicate Their Entries" names entries as the topic.'
- id: media_cf_bx48xu2je_a
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: Title says "1:7 Risk To Reward Trade", which names risk:reward.
- id: media_cf_by6e_ml__ac
  covers:
  - concept_trade_execution?
  link_reason: '"WAIT For The Breakout To CONFIRM" refers to confirmation entries.'
- id: media_cf_c0_6abzp_fm
  covers:
  - concept_trading_plan?
  link_reason: '"Your Trading Day Starts BEFORE The Open" describes a pre-market routine, part of the trading plan.'
- id: media_cf_c7ukk66uc4o
  covers:
  - concept_chart_patterns?
  link_reason: '"THIS Chart Pattern Will FIX Your Trading" names chart patterns directly.'
- id: media_cf_cajaizmkfrs
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"Hit 9R Trades CONSISTENTLY" names an R-multiple (9R).'
- id: media_cf_cmkoaopbcl4
  covers:
  - concept_chart_patterns?
  link_reason: '"Pattern Trading Is A SCAM" names pattern trading (classical chart patterns).'
- id: media_cf_cpgtza0xeza
  covers:
  - concept_trade_execution?
  link_reason: Title says "His Secret Entry Formula", which is about entry execution.
- id: media_cf_crhidoppcza
  covers:
  - concept_trend_following?
  - concept_trade_execution?
  link_reason: '"The ONLY Smart Way To Enter A Trend" names entering a trend (trend following plus entry execution).'
- id: media_cf_crxpxxpcnns
  covers:
  - concept_news_trading?
  link_reason: '"The SECRET To Trading News" names news trading directly.'
- id: media_cf_csy2wy5_jq4
  covers:
  - concept_mean_reversion?
  link_reason: '"Counter Trend Traders Blow Accounts" names counter-trend (fade) trading and blowing accounts (ruin).'
- id: media_cf_cxgxkvgs23c
  covers:
  - concept_liquidity?
  link_reason: '"Trade The DRAW On Liquidity" names liquidity as the price target.'
- id: media_cf_cybgqa_nuzm
  covers:
  - concept_market_regimes?
  link_reason: '"SURVIVE Choppy Markets" is about trading choppy, ranging market conditions.'
- id: media_cf_dc4jc2icrxe
  covers:
  - concept_trade_management?
  link_reason: '"MOST Traders Get Stopped Out" is about stop-loss placement.'
- id: media_cf_dprhxqeu8ag
  covers:
  - concept_performance_metrics?
  link_reason: '"Transform Your WR" names win rate, a performance metric.'
- id: media_cf_dquhz6vadow
  covers:
  - concept_trade_execution?
  link_reason: '"How To Get The BEST Trade Entries" is explicitly about entry execution.'
- id: media_cf_dw45qcwdvrc
  covers:
  - concept_trading_psychology?
  link_reason: '"Adapt THIS Mindset" names trader mindset/psychology.'
- id: media_cf_ectrllyvhxu
  covers:
  - concept_mean_reversion?
  link_reason: '"Gap Up Short Trading Strategy" means shorting a gap up, which is a fade, the vocabulary''s alias for mean reversion.'
- id: media_cf_ed6mombvmti
  covers:
  - concept_trading_psychology?
  link_reason: Title says "Never Reach The Zone", the 'trading in the zone' mental state, which is psychology.
- id: media_cf_edifm5qithe
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"Trade This Specific Time Everyday" is about a time-of-day edge (sessions / kill zones).'
- id: media_cf_ejkc8rt8seo
  covers:
  - concept_options_greeks?
  link_reason: Title says "MASTER Option Trading", which names options.
- id: media_cf_eociqkoecq4
  covers:
  - concept_liquidity?
  link_reason: '"How Liquidity WORKS" names liquidity.'
- id: media_cf_epndnpic4ns
  covers:
  - concept_order_flow?
  link_reason: '"EVERY Trader NEEDS Orderflow" names order flow directly.'
- id: media_cf_expywhqt86m
  covers:
  - concept_chart_patterns?
  link_reason: '"THIS Chart Pattern Makes MILLIONS" names a chart pattern.'
- id: media_cf_ez_l7zovyrw
  covers:
  - concept_trend_following?
  link_reason: '"Master The TREND Trading Futures" names trend trading.'
- id: media_cf_f1w2ftazr8i
  covers:
  - concept_trade_execution?
  link_reason: '"THIS Entry Strategy" names trade entries/execution.'
- id: media_cf_f41dpj6xllm
  covers:
  - concept_trend_following?
  link_reason: '"STOP Fighting The Trend" names trading with the trend.'
- id: media_cf_fcnqwcrghnc
  covers:
  - concept_trade_execution?
  link_reason: '"SIMPLE Pullback Entry" names an entry technique.'
- id: media_cf_fj1lnrzxgto
  covers:
  - concept_multi_timeframe_analysis?
  link_reason: '"How To CORRECTLY Use The Lower Timeframes" names the lower timeframes (LTF), part of multi-timeframe analysis.'
- id: media_cf_fubsxzvk_de
  covers:
  - strategy_clement_ang_price_cycle?
  link_reason: '"Clement placing ... in the US Investing Championships" names Clement (Ang), the author of the Price Cycle playbook.'
- id: media_cf_fwddqdm_zru
  covers:
  - concept_trading_plan?
  link_reason: '"The BEST Traders ADAPT Their Plan" names the trading plan.'
- id: media_cf_fyowzx1xjxw
  covers:
  - concept_trade_management?
  link_reason: '"How PROS Manage Winners" names trade management.'
- id: media_cf_gg9cq9ig02q
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"STOP Trading At The WRONG Time Of Day" is about the time-of-day / session edge.'
- id: media_cf_gjz_k2v2ide
  covers:
  - concept_trade_execution?
  link_reason: '"The Confirmation MOST Traders MISS" is about the entry confirmation trigger, part of trade execution.'
- id: media_cf_glkjxyocrqu
  covers:
  - concept_trade_management?
  link_reason: '"How To Scale In WITHOUT Increasing RISK" names scaling in (trade management) while keeping risk fixed (position sizing).'
- id: media_cf_gwhgtpqn7su
  covers:
  - concept_trade_execution?
  link_reason: Title names a "Simple Trade Entry Model", which is about entries (trade execution).
- id: media_cf_h1j5x7ecx6a
  covers:
  - concept_risk_of_ruin_drawdown?
  link_reason: '"Geometric Losses KILL Accounts" refers to drawdown recovery math, where losses compound and destroy accounts.'
- id: media_cf_h_mo02_ujke
  covers:
  - concept_news_trading?
  link_reason: '"How To Trade Around Trump News" is explicitly about news trading.'
- id: media_cf_hdzguzekc_8
  covers:
  - concept_edge?
  link_reason: '"Develop The ULTIMATE EDGE" names developing a trading edge.'
- id: media_cf_hepul_nkllo
  covers:
  - concept_trade_execution?
  link_reason: '"Get The BEST Short Entries" names entries as the topic.'
- id: media_cf_hns3dllzgqu
  covers:
  - concept_trading_psychology?
  link_reason: '"The Mental Shift That Separates Winning Traders" is about trading mindset.'
- id: media_cf_hqjbgkutr80
  covers:
  - concept_trade_management?
  link_reason: '"MOST Traders Scale Out WRONG" names scaling out, a trade-management technique.'
- id: media_cf_hvfu_pyhrnm
  covers:
  - concept_liquidity?
  link_reason: '"THIS Liquidity Strategy" names liquidity.'
- id: media_cf_hvyf6frvcca
  covers:
  - concept_order_flow?
  link_reason: '"His EXACT OrderFlow Strategy" names order flow.'
- id: media_cf_i2fs7iz4k6w
  covers:
  - concept_scalping?
  link_reason: Title says "If You Scalp", which names scalping.
- id: media_cf_ibrq6sdl8co
  covers:
  - concept_support_resistance?
  link_reason: '"Draw Levels WRONG" refers to drawing support/resistance levels.'
- id: media_cf_igzvt0obpzs
  covers:
  - concept_trade_management?
  link_reason: '"WHY You Should Exit Traders EARLY" is about exits and taking profit.'
- id: media_cf_ij_7cfraxkc
  covers:
  - concept_liquidity?
  link_reason: '"The Liquidity TRAP Most Traders FALL For" names liquidity.'
- id: media_cf_ijknyfdyrpc
  covers:
  - concept_support_resistance?
  link_reason: '"THESE Levels Made Him MILLIONS" refers to price levels, meaning key support and resistance levels.'
- id: media_cf_ivhamax7koe
  covers:
  - concept_trade_execution?
  link_reason: '"MOST Traders Enter TOO EARLY" is about entry timing, which is trade execution.'
- id: media_cf_ivtlj_nffsa
  covers:
  - concept_liquidity_sweep_reversal?
  link_reason: '"Buy BELOW The Lows, NOT Above Them" describes buying a sweep of the lows (stop-hunt reversal).'
- id: media_cf_j5t2cyg8ngo
  covers:
  - concept_liquidity?
  - concept_trade_execution?
  link_reason: '"Think Liquidity Is The Entry" names liquidity and contrasts it with the entry, which is a trade-execution topic.'
- id: media_cf_j_vkw1ogpv0
  covers:
  - concept_liquidity?
  link_reason: '"START Trading Liquidity" names liquidity directly.'
- id: media_cf_jcmj9s2fcyq
  covers:
  - concept_scalping?
  link_reason: '"The 15 Second Chart" names a sub-minute chart, which is scalping.'
- id: media_cf_jcnfooonfys
  covers:
  - concept_order_flow?
  link_reason: '"Orderflow Is The ONLY Way To Be PROFITABLE" names order flow (one-word spelling).'
- id: media_cf_je7ymbsg1ne
  covers:
  - concept_smart_money_concepts?
  link_reason: '"THIS Market Maker Model" names the ICT Market Maker Model, which is a Smart Money Concepts model.'
- id: media_cf_jjgxgtwjzi4
  covers:
  - concept_market_regimes?
  link_reason: '"Where MOST Traders Get CHOPPED Up" refers to choppy/ranging market conditions.'
- id: media_cf_jlugbuokkiy
  covers:
  - concept_liquidity?
  link_reason: '"The ONLY Liquidity Video" names liquidity.'
- id: media_cf_jugpel_o3ik
  covers:
  - concept_trading_psychology?
  link_reason: Title says "Profitable Trading Isn't Luck, It's Psychology".
- id: media_cf_jz7ybunqzlq
  covers:
  - concept_trade_execution?
  link_reason: Title says "REVEALS His ENTRY METHOD", which is about entry execution.
- id: media_cf_k32abuyakxg
  covers:
  - concept_trade_execution?
  link_reason: '"How To Catch Sniper Entires [entries]" is explicitly about entry execution.'
- id: media_cf_k_ndswfdjsg
  covers:
  - concept_trading_psychology?
  link_reason: '"HOW To FIX Your Emotions" names emotions, which is trading psychology.'
- id: media_cf_kakeey6rwio
  covers:
  - concept_trade_execution?
  link_reason: Title says "Get PERFECT Trade Entires" (Entries), which is about entry execution.
- id: media_cf_kheq5g55dq4
  covers:
  - concept_scalping?
  link_reason: '"The 1-Minute Strategy" names a 1-minute scalping approach.'
- id: media_cf_kkbjrcexwts
  covers:
  - concept_trade_execution?
  link_reason: Title says "The Perfect Entry Technique In Trading", which is about entry execution.
- id: media_cf_kkttckr_3ew
  covers:
  - concept_order_flow?
  link_reason: '"ICT & Orderflow Futures Trading Strategy" names order flow, and the ICT plus order flow pairing is the method of Abraham Perez''s ICT & Order Flow playbook.'
- id: media_cf_kneiufggah0
  covers:
  - concept_trade_management?
  link_reason: '"SHOULDN''T Be In A Trade For Longer Than 15 Minutes" is about how long to hold a trade, which is trade management.'
- id: media_cf_ksjf5vxfwfi
  covers:
  - concept_liquidity?
  link_reason: '"Market Makers AREN''T Hunting You" addresses the stop-hunt idea, which belongs to the liquidity (stop pools, stop hunt) concept.'
- id: media_cf_lgsdgyvzrkk
  covers:
  - concept_liquidity?
  link_reason: Title names a "Simple Liquidity Trading Strategy".
- id: media_cf_lii2orgcr4s
  covers:
  - concept_trade_execution?
  link_reason: '"Most Traders Wait For Confirmation... he''s ALREADY In" is about when to enter, confirmation entry versus early entry.'
- id: media_cf_liquidity_trap
  covers:
  - concept_liquidity?
  link_reason: '"Liquidity TRAP Trading Strategy" names liquidity as the topic.'
- id: media_cf_mencbj_kkb4
  covers:
  - concept_wyckoff_method?
  link_reason: '"HOW To SPOT Accumulation vs Distribution" names the Wyckoff accumulation and distribution phases.'
- id: media_cf_mfufchfag1m
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"RR That Makes MILLIONS" names RR (risk:reward).'
- id: media_cf_mj1finozo2a
  covers:
  - concept_trading_psychology?
  link_reason: Title is about "No Emotion" traders failing, so it is about emotions and psychology.
- id: media_cf_mkgzdipkcxg
  covers:
  - concept_expectancy?
  link_reason: '"You DON''T Need A HIGH Win Rate To Make Money" is the classic expectancy point that win rate alone does not decide profitability.'
- id: media_cf_mmi8qgxnm_c
  covers:
  - concept_probabilistic_thinking?
  link_reason: '"EVERY Trader MUST Understand Variance" names the spread of outcomes, a probabilistic-thinking topic.'
- id: media_cf_mmixobv0f4w
  covers:
  - concept_candlestick_patterns?
  link_reason: '"How MILLIONAIRE Traders Read Candles" is about candlestick reading.'
- id: media_cf_mrt24iaspgy
  covers:
  - concept_trade_management?
  link_reason: Title says "HOW To Manage Your Trade The RIGHT Way", which is trade management.
- id: media_cf_nbahz5ipqcc
  covers:
  - concept_order_flow?
  link_reason: '"Aggressive Buyers" is order-flow language for market buy orders lifting the offer.'
- id: media_cf_nevm0kk3wmy
  covers:
  - concept_liquidity?
  link_reason: '"Liquidity EXPLAINED in 30 Seconds" names liquidity directly.'
- id: media_cf_ngchsfcl3te
  covers:
  - concept_trade_management?
  link_reason: '"How EXPERTS Add To Positions" is about scaling in and pyramiding, part of trade management.'
- id: media_cf_nkky8oakbfe
  covers:
  - concept_candlestick_patterns?
  link_reason: '"THESE Candles Can Make You MILLIONS" names candlesticks as the topic.'
- id: media_cf_nlynh6xhxfi
  covers:
  - concept_market_microstructure?
  link_reason: '"How Smart Money Hides Their Orders" is about hidden orders in the order book (microstructure).'
- id: media_cf_nmhywubr2xc
  covers:
  - concept_liquidity?
  link_reason: '"7 Figure Liquidity HACK" names liquidity as the topic.'
- id: media_cf_nmwki_bqui4
  covers:
  - concept_trade_execution?
  link_reason: '"Most Traders MISS This Entry" names entries as the topic.'
- id: media_cf_npkpg7fwkp4
  covers:
  - concept_trade_execution?
  link_reason: '"Most Traders MISS The BEST Entries" is about trade entries/execution.'
- id: media_cf_nsfelk1kvxk
  covers:
  - concept_trend_following?
  link_reason: '"Trade WITH The Trend" names trend following.'
- id: media_cf_nsyz8srwjzc
  covers:
  - concept_liquidity?
  link_reason: '"The Liquidity TRAP" names liquidity explicitly.'
- id: media_cf_o_tnadk9e5g
  covers:
  - concept_liquidity?
  link_reason: '"THIS Liquidity Strategy" names liquidity as the topic.'
- id: media_cf_oauhio8woz8
  covers:
  - concept_liquidity?
  link_reason: '"Market Makers AREN''T Hunting You" is about the idea of stop hunting, which falls under liquidity and stop pools.'
- id: media_cf_obsljovj780
  covers:
  - concept_trade_execution?
  link_reason: '"Get SNIPER Accurate Trading Entries" is explicitly about entry execution.'
- id: media_cf_ohg4oqfnv3g
  covers:
  - concept_trade_management?
  link_reason: '"Why Your SL Always Gets HIT" names the stop loss (SL).'
- id: media_cf_oj756ggwmzi
  covers:
  - concept_trade_management?
  link_reason: '"Manage Your Trades Like A Pro Trader" names trade management.'
- id: media_cf_onbgsi30vay
  covers:
  - concept_trade_execution?
  link_reason: '"Use This Simple CONFIRMATION to Win More Trades" refers to confirmation entries (trade execution).'
- id: media_cf_owbomehkhju
  covers:
  - concept_edge?
  link_reason: '"Retail Traders CAN Have An Edge" names trading edge directly.'
- id: media_cf_ox9l20blsn4
  covers:
  - concept_market_sentiment?
  link_reason: '"Trade AGAINST The Crowd" describes contrarian positioning against crowd sentiment.'
- id: media_cf_pclngwdlcrc
  covers:
  - concept_auction_market_theory?
  link_reason: '"Trade Value Shifts" names value migration, a core Auction Market Theory idea (balance, imbalance, value).'
- id: media_cf_phztaycy2es
  covers:
  - concept_trading_psychology?
  link_reason: '"Psychology ISN''T Your Trading PROBLEM" names trading psychology as the topic.'
- id: media_cf_pjpg2w52n5i
  covers:
  - concept_edge?
  link_reason: '"THIS Is What A REAL Edge Is" names trading edge.'
- id: media_cf_pk_kjwracke
  covers:
  - concept_trade_execution?
  link_reason: '"THIS One Candle CONFIRMS Breakouts" names a candle used as a confirmation signal.'
- id: media_cf_pmoo_zf45ta
  covers:
  - concept_trading_psychology?
  link_reason: '"Don''t Panic When Price Moves Against Them" is about emotional control.'
- id: media_cf_pskvelr0siq
  covers:
  - concept_liquidity?
  link_reason: '"SIMPLE Liquidity Strategy" names liquidity.'
- id: media_cf_pxvp6_knwpw
  covers:
  - concept_trade_management?
  link_reason: '"CUT The Trade When The Idea BREAKS" is about exiting a trade on invalidation, which is trade management (stops/exits).'
- id: media_cf_pzmra1plrda
  covers:
  - concept_market_regimes?
  link_reason: '"Get Chopped Up In Ranges" is about ranging market regimes.'
- id: media_cf_pznzl_4_pto
  covers:
  - concept_trade_execution?
  link_reason: '"The Entry Price MOST Traders Get WRONG" is about entry execution.'
- id: media_cf_q2al3tmmhdc
  covers:
  - concept_wyckoff_method?
  link_reason: '"How PROS Spot Accumulation vs Distribution" names the Wyckoff accumulation and distribution phases.'
- id: media_cf_q9e2ot6axqi
  covers:
  - concept_edge?
  link_reason: '"Reveals The TRUE EDGE" names the trading-edge concept.'
- id: media_cf_q_ax7ujqf6w
  covers:
  - concept_candlestick_patterns?
  link_reason: '"THIS Candle Pattern" names a candlestick pattern directly.'
- id: media_cf_qceck78bho0
  covers:
  - concept_price_action?
  link_reason: '"Trading Price ONLY Is NOT Enough" is about the limits of pure price action trading.'
- id: media_cf_qfuqplcztue
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"The 1:10 Trade Management Strategy" names a 1:10 risk:reward ratio.'
- id: media_cf_qicrckwhfj4
  covers:
  - strategy_marco_trades_liquidity_grab?
  link_reason: '"Chart Fanatics x MARCO" names Marco (Marco Trades), the author of the Liquidity Grab playbook.'
- id: media_cf_qrrcfedmjym
  covers:
  - concept_liquidity?
  link_reason: '"Your Stop Loss Is EXACTLY Where Institutions Want It" refers to stop pools that institutions target, i.e. liquidity.'
- id: media_cf_quvb04xk48k
  covers:
  - concept_options_greeks?
  link_reason: Title says "Understand The GREEKS", which names the options Greeks.
- id: media_cf_r4pld_yye68
  covers:
  - concept_trading_psychology?
  link_reason: '"EVERY Trader NEEDS This Mindset" clearly points to trading psychology.'
- id: media_cf_rfve7mnr__e
  covers:
  - concept_order_flow?
  link_reason: '"The A+ Orderflow Setup EXPLAINED" names order flow explicitly.'
- id: media_cf_roobfoes3co
  covers:
  - concept_market_regimes?
  link_reason: '"Get DESTROYED In Ranges" names ranging markets, a market-regime topic.'
- id: media_cf_rsketshswjk
  covers:
  - concept_trade_management?
  link_reason: '"AVOID Getting Stopped Out INSTANTLY" is about stop-loss placement, part of trade management.'
- id: media_cf_rtwdlnbw4ai
  covers:
  - concept_prop_firm_risk_rules?
  link_reason: '"The Prop Game" refers to prop-firm trading.'
- id: media_cf_rvndlg_jg5i
  covers:
  - concept_trade_execution?
  link_reason: '"Where & When To Enter" names the entry location and timing (trade execution).'
- id: media_cf_rxrnaywcmgu
  covers:
  - concept_trend_following?
  link_reason: '"MOST Trend Traders Are Getting TRAPPED" names trend traders, meaning trend following.'
- id: media_cf_sar8z2go3ki
  covers:
  - concept_options_greeks?
  link_reason: Title says "MASTER Options Trading", which names options.
- id: media_cf_smsqqtbxjc0
  covers:
  - concept_breakout_trading?
  - concept_support_resistance?
  link_reason: '"Break And Retest Trading Strategy" names a breakout followed by a level retest, which is Vincent Desiano''s Break & Retest playbook.'
- id: media_cf_snexzy6ye8i
  covers:
  - concept_market_regimes?
  link_reason: '"LOSE Money In CHOPPY Markets" names choppy (ranging) market conditions, a market-regime topic.'
- id: media_cf_t5md7lktbg8
  covers:
  - concept_trade_execution?
  link_reason: '"Broke Down His ELITE Entry Model" names an entry model.'
- id: media_cf_t_djsnbmv00
  covers:
  - concept_liquidity?
  link_reason: '"The ONE Liquidity Trading Pattern" names liquidity as the topic.'
- id: media_cf_t_fhifmihdo
  covers:
  - concept_trade_management?
  link_reason: '"REMOVE Risk As SOON As You Can" is about moving the stop to breakeven or de-risking, part of trade management.'
- id: media_cf_tg_capital
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"(1:20+ RR)" names a risk:reward ratio.'
- id: media_cf_tm0puu_lbze
  covers:
  - concept_options_greeks?
  link_reason: '"WHAT Options Traders REALLY Care About" names options trading.'
- id: media_cf_tos9dypi_ew
  covers:
  - strategy_tori_trendline_4h?
  link_reason: '"Using Tori Trade''s Simple Trading Strategy" names the playbook author, Tori Trades.'
- id: media_cf_twmnp8svqmi
  covers:
  - concept_options_greeks?
  link_reason: '"This Will Save Your Options Trading" names options trading.'
- id: media_cf_tyftskksaby
  covers:
  - concept_news_trading?
  link_reason: '"Trading Trump''s Tweets" names trading on news events.'
- id: media_cf_tyhtetarss4
  covers:
  - strategy_naoufel_taief_algorithmic?
  link_reason: '"Master ALGO Trading ... (NO Coding)" names the distinctive method of Naoufel Taief''s No-Code Algorithmic Strategy playbook.'
- id: media_cf_u8v_uhrefpo
  covers:
  - concept_support_resistance?
  link_reason: '"You''re Drawing Zones WRONG" refers to drawing support/resistance zones.'
- id: media_cf_ubt_0gbpp9m
  covers:
  - concept_liquidity?
  link_reason: '"BEST Liquidity Trap Trader" names liquidity explicitly.'
- id: media_cf_ued4nwuutzu
  covers:
  - strategy_okala_80_20_nasdaq?
  link_reason: '"The 80/20 Reversal" names the distinctive method of Okala''s 80/20 Nasdaq strategy (reactions at 20 and 80 price endings).'
- id: media_cf_uf7zswzp3by
  covers:
  - concept_market_structure?
  link_reason: '"Read Trend Structure" refers to swing/market structure.'
- id: media_cf_uhkrrqo1gqm
  covers:
  - concept_order_flow?
  link_reason: '"Trading using OrderFlow (Full Masterclass)" names order flow and matches Carmine Rosato''s "Order Flow Masterclass" playbook.'
- id: media_cf_ukj1ytgfdd8
  covers:
  - concept_liquidity?
  link_reason: '"Liquidity Traders Get THIS Wrong" names liquidity.'
- id: media_cf_uotw_smkezo
  covers:
  - concept_trade_management?
  link_reason: '"Risk Management RULE That PROTECTS Winning Trades" refers to protecting open winners with stops, breakeven or trailing.'
- id: media_cf_uub_mmgqmey
  covers:
  - concept_trade_execution?
  link_reason: '"THIS Entry Strategy" names entries as the topic.'
- id: media_cf_uxqvyunjju0
  covers:
  - concept_liquidity?
  link_reason: Title says "Master Trading Liquidity In ONLY 3 Steps", which names liquidity.
- id: media_cf_vj6eefqc4re
  covers:
  - concept_overfitting_validation?
  link_reason: '"HOW To VALIDATE Your Strategy" names strategy and edge validation, which is done by backtesting.'
- id: media_cf_vnl_ejwwtwy
  covers:
  - concept_liquidity?
  link_reason: '"Liquidity Traders Get This Wrong" names liquidity.'
- id: media_cf_vo5izoukgr4
  covers:
  - concept_multi_timeframe_analysis?
  link_reason: '"Trading using ONLY 2 Timeframes" is about multi-timeframe analysis.'
- id: media_cf_vp7hhpcciii
  covers:
  - concept_support_resistance?
  link_reason: '"STOP Waiting For PERFECT Levels" is about price levels, i.e. support/resistance.'
- id: media_cf_w57faelgdso
  covers:
  - concept_candlestick_patterns?
  link_reason: '"How MILLIONAIRE Traders Read Candles" is about candlestick reading.'
- id: media_cf_w5jggy0_jfm
  covers:
  - concept_order_flow?
  link_reason: '"Orderflow Trader Makes $3000 LIVE Trading" names order flow. The keyword matcher missed the one-word spelling.'
- id: media_cf_wbjxfbvsl84
  covers:
  - concept_trading_plan?
  link_reason: '"Mechanical Trading WILL Make You PROFITABLE" refers to trading by fixed, pre-written rules.'
- id: media_cf_wind72rumrg
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"The REAL Market Opening Time Traders Need To KNOW" is about market hours and session timing.'
- id: media_cf_wuccj1vr1iu
  covers:
  - concept_risk_reward_r_multiples?
  link_reason: '"Turns 1:2 INTO 1:10" names risk:reward ratios / R-multiples.'
- id: media_cf_x_z4crmfqns
  covers:
  - concept_trade_execution?
  link_reason: '"Where Smart Traders Enter (Not At Highs)" is about entry location.'
- id: media_cf_xeatqqgxz9m
  covers:
  - concept_order_flow?
  link_reason: '"The BEST Trades Start With TRAPPED Traders" names trapped traders, which is an order-flow idea and Trader Yush''s distinctive trapped-buyers-and-sellers method.'
- id: media_cf_xggjn4t3shy
  covers:
  - concept_trade_execution?
  link_reason: Title says "Perfect Trading Entries Using This ICT Strategy", which is about entry execution.
- id: media_cf_xlurcy5cho8
  covers:
  - concept_liquidity?
  link_reason: '"The TRUTH About Liquidity" names liquidity.'
- id: media_cf_xveo_1vc0h0
  covers:
  - concept_trade_execution?
  link_reason: '"How To CATCH The BEST Entries" is about entry execution.'
- id: media_cf_xvu8egafojg
  covers:
  - concept_auction_market_theory?
  link_reason: '"Value Areas Are Where The MOST Moneys MADE" names value areas, a core auction market theory / market profile idea of value.'
- id: media_cf_xvx_fgw5jey
  covers:
  - concept_overfitting_validation?
  link_reason: '"Your Backtest Means NOTHING Until It SURVIVES A Monte Carlo Test" is about robustness and edge validation of a backtest.'
- id: media_cf_xwktkny6cck
  covers:
  - concept_support_resistance?
  link_reason: '"Identifying Key Trading Levels" names key levels (support/resistance).'
- id: media_cf_xychcvw8a3y
  covers:
  - concept_trade_execution?
  link_reason: '"Broke Down His ELITE Entry Model" names an entry model.'
- id: media_cf_ycfpfmharma
  covers:
  - concept_trading_psychology?
  link_reason: '"Pro Traders DON''T Chase Big Moves" is about FOMO and discipline.'
- id: media_cf_ypm9oocqk_o
  covers:
  - concept_trading_plan?
  link_reason: '"How Pros Plan Trades BEFORE The Open" names pre-market trade planning.'
- id: media_cf_ywvgecj01ew
  covers:
  - concept_trading_psychology?
  link_reason: '"Traders MUST Adapt To THIS Mindset" names mindset, which is trading psychology.'
- id: media_cf_yxqm8bzl2rk
  covers:
  - concept_trading_psychology?
  link_reason: Title says "The Emotional TRAP That Blows Up Accounts", which names emotions (psychology) and blowing up accounts (ruin).
- id: media_cf_z1kguqyi9xo
  covers:
  - concept_market_regimes?
  link_reason: '"How A MILLIONAIRE Trader Trades CHOP" names choppy, ranging market conditions.'
- id: media_cf_z22me9yttjm
  covers:
  - concept_options_greeks?
  link_reason: Title says "SIMPLE Options Trading Strategy", which names options.
- id: media_cf_z5p35acclik
  covers:
  - concept_position_sizing?
  link_reason: '"WHY Trading SMALLER Can Actually Make You MORE Money" names smaller position size.'
- id: media_cf_z_tasf5wzms
  covers:
  - concept_trade_execution?
  link_reason: Title says "Waiting For Candle Closes Is KILLING Your Trades", which is about waiting for confirmation before entering.
- id: media_cf_zbt7jqqzixg
  covers:
  - concept_trade_management?
  link_reason: '"HOW To MANAGE Trades Like A PROFESSIONAL" names trade management directly.'
- id: media_cf_zeqiir_l8ey
  covers:
  - concept_liquidity?
  link_reason: '"Make MILLIONS Leveraging Liquidity" names liquidity directly.'
- id: media_cf_zhup_b6dbla
  covers:
  - concept_trading_sessions_killzones?
  link_reason: '"MAKE MONEY At Market Open" is about trading a specific session time, the open.'
- id: media_cf_zpveeycakto
  covers:
  - concept_trading_psychology?
  link_reason: Title says "How To Master Your Mind", which is trading psychology.
- id: media_cf_zyymg7pbnrc
  covers:
  - concept_market_regimes?
  link_reason: '"AVOID Getting CHOPPED By Markets" refers to choppy, ranging market conditions, which is the trend-vs-range regime topic.'
- id: media_cf_zzsj16qbgf4
  covers:
  - concept_trading_psychology?
  link_reason: '"STOPS Traders From OVERTRADING" names overtrading, a discipline problem.'
```
