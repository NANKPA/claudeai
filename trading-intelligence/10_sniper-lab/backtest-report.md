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

> Generated 2026-10-20 by `python -m trading_intelligence.sniper lab`. Markets: BTCUSDT, ETHUSDT, EURUSD, GBPUSD, SOLUSDT, USDJPY, XAUUSD (crypto: Binance spot archive; forex and gold: Dukascopy BID candles). Timeframes: 5m, 15m, 1h, 4h. Period 2022-01 to last full month. Rules and the allowed regimes/sessions are chosen on data before 2024-01-01 and judged only on data after it. Fills are conservative (a limit fills only when price trades at or through it; when stop and target share a bar the stop counts). Education and research, not a trading signal.

## Cost levels (per side, fraction of price)

| Level | Market | Resting limit | Market order / stop | Extra slippage on stops |
|---|---|---|---|---|
| std | crypto | 0.0800% | 0.1000% | 0.0200% |
| low | crypto | 0.0000% | 0.0500% | 0.0100% |
| ultra | crypto | 0.0000% | 0.0200% | 0.0100% |
| fx_std | fx | 0.0000% | 0.0000% | 0.0020% |
| fx_raw | fx | 0.0032% | 0.0032% | 0.0010% |

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

IS = in-sample (before the split), OOS = out-of-sample. The candles are bid prices and every buy pays the ask, so **gross R is already after the spread**; the cost column is commission plus slippage only. fx_std = spread-only account (about 1.3 pips), fx_raw = raw spread (about 0.15 pip) plus commission.

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
| sniper_ob_mean_threshold | 15m | ultra | range_high_vol | late | 4 | +2.635 | 4 | +0.754 | 0.40 | 0.40 |
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

Passing Gate 4 is necessary, not sufficient. These were chosen out of every configuration tried, using the same out-of-sample years that now make them look good; the multiple-testing result below says whether that choice could be luck.

**They do not survive it, so every record is marked provisional.** The scanner paper-trades them through the gate as usual, but it hands a take to the owner's own order code (`--on-take`) only when that setup's FORWARD trades alone (signals after the lab's data ended) pass Gate 4 by themselves. Those trades played no part in choosing the setup, so they are the clean test.

## Multiple testing

128 configurations were tried; 12 had at least 30 effectively independent out-of-sample trades inside their chosen conditions. The best of those (`trend_donchian_breakout@4h@fx_std`, per-trade Sharpe +0.178 over 112 trades) has a deflated-Sharpe probability of 0.24 of being real once the number of trials is counted (Bailey & López de Prado; 0.95 is the usual bar).

## Reading this as the owner's philosophy asks

- **Crypto.** Best out-of-sample average before costs: +0.064R per trade (trend_donchian_breakout 15m). 0 of 84 configurations are positive after costs out-of-sample (before the in-sample condition filter).
- **Forex and gold.** Best out-of-sample average before costs: +0.316R per trade (sniper_ob_mean_threshold 4h). 7 of 44 configurations are positive after costs out-of-sample (before the in-sample condition filter).
- A pattern that does not pay before costs cannot be rescued by a cheaper venue; cheaper costs only shrink the loss (Section VII: expected value first).
- Cost in R = round-trip cost / stop distance. A 5-minute crypto stop of 0.2-0.3% against a 0.2% round trip costs most of 1R; the same stop in EUR/USD against a 0.01% round trip costs a few hundredths (Gate 5.6).
- More trades is not more edge: every trade pays the cost, so frequency multiplies a negative expectancy.
- Only the out-of-sample columns are evidence; in-sample numbers chose the conditions (Section XVII).
