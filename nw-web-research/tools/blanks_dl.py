import json, urllib.request, time, re, sys
from pathlib import Path
UA={"User-Agent":"NotionWorldResearch/1.0 (github NANKPA)"}
out=Path(sys.argv[1]); r=json.load(open("blanks_candidates.json",encoding="utf-8"))
items=[]; seen=set()
skip=re.compile(r"coca|colorful|women's|drawing|wikimania|logo", re.I)
for k,v in r.items():
    if k.startswith("openverse") and isinstance(v,list):
        for x in v:
            if x["source"]=="rawpixel" and x["license"]=="cc0" and x["url"] not in seen and not skip.search(x["title"]):
                seen.add(x["url"]); items.append({"src":"rawpixel (via Openverse)","title":x["title"],"file_url":x["url"],"page":x["foreign_landing_url"],"license":"CC0 1.0 (Public Domain Dedication)","author":x.get("creator") or "rawpixel (public domain collection)"})
want={"File:T-shirt mocup.jpg","File:T-shirt.png","File:T-shirt2.jpg","File:Yerevan armenia black t-shirt.webp"}
for k,v in r.items():
    if k.startswith("commons") and isinstance(v,list):
        for x in v:
            if x["title"] in want and x["title"] not in seen:
                seen.add(x["title"]); items.append({"src":"Wikimedia Commons","title":x["title"],"file_url":x.get("thumb") or x["url"],"page":x["page"],"license":x["license"],"author":re.sub("<[^>]+>","",x["artist"] or "").strip()})
for i,it in enumerate(items,1):
    ext=".png" if it["file_url"].lower().endswith(".png") else ".jpg"
    name=f"{i:02d}-"+re.sub(r"[^a-z0-9]+","-",it["title"].lower().replace("file:","")).strip("-")[:50]+ext
    try:
        data=urllib.request.urlopen(urllib.request.Request(it["file_url"],headers=UA),timeout=60).read()
        (out/name).write_bytes(data); it["file"]=name; it["bytes"]=len(data)
    except Exception as e: it["error"]=str(e)
    print(name, it.get("bytes"), it.get("error",""))
    time.sleep(2)
json.dump(items,open(out/"blanks_manifest.json","w",encoding="utf-8"),indent=1,ensure_ascii=False)
