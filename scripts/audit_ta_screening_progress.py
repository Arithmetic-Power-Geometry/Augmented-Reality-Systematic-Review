#!/usr/bin/env python3
"""Audit genuine title/abstract progress without manufacturing decisions."""
import csv, json
from pathlib import Path
root=Path("evidence/screening/formal_pubmed_batches")
expected={f"TA-{i:02d}":250 for i in range(1,31)}; expected["TA-31"]=228
rows=[]
total_valid=0
for bid,n in expected.items():
    p=root/f"{bid}.csv"
    state="NOT_COMMITTED"
    valid=0; blank=n
    if p.exists():
        rs=list(csv.DictReader(p.open(encoding="utf-8-sig")))
        vals=[(r.get("ta_decision") or r.get("primary_decision") or "").strip().lower() for r in rs]
        valid=sum(v in {"include","exclude","uncertain"} for v in vals)
        blank=len(rs)-valid
        state="COMPLETE" if len(rs)==n and valid==n else "IN_PROGRESS"
    rows.append({"batch_id":bid,"expected":n,"valid_primary_decisions":valid,"remaining":blank,"state":state})
    total_valid+=valid
out=Path("paper_writing/paper_artifacts/provenance/RUN58_TA_SCREENING_PROGRESS.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({"expected_total":7728,"valid_primary_decisions":total_valid,"remaining":7728-total_valid,"batches":rows},indent=2),encoding="utf-8")
print(f"TA_PROGRESS valid={total_valid} remaining={7728-total_valid}")

# Run 58 execution trigger.
