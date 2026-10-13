"""Every path through the decision protocol (Gates 0-6), checked against decision-protocol.md."""
import math

import pytest

from trading_intelligence import AccountState, Limits, PhilosophyGate, SetupRecord, TradeProposal

GOOD_SETUP = dict(setup_id="sweep-v1", n=200, win_rate=0.45, avg_win_r=2.0, avg_loss_r=1.0, avg_cost_r=0.05)


def proposal(**kw):
    base = dict(setup_id="sweep-v1", instrument="TEST", side="long", entry=100.0, stop=98.0, target=104.0,
                cost_price=0.1, timeframe="1h/5m", regime_tag="trend_low_vol", session="ny_am",
                observation="Price traded below the prior-day low and closed back above it.",
                interpretation="Sell stops below the low were absorbed.",
                hypothesis="1h: price reaches the prior-day high within the session.",
                invalidation="A 5m close below the sweep low.",
                explanation="Stops below an obvious low supply liquidity to larger buyers.",
                undermined_by="A trend day down with no reclaim.",
                required_conditions=["sweep", "reclaim", "htf_uptrend"],
                conditions_present={"sweep": True, "reclaim": True, "htf_uptrend": True})
    base.update(kw)
    return TradeProposal(**base)


def account(**kw):
    base = dict(equity=10_000.0, point_value=1.0, base_risk_pct=0.5, emotional_state="calm,focused")
    base.update(kw)
    return AccountState(**base)


def run(p=None, s=None, a=None, limits=None):
    return PhilosophyGate(limits).evaluate(p or proposal(), SetupRecord(**(s or GOOD_SETUP)) if s is not False else None,
                                           a or account())


def test_take_path_sizes_by_fixed_fraction():
    d = run()
    assert d.action == "take", d.explain()
    assert (d.understanding_score, d.evidence_score, d.math_score) == (2, 2, 2)
    assert d.est_ev_r == pytest.approx(0.45 * 2 - 0.55 * 1 - 0.05, abs=1e-3)
    assert d.position_size == 25 and d.risk_pct == pytest.approx(0.5)
    assert d.journal_row["decision"] == "take" and d.journal_row["risk_pct"] == pytest.approx(0.5)


def test_short_geometry():
    d = run(proposal(side="short", entry=100, stop=102, target=96))
    assert d.action == "take" and d.position_size == 25


@pytest.mark.parametrize("state", ["frustrated", "revenge", "calm,fomo"])
def test_red_state_steps_back(state):
    assert run(a=account(emotional_state=state)).action == "skip"


def test_amber_halves_risk_and_rounds_down():
    d = run(a=account(emotional_state="tired"))
    assert d.action == "take" and d.position_size == 12 and d.risk_pct == pytest.approx(0.24)


def test_amber_can_step_back_and_unrecorded_state_skips():
    assert run(a=account(emotional_state="anxious", step_back_when_amber=True)).action == "skip"
    assert run(a=account(emotional_state="")).action == "skip"


def test_after_loss_pause_waits():
    assert run(a=account(minutes_since_last_loss=5)).action == "wait"
    assert run(a=account(minutes_since_last_loss=30)).action == "take"


@pytest.mark.parametrize("kw", [dict(realized_today_r=-3.0), dict(realized_week_r=-5.5),
                                dict(consecutive_losses_setup_session=3), dict(drawdown_from_peak_pct=20.0)])
def test_circuit_breakers_skip(kw):
    assert run(a=account(**kw)).action == "skip"


def test_drawdown_halves_base_risk():
    d = run(a=account(drawdown_from_peak_pct=12.0))
    assert d.action == "take" and d.risk_pct == pytest.approx(0.24)


def test_no_invalidation_or_wrong_side_skips():
    assert run(proposal(invalidation="")).action == "skip"
    assert run(proposal(stop=101.0)).action == "skip"          # stop above a long entry
    assert run(proposal(target=99.0)).action == "skip"


def test_ladder_and_explanation():
    assert run(proposal(explanation="")).action == "skip"       # "it is moving" is not an explanation
    assert run(proposal(interpretation="")).action == "skip"
    d = run(proposal(undermined_by=""))
    assert d.understanding_score == 1 and d.action == "wait"


