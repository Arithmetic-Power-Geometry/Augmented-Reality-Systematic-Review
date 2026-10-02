#!/usr/bin/env python3
import argparse,csv,math
from pathlib import Path
REQ=["timestamp","tx","ty","tz","qx","qy","qz","qw"]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("trajectory"); a=ap.parse_args()
    with Path(a.trajectory).open(newline="",encoding="utf-8") as f:
        r=csv.DictReader(f)
        if r.fieldnames!=REQ: raise SystemExit("invalid trajectory header")
        rows=list(r)
    if not rows: raise SystemExit("empty trajectory")
    last=None
    for i,row in enumerate(rows,2):
        vals=[float(row[k]) for k in REQ]
        if not all(math.isfinite(x) for x in vals): raise SystemExit(f"non-finite value line {i}")
        if last is not None and vals[0]<=last: raise SystemExit(f"non-increasing timestamp line {i}")
        q=vals[4:8]; norm=sum(x*x for x in q)**0.5
        if abs(norm-1.0)>1e-2: raise SystemExit(f"non-unit quaternion line {i}: {norm}")
        last=vals[0]
    print(f"TRAJECTORY_VALID poses={len(rows)}")
if __name__=="__main__": main()
