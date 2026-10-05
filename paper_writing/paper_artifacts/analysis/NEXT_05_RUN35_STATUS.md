# NEXT-05 Run 35 — Formal Search Ingestion Infrastructure

Pre-run repository, formal execution matrix, registry, translation spec, raw-export contract, screening/dedup/family templates, bibliography and artifact manifest inspected.

Current validated bibliography: **156**. No bibliography padding was performed in this run because the critical path is formal corpus provenance.

Created:
- scripts/ingest_search_exports.py
- scripts/test_ingest_search_exports.py
- paper-facing ingestion algorithm/spec
- readiness matrix
- provenance-flow figure

The importer requires an EXECUTED registry row and matching SHA-256, supports CSV/RIS/BibTeX, normalizes DOI/title/first-author/year, emits exact/fuzzy dedup candidates, never auto-deletes fuzzy matches, never auto-merges study families, and verifies exported_count when declared.

Execution boundary: code is committed and inspectable; the synthetic self-test is committed but is NOT claimed as passed because no repository runtime/CI execution result was available in this work session.

Formal execution matrix remains 91 planned source-query cells, all NOT_EXECUTED. Therefore NEXT-05 remains open.

Paper writing starts immediately after formal corpus freeze; reaching 200 references is not the gate.
