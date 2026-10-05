# NEXT-05 Run 36 — CI Gate, Methods References, and Manuscript Start Decision

Pre-run state inherited from Run 35 was rechecked: formal matrix has 91 planned source-query cells and search registry has no executed formal runs.

Actions:
1. Added GitHub Actions workflow .github/workflows/formal-search-ingestion-integrity.yml.
2. Workflow checks Python syntax, runs the synthetic importer test, guards matrix status values, and requires provenance fields for any EXECUTED registry row.
3. Queried workflow runs associated with the workflow commit; none were returned by the available pull-request-run endpoint. Therefore no CI PASS is claimed.
4. Added five validated Methods references: PRISMA 2020, PRISMA-S, PRESS, Bramer 2016 deduplication, Bramer 2017 database combinations.
5. Bibliography advanced 156 -> **161**.
6. Added manuscript-start gate, claim-state algorithm, and figure.

Decision:
We do not need to wait for 200 references to begin drafting. A Methods-first manuscript skeleton can be created now using validated prior literature and prospective wording. Final corpus-derived Results, PRISMA counts, prevalence and final gap claims remain blocked until NEXT-05 freeze.

Remaining to 200+ breadth target: 39+ validated references. This target runs in parallel with formal corpus completion.
