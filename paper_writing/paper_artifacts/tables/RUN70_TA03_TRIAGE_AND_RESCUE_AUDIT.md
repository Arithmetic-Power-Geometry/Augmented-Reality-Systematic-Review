# Run 70 — TA-03 Assisted Triage and Exclusion Rescue Audit

TA-03 (formal screening ordinals 501–750) was materialized from the frozen deterministic PubMed prescreen and contains exactly **250** records.

## Initial assisted triage
| State | Records |
|---|---:|
| INCLUDE_CANDIDATE | 238 |
| EXCLUDE_CANDIDATE | 12 |
| Official primary decisions | 0 |
| Total | 250 |

Assisted ledger SHA-256: `8bafbbd24e957a0771e93241719773d2c7b748f4ec136414ceca3ffe1e747edc`.

## Exclusion-side rescue audit
All 12 exclusion candidates were inspected. No record contains sufficient evidence of an implemented/separable augmented-reality study to warrant automatic rescue from the available title/abstract evidence.

Notable boundary cases:
- ordinal 571 is a narrative review covering extended-reality platforms and therefore remains a likely secondary exclusion;
- ordinals 660, 682 and 683 are VR-focused primary studies and remain likely `E-VR-ONLY` under the frozen AR scope unless a separable AR arm is established;
- ordinal 750 mentions augmented-reality surgical navigation only as a future development;
- ordinal 589 uses holographic/immersive visualization and requires genuine reviewer confirmation of whether it satisfies the frozen AR materiality criterion.

Therefore the machine-side audit writes **zero official exclusions**. The 12 records remain reviewer-confirmation cases, with ordinal 589 prioritized for scope verification.
