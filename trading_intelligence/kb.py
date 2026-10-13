"""Query the trading-intelligence knowledge base: the owner's philosophy first, then concepts,
playbooks, books, people and the evidence behind them."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from functools import cached_property
from pathlib import Path

import yaml

from ._paths import ensure_tools_on_path

ROOT = ensure_tools_on_path()
from ti_lib import load_kb  # noqa: E402

KB_DIR = ROOT / "trading-intelligence"
PHILO_DIR = KB_DIR / "00_philosophy"
PHILO_KINDS = {"philosophy", "principle", "hypothesis", "question"}
LINEAGE_RELATIONS = {"derived_from", "influenced_by"}
_WORD = re.compile(r"[a-z0-9]+")


def _words(text: str) -> list[str]:
    return [w for w in _WORD.findall((text or "").lower()) if len(w) > 1]


def _clean(text: str) -> str:
    text = re.sub(r"\[\[([a-z0-9_]+)\]\]", r"\1", text or "")
    return re.sub(r"\n{3,}", "\n\n", text).strip()


class KnowledgeBase:
    """Read-only view of the knowledge base. Loading takes a second or two; reuse one instance."""

    def __init__(self) -> None:
        self._kb = load_kb(include_raw=False)
        self.nodes = self._kb.nodes
        self._out: dict[str, list] = defaultdict(list)
        self._in: dict[str, list] = defaultdict(list)
        for e in self._kb.edges:
            self._out[e.source].append(e)
            self._in[e.target].append(e)

    # ── lookup ──────────────────────────────────────────────────────────────
    def _summary(self, nid: str) -> str:
        n = self.nodes[nid]
        a = n.attrs
        for key in ("summary", "statement", "known_for", "key_idea", "key_takeaways"):
            if a.get(key):
                return str(a[key])
        for para in re.split(r"\n\s*\n", n.body or ""):
            p = para.strip()
            if len(p) >= 60 and p[0] not in "#|>`-":
                return _clean(p)[:500]
        return ""

    def node(self, node_id: str, body_chars: int = 2000) -> dict:
        """One node: label, kind, layer, summary, source file, an excerpt of its text and its links."""
        if node_id not in self.nodes:
            raise KeyError(f"unknown node id {node_id!r}; use search() to find ids")
        n = self.nodes[node_id]
        links: dict[str, list[dict]] = defaultdict(list)
        for e in self._out[node_id]:
            links[e.relation].append({"id": e.target, "label": self.nodes[e.target].label, "inferred": e.inferred})
        for e in self._in[node_id]:
            links[f"{e.relation} (incoming)"].append({"id": e.source, "label": self.nodes[e.source].label,
                                                       "inferred": e.inferred})
        body = _clean(n.body)
        return {
            "id": n.id, "label": n.label, "kind": n.kind, "layer": n.attrs.get("layer"),
            "status": n.attrs.get("status"), "source_file": f"trading-intelligence/{n.source_file}",
            "url": n.attrs.get("url"), "summary": self._summary(node_id),
            "text": body[:body_chars] + ("…" if len(body) > body_chars else ""),
            "links": dict(links),
        }

    def search(self, query: str, kinds: list[str] | None = None, limit: int = 10) -> list[dict]:
        """Keyword search over labels, aliases and text. Philosophy nodes get a small boost, so the
        owner's own framing comes first when it is relevant."""
        q = set(_words(query))
        if not q:
            return []
        hits = []
        for nid, n in self.nodes.items():
            if n.auto or (kinds and n.kind not in kinds):
                continue
            label = set(_words(n.label))
            aliases = set(_words(" ".join(map(str, n.attrs.get("aliases") or []))))
            text = set(_words(self._summary(nid) + " " + (n.body or "")[:4000]))
            score = 3 * len(q & label) + 2 * len(q & aliases) + len(q & text)
            if not score:
                continue
            if n.kind in PHILO_KINDS:
                score *= 1.25
            hits.append((score, nid))
        hits.sort(key=lambda h: (-h[0], h[1]))
        return [{"id": nid, "label": self.nodes[nid].label, "kind": self.nodes[nid].kind,
                 "layer": self.nodes[nid].attrs.get("layer"), "score": round(s, 2),
                 "summary": self._summary(nid)[:300]} for s, nid in hits[:limit]]

    def neighbors(self, node_id: str, relation: str | None = None, direction: str = "both") -> list[dict]:
        out = []
        if direction in ("out", "both"):
            out += [{"id": e.target, "label": self.nodes[e.target].label, "relation": e.relation, "direction": "out"}
                    for e in self._out[node_id] if relation in (None, e.relation)]
        if direction in ("in", "both"):
            out += [{"id": e.source, "label": self.nodes[e.source].label, "relation": e.relation, "direction": "in"}
                    for e in self._in[node_id] if relation in (None, e.relation)]
        return out

    def lineage(self, node_id: str, max_depth: int = 8) -> list[dict]:
        """Where an idea comes from: follow derived_from / influenced_by upstream."""
        seen = {node_id: 0}
        queue = [node_id]
        while queue:
            cur = queue.pop(0)
            if seen[cur] >= max_depth:
                continue
            for e in self._out[cur]:
                if e.relation in LINEAGE_RELATIONS and e.target not in seen:
                    seen[e.target] = seen[cur] + 1
                    queue.append(e.target)
        return [{"id": n, "label": self.nodes[n].label, "depth": d} for n, d in sorted(seen.items(), key=lambda x: x[1])]

    # ── the philosophy ──────────────────────────────────────────────────────
    @cached_property
    def _blueprint(self) -> dict:
        return yaml.safe_load((PHILO_DIR / "blueprint.yaml").read_text(encoding="utf-8"))

    @cached_property
    def _philosophy_lines(self) -> list[str]:
        return (PHILO_DIR / "philosophy-of-the-relationship.md").read_text(encoding="utf-8").splitlines()

    def principles(self) -> list[dict]:
        """The 12 principles of the Practical Doctrine (Section XVIII), in the owner's words."""
        text = "\n".join(self._philosophy_lines)
        stated = {int(m.group(1)): (m.group(2).strip().rstrip("."), m.group(3).strip())
                  for m in re.finditer(r"\*\*Principle (\d+): (.+?)\*\*\n(.+)", text)}
        out = []
        for p in self._blueprint["principles"]:
            num = p["number"]
            title, statement = stated.get(num, (p["title"], ""))
            out.append({"id": p["id"], "number": num, "title": title, "statement": statement,
                        "playbooks_stating_it": len(p.get("exemplified_by") or [])})
        return out

    def philosophy(self, which: str) -> dict:
        """Full text of one section (by id such as philo_acb_principle, or numeral such as III) or one
        principle (principle_* id or a number 1-12)."""
        w = which.strip()
        for p in self.principles():
            if w in (p["id"], str(p["number"]), f"P{p['number']}"):
                return {"id": p["id"], "title": f"Principle {p['number']}: {p['title']}", "text": p["statement"]}
        for s in self._blueprint["sections"]:
            if w in (s["id"], s["numeral"], s["numeral"].lower()):
                a, b = (int(x) for x in s["lines"].split(":")[1].split("-"))
                return {"id": s["id"], "title": s["title"], "text": "\n".join(self._philosophy_lines[a - 1:b]).strip(),
                        "links": {k: [x.rstrip("?") for x in s.get(k, [])] for k in
                                  ("grounded_in", "supported_by", "challenged_by", "operationalized_by")}}
        raise KeyError(f"no section or principle {which!r}; use a numeral I-XXI, a principle number 1-12, or an id")

    # ── practice and evidence ───────────────────────────────────────────────
    @cached_property
    def _alignment(self) -> dict[str, dict]:
        res = json.loads((PHILO_DIR / "mapping-results.json").read_text(encoding="utf-8"))
        return {g["strategy_id"]: g for a in res.get("align", []) for g in a.get("grades", [])}

    def alignment(self, strategy_id: str) -> dict:
        """How a Chart Fanatics playbook scores against the 12 principles (2 explicit, 1 partial, 0 absent)."""
        g = self._alignment.get(strategy_id)
        if not g:
            raise KeyError(f"no alignment grades for {strategy_id!r}")
        scores = [{"principle_id": s["principle_id"], "score": s["score"], "evidence": s.get("evidence", "")}
                  for s in g["scores"]]
        return {"strategy_id": strategy_id, "label": self.nodes[strategy_id].label,
                "total": sum(s["score"] for s in scores), "max": 24, "scores": scores,
                "summary": g.get("summary", ""), "biggest_gap": g.get("biggest_gap", "")}

    def hypotheses(self, status: str | None = None) -> list[dict]:
        data = yaml.safe_load((PHILO_DIR / "hypotheses.yaml").read_text(encoding="utf-8"))
        keep = ("id", "title", "statement", "status", "evidence", "falsified_if", "tests")
        return [{k: h.get(k) for k in keep} for h in data["hypotheses"] if status in (None, h.get("status"))]

    def evidence_lab_summary(self) -> list[dict]:
        """The evidence lab's summary table: study, section tested, verdict, one-line finding."""
        rows = []
        for line in (PHILO_DIR / "evidence-lab.md").read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) == 4 and re.fullmatch(r"S\d+", cells[0]):
                rows.append(dict(zip(("study", "section", "verdict", "finding"), cells)))
        return rows
