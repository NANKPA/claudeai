import json, glob, os, sys
from collections import Counter
root=sys.argv[1]; rows=[]; libs=Counter(); fonts=Counter()
for f in sorted(glob.glob(os.path.join(root,"records","*.json"))):
    if os.path.basename(f).startswith("_"): continue
    d=json.load(open(f,encoding="utf-8"))
    for kind,p in d["pages"].items():
        x=p.get("data") or {}
        h=x.get("header") or {}; pc=x.get("productCard") or {}; pdp=x.get("pdp") or {}; hero=x.get("hero") or {}; mo=x.get("motion") or {}
        rows.append({"site":d["key"],"group":d["group"],"page":kind,"status":p.get("status"),"blocked":p.get("blocked"),"skipped":p.get("skipped"),"errors":p.get("errors"),
          "header":f"{h.get('position')} h{h.get('height')} {'transparent' if h.get('transparent') else h.get('bg')} {'glass' if h.get('glass') else ''}".strip() if h else None,
          "headerOnScroll":p.get("headerOnScroll"),"nav":(x.get("nav") or [])[:14],
          "hero":hero,"card":{k:pc.get(k) for k in ("imageRatio","hoverSwapLikely","quickAdd","swatches","badges")} if pc else None,
          "filters":x.get("filterSort"),"pdp":{k:pdp.get(k) for k in ("sizeButtons","sizeGuide","accordions","deliveryCopy","crossSell","addToCart","stickyColumn")} if kind=="product" else None,
          "cart":p.get("cart"),"footer":x.get("footer"),"fonts":[q["value"] for q in x.get("fonts",[])][:4],"heading":(x.get("headingSample") or [None])[0],
          "textColours":[q["value"] for q in x.get("textColours",[])][:4],"bg":[q["value"] for q in x.get("bgColours",[])][:4],
          "libraries":x.get("libraries"),"motion":mo,"mobile":p.get("mobile"),"headings":(x.get("headings") or [])[:25]})
        if kind=="home":
            libs.update(x.get("libraries") or []); fonts.update([q["value"] for q in x.get("fonts",[])][:2])
json.dump({"rows":rows,"libraryCounts":libs.most_common(),"fontCounts":fonts.most_common(40)},open(os.path.join(root,"records","_index.json"),"w",encoding="utf-8"),indent=1,ensure_ascii=False)
print(len(rows), libs.most_common(20))
