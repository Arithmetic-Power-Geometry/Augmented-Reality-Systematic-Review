# Formal Screening Workplan — Run 53

**Date:** 2026-10-05  
**Paper:** P1 — AR systematic review  
**Frozen input:** PubMed Q00 deterministic prescreen  
**Input total:** 10,198 unique PMIDs

## Audited state

| State | Records | Final? |
|---|---:|---|
| Deterministic exclusion — E-LANGUAGE | 227 | yes, subject to audit |
| Deterministic exclusion — E-SECONDARY | 2,232 | yes, subject to audit |
| Title/abstract review required | 7,728 | no |
| Metadata unavailable | 11 | no |
| Total unresolved/advance | 7,739 | no |

Check: 227 + 2,232 + 7,728 + 11 = 10,198.

## Execution batches

The 7,728 title/abstract records are partitioned deterministically into 31 batches: 30 batches of 250 records and one final batch of 228 records. Batch membership must be based on the immutable Q00 derived record order/identifier list and must never be reshuffled after decisions begin.

Each screening row must preserve:
- record identifier (PMID and DOI when available);
- title;
- year;
- source;
- batch ID;
- screening stage;
- decision: include / exclude / uncertain;
- controlled reason code from `protocol/SCREENING_CODES.csv`;
- screener;
- decision timestamp;
- evidence note;
- decision version;
- second-verification state;
- adjudication state.

## Fail-closed rules

1. No uncertain record is excluded by keyword heuristic.
2. Title/abstract uncertainty advances to full text.
3. Decisions are append/versioned; prior decisions are not silently overwritten.
4. Final includes require genuine independent second verification.
5. A stratified exclusion sample requires genuine independent second verification.
6. No agreement statistic is reported unless it comes from genuinely independent decisions.
7. PRISMA final counts remain locked until all registered source cells are executed or limitation-documented, screening/full text are complete, study families are resolved, citation chasing reaches the frozen stopping rule, and the corpus is checksum-frozen.

## Immediate completion sequence

B01–B31 title/abstract screening → resolve 11 metadata records → full-text retrieval → full-text decisions/reasons → study-family resolution → backward/forward citation chasing → second verification/adjudication → corpus checksum freeze → final PRISMA → rerun NEXT-06..NEXT-19.

This workplan is a workflow artifact, not a claim that human screening has been completed.
