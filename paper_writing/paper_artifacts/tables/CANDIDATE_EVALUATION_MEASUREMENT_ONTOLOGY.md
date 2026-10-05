# Candidate AR Evaluation and Measurement Ontology

## Measurement families

| Code | Family | Examples | Interpretation constraint |
|---|---|---|---|
| M1 | objective task performance | completion time, accuracy, error rate, success, throughput | task/protocol dependent |
| M2 | perceived usability / UX | SUS, UEQ, satisfaction, ease of use | self-report; instrument/version must be retained |
| M3 | cognitive/workload | NASA-TLX, Paas scales, secondary-task measures | workload construct/subscales must not be collapsed blindly |
| M4 | physiological / behavioral state | eye tracking, pupil, EEG, EDA, HR/HRV | requires baseline/reference and signal-processing provenance |
| M5 | presence/immersion/embodiment | presence scales, immersion, ownership | construct and scale dependent |
| M6 | acceptance/adoption | TAM/UTAUT, intention, perceived usefulness | not equivalent to usability or performance |
| M7 | learning/retention | pre/post tests, delayed retention, transfer | time horizon and comparator required |
| M8 | safety | hazard detection, situational awareness, collisions/near-misses | mobility/environment/display conditions required |
| M9 | collaboration/social | coordination, shared awareness, communication, social presence | group structure and collaboration mode required |
| M10 | system/resource | latency, FPS, memory, energy, bandwidth, tracking error | hardware/software/network boundary required |

## Multi-method evidence rule
A study using multiple instruments is coded into multiple M-families. It is not assigned a single generic “UX metric.”

## Comparability rule
Two measurements are candidates for quantitative comparison only if:
1. construct is equivalent;
2. instrument/metric definition is compatible;
3. task and exposure are sufficiently aligned;
4. reporting includes required denominator/variance where relevant;
5. device/environment effects are not known major confounders.

## Evidence basis
- Dey et al. 2018: 291 papers / 369 user studies; strong laboratory dominance in historical AR usability research.
- Lim et al. 2019: 72 MAR-learning articles; usability metrics/methods/techniques are heterogeneous.
- Buchner et al. 2021: 64 AR cognitive-load studies; NASA-TLX most common; load-type differentiation largely missing.
- Suzuki et al. 2024: 23 physiological cognitive-load studies; eye tracking most common; multi-method validation recommended.
- Hughes & Karwowski 2025: 86 AR interaction/UX papers; self-report dominates, objective/physiological evaluation remains sparse.

This ontology is pre-freeze and must be audited against the final eligible corpus.
