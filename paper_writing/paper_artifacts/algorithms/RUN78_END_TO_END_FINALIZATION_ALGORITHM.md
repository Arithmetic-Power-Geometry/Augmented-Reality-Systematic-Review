# Run 78 — End-to-End Finalization Algorithm

**Input:** genuine reviewer-completed 7,728-row title/abstract ledger.

1. Validate every decision, reviewer attribution and exclusion reason.
2. Populate full-text retrieval and eligibility ledger from advanced records.
3. Require explicit full-text exclusion reasons.
4. Resolve reports into canonical study families.
5. Execute backward/forward citation chasing and record every candidate disposition.
6. Complete independent verification and adjudication.
7. Run the strict corpus-freeze gate and write immutable checksums.
8. Rerun NEXT-06 through NEXT-19 against the frozen corpus only.
9. Generate PRISMA counts from ledgers.
10. Generate final included-study count from canonical family IDs.
11. Generate percentages and gap prevalence using explicit frozen denominators.
12. Generate final Results tables/figures.
13. Generate the numerical Abstract and Conclusions last.
14. Abort if any required evidence or provenance field is missing.
