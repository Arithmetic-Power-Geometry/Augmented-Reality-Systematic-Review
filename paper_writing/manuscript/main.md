# Augmented Reality: A Systematic Review of Technologies, Algorithms, Benchmarks, Evaluation Methods, Research Gaps, and Future Directions

**Manuscript status:** Draft V0.2 — methods-first, pre-corpus-freeze
**Target venue:** IEEE Transactions on Visualization and Computer Graphics
**Claim boundary:** No final corpus size, PRISMA counts, prevalence, or corpus-derived result is asserted before NEXT-05 freeze.

## Abstract

Augmented reality (AR) research spans tracking and registration, perception, visualization, interaction, networking, intelligent adaptation, human factors, safety, privacy, accessibility, and application-specific evaluation. This breadth has produced substantial technical progress, but it also makes evidence difficult to compare: studies frequently differ in device, sensing stack, environment, task, user population, metric definition, benchmark, and reproducibility support. This systematic review develops an evidence-centered synthesis designed to distinguish technological progress from differences in experimental conditions. The review is organized around a multidimensional study representation covering domain, technology, hardware, sensing, algorithm or method, metrics and evaluation, environment, users, and reproducibility. It further separates direct, conditional, and invalid comparisons; distinguishes reported, observed, persistent, contradictory, reproducibility-limited, experimentally actionable, and verified research gaps; and treats study-family provenance and replication evidence as first-class review objects. Searches are specified across IEEE Xplore, ACM Digital Library, Scopus, Web of Science Core Collection, ScienceDirect, SpringerLink, and PubMed, supplemented by citation chasing. **PENDING_FORMAL_EXECUTION:** final retrieval, screening, inclusion, and synthesis results will be inserted only after the registered search corpus is frozen. The intended contribution is therefore not another broad taxonomy of AR, but an auditable map connecting methods to the conditions under which their evidence is valid and useful for future research.

**Keywords:** augmented reality; systematic review; tracking; interaction; evaluation; benchmarking; reproducibility; human factors; evidence synthesis

## I. Introduction

Augmented reality has developed from early systems concerned primarily with registration, display, and tracking into a broad research area that now intersects computer vision, human-computer interaction, visualization, robotics, networking, artificial intelligence, healthcare, education, and industrial systems. Foundational surveys established the central technical problems of combining real and virtual information, interactive operation, and spatial registration [Azuma1997Survey, Azuma2001Advances]. Later syntheses documented the expansion of AR technologies and interaction paradigms [Billinghurst2015Survey], while specialized reviews have examined collaborative AR [Sereno2022Collaborative], occlusion handling [Macedo2023Occlusion], medical head-mounted displays [Gsaxner2023HoloLensMedicine, Birlo2022OSTSurgery], tracking and SLAM [Sheng2024SLAMReview], industrial maintenance and assembly [Palmarini2018Maintenance, Wang2016Assembly], accessibility, education, security, intelligent AR, and other application-specific areas.

This expansion creates a methodological problem for evidence synthesis. Two papers may address nominally similar AR tasks while using different display classes, sensing configurations, registration assumptions, environments, participant populations, workloads, baselines, or metric definitions. A higher reported accuracy, lower task time, or improved usability score is therefore not necessarily evidence that one method is universally superior. The same difficulty applies to claims about field readiness: performance in a controlled laboratory study cannot automatically be generalized to an operational workplace, clinical setting, or long-term deployment.

A second problem is reproducibility. AR systems often combine hardware, calibration, software, datasets, interaction procedures, and environment-specific assumptions. Consequently, availability of a paper or even source code is not equivalent to independent executability, reproduction of a reported result, or replication of the underlying study. A recent scoping review of IEEE ISMAR and IEEE VR highlighted the limited visibility of replication work [Arefin2025Replication]. The present review therefore treats reproducibility and replication as graded evidence rather than binary labels.

A third problem concerns research gaps. Absence of publications in a particular combination of task, device, environment, user, and metric does not by itself establish a scientifically important gap. A useful gap should survive checks for prior art, comparability, contradictory evidence, reproducibility limitations, and experimental actionability. This review consequently distinguishes empty evidence cells from persistent and testable research opportunities.

