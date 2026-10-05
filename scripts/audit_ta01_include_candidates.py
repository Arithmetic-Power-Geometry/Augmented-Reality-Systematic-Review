#!/usr/bin/env python3
"""Run 62: audit TA-01 include candidates for obvious false-positive/secondary-risk signals."""
import csv,re,json
from pathlib import Path
src=Path("evidence/screening/assisted/TA-01_ASSISTED_TRIAGE_RUN60.csv")
rows=list(csv.DictReader(src.open(encoding="utf-8-sig")))
inc=[r for r in rows if r.get("assisted_recommendation")=="INCLUDE_CANDIDATE"]
if len(inc)!=211: raise SystemExit(f"BLOCK expected 211 include candidates, got {len(inc)}")
secondary=re.compile(r"\b(review|commentary|editorial|perspective|overview|future of|state of the art)\b",re.I)
weak_future=re.compile(r"\b(future|potential|could|may)\b",re.I)
explicit=re.compile(r"augmented[- ]reality|mixed[- ]reality|blended reality",re.I)
out=[]
for r in inc:
    title=r.get("title",""); abstract=r.get("abstract",""); text=title+" "+abstract
    flags=[]
    if secondary.search(title): flags.append("SECONDARY_OR_COMMENTARY_TITLE")
    if not explicit.search(title) and explicit.search(abstract) and weak_future.search(abstract): flags.append("AR_MENTION_MAY_BE_CONTEXT_ONLY")
    if not abstract.strip(): flags.append("ABSTRACT_MISSING")
    if re.search(r"virtual reality",text,re.I) and not explicit.search(text): flags.append("VR_WITHOUT_EXPLICIT_AR_MR")
    state="PRIORITY_VERIFY" if flags else "LIKELY_ADVANCE_PENDING_PRIMARY_REVIEW"
    out.append({**r,"run62_audit_state":state,"run62_flags":";".join(flags)})
dest=Path("evidence/screening/assisted/TA-01_INCLUDE_CANDIDATE_AUDIT_RUN62.csv");dest.parent.mkdir(parents=True,exist_ok=True)
fields=list(out[0]); 
with dest.open("w",encoding="utf-8",newline="") as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(out)
from collections import Counter
c=Counter(r["run62_audit_state"] for r in out)
flag=Counter(x for r in out for x in r["run62_flags"].split(";") if x)
summary={"n":len(out),"states":dict(c),"flags":dict(flag)}
Path("paper_writing/paper_artifacts/provenance/RUN62_TA01_INCLUDE_AUDIT.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
print("RUN62_INCLUDE_AUDIT",json.dumps(summary,sort_keys=True))
