# Algorithm — Parallel Formal Corpus Completion Pipeline

Input: source-native formal exports and execution metadata
Output: frozen primary corpus, PRISMA counts, final analyses and Results artifacts

## Parallel lane A — provenance and ingestion
For every source/query cell independently:
1. validate exact query and frozen date window;
2. hash immutable export;
3. reconcile exported_count;
4. normalize into canonical pooled schema;
5. emit ingestion manifest.

Barrier A: all 91 cells are EXECUTED or explicitly documented as source limitations.

## Parallel lane B — duplicate candidates
After each ingestion batch:
1. exact DOI candidates;
2. exact stable-ID candidates;
3. exact-title candidates;
4. fuzzy title + first author + year candidates;
5. never auto-delete fuzzy matches.

Barrier B: adjudicate every duplicate candidate; freeze deduplicated pool.

## Parallel lane C — title/abstract screening
Partition canonical records into deterministic batches.
Apply frozen I1-I5 / exclusion codes.
Uncertain advances.
Second independent human verification is required for final includes and stratified exclusions; no synthetic agreement statistic.

Barrier C: every canonical record has a TA disposition.

## Parallel lane D — full text and study families
For TA include/uncertain:
1. retrieve full text where available;
2. apply eligibility;
3. link preprint/conference/journal companions;
4. retain materially distinct evidence;
5. assign canonical study family.

Barrier D: every sought report has retrieval/full-text/family disposition.

## Parallel lane E — citation chasing
Backward and forward chase designated included seeds.
New records re-enter provenance/dedup/screening.
Stop only when frozen stopping rule is satisfied.

Barrier E: no unprocessed eligible citation branch remains inside date window.

## Freeze
Checksum registry + dedup ledger + screening ledger + family ledger + included primary corpus.
Derive PRISMA arithmetic from ledgers only.

## Parallel lane F — final extraction/analysis
On frozen included studies, run in parallel:
- P_i extraction;
- C0-C3 comparability;
- reproducibility R grading;
- field validity;
- benchmark/evidence infrastructure;
- human/accessibility/UX;
- contradiction and failure-regime mining;
- Evidence Cube;
- gap-promotion audit.

Final barrier: reconcile module outputs against corpus IDs and evidence provenance.
Then generate final Results tables/figures and unlock manuscript.
