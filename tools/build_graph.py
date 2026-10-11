#!/usr/bin/env python3
"""Compile the trading-intelligence knowledge base into a graphify knowledge graph.

Pipeline:
  1. ti_lib.load_kb()  -> nodes + typed edges from frontmatter, wikilinks and registries
  2. emit a graphify extraction (nodes/edges with EXTRACTED/INFERRED confidence)
  3. graphify: build_from_json -> cluster (Leiden) -> score -> god nodes ->
     surprising connections -> suggested questions -> report -> graph.json ->
     graph.html -> wiki
  4. label communities from anchor concepts (deterministic) and write BUILD_REPORT.md

Usage: python3 tools/build_graph.py [--no-wiki]
"""
from __future__ import annotations

import argparse
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ti_lib import FILE_TYPE_BY_KIND, KB_ROOT, load_kb  # noqa: E402

OUT_DIR = KB_ROOT / "09_knowledge-graph"

# Community naming: if a community contains one of these anchors, it is named
# after the first (highest-priority) anchor present. Otherwise it falls back to
# the community's highest-degree concept-like nodes.
ANCHOR_LABELS: list[tuple[str, str]] = [
    ("concept_auction_market_theory", "Auction Market Theory & Order Flow"),
    ("concept_smart_money_concepts", "Smart Money / ICT & Liquidity"),
    ("concept_liquidity_sweep_reversal", "Liquidity Sweeps & Reversals"),
    ("concept_wyckoff_method", "Wyckoff, Tape Reading & AMD"),
    ("concept_trend_following", "Trend Following & the Turtles"),
    ("concept_growth_momentum_canslim", "Growth-Stock Momentum (CANSLIM→VCP→EP)"),
    ("concept_kelly_criterion_optimal_f", "Kelly, Sizing & Money Management"),
    ("concept_position_sizing", "Position Sizing & Risk"),
    ("concept_trading_psychology", "Psychology, Plan & Discipline"),
    ("concept_overfitting_validation", "Backtesting, ML & Edge Validation"),
    ("concept_machine_learning_finance", "Quant ML & Validation"),
    ("concept_optimal_execution_market_impact", "Microstructure & Optimal Execution"),
    ("concept_market_microstructure", "Market Microstructure"),
    ("concept_stochastic_processes", "Stochastic Calculus, Options & Derivatives"),
    ("concept_options_greeks", "Options & Volatility"),
    ("concept_probability_fat_tails", "Probability, Expectancy & Fat Tails"),
    ("concept_random_walk_efficient_markets", "Efficient Markets Debate"),
    ("concept_fundamental_macro_analysis", "Macro, Fundamentals & Reflexivity"),
    ("concept_chart_patterns", "Classical Charting & Patterns"),
    ("concept_oscillators_momentum", "Indicators & Oscillators"),
    ("concept_candlestick_patterns", "Candlesticks & Price Action"),
    ("concept_elliott_wave", "Elliott Wave & Fibonacci"),
    ("concept_market_structure", "Market Structure & Context"),
    ("concept_trading_sessions_killzones", "Sessions, Time & Kill Zones"),
    ("concept_trading_journal_review", "Journal, Review & Metrics"),
    ("course_babypips_school_of_pipsology", "BabyPips School of Pipsology"),
    ("channel_chart_fanatics", "Chart Fanatics Ecosystem"),
    ("podcast_chat_with_traders", "Trading Podcasts"),
]


def to_extraction(kb) -> dict:
    nodes = []
    for n in kb.nodes.values():
        a = n.attrs
        nodes.append({
            "id": n.id,
            "label": n.label,
            "file_type": FILE_TYPE_BY_KIND.get(n.kind, "concept"),
            "source_file": n.source_file,
            "source_location": None,
            "source_url": a.get("url") or a.get("source_url"),
            "captured_at": a.get("captured_at"),
            "author": a.get("author") if isinstance(a.get("author"), str) else None,
            "contributor": "trading-intelligence",
            # domain attributes (graphify keeps extra keys on nodes)
            "kind": n.kind,
            "layer": a.get("layer"),
            "partition": n.source_file.split("/")[0],
            "status": a.get("status"),
            "auto_created": bool(n.auto),
        })
    edges = []
    for e in kb.edges:
        edges.append({
            "source": e.source,
            "target": e.target,
            "relation": e.relation,
            "confidence": "INFERRED" if e.inferred else "EXTRACTED",
            "confidence_score": 0.75 if e.inferred else 1.0,
            "source_file": e.source_file,
            "source_location": None,
            "weight": 0.75 if e.inferred else 1.0,
        })
    return {"nodes": nodes, "edges": edges, "hyperedges": [], "input_tokens": 0, "output_tokens": 0}


def label_communities(G, communities: dict[int, list[str]]) -> dict[int, str]:
    labels: dict[int, str] = {}
    used: Counter = Counter()
    for cid, members in communities.items():
        mset = set(members)
        name = next((lbl for anchor, lbl in ANCHOR_LABELS if anchor in mset), None)
        if name is None:
            ranked = sorted(
                (m for m in members if G.nodes[m].get("kind") in ("concept", "strategy", "course", "channel", "podcast", "synthesis", "framework", "track")),
                key=lambda m: -G.degree(m),
            ) or sorted(members, key=lambda m: -G.degree(m))
            name = " / ".join(G.nodes[m].get("label", m).split(" (")[0] for m in ranked[:2])
        used[name] += 1
        labels[cid] = name if used[name] == 1 else f"{name} ({used[name]})"
    return labels


