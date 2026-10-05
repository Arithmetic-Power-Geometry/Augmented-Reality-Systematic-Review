# Algorithm — Formal Screening Decision Gate (Run 53)

**Purpose:** convert each unresolved formal record into a reproducible screening disposition without inventing evidence.

## Input
A record from the frozen formal corpus, frozen eligibility criteria I1–I5, and controlled screening codes.

## Procedure

1. Verify bibliographic identity and available title/abstract metadata.
2. If metadata are insufficient for a defensible title/abstract decision, assign `U-UNCERTAIN` and advance.
3. Otherwise test the frozen scope and primary-study criteria.
4. If a controlled exclusion criterion is directly supported, assign exactly one primary exclusion code and retain the evidence note.
5. If the record plausibly satisfies I1–I5, assign `include` for progression to full text; this is not final study inclusion.
6. Never infer exclusion from absence of a keyword when semantic eligibility remains possible.
7. At full text, repeat against I1–I5 using the complete report and record a controlled exclusion reason where applicable.
8. Link duplicates/companions through canonical report and `study_family_id`.
9. Route all final includes and the frozen stratified exclusion sample to a genuine independent verifier.
10. Resolve disagreements against the frozen protocol; preserve both original decisions and adjudication.
11. Unlock corpus freeze only when no unresolved record remains and citation-chasing/stopping conditions are satisfied.

## Output
Versioned screening ledger + full-text exclusion ledger + verification/adjudication fields.

## Integrity invariant
No automated or AI-assisted prioritization step may be represented as an independent human screening decision.