The review is designed around this evidence problem rather than around breadth alone. Broad and longitudinal AR reviews already exist, and domain-specific reviews provide substantial prior taxonomic coverage. Accordingly, the contribution claimed here is not that AR has never been reviewed comprehensively. Instead, the review integrates technical, experimental, human, environmental, and reproducibility evidence into a common architecture intended to answer a practical question: **under what conditions should an AR result be believed, compared, transferred, reproduced, or used as the basis for new research?**

### A. Contributions

Subject to final corpus verification, this review makes five methodological contributions.

1. **Multidimensional evidence representation.** Each eligible primary study is represented by P_i=(D,T,H,S,A,M,E,U,R), covering domain, AR technology, hardware, sensing, algorithm/method, metrics/evaluation, environment, users, and reproducibility.
2. **Condition-aware comparability.** Reported results are interpreted through comparability levels rather than a universal leaderboard. Differences in task, dataset, hardware, environment, user population, protocol, and metric semantics can convert an apparently direct comparison into a conditional or invalid one.
3. **Evidence-cube synthesis.** Method evidence is examined across interacting dimensions including technique, environment, device, user, metric, and domain so that sparse cells are distinguished from meaningful persistent limitations.
4. **Reproducibility and study-family provenance.** Code, data, configuration, execution environment, reproduction, replication, and relationships among preprint, conference, and journal reports are retained explicitly.
5. **Gap-to-experiment gate.** Candidate gaps are promoted only when they remain meaningful after prior-art, contradiction, comparability, reproducibility, and feasibility checks. This prevents an empty literature cell from being presented as a new research problem.

These contributions are provisional until the formal corpus and closest-prior-work audit are frozen.

### B. Positioning Against Prior Reviews

The AR literature already contains substantial review coverage, so the present study is positioned against that prior synthesis rather than treating breadth as novelty. In industrial contexts, Palmarini et al. synthesized AR maintenance applications and identified fragmentation across hardware, software, and solution choices [Palmarini2018Maintenance]. Fernández del Amo et al. subsequently examined 74 maintenance-related papers through authoring, context-awareness, interaction analysis, and knowledge-transfer mechanisms [FernandezDelAmo2018KnowledgeTransfer]. Vocational-training research has likewise been synthesized across industrial, medical, and educational applications [Chiang2022VocationalTraining]. These reviews establish that application taxonomy, technology enumeration, and training-effect summaries are already mature review objectives.

Education has an equally substantial synthesis base. Meta-analyses have evaluated learning gains and pedagogical moderators [Garzon2019LearningGains, Garzon2020Pedagogy], while later work has examined K–12 evidence, cognitive load, and mixed-reality learning effectiveness [Zhang2022K12AR, Zhu2026CognitiveLoad, Huang2025MixedRealityEducation]. Consequently, this review does not treat a positive learning effect, engagement advantage, or device comparison as transferable without retaining pedagogy, learner, comparator, exposure, outcome, and time-horizon conditions.

Healthcare provides an especially strong test of overclaiming. Earlier reviews evaluated the validity of AR for medical training [Barsom2016MedicalTraining] and medical education more broadly [Tang2020MedicalEducation]. Subsequent syntheses examined surgical education [Kovoor2021SurgicalEducation, ElAshry2026SurgicalTrainingReview], health-sciences higher education [RodriguezAbad2021HealthSciences], and the combined VR/AR medical-education review landscape [Tene2024MedicalUmbrella]. A 2026 U.S. scoping review further focused on XR head-mounted displays in healthcare education [Lauinger2026XRHealthEducation]. These studies make a new healthcare taxonomy neither necessary nor defensibly novel.

