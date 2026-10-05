# Candidate Collaborative AR Two-Layer Evidence Model

## Layer C1 — Shared-system state
Code:
- co-located / remote / hybrid;
- device topology and platform heterogeneity;
- shared coordinate frame / spatial anchors;
- registration and alignment error;
- scene reconstruction / environment representation;
- state synchronization and consistency;
- network latency / bandwidth / loss;
- persistence and late-join behavior;
- privacy/cloud dependency;
- scale/complexity of shared spatial state.

Representative evidence:
- Wang et al. 2021: 215-paper AR/MR remote-collaboration review; architectures, interfaces, reconstruction and non-verbal cues.
- Vidal-Balea et al. 2025: off-cloud spatial-anchor synchronization across HoloLens 2 and desktop; anchor complexity materially changes synchronization time.
- Vanukuru et al. 2023: mobile AR spatial communication sharing users and surroundings, including persistent shared-space representations.

## Layer C2 — Human collaboration
Code:
- task type and role structure;
- communication modality;
- shared gaze / gesture / annotation / avatar / proxy;
- attention and shared awareness;
- coordination;
- social/co-presence;
- workload;
- task performance;
- learning/retention;
- trust/acceptance;
- accessibility/inclusion.

Representative evidence:
- Wang et al. 2021: non-verbal cue families and local/remote interface types.
- Ghamandi et al. 2023: 148 retained papers used to build a human-centered collaborative-XR task taxonomy.
- Upadhyay et al. 2024: 20 higher-education collaborative-AR experiments, framed around instructional system, collaboration process and learning outcomes.

## Comparability rule
Collaborative AR studies are candidates for comparison only when both layers are sufficiently aligned:

`C = C1(shared-system configuration) + C2(human collaboration configuration)`.

A low-latency anchor-sharing benchmark does not establish better teamwork; a high collaboration score does not establish shared-state consistency.

## Candidate gap test
A collaborative-AR gap is actionable only when the missing evidence can be located in a specific C1×C2 cell and closest prior work does not already address it.
