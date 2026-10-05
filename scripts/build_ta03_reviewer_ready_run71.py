#!/usr/bin/env python3
"""Run 71: build TA-03 reviewer-ready packet from validated assistance states."""
import csv,hashlib
from pathlib import Path
base=list(csv.DictReader(Path("evidence/screening/assisted/TA-03_ASSISTED_TRIAGE_RUN60.csv").open(encoding="utf-8-sig")))
audit={r["screening_ordinal"]:r for r in csv.DictReader(Path("evidence/screening/assisted/TA-03_INCLUDE_CANDIDATE_AUDIT_RUN71.csv").open(encoding="utf-8-sig"))}
assert len(base)==250 and len(audit)==238
direct=set("521 538 541 583 611".split())
out=[]
for r in base:
 o=r["screening_ordinal"]; a=audit.get(o,{})
 flags=a.get("run71_flags","")
 if r["assisted_recommendation"]=="EXCLUDE_CANDIDATE":
  prompt="LIKELY_EXCLUDE_CONFIRM"; reason=""; tier=1; basis="Run70 exclusion-side safety audit"
 elif "SECONDARY_OR_COMMENTARY_TITLE" in flags:
  prompt="LIKELY_EXCLUDE_CONFIRM"; reason="E-SECONDARY"; tier=2; basis="Run71 secondary-title verification"
 elif "ABSTRACT_MISSING" in flags:
  prompt="UNCERTAIN_ADVANCE"; reason=""; tier=3; basis="Run71 authoritative-report check required"
 elif o in direct:
  prompt="LIKELY_ADVANCE_CONFIRM"; reason=""; tier=4; basis="Run71 explicit AR/MR title evidence"
 elif a.get("run71_audit_state")=="PRIORITY_VERIFY":
  prompt="PRIORITY_VERIFY"; reason=""; tier=5; basis="Run71 contextual verification"
 else:
  prompt="LIKELY_ADVANCE_CONFIRM"; reason=""; tier=6; basis="Run71 no predefined high-risk flag"
 out.append({"review_order_tier":tier,"screening_ordinal":o,"batch_id":r["batch_id"],"pmid":r["pmid"],"doi":r["doi"],"title":r["title"],"abstract":r["abstract"],"year":r["year"],"journal":r["journal"],"risk_flags":flags,"reviewer_prompt":prompt,"suggested_reason_code":reason,"recommendation_basis":basis,"primary_decision":"","primary_reason_code":"","primary_screener":"","decision_timestamp":"","evidence_note":"","decision_version":"","second_verification_state":"","adjudication_state":""})
out.sort(key=lambda x:(x["review_order_tier"],int(x["screening_ordinal"])))
assert len(out)==250 and len({r["pmid"] for r in out})==250
dest=Path("evidence/screening/reviewer_ready/TA-03_REVIEWER_READY_RUN71.csv");dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
from collections import Counter
c=Counter(r["reviewer_prompt"] for r in out);sha=hashlib.sha256(dest.read_bytes()).hexdigest()
print("RUN71_TA03_REVIEWER_READY",dict(c),"sha256",sha)
