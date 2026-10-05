# Run 68 — TA-02 Include False-Positive Gate

For each assisted include candidate:

1. Flag a secondary/commentary title when review, commentary, editorial, perspective, overview or state-of-the-art language is present.
2. Flag records with no available abstract for authoritative-report verification.
3. Flag possible context-only AR when explicit AR/MR/XR terminology occurs in the abstract, not the title, together with future/potential language.
4. Assign `PRIORITY_VERIFY` when any flag is present; otherwise assign `LIKELY_ADVANCE_PENDING_PRIMARY_REVIEW`.
5. Treat all flags as prioritization signals only.
6. Never populate `primary_decision`, reason code, screener identity, independent-verification state or adjudication state.
7. Verify priority records record-by-record before constructing the final reviewer-ready TA-02 sheet.
