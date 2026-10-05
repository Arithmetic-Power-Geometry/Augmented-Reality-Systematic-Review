# Algorithm — Formal Corpus Completion Gate

1. For every planned source/query cell, require either:
   a. EXECUTED with exact query, date, counts, export file and SHA-256; or
   b. LIMITATION with a documented source-access/export reason.
2. Never convert general web search into a formal-source execution.
3. Ingest every EXECUTED raw export using the deterministic importer.
4. Fail on checksum/count mismatch.
5. Pool canonical records.
6. Generate exact and fuzzy duplicate candidates.
7. Human-adjudicate fuzzy duplicates and report families.
8. Freeze deduplicated pool.
9. Perform title/abstract screening with controlled reasons.
10. Advance uncertain records to full text.
11. Perform full-text screening and second verification.
12. Resolve study families and provenance.
13. Complete backward/forward citation chasing until the frozen stopping rule is met.
14. Freeze corpus and checksums.
15. Derive PRISMA counts programmatically.
16. Execute P_i extraction, C0-C3 comparability, reproducibility, contradiction, failure-regime, transfer and gap analyses.
17. Only then unlock final Results/Discussion.

If Step 1 is incomplete, downstream final outputs are BLOCKED; do not estimate them.
