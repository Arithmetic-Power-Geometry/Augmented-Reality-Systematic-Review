# Stage 2 — Coding Reliability Codebook

## P_i
- **D Domain:** research/application domain evidenced by the study.
- **T AR technology:** AR modality, display/role, or implementation class.
- **H Hardware:** named device and compute boundary.
- **S Sensing:** sensors/input channels used materially by the method/evaluation.
- **A Method:** algorithm, interaction, guidance, adaptation, or system mechanism.
- **M Metrics:** measured outcome semantics, not merely metric labels.
- **E Environment:** lab/field/simulation and relevant environmental conditions.
- **U Users:** participant/population or system-only evaluation.
- **R Reproducibility:** component evidence and derived reproducibility state.

## C0–C3
- C0: direct numerical comparison invalid due to consequential incompatibility.
- C1: same broad problem; contextual/stratified comparison only.
- C2: benchmark/task/metric/core protocol sufficiently aligned for direct comparison with residual differences disclosed.
- C3: controlled reproduction with harmonized data, metrics, and reporting.

## T0–T5
- T0: result demonstrated only in its original narrow test condition.
- T1: transfer across repeated runs/splits within the same benchmark regime.
- T2: transfer across device/hardware configuration.
- T3: transfer across environment/site/context.
- T4: transfer across user/task population or operational workflow.
- T5: sustained field/multi-context evidence supporting the broader claim.
A higher level is not inferred from rhetoric; evidence must document the boundary crossed.

## R0–R8
R-level is an ordinal summary derived from component evidence:
- R0: insufficient artifact/procedural information to independently inspect execution.
- R1: method/procedure described.
- R2: key materials/data identifiers available.
- R3: code or executable implementation available.
- R4: environment/configuration sufficiently specified for attempted rerun.
- R5: independent execution demonstrated.
- R6: reported computational/technical result reproduced.
- R7: independent replication on a materially new sample/context.
- R8: multi-context or repeated independent replication supporting robustness.
The exact derived level must never exceed the strongest documented component state.

## Missingness
Use: reported, not_reported, unclear, not_applicable. Never map unclear/not_reported to a negative scientific result.
