# Augmented Reality Systematic Review

A reproducible research program for systematically mapping augmented reality (AR) research, auditing comparability and reproducibility, benchmarking representative algorithms where fair comparison is possible, and identifying experimentally actionable research gaps.

## Research chronology

This repository follows a research-first workflow:

1. Define the review protocol and evidence model.
2. Mine prior reviews and primary AR studies.
3. Build a structured evidence base.
4. Audit algorithms, datasets, metrics, hardware, environments, users, and reproducibility.
5. Identify candidate gaps.
6. Verify each candidate against closest prior work.
7. Reproduce and compare representative algorithms only when protocols are sufficiently comparable.
8. Formulate a new algorithm only if a genuine, experimentally testable gap survives the audit.
9. Run experiments, ablations, robustness checks, and statistical analyses.
10. Generate figures, tables, timelines, benchmark summaries, and other artifacts from code.
11. Freeze the reproducible evidence and artifact release.
12. Write the review paper from the frozen evidence.

The repository is not organized around manuscript generation. Paper text will be written only after the evidence, experiments, and artifacts are complete.

## Core research questions

- How has AR research evolved from foundational work to current intelligent and context-aware systems?
- Which technical, human, system, and application dimensions dominate the literature?
- Which algorithms can be compared fairly, and which cannot because of incompatible datasets, hardware, protocols, or metrics?
- Which datasets and benchmarks are reused sufficiently to support cumulative evidence?
- Where are evaluation and reproducibility weakest?
- Which reported gaps persist across time rather than appearing only in individual papers?
- Which underexplored combinations of technology, environment, hardware, user population, task, and metric represent credible research opportunities?
- Which of those gaps can be tested experimentally?
- Does any experimentally verified gap justify a new algorithm or method?

## Evidence layers

The project separates:
- prior-review evidence;
- primary-study evidence;
- algorithm evidence;
- dataset and benchmark evidence;
- evaluation-metric evidence;
- hardware and sensing evidence;
- user-study evidence;
- reproducibility evidence;
- reported limitations;
- computed candidate gaps;
- experimentally verified gaps.

## Planned outputs

The workflow will generate machine-readable evidence tables and reproducible artifacts including temporal maps, taxonomy figures, dataset and benchmark matrices, comparability graphs, metric-fragmentation analyses, reproducibility maps, contradiction maps, persistent-gap timelines, benchmark results, ablations, and statistical summaries.

## Target paper

Working title:

**Augmented Reality: A Systematic Review of Technologies, Algorithms, Benchmarks, Evaluation Methods, Research Gaps, and Future Directions**

Primary target under evaluation: **IEEE Transactions on Visualization and Computer Graphics (TVCG)**.

The final title and journal positioning will be frozen only after the evidence landscape and closest prior reviews have been audited.
