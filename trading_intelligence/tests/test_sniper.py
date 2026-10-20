"""Sniper engine: fill rules, causality, parity between the backtester and the paper broker, records."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from trading_intelligence.sniper import records as rec
from trading_intelligence.sniper.backtest import Book, Costs, _close, run
from trading_intelligence.sniper.setups import SETUPS, Signal, prepare


def _walk(n=6000, seed=7, freq="5min", start="2024-01-01"):
    rng = np.random.default_rng(seed)
    r = rng.standard_t(4, n) * 0.0015 + np.sin(np.arange(n) / 400) * 0.0004
    close = 40000 * np.exp(np.cumsum(r))
    open_ = np.r_[close[0], close[:-1]] * (1 + rng.normal(0, 0.0002, n))
    span = np.abs(rng.normal(0, 0.0015, n)) * close
    high = np.maximum(open_, close) + span * rng.random(n)
    low = np.minimum(open_, close) - span * rng.random(n)
    idx = pd.date_range(start, periods=n, freq=freq, tz="UTC")
    return pd.DataFrame({"open": open_, "high": high, "low": low, "close": close,
                         "volume": rng.lognormal(3, 1, n)}, index=idx)


def _reference_run(d, setup, costs, symbol="", warmup=300):
    """The backtester's loop as first written (before the Book refactor), kept to prove parity."""
    o, h, l, c = (d[k].to_numpy() for k in ("open", "high", "low", "close"))
    idx, n, trades, pending, pos, i = d.index, len(d), [], None, None, warmup
    while i < n:
        if pos is not None:
            s = pos["sig"]
            side = 1 if s.side == "long" else -1
            exit_px = reason = None
            if i > pos["fill_k"] or pos["check_stop_on_fill"]:
                if (l[i] <= s.stop) if side == 1 else (h[i] >= s.stop):
                    gap = (o[i] < s.stop) if side == 1 else (o[i] > s.stop)
                    exit_px, reason = (o[i] if gap and i > pos["fill_k"] else s.stop), "stop"
                elif i > pos["fill_k"] and ((h[i] >= s.target) if side == 1 else (l[i] <= s.target)):
                    gap = (o[i] > s.target) if side == 1 else (o[i] < s.target)
                    exit_px, reason = (o[i] if gap else s.target), "target"
            pos["mae"] = min(pos["mae"], ((l[i] if side == 1 else h[i]) - pos["entry"]) * side)
            pos["mfe"] = max(pos["mfe"], ((h[i] if side == 1 else l[i]) - pos["entry"]) * side)
            if exit_px is None and i - pos["fill_k"] >= s.max_hold_bars:
                exit_px, reason = c[i], "time"
            pos["check_stop_on_fill"] = False
            if exit_px is not None:
                trades.append(_close(pos, i, idx[i], exit_px, reason, costs, symbol))
                pos = None
        elif pending is not None:
            s, last = pending
            side = 1 if s.side == "long" else -1
            if (l[i] <= s.entry) if side == 1 else (h[i] >= s.entry):
                fill = min(o[i], s.entry) if side == 1 else max(o[i], s.entry)
                pos = {"sig": s, "fill_k": i, "entry_time": idx[i], "entry": fill, "maker": True,
                       "check_stop_on_fill": True, "mae": 0.0, "mfe": 0.0}
                pending = None
                if (l[i] <= s.stop) if side == 1 else (h[i] >= s.stop):
                    trades.append(_close(pos, i, idx[i], s.stop, "stop", costs, symbol))
                    pos = None
            elif ((h[i] >= s.target) if side == 1 else (l[i] <= s.target)) or i >= last:
                pending = None
        if pos is None and pending is None and i < n - 1:
            sig = setup.signal_at(d, i)
            if sig is not None:
                if sig.order == "market":
                    fill, side = o[i + 1], 1 if sig.side == "long" else -1
                    if (fill - sig.stop) * side > 0 and (sig.target - fill) * side > 0:
                        pos = {"sig": sig, "fill_k": i + 1, "entry_time": idx[i + 1], "entry": fill, "maker": False,
                               "check_stop_on_fill": True, "mae": 0.0, "mfe": 0.0}
                else:
                    pending = (sig, i + max(sig.expiry_bars, 1))
        i += 1
    return pd.DataFrame(trades)


@pytest.fixture(scope="module")
def prepared():
    return prepare(_walk(), htf="1h")


