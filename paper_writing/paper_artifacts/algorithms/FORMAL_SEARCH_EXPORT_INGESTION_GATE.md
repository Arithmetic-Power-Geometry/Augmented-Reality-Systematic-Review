# Formal Search Export Importer — Run 35

## Purpose
Convert immutable database exports into deterministic canonical records while preserving search provenance. This tool does **not** execute searches and does not create PRISMA counts by hand.

## Fail-closed gates
An import is rejected unless:
1. an exact (source, search_run_id, query_id) row exists with status EXECUTED;
2. registry SHA-256 exists and matches raw export bytes;
3. format is CSV, RIS, or BibTeX;
4. every parsed record has a title;
5. parsed record count matches exported_count when declared.

## Derived outputs
- pooled_raw_index.csv
- dedup_candidates.csv
- ingestion_manifest.json

## Deduplication
Exact DOI -> exact stable ID -> exact normalized title -> fuzzy title + first author + year.
Fuzzy candidates are always MANUAL_REVIEW. No record is auto-deleted by fuzzy matching.

## Study families
The importer does not merge preprint/conference/journal versions. Family decisions remain explicit human-reviewed ledger operations.

## PRISMA
The importer creates evidence needed for later arithmetic. It does not invent or manually type final identification/screening counts.

## Execution status
Repository code and a synthetic self-test are committed in Run 35. A passing scientific/formal-search execution claim requires an actual runtime or CI record; code inspection alone is not such a claim.
