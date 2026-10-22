# Partition 10_sniper-lab


<!-- ===== FILE: trading-intelligence/10_sniper-lab/README.md ===== -->

# Partition 10 — Sniper Lab

The owner asked for precise "sniper" entries that trade every day, on a small account (any size),
without waiting for a 60% win rate. This partition answers that question with code and real data.
The answer comes through the philosophy's own test: understanding, evidence and mathematics must
agree before a trade (Section VIII). Expected value after costs, out of sample, is the sword
(Section VII).

> Education and research, not financial advice. Every number here comes from historical data under
> stated assumptions. Nothing here promises a result.

## Read in this order

| # | File | What it is |
|---|---|---|
| 1 | `backtest-report.md` | **The result.** Every codified setup on crypto, forex and gold, 2022–2026. Rules are chosen in-sample and judged out-of-sample, after costs, with multiple testing counted. |
| 2 | `sniper-entries.md` | The 12 entry specs (S1–S12) as exact rules, the playbooks they come from, the published evidence for and against each, and measured frequency and stop sizes. |
| 3 | `small-account-venues.md` | Where a small account can trade: fees, minimum orders, cent accounts, leverage limits, and which venues fit which stop sizes. `venues.yaml` is the same table for the size calculator. |
| 4 | `reading-list.md` | Books on precise entries, short-term systems and validation. `books-sniper.yaml` adds 19 books that are not in the top 100. |
| 5 | `setups.yaml` | Generated. The codified setups as graph nodes, linked to the playbooks and concepts they were coded from, each with its out-of-sample verdict. |

## What the lab found (2026-10-20)

**What ran.** 128 configurations. A configuration is one setup on one timeframe at one cost level,
pooled across its markets:

- **Crypto:** 14 setups × 2 timeframes × 3 fee levels, 84 in all. The three fee levels re-price the
  same trades. Data: BTC and ETH on 5m and 15m, SOL on 5m only. The owner stopped the crypto run there,
  so BNB, XRP and 1h/4h crypto were not run.
- **Forex and gold:** 11 setups × 2 timeframes × 2 account types, 44 in all. Data: EUR/USD, GBP/USD,
  USD/JPY and XAU/USD on 1h and 4h. The other three setups only work intraday and were not run here.
  Intraday forex (5m/15m) needs minute history that throttles cloud servers; run it at home
  (HANDOFF.md).

Allowed regimes and sessions were chosen on 2022–2023. The trades in both a kept regime and a kept
session also had to be positive in-sample. Everything was then judged on 2024 to September 2026. Those
same years were used afterwards to see which configurations pass, which is why the multiple-testing
check matters.

| | Crypto | Forex and gold |
|---|---|---|
| Configurations positive after costs, out of sample | **0 of 84** | 7 of 44 |
| Typical result (median, R per trade) | −0.01 before fees | −0.07 after the spread, before commission |
| Typical cost (median, R per trade) | 0.32 in fees | about 0.10 on a spread-only account and 0.06 on raw spread, spread included |
| Pass Gate 4 inside conditions that held in-sample | none | **1:** VWAP reversion 1h, raw-spread account, +0.25R per trade over 123 trades |

**The one that passes is not proven.** With 128 configurations tried, its deflated-Sharpe probability
of being real is 0.35 (0.95 is the bar). It was positive in each year: 2024 +0.24R, 2025 +0.22R and
2026 +0.29R per trade. Gold and GBP/USD carried it, while USD/JPY was flat. Its 5 best trades are 66% of
the total. On a spread-only or cent account at about 1.3 pips it makes only +0.12R, with a t of 0.8,
and fails. So the record is *provisional*. The scanner paper-trades it through the gate. It hands a
trade to your bot's order code only when the full gate, run on the setup's **forward** trades alone,
also says take. Forward trades are the signals after the lab's data, so they played no part in choosing
the setup. At about 3–4 trades a month, 30 forward trades take many months.

What it means for the owner's question:

- **Precise 5-minute crypto entries do not pay at any fee level found.** The median result before fees
  is about zero, and four setups lose 0.14–0.24R per trade even before fees. Only the EMA pullback with
  a market entry shows a gross edge that held out of sample: +0.035R per trade, against 0.27R of cost
  on the cheapest venue found.
- **The cost in R decides.** It is the round-trip cost divided by the stop distance. Tight stops pay
  for themselves only where the round trip is tiny, as on raw-spread forex accounts. The one survivor
  has tight stops (median 0.11%) and works only at raw-spread cost, about 0.10R per trade.
- **"Trading every day" and "having an edge" pull against each other.** The survivor trades about 3–4
  times a month across four markets. The busiest setups (the EMA pullback, its limit version and the
  Donchian model on 5m crypto) trade about 10 times a day per coin, about 30 a day across three coins.
  They lose the most R per day, because every trade pays the cost. The tight-stop setups lose the most
  per trade.
- **Known limits** (listed at the end of `backtest-report.md`). Targets fill on a touch, and the forex
  spread is modelled. Together they can only flatter results. Forward evidence must come from data
  like the lab's: use `--venue csv` with your broker's own candles. Yahoo has no spot gold.

## The engine (in the `trading_intelligence` package)

```
pip install "trading-intelligence[mcp] @ git+https://github.com/NANKPA/claudeai.git"

python -m trading_intelligence.sniper size --equity 20 --risk-pct 1      # what a stop costs, venue by venue
python -m trading_intelligence.sniper scan --fees low --min-notional 1   # live crypto scan, paper only
python -m trading_intelligence.sniper scan --venue csv --csv-dir ~/bot/candles --symbols EURUSD GBPUSD USDJPY XAUUSD \
       --timeframes 1h 4h --fees fx_raw --lot-step 10 --min-notional 11.5 --max-leverage 30   # forex/gold, broker candles
python -m trading_intelligence.sniper scan --report                      # forward results so far
python -m trading_intelligence.sniper lab                                # re-run every backtest (about an hour)
```

| Module | Job |
|---|---|
| `sniper/setups.py` | 14 setups: the six classic sniper entries, four more from the research specs (break and retest, Asia→London sweep, round-number sweep, order block), two maker-only variants, a Donchian trend model and the published intraday-momentum effect. Every indicator is causal and tested for it. |
| `sniper/backtest.py` | One `Book` per setup and market. Limits fill only when price trades through them. When stop and target fall in the same bar, the stop counts. A bar that fills and closes beyond the target exits at the target. On forex, buys pay the ask and sells get the bid. R is measured on the planned risk. The backtester and the paper broker share this code, and a test checks that paper trades equal the backtest's trade for trade. |
| `sniper/lab.py` | The grid: setups × markets × timeframes × cost levels. In-sample is 2022–2023 and out-of-sample is 2024 on. The deflated Sharpe ratio counts every configuration tried. |
| `sniper/scanner.py` | Live closed candles → signal → `TradeProposal` → **PhilosophyGate** → journal → paper fill. Every signal is also followed in a shadow book, so the forward record keeps growing whatever the gate decides. `--on-take` passes the gate's takes to your own order code; for a provisional record, only once its forward trades pass on their own. State is crash-safe and kept in one folder per cost level. |
| `sniper/smallaccount.py` | Any account size: risk, order value, leverage needed, venue minimums, cost in R and the break-even win rate. |

## Three facts that decide everything

1. **Cost in R = round-trip cost ÷ stop distance.** Account size cancels out, so a $20 account and a
   $20,000 account pay the same cost in R. What account size changes is whether the order clears the
   venue's minimum, and how much leverage a tight stop needs.
2. **A tight crypto stop is mostly cost.** A 0.25% stop with 0.10% fees per side gives up most of 1R
   to fees. The same stop on EUR/USD, at about one pip round trip, gives up a few hundredths of 1R.
3. **Frequency is easy; edge is not.** The setups place several orders a day per market. Each trade
   pays the cost, so more trades only multiply the expectancy, positive or negative.

## How it connects

Each setup is a `setup` node with `derived_from` links to the Chart Fanatics playbooks, legends and
concepts it was coded from (`setups.yaml`). The notes link to the philosophy's principles,
especially 4 (conditional probability), 5 (mathematical justification), 6 (do not force) and 9
(protect capital). The gate is `00_philosophy/decision-protocol.md`, run as code.


<!-- ===== FILE: trading-intelligence/10_sniper-lab/backtest-report.md ===== -->

---
id: synthesis_sniper_backtests
type: synthesis
title: "Sniper Lab — backtests of the codified sniper entries (in-sample vs out-of-sample)"
partition: 10_sniper-lab
layer: L8
related: [synthesis_sniper_entries, synthesis_small_account_venues, synthesis_evidence_lab, framework_decision_protocol, philosophy_relationship]
status: computed
---

# Sniper Lab — backtests

> Generated 2026-10-20 by `python -m trading_intelligence.sniper lab`. Education and research, not a trading signal.

**What ran.** Crypto (Binance spot archive): BTCUSDT 5m/15m, ETHUSDT 5m/15m, SOLUSDT 5m; signals 2022-01-02 to 2026-09-30. Forex and gold (Dukascopy BID candles): EURUSD 1h/4h, GBPUSD 1h/4h, USDJPY 1h/4h, XAUUSD 1h/4h; signals 2022-01-19 to 2026-09-30.

**Method.** Allowed regimes and sessions are chosen on signals before 2024-01-01 (in-sample); the trades in a kept regime AND a kept session must also have been positive in-sample. Everything is then judged on signals from 2024-01-01 on (out-of-sample). Each configuration (setup × timeframe × cost level) pools its markets. The three crypto fee levels are the same trades re-priced; each forex account type is its own simulation.

**Fills.** A market entry fills at the next bar's open. A resting limit entry fills only when price trades THROUGH it (a touch is not a fill). On later bars, when the stop and the target fall in the same bar, the stop counts; a bar that opens beyond the stop exits at that open. On the fill bar the stop is checked first, and a bar that closes beyond the target exits at the target. A target fills on a TOUCH at the target price and pays the maker fee: that assumes queue priority and is the one optimistic rule (see Known limits). R is measured on the planned risk, the risk the gate sizes on.

## Cost levels (fraction of price)

| Level | Market | Resting limit (per side) | Market order / stop (per side) | Slippage on market entries, stops, time exits | Spread per round trip (paid in the prices) |
|---|---|---|---|---|---|
| std | crypto | 0.0800% | 0.1000% | 0.0200% | 0.0000% |
| low | crypto | 0.0000% | 0.0500% | 0.0100% | 0.0000% |
| ultra | crypto | 0.0000% | 0.0200% | 0.0100% | 0.0000% |
| fx_std | fx | 0.0000% | 0.0000% | 0.0020% | 0.0120% |
| fx_raw | fx | 0.0032% | 0.0032% | 0.0010% | 0.0015% |

## Crypto: every trade, pooled across markets

IS = in-sample (before the split), OOS = out-of-sample. Gross R is before fees; net R is after fees and slippage at that level.

| Setup | TF | Costs | OOS trades/day | Stop % | IS gross R | OOS gross R | OOS cost R | OOS net R |
|---|---|---|---|---|---|---|---|---|
| lit_intraday_momentum | 15m | low | 2.00 | 0.97 | +0.012 | -0.005 | +0.143 | -0.148 |
| sniper_asia_london_judas | 15m | low | 0.45 | 0.28 | +0.129 | -0.318 | +0.274 | -0.592 |
| sniper_break_retest | 15m | low | 0.67 | 0.22 | +0.012 | +0.004 | +0.219 | -0.214 |
| sniper_ema_pullback | 15m | low | 6.69 | 0.38 | -0.003 | +0.008 | +0.337 | -0.329 |
| sniper_ema_pullback_limit | 15m | low | 6.57 | 0.38 | -0.020 | -0.020 | +0.137 | -0.157 |
| sniper_fvg_retrace | 15m | low | 1.18 | 0.34 | -0.190 | -0.015 | +0.167 | -0.182 |
| sniper_ob_mean_threshold | 15m | low | 0.70 | 0.17 | -0.143 | -0.009 | +0.418 | -0.426 |
| sniper_orb_retest | 15m | low | 1.22 | 0.41 | +0.035 | -0.015 | +0.147 | -0.161 |
| sniper_ote_retrace | 15m | low | 1.34 | 0.63 | -0.020 | -0.017 | +0.082 | -0.099 |
| sniper_round_number_sweep | 15m | low | 1.23 | 0.19 | -0.310 | -0.256 | +0.363 | -0.620 |
| sniper_sweep_reclaim | 15m | low | 3.37 | 0.42 | +0.063 | +0.028 | +0.307 | -0.279 |
| sniper_sweep_reclaim_limit | 15m | low | 0.81 | 0.27 | -0.012 | -0.095 | +0.229 | -0.324 |
| sniper_vwap_reversion | 15m | low | 0.61 | 0.41 | -0.090 | -0.005 | +0.330 | -0.335 |
| trend_donchian_breakout | 15m | low | 5.97 | 0.67 | -0.012 | +0.064 | +0.195 | -0.131 |
| lit_intraday_momentum | 5m | low | 3.00 | 0.57 | +0.015 | +0.006 | +0.258 | -0.252 |
| sniper_asia_london_judas | 5m | low | 1.18 | 0.26 | -0.039 | -0.201 | +0.351 | -0.552 |
| sniper_break_retest | 5m | low | 3.43 | 0.14 | -0.058 | -0.140 | +0.391 | -0.531 |
| sniper_ema_pullback | 5m | low | 30.35 | 0.24 | +0.024 | +0.035 | +0.530 | -0.495 |
| sniper_ema_pullback_limit | 5m | low | 29.51 | 0.25 | -0.014 | -0.014 | +0.218 | -0.232 |
| sniper_fvg_retrace | 5m | low | 6.07 | 0.19 | -0.090 | -0.084 | +0.373 | -0.457 |
| sniper_ob_mean_threshold | 5m | low | 2.32 | 0.10 | -0.230 | -0.039 | +0.752 | -0.791 |
| sniper_orb_retest | 5m | low | 2.10 | 0.46 | +0.022 | -0.008 | +0.132 | -0.139 |
| sniper_ote_retrace | 5m | low | 6.01 | 0.41 | -0.038 | -0.001 | +0.129 | -0.129 |
| sniper_round_number_sweep | 5m | low | 2.58 | 0.12 | -0.330 | -0.235 | +0.548 | -0.784 |
| sniper_sweep_reclaim | 5m | low | 8.61 | 0.29 | +0.055 | +0.028 | +0.476 | -0.448 |
| sniper_sweep_reclaim_limit | 5m | low | 1.93 | 0.19 | -0.080 | -0.146 | +0.339 | -0.486 |
| sniper_vwap_reversion | 5m | low | 3.00 | 0.34 | -0.064 | -0.001 | +0.436 | -0.437 |
| trend_donchian_breakout | 5m | low | 28.23 | 0.41 | +0.002 | +0.005 | +0.342 | -0.337 |
| lit_intraday_momentum | 15m | std | 2.00 | 0.97 | +0.012 | -0.005 | +0.286 | -0.292 |
| sniper_asia_london_judas | 15m | std | 0.45 | 0.28 | +0.129 | -0.318 | +0.977 | -1.294 |
| sniper_break_retest | 15m | std | 0.67 | 0.22 | +0.012 | +0.004 | +1.022 | -1.018 |
| sniper_ema_pullback | 15m | std | 6.69 | 0.38 | -0.003 | +0.008 | +0.762 | -0.754 |
| sniper_ema_pullback_limit | 15m | std | 6.57 | 0.38 | -0.020 | -0.020 | +0.624 | -0.644 |
| sniper_fvg_retrace | 15m | std | 1.18 | 0.34 | -0.190 | -0.015 | +0.745 | -0.759 |
| sniper_ob_mean_threshold | 15m | std | 0.70 | 0.17 | -0.143 | -0.009 | +1.556 | -1.564 |
| sniper_orb_retest | 15m | std | 1.22 | 0.41 | +0.035 | -0.015 | +0.653 | -0.667 |
| sniper_ote_retrace | 15m | std | 1.34 | 0.63 | -0.020 | -0.017 | +0.360 | -0.377 |
| sniper_round_number_sweep | 15m | std | 1.23 | 0.19 | -0.310 | -0.256 | +1.495 | -1.751 |
| sniper_sweep_reclaim | 15m | std | 3.37 | 0.42 | +0.063 | +0.028 | +0.691 | -0.663 |
| sniper_sweep_reclaim_limit | 15m | std | 0.81 | 0.27 | -0.012 | -0.095 | +0.974 | -1.069 |
| sniper_vwap_reversion | 15m | std | 0.61 | 0.41 | -0.090 | -0.005 | +0.731 | -0.736 |
| trend_donchian_breakout | 15m | std | 5.97 | 0.67 | -0.012 | +0.064 | +0.424 | -0.360 |
| lit_intraday_momentum | 5m | std | 3.00 | 0.57 | +0.015 | +0.006 | +0.516 | -0.510 |
| sniper_asia_london_judas | 5m | std | 1.18 | 0.26 | -0.039 | -0.201 | +1.250 | -1.451 |
| sniper_break_retest | 5m | std | 3.43 | 0.14 | -0.058 | -0.140 | +1.704 | -1.843 |
| sniper_ema_pullback | 5m | std | 30.35 | 0.24 | +0.024 | +0.035 | +1.206 | -1.171 |
| sniper_ema_pullback_limit | 5m | std | 29.51 | 0.25 | -0.014 | -0.014 | +0.995 | -1.009 |
| sniper_fvg_retrace | 5m | std | 6.07 | 0.19 | -0.090 | -0.084 | +1.591 | -1.675 |
| sniper_ob_mean_threshold | 5m | std | 2.32 | 0.10 | -0.230 | -0.039 | +2.791 | -2.830 |
| sniper_orb_retest | 5m | std | 2.10 | 0.46 | +0.022 | -0.008 | +0.582 | -0.590 |
| sniper_ote_retrace | 5m | std | 6.01 | 0.41 | -0.038 | -0.001 | +0.564 | -0.564 |
| sniper_round_number_sweep | 5m | std | 2.58 | 0.12 | -0.330 | -0.235 | +2.257 | -2.493 |
| sniper_sweep_reclaim | 5m | std | 8.61 | 0.29 | +0.055 | +0.028 | +1.080 | -1.052 |
| sniper_sweep_reclaim_limit | 5m | std | 1.93 | 0.19 | -0.080 | -0.146 | +1.450 | -1.596 |
| sniper_vwap_reversion | 5m | std | 3.00 | 0.34 | -0.064 | -0.001 | +0.935 | -0.935 |
| trend_donchian_breakout | 5m | std | 28.23 | 0.41 | +0.002 | +0.005 | +0.742 | -0.737 |
| lit_intraday_momentum | 15m | ultra | 2.00 | 0.97 | +0.012 | -0.005 | +0.072 | -0.077 |
| sniper_asia_london_judas | 15m | ultra | 0.45 | 0.28 | +0.129 | -0.318 | +0.137 | -0.455 |
| sniper_break_retest | 15m | ultra | 0.67 | 0.22 | +0.012 | +0.004 | +0.109 | -0.105 |
| sniper_ema_pullback | 15m | ultra | 6.69 | 0.38 | -0.003 | +0.008 | +0.169 | -0.161 |
| sniper_ema_pullback_limit | 15m | ultra | 6.57 | 0.38 | -0.020 | -0.020 | +0.069 | -0.089 |
| sniper_fvg_retrace | 15m | ultra | 1.18 | 0.34 | -0.190 | -0.015 | +0.084 | -0.098 |
| sniper_ob_mean_threshold | 15m | ultra | 0.70 | 0.17 | -0.143 | -0.009 | +0.209 | -0.217 |
| sniper_orb_retest | 15m | ultra | 1.22 | 0.41 | +0.035 | -0.015 | +0.073 | -0.088 |
| sniper_ote_retrace | 15m | ultra | 1.34 | 0.63 | -0.020 | -0.017 | +0.041 | -0.058 |
| sniper_round_number_sweep | 15m | ultra | 1.23 | 0.19 | -0.310 | -0.256 | +0.182 | -0.438 |
| sniper_sweep_reclaim | 15m | ultra | 3.37 | 0.42 | +0.063 | +0.028 | +0.153 | -0.125 |
| sniper_sweep_reclaim_limit | 15m | ultra | 0.81 | 0.27 | -0.012 | -0.095 | +0.115 | -0.209 |
| sniper_vwap_reversion | 15m | ultra | 0.61 | 0.41 | -0.090 | -0.005 | +0.165 | -0.170 |
| trend_donchian_breakout | 15m | ultra | 5.97 | 0.67 | -0.012 | +0.064 | +0.098 | -0.033 |
| lit_intraday_momentum | 5m | ultra | 3.00 | 0.57 | +0.015 | +0.006 | +0.129 | -0.123 |
| sniper_asia_london_judas | 5m | ultra | 1.18 | 0.26 | -0.039 | -0.201 | +0.175 | -0.376 |
| sniper_break_retest | 5m | ultra | 3.43 | 0.14 | -0.058 | -0.140 | +0.196 | -0.335 |
| sniper_ema_pullback | 5m | ultra | 30.35 | 0.24 | +0.024 | +0.035 | +0.265 | -0.230 |
| sniper_ema_pullback_limit | 5m | ultra | 29.51 | 0.25 | -0.014 | -0.014 | +0.109 | -0.123 |
| sniper_fvg_retrace | 5m | ultra | 6.07 | 0.19 | -0.090 | -0.084 | +0.186 | -0.270 |
| sniper_ob_mean_threshold | 5m | ultra | 2.32 | 0.10 | -0.230 | -0.039 | +0.376 | -0.415 |
| sniper_orb_retest | 5m | ultra | 2.10 | 0.46 | +0.022 | -0.008 | +0.066 | -0.073 |
| sniper_ote_retrace | 5m | ultra | 6.01 | 0.41 | -0.038 | -0.001 | +0.064 | -0.065 |
| sniper_round_number_sweep | 5m | ultra | 2.58 | 0.12 | -0.330 | -0.235 | +0.274 | -0.509 |
| sniper_sweep_reclaim | 5m | ultra | 8.61 | 0.29 | +0.055 | +0.028 | +0.238 | -0.210 |
| sniper_sweep_reclaim_limit | 5m | ultra | 1.93 | 0.19 | -0.080 | -0.146 | +0.170 | -0.316 |
| sniper_vwap_reversion | 5m | ultra | 3.00 | 0.34 | -0.064 | -0.001 | +0.218 | -0.219 |
| trend_donchian_breakout | 5m | ultra | 28.23 | 0.41 | +0.002 | +0.005 | +0.171 | -0.166 |

## Forex and gold: every trade, pooled across markets

IS = in-sample (before the split), OOS = out-of-sample. The candles are bid prices and every buy pays the ask, so **gross R is already after the spread** (it changes with the account type); the cost column is commission plus slippage only. The ask is modelled as bid × (1 + spread): 0.012% on fx_std (about 1.4 pips on EUR/USD, 1.8 on USD/JPY, $0.40 on gold) and 0.0015% on fx_raw (about 0.17 pip, 0.23 pip, $0.05), the same fraction for every market and hour, with no widening at rollover or news.