Recent reviews also narrow interaction, evaluation, replication, intelligent AR, digital-twin integration, accessibility, and field-deployment questions. For example, interaction/UX evaluation has been synthesized directly [Hughes2025InteractionUX], while replication practices across IEEE ISMAR and IEEE VR have been examined independently [Arefin2025Replication]. Intelligent and conversational AR, adaptive multimodal interfaces, and AR–digital-twin integration likewise have dedicated recent reviews [Bassyouni2021AIRobotics, Wu2026ConversationalAR, Ramtohul2025AdaptiveMultimodal, Yin2023ARDigitalTwin, Kautsar2026Bidirectional].

The resulting opportunity is therefore methodological rather than taxonomic. Existing reviews usually optimize for a domain, technology family, outcome class, or application question. The present review instead asks whether evidence produced under heterogeneous AR conditions can be **compared, transferred, reproduced, reconciled, and converted into a defensible next experiment**. Its organizing contribution is the joint use of P_i=(D,T,H,S,A,M,E,U,R), C0–C3 comparability, the Evidence Cube, study-family provenance, graded reproducibility/replication evidence, contradiction analysis, and a gap-promotion gate. Final claims that this combination is distinct from all closest prior reviews remain provisional until the formal review-of-reviews and primary corpus are frozen.

### C. Research Questions

**RQ1 — Evolution:** How have AR research problems, enabling technologies, devices, algorithms, applications, and evaluation practices evolved from foundational work to the present?

**RQ2 — Research structure:** What technical, human, system, and application dimensions form a sufficiently expressive taxonomy of AR research?

**RQ3 — Methods:** Which algorithm and method families are used for tracking/localization, mapping, registration, perception, visualization, interaction, collaboration, networking, adaptation, security, and intelligent AR?

**RQ4 — Evidence infrastructure:** Which datasets, benchmarks, metrics, hardware configurations, sensor configurations, experimental environments, and user populations support each research problem?

**RQ5 — Comparability:** Under what conditions are results from two AR studies directly comparable, conditionally comparable, or non-comparable?

**RQ6 — Reproducibility:** What evidence is available to reproduce reported AR results, including code, data, models, configuration, hardware, seeds, and evaluation scripts?

**RQ7 — Failure regimes:** Under which environmental, hardware, user, workload, sensing, latency, or deployment conditions do methods degrade or fail?

**RQ8 — Contradictions:** Where do studies addressing materially similar problems report conflicting findings, and can protocol differences explain those conflicts?

**RQ9 — Persistent gaps:** Which limitations and under-evidenced regions persist over time despite growth in publication volume?

**RQ10 — Cross-dimensional gaps:** Which combinations of task × device × environment × user × method × metric remain weakly evidenced, and which are scientifically meaningful rather than merely empty literature cells?

**RQ11 — Researcher decision support:** For a given AR research problem, what method families, datasets, metrics, baselines, evaluation protocols, and reproducibility requirements are supported by the accumulated evidence?

**RQ12 — Experimental opportunities:** Which verified gaps admit reproducible benchmark experiments against defensible baselines?

**RQ13 — New-method gate:** After closest-prior-work and benchmark analysis, does any verified gap justify a new algorithm or method, and if so, what measurable hypothesis distinguishes it from existing approaches?

## II. Review Methodology

### A. Reporting and Search-Quality Framework

The review is designed for transparent systematic-review reporting using PRISMA 2020 [Page2021PRISMA]. Search reporting follows PRISMA-S [Rethlefsen2021PRISMAS], and the search strategy is structured so that it can be independently reviewed using principles consistent with PRESS [McGowan2016PRESS]. Deduplication is treated as an auditable methodological stage rather than an invisible reference-manager operation [Bramer2016Deduplication]. Database coverage is deliberately multi-source because retrieval differs across bibliographic systems [Bramer2017DatabaseCombinations].

### B. Scope

The principal phenomenon is augmented reality. Mixed reality and extended reality records are eligible when an AR component is separable or when the study directly informs an AR method, benchmark, sensing/device configuration, interaction/evaluation protocol, user population, or reproducibility question. Pure virtual-reality studies without separable AR evidence are excluded.

