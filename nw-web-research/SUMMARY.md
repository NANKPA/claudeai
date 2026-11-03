# Notion World: web research summary

Scraped on 3 Nov 2026 from khidr's PC with Playwright (Chromium). The scraper checked robots.txt before each page and waited 4–7 s between page loads. Screenshots are for reference only: no product photos, logos or code were taken for reuse.

## What's in this folder

| Path | Contents |
|---|---|
| `screenshots/` | `<site>__<home/collection/product>__<1440/390>.jpg`, full-page captures saved as JPEG (quality 80). The 390 px phone shots are rendered at 2x. Captures taller than 60,000 px are split into `_partN` files. |
| `records/<site>.json` | One record per site, with per-page data on header behaviour, nav, hero, product-card anatomy, filters and sort, PDP anatomy, cart drawer, footer, fonts, colours, JS libraries and motion signals. |
| `records/_index.json` | Every page condensed into one table, plus library and font counts. Start here. |
| `blanks/` | 20 CC0/public-domain blank tee photos, plus `LICENSES.md` and `blanks_manifest.json`. |
| `tools/` | The scraper (`scrape.py`), targets list, aggregator and blank-tee search scripts, so the run can be repeated. |

## Coverage

- Stores, complete (home, collection and product): Kith, Aimé Leon Dore, Acne Studios, Represent, Fear of God, Essentials, Stüssy, Corteiz, Palace, Guest in Residence, Dairy Boy, Nocta.
- Stores, partial:
  - SSENSE: home only. The collection page returned Cloudflare's "Just a moment" challenge (403).
  - Cactus Plant Flea Market: the whole store is one page, so the home page covers everything.
  - entireworld.com: now redirects to entireworld.us, a design-studio portfolio rather than a shop. Home only.
- Stores, blocked:
  - COS: Akamai "Access Denied".
  - Jacquemus: 403 maintenance page on both attempts.
  - Prada: `ERR_HTTP2_PROTOCOL_ERROR` on every request, most likely bot protection.

  I didn't try to get around any of these bot walls.
- Design and library sites, all captured: GSAP showcase, Lenis, Laws of UX, Annnimate, Kokonut UI, dqnamo kitchen, 21st.dev, Awwwards (e-commerce and fashion category pages), Godly, SiteInspire, Land-book, 3dwebsites.design, abtest.design, Refactoring UI, rauno.me.
- Awwwards: the category pages list the current top sites (the studio names are in `records/awwwards-*.json` → `headings`). I didn't open each winner's site.

## What the stack data says

- 12 of 18 stores run on Shopify, and 10 use Klaviyo. Swiper is the default carousel (7 sites).
- GSAP appears on only 2 stores (Represent, plus the GSAP showcase itself) and Lenis on none. The luxury feel these stores have comes from type, spacing and photography, not heavy motion. Use motion sparingly.
- Fonts in use:
  - Condensed Helvetica with Optima: Fear of God and Essentials.
  - Söhne with DIN: Aimé Leon Dore.
  - Helvetica Now Text and Helvetica Mono: Acne.
  - Monument Grotesk with GT Alpina serif: Dairy Boy.
  - Favorit with Favorit Mono: Guest in Residence.
  - Courier New: Corteiz.
  - Proxima Nova with a Georgia serif: Kith.
  - Instrument Sans with Swiss 721 Bold Extended: Nocta.
  - Large uppercase grotesk, 95 px with -4.5 px tracking: SSENSE.

  The common shape is one neutral grotesk plus one "voice" face, either a serif or a mono.
- Palettes are near-monochrome: #000 or #181818 on #FFF, #F7F7F7 or #F2F2F2. Single accents are rare: Acne's link blue (rgb 0 24 168), Guest in Residence's amber bar (#F5A800) and Dairy Boy's dark brown (#2E1A0E).

## Top 30 patterns worth adopting

