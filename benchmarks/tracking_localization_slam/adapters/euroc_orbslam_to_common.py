#!/usr/bin/env python3
"""Normalize ORB-SLAM3 SaveTrajectoryEuRoC output.
Expected upstream row: timestamp tx ty tz qx qy qz qw
"""
import argparse,csv,math
from pathlib import Path
H=["timestamp","tx","ty","tz","qx","qy","qz","qw"]
ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("output"); a=ap.parse_args()
rows=[]
for n,line in enumerate(Path(a.input).read_text(encoding="utf-8").splitlines(),1):
    s=line.strip()
    if not s or s.startswith("#"): continue
    p=s.split()
    if len(p)!=8: raise SystemExit(f"line {n}: expected 8 fields, got {len(p)}")
    v=[float(x) for x in p]
    if not all(math.isfinite(x) for x in v): raise SystemExit(f"line {n}: non-finite")
    rows.append(v)
if not rows: raise SystemExit("empty ORB-SLAM3 trajectory")
Path(a.output).parent.mkdir(parents=True,exist_ok=True)
with Path(a.output).open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(H); w.writerows(rows)
print(f"ORB_EUROC_NORMALIZED poses={len(rows)}")
