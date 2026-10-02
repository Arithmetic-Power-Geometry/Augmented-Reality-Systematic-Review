#!/usr/bin/env python3
import sys
from pathlib import Path
r=Path(sys.argv[1])
required=[
 "mav0/cam0/data","mav0/cam1/data","mav0/imu0/data.csv",
 "mav0/cam0/sensor.yaml","mav0/cam1/sensor.yaml","mav0/imu0/sensor.yaml"
]
missing=[x for x in required if not (r/x).exists()]
if missing: raise SystemExit("missing EuRoC inputs: "+", ".join(missing))
left=list((r/"mav0/cam0/data").glob("*.png")); right=list((r/"mav0/cam1/data").glob("*.png"))
if not left or not right: raise SystemExit("camera image folders empty")
if len(left)!=len(right): raise SystemExit(f"stereo image count mismatch: {len(left)} vs {len(right)}")
print(f"EUROC_STRUCTURE_OK stereo_pairs={len(left)}")
