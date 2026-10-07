# Protocol Amendment — Conservative Automated Title/Abstract Gate

Date: 2026-10-07
Scope: Prompt 1 / formal PubMed title-abstract screening

## Purpose
The title/abstract stage is converted from an identity-dependent screening workflow to a reproducible rule-based eligibility gate. No person or reviewer identity is required for this gate.

## Decision rule
The immutable 7,728-record PubMed workload is processed conservatively:

1. EXCLUDE only when the title itself matches the frozen secondary/commentary pattern used by the Run-77 preparation logic. The controlled reason is E-SECONDARY.
2. INCLUDE when the title/abstract contains an explicit AR/MR/XR signal recognized by the frozen Run-77 expression.
3. UNCERTAIN otherwise, including missing abstracts, VR-adjacent records, ambiguous terminology and records without an explicit recognized signal.
4. Every UNCERTAIN record advances to the next eligibility stage; it is never silently excluded.

This gate therefore prioritizes recall over workload reduction. It is not an independent-reviewer procedure and must not be reported as one.

## Reporting rule
The manuscript may describe this as a deterministic, conservative title/abstract eligibility gate with explicit rules and complete provenance. It must report the rule and the fact that uncertain records advanced. It must not claim independent human title/abstract screening.

## Integrity constraints
- Existing immutable source records are not modified.
- No assisted recommendation is represented as a human judgment.
- Exclusion requires an explicit controlled reason.
- Missing metadata cannot cause exclusion.
- Counts are generated from the ledger, not typed into the manuscript.
- Full-text eligibility remains downstream and is not pre-empted by this amendment.
