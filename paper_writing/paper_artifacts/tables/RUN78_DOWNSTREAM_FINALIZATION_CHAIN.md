# Run 78 — Downstream Finalization Chain

Run 78 operationalizes the complete post-screening chain.

| Stage | Repository artifact | Current state |
|---|---|---|
| Genuine TA validation | `final_title_abstract_ledger.csv` + validator | **BLOCKED: 0/7,728 genuine decisions** |
| Full-text screening | `final_full_text_ledger.csv` | Initialized, evidence pending |
| Study-family resolution | `final_study_family_ledger.csv` | Initialized, evidence pending |
| Citation chasing | `final_citation_chase_ledger.csv` | Initialized, evidence pending |
| Independent verification/adjudication | `final_independent_verification.csv` | Initialized, evidence pending |
| Corpus freeze | `FINAL_CORPUS_FREEZE.sha256` | Fail-closed |
| Final PRISMA | `generate_final_prisma_run78.py` | Fail-closed |
| NEXT-06–NEXT-19 | existing final-analysis contract | Runs after freeze |
| Numerical Abstract/Results/Conclusions | existing manuscript numerics contract | Runs last |

The chain was executed on 2026-10-06 and behaved correctly: downstream ledgers were created, but no eligibility decision or final number was fabricated.
