# Plug the trading intelligence into a trading bot

**Address:** https://github.com/NANKPA/claudeai (public; the default branch holds everything)

The bot gets two things:

1. **For the bot's Claude session:** an MCP server with 17 read-only tools. They cover your
   philosophy and its 12 principles, the knowledge graph (concepts, 47 playbooks, books, people,
   idea lineage), the evidence lab, the hypotheses, the decision protocol (`evaluate_trade`), and the
   maths: expected value, trades needed, losing streaks, ruin, recovery, consistency, journal review.
2. **For the bot's code:** a Python package. It provides `PhilosophyGate`, which runs your decision
   protocol (Gates 0-6) before every order and returns take / skip / wait with the principle behind
   each reason, plus the size. It also provides `Journal`, an append-only journal in your template
   format, and `KnowledgeBase` for queries.

Nothing in it places orders or touches a broker. It is decision support and education, not advice.

## Option A: paste this into the bot's Claude session (easiest)

> Install the trading intelligence from https://github.com/NANKPA/claudeai and connect it to this
> project:
> 1. `python -m pip install "trading-intelligence[mcp] @ git+https://github.com/NANKPA/claudeai.git"`
> 2. `claude mcp add trading-intelligence -- python -m trading_intelligence`, then restart the session
>    so the tools load. The first run downloads the knowledge base into ~/.cache/trading-intelligence.
> 3. Call the `principles` tool and read BOT_INTEGRATION.md in that repository. Then wire
>    `trading_intelligence.PhilosophyGate` into the bot so that every order first goes through
>    `evaluate_trade` / `PhilosophyGate.evaluate`. Before the order is sent, record the decision with
>    `trading_intelligence.Journal(...).record_decision(decision)`. Only place an order when
>    `decision.action == "take"`, at `decision.position_size`, with the proposal's stop.
> 4. Paper-trade only until each setup's own out-of-sample record passes the gate.

Use the same `python` for both commands: the one the bot runs with (its virtual environment, if it
has one).

## Option B: work on a local clone

```bash
git clone https://github.com/NANKPA/claudeai.git
python -m pip install -e "./claudeai[mcp]"
claude mcp add trading-intelligence -- python -m trading_intelligence
```

An editable install reads the knowledge base from the clone, so `git pull` updates it. To use a
clone from a different install, set `TI_ROOT=/path/to/claudeai`.

## In the bot's code

```python
from trading_intelligence import PhilosophyGate, TradeProposal, SetupRecord, AccountState, Journal

journal = Journal("journal.csv")                 # 00_philosophy/journal-template.csv columns
gate = PhilosophyGate()                          # Limits() holds the Gate 6.3 example defaults; set your own

proposal = TradeProposal(
    setup_id="nq-sweep-v1", instrument="MNQ", side="long",
    entry=18402.0, stop=18392.0, target=18432.0, cost_price=0.5,            # cost = spread + fees + slippage
    timeframe="1h/5m", regime_tag="trend_low_vol", session="ny_am",
    observation="Price traded 6 points below the prior-day low and closed back above it.",
    interpretation="Sell stops under the low were absorbed.",
    alternative_interpretation="A stop run inside a developing down day.",
    hypothesis="1h: price reaches the prior-day high this session.",
    horizon="by the New York close",
    invalidation="A 5m close back below the sweep low.",
    explanation="Stops below an obvious low supply liquidity to larger buyers.",
    undermined_by="A trend day down with no reclaim.",
    required_conditions=["sweep", "reclaim", "htf_uptrend"],
    conditions_present={"sweep": True, "reclaim": True, "htf_uptrend": True},
)
# The setup's OWN out-of-sample / forward / live record. Never someone else's claims.
setup = SetupRecord(setup_id="nq-sweep-v1", results_r=past_net_r_multiples)
account = AccountState(equity=25_000, point_value=2.0, base_risk_pct=0.5, emotional_state="calm,focused",
                       realized_today_r=-1.0, minutes_since_last_loss=40)

decision = gate.evaluate(proposal, setup, account)
journal.record_decision(decision)                # the reasoning is saved BEFORE the order (Section XVI)
print(decision.explain())
if decision.action == "take":
    place_order(size=decision.position_size, stop=proposal.stop, target=proposal.target)   # your broker code
# ... after the exit:
journal.record_outcome(decision.journal_row["trade_id"], executed_per_plan="y", exit_reason="target",
                       result_r=2.9, cost_r=0.05, outcome_within_expected="y")
```

