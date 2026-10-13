"""Trading intelligence for a trading bot, built on the owner's "Philosophy of the Relationship".

    from trading_intelligence import PhilosophyGate, TradeProposal, SetupRecord, AccountState, Journal

    decision = PhilosophyGate().evaluate(proposal, setup_record, account)   # Gates 0-6 of the protocol
    Journal("journal.csv").record_decision(decision)                         # BEFORE any order
    if decision.action == "take":
        ...  # the bot places decision.position_size, with the stop it proposed

    from trading_intelligence import KnowledgeBase
    kb = KnowledgeBase(); kb.principles(); kb.search("liquidity sweep"); kb.philosophy("III")

Education and decision support, not financial advice. Nothing in this package places orders.
"""
from .gate import (AccountState, Decision, GateResult, JOURNAL_COLUMNS, Limits, PhilosophyGate,
                   SetupRecord, TradeProposal, emotion_colour)
from .journal import Journal


def __getattr__(name):  # the knowledge base loads lazily (it reads ~1,000 notes)
    if name == "KnowledgeBase":
        from .kb import KnowledgeBase
        return KnowledgeBase
    raise AttributeError(name)


__all__ = ["AccountState", "Decision", "GateResult", "JOURNAL_COLUMNS", "Journal", "KnowledgeBase", "Limits",
           "PhilosophyGate", "SetupRecord", "TradeProposal", "emotion_colour"]
__version__ = "1.0.0"
