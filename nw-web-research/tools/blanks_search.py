import json, urllib.request, urllib.parse, time
UA={"User-Agent":"NotionWorldResearch/1.0 (contact via github NANKPA)"}
def get(u):
    return json.loads(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read())
res={}
for q in ["blank t-shirt","white t-shirt flat lay","black t-shirt mockup","t-shirt hanger","oversized t-shirt","plain tshirt","t-shirt back","ghost mannequin shirt"]:
    u="https://api.openverse.org/v1/images/?"+urllib.parse.urlencode({"q":q,"license":"cc0,pdm","page_size":20,"mature":"false"})
    try:
        d=get(u); res["openverse:"+q]=[{k:r.get(k) for k in ("title","url","foreign_landing_url","creator","license","license_version","source","width","height","tags")} for r in d.get("results",[])]
    except Exception as e: res["openverse:"+q]=str(e)
    time.sleep(2)
for q in ["t-shirt","tshirt","shirt"]:
    try:
        d=get("https://api.sketchfab.com/v3/search?"+urllib.parse.urlencode({"type":"models","q":q,"downloadable":"true","license":"cc0","count":24}))
        res["sketchfab-cc0:"+q]=[{"name":r["name"],"url":r["viewerUrl"],"user":r["user"]["username"],"license":(r.get("license") or {}).get("label")} for r in d["results"]]
        d=get("https://api.sketchfab.com/v3/search?"+urllib.parse.urlencode({"type":"models","q":q,"downloadable":"true","license":"by","count":24}))
        res["sketchfab-ccby:"+q]=[{"name":r["name"],"url":r["viewerUrl"],"user":r["user"]["username"],"license":(r.get("license") or {}).get("label")} for r in d["results"]]
    except Exception as e: res["sketchfab:"+q]=str(e)
    time.sleep(2)
try:
    d=get("https://api.polyhaven.com/assets?t=models")
    res["polyhaven"]=[{"id":k,"name":v["name"],"categories":v.get("categories"),"tags":v.get("tags")} for k,v in d.items() if any(w in (v["name"]+" ".join(v.get("tags",[]))+" ".join(v.get("categories",[]))).lower() for w in ("shirt","cloth","garment","fabric","hanger","textile"))]
except Exception as e: res["polyhaven"]=str(e)
for q in ["blank t-shirt","white t-shirt","black t-shirt","T-shirt flat"]:
    u="https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({"action":"query","format":"json","generator":"search","gsrsearch":q+" filetype:bitmap","gsrnamespace":6,"gsrlimit":25,"prop":"imageinfo","iiprop":"url|extmetadata|size","iiurlwidth":1600})
    try:
        d=get(u)
        out=[]
        for p in (d.get("query",{}).get("pages",{}) or {}).values():
            ii=p["imageinfo"][0]; m=ii.get("extmetadata",{})
            out.append({"title":p["title"],"page":ii["descriptionurl"],"url":ii["url"],"thumb":ii.get("thumburl"),"w":ii["width"],"h":ii["height"],
              "license":m.get("LicenseShortName",{}).get("value"),"artist":m.get("Artist",{}).get("value","")[:200],"usage":m.get("UsageTerms",{}).get("value")})
        res["commons:"+q]=out
    except Exception as e: res["commons:"+q]=str(e)
    time.sleep(2)
json.dump(res,open("blanks_candidates.json","w",encoding="utf-8"),indent=1,ensure_ascii=False)
for k,v in res.items():
    print("##",k, len(v) if isinstance(v,list) else v)
    if isinstance(v,list):
        for r in v[:25]: print("   ", (r.get("title") or r.get("name") or r.get("id"))[:70], "|", r.get("license"), "|", r.get("w") or r.get("width"), "|", r.get("source") or r.get("user") or "")
