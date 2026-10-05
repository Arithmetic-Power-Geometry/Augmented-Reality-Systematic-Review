# Run 63 — TA-01 Priority-Verification Findings

## Scope
The 40 `PRIORITY_VERIFY` records from Run 62 were isolated for record-level primary-review preparation. These findings remain **recommendations**, not official reviewer decisions.

## Highest-confidence exclusions to confirm first
| Ordinal | PMID | Recommended code | Rationale |
|---:|---:|---|---|
| 3 | 11486208 | E-SECONDARY | Review of pediatric video-assisted cardiothoracic surgery; AR appears only as a future development. |
| 17 | 10173059 | E-VR-ONLY / E-NOT-AR | Work is principally a virtual operating-room/VR prototype; AR is described as a future environment rather than the evaluated system. |
| 67 | 22806676 | E-NOT-AR | Monocular SLAM/landmark paper; AR occurs as an application context/reference venue rather than the principal evaluated setting. |
| 220 | 23616830 | E-SECONDARY | Explorative Web 2.0 trends paper discussing AR as one of several future clinical-informatics trends. |
| 227 | 19964961 | E-NOT-AR | Avatar body-monitoring system is evaluated for VR; AR is listed only as a possible application. |
| 237 | 19691977 | E-SECONDARY | Explicit commentary on another mixed-reality study. |

## Strong advance candidates
Records such as ordinals **11, 21, 22, 25, 29, 71, 174, 189, 190, and 234** describe an implemented/evaluated AR system, simulator, overlay, navigation or interface and therefore should advance unless a different frozen exclusion criterion applies.

## Missing-abstract queue
Seven records were flagged because PubMed supplied no abstract. Missing abstract alone is **not** an exclusion reason. Their title/identifier must be checked against the full report or authoritative metadata before a primary decision.

## Context-only queue
Thirty-two records were flagged by a deliberately sensitive rule because AR appeared with future/potential language. Record-level inspection shows that this flag is intentionally over-inclusive: several are genuine evaluated AR systems. It is therefore useful for prioritization but unsuitable as an automatic exclusion rule.

## Methodological result
The Run 62 flag `AR_MENTION_MAY_BE_CONTEXT_ONLY` has high sensitivity but insufficient specificity for exclusion. It should remain a review-priority flag only. The six records above are the clearest likely exclusions for rapid genuine confirmation; ambiguous cases advance.
