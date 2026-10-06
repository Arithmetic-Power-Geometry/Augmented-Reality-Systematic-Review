#!/usr/bin/env python3
"""Run 73: audit TA-05 include candidates for false-positive risk without writing eligibility decisions."""
import csv, json, hashlib, re
from pathlib import Path
src=Path("evidence/screening/assisted/TA-05_ASSISTED_TRIAGE_RUN60.csv")
rows=[r for r in csv.DictReader(src.open(encoding="utf-8-sig")) if r["assisted_recommendation"]=="INCLUDE_CANDIDATE"]
assert len(rows)==238, len(rows)
secondary=re.compile(r"\b(review|commentary|editorial|perspective|overview|state[- ]of[- ]the[- ]art)\b",re.I)
future=re.compile(r"\b(future|potential|could|may|promising|prospect)\b",re.I)
explicit=re.compile(r"augmented[- ]reality|mixed[- ]reality|blended reality|extended reality|\bXR\b",re.I)
out=[]
for r in rows:
    flags=[]
    title=r["title"] or ""; abstract=r["abstract"] or ""
    if secondary.search(title): flags.append("SECONDARY_OR_COMMENTARY_TITLE")
    if not abstract.strip(): flags.append("ABSTRACT_MISSING")
    if explicit.search(abstract) and not explicit.search(title) and future.search(abstract):
        flags.append("AR_MENTION_MAY_BE_CONTEXT_ONLY")
    state="PRIORITY_VERIFY" if flags else "LIKELY_ADVANCE_PENDING_PRIMARY_REVIEW"
    out.append({**r,"run73_flags":";".join(flags),"run73_audit_state":state})
dest=Path("evidence/screening/assisted/TA-05_INCLUDE_CANDIDATE_AUDIT_RUN73.csv")
fields=list(out[0])
with dest.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
from collections import Counter
states=Counter(r["run73_audit_state"] for r in out); flags=Counter()
for r in out:
    for x in r["run73_flags"].split(";"):
        if x: flags[x]+=1
sha=hashlib.sha256(dest.read_bytes()).hexdigest()
prov={"n":len(out),"states":dict(states),"flags":dict(flags),"sha256":sha,"official_primary_decisions_written":0}
pp=Path("paper_writing/paper_artifacts/provenance/RUN73_TA05_INCLUDE_AUDIT.json");pp.parent.mkdir(parents=True,exist_ok=True);pp.write_text(json.dumps(prov,indent=2),encoding="utf-8")
print("RUN73_TA05_INCLUDE_AUDIT",json.dumps(prov,sort_keys=True))
