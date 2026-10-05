# Algorithm — Post-200 Reference Admission Gate

Input: candidate reference r
Output: ADMIT or HOLD

1. Verify complete bibliographic metadata against authoritative or independent scholarly records.
2. Reject exact DOI duplicates and title-level duplicates.
3. Assign r to at least one evidence obligation:
   - corpus provenance;
   - closest prior work;
   - evidence-model definition;
   - result interpretation;
   - contradiction;
   - limitation;
   - reproducibility;
   - experimentally actionable gap.
4. If r only increases bibliography size, HOLD.
5. For mixed XR, apply MIXED_XR_SEPARABILITY_GATE.
6. For secondary reviews, apply SECONDARY_REVIEW_EVIDENCE_PROMOTION_GATE.
7. For primary studies discovered outside formal exports, mark supplementary-discovery status until screened under the frozen protocol.
8. Append to master.bib and validation ledger only after Steps 1–7 pass.
