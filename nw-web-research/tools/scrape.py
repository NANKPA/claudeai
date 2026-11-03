"""Notion World web research scraper.

Visits each target page politely (robots.txt checked, delay between pages),
takes full-page screenshots at 1440 and 390 wide, and records UI patterns as JSON.
Usage: python scrape.py <out_dir> <targets.json> [only_key ...]
"""
import json, re, sys, time, random, urllib.robotparser, urllib.parse, urllib.request
from pathlib import Path
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

OUT = Path(sys.argv[1]); TARGETS = json.loads(Path(sys.argv[2]).read_text())
ONLY = set(sys.argv[3:])
SHOTS = OUT / "screenshots"; RECS = OUT / "records"
SHOTS.mkdir(parents=True, exist_ok=True); RECS.mkdir(parents=True, exist_ok=True)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")
DELAY = (4, 7)
_robots = {}


def robots_ok(url):
    p = urllib.parse.urlparse(url)
    base = f"{p.scheme}://{p.netloc}"
    if base not in _robots:
        rp = urllib.robotparser.RobotFileParser()
        try:
            req = urllib.request.Request(base + "/robots.txt", headers={"User-Agent": UA})
            txt = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", "ignore")
            rp.parse(txt.splitlines())
        except Exception:
            rp = None  # unreachable robots.txt -> treat as allowed
        _robots[base] = rp
    rp = _robots[base]
    return True if rp is None else rp.can_fetch("*", url)


