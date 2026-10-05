#!/usr/bin/env python3
"""Deterministic formal-search export ingestion for NEXT-05.

This tool DOES NOT execute database searches. It ingests already-exported CSV,
RIS, or BibTeX files, preserves raw provenance, normalizes identifiers, emits
dedup candidates, and fails closed on malformed or unregistered inputs.
"""
from __future__ import annotations
import argparse, csv, hashlib, json, re, unicodedata
from pathlib import Path
from difflib import SequenceMatcher

DOI_RE=re.compile(r"10\.\d{4,9}/[-._;()/:A-Z0-9]+",re.I)
FIELDS=["record_id","source","search_run_id","query_id","title_raw","title_normalized",
"authors_raw","first_author_normalized","year","doi_raw","doi_normalized",
"stable_id_type","stable_id","venue","abstract","url_or_locator","source_record_id",
"raw_export_file","raw_row_or_record","study_family_id","dedup_status","canonical_record_id"]

def sha256(p:Path)->str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def norm_text(s:str)->str:
    s=unicodedata.normalize("NFKC",s or "").lower()
    s=re.sub(r"[^\w\s]"," ",s,flags=re.UNICODE)
    return re.sub(r"\s+"," ",s).strip()

def norm_doi(s:str)->str:
    m=DOI_RE.search(s or "")
    return m.group(0).lower().rstrip(".,;)") if m else ""

def first_author(s:str)->str:
    if not s:return ""
    a=re.split(r";|\band\b|\|",s,flags=re.I)[0]
    a=re.sub(r"[^\w\s'-]"," ",a,flags=re.UNICODE)
    return re.sub(r"\s+"," ",a).strip().lower()

def read_registry(p:Path):
    rows=list(csv.DictReader(p.open(encoding="utf-8-sig",newline="")))
    return {(r["source"].strip(),r["search_run_id"].strip(),r["query_id"].strip()):r for r in rows if r.get("status","").strip().upper()=="EXECUTED"}

def parse_csv(p:Path):
    with p.open(encoding="utf-8-sig",errors="strict",newline="") as f:
        rows=list(csv.DictReader(f))
    for i,r in enumerate(rows,2): yield str(i),r

def parse_ris(p:Path):
    rec={}; n=0
    for line in p.read_text(encoding="utf-8-sig",errors="strict").splitlines():
        if line.startswith("TY  -"):
            rec={}; n+=1
        elif line.startswith("ER  -"):
            yield str(n),rec; rec={}
        elif len(line)>=6 and line[2:6]=="  - ":
            k=line[:2]; v=line[6:].strip()
            rec[k]=rec.get(k,"")+("; " if k in rec else "")+v

def parse_bib(p:Path):
    text=p.read_text(encoding="utf-8-sig",errors="strict")
    entries=re.split(r"(?=@\w+\s*\{)",text)
    for i,e in enumerate(entries,1):
        if not e.strip().startswith("@"): continue
        r={}
        for k,v in re.findall(r"(\w+)\s*=\s*[\{\"]([^\}\"]*)",e,re.S):
            r[k.lower()]=re.sub(r"\s+"," ",v).strip()
        yield str(i),r

def pick(r,*names):
    low={str(k).lower():str(v or "") for k,v in r.items()}
    for n in names:
        if low.get(n.lower()): return low[n.lower()].strip()
    return ""

def canonicalize(raw, source, run, qid, file, pos, rid):
    title=pick(raw,"title","document title","ti","t1")
    authors=pick(raw,"authors","author","au","a1")
    doi=pick(raw,"doi","do")
    year=pick(raw,"year","publication year","py","y1")
    stable=pick(raw,"pmid","eid","accession number","an","ut","isbn")
    stype="PMID" if pick(raw,"pmid") else ("SOURCE_ID" if stable else "")
    return dict(record_id=rid,source=source,search_run_id=run,query_id=qid,
      title_raw=title,title_normalized=norm_text(title),authors_raw=authors,
      first_author_normalized=first_author(authors),year=year[:4],
      doi_raw=doi,doi_normalized=norm_doi(doi),stable_id_type=stype,stable_id=stable,
      venue=pick(raw,"journal","publication title","jo","jf","booktitle"),
      abstract=pick(raw,"abstract","ab"),url_or_locator=pick(raw,"url","ur"),
      source_record_id=pick(raw,"document identifier","id","accession number","ut","eid"),
      raw_export_file=str(file),raw_row_or_record=pos,study_family_id="",
      dedup_status="UNRESOLVED",canonical_record_id="")

