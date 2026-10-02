# Review and Evidence-Mining Protocol

## 1. Study design

The project uses a staged design combining:
1. tertiary review of existing AR/XR review literature;
2. systematic review of primary AR studies;
3. structured evidence mapping;
4. algorithm/dataset/metric comparability analysis;
5. reproducibility audit;
6. temporal and cross-dimensional gap mining;
7. executable benchmarking where fair comparison is possible;
8. optional development of a new method only after gap verification.

## 2. Scope

The core scope is augmented reality. Mixed reality and extended reality studies are included only when the AR component is separable or materially informs an AR method, benchmark, dataset, interaction technique, evaluation protocol, or research gap.

## 3. Historical coverage

The search is intentionally longitudinal:
- foundational AR research;
- 1990s;
- 2000–2009;
- 2010–2019;
- 2020–2024;
- 2025 onward.

No temporal gap is inferred from raw publication counts alone.

## 4. Review-of-reviews phase

Before primary-study synthesis, existing systematic reviews, surveys, scoping reviews, meta-analyses, and major historical syntheses are catalogued.

For each review extract:
- scope;
- years covered;
- databases;
- search strategy;
- inclusion/exclusion criteria;
- number of included studies;
- taxonomy;
- technologies;
- algorithms;
- datasets;
- benchmarks;
- metrics;
- user populations;
- devices;
- applications;
- reproducibility treatment;
- limitations;
- research gaps;
- future directions;
- whether code/data are available.

This phase establishes what has already been synthesized and prevents novelty claims based on rediscovering known gaps.

## 5. Primary-study search

Search sources should include, where accessible:
- IEEE Xplore;
- ACM Digital Library;
- Scopus;
- Web of Science;
- ScienceDirect;
- SpringerLink;
- PubMed for health-related AR;
- arXiv only as supplementary preprint coverage.

Backward and forward snowballing is applied to influential and foundational studies.

## 6. Eligibility

A primary study is eligible when it contributes evidence concerning an AR technology, algorithm, system, dataset, benchmark, interaction, evaluation, application, user population, limitation, or reproducibility issue.

Exclusions include:
- purely VR work with no separable AR relevance;
- non-technical commentary lacking analyzable evidence;
- duplicate reports of the same experiment unless the later version materially extends evidence;
- inaccessible records lacking sufficient methodological information for extraction.

## 7. Evidence extraction schema

Each included study is represented using structured fields covering:
- bibliographic identity;
- research problem;
- domain;
- AR modality;
- hardware;
- sensors;
- environment;
- user population;
- task;
- algorithm/method;
- dataset;
- benchmark;
- metric;
- baseline;
- experimental protocol;
- statistical analysis;
- reported result;
- reported limitation;
- code availability;
- data availability;
- model/checkpoint availability;
- environment/configuration availability;
- reproducibility status;
- threats to validity.

## 8. Gap classes

Candidate gaps are classified as:
- literature gap;
- algorithmic gap;
- dataset gap;
- benchmark gap;
- metric gap;
- reproducibility gap;
- population gap;
- hardware gap;
- environment gap;
- longitudinal-evidence gap;
- cross-domain gap;
- integration gap;
- scalability gap;
- contradiction gap;
- real-world-validation gap.

A missing cell is not automatically a research gap.

## 9. Gap verification rule

A candidate gap advances only if:
1. it is supported by structured evidence rather than a single author's future-work statement;
2. closest prior work has been checked;
3. the absence cannot be explained solely by terminology fragmentation;
4. the problem is scientifically meaningful;
5. an evaluation protocol can be specified.

## 10. Algorithm comparability

Algorithms are compared only inside compatible benchmark families. Compatibility considers:
- task definition;
- dataset;
- train/test split;
- device/sensor configuration;
- environment;
- metric definition;
- preprocessing;
- computational budget;
- implementation assumptions.

Results from incompatible protocols are not merged into a single leaderboard.

## 11. Reproducibility audit

Record availability of:
- source code;
- data;
- trained models;
- configuration;
- random seeds;
- hardware specifications;
- dependency versions;
- evaluation scripts;
- raw outputs.

## 12. Novel-method gate

A new algorithm or method is developed only if a verified gap survives prior-art review and can be evaluated against defensible baselines under a reproducible protocol.

The new method must include:
- formal problem definition;
- rationale;
- algorithm/pseudocode;
- complexity or resource analysis where applicable;
- baseline comparison;
- ablation;
- robustness/sensitivity analysis;
- statistical analysis;
- failure cases;
- reproducibility artifacts.

## 13. Artifact generation

Figures and tables used to support research conclusions should be generated from machine-readable evidence or experimental outputs whenever possible.

Planned artifact families include:
- temporal evolution;
- review coverage matrix;
- technology taxonomy;
- algorithm taxonomy;
- dataset/benchmark matrix;
- metric map;
- device/sensor matrix;
- comparability graph;
- reproducibility landscape;
- contradiction graph;
- evidence-density map;
- persistent-gap timeline;
- benchmark tables;
- ablation tables;
- statistical summaries.

## 14. Paper-writing gate

Paper drafting begins only after:
- screening is frozen;
- evidence extraction is validated;
- benchmark definitions are frozen;
- experiments are complete;
- artifacts are reproducibly generated;
- major claims map to evidence;
- closest-prior-review comparison is complete.

The paper reports the completed research process; the repository does not contain authoring instructions intended to manufacture paper claims.
