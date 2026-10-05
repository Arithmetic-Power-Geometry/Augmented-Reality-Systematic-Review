# Candidate Clinical AR Evidence and Translation Model

Represent a clinical AR study as:
C = (UseCase, User, PatientInvolvement, ARFunction, Accuracy, Workflow, Comparator, ClinicalOutcome, Safety, EvidenceDesign, FollowUp, Certainty)

## Clinical evidence ladder
C0 technical/phantom/cadaver feasibility;
C1 simulation or professional training;
C2 patient-involved feasibility/usability;
C3 prospective clinical performance/accuracy;
C4 comparative clinical effectiveness;
C5 patient-centered outcome/safety benefit;
C6 multicenter, longitudinal, cost-effectiveness or implementation evidence.

## Outcome classes
- technical: registration/navigation error, tracking accuracy, latency, visualization quality;
- operator: task time, error, workload, technical skill, learning curve;
- workflow: setup/preparation time, radiation exposure, integration burden;
- patient/procedure: complications, margins, reintervention, operative outcome, recovery;
- implementation: adoption, reliability, maintenance, cost-effectiveness, interoperability;
- safety: device failure, misleading overlay, registration drift, sterility, ergonomic and cognitive risk.

## Prior evidence
- Yoon et al. 2018: 74 surgical wearable-HUD articles; navigation, monitoring and image display prominent.
- Williams et al. 2020 and Suresh et al. 2023: surgical-training evidence.
- Xiong et al. 2025: 12 studies/434 participants; improved basic laparoscopic training metrics but heterogeneous designs and uncertain long-term effectiveness.
- El Ashry et al. 2026 (already in master.bib): 11 studies/347 participants; objective trainee performance, with long-term retention/multicenter evidence still needed.
- Nicolai et al. 2026: 61 patient-only navigated-surgery studies; 51 very-low, 9 low, 1 moderate certainty, none high; accuracy/usability heterogeneous.
- Bollen et al. 2022: intraoperative AR/MR and surgical outcomes review.

## Core synthesis rules
1. Technical accuracy != clinical effectiveness.
2. Simulation/training improvement != patient benefit.
3. Patient-involved feasibility != comparative effectiveness.
4. Reduced radiation/time is a clinical workflow outcome, not automatically a patient-centered outcome.
5. Clinical claims preserve specialty, registration/tracking method, device, comparator, sample size, follow-up and certainty.
6. No “clinically proven” language without appropriate comparative patient evidence.