### Header and navigation
1. **A transparent header over the hero that turns solid white on scroll.** Aimé Leon Dore and Kith do this. The header is 46–61 px tall. Use a white background, not glass; no luxury store used backdrop blur.
2. **A slim, condensed, all-caps nav with five to eight top-level items.** Fear of God and Essentials use: FEATURED, COLLECTIONS, MENS, WOMENS, KIDS, then utilities on the right (SEARCH, ACCOUNT, BAG). Use the words, not icons, for utilities.
3. **A centred wordmark with the categories on the left and utilities on the right.** Acne, Kith, Dairy Boy, Guest in Residence and Fear of God all use this.
4. **A vertical category list down the left side (Stüssy, Corteiz).** It reads as streetwear-native and makes every category one click away. It's a strong fit for a small catalogue.
5. **A bag count in brackets, written as text: `BAG (0)` or `Cart ( 0 )`.** SSENSE and Nocta do this instead of a badge bubble.
6. **A one-line announcement bar above the header,** for shipping thresholds or a drop countdown. Dairy Boy and Guest in Residence rotate several messages with previous/next arrows.

### Home page and hero
7. **A full-viewport editorial hero (100vh) with one line of copy and two text CTAs.** Fear of God uses "DISCOVER / SHOP" and Represent uses "DISCOVER". There are no buttons with heavy fills. Notion World can't use people, so use a single garment, still life or texture image instead.
8. **The home page as a shop grid (Palace, Corteiz, CPFM).** The product grid starts right under the nav, with no hero. This fits the drop model.
9. **A drop or newsletter capture framed as "NEVER MISS A DROP" (Nocta) or "Join the Conversation" (Fear of God).** Keep it to one field and one button, and put it in the footer rather than an on-load modal. Five of the stores open a modal on load and it covers the products; avoid that.
10. **CPFM's oddball data widgets.** CPFM puts the local time, tide height, weather and moon phase on its home page. Notion World could do an Accra version (time, temperature, Gulf of Guinea tide) as a small signature detail that costs little and adds a lot of character.

