#!/usr/bin/env python3
"""Merge the philosophy-mapping results into the knowledge base.

Input: a JSON file with the mapping agents' output (kept in the repo as
00_philosophy/mapping-results.json, the default, so the merge can be re-run at any time)
  {"maps": [{"nodes": [...], "extension_candidates": [...]}, ...],
   "extensions": {"extensions": [...]},
   "align": [{"grades": [...]}, ...]}
Output (all under trading-intelligence/00_philosophy/):
  blueprint.yaml          the philosophy nodes with their typed links (edges in the graph)
  blueprint-map.md        every link with the reason it holds (synthesis_blueprint_map)
  strategy-alignment.md   47 playbooks x 12 principles (synthesis_strategy_alignment)

Every id is checked against the knowledge base; unknown ids are dropped and reported, and links
filed under the wrong key are moved (a concept under supported_by goes to grounded_in, a playbook
to operationalized_by). Agent-mapped links are written as INFERRED edges (trailing "?"), except
structural links and the sources the owner names in Section XX.

Usage: python3 tools/philosophy/merge_blueprint.py [results.json]
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ti_lib import KB_ROOT, kind_of, load_kb  # noqa: E402

PHILO_DIR = KB_ROOT / "00_philosophy"
BLUEPRINT = PHILO_DIR / "blueprint.yaml"
LINK_KEYS = ["grounded_in", "supported_by", "challenged_by", "operationalized_by"]
SOURCE_KINDS = {"book", "mathbook", "paper", "person", "media", "podcast", "channel"}
PRACTICE_KINDS = {"strategy", "framework", "synthesis", "formula", "course", "track"}
PHILO_KINDS = {"philosophy", "principle", "hypothesis", "question"}
# Sources the owner names in Section XX: stated, not inferred.
NAMED_IN_XX = ["mathbook_hasbrouck_empirical_microstructure", "book_trading_and_exchanges",
               "paper_madhavan_2000", "paper_kahneman_tversky_1979"]

HEADER = """# Blueprint — how "The Philosophy of the Relationship" connects to the rest of the knowledge base.
# Nodes: the philosophy's 21 sections (philo_*), its 12 principles (principle_*), the open questions
# of Section XIX (question_*), and research papers Section XX points to (paper_*).
# Edge keys (see tools/ti_lib.py): grounded_in (-> concept), supported_by / challenged_by (-> source),
# operationalized_by (-> playbook / framework / formula), exemplified_by (principle -> playbook that
# states the principle explicitly, from strategy-alignment.md), expresses (section -> principle), part_of.
# A trailing "?" marks an INFERRED link (mapped by an agent; the reason for each is in blueprint-map.md).
# Regenerate: python3 tools/philosophy/merge_blueprint.py   (reads mapping-results.json)
"""


def correct_key(key: str, kind: str) -> str | None:
    if kind in PHILO_KINDS:
        return None
    if key == "challenged_by":
        return key
    if kind in ("concept",):
        return "grounded_in"
    if kind in PRACTICE_KINDS:
        return "operationalized_by"
    if kind in SOURCE_KINDS:
        return "supported_by"
    return key


def clean_maps(maps: list[dict], extensions: list[dict], known: set[str],
               rejected: set[tuple[str, str]] = frozenset()) -> tuple[dict, list[str], list[dict]]:
    """`rejected` holds (node, target) pairs that link verification refuted; they are skipped."""
    out: dict[str, dict] = {}
    dropped: list[str] = []
    for m in maps:
        for node in m.get("nodes", []):
            nid = node["id"]
            if nid not in known:
                dropped.append(f"node {nid}")
                continue
            entry = out.setdefault(nid, {"summary": node.get("summary", ""), "measurable_as": [], "gaps": [],
                                         **{k: [] for k in LINK_KEYS}})
            entry["measurable_as"] += node.get("measurable_as", [])
            entry["gaps"] += node.get("gaps", [])
            for key in LINK_KEYS:
                for link in node.get(key, []):
                    tid = (link.get("id") or "").strip().rstrip("?")
                    if tid not in known:
                        dropped.append(f"{nid}.{key} -> {tid}")
                        continue
                    k2 = correct_key(key, kind_of(tid))
                    if k2 is None or tid == nid or (nid, tid) in rejected:
                        continue
                    if all(x["id"] != tid for x in entry[k2]):
                        entry[k2].append({"id": tid, "why": link.get("why", "")})
    ext_out = []
    for e in extensions:
        applies = [a for a in e.get("applies_to", []) if a in known and kind_of(a) in PHILO_KINDS]
        srcs = [s for s in e.get("source_ids", []) if s in known and kind_of(s) not in PHILO_KINDS]
        dropped += [f"extension '{e.get('title')}' -> {s}" for s in e.get("source_ids", []) if s not in known]
        if applies and srcs:
            ext_out.append({**e, "applies_to": applies, "source_ids": srcs})
    return out, dropped, ext_out


def write_blueprint(mapped: dict, exts: list[dict], exemplars: dict[str, list[str]]) -> Counter:
    doc = yaml.safe_load(BLUEPRINT.read_text(encoding="utf-8"))
    counts: Counter = Counter()
    ext_links: dict[str, dict[str, set]] = defaultdict(lambda: defaultdict(set))
    for e in exts:
        for a in e["applies_to"]:
            for s in e["source_ids"]:
                if e["relation"] == "challenges":
                    key = "challenged_by"
                else:
                    key = correct_key("supported_by", kind_of(s)) or "supported_by"
                ext_links[a][key].add(s)
    for group in ("sections", "principles", "questions"):
        for entry in doc.get(group, []):
            nid = entry["id"]
            m = mapped.get(nid, {})
            if m.get("summary"):
                entry["summary"] = m["summary"]
            for key in LINK_KEYS:
                ids = [x["id"] for x in m.get(key, [])]
                ids += sorted(ext_links[nid][key] - set(ids))
                vals = [f"{i}?" for i in ids]
                if nid == "philo_research_foundations" and key == "supported_by":
                    vals = NAMED_IN_XX + [v for v in vals if v.rstrip("?") not in NAMED_IN_XX]
                if vals:
                    entry[key] = vals
                    counts[key] += len(vals)
                else:
                    entry.pop(key, None)
            if group == "principles" and exemplars.get(nid):
                entry["exemplified_by"] = exemplars[nid]
                counts["exemplified_by"] += len(exemplars[nid])
    root_map = mapped.get("philosophy_relationship")
    if root_map:
        doc["root_links"] = [{"id": "philosophy_relationship",
                              **{k: [f"{x['id']}?" for x in root_map.get(k, [])] for k in LINK_KEYS if root_map.get(k)}}]
        counts.update({k: len(root_map.get(k, [])) for k in LINK_KEYS})
    text = yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=200)
    BLUEPRINT.write_text(HEADER + text, encoding="utf-8")
    return counts


def write_map_md(mapped: dict, exts: list[dict], labels: dict[str, str], order: list[str], dropped: list[str],
                 rejected: list[dict] = ()) -> None:
    lab = lambda i: labels.get(i, i).split(" (")[0]  # noqa: E731
    L = ["---", "id: synthesis_blueprint_map", "type: synthesis",
         'title: "Blueprint Map — every link between the philosophy and the knowledge base, with its reason"',
         "partition: 00_philosophy", "layer: L0",
         "related: [philosophy_relationship, synthesis_philosophy_centrality, synthesis_strategy_alignment, synthesis_philosophy_extensions]",
         "status: synthesized", "---", "",
         "# Blueprint Map", "",
         "> How each section and principle of [[philosophy_relationship]] connects to the rest of the knowledge base. "
         "Links were mapped by research agents that read the philosophy and the linked notes; every id was checked "
         "against the knowledge base. They are judgments (INFERRED edges in the graph), offered for the owner to "
         "accept, reject or extend. Generated by `tools/philosophy/merge_blueprint.py`.", "",
         "Ids are given as `code` rather than wikilinks so this page does not duplicate the edges already in "
         "`blueprint.yaml`. Key: **Grounded in** = the concepts it rests on · **Supported by** = independent sources that argue the same · "
         "**Challenged by** = what complicates it · **Put into practice by** = playbooks, frameworks and formulas that "
         "operationalise it.", ""]
    titles = {"grounded_in": "Grounded in", "supported_by": "Supported by", "challenged_by": "Challenged by",
              "operationalized_by": "Put into practice by"}
    for nid in order:
        m = mapped.get(nid)
        if not m:
            continue
        L += [f"## {labels.get(nid, nid)}", "", f"`{nid}`", ""]
        if m.get("summary"):
            L += [f"*{m['summary']}*", ""]
        for key in LINK_KEYS:
            if m.get(key):
                L.append(f"**{titles[key]}**")
                L += [f"- **{lab(x['id'])}** (`{x['id']}`) — {x['why']}" for x in m[key]]
                L.append("")
        if m.get("measurable_as"):
            L += ["**How it could be measured**"] + [f"- {x}" for x in m["measurable_as"]] + [""]
        if m.get("gaps"):
            L += ["**Gaps in the knowledge base**"] + [f"- {x}" for x in m["gaps"]] + [""]
    if exts:
        L += ["## Extension links", "",
              "Ideas from [[synthesis_philosophy_extensions]] that add, sharpen or challenge parts of the philosophy.", "",
              "| Extension | Relation | Applies to | Sources |", "|---|---|---|---|"]
        for e in exts:
            L.append(f"| {e['title']} | {e['relation']} | " + ", ".join(f"`{a}`" for a in e["applies_to"]) + " | "
                     + ", ".join(f"{lab(s)} (`{s}`)" for s in e["source_ids"]) + " |")
        L.append("")
    if rejected:
        L += ["## Links removed by verification", "",
              f"Independent verifier agents re-read the cited notes and refuted {len(rejected)} proposed links. "
              "They are not in the graph:", "", "| Node | Link | Proposed as | Reason |", "|---|---|---|---|"]
        L += [f"| `{r['node']}` | {lab(r['id'])} (`{r['id']}`) | {r.get('key', '')} | {r.get('reason', '').replace('|', '/')} |"
              for r in rejected]
        L.append("")
    if dropped:
        L += ["## Dropped during validation", "", f"{len(dropped)} proposed links named ids that do not exist in the "
              "knowledge base and were removed:", ""] + [f"- `{d}`" for d in dropped[:60]] + [""]
    (PHILO_DIR / "blueprint-map.md").write_text("\n".join(L), encoding="utf-8")


def write_alignment(align: list[dict], labels: dict[str, str], principles: list[dict], known: set[str]) -> dict[str, list[str]]:
    pids = [p["id"] for p in principles]
    grades = {}
    for a in align:
        for g in a.get("grades", []):
            if g["strategy_id"] in known:
                grades[g["strategy_id"]] = g
    score = {s: {x["principle_id"]: int(x["score"]) for x in g["scores"]} for s, g in grades.items()}
    evid = {s: {x["principle_id"]: x.get("evidence", "") for x in g["scores"]} for s, g in grades.items()}
    total = {s: sum(score[s].get(p, 0) for p in pids) for s in grades}
    exemplars = {p: sorted(s for s in grades if score[s].get(p) == 2) for p in pids}
    n = len(grades)
    lab = lambda i: labels.get(i, i).split(" — ")[0].split(" (")[0]  # noqa: E731
    L = ["---", "id: synthesis_strategy_alignment", "type: synthesis",
         'title: "Strategy Alignment — 47 Chart Fanatics playbooks graded against the 12 principles"',
         "partition: 00_philosophy", "layer: L8",
         "related: [philosophy_relationship, philo_practical_doctrine, synthesis_blueprint_map, synthesis_cf_playbook_patterns]",
         "status: synthesized", "---", "",
         "# Strategy Alignment", "",
         f"> Each of the {n} first-party playbooks in `01_chart-fanatics/strategies/` graded against the 12 principles of "
         "[[philo_practical_doctrine]]: **2** = stated explicitly as a rule or practice, **1** = partial or implied, "
         "**0** = absent from the playbook. Grades describe what the written playbook says, not how the trader actually "
         "trades. Generated by `tools/philosophy/merge_blueprint.py` from agent grading with quoted evidence.", "",
         "## Coverage by principle", "",
         "| # | Principle | Explicit (2) | Partial (1) | Absent (0) | Mean |", "|---|---|---|---|---|---|"]
    for i, p in enumerate(principles, 1):
        vals = [score[s].get(p["id"], 0) for s in grades]
        L.append(f"| P{i} | {p['title']} (`{p['id']}`) | {vals.count(2)} | {vals.count(1)} | {vals.count(0)} | {sum(vals) / max(n, 1):.2f} |")
    weakest = sorted(principles, key=lambda p: sum(score[s].get(p["id"], 0) for s in grades))[:3]
    strongest = sorted(principles, key=lambda p: -sum(score[s].get(p["id"], 0) for s in grades))[:3]
    L += ["", f"**Most often stated:** " + ", ".join(p["title"] for p in strongest) + ".  ",
          f"**Most often missing:** " + ", ".join(p["title"] for p in weakest) + ".", "",
          "The pattern matters for the owner: practitioner playbooks are strongest where the philosophy is about "
          "execution mechanics and weakest where it asks for measurement. Those missing pieces are what the "
          "[[framework_decision_protocol]], the [[framework_trading_journal]] and the [[synthesis_evidence_lab]] supply.", "",
          "## Matrix", "", "| Playbook | " + " | ".join(f"P{i}" for i in range(1, 13)) + " | Total /24 |",
          "|---|" + "---|" * 13]
    for s in sorted(grades, key=lambda s: -total[s]):
        L.append(f"| {lab(s)} (`{s}`) | " + " | ".join(str(score[s].get(p, 0)) for p in pids) + f" | **{total[s]}** |")
    L += ["", "## Most aligned playbooks", ""]
    for s in sorted(grades, key=lambda s: -total[s])[:8]:
        L.append(f"- **{lab(s)}** (`{s}`, {total[s]}/24) — {grades[s].get('summary', '')}")
    L += ["", "## Least aligned playbooks", ""]
    for s in sorted(grades, key=lambda s: total[s])[:8]:
        L.append(f"- **{lab(s)}** (`{s}`, {total[s]}/24) — biggest gap: {grades[s].get('biggest_gap', '')}")
    L += ["", "## Evidence per playbook", ""]
    for s in sorted(grades):
        L += [f"### {lab(s)} · {total[s]}/24", "", f"`{s}` — {grades[s].get('summary', '')}", ""]
        for i, p in enumerate(pids, 1):
            L.append(f"- P{i} = {score[s].get(p, 0)}: {evid[s].get(p, '')}")
        L += [f"- Biggest gap: {grades[s].get('biggest_gap', '')}", ""]
    (PHILO_DIR / "strategy-alignment.md").write_text("\n".join(L), encoding="utf-8")
    return exemplars


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else PHILO_DIR / "mapping-results.json"
    res = json.loads(src.read_text(encoding="utf-8"))
    kb = load_kb()
    known = set(kb.nodes)
    labels = {i: n.label for i, n in kb.nodes.items()}
    doc = yaml.safe_load(BLUEPRINT.read_text(encoding="utf-8"))
    principles = [{"id": p["id"], "title": p["title"].split(": ", 1)[-1]} for p in doc["principles"]]
    order = ["philosophy_relationship"] + [e["id"] for g in ("sections", "principles", "questions") for e in doc.get(g, [])]
    exts = (res.get("extensions") or {}).get("extensions", [])
    rejected = res.get("rejected", [])
    rej = {(r["node"], r["id"]) for r in rejected}
    mapped, dropped, exts = clean_maps(res.get("maps", []), exts, known, rej)
    exemplars = write_alignment(res.get("align", []), labels, principles, known)
    counts = write_blueprint(mapped, exts, exemplars)
    write_map_md(mapped, exts, labels, order, dropped, rejected)
    print(f"mapped {len(mapped)} philosophy nodes; links: {dict(counts)}; dropped {len(dropped)} unknown ids; "
          f"{len(rejected)} refuted by verification")


if __name__ == "__main__":
    main()
