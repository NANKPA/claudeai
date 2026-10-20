---
id: synthesis_sniper_entries
type: synthesis
title: "Sniper Entries — codeable rules from the playbooks and the web"
partition: 10_sniper-lab
layer: L4
related: [philosophy_relationship, framework_decision_protocol, synthesis_evidence_lab, framework_source_tiers, formula_sheet, concept_liquidity_sweep_reversal, concept_liquidity, concept_fair_value_gap, concept_premium_discount_ote, concept_fibonacci, concept_order_blocks_breakers, concept_market_structure, concept_breakout_trading, concept_support_resistance, concept_vwap, concept_mean_reversion, concept_moving_averages, concept_trend_following, concept_trading_sessions_killzones, concept_amd_power_of_three, concept_scalping, concept_trade_execution, concept_order_flow, concept_volume_profile, concept_auction_market_theory, concept_backtesting, concept_overfitting_validation, concept_expectancy, strategy_marco_trades_liquidity_grab, strategy_candace_lau_nq_sweep_reversal, strategy_jadecap_liquidity_volatility, strategy_tanja_amd_futures, strategy_dhesi_liquidity_inversion, strategy_traveling_trader_universal, strategy_nbb_trader_po3_ote_adr, strategy_trader_mayne_structure_ote, strategy_matteo_conti_institutional, strategy_ariel_hernandez_real_simple, strategy_vincent_desiano_break_retest, strategy_gala_trades_price_action, strategy_jj_simon_fair_pricing, strategy_abraham_perez_ict_orderflow, strategy_tg_capital_trident, strategy_marci_silfrain_measured_move, strategy_okala_80_20_nasdaq, strategy_fabio_valentini_amt_order_flow, strategy_carmine_rosato_lvn, strategy_yush_order_flow, strategy_trader_kane_lab_model, principle_05_mathematical_justification, question_survives_costs, framework_trading_journal, principle_11_record_and_investigate, philo_practical_doctrine, philo_acb_principle, book_street_smarts, principle_02_context_before_movement, principle_03_future_is_uncertain, principle_06_do_not_force, principle_01_understand_before_acting, principle_04_conditional_probability, principle_07_respond_methodically, book_crabel_opening_range, principle_09_protect_capital, synthesis_consensus_conflicts, concept_multi_timeframe_analysis, philo_step_back, concept_position_sizing, concept_risk_of_ruin_drawdown, philo_conditional_probability, philo_mathematics_sword, principle_10_emotional_independence, principle_12_process_not_money, synthesis_pre_trade_checklist]
status: researched
---

# Sniper Entries — codeable rules from the playbooks and the web

> **Education, not financial advice.** Every rule below is a hypothesis to
> test, not a working edge. No win rate or P&L in this note is a fact about
> what these setups earn. Third-party performance figures are labelled T4
> ([[framework_source_tiers]]). The only numbers we measured ourselves are
> **how often each rule fires and how wide its stop is**. We did not
> measure whether any rule makes money.

## What "sniper" means here

In the playbooks, a "sniper entry" means three things. You mark a level
before price gets there. You wait for price to prove something at that
level, such as a sweep, a displacement or a structure shift. Then you
enter close to the level, so the invalidation is a short distance away. For
a bot that only sees OHLCV candles, that becomes:

1. **A level computed from closed candles only:** a prior-day high, a gap
   midpoint, a Fibonacci level, VWAP, an opening-range edge, an EMA.
2. **A trigger evaluated at a candle close:** reclaim, displacement,
   structure break.
3. **A resting limit order at the level,** placed after that close and
   sent post-only (maker), with a stop beyond the structure that proves the
   idea wrong.

The limit order is what keeps the stop tight and the fee at the maker
rate. It also brings the main hidden cost of limit entries: you get
filled most reliably on the trades that run straight through your level
([[concept_trade_execution]], adverse selection).

## The four findings that decide everything else

1. **Stops on BTC 5m are tiny.** Across the codeable specs, the median
   stop at fill ran from **0.08% to 0.44%** of price. The rare Trident is
   the exception at 0.70%. The 5m ATR(14) on BTC had a median of **0.14%** over the
   12 months to 2026-09-30 (our measurement; method below).
