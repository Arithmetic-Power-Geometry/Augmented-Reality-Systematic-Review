# Run 71 — TA-03 Include-Candidate Risk Audit and Verification

## Executed audit
All **238** TA-03 assisted include candidates were audited.

| Audit state | Records |
|---|---:|
| LIKELY_ADVANCE_PENDING_PRIMARY_REVIEW | 164 |
| PRIORITY_VERIFY | 74 |
| Official primary decisions written | 0 |
| Total | 238 |

The 74 priority records carry 80 nonexclusive flags: 55 context-only-risk, 18 secondary/commentary-title flags and 7 missing-abstract flags. Audit SHA-256: `3a8afe386b51d24a823b08bc5326526f5525d4e4ae0b65d173a2de7d74e411cd`.

## Record-level verification structure
The 74 records were then inspected as a reviewer-priority set.

- **18** carry explicit secondary/commentary/review title signals and therefore receive a likely-secondary confirmation prompt, not an automatic exclusion.
- **6** additional records have missing abstracts without a secondary-title signal and therefore advance for authoritative-report verification.
- **5** nonsecondary context-flagged records have explicit AR/MR terminology in the title (ordinals 521, 538, 541, 583, 611) and are promoted to likely-advance confirmation.
- **45** remaining context-flagged records stay priority-review cases because title/abstract context must determine whether AR is implemented/material or merely an application/future mention.

One seventh missing-abstract record (ordinal 733) also has a secondary/correction title signal and is counted in the 18 secondary-priority records above.

## Integrity rule
These categories order genuine review. They do not replace it. Missing metadata never causes exclusion, and secondary-title signals must be confirmed against the report before a final reason code is recorded.
