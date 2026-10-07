# Final 8-Prompt Execution Plan — AR Systematic Review

Status: ACTIVE
Rule: advance only when the current prompt's evidence gates are genuinely satisfied. Assisted/automated labels must never be relabeled as independent human/reviewer decisions.

## Prompt 1 — Screening and eligibility
Complete genuine title/abstract screening and eligibility for the formal PubMed workload, including resolution of metadata-unavailable records. Preserve inclusion/exclusion codes, uncertainty, provenance, and reviewer identity. Do not substitute assisted triage labels for primary decisions.

Exit gate: all title/abstract records have genuine primary decisions; unresolved metadata records are explicitly resolved or retained as documented unavailable cases; screening arithmetic validates.

## Prompt 2 — Full text, families, citation chasing, corpus closure
Complete full-text assessment with reasons, resolve companion reports/study families, complete backward/forward citation chasing to the registered stopping rule, reconcile additions, and close the candidate corpus.

Exit gate: full-text ledger, family ledger, citation-chase ledger, and corpus accounting reconcile with no silent unresolved records.

## Prompt 3 — Final extraction and Coder-B reliability
Complete final structured extraction, including P_i fields, C0-C3 comparability, T0-T5 transfer, R0-R8 reproducibility, study-design appraisal and Evidence Cube fields. Complete independent Coder-B verification, disagreements/adjudication, and agreement statistics only over genuinely double-coded material.

Exit gate: extraction completeness and reliability gates pass.

## Prompt 4 — Final synthesis
Run comparability, transfer, reproducibility, contradiction, failure-regime, persistent-gap, closest-prior-work, domain/temporal and Evidence Cube analyses. Distinguish NOT_COMPARABLE, INSUFFICIENT_EVIDENCE, CONDITION_DEPENDENT and VERIFIED_CONTRADICTION states.

Exit gate: every synthesis claim maps to frozen evidence and denominators.

## Prompt 5 — Experiments, benchmark, statistics, robustness and sensitivity
Run only defensible executable AR benchmark/experimental analyses supported by the audited evidence. Complete statistics, ablations where applicable, robustness checks, and prespecified database/coder/threshold/unresolved-field/study-family/quality/comparability sensitivity analyses.

Exit gate: executable artifacts, statistics and sensitivity outputs are frozen and internally consistent.

## Prompt 6 — Freeze, PRISMA and final artifacts
Freeze the final corpus; derive PRISMA from ledgers rather than manual counts; generate final figures, tables and algorithms; freeze hashes/provenance; run claim-to-evidence and numerical-consistency audits.

Exit gate: final-results release gate passes with no blocked prerequisite.

## Prompt 7 — Complete manuscript
Write the complete submission-level paper from the frozen evidence and artifacts. No manuscript claim may outrun the evidence. Integrate all cited tables, figures, algorithms, limitations, data/code statement and declarations.

Exit gate: compilable, internally consistent, submission-ready manuscript package.

## Prompt 8 — Hostile TVCG review and final revision
Review the manuscript as a hostile expert TVCG reviewer, enumerate reject-level weaknesses section by section, verify each against artifacts, revise all defensible issues, and perform final submission audit.

Exit gate: no known critical evidence, consistency, provenance, citation, figure/table/algorithm, or reproducibility defect remains.

## Current execution
Prompt 1 is the active gate. Prompts 2–8 must not be represented as complete before their exit gates pass.
