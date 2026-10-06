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

### Stage-4 implementation specification

**Condition-normalized contradiction test.** Candidate opposing claims are first aligned on task, population/user, device, sensing stack, environment, metric semantics, comparator, protocol and deployment maturity. C0 pairs cannot establish contradiction. C1 pairs may define contextual tension only. C2/C3 pairs may enter a contradiction test when outcome direction is genuinely opposed after normalization. Each cluster ends as VERIFIED_CONTRADICTION, CONDITION_DEPENDENT, INSUFFICIENT_EVIDENCE, or NOT_COMPARABLE.

**Failure-regime extraction.** For each supported degradation/failure claim, record method, triggering condition, baseline condition, outcome/metric, direction/magnitude when reported, evidence provenance, comparability level and replication status. A failure regime requires a condition-linked degradation signal, not merely a study limitation.

**Persistent-gap promotion.** A sparse Evidence Cube cell is only a candidate. Promotion requires: corpus persistence; not explained by scope/search limitations; contradiction check; reproducibility/evidence-quality check; closest-prior-work search; and an experimentally actionable missing comparison or condition. Terminal states are VERIFIED_OPPORTUNITY, PERSISTENT_BUT_NOT_ACTIONABLE, EXPLAINED_BY_EXISTING_WORK, EVIDENCE_TOO_WEAK, or UNRESOLVED.

**Closest-prior-work gate.** Search the frozen included corpus, linked companion reports, review-of-reviews library and citation-chase additions for the same task × method × condition × outcome combination before any novelty/opportunity claim.

**Domain and temporal synthesis.** Report counts and normalized proportions by domain, technology, hardware/sensing, study design, evidence maturity and year/era. Interpret temporal change only when database coverage and inclusion policy are stable enough for the comparison.

**Sensitivity analyses.** Recompute central findings under: (S1) source/database inclusion sets; (S2) Reviewer-A vs Reviewer-B pre-adjudication coding; (S3) alternative defensible C/T/R boundary thresholds; (S4) unresolved-field best/worst/complete-case handling; (S5) report-level versus canonical study-family counting; (S6) exclusion of high-concern study-quality domains; and (S7) exclusion of weakly comparable C0/C1 evidence where a claim depends on direct comparison.

**Robustness rule.** A manuscript conclusion is robust only if its direction/interpretation survives the prespecified relevant sensitivity analyses or the sensitivity dependence is disclosed explicitly.

**Final outputs.** Frozen contradiction/failure ledger; gap-promotion ledger; closest-prior-work ledger; domain/temporal tables; sensitivity matrix; RQ1–RQ13 answer ledger; provenance/checksums.

**Pilot restriction.** Existing 16-study contradiction and gap tables remain method-validation artifacts only. They contain candidate tensions and no VERIFIED OPPORTUNITY; they cannot be converted into field-wide prevalence or novelty claims.

**Exit:** all RQ-level findings and robustness checks frozen.

## Stage 5 — Final evidence artifacts and manuscript
Real PRISMA flow; data-rich figures; final result tables; explicit RQ1-RQ13 answers; revise related-framework comparison; replace prospective language; distinguish background references from included primary studies; rewrite Results/Discussion/Abstract/Conclusion; reduce project-management material; bibliographic audit; final IEEE preflight.

### Stage-5 implementation specification

**Paper identity.** Paper 1 is a completed systematic review and evidence-synthesis paper. It does not require a live-user study, new participant recruitment, or a new human-subject experiment. Any proposed experiment/new adaptive method is future work or a separate paper and is not used to validate Paper-1 review conclusions.

**PRISMA.** Derive the flow only from frozen search, deduplication, screening, full-text, study-family and citation-chasing ledgers. No hand-entered or estimated count is authoritative.

**RQ closure.** RQ1–RQ13 must each resolve through the Stage-4 RQ answer ledger as ANSWERED, PARTIALLY_ANSWERED, or INSUFFICIENT_EVIDENCE, with denominator, evidence references, sensitivity status and limitations.

**Results-first figures.** Replace schematic/project-management graphics where possible with corpus-derived PRISMA, temporal evolution, domain/technology distribution, Evidence Cube occupancy, C0–C3 comparability, R0–R8 reproducibility, study-quality, contradiction/failure-regime, and persistent-gap/robustness figures.

**Results-first tables.** Prioritize corpus characteristics, design/quality appraisal, comparability causes, reproducibility distribution, domain/user/environment evidence, contradictions/failure regimes, sensitivity analyses, verified opportunities and RQ answers. Methodological framework tables are retained only when needed to interpret results.

**Manuscript rewrite.** Abstract reports completed-review methods and empirical findings. Results contain only frozen-corpus outputs. Discussion interprets those outputs against prior reviews/frameworks. Conclusion states empirical findings and limitations, not prospective promises.

**Bibliography-role audit.** Separate background/method references from included primary-study evidence. Every field-level synthesis claim resolves to included-study IDs rather than citation-range decoration.

**No-live-user rule.** NEXT-20–NEXT-29 experimental work is outside Paper 1. Remove any implication that E001/E002/E003, live-user validation, participant recruitment, or a novel adaptive method is required for acceptance of the systematic review. The review may identify experimentally actionable future work without executing it.

**Final release gate.** Compile/preflight only after Stages 1–4 PASS. Verify PRISMA identities, all RQ answers, denominators, cross-references, figure/table citations, bibliography integrity, repository provenance, manuscript/repository separation, and absence of pilot denominators in final claims.

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
