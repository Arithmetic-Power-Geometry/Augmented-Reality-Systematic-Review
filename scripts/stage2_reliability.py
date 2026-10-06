#!/usr/bin/env python3
"""Stage-2 reliability calculator. Never generates reviewer judgments."""
import csv, json, math, sys
from collections import Counter, defaultdict
from pathlib import Path

def read_csv(p):
    with open(p, newline='', encoding='utf-8-sig') as f:
        return list(csv.DictReader(f))

def kappa(a,b,weights=None):
    cats=sorted(set(a)|set(b))
    if not a or len(a)!=len(b): return None
    n=len(a); idx={c:i for i,c in enumerate(cats)}
    cm=[[0]*len(cats) for _ in cats]
    for x,y in zip(a,b): cm[idx[x]][idx[y]]+=1
    if weights is None:
        po=sum(cm[i][i] for i in range(len(cats)))/n
        ra=[sum(r) for r in cm]; cb=[sum(cm[i][j] for i in range(len(cats))) for j in range(len(cats))]
        pe=sum(ra[i]*cb[i] for i in range(len(cats)))/(n*n)
        return (po-pe)/(1-pe) if pe<1 else 1.0
    k=len(cats); den=max(k-1,1)
    w=[[1-((i-j)/den)**2 for j in range(k)] for i in range(k)]
    po=sum(w[i][j]*cm[i][j] for i in range(k) for j in range(k))/n
    ra=[sum(r) for r in cm]; cb=[sum(cm[i][j] for i in range(k)) for j in range(k)]
    pe=sum(w[i][j]*ra[i]*cb[j] for i in range(k) for j in range(k))/(n*n)
    return (po-pe)/(1-pe) if pe<1 else 1.0

def agreement(a,b):
    return sum(x==y for x,y in zip(a,b))/len(a) if a else None

def compare(a_path,b_path,key,a_field,b_field=None,weighted=False):
    b_field=b_field or a_field
    A={r[key]:r for r in read_csv(a_path) if r.get(key)}
    B={r[key]:r for r in read_csv(b_path) if r.get(key)}
    ids=sorted(set(A)&set(B))
    av=[]; bv=[]; missing=[]
    for i in ids:
        x=A[i].get(a_field,'').strip(); y=B[i].get(b_field,'').strip()
        if not x or not y: missing.append(i); continue
        av.append(x); bv.append(y)
    return {"matched_ids":len(ids),"coded_pairs":len(av),"missing_pairs":len(missing),
            "raw_agreement":agreement(av,bv),"kappa":kappa(av,bv,weights='quadratic' if weighted else None),
            "disagreements":sum(x!=y for x,y in zip(av,bv))}

def main():
    if len(sys.argv)<2:
        print("usage: stage2_reliability.py config.json [output.json]"); return 2
    cfg=json.load(open(sys.argv[1],encoding='utf-8'))
    out={"stage2_reliability_version":"1.0","comparisons":[]}
    for c in cfg.get("comparisons",[]):
        out["comparisons"].append({"name":c["name"],**compare(c["reviewer_a"],c["reviewer_b"],c["key"],c["a_field"],c.get("b_field"),c.get("weighted",False))})
    target=sys.argv[2] if len(sys.argv)>2 else "STAGE2_RELIABILITY_REPORT.json"
    Path(target).write_text(json.dumps(out,indent=2)+"\n",encoding='utf-8')
    print(json.dumps(out,indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
