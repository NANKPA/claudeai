"""Shared helpers for the trading-intelligence scrapers: polite HTTP, robots.txt,
markdown-with-frontmatter output, and a reachability preflight."""
from __future__ import annotations

import sys
import time
import urllib.robotparser
from pathlib import Path
from urllib.parse import urlparse

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from ti_lib import KB_ROOT, slug  # noqa: E402,F401  (re-exported for scrapers)

USER_AGENT = "trading-intelligence-kb/1.0 (personal research; contact: repo owner)"


class PoliteSession:
    """requests.Session with a fixed delay between calls, retries, and robots.txt."""

    def __init__(self, delay: float = 2.0, respect_robots: bool = True, cookies_file: str | None = None):
        self.delay = delay
        self.respect_robots = respect_robots
        self.session = requests.Session()
        self.session.headers["User-Agent"] = USER_AGENT
        if cookies_file:
            import http.cookiejar
            jar = http.cookiejar.MozillaCookieJar(cookies_file)
            jar.load(ignore_discard=True, ignore_expires=True)
            self.session.cookies = jar  # type: ignore[assignment]
        self._robots: dict[str, urllib.robotparser.RobotFileParser] = {}
        self._last = 0.0

    def allowed(self, url: str) -> bool:
        if not self.respect_robots:
            return True
        host = "{0.scheme}://{0.netloc}".format(urlparse(url))
        rp = self._robots.get(host)
        if rp is None:
            rp = urllib.robotparser.RobotFileParser()
            try:
                resp = self.session.get(host + "/robots.txt", timeout=20)
                rp.parse(resp.text.splitlines() if resp.ok else [])
            except requests.RequestException:
                rp.parse([])
            self._robots[host] = rp
        return rp.can_fetch(USER_AGENT, url)

    def get(self, url: str, **kw) -> requests.Response | None:
        if not self.allowed(url):
            print(f"  robots.txt disallows {url} - skipped", file=sys.stderr)
            return None
        for attempt in range(4):
            wait = self.delay - (time.time() - self._last)
            if wait > 0:
                time.sleep(wait)
            self._last = time.time()
            try:
                resp = self.session.get(url, timeout=30, **kw)
            except requests.RequestException as exc:
                print(f"  {exc.__class__.__name__} on {url} (attempt {attempt + 1})", file=sys.stderr)
                time.sleep(2 ** (attempt + 1))
                continue
            if resp.status_code in (429, 500, 502, 503, 504):
                time.sleep(2 ** (attempt + 2))
                continue
            return resp
        return None


def preflight(url: str) -> None:
    """Fail fast with an actionable message when the network policy blocks a host."""
    try:
        requests.head(url, timeout=15, allow_redirects=True, headers={"User-Agent": USER_AGENT})
    except requests.RequestException as exc:
        host = urlparse(url).netloc
        raise SystemExit(
            f"Cannot reach {host}: {exc.__class__.__name__}.\n"
            f"If you are in a sandbox/cloud session, add {host} to the environment's allowed domains "
            f"(or run this script on your own machine)."
        )


def write_markdown(path: Path, frontmatter: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fm = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000).strip()
    path.write_text(f"---\n{fm}\n---\n\n{body.strip()}\n", encoding="utf-8")


def write_yaml(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")
