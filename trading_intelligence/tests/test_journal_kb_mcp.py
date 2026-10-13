"""Journal append-only rules, knowledge-base queries and the MCP server's tool surface."""
import asyncio
import sys

import pytest

from trading_intelligence import Journal, JOURNAL_COLUMNS, PhilosophyGate
from trading_intelligence.tests.test_gate import GOOD_SETUP, account, proposal
from trading_intelligence import SetupRecord


def _decision(trade_id="T1"):
    return PhilosophyGate().evaluate(proposal(trade_id=trade_id), SetupRecord(**GOOD_SETUP), account())


def test_journal_append_freeze_and_review(tmp_path):
    j = Journal(tmp_path / "journal.csv")
    assert j.record_decision(_decision("T1")) == "T1"
    j.record_decision(_decision("T2"))
    with pytest.raises(ValueError):
        j.record_decision(_decision("T1"))                     # a new decision needs a new row
    with pytest.raises(ValueError):
        j.record_outcome("T1", hypothesis="rewritten after the fact")   # pre-trade fields are frozen
    row = j.record_outcome("T1", executed_per_plan="y", exit_reason="target", result_r=2.0, cost_r=0.05,
                           outcome_within_expected="y", lesson="followed the plan")
    assert str(row["result_r"]) == "2.0" and row["hypothesis"].startswith("1h:")
    rows = j.rows()
    assert [r["trade_id"] for r in rows] == ["T1", "T2"] and rows[1]["result_r"] == ""
    header = (tmp_path / "journal.csv").read_text().splitlines()[0].split(",")
    assert tuple(header) == JOURNAL_COLUMNS
    from trading_intelligence._paths import ensure_tools_on_path
    ensure_tools_on_path()
    import journal_review
    out = journal_review.write_review(str(tmp_path / "journal.csv"), tmp_path / "review.md", 20, 10, None)
    assert "decision" in out.read_text().lower()


def test_journal_rejects_foreign_csv(tmp_path):
    p = tmp_path / "other.csv"
    p.write_text("a,b\n1,2\n")
    with pytest.raises(ValueError):
        Journal(p)


@pytest.fixture(scope="module")
def kb():
    from trading_intelligence import KnowledgeBase
    return KnowledgeBase()


def test_principles_are_the_owners_words(kb):
    ps = kb.principles()
    assert [p["number"] for p in ps] == list(range(1, 13))
    assert ps[0]["statement"].startswith("Do not enter a trade merely because the price is moving")
    assert all(p["statement"] for p in ps)


def test_philosophy_lookup(kb):
    s = kb.philosophy("III")
    assert s["id"] == "philo_acb_principle" and "A → C → B" in s["text"] and s["links"]["grounded_in"]
    assert kb.philosophy("5")["id"] == "principle_05_mathematical_justification"
    with pytest.raises(KeyError):
        kb.philosophy("XXV")


def test_search_node_lineage_alignment(kb):
    hits = kb.search("expected value costs", limit=5)
    assert hits and all("id" in h for h in hits)
    n = kb.node("philosophy_relationship")
    assert n["kind"] == "philosophy" and n["links"]
    assert kb.lineage("concept_smart_money_concepts")[0]["id"] == "concept_smart_money_concepts"
    a = kb.alignment("strategy_matteo_conti_institutional")
    assert len(a["scores"]) == 12 and 0 <= a["total"] <= 24
    assert len(kb.evidence_lab_summary()) == 7
    assert {h["status"] for h in kb.hypotheses()} <= {"supported", "qualified", "not-supported", "untested"}


def test_mcp_server_tools():
    pytest.importorskip("mcp")
    from trading_intelligence import mcp_server as m
    names = {t.name for t in asyncio.run(m.server.list_tools())}
    expected = {"principles", "philosophy", "search_knowledge", "get_node", "neighbors", "idea_lineage",
                "playbook_alignment", "hypotheses", "evidence_lab", "evaluate_trade", "expected_value",
                "trades_needed", "losing_streak_probability", "ruin_simulation", "recovery_required",
                "consistency_check", "review_journal"}
    assert expected <= names
    assert m.expected_value(0.6, 100, 120, 5)["expected_value"] == pytest.approx(7.0)   # Section VII's $7
    out = m.evaluate_trade(
        proposal={k: v for k, v in proposal().__dict__.items()},
        account={"equity": 10_000, "emotional_state": "calm"}, setup=GOOD_SETUP)
    assert out["action"] == "take" and "Decision: TAKE" in out["explanation"]
