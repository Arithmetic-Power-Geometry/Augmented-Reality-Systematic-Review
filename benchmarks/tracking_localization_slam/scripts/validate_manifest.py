#!/usr/bin/env python3
import json, sys
from pathlib import Path

REQUIRED = ["run_id","method","method_commit","dataset","sequence","sensor_mode","environment","hardware","evaluator_commit","status"]
VALID_STATUS = {"planned","running","success","failed","invalid"}

def main(path):
    p=Path(path)
    data=json.loads(p.read_text(encoding="utf-8"))
    missing=[k for k in REQUIRED if k not in data]
    if missing:
        raise SystemExit("missing required fields: "+", ".join(missing))
    if data["status"] not in VALID_STATUS:
        raise SystemExit("invalid status")
    if len(str(data["method_commit"])) < 7:
        raise SystemExit("method_commit must be pinned, not a branch name")
    print(f"VALID {data['run_id']}")

if __name__=="__main__":
    if len(sys.argv)!=2:
        raise SystemExit("usage: validate_manifest.py RUN_MANIFEST.json")
    main(sys.argv[1])
