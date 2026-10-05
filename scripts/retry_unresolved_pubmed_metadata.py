#!/usr/bin/env python3
import csv, time, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from pathlib import Path

SRC=Path("evidence/search/derived/pubmed/PUBMED_Q00_DETERMINISTIC_PRESCREEN_2026-10-05.csv")
OUT=Path("evidence/search/derived/pubmed/run56_metadata_retry")
OUT.mkdir(parents=True,exist_ok=True)
rows=list(csv.DictReader(SRC.open(encoding="utf-8")))
targets=[r for r in rows if r.get("prescreen_reason")=="METADATA_UNAVAILABLE"]
if len(targets)!=11: raise SystemExit(f"FAIL expected 11 metadata-unavailable rows, got {len(targets)}")
ids=[r["pmid"] for r in targets]
url="https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?"+urllib.parse.urlencode({"db":"pubmed","id":",".join(ids),"retmode":"xml"})
req=urllib.request.Request(url,headers={"User-Agent":"AR-Systematic-Review/Run56 reproducibility workflow"})
with urllib.request.urlopen(req,timeout=60) as resp: data=resp.read()
(OUT/"NCBI_EFETCH_RETRY.xml").write_bytes(data)
root=ET.fromstring(data)
found={}
for art in root.findall(".//PubmedArticle"):
    pmid=(art.findtext(".//MedlineCitation/PMID") or "").strip()
    title="".join(art.find(".//ArticleTitle").itertext()) if art.find(".//ArticleTitle") is not None else ""
    abstract=" ".join("".join(x.itertext()) for x in art.findall(".//Abstract/AbstractText"))
    journal=art.findtext(".//Article/Journal/Title") or ""
    year=art.findtext(".//Article/Journal/JournalIssue/PubDate/Year") or art.findtext(".//Article/Journal/JournalIssue/PubDate/MedlineDate") or ""
    doi=""
    for x in art.findall(".//ArticleId"):
        if x.attrib.get("IdType")=="doi": doi=(x.text or "")
    found[pmid]={"pmid":pmid,"doi":doi,"title":title,"abstract":abstract,"journal":journal,"year":year,"retry_status":"RESOLVED"}
outrows=[]
for pmid in ids:
    outrows.append(found.get(pmid,{"pmid":pmid,"doi":"","title":"","abstract":"","journal":"","year":"","retry_status":"STILL_UNAVAILABLE"}))
with (OUT/"METADATA_RETRY_RESULTS.csv").open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=["pmid","doi","title","abstract","journal","year","retry_status"]); w.writeheader(); w.writerows(outrows)
resolved=sum(r["retry_status"]=="RESOLVED" for r in outrows)
print(f"RUN56_METADATA_RETRY target=11 resolved={resolved} still_unavailable={11-resolved}")
