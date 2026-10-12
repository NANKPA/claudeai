#!/usr/bin/env python3
"""Where does the owner's philosophy sit in the knowledge graph?

Reads the graph view (09_knowledge-graph/graph.json, the same nodes the explorer draws) and
measures the philosophy two ways:

* as individual nodes (the root `philosophy_relationship`, its 21 sections, 12 principles,
  hypotheses and open questions): degree, PageRank and betweenness ranks;
* as ONE unit: every philosophy node contracted into a single super-node, then ranked against
  every other node (PageRank, betweenness, closeness), with its reach (share of the graph within
  1, 2 and 3 links) and the communities it touches.

It also runs a personalised PageRank seeded on the philosophy, which answers "which concepts,
playbooks, books and people does the philosophy pull in most?", and finds each section's home
community from its neighbours (which part of the graph it is most entangled with).

Writes trading-intelligence/00_philosophy/centrality-report.md and centrality.json.
Usage: python3 tools/philosophy/centrality.py
"""
from __future__ import annotations

import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

import networkx as nx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ti_lib import KB_ROOT  # noqa: E402

PHILO_KINDS = {"philosophy", "principle", "hypothesis", "question"}
ROOT_ID = "philosophy_relationship"
SUPER = "__philosophy__"
OUT_MD = KB_ROOT / "00_philosophy" / "centrality-report.md"
OUT_JSON = KB_ROOT / "00_philosophy" / "centrality.json"


def load_graph() -> tuple[nx.Graph, dict]:
    data = json.loads((KB_ROOT / "09_knowledge-graph" / "graph.json").read_text(encoding="utf-8"))
    G = nx.Graph()
    for n in data["nodes"]:
        G.add_node(n["id"], **{k: n.get(k) for k in ("label", "kind", "community", "community_name", "layer", "partition")})
    for e in data["links"]:
        if G.has_edge(e["source"], e["target"]):
            G[e["source"]][e["target"]]["rels"].append(e["relation"])
        else:
            G.add_edge(e["source"], e["target"], rels=[e["relation"]])
    names = {n["community"]: n.get("community_name") for n in data["nodes"]}
    return G, names


def rank_of(scores: dict[str, float], node: str) -> int:
    ordered = sorted(scores, key=lambda n: -scores[n])
    return ordered.index(node) + 1


def contracted(G: nx.Graph, philo: set[str]) -> nx.Graph:
    H = nx.Graph()
    H.add_nodes_from(n for n in G if n not in philo)
    H.add_node(SUPER)
    for u, v in G.edges:
        a = SUPER if u in philo else u
        b = SUPER if v in philo else v
        if a != b:
            H.add_edge(a, b)
    return H


def short(label: str) -> str:
    return (label or "").split(" (")[0].split(" — ")[0]


def community_units(G: nx.Graph, philo: set[str], names: dict) -> list[dict]:
    """Every community contracted to one unit (the philosophy is one of them). For each unit: weighted
    PageRank and betweenness on the community graph, the number of other communities it links to, and
    its participation coefficient P = 1 - sum_c (w_c / W)^2 (Guimera & Amaral), which is near 1 when a
    unit's outside links are spread evenly over many communities and near 0 when they go to one."""
    unit = {n: ("PHILOSOPHY" if n in philo else G.nodes[n]["community"]) for n in G}
    CG = nx.Graph()
    CG.add_nodes_from(set(unit.values()))
    for u, v in G.edges:
        a, b = unit[u], unit[v]
        if a != b:
            CG.add_edge(a, b, weight=CG.get_edge_data(a, b, {}).get("weight", 0) + 1)
    for _, _, d in CG.edges(data=True):
        d["dist"] = 1.0 / d["weight"]
    pr = nx.pagerank(CG, weight="weight")
    bt = nx.betweenness_centrality(CG, weight="dist")
    size = Counter(unit.values())
    rows = []
    for c in CG:
        w = [d["weight"] for _, _, d in CG.edges(c, data=True)]
        W = sum(w)
        rows.append({"unit": c, "name": "The Philosophy of the Relationship" if c == "PHILOSOPHY" else names.get(c, str(c)),
                     "size": size[c], "outside_links": W, "communities_linked": len(w),
                     "participation": round(1 - sum((x / W) ** 2 for x in w), 3) if W else 0.0,
                     "pagerank": pr[c], "betweenness": bt[c]})
    for key in ("pagerank", "betweenness", "participation"):
        for i, r in enumerate(sorted(rows, key=lambda r: -r[key]), 1):
            r[f"{key}_rank"] = i
    return sorted(rows, key=lambda r: r["pagerank_rank"])


