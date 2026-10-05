# NEXT-04 Adversarial IEEE/TVCG Reviewer Gate

## Reject-first findings

### HIGH — False precision from incomplete full-text extraction
Several seed studies have enough metadata to establish study design but not enough to safely claim every reproducibility/statistical field.
**Fix:** use `unknown` and `pilot_partial`; never infer absent artifacts or statistics.
**Resolution:** implemented. RESOLVED.

### HIGH — Evidence Cube could imply inappropriate comparability
Security attacks, cognitive load, localization and usability cannot be pooled.
**Fix:** preserve task/domain-specific metric families and state that common schema does not mean common leaderboard.
**Resolution:** implemented. RESOLVED.

### HIGH — Bibliography contamination
A DOI alone is insufficient for a publication-ready BibTeX entry if authors/venue/pages have not been independently validated.
**Fix:** master.bib contains only fully validated entries; all others remain in BIB_VALIDATION_STATUS.csv and are prohibited from manuscript citation until validated.
**Resolution:** implemented. RESOLVED.

### HIGH — Reported findings could be mistaken for computed review results
**Fix:** source-level findings are explicitly labelled `reported_finding`; computed synthesis begins only after the systematic corpus is frozen.
**Resolution:** implemented. RESOLVED.

### MEDIUM — Full 16-record extraction still needs deeper field-level provenance
The pilot extraction is sufficient to validate the schema and begin drafting framework/method prose, but not sufficient for final Results.
**Next action:** expand/cross-check full-text extraction while NEXT-05 executes the systematic search and corpus freeze.

## Verdict
**PASS as pilot structured extraction.** CRITICAL unresolved=0; HIGH unresolved=0.