| Setup | TF | Costs | OOS trades/day | Stop % | IS gross R | OOS gross R | OOS cost R | OOS net R |
|---|---|---|---|---|---|---|---|---|
| sniper_break_retest | 1h | fx_raw | 0.66 | 0.07 | -0.231 | -0.251 | +0.101 | -0.353 |
| sniper_ema_pullback | 1h | fx_raw | 2.08 | 0.18 | -0.023 | -0.008 | +0.054 | -0.063 |
| sniper_ema_pullback_limit | 1h | fx_raw | 2.06 | 0.18 | -0.025 | -0.026 | +0.048 | -0.074 |
| sniper_fvg_retrace | 1h | fx_raw | 0.42 | 0.16 | -0.012 | -0.057 | +0.051 | -0.108 |
| sniper_ob_mean_threshold | 1h | fx_raw | 0.19 | 0.07 | -0.135 | -0.070 | +0.111 | -0.180 |
| sniper_ote_retrace | 1h | fx_raw | 0.44 | 0.26 | +0.015 | -0.046 | +0.030 | -0.075 |
| sniper_round_number_sweep | 1h | fx_raw | 1.20 | 0.07 | -0.244 | -0.218 | +0.129 | -0.347 |
| sniper_sweep_reclaim | 1h | fx_raw | 2.75 | 0.15 | -0.014 | +0.039 | +0.071 | -0.032 |
| sniper_sweep_reclaim_limit | 1h | fx_raw | 0.92 | 0.10 | -0.068 | -0.072 | +0.105 | -0.177 |
| sniper_vwap_reversion | 1h | fx_raw | 0.16 | 0.10 | +0.438 | +0.142 | +0.101 | +0.041 |
| trend_donchian_breakout | 1h | fx_raw | 2.12 | 0.27 | +0.010 | +0.025 | +0.032 | -0.008 |
| sniper_break_retest | 4h | fx_raw | 0.37 | 0.17 | -0.075 | -0.067 | +0.044 | -0.111 |
| sniper_ema_pullback | 4h | fx_raw | 0.65 | 0.38 | +0.084 | -0.042 | +0.027 | -0.069 |
| sniper_ema_pullback_limit | 4h | fx_raw | 0.65 | 0.37 | +0.082 | -0.041 | +0.024 | -0.065 |
| sniper_fvg_retrace | 4h | fx_raw | 0.11 | 0.40 | -0.159 | +0.112 | +0.021 | +0.090 |
| sniper_ob_mean_threshold | 4h | fx_raw | 0.05 | 0.14 | -0.107 | +0.316 | +0.061 | +0.255 |
| sniper_ote_retrace | 4h | fx_raw | 0.12 | 0.53 | +0.065 | -0.124 | +0.014 | -0.138 |
| sniper_round_number_sweep | 4h | fx_raw | 0.46 | 0.14 | -0.062 | -0.183 | +0.069 | -0.252 |
| sniper_sweep_reclaim | 4h | fx_raw | 1.37 | 0.28 | -0.029 | +0.007 | +0.037 | -0.030 |
| sniper_sweep_reclaim_limit | 4h | fx_raw | 0.53 | 0.15 | -0.152 | -0.186 | +0.059 | -0.245 |
| sniper_vwap_reversion | 4h | fx_raw | 0.02 | 0.16 | -0.629 | -0.198 | +0.072 | -0.270 |
| trend_donchian_breakout | 4h | fx_raw | 0.52 | 0.57 | +0.034 | +0.094 | +0.015 | +0.080 |
| sniper_break_retest | 1h | fx_std | 0.65 | 0.07 | -0.313 | -0.369 | +0.022 | -0.391 |
| sniper_ema_pullback | 1h | fx_std | 2.10 | 0.18 | -0.079 | -0.080 | +0.023 | -0.102 |
| sniper_ema_pullback_limit | 1h | fx_std | 2.06 | 0.18 | -0.083 | -0.098 | +0.010 | -0.108 |
| sniper_fvg_retrace | 1h | fx_std | 0.41 | 0.16 | -0.056 | -0.119 | +0.010 | -0.130 |
| sniper_ob_mean_threshold | 1h | fx_std | 0.20 | 0.07 | -0.245 | -0.241 | +0.028 | -0.269 |
| sniper_ote_retrace | 1h | fx_std | 0.43 | 0.26 | -0.036 | -0.078 | +0.006 | -0.084 |
| sniper_round_number_sweep | 1h | fx_std | 1.18 | 0.07 | -0.379 | -0.352 | +0.030 | -0.382 |
| sniper_sweep_reclaim | 1h | fx_std | 2.81 | 0.15 | -0.073 | -0.058 | +0.030 | -0.088 |
| sniper_sweep_reclaim_limit | 1h | fx_std | 0.91 | 0.10 | -0.159 | -0.223 | +0.024 | -0.247 |
| sniper_vwap_reversion | 1h | fx_std | 0.16 | 0.10 | +0.236 | -0.029 | +0.043 | -0.073 |
| trend_donchian_breakout | 1h | fx_std | 2.13 | 0.27 | -0.016 | -0.016 | +0.014 | -0.030 |
| sniper_break_retest | 4h | fx_std | 0.36 | 0.17 | -0.126 | -0.144 | +0.009 | -0.153 |
| sniper_ema_pullback | 4h | fx_std | 0.65 | 0.38 | +0.073 | -0.079 | +0.011 | -0.091 |
| sniper_ema_pullback_limit | 4h | fx_std | 0.64 | 0.38 | +0.074 | -0.088 | +0.005 | -0.092 |
| sniper_fvg_retrace | 4h | fx_std | 0.11 | 0.40 | -0.183 | +0.059 | +0.004 | +0.055 |
| sniper_ob_mean_threshold | 4h | fx_std | 0.05 | 0.14 | -0.029 | +0.228 | +0.015 | +0.213 |
| sniper_ote_retrace | 4h | fx_std | 0.12 | 0.53 | +0.075 | -0.144 | +0.003 | -0.147 |
| sniper_round_number_sweep | 4h | fx_std | 0.46 | 0.14 | -0.107 | -0.264 | +0.015 | -0.278 |
| sniper_sweep_reclaim | 4h | fx_std | 1.38 | 0.28 | -0.056 | -0.055 | +0.016 | -0.070 |
| sniper_sweep_reclaim_limit | 4h | fx_std | 0.52 | 0.15 | -0.190 | -0.278 | +0.013 | -0.291 |
| sniper_vwap_reversion | 4h | fx_std | 0.02 | 0.15 | -0.679 | -0.349 | +0.033 | -0.382 |
| trend_donchian_breakout | 4h | fx_std | 0.52 | 0.57 | +0.031 | +0.072 | +0.006 | +0.066 |

## Inside the conditions chosen in-sample (the record the gate reads)

A regime and a session are each kept when, on their own, they were positive after costs in-sample on at least 20 trades. The trades in both a kept regime and a kept session must then also be positive in-sample on at least 20 trades ("held"); only then is there a record. The out-of-sample trades inside the conditions are the evidence.

| Setup | TF | Costs | Allowed regimes | Allowed sessions | IS n | IS net R | Held | OOS n | OOS net R | OOS t | OOS t (by day) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| sniper_ob_mean_threshold | 15m | ultra | range_high_vol | late | 4 | +2.635 | no | 4 | +0.754 | 0.40 | 0.40 |
| sniper_ote_retrace | 1h | fx_raw | trend_low_vol | asia london | 123 | +0.039 | yes | 154 | -0.074 | -0.62 | -0.59 |
| sniper_vwap_reversion | 1h | fx_raw | range_high_vol range_low_vol | london ny | 97 | +0.426 | yes | 123 | +0.250 | 1.73 | 1.80 |
| trend_donchian_breakout | 1h | fx_raw | trend_low_vol | ny | 196 | +0.120 | yes | 313 | -0.025 | -0.26 | -0.24 |
| sniper_ema_pullback | 4h | fx_raw | trend_low_vol | asia ny | 118 | +0.209 | yes | 217 | -0.050 | -0.52 | -0.52 |
| sniper_ema_pullback_limit | 4h | fx_raw | trend_low_vol | asia ny | 117 | +0.231 | yes | 217 | -0.039 | -0.40 | -0.41 |
| sniper_ote_retrace | 4h | fx_raw | trend_low_vol | london | 22 | +0.477 | yes | 22 | -0.426 | -1.56 | -1.52 |
| sniper_sweep_reclaim | 4h | fx_raw | range_high_vol range_low_vol | asia | 25 | -0.231 | no | 73 | +0.093 | 0.52 | 0.53 |
| trend_donchian_breakout | 4h | fx_raw | trend_high_vol | asia london | 90 | -0.051 | no | 111 | +0.312 | 1.86 | 1.90 |
| sniper_fvg_retrace | 1h | fx_std | trend_low_vol | ny | 38 | +0.420 | yes | 59 | -0.084 | -0.46 | -0.44 |
| sniper_vwap_reversion | 1h | fx_std | range_high_vol range_low_vol | london ny | 97 | +0.280 | yes | 123 | +0.115 | 0.83 | 0.85 |
| sniper_ema_pullback | 4h | fx_std | trend_low_vol | asia ny | 119 | +0.218 | yes | 217 | -0.078 | -0.81 | -0.82 |
| sniper_ema_pullback_limit | 4h | fx_std | trend_high_vol trend_low_vol | asia ny | 287 | +0.135 | yes | 431 | -0.117 | -1.80 | -1.75 |
| sniper_ote_retrace | 4h | fx_std | trend_low_vol | london | 22 | +0.487 | yes | 21 | -0.385 | -1.35 | -1.33 |
| trend_donchian_breakout | 4h | fx_std | trend_high_vol | asia london | 90 | -0.053 | no | 112 | +0.313 | 1.89 | 1.91 |

## What passes the owner's gate

