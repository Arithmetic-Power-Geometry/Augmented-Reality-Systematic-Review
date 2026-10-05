# Run 61 — TA-01 Exclusion-Candidate Verification Audit

## Scope
Manual evidence audit of the 39 `EXCLUDE_CANDIDATE` records produced by Run 60. This is a **verification queue**, not an official primary-reviewer decision ledger.

## Outcome
The assisted rule produced several false-negative candidates because hyphenated `mixed-reality` and contextual MR language were not fully captured.

| Ordinal | PMID | Audit disposition | Evidence |
|---:|---:|---|---|
| 114 | 21674362 | ADVANCE / UNCERTAIN | Abstract explicitly reports testing in “mixed-reality environments”; AR-separability/materiality requires reviewer assessment. |
| 132 | 21441182 | ADVANCE / UNCERTAIN | Patient-specific 3-D model guidance augments the clinician's anatomical view; modality may be image guidance rather than AR and requires reviewer assessment. |
| 135 | 21441185 | ADVANCE | Explicit mixed-reality environment for clinical breast-examination training. |
| 160 | 21335855 | ADVANCE | Explicit “mixed-reality approach” combining physical/virtual models and spatial tracking. |
| 219 | 20106745 | ADVANCE | Explicit mixed-reality visualization modalities evaluated with novice users. |
| 244 | 19592738 | ADVANCE | Explicit interactive mixed-reality/blended-reality environment. |
| 245 | 19544967 | ADVANCE | Explicit immersive mixed-reality learning environment. |

The other **32/39** records are retained as `LIKELY_E_NOT_AR_PENDING_PRIMARY_REVIEW`: their titles/abstracts concern unrelated meanings of AR (adrenergic/androgen receptors, antigen retrieval, acid resistance, chemical notation, automatic registration, etc.) or domains without evidence that augmented/mixed reality is the principal or separable setting.

## Integrity consequence
No official `primary_decision` was written. The audit therefore identifies **7 records that must not be auto-excluded** and 32 records that can be prioritized for rapid human confirmation. This demonstrates why the Run 60 triage cannot replace screening.

## Rule correction
Future assisted triage must recognize `mixed-reality`, `blended reality`, and contextual mixed-reality-environment language before proposing exclusion.