@pytest.mark.parametrize("key", sorted(SETUPS))
def test_book_matches_reference_loop(prepared, key):
    costs = Costs()
    new = run(prepared, SETUPS[key](), costs, "X", prepared=True)
    ref = _reference_run(prepared, SETUPS[key](), costs, "X")
    assert len(new) == len(ref)
    if len(ref):
        cols = ["entry_time", "exit_time", "entry", "exit", "exit_reason", "net_r", "mae_r", "mfe_r", "bars_held"]
        pd.testing.assert_frame_equal(new[cols].reset_index(drop=True), ref[cols].reset_index(drop=True))


def test_setups_produce_trades(prepared):
    counts = {k: len(run(prepared, S(), Costs(), prepared=True)) for k, S in SETUPS.items()}
    assert sum(counts.values()) > 20, counts


def test_prepare_is_causal():
    df = _walk(4000)
    full = prepare(df, htf="1h")
    cols = ["atr", "ema20", "ema50", "htf_ema20", "htf_ema50", "pdh", "pdl", "vwap", "vwap_sd", "htf_dir", "regime", "session"]
    for cut in (1700, 2333, 3999):
        part = prepare(df.iloc[:cut + 1], htf="1h")
        a, b = full[cols].iloc[cut], part[cols].iloc[cut]
        for col in cols:
            if isinstance(a[col], float):
                assert a[col] == pytest.approx(b[col], rel=1e-9, nan_ok=True), (cut, col)
            else:
                assert a[col] == b[col], (cut, col)


def test_signals_only_read_the_past(prepared):
    """A signal at bar i is identical whether or not the future bars exist."""
    for key, S in SETUPS.items():
        st = S()
        hits = [i for i in range(400, len(prepared) - 1) if st.signal_at(prepared, i) is not None][:5]
        for i in hits:
            a, b = st.signal_at(prepared, i), st.signal_at(prepared.iloc[:i + 1], i)
            assert (a.side, a.entry, a.stop, a.target) == (b.side, b.entry, b.stop, b.target), key


def _sig(side="long", entry=100.0, stop=99.0, target=102.0, order="limit", expiry=3, hold=10):
    return Signal("s", 0, pd.Timestamp("2024-01-01", tz="UTC"), side, entry, stop, target, order, expiry, hold,
                  "trend_low_vol", "ny")


def test_limit_fills_only_when_traded_through():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 101, 101.5, 100.5, 101)
    b.submit(_sig())
    assert b.on_bar(1, 101, 101.2, 100.01, 101) == [] and b.pending is not None   # never reached 100
    b.on_bar(2, 100.5, 100.6, 99.9, 100.2)
    assert b.pos is not None and b.pos["entry"] == 100.0 and b.pos["maker"]
    out = b.on_bar(3, 100.2, 102.5, 100.1, 102.2)
    assert out[0]["exit_reason"] == "target" and out[0]["gross_r"] == pytest.approx(2.0)


def test_limit_gap_fills_at_open_and_stop_first_same_bar():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 101, 101, 101, 101)
    b.submit(_sig())
    out = b.on_bar(1, 99.5, 99.6, 98.5, 99.0)        # gaps below the limit AND through the stop
    assert out and out[0]["entry"] == 99.5 and out[0]["exit_reason"] == "stop"
    b.submit(_sig())
    b.on_bar(2, 100, 100, 99.95, 100)                # fills at 100
    out = b.on_bar(3, 100, 102.5, 98.9, 101)         # stop and target in one bar: stop counts
    assert out[0]["exit_reason"] == "stop" and out[0]["gross_r"] == pytest.approx(-1.0)


def test_limit_cancelled_when_target_trades_first_or_expiry():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 101, 101, 101, 101)
    b.submit(_sig())
    b.on_bar(1, 101, 102.1, 100.5, 102)              # ran to target without us
    assert b.flat
    b.submit(_sig(expiry=2))
    b.on_bar(2, 101, 101.5, 100.5, 101)
    b.on_bar(3, 101, 101.5, 100.5, 101)
    assert b.flat


def test_market_order_dropped_when_open_gaps_past_stop():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 101, 101, 101, 101)
    b.submit(_sig(order="market", entry=101))
    assert b.on_bar(1, 98.5, 99, 98, 98.5) == [] and b.flat


def test_costs_and_recost_agree(prepared):
    from trading_intelligence.sniper.lab import recost
    c = Costs(0.0008, 0.001, 0.0002)
    t = run(prepared, SETUPS["sniper_fvg_retrace"](), c, prepared=True)
    if t.empty:
        pytest.skip("no trades on the synthetic walk")
    pd.testing.assert_series_equal(recost(t, c)["net_r"], t["net_r"], check_names=False)
    cheaper = recost(t, Costs(0, 0.0005, 0.0001))
    assert (cheaper["cost_r"] < t["cost_r"]).all()


