"""Append-only trading journal in the owner's template format (00_philosophy/journal-template.csv).

Section XVI: the reasoning is recorded at the decision, never rebuilt afterwards. So:
- `record_decision()` appends the pre-trade row. Call it BEFORE the order is sent.
- `record_outcome()` fills only the post-trade columns of that row. It refuses to touch any
  pre-trade column; corrections go into `lesson` as "correction: ...".
The file stays compatible with `tools/philosophy/journal_review.py`.
"""
from __future__ import annotations

import csv
import os
from datetime import datetime, timezone
from pathlib import Path

from .gate import JOURNAL_COLUMNS, PRE_TRADE_COLUMNS, Decision

POST_TRADE_COLUMNS = JOURNAL_COLUMNS[28:]


class Journal:
    def __init__(self, path: str | os.PathLike):
        self.path = Path(path)
        if not self.path.exists() or self.path.stat().st_size == 0:
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open("w", newline="", encoding="utf-8") as f:
                csv.writer(f).writerow(JOURNAL_COLUMNS)
        else:
            with self.path.open(newline="", encoding="utf-8") as f:
                header = next(csv.reader(f), [])
            if tuple(header) != JOURNAL_COLUMNS:
                raise ValueError(f"{self.path} does not have the journal template's 39 columns")

    def rows(self) -> list[dict]:
        with self.path.open(newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))

    def record_decision(self, decision: Decision | dict) -> str:
        """Append the pre-trade row (takes, skips and waits alike: not trading is a decision)."""
        row = decision.journal_row if isinstance(decision, Decision) else dict(decision)
        missing = [c for c in PRE_TRADE_COLUMNS if c not in row]
        if missing:
            raise ValueError(f"journal row is missing pre-trade columns: {missing}")
        if any(r["trade_id"] == str(row["trade_id"]) for r in self.rows()):
            raise ValueError(f"trade_id {row['trade_id']!r} already in the journal; a new decision needs a new row")
        with self.path.open("a", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow([row.get(c, "") for c in JOURNAL_COLUMNS])
        return str(row["trade_id"])

    def record_outcome(self, trade_id: str, **post: object) -> dict:
        """Fill post-trade columns (executed_per_plan, exit_reason, result_r, cost_r, mae_r, mfe_r,
        emotional_state_during, outcome_within_expected, lesson, hypothesis_update, reviewed_at)."""
        bad = [k for k in post if k not in POST_TRADE_COLUMNS]
        if bad:
            frozen = [k for k in bad if k in PRE_TRADE_COLUMNS]
            raise ValueError(f"pre-trade fields are frozen after the decision: {frozen}; "
                             "write corrections in lesson as 'correction: ...'" if frozen else f"unknown columns: {bad}")
        rows = self.rows()
        hit = [r for r in rows if r["trade_id"] == str(trade_id)]
        if not hit:
            raise KeyError(f"trade_id {trade_id!r} not in the journal")
        post.setdefault("reviewed_at", datetime.now(timezone.utc).isoformat(timespec="seconds"))
        hit[0].update({k: "" if v is None else v for k, v in post.items()})
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        with tmp.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=JOURNAL_COLUMNS)
            w.writeheader()
            w.writerows(rows)
        tmp.replace(self.path)
        return hit[0]