2. **On 5m, fees decide.** At a **0.20% round trip** (0.10% a side, the
   regular spot tier third-party sites report for Binance, see
   [Costs](#costs-and-the-20-account)), fees alone cost **about 0.5R to
   2.6R** per trade at the median stop, the Trident aside. Only **1 of
   3,438** BTC 5m fills in 12 months (7 of 3,120 on ETH) had a stop wide
   enough to keep fees under 0.1R. At a **0.02% round trip**, 1,378 BTC
   fills passed (40%), from 8% to 86% depending on the spec. **On a
   regular-fee venue, 5m sniper trading is mathematically untradeable on
   any account size.** Either the round trip falls to around 0.02%, or the
   bot moves up to 1h or 4h, where stops are 4 to 9 times wider.
3. **Frequency is not the problem.** On BTC 5m, the specs place between
   0.1 and 3 orders a day each. Together they place about 14 a day per
   market, and about two-thirds of those orders fill (9.4 fills a day on
   BTC). "Trading every day"
   is easy to get. Positive expectancy after costs is the hard part.
4. **No published, controlled test supports the ICT tools themselves**
   (FVG, order block, OTE). What published research does support is the
   *ingredients*. Stop and take-profit orders cluster at round numbers in
   FX (Osler). Intraday momentum exists in equities and in Bitcoin (Gao et
   al.; Shen et al.). Session timing matters. In controlled studies,
   Fibonacci levels did no better than chance. The vendor backtests we
   found were mostly negative after costs (T4). See [Evidence](#evidence).

The philosophy's frame for all four is Section VII and
[[principle_05_mathematical_justification]]: an explanation is not an
advantage until expected value after costs, over a large sample, says so.
The owner's wish to stop "waiting for 60%" fits the philosophy, because the
philosophy asks for **positive EV after costs**, not a high hit rate. A 2R
bracket breaks even at 33% before costs. Costs move that line, though.
With cost *c* in R, the break-even win rate is (1 + *c*) / (target_R + 1).
For a 2R target at *c* = 0.13R, that is 37.7%. At *c* = 1.31R, it is 77%.

---

## Shared conventions (apply to every spec)

| Item | Rule |
|---|---|
| Data | OHLCV only. Decisions happen at a candle **close**. An order decided at the close of bar *i* can fill from bar *i+1* onward. |
| Higher timeframes | Use the last **completed** 1h, 15m or 30m bar only. In a backtest, a 1h value becomes visible at that hour's close, never earlier. |
| Clock | Session windows are in **America/New_York** time, with daylight saving handled by the timezone library. The crypto "day" for prior-day levels is the **00:00 UTC** daily candle. For forex, the day starts at **17:00 New York** (rollover). |
| ATR | Wilder ATR(14) on the entry timeframe, read at the decision close. Every buffer and threshold is a multiple of ATR, so the rules scale with price and volatility. (The [Backtrex FVG test](#evidence) shows why fixed point stops drift.) |
| Swing pivots | Fractal with k = 3. A pivot high at bar *j* needs its high above the 3 bars before it and at least the 3 after it. It is **known only at bar j+3**. This lag is what removes look-ahead. |
| Orders | Entries are **post-only limit** orders (Binance lists `LIMIT_MAKER` for BTCUSDT) unless the spec says otherwise. Backtests count a limit as filled when price touches it. That is optimistic, so a stricter test requires a trade *through* the level by one tick. Stops are stop-market orders (taker, with slippage). Targets are resting limit orders (maker). |
| Ambiguous bar | If a bar touches both the stop and the target, count the stop. If a limit fills and the stop is hit in the same bar, count a loss. |
| Shorts | The exact mirror of the long rules: swap highs and lows, flip every inequality. The measurement ran the long code on the negated price series, so the mirror is exact. |
| Occupancy | One pending order or open position per spec, symbol and side. A spec that loses **twice in a session stops for the session** (Tanja Trades' and Dhesi's two-loss rule, [[strategy_tanja_amd_futures]], [[strategy_dhesi_liquidity_inversion]]). |
| **Fee gate** | Skip the order if (expected round-trip cost % + expected stop slippage %) ÷ stop % > `max_cost_r` (default **0.10**). Fees, spread and slippage are measured per venue, not assumed (see Section XIX question 4 of the philosophy, [[question_survives_costs]]). |
| Minimum size | Binance BTCUSDT spot: minimum notional **5 USDT**, quantity step 0.00001 BTC (live `exchangeInfo`, https://data-api.binance.vision/api/v3/exchangeInfo?symbol=BTCUSDT, read 2026-10-20). |
| Journal | Every order, cancel, fill and *skip* (including fee-gate skips) is a journal row ([[framework_trading_journal]], [[principle_11_record_and_investigate]]). |

---

## Measured frequency and stop size (BTC and ETH, 5m)

**Method (our measurement).** Binance spot 5m klines from the public archive
(https://data.binance.vision/data/spot/monthly/klines/BTCUSDT/5m/ and the
ETHUSDT equivalent, downloaded 2026-10-20). The sample runs from
2025-10-01 to 2026-09-30, 365 days and 105,120 bars per symbol. Each spec
below was coded with its default parameters, longs and shorts together.
"Orders" means limit orders placed (setups that triggered). "Fills" means
orders that price reached before expiry or cancellation. The stop % is
(entry − stop) ÷ entry at the fill. The run simulated exits only to free
the one-position slot. **It reports no outcome statistics**: it covers one
in-sample year, ignores costs and has no out-of-sample test. Outcomes
belong to the backtest, under [[concept_overfitting_validation]].

| Spec | BTC orders/day | BTC fills/day | BTC median stop % (IQR) | Stop in ATR | ETH orders/day | ETH median stop % | Fee drag at 0.02% / 0.20% round trip (R) | BTC fills with stop ≥ 0.2% |
|---|---|---|---|---|---|---|---|---|
| S1 PDH/PDL sweep + reclaim | 0.13 | 0.11 | 0.15 (0.09–0.26) | 0.74 | 0.14 | 0.17 | 0.13 / 1.31 | 36% |
| S2 FVG retrace | 1.55 | 1.02 | 0.19 (0.11–0.29) | 1.42 | 1.34 | 0.25 | 0.11 / 1.08 | 44% |
| S3 OTE after MSS | 1.56 | 0.93 | 0.21 (0.14–0.35) | 1.57 | 1.46 | 0.29 | 0.09 / 0.93 | 56% |
| S4 ORB + retest | 1.09 | 0.84 | 0.37 (0.20–0.53) | 1.54 | 1.05 | 0.43 | 0.05 / 0.54 | 75% |
| S5 Break + retest | 1.38 | 1.06 | 0.10 (0.07–0.15) | 0.60 | 1.32 | 0.13 | 0.20 / 2.00 | 8% |
| S6 VWAP reclaim | 0.59 | 0.50 | 0.44 (0.26–0.60) | 2.33 | 0.59 | 0.55 | 0.05 / 0.46 | 86% |
| S6 fade variant | 0.84 | 0.65 | 0.27 (0.16–0.40) | 1.27 | 0.81 | 0.37 | 0.07 / 0.74 | 67% |
| S7 EMA pullback in 1h trend | 3.04 | 2.02 | 0.17 (0.10–0.28) | 1.21 | 2.99 | 0.23 | 0.12 / 1.19 | 41% |
| S8 Asia range → London sweep | 0.36 | 0.27 | 0.08 (0.05–0.17) | 0.97 | 0.36 | 0.12 | 0.24 / 2.41 | 16% |
| S9 Round-number stop run | 1.43 | 1.12 | 0.08 (0.05–0.13) | 0.39 | 0.62 | 0.15 | 0.26 / 2.55 | 11% |
| S10 Order block (15m) | 2.02 | 0.89 | 0.13 (0.09–0.19) | 0.93 | 2.15 | 0.18 | 0.16 / 1.57 | 21% |
| S11 Trident (30m London) | 0.005 | 0.005 | 0.70 (2 fills) | 5.6 | 0.008 | 0.80 | 0.03 / 0.29 | 100% (n = 2) |
| S12 LVN absorption | not codeable on OHLCV | | | | | | | |

Context for the table, also our measurement on the same data:

- **ATR(14) median as a % of price, BTC:** 0.14% on 5m, 0.27% on 15m,
  0.60% on 1h, 1.23% on 4h. For ETH: 0.20%, 0.38%, 0.82% and 1.70%.
- **To keep fees at or below 0.1R, the stop must be at least 10× the round
  trip.** At 0.20% that means a stop of 2.0% or more, wider than a typical
  4h ATR on BTC. One BTC 5m fill in 12 months cleared it, and at most
  about 1% of any spec's ETH fills did. At 0.02% the stop needs to be 0.2% or more, which the last
  column shows.
- **EUR/USD 5m:** the median ATR(14) is **2.2 pips**, and 2.8 pips in the
  08:00–11:00 New York window (Yahoo 5m bars, 2026-07-28 to 2026-10-20,
  https://query1.finance.yahoo.com/v8/finance/chart/EURUSD=X?interval=5m&range=60d,
  read 2026-10-20). A retail EUR/USD spread of about **0.9 pips** (OANDA
  figure on BrokerChooser, a T3 search-result summary,
  https://brokerchooser.com/he/broker-reviews/oanda-review/oanda-eurusd-spread,
  read 2026-10-20) costs about **0.4R on a 1-ATR stop**. 5m forex sniping
  is also bound by costs, so 15m or 1h is the realistic floor. Yahoo FX
  bars carry **no volume**, so S6 (VWAP) cannot run on forex from this
  feed.
- **Signals per day across all specs:** about 14 orders and 9 fills per
  day per crypto market (BTC 14.0 and 9.4, ETH 12.8 and 8.6). That is the "trades every day" the owner asked
  about, *before* the fee gate removes most of them on a regular-fee
  venue.

---

## The specs

Each spec gives the long rules (shorts mirror them), its parameters with
defaults, where it comes from, what we measured, why it should work, what
undermines it, and the principles of
[[philo_practical_doctrine]] it touches. Section III's A → C → B frame
([[philo_acb_principle]]) applies to all of them. The sweep or the pullback
is the move against the idea (C). The target is B, which is a hypothesis.
The stop is the written point where C stops being a detour and becomes
evidence that the structure changed.

### S1 · `sniper_pdhl_sweep_reclaim` — prior-day high/low sweep + reclaim

**Comes from.** Marco Trades' rule of buying only below a swept low and
selling only above a swept high ([[strategy_marco_trades_liquidity_grab]]). Candace Lau's sweep, then
confirmed reversal ([[strategy_candace_lau_nq_sweep_reversal]]). Jadecap's
New York raid of the prior-day and session levels
([[strategy_jadecap_liquidity_volatility]]). The generic rules in
[[concept_liquidity_sweep_reversal]] and [[concept_liquidity]]. The older
lineage is Raschke and Connors' Turtle Soup ([[book_street_smarts]]): a
stop order back inside a failed 20-day breakout (rules as summarised by
WH SelfInvest, https://www.whselfinvest.de/en/trading_strategies_38_Turtle_Soup.php,
search result read 2026-10-20, T3).

**Rules (long).**
- *Level:* the prior day's low (PDL). It must be **untouched today**. If
  price traded below it earlier in the day, including outside the windows,
  the level is spent.
- *Setup:* inside a window, a 5m bar trades below PDL. Within **3 bars**
  (that bar plus 2 more), a 5m bar **closes back above PDL**. The deepest
  low reached must be no more than 1.5 ATR below PDL. A deeper break is
  treated as a breakdown, not a grab.
- *Entry:* at the reclaim close, place a **post-only limit buy at PDL**
  (the retest of the reclaimed level). It expires after 6 bars.
- *Stop:* the sweep low minus 0.1 ATR.
- *Target:* 2R. Structural option: the prior-day midpoint or PDH.
- *Time:* the sweep and reclaim must happen inside 02:00–05:00 or
  08:00–11:00 New York time. The position closes at market after 48 bars
  (4h).
- *Invalidation:* a 5m close below the sweep low before the fill cancels
  the order. No reclaim within 3 bars spends the level for the day.

**Parameters:** `day_anchor="00:00 UTC"` (forex `"17:00 NY"`),
`windows=["02:00-05:00","08:00-11:00"]`, `reclaim_bars=3`,
`max_sweep_depth_atr=1.5`, `entry="level"`, `expiry_bars=6`,
`stop_buffer_atr=0.1`, `target_r=2.0`, `max_hold_bars=48`, `atr_len=14`.

**Measured.** 0.13 orders a day on BTC. It is rare, because a prior-day
extreme usually gets taken in only one of the windows. The median stop is
0.15%. At a 0.20% round trip, fees cost 1.31R.

**Why it should work.** Stops and breakout orders rest just beyond obvious
extremes. Osler found executed stop-loss orders clustered just beyond
round-number support and resistance, and noted that hitting them speeds up
the move (NY Fed Staff Report 125,
https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf,
read 2026-10-20). A fast reclaim shows the triggered orders were absorbed
rather than followed.

**What undermines it.** A sweep that keeps going is simply a breakout. That
is why every source treats the sweep as context, not a trigger (LuxAlgo,
https://www.luxalgo.com/library/concept/liquidity-sweep/, read 2026-10-20,
T3). The tight stop (0.74 ATR) puts it right next to fees. In the one
published systematic test of a sweep-reclaim (equal lows on the Dow, 1m),
the vendor reports a positive result on only **70 trades** (T4, see
Evidence). That sample is far too small to trust (Section VI).

**Principles.** [[principle_02_context_before_movement]] (a sweep is
movement inside a structure until the reclaim fails),
[[principle_03_future_is_uncertain]] (the invalidation is written before
entry), [[principle_06_do_not_force]] (no reclaim means no trade),
[[principle_05_mathematical_justification]] (the fee drag).

### S2 · `sniper_fvg_displacement_retrace` — FVG retrace after displacement

**Comes from.** Tanja Trades only trades the retrace into the FVG that
displacement left, and never chases ([[strategy_tanja_amd_futures]]).
Traveling Trader's sequence is catalyst, displacement, retracement
([[strategy_traveling_trader_universal]]). Dhesi's FVG inversion speed test
([[strategy_dhesi_liquidity_inversion]]). The three-candle definition and
consequent encroachment come from [[concept_fair_value_gap]]. The idea that
only displacement that broke structure counts comes from
[[concept_market_structure]].

**Rules (long).**
- *Displacement (candle c2):* body ≥ **1.0 × ATR**, body ÷ range ≥ 0.6,
  and a close above the highest high of the 12 bars before it. That is the
  local structure break.
- *Gap:* at the close of c3, low(c3) > high(c1), and the gap is at least
  0.2 ATR.
- *Context filter:* the last completed 1h close is above the 1h EMA(50).
- *Entry:* a post-only **limit at the gap's 50% (consequent
  encroachment)**, placed at the c3 close and valid for 12 bars. Option:
  the proximal edge, low(c3).
- *Stop:* the low of c1 minus 0.1 ATR (the origin of the displacement).
- *Target:* 2R. Option: the displacement high.
- *Time:* c3 must close inside the kill zones (02:00–05:00, 08:00–11:00
  New York). Maximum hold is 48 bars.
- *Invalidation:* a 5m close below high(c1) before the fill cancels the
  order. The gap has been closed through and is now an inversion.

**Parameters:** `disp_body_atr=1.0`, `disp_body_ratio=0.6`,
`structure_lookback=12`, `min_gap_atr=0.2`, `entry_level=0.5`,
`expiry_bars=12`, `stop="c1_low"`, `stop_buffer_atr=0.1`, `target_r=2.0`,
`htf_filter="1h close > EMA50"`, `windows=kill_zones`.

**Measured.** 1.55 orders a day on BTC, and 66% fill. The median stop is
0.19%. At a 0.20% round trip, fees cost 1.08R.

**Why it should work.** A displacement candle means one side traded
aggressively, and the gap is the price range that traded only one way.
Price often comes back into recent ranges. The rule bets that the side
that displaced defends the gap's midpoint.

**What undermines it.** Gap fills are common **by construction**, because
price revisits most recent ranges. A fill rate on its own proves nothing.
One TradingView author compares post-gap outcomes against placebo zones of
the same size, and reports that a 50% baseline made the same gaps look
significantly profitable in one period and significantly unprofitable in
another (https://www.tradingview.com/script/Kbq3WncE-Fair-Value-Gap-FVG-Statistics-with-Placebo-Control/,
listing text read 2026-10-20, T3). The vendor tests of FVG entries were
weak or negative (T4, see Evidence). **Backtest S2 against random zones of
the same size.**

**Principles.** [[principle_01_understand_before_acting]],
[[principle_04_conditional_probability]] (the gap only counts conditional
on displacement and the 1h trend), [[principle_05_mathematical_justification]]
(the placebo baseline).

### S3 · `sniper_ote_mss` — OTE (0.62–0.79) retrace after a sweep and structure shift

**Comes from.** NBB Trader's fixed-geometry Fibonacci entries: stop at
1.0, first target at 0.0, so the R depends only on the entry level
([[strategy_nbb_trader_po3_ote_adr]]). Trader Mayne's sweep, then market
structure break, then retest ([[strategy_trader_mayne_structure_ote]]).
The concepts are [[concept_premium_discount_ote]] and
[[concept_fibonacci]]. The band definition is 61.8% to 79%, with 70.5% as
the midline (LuxAlgo, https://www.luxalgo.com/library/concept/optimal-trade-entry/,
read 2026-10-20, T3).

**Rules (long).**
- *Structure:* track confirmed 5m pivots (k = 3). Let *PH* be the last
  confirmed pivot high, formed within the last 48 bars.
- *Sweep:* the lowest low since *PH* is below the last confirmed pivot low
  that formed **before** *PH*. Sell-side liquidity was taken. The sweep low
  must sit no more than 36 bars before the shift.
- *Shift (MSS):* a 5m close crosses above *PH* (the previous close was at
  or below it), with a body of at least 0.5 ATR.
- *Leg:* level 1.0 is the sweep low and level 0.0 is the highest high
  since the sweep. The leg must be at least 2 ATR.
- *Entry:* a post-only **limit at the 0.705 retracement**. While unfilled,
  each close re-anchors 0.0 to any new high and moves the limit with it.
  Options: 0.62 or 0.79. The order is valid for 24 bars.
- *Stop:* the sweep low minus 0.1 ATR.
- *Target:* level 0.0 (the leg high). Skip the setup if that gives less
  than 1.5R at placement. Before the buffer, NBB's geometry gives
  x ÷ (1 − x) = 2.39R at 0.705.
- *Time:* the shift must happen in the kill zones. Maximum hold is 48
  bars.
- *Invalidation:* a trade below the sweep low before the fill.

**Parameters:** `pivot_k=3`, `max_ph_age=48`, `max_sweep_age=36`,
`mss_body_atr=0.5`, `min_leg_atr=2.0`, `fib_entry=0.705`,
`fib_stop=1.0`, `stop_buffer_atr=0.1`, `target="fib_0"`, `min_r=1.5`,
`expiry_bars=24`, `reanchor=true`.

**Measured.** 1.56 orders a day on BTC, and 60% fill. The median stop is
0.21%. At a 0.20% round trip, fees cost 0.93R.

**Why it should work.** The sweep takes liquidity and the shift shows the
other side took control. A deep retrace lets you join that new leg with a
stop at its origin, which forces good location ([[concept_premium_discount_ote]]).

**What undermines it.** Fibonacci ratios have **no special predictive
standing** in the controlled studies. A City University thesis tested
turning points in the Dow Jones and found ratio anchoring no more often
than chance (https://openaccess.city.ac.uk/id/eprint/18945/, read
2026-10-20, T1). A 2022 *Expert Systems with Applications* study found
that price bounces near retracement zones, but that Fibonacci zones did
not differ from non-Fibonacci zones (Tsinaslanidis, Guijarro and
Voukelatos, vol. 187, 115893; abstract as summarised in a search result,
https://www.datalearner.com/academic/journal-papers/0957-4174/volumes-and-issues/391/paper-detail/17703,
read 2026-10-20, T1 paper, not read in full). So 0.705 is a **location
and R:R device, not a magic level**. Test 0.5 and 0.79 alongside it. The
re-anchoring rule also has to be coded exactly, or the backtest will look
ahead.

**Principles.** [[principle_03_future_is_uncertain]] (0.0 is B, a
hypothesis), [[principle_05_mathematical_justification]],
[[principle_07_respond_methodically]] (the re-anchoring is mechanical, not
a decision made mid-trade).

### S4 · `sniper_orb_retest` — opening-range breakout + retest

**Comes from.** Matteo Conti's ORB research model: a 9:30–10:00 range, a
close beyond it (not a touch), a 1–2R target and a 15:30 time exit
([[strategy_matteo_conti_institutional]]). Ariel Hernandez's 5-minute
opening-range break ([[strategy_ariel_hernandez_real_simple]]). The
concept is [[concept_breakout_trading]]. The lineage is Crabel's opening
range breakout ([[book_crabel_opening_range]]).

**Rules (long).**
- *Range:* the high and low of the 6 five-minute bars from **09:30 to
  10:00 New York** (the US equity open, when US participation arrives in
  crypto too).
- *Breakout:* the **first** 5m close above the range high + 0.1 ATR,
  between 10:00 and 12:00. Only one attempt per side per day.
- *Entry:* a post-only **limit at the range high** (the retest), valid for
  12 bars.
- *Stop:* the range midpoint.
- *Target:* 2R. Close everything by **15:30 New York** if neither the stop
  nor the target is hit.
- *Invalidation:* a close below the midpoint before the fill. A failed
  breakout means no re-entry that day.

**Parameters:** `session_open="09:30 NY"`, `or_minutes=30`,
`break_window="10:00-12:00"`, `break_buffer_atr=0.1`, `entry="or_edge"`,
`stop="or_mid"`, `target_r=2.0`, `time_exit="15:30 NY"`,
`expiry_bars=12`. Variants to test separately: London open at 03:00 New
York, the 00:00 UTC crypto daily open, and Matteo's original
(market-on-close entry, stop at the far side of the range).

**Measured.** 1.09 orders a day on BTC, and 77% fill. The median stop is
0.37%, among the widest of the specs. At a 0.20% round trip, fees cost
0.54R.

**Why it should work.** Opening ranges bundle the session's first order
imbalance. Gao, Han, Li and Zhou find that the first half-hour return
predicts the last half-hour return in the S&P 500 ETF, more strongly on
volatile and high-volume days (*Journal of Financial Economics* 2018,
https://profiles.wustl.edu/en/publications/market-intraday-momentum/, read
2026-10-20, T1). For Bitcoin, Shen, Urquhart and Wang use volume to define
the session and find the same first-to-last half-hour momentum
(*Financial Review* 2022,
https://research.birmingham.ac.uk/en/publications/bitcoin-intraday-time-series-momentum/,
read 2026-10-20, T1).

**What undermines it.** The ORB papers by Zarattini, Barbon and Aziz report
large net returns for US "stocks in play", 2016–2023 (more than 1,600%
net and a Sharpe of 2.81 for a top-20 portfolio, as summarised on the
authors' own site,
https://concretumgroup.com/a-profitable-day-trading-strategy-for-the-u-s-equity-market/,
read 2026-10-20). Those figures are **T4**: self-reported, in-sample, from
authors with commercial interests. A replication summarised by search
reproduced the gross result on NQ but found nothing distinguishable from
zero after costs across five indices (MQL5 blog,
https://www.mql5.com/en/blogs/post/776235, search-result summary read
2026-10-20, not opened, T4). Intraday momentum in the papers is a weak
effect (R² of about 0.02 in the early SPY version, per Alpha Architect,
https://alphaarchitect.com/2014/08/attention-prop-traders-the-first-half-hour-of-trading-predicts-the-last-half-hour/,
search result read 2026-10-20, T3). It is not a 2R bracket.

**Principles.** [[principle_04_conditional_probability]] (a session-open
effect may not carry over from US equities to 24/7 crypto),
[[principle_05_mathematical_justification]].

### S5 · `sniper_break_retest` — break and retest of a key level

**Comes from.** Vincent Desiano: never trade the break itself, only the
retest, and skip the trade when no retest comes
([[strategy_vincent_desiano_break_retest]]). Gala
Trades' breaking retest of hourly levels
([[strategy_gala_trades_price_action]]). Abraham Perez's break-and-retest
continuation ([[strategy_abraham_perez_ict_orderflow]]). The concepts are
[[concept_support_resistance]] and [[concept_breakout_trading]].

**Rules (long).**
- *Levels:* PDH, and the last confirmed 1h pivot high (k = 3 on the 1h
  chart, known 3 hours after the pivot). Each level is used once per day.
- *Break:* a 5m close above the level + 0.2 ATR, after a previous close at
  or below it, with a body of at least 0.6 ATR (momentum). Between 03:00
  and 12:00 New York.
- *Entry:* a post-only **limit at level + 0.1 ATR**, which front-runs the
  retest slightly. Valid for 12 bars.
- *Stop:* the level − 0.5 ATR.
- *Target:* 2R. Desiano's TP1 is the prior high, with 25–50% taken off
  there. Maximum hold is 48 bars.
- *Invalidation:* a close below the stop level before the fill.
- *Strict variant (not measured):* wait for a retest candle whose low is at
  or below the level and which closes above it, then go **market-on-close**,
  with the stop below that candle's low − 0.1 ATR (Desiano's confirmation
  candle).

**Parameters:** `levels=["PDH","1h_pivot_high"]`, `break_buffer_atr=0.2`,
`break_body_atr=0.6`, `entry_offset_atr=0.1`, `stop_atr_below_level=0.5`,
`target_r=2.0`, `window="03:00-12:00 NY"`, `expiry_bars=12`.

**Measured.** 1.38 orders a day on BTC, and 76% fill. The median stop is
**0.10%** (0.6 ATR), the tightest of the codeable specs. At a 0.20% round
trip, fees cost **2.0R**. Only 8% of fills cleared even the 0.02% fee gate.

**Why it should work.** A broken level changes role, because orders that
defended it become trapped and add fuel on the retest
([[concept_support_resistance]]). Osler's second prediction is that trends
gain momentum once support and resistance are crossed, and she traces it to
stop-loss orders clustered just beyond those levels (SR125, read
2026-10-20, T1).

**What undermines it.** As taught, the stop is too tight for 5m costs.
Vendor tests of plain breakouts in FX lost money (PDH/PDL breakout on
GBPUSD, T4, see Evidence). A retest limit fills on every failed break,
which is exactly the adverse-selection case.

**Principles.** [[principle_06_do_not_force]] (no retest means no trade),
[[principle_05_mathematical_justification]] (the cost math disqualifies
the taught stop on 5m), [[principle_09_protect_capital]].

### S6 · `sniper_vwap_reclaim` — VWAP reclaim retest (with a 2σ fade variant)

**Comes from.** Matteo Conti's VWAP trend model: long on a close above
VWAP, exit on a cross back below ([[strategy_matteo_conti_institutional]]).
JJ Simon's reversion toward a fair price after a confirmed momentum shift,
with the Three-Loss Rule ([[strategy_jj_simon_fair_pricing]]). Abraham
Perez's use of VWAP and POC as support for the trade
([[strategy_abraham_perez_ict_orderflow]]). The concepts are
[[concept_vwap]] and [[concept_mean_reversion]].

**Rules (long, reclaim mode, the default).**
- *VWAP:* anchored at **00:00 UTC**, using typical price × volume. σ is the
  volume-weighted standard deviation of typical price since the anchor.
  Requires at least 8h (96 bars) since the anchor.
- *Setup:* within the last 36 bars, at least one close at or below VWAP −
  1.5σ (price was stretched below value). The 12 closes before now were
  all below VWAP. Now a 5m close **above VWAP**, with a body of at least
  0.3 ATR.
- *Entry:* a post-only **limit at VWAP** (its value at the signal close),
  valid for 12 bars.
- *Stop:* the entry minus max(1σ, 0.75 ATR).
- *Target:* 2R (close to VWAP + 2σ when σ sets the stop).
- *Time:* 08:00–16:00 New York, once per side per day. Maximum hold is 48
  bars.
- *Invalidation:* a close below the stop before the fill.

**Fade mode (variant).** The previous close was below VWAP − 2σ and this
close is back above it. Place a limit at VWAP − 2σ. The stop is the lowest
low of the last 6 bars − 0.25 ATR. The target is VWAP itself, and the
target must be at least as far as the stop (R ≥ 1). Valid for 6 bars. Skip
the fade after 3 losing fades in a session (JJ Simon's Three-Loss Rule:
the market may be trending and setting a new fair value).

**Parameters:** `anchor="00:00 UTC"`, `min_bars_since_anchor=96`,
`stretch_sigma=1.5`, `stretch_lookback=36`, `below_bars=12`,
`reclaim_body_atr=0.3`, `stop="max(1 sigma, 0.75 ATR)"`, `target_r=2.0`,
`window="08:00-16:00 NY"`, `mode="reclaim"|"fade"`, `fade_sigma=2.0`,
`fade_min_r=1.0`, `fade_session_loss_limit=3`.

**Measured.** Reclaim: 0.59 orders a day on BTC, 84% fill, median stop
**0.44%** (2.3 ATR). At a 0.20% round trip, fees cost 0.46R. It is the
cheapest spec to trade after the rare Trident. Fade: 0.84 orders a day,
median stop 0.27%.

**Why it should work.** VWAP is the benchmark that institutional execution
is measured against ([[concept_vwap]]). A reclaim after a stretch says the
session's average participant is back in profit on the long side.
Zarattini and Aziz report that a long-above / short-below VWAP rule on QQQ,
2018–2023, turned $25,000 into $192,656 net of commissions
(https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/,
read 2026-10-20). That figure is **T4**: self-reported and in-sample, with
commissions but not spread or slippage.

**What undermines it.** Trend days walk along the band, and fades get
stopped repeatedly. A vendor test of fading every 2σ close on the DAX 15m
lost about 99% over 8,943 trades. Its target was smaller than its stop
(T4, see Evidence). Our fade variant requires R ≥ 1 for that reason. Trend
following and mean reversion conflict here
([[synthesis_consensus_conflicts]]): the reclaim mode is the trend reading,
the fade the reversion reading, so test them separately. Crypto only, since
forex OHLCV from free feeds has no real volume.

**Principles.** [[principle_04_conditional_probability]] (a trend-day
reading versus a range-day reading), [[principle_07_respond_methodically]]
(the three-loss rule), [[principle_05_mathematical_justification]].

### S7 · `sniper_ema_pullback_htf` — trend pullback to EMA in a higher-timeframe trend

**Comes from.** TG Capital's EMA-stack gate: if the EMAs are tangled,
there is no trade ([[strategy_tg_capital_trident]]). Traveling Trader's
retest of the 21 EMA ([[strategy_traveling_trader_universal]]). Marci
Silfrain's preference for the first or second structure of a fresh trend,
and her measured-move target ([[strategy_marci_silfrain_measured_move]]). The concepts are
[[concept_moving_averages]], [[concept_trend_following]] and
[[concept_multi_timeframe_analysis]].

**Rules (long).**
- *Higher-timeframe trend:* the last completed 1h bar has close > EMA(50) >
  EMA(200).
- *Entry-timeframe trend:* on 5m, EMA(9) > EMA(21) > EMA(50). Count the
  pullbacks (fresh touches of EMA(21)) since the stack last formed. Only
  the **first two** qualify, following Silfrain's early-structure rule.
- *Extension first:* the highest high of the last 13 bars is at least
  EMA(21) + 1.5 ATR, and the current bar's low is still above EMA(21).
- *Entry:* a post-only **limit at EMA(21)**, cancelled and replaced at
  each close at the new EMA value. It is cancelled when the stack breaks.
  Valid for up to 12 bars.
- *Stop:* EMA(50) − 0.5 ATR, recomputed with the order and fixed at the
  fill. The distance must be between 0.5 and 3 ATR.
- *Target:* 2R. Variant: Silfrain's measured move (impulse length
  projected from the pullback low).
- *Time:* 02:00–16:00 New York. Maximum hold is 48 bars.
- *Invalidation:* the 5m stack breaks before the fill.

**Parameters:** `htf="1h"`, `htf_rule="close>EMA50>EMA200"`,
`ltf_emas=[9,21,50]`, `max_pullback_index=2`, `extension_atr=1.5`,
`extension_lookback=12`, `entry_ema=21`,
`stop="EMA50 - 0.5 ATR"`, `stop_atr_range=[0.5,3.0]`, `target_r=2.0`,
`window="02:00-16:00 NY"`, `expiry_bars=12`.

**Measured.** 3.04 orders a day on BTC, the most frequent spec, with 67%
fill. The median stop is 0.17%. At a 0.20% round trip, fees cost 1.19R.

**Why it should work.** It joins an existing trend at a pullback, which is
the most robust family in the long-run evidence ([[concept_trend_following]]).
In high-frequency Bitcoin data, Corbet, Eraslan, Lucey and Sensoy found
significant support for moving-average rules
(*Finance Research Letters* 2019,
https://ideas.repec.org/a/eee/finlet/v31y2019icp32-37.html, read
2026-10-20, T1).

**What undermines it.** Svogun and Bazán-Palomino tested 69
moving-average and breakout rules on daily and 1-minute data, with and
without costs, 2016–2021. Whether the best rules beat buy-and-hold depended
on the coin and on bubble periods. Bitcoin did not gain from bubble periods
(*JIFMIM* 2022,
https://ideas.repec.org/a/eee/intfin/v79y2022ics1042443122000816.html,
read 2026-10-20, T1). EMA lengths invite parameter fishing
([[concept_overfitting_validation]]). Fix 9/21/50 and 50/200 before
testing, and never tune them on the test data.

**Principles.** [[principle_02_context_before_movement]] (the 1h trend
frames the 5m pullback, so the pullback is C on the way to B),
[[principle_04_conditional_probability]].

### S8 · `sniper_asia_london_judas` — Asia range → London sweep → return (session liquidity model)

**Comes from.** Candace Lau's London model, in which the Asia range is the
default liquidity pool ([[strategy_candace_lau_nq_sweep_reversal]]). NBB
Trader's sequence of Asia accumulation, London manipulation and New York
distribution ([[strategy_nbb_trader_po3_ote_adr]]). Jadecap's Asian and
London session levels ([[strategy_jadecap_liquidity_volatility]]). The
concepts are [[concept_amd_power_of_three]] and
[[concept_trading_sessions_killzones]].

**Rules (long, after the Asia low is swept).**
- *Asia range:* the high and low of the 5m bars opening from 20:00 to
  23:55 New York.
- *Accumulation filter:* the Asia range is at most **0.5 × the average
  daily range of the last 10 days**, so it really was a compressed range.
- *Manipulation:* between 02:00 and 05:00 New York, price trades below the
  Asia low by at least 0.05 ATR.
- *Return:* within 6 bars of the sweep, a 5m close above the Asia low + 0.1
  ATR.
- *Entry:* a post-only **limit at the Asia low**. It expires at 05:00 New
  York or after 12 bars, whichever comes first.
- *Stop:* the sweep extreme − 0.1 ATR.
- *Target:* the **Asia high** (distribution to the opposite side). Skip the
  setup if that gives less than 1.5R.
- *Time:* flat by 11:00 New York. One setup per side per day.
- *Invalidation:* a close below the sweep extreme before the fill, or no
  return within 6 bars.

**Parameters:** `asia="20:00-24:00 NY"`, `max_range_adr=0.5`,
`adr_days=10`, `london="02:00-05:00 NY"`, `sweep_atr=0.05`,
`return_bars=6`, `return_atr=0.1`, `entry="asia_extreme"`,
`stop_buffer_atr=0.1`, `target="opposite_asia_extreme"`, `min_r=1.5`,
`flat_by="11:00 NY"`.

**Measured.** 0.36 orders a day on BTC. The median stop is **0.08%**,
because the return happens close to the swept level. At a 0.20% round
trip, fees cost 2.41R. Only 16% of fills cleared even the 0.02% gate. Wider
variants, such as a stop at the sweep extreme minus 1 ATR, have to be
tested before this model is usable on 5m.

**Why it should work.** Session timing matters. Liquidity and volatility
step up at the London open ([[concept_trading_sessions_killzones]]).
Breedon and Ranaldo document time-of-day patterns in FX returns: currencies
tend to weaken during their own local trading hours, and the pattern shows
up in order flow (SNB Working Paper 2011-04,
https://www.snb.ch/en/publications/research/working-papers/2011/working_paper_2011_04,
read 2026-10-20, T1). Session-dependent flows are real, which is the
precondition for a session model.

**What undermines it.** The opposite reading, a London *breakout* of the
Asia range, lost money in vendor tests on GBPUSD 15m (−60% over 2,432
trades) and EURUSD 1h (−28%) (T4, see Evidence). That says nothing direct
about the fade. It does show that the Asia range's edges are not a free
lunch. For 24/7 crypto, "Asia" is a time window, not a market that closes.

**Principles.** [[principle_04_conditional_probability]] (session- and
compression-conditional), [[principle_06_do_not_force]] (no compression or
no return means no trade), [[principle_02_context_before_movement]].

### S9 · `sniper_round_number_sweep` — round-number stop run + reclaim

**Comes from.** Okala's reactions at price endings, location first and
structure second ([[strategy_okala_80_20_nasdaq]]). The 20/80 endings are
NQ-specific, so this spec generalises them to the round numbers where
Osler measured order clustering. Also Marco Trades' trap logic
([[strategy_marco_trades_liquidity_grab]]) and the concept
[[concept_support_resistance]].

**Rules (long).**
- *Grid:* BTC every $1,000, ETH every $100, EUR/USD every 0.0050.
- *Level:* the nearest grid line below the previous close, which must have
  been approached from above: the last 12 closes were all above it.
- *Setup:* a 5m bar trades at least 0.05 ATR below the level, no more than
  1.0 ATR below it, and **closes back above it**.
- *Entry:* a post-only **limit at the round number**, valid for 6 bars.
- *Stop:* the bar's low − 0.1 ATR.
- *Target:* 2R.
- *Time:* 02:00–16:00 New York. Each level once per day.
- *Invalidation:* a close below the stop before the fill.

**Parameters:** `grid={"BTC":1000,"ETH":100,"EURUSD":0.0050}`,
`approach_bars=12`, `min_poke_atr=0.05`, `max_poke_atr=1.0`,
`expiry_bars=6`, `stop_buffer_atr=0.1`, `target_r=2.0`,
`window="02:00-16:00 NY"`.

**Measured.** 1.43 orders a day on BTC and 0.62 on ETH. The median stop is
**0.08%** (0.39 ATR). At a 0.20% round trip, fees cost 2.55R.

**Why it should work.** Osler's dealing-bank order data showed stop-loss
and take-profit orders clustered strongly at round numbers, in different
patterns. Take-profits sit at the number, which supports reversals there.
Stop-losses sit just beyond it, which accelerates moves through it (SR125,
read 2026-10-20, T1). A poke through and a close back means the stops
beyond the number fired without follow-through.

**What undermines it.** That evidence comes from FX dealing-bank orders in
1999–2000. For Bitcoin, Urquhart found price **clustering** at round
numbers, but **no significant pattern of returns after the round number**
(*Economics Letters* 2017,
https://ideas.repec.org/a/eee/ecolet/v159y2017icp145-148.html, read
2026-10-20, T1). Urquhart's round numbers are price endings in 00 cents,
not $1,000 levels. The stop is the tightest of any spec, so on 5m it is
dominated by fees.

**Principles.** [[principle_01_understand_before_acting]] (there is a
defensible mechanism), [[principle_04_conditional_probability]] (FX
evidence does not automatically transfer to BTC),
[[principle_05_mathematical_justification]].

### S10 · `sniper_ob_mean_threshold` — order-block retest at the 50% after a 15m break of structure

**Comes from.** Trader Mayne's point of interest: the order block that
caused the break, in the discount half, with external liquidity as the
target ([[strategy_trader_mayne_structure_ote]]). The concept is
[[concept_order_blocks_breakers]].

**Rules (long).**
- *Break (15m):* a 15m close crosses above the last confirmed 15m pivot
  high (k = 3), with a body of at least 0.8 × ATR(14, 15m).
- *Dealing range:* from the lowest low of the last 21 15m bars to the high
  of the break bar.
- *Order block:* the most recent **down-close** 15m candle within the 8
  bars before the break bar.
- *Discount:* the order block's 50% (mean threshold) sits at or below the
  dealing range's 50%.
- *Entry:* a post-only **limit at the order block's 50%**, executed on 5m
  bars, valid for 48 five-minute bars (4h).
- *Stop:* the order block's low − 0.1 × ATR(15m).
- *Target:* the dealing-range high (external liquidity). Skip the setup if
  that gives less than 1.5R.
- *Time:* no window in the measured default. A kill-zone filter is an
  option. Maximum hold is 96 five-minute bars.
- *Invalidation:* a 5m close below the order block's low before the fill.

**Parameters:** `htf="15m"`, `pivot_k=3`, `bos_body_atr=0.8`,
`range_lookback=21`, `ob_lookback=8`, `entry="mean_threshold"`,
`discount_max=0.5`, `stop_buffer_atr=0.1`, `target="range_high"`,
`min_r=1.5`, `expiry_5m_bars=48`.

**Measured.** 2.02 orders a day on BTC but only **44% fill**, because many
breaks never return to the block. The median stop is 0.13%. At a 0.20%
round trip, fees cost 1.57R.

**Why it should work.** The order block marks where the side that broke
structure last added size. The 50% of a discount block is a location with
the stop at the block's far edge.

**What undermines it.** The concept note itself warns that order blocks
are confluence, not stand-alone triggers. A vendor test of order-block
retests on GBPUSD 1h with a change-of-character exit lost money over 203
trades (T4, see Evidence). Which candle counts as the last opposite one is
very sensitive to how far back you look, so fix `ob_lookback` before
testing.

**Principles.** [[principle_05_mathematical_justification]],
[[principle_02_context_before_movement]].

### S11 · `sniper_trident_london_fvg` — TG Capital Trident (30m London FVG + doji at 50% + confirmation)

**Comes from.** [[strategy_tg_capital_trident]], with
[[concept_fair_value_gap]] and [[concept_moving_averages]].

**Rules (long).**
- *Timeframe:* 30m. The EMAs are read on 30m, which is our choice, since
  the playbook does not name the timeframe.
- *Bias:* the 30m close is above EMA(200), and EMA(5) > EMA(9) > EMA(13) >
  EMA(21).
- *Gap:* a three-candle 30m FVG whose third candle closes between **02:30
  and 04:00 New York**.
- *Trident candle (c4):* body ≤ 0.3 × its range. Its low reaches the
  gap's 50% but stays above the top of c1, so the gap is not fully filled.
- *Confirmation (c5):* closes **above c4's high**. The page's wording reads
  inverted for a long; this is our reading, and the KB note flags it.
- *Entry:* **market on close of c5** (TG's default). The c5 close must fall
  between 03:00 and 06:30 New York. Variant: a post-only limit at the gap's
  50%.
- *Stop:* the low of c1 − 0.1 ATR.
- *Target:* 3R. The playbook uses daily structure, which is not defined.
  Maximum hold is 48h.
- *Invalidation:* a close below the stop.

**Parameters:** `tf="30m"`, `fvg_close_window="02:30-04:00 NY"`,
`entry_window="03:00-06:30 NY"`, `doji_body_ratio=0.3`,
`emas=[5,9,13,21,200]`, `entry="market_on_close"`, `stop="c1_low"`,
`target_r=3.0`, `max_hold_hours=48`.

**Measured.** **2 setups in 12 months on BTC and 3 on ETH.** The stop is
wide (0.7–0.8%), so fees are a small fraction of risk. The playbook itself
says setups come only a handful of times a year.

**Why it should work.** It stacks location (the gap's 50%), a rejection
candle, a strict trend filter and a time window. It is the most mechanical
playbook in the KB.

**What undermines it.** At about 2 trades a year per market, it **cannot
be validated** in any useful time. Section VI needs hundreds of trades, not
a handful. Treat it as a scanner alert, not a bot strategy. The confirmation
rule is ambiguous on the source page.

**Principles.** [[principle_06_do_not_force]] (long waits by design),
[[principle_05_mathematical_justification]] (sample size), and
[[philo_step_back]].

### S12 · `sniper_lvn_absorption` — LVN revisit with order-flow absorption (needs order-flow data, NOT codeable on OHLCV)

**Comes from.** Fabio Valentini's market state, then location, then
aggression ([[strategy_fabio_valentini_amt_order_flow]]). Carmine Rosato's
LVN defence ([[strategy_carmine_rosato_lvn]]). Trader Yush's trapped
traders ([[strategy_yush_order_flow]]). Abraham Perez's playbook puts the
idea in a phrase: "liquidity can attract price, but aggression moves
price" ([[strategy_abraham_perez_ict_orderflow]]). The concepts are
[[concept_volume_profile]], [[concept_order_flow]] and
[[concept_auction_market_theory]].

**Rules (long).**
- *State:* the market is out of balance, with displacement away from prior
  value.
- *Location:* build a volume-by-price profile of the impulse leg that broke
  structure and mark its low-volume nodes. They are zones, not single
  prices.
- *Trigger:* price returns into the LVN and the footprint shows aggressive
  buying, or selling being absorbed: imbalances, large prints, CVD turning
  up.
- *Entry:* market at the trigger. Fabio advises against resting blind
  limit orders there. In a bar-based bot, that means market on close of
  the trigger bar.
- *Stop:* 1–2 ticks beyond the aggressive print, or just beyond the LVN.
- *Target:* the previous balance's POC, all out.

**Why it is not codeable here.** The profile needs volume at each price,
from trades or ticks. Absorption needs the bid/ask split of each trade
(footprint, delta). OHLCV has neither. Two proxies exist but are weaker.
Volume-at-price can be built from 1m bars by spreading each bar's volume
across its range, and Binance klines include taker-buy volume per bar, a
bar-level delta proxy. A spec built on those proxies is a different spec,
and it must be tested as such. Until then, the honest answer for an OHLCV
bot is to step back from this model ([[philo_step_back]]).

**Principles.** [[principle_01_understand_before_acting]] (state, then
location, then aggression), [[principle_06_do_not_force]] (no data, no
trade).

---

## Evidence

Sources found on 2026-10-20. Tiers follow [[framework_source_tiers]]. No
peer-reviewed or working paper tests FVGs, order blocks, OTE or ICT kill
zones as such. A targeted search turned up only indicator pages and vendor
material.

| Claim | Source | Tier | What it supports | What it does not |
|---|---|---|---|---|
| Stop-loss and take-profit orders cluster at round numbers, differently, explaining reversals at and acceleration through support and resistance | Osler, NY Fed Staff Report 125 (2001), https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr125.pdf | T1 | S1, S5, S9 mechanisms | Bitcoin; any trading P&L |
| BTC prices cluster at round numbers, with no significant return pattern after them | Urquhart, *Economics Letters* 2017, https://ideas.repec.org/a/eee/ecolet/v159y2017icp145-148.html | T1 | Clustering exists in BTC | Undermines a naive round-number reversal |
| The first half-hour return predicts the last half-hour return (SPY 1993–2013), more strongly on volatile, high-volume and news days | Gao, Han, Li, Zhou, *JFE* 2018, https://profiles.wustl.edu/en/publications/market-intraday-momentum/ | T1 | S4 timing logic | A 2R bracket after costs |
| Bitcoin intraday momentum from the first to the last half-hour, strongest in high-volume or high-volatility sessions | Shen, Urquhart, Wang, *Financial Review* 2022, https://research.birmingham.ac.uk/en/publications/bitcoin-intraday-time-series-momentum/ | T1 | Session effects in BTC | 5m entries |
| Moving-average rules supported on high-frequency BTC returns | Corbet, Eraslan, Lucey, Sensoy, *FRL* 2019, https://ideas.repec.org/a/eee/finlet/v31y2019icp32-37.html | T1 | S7 trend filter | Pullback entries specifically |
| 69 MA and breakout rules, daily and 1-minute, with and without costs: results depend on the coin and on bubble periods | Svogun, Bazán-Palomino, *JIFMIM* 2022, https://ideas.repec.org/a/eee/intfin/v79y2022ics1042443122000816.html | T1 | Costs and regimes matter | Any stable edge |
| FX currencies depreciate during their local trading hours; also visible in order flow | Breedon, Ranaldo, SNB WP 2011-04, https://www.snb.ch/en/publications/research/working-papers/2011/working_paper_2011_04 | T1 | S8 session premise | Asia-range sweeps |
| Fibonacci ratio anchoring in the DJIA: no more than chance | City University London thesis, https://openaccess.city.ac.uk/id/eprint/18945/ | T1 | Treat OTE as location only | — |
| Fibonacci and non-Fibonacci retracement zones do not differ statistically | Tsinaslanidis, Guijarro, Voukelatos, *ESWA* 187 (2022), abstract via https://www.datalearner.com/academic/journal-papers/0957-4174/volumes-and-issues/391/paper-detail/17703 | T1 (abstract only) | Same | — |
| ORB on US stocks in play, 2016–2023: more than 1,600% net, Sharpe 2.81 (top 20) | Zarattini, Barbon, Aziz, summarised at https://concretumgroup.com/a-profitable-day-trading-strategy-for-the-u-s-equity-market/ | **T4** (self-reported, in-sample) | That the idea is testable | Net edge in crypto |
| VWAP trend on QQQ, 2018–2023: $25k → $192,656 net of commissions | Zarattini, Aziz, https://concretumgroup.com/volume-weighted-average-price-vwap-the-holy-grail-for-day-trading-systems/ | **T4** | Same | Net of spread and slippage |
| ORB replicated on five indices: gross reproduced, net indistinguishable from zero | MQL5 blog, https://www.mql5.com/en/blogs/post/776235 (search summary only, not opened) | **T4** | Costs can erase it | — |
| Vendor backtests, 10 years unless noted, 0.02% commission per side: ICT FVG on Nasdaq 15m +37.7% vs buy-and-hold +527%, PF 1.08, 852 trades, flat or negative 2024–2026 · kill-zone FVG on GBPUSD 15m −30.3%, PF 0.80, 1,009 trades · equal-low sweep on Dow 1m +23.7%, PF 1.95, **70 trades** (Oct 2024–2026) · order block on GBPUSD 1h −15.3%, PF 0.83, 203 trades · VWAP 2σ fade on DAX 15m −98.6%, PF 0.64, 8,943 trades · London breakout on GBPUSD 15m −60.0%, PF 0.72, 2,432 trades · PDH/PDL breakout on GBPUSD 1h −65.6%, PF 0.76 | Backtrex, https://backtrex.com/en/backtests/ (pages ict-fair-value-gap-nasdaq, ict-kill-zone-fvg-gbp-usd, liquidity-sweep-dow-jones, order-block-gbp-usd, vwap-band-fade-dax, london-breakout-gbp-usd, previous-day-high-low-breakout-gbp-usd) | **T4** (vendor of a backtesting tool; rules published, not replicated) | Simple codings of these ideas are not free money; costs and fixed-point stops hurt | That a better coding fails |
| How the ICT models are taught (OTE band, Silver Bullet windows, sweep then confirmation) | LuxAlgo library, https://www.luxalgo.com/library/concept/optimal-trade-entry/, https://www.luxalgo.com/library/concept/silver-bullet/, https://www.luxalgo.com/library/concept/liquidity-sweep/ | T3 | Rule definitions | Any performance |

On the Silver Bullet window rule, LuxAlgo puts it plainly: "No valid gap
inside the window means no trade that session." That is
[[principle_06_do_not_force]] written as code.

---

## Costs and the $20 account

These are facts read on 2026-10-20. Choosing a venue belongs to the L6
notes, not this one.

- **Binance (third-party figure, T3):** the regular-tier spot fee is
  **0.10% maker and 0.10% taker**, or 0.075% each when paying in BNB
  (comparison page dated 2026-07-08, as summarised in a search result,
  https://comparedge.com/tools/binance/pricing). We could not confirm this
  on Binance's own page from this environment.
- **Kraken Pro (first-party page):** spot tier 1 (under $2.5K of 30-day
  volume) shows **0.40% maker and 0.80% taker** (https://www.kraken.com/features/fee-schedule,
  read 2026-10-20). A maker-in, taker-stop loser costs 1.20% round trip,
  which is 8R on a median S1 stop.
- **Binance.US (first-party announcement, US residents only):** **0% maker
  and 0.02% taker** on spot from 2026-04-22 (https://blog.binance.us/zero-fee-trading/,
  read 2026-10-20). This is an example that a round trip near 0.02% exists
  for some users. Check availability in your jurisdiction and whether it
  has changed.
- **Spot at 1× on $20:** the position is at most $20, so the dollars at
  risk per trade are $20 × stop %. At the measured medians that is about
  **2 to 9 cents a trade**, and a 2R winner pays about 4 to 18 cents before
  fees. Account risk per trade is small (0.1–0.4%), which suits
  [[principle_09_protect_capital]]. It also means "scraping trades day by
  day" on $20 is a **learning and validation exercise, not an income**.
  Leverage would raise the cents and the risk of ruin together; that
  decision belongs to the sizing note under
  [[concept_position_sizing]] and [[concept_risk_of_ruin_drawdown]].
- **Order mechanics:** with a 5 USDT minimum notional, $20 can hold up to
  four concurrent $5 orders. Use `LIMIT_MAKER` (post-only) for entries, so a
  limit that would cross the spread is rejected instead of silently paying
  the taker fee.

**What follows for the bot.**

1. Put the fee gate (`max_cost_r = 0.10`) in front of every spec, using
   the venue's actual fees.
2. On a 0.20% round-trip venue, run the **same specs on 1h and 4h candles**
   (stops roughly 4–9× wider). Expect far fewer signals, perhaps a few a
   week per market.
3. On a near-zero-maker venue, 5m can work for S3, S4 and S6, which have
   the widest stops. S5, S8 and S9 still mostly fail the gate.
4. Exits by stop are taker orders, so count slippage on every stop in the
   backtest.

---

## How much evidence a spec needs before real money

Use [[formula_sheet]] and Section VI ([[philo_conditional_probability]]).
A −1R / +2R bracket has an outcome standard deviation of about 1.4R. To
pin expectancy to ±0.1R at 95% confidence takes about (1.96 × 1.4 ÷ 0.1)²,
or **roughly 750 trades**. At 1 fill a day per market, that is about two
years on one market, or about one year across BTC and ETH, **per spec**.
That is why the order of work is:

1. Code each spec exactly as written here.
2. Backtest it with real fees and stop slippage, and compare it with a
   placebo (random levels of the same size).
3. Freeze the parameters, then test out of sample.
4. Paper trade forward.
5. Only then pass it through [[framework_decision_protocol]] Gates 4–6
   with its **own** record ([[synthesis_evidence_lab]] S3 and S5 show what
   small samples and best-of-many selection do).

## Principles touched across all specs

- [[principle_05_mathematical_justification]] and Section VII
  ([[philo_mathematics_sword]]): the fee gate and the sample-size rule.
- [[principle_06_do_not_force]]: every spec has a no-trade outcome, and a
  skip is a recorded decision.
- [[principle_09_protect_capital]]: the two-loss rule per session, and spot
  at 1× until a spec passes validation.
- [[principle_10_emotional_independence]] and
  [[principle_12_process_not_money]]: a bot removes impulse only if no
  rule can be overridden mid-trade. The urge to "trade every day" is what
  the fee gate protects against.
- [[principle_11_record_and_investigate]]: journal fills, cancels and
  skips alike. The fill rate and the skip reasons are evidence too.

Pre-trade, the items from [[synthesis_pre_trade_checklist]] that apply to a
bot are: the level was defined before price arrived; the invalidation was
written; EV was checked after costs; size came from the stop; the setup
has its own out-of-sample record.