### Product grid and cards
11. **A 4:5 (0.8) image ratio for apparel cards.** ALD, Stüssy and Nocta use 4:5, Represent and Fear of God use 3:4, and Kith, Palace and Corteiz use 1:1 for packshots. With no models, Notion World could use 1:1 or 4:5 on an off-white (#F2F2F2–#F7F7F7) background.
12. **A second image on hover (front, then back).** Most stores do this. It suits flat-lay front and back shots, so no models are needed.
13. **Quiet card text:** product name and price in 10–12 px uppercase, with no stars and no "add" button. Represent is the only one with quick-add.
14. **Small, sparing text badges** such as "ONLY 1 LEFT", "Trending" (Dairy Boy) and "100% CASHMERE" (Guest in Residence). Use them for scarcity and material, not discounts.
15. **Swatches under the card or on the PDP:** small squares of the garment in each colourway (Corteiz, Stüssy, Dairy Boy).
16. **Filter and sort behind a single "FILTER & SORT" toggle** (Essentials: "828 ITEMS · FILTER & SORT") rather than a permanent sidebar. ALD and Palace show filters inline because their catalogues are huge, which Notion World doesn't need.

### Product page (PDP)
17. **Two columns: a large gallery on the left and a sticky info column on the right.** About 10 of 12 PDPs used a sticky info column (`stickyColumn: true`).
18. **Size buttons in a row, XS–XXL, outlined, with out-of-stock sizes struck through or greyed** (Kith, Stüssy, Essentials, Nocta, Dairy Boy). Put the "SIZE GUIDE" link to the right of the size label; 11 of 12 PDPs have one.
19. **Put sizing advice in the copy, as Palace does: "Model is 182cm wearing size large".** Without models, write "Garment is boxy — size down for a regular fit" plus a flat measurement table (chest, length, sleeve).
20. **Short accordions:** DETAILS / SIZE & FIT / SHIPPING & RETURNS (Stüssy, Corteiz, Kith, Fear of God). Keep it to three.
21. **Delivery promise next to the add-to-bag button.** Acne shows "FREE DELIVERY & RETURNS · Estimated delivery within 2–4 business days. Incl. import duties", and Represent shows "Fastest delivery Wed, Nov 4 – Thu, Nov 5". For Notion World, state Accra/Ghana delivery times and the international duties policy clearly.
22. **A single full-width black ADD TO BAG button** (Acne, Dairy Boy and Corteiz use "SELECT SIZE" until a size is picked).
23. **Cross-sell as "COMPLETE THE LOOK" (Kith, Dairy Boy, Nocta) and "YOU MAY ALSO LIKE" below.** With no models, show the matching items side by side.
24. **Pay-in-instalments messaging under the price** (Dairy Boy: "4 payments of…", Guest in Residence: Afterpay). Check what Ghana payment providers support (e.g. Paystack) before promising this.

### Cart
25. **A slide-in drawer, not a cart page.** Kith's empty drawer still shows "Recommended For You", which is a smart way to fill it. Palace sends you to a full cart page, which feels dated by comparison.
26. **A free-shipping threshold, stated in copy:** "Free shipping on all domestic orders $175+" (Dairy Boy), "Free shipping over $175" (Represent), "orders over $200" (Stüssy). A progress bar inside the drawer is the stronger version. I didn't see one in the empty drawers, because the drawers were empty.

### Footer, type and motion
27. **A few footer columns with plain labels.** Kith uses JOIN OUR LIST / LEARN / KITH / POLICIES / FOLLOW US. Palace uses wit instead: "DO WATCH THAT" for socials and "BORING STUFF" for legal. That wit suits Notion World's voice.
28. **Typography system:** a neutral grotesk for UI at 10–12 px uppercase with +0.3–0.6 px tracking, plus a voice face for product names and editorial: a serif like Optima (Fear of God), GT Alpina (Dairy Boy) or Georgia (Kith), or a mono like Courier (Corteiz) or Favorit Mono (Guest in Residence). Pick from the `awesome-fonts` free list rather than licensing these.
29. **Motion should be restrained and functional:** image cross-fades, header colour transitions (100+ links with CSS transitions on Fear of God and Represent), and marquees only for announcements (Stüssy). Save Lenis and GSAP for one editorial or lookbook page, and honour `prefers-reduced-motion`; 9 of 18 stores ship that media query.
30. **Micro-interactions from the component sites, used sparingly:**
    - dqnamo's "Hold to Confirm", "Receipt Printer" and "Ticket"/"Stamp". Use a receipt or ticket animation on order confirmation and a stamp for "Sold out".
    - Kokonut UI or 21st.dev animated buttons and cards for the drop countdown.
    - Laws of UX checks: Hick's law (fewer nav items), Fitts's law (big ADD TO BAG), Peak-End rule (make the confirmation page delightful).
    - abtest.design evidence: showing pricing and shipping costs upfront lifts conversion.

## Things to avoid (seen in the scrape)
- **On-load modals.** Region pickers and newsletter pop-ups covered the products on six sites (ALD, Represent, Fear of God, Essentials, Nocta and Kith; Acne also had a location gate). They also hurt the first impression. Detect the country automatically and offer a small banner instead. I re-shot those six with stronger modal dismissal. Fear of God and Essentials still show a timed newsletter pop-up that reappears after it's closed, so their screenshots have it, and Aimé Leon Dore's home hero rendered blank (white) in the capture.
- **Untranslated placeholder strings in the UI** (Kith's search button reads "Translation missing: en.accessibility.search").
- **Full-viewport heroes made of people photography.** Not an option for Notion World, so put the effort into garment still-life, fabric macro, and Accra textures and architecture.

## Gallery sites to browse by hand for more
- Godly: video-heavy, motion-led sites.
- 3dwebsites.design: WebGL and 3D. Useful if Notion World ever does a 3D tee viewer; see the Sketchfab CC-BY models in `blanks/LICENSES.md`.
- Awwwards Fashion and E-Commerce: recent winners include Studio Almond, Domaine Public, coi and ARRAY. Open them for lookbook layouts.
- Land-book and SiteInspire: static layout references.
