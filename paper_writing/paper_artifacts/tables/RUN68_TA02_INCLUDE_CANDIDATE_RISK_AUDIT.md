# Run 68 — TA-02 Include-Candidate False-Positive Risk Audit

## Executed result
The complete set of **209** TA-02 `INCLUDE_CANDIDATE` records was audited using conservative false-positive risk flags.

| Audit state | Records |
|---|---:|
| LIKELY_ADVANCE_PENDING_PRIMARY_REVIEW | 166 |
| PRIORITY_VERIFY | 43 |
| Official primary inclusions/exclusions written | 0 |
| **Total** | **209** |

Risk flags within the 43 priority records:
- `AR_MENTION_MAY_BE_CONTEXT_ONLY`: **34**
- `ABSTRACT_MISSING`: **9**
- `SECONDARY_OR_COMMENTARY_TITLE`: **0**

The categories are mutually exclusive in this run, so 34 + 9 = 43.

Audit CSV SHA-256: `cff8450dddd114fc20ef7a4649bf6a0ac839201e521e9981513a8d850501581f`.

## Interpretation
The context-only flag is deliberately sensitive. Several flagged records are plainly AR-relevant from their titles and available evidence, so the flag must be used only to order verification effort. A missing abstract is never an exclusion criterion.

## Screening state after Runs 66–68
Across all 250 TA-02 records:
- 166 low-risk likely-advance prompts from the include side;
- 43 include-side priority-verification records;
- 1 exclusion-side record rescued as advance/uncertain;
- 40 likely non-AR records pending genuine primary review;
- **0 official primary decisions**.

These states prepare the human review workload; they are not PRISMA inclusion/exclusion counts.
