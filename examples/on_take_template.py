#!/usr/bin/env python3
"""Hand-off from the sniper scanner to YOUR bot's order code (template).

The scanner runs this for every trade the PhilosophyGate approves (and, for a provisional record, only
once the setup's forward trades pass on their own):

    python -m trading_intelligence.sniper scan ... --on-take "python examples/on_take_template.py"

It receives one JSON object on stdin:
    trade_id, setup, symbol, timeframe, side ("long"/"short"), order ("limit"/"market"),
    entry, stop, target, size (units, already sized by Gate 6), risk_pct, expiry_bars,
    max_hold_bars, est_ev_r, decided_at
The decision is already in the journal before this runs. Exit 0 when the order was accepted; any
other exit code (or an exception) is written into the journal row as a failed hand-off.

DRY RUN BY DEFAULT: nothing is sent until TI_LIVE=1 is set in this process's environment. Replace
place_order() with a call to your bot's own order function. Keep broker keys in your bot's own
config or environment, never in this repository.
"""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

LOG = Path(os.environ.get("TI_ON_TAKE_LOG", Path.home() / ".trading-intelligence" / "on_take.log"))


def validate(t: dict) -> None:
    need = ("trade_id", "symbol", "side", "order", "entry", "stop", "target", "size")
    missing = [k for k in need if t.get(k) in (None, "")]
    if missing:
        raise ValueError(f"missing fields {missing}")
    side = 1 if t["side"] == "long" else -1 if t["side"] == "short" else 0
    if not side:
        raise ValueError(f"bad side {t['side']!r}")
    e, s, g, q = (float(t[k]) for k in ("entry", "stop", "target", "size"))
    if not (q > 0 and (e - s) * side > 0 and (g - e) * side > 0):
        raise ValueError(f"inconsistent order: entry {e}, stop {s}, target {g}, size {q}")
    if t["order"] not in ("limit", "market"):
        raise ValueError(f"bad order type {t['order']!r}")


def place_order(t: dict) -> str:
    """Replace with your bot's own call, e.g. bot.broker.place(symbol, side, size, entry, sl, tp, ...).
    A limit order should expire after `expiry_bars` bars of `timeframe`; the position should be closed
    after `max_hold_bars` bars if neither the stop nor the target was hit (the backtest's rules).
    Return the broker's order id."""
    raise NotImplementedError("wire place_order() to your bot's order function")


def main() -> int:
    t = json.loads(sys.stdin.read())
    validate(t)
    live = os.environ.get("TI_LIVE") == "1"
    LOG.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    if not live:
        with LOG.open("a", encoding="utf-8") as f:
            f.write(f"{stamp} DRY RUN {json.dumps(t)}\n")
        print(f"dry run: would {t['side']} {t['size']} {t['symbol']} ({t['order']} @ {t['entry']}, "
              f"stop {t['stop']}, target {t['target']})")
        return 0
    oid = place_order(t)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(f"{stamp} SENT {oid} {json.dumps(t)}\n")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:  # noqa: BLE001 - the scanner journals a non-zero exit
        print(f"on-take failed: {e}", file=sys.stderr)
        sys.exit(1)
