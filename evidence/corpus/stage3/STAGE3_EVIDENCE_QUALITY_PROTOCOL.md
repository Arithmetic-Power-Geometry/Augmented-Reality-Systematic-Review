# Stage 3 — Evidence and Study-Quality Analysis Protocol

Status: analysis architecture complete; final execution gated by Stages 1–2.

## Objective
Transform the independently validated corpus into auditable evidence matrices without pooling incompatible AR studies.

## Final evidence representation
For each canonical study, extract P_i=(D,T,H,S,A,M,E,U,R): domain, AR technology, hardware, sensing, method, metrics/outcomes, environment, users/population, and reproducibility. Missingness is explicit: reported, not_reported, unclear, not_applicable.

## Comparability C0–C3
C0 non-comparable; C1 contextual comparison; C2 benchmark comparable; C3 controlled reproduction comparable. Pairwise judgments record task, dataset/material, metric semantics, protocol, and hardware/context alignment.

## Transfer T0–T5
Assign a transfer level only to a documented claim and boundary crossing. Generalization rhetoric is not transfer evidence.

## Reproducibility R0–R8
Derive R-level from component evidence. Open full text, named hardware, or a repository link alone does not establish reproduction or replication.

## Study-design classification
Classify observable design features before quality appraisal: controlled human experiment; observational/user study; technical/algorithm benchmark; system/prototype evaluation; field/action-research/case study; mixed-methods; other/unclear.

## Design-appropriate quality / risk-of-bias assessment
One universal numeric quality score is prohibited.

For studies genuinely estimating intervention effects, use an appropriate established design-specific risk-of-bias approach and preserve domain-level judgments.

For technical/system/benchmark studies, use the technical evidence-quality profile:
1 task/problem definition clarity;
2 dataset/material provenance;
3 comparator appropriateness;
4 metric semantics/calculation;
5 calibration/train-test/evaluation separation where applicable;
6 hardware/environment specification;
7 repeated runs/uncertainty/statistical analysis where applicable;
8 failure-case reporting;
9 artifact/configuration availability;
10 claim-to-evidence alignment.

For qualitative/mixed-methods/action-research studies assess sampling/context transparency, data-collection transparency, analytic traceability, reflexivity/triangulation where applicable, missingness, and claim-to-evidence alignment.

Allowed judgments: low_concern, some_concern, high_concern, unclear, not_applicable. No arithmetic total substitutes for domain judgments.

## Evidence Cube
Populate technique × environment × device × user × metric × domain cells from frozen P_i records. Sparse cells are observations, not automatic gaps.

## Final outputs
P_i matrix; C0–C3 matrix; T0–T5 matrix; reproducibility component matrix/R distribution; design classification; quality/risk-of-bias matrix; Evidence Cube occupied-cell table; provenance/checksums.

## Exit
PASS requires Stage 1 PASS and Stage 2 PASS plus complete reconciled matrices for every canonical included study. Pilot outputs remain PILOT and cannot satisfy the final gate.