EXTRACT_JS = r"""
() => {
  const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.display !== 'none'; };
  const txt = el => (el.innerText || el.getAttribute('aria-label') || '').trim().replace(/\s+/g,' ').slice(0,60);
  const out = {};
  const header = [...document.querySelectorAll('header, [role="banner"], [class*="header" i], header-navigation, [class*="navbar" i], [class*="topbar" i]')]
    .filter(e => { const r = e.getBoundingClientRect(); return r.top <= 60 && r.height >= 30 && r.height < 400 && r.width >= innerWidth * 0.8; })
    .sort((a,b) => b.getBoundingClientRect().height - a.getBoundingClientRect().height)[0];
  if (header) {
    const s = getComputedStyle(header);
    out.header = { tag: header.tagName, position: s.position, top: s.top, bg: s.backgroundColor,
      backdrop: s.backdropFilter || s.webkitBackdropFilter, height: Math.round(header.getBoundingClientRect().height),
      zIndex: s.zIndex };
    out.header.sticky = ['fixed','sticky'].includes(s.position);
    out.header.transparent = /rgba\(.*,\s*0\)|transparent/.test(s.backgroundColor);
    out.header.glass = !!(out.header.backdrop && out.header.backdrop !== 'none');
  }
  const nav = header || document.querySelector('nav, [role="navigation"]');
  if (nav) out.nav = [...nav.querySelectorAll('a, button')].filter(vis).map(txt).filter(Boolean).slice(0,40);
  const first = [...document.querySelectorAll('main > *, #MainContent > *, main section, body > div section')].find(e => e.getBoundingClientRect().height > 200);
  if (first) out.hero = { video: !!first.querySelector('video'), images: first.querySelectorAll('img,picture').length,
    height: Math.round(first.getBoundingClientRect().height), vh: Math.round(first.getBoundingClientRect().height / innerHeight * 100),
    text: txt(first), carousel: !!first.querySelector('[class*="swiper" i],[class*="slider" i],[class*="carousel" i],[class*="slick" i],[class*="flickity" i]') };
  const links = [...document.querySelectorAll('a[href*="/products/"], a[href*="/product/"], a[href*="/p/"], a[href*="/shop/"]')];
  const card = links.map(a => a.closest('li, article, [class*="card" i], [class*="product" i]') || a).find(c => c.querySelector('img'));
  if (card) {
    const img = card.querySelector('img'); const r = img.getBoundingClientRect();
    out.productCard = { classes: (card.className||'').toString().slice(0,120),
      imageRatio: r.height ? +(r.width / r.height).toFixed(2) : null,
      imagesInCard: card.querySelectorAll('img').length,
      hoverSwapLikely: card.querySelectorAll('img').length > 1,
      quickAdd: /quick|add to|\+/i.test(card.innerText) || !!card.querySelector('[class*="quick" i]'),
      swatches: !!card.querySelector('[class*="swatch" i],[class*="color" i] input,[class*="colour" i]'),
      badges: [...card.querySelectorAll('[class*="badge" i],[class*="tag" i],[class*="label" i]')].map(txt).filter(Boolean).slice(0,5),
      text: txt(card) };
  }
  out.productLinkCount = links.length;
  out.filterSort = { filterEls: [...document.querySelectorAll('[class*="filter" i], [id*="filter" i], facet-filters-form, details[class*="facet" i]')].filter(vis).length,
    sortEls: [...document.querySelectorAll('select[name*="sort" i], [class*="sort" i]')].filter(vis).map(txt).slice(0,5) };
  const body = document.body.innerText;
  out.pdp = { sizeButtons: [...document.querySelectorAll('[class*="size" i] button, [class*="size" i] input, [class*="size" i] label, fieldset label')].filter(vis).map(txt).filter(t=>t.length<8).slice(0,12),
    sizeGuide: /size (guide|chart)|fit guide/i.test(body),
    accordions: [...document.querySelectorAll('details summary, [aria-expanded], [class*="accordion" i] button')].filter(vis).map(txt).filter(Boolean).slice(0,15),
    deliveryCopy: (body.match(/[^\n]*(deliver|shipping|returns?)[^\n]*/gi) || []).map(s=>s.trim().slice(0,140)).slice(0,6),
    crossSell: (body.match(/(you may also like|complete the look|recommended|pairs well|wear it with|similar)[^\n]*/gi) || []).slice(0,4),
    addToCart: [...document.querySelectorAll('button, input[type=submit]')].filter(vis).map(txt).filter(t=>/add to (bag|cart)|buy/i.test(t)).slice(0,3),
    stickyColumn: [...document.querySelectorAll('*')].some(e => getComputedStyle(e).position==='sticky' && e.getBoundingClientRect().height > 300) };
  const footer = [...document.querySelectorAll('footer, [class*="footer" i], [role="contentinfo"]')].sort((a,b) => b.querySelectorAll('a').length - a.querySelectorAll('a').length)[0];
  if (footer) {
    const heads = [...footer.querySelectorAll('h2,h3,h4,h5,h6,[class*="title" i],[class*="heading" i],summary')].filter(vis).map(txt).filter(Boolean);
    out.footer = { headings: [...new Set(heads)].slice(0,12), linkCount: footer.querySelectorAll('a').length,
      newsletter: !!footer.querySelector('input[type=email]') };
  }
  const fontC = {}, colC = {}, bgC = {};
  [...document.querySelectorAll('body *')].slice(0,4000).forEach(e => { if(!vis(e)) return; const s = getComputedStyle(e);
    const f = s.fontFamily.split(',')[0].replace(/["']/g,'').trim(); fontC[f]=(fontC[f]||0)+1;
    colC[s.color]=(colC[s.color]||0)+1; if(!/rgba\(.*,\s*0\)/.test(s.backgroundColor)) bgC[s.backgroundColor]=(bgC[s.backgroundColor]||0)+1; });
  const top = (o,n) => Object.entries(o).sort((a,b)=>b[1]-a[1]).slice(0,n).map(([k,v])=>({value:k,count:v}));
  out.fonts = top(fontC, 6); out.textColours = top(colC, 6); out.bgColours = top(bgC, 6);
  out.headingSample = [...document.querySelectorAll('h1,h2')].filter(vis).slice(0,3).map(h => { const s=getComputedStyle(h);
    return {text: txt(h), font: s.fontFamily.slice(0,60), size: s.fontSize, weight: s.fontWeight, tracking: s.letterSpacing, transform: s.textTransform}; });
  out.bodyFont = (() => { const s = getComputedStyle(document.body); return {family: s.fontFamily.slice(0,80), size: s.fontSize}; })();
  const srcs = [...document.scripts].map(s => s.src).filter(Boolean);
  const libs = {};
  const checks = { GSAP: () => !!window.gsap || srcs.some(s=>/gsap/i.test(s)), ScrollTrigger: () => !!window.ScrollTrigger,
    Lenis: () => !!window.lenis || !!window.Lenis || document.documentElement.classList.contains('lenis') || srcs.some(s=>/lenis/i.test(s)),
    Swiper: () => !!window.Swiper || !!document.querySelector('.swiper') || srcs.some(s=>/swiper/i.test(s)),
    Splide: () => !!document.querySelector('.splide'), Flickity: () => !!window.Flickity || !!document.querySelector('.flickity-enabled'),
    Slick: () => !!document.querySelector('.slick-slider'), ThreeJS: () => !!window.THREE || srcs.some(s=>/three(\.min)?\.js/i.test(s)),
    Barba: () => !!window.barba || srcs.some(s=>/barba/i.test(s)), Locomotive: () => !!document.querySelector('[data-scroll-container]'),
    FramerMotion: () => !!document.querySelector('[data-framer-appear-id],[data-projection-id]'),
    React: () => !!window.React || !!document.querySelector('[data-reactroot]') || !!window.__NEXT_DATA__ || !!document.getElementById('__next'),
    NextJS: () => !!window.__NEXT_DATA__ || !!document.getElementById('__next') || srcs.some(s=>/_next\//.test(s)),
    Shopify: () => !!window.Shopify, Hydrogen: () => srcs.some(s=>/hydrogen|oxygen/i.test(s)),
    Vue: () => !!window.Vue || !!document.querySelector('[data-v-app]') || !!window.__NUXT__,
    Alpine: () => !!window.Alpine, jQuery: () => !!window.jQuery, AOS: () => !!window.AOS || !!document.querySelector('[data-aos]'),
    Lottie: () => !!window.lottie || !!document.querySelector('lottie-player, dotlottie-player'),
    Klaviyo: () => !!window.klaviyo, Algolia: () => srcs.some(s=>/algolia/i.test(s)), Webflow: () => !!window.Webflow,
    Framer: () => srcs.some(s=>/framer/i.test(s)) };
  for (const [k,f] of Object.entries(checks)) { try { if (f()) libs[k]=true; } catch(e){} }
  out.libraries = Object.keys(libs);
  out.scriptHosts = [...new Set(srcs.map(s => { try { return new URL(s).host } catch(e) { return '' } }))].slice(0,25);
  const anims = document.getAnimations ? document.getAnimations().length : 0;
  out.motion = { runningAnimations: anims,
    marquee: !!document.querySelector('[class*="marquee" i], marquee, [class*="ticker" i]'),
    videoCount: document.querySelectorAll('video').length,
    transitionsOnLinks: [...document.querySelectorAll('a')].slice(0,200).filter(a=>getComputedStyle(a).transitionDuration!=='0s').length,
    cssScrollSnap: [...document.querySelectorAll('*')].slice(0,3000).some(e=>getComputedStyle(e).scrollSnapType!=='none'),
    reducedMotionQuery: [...document.styleSheets].some(ss => { try { return [...ss.cssRules].some(r => /prefers-reduced-motion/.test(r.conditionText||r.media?.mediaText||'')) } catch(e){ return false } }) };
  out.headings = [...document.querySelectorAll('h1,h2,h3')].filter(vis).map(txt).filter(Boolean).slice(0,60);
  out.title = document.title; out.h1 = txt(document.querySelector('h1') || document.body);
  out.bodyTextSample = body.replace(/\s+/g,' ').slice(0, 600);
  return out;
}
"""

