#!/usr/bin/env python3
"""Fail-closed final corpus gate. It validates readiness; it never invents decisions."""
import csv, hashlib, json
from pathlib import Path

ROOT=Path(".")
checks=[]
def add(name,ok,evidence,detail):
    checks.append({"gate":name,"pass":bool(ok),"evidence":evidence,"detail":detail})

# Formal source matrix
mx=ROOT/"evidence/search/formal_search_execution_matrix.csv"
if mx.exists():
    rows=list(csv.DictReader(mx.open(encoding="utf-8-sig")))
    statuses=[(r.get("status") or r.get("execution_status") or "").upper() for r in rows]
    executed=sum(s=="EXECUTED" for s in statuses)
    registry=ROOT/"evidence/search/search_registry.csv"
    limitation_rows=0
    if registry.exists():
        rr=list(csv.DictReader(registry.open(encoding="utf-8-sig")))
        limitation_rows=sum((x.get("status") or "").upper()=="LIMITATION" for x in rr)
    accounted=executed+limitation_rows
    add("registered_source_cells_accounted",len(rows)>=91 and accounted>=91,str(mx),f"matrix_rows={len(rows)} executed={executed} limitation_registry_rows={limitation_rows} accounted={accounted}")
else: add("registered_source_cells_accounted",False,str(mx),"missing")

# Screening completion cannot be inferred from work-unit generation.
screen_candidates=list((ROOT/"evidence/screening").glob("**/*.csv")) if (ROOT/"evidence/screening").exists() else []
completed=0; unresolved=0
for p in screen_candidates:
    try:
        rs=list(csv.DictReader(p.open(encoding="utf-8-sig")))
    except Exception: continue
    for r in rs:
        if "ta_decision" in r:
            d=(r.get("ta_decision") or "").strip().lower()
            if d in {"include","exclude","uncertain"}: completed+=1
            else: unresolved+=1
add("title_abstract_screening_complete",completed>=7728 and unresolved==0,"evidence/screening/",f"coded={completed} blank_or_unresolved={unresolved}")

# Required final ledgers: intentionally strict.
required=[
 ("full_text_complete","evidence/screening/final_full_text_ledger.csv"),
 ("study_families_resolved","evidence/primary/final_study_family_ledger.csv"),
 ("citation_chasing_complete","evidence/search/final_citation_chase_ledger.csv"),
 ("independent_verification_complete","evidence/screening/final_independent_verification.csv"),
]
for name,path in required:
    p=ROOT/path
    ok=p.exists() and p.stat().st_size>50
    add(name,ok,path,"present" if ok else "not yet frozen")

all_pass=all(x["pass"] for x in checks)
out=ROOT/"paper_writing/paper_artifacts/provenance/RUN57_FINAL_CORPUS_GATE.json"
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"all_pass":all_pass,"checks":checks},indent=2),encoding="utf-8")
if all_pass:
    freeze=ROOT/"paper_writing/paper_artifacts/provenance/FINAL_CORPUS_FREEZE.sha256"
    targets=[mx]+[ROOT/p for _,p in required]
    lines=[]
    for p in targets:
        lines.append(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.as_posix()}")
    freeze.write_text("\n".join(lines)+"\n",encoding="utf-8")
    print("FINAL_CORPUS_GATE PASS")
else:
    print("FINAL_CORPUS_GATE BLOCKED")
    for x in checks:
        print(("PASS" if x["pass"] else "BLOCK"),x["gate"],x["detail"])

# Run 57 execution trigger.
