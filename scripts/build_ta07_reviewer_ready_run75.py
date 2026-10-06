#!/usr/bin/env python3
"""Run 75: build TA-07 reviewer-ready packet after safety audits."""
import csv,hashlib
from pathlib import Path
base=list(csv.DictReader(Path("evidence/screening/assisted/TA-07_ASSISTED_TRIAGE_RUN60.csv").open(encoding="utf-8-sig")))
audit={r["screening_ordinal"]:r for r in csv.DictReader(Path("evidence/screening/assisted/TA-07_INCLUDE_CANDIDATE_AUDIT_RUN75.csv").open(encoding="utf-8-sig"))}
assert len(base)==250 and len(audit)==236
rescue_advance=set("1509 1632".split())
rescue_uncertain=set("1714".split())
vr_only=set("1628 1643 1702".split())
secondary_excl=set("1594 1641 1732".split())
direct=set("1503".split())
out=[]
for r in base:
 o=r["screening_ordinal"];a=audit.get(o,{});flags=a.get("run75_flags","")
 if o in rescue_advance: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=2;basis="Run75 exclusion rescue: material AR intervention"
 elif o in rescue_uncertain: prompt="UNCERTAIN_ADVANCE";reason="";tier=3;basis="Run75 XR separability/materiality requires reviewer"
 elif o in secondary_excl: prompt="LIKELY_EXCLUDE_CONFIRM";reason="E-SECONDARY";tier=1;basis="Run75 secondary/perspective confirmation"
 elif r["assisted_recommendation"]=="EXCLUDE_CANDIDATE":
  prompt="LIKELY_EXCLUDE_CONFIRM";reason="E-VR-ONLY" if o in vr_only else "E-NOT-AR";tier=1;basis="Run75 exclusion-side safety audit"
 elif "SECONDARY_OR_COMMENTARY_TITLE" in flags: prompt="LIKELY_EXCLUDE_CONFIRM";reason="E-SECONDARY";tier=2;basis="Run75 secondary-title confirmation"
 elif "ABSTRACT_MISSING" in flags: prompt="UNCERTAIN_ADVANCE";reason="";tier=3;basis="Run75 authoritative-report check"
 elif o in direct: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=4;basis="Run75 explicit AR title"
 elif a.get("run75_audit_state")=="PRIORITY_VERIFY": prompt="PRIORITY_VERIFY";reason="";tier=5;basis="Run75 contextual verification"
 else: prompt="LIKELY_ADVANCE_CONFIRM";reason="";tier=6;basis="Run75 no predefined high-risk flag"
 out.append({"review_order_tier":tier,"screening_ordinal":o,"batch_id":r["batch_id"],"pmid":r["pmid"],"doi":r["doi"],"title":r["title"],"abstract":r["abstract"],"year":r["year"],"journal":r["journal"],"risk_flags":flags,"reviewer_prompt":prompt,"suggested_reason_code":reason,"recommendation_basis":basis,"primary_decision":"","primary_reason_code":"","primary_screener":"","decision_timestamp":"","evidence_note":"","decision_version":"","second_verification_state":"","adjudication_state":""})
out.sort(key=lambda x:(x["review_order_tier"],int(x["screening_ordinal"])))
assert len(out)==250 and len({r["pmid"] for r in out})==250
dest=Path("evidence/screening/reviewer_ready/TA-07_REVIEWER_READY_RUN75.csv");dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
from collections import Counter
c=Counter(r["reviewer_prompt"] for r in out);sha=hashlib.sha256(dest.read_bytes()).hexdigest()
print("RUN75_TA07_REVIEWER_READY",dict(c),"sha256",sha)
