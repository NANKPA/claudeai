"""Locate the knowledge base and make the repo's tools importable.

Resolution order:
1. TI_ROOT, if set: a local clone of the repository.
2. The repository this package sits in (editable install: `pip install -e /path/to/claudeai`).
3. A cached download of the public repository from GitHub (installed straight from GitHub with
   `pip install "trading-intelligence[mcp] @ git+https://github.com/NANKPA/claudeai.git"`).
   The first use downloads the default branch as a zip into ~/.cache/trading-intelligence;
   `python -m trading_intelligence --update` refreshes it. Set TI_NO_DOWNLOAD=1 to forbid this.
"""
from __future__ import annotations

import io
import os
import shutil
import sys
import urllib.request
import zipfile
from pathlib import Path

REPO = os.environ.get("TI_REPO", "NANKPA/claudeai")
BRANCH = os.environ.get("TI_BRANCH", "claude/trading-intelligence-scraper-5ep9cj")
CACHE = Path(os.environ.get("TI_CACHE", Path.home() / ".cache" / "trading-intelligence"))


def _is_repo(root: Path) -> bool:
    return (root / "trading-intelligence").is_dir() and (root / "tools" / "ti_lib.py").is_file()


def download(force: bool = False) -> Path:
    """Fetch the public repository (no git needed) into the cache and return its folder."""
    target = CACHE / "claudeai"
    if _is_repo(target) and not force:
        return target
    url = f"https://codeload.github.com/{REPO}/zip/refs/heads/{BRANCH}"
    print(f"trading-intelligence: downloading the knowledge base from {url}", file=sys.stderr)
    with urllib.request.urlopen(url, timeout=120) as resp:
        data = resp.read()
    tmp = CACHE / "download.tmp"
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        z.extractall(tmp)
    top = next(p for p in tmp.iterdir() if p.is_dir())
    shutil.rmtree(target, ignore_errors=True)
    top.rename(target)
    shutil.rmtree(tmp, ignore_errors=True)
    return target


def repo_root() -> Path:
    env = os.environ.get("TI_ROOT")
    if env:
        root = Path(env).expanduser().resolve()
        if not _is_repo(root):
            raise RuntimeError(f"TI_ROOT={root} is not a clone of {REPO}")
        return root
    here = Path(__file__).resolve().parent.parent
    if _is_repo(here):
        return here
    if _is_repo(CACHE / "claudeai"):
        return CACHE / "claudeai"
    if os.environ.get("TI_NO_DOWNLOAD"):
        raise RuntimeError(f"knowledge base not found; clone https://github.com/{REPO} and set TI_ROOT")
    return download()


def ensure_tools_on_path() -> Path:
    root = repo_root()
    for p in (root / "tools", root / "tools" / "philosophy"):
        s = str(p)
        if s not in sys.path:
            sys.path.insert(0, s)
    return root
