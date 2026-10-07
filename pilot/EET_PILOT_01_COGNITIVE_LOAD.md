# EET Pilot 01 — Cognitive-Load Claim Entitlement

## Purpose
Stress-test Evidence Entitlement Theory (EET) before corpus-wide use. The pilot asks whether a claim-entitlement analysis reveals scientifically relevant structure that conventional counting, taxonomy, evidence-gap mapping, simple quality scoring, or generic value-of-information reasoning does not expose directly.

## Pilot domain
AR cognitive load and procedural/assembly performance.

## Evidence seed
The pilot deliberately uses a small heterogeneous seed:
- Baumeister et al. (2017): display technology, procedural task, cognitive-load/performance differences.
- Yang et al. (2019): assembly task decomposed by subtask, stage, and complexity; AR decreases load in commissioning but can increase it in low-complexity joining.
- Atici-Ulusu et al. (2021): automotive assembly; EEG and NASA-TLX; AR-glasses comparison.
- Zhu et al. (2026): educational AR cognitive-load meta-analysis; pooled reduction but very high heterogeneity (I2=92.7%) and moderator effects.

This is a theory pilot, not the final systematic corpus analysis.

## Candidate claim poset
c0: AR can alter cognitive load in a specified task/context.
c1: AR reduces cognitive load in the observed context.
c2: AR reduces cognitive load across comparable procedural tasks.
c3: AR generally reduces cognitive load across AR use contexts.
c4: AR reduces cognitive load independently of task stage, device, population, feedback and intervention regime.

Order: c0 < c1 < c2 < c3 < c4 where each upward step increases scope/strength.

## Core obligations
O1 intervention/comparator identity
O2 cognitive-load construct/measurement compatibility
O3 task compatibility
O4 task-stage/complexity compatibility
O5 device/display compatibility
O6 population compatibility
O7 environment compatibility
O8 validation-design compatibility
O9 evidence across the boundary being generalized
O10 heterogeneity/condition-dependence adequately resolved

## Pilot entitlement result
The seed evidence supports c0 strongly: AR can alter cognitive load, and the direction is condition dependent.
The seed supports localized c1 claims in several contexts.
The seed does not justify unconditional promotion to c3/c4. Yang et al. supplies an internal counterexample to a context-free reduction claim because direction changes by assembly subtask/complexity. Baumeister et al. identifies display/FOV as a load-relevant condition. The educational meta-analysis reports a pooled reduction but extreme heterogeneity and significant moderation by intervention frequency and feedback form. Therefore the strongest common claim is conditional rather than universal.

Pilot frontier:
F(S) contains localized/conditional claims, not the universal reduction claim.

## Minimal obstruction candidate
For the broad claim "AR generally reduces cognitive load across contexts", the principal blocking set is:
{cross-context evidence alignment, task/stage compatibility, device/display compatibility, measurement semantics, unresolved heterogeneity}.

The final minimum hitting set must be computed after full pilot extraction; this file records the theory-level pilot result only.

## Apparent contradiction decomposition
The seed contains both cognitive-load reductions and increases. Conventional synthesis can label this mixed evidence/heterogeneity. EET adds a different question: do opposite directions instantiate the same claim object?
Yang et al. shows that opposite directions can occur inside one research program after the task is decomposed. The appropriate state is therefore CONDITION_SPLIT rather than automatic SAME_CLAIM_CONFLICT.

## Comparison with alternatives

| Method | Native output on this pilot | What it misses relative to EET |
|---|---|---|
| Taxonomy/counting | studies by device/domain/task/metric | does not state maximum licensed claim |
| Meta-analysis | pooled effect + heterogeneity/moderators when effects are commensurable | does not by itself define a cross-domain claim-strength order or exact promotion obligations |
| Evidence-gap map | dense/sparse evidence cells | sparse cell is not necessarily a missing obligation blocking a claim |
| Quality score | stronger/weaker studies | study quality alone does not determine scope of an entitled claim |
| Generic VOI | value of reducing decision uncertainty / collecting data | utility is not specifically movement/correction of a scientific claim-entitlement frontier |
| EET | licensed claim region/frontier + blocking obligations + condition split + stability target | added complexity; usefulness must be validated quantitatively |

## Falsification criteria
Do not scale EET if, after full pilot extraction:
1. EET yields the same actionable conclusions as the simpler baselines;
2. claim ordering cannot be specified without arbitrary choices;
3. obligation definitions are unstable under reasonable perturbations;
4. frontier states cannot be reproduced from frozen evidence;
5. minimal obstructions are not more actionable than ordinary gap statements;
6. EET complexity is not justified by measurable information gain.

## Required quantitative pilot next
1. Fully extract 15–30 cognitive-load/procedural AR studies.
2. Freeze claim vocabulary and obligations before computing results.
3. Compute baseline outputs and EET outputs on exactly the same studies.
4. Measure claim downgrades, condition-split resolution, obstruction specificity, stability under perturbation, and actionable-next-study agreement/disagreement.
5. Ablate order, obligation, stability, and obstruction components.
6. Decide GO / MODIFY / STOP before applying EET to the complete corpus.

## Preliminary decision
GO TO QUANTITATIVE PILOT, NOT YET GO TO FULL CORPUS.

The small seed already demonstrates the phenomenon EET is designed to capture: evidence can support strong local claims while failing to license a broad universal claim, and apparently conflicting directions can become condition splits after claim normalization. This is promising but is not yet proof that EET outperforms existing synthesis methods.
