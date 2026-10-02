#!/usr/bin/env python3
"""Normalize a TUM-style trajectory into the project trajectory contract.

Input rows (whitespace separated):
timestamp tx ty tz qx qy qz qw

This adapter does not align, interpolate, filter, or alter estimates.
"""
import argparse, csv
from pathlib import Path

HEADER=["timestamp","tx","ty","tz","qx","qy","qz","qw"]

def parse(src):
    rows=[]
    for n,line in enumerate(Path(src).read_text(encoding="utf-8").splitlines(),1):
        s=line.strip()
        if not s or s.startswith("#"): continue
        parts=s.split()
        if len(parts)!=8:
            raise ValueError(f"line {n}: expected 8 fields, got {len(parts)}")
        vals=[float(x) for x in parts]
        rows.append(vals)
    if not rows: raise ValueError("no trajectory rows")
    for a,b in zip(rows,rows[1:]):
        if b[0] <= a[0]:
            raise ValueError("timestamps must be strictly increasing")
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("output")
    args=ap.parse_args()
    rows=parse(args.input)
    with open(args.output,"w",newline="",encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(HEADER); w.writerows(rows)
    print(f"WROTE {len(rows)} poses to {args.output}")

if __name__=="__main__": main()
