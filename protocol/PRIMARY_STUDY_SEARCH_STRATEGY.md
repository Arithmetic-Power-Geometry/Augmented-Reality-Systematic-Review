# Systematic Primary-Study Search Strategy — Frozen Protocol V1

**Stage:** NEXT-01  
**Target paper:** TVCG systematic review of augmented reality  
**Protocol freeze date:** 2026-10-05  
**Search end date:** 2026-10-05 inclusive  
**Status:** protocol frozen; searches not yet claimed executed

## Objective

Construct a reproducible, longitudinal primary-study corpus that can support the project's evidence representation `P_i=(D,T,H,S,A,M,E,U,R)`, Evidence Cube, C0–C3 comparability analysis, reproducibility audit, contradiction mining, and persistent-gap analysis.

## Scope rule

The core phenomenon is augmented reality (AR). Mixed reality (MR) and extended reality (XR) records are eligible only when the AR component is separable or the study contributes directly to an AR method, benchmark, device/sensor configuration, interaction/evaluation protocol, user population, or reproducibility question. Pure VR studies are excluded unless they contain a separable AR arm.

## Search sources

The primary bibliographic sources are:
1. IEEE Xplore;
2. ACM Digital Library;
3. Scopus;
4. Web of Science Core Collection;
5. ScienceDirect;
6. SpringerLink;
7. PubMed for health/clinical AR.

Supplementary discovery:
- backward citation chasing from included studies and influential reviews;
- forward citation chasing where supported;
- arXiv for supplementary preprint discovery only. When a peer-reviewed version is identified, the peer-reviewed report is the canonical record.

Database access limitations, export limits, and query adaptations must be recorded in the search registry. A source is never silently omitted.

## Search architecture

The search is deliberately split into a high-recall AR core and specialist concept blocks. This avoids requiring every eligible study to use modern terminology.

### AR core

`"augmented reality" OR "mixed reality" OR "extended reality" OR "AR system" OR "AR application"`

Acronyms `AR`, `MR`, and `XR` must not be used alone in broad full-text searches because of severe ambiguity.

### Specialist concept blocks

**B01 Tracking/localization/SLAM**  
`tracking OR localization OR localisation OR SLAM OR "simultaneous localization and mapping" OR registration OR calibration OR pose`

**B02 Perception/occlusion/scene understanding**  
`occlusion OR depth OR segmentation OR detection OR recognition OR "scene understanding" OR perception`

**B03 Interaction/multimodal/collaboration**  
`interaction OR gesture OR gaze OR haptic OR speech OR multimodal OR collaborative OR collaboration OR multiuser OR "multi-user"`

**B04 Networking/resources**  
`edge OR cloud OR networking OR latency OR bandwidth OR energy OR thermal OR resource`

**B05 Security/privacy/safety/governance**  
`security OR privacy OR safety OR governance OR attack OR adversarial OR authentication`

**B06 Human factors/accessibility/UX**  
`usability OR "user experience" OR cognitive OR workload OR accessibility OR disability OR inclusive OR ergonomics OR presence`

**B07 Adaptive/intelligent/generative AR**  
`adaptive OR context-aware OR intelligent OR agent OR "large language model" OR LLM OR generative OR multimodal OR transformer`

**B08 Digital twin/cyber-physical**  
`"digital twin" OR "cyber-physical" OR "cyber physical"`

**B09 Education/training**  
`education OR learning OR teaching OR training`

**B10 Health/clinical**  
`health OR healthcare OR clinical OR medical OR surgery OR rehabilitation OR patient`

**B11 Industrial/maintenance/assembly**  
`industrial OR manufacturing OR maintenance OR assembly OR inspection OR warehouse OR logistics`

**B12 Evidence/benchmark/reproducibility**  
`dataset OR benchmark OR metric OR evaluation OR experiment OR reproducibility OR replication OR code OR "open source"`

## Query construction

For each source, run:
- Q00 = AR core alone for broad coverage where the source/export volume permits;
- Q01–Q12 = AR core AND each specialist block.

Database-specific syntax may be adapted only for field names, phrase syntax, wildcard syntax, or query-length restrictions. The semantic terms must remain equivalent. Every executed query must be preserved verbatim in `evidence/search/search_registry.csv`.

## Time and language

- Earliest date: no lower bound; foundational AR literature is eligible.
- Latest publication/search date: 2026-10-05.
- Search language: English search terms.
- Study language: English full text required for the coded primary-study corpus. Non-English records discovered during searching are retained in the screening ledger and excluded with the explicit reason `E-LANGUAGE`; this limitation must be reported.

