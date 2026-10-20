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

> Generated 2026-10-20 by `python -m trading_intelligence.sniper lab`. Markets: BTCUSDT, ETHUSDT, SOLUSDT, BNBUSDT, XRPUSDT (Binance spot history). Timeframes: 5m, 15m, 1h. Period 2022-01 to last full month; rules and the allowed regimes/sessions are chosen on data before 2024-01-01 and judged only on data after it. Fills are conservative (limits fill only when traded at or through, stop first when stop and target share a bar). Not a trading signal; education and research.

## Fee levels

| Level | Maker | Taker | Slippage on taker fills |
|---|---|---|---|
| std | 0.08% | 0.10% | 0.02% |
| low | 0.00% | 0.05% | 0.01% |

## Results (pooled across markets)

Every trade each setup produced. IS = in-sample (2022-2023), OOS = out-of-sample (2024 on). Gross R is before costs, net R after fees and slippage at that fee level. Stop % is the median stop distance.

| Setup | TF | Fees | OOS trades/day | Stop % | IS gross R | OOS gross R | OOS cost R | OOS net R |
|---|---|---|---|---|---|---|---|---|
| ema_pullback | 15m | low | 16.53 | 0.44 | -0.002 | +0.034 | +0.287 | -0.254 |
| fvg_retrace | 15m | low | 2.69 | 0.40 | -0.087 | -0.012 | +0.138 | -0.150 |
| orb_retest | 15m | low | 3.05 | 0.37 | +0.019 | -0.010 | +0.147 | -0.157 |
| ote_retrace | 15m | low | 3.26 | 0.72 | -0.019 | -0.004 | +0.070 | -0.075 |
| sweep_reclaim | 15m | low | 8.97 | 0.46 | +0.050 | -0.003 | +0.284 | -0.287 |
| vwap_reversion | 15m | low | 1.62 | 0.47 | -0.075 | +0.031 | +0.289 | -0.258 |
| ema_pullback | 1h | low | 3.89 | 0.96 | -0.018 | +0.004 | +0.130 | -0.126 |
| fvg_retrace | 1h | low | 0.67 | 0.94 | +0.059 | -0.006 | +0.055 | -0.060 |
| ote_retrace | 1h | low | 0.77 | 1.51 | -0.083 | -0.045 | +0.033 | -0.078 |
| sweep_reclaim | 1h | low | 4.85 | 0.86 | +0.074 | -0.012 | +0.150 | -0.162 |
| vwap_reversion | 1h | low | 0.28 | 0.62 | +0.101 | -0.147 | +0.198 | -0.346 |
| ema_pullback | 5m | low | 50.35 | 0.24 | +0.021 | +0.035 | +0.528 | -0.493 |
| fvg_retrace | 5m | low | 9.92 | 0.19 | -0.062 | -0.054 | +0.332 | -0.387 |
| orb_retest | 5m | low | 3.58 | 0.38 | +0.014 | -0.031 | +0.146 | -0.178 |
| ote_retrace | 5m | low | 9.69 | 0.40 | -0.018 | -0.014 | +0.129 | -0.143 |
| sweep_reclaim | 5m | low | 14.54 | 0.27 | +0.050 | +0.031 | +0.496 | -0.465 |
| vwap_reversion | 5m | low | 5.15 | 0.32 | -0.038 | +0.002 | +0.466 | -0.464 |
| ema_pullback | 15m | std | 16.53 | 0.44 | -0.002 | +0.034 | +0.652 | -0.618 |
| fvg_retrace | 15m | std | 2.69 | 0.40 | -0.087 | -0.012 | +0.628 | -0.640 |
| orb_retest | 15m | std | 3.05 | 0.37 | +0.019 | -0.010 | +0.673 | -0.683 |
| ote_retrace | 15m | std | 3.26 | 0.72 | -0.019 | -0.004 | +0.309 | -0.313 |
| sweep_reclaim | 15m | std | 8.97 | 0.46 | +0.050 | -0.003 | +0.637 | -0.640 |
| vwap_reversion | 15m | std | 1.62 | 0.47 | -0.075 | +0.031 | +0.641 | -0.611 |
| ema_pullback | 1h | std | 3.89 | 0.96 | -0.018 | +0.004 | +0.294 | -0.291 |
| fvg_retrace | 1h | std | 0.67 | 0.94 | +0.059 | -0.006 | +0.250 | -0.256 |
| ote_retrace | 1h | std | 0.77 | 1.51 | -0.083 | -0.045 | +0.142 | -0.187 |
| sweep_reclaim | 1h | std | 4.85 | 0.86 | +0.074 | -0.012 | +0.336 | -0.348 |
| vwap_reversion | 1h | std | 0.28 | 0.62 | +0.101 | -0.147 | +0.443 | -0.590 |
| ema_pullback | 5m | std | 50.35 | 0.24 | +0.021 | +0.035 | +1.198 | -1.163 |
| fvg_retrace | 5m | std | 9.92 | 0.19 | -0.062 | -0.054 | +1.446 | -1.500 |
| orb_retest | 5m | std | 3.58 | 0.38 | +0.014 | -0.031 | +0.665 | -0.696 |
| ote_retrace | 5m | std | 9.69 | 0.40 | -0.018 | -0.014 | +0.565 | -0.579 |
| sweep_reclaim | 5m | std | 14.54 | 0.27 | +0.050 | +0.031 | +1.123 | -1.092 |
| vwap_reversion | 5m | std | 5.15 | 0.32 | -0.038 | +0.002 | +0.998 | -0.995 |

