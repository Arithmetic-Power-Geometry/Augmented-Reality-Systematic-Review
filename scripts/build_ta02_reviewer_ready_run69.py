#!/usr/bin/env python3
"""Run 69: consolidate TA-02 into a reviewer-ready 250-record packet."""
import csv, hashlib
from pathlib import Path
base=list(csv.DictReader(Path("evidence/screening/assisted/TA-02_ASSISTED_TRIAGE_RUN60.csv").open(encoding="utf-8-sig")))
audit={r["screening_ordinal"]:r for r in csv.DictReader(Path("evidence/screening/assisted/TA-02_INCLUDE_CANDIDATE_AUDIT_RUN68.csv").open(encoding="utf-8-sig"))}
assert len(base)==250 and len(audit)==209
rescued={"497"}
likely_excl_priority={"309":"E-NOT-AR","332":"E-SECONDARY","356":"E-SECONDARY","365":"E-SECONDARY","448":"E-SECONDARY","465":"E-NOT-AR","483":"E-SECONDARY","498":"E-NOT-AR"}
strong_adv=set("270 272 273 286 291 302 312 315 319 345 346 352 357 360 362 375 379 381 396 401 420 453 494".split())
missing=set("367 372 373 385 386 387 388 406 459".split())
contextual=set("322 446 463".split())
out=[]
for r in base:
 o=r["screening_ordinal"]; ar=audit.get(o,{})
 if o in likely_excl_priority: tier=1; prompt="LIKELY_EXCLUDE_CONFIRM"; reason=likely_excl_priority[o]; basis="Run69 record-level priority verification"
 elif r["assisted_recommendation"]=="EXCLUDE_CANDIDATE" and o not in rescued: tier=2; prompt="LIKELY_EXCLUDE_CONFIRM"; reason="E-NOT-AR"; basis="Run67 exclusion-candidate rescue audit"
 elif o in rescued: tier=3; prompt="UNCERTAIN_ADVANCE"; reason=""; basis="Run67 XR/AR rescue"
 elif o in missing: tier=3; prompt="UNCERTAIN_ADVANCE"; reason=""; basis="Run69 missing abstract; authoritative report required"
 elif o in contextual: tier=4; prompt="PRIORITY_VERIFY"; reason=""; basis="Run69 contextual genuine-review case"
 elif o in strong_adv: tier=5; prompt="LIKELY_ADVANCE_CONFIRM"; reason=""; basis="Run69 direct implemented/evaluated AR/MR evidence"
 elif ar.get("run68_audit_state")=="PRIORITY_VERIFY": tier=4; prompt="PRIORITY_VERIFY"; reason=""; basis="Run68 risk flag"
 else: tier=6; prompt="LIKELY_ADVANCE_CONFIRM"; reason=""; basis="Run68 no predefined high-risk flag"
 out.append({"review_order_tier":tier,"screening_ordinal":o,"batch_id":r["batch_id"],"pmid":r["pmid"],"doi":r["doi"],"title":r["title"],"abstract":r["abstract"],"year":r["year"],"journal":r["journal"],"assisted_recommendation":r["assisted_recommendation"],"risk_flags":ar.get("run68_flags",""),"reviewer_prompt":prompt,"suggested_reason_code":reason,"recommendation_basis":basis,"primary_decision":"","primary_reason_code":"","primary_screener":"","decision_timestamp":"","evidence_note":"","decision_version":"","second_verification_state":"","adjudication_state":""})
out.sort(key=lambda x:(x["review_order_tier"],int(x["screening_ordinal"])))
assert len(out)==250 and len({r["pmid"] for r in out})==250
dest=Path("evidence/screening/reviewer_ready/TA-02_REVIEWER_READY_RUN69.csv");dest.parent.mkdir(parents=True,exist_ok=True)
with dest.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(out[0]));w.writeheader();w.writerows(out)
from collections import Counter
c=Counter(r["reviewer_prompt"] for r in out); t=Counter(str(r["review_order_tier"]) for r in out)
sha=hashlib.sha256(dest.read_bytes()).hexdigest()
print("RUN69_TA02_REVIEWER_READY",dict(c),dict(t),"sha256",sha)
