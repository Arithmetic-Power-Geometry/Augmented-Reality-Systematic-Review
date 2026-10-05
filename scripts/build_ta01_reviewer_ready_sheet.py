#!/usr/bin/env python3
"""Run 64: build reviewer-ready TA-01 sheet without fabricating primary decisions."""
import csv, hashlib
from pathlib import Path

base=Path("evidence/screening/assisted/TA-01_ASSISTED_TRIAGE_RUN60.csv")
audit=Path("evidence/screening/assisted/TA-01_INCLUDE_CANDIDATE_AUDIT_RUN62.csv")
if not base.exists(): raise SystemExit("BLOCK missing Run60 TA-01 ledger")
B=list(csv.DictReader(base.open(encoding="utf-8-sig")))
if len(B)!=250: raise SystemExit(f"BLOCK expected 250, got {len(B)}")
A={}
if audit.exists():
    for r in csv.DictReader(audit.open(encoding="utf-8-sig")):
        A[r["screening_ordinal"]]=r

rescued={"114","132","135","160","219","244","245"}
likely_non_ar=set()
for r in B:
    if r.get("assisted_recommendation")=="EXCLUDE_CANDIDATE" and r["screening_ordinal"] not in rescued:
        likely_non_ar.add(r["screening_ordinal"])
run63={
"3":("E-SECONDARY","Review; AR appears only as future development."),
"17":("E-VR-ONLY","Principally VR; AR described as future environment."),
"67":("E-NOT-AR","SLAM paper; AR is application/reference context."),
"220":("E-SECONDARY","Trend/overview paper; AR one of several future topics."),
"227":("E-NOT-AR","Evaluated for VR; AR only possible application."),
"237":("E-SECONDARY","Commentary on another mixed-reality study.")
}
strong_advance={"11","21","22","25","29","71","174","189","190","234"}

out=[]
for r in B:
    o=r["screening_ordinal"]; ar=A.get(o,{})
    if o in run63:
        tier=1; recommendation="LIKELY_EXCLUDE_CONFIRM"; reason,why=run63[o]
    elif o in likely_non_ar:
        tier=2; recommendation="LIKELY_EXCLUDE_CONFIRM"; reason="E-NOT-AR"; why="Run61 likely non-AR candidate; genuine confirmation required."
    elif o in rescued:
        tier=3; recommendation="ADVANCE_OR_UNCERTAIN_CONFIRM"; reason=""; why="Run61 rescued from assisted false-negative exclusion."
    elif ar.get("run62_audit_state")=="PRIORITY_VERIFY":
        tier=4; recommendation="PRIORITY_VERIFY"; reason=""; why=ar.get("run62_flags","")
    elif o in strong_advance:
        tier=5; recommendation="LIKELY_ADVANCE_CONFIRM"; reason=""; why="Run63 implemented/evaluated AR evidence."
    else:
        tier=6; recommendation="LIKELY_ADVANCE_CONFIRM"; reason=""; why="No predefined high-risk flag; primary review still required."
    out.append({
      "review_order_tier":tier,"screening_ordinal":o,"batch_id":r["batch_id"],"pmid":r["pmid"],"doi":r["doi"],
      "title":r["title"],"abstract":r["abstract"],"year":r["year"],"journal":r["journal"],
      "assisted_recommendation_run60":r["assisted_recommendation"],
      "run62_flags":ar.get("run62_flags",""),"reviewer_prompt":recommendation,
      "suggested_reason_code":reason,"reviewer_context":why,
      "primary_decision":"","primary_reason_code":"","primary_screener":"","decision_timestamp":"",
      "evidence_note":"","decision_version":"","second_verification_state":"","adjudication_state":""
    })
out.sort(key=lambda x:(x["review_order_tier"],int(x["screening_ordinal"])))
dest=Path("evidence/screening/reviewer_ready/TA-01_REVIEWER_READY_RUN64.csv");dest.parent.mkdir(parents=True,exist_ok=True)
fields=list(out[0])
with dest.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
from collections import Counter
c=Counter(x["reviewer_prompt"] for x in out); tiers=Counter(str(x["review_order_tier"]) for x in out)
sha=hashlib.sha256(dest.read_bytes()).hexdigest()
print("RUN64_REVIEWER_READY n=250 prompts="+str(dict(c))+" tiers="+str(dict(tiers))+" sha256="+sha)
