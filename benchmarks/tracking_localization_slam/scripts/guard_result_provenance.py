#!/usr/bin/env python3
"""Fail CI if a scientific result appears without minimum provenance."""
import csv,sys
from pathlib import Path
p=Path(sys.argv[1])
rows=list(csv.DictReader(p.open(newline="",encoding="utf-8")))
required=["run_id","method_commit","dataset_id","sequence_or_query","hardware_id","environment_id","evaluator_commit","raw_output_path"]
for n,row in enumerate(rows,2):
    populated=any((row.get(k) or "").strip() for k in ["ate","rpe","localization_recall","latency_ms","fps","peak_memory_mb","energy_j"])
    if populated:
        miss=[k for k in required if not (row.get(k) or "").strip()]
        if miss: raise SystemExit(f"line {n}: result without provenance: {','.join(miss)}")
print("RESULT_PROVENANCE_GUARD_OK")