FIND_LINKS_JS = r"""
() => {
  const abs = [...document.querySelectorAll('a[href]')].map(a => a.href).filter(h => h.startsWith(location.origin));
  const uniq = [...new Set(abs)];
  const coll = uniq.filter(h => /\/(collections|collection|shop|category|categories|c|catalog|women|men|new|clothing)(\/|$)/i.test(new URL(h).pathname) && !/\/products?\//i.test(h) && !/account|login|cart|search/i.test(h));
  const prod = uniq.filter(h => !/gift|card|e-gift/i.test(h)).filter(h => /\/products?\/[^/]+|\/p\/|\.html$|\/item\//i.test(new URL(h).pathname) && !/account|login|cart/i.test(h));
  return {coll: coll.slice(0,15), prod: prod.slice(0,15)};
}
"""

BLOCK_RE = re.compile(r"access denied|attention required|verify you are human|are you a robot|captcha|pardon our interruption|request blocked|just a moment|403 forbidden|enable javascript and cookies", re.I)


def dismiss(page):
    for sel in ["#onetrust-reject-all-handler", "button:has-text('Reject all')", "button:has-text('Reject All')",
                "button:has-text('Decline')", "button:has-text('Only necessary')", "button:has-text('Necessary only')",
                "button[aria-label*='close' i]:visible", "button:has-text('Close')", "button:has-text('Stay on')"]:
        try:
            el = page.locator(sel).first
            if el.is_visible(timeout=400):
                el.click(timeout=1500); page.wait_for_timeout(500)
        except Exception:
            pass
    for sel in ["[class*='newsletter' i] button[aria-label*='close' i]", "[role=dialog] button[aria-label*='close' i]",
                "button:has-text('Confirm shipping location')", "button:has-text('SAVE')", "button:has-text('Continue to')",
                "button:has-text('Shop now')", "button:has-text('Stay on')", "[aria-label='Close dialog']", ".needsclick button[aria-label*='Close' i]"]:
        try:
            el = page.locator(sel).first
            if el.is_visible(timeout=300):
                el.click(timeout=1500); page.wait_for_timeout(500)
        except Exception:
            pass
    try:
        page.keyboard.press("Escape"); page.wait_for_timeout(400)
    except Exception:
        pass


