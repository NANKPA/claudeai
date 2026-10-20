"""Sniper engine: fill rules, causality, parity between the backtester and the paper broker, records."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from trading_intelligence.sniper import records as rec
from trading_intelligence.sniper.backtest import Book, Costs, run
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


@pytest.fixture(scope="module")
def prepared():
    return prepare(_walk(), htf="1h")


def test_setups_produce_trades(prepared):
    counts = {k: len(run(prepared, S(), Costs(), prepared=True)) for k, S in SETUPS.items()}
    assert sum(counts.values()) > 20, counts


def test_prepare_is_causal():
    df = _walk(4000)
    full = prepare(df, htf="1h")
    cols = ["atr", "ema20", "ema50", "htf_ema20", "htf_ema50", "pdh", "pdl", "vwap", "vwap_sd", "htf_dir", "regime", "session",
            "htf_pivot_high", "htf_pivot_low", "piv_hi", "piv_lo", "adr10", "asia_hi", "asia_lo", "or_hi", "or_lo",
            "or_closed_above_before", "or_closed_below_before", "dc20_hi", "dc20_lo", "first_half_hour_r", "ny_min"]
    for cut in (1700, 2333, 2650, 3999):
        part = prepare(df.iloc[:cut + 1], htf="1h")
        a, b = full[cols].iloc[cut], part[cols].iloc[cut]
        for col in cols:
            if isinstance(a[col], (float, np.floating)):
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
    assert b.on_bar(2, 100.5, 100.6, 100.0, 100.2) == [] and b.pending is not None  # a touch is not a fill
    b.on_bar(3, 100.5, 100.6, 99.9, 100.2)
    assert b.pos is not None and b.pos["entry"] == 100.0 and b.pos["maker"]
    out = b.on_bar(4, 100.2, 102.5, 100.1, 102.2)
    assert out[0]["exit_reason"] == "target" and out[0]["gross_r"] == pytest.approx(2.0)


def test_limit_gap_fills_at_open_and_stop_first_same_bar():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 101, 101, 101, 101)
    b.submit(_sig())
    out = b.on_bar(1, 99.5, 99.6, 98.5, 99.0)        # gaps below the limit, then trades through the stop
    assert out and out[0]["entry"] == 99.5 and out[0]["exit_reason"] == "stop"
    assert out[0]["gross_r"] == pytest.approx(-0.5)   # R of the PLANNED risk (100 -> 99)
    b.submit(_sig())
    b.on_bar(2, 100, 100, 99.9, 100)                 # fills at 100
    out = b.on_bar(3, 100, 102.5, 98.9, 101)         # stop and target in one bar: stop counts
    assert out[0]["exit_reason"] == "stop" and out[0]["gross_r"] == pytest.approx(-1.0)


def test_limit_gap_through_the_stop_is_not_a_win():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 101, 101, 101, 101)
    b.submit(_sig())
    out = b.on_bar(1, 98, 98.5, 97.5, 98)            # opens below the stop: filled and out at the same price
    assert out[0]["exit_reason"] == "stop" and out[0]["gross_r"] == pytest.approx(0.0)
    b.submit(_sig(side="short", entry=100, stop=101, target=98))
    out = b.on_bar(2, 102, 102.5, 101.5, 102)
    assert out[0]["gross_r"] == pytest.approx(0.0)


@pytest.mark.parametrize("order", ["market", "limit"])
def test_target_reached_on_the_fill_bar_exits_at_the_target(order):
    """A fill bar that closes beyond the target crossed it after the fill: book the target, not the next open."""
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 100.5, 100.5, 100.5, 100.5)
    b.submit(_sig(order=order, entry=100.5 if order == "market" else 100.0))
    out = b.on_bar(1, 100.4, 106, 99.8, 105.5)
    assert out and out[0]["exit_reason"] == "target" and out[0]["exit"] == 102.0
    assert out[0]["gross_r"] <= 2.0 + 1e-9


def test_fill_bar_stop_is_checked_before_the_target():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 100.5, 100.5, 100.5, 100.5)
    b.submit(_sig(order="market", entry=100.5, stop=99.5, target=102.5))
    out = b.on_bar(1, 100.4, 103, 99.4, 102.8)       # through both stop and target: the stop counts
    assert out[0]["exit_reason"] == "stop"


def test_bid_candles_need_the_spread_for_buy_side_triggers():
    b = Book(Costs(0, 0, 0), trigger_spread=0.001)   # 0.1%: a buy fills only when the bid is 0.1 below
    b.on_bar(0, 101, 101, 101, 101)
    b.submit(_sig())
    assert b.on_bar(1, 100.5, 100.6, 99.95, 100.2) == [] and b.pending is not None
    b.on_bar(2, 100.5, 100.6, 99.85, 100.2)
    assert b.pos is not None
    s = Book(Costs(0, 0, 0), trigger_spread=0.001)   # a short's stop triggers when the ASK reaches it
    s.on_bar(0, 99, 99, 99, 99)
    s.submit(_sig(side="short", entry=100, stop=101, target=98, order="limit"))
    s.on_bar(1, 99.9, 100.2, 99.9, 100.0)            # sells at 100
    out = s.on_bar(2, 100.2, 100.92, 100.1, 100.5)   # bid 100.92 = ask ~101.02: stopped
    assert out and out[0]["exit_reason"] == "stop"


def test_limit_cancelled_when_target_trades_first_or_expiry():
    b = Book(Costs(0, 0, 0))
    b.on_bar(0, 101, 101, 101, 101)
    b.submit(_sig())
    b.on_bar(1, 101, 102.1, 100.5, 102)              # ran to target without us (never traded through 100)
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
    pd.testing.assert_series_equal(recost(t, c)["net_r"], t["net_r"], check_names=False, rtol=1e-9)
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
                           records=str(tmp_path / "none.json"), home=str(tmp_path / "home"), once=True, report=False,
                           on_take=None)
    for k, v in kw.items():
        setattr(a, k, v)
    sc = Scanner(a)
    sc.lab = lab
    return sc


def _replay(sc, df, start=2250, stop=None):
    lines = []
    for end in range(start, (stop or len(df)) + 1):
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
    assert all(v["last_time"] == df.index[2399].isoformat() for v in sc2.state.values())


def test_prepare_is_causal_on_the_fx_day():
    df = _walk(3000, freq="15min")
    full = prepare(df, htf="4h", day="fx")
    for cut in (1500, 2222, 2999):
        part = prepare(df.iloc[:cut + 1], htf="4h", day="fx")
        for col in ("pdh", "pdl", "adr10", "vwap", "asia_hi", "or_hi", "htf_pivot_low"):
            assert full[col].iloc[cut] == pytest.approx(part[col].iloc[cut], rel=1e-9, nan_ok=True), (cut, col)


def test_new_york_opening_range_follows_daylight_saving():
    winter = prepare(_walk(3000, start="2024-01-08"), htf="1h")
    summer = prepare(_walk(3000, start="2024-07-08"), htf="1h")
    w = winter[winter["or_hi"].notna()].index[0]
    su = summer[summer["or_hi"].notna()].index[0]
    assert (w.hour, w.minute) == (15, 0) and (su.hour, su.minute) == (14, 0)      # 10:00 New York


def test_on_take_hands_only_gated_takes_to_the_owner_code(tmp_path):
    import json as _json
    import sys
    out = tmp_path / "handed.jsonl"
    hook = f"{sys.executable} -c \"import sys; open({str(out)!r}, 'a').write(sys.stdin.read() + chr(10))\""
    regimes = ["trend_high_vol", "trend_low_vol", "range_high_vol", "range_low_vol"]
    lab = {f"{k}@5m@std": {"record": {"setup_id": f"{k}@5m@std", "results_r": [2.0] * 40 + [-1.0] * 30, "avg_cost_r": 0.05,
                                      "out_of_sample": True, "source": "own", "valid_regimes": regimes,
                                      "valid_sessions": ["asia", "london", "ny", "late"]}}
           for k in ("sniper_ema_pullback",)}
    sc = _scanner(tmp_path, lab=lab, on_take=hook)
    _replay(sc, _walk(2600))
    takes = [r for r in sc.journal.rows() if r["decision"] == "take"]
    handed = [_json.loads(x) for x in out.read_text().splitlines()] if out.exists() else []
    assert takes and len(handed) == len(takes)
    assert {h["trade_id"] for h in handed} == {r["trade_id"] for r in takes}
    assert all(h["setup"] == "sniper_ema_pullback@5m@std" and h["size"] > 0 for h in handed)


@pytest.mark.parametrize("bars_per_pass", [1, 3])
def test_scanner_follows_exactly_the_backtest_trades(tmp_path, bars_per_pass):
    """Paper (shadow) trades equal the backtest's trades, even when a pass catches up several bars."""
    df = _walk(2700)
    key = "sniper_ema_pullback"
    sc = _scanner(tmp_path / str(bars_per_pass), lab={}, setups=[key])
    start = 2250
    sc.frames[("BTCUSDT", "5m")] = df.iloc[:start]
    for end in range(start, len(df) + 1, bars_per_pass):
        sc.candles = lambda sym, tf, _d=df.iloc[:end]: _d
        sc.pass_once()
    fwd = pd.read_csv(tmp_path / str(bars_per_pass) / "home" / "forward.csv", parse_dates=["signal_time"])
    bt = run(prepare(df, htf="1h"), SETUPS[key](tf="5m", htf="1h", symbol="BTCUSDT"), Costs(0.0008, 0.0010, 0.0002), "BTCUSDT",
             prepared=True)
    # the scanner starts flat while the backtest may hold an older position; once both are flat on the
    # same signal they must stay in lockstep
    common = sorted(set(fwd["signal_time"]) & set(bt["signal_time"]))
    assert common, "no shared signal"
    fwd = fwd[fwd["signal_time"] >= common[0]].reset_index(drop=True)
    bt = bt[bt["signal_time"] >= common[0]].reset_index(drop=True)
    assert len(fwd) > 5
    assert list(fwd["signal_time"]) == list(bt["signal_time"])
    np.testing.assert_allclose(fwd["net_r"].to_numpy(), bt["net_r"].to_numpy(), rtol=1e-9)


