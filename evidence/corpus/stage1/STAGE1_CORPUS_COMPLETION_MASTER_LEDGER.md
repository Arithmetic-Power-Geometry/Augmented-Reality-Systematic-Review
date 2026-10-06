# Stage 1 — Corpus Completion Master Ledger

**Frozen protocol:** V1, 2026-10-05  
**Purpose:** complete the review corpus before final evidence analysis or manuscript claims.

## Stage 1 completion definition

Stage 1 is COMPLETE only when all of the following are true:

1. Every registered source-query cell is either genuinely executed with immutable export provenance or explicitly retained as an access limitation; limitation-documented cells are never relabeled as executed.
2. All source exports are merged into one provenance-preserving master record set.
3. Cross-source deduplication is completed using DOI/stable-ID/title/fuzzy verification rules.
4. Every title/abstract record has a genuine eligibility decision.
5. Every advanced record has a full-text decision and controlled exclusion reason where excluded.
6. Companion reports are linked into study families and a canonical report is designated without losing report-level provenance.
7. Backward/forward citation chasing is processed to the frozen stopping rule.
8. A Stage-1 gate reports zero unresolved corpus-selection blockers.

## Current evidence boundary

| Component | Current state | Claim allowed |
|---|---|---|
| Registered source-query cells | 91 | registration only |
| PubMed cells | 13/13 EXECUTED | genuine executed-search provenance |
| Non-PubMed cells | 78 LIMITATION | access limitation only; NOT searched |
| PubMed Q00 raw records | 10,198 | retrieval count |
| Deterministic prescreen removals | 2,459 | preprocessing count |
| Genuine TA decisions required | 7,728 | screening workload |
| Metadata-unavailable identities | 11 | unresolved identity set |
| Final full-text corpus | not frozen | no included-study total |
| PRISMA | blocked | no final PRISMA counts |

## Continuous Stage-1 pipeline

### S1.1 Search execution and provenance
- Preserve PubMed Q00–Q12 immutable exports and checksums.
- For IEEE Xplore, ACM DL, Scopus, Web of Science, ScienceDirect, and SpringerLink, import only source-native exports produced by genuine execution.
- Record exact source-specific query, date, filters, returned count, exported count, filename and SHA-256.
- Never substitute web-search counts for database-native counts.

### S1.2 Merge and normalize
Required output: `evidence/corpus/stage1/master_records.csv`.
Preserve source, query IDs, source-native identifiers, DOI, title, authors, year, abstract and export provenance.

### S1.3 Cross-source deduplication
Order: DOI exact -> stable identifier exact -> normalized title exact -> fuzzy title + first author + year candidate -> human verification.
Required outputs: canonical-record ledger, duplicate-link ledger and reconciliation report.

### S1.4 Title/abstract screening
- 31 deterministic PubMed work units cover 7,728 records.
- Automation may prioritize or flag; it does not populate genuine reviewer identity or binding eligibility decisions.
- Uncertain records advance.

### S1.5 Full-text eligibility
For every advanced record capture retrieval state, final decision, controlled exclusion code, reviewer, evidence note and version.

### S1.6 Study-family resolution
Link preprint/conference/journal/companion reports to one study family where they describe the same underlying study; retain materially distinct evidence.

### S1.7 Citation chasing
Process backward and forward citations from the designated included seed set. Continue until the frozen stopping rule is met and no unsearched citation branch remains within the date window.

### S1.8 Stage-1 gate
Pass only when title/abstract, full text, study-family and citation-chasing ledgers reconcile and no required genuine decision is blank.

## Reviewer suggestions captured for Stage 1

1. Execute missing technical databases, especially IEEE Xplore and ACM DL.
2. Preserve complete database-specific search strings, dates, filters, export counts and checksums.
3. Complete genuine title/abstract screening.
4. Complete full-text eligibility and controlled exclusion reasons.
5. Resolve study families before counting studies.
6. Complete backward/forward citation chasing.
7. Keep background/review bibliography distinct from the included primary-study corpus.
8. Do not release final PRISMA or field-wide percentages before this gate passes.

## Integrity rule

A source marked LIMITATION is accounted for but is not EXECUTED. An automated triage label is not a human screening decision. A reviewer-ready packet is not an included-study corpus. These distinctions are immutable in downstream reporting.
