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

128 configurations: 14 setups × markets × timeframes × cost levels. The setups were chosen and filtered on
2022–2023 and judged on 2024 to September 2026. Coverage:

- **Crypto:** BTC, ETH and SOL on 5m, and BTC and ETH on 15m, at three fee levels (0.08/0.10%, 0/0.05%
  and 0/0.02%). The owner stopped the crypto run at that point. BNB, XRP and the 1h/4h crypto
  timeframes were not run.
- **Forex and gold:** EUR/USD, GBP/USD, USD/JPY and XAU/USD on 1h and 4h, at two account types:
  spread-only at about 1.3 pips, and raw spread at about 0.15 pip plus commission. Intraday forex
  (5m/15m) needs minute history, and the free archive throttles cloud servers, so run it at home
  (HANDOFF.md).

| | Crypto | Forex and gold |
|---|---|---|
| Configurations positive after costs, out of sample | **0 of 84** | 7 of 44 |
| Typical result before costs (median, R per trade) | −0.01 | −0.07 |
| Typical cost (median, R per trade) | 0.32 | 0.03 (plus the spread, paid in the prices) |
| Pass Gate 4 inside the conditions chosen in-sample | none | 3: Donchian trend 4h (both account types, +0.31R per trade over 112 trades) and VWAP reversion 1h (raw spread, +0.25R over 123) |

**Read the three survivors with care.** With 128 configurations tried, the best one has a
deflated-Sharpe probability of 0.24 of being real (0.95 is the bar). So the lab marks every record
*provisional*. The scanner paper-trades these setups through the gate, but hands a trade to your bot's
order code only when the setup's **forward** trades alone pass Gate 4. Forward trades are the signals
after the lab's data ends, so they played no part in choosing the setup.

What it means for the owner's question:

- **Precise 5-minute crypto entries do not pay at any fee level found.** Before costs they average
  about zero. After costs they lose, because a 0.2–0.3% stop makes even a 0.02% fee a real share of 1R.
- **Wider stops and cheap spreads are where anything survives.** That means 1h and 4h forex and gold,
  on a raw-spread or cent account. There the cost is a few hundredths of 1R.
- **"Trading every day" and "having an edge" pull against each other.** The survivors trade about 3–4
  times a month across four markets. The busy setups trade 10–50 times a day and lose the most.

## The engine (in the `trading_intelligence` package)

```
pip install "trading-intelligence[mcp] @ git+https://github.com/NANKPA/claudeai.git"

python -m trading_intelligence.sniper size --equity 20 --risk-pct 1      # what a stop costs, venue by venue
python -m trading_intelligence.sniper scan --fees low --min-notional 1   # live crypto scan, paper only
python -m trading_intelligence.sniper scan --venue yahoo --symbols EURUSD GBPUSD USDJPY XAUUSD \
       --timeframes 1h 4h --fees fx_raw --lot-step 10 --min-notional 11.5 --max-leverage 30   # forex/gold
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
