# Algorithm — Secondary-Review Evidence Promotion Gate

Input: validated secondary review r
Output: POSITIONING, MODEL_REFINEMENT, PRIMARY_CORPUS_EXCLUDE

1. Verify complete bibliographic metadata and DOI.
2. Mark r as secondary evidence; never count it as a primary included study.
3. Extract only review-level facts needed for:
   a. closest-prior-work positioning;
   b. evidence-dimension refinement;
   c. candidate primary-study discovery.
4. Preserve population, modality, comparator, outcome and time-horizon conditions.
5. Do not transfer a pooled effect to another domain or AR configuration.
6. If r mixes VR/MR/AR, record whether AR evidence is separable.
7. Send cited primary reports to supplementary discovery, not automatic inclusion.
8. Final primary-corpus inclusion requires the frozen primary-study screening protocol.
