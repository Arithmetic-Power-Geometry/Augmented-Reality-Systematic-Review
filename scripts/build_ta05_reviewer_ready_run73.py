#!/usr/bin/env python3
"""Run 73: build TA-05 reviewer-ready packet after safety audits."""
import csv,hashlib
from pathlib import Path
base=list(csv.DictReader(Path("evidence/screening/assisted/TA-05_ASSISTED_TRIAGE_RUN60.csv").open(encoding="utf-8-sig")))
audit={r["screening_ordinal"]:r for r in csv.DictReader(Path("evidence/screening/assisted/TA-05_INCLUDE_CANDIDATE_AUDIT_RUN73.csv").open(encoding="utf-8-sig"))}
assert len(base)==250 and len(audit)==238
rescue_advance=set("1129 1210".split())
rescue_uncertain=set()
vr_only=set("1050 1082 1241 1243".split())
secondary_excl={"1233":"E-COMPANION"}
direct=set("1069 1134 1224".split())
out=[]
for r in base:
 o=r["screening_ordinal"];a=audit.get(o,{});flags=a.get("run73_flags","")
 if o in rescue_advance: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=2;basis="Run73 exclusion rescue: material XR/Next-AR intervention"
 elif o in rescue_uncertain: prompt="UNCERTAIN_ADVANCE";reason="";tier=3;basis="Run73 exclusion rescue"
 elif o in secondary_excl: prompt="LIKELY_EXCLUDE_CONFIRM";reason=secondary_excl[o];tier=1;basis="Run73 correction/companion verification"
 elif r["assisted_recommendation"]=="EXCLUDE_CANDIDATE":
  prompt="LIKELY_EXCLUDE_CONFIRM";reason="E-VR-ONLY" if o in vr_only else "E-NOT-AR";tier=1;basis="Run73 exclusion-side safety audit"
 elif "SECONDARY_OR_COMMENTARY_TITLE" in flags: prompt="LIKELY_EXCLUDE_CONFIRM";reason="E-SECONDARY";tier=2;basis="Run73 secondary-title confirmation"
 elif "ABSTRACT_MISSING" in flags: prompt="UNCERTAIN_ADVANCE";reason="";tier=3;basis="Run73 authoritative-report check"
 elif o in direct: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=4;basis="Run73 explicit AR/XR title"
 elif a.get("run73_audit_state")=="PRIORITY_VERIFY": prompt="PRIORITY_VERIFY";reason="";tier=5;basis="Run73 contextual verification"
 else: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=6;basis="Run73 no predefined high-risk flag"
 out.append({"review_order_tier":tier,"screening_ordinal":o,"batch_id":r["batch_id"],"pmid":r["pmid"],"doi":r["doi"],"title":r["title"],"abstract":r["abstract"],"year":r["year"],"journal":r["journal"],"risk_flags":flags,"reviewer_prompt":prompt,"suggested_reason_code":reason,"recommendation_basis":basis,"primary_decision":"","primary_reason_code":"","primary_screener":"","decision_timestamp":"","evidence_note":"","decision_version":"","second_verification_state":"","adjudication_state":""})
out.sort(key=lambda x:(x["review_order_tier"],int(x["screening_ordinal"])))
assert len(out)==250 and len({r["pmid"] for r in out})==250
dest=Path("evidence/screening/reviewer_ready/TA-05_REVIEWER_READY_RUN73.csv");dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
from collections import Counter
c=Counter(r["reviewer_prompt"] for r in out);sha=hashlib.sha256(dest.read_bytes()).hexdigest()
print("RUN73_TA05_REVIEWER_READY",dict(c),"sha256",sha)
