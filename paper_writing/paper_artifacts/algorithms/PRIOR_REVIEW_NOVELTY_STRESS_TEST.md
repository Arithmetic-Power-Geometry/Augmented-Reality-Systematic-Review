# Algorithm — Prior-Review Novelty Stress Test

Input: candidate contribution claim c
Output: RETAIN, NARROW, or REJECT

1. Identify the closest review cluster for c.
2. Retrieve validated prior reviews from master.bib.
3. If c is only "broad", "systematic", "longitudinal", "taxonomy", or "covers domain X", REJECT.
4. If a prior review already provides the same taxonomy/outcome synthesis, REJECT or NARROW.
5. Ask whether c operationalizes a relation absent from the closest review: comparability, transfer, provenance, reproducibility grade, contradiction, evidence maturity, or gap-to-experiment promotion.
6. Require explicit representation fields and a reproducible decision rule.
7. Require the claim to survive final review-of-reviews and primary-corpus checks.
8. If closest-prior-work evidence is incomplete, label PROVISIONAL and NARROW.
9. RETAIN only if the contribution is both distinct and auditable.
