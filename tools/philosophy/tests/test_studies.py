"""Small checks of tools/philosophy/studies.py helpers (no market data needed)."""
import numpy as np
import pytest

from tools.philosophy import studies as st


def test_bp_never_prints_a_signed_zero():
    assert st.bp(-0.00003) == "-0.3"
    assert st.bp(0.0) == "+0"
    assert st.bp(0.0072) == "+72"


def test_share_and_prob_do_not_round_to_certainty():
    assert st.share(0.0, 10_000) == "0 of 10,000"
    assert st.share(0.0001, 10_000) == "1 of 10,000"
    assert st.share(0.9997, 10_000) == "9,997 of 10,000"
    assert st.share(1.0, 10_000) == "all 10,000"
    assert st.share(0.25, 10_000) == "25.0%"
    assert st.prob(0.99968) == ">99.9%"
    assert st.prob(1e-9) == "<0.1%"
    assert st.prob(0.5) == "50.0%"


def test_s6_probs_match_the_philosophy_example():
    # one trade of the Section VII strategy: behind with p = 0.4, ahead with p = 0.6
    down, up = st.s6_probs(0.6, 100.0, 120.0, 5.0, 1)
    assert down == pytest.approx(0.4) and up == pytest.approx(0.6)


def test_first_passage_tie_counts_against_reaching_b():
    # one entry; bar 0 touches both C (-1) and B (+3): the adverse move comes first, B is not reached
    hw = np.array([[3.5, 0.0]])
    lw = np.array([[-1.5, -0.5]])
    res, ties = st.first_passage(hw, lw, np.zeros(1), np.ones(1), 3.0, [1.0])
    assert bool(res[("E", 1.0)][0]) and not bool(res[("BC", 1.0)][0]) and ties[1.0] == 1
    hw2 = np.array([[3.5, 3.2]])  # B reached again on the next bar: counts as reaching B after C
    res2, _ = st.first_passage(hw2, lw, np.zeros(1), np.ones(1), 3.0, [1.0])
    assert bool(res2[("BC", 1.0)][0])
