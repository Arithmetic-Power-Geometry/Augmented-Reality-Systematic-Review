# Algorithm — Checksum-Frozen Formal Screening Batch Construction

**Input:** checksum-frozen PubMed Q00 deterministic prescreen.

1. Read the committed prescreen CSV.
2. Assert exactly 10,198 input rows.
3. Select only rows with `UNCERTAIN_REQUIRES_SCREENING / TITLE_ABSTRACT_REVIEW_REQUIRED`.
4. Assert exactly 7,728 selected rows.
5. Assert PMID uniqueness across the selected set.
6. Preserve source order and assign screening ordinals 1..7,728.
7. Partition sequentially into TA-01..TA-31 with batch size 250 except TA-31=228.
8. Append blank versioned decision fields for TA decision, reason, screener, timestamp, evidence note, second verification and adjudication.
9. Compute SHA-256 for every batch and write a checksum manifest.
10. Fail closed on any cardinality, uniqueness or generation mismatch.

**Output:** immutable screening work units suitable for genuine title/abstract review.

**Non-claim:** batch construction is data engineering, not study selection.
