# Run 77 — Human Screening Handoff Algorithm

1. Present each record with title, abstract, identifiers and nonbinding machine prompt.
2. A genuine reviewer records INCLUDE, EXCLUDE or UNCERTAIN.
3. For EXCLUDE, record one frozen controlled reason code.
4. Record the reviewer's real identity/label and decision timestamp.
5. Never copy the machine prompt into the primary-decision field automatically.
6. Advance UNCERTAIN records to the next eligibility stage.
7. Run `validate_genuine_screening_ledger.py`; fail if any of 7,728 records lacks a valid decision or reviewer attribution.
8. Preserve the completed ledger checksum.
9. Start full-text retrieval/screening only after the validated title/abstract ledger is complete.
10. Apply genuine independent verification and adjudication as specified by the frozen protocol.
