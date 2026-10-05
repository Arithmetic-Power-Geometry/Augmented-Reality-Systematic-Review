# Run 62 — TA-01 Include-Candidate Risk Audit

The reproducible audit processed all **211** Run 60 `INCLUDE_CANDIDATE` records.

| Audit state | Count | Meaning |
|---|---:|---|
| LIKELY_ADVANCE_PENDING_PRIMARY_REVIEW | 171 | No predefined false-positive risk flag triggered; still not an official inclusion |
| PRIORITY_VERIFY | 40 | One or more false-positive/insufficient-evidence risk flags triggered |
| Total | 211 | Complete include-candidate audit |

## Risk flags
| Flag | Count |
|---|---:|
| AR_MENTION_MAY_BE_CONTEXT_ONLY | 32 |
| ABSTRACT_MISSING | 7 |
| SECONDARY_OR_COMMENTARY_TITLE | 4 |

Flags can overlap; therefore flag totals do not equal the 40 unique priority records.

## Interpretation
The audit does **not** convert the 171 records into official inclusions. It identifies the 40 records most likely to contain secondary literature, contextual/future-only AR mentions, or insufficient abstract evidence, allowing primary review to concentrate first on the highest-risk cases.

Together with Run 61, TA-01 now has two safety layers: seven false-negative exclusion candidates were rescued, and forty include candidates were prioritized for false-positive verification.
