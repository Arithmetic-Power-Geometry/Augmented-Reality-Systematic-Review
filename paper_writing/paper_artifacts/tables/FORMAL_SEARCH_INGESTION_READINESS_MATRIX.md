# Formal Search Ingestion Readiness Matrix — Run 35

| Gate | Required evidence | Automated by importer | Current state |
|---|---|---:|---|
| Exact executed source/query | registry status=EXECUTED | yes | BLOCKED: no formal executions yet |
| Raw export immutability | SHA-256 | yes | ready once exports exist |
| Export count integrity | exported_count vs parsed | yes | ready |
| Canonical normalization | DOI/title/first author/year | yes | ready |
| Exact duplicate candidates | DOI/stable ID/title | yes | ready |
| Fuzzy duplicate candidates | title+author+year | yes, flag only | ready; human decision mandatory |
| Study-family merge | explicit report relationship | no auto-merge | human ledger required |
| Screening | frozen inclusion/exclusion rules | no | human/reviewer workflow required |
| PRISMA counts | frozen ledgers | downstream only | blocked until formal corpus exists |

**Interpretation:** infrastructure readiness is not formal-search completion. No database retrieval or PRISMA count is claimed here.
