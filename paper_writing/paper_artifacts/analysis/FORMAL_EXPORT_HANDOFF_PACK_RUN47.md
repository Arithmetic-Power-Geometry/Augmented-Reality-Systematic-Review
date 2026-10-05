# Formal Export Handoff Pack — Run 47

For each of the seven registered sources (IEEE Xplore, ACM Digital Library, Scopus, Web of Science Core Collection, ScienceDirect, SpringerLink, PubMed), execute Q00-Q12 using the frozen translation specification.

For every source-query execution preserve:
1. source/database and platform;
2. query ID;
3. exact executed query (copy verbatim);
4. execution date;
5. frozen date filters;
6. any additional filters;
7. raw result count shown by source;
8. exported record count;
9. raw export file (CSV, RIS or BibTeX);
10. SHA-256 of raw export;
11. access or export limitation, if any.

Naming convention:
evidence/search/raw_exports/<source>/<search_run_id>_<query_id>_<YYYY-MM-DD>.<ext>

Do not edit the raw export after download. If a source requires query splitting, retain each subquery/export and document the union before deduplication.

Once exports are present:
- populate search_registry.csv;
- promote matching execution-matrix cells to EXECUTED only after provenance validation;
- run importer;
- reconcile counts;
- pool;
- adjudicate duplicate candidates;
- freeze dedup pool;
- screen;
- full-text assess;
- resolve study families;
- citation chase;
- freeze final corpus;
- derive PRISMA;
- rerun all final analyses.

This pack implements PRISMA/PRISMA-S requirements for source, platform, executed strategy/date and record flow; it does not claim execution itself.