No lower publication-date bound is imposed because foundational AR research is relevant to longitudinal analysis. The frozen upper date is 5 October 2026. English search terms are used. A full English text is required for coded primary-study inclusion; non-English records encountered during searching are retained in the screening audit and excluded using the controlled E-LANGUAGE reason.

### C. Information Sources

The formal bibliographic sources are IEEE Xplore, ACM Digital Library, Scopus, Web of Science Core Collection, ScienceDirect, SpringerLink, and PubMed. PubMed is included specifically to strengthen coverage of health and clinical AR. Supplementary discovery comprises backward citation chasing, forward citation chasing where supported, and preprint discovery. When a peer-reviewed version of a preprint is identified, report relationships are resolved through the study-family procedure rather than treating versions automatically as independent studies.

**Execution state:** PENDING_FORMAL_EXECUTION. Exact execution dates, per-source retrieval totals, export limitations, and final source-level counts will be populated from the immutable search registry rather than reconstructed retrospectively.

### D. Search Strategy

The search architecture combines a high-recall AR core with twelve specialist blocks. The canonical AR core is:

> "augmented reality" OR "mixed reality" OR "extended reality" OR "AR system" OR "AR application"

The standalone acronyms AR, MR, and XR are not used in broad full-text searching because of ambiguity. Q00 applies the AR core alone where platform/export volume permits. Q01–Q12 combine the core with specialist blocks covering: (1) tracking/localization/SLAM; (2) perception/occlusion/scene understanding; (3) interaction/multimodal/collaboration; (4) networking/resources; (5) security/privacy/safety/governance; (6) human factors/accessibility/UX; (7) adaptive/intelligent/generative AR; (8) digital twins/cyber-physical systems; (9) education/training; (10) health/clinical; (11) industrial/maintenance/assembly; and (12) evidence/benchmark/reproducibility.

Database-specific translation may alter field wrappers, quotation syntax, wildcard syntax, or split a query where platform limits require it, but the semantic term set is frozen. Every executed query must be copied verbatim into the search registry. If a query is mechanically split, all subruns are retained and their union is processed before cross-query deduplication.

### E. Eligibility Criteria

A record is eligible for the primary corpus when it is a primary empirical, experimental, technical, methodological, system, dataset, benchmark, or user study; AR is principal, separable, or materially necessary to the contribution; evidence is extractable for at least one review dimension; sufficient methodological information is available; and duplicate/companion reports are resolved to the appropriate canonical study report.

Controlled exclusions are E-NOT-AR, E-VR-ONLY, E-SECONDARY, E-NONRESEARCH, E-DUPLICATE, E-COMPANION, E-INSUFFICIENT, E-LANGUAGE, and E-OUTSIDE-DATE. Secondary reviews are retained in the review-of-reviews and prior-art layer but are not counted as primary studies.

### F. Search Provenance and Raw-Export Integrity

Each formal search execution records source, query identifier, exact executed query, execution date, coverage dates, filters, raw result count, exported count, export filename and SHA-256 checksum, access limitation, operator/tool, and notes. Raw exports are immutable. Normalization, pooling, deduplication, and screening operate only on derived representations.

The ingestion pipeline fails closed if an export lacks a matching executed registry entry, if its checksum differs from the registered checksum, if a declared export count disagrees with the parsed count, or if a record lacks the minimum identity required for screening.

### G. Deduplication and Study Families

Bibliographic deduplication proceeds in the following order: normalized DOI exact match; stable identifier exact match; normalized-title exact match; and fuzzy normalized title plus first author and year. Fuzzy matches are candidates for manual verification and are never automatically deleted.

Report identity is distinguished from study identity. Preprint, conference, and journal versions may belong to one study family but are not automatically duplicates. The most complete peer-reviewed report is normally canonical; companion reports are retained when they contain materially distinct datasets, experiments, populations, methods, or outcomes. Every extracted datum preserves its source-report provenance.

### H. Screening

Screening has two stages: title/abstract followed by full text. Each record receives include, exclude, or uncertain together with a controlled reason. Uncertain records advance rather than being silently discarded. Decisions are versioned rather than overwritten.