1 configuration(s) have at least 30 effectively independent out-of-sample trades and mean - 1 SE > 0 after costs, with the SE clustered by day as well as per trade (Gate 4's math score of 2). The scanner's gate can take only these:

- `sniper_vwap_reversion@1h@fx_raw`: OOS n 123 (effective 123), +0.250R per trade (SE 0.145), in-sample inside the same conditions +0.426R over 97 trades, 0.12 trades/day, regimes range_high_vol, range_low_vol, sessions london, ny
  - by year and market: 2024: 54 trades, +0.243R, total +13.1R; 2025: 35 trades, +0.221R, total +7.7R; 2026: 34 trades, +0.293R, total +9.9R; EURUSD: 34 trades, +0.161R, total +5.5R; GBPUSD: 43 trades, +0.327R, total +14.1R; USDJPY: 20 trades, -0.012R, total -0.2R; XAUUSD: 26 trades, +0.443R, total +11.5R; the 5 best trades are 66% of the total

Passing Gate 4 is necessary, not sufficient. These were chosen out of every configuration tried, using the same out-of-sample years that now make them look good; the multiple-testing result below says whether that choice could be luck.

**They do not survive it, so every record is marked provisional.** The scanner paper-trades them through the gate as usual. It hands a take to the owner's own order code (`--on-take`) only when the FULL gate, run on that setup's forward trades alone (signals after the lab's data ended, inside its chosen regimes and sessions, day-clustered like the lab), also says take; the size handed over comes from that forward-only decision. Forward trades played no part in choosing the setup, so they are the clean test. At a few trades a month, 30 of them take many months.

## Multiple testing

128 configurations were tried; 9 have a record (conditions held in-sample) and at least 30 effectively independent out-of-sample trades inside them. The best of those (`sniper_vwap_reversion@1h@fx_raw`, per-trade Sharpe +0.156 over 123 trades) has a deflated-Sharpe probability of 0.35 of being real once the number of trials is counted (Bailey & López de Prado; 0.95 is the usual bar).

## Reading this as the owner's philosophy asks

- **Crypto.** Best out-of-sample average before fees: +0.064R per trade (trend_donchian_breakout 15m low, 5993 trades; in-sample -0.012R). 0 of 84 configurations are positive after costs out-of-sample before the in-sample condition filter.
- **Forex and gold.** Best out-of-sample average after the spread, before commission: +0.316R per trade (sniper_ob_mean_threshold 4h fx_raw, 43 trades; in-sample -0.107R). 7 of 44 configurations are positive after costs out-of-sample before the in-sample condition filter.
- Crypto: a pattern that does not pay before fees cannot be rescued by a cheaper venue; cheaper fees only shrink the loss (Section VII: expected value first). Forex: the gross column already includes the spread, so the account type changes it.
- Cost in R = round-trip cost / stop distance. A 5-minute crypto stop of 0.2-0.3% against a 0.2% round trip costs most of 1R; the same stop in EUR/USD against a 0.01% round trip costs a few hundredths (Gate 5.6).
- More trades is not more edge: every trade pays the cost, so frequency multiplies a negative expectancy.
- Only the out-of-sample columns are evidence; in-sample numbers chose the conditions (Section XVII).

## Known limits of this test

- **Target fills on a touch** at the target price (queue priority assumed). This can only flatter results.
- **Forex spread is modelled**, a fixed fraction of price on BID candles, not the recorded ask; real spreads widen at rollover and on news.
- **Pooled markets are correlated.** The day-clustered SE and the effective n correct for same-day trades, not for every dependence.
- **The search over regimes and sessions** is not counted as extra trials in the deflated Sharpe, so that check is, if anything, too kind.
- **Forward evidence must come from comparable data.** The lab used Binance trades and Dukascopy bid candles. A scanner fed by another source (Yahoo quotes, a broker feed) builds forward records on different prices.
- **Crypto coverage was cut short by the owner:** BNB, XRP and the 1h/4h crypto timeframes were not run. Intraday forex (5m/15m) needs minute history that throttles cloud servers; run it at home.


<!-- ===== FILE: trading-intelligence/10_sniper-lab/backtests/backtest-report.md ===== -->

---
id: synthesis_sniper_backtests
type: synthesis
title: "Sniper Lab — backtests of the codified sniper entries (in-sample vs out-of-sample)"
partition: 10_sniper-lab
layer: L8
related: [synthesis_sniper_entries, synthesis_small_account_venues, synthesis_evidence_lab, framework_decision_protocol, philosophy_relationship]
status: computed
---

# Sniper Lab — backtests

> Generated 2026-10-20 by `python -m trading_intelligence.sniper lab`. Markets: EURUSD, GBPUSD, USDJPY, XAUUSD (crypto: Binance spot archive; forex and gold: Dukascopy BID candles). Timeframes: 1h, 4h. Period 2022-01 to last full month. Rules and the allowed regimes/sessions are chosen on data before 2024-01-01 and judged only on data after it. Fills are conservative (a limit fills only when price trades at or through it; when stop and target share a bar the stop counts). Education and research, not a trading signal.

## Cost levels (per side, fraction of price)

| Level | Market | Resting limit | Market order / stop | Extra slippage on stops |
|---|---|---|---|---|
| std | crypto | 0.0800% | 0.1000% | 0.0200% |
| low | crypto | 0.0000% | 0.0500% | 0.0100% |
| ultra | crypto | 0.0000% | 0.0200% | 0.0100% |
| fx_std | fx | 0.0000% | 0.0000% | 0.0020% |
| fx_raw | fx | 0.0032% | 0.0032% | 0.0010% |

## Forex and gold: every trade, pooled across markets

IS = in-sample (before the split), OOS = out-of-sample. Gross R is before costs; net R after costs at that level.

| Setup | TF | Costs | OOS trades/day | Stop % | IS gross R | OOS gross R | OOS cost R | OOS net R |
|---|---|---|---|---|---|---|---|---|
| sniper_break_retest | 1h | fx_raw | 0.66 | 0.07 | -0.231 | -0.251 | +0.101 | -0.353 |
| sniper_ema_pullback | 1h | fx_raw | 2.08 | 0.18 | -0.023 | -0.008 | +0.054 | -0.063 |
| sniper_ema_pullback_limit | 1h | fx_raw | 2.06 | 0.18 | -0.025 | -0.026 | +0.048 | -0.074 |
| sniper_fvg_retrace | 1h | fx_raw | 0.42 | 0.16 | -0.012 | -0.057 | +0.051 | -0.108 |
| sniper_ob_mean_threshold | 1h | fx_raw | 0.19 | 0.07 | -0.135 | -0.070 | +0.111 | -0.180 |
| sniper_ote_retrace | 1h | fx_raw | 0.44 | 0.26 | +0.015 | -0.046 | +0.030 | -0.075 |
| sniper_round_number_sweep | 1h | fx_raw | 1.20 | 0.07 | -0.244 | -0.218 | +0.129 | -0.347 |
| sniper_sweep_reclaim | 1h | fx_raw | 2.75 | 0.15 | -0.014 | +0.039 | +0.071 | -0.032 |
| sniper_sweep_reclaim_limit | 1h | fx_raw | 0.92 | 0.10 | -0.068 | -0.072 | +0.105 | -0.177 |
| sniper_vwap_reversion | 1h | fx_raw | 0.16 | 0.10 | +0.438 | +0.142 | +0.101 | +0.041 |
| trend_donchian_breakout | 1h | fx_raw | 2.12 | 0.27 | +0.010 | +0.025 | +0.032 | -0.008 |
| sniper_break_retest | 4h | fx_raw | 0.37 | 0.17 | -0.075 | -0.067 | +0.044 | -0.111 |
| sniper_ema_pullback | 4h | fx_raw | 0.65 | 0.38 | +0.084 | -0.042 | +0.027 | -0.069 |
| sniper_ema_pullback_limit | 4h | fx_raw | 0.65 | 0.37 | +0.082 | -0.041 | +0.024 | -0.065 |
| sniper_fvg_retrace | 4h | fx_raw | 0.11 | 0.40 | -0.159 | +0.112 | +0.021 | +0.090 |
| sniper_ob_mean_threshold | 4h | fx_raw | 0.05 | 0.14 | -0.107 | +0.316 | +0.061 | +0.255 |
| sniper_ote_retrace | 4h | fx_raw | 0.12 | 0.53 | +0.065 | -0.124 | +0.014 | -0.138 |
| sniper_round_number_sweep | 4h | fx_raw | 0.46 | 0.14 | -0.062 | -0.183 | +0.069 | -0.252 |
| sniper_sweep_reclaim | 4h | fx_raw | 1.37 | 0.28 | -0.029 | +0.007 | +0.037 | -0.030 |
| sniper_sweep_reclaim_limit | 4h | fx_raw | 0.53 | 0.15 | -0.152 | -0.186 | +0.059 | -0.245 |
| sniper_vwap_reversion | 4h | fx_raw | 0.02 | 0.16 | -0.629 | -0.198 | +0.072 | -0.270 |
| trend_donchian_breakout | 4h | fx_raw | 0.52 | 0.57 | +0.034 | +0.094 | +0.015 | +0.080 |
| sniper_break_retest | 1h | fx_std | 0.65 | 0.07 | -0.313 | -0.369 | +0.022 | -0.391 |
| sniper_ema_pullback | 1h | fx_std | 2.10 | 0.18 | -0.079 | -0.080 | +0.023 | -0.102 |
| sniper_ema_pullback_limit | 1h | fx_std | 2.06 | 0.18 | -0.083 | -0.098 | +0.010 | -0.108 |
| sniper_fvg_retrace | 1h | fx_std | 0.41 | 0.16 | -0.056 | -0.119 | +0.010 | -0.130 |
| sniper_ob_mean_threshold | 1h | fx_std | 0.20 | 0.07 | -0.245 | -0.241 | +0.028 | -0.269 |
| sniper_ote_retrace | 1h | fx_std | 0.43 | 0.26 | -0.036 | -0.078 | +0.006 | -0.084 |
| sniper_round_number_sweep | 1h | fx_std | 1.18 | 0.07 | -0.379 | -0.352 | +0.030 | -0.382 |
| sniper_sweep_reclaim | 1h | fx_std | 2.81 | 0.15 | -0.073 | -0.058 | +0.030 | -0.088 |
| sniper_sweep_reclaim_limit | 1h | fx_std | 0.91 | 0.10 | -0.159 | -0.223 | +0.024 | -0.247 |
| sniper_vwap_reversion | 1h | fx_std | 0.16 | 0.10 | +0.236 | -0.029 | +0.043 | -0.073 |
| trend_donchian_breakout | 1h | fx_std | 2.13 | 0.27 | -0.016 | -0.016 | +0.014 | -0.030 |
| sniper_break_retest | 4h | fx_std | 0.36 | 0.17 | -0.126 | -0.144 | +0.009 | -0.153 |
| sniper_ema_pullback | 4h | fx_std | 0.65 | 0.38 | +0.073 | -0.079 | +0.011 | -0.091 |
| sniper_ema_pullback_limit | 4h | fx_std | 0.64 | 0.38 | +0.074 | -0.088 | +0.005 | -0.092 |
| sniper_fvg_retrace | 4h | fx_std | 0.11 | 0.40 | -0.183 | +0.059 | +0.004 | +0.055 |
| sniper_ob_mean_threshold | 4h | fx_std | 0.05 | 0.14 | -0.029 | +0.228 | +0.015 | +0.213 |
| sniper_ote_retrace | 4h | fx_std | 0.12 | 0.53 | +0.075 | -0.144 | +0.003 | -0.147 |
| sniper_round_number_sweep | 4h | fx_std | 0.46 | 0.14 | -0.107 | -0.264 | +0.015 | -0.278 |
| sniper_sweep_reclaim | 4h | fx_std | 1.38 | 0.28 | -0.056 | -0.055 | +0.016 | -0.070 |
| sniper_sweep_reclaim_limit | 4h | fx_std | 0.52 | 0.15 | -0.190 | -0.278 | +0.013 | -0.291 |
| sniper_vwap_reversion | 4h | fx_std | 0.02 | 0.15 | -0.679 | -0.349 | +0.033 | -0.382 |
| trend_donchian_breakout | 4h | fx_std | 0.52 | 0.57 | +0.031 | +0.072 | +0.006 | +0.066 |

## Inside the conditions chosen in-sample (the record the gate reads)

Only regimes and sessions that were positive after costs in-sample (at least 20 trades each) are kept; the out-of-sample trades inside them are the evidence.

| Setup | TF | Costs | Allowed regimes | Allowed sessions | IS n | IS net R | OOS n | OOS net R | OOS t | OOS t (by day) |
|---|---|---|---|---|---|---|---|---|---|---|
| sniper_ote_retrace | 1h | fx_raw | trend_low_vol | asia london | 123 | +0.039 | 154 | -0.074 | -0.62 | -0.59 |
| sniper_vwap_reversion | 1h | fx_raw | range_high_vol range_low_vol | london ny | 97 | +0.426 | 123 | +0.250 | 1.73 | 1.80 |
| trend_donchian_breakout | 1h | fx_raw | trend_low_vol | ny | 196 | +0.120 | 313 | -0.025 | -0.26 | -0.24 |
| sniper_ema_pullback | 4h | fx_raw | trend_low_vol | asia ny | 118 | +0.209 | 217 | -0.050 | -0.52 | -0.52 |
| sniper_ema_pullback_limit | 4h | fx_raw | trend_low_vol | asia ny | 117 | +0.231 | 217 | -0.039 | -0.40 | -0.41 |
| sniper_ote_retrace | 4h | fx_raw | trend_low_vol | london | 22 | +0.477 | 22 | -0.426 | -1.56 | -1.52 |
| sniper_sweep_reclaim | 4h | fx_raw | range_high_vol range_low_vol | asia | 25 | -0.231 | 73 | +0.093 | 0.52 | 0.53 |
| trend_donchian_breakout | 4h | fx_raw | trend_high_vol | asia london | 90 | -0.051 | 111 | +0.312 | 1.86 | 1.90 |
| sniper_fvg_retrace | 1h | fx_std | trend_low_vol | ny | 38 | +0.420 | 59 | -0.084 | -0.46 | -0.44 |
| sniper_vwap_reversion | 1h | fx_std | range_high_vol range_low_vol | london ny | 97 | +0.280 | 123 | +0.115 | 0.83 | 0.85 |
| sniper_ema_pullback | 4h | fx_std | trend_low_vol | asia ny | 119 | +0.218 | 217 | -0.078 | -0.81 | -0.82 |
| sniper_ema_pullback_limit | 4h | fx_std | trend_high_vol trend_low_vol | asia ny | 287 | +0.135 | 431 | -0.117 | -1.80 | -1.75 |
| sniper_ote_retrace | 4h | fx_std | trend_low_vol | london | 22 | +0.487 | 21 | -0.385 | -1.35 | -1.33 |
| trend_donchian_breakout | 4h | fx_std | trend_high_vol | asia london | 90 | -0.053 | 112 | +0.313 | 1.89 | 1.91 |

## What passes the owner's gate

3 configuration(s) have at least 30 effectively independent out-of-sample trades and mean - 1 SE > 0 after costs, with the SE clustered by day as well as per trade (Gate 4's math score of 2). The scanner's gate can take only these:

- `trend_donchian_breakout@4h@fx_std`: OOS n 112 (effective 112), +0.313R per trade (SE 0.166), 0.11 trades/day, regimes trend_high_vol, sessions asia, london
- `sniper_vwap_reversion@1h@fx_raw`: OOS n 123 (effective 123), +0.250R per trade (SE 0.145), 0.12 trades/day, regimes range_high_vol, range_low_vol, sessions london, ny
- `trend_donchian_breakout@4h@fx_raw`: OOS n 111 (effective 111), +0.312R per trade (SE 0.167), 0.11 trades/day, regimes trend_high_vol, sessions asia, london

Passing Gate 4 is necessary, not sufficient: read it together with the multiple-testing result below.

## Multiple testing

44 configurations were tried; 12 had at least 30 effectively independent out-of-sample trades inside their chosen conditions. The best of those (`trend_donchian_breakout@4h@fx_std`, per-trade Sharpe +0.178 over 112 trades) has a deflated-Sharpe probability of 0.37 of being real once the number of trials is counted (Bailey & López de Prado; 0.95 is the usual bar).

## Reading this as the owner's philosophy asks

- **Forex and gold.** Best out-of-sample average before costs: +0.316R per trade (sniper_ob_mean_threshold 4h). 7 of 44 configurations are positive after costs out-of-sample (before the in-sample condition filter).
- A pattern that does not pay before costs cannot be rescued by a cheaper venue; cheaper costs only shrink the loss (Section VII: expected value first).
- Cost in R = round-trip cost / stop distance. A 5-minute crypto stop of 0.2-0.3% against a 0.2% round trip costs most of 1R; the same stop in EUR/USD against a 0.01% round trip costs a few hundredths (Gate 5.6).
- More trades is not more edge: every trade pays the cost, so frequency multiplies a negative expectancy.
- Only the out-of-sample columns are evidence; in-sample numbers chose the conditions (Section XVII).


<!-- ===== FILE: trading-intelligence/10_sniper-lab/backtests/setups.yaml ===== -->

```yaml
# Generated by `python -m trading_intelligence.sniper lab` - do not edit by hand.
# The codified sniper setups as graph nodes (kind: setup), each linked to the playbooks and concepts
# it was coded from, with its out-of-sample result (net R per trade after costs; best six configs).
setups:
- id: sniper_sweep_reclaim
  type: setup
  title: Prior-day liquidity sweep + reclaim (codified)
  derived_from:
  - strategy_candace_lau_nq_sweep_reversal
  - strategy_marco_trades_liquidity_grab
  - strategy_dhesi_liquidity_inversion
  - concept_liquidity_sweep_reversal
  - concept_liquidity
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:SweepReclaim
  rules: 'Prior-day low (high) swept by at least `min_sweep_atr` x ATR, and the bar closes back inside: stops below an obvious level were run and absorbed. Enter
    at market on the next open, stop beyond the sweep extreme, target `rr` R.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config: &id001
    config: sniper_sweep_reclaim@4h@fx_raw
    oos_trades: 1375
    oos_gross_r: 0.007
    oos_net_r: -0.03
  tested:
  - *id001
  - config: sniper_sweep_reclaim@1h@fx_raw
    oos_trades: 2762
    oos_gross_r: 0.039
    oos_net_r: -0.032
  - config: sniper_sweep_reclaim@4h@fx_std
    oos_trades: 1381
    oos_gross_r: -0.055
    oos_net_r: -0.07
  - config: sniper_sweep_reclaim@1h@fx_std
    oos_trades: 2822
    oos_gross_r: -0.058
    oos_net_r: -0.088
- id: sniper_fvg_retrace
  type: setup
  title: Fair value gap retrace in the HTF trend (codified)
  derived_from:
  - strategy_trader_mayne_structure_ote
  - strategy_abraham_perez_ict_orderflow
  - strategy_nbb_trader_po3_ote_adr
  - concept_fair_value_gap
  - concept_smart_money_concepts
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:FVGRetrace
  rules: A displacement candle (body >= `disp_atr` x ATR) in the direction of the HTF trend leaves a three-candle fair value gap; rest a LIMIT at the gap's midpoint;
    stop beyond the displacement candle; target `rr` R.
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config: &id002
    config: sniper_fvg_retrace@4h@fx_raw
    oos_trades: 112
    oos_gross_r: 0.112
    oos_net_r: 0.09
  tested:
  - *id002
  - config: sniper_fvg_retrace@4h@fx_std
    oos_trades: 109
    oos_gross_r: 0.059
    oos_net_r: 0.055
  - config: sniper_fvg_retrace@1h@fx_raw
    oos_trades: 415
    oos_gross_r: -0.057
    oos_net_r: -0.108
  - config: sniper_fvg_retrace@1h@fx_std
    oos_trades: 407
    oos_gross_r: -0.119
    oos_net_r: -0.13
- id: sniper_ote_retrace
  type: setup
  title: Optimal trade entry (62-79% retracement) after a break of structure (codified)
  derived_from:
  - strategy_trader_mayne_structure_ote
  - strategy_nbb_trader_po3_ote_adr
  - concept_premium_discount_ote
  - concept_fibonacci
  - concept_market_structure
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:OTERetrace
  rules: 'In an HTF uptrend, a fresh 5m swing high above a leg of >= `leg_atr` x ATR: rest a LIMIT at the `fib` (0.705) retracement of the leg (the optimal trade
    entry zone), stop below the leg''s origin, target the swing high.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config: &id003
    config: sniper_ote_retrace@1h@fx_raw
    oos_trades: 441
    oos_gross_r: -0.046
    oos_net_r: -0.075
  tested:
  - *id003
  - config: sniper_ote_retrace@1h@fx_std
    oos_trades: 431
    oos_gross_r: -0.078
    oos_net_r: -0.084
  - config: sniper_ote_retrace@4h@fx_raw
    oos_trades: 120
    oos_gross_r: -0.124
    oos_net_r: -0.138
  - config: sniper_ote_retrace@4h@fx_std
    oos_trades: 119
    oos_gross_r: -0.144
    oos_net_r: -0.147
- id: sniper_orb_retest
  type: setup
  title: Opening-range breakout and retest (New York open) (codified)
  derived_from:
  - strategy_vincent_desiano_break_retest
  - strategy_okala_80_20_nasdaq
  - concept_breakout_trading
  - concept_trading_sessions_killzones
  - concept_support_resistance
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:ORBRetest
  rules: 'New York opening range (09:30-10:00 New York time, daylight saving included): after the first close beyond the range, rest a LIMIT at the range edge for
    the retest; stop at the range midpoint; target `rr` R. Entries until `last_entry` New York; timeframes of 30 minutes or less.'
  markets:
  - crypto
  - fx
  max_timeframe: 30m
  verdict: not tested
  best_config: null
  tested: []
- id: sniper_ema_pullback
  type: setup
  title: Trend pullback to the 20 EMA with a rejection close (codified)
  derived_from:
  - strategy_marci_silfrain_measured_move
  - strategy_tori_trendline_4h
  - strategy_anthony_crudele_futures_trend
  - concept_trend_following
  - concept_moving_averages
  - concept_multi_timeframe_analysis
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:EMAPullback
  rules: 'HTF trend; a 5m bar dips to the 20 EMA and closes back in the trend direction as a rejection candle: enter at market on the next open, stop beyond the bar,
    target `rr` R.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config: &id004
    config: sniper_ema_pullback@1h@fx_raw
    oos_trades: 2084
    oos_gross_r: -0.008
    oos_net_r: -0.063
  tested:
  - *id004
  - config: sniper_ema_pullback@4h@fx_raw
    oos_trades: 652
    oos_gross_r: -0.042
    oos_net_r: -0.069
  - config: sniper_ema_pullback@4h@fx_std
    oos_trades: 652
    oos_gross_r: -0.079
    oos_net_r: -0.091
  - config: sniper_ema_pullback@1h@fx_std
    oos_trades: 2106
    oos_gross_r: -0.08
    oos_net_r: -0.102
- id: sniper_vwap_reversion
  type: setup
  title: VWAP band re-entry in a range (codified)
  derived_from:
  - strategy_lance_breitstein_mean_reversion
  - strategy_jj_simon_fair_pricing
  - concept_vwap
  - concept_mean_reversion
  - concept_auction_market_theory
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:VWAPReversion
  rules: 'In a range regime, a close back inside the VWAP - `k` sd band after a close outside it: enter at market, stop beyond the 3-bar extreme, target the session
    VWAP.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config: &id005
    config: sniper_vwap_reversion@1h@fx_raw
    oos_trades: 159
    oos_gross_r: 0.142
    oos_net_r: 0.041
  tested:
  - *id005
  - config: sniper_vwap_reversion@1h@fx_std
    oos_trades: 159
    oos_gross_r: -0.029
    oos_net_r: -0.073
  - config: sniper_vwap_reversion@4h@fx_raw
    oos_trades: 19
    oos_gross_r: -0.198
    oos_net_r: -0.27
  - config: sniper_vwap_reversion@4h@fx_std
    oos_trades: 20
    oos_gross_r: -0.349
    oos_net_r: -0.382
- id: sniper_break_retest
  type: setup
  title: Break and retest of a key level (codified)
  derived_from:
  - strategy_vincent_desiano_break_retest
  - strategy_gala_trades_price_action
  - strategy_abraham_perez_ict_orderflow
  - concept_support_resistance
  - concept_breakout_trading
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:BreakRetest
  rules: 'Research spec S5. A momentum close through the prior-day high (low) or the last confirmed HTF pivot, after a close on the other side: rest a LIMIT just
    beyond the level for the retest; stop 0.5 ATR back through the level; target 2R. 03:00-12:00 New York.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config: &id006
    config: sniper_break_retest@4h@fx_raw
    oos_trades: 367
    oos_gross_r: -0.067
    oos_net_r: -0.111
  tested:
  - *id006
  - config: sniper_break_retest@4h@fx_std
    oos_trades: 365
    oos_gross_r: -0.144
    oos_net_r: -0.153
  - config: sniper_break_retest@1h@fx_raw
    oos_trades: 663
    oos_gross_r: -0.251
    oos_net_r: -0.353
  - config: sniper_break_retest@1h@fx_std
    oos_trades: 653
    oos_gross_r: -0.369
    oos_net_r: -0.391
- id: sniper_asia_london_judas
  type: setup
  title: Asia range, London sweep, return (session liquidity model) (codified)
  derived_from:
  - strategy_candace_lau_nq_sweep_reversal
  - strategy_nbb_trader_po3_ote_adr
  - strategy_jadecap_liquidity_volatility
  - concept_amd_power_of_three
  - concept_trading_sessions_killzones
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:AsiaLondonJudas
  rules: 'Research spec S8. A compressed Asia range (20:00-24:00 New York, at most 0.5 x the 10-day average daily range) is swept in the London window (02:00-05:00
    New York) and price closes back inside within 6 bars: rest a LIMIT at the swept Asia extreme; stop beyond the sweep; target the opposite Asia extreme (at least
    1.5R); flat by 11:00 New York.'
  markets:
  - crypto
  - fx
  max_timeframe: 15m
  verdict: not tested
  best_config: null
  tested: []
- id: sniper_round_number_sweep
  type: setup
  title: Round-number stop run and reclaim (codified)
  derived_from:
  - strategy_okala_80_20_nasdaq
  - strategy_marco_trades_liquidity_grab
  - concept_support_resistance
  - concept_liquidity_sweep_reversal
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:RoundNumberSweep
  rules: 'Research spec S9. Price approached a round number from one side for 12 closes, poked through it by 0.05-1.0 ATR and closed back: rest a LIMIT at the round
    number; stop beyond the poke; target 2R. 02:00-16:00 New York. The grid is per market (BTC $1,000, ETH $100, EUR/USD 0.0050, gold $10).'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config: &id007
    config: sniper_round_number_sweep@4h@fx_raw
    oos_trades: 464
    oos_gross_r: -0.183
    oos_net_r: -0.252
  tested:
  - *id007
  - config: sniper_round_number_sweep@4h@fx_std
    oos_trades: 458
    oos_gross_r: -0.264
    oos_net_r: -0.278
  - config: sniper_round_number_sweep@1h@fx_raw
    oos_trades: 1204
    oos_gross_r: -0.218
    oos_net_r: -0.347
  - config: sniper_round_number_sweep@1h@fx_std
    oos_trades: 1182
    oos_gross_r: -0.352
    oos_net_r: -0.382
- id: sniper_ob_mean_threshold
  type: setup
  title: Order-block retest at the 50% after a break of structure (codified)
  derived_from:
  - strategy_trader_mayne_structure_ote
  - concept_order_blocks_breakers
  - concept_market_structure
  - concept_premium_discount_ote
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:OrderBlockMT
  rules: Research spec S10 on one timeframe. A momentum close through the last confirmed pivot (body >= 0.8 ATR); the order block is the last opposite candle in the
    8 bars before the break; if its 50% (mean threshold) is in the discount half of the dealing range, rest a LIMIT there; stop beyond the block; target the dealing-range
    extreme (at least 1.5R).
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config: &id008
    config: sniper_ob_mean_threshold@4h@fx_raw
    oos_trades: 43
    oos_gross_r: 0.316
    oos_net_r: 0.255
  tested:
  - *id008
  - config: sniper_ob_mean_threshold@4h@fx_std
    oos_trades: 46
    oos_gross_r: 0.228
    oos_net_r: 0.213
  - config: sniper_ob_mean_threshold@1h@fx_raw
    oos_trades: 188
    oos_gross_r: -0.07
    oos_net_r: -0.18
  - config: sniper_ob_mean_threshold@1h@fx_std
    oos_trades: 204
    oos_gross_r: -0.241
    oos_net_r: -0.269
- id: sniper_sweep_reclaim_limit
  type: setup
  title: Prior-day sweep + reclaim, retest entry (limit) (codified)
  derived_from:
  - strategy_candace_lau_nq_sweep_reversal
  - strategy_marco_trades_liquidity_grab
  - strategy_dhesi_liquidity_inversion
  - concept_liquidity_sweep_reversal
  - concept_liquidity
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:SweepReclaimRetest
  rules: 'Research spec S1, the maker version of the prior-day sweep: after the sweep and reclaim inside the London or New York morning window, rest a LIMIT at the
    reclaimed level (the retest) instead of buying the next open; stop beyond the sweep; target 2R.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config: &id009
    config: sniper_sweep_reclaim_limit@1h@fx_raw
    oos_trades: 921
    oos_gross_r: -0.072
    oos_net_r: -0.177
  tested:
  - *id009
  - config: sniper_sweep_reclaim_limit@4h@fx_raw
    oos_trades: 531
    oos_gross_r: -0.186
    oos_net_r: -0.245
  - config: sniper_sweep_reclaim_limit@1h@fx_std
    oos_trades: 913
    oos_gross_r: -0.223
    oos_net_r: -0.247
  - config: sniper_sweep_reclaim_limit@4h@fx_std
    oos_trades: 522
    oos_gross_r: -0.278
    oos_net_r: -0.291
- id: sniper_ema_pullback_limit
  type: setup
  title: Trend pullback to the 20 EMA, limit entry (codified)
  derived_from:
  - strategy_marci_silfrain_measured_move
  - strategy_tori_trendline_4h
  - strategy_anthony_crudele_futures_trend
  - concept_trend_following
  - concept_moving_averages
  - concept_multi_timeframe_analysis
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:EMAPullbackLimit
  rules: 'Maker version of the EMA pullback: rest a LIMIT at the rejection bar''s close for 2 bars instead of buying the next open (it fills only if price comes back
    to it).'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config: &id010
    config: sniper_ema_pullback_limit@4h@fx_raw
    oos_trades: 656
    oos_gross_r: -0.041
    oos_net_r: -0.065
  tested:
  - *id010
  - config: sniper_ema_pullback_limit@1h@fx_raw
    oos_trades: 2067
    oos_gross_r: -0.026
    oos_net_r: -0.074
  - config: sniper_ema_pullback_limit@4h@fx_std
    oos_trades: 641
    oos_gross_r: -0.088
    oos_net_r: -0.092
  - config: sniper_ema_pullback_limit@1h@fx_std
    oos_trades: 2059
    oos_gross_r: -0.098
    oos_net_r: -0.108
- id: trend_donchian_breakout
  type: setup
  title: Donchian 20-bar breakout (Turtle-style trend model) (codified)
  derived_from:
  - person_richard_donchian
  - person_richard_dennis
  - book_way_of_the_turtle
  - book_complete_turtletrader
  - book_trend_following_covel
  - concept_trend_following
  - concept_breakout_trading
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:DonchianTrend
  rules: 'Trend model (not a sniper entry): a fresh close beyond the previous 20-bar high (low), market entry, 2 ATR stop, 3R target, time exit after 60 bars. The
    Turtle rule set simplified to a bracket.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config: &id011
    config: trend_donchian_breakout@4h@fx_raw
    oos_trades: 522
    oos_gross_r: 0.094
    oos_net_r: 0.08
  tested:
  - *id011
  - config: trend_donchian_breakout@4h@fx_std
    oos_trades: 524
    oos_gross_r: 0.072
    oos_net_r: 0.066
  - config: trend_donchian_breakout@1h@fx_raw
    oos_trades: 2126
    oos_gross_r: 0.025
    oos_net_r: -0.008
  - config: trend_donchian_breakout@1h@fx_std
    oos_trades: 2139
    oos_gross_r: -0.016
    oos_net_r: -0.03
- id: lit_intraday_momentum
  type: setup
  title: 'Intraday momentum: first half-hour predicts the last half-hour (codified)'
  derived_from:
  - concept_trend_following
  - concept_trading_sessions_killzones
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:IntradayMomentum
  rules: 'Published effect (Gao, Han, Li & Zhou 2018 for the S&P 500; Shen, Urquhart & Wang 2022 for Bitcoin): the first half-hour''s return predicts the last half-hour''s.
    At 23:30 UTC, trade the last half-hour of the UTC day in the direction of the 00:00-00:30 return; protective stop 3 ATR; time exit at 24:00. Crypto only (a 24-hour
    market with a UTC day).'
  markets:
  - crypto
  max_timeframe: 30m
  verdict: not tested
  best_config: null
  tested: []
```


<!-- ===== FILE: trading-intelligence/10_sniper-lab/books-sniper.yaml ===== -->

```yaml
# Sniper-lab reading list: books NOT already in 05_books-top-100/books.yaml.
# Companion to 10_sniper-lab/reading-list.md (id: synthesis_sniper_reading_list),
# which explains why each book matters for a bot that takes precise entries,
# lists the in-KB books to read alongside, and gives the non-book sources
# (ICT 2022 mentorship, academic papers on intraday patterns).
#
# Fields follow books.yaml: id, title, author, year, category, covers (concept ids),
# key_idea (one-sentence paraphrase, Claude's words, T5). Extra fields:
# publisher, format, source (where the bibliographic facts were read, 2026-10-20).
# Education, not financial advice. Nothing here is a win-rate or P&L claim.

books:
  # --- Price action and precise entries -------------------------------------
  - id: book_trading_price_action_trends
    title: "Trading Price Action Trends: Technical Analysis of Price Charts Bar by Bar for the Serious Trader"
    author: "Al Brooks"
    year: 2011
    publisher: "Wiley"
    format: book
    category: price_action
    covers: [concept_price_action, concept_trend_following, concept_market_structure, concept_moving_averages, concept_trade_execution]
    key_idea: "Treats every 5-minute bar as evidence of who controls the market and enters with a trend on its pullbacks, typically the second attempt to resume, rather than predicting turns."
    source: "https://tenlong.com.tw/products/9781118066515"

  - id: book_trading_price_action_trading_ranges
    title: "Trading Price Action Trading Ranges: Technical Analysis of Price Charts Bar by Bar for the Serious Trader"
    author: "Al Brooks"
    year: 2012
    publisher: "Wiley"
    format: book
    category: price_action
    covers: [concept_price_action, concept_breakout_trading, concept_mean_reversion, concept_support_resistance, concept_market_regimes, concept_expectancy, concept_risk_reward_r_multiples]
    key_idea: "Inside a range most breakout attempts fail, so the edges are faded and breakouts are taken only on strong follow-through, with every trade checked against probability times reward versus the chance of loss times risk."
    source: "https://www.oreilly.com/library/view/-/9781118172339/"

  - id: book_trading_price_action_reversals
    title: "Trading Price Action Reversals: Technical Analysis of Price Charts Bar by Bar for the Serious Trader"
    author: "Al Brooks"
    year: 2012
    publisher: "Wiley"
    format: book
    category: price_action
    covers: [concept_price_action, concept_liquidity_sweep_reversal, concept_market_structure, concept_trendlines, concept_chart_patterns]
    key_idea: "Most reversal attempts against a trend fail; a tradeable reversal usually needs a trendline break first and then a failed test of the old extreme before a signal bar is taken."
    source: "https://oreilly.com/library/view/trading-price-action/9781118172308"

  - id: book_forex_price_action_scalping
    title: "Forex Price Action Scalping: An In-Depth Look into the Field of Professional Scalping"
    author: "Bob Volman"
    year: 2011
    publisher: "Light Tower Publishing"
    format: book
    category: price_action
    covers: [concept_scalping, concept_price_action, concept_breakout_trading, concept_support_resistance, concept_moving_averages, concept_trade_execution]
    key_idea: "Scalps EUR/USD on a 70-tick chart with a fixed small bracket, entering only when a tight build-up of bars near a short moving average breaks, and names a small set of break patterns precise enough to code."
    source: "https://www.goodreads.com/book/show/13269524-forex-price-action-scalping"

  - id: book_understanding_price_action
    title: "Understanding Price Action: Practical Analysis of the 5-Minute Time Frame"
    author: "Bob Volman"
    year: 2014
    publisher: "Light Tower Publishing"
    format: book
    category: price_action
    covers: [concept_price_action, concept_scalping, concept_support_resistance, concept_breakout_trading, concept_market_structure, concept_trade_management]
    key_idea: "Walks through six consecutive months of annotated 5-minute EUR/USD charts to train when a setup has real pressure behind it and, just as often, when to skip it."
    source: "https://www.abebooks.com/Understanding-Price-Action-Practical-Analysis-5-Minute/30325842905/bd"

  - id: book_ytc_price_action_trader
    title: "YTC Price Action Trader"
    author: "Lance Beggs"
    year: 2012   # earliest dated mention found (forum post, 2012); original release year not confirmed
    publisher: "Your Trading Coach (self-published)"
    format: e-book course (six PDF volumes)
    category: price_action
    covers: [concept_price_action, concept_multi_timeframe_analysis, concept_support_resistance, concept_market_structure, concept_trading_plan, concept_trade_management, concept_trading_journal_review]
    key_idea: "A top-down process in which higher-timeframe structure and levels decide where to look and lower-timeframe swing strength or weakness decides when to enter, wrapped in a written plan and a review loop."
    source: "https://nexusfi.com/showthread.php?p=233556"

  - id: book_trading_by_the_minute
    title: "Trading by the Minute"
    author: "Joe Ross"
    year: 1997
    publisher: "Ross Trading International"
    format: book
    category: day_trading
    covers: [concept_price_action, concept_market_structure, concept_breakout_trading, concept_trade_management]
    key_idea: "Sorts intraday signals into major, minor and intermediate classes and gives explicit rules for the initial stop and for the stop that protects open profit."
    source: "https://abebooks.com/9789768108258/Trading-Minute-Ross-Joe-9768108258/plp"

  # --- Intraday playbooks ---------------------------------------------------
  - id: book_how_to_day_trade_for_a_living
    title: "How to Day Trade for a Living"
    author: "Andrew Aziz"
    year: 2016
    publisher: "Self-published"
    format: book
    category: day_trading
    covers: [concept_vwap, concept_breakout_trading, concept_support_resistance, concept_moving_averages, concept_position_sizing, concept_risk_reward_r_multiples]
    key_idea: "A beginner's day-trading framework for US stocks: trade only the few names with unusual activity that day, fix the risk per trade in advance, and use a short list of intraday setups."
    source: "https://www.goodreads.com/book/show/31808862"

  - id: book_logical_trader
    title: "The Logical Trader: Applying a Method to the Madness"
    author: "Mark B. Fisher"
    year: 2002
    publisher: "Wiley"
    format: book
    category: day_trading
    covers: [concept_breakout_trading, concept_pivot_points, concept_trading_sessions_killzones, concept_market_structure, concept_position_sizing, concept_trading_psychology]
    key_idea: "The ACD method: mark the opening range, enter only when price clears it by a set offset, stop at a reference level on the other side, and use a daily pivot range to size and filter the trade."
    source: "https://nexusfi.com/a/strategies/acd-trading-method"

  - id: book_the_playbook
    title: "The PlayBook: An Inside Look at How to Think Like a Professional Trader"
    author: "Mike Bellafiore"
    year: 2013
    publisher: "FT Press"
    format: book
    category: day_trading
    covers: [concept_trading_plan, concept_trading_journal_review, concept_trade_execution, concept_support_resistance, concept_breakout_trading, concept_trade_management]
    key_idea: "Write each setup down as a play, with its context, intraday levels, entry, exit and sizing, then review it after the session; this is the prop-desk version of a strategy spec."
    source: "https://ptgmedia.pearsoncmg.com/images/9780132937641/samplepages/0132937646.pdf"

  - id: book_volume_profile_insiders_guide
    title: "Volume Profile: The Insider's Guide to Trading"
    author: "Trader Dale"
    year: 2018
    publisher: "Independently published"
    format: book
    category: auction_market_theory
    covers: [concept_volume_profile, concept_auction_market_theory, concept_support_resistance, concept_order_flow, concept_liquidity]
    key_idea: "Reads volume-at-price to find where large participants built positions and places resting entries at those zones with the stop just beyond them."
    source: "https://ebay.it/itm/363344849625"

  # --- Systematic short-term trading and entry/exit research -----------------
  - id: book_short_term_trading_strategies_that_work
    title: "Short Term Trading Strategies That Work"
    author: "Larry Connors & Cesar Alvarez"
    year: 2008
    publisher: "TradingMarkets"
    format: book
    category: quant_algorithmic
    covers: [concept_mean_reversion, concept_oscillators_momentum, concept_moving_averages, concept_backtesting, concept_market_regimes]
    key_idea: "Buys sharp short-term pullbacks, such as an extreme 2-period RSI, only while price is above its long-term average, and exits on the first snap-back; the claim that stops hurt this style is a hypothesis to test."
    source: "https://www.abebooks.com/Short-Term-Trading-Strategies-Work-Larry/31620720826/bd"

  - id: book_entry_exit_confessions
    title: "Entry and Exit Confessions of a Champion Trader: 52 Ways a Professional Speculator Gets In and Out of the Stock, Futures and Forex Markets"
    author: "Kevin J. Davey"
    year: 2019
    publisher: "Independently published"
    format: book
    category: quant_algorithmic
    covers: [concept_backtesting, concept_trade_execution, concept_trade_management, concept_breakout_trading, concept_overfitting_validation]
    key_idea: "Treats entries and exits as separate parts to be tested one at a time, giving 41 entries and 11 exits in code, so an entry's raw edge can be checked before any exit is added."
    source: "https://www.goodreads.com/work/editions/70058912-entry-and-exit-confessions-of-a-champion-trader-52-ways-a-professional"

  - id: book_machine_trading
    title: "Machine Trading: Deploying Computer Algorithms to Conquer the Markets"
    author: "Ernest P. Chan"
    year: 2017
    publisher: "Wiley"
    format: book
    category: quant_algorithmic
    covers: [concept_market_microstructure, concept_order_flow, concept_time_series_statistics, concept_machine_learning_finance, concept_backtesting, concept_mean_reversion]
    key_idea: "A practitioner's tour of algorithmic strategies with code, including a chapter on intraday trading and market microstructure and one on bitcoin."
    source: "https://www.wiley-vch.de/en/areas-interest/finance-economics-law/machine-trading-978-1-119-21960-6"

  # --- Validation -----------------------------------------------------------
  - id: book_evaluation_optimization_trading_strategies
    title: "The Evaluation and Optimization of Trading Strategies (2nd ed.)"
    author: "Robert Pardo"
    year: 2008
    publisher: "Wiley"
    format: book
    category: quant_algorithmic
    covers: [concept_backtesting, concept_overfitting_validation, concept_performance_metrics, concept_trading_plan]
    key_idea: "Walk-forward analysis: optimise on one window, trade the next unseen window, roll forward, and judge a strategy by how much of its in-sample result survives."
    source: "https://www.wiley-vch.de/en/areas-interest/finance-economics-law/the-evaluation-and-optimization-of-trading-strategies-978-0-470-12801-5"

  - id: book_testing_tuning_trading_systems
    title: "Testing and Tuning Market Trading Systems: Algorithms in C++"
    author: "Timothy Masters"
    year: 2018
    publisher: "Apress"
    format: book
    category: quant_algorithmic
    covers: [concept_backtesting, concept_overfitting_validation, concept_performance_metrics, concept_time_series_statistics, concept_probabilistic_thinking]
    key_idea: "Statistical tests, among them walk-forward, cross-validation and Monte Carlo permutation tests, that ask whether a backtest result could have come from luck or from choosing the best of many tries."
    source: "https://www.abebooks.com/Testing-Tuning-Market-Trading-Systems-Timothy/32234804369/bd"

  # --- Small-account risk, stops and sizing ---------------------------------
  - id: book_leveraged_trading
    title: "Leveraged Trading: A Professional Approach to Trading FX, Stocks on Margin, CFDs, Spread Bets and Futures for All Traders"
    author: "Robert Carver"
    year: 2019
    publisher: "Harriman House"
    format: book
    category: risk_money_management
    covers: [concept_leverage_margin, concept_position_sizing, concept_volatility, concept_risk_of_ruin_drawdown, concept_trade_execution, concept_trend_following]
    key_idea: "Leverage magnifies both losses and costs, so a small trader should start with one simple, volatility-sized rule on one instrument and trade only as often as costs allow."
    source: "https://www.panmacmillan.com/authors/robert-carver/leveraged-trading/9780857197221"

  - id: book_maximum_adverse_excursion
    title: "Maximum Adverse Excursion: Analyzing Price Fluctuations for Trading Management"
    author: "John Sweeney"
    year: 1997
    publisher: "Wiley"
    format: book
    category: risk_money_management
    covers: [concept_trade_management, concept_risk_reward_r_multiples, concept_backtesting, concept_position_sizing]
    key_idea: "Record how far each trade moved against you before it closed; winners and losers tend to separate on that measure, so its distribution shows where a stop belongs."
    source: "https://www.wiley-vch.de/en/areas-interest/finance-economics-law/maximum-adverse-excursion-978-0-471-14152-5"

  - id: book_the_trading_game
    title: "The Trading Game: Playing by the Numbers to Make Millions"
    author: "Ryan Jones"
    year: 1999
    publisher: "Wiley"
    format: book
    category: risk_money_management
    covers: [concept_position_sizing, concept_risk_of_ruin_drawdown, concept_kelly_criterion_optimal_f, concept_leverage_margin]
    key_idea: "Fixed-ratio sizing adds one unit only after a fixed profit per unit already traded, a scheme built for small accounts that cannot trade fractions of the minimum size."
    source: "https://www.adaptrade.com/MSA/fixratio.htm"
```


<!-- ===== FILE: trading-intelligence/10_sniper-lab/reading-list.md ===== -->

---
id: synthesis_sniper_reading_list
type: synthesis
title: "Reading List — precise entries, short-term systems and small accounts"
partition: 10_sniper-lab
layer: L8
aliases: [sniper reading list, scalping books, price action books, intraday books, small account books, day trading books]
tags: [books, reading-list, price-action, scalping, order-flow, systematic, validation, small-account]
as_of: 2026-10-20
related: [philosophy_relationship, framework_decision_protocol, framework_source_tiers, synthesis_sniper_entries, synthesis_small_account_venues, synthesis_sniper_backtests, synthesis_evidence_lab, formula_sheet, framework_trading_journal, principle_04_conditional_probability, principle_05_mathematical_justification, principle_06_do_not_force, principle_09_protect_capital, principle_11_record_and_investigate, philo_mathematics_sword, philo_scientific_method, philo_conditional_probability, philo_capital_preservation, concept_price_action, concept_scalping, concept_order_flow, concept_volume_profile, concept_auction_market_theory, concept_market_microstructure, concept_breakout_trading, concept_mean_reversion, concept_trend_following, concept_market_structure, concept_market_regimes, concept_support_resistance, concept_liquidity_sweep_reversal, concept_vwap, concept_trading_sessions_killzones, concept_smart_money_concepts, concept_fair_value_gap, concept_premium_discount_ote, concept_backtesting, concept_overfitting_validation, concept_performance_metrics, concept_position_sizing, concept_leverage_margin, concept_risk_of_ruin_drawdown, concept_risk_reward_r_multiples, concept_expectancy, concept_trade_management, concept_trade_execution, concept_trading_plan, concept_trading_journal_review, book_reading_price_charts_bar_by_bar, book_crabel_opening_range, book_street_smarts, book_long_term_secrets_short_term_trading, book_trading_sardines, book_mastering_the_trade, book_building_winning_algo_systems, book_quantitative_trading_chan, book_algorithmic_trading_chan, book_systematic_trading, book_trading_systems_and_methods, book_evidence_based_ta, book_definitive_guide_position_sizing, book_mathematics_of_money_management, book_markets_in_profile, book_mind_over_markets, book_trades_about_to_happen, book_trading_and_exchanges, book_market_microstructure_in_practice, book_ta_multiple_timeframes, book_day_swing_trading_currency, book_art_science_technical_analysis, book_advances_financial_ml, mathbook_bouchaud_trades_quotes_prices, mathbook_cartea_algorithmic_hft, mathbook_hasbrouck_empirical_microstructure, paper_deflated_sharpe_2014, paper_bailey_pbo_2017, paper_white_2000, paper_barber_odean_2000, person_al_brooks, person_ernest_chan, person_robert_carver, person_larry_connors, person_perry_kaufman, person_michael_huddleston, person_linda_raschke, person_toby_crabel, strategy_vincent_desiano_break_retest, strategy_gala_trades_price_action, strategy_carmine_rosato_lvn, strategy_forrest_knight_volume_profile, strategy_fabio_valentini_amt_order_flow, strategy_abraham_perez_ict_orderflow, strategy_nbb_trader_po3_ote_adr, strategy_lance_breitstein_mean_reversion, concept_kelly_criterion_optimal_f, concept_liquidity, concept_machine_learning_finance, concept_moving_averages, concept_multi_timeframe_analysis, concept_oscillators_momentum, concept_pivot_points, concept_probabilistic_thinking, concept_probability_fat_tails, concept_time_series_statistics, concept_trendlines, concept_volatility, paper_mclean_pontiff_2016, principle_03_future_is_uncertain]
status: researched
---

# Reading List — precise entries, short-term systems and small accounts

> **Education, not financial advice.** This is a list of things to read and
> test, not a list of edges. Bibliographic facts (publisher, year, chapter
> titles) are cited to the page where they were read on **2026-10-20**; source
> keys like [R4] point to the list at the end. A description of *what a book
> teaches* is Claude's paraphrase (**T5**) unless a source key follows it.
> No win rate or P&L figure here is a fact. Performance figures from authors,
> vendors or replications are labelled **T4** ([[framework_source_tiers]]).
> The machine-readable list of the new books is `10_sniper-lab/books-sniper.yaml`.

## 1. Why this list, and why it starts with validation

The sniper lab has already answered three questions, and they decide what is
worth reading next:

- **Almost nothing survives, and what does is not yet trusted.** Of 128 codified
  configurations, none on crypto is positive after costs out of sample. One on
  forex and gold (VWAP reversion 1h, raw-spread account) passes Gate 4, but its
  deflated-Sharpe probability is only 0.35 once the number of trials is counted
  ([[synthesis_sniper_backtests]]). So its record is provisional until forward
  trades confirm it.
- **Costs decide at short horizons.** On a regular-fee venue, 5-minute sniper
  entries are untradeable at any account size ([[synthesis_sniper_entries]]).
- **At $20 the realistic rhythm is one to three trades a day on 1-hour or
  4-hour structure**, with maker entries and every fee journaled in R
  ([[synthesis_small_account_venues]]).

So the bot does not need more entry ideas first. It needs (1) better ways to
tell a real edge from a lucky backtest, (2) stop and sizing methods that work
at a $20 minimum-order scale, and only then (3) entry logic precise enough to
code, with the conditions under which it is supposed to work. The list is
ordered that way in §9.

The philosophy ([[philosophy_relationship]]) frames all of it. An entry idea is *understanding*; it is not
yet *evidence* or *mathematics* (Section VIII). [[principle_05_mathematical_justification]]
asks for expected value after costs. [[principle_04_conditional_probability]]
asks under which regime, session and market a probability was measured
([[philo_conditional_probability]]).
[[principle_06_do_not_force]] is the selectivity that Volman and Brooks teach
bar by bar. [[principle_09_protect_capital]] governs the sizing books, and
[[principle_11_record_and_investigate]] is what Bellafiore's playbook and
Sweeney's adverse-excursion records put into practice
([[philo_mathematics_sword]], [[philo_scientific_method]]).

On the owner's wish to stop *waiting for 60%*: several of these books make
the same point the lab does. A low hit rate is fine if the payoff and costs
work. Brooks writes it as a trader's equation (§3, Trading Ranges). The
break-even line after costs is in [[formula_sheet]] and in
[[synthesis_sniper_entries]] (a 2R bracket at 0.13R cost breaks even at 37.7%).

## 2. The list at a glance

19 new books, 1 non-book course and 4 research papers (5 papers counting the
companion study). The books already in the KB that belong beside them are in §8.

| # | Title | Author | Year | Type | In KB? | Main concepts | Bot priority |
|---|---|---|---|---|---|---|---|
| 1 | *The Evaluation and Optimization of Trading Strategies* (2nd ed.) | Robert Pardo | 2008 | book | no | backtesting, overfitting | **first** |
| 2 | *Testing and Tuning Market Trading Systems* | Timothy Masters | 2018 | book | no | overfitting, permutation tests | **first** |
| 3 | *Entry and Exit Confessions of a Champion Trader* | Kevin J. Davey | 2019 | book | no | entry isolation tests | **first** |
| 4 | *Maximum Adverse Excursion* | John Sweeney | 1997 | book | no | stop placement from data | **first** |
| 5 | *Leveraged Trading* | Robert Carver | 2019 | book | no | leverage, small-account sizing, costs | **first** |
| 6 | *The Trading Game* | Ryan Jones | 1999 | book | no | fixed-ratio sizing | second |
| 7 | *Trading Price Action Trends* | Al Brooks | 2011 | book | no | price action, pullbacks | second |
| 8 | *Trading Price Action Trading Ranges* | Al Brooks | 2012 | book | no | failed breakouts, trader's equation | second |
| 9 | *Trading Price Action Reversals* | Al Brooks | 2012 | book | no | reversals, sweeps | second |
| 10 | *Understanding Price Action* | Bob Volman | 2014 | book | no | 5m price action, selectivity | second |
| 11 | *Forex Price Action Scalping* | Bob Volman | 2011 | book | no | scalping, break setups | third |
| 12 | *YTC Price Action Trader* | Lance Beggs | c.2012 | e-book course | no | multi-timeframe process | third |
| 13 | *The Logical Trader* | Mark B. Fisher | 2002 | book | no | opening range (ACD), pivots | second |
| 14 | *Short Term Trading Strategies That Work* | Larry Connors & Cesar Alvarez | 2008 | book | no | short-term mean reversion | second |
| 15 | *Machine Trading* | Ernest P. Chan | 2017 | book | no | intraday microstructure, bitcoin | second |
| 16 | *How to Day Trade for a Living* | Andrew Aziz | 2016 | book | no | stocks in play, ORB, VWAP | third |
| 17 | *The PlayBook* | Mike Bellafiore | 2013 | book | no | setup documentation, review | third |
| 18 | *Trading by the Minute* | Joe Ross | 1997 | book | no | intraday signals, stop rules | third |
| 19 | *Volume Profile: The Insider's Guide to Trading* | Trader Dale | 2018 | book | no | volume profile levels | third |
| 20 | 2022 ICT Mentorship (YouTube) | Michael J. Huddleston | 2022 | **non-book** video course | concept note only | sweeps, FVG, OTE, sessions | read as source, not evidence |
| 21 | Intraday Patterns in the Cross-Section of Stock Returns | Heston, Korajczyk, Sadka | 2010 | paper | no | time-of-day effects | second |
| 22 | Market Intraday Momentum | Gao, Han, Li, Zhou | 2018 | paper | cited in [[synthesis_sniper_entries]] | intraday momentum | second |
| 23 | A Profitable Day Trading Strategy for the U.S. Equity Market | Zarattini, Barbon, Aziz | 2024 | paper | cited in [[synthesis_sniper_entries]] | ORB, stocks in play | second |
| 24 | Day Trading for a Living? (+ Barber, Lee, Liu, Odean 2014) | Chague, De-Losso, Giovannetti | 2019 | paper | no | base rates for day traders | **first** |

## 3. Price action and precise entries

**Al Brooks, the price-action trilogy (Wiley, 2011–2012)** — `book_trading_price_action_trends`,
`book_trading_price_action_trading_ranges`, `book_trading_price_action_reversals`. New to the KB;
only his earlier [[book_reading_price_charts_bar_by_bar]] is in it ([[person_al_brooks]]).

- *What it is.* Brooks split his method into three books: trends, trading ranges
  and reversals. The publisher says he trades only 5-minute charts [R1]. The
  *Trading Ranges* volume also covers breakouts, order management and the
  mathematics of trading [R2]; *Reversals* is about spotting and trading trend
  reversals [R2].
- *Why it matters for the bot.* Brooks is the most detailed source on the
  difference between *the same pattern in two regimes*. A breakout in a trend
  and a breakout from a range are different trades with different odds (T5).
  That is exactly the regime conditioning the lab already applies
  ([[concept_market_regimes]], [[principle_04_conditional_probability]]).
  His bar counting (the second pullback attempt in a trend) and his rule that
  a reversal usually needs a trendline break and then a failed test of the
  extreme are precise enough to code on OHLCV (T5). The trader's equation
  (chance of winning × reward must exceed chance of losing × risk) is the
  same gate as [[concept_expectancy]].
- *KB concepts.* [[concept_price_action]], [[concept_trend_following]],
  [[concept_market_structure]], [[concept_breakout_trading]],
  [[concept_mean_reversion]], [[concept_liquidity_sweep_reversal]],
  [[concept_trendlines]], [[concept_risk_reward_r_multiples]].
- *Links.* The failed-breakout logic is the same mechanism as spec S1
  (sweep and reclaim) and S5 (break and retest) in [[synthesis_sniper_entries]],
  and as the playbooks [[strategy_vincent_desiano_break_retest]] and
  [[strategy_gala_trades_price_action]].
- *Caveat.* Practitioners describe the writing as dense; forum readers often
  suggest Volman first [R6][R7]. Brooks's numbers on how often things fail are
  his own estimates, not measured tests (T5).

**Bob Volman, *Understanding Price Action* (Light Tower Publishing, 2014)** — `book_understanding_price_action`, new.

- *What it is.* Six straight months of real EUR/USD 5-minute charts, with
  hundreds of annotated examples, aimed at trading from the bare chart [R3][R4].
- *Why it matters for the bot.* It is a training set for *when not to trade*.
  Volman judges whether a build-up has real pressure behind it and skips most
  setups that look similar but lack it (T5). For a bot, that is a filter, the
  piece the lab's specs are weakest on. It also gives labelled examples a
  developer can turn into test cases.
- *KB concepts.* [[concept_price_action]], [[concept_scalping]],
  [[concept_support_resistance]], [[concept_breakout_trading]],
  [[concept_market_structure]], [[concept_trade_management]].
- *Caveat.* A study of one pair on one timeframe; its transfer to crypto is a
  hypothesis.

**Bob Volman, *Forex Price Action Scalping* (Light Tower Publishing, 2011)** — `book_forex_price_action_scalping`, new.

- *What it is.* A scalping method built on a 70-tick EUR/USD chart; reviewers
  note a 30-second chart can approximate it in the liquid London and New York
  hours [R5]. Readers single it out as a strong pick for scalping [R6].
- *Why it matters for the bot.* Volman names a small set of break setups (a
  build-up of small bars near a short moving average, then a break) with a fixed
  small target and stop (T5; check the exact set and bracket in the book).
  These are among the most codeable discretionary setups in print.
- *The $20 problem.* A fixed small bracket on a tick chart is where cost in R
  explodes. [[synthesis_small_account_venues]] found 1-minute scalps not viable
  on any venue checked. Read it for the entry logic and test it only at the
  low-fee tier, or on 15-minute bars and above.
- *KB concepts.* [[concept_scalping]], [[concept_price_action]],
  [[concept_breakout_trading]], [[concept_moving_averages]],
  [[concept_trade_execution]].

**Lance Beggs, *YTC Price Action Trader* (self-published e-book course, six volumes)** — `book_ytc_price_action_trader`, new.

- *What it is.* Six PDF volumes, about 590 pages, sold by Your Trading Coach;
  a reseller describes it as aimed at experienced intraday traders (T4,
  seller page) [R8]. Forum users praise its checklists and trading-plan
  template and find it easier to read than Brooks [R7]. The original release
  year is not confirmed; the earliest dated mention found is a 2012 forum
  post [R7].
- *Why it matters for the bot.* Its structure suits code. The higher timeframe
  decides *where* to look, and the lower timeframe's swing strength decides
  *when* to enter. Setups are named by what price does at a level: test,
  breakout failure, breakout pullback, pullback (T5). That maps directly onto
  [[concept_multi_timeframe_analysis]] and the lab's level-then-trigger design.
- *KB concepts.* [[concept_price_action]], [[concept_multi_timeframe_analysis]],
  [[concept_support_resistance]], [[concept_trading_plan]],
  [[concept_trading_journal_review]].

**Joe Ross, *Trading by the Minute* (Ross Trading International, 1997)** — `book_trading_by_the_minute`, new.

- *What it is.* Ross sets out major, minor and intermediate intraday signals and
  explains both the initial stop and the stop that protects profit [R9].
- *Why it matters for the bot.* Ross is one of the older sources for explicit
  rules on stop placement and trailing in intraday trading. His wider method
  (the 1-2-3 formation and the Ross hook) is a structure-break entry that
  resembles the market-structure-shift trigger in spec S3 (T5).
- *Caveat.* Old, futures-pit era, thinly documented online. Whether this
  particular book centres on the hook is unconfirmed [R9]. Third priority.
- *KB concepts.* [[concept_price_action]], [[concept_market_structure]],
  [[concept_trade_management]].

## 4. Intraday playbooks

**Mark B. Fisher, *The Logical Trader* (Wiley, 2002)** — `book_logical_trader`, new.

- *What it is.* The ACD method. Price points are plotted relative to the
  opening range; the A and C levels are entry references and the B and D
  levels are stops. Pivot ranges are combined with it to size positions and
  limit risk [R10].
- *Why it matters for the bot.* It is a fully rule-based opening-range method
  with an *offset* (do not enter at the range edge; enter once price has
  cleared it by a set amount). That is a cheap, testable variant of spec S4
  (`sniper_orb_retest`), and it sits in the same lineage as
  [[book_crabel_opening_range]] ([[person_toby_crabel]]). Crypto has no opening
  bell, so the test needs a defined session open (00:00 UTC, London, or New
  York) ([[concept_trading_sessions_killzones]]).
- *KB concepts.* [[concept_breakout_trading]], [[concept_pivot_points]],
  [[concept_trading_sessions_killzones]], [[concept_position_sizing]].
- *Caveat.* Third-party ACD scripts disagree on offsets; take parameters from
  the book itself [R10].

**Andrew Aziz, *How to Day Trade for a Living* (self-published, 2016)** — `book_how_to_day_trade_for_a_living`, new.

- *What it is.* A popular beginner's book on US-stock day trading: risk rules,
  stock selection and core price-action strategies, per a practitioner
  review [R11]. The setup list includes opening-range breakouts, VWAP and
  moving-average trades (T5).
- *Why it matters for the bot.* Its central filter, trading only the few names
  with unusual activity that day, was later tested by Aziz himself with
  Zarattini and Barbon (§7, [R20]). Book and paper together show an idea moving
  from playbook to test. For crypto, the analogue is ranking coins by
  relative volume in the first bars of a session ([[concept_vwap]]).
- *KB concepts.* [[concept_vwap]], [[concept_breakout_trading]],
  [[concept_position_sizing]], [[concept_risk_reward_r_multiples]].
- *Caveat.* The author runs a trading-education community; the book is T2 for
  method, and any performance claim around it is T4.

**Mike Bellafiore, *The PlayBook* (FT Press, 2013)** — `book_the_playbook`, new.

- *What it is.* New traders at SMB Capital walk through real trades and get
  critiqued. Plays include support plays, flags, opening drives, intraday
  levels, bounce and fade trades, pullbacks and scalps [R12]. At SMB, traders
  record one play at the end of each session and review it [R13].
- *Why it matters for the bot.* It is the prop-desk version of what this KB
  already does with Chart Fanatics playbooks. Each play has a context, levels,
  an entry, an exit and a size. That is the schema a bot needs for every
  setup, plus a review loop ([[framework_trading_journal]],
  [[principle_11_record_and_investigate]]).
- *KB concepts.* [[concept_trading_plan]], [[concept_trading_journal_review]],
  [[concept_trade_execution]], [[concept_trade_management]].
- *Caveat.* The SMB blog review is a promotional reprint [R13]; the year varies
  between 2013 (catalogues) and 2014 (copyright page) [R12].

**Trader Dale, *Volume Profile: The Insider's Guide to Trading* (independently published, 2018)** — `book_volume_profile_insiders_guide`, new.

- *What it is.* A short practitioner book (about 196 pages, per a marketplace
  listing) on trading from volume-at-price zones [R14].
- *Why it matters for the bot.* Volume profile is one of the few order-flow
  tools a crypto bot *can* compute: Binance publishes trade-level history, so
  point of control, value area and low-volume nodes can be built without a paid
  feed. It turns [[strategy_carmine_rosato_lvn]] and
  [[strategy_forrest_knight_volume_profile]] into level definitions to test,
  and gives the levels that [[strategy_fabio_valentini_amt_order_flow]] trades from.
  Spec S12 (LVN absorption) still needs true bid/ask data and is not codeable
  on OHLCV ([[synthesis_sniper_entries]]).
- *KB concepts.* [[concept_volume_profile]], [[concept_auction_market_theory]],
  [[concept_order_flow]], [[concept_liquidity]].
- *Caveat.* Self-published and verified here only through a listing (T3).
  For the theory, read [[book_mind_over_markets]] and [[book_markets_in_profile]]
  first; this book adds level-placement habits, not evidence.

## 5. Systematic short-term trading and entry/exit research

**Larry Connors & Cesar Alvarez, *Short Term Trading Strategies That Work* (TradingMarkets, 2008)** — `book_short_term_trading_strategies_that_work`, new.

- *What it is.* The book behind the 2-period RSI pullback: buy sharp
  short-term weakness only while price is above its 200-day average, and exit
  on the first rebound [R15][R16]. The seller blurb mentions 16 strategies;
  its backtest claims are T4 [R15].
- *Why it matters for the bot.* It is the cleanest published family of
  high-hit-rate, short-holding mean-reversion rules, the opposite profile to
  the lab's 2R sniper brackets. It suits the owner's wish to trade often. It
  also brings the risk of that profile: many small wins and occasional large
  losses ([[concept_probability_fat_tails]]). The book argues stops hurt this
  style, which the lab should test, not accept ([[person_larry_connors]];
  same author as [[book_street_smarts]]).
- *Test.* RSI(2) extremes with a 200-period trend filter on 1-hour crypto
  bars, net of maker/taker costs, out of sample.
- *KB concepts.* [[concept_mean_reversion]], [[concept_oscillators_momentum]],
  [[concept_moving_averages]], [[concept_market_regimes]],
  [[strategy_lance_breitstein_mean_reversion]].
- *Caveat.* Built on daily US equities before 2008; the edge may have decayed
  after publication (see [[paper_mclean_pontiff_2016]]).

**Kevin J. Davey, *Entry and Exit Confessions of a Champion Trader* (independently published, 2019)** — `book_entry_exit_confessions`, new.

- *What it is.* 41 entry ideas and 11 exit ideas, each in plain English and
  TradeStation code [R17][R18]. A summary notes they are components, not
  complete strategies [R18].
- *Why it matters for the bot.* The method matters more than the catalogue.
  Test an entry on its own, with a neutral exit (for example a fixed number of
  bars), before adding stops and targets (T5). If the entry has no edge alone,
  no exit will rescue it honestly. The lab's specs mix entry, stop and target
  in one result; this book shows how to separate them. Pair it with Davey's
  [[book_building_winning_algo_systems]], already in the KB.
- *KB concepts.* [[concept_backtesting]], [[concept_trade_execution]],
  [[concept_trade_management]], [[concept_overfitting_validation]].

**Ernest P. Chan, *Machine Trading* (Wiley, 2017)** — `book_machine_trading`, new ([[person_ernest_chan]]).

- *What it is.* A practitioner's guide to algorithmic trading with MATLAB
  code. Chapter 6 is *Intraday Trading and Market Microstructure* and
  chapter 7 is *Bitcoins* [R19].
- *Why it matters for the bot.* The KB has Chan's two earlier books
  ([[book_quantitative_trading_chan]], [[book_algorithmic_trading_chan]]).
  This one adds the two chapters a crypto intraday bot needs most: what the
  order book and order flow can and cannot tell you at short horizons, and how
  bitcoin differs.
- *KB concepts.* [[concept_market_microstructure]], [[concept_order_flow]],
  [[concept_time_series_statistics]], [[concept_machine_learning_finance]].

## 6. Validation, stops and sizing (read these first)

**Robert Pardo, *The Evaluation and Optimization of Trading Strategies* (Wiley, 2nd ed., 2008)** — `book_evaluation_optimization_trading_strategies`, new.

- *What it is.* The standard practitioner text on walk-forward analysis, with
  chapters on walk-forward analysis, performance evaluation and the many faces
  of overfitting [R21]. It revises Pardo's 1992 book [R22].
- *Why it matters for the bot.* The lab uses one split (choose before 2024,
  judge after). Walk-forward rolls that split forward many times. It shows
  whether a configuration works only in one period, and gives a
  walk-forward efficiency to set beside the deflated Sharpe
  ([[paper_deflated_sharpe_2014]], [[paper_bailey_pbo_2017]]). The same
  logic runs through [[synthesis_evidence_lab]]'s overfitting tests.
- *KB concepts.* [[concept_backtesting]], [[concept_overfitting_validation]],
  [[concept_performance_metrics]].

**Timothy Masters, *Testing and Tuning Market Trading Systems* (Apress, 2018)** — `book_testing_tuning_trading_systems`, new.

- *What it is.* Statistical tests for trading systems with C++ code; chapter 7
  is on permutation tests [R23]. The publisher's pitch: "Seemingly good
  backtest performance isn't enough to justify trading real money." [R24]
- *Why it matters for the bot.* A Monte Carlo permutation test asks how often
  the same rule, run on shuffled versions of the price history, does as well
  as it did on the real one. That is the most direct check on whether a sniper
  spec found structure or noise. It complements [[paper_white_2000]] and the
  lab's deflated Sharpe ([[philo_scientific_method]]).
- *KB concepts.* [[concept_overfitting_validation]], [[concept_backtesting]],
  [[concept_time_series_statistics]], [[concept_probabilistic_thinking]].

**John Sweeney, *Maximum Adverse Excursion* (Wiley, 1997)** — `book_maximum_adverse_excursion`, new.

- *What it is.* The first full guide to MAE, a way to estimate a trade's loss
  point before entering by studying how far past trades moved against you
  [R25].
- *Why it matters for the bot.* A sniper entry lives or dies on its stop. At
  $20 the stop also sets whether the position clears the venue minimum
  ([[synthesis_small_account_venues]] §7.4). The lab already writes every trade
  to `10_sniper-lab/backtests/trades.csv.gz`. An MAE and MFE (maximum
  favourable excursion) histogram per spec is the next measurement, and it
  replaces guessed stops with measured ones.
- *KB concepts.* [[concept_trade_management]], [[concept_risk_reward_r_multiples]],
  [[concept_backtesting]].

**Robert Carver, *Leveraged Trading* (Harriman House, 2019)** — `book_leveraged_trading`, new ([[person_robert_carver]]).

- *What it is.* With leverage, losses and costs are magnified. The book's
  answer is a simple starter system on one instrument with one opening rule,
  sized for the right leverage and traded at a suitable frequency, expanded
  later and optionally combined with judgement (semi-automatic trading) [R26].
  The blurb's claim that a few hundred dollars or pounds is enough is publisher
  marketing (T4) [R26].
- *Why it matters for the bot.* This is the closest book to the $20 problem:
  costs set how often you may trade, and volatility sets size. It extends
  [[book_systematic_trading]] to the retail, leveraged, small-account case.
  Read it with [[concept_leverage_margin]] and §8 of
  [[synthesis_small_account_venues]].
- *KB concepts.* [[concept_leverage_margin]], [[concept_position_sizing]],
  [[concept_volatility]], [[concept_risk_of_ruin_drawdown]],
  [[concept_trade_execution]].

**Ryan Jones, *The Trading Game* (Wiley, 1999)** — `book_the_trading_game`, new.

- *What it is.* The source of fixed-ratio sizing. Size goes up one unit only
  after a set profit (the delta) per unit already traded. With a $3,000 delta,
  going from one to two contracts takes $3,000 of profit and from two to three
  another $6,000 [R27]. It was presented as an alternative to fixed-fractional
  sizing for small, unit-based accounts [R28].
- *Why it matters for the bot.* At $20 the minimum order is the binding
  constraint, so fixed-fractional risk often rounds to *one minimum unit or
  nothing*. Fixed ratio is one honest way to plan the step from one unit to two.
  Compare it against [[book_definitive_guide_position_sizing]] and
  [[concept_kelly_criterion_optimal_f]] ([[principle_09_protect_capital]]).
- *Caveat.* A forum user could not reproduce one online table of the formula;
  check the book [R28].

## 7. Non-book course and the research evidence

**ICT 2022 Mentorship (Michael J. Huddleston, Inner Circle Trader YouTube channel)** — non-book, free video course ([[person_michael_huddleston]]).

- *What it is.* A 41-video playlist titled *2022 ICT Mentorship* on the Inner
  Circle Trader channel (read 2026-10-20) [R29]; a summary site dates the
  episodes January to June 2022 [R30]. The KB already describes it in
  [[concept_smart_money_concepts]].
- *Why it matters for the bot.* It is the primary source for the sweep, fair
  value gap, OTE and session models behind specs S1, S2, S3 and S8
  ([[concept_liquidity_sweep_reversal]], [[concept_fair_value_gap]],
  [[concept_premium_discount_ote]], [[concept_trading_sessions_killzones]];
  [[strategy_abraham_perez_ict_orderflow]], [[strategy_nbb_trader_po3_ote_adr]]).
  Read it to get the rules exactly as taught, so the specs test what was
  actually said.
- *What it is not.* Evidence. [[synthesis_sniper_entries]] found no published
  controlled test supporting the ICT tools themselves, and in the lab FVG and
  OTE retraces were negative after costs out of sample. Treat it as T2 for
  method and T4 for any performance claim.

**Heston, Korajczyk & Sadka (2010), *Intraday Patterns in the Cross-Section of Stock Returns*, Journal of Finance 65(4)** [R31] — paper, not in KB.

- *Finding (T1).* Returns continue at half-hour intervals that are exact
  multiples of a trading day, for at least 40 days. Short-term reversal comes
  from liquidity imbalances lasting under an hour and from bid-ask bounce.
  Timing trades can save about the effective spread in execution costs.
- *For the bot.* Two tests. First, does crypto show the same *same time
  tomorrow* continuation on a 24-hour lag? Second, sub-hour reversal is partly
  bid-ask bounce, which a taker cannot capture after paying the spread
  ([[concept_market_microstructure]], [[mathbook_hasbrouck_empirical_microstructure]]).

**Gao, Han, Li & Zhou (2018), *Market Intraday Momentum*, Journal of Financial Economics 129(2)** [R32] — paper, cited in [[synthesis_sniper_entries]].

- *Finding (T1).* On SPY 1993–2013, the first half-hour return (measured from
  the previous close) predicts the last half-hour return. It is stronger on
  volatile, high-volume, recession and major-news days, and appears in ten
  other active ETFs.
- *For the bot.* The best-documented intraday timing effect; the crypto
  version (Shen, Urquhart and Wang) is already in the sniper evidence table.
  It is a candidate *context filter* (trade with the first-hour direction late
  in the session) rather than a sniper entry.

**Zarattini, Barbon & Aziz (2024), *A Profitable Day Trading Strategy for the U.S. Equity Market*, Swiss Finance Institute RP 24-98** [R20] — paper, cited in [[synthesis_sniper_entries]].

- *Finding.* A 5-minute opening-range breakout on more than 7,000 US stocks,
  2016–2023, works much better when limited to stocks with unusual activity
  that day; the paper also compares 15-, 30- and 60-minute ranges [R20].
- *Status.* The headline returns are the authors' backtest and are **T4**
  here, as in [[synthesis_sniper_entries]]. A QuantConnect replication
  reports a positive result (T4) [R33]; an MQL5 replication on indices reports
  net results near zero (T4, via [[synthesis_sniper_entries]]). The lab's own ORB retest on crypto was negative
  after costs out of sample ([[synthesis_sniper_backtests]]). The useful idea
  is the *relative-volume filter*, not the return figure.

**Chague, De-Losso & Giovannetti (2019/2020), *Day Trading for a Living?*** [R34][R35], with **Barber, Lee, Liu & Odean (2014), *The Cross-Section of Speculator Skill*, Journal of Financial Markets 18** [R34][R36] — papers, not in KB.

- *Finding (T1, regulator and exchange data).* Among Brazilians who began day
  trading mini-index futures in 2013–2015 and kept going for at least 300
  days, 97% lost money, only 0.4% earned more than a bank teller, and there was
  no evidence of learning [R35]. The authors conclude it is "virtually
  impossible for an individual to day trade for a living" [R34]. In Taiwan,
  Barber and co-authors found over 80% of day traders lost money after costs
  (2004 study), and fewer than 1% earned predictable profits after fees (2014
  paper) [R36][R37].
- *For the bot.* This is the base rate the sniper lab should assume until its
  own out-of-sample record says otherwise ([[principle_03_future_is_uncertain]],
  [[paper_barber_odean_2000]]). It is also why the lab's gate refuses every
  live signal today. That refusal is the system working, not failing
  ([[philo_capital_preservation]]).

## 8. Already in the KB: read these alongside

These are already in `05_books-top-100/books.yaml`, `06_mathematics-foundations/`
or the KB's paper ids. They are not repeated in `books-sniper.yaml`.

| In-KB id | Why for a sniper bot | Pairs with |
|---|---|---|
| [[book_reading_price_charts_bar_by_bar]] | Brooks's first statement of bar-by-bar reading | Brooks trilogy |
| [[book_crabel_opening_range]] | The original opening-range and narrow-range work behind spec S4 | Fisher, Zarattini et al. |
| [[book_street_smarts]] | Raschke & Connors's short-term patterns, including the Turtle Soup false-breakout entry behind spec S1 ([[person_linda_raschke]]) | Connors & Alvarez |
| [[book_trading_sardines]] | Raschke's short-term trading lessons | Street Smarts |
| [[book_long_term_secrets_short_term_trading]] | Larry Williams's volatility breakouts and short-term patterns | Fisher |
| [[book_mastering_the_trade]] | Carter's intraday setups and session habits | Aziz |
| [[book_ta_multiple_timeframes]] | Shannon on VWAP and moving averages across timeframes | Beggs |
| [[book_art_science_technical_analysis]] | Grimes's pullbacks and failure tests, with tested pattern statistics | Brooks |
| [[book_building_winning_algo_systems]] | Davey's full development and monitoring process | Entry and Exit Confessions |
| [[book_quantitative_trading_chan]], [[book_algorithmic_trading_chan]] | Chan's backtesting and mean-reversion foundations | Machine Trading |
| [[book_systematic_trading]] | Carver's framework for simple, cost-aware rules | Leveraged Trading |
| [[book_trading_systems_and_methods]] | Kaufman's encyclopedia of system types, including the efficiency ratio for regime filters ([[person_perry_kaufman]]) | Pardo |
| [[book_evidence_based_ta]] | Aronson on data-mining bias in rule testing | Masters |
| [[book_advances_financial_ml]] | Labelling with stop, target and time barriers, and meta-labelling to filter a rule's signals | Masters, Davey |
| [[book_definitive_guide_position_sizing]], [[book_mathematics_of_money_management]] | Position sizing and optimal f | The Trading Game |
| [[book_mind_over_markets]], [[book_markets_in_profile]], [[book_trades_about_to_happen]] | Auction market theory, profile and Wyckoff volume reading | Trader Dale |
| [[book_trading_and_exchanges]], [[book_market_microstructure_in_practice]] | How orders, spreads and fills work | Machine Trading ch. 6 |
| [[book_day_swing_trading_currency]] | FX sessions and intraday FX setups | Volman |
| [[mathbook_bouchaud_trades_quotes_prices]], [[mathbook_cartea_algorithmic_hft]] | Order-book dynamics and short-horizon market making, rigorously | Machine Trading |
| [[paper_deflated_sharpe_2014]], [[paper_bailey_pbo_2017]], [[paper_white_2000]] | Multiple-testing corrections the lab already uses | Pardo, Masters |

## 9. Suggested reading order for building the bot (suggestion)

1. **Base rates and validation:** Chague et al. and Barber et al. (§7), then
   Pardo, then Masters. Goal: walk-forward plus a permutation test on the
   lab's best configuration.
2. **Stops and sizing at $20:** Sweeney (MAE from the lab's trade file),
   Carver's *Leveraged Trading*, then Jones. Goal: measured stops and a sizing
   rule that respects the minimum order.
3. **Entry isolation:** Davey's *Entry and Exit Confessions*. Goal: re-run
   each spec with a neutral exit to see whether the entry carries any edge.
4. **Entry logic with its conditions:** Brooks (*Trading Ranges* first, for
   the trader's equation and failed breakouts), then Volman's *Understanding
   Price Action*. Goal: regime-conditioned variants of S1 and S5.
5. **Opening-range family:** Fisher, with [[book_crabel_opening_range]], Gao et
   al. and Zarattini et al. Goal: an ACD-offset variant of S4 with a
   relative-volume filter.
6. **Mean-reversion family:** Connors & Alvarez. Goal: RSI(2) with a trend
   filter on 1-hour crypto, net of costs.
7. **Microstructure for crypto:** Chan's *Machine Trading* chapters 6–7, then
   Trader Dale for volume-profile levels built from trade data.
8. **Source rules, not evidence:** the ICT 2022 mentorship, to check the specs
   match what is taught.

Each goal is a hypothesis for `00_philosophy/research-program.md`, to be judged
by [[framework_decision_protocol]] Gate 4 like every other spec.

## 10. What this list does not settle

- **No book here proves an edge after costs.** The evidence in §7 says the
  base rate for individual day traders is poor, and the lab's own record
  agrees so far.
- **Discretionary books lose context when coded.** Brooks, Volman and Beggs
  rely on judgement the bot does not have. Coding them is a test of a
  simplified version, and a negative result says nothing about the full
  discretionary skill.
- **Transfer is untested.** Most of these books come from US stocks, index
  futures or EUR/USD. Crypto runs 24 hours, has different costs and has no
  single open.
- **Self-published titles** (Beggs, Aziz, Davey's *Confessions*, Trader Dale)
  are T2 for method. Several were verified here only through listings or
  search summaries (marked in Sources).

## Sources

All read on 2026-10-20. *Opened* means the page itself was retrieved; *search
summary* means only a search result describing the page was read.

- [R1] Al Brooks, *Trading Price Action Trends*, Wiley 2011, publisher blurb via bookseller listing: https://tenlong.com.tw/products/9781118066515 (search summary). T1 for what the publisher says.
- [R2] O'Reilly listings for *Trading Price Action Trading Ranges* and *Reversals* (January 2012): https://www.oreilly.com/library/view/-/9781118172339/ and https://oreilly.com/library/view/trading-price-action/9781118172308 (search summary). T1.
- [R3] Bob Volman, *Understanding Price Action*, Light Tower Publishing 2014: https://www.abebooks.com/Understanding-Price-Action-Practical-Analysis-5-Minute/30325842905/bd (opened). T3 listing.
- [R4] Description of *Understanding Price Action* (six months of EUR/USD 5-minute charts): https://www.eltraderfinanciado.com/he/trading-books/understanding-price-action (search summary). T3.
- [R5] *Forex Price Action Scalping* (Light Tower Publishing, 11 October 2011; 70-tick chart, 30-second approximation): https://www.goodreads.com/book/show/13269524-forex-price-action-scalping and https://betterread.com.au/book/forex-price-action-scalping.do (search summary). T3.
- [R6] Practitioner forum, Volman versus Brooks reading order: https://forums.babypips.com/t/new-trader-studying-al-brook-price-action-books/82779 (search summary). T3.
- [R7] NexusFi threads on YTC and Brooks: https://nexusfi.com/showthread.php?p=233556 and https://nexusfi.com/showthread.php?p=908909 (search summary). T3.
- [R8] YTC Price Action Trader reseller page (six volumes, ~590 pages): https://globaltradingtools.com/?p=17029 (search summary). T4.
- [R9] Joe Ross, *Trading by the Minute*, 1997: https://abebooks.com/9789768108258/Trading-Minute-Ross-Joe-9768108258/plp (opened). T3.
- [R10] Mark Fisher, *The Logical Trader* (Wiley 2002) and the ACD method: https://nexusfi.com/a/strategies/acd-trading-method, https://biblio.es/9780471215516, https://www.luxalgo.com/library/concept/acd-method.md (search summary). T3.
- [R11] TraderLion review of *How to Day Trade for a Living*: https://traderlion.com/trading-books/how-to-day-trade-for-a-living/ (search summary). T3.
- [R12] *The PlayBook*, FT Press; library record and Pearson sample pages: https://discover.aclib.us/oreilly/ocn862826961 and https://ptgmedia.pearsoncmg.com/images/9780132937641/samplepages/0132937646.pdf (search summary). T1/T3.
- [R13] SMB Capital blog, review of *The PlayBook*: https://www.smbtraining.com/blog/ls-trades-reviews-the-playbook (search summary). T4 (promotional reprint).
- [R14] Trader Dale, *Volume Profile: The Insider's Guide to Trading*, 2018 listing: https://ebay.it/itm/363344849625 (search summary). T3.
- [R15] Connors & Alvarez, *Short Term Trading Strategies That Work*, TradingMarkets 2008: https://www.abebooks.com/Short-Term-Trading-Strategies-Work-Larry/31620720826/bd (opened). T3.
- [R16] RSI-2 rules as summarised: https://www.luxalgo.com/library/concept/rsi-2.md (search summary). T3.
- [R17] Davey, *Entry and Exit Confessions* editions (independently published, April 2019): https://www.goodreads.com/work/editions/70058912-entry-and-exit-confessions-of-a-champion-trader-52-ways-a-professional (search summary). T3.
- [R18] Summary of *Entry and Exit Confessions* (41 entries, 11 exits; components, not strategies): https://sobrief-staging.onrender.com/books/entry-and-exit-confessions-of-a-champion-trader and https://ebook.cam-ed.com/ebooks/entry-and-exit-confessions-of-a-champion-trader-52-ways-a-professional-speculator-gets-in-and-out-of-the-stock-futures-and-forex-markets (search summary). T3.
- [R19] Wiley-VCH, *Machine Trading* (2017), description and contents: https://www.wiley-vch.de/en/areas-interest/finance-economics-law/machine-trading-978-1-119-21960-6 (opened). T1.
- [R20] Zarattini, Barbon, Aziz, SFI Research Paper 24-98, abstract: https://ideas.repec.org/p/chf/rpseri/rp2498.html (opened). T1 for the method; performance figures T4.
- [R21] Wiley-VCH, Pardo, *The Evaluation and Optimization of Trading Strategies* (2nd ed.), description and contents: https://www.wiley-vch.de/en/areas-interest/finance-economics-law/the-evaluation-and-optimization-of-trading-strategies-978-0-470-12801-5 (opened). T1.
- [R22] Walk forward optimization: https://en.wikipedia.org/wiki/Walk_forward_optimization (search summary). T3.
- [R23] Masters, *Testing and Tuning Market Trading Systems*, catalogue with table of contents: https://ersearch2.cvtisr.sk/vufind/Record/240563/TOC (search summary). T1.
- [R24] Masters, publisher description (Apress 2018): https://www.abebooks.com/Testing-Tuning-Market-Trading-Systems-Timothy/32234804369/bd (opened). T1 for the publisher's text.
- [R25] Wiley-VCH, Sweeney, *Maximum Adverse Excursion* (January 1997, 176 pages): https://www.wiley-vch.de/en/areas-interest/finance-economics-law/maximum-adverse-excursion-978-0-471-14152-5 (opened). T1.
- [R26] Pan Macmillan, Carver, *Leveraged Trading* (Harriman House, 29 October 2019, 346 pages): https://www.panmacmillan.com/authors/robert-carver/leveraged-trading/9780857197221 (opened). T1 for the publisher's text; the few-hundred-dollars line is T4.
- [R27] Adaptrade, fixed ratio position sizing (Jones, *The Trading Game*, Wiley 1999): https://www.adaptrade.com/MSA/fixratio.htm (opened). T3.
- [R28] Fixed ratio summaries and a forum reproduction problem: https://www.luxalgo.com/library/concept/fixed-ratio/ and https://www.metalsmine.com/thread/72590-fixed-ratio-position-sizing-need-help (search summary). T3.
- [R29] YouTube playlist *2022 ICT Mentorship*, Inner Circle Trader channel, 41 videos: https://www.youtube.com/playlist?list=PLVgHx4Z63paYiFGQ56PjTF1PGePL3r69s (opened). T2.
- [R30] Episode dates for the 2022 mentorship: https://videohighlight.com/playlist/PLVgHx4Z63paYiFGQ56PjTF1PGePL3r69s (search summary). T3.
- [R31] Heston, Korajczyk, Sadka, abstract, Journal of Finance 65(4) 1369–1407: https://arxiv.org/abs/1005.3535 (opened). T1.
- [R32] Gao, Han, Li, Zhou, Journal of Financial Economics 129(2) 394–414, abstract: https://profiles.wustl.edu/en/publications/market-intraday-momentum/ (opened). T1.
- [R33] QuantConnect replication of the stocks-in-play ORB: https://www.quantconnect.com/research/18444/opening-range-breakout-for-stocks-in-play/ (search summary). T4.
- [R34] Chague, De-Losso, Giovannetti, working paper 2019, abstract and references: https://ideas.repec.org/p/spa/wpaper/2019wpecon47.html (opened). T1.
- [R35] Chague, De-Losso, Giovannetti, FGV version (2020-02), abstract: https://econpapers.repec.org/RePEc:fgv:eesptd:525 (opened). T1.
- [R36] CXO Advisory on Barber, Lee, Liu, Odean (2004 Taiwan study): https://www.cxoadvisory.com/individual-investing/do-day-traders-make-money/ (opened). T3 summary of a T1 paper.
- [R37] Barber, Lee, Liu, Odean (2014), *The Cross-Section of Speculator Skill*, Journal of Financial Markets 18: https://www.escholarship.org/uc/item/7k75v0qx (search summary). T1.


<!-- ===== FILE: trading-intelligence/10_sniper-lab/setups.yaml ===== -->

```yaml
# Generated by `python -m trading_intelligence.sniper lab` - do not edit by hand.
# The codified sniper setups as graph nodes (kind: setup), each linked to the playbooks and concepts
# it was coded from, with its out-of-sample result (net R per trade after costs; best six configs).
setups:
- id: sniper_sweep_reclaim
  type: setup
  title: Prior-day liquidity sweep + reclaim (codified)
  derived_from:
  - strategy_candace_lau_nq_sweep_reversal
  - strategy_marco_trades_liquidity_grab
  - strategy_dhesi_liquidity_inversion
  - concept_liquidity_sweep_reversal
  - concept_liquidity
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:SweepReclaim
  rules: 'Prior-day low (high) swept by at least `min_sweep_atr` x ATR, and the bar closes back inside: stops below an obvious level were run and absorbed. Enter
    at market on the next open, stop beyond the sweep extreme, target `rr` R.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_sweep_reclaim@4h@fx_raw
    oos_trades: 1375
    oos_gross_r: 0.007
    oos_net_r: -0.03
  tested:
  - config: sniper_sweep_reclaim@4h@fx_raw
    oos_trades: 1375
    oos_gross_r: 0.007
    oos_net_r: -0.03
  - config: sniper_sweep_reclaim@1h@fx_raw
    oos_trades: 2762
    oos_gross_r: 0.039
    oos_net_r: -0.032
  - config: sniper_sweep_reclaim@4h@fx_std
    oos_trades: 1381
    oos_gross_r: -0.055
    oos_net_r: -0.07
  - config: sniper_sweep_reclaim@1h@fx_std
    oos_trades: 2822
    oos_gross_r: -0.058
    oos_net_r: -0.088
  - config: sniper_sweep_reclaim@15m@ultra
    oos_trades: 3367
    oos_gross_r: 0.028
    oos_net_r: -0.125
  - config: sniper_sweep_reclaim@5m@ultra
    oos_trades: 8634
    oos_gross_r: 0.028
    oos_net_r: -0.21
- id: sniper_fvg_retrace
  type: setup
  title: Fair value gap retrace in the HTF trend (codified)
  derived_from:
  - strategy_trader_mayne_structure_ote
  - strategy_abraham_perez_ict_orderflow
  - strategy_nbb_trader_po3_ote_adr
  - concept_fair_value_gap
  - concept_smart_money_concepts
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:FVGRetrace
  rules: A displacement candle (body >= `disp_atr` x ATR) in the direction of the HTF trend leaves a three-candle fair value gap; rest a LIMIT at the gap's midpoint;
    stop beyond the displacement candle; target `rr` R.
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config:
    config: sniper_fvg_retrace@4h@fx_raw
    oos_trades: 112
    oos_gross_r: 0.112
    oos_net_r: 0.09
  tested:
  - config: sniper_fvg_retrace@4h@fx_raw
    oos_trades: 112
    oos_gross_r: 0.112
    oos_net_r: 0.09
  - config: sniper_fvg_retrace@4h@fx_std
    oos_trades: 109
    oos_gross_r: 0.059
    oos_net_r: 0.055
  - config: sniper_fvg_retrace@15m@ultra
    oos_trades: 1184
    oos_gross_r: -0.015
    oos_net_r: -0.098
  - config: sniper_fvg_retrace@1h@fx_raw
    oos_trades: 415
    oos_gross_r: -0.057
    oos_net_r: -0.108
  - config: sniper_fvg_retrace@1h@fx_std
    oos_trades: 407
    oos_gross_r: -0.119
    oos_net_r: -0.13
  - config: sniper_fvg_retrace@15m@low
    oos_trades: 1184
    oos_gross_r: -0.015
    oos_net_r: -0.182
- id: sniper_ote_retrace
  type: setup
  title: Optimal trade entry (62-79% retracement) after a break of structure (codified)
  derived_from:
  - strategy_trader_mayne_structure_ote
  - strategy_nbb_trader_po3_ote_adr
  - concept_premium_discount_ote
  - concept_fibonacci
  - concept_market_structure
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:OTERetrace
  rules: 'In an HTF uptrend, a fresh 5m swing high above a leg of >= `leg_atr` x ATR: rest a LIMIT at the `fib` (0.705) retracement of the leg (the optimal trade
    entry zone), stop below the leg''s origin, target the swing high.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_ote_retrace@15m@ultra
    oos_trades: 1347
    oos_gross_r: -0.017
    oos_net_r: -0.058
  tested:
  - config: sniper_ote_retrace@15m@ultra
    oos_trades: 1347
    oos_gross_r: -0.017
    oos_net_r: -0.058
  - config: sniper_ote_retrace@5m@ultra
    oos_trades: 6028
    oos_gross_r: -0.001
    oos_net_r: -0.065
  - config: sniper_ote_retrace@1h@fx_raw
    oos_trades: 441
    oos_gross_r: -0.046
    oos_net_r: -0.075
  - config: sniper_ote_retrace@1h@fx_std
    oos_trades: 431
    oos_gross_r: -0.078
    oos_net_r: -0.084
  - config: sniper_ote_retrace@15m@low
    oos_trades: 1347
    oos_gross_r: -0.017
    oos_net_r: -0.099
  - config: sniper_ote_retrace@5m@low
    oos_trades: 6028
    oos_gross_r: -0.001
    oos_net_r: -0.129
- id: sniper_orb_retest
  type: setup
  title: Opening-range breakout and retest (New York open) (codified)
  derived_from:
  - strategy_vincent_desiano_break_retest
  - strategy_okala_80_20_nasdaq
  - concept_breakout_trading
  - concept_trading_sessions_killzones
  - concept_support_resistance
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:ORBRetest
  rules: 'New York opening range (09:30-10:00 New York time, daylight saving included): after the first close beyond the range, rest a LIMIT at the range edge for
    the retest; stop at the range midpoint; target `rr` R. Entries until `last_entry` New York; timeframes of 30 minutes or less.'
  markets:
  - crypto
  - fx
  max_timeframe: 30m
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_orb_retest@5m@ultra
    oos_trades: 2104
    oos_gross_r: -0.008
    oos_net_r: -0.073
  tested:
  - config: sniper_orb_retest@5m@ultra
    oos_trades: 2104
    oos_gross_r: -0.008
    oos_net_r: -0.073
  - config: sniper_orb_retest@15m@ultra
    oos_trades: 1218
    oos_gross_r: -0.015
    oos_net_r: -0.088
  - config: sniper_orb_retest@5m@low
    oos_trades: 2104
    oos_gross_r: -0.008
    oos_net_r: -0.139
  - config: sniper_orb_retest@15m@low
    oos_trades: 1218
    oos_gross_r: -0.015
    oos_net_r: -0.161
  - config: sniper_orb_retest@5m@std
    oos_trades: 2104
    oos_gross_r: -0.008
    oos_net_r: -0.59
  - config: sniper_orb_retest@15m@std
    oos_trades: 1218
    oos_gross_r: -0.015
    oos_net_r: -0.667
- id: sniper_ema_pullback
  type: setup
  title: Trend pullback to the 20 EMA with a rejection close (codified)
  derived_from:
  - strategy_marci_silfrain_measured_move
  - strategy_tori_trendline_4h
  - strategy_anthony_crudele_futures_trend
  - concept_trend_following
  - concept_moving_averages
  - concept_multi_timeframe_analysis
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:EMAPullback
  rules: 'HTF trend; a 5m bar dips to the 20 EMA and closes back in the trend direction as a rejection candle: enter at market on the next open, stop beyond the bar,
    target `rr` R.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_ema_pullback@1h@fx_raw
    oos_trades: 2084
    oos_gross_r: -0.008
    oos_net_r: -0.063
  tested:
  - config: sniper_ema_pullback@1h@fx_raw
    oos_trades: 2084
    oos_gross_r: -0.008
    oos_net_r: -0.063
  - config: sniper_ema_pullback@4h@fx_raw
    oos_trades: 652
    oos_gross_r: -0.042
    oos_net_r: -0.069
  - config: sniper_ema_pullback@4h@fx_std
    oos_trades: 652
    oos_gross_r: -0.079
    oos_net_r: -0.091
  - config: sniper_ema_pullback@1h@fx_std
    oos_trades: 2106
    oos_gross_r: -0.08
    oos_net_r: -0.102
  - config: sniper_ema_pullback@15m@ultra
    oos_trades: 6717
    oos_gross_r: 0.008
    oos_net_r: -0.161
  - config: sniper_ema_pullback@5m@ultra
    oos_trades: 30473
    oos_gross_r: 0.035
    oos_net_r: -0.23
- id: sniper_vwap_reversion
  type: setup
  title: VWAP band re-entry in a range (codified)
  derived_from:
  - strategy_lance_breitstein_mean_reversion
  - strategy_jj_simon_fair_pricing
  - concept_vwap
  - concept_mean_reversion
  - concept_auction_market_theory
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:VWAPReversion
  rules: 'In a range regime, a close back inside the VWAP - `k` sd band after a close outside it: enter at market, stop beyond the 3-bar extreme, target the session
    VWAP.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config:
    config: sniper_vwap_reversion@1h@fx_raw
    oos_trades: 159
    oos_gross_r: 0.142
    oos_net_r: 0.041
  tested:
  - config: sniper_vwap_reversion@1h@fx_raw
    oos_trades: 159
    oos_gross_r: 0.142
    oos_net_r: 0.041
  - config: sniper_vwap_reversion@1h@fx_std
    oos_trades: 159
    oos_gross_r: -0.029
    oos_net_r: -0.073
  - config: sniper_vwap_reversion@15m@ultra
    oos_trades: 609
    oos_gross_r: -0.005
    oos_net_r: -0.17
  - config: sniper_vwap_reversion@5m@ultra
    oos_trades: 3010
    oos_gross_r: -0.001
    oos_net_r: -0.219
  - config: sniper_vwap_reversion@4h@fx_raw
    oos_trades: 19
    oos_gross_r: -0.198
    oos_net_r: -0.27
  - config: sniper_vwap_reversion@15m@low
    oos_trades: 609
    oos_gross_r: -0.005
    oos_net_r: -0.335
- id: sniper_break_retest
  type: setup
  title: Break and retest of a key level (codified)
  derived_from:
  - strategy_vincent_desiano_break_retest
  - strategy_gala_trades_price_action
  - strategy_abraham_perez_ict_orderflow
  - concept_support_resistance
  - concept_breakout_trading
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:BreakRetest
  rules: 'Research spec S5. A momentum close through the prior-day high (low) or the last confirmed HTF pivot, after a close on the other side: rest a LIMIT just
    beyond the level for the retest; stop 0.5 ATR back through the level; target 2R. 03:00-12:00 New York.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_break_retest@15m@ultra
    oos_trades: 672
    oos_gross_r: 0.004
    oos_net_r: -0.105
  tested:
  - config: sniper_break_retest@15m@ultra
    oos_trades: 672
    oos_gross_r: 0.004
    oos_net_r: -0.105
  - config: sniper_break_retest@4h@fx_raw
    oos_trades: 367
    oos_gross_r: -0.067
    oos_net_r: -0.111
  - config: sniper_break_retest@4h@fx_std
    oos_trades: 365
    oos_gross_r: -0.144
    oos_net_r: -0.153
  - config: sniper_break_retest@15m@low
    oos_trades: 672
    oos_gross_r: 0.004
    oos_net_r: -0.214
  - config: sniper_break_retest@5m@ultra
    oos_trades: 3445
    oos_gross_r: -0.14
    oos_net_r: -0.335
  - config: sniper_break_retest@1h@fx_raw
    oos_trades: 663
    oos_gross_r: -0.251
    oos_net_r: -0.353
- id: sniper_asia_london_judas
  type: setup
  title: Asia range, London sweep, return (session liquidity model) (codified)
  derived_from:
  - strategy_candace_lau_nq_sweep_reversal
  - strategy_nbb_trader_po3_ote_adr
  - strategy_jadecap_liquidity_volatility
  - concept_amd_power_of_three
  - concept_trading_sessions_killzones
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:AsiaLondonJudas
  rules: 'Research spec S8. A compressed Asia range (20:00-24:00 New York, at most 0.5 x the 10-day average daily range) is swept in the London window (02:00-05:00
    New York) and price closes back inside within 6 bars: rest a LIMIT at the swept Asia extreme; stop beyond the sweep; target the opposite Asia extreme (at least
    1.5R); flat by 11:00 New York.'
  markets:
  - crypto
  - fx
  max_timeframe: 15m
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_asia_london_judas@5m@ultra
    oos_trades: 1184
    oos_gross_r: -0.201
    oos_net_r: -0.376
  tested:
  - config: sniper_asia_london_judas@5m@ultra
    oos_trades: 1184
    oos_gross_r: -0.201
    oos_net_r: -0.376
  - config: sniper_asia_london_judas@15m@ultra
    oos_trades: 454
    oos_gross_r: -0.318
    oos_net_r: -0.455
  - config: sniper_asia_london_judas@5m@low
    oos_trades: 1184
    oos_gross_r: -0.201
    oos_net_r: -0.552
  - config: sniper_asia_london_judas@15m@low
    oos_trades: 454
    oos_gross_r: -0.318
    oos_net_r: -0.592
  - config: sniper_asia_london_judas@15m@std
    oos_trades: 454
    oos_gross_r: -0.318
    oos_net_r: -1.294
  - config: sniper_asia_london_judas@5m@std
    oos_trades: 1184
    oos_gross_r: -0.201
    oos_net_r: -1.451
- id: sniper_round_number_sweep
  type: setup
  title: Round-number stop run and reclaim (codified)
  derived_from:
  - strategy_okala_80_20_nasdaq
  - strategy_marco_trades_liquidity_grab
  - concept_support_resistance
  - concept_liquidity_sweep_reversal
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:RoundNumberSweep
  rules: 'Research spec S9. Price approached a round number from one side for 12 closes, poked through it by 0.05-1.0 ATR and closed back: rest a LIMIT at the round
    number; stop beyond the poke; target 2R. 02:00-16:00 New York. The grid is per market (BTC $1,000, ETH $100, EUR/USD 0.0050, gold $10).'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_round_number_sweep@4h@fx_raw
    oos_trades: 464
    oos_gross_r: -0.183
    oos_net_r: -0.252
  tested:
  - config: sniper_round_number_sweep@4h@fx_raw
    oos_trades: 464
    oos_gross_r: -0.183
    oos_net_r: -0.252
  - config: sniper_round_number_sweep@4h@fx_std
    oos_trades: 458
    oos_gross_r: -0.264
    oos_net_r: -0.278
  - config: sniper_round_number_sweep@1h@fx_raw
    oos_trades: 1204
    oos_gross_r: -0.218
    oos_net_r: -0.347
  - config: sniper_round_number_sweep@1h@fx_std
    oos_trades: 1182
    oos_gross_r: -0.352
    oos_net_r: -0.382
  - config: sniper_round_number_sweep@15m@ultra
    oos_trades: 1228
    oos_gross_r: -0.256
    oos_net_r: -0.438
  - config: sniper_round_number_sweep@5m@ultra
    oos_trades: 2583
    oos_gross_r: -0.235
    oos_net_r: -0.509
- id: sniper_ob_mean_threshold
  type: setup
  title: Order-block retest at the 50% after a break of structure (codified)
  derived_from:
  - strategy_trader_mayne_structure_ote
  - concept_order_blocks_breakers
  - concept_market_structure
  - concept_premium_discount_ote
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:OrderBlockMT
  rules: Research spec S10 on one timeframe. A momentum close through the last confirmed pivot (body >= 0.8 ATR); the order block is the last opposite candle in the
    8 bars before the break; if its 50% (mean threshold) is in the discount half of the dealing range, rest a LIMIT there; stop beyond the block; target the dealing-range
    extreme (at least 1.5R).
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config:
    config: sniper_ob_mean_threshold@4h@fx_raw
    oos_trades: 43
    oos_gross_r: 0.316
    oos_net_r: 0.255
  tested:
  - config: sniper_ob_mean_threshold@4h@fx_raw
    oos_trades: 43
    oos_gross_r: 0.316
    oos_net_r: 0.255
  - config: sniper_ob_mean_threshold@4h@fx_std
    oos_trades: 46
    oos_gross_r: 0.228
    oos_net_r: 0.213
  - config: sniper_ob_mean_threshold@1h@fx_raw
    oos_trades: 188
    oos_gross_r: -0.07
    oos_net_r: -0.18
  - config: sniper_ob_mean_threshold@15m@ultra
    oos_trades: 696
    oos_gross_r: -0.009
    oos_net_r: -0.217
  - config: sniper_ob_mean_threshold@1h@fx_std
    oos_trades: 204
    oos_gross_r: -0.241
    oos_net_r: -0.269
  - config: sniper_ob_mean_threshold@5m@ultra
    oos_trades: 2326
    oos_gross_r: -0.039
    oos_net_r: -0.415
- id: sniper_sweep_reclaim_limit
  type: setup
  title: Prior-day sweep + reclaim, retest entry (limit) (codified)
  derived_from:
  - strategy_candace_lau_nq_sweep_reversal
  - strategy_marco_trades_liquidity_grab
  - strategy_dhesi_liquidity_inversion
  - concept_liquidity_sweep_reversal
  - concept_liquidity
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:SweepReclaimRetest
  rules: 'Research spec S1, the maker version of the prior-day sweep: after the sweep and reclaim inside the London or New York morning window, rest a LIMIT at the
    reclaimed level (the retest) instead of buying the next open; stop beyond the sweep; target 2R.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_sweep_reclaim_limit@1h@fx_raw
    oos_trades: 921
    oos_gross_r: -0.072
    oos_net_r: -0.177
  tested:
  - config: sniper_sweep_reclaim_limit@1h@fx_raw
    oos_trades: 921
    oos_gross_r: -0.072
    oos_net_r: -0.177
  - config: sniper_sweep_reclaim_limit@15m@ultra
    oos_trades: 808
    oos_gross_r: -0.095
    oos_net_r: -0.209
  - config: sniper_sweep_reclaim_limit@4h@fx_raw
    oos_trades: 531
    oos_gross_r: -0.186
    oos_net_r: -0.245
  - config: sniper_sweep_reclaim_limit@1h@fx_std
    oos_trades: 913
    oos_gross_r: -0.223
    oos_net_r: -0.247
  - config: sniper_sweep_reclaim_limit@4h@fx_std
    oos_trades: 522
    oos_gross_r: -0.278
    oos_net_r: -0.291
  - config: sniper_sweep_reclaim_limit@5m@ultra
    oos_trades: 1931
    oos_gross_r: -0.146
    oos_net_r: -0.316
- id: sniper_ema_pullback_limit
  type: setup
  title: Trend pullback to the 20 EMA, limit entry (codified)
  derived_from:
  - strategy_marci_silfrain_measured_move
  - strategy_tori_trendline_4h
  - strategy_anthony_crudele_futures_trend
  - concept_trend_following
  - concept_moving_averages
  - concept_multi_timeframe_analysis
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:EMAPullbackLimit
  rules: 'Maker version of the EMA pullback: rest a LIMIT at the rejection bar''s close for 2 bars instead of buying the next open (it fills only if price comes back
    to it).'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: sniper_ema_pullback_limit@4h@fx_raw
    oos_trades: 656
    oos_gross_r: -0.041
    oos_net_r: -0.065
  tested:
  - config: sniper_ema_pullback_limit@4h@fx_raw
    oos_trades: 656
    oos_gross_r: -0.041
    oos_net_r: -0.065
  - config: sniper_ema_pullback_limit@1h@fx_raw
    oos_trades: 2067
    oos_gross_r: -0.026
    oos_net_r: -0.074
  - config: sniper_ema_pullback_limit@15m@ultra
    oos_trades: 6599
    oos_gross_r: -0.02
    oos_net_r: -0.089
  - config: sniper_ema_pullback_limit@4h@fx_std
    oos_trades: 641
    oos_gross_r: -0.088
    oos_net_r: -0.092
  - config: sniper_ema_pullback_limit@1h@fx_std
    oos_trades: 2059
    oos_gross_r: -0.098
    oos_net_r: -0.108
  - config: sniper_ema_pullback_limit@5m@ultra
    oos_trades: 29628
    oos_gross_r: -0.014
    oos_net_r: -0.123
- id: trend_donchian_breakout
  type: setup
  title: Donchian 20-bar breakout (Turtle-style trend model) (codified)
  derived_from:
  - person_richard_donchian
  - person_richard_dennis
  - book_way_of_the_turtle
  - book_complete_turtletrader
  - book_trend_following_covel
  - concept_trend_following
  - concept_breakout_trading
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:DonchianTrend
  rules: 'Trend model (not a sniper entry): a fresh close beyond the previous 20-bar high (low), market entry, 2 ATR stop, 3R target, time exit after 60 bars. The
    Turtle rule set simplified to a bracket.'
  markets:
  - crypto
  - fx
  max_timeframe: null
  verdict: positive after costs out-of-sample in its best configuration (check the gate and multiple testing)
  best_config:
    config: trend_donchian_breakout@4h@fx_raw
    oos_trades: 522
    oos_gross_r: 0.094
    oos_net_r: 0.08
  tested:
  - config: trend_donchian_breakout@4h@fx_raw
    oos_trades: 522
    oos_gross_r: 0.094
    oos_net_r: 0.08
  - config: trend_donchian_breakout@4h@fx_std
    oos_trades: 524
    oos_gross_r: 0.072
    oos_net_r: 0.066
  - config: trend_donchian_breakout@1h@fx_raw
    oos_trades: 2126
    oos_gross_r: 0.025
    oos_net_r: -0.008
  - config: trend_donchian_breakout@1h@fx_std
    oos_trades: 2139
    oos_gross_r: -0.016
    oos_net_r: -0.03
  - config: trend_donchian_breakout@15m@ultra
    oos_trades: 5993
    oos_gross_r: 0.064
    oos_net_r: -0.033
  - config: trend_donchian_breakout@15m@low
    oos_trades: 5993
    oos_gross_r: 0.064
    oos_net_r: -0.131
- id: lit_intraday_momentum
  type: setup
  title: 'Intraday momentum: first half-hour predicts the last half-hour (codified)'
  derived_from:
  - concept_trend_following
  - concept_trading_sessions_killzones
  related:
  - synthesis_sniper_backtests
  - synthesis_sniper_entries
  code: trading_intelligence/sniper/setups.py:IntradayMomentum
  rules: 'Published effect (Gao, Han, Li & Zhou 2018 for the S&P 500; Shen, Urquhart & Wang 2022 for Bitcoin): the first half-hour''s return predicts the last half-hour''s.
    At 23:30 UTC, trade the last half-hour of the UTC day in the direction of the 00:00-00:30 return; protective stop 3 ATR; time exit at 24:00. Crypto only (a 24-hour
    market with a UTC day).'
  markets:
  - crypto
  max_timeframe: 30m
  verdict: negative after costs out-of-sample in every configuration tested
  best_config:
    config: lit_intraday_momentum@15m@ultra
    oos_trades: 2007
    oos_gross_r: -0.005
    oos_net_r: -0.077
  tested:
  - config: lit_intraday_momentum@15m@ultra
    oos_trades: 2007
    oos_gross_r: -0.005
    oos_net_r: -0.077
  - config: lit_intraday_momentum@5m@ultra
    oos_trades: 3008
    oos_gross_r: 0.006
    oos_net_r: -0.123
  - config: lit_intraday_momentum@15m@low
    oos_trades: 2007
    oos_gross_r: -0.005
    oos_net_r: -0.148
  - config: lit_intraday_momentum@5m@low
    oos_trades: 3008
    oos_gross_r: 0.006
    oos_net_r: -0.252
  - config: lit_intraday_momentum@15m@std
    oos_trades: 2007
    oos_gross_r: -0.005
    oos_net_r: -0.292
  - config: lit_intraday_momentum@5m@std
    oos_trades: 3008
    oos_gross_r: 0.006
    oos_net_r: -0.51
```


<!-- ===== FILE: trading-intelligence/10_sniper-lab/small-account-venues.md ===== -->

---
id: synthesis_small_account_venues
type: synthesis
title: "Trading a $20 Account — venues, fees, minimums and what is tradeable"
partition: 10_sniper-lab
layer: L6
aliases: [small account, $20 account, micro account, cent account, cheapest exchange, minimum order size, minimum notional]
tags: [venues, fees, costs, position-sizing, small-account, api, ccxt]
as_of: 2026-10-20
related: [philosophy_relationship, framework_decision_protocol, principle_05_mathematical_justification, principle_09_protect_capital, principle_06_do_not_force, philo_mathematics_sword, philo_capital_preservation, philo_conditional_probability, philo_acb_principle, philo_source_of_opportunity, concept_position_sizing, concept_leverage_margin, concept_risk_of_ruin_drawdown, concept_expectancy, concept_risk_reward_r_multiples, concept_scalping, concept_trade_execution, concept_market_microstructure, concept_volatility, formula_sheet, synthesis_evidence_lab, synthesis_pre_trade_checklist, framework_source_tiers, framework_trading_journal]
status: researched
---

# Trading a $20 Account — venues, fees, minimums and what is tradeable

> **Education, not financial advice.** Every fee, minimum and rule below was read on
> **2026-10-20** and will change. Check the venue's own page or API before each use.
> Nothing here is a win-rate or P&L claim. Numbers marked **T3** come from third-party
> summaries and **T4** from marketing ([[framework_source_tiers]]). Exchange APIs and
> first-party fee pages are treated as T1. Source keys like [S3] point to the list at the end.

## 0. The answer in six lines

1. **The cheapest venues I could verify:** Binance.US spot charges 0% maker and 0.02% taker on every pair, with a $1 minimum order [S3][S4]. MEXC spot charges 0% / 0.05% with a 1 USDT minimum [S11]. MEXC futures charges 0% / 0.02% [S12]. OKX's EEA/global schedule is 0.08% / 0.10%, with a minimum order of about $0.82 [S9][S10].
2. **Avoid these at $20:** Kraken Pro tier 1 (0.40% / 0.80%) [S1], Coinbase Advanced (about 0.60% / 1.20%, T3) [S21], OKX US (0.20% / 0.35%) [S9], Gate (0.20%) [S20] and Alpaca crypto (0.15% / 0.25%) [S23]. At these venues a 1% stop costs 0.3R to 2.4R per round trip before the market moves at all.
3. **The tightest stop at 1x:** with risk fixed at 0.5% of equity ($0.10), unleveraged spot cannot hold a position larger than $20. That means the tightest stop is 0.5% of price. On BTC today this is roughly a 1-hour structural stop or wider (§7.5).
4. **The widest stop:** a venue's minimum order puts a ceiling on how wide your stop can be, not a floor: widest stop = $0.10 ÷ minimum notional. On $5-minimum venues (Binance global, Bybit, Kraken) a daily-swing stop of about 5% is too wide. A $0.10 risk would need a $2 position, which is below their minimum (§7.4).
5. **1-minute scalps are not viable** on any venue checked here. Even at a 0%-maker venue with a taker stop exit, the cost is about 0.36R or more. Everywhere else it is 1.6R or more. 5-minute trades are marginal at best, and 15-minute trades are marginal on the two cheapest perp venues. 1-hour structure or longer is viable at Binance.US, MEXC and Hyperliquid. OKX needs about 4-hour structure (§7.5).
6. **Leverage does not fix this.** It multiplies fees per dollar of equity. Above about 50x, liquidation sits inside BTC's normal daily range (§8).

What a $20 account can honestly buy is **cheap evidence**: 100 to 300 journaled trades measured in R, with costs included. It cannot buy income. If the true edge is +0.1R per trade, that is $0.01 per trade at this size. This follows the law of large numbers in Section VI and the "evidence" leg of Section VIII ([[philo_source_of_opportunity]]).

## 1. Where this sits in the philosophy

- **Section VII, mathematics is the sword** ([[philo_mathematics_sword]], [[principle_05_mathematical_justification]]). Expected value only means something after costs. At $20, costs are the largest single number in the expected-value equation for short-horizon trades.
- **Section XIV, capital preservation** ([[philo_capital_preservation]], [[principle_09_protect_capital]]). Three risks matter here: liquidation (§8), counterparty and regulatory risk at offshore venues (§9), and fee drag. Fee drag is a slow ruin that a 0.5% risk rule does not prevent.
- **Section III, A → C → B** ([[philo_acb_principle]]). A stop must leave room for the "C" excursion. The cost arithmetic pushes small accounts toward tight stops, but tight stops sit inside C. The two pressures point in opposite directions, so the honest resolution is a longer horizon, not a tighter stop.
- **Sections VIII and IX, and principle 6** ([[principle_06_do_not_force]]). If a setup only works with a stop too tight to survive costs, the decision is not to trade it at this size.

Walk [[framework_decision_protocol]] as usual. This note supplies the "EV after costs" and "size" gates for a $20 account.

## 2. Recommendation table

| Who you are | First choice | Why | Second choice | Avoid at $20 |
|---|---|---|---|---|
| **US resident** in a Binance.US-supported state | **Binance.US spot** (`binanceus`) | 0% / 0.02% on all pairs. $1 minimum. API [S3][S4] | Coinbase Advanced (`coinbase`) only for a pair Binance.US lacks. It has a $1 minimum but costs about 0.60% / 1.20% (T3) [S21] | Kraken Pro tier 1, OKX US, Alpaca crypto |
| **US resident, FX** | **OANDA US** (v20 REST API) | No minimum deposit. Size in units of 1. EUR/USD spread-only pricing listed at 1.4 pips. 50:1 cap on majors [S26] | none needed | Offshore brokers: they do not take US clients [S27][S28] |
| **US resident, stocks** | **Alpaca** (`alpaca-py`; ccxt `alpaca` is crypto only) | $1 fractional orders, commission-free stocks [S23]. The PDT rule was replaced on 2026-06-04 [S24] | — | IBKR Pro Fixed: $1.00 minimum per order [S25] is 5% of a $20 position per side |
| **EU/EEA resident** | **OKX (EEA entity)** (`myokx`) | 0.08% / 0.10% [S9]. Minimum of about $0.82 [S10] | KuCoin EU: 0.10% / 0.10% [S14] | Kraken Pro tier 1, Gate |
| **UK resident** | OKX: its UK-language fee page shows 0.08% / 0.10% [S9]. **Check that you are eligible before relying on it** | — | Bybit UK: spot only, through an FCA-authorised promoter [S18] | Any crypto derivative: the FCA bans them for retail clients [S31]. Binance paused UK onboarding [S8] |
| **Nigeria / rest of Africa** | **MEXC spot** (`mexc`) | 0% / 0.05%, 1 USDT minimum [S11] | KuCoin (0.10% / 0.10%), but its Nigerian entity has only conditional approval-in-principle, not a licence [S16] | Venues that need fiat rails you cannot use. Note Binance ended naira services [S33] |
| **Anyone wanting perps** (where legal) | **MEXC futures** (0% / 0.02%, about $8 minimum) [S12] | Cheapest perp fees I found | **Hyperliquid** (`hyperliquid`): 0.015% / 0.045%, $10 minimum, self-custody [S22] | KuCoin futures: minimum 0.001 BTC, about $81 [S14] |

**The three venues used for the arithmetic in §7** are Binance.US spot, MEXC spot and OKX spot (EEA/global). Between them they cover the US, the rest of the world and the EU, and they are the cheapest spot venues with a verified API minimum.

## 3. Crypto spot venues (lowest tier, as read 2026-10-20)

Minimums come from each venue's public API, with prices from the same session: BTC about $81,500, ETH about $2,389, SOL about $104.4 [S2]. "Effective minimum" is the larger of the minimum quantity times price and the minimum notional.

| Venue (ccxt id) | Maker / taker | BTC / ETH / SOL minimum | Effective minimum | Notes |
|---|---|---|---|---|
| Binance.US (`binanceus`) | **0% / 0.02%** [S3] | 0.00001 BTC / 0.0001 ETH / 0.001 SOL; minimum notional $1 [S4] | **$1** | Flat for every user since 2026-04-22. Excludes the One-Click Buy/Sell product [S3]. 16 unsupported states and territories, including NY, TX, NC, OH, OR and WA [S5] |
| MEXC (`mexc`) | **0% / 0.05%** [S11] | Quantity step 0.000001 BTC; minimum order 1 USDT [S11] | **$1** | The API field `quoteAmountPrecision` is the minimum cost. ccxt's own source code notes this [S11]. Not available in the US, UK or Canada (T3) [S13] |
| OKX EEA/global (`myokx` / `okx`) | **0.08% / 0.10%** [S9] | 0.00001 BTC / 0.0001 ETH / 0.01 SOL [S10] | **$0.82** | The same site shows different regular-user rates by region: US 0.20% / 0.35% (`okxus`), UAE 0.40% / 0.60%, Australia 0.70% / 0.70% [S9] |
| KuCoin (`kucoin`) | 0.10% / 0.10% (LV0, EU page) [S14] | 0.00001 BTC; minimum funds 0.1 USDT [S14] | $0.82 | Exited the US under a 2025 plea agreement, for at least two years [S15] |
| Binance global (`binance`) | 0.10% / 0.10% (T3) [S7] | Minimum notional 5 USDT [S6] | **$5** | The API returns HTTP 451 to US IP addresses. UK onboarding paused in 2025 [S8] |
| Bybit (`bybit`) | 0.10% / 0.10% (VIP 0, page updated 2026-09-02) [S17] | Reported 5 USDT (T3) [S18] | $5 (T3) | API returns 403 to US IP addresses. EEA users are moved to Bybit EU. Not available in the US (T3) [S18] |
| Bitget (`bitget`) | 0.10% / 0.10% (T3, citing Bitget's FAQ) [S19] | Minimum 1 USDT [S19] | $1 | The public API reports a 0.2% fee field per symbol. This conflicts with the FAQ, so check your own account. Not available in the US (T3) [S35] |
| Gate (`gate`) | 0.20% / 0.20% (API field; T3 agrees) [S20] | Minimum quote 3 USDT [S20] | $3 | The entry tier reportedly rose from 0.10% to 0.20% in 2026 (T3) [S20] |
| Kraken Pro (`kraken`) | **0.40% / 0.80%** (tier 1, $0+) [S1] | 0.00006 BTC / 0.002 ETH / 0.05 SOL; minimum cost $0.50 [S2] | **$4.89** | Tier 2 needs $2.5K of 30-day volume (0.30% / 0.60%). The app's Instant Buy charges 1% [S1] |
| Coinbase Advanced (`coinbase`) | about **0.60% / 1.20%** (T3; Coinbase does not publish the full table) [S21] | Minimum quote $1 [S21] | $1 | Binance.US's own comparison page shows the same entry rates, observed 2026-04-21 (T4, a competitor's marketing) [S3] |
| Alpaca crypto (`alpaca`) | 0.15% / 0.25% (tier 1) [S23] | Docs example: 0.0001 BTC [S23] | about $8 | No margin and no shorting on crypto [S23] |

**Spreads are not the problem on majors.** A snapshot at 2026-10-20 07:55 UTC showed these top-of-book spreads [S4][S10][S11][S22]:

- **BTC:** 0.0000% to 0.0003%.
- **ETH:** 0.0004% to 0.005%.
- **SOL:** about 0.01% to 0.02%.

Fees dominate. Slippage on stop-market exits is not modelled here and should be added for thin pairs and fast markets.

**Minimum deposit.** Crypto deposits on these exchanges have no stated account minimum. The practical floor is set by the funding method (card or bank rails) and by network withdrawal fees. I did not verify per-method minimums, so check them in your account.

## 4. Crypto perpetuals (where legal for you)

| Venue | Maker / taker | Minimum order | Maximum leverage (API) | Source |
|---|---|---|---|---|
| MEXC futures | 0% / 0.02% (BTC), 0% / 0.01% (ETH) | 1 contract = 0.0001 BTC (about $8.15) | 500x | Contract API [S12] |
| Hyperliquid | 0.015% / 0.045% (tier 0) | $10 per order | 40x on BTC | Docs and info API [S22] |
| Bybit | 0.02% / 0.055% (VIP 0) | not verified (API blocked from the US) | — | Fee page [S17] |
| Bitget | 0.02% / 0.06% | 0.0001 BTC and 5 USDT | 150x | Contract API [S19] |
| KuCoin | 0.02% / 0.06% | 0.001 BTC (about $81), too large for $20 at sane risk | 125x | Contract API [S14] |
| OKX | (fees not verified here) | 0.01 contracts × 0.01 BTC = 0.0001 BTC (about $8.15) | 100x | Instrument API [S10] |

Fee rates printed in contract APIs are defaults. Your account tier sets what you actually pay. Funding payments add a cost or a credit on any position held across funding times; they are not modelled here. Binance futures is 0.02% / 0.05% for regular users (T3) [S36], but its minimum notional could not be read from a US IP address.

## 5. Forex and CFDs: micro lots, nano sizes and cent accounts

**Yes, cent accounts exist.** They show the balance in cents ($10 appears as 1,000 US cents) and scale lot sizes down by 100. They change the **units, not the costs**: the spread as a percentage of price is the same as on a normal account.

EUR/USD was about 1.1227 on the day [S2].

| Broker / account | Minimum deposit | EUR/USD cost | Minimum size | Pip value at minimum size | API |
|---|---|---|---|---|---|
| **OANDA US** | None, except premium status [S26] | Spread-only, 1.4 pips listed [S26] | **1 unit** [S26] | $0.0001 | v20 REST and streaming |
| IC Markets Raw (global site, now ic.com) | $0 [S27] | Average 0.1 pip plus $3.50 per lot per side ($0.07 round trip per 0.01 lot) [S27] | 0.01 lot = 1,000 units | **$0.10** | MetaTrader 4/5 and cTrader |
| Exness Standard Cent | No account minimum; the floor depends on the payment method [S28] | No commission. Spreads "from" about 0.2–0.3 pips (T3) | 0.01 cent lot = 10 units [S28] | **$0.001** | MetaTrader 4/5 |
| RoboForex ProCent | $10 [S29] | Spread from 1.3 pips, no commission [S29] | 0.01 lot on MT5, 0.1 lot on MT4 [S29] | $0.001 (MT5) | MetaTrader 4/5 |
| XM Micro | $5 (older page) [S30] | not verified | 1 lot = 1,000 units [S30] | check | MetaTrader 4/5 |

How the pip value of the minimum size limits a $0.10 risk on EUR/USD:

- **Micro lot (1,000 units, $0.10 per pip):** the widest stop you can use is **1 pip**. That is unusable. IC Markets' minimum size forces you to risk 5% of the account on a 10-pip stop.
- **About 100 units ($0.01 per pip):** up to a 10-pip stop. Some brokers offer this size; OANDA units can.
- **Cent account 0.01 cent lot or 10 OANDA units ($0.001 per pip):** up to a 100-pip stop.
- **1 OANDA unit ($0.0001 per pip):** any realistic stop.

Leverage rules:

- **US:** 50:1 on majors and 20:1 on other pairs [S26].
- **EU retail CFDs:** capped from 30:1 (major FX) down to 2:1 (crypto), with negative-balance protection [S32].
- **Offshore entities:** much higher. RoboForex offers up to 1:2000 with conditions [S29]. Exness offers up to "unlimited" for eligible accounts, with a 0% stop-out on Standard Cent [S28]. IC Markets' global site offers up to 1:5000 [S27].

These ceilings are a hazard, not a feature (§8). On MetaTrader brokers, "API" means Expert Advisors in MQL, or the MetaTrader 5 Python package, which runs on Windows. That is a much thinner automation path than OANDA's REST API (T5).

## 6. Fractional shares with an API

- **Alpaca** [S23]:
  - Orders from $1 on more than 2,000 US equities.
  - Market, limit, stop and stop-limit orders, all with `time_in_force=day`.
  - Notional or quantity sizing, up to 9 decimal places.
  - Extended and overnight sessions for eligible symbols.
  - Non-US users can fund from $1 (USD only) [S23].
- **The hidden floor at Alpaca:** regulatory fees (FINRA TAF on sells, CAT on buys and sells) are added up per day and **rounded up to $0.01** [S23]. A day with a fee-bearing trade therefore costs at least $0.01. At R = $0.10 that is **0.1R**, or 0.1–0.2R per round trip if entry and exit fall on different days.
- **PDT rule:** the SEC approved FINRA's replacement of the pattern-day-trader rule and its $25,000 minimum with intraday margin standards. The change took effect **2026-06-04**. Firms may phase it in until **2027-10-20**, so check what your broker actually applies [S24]. This mainly matters for margin accounts.
- **IBKR Pro Fixed:** $0.005 per share with a $1.00 minimum per order [S25]. On a $20 position that is about 10% of the position per round trip, which rules it out at this size.

## 7. The honest arithmetic

### 7.1 Formula

Position notional N = risk ÷ stop%. Round-trip cost = N × (entry fee + exit fee + any spread crossed). So the cost in R is:

> **cost_R = (fee_in + fee_out + spread crossed) ÷ stop%**

The notional cancels out, so **cost in R depends only on fee% and stop%**, not on account size. Account size matters through the **constraints** in §7.4: minimum orders, the 1x equity cap, and per-order or per-day floors like Alpaca's rounding. [[formula_sheet]] has the general form, `cost = ½·spread + commission + slippage`.

### 7.2 The three best options: cost in R per round trip

Each cell shows three cases, written maker / mixed / taker:

- **Maker:** both legs are resting limit orders, as when a target fills.
- **Mixed:** maker entry and a taker stop exit. This is the usual losing trade.
- **Taker:** both legs are market orders.

Spread uses the 2026-10-20 BTC snapshot. Slippage and funding are excluded.

| Venue | Stop 0.3% | Stop 0.5% | Stop 1% | Stop 2% |
|---|---|---|---|---|
| **Binance.US spot** (0 / 0.02%) | 0.000 / 0.067 / **0.134** | 0.000 / 0.040 / **0.081** | 0.000 / 0.020 / **0.040** | 0.000 / 0.010 / **0.020** |
| **MEXC spot** (0 / 0.05%) | 0.000 / 0.167 / **0.333** | 0.000 / 0.100 / **0.200** | 0.000 / 0.050 / **0.100** | 0.000 / 0.025 / **0.050** |
| **OKX spot EEA/global** (0.08 / 0.10%) | 0.533 / 0.600 / **0.667** | 0.320 / 0.360 / **0.400** | 0.160 / 0.180 / **0.200** | 0.080 / 0.090 / **0.100** |
| *For contrast:* MEXC futures (0 / 0.02%) | 0.000 / 0.067 / 0.133 | 0.000 / 0.040 / 0.080 | 0.000 / 0.020 / 0.040 | 0.000 / 0.010 / 0.020 |
| *For contrast:* Hyperliquid perp (0.015 / 0.045%) | 0.100 / 0.202 / 0.304 | 0.060 / 0.121 / 0.182 | 0.030 / 0.061 / 0.091 | 0.015 / 0.030 / 0.046 |

### 7.3 The expensive venues, all-taker cost in R

| Venue | 0.3% | 0.5% | 1% | 2% |
|---|---|---|---|---|
| KuCoin / Binance global / Bybit / Bitget (0.10%) | 0.667 | 0.400 | 0.200 | 0.100 |
| Gate (0.20%) | 1.333 | 0.800 | 0.400 | 0.200 |
| Alpaca crypto (0.25% taker) | 1.667 | 1.000 | 0.500 | 0.250 |
| OKX US (0.35% taker) | 2.333 | 1.400 | 0.700 | 0.350 |
| Kraken Pro tier 1 (0.80% taker) | **5.334** | 3.200 | 1.600 | 0.800 |
| Coinbase Advanced (about 1.20% taker, T3) | **8.000** | 4.800 | 2.400 | 1.200 |

At Kraken tier 1, a 0.3% stop costs more than five times the risk being taken. No entry signal can overcome that.

### 7.4 The stop window that $0.10 risk allows

The question "what is the smallest stop that lets a $0.10 risk meet the venue minimum" turns out to point the other way. The minimum order caps the stop from **above**. The account's equity, at a given leverage, caps it from **below**:

- **Widest stop** = $0.10 ÷ minimum notional. Wider than this and the position falls below the minimum.
- **Tightest stop** = $0.10 ÷ (equity × leverage) = **0.5% at 1x**, 0.1% at 5x, 0.05% at 10x.
- Put the other way: at stop s, the **smallest risk the venue allows** is minimum notional × s.

| Venue | Effective minimum | Widest stop at $0.10 risk | Smallest possible risk at 0.3% / 0.5% / 1% / 2% stop |
|---|---|---|---|
| OKX spot / KuCoin | $0.82 | 12.2% | $0.002 / $0.004 / $0.008 / $0.016 |
| Binance.US / MEXC / Bitget / Coinbase | $1.00 | 10.0% | $0.003 / $0.005 / $0.010 / $0.020 |
| Gate | $3.00 | 3.3% | $0.009 / $0.015 / $0.030 / $0.060 |
| Kraken Pro | $4.89 | 2.0% | $0.015 / $0.024 / $0.049 / $0.098 |
| Binance global / Bybit | $5.00 | 2.0% | $0.015 / $0.025 / $0.050 / **$0.100** |
| Alpaca crypto / MEXC futures | about $8.15 | 1.2% | $0.024 / $0.041 / $0.082 / **$0.163** ✗ |
| Hyperliquid | $10.00 | 1.0% | $0.030 / $0.050 / $0.100 / **$0.200** ✗ |

✗ means a 0.5%-of-equity risk cannot be met: the minimum order forces a larger risk. So on unleveraged spot with $20, every stop from 0.5% up to the venue's ceiling is placeable at 0.5% risk. Stops tighter than 0.5% need leverage.

### 7.5 Which holding periods survive costs (BTC, measured)

**Method.** I took 720 bars per timeframe from Kraken's public OHLC endpoint [S2] and used a stop of 1.5 × the mean true range of the bar. This is a stand-in for a structural stop at that horizon, not a rule. The 1-minute sample covers only the 12 hours to 07:53 UTC on 2026-10-20, a quiet Asia session, so 1-minute ranges in busy sessions will be larger. Costs are taker / mixed, in R.

Median true range per bar was:

- **1m:** 0.032%
- **5m:** 0.086%
- **15m:** 0.183%
- **1h:** 0.383%
- **4h:** 0.862%
- **1d:** 2.93%

| Bar | Stop | Notional at $0.10 risk | Leverage needed | Binance.US / MEXC futures | MEXC spot | OKX spot | Hyperliquid | Kraken Pro | Coinbase (T3) |
|---|---|---|---|---|---|---|---|---|---|
| 1m | 0.057% | $176 | 8.8x (spot impossible) | 0.71 / 0.36 | 1.76 / 0.88 | 3.53 / 3.18 | 1.61 / 1.07 | 28.2 / 21.2 | 42.4 / 31.8 |
| 5m | 0.159% | $63 | 3.1x (spot impossible) | 0.25 / 0.13 | 0.63 / 0.31 | 1.25 / 1.13 | 0.57 / 0.38 | 10.0 / 7.5 | 15.1 / 11.3 |
| 15m | 0.347% | $29 | 1.4x (spot impossible) | 0.12 / 0.06 | 0.29 / 0.14 | 0.58 / 0.52 | 0.26 / 0.17 | 4.6 / 3.5 | 6.9 / 5.2 |
| 1h | 0.718% | $13.9 | 0.7x | **0.06 / 0.03** | **0.14 / 0.07** | 0.28 / 0.25 | 0.13 / 0.08 | 2.2 / 1.7 | 3.3 / 2.5 |
| 4h | 1.569% | $6.4 | 0.3x | 0.03 / 0.01 | 0.06 / 0.03 | 0.13 / 0.11 | 0.06 / 0.04 | 1.0 / 0.8 | 1.5 / 1.2 |
| 1d | 5.096% | $1.96 | 0.1x | 0.01 / 0.00 | 0.02 / 0.01 | 0.04 / 0.04 | below $10 minimum | below $4.89 minimum | 0.47 / 0.35 |

**A working scale (suggestion, not doctrine).** I call cost ≤ 0.10R viable, 0.10–0.25R marginal and > 0.25R not viable. The reason: at a 2R target, a 0.10R cost lifts the break-even win rate from 33.3% to 36.7%, and 0.25R lifts it to 41.7% (§7.7). Detecting a few points of win-rate difference takes hundreds of trades.

- **Not viable:** 1-minute scalps anywhere. 5-minute trades except possibly maker-in entries on 0% / 0.02% perps (0.13R, marginal). Anything at Kraken Pro tier 1 or Coinbase except, at best, daily swings.
- **Marginal:** 15-minute trades on MEXC futures (0.06–0.12R), which need 1.4x leverage, so perps only. 1-hour trades at OKX (0.25–0.28R).
- **Viable:** 1-hour structure or wider at Binance.US, MEXC spot or futures, and Hyperliquid. 4-hour or wider at OKX. Daily swings on $1-minimum venues.

### 7.6 The same test for EUR/USD at OANDA US

Spread-only at 1.4 pips is **0.0125% of price** [S26]. The bars are Kraken's 24/7 EUR/USD pair [S2], which includes weekends, so ranges are understated relative to the interbank session.

| Bar | Stop | Pips | Cost in R | Units for $0.10 risk | Margin at 2% |
|---|---|---|---|---|---|
| 1m | 0.010% | 1.1 | **1.28** | 916 | $20.57 (more than the account) |
| 5m | 0.031% | 3.5 | 0.40 | 288 | $6.46 |
| 15m | 0.065% | 7.3 | 0.19 | 136 | $3.06 |
| 1h | 0.158% | 17.8 | **0.08** | 56 | $1.26 |
| 4h | 0.309% | 34.6 | 0.04 | 29 | $0.65 |

FX tells the same story as crypto. Spread-only FX is viable from about 1-hour structure (an 18-pip stop). 1-minute FX scalping costs more than the risk taken.

### 7.7 Break-even win rate after costs

With a target of T R and a cost of c R, the break-even win rate is **p = (1 + c) ÷ (T + 1)**.

| Cost in R | T = 1 | T = 2 | T = 3 |
|---|---|---|---|
| 0 | 50.0% | 33.3% | 25.0% |
| 0.05 | 52.5% | 35.0% | 26.2% |
| 0.10 | 55.0% | 36.7% | 27.5% |
| 0.25 | 62.5% | 41.7% | 31.2% |
| 0.50 | 75.0% | 50.0% | 37.5% |
| 1.00 | 100% | 66.7% | 50.0% |

**How sure can you be of a win rate?** The 95% error band on a measured 40% win rate is about ±17.5 points after 30 trades, ±9.6 after 100, ±5.5 after 300 and ±3.0 after 1,000. A cost of 0.10R moves the break-even by 3.3 points at T = 2, which is smaller than the error after 300 trades. Run the expectancy check in `tools/philosophy/edge_lab.py` on any rule set before trusting it. [[synthesis_evidence_lab]] (S7) shows what costs do to the best-looking cell, and its sample-size study shows how often a real small edge looks like a loser ([[philo_conditional_probability]]).

### 7.8 What this means for "scraping trades day by day"

**Trading often means tight stops, and tight stops are exactly where costs in R explode.** A realistic daily rhythm for $20 is **one to three trades a day on 1-hour or 4-hour structure**, with these habits:

- Post-only limit entries at a 0%-maker venue.
- A stop-market exit, budgeted at the taker rate.
- Every fee journaled in R ([[framework_trading_journal]]).

This is not "waiting all day for 60%". The aim is to take only the trades whose cost in R leaves room for the edge you are trying to prove.

## 8. What leverage does to a $20 account

On an isolated perp, the liquidation distance is roughly 1/L minus the maintenance margin rate (MMR). The table below ignores fees and funding.

| Leverage on the full $20 | Notional | Liquidation move (MMR 0.4%) | Compared with BTC's measured median range |
|---|---|---|---|
| 5x | $100 | about 19.6% | about 7 median daily ranges |
| 10x | $200 | about 9.6% | about 3 daily ranges |
| 20x | $400 | about 4.6% | about 1.6 daily ranges |
| 50x | $1,000 | **about 1.6%** | inside one median daily range (2.93%) |
| 100x | $2,000 | about 0.6% | about 1.5 median hourly ranges (0.38%) |
| 500x (MEXC maximum, MMR 0.1%) | $10,000 | **about 0.1%** | about one median 5-minute range |

The MMR values come from the contract APIs: KuCoin 0.4%, Gate 0.3%, MEXC 0.1% [S12][S14][S20].

The right way to read leverage:

1. **Risk comes from the stop × the notional, not from the leverage setting.** For a 0.5% risk, the leverage you need is 0.5% ÷ stop%. A 1-hour BTC stop of 0.72% needs 0.7x, which is no leverage at all. Leverage only becomes necessary for stops below 0.5%, and that is the zone §7.5 shows is not viable after costs.
2. **Fees are charged on notional.** Running $20 at 10x on Hyperliquid costs 0.9% of equity per taker round trip. Ten round trips a day comes to about 9% of the account per day before any loss.
3. **Liquidation must sit well beyond the stop.** Gaps, outages and stop slippage happen. A 2% liquidation fee also applies on Kraken margin [S1].
4. **Offshore FX leverage of 1:2000 to "unlimited" is real.** With a 0% stop-out [S28], the whole $20 can go in one move. Negative-balance protection is required for EU retail CFDs [S32], but it is not universal offshore.

See [[concept_leverage_margin]], [[concept_risk_of_ruin_drawdown]] and [[concept_position_sizing]].

## 9. Regional notes (verify before you act)

- **United States:**
  - Binance.US does not serve 16 states and territories, including NY, TX, NC, OH, OR and WA [S5].
  - KuCoin left under its 2025 plea deal [S15].
  - MEXC, Bybit and Bitget do not serve US persons (T3) [S13][S18][S35].
  - OKX serves the US through OKX US at higher fees [S9].
  - Kraken excludes some states; NY and Maine are cited by T3 sources [S34].
  - Offshore FX and CFD brokers do not take US clients [S27][S28].
  - Forex is limited to 50:1 or 20:1 at registered dealers like OANDA [S26].
- **United Kingdom:**
  - The FCA's retail ban on crypto derivatives took effect on 2021-01-06. I found no repeal, but did not re-verify its current status [S31].
  - Binance paused new UK users in 2025 and is reported to be preparing an FCA application [S8].
  - Bybit returned for spot only [S18].
- **EU/EEA:**
  - Bybit serves the EEA through Bybit EU, authorised in Austria under MiCA [S18].
  - OKX serves the EEA from a separate site with its own fee page; ccxt uses the id `myokx` for it [S9]. I did not verify OKX's licence here.
  - Retail CFDs are capped from 30:1 down to 2:1 [S32].
- **Nigeria / Africa:**
  - The local exchanges Quidax and Busha are reported to hold SEC approval-in-principle under the incubation programme (ARIP) [S33].
  - KuCoin Nigeria received conditional approval-in-principle on 2026-10-13. This does not yet allow it to operate or onboard clients [S16].
  - Binance ended naira services in March 2024 [S33].
  - In practice, residents use offshore venues through P2P funding. Those venues are not locally licensed, so counterparty and legal risk sits with you (Section XIV).

## 10. Execution habits this implies (suggestions)

1. **Read limits from the API before every order:** ccxt `market['limits']['amount']['min']` and `['cost']['min']`, and the `precision` fields. Round the size down, then confirm that notional ≥ minimum. Never hard-code the figures in this note.
2. **Default to post-only limit entries** at 0%-maker venues. Budget every stop at the taker rate (the "mixed" column in §7.2).
3. **Log cost_R for every trade** in the journal, next to the gross R.
4. **Do not raise the risk percentage** to get around a minimum order (§7.4 ✗ rows). Change the venue or the horizon instead ([[principle_09_protect_capital]]).
5. **Keep only what you can afford to lose at any offshore venue,** and withdraw profits on a schedule ([[philo_capital_preservation]]).
6. **Finish with the applicable [[synthesis_pre_trade_checklist]] items.** Related notes: [[concept_trade_execution]], [[concept_market_microstructure]], [[concept_scalping]].

## 11. Method, data and limits

- All figures were read on **2026-10-20** from a US-located network. Some pages and APIs were geo-blocked (Binance global API returned 451, Bybit API 403). Some fee pages were blocked by bot protection (Coinbase, Gate, MEXC, Exness), so those facts come from search-index copies or third-party sources and are marked as such.
- Fee figures are the **lowest-volume tier** for regular users, before token discounts, referral rebates or promotions.
- Ranges come from one venue (Kraken) and one 720-bar window per timeframe. They describe this window, not the future ([[concept_volatility]]).
- Not modelled: slippage, funding, withdrawal and network fees, taxes, FX conversion and the opportunity cost of your time.
- The calculator scripts used for §7 and §8 were run ad hoc and are not saved in the knowledge base. Every result is reproducible from the formulas and inputs shown.

## Sources

All were read on **2026-10-20**. "API" means a public JSON endpoint read directly.

| Key | Source | Tier |
|---|---|---|
| S1 | Kraken fee schedule (spot tiers, Instant Buy, margin liquidation fee): https://www.kraken.com/features/fee-schedule | T1 |
| S2 | Kraken public API, AssetPairs / Ticker / OHLC: https://api.kraken.com/0/public/AssetPairs?pair=XBTUSD,ETHUSD,SOLUSD · https://api.kraken.com/0/public/OHLC?pair=XBTUSD&interval=60 | T1 |
| S3 | Binance.US, "0% maker, 0.02% taker spot trading fees" (2026-04-22): https://blog.binance.us/zero-fee-trading/ | T1 (fees); T4 (competitor comparison) |
| S4 | Binance.US API exchangeInfo / bookTicker: https://api.binance.us/api/v3/exchangeInfo · https://api.binance.us/api/v3/ticker/bookTicker?symbol=BTCUSD | T1 |
| S5 | Binance.US supported and unsupported states (via search index): https://support.binance.us/en/articles/9842798-list-of-supported-and-unsupported-states-and-regions | T1 |
| S6 | Binance market-data API exchangeInfo (NOTIONAL filter 5 USDT): https://data-api.binance.vision/api/v3/exchangeInfo ; api.binance.com returned HTTP 451 | T1 |
| S7 | Binance spot fees (via search index): https://cryptopotato.com/binance-fees/ · https://coinspot.io/en/analysis/binance-fees-2025-the-ultimate-guide/ | T3 |
| S8 | Binance UK onboarding pause and licence plans (via search index): https://www.theblock.co/amp/post/257721/binance-to-temporarily-stop-accepting-new-uk-users-after-fca-restriction · https://cryptorank.io/news/feed/935f2-binance-return-uk-new-licence | T3 |
| S9 | OKX fee pages (embedded fee JSON by locale): https://www.okx.com/en-eu/fees · https://www.okx.com/en-gb/fees · https://www.okx.com/fees (served as OKX US) · https://www.okx.com/en-ae/fees · https://www.okx.com/en-au/fees | T1 |
| S10 | OKX public instruments and ticker API: https://www.okx.com/api/v5/public/instruments?instType=SPOT&instId=BTC-USDT · https://www.okx.com/api/v5/public/instruments?instType=SWAP&instId=BTC-USDT-SWAP | T1 |
| S11 | MEXC API exchangeInfo / bookTicker: https://api.mexc.com/api/v3/exchangeInfo?symbols=BTCUSDT,ETHUSDT,SOLUSDT ; ccxt 4.5.88 from PyPI, file `ccxt/mexc.py`, whose comment maps `quoteAmountPrecision` to the minimum order cost: https://pypi.org/project/ccxt/ | T1 |
| S12 | MEXC contract API: https://contract.mexc.com/api/v1/contract/detail?symbol=BTC_USDT | T1 |
| S13 | MEXC restricted countries (via search index): https://www.cryptoninjas.net/crypto/mexc-restricted-and-supported-countries/ | T3 |
| S14 | KuCoin EU fee table: https://www.kucoin.com/bn-eu/support/48142946141092 ; KuCoin APIs: https://api.kucoin.com/api/v2/symbols · https://api-futures.kucoin.com/api/v1/contracts/XBTUSDTM | T1 |
| S15 | KuCoin US plea and exit (via search index): https://cryptoslate.com/kucoin-exits-us-market-pays-300m-fine-for-unlicensed-operations/ · https://cointelegraph.com/news/kucoin-pleads-guilty-us-charges-300-million-fine | T3 |
| S16 | KuCoin Nigeria conditional approval-in-principle (2026-10-13, via search index): https://www.cryptotimes.io/2026/10/13/kucoin-nigeria-gains-conditional-entry-into-sec-regulatory-program/ | T3 |
| S17 | Bybit Trading Fee Structure (updated 2026-09-02): https://www.bybit.com/en/help-center/article/Trading-Fee-Structure | T1 |
| S18 | Bybit UK, EU and minimum order (via search index): https://coin360.com/news/bybit-returns-uk-fca-compliance-spot-trading · https://www.coindesk.com/business/2026/04/21/uk-invites-crypto-giant-bybit-to-london-to-win-over-some-of-uae-s-innovation-shine · https://glama.ai/mcp/servers/@TheMacroeconomicDao/bybit-ai-trader/blob/933307b9fdb8a27cd5a5a341962f405108d0389a/FINAL_ORDER_LIMITS_RESEARCH.md | T3 |
| S19 | Bitget APIs: https://api.bitget.com/api/v2/spot/public/symbols · https://api.bitget.com/api/v2/mix/market/contracts?productType=USDT-FUTURES&symbol=BTCUSDT ; fee FAQ summary (via search index): https://vocus.cc/article/6ab9d509fd89780001855c4c | T1 (API) / T3 (fees) |
| S20 | Gate APIs: https://api.gateio.ws/api/v4/spot/currency_pairs/BTC_USDT · https://api.gateio.ws/api/v4/futures/usdt/contracts/BTC_USDT ; fee change summary (via search index): https://bitsgap.com/blog/gate-io-trading-fees-explained-what-it-costs | T1 (API) / T3 (fees) |
| S21 | Coinbase Advanced public product API: https://api.coinbase.com/api/v3/brokerage/market/products/BTC-USD ; entry-tier fees (via search index): https://www.bankrate.com/investing/coinbase-review | T1 (API) / T3 (fees) |
| S22 | Hyperliquid fees: https://hyperliquid.gitbook.io/hyperliquid-docs/trading/fees ; $10 minimum: https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/error-responses ; info API: https://api.hyperliquid.xyz/info | T1 |
| S23 | Alpaca docs: https://docs.alpaca.markets/docs/fractional-trading · https://docs.alpaca.markets/us/docs/crypto-fees · https://docs.alpaca.markets/docs/crypto-trading · https://docs.alpaca.markets/us/docs/regulatory-fees · https://docs.alpaca.markets/us/docs/understanding-finras-new-intraday-margin-rule-and-the-end-of-pdt ; international $1 funding (via search index): https://alpaca.markets/support/is-alpaca-available-outside-the-us | T1 |
| S24 | FINRA Regulatory Notice 26-10 (effective 2026-06-04; phase-in to 2027-10-20): https://www.finra.org/sites/default/files/2026-04/Regulatory-Notice-26-10.pdf | T1 |
| S25 | Interactive Brokers commissions (via search index): https://www.interactivebrokers.com/en/pricing/commissions-home.php | T1 |
| S26 | OANDA US: https://help.oanda.com/us/en/faqs/account-types-and-leverage-us.htm · https://help.oanda.com/uk/en/faqs/micro-lots.htm · https://www.oanda.com/us-en/trading/our-pricing/ ; CFTC 50:1 / 20:1 (via search index): https://www.oanda.com/us-en/trading/spreads-margin/ | T1 |
| S27 | IC Markets account overview (redirects to ic.com): https://www.ic.com/en/trading-accounts/overview/ · https://www.icmarkets.eu/en/trading-pricing/trading-costs ; restricted countries (via search index): https://icmarkets.com/lp/en/icyourtrade6 | T1 |
| S28 | Exness help centre (via search index; direct fetch returned 403): https://get.exness.help/hc/en-us/articles/17537782786588-Standard-Cent-account · https://get.exness.help/hc/en-us/articles/360014693340-Margin-call-and-stop-out-levels-by-account-type ; US exclusion: https://brokerlistings.com/reviews/exness/is-exness-available-in-the-usa | T1 / T3 |
| S29 | RoboForex ProCent: https://roboforex.com/forex-trading/trading/cent-account/ | T1 |
| S30 | XM account types and Australian PDS (via search index): https://www.xm.com/account-types · https://www.xm.com/assets/pdf/new/docs/XMAU-Product-Disclosure-Statement.pdf | T1 |
| S31 | FCA retail crypto-derivatives ban (via search index): https://www.theblock.co/amp/post/79911/uk-regulator-fca-bans-crypto-derivatives-retail-users | T3 |
| S32 | ESMA CFD product intervention measures (via search index): https://www.esma.europa.eu/node/85445 | T1 |
| S33 | Nigeria SEC licensing, Binance naira exit, Bybit status (via search index): https://dabafinance.com/en/news/nigerias-sec-to-issue-first-crypto-exchange-licenses-this-month · https://kkinvesting.io/en/posts/bybit-exchange-guide-nigeria/ · https://kudicompass.com/nigeria-crypto-regulation/ · https://www.datawallet.com/crypto/best-crypto-exchanges-nigeria | T3 |
| S34 | Kraken US state exclusions (via search index): https://coinbureau.com/review/kraken/ | T3 |
| S35 | Bitget restricted countries (via search index): https://www.coinperps.com/zh/learn/bitget-restricted-countries | T3 |
| S36 | Binance futures regular-user fees (via search index): https://www.finder.com/cryptocurrency/trading/binance-futures-fees | T3 |


<!-- ===== FILE: trading-intelligence/10_sniper-lab/sniper-entries.md ===== -->

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


<!-- ===== FILE: trading-intelligence/10_sniper-lab/venues.yaml ===== -->

```yaml
# Venues for small accounts, read by `python -m trading_intelligence.sniper size`.
# Transcribed from small-account-venues.md (synthesis_small_account_venues), researched 2026-10-20.
# Fees are fractions of notional per side for the entry tier (no volume discount, no token discount).
# Forex/CFD rows carry the spread as a per-side cost in both maker and taker (no maker rebate exists).
# min_notional is the smallest order VALUE in USD. Fees and rules change: check the venue's own page
# before trading, and check that the venue is legal and licensed where you live.
# Education and research, not a recommendation of any venue.

venues:
  # ── crypto spot ──────────────────────────────────────────────────────────
  - venue_id: binance_us_spot
    name: "Binance.US spot"
    kind: spot
    maker: 0.0
    taker: 0.0002
    min_notional: 1.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "US residents only (16 states/territories excluded); one flat rate since 2026-04-22"
  - venue_id: mexc_spot
    name: "MEXC spot"
    kind: spot
    maker: 0.0
    taker: 0.0005
    min_notional: 1.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "offshore; excludes US/UK/Canada; reachable from Nigeria but not locally licensed (counterparty risk)"
  - venue_id: okx_spot
    name: "OKX spot (global/EEA schedule)"
    kind: spot
    maker: 0.0008
    taker: 0.0010
    min_notional: 1.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "regional fee schedules differ (OKX US 0.20%/0.35%)"
  - venue_id: binance_spot
    name: "Binance spot (global)"
    kind: spot
    maker: 0.0010
    taker: 0.0010
    min_notional: 5.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "fees T3; BNB payment discounts not included"
  - venue_id: bybit_spot
    name: "Bybit spot"
    kind: spot
    maker: 0.0010
    taker: 0.0010
    min_notional: 5.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "VIP 0; not for US persons; EEA users moved to Bybit EU"
  - venue_id: kucoin_spot
    name: "KuCoin spot"
    kind: spot
    maker: 0.0010
    taker: 0.0010
    min_notional: 1.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "LV0 rates; exited the US (2025)"
  - venue_id: kraken_pro_spot
    name: "Kraken Pro spot"
    kind: spot
    maker: 0.0040
    taker: 0.0080
    min_notional: 5.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "tier 1; not viable for short-term entries at small size"
  - venue_id: coinbase_advanced
    name: "Coinbase Advanced spot"
    kind: spot
    maker: 0.0060
    taker: 0.0120
    min_notional: 1.0
    max_leverage: 1.0
    slippage: 0.0001
    note: "entry tier (T3); not viable for short-term entries"
  # ── crypto perpetuals (leverage magnifies losses; liquidation is a real risk) ──
  - venue_id: mexc_futures
    name: "MEXC USDT perpetuals"
    kind: perp
    maker: 0.0
    taker: 0.0002
    min_notional: 8.2
    max_leverage: 5.0
    slippage: 0.0001
    note: "venue lists up to 500x; capped here at 5x for sizing; 1 contract = 0.0001 BTC; not for US/UK persons"
  - venue_id: hyperliquid_perp
    name: "Hyperliquid perpetuals"
    kind: perp
    maker: 0.00015
    taker: 0.00045
    min_notional: 10.0
    max_leverage: 5.0
    slippage: 0.0001
    note: "self-custody; venue lists 40x on BTC; capped here at 5x"
  - venue_id: bybit_perp
    name: "Bybit USDT perpetuals"
    kind: perp
    maker: 0.0002
    taker: 0.00055
    min_notional: 5.0
    max_leverage: 5.0
    slippage: 0.0001
    note: "VIP 0; minimum order not verified; not for US persons; UK retail cannot use crypto derivatives"
  # ── forex and gold ───────────────────────────────────────────────────────
  - venue_id: oanda_us
    name: "OANDA US (spread-only)"
    kind: cfd
    maker: 0.0000625
    taker: 0.0000625
    min_notional: 1.2
    max_leverage: 50.0
    slippage: 0.00002
    note: "US residents; EUR/USD 1.4 pips listed; size in single units"
  - venue_id: icmarkets_raw
    name: "IC Markets Raw Spread"
    kind: cfd
    maker: 0.0000355
    taker: 0.0000355
    min_notional: 1150.0
    max_leverage: 30.0
    slippage: 0.00001
    note: "0.1 pip average + $3.50 per lot per side; minimum 0.01 lot (1,000 units) is too big for tight risk on $20"
  - venue_id: exness_std_cent
    name: "Exness Standard Cent"
    kind: cfd
    maker: 0.0000455
    taker: 0.0000455
    min_notional: 11.5
    max_leverage: 30.0
    slippage: 0.00002
    note: "cent account: 0.01 cent lot = 10 units; spreads 'from' 0.2-0.3 pips, about 1 pip assumed typical; offshore entity"
  - venue_id: roboforex_procent
    name: "RoboForex ProCent"
    kind: cfd
    maker: 0.000059
    taker: 0.000059
    min_notional: 11.5
    max_leverage: 30.0
    slippage: 0.00002
    note: "cent account; spreads from 1.3 pips; Belize entity; not for US/EU/UK clients"
```
