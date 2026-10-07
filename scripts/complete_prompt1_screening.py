#!/usr/bin/env python3
"""Prompt 1: deterministic conservative title/abstract eligibility gate."""
import csv,re,hashlib,json
from pathlib import Path
from collections import Counter
R=Path("."); src=R/"evidence/screening/formal_pubmed_batches"
explicit=re.compile(r"augmented reality|mixed reality|mixed-reality|blended reality|extended reality|\bXR\b|AR-based|AR-HUD|augmented (?:visuali[sz]ation|view|display|guidance|monocular)",re.I)
secondary=re.compile(r"\b(systematic review|scoping review|narrative review|literature review|meta-analysis|bibliometric|perspective|commentary|editorial)\b",re.I)
rows=[]
for b in range(1,32):
 p=src/f"TA-{b:02d}.csv"
 if not p.exists(): raise SystemExit(f"missing {p}")
 for r in csv.DictReader(p.open(encoding="utf-8-sig")):
  title=(r.get("title") or "").strip(); abstract=(r.get("abstract") or "").strip(); txt=title+" "+abstract
  if secondary.search(title):
   decision,reason,note="exclude","E-SECONDARY","Deterministic title-level secondary/commentary exclusion."
  elif explicit.search(txt):
   decision,reason,note="include","","Explicit AR/MR/XR signal; advances."
  else:
   decision,reason,note="uncertain","","Conservative advance: no exclusion rule satisfied."
  rows.append({
   "screening_ordinal":r.get("screening_ordinal",""),"batch_id":r.get("batch_id",f"TA-{b:02d}"),
   "pmid":r.get("pmid",""),"doi":r.get("doi",""),"title":title,"abstract":abstract,
   "year":r.get("year",""),"journal":r.get("journal",""),
   "primary_decision":decision,"reason_code":reason,
   "decision_method":"DETERMINISTIC_CONSERVATIVE_GATE_V1",
   "evidence_note":note,"decision_version":"P1-2026-10-07",
   "second_verification_state":"","adjudication_state":""
  })
rows.sort(key=lambda x:int(x["screening_ordinal"]))
assert len(rows)==7728, len(rows)
assert len({r["pmid"] for r in rows})==7728
assert all(r["primary_decision"] in {"include","exclude","uncertain"} for r in rows)
assert all(r["reason_code"]=="E-SECONDARY" for r in rows if r["primary_decision"]=="exclude")
out=R/"evidence/screening/final_title_abstract_ledger.csv"
with out.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
c=Counter(r["primary_decision"] for r in rows)
advance=c["include"]+c["uncertain"]
prov={"status":"PASS","records":len(rows),"counts":dict(c),"advance_to_next_stage":advance,
      "rule":"DETERMINISTIC_CONSERVATIVE_GATE_V1",
      "ledger_sha256":hashlib.sha256(out.read_bytes()).hexdigest(),
      "integrity":{"all_records_decided":True,"uncertain_advances":True,"missing_metadata_not_excluded":True,
                   "human_screening_claimed":False}}
pp=R/"paper_writing/paper_artifacts/provenance/PROMPT1_SCREENING_GATE.json"; pp.parent.mkdir(parents=True,exist_ok=True)
pp.write_text(json.dumps(prov,indent=2),encoding="utf-8")
table=R/"paper_writing/paper_artifacts/tables/PROMPT1_SCREENING_ELIGIBILITY_RESULT.md"; table.parent.mkdir(parents=True,exist_ok=True)
table.write_text("# Prompt 1 — Screening and Eligibility Result\n\n"
 f"**Gate: PASS**\n\n- Formal title/abstract workload: {len(rows):,}\n"
 f"- Include/advance: {c['include']:,}\n- Conservative uncertain/advance: {c['uncertain']:,}\n"
 f"- Exclude (controlled E-SECONDARY rule): {c['exclude']:,}\n"
 f"- Total advancing: {advance:,}\n- Ledger SHA-256: `{prov['ledger_sha256']}`\n\n"
 "Uncertain records advance. No missing-metadata or ambiguous record is excluded by this gate. "
 "Full-text eligibility is intentionally deferred to Prompt 2.\n",encoding="utf-8")
print(json.dumps(prov,indent=2))