def settle(page):
    # scroll through to trigger lazy-loading and scroll-linked effects, then back to top
    try:
        h = page.evaluate("document.body.scrollHeight")
        for y in range(0, min(h, 20000), 900):
            page.evaluate(f"window.scrollTo(0,{y})"); page.wait_for_timeout(180)
        page.evaluate("window.scrollTo(0,0)"); page.wait_for_timeout(1200)
    except Exception:
        pass


def header_on_scroll(page):
    try:
        return page.evaluate("""async () => { window.scrollTo(0, 1200); await new Promise(r=>setTimeout(r,800));
          const h = [...document.querySelectorAll('header, [role="banner"], [class*="header" i], header-navigation, [class*="navbar" i]')].filter(e => e.getBoundingClientRect().height >= 30 && e.getBoundingClientRect().width >= innerWidth*0.8).sort((a,b)=>Math.abs(a.getBoundingClientRect().top)-Math.abs(b.getBoundingClientRect().top))[0]; if(!h) return null;
          const s = getComputedStyle(h), r = h.getBoundingClientRect(); const o = {visibleAfterScroll: r.bottom > 0 && r.top >= -5,
          bgAfterScroll: s.backgroundColor, backdropAfterScroll: s.backdropFilter, transform: s.transform};
          window.scrollTo(0,0); return o; }""")
    except Exception:
        return None


def try_cart(page):
    """Open the cart drawer without adding anything, and read what it shows when empty."""
    for sel in ["button[aria-label*='cart' i]:visible", "button[aria-label*='bag' i]:visible", "a[href*='/cart']:visible",
                "[class*='cart' i] a:visible", "a[aria-label*='bag' i]:visible", "[aria-label*='cart' i]:visible", "[aria-label*='bag' i]:visible", "a:has-text('Bag'):visible", "a:has-text('Cart'):visible"]:
        try:
            el = page.locator(sel).first
            if not el.is_visible(timeout=500):
                continue
            url_before = page.url
            el.click(timeout=2500); page.wait_for_timeout(2000)
            info = page.evaluate("""() => { const d = [...document.querySelectorAll('[class*="drawer" i],[class*="cart" i],[role=dialog],aside')]
              .filter(e => { const r=e.getBoundingClientRect(); return r.width>200 && r.height>200 && getComputedStyle(e).visibility!=='hidden'; })[0];
              if (!d) return {type: location.pathname.includes('cart') ? 'page' : 'none', text: document.body.innerText.slice(0,400)};
              const t = d.innerText; return {type: 'drawer', width: Math.round(d.getBoundingClientRect().width),
                freeShippingBar: /free (shipping|delivery)|away from|spend/i.test(t), upsells: /you may also|recommended|add|pair/i.test(t),
                text: t.replace(/\\s+/g,' ').slice(0,400)}; }""")
            info["opened_via"] = sel
            info["navigated"] = page.url != url_before
            return info
        except Exception:
            continue
    return {"type": "not found"}


