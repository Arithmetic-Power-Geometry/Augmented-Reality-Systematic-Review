#!/usr/bin/env python3
"""Run 65: validate TA-01 genuine primary screening completion."""
import csv,json
from pathlib import Path
p=Path("evidence/screening/reviewer_ready/TA-01_REVIEWER_READY_RUN64.csv")
out=Path("paper_writing/paper_artifacts/provenance/RUN65_TA01_PRIMARY_COMPLETION.json")
if not p.exists():
    result={"complete":False,"blocker":"reviewer-ready sheet not materialized in repository"}
else:
    rows=list(csv.DictReader(p.open(encoding="utf-8-sig")))
    valid={"INCLUDE","EXCLUDE","UNCERTAIN"}
    decided=[r for r in rows if (r.get("primary_decision") or "").strip().upper() in valid]
    invalid=[r for r in rows if (r.get("primary_decision") or "").strip() and (r.get("primary_decision") or "").strip().upper() not in valid]
    missing_identity=[r for r in decided if not (r.get("primary_screener") or "").strip()]
    result={"complete":len(rows)==250 and len(decided)==250 and not invalid and not missing_identity,
            "rows":len(rows),"valid_primary_decisions":len(decided),"remaining":len(rows)-len(decided),
            "invalid_states":len(invalid),"decisions_missing_screener_identity":len(missing_identity)}
out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2),encoding="utf-8")
print("RUN65_TA01_PRIMARY_COMPLETION",json.dumps(result,sort_keys=True))
if not result["complete"]: raise SystemExit(2)
