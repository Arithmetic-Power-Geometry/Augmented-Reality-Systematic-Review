# Algorithm — Reproducibility Evidence Classification and Claim Gate

Input: study s
Output: component flags, R-level descriptor, and allowed synthesis claims

1. Verify bibliographic identity and study-family membership.
2. Extract reporting completeness: participants/data, hardware/device, software/version, task/protocol, measures, analysis.
3. Record materials availability independently.
4. Record data availability and persistent identifier/license where present.
5. Record source/analysis code or executable artifact availability.
6. Record environment/dependency/hardware/configuration/seed provenance.
7. Record whether an independent execution is documented.
8. Record whether the published result itself was reproduced.
9. Record whether the empirical finding was directly or conceptually replicated.
10. Assign component flags; assign the highest defensible R descriptor without inferring missing lower components.
11. For cross-study synthesis, label every numerical value REPORTED or REPRODUCED.
12. Permit a replication claim only when the later study explicitly tests an earlier finding or the relationship is established by study-family/prior-work evidence.
13. Never convert unavailable artifacts into evidence of incorrectness.
14. Never convert code availability into independent reproducibility.

Output PROMOTE only claims supported at their stated evidence level; otherwise QUALIFY or HOLD.
