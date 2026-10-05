#!/usr/bin/env python3
"""Generate final manuscript numerics only after the fail-closed corpus gate passes."""
import csv,json,hashlib
from pathlib import Path
R=Path(".")
gate=R/"paper_writing/paper_artifacts/provenance/RUN57_FINAL_CORPUS_GATE.json"
if not gate.exists(): raise SystemExit("BLOCK: final corpus gate evidence missing")
g=json.loads(gate.read_text(encoding="utf-8"))
if not g.get("all_pass"): raise SystemExit("BLOCK: final corpus gate has not passed")

screen=R/"evidence/screening/final_title_abstract_ledger.csv"
full=R/"evidence/screening/final_full_text_ledger.csv"
families=R/"evidence/primary/final_study_family_ledger.csv"
verify=R/"evidence/screening/final_independent_verification.csv"
for p in [screen,full,families,verify]:
    if not p.exists(): raise SystemExit(f"BLOCK: missing {p}")

sr=list(csv.DictReader(screen.open(encoding="utf-8-sig")))
fr=list(csv.DictReader(full.open(encoding="utf-8-sig")))
fam=list(csv.DictReader(families.open(encoding="utf-8-sig")))
def val(r,*ks):
    for k in ks:
        if k in r and r[k] is not None:return r[k].strip().lower()
    return ""
ta_inc=sum(val(r,"decision","ta_decision","primary_decision")=="include" for r in sr)
ta_exc=sum(val(r,"decision","ta_decision","primary_decision")=="exclude" for r in sr)
ta_unc=sum(val(r,"decision","ta_decision","primary_decision")=="uncertain" for r in sr)
ft_inc=sum(val(r,"decision","full_text_decision")=="include" for r in fr)
ft_exc=sum(val(r,"decision","full_text_decision")=="exclude" for r in fr)
included_studies=len({(r.get("study_family_id") or r.get("canonical_record_id") or "").strip() for r in fam if (r.get("study_family_id") or r.get("canonical_record_id") or "").strip()})
prisma={"records_screened":len(sr),"ta_included":ta_inc,"ta_excluded":ta_exc,"ta_uncertain":ta_unc,"full_text_assessed":len(fr),"full_text_included_reports":ft_inc,"full_text_excluded":ft_exc,"included_studies":included_studies}
out=R/"paper_writing/paper_artifacts/final_generated";out.mkdir(parents=True,exist_ok=True)
(out/"FINAL_PRISMA_COUNTS.json").write_text(json.dumps(prisma,indent=2),encoding="utf-8")
abstract=f"""# Final Numerical Abstract — Generated from Frozen Corpus\n\nA systematic review of augmented-reality research screened {len(sr):,} formally eligible title/abstract records after deterministic preprocessing. {len(fr):,} reports proceeded to full-text assessment, yielding {ft_inc:,} included reports representing {included_studies:,} canonical studies after study-family resolution. Final corpus-wide percentages, evidence-structure distributions, reproducibility results, contradiction states and verified-gap prevalence are inserted only from the frozen NEXT-06--NEXT-19 rerun outputs.\n"""
(out/"FINAL_NUMERICAL_ABSTRACT.md").write_text(abstract,encoding="utf-8")
results=f"""# Final Results — Frozen-Corpus Core\n\n## Study selection\nThe final title/abstract ledger contained {len(sr):,} records: {ta_inc:,} included for progression, {ta_exc:,} excluded, and {ta_unc:,} uncertain at that stage. Full-text assessment covered {len(fr):,} reports; {ft_inc:,} were retained and {ft_exc:,} excluded. Study-family resolution yielded {included_studies:,} canonical included studies.\n\n## Corpus-wide analyses\nPopulate exclusively from regenerated NEXT-06--NEXT-19 outputs linked to the same freeze checksum. No pilot denominator may be substituted.\n"""
(out/"FINAL_RESULTS_CORE.md").write_text(results,encoding="utf-8")
conc=f"""# Final Conclusions — Frozen-Corpus Gate\n\nThe review conclusions must be synthesized from the frozen NEXT-06--NEXT-19 outputs for {included_studies:,} canonical included studies. Claims about prevalence, reproducibility, contradictions, failure regimes and research gaps are permitted only when their denominators and evidence references resolve to the frozen corpus.\n"""
(out/"FINAL_CONCLUSIONS_CORE.md").write_text(conc,encoding="utf-8")
print("FINAL_MANUSCRIPT_GENERATION PASS",prisma)

# Run 59 fail-closed execution trigger.
