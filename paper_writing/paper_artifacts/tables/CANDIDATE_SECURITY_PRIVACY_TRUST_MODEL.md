# Candidate AR Security, Privacy, and Trust Evidence Model

Represent a security/privacy record as:
S = (Asset, Actor, AttackSurface, Threat, Consequence, Mitigation, Evidence, UsabilityCost, Context)

## Assets
identity/credentials; camera/audio/environmental sensing; biometrics; gaze/gesture/behavior; spatial maps/anchors; location; communications/shared state; rendered output; application/data stores.

## Actors
wearer; bystander; collaborator; application/provider; network/cloud; malicious local/remote actor.

## Threat families
1. sensing/data leakage and inference;
2. authentication/identity/access-control failure;
3. malicious or deceptive output/perceptual manipulation;
4. tracking/spatial-map/anchor manipulation;
5. network/session/shared-state attacks;
6. adversarial ML/perception attacks;
7. bystander privacy and consent;
8. physical/safety consequences induced by cyber/perceptual compromise.

## Mitigation families
permission/access control; authentication; minimization/redaction; privacy-preserving sensing/processing; secure rendering/output; encryption/secure communication; integrity/anomaly detection; user/bystander notification and consent; policy/governance.

## Comparability rule
Do not rank mitigations unless asset, threat model, attacker capability, device/context, security metric and usability/performance cost are aligned.

## Evidence basis
- de Guzman et al. 2019: MR security/privacy survey; limited implementation/evaluation of protection approaches.
- Stephenson et al. 2022: AR/VR authentication SoK, including proposed and deployed mechanisms plus user-experience properties.
- Alzahrani & Alfouzan 2022: AR/cybersecurity systematic review in smart-city context.
- Hallal et al. 2024: XR authentication survey; 1,186 initial records and 197 retained publications.
- Adams et al. 2022: everyday-AR bystander privacy/consent study (N=102), already represented in the broader privacy evidence base.
