#!/usr/bin/env python3
import csv, subprocess, sys, tempfile
from pathlib import Path

root=Path(__file__).resolve().parents[1]
adapter=root/"adapters"/"tum_trajectory_to_common.py"
sample=root/"testdata"/"synthetic_tum.txt"
with tempfile.TemporaryDirectory() as d:
    out=Path(d)/"trajectory.csv"
    subprocess.check_call([sys.executable,str(adapter),str(sample),str(out)])
    rows=list(csv.DictReader(out.open(encoding="utf-8")))
    assert len(rows)==3
    assert rows[0]["timestamp"]=="0.0"
    assert rows[-1]["tx"]=="0.2"
print("ADAPTER_SMOKE_OK")
