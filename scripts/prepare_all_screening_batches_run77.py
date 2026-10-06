#!/usr/bin/env python3
"""Run 77: prepare all remaining TA batches and canonical human screening ledger.
Automation supplies nonbinding prompts only; primary decisions remain blank."""
import csv,re,hashlib,json
from pathlib import Path
R=Path("."); src=R/"evidence/screening/formal_pubmed_batches"
outdir=R/"evidence/screening/reviewer_ready"; outdir.mkdir(parents=True,exist_ok=True)
explicit=re.compile(r"augmented reality|mixed reality|mixed-reality|blended reality|extended reality|\bXR\b|AR-based|AR-HUD|augmented (?:visuali[sz]ation|view|display|guidance|monocular)",re.I)
secondary=re.compile(r"\b(systematic review|scoping review|narrative review|literature review|meta-analysis|bibliometric|perspective|commentary|editorial)\b",re.I)
vr=re.compile(r"\bvirtual reality\b",re.I)
allrows=[]; summary=[]
for b in range(1,32):
 p=src/f"TA-{b:02d}.csv"
 if not p.exists(): continue
 rs=list(csv.DictReader(p.open(encoding="utf-8-sig")))
 prepared=[]
 for r in rs:
  title=(r.get("title") or ""); abstract=(r.get("abstract") or ""); txt=title+" "+abstract
  flags=[]
  if not abstract.strip(): flags.append("ABSTRACT_MISSING")
  if secondary.search(title): flags.append("SECONDARY_OR_COMMENTARY_TITLE")
  if explicit.search(txt): prompt="LIKELY_ADVANCE_CONFIRM"; reason=""
  elif secondary.search(title): prompt="LIKELY_EXCLUDE_CONFIRM"; reason="E-SECONDARY"
  elif vr.search(txt): prompt="PRIORITY_VERIFY"; reason=""
  else: prompt="PRIORITY_VERIFY"; reason=""
  x={"screening_ordinal":r.get("screening_ordinal",""),"batch_id":r.get("batch_id",f"TA-{b:02d}"),"pmid":r.get("pmid",""),"doi":r.get("doi",""),"title":title,"abstract":abstract,"year":r.get("year",""),"journal":r.get("journal",""),"risk_flags":";".join(flags),"reviewer_prompt":prompt,"suggested_reason_code":reason,"primary_decision":"","primary_reason_code":"","primary_screener":"","decision_timestamp":"","evidence_note":"","decision_version":"","second_verification_state":"","adjudication_state":""}
  prepared.append(x);allrows.append(x)
 dest=outdir/f"TA-{b:02d}_REVIEWER_READY_RUN77.csv"
 with dest.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=list(prepared[0]));w.writeheader();w.writerows(prepared)
 from collections import Counter
 c=Counter(x["reviewer_prompt"] for x in prepared)
 summary.append({"batch":f"TA-{b:02d}","n":len(prepared),**dict(c),"sha256":hashlib.sha256(dest.read_bytes()).hexdigest()})
# Canonical ledger: exactly the formal 7,728 records, ordered once.
allrows.sort(key=lambda r:int(r["screening_ordinal"]))
assert len(allrows)==7728,(len(allrows),"expected 7728")
assert len({r["pmid"] for r in allrows})==7728
ledger=R/"evidence/screening/final_title_abstract_ledger.csv"
with ledger.open("w",encoding="utf-8",newline="") as f:
 w=csv.DictWriter(f,fieldnames=list(allrows[0]));w.writeheader();w.writerows(allrows)
prov=R/"paper_writing/paper_artifacts/provenance/RUN77_ALL_BATCH_PREPARATION.json";prov.parent.mkdir(parents=True,exist_ok=True)
prov.write_text(json.dumps({"records":7728,"batches":len(summary),"official_primary_decisions":0,"ledger_sha256":hashlib.sha256(ledger.read_bytes()).hexdigest(),"batches_summary":summary},indent=2),encoding="utf-8")
print("RUN77_ALL_BATCH_PREPARATION PASS records=7728 batches=",len(summary),"official_decisions=0","ledger_sha256=",hashlib.sha256(ledger.read_bytes()).hexdigest())
