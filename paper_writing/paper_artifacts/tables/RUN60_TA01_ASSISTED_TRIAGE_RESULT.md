# Run 60 — TA-01 Assisted Triage Result

TA-01 contains 250 immutable PubMed records recovered from the verified Run 54/55 screening-batch artifact.

| Assisted state | Count | Interpretation |
|---|---:|---|
| INCLUDE_CANDIDATE | 211 | Explicit or contextually strong augmented-/mixed-reality signal; still requires primary reviewer decision |
| EXCLUDE_CANDIDATE | 39 | No explicit AR/MR signal detected by the reproducible triage rule; exclusion is **not** final until manually verified |
| Genuine primary decisions | 0 | No assisted recommendation is counted as a reviewer decision |
| Total | 250 | TA-01 cardinality check |

The assisted ledger SHA-256 generated in the local verification run was `45fcdb4a03ff17b2c6bee6c56e1535e18a67a7d1716e706b9b639f2ceffe859c`.

## Interpretation
This run begins work on the actual screening records while preserving the PRISMA automation boundary. The triage is a prioritization/recommendation layer only. It is not an independent screener and cannot populate the primary-decision denominator.