def test_scanner_restart_after_a_crash_counts_nothing_twice(tmp_path):
    df = _walk(2500)
    regimes = ["trend_high_vol", "trend_low_vol", "range_high_vol", "range_low_vol"]
    lab = {"sniper_ema_pullback@5m@std": {"record": {"setup_id": "sniper_ema_pullback@5m@std",
                                                     "results_r": [2.0] * 40 + [-1.0] * 30, "avg_cost_r": 0.05,
                                                     "out_of_sample": True, "source": "own", "valid_regimes": regimes,
                                                     "valid_sessions": ["asia", "london", "ny", "late"]}}}
    sc = _scanner(tmp_path, lab=lab, setups=["sniper_ema_pullback"])
    _replay(sc, df, 2250, 2450)
    books = (tmp_path / "home" / "books.json").read_text()
    _replay(sc, df, 2450, 2500)
    # crash: the books file is from before the last 50 bars, but forward/account/journal already have them
    (tmp_path / "home" / "books.json").write_text(books)
    sc2 = _scanner(tmp_path, lab=lab, setups=["sniper_ema_pullback"])
    _replay(sc2, df, 2450, 2500)
    fwd = pd.read_csv(tmp_path / "home" / "forward.csv")
    assert fwd["uid"].is_unique
    acc = sc2.account.rows()
    assert len({r["trade_id"] for r in acc}) == len(acc)
    ids = [r["trade_id"] for r in sc2.journal.rows()]
    assert len(ids) == len(set(ids))


