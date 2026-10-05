# Run 64 — TA-01 Reviewer-Ready Decision Sheet

## Purpose
Run 64 consolidates the complete 250-record TA-01 work unit into a single reviewer-facing decision sheet. It combines the immutable source record with Run 60 assistance, Run 61 rescue/non-AR audit, Run 62 false-positive risk flags, and Run 63 record-level priority findings.

## Review order
| Tier | Reviewer task | Records |
|---:|---|---:|
| 1 | Confirm six highest-confidence likely exclusions identified in Run 63 | 6 |
| 2 | Confirm remaining Run 61 likely non-AR candidates | 28 |
| 3 | Resolve Run 61 rescued records as advance/uncertain | 7 |
| 4 | Review remaining Run 62 priority-risk candidates | 34 |
| 6 | Confirm remaining likely-advance records | 175 |
| **Total** | | **250** |

Tier 5 is logically available for explicit Run 63 strong-advance exemplars, but those records also carry Run 62 priority flags and therefore remain in Tier 4 under the conservative ordering.

## Decision fields
The generated sheet contains blank fields for `primary_decision`, `primary_reason_code`, `primary_screener`, timestamp, evidence note, decision version, second-verification state and adjudication state.

## Valid primary states
- INCLUDE
- EXCLUDE with one controlled frozen reason code
- UNCERTAIN, which advances

No assisted recommendation is converted into a primary decision.

## Paper use
This sheet supplies the auditable transition from computational prioritization to genuine record screening. Final PRISMA counts will be derived from completed versioned decision ledgers, not from the reviewer prompts in this sheet.
