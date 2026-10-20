"""Any account size: what a sniper stop costs in R, and whether a venue lets this account place it.

    python -m trading_intelligence.sniper size --equity 20 --risk-pct 1
    python -m trading_intelligence.sniper size --equity 500 --risk-pct 0.5 --venue binance_spot --stop-pct 0.3

Account size changes only two things: whether the position clears the venue's minimum order and lot
step, and how much leverage a tight stop needs. Percentage fees cost the same in R at $20 or $20,000:
a round trip of 0.2% on a 0.25% stop is 0.8R whatever the balance. So the edge question ("does this
setup make money after costs?") is the same for every account; the sizing question is not.
"""
from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path

import yaml

from .._paths import repo_root

VENUES_FILE = repo_root() / "trading-intelligence" / "10_sniper-lab" / "venues.yaml"
STOPS_PCT = (0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0)


@dataclass
class Venue:
    id: str
    name: str
    kind: str                       # spot / perp / cfd
    maker: float                    # fraction of notional
    taker: float
    min_notional: float             # smallest order value, account currency
    max_leverage: float = 1.0
    slippage: float = 0.0002
    note: str = ""


def load_venues(path: Path = VENUES_FILE) -> dict[str, Venue]:
    out = {}
    if path.exists():
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        for v in data.get("venues", []):
            v = {**v, "id": v.get("venue_id") or v.get("id")}       # venue_id keeps venues out of the knowledge graph
            out[v["id"]] = Venue(**{k: v[k] for k in Venue.__dataclass_fields__ if k in v})
    if not out:     # generic fee levels until a venue table exists
        out = {"generic_std": Venue("generic_std", "Typical retail spot (0.08% maker / 0.10% taker)", "spot", 0.0008, 0.0010, 5.0),
               "generic_low": Venue("generic_low", "Zero-maker venue (0% maker / 0.05% taker)", "spot", 0.0, 0.0005, 5.0)}
    return out


def plan(equity: float, risk_pct: float, stop_pct: float, v: Venue, price: float = 1.0, lot_step: float = 0.0,
         rr: float = 2.0) -> dict:
    """One trade's arithmetic. stop_pct is the stop distance as a percent of price."""
    if not (equity > 0 and risk_pct > 0 and stop_pct > 0):
        raise ValueError("equity, risk_pct and stop_pct must be > 0")
    s = stop_pct / 100
    risk = equity * risk_pct / 100
    notional = risk / s
    lev_needed = notional / equity
    capped = notional > v.max_leverage * equity
    if capped:
        notional = v.max_leverage * equity
    if lot_step > 0 and price > 0:
        notional = math.floor(notional / price / lot_step + 1e-9) * lot_step * price
    actual_risk = notional * s
    c_maker = 2 * v.maker / s                                  # limit in, limit out at the target
    c_mixed = (v.maker + v.taker + v.slippage) / s             # limit in, stopped out at market
    c_taker = 2 * (v.taker + v.slippage) / s                   # market in, market out
    return {"venue": v.id, "stop_pct": stop_pct, "risk": round(risk, 4), "notional_needed": round(risk / s, 2),
            "leverage_needed": round(lev_needed, 2), "capped_by_leverage": capped, "notional": round(notional, 2),
            "actual_risk": round(actual_risk, 4), "actual_risk_pct": round(actual_risk / equity * 100, 3),
            "meets_minimum": notional >= v.min_notional and notional > 0,
            "cost_r_maker": round(c_maker, 3), "cost_r_stop_out": round(c_mixed, 3), "cost_r_taker": round(c_taker, 3),
            "breakeven_win_rate_taker": round((1 + c_taker) / (1 + rr), 3),
            "breakeven_win_rate_maker": round((1 + (c_maker + c_mixed) / 2) / (1 + rr), 3)}


def min_stop_for(cost_r: float, v: Venue, taker: bool = True) -> float:
    """Smallest stop (% of price) whose round-trip cost is at most `cost_r` R."""
    rt = 2 * (v.taker + v.slippage) if taker else 2 * v.maker
    return rt / cost_r * 100


def table(equity: float, risk_pct: float, venues: dict[str, Venue], rr: float = 2.0) -> str:
    L = [f"Account {equity:g}, risk {risk_pct:g}% = {equity * risk_pct / 100:.4g} per trade, target {rr:g}R", ""]
    for v in venues.values():
        L += [f"{v.name} [{v.id}] maker {v.maker:.3%} taker {v.taker:.3%} min order {v.min_notional:g} "
              f"max leverage {v.max_leverage:g}x" + (f" - {v.note}" if v.note else ""),
              "  stop%  order value  leverage  order ok?                  cost in R: maker / stop-out / taker   break-even win rate (taker)"]
        for sp in STOPS_PCT:
            p = plan(equity, risk_pct, sp, v, rr=rr)
            ok = "yes" if p["meets_minimum"] else "NO (below minimum)"
            if p["capped_by_leverage"]:
                ok += f", risk cut to {p['actual_risk_pct']:.2f}%"
            be = p["breakeven_win_rate_taker"]
            L.append(f"  {sp:5.2f}  {p['notional_needed']:11.2f}  {p['leverage_needed']:7.2f}x  {ok:<26} "
                     f"{p['cost_r_maker']:5.2f} / {p['cost_r_stop_out']:5.2f} / {p['cost_r_taker']:5.2f}"
                     f"{'':17}{'impossible' if be >= 1 else f'{be:.0%}'}")
        mk = "any stop" if v.maker == 0 else f"{min_stop_for(0.10, v, taker=False):.2f}%"
        L += [f"  costs <= 0.10R need a stop of at least {min_stop_for(0.10, v):.2f}% with market orders, {mk} with "
              "limit orders on both sides", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="sniper size")
    ap.add_argument("--equity", type=float, default=20.0)
    ap.add_argument("--risk-pct", type=float, default=1.0)
    ap.add_argument("--venue", nargs="*", default=None, help="venue ids from 10_sniper-lab/venues.yaml (default: all)")
    ap.add_argument("--stop-pct", type=float, default=None, help="one stop size, percent of price")
    ap.add_argument("--rr", type=float, default=2.0)
    a = ap.parse_args(argv)
    venues = load_venues()
    if a.venue:
        missing = [x for x in a.venue if x not in venues]
        if missing:
            ap.error(f"unknown venue(s) {missing}; known: {sorted(venues)}")
        venues = {k: venues[k] for k in a.venue}
    if a.stop_pct:
        for v in venues.values():
            print(v.id, plan(a.equity, a.risk_pct, a.stop_pct, v, rr=a.rr))
    else:
        print(table(a.equity, a.risk_pct, venues, a.rr))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
