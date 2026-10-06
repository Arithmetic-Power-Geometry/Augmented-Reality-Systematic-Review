# Reviewer-Driven Revision Roadmap — Stages 1–5

This file preserves every substantive reviewer suggestion and assigns it to the research chronology. Final manuscript rewriting is intentionally last.

## Stage 1 — Complete corpus
Search execution/provenance; source merge; cross-source deduplication; genuine title/abstract screening; full-text eligibility; exclusion reasons; study-family resolution; backward/forward citation chasing.

**Exit:** frozen selection corpus is possible.

## Stage 2 — Validate corpus and coding
Independent verification; disagreements/adjudication; eligibility agreement; P_i schema validation and per-dimension agreement; C0-C3 agreement; T0-T5 coding reliability; R0-R8 coding reliability.

**Exit:** independently validated frozen corpus and codebook.

## Stage 3 — Evidence and quality analysis
Final P_i extraction; C0-C3 comparability; T0-T5 transfer states; R0-R8 reproducibility; risk-of-bias/study-quality appraisal differentiated by study type; populated Evidence Cube.

**Stage-3 implementation specification:** For each canonical study extract P_i=(D,T,H,S,A,M,E,U,R); generate pairwise C0-C3 comparability records; claim-level T0-T5 transfer records; component-derived R0-R8 reproducibility records; classify observable study design before appraisal; apply design-appropriate domain-level study appraisal rather than one universal numeric score; populate technique × environment × device × user × metric × domain Evidence Cube cells; preserve explicit missingness and evidence notes; compute final distributions only after Stages 1 and 2 pass. Sparse cube cells are observations, not automatic gaps. Pilot outputs cannot satisfy the final gate.\n\n**Exit:** primary evidence matrices frozen.

## Stage 4 — Higher-level synthesis
Failure regimes; contradictions after condition normalization; persistent gaps; closest-prior-work checks; verified-opportunity gate; domain analysis; temporal analysis; database/coder/threshold/unresolved-field/study-family sensitivity analyses.

**Exit:** all RQ-level findings and robustness checks frozen.

## Stage 5 — Final evidence artifacts and manuscript
Real PRISMA flow; data-rich figures; final result tables; explicit RQ1-RQ13 answers; revise related-framework comparison; replace prospective language; distinguish background references from included primary studies; rewrite Results/Discussion/Abstract/Conclusion; reduce project-management material; bibliographic audit; final IEEE preflight.

## Reviewer-suggestion mapping
- Genre/title ambiguity -> Stage 5 after completed evidence.
- Abstract lacks completed-review outcomes -> Stage 5.
- Novelty vs named frameworks insufficient -> Stages 3–5.
- Prior-review landscape too descriptive -> Stage 4/5 coded comparison.
- RQ1–RQ13 unanswered -> Stage 4/5.
- P_i under-validated -> Stage 2/3.
- C0–C3 reliability missing -> Stage 2/3.
- T0–T5 empirical justification -> Stage 2/3.
- Gap-promotion terminal state untested -> Stage 4.
- Evidence Cube unpopulated -> Stage 3.
- Missing databases -> Stage 1.
- Search strings not fully auditable -> Stage 1.
- Screening incomplete -> Stage 1.
- PRISMA missing -> Stage 5, generated only after Stages 1–4.
- 16-study pilot insufficient -> Stages 2–4 on final corpus.
- Narrative synthesis not corpus-derived -> Stage 4/5.
- R0–R8 lacks distribution -> Stage 3.
- Citation-range coverage feels mechanical -> Stage 5.
- Experimental-design scope overextended -> Stage 5; retain only if validated.
- Discussion prospective -> Stage 5.
- Limitations currently describe incompleteness -> resolve in Stages 1–4.
- Software stronger than evidence -> resolve by completing Stages 1–4.
- Release checklist too project-management-like -> move to repository/supplement in Stage 5.
- Figures too schematic -> Stage 5 data-rich replacements.
- Tables too framework-heavy -> Stage 5 results-table rebalance.
- Bibliography needs role separation/audit -> Stages 1 and 5.
- Risk-of-bias missing -> Stage 3.
- Inter-rater reliability missing -> Stage 2.
- Sensitivity analysis weak -> Stage 4.
- Conclusion must be empirical -> Stage 5.

## Non-negotiable chronology
Concept/framework -> software/workflow -> Stage 1 corpus -> Stage 2 validation -> Stage 3 evidence analysis -> Stage 4 higher-level synthesis -> Stage 5 final paper.
