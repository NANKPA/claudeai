#!/usr/bin/env python3
"""Build the interactive Trading Intelligence Map (explorer.html) from graph.json.

Embeds a compact copy of the graph with a precomputed, community-grouped layout
(so the page renders instantly with physics off), short summaries for every
node, the 9-layer framework band, partition status and the deepest lineage
chains. Writes:
  trading-intelligence/09_knowledge-graph/explorer.html   (standalone document)
  dist/explorer.artifact.html                            (same page without the
                                                          document skeleton, for publishing)
"""
from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ti_lib import KB_ROOT, REPO_ROOT, lineage_chains, load_kb  # noqa: E402

TEMPLATE = Path(__file__).resolve().parent / "explorer_template.html"
GITHUB_BLOB = "https://github.com/NANKPA/claudeai/blob/claude/trading-intelligence-scraper-5ep9cj/trading-intelligence/"

LAYERS = [
    ("L0", "Edge & math", "Is there an edge at all?"),
    ("L1", "Mechanics", "How do orders become prices?"),
    ("L2", "Context", "What state is the market in?"),
    ("L3", "Analysis lens", "Which lens reads that state?"),
    ("L4", "Setups", "What repeatable pattern do I trade?"),
    ("L5", "Execution", "When and how do I get in and out?"),
    ("L6", "Risk", "How much, and can I survive?"),
    ("L7", "Psychology", "Will I actually follow the plan?"),
    ("L8", "Review", "Is the edge real, and still working?"),
]
FAMILY = {  # kind -> (family, shape)
    "concept": ("idea", "dot"), "strategy": ("idea", "diamond"), "formula": ("idea", "hexagon"),
    "framework": ("idea", "hexagon"), "synthesis": ("idea", "hexagon"), "course": ("idea", "square"),
    "track": ("idea", "square"), "person": ("person", "dot"),
    "book": ("source", "square"), "mathbook": ("source", "square"), "paper": ("source", "square"),
    "media": ("source", "triangle"), "podcast": ("source", "star"), "channel": ("source", "star"),
}
PARTITION_INFO = {
    "00_framework": ("Framework", "complete"),
    "01_chart-fanatics": ("Chart Fanatics", "captured"),
    "02_podcasts-interviews": ("Podcasts & interviews", "captured"),
    "03_legends-authorities": ("Legends & authorities", "complete"),
    "04_babypips-school-of-pipsology": ("BabyPips School of Pipsology", "blocked"),
    "05_books-top-100": ("Top-100 trading books", "complete"),
    "06_mathematics-foundations": ("Mathematics foundations", "complete"),
    "07_concepts": ("Concepts", "complete"),
    "08_synthesis": ("Synthesis", "complete"),
}
PARTITION_NOTE = {
    "01_chart-fanatics": "47 first-party playbooks (T2) and the full 1,029-upload catalog. Video transcripts need a home machine (YouTube bot check).",
    "02_podcasts-interviews": "4,460 episodes from 15 shows, 270 linked to known guests, plus the view-ranked top 100.",
    "04_babypips-school-of-pipsology": "11-course map and concept summaries. Lesson text is behind Cloudflare; run the crawler at home.",
    "03_legends-authorities": "Influence lineage across traders, authors and researchers.",
    "05_books-top-100": "Ranked canon with book-to-book lineage and 13 deep summaries.",
    "06_mathematics-foundations": "Six study tracks, formula sheet, and the view-ranked top 100 math videos.",
    "07_concepts": "Atomic notes on every layer, the backbone of the graph.",
    "08_synthesis": "Unified framework, lineage map, consensus and conflicts, checklist.",
    "00_framework": "Ontology, note schema, source tiers, learning path.",
}


