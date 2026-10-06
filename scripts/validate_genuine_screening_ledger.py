#!/usr/bin/env python3
"""Validate genuine reviewer-entered title/abstract decisions before downstream use."""
import csv,sys
from pathlib import Path
p=Path("evidence/screening/final_title_abstract_ledger.csv")
rs=list(csv.DictReader(p.open(encoding="utf-8-sig")))
assert len(rs)==7728, f"expected 7728 rows, got {len(rs)}"
allowed={"include","exclude","uncertain"}
errors=[]
for i,r in enumerate(rs,2):
 d=(r.get("primary_decision") or "").strip().lower()
 reviewer=(r.get("primary_screener") or "").strip()
 reason=(r.get("primary_reason_code") or "").strip()
 if d not in allowed: errors.append((i,"decision",d))
 if not reviewer: errors.append((i,"reviewer","blank"))
 if d=="exclude" and not reason: errors.append((i,"exclude_reason","blank"))
 if (r.get("reviewer_prompt") or "")==d: pass
print(f"rows={len(rs)} validation_errors={len(errors)}")
if errors:
 for e in errors[:30]: print("ERROR",e)
 sys.exit(2)
print("GENUINE_SCREENING_LEDGER VALID")
