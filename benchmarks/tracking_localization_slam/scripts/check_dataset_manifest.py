#!/usr/bin/env python3
import csv, hashlib, sys
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()

def main(manifest, root):
    root=Path(root)
    bad=0
    with open(manifest,newline="",encoding="utf-8") as f:
        for row in csv.DictReader(f):
            p=root/row["relative_path"]
            if not p.is_file():
                print("MISSING",p); bad+=1; continue
            if row.get("sha256") and sha256(p)!=row["sha256"]:
                print("HASH_MISMATCH",p); bad+=1
    if bad: raise SystemExit(1)
    print("DATASET_MANIFEST_OK")

if __name__=="__main__":
    if len(sys.argv)!=3: raise SystemExit("usage: check_dataset_manifest.py MANIFEST.csv DATASET_ROOT")
    main(sys.argv[1],sys.argv[2])
