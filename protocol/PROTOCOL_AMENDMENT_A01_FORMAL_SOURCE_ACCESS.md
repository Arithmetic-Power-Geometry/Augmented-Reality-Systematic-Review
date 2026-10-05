# Protocol Amendment Decision A01 — Formal-Source Access Constraint

**Date:** 2026-10-05
**Stage:** before formal database execution and before final corpus freeze
**Original protocol:** Frozen Protocol V1
**Decision:** retain the seven-source systematic-review protocol; do not silently narrow or substitute sources.

## Trigger

Run 39 established that no source-native export satisfying the frozen provenance contract could be obtained from the available execution environment. A direct attempt to access the PubMed search interface from the available web interface also did not yield an accessible source-native result/export. Therefore replacing seven formal sources with “PubMed only” would not remove the provenance blocker.

## Amendment considered

A reduced-source formal search was considered as a way to finish the review under access constraints.

## Decision and rationale

The reduced-source amendment is **not activated** at this stage. The systematic-review claim remains tied to the original seven-source protocol:
IEEE Xplore, ACM Digital Library, Scopus, Web of Science Core Collection, ScienceDirect, SpringerLink, and PubMed.

Reasons:
1. no alternative source can currently be executed here with the exact query/count/export provenance required by the frozen contract;
2. silently replacing subscription/index databases with general web search would change the sampling frame;
3. general web discovery is useful for bibliography validation and supplementary discovery but is not equivalent to executing the registered bibliographic databases;
4. preserving the original plan makes the access constraint auditable rather than hiding it.

## Two legitimate completion paths

### Path S — Systematic-review completion
Obtain source-native executions/exports for the registered formal sources (or explicitly documented source limitations), then complete ingestion, deduplication, screening, study-family resolution, citation chasing, corpus freeze, PRISMA, extraction, and synthesis.

### Path E — Evidence-centered structured-review conversion
If formal database access cannot be obtained, explicitly change the article type and title so it no longer claims a PRISMA systematic review. The validated evidence library and thematic artifacts may then support a structured evidence-centered review, but:
- no PRISMA flow is reported;
- no claims of exhaustive/systematic retrieval are made;
- corpus prevalence is not inferred from the curated library;
- selection limitations are explicit;
- the original systematic protocol remains archived as an unexecuted plan.

Path E requires an explicit author decision before activation; it is not silently applied.

## Current status

Path S remains active.
Formal corpus status: BLOCKED_BY_FORMAL_SOURCE_EXPORTS.
Validated bibliography: 167.
Manuscript V0.2 remains parked; no final Results are unlocked.