def random_baseline(G: nx.Graph, philo: set[str], trials: int = 200, seed: int = 11) -> dict:
    """Contract random node sets of the philosophy's size (drawn from the rest of the graph) and rank
    the merged node by PageRank, to show how much of the philosophy's rank merging alone explains."""
    rest = G.subgraph([n for n in G if n not in philo]).copy()
    pool = sorted(rest)
    rng = random.Random(seed)
    ranks, reach2 = [], []
    for _ in range(trials):
        sample = set(rng.sample(pool, len(philo)))
        H = contracted(rest, sample)
        pr = nx.pagerank(H)
        ranks.append(rank_of(pr, SUPER))
        dist = nx.single_source_shortest_path_length(H, SUPER, cutoff=2)
        reach2.append(100 * sum(1 for d in dist.values() if 0 < d <= 2) / (H.number_of_nodes() - 1))
    ranks.sort()
    reach2.sort()
    return {"trials": trials, "set_size": len(philo), "median_rank": ranks[len(ranks) // 2],
            "best_rank": ranks[0], "share_rank_1": sum(r == 1 for r in ranks) / trials,
            "median_reach2": round(reach2[len(reach2) // 2], 1), "p95_reach2": round(reach2[int(0.95 * len(reach2))], 1)}


def compute(G: nx.Graph, names: dict) -> dict:
    # The 00_philosophy working documents (blueprint map, alignment, lab, protocol...) are commentary
    # ABOUT the philosophy; their links restate the blueprint, so they are left out of the measurement.
    docs = [n for n, a in G.nodes(data=True) if a.get("partition") == "00_philosophy" and a.get("kind") in ("synthesis", "framework")]
    G.remove_nodes_from(docs)
    philo = {n for n, a in G.nodes(data=True) if a.get("kind") in PHILO_KINDS}
    if ROOT_ID not in G:
        raise SystemExit("philosophy_relationship is not in graph.json; run tools/build_graph.py first")
    n_total = G.number_of_nodes()
    pr = nx.pagerank(G)
    bt = nx.betweenness_centrality(G, k=min(600, n_total), seed=7)
    deg = dict(G.degree)

    H = contracted(G, philo)
    pr_h = nx.pagerank(H)
    bt_h = nx.betweenness_centrality(H, k=min(600, H.number_of_nodes()), seed=7)
    cl_h = nx.closeness_centrality(H, u=SUPER)
    cl_all = {}
    sample = sorted(H, key=lambda n: -H.degree(n))[:150]
    for n in sample:
        cl_all[n] = nx.closeness_centrality(H, u=n)
    cl_all[SUPER] = cl_h
    dist = nx.single_source_shortest_path_length(H, SUPER, cutoff=3)
    reach = {k: round(100 * sum(1 for d in dist.values() if 0 < d <= k) / (H.number_of_nodes() - 1), 1) for k in (1, 2, 3)}

    # communities touched: non-philosophy communities with at least one direct neighbour
    neigh = {m for p in philo for m in G[p] if m not in philo}
    comm_touch = Counter(G.nodes[m]["community"] for m in neigh)
    philo_comm = G.nodes[ROOT_ID]["community"]
    other_comms = {a["community"] for n, a in G.nodes(data=True) if n not in philo}

    # personalised PageRank from the philosophy
    pers = {n: (1.0 if n in philo else 0.0) for n in G}
    ppr = nx.pagerank(G, personalization=pers, alpha=0.85)
    pulled = {}
    for kind in ("concept", "strategy", "book", "mathbook", "paper", "person", "synthesis", "framework"):
        cands = [n for n in G if G.nodes[n].get("kind") == kind]
        pulled[kind] = [(n, ppr[n]) for n in sorted(cands, key=lambda n: -ppr[n])[:10]]

    # home community per philosophy node (majority of non-philosophy neighbours)
    homes = {}
    for p in sorted(philo):
        cs = Counter(G.nodes[m]["community"] for m in G[p] if m not in philo)
        if cs:
            cid, k = cs.most_common(1)[0]
            homes[p] = {"community": cid, "name": names.get(cid), "share": round(k / sum(cs.values()), 2), "spread": len(cs)}

    # which concepts tie the philosophy to the most practitioner playbooks
    bridges = []
    for c in neigh:
        if G.nodes[c].get("kind") != "concept":
            continue
        n_strat = sum(1 for m in G[c] if G.nodes[m].get("kind") == "strategy")
        n_philo = sum(1 for m in G[c] if m in philo)
        bridges.append((c, n_philo, n_strat))
    bridges.sort(key=lambda t: -(t[1] * max(t[2], 1)))

    nodes_tbl = []
    for p in philo:
        nodes_tbl.append({"id": p, "label": G.nodes[p]["label"], "kind": G.nodes[p]["kind"], "degree": deg[p],
                          "pagerank_rank": rank_of(pr, p), "betweenness_rank": rank_of(bt, p)})
    nodes_tbl.sort(key=lambda r: r["pagerank_rank"])

    top_pr = sorted(pr_h, key=lambda n: -pr_h[n])[:12]
    units = community_units(G, philo, names)
    baseline = random_baseline(G, philo)
    return {
        "units": units,
        "baseline": baseline,
        "graph": {"nodes": n_total, "edges": G.number_of_edges(), "communities": len(other_comms) + 1, "philosophy_nodes": len(philo)},
        "root": {"degree": deg[ROOT_ID], "pagerank_rank": rank_of(pr, ROOT_ID), "betweenness_rank": rank_of(bt, ROOT_ID)},
        "super": {"pagerank_rank": rank_of(pr_h, SUPER), "betweenness_rank": rank_of(bt_h, SUPER),
                  "closeness_rank_among_top150": rank_of(cl_all, SUPER), "degree": H.degree(SUPER),
                  "reach_pct": reach, "communities_touched": len(comm_touch), "communities_other": len(other_comms),
                  "top_pagerank": [(n if n != SUPER else "THE PHILOSOPHY (all philosophy nodes as one)", round(pr_h[n], 5)) for n in top_pr]},
        "communities_touched": [(names.get(c), k) for c, k in comm_touch.most_common()],
        "nodes": nodes_tbl,
        "pulled": {k: [(n, G.nodes[n]["label"], round(v, 5)) for n, v in vs] for k, vs in pulled.items()},
        "homes": homes,
        "bridges": [(c, G.nodes[c]["label"], a, b) for c, a, b in bridges[:15]],
        "philosophy_community": names.get(philo_comm),
    }


def fair_comparisons(res: dict) -> list[str]:
    b, units = res["baseline"], res["units"]
    ph = next(u for u in units if u["unit"] == "PHILOSOPHY")
    n = len(units)
    L = ["## Fair comparison 1: every community as one unit", "",
         f"All {n} communities contracted to one node each, the philosophy among them. Links between units are "
         "weighted by how many edges join them.", "",
         f"The philosophy ranks **#{ph['pagerank_rank']} of {n} by PageRank**, **#{ph['betweenness_rank']} by "
         f"betweenness** and **#{ph['participation_rank']} by participation** (participation {ph['participation']}: "
         f"its {ph['outside_links']} outside links reach {ph['communities_linked']} of the other {n - 1} communities).", "",
         "| Rank (PageRank) | Community | Nodes | Outside links | Communities linked | Participation | Betweenness rank |",
         "|---|---|---|---|---|---|---|"]
    for u in units[:12]:
        name = f"**{u['name']}**" if u["unit"] == "PHILOSOPHY" else u["name"]
        L.append(f"| {u['pagerank_rank']} | {name} | {u['size']} | {u['outside_links']} | {u['communities_linked']} | "
                 f"{u['participation']} | {u['betweenness_rank']} |")
    L += ["", "## Fair comparison 2: random sets of the same size", "",
          f"{b['trials']} random sets of {b['set_size']} nodes from the rest of the graph, each contracted into one "
          f"node. Median PageRank rank of the merged random set: **#{b['median_rank']}** (best #{b['best_rank']}; "
          f"rank #1 in {b['share_rank_1']:.0%} of trials). Median reach within 2 links: **{b['median_reach2']}%** "
          f"(95th percentile {b['p95_reach2']}%), against **{res['super']['reach_pct'][2]}%** for the philosophy.", "",
          "So part of the philosophy's headline rank comes from merging alone; the part that does not is what the "
          "comparison with the random sets and with the other communities shows.", ""]
    return L


def render(res: dict, G: nx.Graph) -> str:
    s, r, g = res["super"], res["root"], res["graph"]
    lab = lambda n: short(G.nodes[n]["label"]) if n in G else n  # noqa: E731
    L = ["---", "id: synthesis_philosophy_centrality", "type: synthesis",
         'title: "Centrality — where the Philosophy of the Relationship sits in the graph"',
         "partition: 00_philosophy", "layer: L0",
         "related: [philosophy_relationship, synthesis_blueprint_map, synthesis_strategy_alignment]",
         "status: computed", "---", "",
         "# Centrality — where the Philosophy of the Relationship sits in the graph", "",
         "> Generated by `python3 tools/philosophy/centrality.py` from the graph view "
         "(`09_knowledge-graph/graph.json`). Re-run after `tools/build_graph.py`.", "",
         "## Headline", "",
         f"The measured graph (the explorer's graph view without the 00_philosophy working documents) has "
         f"**{g['nodes']:,} nodes**, **{g['edges']:,} edges** and **{g['communities']} communities**; "
         f"**{g['philosophy_nodes']}** of those nodes are the philosophy (the root, 21 sections, 12 principles, the open "
         "questions and the hypotheses). The 00_philosophy working documents (this report, the blueprint map, the "
         "alignment matrix, the lab, the protocol) are left out of the measurement: they describe the philosophy, and "
         "counting their links would inflate it.", "",
         "Treated as **one unit** (all philosophy nodes contracted into a single node):", "",
         "| Measure | Value |", "|---|---|",
         f"| PageRank rank | **#{s['pagerank_rank']}** of {g['nodes'] - g['philosophy_nodes'] + 1:,} |",
         f"| Betweenness rank (bridging) | **#{s['betweenness_rank']}** |",
         f"| Closeness rank among the 150 best-connected nodes | **#{s['closeness_rank_among_top150']}** |",
         f"| Direct links to the rest of the graph | {s['degree']:,} |",
         f"| Reach within 1 / 2 / 3 links | {s['reach_pct'][1]}% / {s['reach_pct'][2]}% / {s['reach_pct'][3]}% of the graph |",
         f"| Communities touched directly | {s['communities_touched']} of {s['communities_other']} |", "",
         "The root note alone (`philosophy_relationship`): "
         f"degree {r['degree']}, PageRank rank #{r['pagerank_rank']}, betweenness rank #{r['betweenness_rank']}.", "",
         "How to read this: PageRank asks \"how much of the graph's linking flows into this node\"; betweenness asks "
         "\"how many shortest paths between other ideas pass through it\". **Caveat:** contracting dozens of nodes into "
         "one adds up their links, so a merged unit outranks single nodes almost automatically. The two fair "
         "comparisons below control for that.", "",
         *fair_comparisons(res),
         "## The most central nodes when the philosophy counts as one", "",
         "| # | Node | PageRank |", "|---|---|---|"]
    for i, (n, v) in enumerate(s["top_pagerank"], 1):
        L.append(f"| {i} | {lab(n) if n in G else n} | {v} |")
    L += ["", "## Communities the philosophy touches", "",
          "Number of direct links from philosophy nodes into each community.", "",
          "| Community | Links |", "|---|---|"]
    L += [f"| {c} | {k} |" for c, k in res["communities_touched"]]
    L += ["", "## What the philosophy pulls in most (personalised PageRank)", "",
          "A random walk that keeps restarting from the philosophy: these are the nodes it visits most. "
          "This is the part of the knowledge base the philosophy is built on.", ""]
    titles = {"concept": "Concepts", "strategy": "Practitioner playbooks", "book": "Books", "mathbook": "Mathematics books",
              "paper": "Papers", "person": "People", "synthesis": "Synthesis notes", "framework": "Frameworks"}
    for k, rows in res["pulled"].items():
        if not rows:
            continue
        L.append(f"**{titles[k]}:** " + ", ".join(f"{short(lbl)} (`{n}`)" for n, lbl, _v in rows[:8]))
        L.append("")
    L += ["## Bridge concepts", "",
          "Concepts linked to several philosophy nodes AND used by many playbooks: the places where the philosophy "
          "meets practice.", "", "| Concept | Philosophy links | Playbooks using it |", "|---|---|---|"]
    L += [f"| {short(lbl)} (`{c}`) | {a} | {b} |" for c, lbl, a, b in res["bridges"]]
    L += ["", "## Each section's home in the graph", "",
          "For every philosophy node, the community that holds most of its non-philosophy neighbours (share of its "
          "links) and how many communities it reaches.", "",
          "| Node | Home community | Share | Communities reached |", "|---|---|---|---|"]
    order = [n for n in res["homes"] if n.startswith("philo")] + [n for n in res["homes"] if n.startswith("principle")]
    for n in order:
        h = res["homes"][n]
        L.append(f"| {lab(n)} (`{n}`) | {h['name']} | {int(h['share'] * 100)}% | {h['spread']} |")
    L += ["", "## Philosophy nodes ranked", "", "| Node | Kind | Degree | PageRank rank | Betweenness rank |", "|---|---|---|---|---|"]
    for row in res["nodes"][:40]:
        L.append(f"| {short(row['label'])} (`{row['id']}`) | {row['kind']} | {row['degree']} | #{row['pagerank_rank']} | #{row['betweenness_rank']} |")
    L += ["", "## Method notes", "",
          "- The graph view leaves out YouTube shorts and podcast episodes with no known guest (see "
          "`09_knowledge-graph/BUILD_REPORT.md`).",
          "- Betweenness is estimated from 600 sampled sources (seed 7); ranks near the top are stable, deep ranks are approximate.",
          "- The philosophy's links come from `00_philosophy/blueprint.yaml` (mapped by agents, rationale for every link in "
          "`blueprint-map.md`) and from wikilinks in the 00_philosophy notes. Its centrality therefore measures how much of "
          "the existing knowledge base the philosophy was found to rest on, support or challenge; it is not evidence that "
          "the philosophy is profitable (see `evidence-lab.md` and `hypotheses.md` for that).", ""]
    return "\n".join(L)


def main() -> None:
    G, names = load_graph()
    res = compute(G, names)
    OUT_JSON.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
    OUT_MD.write_text(render(res, G), encoding="utf-8")
    s = res["super"]
    print(f"philosophy as one unit: PageRank #{s['pagerank_rank']}, betweenness #{s['betweenness_rank']}, "
          f"reach {s['reach_pct']}, communities {s['communities_touched']}/{s['communities_other']}")
    print(f"wrote {OUT_MD.relative_to(KB_ROOT)}")


if __name__ == "__main__":
    main()
