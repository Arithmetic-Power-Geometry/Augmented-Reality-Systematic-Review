# Algorithm — Clinical AR Evidence Translation Gate

Input: clinical/medical AR study s and proposed claim c
Output: C0-C6, certainty flag, PROMOTE/QUALIFY/HOLD

1. Identify whether evidence is phantom/cadaver/simulation, trainee/professional, or patient-involved.
2. Identify clinical specialty, procedure and intended use.
3. Extract AR function: navigation, guidance, visualization, monitoring, telestration, training, rehabilitation, etc.
4. Separate technical accuracy from operator, workflow and patient outcomes.
5. Record registration/tracking method and error definition when navigation accuracy is used.
6. Record comparator and whether allocation is randomized/prospective/retrospective/single-arm.
7. Record sample size, site count and user expertise.
8. Record adverse events, failure modes, misleading overlays, drift and ergonomic/workflow burden.
9. Record follow-up and whether retention or patient recovery is actually measured.
10. Record evidence-certainty/risk-of-bias assessment when available.
11. Assign C0-C6 using demonstrated evidence rather than authors' clinical-readiness wording.
12. Do not promote simulator/training effects to patient outcomes.
13. Do not promote accuracy improvements to clinical effectiveness without outcome evidence.
14. Do not call a system field-ready from a small single-center feasibility study.
15. PROMOTE only at the claim level directly supported; otherwise QUALIFY or HOLD.