def candidate_basis(a,b):
    if a["doi_normalized"] and a["doi_normalized"]==b["doi_normalized"]: return "EXACT_DOI",1.0
    if a["stable_id"] and a["stable_id"]==b["stable_id"]: return "EXACT_STABLE_ID",1.0
    if a["title_normalized"] and a["title_normalized"]==b["title_normalized"]: return "EXACT_TITLE",1.0
    sim=SequenceMatcher(None,a["title_normalized"],b["title_normalized"]).ratio()
    if sim>=0.90 and a["first_author_normalized"] and a["first_author_normalized"]==b["first_author_normalized"] and a["year"] and a["year"]==b["year"]:
        return "FUZZY_TITLE_AUTHOR_YEAR_MANUAL",sim
    return "",sim

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--registry",required=True); ap.add_argument("--source",required=True)
    ap.add_argument("--search-run-id",required=True); ap.add_argument("--query-id",required=True)
    ap.add_argument("--input",required=True); ap.add_argument("--outdir",required=True)
    args=ap.parse_args(); p=Path(args.input); out=Path(args.outdir)
    if not p.is_file(): raise SystemExit("INGEST_FAIL: input export does not exist")
    reg=read_registry(Path(args.registry)); key=(args.source,args.search_run_id,args.query_id)
    if key not in reg: raise SystemExit("INGEST_FAIL: matching EXECUTED registry row required")
    rr=reg[key]; digest=sha256(p)
    expected=(rr.get("export_sha256") or "").strip().lower()
    if not expected: raise SystemExit("INGEST_FAIL: registry export_sha256 missing")
    if digest!=expected: raise SystemExit("INGEST_FAIL: SHA256 mismatch; raw export may have changed")
    ext=p.suffix.lower()
    parser={".csv":parse_csv,".ris":parse_ris,".bib":parse_bib}.get(ext)
    if not parser: raise SystemExit("INGEST_FAIL: supported formats are CSV, RIS, BibTeX")
    out.mkdir(parents=True,exist_ok=True)
    records=[]
    for n,(pos,raw) in enumerate(parser(p),1):
        rec=canonicalize(raw,args.source,args.search_run_id,args.query_id,p,pos,f"{args.search_run_id}-{args.query_id}-{n:07d}")
        if not rec["title_raw"]: raise SystemExit(f"INGEST_FAIL: record {pos} has no title")
        records.append(rec)
    declared=(rr.get("exported_count") or "").strip()
    if declared and int(declared)!=len(records): raise SystemExit(f"INGEST_FAIL: exported_count={declared}, parsed={len(records)}")
    with (out/"pooled_raw_index.csv").open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=FIELDS); w.writeheader(); w.writerows(records)
    pairs=[]
    for i,a in enumerate(records):
        for b in records[i+1:]:
            basis,sim=candidate_basis(a,b)
            if basis:pairs.append({"record_id_a":a["record_id"],"record_id_b":b["record_id"],"match_basis":basis,"title_similarity":f"{sim:.6f}","decision":"MANUAL_REVIEW" if basis.startswith("FUZZY") else "CANDIDATE_DUPLICATE"})
    with (out/"dedup_candidates.csv").open("w",encoding="utf-8",newline="") as f:
        cols=["record_id_a","record_id_b","match_basis","title_similarity","decision"]; w=csv.DictWriter(f,fieldnames=cols); w.writeheader(); w.writerows(pairs)
    meta={"source":args.source,"search_run_id":args.search_run_id,"query_id":args.query_id,"input":str(p),"sha256":digest,"parsed_records":len(records),"dedup_candidates":len(pairs),"note":"No fuzzy candidate is auto-deleted; study-family merging is never automatic."}
    (out/"ingestion_manifest.json").write_text(json.dumps(meta,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps(meta,indent=2))

if __name__=="__main__": main()
