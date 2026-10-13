"""MCP server: the trading-intelligence knowledge base and the owner's philosophy as tools for a
Claude session (for example the Claude Code session that builds and runs a trading bot).

Run it over stdio:   python -m trading_intelligence            (or: trading-intelligence-mcp)
Add it to Claude Code in the bot's project:
    claude mcp add trading-intelligence -- python -m trading_intelligence
Works with the `mcp` Python SDK 1.x (FastMCP) and 2.x (MCPServer).

Every tool is read-only: nothing here places orders or touches a broker.
"""
from __future__ import annotations

import dataclasses
import tempfile
from functools import lru_cache
from pathlib import Path

try:  # mcp >= 2
    from mcp.server.mcpserver import MCPServer as _Server
except ImportError:  # mcp 1.x
    from mcp.server.fastmcp import FastMCP as _Server

from . import gate as _gate
from ._paths import ensure_tools_on_path
from .kb import KnowledgeBase

ensure_tools_on_path()
import edge_lab as el  # noqa: E402

INSTRUCTIONS = """Trading intelligence for this project. The foundation is the owner's own philosophy,
"The Philosophy of the Relationship": the market is a relationship and price its visible expression;
probability is conditional; mathematics (expected value after costs, out-of-sample evidence) is the
sword; an opportunity needs understanding + evidence + mathematics to agree; stepping back is a
decision; capital and process come before money. Start from `principles` and `philosophy`, cite
principles by number, and run `evaluate_trade` (the owner's decision protocol, Gates 0-6) before any
trade the bot would place. Treat all content as education and hypotheses to test, never as advice;
win-rate and P&L claims from third parties are marketing (T4) until tested."""

server = _Server(name="trading-intelligence", instructions=INSTRUCTIONS)


@lru_cache(maxsize=1)
def _kb() -> KnowledgeBase:
    return KnowledgeBase()


