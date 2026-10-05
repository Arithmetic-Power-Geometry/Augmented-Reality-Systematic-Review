# TVCG Execution Master Plan

**Target:** IEEE Transactions on Visualization and Computer Graphics (TVCG)  
**Purpose:** persistent completion ledger and sequential execution queue for the AR systematic-review programme.

## Completed foundation

- Research problem, chronology and 13 research questions: complete.
- Evidence representation `P_i=(D,T,H,S,A,M,E,U,R)`: complete.
- Evidence Cube concept: complete.
- Comparability classes C0-C3: complete.
- Seven-state gap model: complete.
- Researcher decision model: complete.
- 25 specialist AR workstreams: defined.
- Review-of-reviews: 19 verified seed reviews.
- Phase-1 candidate gaps: six registered.
- Tracking/localization/SLAM technical audit: advanced.
- ORB-SLAM3, VINS-Mono, OpenVINS and LaMAR baseline family: registered.
- EuRoC/TUM/TUM-VI/LaMAR benchmark map: initial complete.
- ATE/RPE/recall/latency/FPS/memory/energy/failure metric contracts: initial complete.
- E001 protocol: preregistered.
- Common evaluator and synthetic mathematical tests: complete.
- EuRoC ground-truth adapter: complete.
- One-command E001/provenance pipeline: implemented.
- ORB-SLAM3 and Pangolin revisions: immutable full SHAs frozen.
- Ubuntu 18.04 container reconciliation and build-smoke workflow: implemented.
- Scientific E001/E002/E003 performance results: **none yet**.

## Manuscript contribution gates

1. Unified AR evidence representation.
2. Formal C0-C3 comparability framework.
3. Evidence-qualified gap discovery.
4. Reproducibility/comparability audit.
5. Review-to-experiment bridge.

Candidate gaps are not findings. Reported results are not reproduced results. Empty Evidence Cube cells are not automatically research gaps. The adaptive localization method must not be called novel before closest-prior-work and experimental failure-regime audits.

## Sequential execution queue

| ID | Task | Gate | Paper | Status |
|---|---|---|---|---|
| NEXT-01 | Freeze systematic primary-study search protocol: sources, queries, dates, inclusion/exclusion, deduplication, screening rules and search registry | BLOCKING | P1 | **COMPLETE — adversarial gate PASS** |
| NEXT-02 | Primary-study discovery batch 1 across 25 workstreams; preserve raw discovery records | BLOCKING | P1 | **COMPLETE — discovery-only reviewer PASS** |
| NEXT-03 | Deduplication and screening engine with exclusion reasons | BLOCKING | P1 | **COMPLETE — reviewer PASS** |
| NEXT-04 | Populate D,T,H,S,A,M,E,U,R and reproducibility fields for eligible studies | BLOCKING | P1 | **COMPLETE — pilot extraction reviewer PASS** |
| NEXT-05 | Continue search/screening to exhaustion; freeze eligible corpus and PRISMA counts | BLOCKING | P1 | **BLOCKED — source-native formal exports required** |
| NEXT-06 | Temporal evolution analysis | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-07 | Domain × technology / Evidence Cube analysis | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-08 | Finalize algorithm/method taxonomy beyond localization | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-09 | Hardware × sensor × environment analysis | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-10 | Dataset × algorithm analysis | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-11 | Metric-fragmentation analysis | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-12 | Compute C0-C3 comparability distribution and causes | CORE NOVELTY | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-13 | Primary-study reproducibility audit | CORE NOVELTY | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-14 | User/population/accessibility analysis | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-15 | Cognitive-load stratification | REQUIRED | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-16 | Contradiction mining | CORE NOVELTY | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-17 | Persistent-gap analysis | CORE NOVELTY | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-18 | Researcher decision map | CORE NOVELTY | P1 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-19 | Rank experimentally actionable opportunities after closest-prior-work checks | REQUIRED | P1/P2 | **PILOT COMPLETE — final corpus rerun blocked** |
| NEXT-20 | Confirm actual ORB-SLAM3 build-smoke evidence | BLOCKING | P2 | TODO |
| NEXT-21 | Execute E001; preserve raw/provenance/ATE/RPE | BLOCKING | P2 | TODO |
| NEXT-22 | Design sensor-fair mono-inertial ORB-SLAM3 baseline | REQUIRED | P2 | TODO |
| NEXT-23 | Execute matched VINS-Mono/OpenVINS runs | REQUIRED | P2 | TODO |
| NEXT-24 | Freeze and execute LaMAR AR-native track | REQUIRED | P2 | TODO |
| NEXT-25 | Benchmark-transfer stability analysis | CORE RESULT | P2 | TODO |
| NEXT-26 | Failure-regime analysis | CORE RESULT | P2/P3 | TODO |
| NEXT-27 | Adaptive-method closest-prior-work novelty audit | NOVELTY GATE | P3 | TODO |
| NEXT-28 | Formulate new method only if verified gap survives | CONDITIONAL | P3 | TODO |
| NEXT-29 | Novel-method baselines, ablations, robustness and statistics | CONDITIONAL | P3 | TODO |
| NEXT-30 | Generate/freeze final paper figures, tables and evidence release | BLOCKING | P1 | TODO |
| NEXT-31 | Write TVCG manuscript from frozen evidence | FINAL | P1 | TODO |
| NEXT-32 | Final TVCG submission audit | FINAL | P1 | TODO |

## Writing gate

Framework/Methods prose may be drafted before the evidence corpus is frozen. Results, Discussion and novelty claims must wait for committed analysis artifacts. Full Paper 1 writing begins after NEXT-05 and the core analyses NEXT-06 through NEXT-18 are reproducibly available.

## Planned final evidence package

**Figures:** research workflow; PRISMA; temporal evolution; unified taxonomy; Evidence Cube; comparability network; reproducibility landscape; persistent/contradictory gap map; researcher decision framework.

**Tables:** closest reviews; protocol/search strategy; evidence dimensions; method families; datasets/benchmarks; metric/comparability rules; reproducibility findings; verified gaps/opportunities.

**Repository/supplement:** primary-study database, screening ledger, extraction tables, complete matrices, scripts, manifests, provenance, experimental raw/derived outputs and generated figures/tables.

## Current project-management state

Paper-1 methodology, bibliography, pilot extraction and pilot analyses NEXT-06 through NEXT-19 are complete. Final population-level reruns remain dependent on NEXT-05 formal source exports and corpus freeze. P2/P3 experiments remain separate future work and are not required to fabricate Paper-1 review findings.

## Resume marker

> **NEXT TASK: NEXT-05 EXTERNAL INPUT — obtain source-native formal exports. On arrival, execute the already-frozen ingestion → deduplication → screening → study-family → citation-chase → corpus-freeze → PRISMA → final-analysis pipeline.**