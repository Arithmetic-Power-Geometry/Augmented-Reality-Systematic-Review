# Algorithm A1 — Candidate Discovery-to-Screening Handoff

**Purpose:** preserve discovery evidence without allowing unscreened records to become manuscript findings.

1. Receive immutable raw discovery record.
2. Assign a discovery ID and source provenance.
3. Determine whether the record appears to contain primary empirical/technical evidence.
4. If clearly secondary, route to the review-of-reviews layer; do not enter the primary candidate registry.
5. Otherwise retain as a primary-study candidate without an inclusion claim.
6. At NEXT-03, canonicalize DOI/title/venue/year.
7. Deduplicate by DOI → stable ID → normalized title → fuzzy title+author+year.
8. Apply frozen title/abstract screening codes.
9. Advance uncertain records to full-text screening.
10. Only screened included records may enter the Evidence Cube and contribute to manuscript counts.

This algorithm is a review-workflow control procedure, not a scientific AR algorithm.
