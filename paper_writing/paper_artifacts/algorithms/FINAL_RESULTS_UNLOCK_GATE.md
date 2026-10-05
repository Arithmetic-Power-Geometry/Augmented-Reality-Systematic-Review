# Algorithm — Final Results Unlock Gate

Input: repository evidence state
Output: METHODS_ONLY, PARTIAL_RESULTS, or FINAL_RESULTS_UNLOCKED

1. Require every declared formal source/query execution to have a registry record or an explicit documented source limitation.
2. For executed searches require exact query, date, source count, export count, raw export and SHA-256.
3. Require pooled ingestion and reconciled dedup decisions.
4. Require title/abstract screening decisions for every deduplicated record.
5. Require full-text disposition for every report sought.
6. Require study-family resolution for included reports.
7. Require citation-chase stopping rule to be satisfied.
8. Reconcile all PRISMA identities.
9. Freeze the included primary corpus and its checksum.
10. Run structured P_i extraction and quality checks.
11. If Steps 1-9 fail: METHODS_ONLY.
12. If Steps 1-9 pass but extraction/analysis incomplete: PARTIAL_RESULTS.
13. Only after Steps 1-10 and module-specific checks: FINAL_RESULTS_UNLOCKED.
14. Final manuscript Results/Discussion may then consume only frozen artifacts.
