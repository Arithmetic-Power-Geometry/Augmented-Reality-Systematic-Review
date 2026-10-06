#!/usr/bin/env python3
"""Run 76: fail-closed final-results readiness audit. Never infers or fabricates review decisions."""
import csv,json
from pathlib import Path
R=Path(".")
def rows(p):
    return list(csv.DictReader(p.open(encoding="utf-8-sig"))) if p.exists() else []
def nonempty(r,*ks):
    return next(((r.get(k) or "").strip() for k in ks if (r.get(k) or "").strip()),"")
checks=[]
def add(name,ok,path,detail): checks.append(dict(gate=name,passed=bool(ok),path=str(path),detail=detail))

ta=R/"evidence/screening/final_title_abstract_ledger.csv"; tr=rows(ta)
valid={"include","exclude","uncertain"}
coded=[r for r in tr if nonempty(r,"primary_decision","ta_decision","decision").lower() in valid]
human=[r for r in coded if nonempty(r,"primary_screener","ta_screener","reviewer")]
add("title_abstract_final_ledger",len(tr)==7728 and len(coded)==7728 and len(human)==7728,ta,f"rows={len(tr)} coded={len(coded)} reviewer_attributed={len(human)} required=7728")

ft=R/"evidence/screening/final_full_text_ledger.csv"; fr=rows(ft)
ftcoded=[r for r in fr if nonempty(r,"full_text_decision","decision").lower() in {"include","exclude"}]
add("full_text_complete",bool(fr) and len(ftcoded)==len(fr),ft,f"rows={len(fr)} coded={len(ftcoded)}")

fam=R/"evidence/primary/final_study_family_ledger.csv"; famr=rows(fam)
add("study_families_resolved",bool(famr) and all(nonempty(r,"study_family_id","canonical_record_id") for r in famr),fam,f"rows={len(famr)}")

cc=R/"evidence/search/final_citation_chase_ledger.csv"; ccr=rows(cc)
add("citation_chasing_complete",bool(ccr) and all(nonempty(r,"status","decision") for r in ccr),cc,f"rows={len(ccr)}")

iv=R/"evidence/screening/final_independent_verification.csv"; ivr=rows(iv)
add("independent_verification_complete",bool(ivr) and all(nonempty(r,"second_reviewer","reviewer_2","verifier") for r in ivr),iv,f"rows={len(ivr)}")

freeze=R/"paper_writing/paper_artifacts/provenance/FINAL_CORPUS_FREEZE.sha256"
add("corpus_frozen",freeze.exists() and freeze.stat().st_size>20,freeze,"present" if freeze.exists() else "missing")

analysis_dir=R/"paper_writing/paper_artifacts/final_analysis"
needed=[f"NEXT-{i:02d}" for i in range(6,20)]
present=[x for x in needed if any(analysis_dir.glob(x+"*"))] if analysis_dir.exists() else []
add("final_NEXT06_NEXT19_rerun",len(present)==len(needed),analysis_dir,f"present={len(present)}/14")

all_pass=all(x["passed"] for x in checks)
out=R/"paper_writing/paper_artifacts/provenance/RUN76_FINAL_RESULTS_READINESS.json";out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"all_pass":all_pass,"checks":checks},indent=2),encoding="utf-8")
print("RUN76_FINAL_RESULTS_READINESS", "PASS" if all_pass else "BLOCKED")
for x in checks: print(("PASS" if x["passed"] else "BLOCK"),x["gate"],x["detail"])
raise SystemExit(0 if all_pass else 2)
