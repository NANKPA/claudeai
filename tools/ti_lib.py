"""Shared loader for the trading-intelligence knowledge base.

Reads every markdown note (YAML frontmatter) and every YAML registry under
``trading-intelligence/`` and normalises them into a single list of nodes and
edges. ``build_graph.py``, ``render_registries.py`` and ``bundle_for_claude.py``
all build on this so the three views can never drift apart.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
KB_ROOT = REPO_ROOT / "trading-intelligence"

# Frontmatter / registry keys whose values are lists of target ids, mapped to the
# relation name stored on the edge (source -> target).
RELATION_KEYS: dict[str, str] = {
    "related": "related",
    "derived_from": "derived_from",
    "influenced_by": "influenced_by",
    "uses": "uses",
    "covers": "covers",
    "teaches": "teaches",
    "taught_by": "taught_by",
    "featured_in": "featured_in",
    "hosted_by": "hosted_by",
    "hosts": "hosted_by",
    "founded_by": "founded_by",
    "part_of": "part_of",
    "contrasts_with": "contrasts_with",
    "validates": "validates",
    "challenges": "challenges",
    "authors": "authored_by",
    "features": "features",
    "speaker_ids": "features_speaker",
    # Philosophy layer (00_philosophy): how the owner's principles connect to the rest.
    "grounded_in": "grounded_in",
    "supported_by": "supported_by",
    "challenged_by": "challenged_by",
    "operationalized_by": "operationalized_by",
    "exemplified_by": "exemplified_by",
    "expresses": "expresses",
    "tests": "tests",
    "tested_by": "tested_by",
    "answers": "answers",
}
# Scalar keys that point at one id.
SCALAR_RELATION_KEYS: dict[str, str] = {
    "track": "part_of",
    "also_in_top100": "same_as",
}

# Our node kinds -> graphify's six allowed file_type values.
FILE_TYPE_BY_KIND = {
    "book": "paper",
    "mathbook": "paper",
    "paper": "paper",
    "media": "document",
    "podcast": "document",
    "channel": "document",
    "course": "document",
    "track": "document",
    "framework": "rationale",
    "synthesis": "rationale",
    "formula": "concept",
    "concept": "concept",
    "strategy": "concept",
    "person": "concept",
    "philosophy": "rationale",
    "principle": "rationale",
    "hypothesis": "rationale",
    "question": "rationale",
}

ID_PREFIX_KIND = {
    "concept_": "concept",
    "strategy_": "strategy",
    "person_": "person",
    "book_": "book",
    "mathbook_": "mathbook",
    "paper_": "paper",
    "podcast_": "podcast",
    "media_": "media",
    "course_": "course",
    "channel_": "channel",
    "formula_": "formula",
    "framework_": "framework",
    "synthesis_": "synthesis",
    "track_": "track",
    "lesson_": "course",
    "philosophy_": "philosophy",
    "philo_": "philosophy",
    "principle_": "principle",
    "hypothesis_": "hypothesis",
    "question_": "question",
}

ID_RE = re.compile(r"^[a-z0-9_]+$")
WIKILINK_RE = re.compile(r"\[\[([a-z0-9_]+)\]\]")
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.S)


def kind_of(node_id: str) -> str:
    for prefix, kind in ID_PREFIX_KIND.items():
        if node_id.startswith(prefix):
            return kind
    return "concept"


def slug(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def label_from_id(node_id: str) -> str:
    stem = node_id.split("_", 1)[1] if "_" in node_id else node_id
    return " ".join(w.capitalize() for w in stem.split("_"))


@dataclass
class Edge:
    source: str
    target: str
    relation: str
    inferred: bool
    source_file: str


@dataclass
class Node:
    id: str
    label: str
    kind: str
    source_file: str
    attrs: dict = field(default_factory=dict)
    body: str = ""
    auto: bool = False


@dataclass
class KnowledgeBase:
    nodes: dict[str, Node]
    edges: list[Edge]
    errors: list[str]
    warnings: list[str]


def parse_frontmatter(path: Path) -> tuple[dict | None, str]:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)) or {}, m.group(2)


def _iter_ids(value) -> list[tuple[str, bool]]:
    """Normalise a relation value to [(id, inferred)]; a trailing '?' marks INFERRED."""
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    out = []
    for item in items:
        if not isinstance(item, str):
            continue
        item = item.strip()
        inferred = item.endswith("?")
        out.append((item.rstrip("?"), inferred))
    return out


def _registry_entries(data: dict) -> list[dict]:
    """Every list-of-mappings value in a registry file is a list of entities."""
    entries: list[dict] = []
    for key, value in (data or {}).items():
        if key in {"discovery_queries"}:
            continue
        if isinstance(value, list):
            entries.extend(v for v in value if isinstance(v, dict) and "id" in v)
    return entries


class _Builder:
    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.edges: list[Edge] = []
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def add_entity(self, entity: dict, source_file: str, body: str = "") -> None:
        node_id = str(entity["id"])
        if not ID_RE.match(node_id):
            self.errors.append(f"{source_file}: invalid id {node_id!r} (use [a-z0-9_])")
            return
        label = entity.get("title") or entity.get("name") or label_from_id(node_id)
        kind = entity.get("type") or kind_of(node_id)
        attrs = {k: v for k, v in entity.items() if k not in RELATION_KEYS and k not in ("id",)}
        existing = self.nodes.get(node_id)
        if existing is None:
            self.nodes[node_id] = Node(node_id, str(label), kind, source_file, attrs, body)
        elif "ref" in existing.attrs and "ref" not in attrs:
            # The first sighting was only a cross-reference stub; the full entry wins.
            existing.label, existing.kind, existing.source_file = str(label), kind, source_file
            existing.attrs = {**existing.attrs, **attrs}
            existing.attrs.pop("ref", None)
            existing.body = body or existing.body
        elif existing.label == label_from_id(node_id) and (entity.get("title") or entity.get("name")):
            # The first sighting had no title (an id-only stub): the titled entry wins.
            existing.label, existing.kind = str(label), entity.get("type") or existing.kind
            existing.attrs.update(attrs)
            if body and len(body) > len(existing.body):
                existing.body, existing.source_file = body, source_file
        else:
            # Merge: a registry entry and a summary note may describe the same node.
            # Registry label wins (it is the canonical title); the longer body wins.
            if source_file.endswith(".yaml") and existing.source_file.endswith(".md") and (entity.get("title") or entity.get("name")):
                existing.label = str(label)
                existing.attrs.update(attrs)
            else:
                for k, v in attrs.items():
                    existing.attrs.setdefault(k, v)
            if body and len(body) > len(existing.body):
                existing.body = body
                existing.source_file = source_file

        for key, relation in RELATION_KEYS.items():
            for target, inferred in _iter_ids(entity.get(key)):
                self.edges.append(Edge(node_id, target, relation, inferred, source_file))
        for key, relation in SCALAR_RELATION_KEYS.items():
            for target, inferred in _iter_ids(entity.get(key)):
                self.edges.append(Edge(node_id, target, relation, inferred, source_file))
        for target in WIKILINK_RE.findall(body):
            if target != node_id:
                self.edges.append(Edge(node_id, target, "related", False, source_file))

    def finalize(self) -> KnowledgeBase:
        # Auto-create referenced people (e.g. book co-authors) so authorship edges
        # resolve without hand-maintaining every author in people.yaml.
        for e in self.edges:
            if e.target not in self.nodes and e.target.startswith("person_"):
                self.nodes[e.target] = Node(
                    e.target, label_from_id(e.target), "person", e.source_file,
                    {"auto_created": True}, auto=True,
                )
        kept: list[Edge] = []
        seen: set[tuple[str, str, str]] = set()
        for e in self.edges:
            if e.target not in self.nodes:
                self.errors.append(f"{e.source_file}: dangling reference {e.source} -[{e.relation}]-> {e.target}")
                continue
            if e.source == e.target:
                continue
            key = (e.source, e.target, e.relation)
            if key in seen:
                continue
            seen.add(key)
            kept.append(e)
        return KnowledgeBase(self.nodes, kept, self.errors, self.warnings)


def load_kb(root: Path = KB_ROOT, include_raw: bool = True) -> KnowledgeBase:
    b = _Builder()
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(("09_knowledge-graph/", "graphify-out/")):
            continue
        if "/raw/" in f"/{rel}" and not include_raw:
            continue
        fm, body = parse_frontmatter(path)
        if not fm:
            continue  # generated tables and plain docs carry no node
        if "id" not in fm:
            b.warnings.append(f"{rel}: frontmatter without id - skipped")
            continue
        b.add_entity(fm, rel, body)
    for path in sorted(root.rglob("*.yaml")):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(("09_knowledge-graph/", "graphify-out/")) or rel.endswith(".enriched.yaml"):
            continue  # enrichment files are QA metadata (Open Library lookups), not nodes
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        for entity in _registry_entries(data):
            alias = entity.get("also_in_top100")
            if alias:
                # The same book listed in two registries: fold it into one node,
                # keeping the extra relations (e.g. its math track).
                entity = {k: v for k, v in entity.items() if k not in ("also_in_top100", "title", "key_idea")}
                entity["id"] = alias
            b.add_entity(entity, rel)
    return b.finalize()


def lineage_chains(kb: KnowledgeBase, limit: int = 10, min_len: int = 3) -> list[list[str]]:
    """Deepest idea-lineage chains (descendant first). Follows `derived_from` edges and
    person-to-person `influenced_by` edges; a concept's `influenced_by` person credits a
    contributor rather than an ancestor idea, so it is not followed here. One chain per root path."""
    parents: dict[str, list[str]] = {}
    for e in kb.edges:
        src_kind = kb.nodes[e.source].kind
        if e.relation == "derived_from" or (e.relation == "influenced_by" and src_kind == "person"):
            parents.setdefault(e.source, []).append(e.target)

    def deepest(n: str, seen: tuple = ()) -> list[str]:
        if n in seen or not parents.get(n):
            return [n]
        return [n] + max((deepest(p, seen + (n,)) for p in parents[n]), key=len)

    out: list[list[str]] = []
    roots_seen: set[tuple[str, ...]] = set()
    for chain in sorted((deepest(n) for n in parents), key=len, reverse=True):
        key = tuple(chain[-3:])
        if len(chain) < min_len or key in roots_seen:
            continue
        roots_seen.add(key)
        out.append(chain)
        if len(out) >= limit:
            break
    return out
