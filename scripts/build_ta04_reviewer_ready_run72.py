#!/usr/bin/env python3
"""Run 72: build TA-04 reviewer packet after exclusion rescue and include-risk validation."""
import csv,hashlib
from pathlib import Path
base=list(csv.DictReader(Path("evidence/screening/assisted/TA-04_ASSISTED_TRIAGE_RUN60.csv").open(encoding="utf-8-sig")))
audit={r["screening_ordinal"]:r for r in csv.DictReader(Path("evidence/screening/assisted/TA-04_INCLUDE_CANDIDATE_AUDIT_RUN72.csv").open(encoding="utf-8-sig"))}
assert len(base)==250 and len(audit)==233
rescue_advance=set("765 773 902 917 960".split())
rescue_uncertain=set("589 825 982".split())
vr_only=set("775 998".split())
direct=set("756 757 991".split())
out=[]
for r in base:
 o=r["screening_ordinal"];a=audit.get(o,{});flags=a.get("run72_flags","")
 if o in rescue_advance: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=2;basis="Run72 exclusion rescue: implemented AR/augmented-visualization evidence"
 elif o in rescue_uncertain: prompt="UNCERTAIN_ADVANCE";reason="";tier=3;basis="Run72 exclusion rescue: AR materiality/separability requires reviewer"
 elif r["assisted_recommendation"]=="EXCLUDE_CANDIDATE":
  prompt="LIKELY_EXCLUDE_CONFIRM";reason="E-VR-ONLY" if o in vr_only else "E-NOT-AR";tier=1;basis="Run72 exclusion-side safety audit"
 elif "SECONDARY_OR_COMMENTARY_TITLE" in flags: prompt="LIKELY_EXCLUDE_CONFIRM";reason="E-SECONDARY";tier=2;basis="Run72 secondary-title confirmation"
 elif "ABSTRACT_MISSING" in flags: prompt="UNCERTAIN_ADVANCE";reason="";tier=3;basis="Run72 authoritative-report check"
 elif o in direct: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=4;basis="Run72 explicit AR title"
 elif a.get("run72_audit_state")=="PRIORITY_VERIFY": prompt="PRIORITY_VERIFY";reason="";tier=5;basis="Run72 contextual verification"
 else: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=6;basis="Run72 no predefined high-risk flag"
 out.append({"review_order_tier":tier,"screening_ordinal":o,"batch_id":r["batch_id"],"pmid":r["pmid"],"doi":r["doi"],"title":r["title"],"abstract":r["abstract"],"year":r["year"],"journal":r["journal"],"risk_flags":flags,"reviewer_prompt":prompt,"suggested_reason_code":reason,"recommendation_basis":basis,"primary_decision":"","primary_reason_code":"","primary_screener":"","decision_timestamp":"","evidence_note":"","decision_version":"","second_verification_state":"","adjudication_state":""})
out.sort(key=lambda x:(x["review_order_tier"],int(x["screening_ordinal"])))
assert len(out)==250 and len({r["pmid"] for r in out})==250
dest=Path("evidence/screening/reviewer_ready/TA-04_REVIEWER_READY_RUN72.csv");dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
from collections import Counter
c=Counter(r["reviewer_prompt"] for r in out);sha=hashlib.sha256(dest.read_bytes()).hexdigest()
print("RUN72_TA04_REVIEWER_READY",dict(c),"sha256",sha)
