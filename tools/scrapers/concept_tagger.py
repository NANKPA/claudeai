"""Tag free text (transcripts, lessons, show notes) with concept and person ids.

Builds an alias index from every concept note's `title` + `aliases` and every
person's `name`, then counts whole-word matches. Scraped documents get
`covers:` / `speaker_ids:` lists, which is what wires them into the graph.
"""
from __future__ import annotations

import re
import sys
from collections import Counter
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ti_lib import load_kb  # noqa: E402

# Aliases too generic to count as evidence on their own.
STOP_ALIASES = {"edge", "liquidity", "trend", "volatility", "risk", "margin", "plan", "review", "fib", "ma", "bb", "ep", "smt", "amd", "ote", "mss"}


@lru_cache(maxsize=1)
def _index() -> tuple[list[tuple[re.Pattern, str]], list[tuple[re.Pattern, str]]]:
    kb = load_kb(include_raw=False)
    concept_pats: list[tuple[re.Pattern, str]] = []
    person_pats: list[tuple[re.Pattern, str]] = []
    for node in kb.nodes.values():
        if node.kind == "concept":
            names = {node.label.split(" (")[0]} | set(node.attrs.get("aliases") or [])
            for name in names:
                name = str(name).strip()
                if len(name) < 3 or name.lower() in STOP_ALIASES:
                    continue
                stem = re.escape(name[:-1] if name.lower().endswith("s") and len(name) > 4 else name)
                concept_pats.append((re.compile(r"\b" + stem + r"(?:s|es)?\b", re.I), node.id))
        elif node.kind == "person" and not node.auto:
            name = str(node.attrs.get("name") or node.label)
            if len(name.split()) >= 2:
                person_pats.append((re.compile(r"\b" + re.escape(name) + r"\b", re.I), node.id))
    return concept_pats, person_pats


def tag(text: str, min_hits: int = 2, top: int = 12) -> dict[str, list[str]]:
    concept_pats, person_pats = _index()
    hits: Counter = Counter()
    for pat, cid in concept_pats:
        n = len(pat.findall(text))
        if n:
            hits[cid] += n
    people = sorted({pid for pat, pid in person_pats if pat.search(text)})
    covers = [cid for cid, n in hits.most_common(top) if n >= min_hits]
    return {"covers": covers, "speaker_ids": people}


if __name__ == "__main__":
    sample = sys.stdin.read() if not sys.stdin.isatty() else "We wait for a liquidity sweep of the Asian high, then a market structure shift and a fair value gap entry during the London kill zone. Volume profile POC and VWAP give targets."
    print(tag(sample, min_hits=1))
