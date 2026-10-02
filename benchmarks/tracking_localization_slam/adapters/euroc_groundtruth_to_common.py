#!/usr/bin/env python3
"""Convert canonical EuRoC state_groundtruth_estimate0/data.csv to common pose CSV.

Canonical pose columns:
#timestamp [ns], p_RS_R_x/y/z [m], q_RS_w/x/y/z []
Output quaternion order is qx,qy,qz,qw.
"""
import argparse,csv,math
from pathlib import Path
OUT=["timestamp","tx","ty","tz","qx","qy","qz","qw"]
POSE=["#timestamp [ns]","p_RS_R_x [m]","p_RS_R_y [m]","p_RS_R_z [m]",
      "q_RS_w []","q_RS_x []","q_RS_y []","q_RS_z []"]
def norm(s): return s.strip()
ap=argparse.ArgumentParser(); ap.add_argument("input"); ap.add_argument("output"); a=ap.parse_args()
with Path(a.input).open(newline="",encoding="utf-8-sig") as f:
    r=csv.DictReader(f,skipinitialspace=True)
    fields=[norm(x) for x in (r.fieldnames or [])]
    missing=[x for x in POSE if x not in fields]
    if missing: raise SystemExit("non-canonical/missing EuRoC columns: "+", ".join(missing))
    rows=[]
    for n,raw in enumerate(r,2):
        row={norm(k):v for k,v in raw.items()}
        ns=int(row["#timestamp [ns]"])
        p=[float(row[x]) for x in POSE[1:4]]
        qw,qx,qy,qz=[float(row[x]) for x in POSE[4:8]]
        vals=p+[qx,qy,qz,qw]
        if not all(math.isfinite(x) for x in vals): raise SystemExit(f"line {n}: non-finite")
        qn=math.sqrt(qx*qx+qy*qy+qz*qz+qw*qw)
        if abs(qn-1)>1e-2: raise SystemExit(f"line {n}: quaternion norm {qn}")
        rows.append([ns/1e9,*vals])
if len(rows)<2: raise SystemExit("insufficient ground-truth poses")
if any(rows[i][0]>=rows[i+1][0] for i in range(len(rows)-1)): raise SystemExit("timestamps not strictly increasing")
Path(a.output).parent.mkdir(parents=True,exist_ok=True)
with Path(a.output).open("w",newline="",encoding="utf-8") as f:
    w=csv.writer(f); w.writerow(OUT); w.writerows(rows)
print(f"EUROC_GT_NORMALIZED poses={len(rows)}")
