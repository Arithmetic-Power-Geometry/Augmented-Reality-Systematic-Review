#!/usr/bin/env python3
"""Run 78: initialize downstream evidence ledgers without inventing evidence."""
import csv,json,hashlib
from pathlib import Path
R=Path(".")
ta=R/"evidence/screening/final_title_abstract_ledger.csv"
rs=list(csv.DictReader(ta.open(encoding="utf-8-sig")))
assert len(rs)==7728
valid={"include","exclude","uncertain"}
coded=[r for r in rs if (r.get("primary_decision") or "").strip().lower() in valid and (r.get("primary_screener") or "").strip()]
ready=len(coded)==7728
specs={
"evidence/screening/final_full_text_ledger.csv":["report_id","pmid","doi","title","retrieval_status","full_text_decision","full_text_reason_code","primary_screener","decision_timestamp","evidence_note","second_verification_state","adjudication_state"],
"evidence/primary/final_study_family_ledger.csv":["report_id","study_family_id","canonical_record_id","relation_type","resolution_note","resolver","timestamp"],
"evidence/search/final_citation_chase_ledger.csv":["seed_study_family_id","direction","candidate_id","citation","status","decision","reason_code","reviewer","timestamp"],
"evidence/screening/final_independent_verification.csv":["record_or_report_id","stage","primary_decision","second_decision","second_reviewer","agreement_state","adjudicated_decision","adjudicator","timestamp"]
}
for path,fields in specs.items():
 p=R/path;p.parent.mkdir(parents=True,exist_ok=True)
 if not p.exists():
  with p.open("w",encoding="utf-8",newline="") as f: csv.DictWriter(f,fieldnames=fields).writeheader()
prov=R/"paper_writing/paper_artifacts/provenance/RUN78_DOWNSTREAM_INITIALIZATION.json";prov.parent.mkdir(parents=True,exist_ok=True)
prov.write_text(json.dumps({"title_abstract_ready":ready,"genuine_decisions":len(coded),"required":7728,"downstream_ledgers_initialized":list(specs),"note":"Headers only until genuine upstream evidence exists."},indent=2),encoding="utf-8")
print("RUN78_DOWNSTREAM_INIT", "READY" if ready else "BLOCKED", f"genuine_decisions={len(coded)}/7728")