def test_scanner_refuses_crosses_and_mismatched_cost_levels(tmp_path):
    from trading_intelligence.sniper.scanner import point_value
    assert point_value("EURUSD", 1.1) == 1.0 and point_value("USDJPY", 150.0) == pytest.approx(1 / 150)
    with pytest.raises(ValueError):
        point_value("EURJPY", 160.0)
    with pytest.raises(SystemExit):
        _scanner(tmp_path, lab={}, symbols=["EURUSD"])          # crypto cost level with a forex market


def test_after_loss_pause_counts_from_the_bar_close(tmp_path):
    from datetime import datetime, timezone
    from trading_intelligence.sniper.scanner import PaperAccount
    acc = PaperAccount(tmp_path, 20.0)
    tr = {"plan_entry": 100.0, "stop": 99.0, "net_r": -1.0, "symbol": "X", "session": "ny", "exit_time": "2024-01-02T14:00:00+00:00"}
    acc.book_trade(tr, {"trade_id": "t1", "key": "k", "size": 0.1, "risk_pct": 0.5}, pd.Timestamp("2024-01-02T14:15:00+00:00"))
    st = acc.state("k", "ny", datetime(2024, 1, 2, 14, 15, 5, tzinfo=timezone.utc), 0.0, "calm", 0.5, 0.001, 0.0, "intraday")
    assert st.minutes_since_last_loss == pytest.approx(5 / 60, abs=1e-6)        # seconds after the close, not 15 min
    assert acc.book_trade(tr, {"trade_id": "t1", "key": "k", "size": 0.1, "risk_pct": 0.5}, pd.Timestamp("2024-01-02T14:15:00+00:00")) is None


