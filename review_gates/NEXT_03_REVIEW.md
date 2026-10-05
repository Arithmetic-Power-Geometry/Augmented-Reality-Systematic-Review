# NEXT-03 Adversarial IEEE/TVCG Review

## Reject-first findings

### HIGH — Screening 16/16 could look implausibly selective
A reviewer could infer cherry-picking because every seed candidate advances.

**Fix:** explicitly label Batch 1 as a curated discovery seed, not database search output; prohibit use of its 100% advancement rate as an eligibility/prevalence statistic.
**Resolution:** screening table/report updated. **RESOLVED.**

### HIGH — Metadata correction could silently alter source evidence
PD0011's discovery venue was provisional and incorrect.

**Fix:** keep raw discovery CSV immutable and record canonical correction only in the derived screening ledger.
**Resolution:** implemented. **RESOLVED.**

### HIGH — No-duplicate result could be overstated
Zero duplicates among 16 seed records says nothing about duplication in the future systematic database exports.

**Fix:** state that duplicate count applies only within Batch 1; retain full DOI→ID→title→fuzzy deduplication procedure for NEXT-05 corpus processing.
**Resolution:** implemented. **RESOLVED.**

### HIGH — Title/abstract screening is not a substitute for systematic search
These records were discovered by parallel seed searches rather than the frozen database-query execution.

**Fix:** do not call them the final included corpus or use them for PRISMA database counts. NEXT-04 may code them as pilot evidence; systematic corpus freeze remains NEXT-05.
**Resolution:** implemented. **RESOLVED.**

### MEDIUM — Some full texts require deeper extraction
Bibliographic/abstract evidence establishes primary-study eligibility, but exact D,T,H,S,A,M,E,U,R coding and reproducibility fields require full-text extraction.
**Required next action:** NEXT-04 structured evidence extraction with field-level provenance.

## Verdict
**PASS for canonicalization/deduplication/seed screening.** CRITICAL unresolved=0; HIGH unresolved=0.
