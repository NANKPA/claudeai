#!/usr/bin/env python3
"""Connect scraped videos to the people in them and to those people's playbooks.

The cloud scrape of the Chart Fanatics channel captured titles only (descriptions and transcripts
need a home machine). A title that names a known trader ("... - Tori Trades", "with Jared Tendler")
is enough to link the video to that person (`speaker_ids`) and to every playbook the person teaches
(`covers`). Run after the scrapers; idempotent. When transcripts arrive, the scrapers' own concept
tagging adds the content links on top.

Usage: python3 tools/link_media.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ti_lib import KB_ROOT, load_kb  # noqa: E402

FILES = ["01_chart-fanatics/catalog.scraped.yaml", "02_podcasts-interviews/landmark-media.scraped.yaml",
         "06_mathematics-foundations/lectures.scraped.yaml"]


def main() -> None:
    kb = load_kb(include_raw=False)
    names: dict[str, str] = {}
    for pid, n in kb.nodes.items():
        if n.kind != "person" or n.auto:
            continue
        for a in [str(n.attrs.get("name") or n.label)] + [str(v) for v in (n.attrs.get("aliases") or [])]:
            if len(a) >= 5:
                names[a.lower()] = pid
    teaches: dict[str, set[str]] = {}
    for e in kb.edges:
        if e.relation == "taught_by" and kb.nodes[e.source].kind == "strategy":
            teaches.setdefault(e.target, set()).add(e.source)
    patterns = [(re.compile(r"\b" + re.escape(a) + r"\b"), pid) for a, pid in sorted(names.items(), key=lambda x: -len(x[0]))]
    for rel in FILES:
        path = KB_ROOT / rel
        if not path.exists():
            continue
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        key = next((k for k, v in data.items() if isinstance(v, list)), None)
        if key is None:
            continue
        added_people = added_plays = 0
        for item in data[key]:
            text = f"{item.get('title') or ''} {item.get('description') or ''}".lower()
            found = {pid for rx, pid in patterns if rx.search(text)}
            if not found:
                continue
            sp = list(item.get("speaker_ids") or [])
            for pid in sorted(found):
                if pid not in sp:
                    sp.append(pid)
                    added_people += 1
            item["speaker_ids"] = sp
            cov = list(item.get("covers") or [])
            for pid in sorted(found):
                for sid in sorted(teaches.get(pid, ())):
                    if sid not in cov:
                        cov.append(sid)
                        added_plays += 1
            item["covers"] = cov
        text = path.read_text(encoding="utf-8")
        header = "".join(line + "\n" for line in text.splitlines() if line.startswith("#"))
        path.write_text(header + yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=200), encoding="utf-8")
        print(f"{rel}: +{added_people} person links, +{added_plays} playbook links")


if __name__ == "__main__":
    main()
