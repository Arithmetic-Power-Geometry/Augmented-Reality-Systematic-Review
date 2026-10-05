# Run 67 — TA-02 Exclusion-Candidate Rescue Audit

## Scope
All **41** Run 66 `EXCLUDE_CANDIDATE` records were inspected for terminology collisions and missed AR/MR/XR evidence. This is a safety audit, not an official reviewer-decision ledger.

## Rescue finding
| Ordinal | PMID | Audit disposition | Evidence |
|---:|---:|---|---|
| 497 | 42819441 | ADVANCE / UNCERTAIN | Primary cross-sectional XR education study; abstract explicitly states that the work guided development of an **AR-based shoulder dystocia training module**. AR separability/materiality must be assessed by the genuine reviewer rather than auto-excluded. |

The remaining **40/41** records are retained as `LIKELY_E_NOT_AR_PENDING_PRIMARY_REVIEW`. Their abstracts overwhelmingly use unrelated meanings of “AR” such as androgen/adrenergic receptor, acid resistance, autoradiography, argon, or other biomedical/chemical abbreviations.

## Important false hit resolved
Ordinal 473 contains the English word “augments” and beta-AR terminology, but it is a cardiac gene-transfer study and contains no augmented-reality evidence. It therefore remains a likely non-AR candidate.

## Integrity consequence
- Rescued / advance-uncertain: **1**
- Likely non-AR pending genuine primary review: **40**
- Official exclusions written by automation: **0**

## Rule implication
The assistance vocabulary should include **Extended Reality/XR as a rescue trigger**, but XR should not automatically establish inclusion because the frozen scope requires AR to be separable or materially necessary.
