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
                alternative_interpretation="A brief stop run inside a developing down day.",
                hypothesis="1h: price reaches the prior-day high within the session.",
                horizon="by the end of the New York session",
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
    assert run(proposal(timeframe="")).action == "skip"         # the level cannot be named
    for missing in ("undermined_by", "alternative_interpretation", "horizon"):
        d = run(proposal(**{missing: ""}))
        assert d.understanding_score == 1 and d.action == "wait", missing


def test_conditions():
    assert run(proposal(conditions_present={"sweep": True, "reclaim": False, "htf_uptrend": True})).action == "skip"
    assert run(proposal(required_conditions=[])).action == "skip"
    d = run(proposal(conditions_present={"sweep": True, "reclaim": "borderline", "htf_uptrend": True}))
    assert d.evidence_score == 1 and d.action == "wait"
    assert run(proposal(evidence_against=["CPI in 10 minutes"])).action == "wait"
    # resolved arguments are recorded but do not block (the protocol's worked example)
    d = run(proposal(resolved_against=["room exactly at the 2R threshold: checked"]))
    assert d.action == "take" and "resolved: room" in d.journal_row["evidence_against"]


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


def test_mismatched_setup_skips():
    assert run(s={**GOOD_SETUP, "setup_id": "other"}).action == "skip"


def test_journal_row_has_all_columns_and_keeps_skips():
    from trading_intelligence import JOURNAL_COLUMNS
    d = run(a=account(emotional_state="revenge"))
    assert list(d.journal_row) == list(JOURNAL_COLUMNS)
    assert d.journal_row["decision"] == "skip" and d.journal_row["risk_pct"] == ""


# ── regressions from the adversarial review (each was a take that must not be) ───────────────
NAN, INF = float("nan"), float("inf")


@pytest.mark.parametrize("kw", [dict(cost_price=NAN), dict(cost_price=-1.0), dict(cost_price=None),
                                dict(entry=NAN), dict(stop=INF), dict(side="sideways"), dict(regime_tag="unclear"),
                                dict(regime_tag=""), dict(session="")])
def test_bad_or_missing_proposal_inputs_skip(kw):
    d = run(proposal(**kw))
    assert d.action == "skip", (kw, d.explain())
    assert d.journal_row["decision"] == "skip"


@pytest.mark.parametrize("kw", [dict(equity=NAN), dict(equity=0), dict(point_value=0), dict(lot_step=-0.3),
                                dict(lot_step=INF), dict(lot_step=0), dict(base_risk_pct=NAN),
                                dict(open_risk_pct=-1.9), dict(realized_today_r=NAN), dict(drawdown_from_peak_pct=NAN),
                                dict(emotional_state=None), dict(minutes_since_last_loss=NAN)])
def test_bad_account_inputs_skip(kw):
    assert run(a=account(**kw)).action == "skip", kw


@pytest.mark.parametrize("kw", [dict(avg_loss_r=-1.0), dict(avg_loss_r=0.0), dict(win_rate=1.5), dict(win_rate=-0.1),
                                dict(avg_cost_r=-0.5), dict(avg_cost_r=NAN), dict(win_rate=NAN)])
def test_bad_setup_inputs_skip(kw):
    assert run(s={**GOOD_SETUP, **kw}).action == "skip", kw


def test_side_aliases_accepted():
    assert run(proposal(side=" LONG ")).action == "take"
    assert run(proposal(side="sell", entry=100, stop=102, target=96)).action == "take"


def test_drawdown_sign_is_a_magnitude():
    assert run(a=account(drawdown_from_peak_pct=-25.0)).action == "skip"
    d = run(a=account(drawdown_from_peak_pct=-12.0))
    assert d.action == "take" and d.risk_pct == pytest.approx(0.24)


def test_net_results_are_converted_to_gross_before_the_target_cap():
    # 1100 x +2.0 and 900 x -1.111 net, 0.20R of cost inside; 1R of room and 0.20R of cost on this trade
    results = [2.0] * 1100 + [-1.111] * 900
    d = run(proposal(target=102.0, cost_price=0.4), dict(setup_id="sweep-v1", results_r=results, avg_cost_r=0.20))
    assert d.action == "skip" and d.est_ev_r < 0
    row = d.journal_row      # the row's own numbers satisfy the template's EV formula
    ev = row["est_win_prob"] * row["est_avg_win_r"] - (1 - row["est_win_prob"]) * row["est_avg_loss_r"] - row["est_cost_r"]
    assert ev == pytest.approx(row["est_ev_r"], abs=1e-3)


def test_record_without_losses_cannot_score_2():
    d = run(s=dict(setup_id="sweep-v1", results_r=[1.0] * 50, avg_cost_r=0.05))
    assert d.math_score == 1 and d.action == "wait"


