# NEXT-03 Canonicalization and Deduplication Report

## Input
16 immutable discovery candidates from Batch 1.

## Canonicalization
- 15 records retained their discovery bibliographic identity.
- 1 material metadata correction: PD0011 venue changed from the provisional discovery label to **Sensors 21(19), 6623**, DOI **10.3390/s21196623**.
- PD0001 has no DOI recorded in the authoritative USENIX proceedings entry used here; canonical stable identity is USENIX proceedings record 294552 rather than an invented DOI.

## Deduplication
The 16 records have 16 distinct canonical DOI/stable identifiers and distinct normalized titles. No Batch-1 pair is a bibliographic duplicate. No candidate is currently merged as a companion report.

## Screening
All 16 pass title/abstract eligibility as primary AR studies and advance to structured evidence extraction. This is **not** the final systematic corpus and not a prevalence estimate. The full systematic database search remains to be executed under the frozen search protocol.

## Integrity rule
Raw discovery rows were not overwritten. Canonical corrections live in the screening ledger so the transformation is auditable.