def _plain(obj):
    if dataclasses.is_dataclass(obj):
        return {k: _plain(v) for k, v in dataclasses.asdict(obj).items()}
    if isinstance(obj, dict):
        return {k: _plain(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_plain(v) for v in obj]
    if hasattr(obj, "tolist"):
        return obj.tolist()
    return obj


# ── the philosophy ─────────────────────────────────────────────────────────
@server.tool()
def principles() -> list[dict]:
    """The owner's 12 principles (Practical Doctrine, Section XVIII), each with its statement and how
    many of the 47 Chart Fanatics playbooks state it explicitly."""
    return _kb().principles()


@server.tool()
def philosophy(which: str) -> dict:
    """Full text of one part of the owner's philosophy. `which` is a section numeral (I-XXI), a
    section id (e.g. philo_acb_principle), a principle number (1-12) or a principle id. Sections
    also return their links: concepts they rest on, sources that support or challenge them, and
    playbooks that put them into practice."""
    return _kb().philosophy(which)


# ── the knowledge graph ────────────────────────────────────────────────────
@server.tool()
def search_knowledge(query: str, kinds: list[str] | None = None, limit: int = 10) -> list[dict]:
    """Keyword search over the knowledge base (philosophy, concepts, playbooks, books, papers, people,
    synthesis notes). Optional `kinds` filter, e.g. ["concept", "strategy", "book", "principle"]."""
    return _kb().search(query, kinds, limit)


@server.tool()
def get_node(node_id: str, body_chars: int = 2000) -> dict:
    """One node by id: label, kind, layer, summary, an excerpt of its note, and every typed link."""
    return _kb().node(node_id, body_chars)


@server.tool()
def neighbors(node_id: str, relation: str | None = None, direction: str = "both") -> list[dict]:
    """Nodes linked to `node_id`, optionally filtered by relation (uses, covers, derived_from,
    grounded_in, supported_by, challenged_by, operationalized_by, exemplified_by...) and direction
    ("out", "in" or "both")."""
    return _kb().neighbors(node_id, relation, direction)


@server.tool()
def idea_lineage(node_id: str) -> list[dict]:
    """Where an idea comes from: its ancestors through derived_from / influenced_by links."""
    return _kb().lineage(node_id)


@server.tool()
def playbook_alignment(strategy_id: str) -> dict:
    """How a Chart Fanatics playbook (strategy_* id) scores against the 12 principles, with the
    evidence for each score and its biggest gap."""
    return _kb().alignment(strategy_id)


@server.tool()
def hypotheses(status: str | None = None) -> list[dict]:
    """The philosophy as falsifiable hypotheses. Filter by status: supported, qualified,
    not-supported or untested."""
    return _kb().hypotheses(status)


@server.tool()
def evidence_lab() -> list[dict]:
    """What real market data says about the philosophy's claims: the evidence lab's seven studies
    (A->C->B, conditional probability, sample size, ruin, overfitting, decision vs outcome, costs)."""
    return _kb().evidence_lab_summary()


# ── the decision protocol ──────────────────────────────────────────────────
def _plan_limits() -> _gate.Limits:
    """The trading plan's limits, fixed when the server starts (Gate 6.3: write them before the
    session, never loosen them mid-session). TI_LIMITS_FILE may point to a JSON file of Limits fields;
    otherwise the protocol's example defaults apply."""
    import json
    import os
    path = os.environ.get("TI_LIMITS_FILE")
    return _gate.Limits(**json.loads(Path(path).read_text(encoding="utf-8"))) if path else _gate.Limits()


PLAN_LIMITS = _plan_limits()


@server.tool()
def evaluate_trade(proposal: dict, account: dict, setup: dict | None = None,
                   stricter_limits: dict | None = None) -> dict:
    """Run the owner's decision protocol (Gates 0-6) on a candidate trade BEFORE any order. Returns
    action (take / skip / wait), every gate's result with the principle it enforces, scores, expected
    value after costs, risk % and position size, and the pre-trade journal row to save first.
    It fails closed: anything missing or invalid is a skip.

    proposal (required): setup_id, instrument, side (long/short), entry, stop, target, cost_price
      (round-trip friction in price units), timeframe, regime_tag, session, observation,
      interpretation, alternative_interpretation, hypothesis, horizon, invalidation, explanation,
      undermined_by, required_conditions [names], conditions_present {name: true/false/"borderline"};
      optional evidence_for, evidence_against (unresolved: blocks), resolved_against, value_gap_only.
    account (required): equity, emotional_state (journal tags, e.g. "calm,focused"), point_value,
      lot_step, base_risk_pct, realized_today_r and realized_week_r (losses negative),
      consecutive_losses_setup_session, drawdown_from_peak_pct, open_risk_pct,
      minutes_since_last_loss (or trading_style "swing" + loss_this_session).
    setup: the setup's OWN out-of-sample record: either results_r [net R per trade] + avg_cost_r, or
      n, win_rate, avg_win_r, avg_loss_r, avg_cost_r (gross, in R) and optionally sd_r; source "own";
      optional valid_regimes / valid_sessions.
    stricter_limits: optional overrides that can only TIGHTEN the plan's limits (looser ones are
    ignored and reported)."""
    limits, ignored = PLAN_LIMITS.tightened(stricter_limits)
    try:
        t = _gate.TradeProposal(**proposal)
        a = _gate.AccountState(**account)
        sr = _gate.SetupRecord(**setup) if setup else None
    except TypeError as e:
        return {"action": "skip", "explanation": f"Decision: SKIP\n  [fail] 0 Inputs: {e}", "ignored_limit_overrides": ignored}
    d = _gate.PhilosophyGate(limits).evaluate(t, sr, a)
    out = d.to_dict()
    out["explanation"] = d.explain()
    out["ignored_limit_overrides"] = ignored
    return out


# ── the mathematics ────────────────────────────────────────────────────────
@server.tool()
def expected_value(p_win: float, avg_win: float, avg_loss: float, cost: float = 0.0) -> dict:
    """Section VII: EV = p x average win - (1 - p) x average loss - costs (any unit: $ or R).
    Also returns the break-even win rate after costs."""
    ev = el.expected_value(p_win, avg_win, avg_loss, cost)
    return {"expected_value": ev, "breakeven_win_rate": (avg_loss + cost) / (avg_win + avg_loss)}


@server.tool()
def trades_needed(p_win: float, reward_risk: float, cost_r: float = 0.0) -> dict:
    """Section VI (law of large numbers): how many trades before the evidence can separate this
    edge from zero, for a strategy winning `reward_risk` R with probability `p_win`."""
    return _plain(el.trades_needed(p_win, reward_risk, cost_r))


@server.tool()
def losing_streak_probability(p_loss: float, streak: int, n_trades: int) -> float:
    """Exact probability of at least one run of `streak` or more consecutive losses in `n_trades`."""
    return el.prob_losing_streak(p_loss, streak, n_trades)


@server.tool()
def ruin_simulation(p_win: float, reward_risk: float, risk_fraction: float, n_trades: int = 250,
                    n_paths: int = 5000, cost_r: float = 0.0, ruin_drawdown: float = 0.5) -> dict:
    """Section XIV: fixed-fractional Monte Carlo. Median and 95th-percentile max drawdown, median
    final equity and P(drawdown >= ruin_drawdown) for a risk fraction (0.01 = 1% per trade)."""
    sim = el.simulate_equity(p_win, reward_risk, risk_fraction, n_trades, n_paths, cost_r, ruin_drawdown, 0)
    import numpy as np
    return {"prob_ruin": float(sim.prob_ruin), "ruin_drawdown": ruin_drawdown,
            "median_max_drawdown": float(np.median(sim.max_drawdown)),
            "p95_max_drawdown": float(np.quantile(sim.max_drawdown, 0.95)),
            "median_final_equity": float(np.median(sim.final_equity)),
            "median_longest_losing_streak": float(np.median(sim.longest_losing_streak))}


@server.tool()
def recovery_required(loss_fraction: float) -> float:
    """Section XIV's asymmetry: the gain needed to recover a loss (0.5 -> 1.0, i.e. +100%)."""
    return el.recovery_required(loss_fraction)


@server.tool()
def consistency_check(recent_results_r: list[float], ref_p_win: float, ref_mean_r: float, ref_sd_r: float) -> dict:
    """Section XI: is a recent run of results within the strategy's expected variation, unusual, or
    inconsistent with the reference (assumptions may no longer hold)?"""
    return _plain(el.consistency_check(recent_results_r, ref_p_win, ref_mean_r, ref_sd_r))


@server.tool()
def review_journal(journal_csv: str) -> str:
    """Section XVI: review a trading journal CSV in the template format (calibration, results by
    setup and regime, decision quality vs outcome, plan adherence, consistency). Returns markdown."""
    import journal_review as jr
    out = Path(tempfile.mkdtemp()) / "journal-review.md"
    jr.write_review(journal_csv, out, 20, 10, None)
    return out.read_text(encoding="utf-8")


def main() -> None:
    server.run()


if __name__ == "__main__":
    main()