def test_conditions_are_chosen_in_sample_only():
    rng = np.random.default_rng(1)
    times = pd.date_range("2023-01-01", periods=400, freq="12h", tz="UTC")
    t = pd.DataFrame({"signal_time": times, "entry_time": times, "exit_time": times + pd.Timedelta("1h"),
                      "regime": np.where(np.arange(400) % 2, "trend_low_vol", "range_low_vol"), "session": "ny",
                      "gross_r": 0.0, "cost_r": 0.1, "stop_pct": 0.01})
    # in-sample: trend is good, range is bad; out-of-sample: the reverse (must NOT change the choice)
    is_mask = t["signal_time"] < pd.Timestamp("2023-07-01", tz="UTC")
    good = t["regime"] == "trend_low_vol"
    t["net_r"] = np.where(is_mask, np.where(good, 0.5, -0.2), np.where(good, -0.5, 0.5)) + rng.normal(0, 0.01, 400)
    e = rec.build_record(t, "k", "2023-07-01")
    assert e["valid_regimes"] == ["trend_low_vol"]
    assert e["oos"]["mean_net_r"] < 0 and e["record"]["valid_regimes"] == ["trend_low_vol"]


def _scanner(tmp_path, lab, **kw):
    import argparse
    from trading_intelligence.sniper.scanner import Scanner
    a = argparse.Namespace(venue="binance", symbols=["BTCUSDT"], timeframes=["5m"], setups=sorted(SETUPS), fees="std",
                           maker=None, taker=None, slippage=None, equity=20.0, risk_pct=1.0, lot_step=0.000001,
                           min_notional=0.0, max_leverage=50.0, style="intraday", state="calm",
                           records=str(tmp_path / "none.json"), home=str(tmp_path / "home"), once=True, report=False)
    for k, v in kw.items():
        setattr(a, k, v)
    sc = Scanner(a)
    sc.lab = lab
    return sc


def _replay(sc, df, start=2250, stop=None):
    lines = []
    for end in range(start, stop or len(df)):
        sc.frames[("BTCUSDT", "5m")] = df.iloc[:end]
        sc.candles = lambda sym, tf, _d=df.iloc[:end]: _d
        lines += sc.pass_once()
    return lines


def test_scanner_replay_journals_every_signal_and_follows_them(tmp_path):
    df = _walk(2600)
    sc = _scanner(tmp_path, lab={})
    lines = _replay(sc, df)
    rows = sc.journal.rows()
    assert rows and all(r["decision"] == "skip" for r in rows)          # no records: the gate stands aside
    fwd = (tmp_path / "home" / "forward.csv")
    assert fwd.exists() and len(fwd.read_text().splitlines()) > 1        # ...but every signal is followed (shadow)
    assert not (tmp_path / "home" / "account.csv").exists()
    assert any("SKIP" in x for x in lines)


def test_scanner_takes_when_the_record_passes_and_books_outcomes(tmp_path):
    from trading_intelligence.sniper.scanner import Scanner  # noqa: F401
    regimes = ["trend_high_vol", "trend_low_vol", "range_high_vol", "range_low_vol"]
    sessions = ["asia", "london", "ny", "late"]
    good = [2.0] * 40 + [-1.0] * 30                                      # mean +0.71R, n = 70
    lab = {f"{k}@5m@std": {"record": {"setup_id": f"{k}@5m@std", "results_r": good, "avg_cost_r": 0.05,
                                      "out_of_sample": True, "source": "own", "valid_regimes": regimes,
                                      "valid_sessions": sessions}} for k in SETUPS}
    sc = _scanner(tmp_path, lab=lab)
    _replay(sc, _walk(2600))
    rows = sc.journal.rows()
    takes = [r for r in rows if r["decision"] == "take"]
    assert takes, [r["evidence_against"][:200] for r in rows[:5]]
    acc = sc.account.rows()
    done = [r for r in takes if r["result_r"] != ""]
    assert done and len(acc) == len([r for r in done if r["exit_reason"] != "not_filled"])
    assert float(acc[-1]["equity"]) == pytest.approx(20.0 + sum(float(r["pnl"]) for r in acc), rel=1e-6)
    for r in takes:                                                      # Gate 6 never exceeds the budget
        assert float(r["risk_pct"]) <= 1.0 + 1e-9


def test_scanner_state_survives_a_restart(tmp_path):
    df = _walk(2400)
    sc = _scanner(tmp_path, lab={})
    _replay(sc, df, 2000, 2200)
    sc2 = _scanner(tmp_path, lab={})
    assert sc2.state.keys() == sc.state.keys()
    _replay(sc2, df, 2200, 2400)
    assert all(v["last_time"] == df.index[2398].isoformat() for v in sc2.state.values())