## Inside the conditions chosen in-sample

The lab keeps only the regimes and sessions that were positive after costs in-sample (at least 20 trades each), then judges the out-of-sample trades inside them. This is the record the gate reads.

| Setup | TF | Fees | Allowed regimes | Allowed sessions | IS n | IS net R | OOS n | OOS net R | OOS t |
|---|---|---|---|---|---|---|---|---|---|
| fvg_retrace | 1h | low | trend_high_vol | late london | 79 | +0.290 | 111 | -0.205 | -1.57 |
| ote_retrace | 1h | low | trend_high_vol | london | 49 | +0.218 | 64 | -0.409 | -2.83 |
| sweep_reclaim | 1h | low | range_high_vol range_low_vol | asia | 176 | -0.085 | 220 | +0.019 | 0.18 |

## What passes the owner's gate

**None.** No configuration has an out-of-sample record that clears Gate 4 after costs. The gate will skip every live signal from these setups until a record does; the scanner keeps paper-trading them to build forward evidence.

## Multiple testing

34 configurations were tried; 3 had at least 30 out-of-sample trades inside their chosen conditions. The best of those (sniper_sweep_reclaim@1h@low, per-trade Sharpe +0.012 over 220 trades) has a deflated-Sharpe probability of 0.00 of being real once the number of trials is accounted for (Bailey & López de Prado; above 0.95 is the usual bar).

## Reading this as the owner's philosophy asks

- **Before any cost, the edge is about zero.** The best out-of-sample average before costs is +0.035R per trade (ema_pullback 5m). A pattern that does not pay before costs cannot be rescued by a cheaper venue; cheaper fees only shrink how much is lost (Section VII: expected value first).
- Costs in R are the deciding number: a 5-minute 'sniper' stop is often 0.2-0.3% of price, so a 0.1% fee per side is already a large fraction of 1R. Higher timeframes and maker-only orders shrink the cost in R (Gate 5.6).
- Several setups were mildly positive in-sample and about zero afterwards: the usual decay of a pattern fitted to the past (Section XVII). Only the out-of-sample columns are evidence.
- More trades is not more edge: the busiest setup (EMA pullback on 5m, about 50 trades a day across five markets) loses the most, because every trade pays the cost.
- What the gate does with this: it skips every live signal from these setups. The scanner still follows each signal on paper (the shadow book), so if a setup starts to work in new data the record will show it.
