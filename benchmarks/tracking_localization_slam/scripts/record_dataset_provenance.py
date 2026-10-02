#!/usr/bin/env python3
"""Create provenance metadata for a locally acquired dataset archive/file.

This script does not download datasets. It records a SHA-256 checksum and
size for a file the researcher obtained from the official source.
"""
import argparse,hashlib,json
from pathlib import Path
def sha256(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()
ap=argparse.ArgumentParser()
ap.add_argument("file"); ap.add_argument("--dataset",required=True)
ap.add_argument("--sequence",required=True); ap.add_argument("--source",required=True)
ap.add_argument("--output",required=True)
a=ap.parse_args(); p=Path(a.file)
if not p.is_file(): raise SystemExit("dataset file not found")
d={"dataset":a.dataset,"sequence":a.sequence,"official_source":a.source,
   "filename":p.name,"size_bytes":p.stat().st_size,"sha256":sha256(p)}
Path(a.output).write_text(json.dumps(d,indent=2)+"\n",encoding="utf-8")
print(json.dumps(d,indent=2))
