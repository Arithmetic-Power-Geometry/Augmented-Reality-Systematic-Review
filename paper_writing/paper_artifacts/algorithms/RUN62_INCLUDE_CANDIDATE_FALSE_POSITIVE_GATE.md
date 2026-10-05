# Run 62 — Include-Candidate False-Positive Risk Gate

Input: the 211 TA-01 records labelled `INCLUDE_CANDIDATE` in Run 60.

1. Preserve every original record and assisted state.
2. Flag titles containing review/commentary/editorial/perspective/overview signals.
3. Flag records with missing abstracts.
4. Flag cases where explicit AR/MR terminology appears only in the abstract together with future/potential/contextual language.
5. Flag VR-only records if no explicit AR/MR/blended-reality term exists.
6. Assign any flagged record to `PRIORITY_VERIFY`.
7. Assign all others to `LIKELY_ADVANCE_PENDING_PRIMARY_REVIEW`.
8. Never populate the official primary-decision field.
9. Report overlapping risk flags separately from unique record states.

Invariant: this gate prioritizes human screening; it does not replace it.
