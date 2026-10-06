#!/usr/bin/env python3
"""Fail-closed Stage-2 gate."""
import csv, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s1=ROOT/"evidence/corpus/stage1/STAGE1_GATE_CHECKLIST.csv"
checks=[]
if s1.exists():
    rows=list(csv.DictReader(s1.open(encoding="utf-8-sig")))
    checks.append(("stage1_complete", bool(rows) and all(r["status"]=="PASS" for r in rows)))
else: checks.append(("stage1_complete",False))
required=[
"evidence/corpus/stage2/REVIEWER_B_ELIGIBILITY_TEMPLATE.csv",
"evidence/corpus/stage2/REVIEWER_B_PI_TEMPLATE.csv",
"evidence/corpus/stage2/REVIEWER_B_COMPARABILITY_TEMPLATE.csv",
"evidence/corpus/stage2/REVIEWER_B_TRANSFER_TEMPLATE.csv",
"evidence/corpus/stage2/ADJUDICATION_TEMPLATE.csv"]
for p in required:
    fp=ROOT/p
    rows=list(csv.DictReader(fp.open(encoding="utf-8-sig"))) if fp.exists() else []
    checks.append((p, len(rows)>0))
report={"all_pass":all(v for _,v in checks),"checks":[{"name":k,"pass":v} for k,v in checks]}
out=ROOT/"evidence/corpus/stage2/STAGE2_GATE_REPORT.json";out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report,indent=2))
sys.exit(0 if report["all_pass"] else 2)
