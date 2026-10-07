# Evidence Qualification Pipeline (EQP)

## Purpose

This study uses a data-centric methodology in which evidence is qualified by explicit, reproducible gates rather than by the identity of a person performing a screening or coding action. The unit of authority is the versioned evidence record plus its provenance.

The pipeline is designed for heterogeneous augmented-reality literature, where apparently similar studies may differ in task, device, sensing, environment, user population, metric semantics, validation design or deployment maturity.

## 1. Record state

Each retrieved record is represented as

\[
q_i=(x_i,m_i,s_i,r_i,p_i)
\]

where x_i is the available bibliographic/text evidence, m_i is metadata completeness, s_i is the current eligibility state, r_i is the controlled reason state, and p_i is provenance.

Allowed eligibility states are ADVANCE, EXCLUDE and UNCERTAIN. UNCERTAIN always advances to the next evidence stage.

## 2. Conservative qualification gate

A record may be excluded at title/abstract level only when a frozen controlled rule is satisfied by observable record evidence. An ambiguous signal, missing abstract, mixed terminology or unresolved metadata cannot itself produce exclusion.

Thus the gate is asymmetric:

\[
G(q_i)=
\begin{cases}
EXCLUDE,&\text{if a frozen exclusion predicate is satisfied},\\
ADVANCE,&\text{if an explicit in-scope AR/MR/XR predicate is satisfied},\\
UNCERTAIN,&\text{otherwise}.
\end{cases}
\]

The operational advance set is ADVANCE union UNCERTAIN. This intentionally favors recall over early workload reduction.

## 3. Evidence vector

For each canonical eligible study, extract the structured vector

\[
P_i=(D,T,H,S,A,M,E,U,R)
\]

covering domain, task, hardware, sensing, algorithm/approach, metrics, environment, users and reproducibility evidence. Missing values remain explicit rather than being imputed.

## 4. Comparability gate C0-C3

Pairwise comparison is permitted only after the relevant evidence dimensions are aligned. C0 denotes non-comparable evidence; higher states represent increasing support for a direct comparative claim. A shared topic label is insufficient for comparability.

## 5. Transfer gate T0-T5

Transferability is evaluated separately from within-study validity. The transfer state records how far a claim can move across changes in device, environment, population, task, sensing stack, metric semantics and deployment maturity without changing the estimand.

## 6. Reproducibility state R0-R8

Reproducibility is component-derived rather than inferred from a repository link or open full text. The state is calculated from available specification, data, code/artifact, execution, regeneration, semantic-match and independent-evidence components defined in the frozen codebook.

## 7. Evidence Cube

Qualified studies populate a multidimensional Evidence Cube spanning technique × environment × device × user × metric × domain. Occupancy is descriptive. A sparse or empty cell is not called a research gap until it survives closest-prior-work and evidence-sufficiency tests.

## 8. Contradiction and failure qualification

Opposing claims are normalized on task, population, device, sensing stack, environment, metric semantics, comparator, protocol and deployment maturity before contradiction is considered. Candidate pairs terminate as NOT_COMPARABLE, INSUFFICIENT_EVIDENCE, CONDITION_DEPENDENT or VERIFIED_CONTRADICTION.

Failure regimes are condition-linked degradation states, not generic limitations.

## 9. Reliability without identity dependence

Reliability is established through reproducibility of the evidence transformation itself:

- provenance replay from immutable source records;
- rule-version hashes and deterministic regeneration;
- threshold/definition perturbation;
- unresolved-field sensitivity;
- leave-family-out and study-quality sensitivity;
- disagreement-state maps between baseline and perturbed classifications;
- claim-to-evidence traceability.

A conclusion is stable only when its interpretation survives the prespecified perturbations relevant to that claim. This replaces identity-based agreement as the principal reliability mechanism.

## 10. Corpus freeze

Final counts are generated only from completed ledgers. Corpus freeze records hashes of the source set, eligibility ledger, canonical-study ledger and extraction matrices. PRISMA accounting, prevalence estimates, Evidence Cube distributions, contradiction results and final conclusions are generated after freeze.

## Methodological novelty

EQP changes the unit of trust from *who classified a study* to *whether the classification can be regenerated from frozen evidence under explicit rules and whether the resulting scientific claim remains stable under controlled perturbation*. It therefore joins eligibility, comparability, transfer, reproducibility, contradiction qualification, failure regimes and sensitivity into one auditable evidence architecture for AR research.
