# Run 58 — TA-01 Assisted Screening and Human-Verification Protocol

## Purpose
Begin the genuine title/abstract stage without representing automated assistance as an independent human reviewer.

## Frozen unit
TA-01 is the first 250-record work unit from the immutable 7,728-record PubMed title/abstract set generated in Run 55.

## Decision states
Every record must end the primary pass in exactly one state: `include`, `exclude`, or `uncertain`. Exclusions require a controlled code from `protocol/SCREENING_CODES.csv`. Uncertain records advance.

## Permitted assistance
Software/AI may normalize metadata, display the frozen eligibility criteria, flag missing abstracts, identify exact controlled-code candidates, and produce a nonbinding recommendation with rationale. It may not be recorded as an independent human screener and may not silently exclude a record.

## Human verification fields
For each record preserve:
- PMID / DOI and immutable screening ordinal;
- title and abstract used for the decision;
- assisted recommendation, confidence and rationale, if used;
- primary human decision;
- controlled reason code;
- primary screener identity;
- timestamp and evidence note;
- decision version;
- second-verification state;
- adjudication state.

## Fail-closed rules
1. Missing or ambiguous evidence => `uncertain`.
2. Keyword absence alone is never an exclusion reason.
3. Automated recommendation never overwrites a human decision.
4. Corrections create a new version rather than deleting the earlier decision.
5. TA completion is not asserted until all 250 TA-01 rows have valid primary decisions.
6. Independent verification is a later genuine reviewer pass and is never simulated by the same model/workflow.

## Progression
TA-01 complete -> TA-02 ... TA-31 -> full text -> study families -> citation chasing -> independent verification/adjudication -> final corpus gate -> checksum freeze -> PRISMA -> NEXT-06..NEXT-19 final reruns.
