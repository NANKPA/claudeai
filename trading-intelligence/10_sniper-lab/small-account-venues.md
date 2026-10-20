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
