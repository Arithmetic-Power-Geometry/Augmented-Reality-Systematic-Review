# Stage 2 — Pilot Validation Packet

## Purpose
Exercise the Stage-2 instruments on the existing 16-study pilot before final-corpus execution. This packet does not create a second reviewer's judgments.

## Pilot studies
S0001–S0016 from `evidence/primary/structured_extraction_batch01.csv`.

## Reviewer-B assignment
Independently inspect the source report for each pilot study and complete:
1. P_i fields D,T,H,S,A,M,E,U.
2. Reproducibility components and R-level.
3. Evidence note identifying the source location supporting each non-obvious judgment.

## Comparability validation pairs
The following pairs deliberately cover different expected difficulty:
- S0005 vs S0006 — human factors/cognitive workload.
- S0005 vs S0016 — workload with physiological measures.
- S0003 vs S0012 — accessibility in different contexts/populations.
- S0008 vs S0009 — AR/digital-twin industrial systems.
- S0008 vs S0015 — operator-facing digital-twin evidence.
- S0010 vs S0014 — localization/tracking under different sensing/environment.
- S0002 vs S0011 — HMD interaction with different populations/tasks.
- S0001 vs S0005 — deliberate cross-domain negative-control pair.

Reviewer B assigns C0–C3 independently and records task, dataset, metric, protocol and hardware alignment.

## Transfer validation
For each study with an explicit transfer/generalization claim, code T0–T5 only from documented evidence. If no transfer claim/evidence exists, use not_applicable rather than inventing a level.

## Reliability outputs
After Reviewer B submission:
- preserve Reviewer-A and Reviewer-B files;
- run `scripts/stage2_reliability.py`;
- inspect confusion matrices/disagreements;
- adjudicate in a separate ledger;
- freeze the post-training codebook before final-corpus reliability coding.

## Critical prohibition
The existing pilot descriptions, assisted labels, or prior C-level notes must not be copied into Reviewer B's form. They may be used only after independent submission for comparison/adjudication.
