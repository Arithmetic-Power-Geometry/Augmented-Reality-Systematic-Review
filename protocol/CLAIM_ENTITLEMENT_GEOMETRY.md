# Claim-Entitlement Geometry (CEG)

## Core idea

The methodology does not classify evidence by the identity or type of the entity that processed it. It treats every literature record as an evidence object and every scientific conclusion as a claim that must earn a permitted scope.

The central question is:

> Given the observable evidence attached to a set of studies, what is the strongest claim that the evidence is entitled to support?

This reverses the usual review workflow. Instead of papers -> categories -> counts -> conclusions, CEG uses:

evidence objects -> claim obligations -> compatibility geometry -> support frontier -> perturbation survival -> entitled claim.

## 1. Evidence objects

For study i, define an evidence object

E_i = (D,T,H,S,A,M,V,U,R,Q)

where D=domain, T=task, H=hardware, S=sensing/data path, A=approach, M=measurement semantics, V=validation design, U=population/use context, R=reproducibility components, and Q=evidence quality/provenance.

Missing coordinates are retained as unknowns.

## 2. Claim objects

A candidate claim c is represented as

c = (theta, Omega, kappa)

where theta is the estimand/proposition, Omega is the domain over which the claim is intended to hold, and kappa is claim strength.

Examples of kappa are descriptive, comparative, superiority, transfer, contradiction, robustness and gap/opportunity.

## 3. Claim obligations

Every claim type induces an obligation set O(c). An obligation is an evidence condition that must be satisfied before the claim is promoted.

For example, a comparative superiority claim may require compatible task, comparator, metric semantics, population and validation conditions; a transfer claim additionally requires evidence across the boundary being crossed.

## 4. Compatibility geometry

For a set of evidence objects S and claim c, define a claim-relative compatibility vector

K_c(S) = (k_1,...,k_m),  k_j in {0,1,?}

where 1 means the j-th obligation is supported, 0 means contradicted/incompatible, and ? means unresolved.

Compatibility is claim-relative: the same two studies can be compatible for a descriptive claim and incompatible for a superiority claim.

## 5. Support frontier

Let C be the partially ordered set of candidate claims, ordered by strength/scope. Define

F(S) = max { c in C : O(c) is satisfied by S }.

F(S) is the Claim-Entitlement Frontier: the strongest non-dominated claim(s) supportable by the current evidence.

Evidence may therefore support a weaker claim while blocking a stronger one rather than being reduced to included/excluded.

## 6. Transfer distance

For a claim promoted in context Omega_0 and proposed for Omega_1, define boundary crossings over device, sensing, environment, task, population, metric and deployment coordinates. Transfer evidence is evaluated against those crossings. Transferability is therefore a distance from demonstrated support, not a narrative adjective.

## 7. Contradiction test

Two results are contradictory only if they target the same claim object after compatibility normalization. Otherwise the terminal state is one of:
- SAME_CLAIM_CONFLICT;
- CONDITION_SPLIT;
- ESTIMAND_SPLIT;
- INSUFFICIENT_OVERLAP;
- UNRESOLVED.

Thus disagreement becomes a geometric relation between claim domains rather than a count of opposite conclusions.

## 8. Gap test as missing claim support

An empty literature cell is not a gap. A gap exists only when:
1. a scientifically meaningful claim object c can be specified;
2. c lies beyond the current support frontier;
3. the missing obligation is identifiable;
4. closest prior evidence does not already satisfy it; and
5. a feasible observation/experiment could discharge the obligation.

The output is therefore a missing evidence obligation, not merely an under-populated topic.

## 9. Perturbation survival

Let P be a prespecified family of admissible perturbations to definitions, thresholds, unresolved fields, study-family choices and quality restrictions. For claim c define

rho(c) = |{p in P : c remains within F_p(S)}| / |P|.

rho is a claim-stability quantity. It does not measure agreement between entities; it measures survival of the scientific conclusion under legitimate analytic variation.

## 10. Evidence value of a new study

For a proposed study e, define its frontier gain

Delta(e|S) = d(F(S union {e}), F(S)),

where d measures how much the support frontier expands in claim strength or domain. This turns future-work selection into an evidence-acquisition problem: prefer experiments that discharge blocking obligations or expand the frontier, rather than merely filling sparse taxonomy cells.

## 11. Provenance closure

Every promoted claim stores:
- supporting evidence-object IDs;
- satisfied and unresolved obligations;
- compatibility state;
- perturbation-survival result;
- source/version hashes.

A claim without provenance closure cannot enter the final Results or Conclusion.

## Novel methodological proposition

CEG changes systematic synthesis from literature classification to claim authorization. Its primary output is not a taxonomy or paper count but a frontier separating claims currently supportable by the evidence from stronger claims that remain unsupported, together with the exact evidence obligations blocking promotion.
