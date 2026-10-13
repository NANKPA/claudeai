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
    hypothesis="1h: price reaches the prior-day high this session.",
    invalidation="A 5m close back below the sweep low.",
    explanation="Stops below an obvious low supply liquidity to larger buyers.",
    undermined_by="A trend day down with no reclaim.",
    required_conditions=["sweep", "reclaim", "htf_uptrend"],
    conditions_present={"sweep": True, "reclaim": True, "htf_uptrend": True},
)
# The setup's OWN out-of-sample / forward / live record. Never someone else's claims.
setup = SetupRecord(setup_id="nq-sweep-v1", results_r=past_net_r_multiples)
account = AccountState(equity=25_000, point_value=2.0, base_risk_pct=0.5,
                       emotional_state="calm", realized_today_r=-1.0)

decision = gate.evaluate(proposal, setup, account)
journal.record_decision(decision)                # the reasoning is saved BEFORE the order (Section XVI)
print(decision.explain())
if decision.action == "take":
    place_order(size=decision.position_size, stop=proposal.stop, target=proposal.target)   # your broker code
# ... after the exit:
journal.record_outcome(decision.journal_row["trade_id"], executed_per_plan="y", exit_reason="target",
                       result_r=2.9, cost_r=0.05, outcome_within_expected="y")
```

What the gate enforces (from `trading-intelligence/00_philosophy/decision-protocol.md`):

| Gate | Rule | Principle |
|---|---|---|
| 0 | Red emotional state → skip. Amber → half risk. Pause after a loss. Daily (3R), weekly (5R), 3-in-a-row and 20%-drawdown breakers. | P10, P12, P9 |
| 1–2 | Observation, interpretation and hypothesis written separately. A real explanation. Invalidation written before entry. Stop and target on the right side. | P1, P2, P3 |
| 3 | Every required condition of the setup present. A price-vs-value gap alone is not evidence. | P4 |
| 4 | Own out-of-sample record: n ≥ 30 and mean − 1 SE > 0 for a 2. Any 0 → skip; any 1 → wait. | P1, P5, P6 |
| 5 | This trade's EV after its own costs, with the average win capped at the target, must be > 0. | P5 |
| 6 | Fixed-fractional size: full base risk only when mean − 2 SE > 0, otherwise half. ¼ Kelly from the conservative win rate as a ceiling. Heat ≤ 2%. Rounded down. | P9 |

Run the tests: `python -m pytest -q trading_intelligence/tests tools/philosophy/tests`.