## Inclusion criteria

Include a record when all applicable conditions hold:
- I1: it is a primary empirical, experimental, technical, methodological, system, dataset, benchmark, or user study;
- I2: AR is the principal setting, a separable experimental arm, or materially necessary to the contribution;
- I3: it provides extractable evidence for at least one project dimension (technology, hardware, sensing, algorithm/method, metric/evaluation, environment, user/task, dataset/benchmark, result/limitation, or reproducibility);
- I4: sufficient methodological information is available to code the relevant evidence;
- I5: for duplicate reports, the record is the canonical or materially extended report.

## Exclusion codes

- E-NOT-AR: no separable/material AR contribution.
- E-VR-ONLY: pure VR without separable AR evidence.
- E-SECONDARY: review, survey, meta-analysis, editorial or perspective (retained in the review-of-reviews layer where relevant).
- E-NONRESEARCH: news, abstract-only announcement, poster summary without extractable method, commercial page, tutorial or commentary.
- E-DUPLICATE: bibliographic duplicate.
- E-COMPANION: same underlying study with no materially additional evidence; linked to canonical report.
- E-INSUFFICIENT: insufficient methodological information for extraction.
- E-LANGUAGE: full text not available in English.
- E-OUTSIDE-DATE: publication after frozen search end date.

Exclusion is based on scope/method evidence, never on whether the result supports a desired hypothesis.

## Duplicate and companion-report resolution

Deduplicate in this order:
1. normalized DOI exact match;
2. PubMed ID / other stable identifier exact match;
3. normalized title exact match;
4. fuzzy title + first author + year candidate, followed by manual verification.

Preprint/conference/journal versions are not blindly counted as independent studies. Reports describing the same experiment receive a `study_family_id`. The most complete peer-reviewed report becomes canonical; companion reports are retained only when they add materially distinct datasets, experiments, populations, methods, or outcomes. Evidence provenance retains the source report for each extracted datum.

## Screening procedure

Two-stage screening:
1. title/abstract;
2. full text.

Each record receives `include`, `exclude`, or `uncertain`, plus a controlled reason. Uncertain records advance to the next stage. Screening decisions are never overwritten; corrections are versioned.

For the final corpus, a second independent verification pass is required for all included studies and for a stratified sample of exclusions. Disagreements are resolved against the frozen eligibility rules and recorded in an adjudication field. Inter-rater agreement will be reported if a genuine second screener is available; it will not be fabricated or simulated by an AI reviewer.

## Search saturation and stopping rule

Searching stops only after:
1. all registered database/source queries are executed or an access limitation is explicitly logged;
2. deduplication and both screening stages are complete;
3. backward/forward snowballing of the designated seed set is processed;
4. newly discovered eligible records from the final snowballing iteration no longer introduce unsearched citation branches within the frozen date window;
5. the final search registry, screening ledger, and corpus checksum are frozen.

No target number of included studies is used as a stopping criterion.

## Evidence extraction

Included studies are coded to bibliographic identity plus:
`D,T,H,S,A,M,E,U,R` = domain, AR technology, hardware, sensing, algorithm/method, metrics/evaluation, environment, users, reproducibility.

Additional fields include task, dataset, benchmark, baseline, protocol, statistics, reported results, limitations, code, data, model/checkpoint, configuration, hardware specification, seeds, evaluator, raw outputs, and threats to validity.

## Audit trail

Every search execution records:
- source;
- query ID;
- exact executed query;
- execution date;
- coverage dates;
- filters;
- raw result count;
- exported count;
- export filename/checksum;
- access limitation;
- operator/tool;
- notes.

Raw exports are immutable. Normalization, deduplication, and screening operate on derived copies.

## Anti-bias rules

- No study is excluded because its result is negative, null, contradictory, or inconvenient.
- Empty cells are not automatically gaps.
- Review-reported gaps remain distinct from gaps computed from the primary corpus.
- Reported performance remains distinct from reproduced performance.
- Search terms may be expanded only through a versioned protocol amendment; post hoc additions cannot silently alter V1.
- Any amendment must state why it was needed and rerun affected searches.

## NEXT-01 pass condition

NEXT-01 passes only when:
- this protocol is committed;
- a machine-readable search registry template is committed;
- exclusion codes and duplicate rules are frozen;
- a strict reviewer audit contains no unresolved CRITICAL or HIGH issue.

Actual database searching begins at NEXT-02.
