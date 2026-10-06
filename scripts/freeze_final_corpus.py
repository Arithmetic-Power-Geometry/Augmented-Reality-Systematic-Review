#!/usr/bin/env python3
"""Freeze final corpus only after every evidence gate passes."""
import csv,hashlib,json,sys
from pathlib import Path
R=Path(".")
def rows(p): return list(csv.DictReader(p.open(encoding="utf-8-sig"))) if p.exists() else []
ta=rows(R/"evidence/screening/final_title_abstract_ledger.csv")
ok_ta=len(ta)==7728 and all((r.get("primary_decision") or "").lower() in {"include","exclude","uncertain"} and (r.get("primary_screener") or "").strip() for r in ta)
ft=rows(R/"evidence/screening/final_full_text_ledger.csv"); ok_ft=bool(ft) and all((r.get("full_text_decision") or "").lower() in {"include","exclude"} for r in ft)
fam=rows(R/"evidence/primary/final_study_family_ledger.csv"); ok_fam=bool(fam) and all((r.get("study_family_id") or "").strip() for r in fam)
cc=rows(R/"evidence/search/final_citation_chase_ledger.csv"); ok_cc=bool(cc) and all((r.get("status") or "").strip() for r in cc)
iv=rows(R/"evidence/screening/final_independent_verification.csv"); ok_iv=bool(iv) and all((r.get("second_reviewer") or "").strip() for r in iv)
checks={"title_abstract":ok_ta,"full_text":ok_ft,"families":ok_fam,"citation_chase":ok_cc,"verification":ok_iv}
if not all(checks.values()):
 print("CORPUS_FREEZE BLOCKED",checks);sys.exit(2)
parts=[]
for p in ["evidence/screening/final_title_abstract_ledger.csv","evidence/screening/final_full_text_ledger.csv","evidence/primary/final_study_family_ledger.csv","evidence/search/final_citation_chase_ledger.csv","evidence/screening/final_independent_verification.csv"]:
 b=(R/p).read_bytes();parts.append(p+":"+hashlib.sha256(b).hexdigest())
digest=hashlib.sha256("\n".join(parts).encode()).hexdigest()
out=R/"paper_writing/paper_artifacts/provenance/FINAL_CORPUS_FREEZE.sha256";out.parent.mkdir(parents=True,exist_ok=True);out.write_text(digest+"\n"+"\n".join(parts)+"\n")
print("CORPUS_FREEZE PASS",digest)