def clean_md(text: str, labels: dict[str, str]) -> str:
    text = re.sub(r"\[\[([a-z0-9_]+)\]\]", lambda m: labels.get(m.group(1), m.group(1)), text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def summary_for(node, labels) -> str:
    a = node.attrs
    if node.body:
        for para in re.split(r"\n\s*\n", node.body):
            p = para.strip()
            if not p or p[0] in "#|>`-" or p.startswith(("```", "<!--")) or re.match(r"^\d+\.", p):
                continue
            p = clean_md(p, labels)
            if len(p) >= 60:
                return p[:420] + ("…" if len(p) > 420 else "")
    if node.kind in ("book", "mathbook", "paper"):
        bits = [a.get("author"), str(a.get("year") or ""), a.get("category") or (f"level {a['level']}" if a.get("level") else None)]
        head = " · ".join(b for b in bits if b)
        return f"{head}. {a.get('key_idea', '')}".strip()
    if node.kind == "person":
        head = " · ".join(b for b in (a.get("role"), a.get("era")) if b)
        return f"{head}. {a.get('known_for', '')}".strip(". ") + ("." if a.get("known_for") else "")
    if node.kind == "media":
        head = " · ".join(str(b) for b in (a.get("format"), a.get("year"), a.get("verification")) if b)
        return f"{head}. {a.get('key_takeaways', '')}".strip(". ")
    if node.kind == "podcast":
        return " ".join(b for b in (a.get("focus"), a.get("rank_signal")) if b)
    return a.get("known_for") or a.get("key_idea") or ""


def layout(nodes: list[str], edges: list[tuple[str, str]], community: dict[str, int]) -> dict[str, tuple[float, float]]:
    G = nx.Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    CG = nx.Graph()
    members = defaultdict(list)
    for n in nodes:
        members[community[n]].append(n)
        CG.add_node(community[n])
    for u, v in edges:
        cu, cv = community[u], community[v]
        if cu != cv:
            w = CG.get_edge_data(cu, cv, {}).get("weight", 0) + 1
            CG.add_edge(cu, cv, weight=w)
    centers = nx.spring_layout(CG, weight="weight", seed=11, k=2.2, iterations=300)
    pos: dict[str, tuple[float, float]] = {}
    for cid, mem in members.items():
        sub = G.subgraph(mem)
        local = nx.spring_layout(sub, seed=11, k=0.9 / math.sqrt(max(len(mem), 1)) * 3, iterations=150)
        radius = 34 * math.sqrt(len(mem))
        cx, cy = centers[cid][0] * 760, centers[cid][1] * 760
        for n, (x, y) in local.items():
            pos[n] = (cx + x * radius, cy + y * radius)
    return pos


def main() -> None:
    kb = load_kb()
    graph = json.loads((KB_ROOT / "09_knowledge-graph" / "graph.json").read_text(encoding="utf-8"))
    gnodes = {n["id"]: n for n in graph["nodes"]}
    community = {nid: n["community"] for nid, n in gnodes.items()}
    comm_names = {n["community"]: n.get("community_name") for n in graph["nodes"]}
    labels = {nid: kb.nodes[nid].label for nid in gnodes if nid in kb.nodes}

    ids = sorted(gnodes, key=lambda i: (community[i], i))
    index = {nid: k for k, nid in enumerate(ids)}
    rel_names = sorted({e.relation for e in kb.edges})
    rel_index = {r: k for k, r in enumerate(rel_names)}
    edges = [(index[e.source], index[e.target], rel_index[e.relation], int(e.inferred))
             for e in kb.edges if e.source in index and e.target in index]
    degree = Counter()
    for s, t, _, _ in edges:
        degree[s] += 1
        degree[t] += 1
    pos = layout(ids, [(ids[s], ids[t]) for s, t, _, _ in edges], community)

    nodes_out = []
    for nid in ids:
        node = kb.nodes[nid]
        fam, shape = FAMILY.get(node.kind, ("idea", "dot"))
        x, y = pos[nid]
        a = node.attrs
        nodes_out.append({
            "id": nid, "l": node.label, "k": node.kind, "f": fam, "sh": shape,
            "ly": a.get("layer"), "c": community[nid], "x": round(x, 1), "y": round(y, 1),
            "d": degree[index[nid]], "p": node.source_file.split("/")[0], "sf": node.source_file,
            "st": a.get("status"), "u": a.get("url") or a.get("source_url"), "a": int(node.auto),
            "s": summary_for(node, labels),
        })

    comms = []
    for cid in sorted(set(community.values())):
        mem = [n for n in ids if community[n] == cid]
        xs, ys = [pos[n][0] for n in mem], [pos[n][1] for n in mem]
        cx, cy = sum(xs) / len(xs), sum(ys) / len(ys)
        comms.append({"id": cid, "name": comm_names[cid], "size": len(mem), "x": round(cx, 1), "top": round(min(ys) - 34, 1)})

    layer_counts = Counter(n["ly"] for n in nodes_out if n["ly"])
    part_counts = Counter(n["p"] for n in nodes_out if not n["a"])
    data = {
        "meta": {"nodes": len(ids), "edges": len(edges), "communities": len(comms),
                 "concepts": sum(n["k"] == "concept" for n in nodes_out),
                 "strategies": sum(n["k"] == "strategy" for n in nodes_out),
                 "books": sum(n["k"] == "book" for n in nodes_out),
                 "people": sum(n["k"] == "person" for n in nodes_out),
                 "github": GITHUB_BLOB},
        "rels": rel_names,
        "layers": [{"code": c, "name": nm, "q": q, "n": layer_counts.get(c, 0)} for c, nm, q in LAYERS],
        "communities": comms,
        "nodes": nodes_out,
        "edges": edges,
        "partitions": [{"dir": d, "name": nm, "status": st, "n": part_counts.get(d, 0), "note": PARTITION_NOTE.get(d, "")}
                       for d, (nm, st) in PARTITION_INFO.items()],
        "chains": [[index[c] for c in ch if c in index] for ch in lineage_chains(kb)],
        "start": "concept_liquidity_sweep_reversal",
    }
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    page = TEMPLATE.read_text(encoding="utf-8").replace("__TI_DATA__", payload)
    standalone = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
                  '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                  '</head>\n<body>\n' + page + '\n</body>\n</html>\n')
    out = KB_ROOT / "09_knowledge-graph" / "explorer.html"
    out.write_text(standalone, encoding="utf-8")
    (REPO_ROOT / "dist").mkdir(exist_ok=True)
    (REPO_ROOT / "dist" / "explorer.artifact.html").write_text(page, encoding="utf-8")
    print(f"wrote {out.relative_to(REPO_ROOT)} ({len(standalone) / 1024:.0f} KB) and dist/explorer.artifact.html")


if __name__ == "__main__":
    main()
