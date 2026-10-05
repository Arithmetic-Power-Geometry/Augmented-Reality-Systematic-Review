# Adversarial IEEE/TVCG Reviewer Gate

## Role

This repository uses a deliberately skeptical internal reviewer role at every execution stage. The role is not a substitute for external peer review and cannot guarantee acceptance. Its purpose is to expose reasons a demanding IEEE/TVCG reviewer could reject the work before the next stage is allowed to proceed.

The reviewer must assume the manuscript should be rejected unless the evidence overcomes the objection.

## Mandatory review dimensions

At every stage inspect:
1. scope fit and research significance;
2. novelty relative to closest prior work;
3. protocol completeness and preregistration/freeze integrity;
4. sampling/search bias and missing evidence;
5. data provenance and leakage;
6. validity of metrics and statistical analysis;
7. baseline and comparison fairness;
8. reproducibility and environment specification;
9. robustness, ablation and failure cases where applicable;
10. claim–evidence alignment and overclaiming;
11. figure/table traceability;
12. threats to validity and generalizability;
13. whether an apparently positive result could arise from a weaker alternative explanation.

## Severity

- CRITICAL: invalidates the stage or a central claim; stage cannot pass.
- HIGH: plausible rejection reason; stage cannot pass.
- MEDIUM: material weakness; resolve before manuscript freeze unless explicitly justified.
- LOW: clarity/presentation/secondary robustness issue.

## Required output

Each stage review must record:
`review_id, stage_id, severity, rejection_comment, evidence, required_fix, resolution, status`.

A stage is **PASS** only when CRITICAL=0 and HIGH=0 unresolved. The reviewer must not lower severity merely to advance the project.

## Reviewer independence rule

The reviewer critiques artifacts actually produced. It must not invent a second human screener, fabricated experiment, fabricated citation, or fabricated replication. Where genuine independent human verification is required, the gate records that dependency.

## NEXT-01 adversarial review

### R-N01-01 — HIGH — Search reproducibility
**Reject comment:** The prior protocol lists databases but does not preserve exact executed queries or source-specific adaptations; the search cannot be independently reconstructed.
**Required fix:** Freeze semantic query blocks and require verbatim executed queries, dates, filters, counts, exports and checksums in a machine-readable registry.
**Resolution:** Implemented in `protocol/PRIMARY_STUDY_SEARCH_STRATEGY.md` and `evidence/search/search_registry.csv`.
**Status:** RESOLVED.

### R-N01-02 — HIGH — Selection drift
**Reject comment:** Eligibility language is broad enough to permit post hoc inclusion/exclusion decisions.
**Required fix:** Freeze inclusion criteria and controlled exclusion codes before discovery.
**Resolution:** Controlled criteria and `protocol/SCREENING_CODES.csv` added.
**Status:** RESOLVED.

### R-N01-03 — HIGH — Duplicate publication bias
**Reject comment:** Conference, preprint and journal versions may be counted as independent evidence, inflating evidence density.
**Required fix:** Add DOI/title deduplication and study-family/companion-report rules.
**Resolution:** Canonical-report and `study_family_id` rules frozen.
**Status:** RESOLVED.

### R-N01-04 — HIGH — Arbitrary corpus-size target
**Reject comment:** A target such as 150–300 studies could bias stopping and inclusion.
**Required fix:** Use process-based search exhaustion/snowballing stopping criteria, not a desired number of studies.
**Resolution:** Search saturation/stopping rule frozen; no target N is a stopping criterion.
**Status:** RESOLVED.

### R-N01-05 — HIGH — Reviewer independence
**Reject comment:** Calling an AI critique an independent second reviewer would misrepresent screening reliability.
**Required fix:** Separate adversarial methodological review from genuine independent human screening; never fabricate inter-rater reliability.
**Resolution:** Explicitly prohibited in the protocol and this gate.
**Status:** RESOLVED.

### R-N01-06 — MEDIUM — English-only full-text restriction
**Reject comment:** English-only coding may introduce language bias.
**Required fix:** Preserve non-English discoveries in the screening ledger, use an explicit exclusion code, and report the limitation.
**Resolution:** E-LANGUAGE and reporting requirement added.
**Status:** RESOLVED.

## NEXT-01 verdict

**PASS after revision.** Unresolved CRITICAL: 0. Unresolved HIGH: 0.

This verdict means the search protocol is sufficiently specified to begin discovery. It does not imply that the eventual corpus or manuscript will be accepted by TVCG.
