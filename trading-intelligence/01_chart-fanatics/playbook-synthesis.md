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