For the final corpus, all included studies require a second independent verification pass, together with a stratified sample of exclusions. Any genuine inter-rater agreement statistic will be reported only if a genuine second screener performs the verification; no synthetic reviewer agreement will be created.

**Screening state:** final formal screening is externally blocked pending source-native exports; the 16-study Pilot Corpus V1 has completed pilot screening and downstream validation.

### I. Evidence Extraction

Included studies are coded using P_i=(D,T,H,S,A,M,E,U,R): domain, AR technology, hardware, sensing, algorithm/method, metrics/evaluation, environment, users, and reproducibility. Additional fields capture task, dataset, benchmark, baseline, protocol, statistics, reported results, limitations, code, data, models/checkpoints, configuration, hardware specifications, seeds, evaluators, raw outputs, and threats to validity.

The representation is intentionally condition-aware. A reported result is interpreted together with the experimental conditions that make it meaningful rather than extracted as an isolated performance number.

### J. Comparability and Evidence Synthesis

Comparability is evaluated on an ordinal C0–C3 scale spanning non-comparable to directly comparable evidence. Assignment considers task identity, dataset or stimulus, hardware/sensing stack, environment, user population, baseline, metric semantics, and evaluation protocol. Cross-study rankings are prohibited when evidence is not sufficiently comparable.

The Evidence Cube organizes evidence across technique, environment, device, user, metric, and domain. Sparse combinations are diagnostic observations, not automatic research gaps. Candidate gaps are evaluated for persistence, contradiction, reproducibility limitations, closest prior work, and experimental actionability before being promoted.

Where quantitative meta-analysis is inappropriate because outcomes, metrics, tasks, or protocols are not commensurate, synthesis will remain structured and stratified rather than pooling incompatible effect estimates.

### K. Reproducibility and Replication

Reproducibility is coded beyond simple artifact availability. The review distinguishes reporting transparency, materials, data, code, environment/configuration, independent executability, result reproduction, and study replication. A paper with public code is therefore not automatically classified as reproduced or replicated.

### L. Search Stopping and Corpus Freeze

Searching stops only after all registered formal source-query cells are executed or a limitation is explicitly documented; deduplication and both screening stages are complete; designated backward/forward citation chasing is processed; the final citation-chasing iteration introduces no unsearched branches inside the frozen date window; and the registry, screening ledger, study-family ledger, and corpus checksums are frozen.

No target number of included studies is used as a stopping rule.

### M. PRISMA Count Derivation

PRISMA identification, screening, retrieval, exclusion, and inclusion totals are derived programmatically from frozen registries and ledgers. Counts are never typed manually into the manuscript. The following identities must reconcile before corpus freeze:

- records_after_dedup = records_screened;
- records_screened = records_excluded_title_abstract + reports_sought;
- reports_sought = reports_not_retrieved + reports_assessed;
- reports_assessed = reports_excluded_full_text + included_reports.

**All final numeric PRISMA fields remain externally blocked pending source-native formal-search execution and corpus freeze.**

## III. Results

**FINAL SYSTEMATIC RESULTS BLOCKED UNTIL NEXT-05 CORPUS FREEZE.** Pilot Corpus V1 results are available as workflow-validation evidence, but no final corpus-derived prevalence estimate, PRISMA count, gap frequency, or universal cross-study ranking is asserted.

## IV. Discussion

A section architecture is reserved for: evolution of AR evidence; comparability and benchmark transfer; reproducibility and replication; human-factor and field-validity contradictions; persistent versus merely sparse gaps; implications for researchers; and limitations of the review. Final interpretation is deferred until the corpus is frozen and the synthesis gates have been executed.

## V. Conclusion

**FINAL CONCLUSION LOCKED TO FINAL SYNTHESIS.** The conclusion will be written only after the evidence map, contradiction analysis, reproducibility audit, and verified-gap analysis are complete.

## References

The manuscript bibliography is maintained in paper_writing/paper_artifacts/references/master.bib. The current evidence library contains 212 validated BibTeX records; manuscript citations must use keys present in that master file.
