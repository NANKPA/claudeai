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