def test_htf_pivots_wait_for_the_real_third_bar_across_gaps():
    rng = np.random.default_rng(3)
    n = 5000
    idx = pd.date_range("2024-01-01", periods=n, freq="15min", tz="UTC")
    keep = ~((idx.dayofweek == 5) | ((idx.dayofweek == 6) & (idx.hour < 21)))      # forex weekend
    c = 1.1 * np.exp(np.cumsum(rng.normal(0, 0.0008, n)))
    df = pd.DataFrame({"open": np.r_[c[0], c[:-1]], "close": c}, index=idx)
    df["high"] = df[["open", "close"]].max(axis=1) * (1 + abs(rng.normal(0, 0.0004, n)))
    df["low"] = df[["open", "close"]].min(axis=1) * (1 - abs(rng.normal(0, 0.0004, n)))
    df["volume"] = 1.0
    df = df[keep]
    full = prepare(df, htf="4h", day="fx")
    for cut in range(1500, len(df) - 1, 61):
        part = prepare(df.iloc[:cut + 1], htf="4h", day="fx")
        for col in ("htf_pivot_high", "htf_pivot_low"):
            assert full[col].iloc[cut] == pytest.approx(part[col].iloc[cut], nan_ok=True), (cut, col)


def test_breakeven_win_rates_are_exact():
    from trading_intelligence.sniper.smallaccount import Venue, plan
    v = Venue("v", "v", "spot", 0.0, 0.0005, 1.0, slippage=0.0001)
    pl = plan(1000, 1, 0.25, v, rr=2)
    c_mk, c_mx, c_tk = 0.0, (0.0005 + 0.0001) / 0.0025, 2 * 0.0006 / 0.0025
    p = pl["breakeven_win_rate_maker"]
    assert p * (2 - c_mk) - (1 - p) * (1 + c_mx) == pytest.approx(0, abs=2e-3)
    q = pl["breakeven_win_rate_taker"]
    assert q * (2 - c_tk) - (1 - q) * (1 + c_tk) == pytest.approx(0, abs=2e-3)