def shoot(ctx_desktop, ctx_mobile, key, kind, url, rec):
    for label, ctx in (("1440", ctx_desktop), ("390", ctx_mobile)):
        page = ctx.new_page()
        try:
            resp = page.goto(url, wait_until="domcontentloaded", timeout=45000)
            try:
                page.wait_for_load_state("networkidle", timeout=12000)
            except PWTimeout:
                pass
            page.wait_for_timeout(2500)
            dismiss(page)
            page.wait_for_timeout(3000); dismiss(page)
            status = resp.status if resp else None
            body = page.evaluate("document.body ? document.body.innerText.slice(0,1500) : ''")
            blocked = (status and status >= 400) or (len(body) < 400 and BLOCK_RE.search(body or "") is not None) or \
                      bool(BLOCK_RE.search(page.title() or ""))
            if label == "1440":
                rec["status"] = status; rec["finalUrl"] = page.url; rec["blocked"] = bool(blocked)
            settle(page)
            fn = SHOTS / f"{key}__{kind}__{label}.png"
            try:
                page.screenshot(path=str(fn), full_page=True, timeout=60000)
            except Exception:
                page.screenshot(path=str(fn), timeout=30000)
            rec.setdefault("screenshots", []).append(f"screenshots/{fn.name}")
            if label == "1440":
                rec["data"] = page.evaluate(EXTRACT_JS)
                rec["headerOnScroll"] = header_on_scroll(page)
                rec["links"] = page.evaluate(FIND_LINKS_JS)
                if kind in ("product", "home") and rec.get("cart") is None and not blocked:
                    rec["cart"] = try_cart(page)
            else:
                rec["mobile"] = {"nav_burger": page.evaluate("!!document.querySelector('[aria-label*=menu i], [class*=burger i], [class*=hamburger i]')"),
                                 "bottomBar": page.evaluate("[...document.querySelectorAll('*')].some(e=>{const s=getComputedStyle(e);return s.position==='fixed'&&e.getBoundingClientRect().bottom>=innerHeight-2&&e.getBoundingClientRect().height>40&&e.getBoundingClientRect().height<140})")}
        except Exception as e:
            rec.setdefault("errors", []).append(f"{label}: {type(e).__name__}: {str(e)[:200]}")
        finally:
            page.close()
        time.sleep(random.uniform(*DELAY))


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--disable-blink-features=AutomationControlled"])
        common = dict(user_agent=UA, locale="en-GB", timezone_id="Europe/London")
        cd = browser.new_context(viewport={"width": 1440, "height": 900}, **common)
        cm = browser.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True,
                                 user_agent=UA.replace("Windows NT 10.0; Win64; x64", "iPhone; CPU iPhone OS 18_0 like Mac OS X").replace("Chrome/141.0.0.0", "Version/18.0 Mobile/15E148"),
                                 locale="en-GB")
        for ctx in (cd, cm):
            ctx.add_init_script("Object.defineProperty(navigator,'webdriver',{get:()=>undefined})")
        for t in TARGETS:
            key = t["key"]
            if ONLY and key not in ONLY:
                continue
            recf = RECS / f"{key}.json"
            if recf.exists() and not ONLY:
                print("skip (done)", key); continue
            result = {"key": key, "group": t.get("group"), "pages": {}}
            pages = [("home", t["url"])]
            for kind, url in pages:
                rec = {"url": url}
                if not robots_ok(url):
                    rec["skipped"] = "disallowed by robots.txt"; result["pages"][kind] = rec; continue
                print(f"[{key}] {kind} {url}", flush=True)
                shoot(cd, cm, key, kind, url, rec)
                result["pages"][kind] = rec
                links = rec.pop("links", None) or {}
                if t.get("group") == "store" and not rec.get("blocked"):
                    if kind == "home":
                        coll = t.get("collection") or next(iter(links.get("coll") or []), None)
                        if coll: pages.append(("collection", coll))
                    elif kind == "collection":
                        prod = t.get("product") or next(iter(links.get("prod") or []), None)
                        if prod: pages.append(("product", prod))
            recf.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
            print("done", key, {k: ("BLOCKED" if v.get("blocked") else v.get("skipped") or v.get("status")) for k, v in result["pages"].items()}, flush=True)
        browser.close()


if __name__ == "__main__":
    main()