**It fails closed.** A missing, non-finite, negative or ambiguous input (no `cost_price`, no
`emotional_state`, regime `unclear`, NaN anywhere, a signed loss, a bad side) is a `skip` with a
"0 Inputs" reason and a journal row. It never raises, and it never returns `take`. Sign
conventions: prices and costs are positive; `realized_today_r` and `realized_week_r` are signed
(losses negative); `drawdown_from_peak_pct` is a magnitude; `open_risk_pct` ≥ 0.

**Limits come from your plan.** Build `Limits(...)` once from your trading plan. The protocol's own
floors are enforced: n ≥ 30, Kelly fraction ≤ ½, EV floor ≥ 0. For the MCP server, put the plan in a
JSON file and set `TI_LIMITS_FILE`. A per-call `stricter_limits` can only tighten it; looser values
are ignored and reported.

What the gate enforces (from `trading-intelligence/00_philosophy/decision-protocol.md`):

| Gate | Rule | Principle |
|---|---|---|
| 0 | Red emotional state (incl. fomo, revenge, greed, excitement) → skip. Amber → half the final risk. State not recorded → skip. Daily (3R), weekly (5R), 3-in-a-row and 20%-drawdown breakers come first, then the pause after a loss (15 min intraday, next session for swing). | P10, P12, P9 |
| 1–2 | Observation, interpretation, alternative interpretation and hypothesis written separately. A real explanation. Level (timeframe) and horizon named. Invalidation written before entry. Stop and target on the right side. | P1, P2, P3 |
| 3 | Regime and session tagged and not "unclear". Every required condition present, and today's regime/session among those the record was measured in. Unresolved arguments against → wait. A price-vs-value gap alone is not evidence. | P4, P6 |
| 4 | Own out-of-sample record: n ≥ 30 and mean − 1 SE > 0 for a 2. Any 0 → skip; any 1 → wait. | P1, P5, P6 |
| 5 | `cost_price` required. This trade's EV, using gross win and loss with the win capped at the target, minus this trade's own cost in R, must be > 0. | P5 |
| 6 | Fixed-fractional size: full base risk only when mean − 2 SE > 0, otherwise half. ¼ Kelly from the conservative win rate as a ceiling. Heat ≤ 2%. Rounded down. A leverage cap cuts the size (less risk); an order below the venue's minimum (`min_order_notional`) is a skip. | P9 |

Run the tests: `python -m pytest -q trading_intelligence/tests tools/philosophy/tests`.

## The sniper engine: scan, gate, paper-trade

The package also contains a scanner that finds the setups by itself and runs each one through the gate
(`trading_intelligence/sniper`, results in `trading-intelligence/10_sniper-lab/`):

```bash
python -m trading_intelligence.sniper size --equity 20 --risk-pct 1        # any account size: cost in R per venue
python -m trading_intelligence.sniper scan --equity 20 --risk-pct 1 --fees low --min-notional 1   # crypto, loops
python -m trading_intelligence.sniper scan --venue csv --csv-dir ~/bot/candles --symbols EURUSD XAUUSD \
       --timeframes 1h 4h --fees fx_raw --lot-step 10 --min-notional 11.5 --max-leverage 30       # forex / gold
python -m trading_intelligence.sniper scan --report                        # forward (shadow) and account results
```

- Every signal is journaled (`~/.trading-intelligence/sniper-paper/journal.csv`, the owner's template) with
  the gate's decision and reasons. Every signal is also followed on paper with the backtest's fill rules
  (`forward.csv`): that forward record is added to the setup's evidence, so a setup that starts working
  in new data can earn its way through Gate 4.
- Only gate **takes** reach the paper account (`account.csv`), sized by Gate 6 for your equity.
- For forex and gold, have your bot write its broker's closed candles to `<csv-dir>/<SYMBOL>_<tf>.csv`
  (`time,open,high,low,close,volume`, time = bar open in UTC) and use `--venue csv`: the forward record
  then comes from the prices you actually trade. Yahoo has forex pairs but no spot gold.
- Records chosen out of many backtests are **provisional**: a take is handed to `--on-take` only when
  the gate also says take on the setup's forward trades alone (see `10_sniper-lab/backtest-report.md`).
- Gate 0 reads your state from `~/.trading-intelligence/sniper-paper/state.txt` on every pass: write
  `tired` and risk halves, `frustrated` and it stands aside.
- **To trade for real**, pass `--on-take "python my_bot_order.py"`: the scanner calls your own order code
  with the trade as JSON on stdin, only for gate takes, after the journal row is written. Broker keys
  stay in your bot, on your machine, never in this repo.
- Run the scanner with `--once` from cron or Task Scheduler instead of the loop if you prefer.