def test_conditions():
    assert run(proposal(conditions_present={"sweep": True, "reclaim": False, "htf_uptrend": True})).action == "skip"
    assert run(proposal(required_conditions=[])).action == "skip"
    assert run(proposal(value_gap_only=True)).action == "skip"
    d = run(proposal(conditions_present={"sweep": True, "reclaim": "borderline", "htf_uptrend": True}))
    assert d.evidence_score == 1 and d.action == "wait"
    assert run(proposal(evidence_against=["CPI in 10 minutes"])).action == "wait"


def test_record_rules():
    assert run(s=False).action == "skip"                                       # no record
    assert run(s={**GOOD_SETUP, "source": "claimed"}).action == "skip"         # T4
    assert run(s={**GOOD_SETUP, "out_of_sample": False}).action == "skip"     # in-sample
    assert run(s={**GOOD_SETUP, "win_rate": 0.30}).action == "skip"           # negative expectancy
    d = run(s={**GOOD_SETUP, "n": 20})
    assert d.math_score == 1 and d.action == "wait"                            # anecdote


def test_trade_costs_can_kill_the_edge():
    d = run(proposal(cost_price=1.0))       # 0.5R of friction on a 2-point stop
    assert d.action == "skip" and d.est_ev_r < 0 and d.math_score == 0


def test_target_caps_the_average_win():
    d = run(proposal(target=101.0))         # 0.5R of room: EV = .45*.5 - .55 - .05 < 0
    assert d.action == "skip"


def test_evidence_scaled_risk():
    # n = 60: mean - 1 SE > 0 but mean - 2 SE <= 0 -> half base risk
    s = {**GOOD_SETUP, "n": 60}
    se = 3.0 * math.sqrt(0.45 * 0.55) / math.sqrt(60)
    assert 0.30 - se > 0 >= 0.30 - 2 * se
    d = run(s=s)
    assert d.action == "take" and d.risk_pct == pytest.approx(0.24)


def test_kelly_ceiling_binds_for_a_thin_edge():
    # p = 0.52 at 1:1 over 2,000 trades: math 2, evidence factor 0.5 (base 1% -> 0.5%), but a quarter of
    # the conservative Kelly fraction is only ~0.44%, so Kelly is the binding limit (Gate 6.5).
    s = dict(setup_id="sweep-v1", n=2000, win_rate=0.52, avg_win_r=1.0, avg_loss_r=1.0, avg_cost_r=0.0)
    d = run(proposal(target=102.0, cost_price=0.0), s, account(base_risk_pct=1.0))
    p_cons = 0.52 - math.sqrt(0.52 * 0.48 / 2000)
    kelly = p_cons - (1 - p_cons) / 1.0
    assert d.action == "take", d.explain()
    assert 0.25 * kelly * 100 < 0.5
    assert d.risk_pct <= 0.25 * kelly * 100 + 1e-9


def test_heat_limit():
    d = run(a=account(open_risk_pct=1.8))
    assert d.action == "take" and d.risk_pct <= 0.2 + 1e-9
    assert run(a=account(open_risk_pct=2.0)).action == "skip"


def test_size_rounds_to_zero_skips():
    assert run(a=account(equity=100.0)).action == "skip"


def test_net_results_record():
    results = [2.0] * 90 + [-1.0] * 110        # net R; mean = (180 - 110) / 200 = 0.35
    d = run(s=dict(setup_id="sweep-v1", results_r=results, avg_cost_r=0.05))
    assert d.math_score == 2 and d.action == "take"


def test_mismatched_setup_raises():
    with pytest.raises(ValueError):
        run(s={**GOOD_SETUP, "setup_id": "other"})


def test_journal_row_has_all_columns_and_keeps_skips():
    from trading_intelligence import JOURNAL_COLUMNS
    d = run(a=account(emotional_state="revenge"))
    assert list(d.journal_row) == list(JOURNAL_COLUMNS)
    assert d.journal_row["decision"] == "skip" and d.journal_row["risk_pct"] == ""
