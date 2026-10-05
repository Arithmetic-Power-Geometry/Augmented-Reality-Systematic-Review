# NEXT-05 Formal Search Execution Pack — Protocol V1

**Purpose:** convert the frozen NEXT-01 protocol into an auditable execution checklist without claiming any database query has run.

## Sources
IEEE Xplore; ACM Digital Library; Scopus; Web of Science Core Collection; ScienceDirect; SpringerLink; PubMed.

## Query IDs
Q00 AR core alone; Q01–Q12 = AR core AND B01–B12 exactly as defined in `protocol/PRIMARY_STUDY_SEARCH_STRATEGY.md`.

## Required capture for every source-query execution
`search_run_id, source, query_id, concept_block, exact_executed_query, execution_date, date_from, date_to, filters, raw_result_count, exported_count, export_file, export_sha256, access_limitation, operator_or_tool, status, notes`.

## Execution rule
1. Adapt only database syntax/field names/wildcards/query-length mechanics.
2. Preserve semantic terms from frozen V1.
3. Save raw export immutably under `evidence/search/raw_exports/<source>/`.
4. Compute SHA-256 immediately after export.
5. Append one registry row; never overwrite a prior run.
6. If a database/export is inaccessible, record the limitation instead of substituting a fabricated count.
7. Do not deduplicate inside raw exports; pooled deduplication is a derived stage.
8. Search end date remains 2026-10-05 inclusive.

## Completion arithmetic
7 declared databases × 13 query IDs = **91 planned source-query executions**, unless a source documents a query-length/export limitation. Limitations count as documented protocol outcomes, not silent omissions.

## Gate
Formal search execution is complete only when every planned source-query pair has either:
- an executed registry row with raw/export counts + export checksum; or
- an explicit access/query limitation row.

No PRISMA identification count may be frozen before this gate.
