# Researcher-Facing Decision Model

A central objective is to make the review operationally useful rather than merely descriptive.

For each AR research problem, the evidence base should ultimately permit a researcher to traverse:

**Problem → Method family → Candidate algorithms → Dataset/benchmark → Metrics → Hardware/sensors → Evaluation protocol → Comparable baselines → Evidence strength → Reproducibility → Failure regimes → Open gaps**

## Comparability classes

### C0 — Non-comparable
Material differences in task definition, metric semantics, dataset, protocol, or sensing assumptions prevent a defensible direct numerical comparison.

### C1 — Contextually comparable
Studies address the same problem but differ in one or more consequential experimental conditions. Qualitative or stratified comparison is appropriate.

### C2 — Benchmark comparable
Task, dataset/split, metric semantics, and core protocol are sufficiently aligned for direct comparison, while hardware/compute differences are explicitly reported.

### C3 — Reproduction comparable
Methods are rerun within the project's controlled benchmark environment using harmonized data, metrics, and reporting.

No global AR leaderboard will combine incompatible problem families.

## Gap states

- **Reported** — stated as a limitation/future direction in prior work.
- **Observed** — low evidence density detected in the structured corpus.
- **Persistent** — observed across multiple time windows.
- **Contradictory** — materially comparable studies disagree.
- **Reproducibility-limited** — claims cannot be independently checked with available artifacts.
- **Experimentally actionable** — a testable hypothesis and defensible benchmark can be specified.
- **Verified opportunity** — survives closest-prior-work audit and experimental feasibility checks.

Only the final two states may trigger new algorithm development.
