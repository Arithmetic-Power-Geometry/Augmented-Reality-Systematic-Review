# Candidate AR Reproducibility and Replication Evidence Model

Represent reproducibility evidence as:
R = (Reporting, Materials, Data, Code, Environment, Protocol, Executability, Reproduction, Replication, Provenance)

| Level | Evidence state | Minimum meaning |
|---|---|---|
| R0 | opaque | insufficient methodological/artifact detail |
| R1 | reported | method/device/sample/measures sufficiently described |
| R2 | materials available | questionnaires/stimuli/configuration/protocol available |
| R3 | data available | analysis-ready or documented raw/processed data available |
| R4 | code/software available | implementation/analysis code or executable artifact available |
| R5 | environment captured | versions, hardware, dependencies, parameters and seeds/config captured |
| R6 | independently executable | external party can run the released workflow/artifact |
| R7 | result reproduced | reported computational/technical result independently reproduced |
| R8 | study replicated | independent direct/conceptual replication of empirical finding |

Levels are descriptive evidence states, not a universal quality score. A study may expose data without code, or code without data; retain component flags in addition to the ladder.

## Comparability
Reported result != reproduced result != replicated finding.

## Evidence basis
- Merino et al. 2020: 458 MR/AR evaluation papers; 248 user studies, 5,761 participants; 216/248 laboratory studies.
- Hepperle et al. 2021: reproducibility/replicability vulnerabilities and workflow/toolkit recommendations for VR research.
- Arefin et al. 2025: 2,167 IEEE ISMAR/VR papers (2010-2024), only 83 replication studies (<4%).
- RATE-XR 2024: 17 XR-specific plus 14 generic reporting items for early clinical XR evaluation.
- Banzi et al. 2026: international consensus core reproducibility items spanning planning through dissemination.

## Review implication
Transparency, reproducibility and replication are coded separately. Missing artifacts are not automatically evidence that a result is false; they reduce the evidence available for independent verification.
