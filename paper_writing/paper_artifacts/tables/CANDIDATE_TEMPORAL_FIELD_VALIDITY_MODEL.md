# Candidate Temporal and Field-Validity Evidence Model

## Evidence tiers

| Tier | Evaluation context | What it can support |
|---|---|---|
| F0 | simulation / synthetic benchmark | mechanism feasibility under modeled conditions |
| F1 | controlled laboratory task | causal/task effects under controlled conditions |
| F2 | realistic task with representative hardware/material | near-field ecological validity |
| F3 | field study with intended workers/environment | operational validity in a real context |
| F4 | repeated/longitudinal field evaluation | learning, adaptation, retention and temporal stability |
| F5 | sustained deployment / multi-site operational evidence | deployment robustness, organizational fit and scalability |

These tiers are not quality scores. A strong F0 study may answer a different question from an F4 study.

## Evidence motivating the hierarchy
- Masood & Egger 2020: 22 experiments; industrial adoption depends materially on organizational fit, user acceptance, compatibility, hardware capability and scaling.
- Loizeau et al. 2021: field evaluation requires task-appropriate criteria and real maintenance constraints; laboratory-only criteria may be unsuitable.
- Zigart & Schlund 2022: skilled workers/students, industrial assembly/wiring, tablet versus spatial AR.
- Gürerk et al. 2025: repeated real repair task; temporal learning changed the comparative result.
- Scargill et al. 2024: persistent markerless AR shows environment texture is an active variable affecting tracking/perception/task performance.

## Evidence-Cube refinement
Refine `E_environment` into at least:
`E = {setting, texture/features, lighting, dynamics, mobility, clutter, persistence/session structure, operational constraints}`.

For persistent/shared AR, environment is not merely context; it can be part of the effective system configuration.

## Candidate longitudinal-gap test
A field may be labeled longitudinally weak only if:
1. a meaningful body of one-shot evidence exists;
2. repeated/sustained behavior is scientifically relevant to the claim;
3. targeted search finds sparse repeated/deployment evidence;
4. closest prior longitudinal studies are coded explicitly.
