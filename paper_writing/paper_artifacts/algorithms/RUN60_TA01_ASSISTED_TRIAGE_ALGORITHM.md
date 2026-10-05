# Run 60 — TA-01 Assisted Triage Algorithm

**Input:** frozen TA-01 work unit, 250 records.

1. Preserve immutable ordinal, PMID, DOI, title and abstract.
2. Search title+abstract for explicit AR/MR signals: augmented reality, mixed reality, augmented-reality, head-mounted display, HoloLens, Magic Leap, optical/video see-through, or spatial computing.
3. If an explicit signal exists, assign `INCLUDE_CANDIDATE` with high assisted confidence.
4. If contextual augmented visualization/guidance terminology exists, assign `INCLUDE_CANDIDATE` with medium assisted confidence.
5. Otherwise assign `EXCLUDE_CANDIDATE` with the explicit warning that manual verification is required before exclusion.
6. Leave `primary_decision`, reviewer identity, controlled exclusion code, second-verification and adjudication fields blank.
7. Compute the assisted-ledger checksum.
8. Count no assisted state as a genuine title/abstract decision.

**Safety invariant:** assistance may prioritize review but cannot reduce the PRISMA screening denominator or simulate reviewer independence.
