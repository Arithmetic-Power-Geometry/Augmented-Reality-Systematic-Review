# Stage 2 — Independent Validation and Coding Reliability Protocol

**Status:** methodology/software complete; final-corpus execution gated by Stage 1.

## Objective
Stage 2 establishes whether eligibility and evidence coding are reproducible across genuinely independent human reviewers before any final evidence synthesis is released.

## Independence rule
Reviewer B receives source material, frozen definitions, and blank coding fields. Reviewer B must not receive Reviewer A's binding judgments before submitting the independent form. Automation may validate syntax and calculate agreement; it must not generate reviewer judgments.

## Validation layers

### V1 — Eligibility decisions
Unit: record/report. Categories: include, exclude, uncertain. For exclusions, controlled reason codes are also compared.

Metrics:
- N double-screened
- raw percent agreement
- Cohen's kappa for nominal eligibility
- reason-code agreement among jointly excluded records
- confusion matrix
- disagreement count and rate

### V2 — P_i structured extraction
Dimensions: D, T, H, S, A, M, E, U, R.
Each dimension is compared independently. Multi-label fields are normalized as sets before comparison.

Metrics per dimension:
- exact agreement
- set/Jaccard agreement for multi-label fields
- missingness disagreement
- optional nominal kappa where categories are sufficiently recurrent

### V3 — C0–C3 comparability
Independent reviewers assign C0, C1, C2 or C3 using the frozen decision model.
Report raw agreement, weighted kappa, confusion matrix, and adjudicated state.

### V4 — T0–T5 transfer
Independent reviewers assign transfer level only when the evidence supports a transfer claim. Report weighted kappa and disagreements by boundary transition.

### V5 — R0–R8 reproducibility
Independent reviewers code component evidence first (materials, data, code, environment/configuration, executability, reproduction, replication) and derive the R-level only after component coding. Unknown is never converted to unavailable.

## Disagreement resolution
1. Preserve Reviewer A and Reviewer B raw forms unchanged.
2. Generate machine comparison without changing either form.
3. Reviewers discuss each disagreement using the source evidence and codebook.
4. If unresolved, route to an adjudicator.
5. Store consensus/adjudicated value separately.
6. Never overwrite the original independent judgments.

## Reliability interpretation
No universal kappa threshold is used as an automatic validity verdict. Agreement statistics are reported with N, category prevalence, confusion matrices, and substantive disagreement patterns. Low agreement triggers codebook clarification and, where necessary, recoding.

## Training/pilot
Before final-corpus coding, both reviewers independently code the same pilot studies. Training discussion may refine definitions, but the reliability sample used for reporting must be coded independently under the frozen post-training codebook.

## Final Stage-2 exit gate
PASS requires:
- Stage 1 frozen corpus exists;
- required independent eligibility verification completed;
- required independent extraction completed;
- C0–C3, T0–T5, R0–R8 validation samples completed where applicable;
- all disagreements either resolved or explicitly retained as unresolved;
- agreement report generated from raw independent forms;
- consensus/adjudication ledger reconciles to raw forms;
- Stage-2 checksums written.

No Stage-3 evidence distribution is released before this gate passes.
