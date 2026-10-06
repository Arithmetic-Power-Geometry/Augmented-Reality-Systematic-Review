# Run 76 — Final Results Release Algorithm

1. Import exactly 7,728 genuine title/abstract decisions with reviewer attribution.
2. Validate allowed decision/reason codes and reject blank reviewer identities.
3. Retrieve and screen all advanced full texts; record exclusion reasons.
4. Resolve multiple reports into canonical study families.
5. Complete backward/forward citation chasing under the frozen stopping rule.
6. Complete genuine independent verification and adjudication.
7. Freeze ledgers and write corpus checksums.
8. Rerun NEXT-06 through NEXT-19 exclusively on the frozen corpus.
9. Derive PRISMA counts from the ledgers, never by hand.
10. Compute included-study count from canonical study-family IDs.
11. Compute every percentage with an explicit frozen denominator.
12. Compute gap prevalence only from the final evidence-obligation/gap states.
13. Generate final Results tables/figures.
14. Generate the numerical Abstract and Conclusions last.
15. Fail closed if any upstream ledger, reviewer identity, checksum or final-analysis artifact is absent.
