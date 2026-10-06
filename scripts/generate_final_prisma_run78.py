#!/usr/bin/env python3
"""Run 78 final PRISMA/manuscript numerical generator. Requires frozen corpus."""
import csv,json,re,sys
from pathlib import Path
R=Path("."); freeze=R/"paper_writing/paper_artifacts/provenance/FINAL_CORPUS_FREEZE.sha256"
if not freeze.exists(): print("FINAL_GENERATOR BLOCKED: corpus not frozen");sys.exit(2)
def rows(p): return list(csv.DictReader(p.open(encoding="utf-8-sig")))
ta=rows(R/"evidence/screening/final_title_abstract_ledger.csv"); ft=rows(R/"evidence/screening/final_full_text_ledger.csv"); fam=rows(R/"evidence/primary/final_study_family_ledger.csv")
inc_ta=sum((r.get("primary_decision") or "").lower() in {"include","uncertain"} for r in ta); exc_ta=len(ta)-inc_ta
inc_reports=[r for r in ft if (r.get("full_text_decision") or "").lower()=="include"]; exc_reports=[r for r in ft if (r.get("full_text_decision") or "").lower()=="exclude"]
studies=len({(r.get("study_family_id") or "").strip() for r in fam if (r.get("study_family_id") or "").strip()})
prisma={"unique_pubmed_q00":10198,"prescreen_excluded":2459,"records_screened":7728,"title_abstract_excluded":exc_ta,"reports_sought":inc_ta,"reports_assessed":len(ft),"full_text_excluded":len(exc_reports),"included_reports":len(inc_reports),"included_studies":studies}
out=R/"paper_writing/paper_artifacts/final_analysis";out.mkdir(parents=True,exist_ok=True)
(out/"FINAL_PRISMA_COUNTS.json").write_text(json.dumps(prisma,indent=2),encoding="utf-8")
md="# Final PRISMA Counts\n\n"+"\n".join(f"- **{k.replace('_',' ').title()}:** {v}" for k,v in prisma.items())+"\n"
(out/"FINAL_PRISMA_COUNTS.md").write_text(md,encoding="utf-8")
print("FINAL_PRISMA_GENERATED",json.dumps(prisma))