def build_report(kb, G, communities, labels, gods) -> str:
    kinds = Counter(n.kind for n in kb.nodes.values())
    layers = Counter(n.attrs.get("layer") for n in kb.nodes.values() if n.attrs.get("layer"))
    rels = Counter(e.relation for e in kb.edges)
    lines = ["# Build Report — Trading Intelligence Knowledge Graph\n",
             f"- **{G.number_of_nodes()} nodes · {G.number_of_edges()} edges · {len(communities)} communities**",
             f"- Inferred (lower-confidence) edges: {sum(e.inferred for e in kb.edges)}",
             f"- Dangling references: {len(kb.errors)}\n",
             "## Nodes by kind\n", "| Kind | Count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in kinds.most_common()]
    lines += ["\n## Notes by layer (L0–L8)\n", "| Layer | Count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(layers.items())]
    lines += ["\n## Edges by relation\n", "| Relation | Count |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in rels.most_common()]
    lines += ["\n## Communities\n", "| # | Name | Size | Top members |", "|---|---|---|---|"]
    for cid in sorted(communities, key=lambda c: -len(communities[c])):
        top = sorted(communities[cid], key=lambda m: -G.degree(m))[:6]
        lines.append(f"| {cid} | {labels[cid]} | {len(communities[cid])} | " + ", ".join(G.nodes[m].get("label", m) for m in top) + " |")
    lines += ["\n## Hub nodes (highest degree)\n", "| Node | Kind | Degree |", "|---|---|---|"]
    for g in gods[:25]:
        nid = g.get("id") or g.get("node")
        if nid in G:
            lines.append(f"| {G.nodes[nid].get('label', nid)} | {G.nodes[nid].get('kind')} | {G.degree(nid)} |")
    # Lineage: longest derived_from / influenced_by chains
    parents = defaultdict(list)
    for e in kb.edges:
        if e.relation in ("derived_from", "influenced_by"):
            parents[e.source].append(e.target)

    def depth(n, seen=()):
        if n in seen or not parents.get(n):
            return [n]
        best = max((depth(p, seen + (n,)) for p in parents[n]), key=len)
        return [n] + best

    chains = sorted((depth(n) for n in parents), key=len, reverse=True)
    lines += ["\n## Deepest idea-lineage chains\n"]
    shown = set()
    for ch in chains:
        key = ch[-1], len(ch)
        if key in shown or len(ch) < 3:
            continue
        shown.add(key)
        lines.append("- " + " → ".join(kb.nodes[c].label.split(" (")[0].split(" — ")[0] for c in ch))
        if len(shown) >= 15:
            break
    if kb.errors:
        lines += ["\n## Dangling references\n"] + [f"- {e}" for e in kb.errors]
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-wiki", action="store_true")
    args = ap.parse_args()

    from graphify.analyze import god_nodes, suggest_questions, surprising_connections
    from graphify.build import build_from_json
    from graphify.cluster import cluster, score_all
    from graphify.detect import detect
    from graphify.export import to_html, to_json
    from graphify.report import generate
    from graphify.validate import validate_extraction

    kb = load_kb()
    if kb.errors:
        print(f"warning: {len(kb.errors)} dangling references (see BUILD_REPORT.md)", file=sys.stderr)
    extraction = to_extraction(kb)
    problems = validate_extraction(extraction)
    if problems:
        raise SystemExit("extraction invalid:\n" + "\n".join(problems[:20]))

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "extraction.json").write_text(json.dumps(extraction, indent=1, ensure_ascii=False), encoding="utf-8")

    G = build_from_json(extraction, root=str(KB_ROOT), directed=False, dedup=False)
    communities = cluster(G)
    cohesion = score_all(G, communities)
    gods = god_nodes(G, top_n=25)
    surprises = surprising_connections(G, communities)
    labels = label_communities(G, communities)
    questions = suggest_questions(G, communities, labels)

    detection = detect(KB_ROOT)
    graph_json = OUT_DIR / "graph.json"
    if graph_json.exists():
        graph_json.unlink()  # full rebuild: bypass graphify's shrink guard
    to_json(G, communities, str(graph_json), community_labels=labels)
    report = generate(G, communities, cohesion, labels, gods, surprises, detection,
                      {"input": 0, "output": 0}, "trading-intelligence", suggested_questions=questions)
    (OUT_DIR / "GRAPH_REPORT.md").write_text(report, encoding="utf-8")
    to_html(G, communities, str(OUT_DIR / "graph.html"), community_labels=labels)
    (OUT_DIR / "community_labels.json").write_text(json.dumps({str(k): v for k, v in labels.items()}, indent=1), encoding="utf-8")
    if not args.no_wiki:
        from graphify.wiki import to_wiki
        wiki_dir = OUT_DIR / "wiki"
        if wiki_dir.exists():
            shutil.rmtree(wiki_dir)
        n = to_wiki(G, communities, str(wiki_dir), community_labels=labels, cohesion=cohesion, god_nodes_data=gods)
        print(f"wiki: {n} articles")
    (OUT_DIR / "BUILD_REPORT.md").write_text(build_report(kb, G, communities, labels, gods), encoding="utf-8")
    print(f"graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges, {len(communities)} communities")
    for cid in sorted(communities, key=lambda c: -len(communities[c])):
        print(f"  [{cid:>2}] {labels[cid]} ({len(communities[cid])})")


if __name__ == "__main__":
    main()
