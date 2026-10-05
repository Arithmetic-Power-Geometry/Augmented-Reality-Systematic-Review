#!/usr/bin/env python3
"""Create nonbinding TA-01 assisted recommendations from the frozen committed batch."""
import csv,re,hashlib
from pathlib import Path
src=Path("evidence/screening/formal_pubmed_batches/TA-01.csv")
out=Path("evidence/screening/assisted/TA-01_ASSISTED_TRIAGE_RUN60.csv")
if not src.exists(): raise SystemExit("BLOCK: TA-01 is not committed")
rows=list(csv.DictReader(src.open(encoding="utf-8-sig")))
if len(rows)!=250: raise SystemExit(f"BLOCK: expected 250 rows, got {len(rows)}")
strong=["augmented reality","mixed reality","augmented-reality","head-mounted display","head mounted display","hololens","magic leap","optical see-through","video see-through","spatial computing"]
fields=["screening_ordinal","batch_id","pmid","doi","title","abstract","year","journal","assisted_recommendation","assisted_confidence","assisted_rationale","primary_decision","reason_code","primary_screener","decision_timestamp","evidence_note","decision_version","second_verification_state","adjudication_state"]
out.parent.mkdir(parents=True,exist_ok=True); rr=[]
for r in rows:
 t=(r.get("title","")+" "+r.get("abstract","")).lower(); hits=[x for x in strong if x in t]
 if hits: rec,conf,rat="INCLUDE_CANDIDATE","HIGH","Explicit AR/MR signal: "+", ".join(hits[:3])
 elif re.search(r"\\baugmented\\b",t) and any(x in t for x in ["image","visual","display","surg","guid","navigation","reality"]): rec,conf,rat="INCLUDE_CANDIDATE","MEDIUM","Augmented visualization/guidance signal; verify against frozen AR criteria."
 else: rec,conf,rat="EXCLUDE_CANDIDATE","MEDIUM","No explicit AR/MR signal detected; manual verification required before any exclusion."
 d={k:r.get(k,"") for k in fields}; d.update(assisted_recommendation=rec,assisted_confidence=conf,assisted_rationale=rat,primary_decision="",reason_code="",primary_screener="",decision_timestamp="",evidence_note="",decision_version="",second_verification_state="",adjudication_state=""); rr.append(d)
with out.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rr)
from collections import Counter
c=Counter(x["assisted_recommendation"] for x in rr)
print("RUN60_TA01_ASSISTED",dict(c),"sha256",hashlib.sha256(out.read_bytes()).hexdigest())
