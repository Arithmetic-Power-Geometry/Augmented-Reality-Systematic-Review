# Candidate Human-Factor and Safety Evidence Model

Represent safety evidence as:
H = (SafetyGoal, Exposure, HumanState, ARFunction, Outcome, TimeHorizon, Context, Device)

| Layer | Examples | Do not conflate with |
|---|---|---|
| H1 Safety training | knowledge, skill, hazard recognition | live operational safety |
| H2 Operational assistance | warnings, task guidance, hazard overlays | training retention |
| H3 Situation awareness | attention allocation, hazard detection, response | model/system accuracy alone |
| H4 Cognitive state | workload, fatigue, stress, overload | generic usability |
| H5 Physical/visual burden | eye fatigue, discomfort, device weight, psychomotor fatigue | cybersickness without evidence |
| H6 Behavioral/physical risk | distraction, collision/near-miss, unsafe movement | subjective preference |
| H7 Adaptive safety | sensing cognition + adapting AR intervention | open-loop warning systems |

## Comparability
Safety studies are quantitatively comparable only when safety goal, exposure duration, outcome construct, comparator, user population, device and context are aligned.

## Evidence basis
- Gong et al. 2024: 37 AR safety-training papers; positive overall training effect but no significant AR advantage for knowledge acquisition and limited retention evidence.
- Dodoo et al. 2025: 41 XR worker-safety studies across high-risk industries; human and socio-technical limitations include field of view, motion sickness and control issues.
- Ma et al. 2026: 128 studies; construction AR is strong in site-state support but largely open-loop to worker cognition.
- Gonnermann-Müller & Krüger 2025: empirical cognitive-load evidence supports design-specific rather than medium-level conclusions.

Candidate synthesis: safety benefit and safety burden can coexist in the same AR system; both must be coded.
