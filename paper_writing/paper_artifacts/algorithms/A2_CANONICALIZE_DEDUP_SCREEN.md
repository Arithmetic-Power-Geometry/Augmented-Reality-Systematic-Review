# Algorithm A2 — Canonicalization, Deduplication and Screening

**Input:** immutable discovery records and frozen screening codes.

1. Resolve canonical title, year, venue and DOI/stable identifier from authoritative bibliographic/publisher records.
2. Preserve any correction in the canonical ledger; never rewrite the raw discovery record.
3. Normalize DOI and title.
4. Form duplicate candidates in priority order: DOI exact → stable identifier exact → normalized title exact → fuzzy title + author + year.
5. Manually adjudicate fuzzy/companion candidates before merging.
6. Assign a study-family identifier when multiple reports describe the same underlying experiment.
7. Apply frozen title/abstract criteria without considering whether results support project hypotheses.
8. Record include/exclude/uncertain plus a controlled code and reason.
9. Advance uncertain records to full-text adjudication.
10. Permit only screened primary studies to enter structured evidence extraction.
11. Report seed-batch screening separately from final systematic-search PRISMA counts.

**Invariant:** raw discovery evidence is immutable; all transformations are traceable.