def test_recorded_sd_widens_the_standard_error():
    s = dict(setup_id="sweep-v1", n=120, win_rate=0.48, avg_win_r=1.90, avg_loss_r=1.05, avg_cost_r=0.06)
    p = proposal(entry=100, stop=98, target=104, cost_price=0.12)
    full = run(p, s)
    half = run(p, {**s, "sd_r": 1.8})
    assert full.action == half.action == "take"
    assert half.risk_pct == pytest.approx(full.risk_pct / 2, rel=0.1)


def test_amber_halves_the_final_risk_even_when_kelly_binds():
    s = dict(setup_id="sweep-v1", n=2000, win_rate=0.52, avg_win_r=1.0, avg_loss_r=1.0, avg_cost_r=0.0)
    p = proposal(target=102.0, cost_price=0.0)
    green = run(p, s, account(base_risk_pct=1.0))
    amber = run(p, s, account(base_risk_pct=1.0, emotional_state="tired"))
    assert green.action == amber.action == "take"
    assert amber.risk_pct == pytest.approx(green.risk_pct / 2, rel=0.02)


@pytest.mark.parametrize("state", ["calm/fomo", "calm|fomo", "fomo revenge", "FOMO!", "revenge-trading",
                                   "calm;excited", "calm;greedy", "focused - revenge"])
def test_red_tags_in_any_format(state):
    assert run(a=account(emotional_state=state)).action == "skip"


def test_unrecognised_words_count_as_amber():
    from trading_intelligence import emotion_colour
    assert emotion_colour("calm hungry") == "amber" and emotion_colour("calm, focused") == "green"


def test_breakers_take_precedence_over_the_pause():
    d = run(a=account(realized_today_r=-3.5, minutes_since_last_loss=5))
    assert d.action == "skip" and "daily loss" in d.explain()


def test_unknown_time_since_a_loss_waits_and_swing_style_waits_for_next_session():
    assert run(a=account(realized_today_r=-1.0)).action == "wait"
    assert run(a=account(realized_today_r=-1.0, minutes_since_last_loss=30)).action == "take"
    assert run(a=account(trading_style="swing", loss_this_session=True)).action == "wait"


def test_regime_and_session_must_match_the_record():
    s = {**GOOD_SETUP, "valid_regimes": ["trend_low_vol"], "valid_sessions": ["ny_am"]}
    assert run(s=s).action == "take"
    assert run(proposal(regime_tag="trend_high_vol"), s).action == "skip"
    assert run(proposal(session="asia"), s).action == "skip"


def test_tight_stop_without_cost_cannot_size_up():
    assert run(proposal(stop=99.999, cost_price=None)).action == "skip"
    assert run(proposal(stop=99.999, cost_price=0.1)).action == "skip"


def test_limits_floors_and_tighten_only():
    from trading_intelligence.gate import InputError
    for bad in (dict(min_trades=5), dict(kelly_fraction_cap=1.0), dict(daily_loss_r=NAN), dict(max_heat_pct=-1)):
        with pytest.raises(InputError):
            Limits(**bad)
    tight, ignored = Limits().tightened({"daily_loss_r": 50, "drawdown_stop_pct": 99, "min_trades": 5,
                                         "max_heat_pct": 1.0, "min_trades_x": 1})
    assert tight.daily_loss_r == 3.0 and tight.drawdown_stop_pct == 20.0 and tight.min_trades == 30
    assert tight.max_heat_pct == 1.0 and len(ignored) == 4


def test_value_gap_with_a_card_is_judged_by_the_card():
    p = proposal(value_gap_only=True, required_conditions=["gap_gt_2atr_from_vwap", "no_news"],
                 conditions_present={"gap_gt_2atr_from_vwap": True, "no_news": True})
    assert run(p).action == "take"
    assert run(proposal(value_gap_only=True, required_conditions=[])).action == "skip"


def test_generated_trade_ids_are_unique():
    a = run(proposal(instrument="ES", decided_at="2026-10-13T09:47:00+00:00"))
    b = run(proposal(instrument="NQ", decided_at="2026-10-13T09:47:00+00:00"))
    c = run(proposal(instrument="NQ", decided_at="2026-10-13T09:47:00+00:00"))
    ids = {a.journal_row["trade_id"], b.journal_row["trade_id"], c.journal_row["trade_id"]}
    assert len(ids) == 3


def test_exceptions_never_escape():
    d = PhilosophyGate().evaluate(proposal(evidence_against="CPI soon"), SetupRecord(**GOOD_SETUP), account())
    assert d.action == "wait"
    d = PhilosophyGate().evaluate(proposal(), SetupRecord(**{**GOOD_SETUP, "setup_id": "other"}), account())
    assert d.action == "skip" and "0 Inputs" in d.explain()
