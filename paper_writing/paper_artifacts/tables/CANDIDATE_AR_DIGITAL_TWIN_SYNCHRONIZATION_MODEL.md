# Candidate AR–Digital-Twin Integration and Synchronization Model

Represent an AR–DT system as:
D = (PhysicalAsset, DigitalRepresentation, DataLink, Directionality, UpdateMode, StateConsistency, ARRole, Control, Lifecycle, HumanRole, Evaluation)

## Integration maturity
D0 Static digital content: model/document/overlay with no live asset linkage.
D1 Digital model: digital representation updated manually/offline.
D2 Digital shadow: physical -> digital automated data flow; no demonstrated digital -> physical control.
D3 Connected AR shadow: live physical -> digital state exposed through AR/MR.
D4 Bidirectional twin interface: physical <-> digital synchronization with AR/MR interaction/control.
D5 Closed-loop operational twin: synchronized state, decision/control loop, measured latency/consistency/failure handling.
D6 Lifecycle/field twin: sustained operational use across intended users/assets/time, with interoperability/provenance evidence.

## AR roles
visualization; inspection; maintenance guidance; assembly; monitoring; remote collaboration; planning; simulation; control; training; decision support.

## Required evidence
- physical asset/process identity;
- digital representation and state variables;
- data source and update mechanism;
- synchronization direction;
- update rate/latency where real-time is claimed;
- state consistency/error;
- control authority and safety constraints where bidirectional;
- interoperability/protocol;
- user/task outcome;
- field duration and lifecycle phase;
- security/privacy/provenance.

## Prior-art positioning
Yin et al. 2023 already surveys AR-assisted DT for human-centric industry.
Kautsar et al. 2026 already reviews bidirectional AR/MR-DT synchronization in manufacturing.
Sthapit & Olbina 2026 reviews 52 DT/XR construction studies and reports interoperability/standardization barriers.
Qiu et al. 2019 reviews AR and DT for digital assembly.
Errandonea et al. 2020 reviews DT maintenance across industrial sectors.

## Contribution restraint
Do not claim AR-DT integration as novel. Our contribution is review-wide evidence normalization: synchronization maturity + field tier + human outcome + comparability + safety/privacy + reproducibility.

## Core rule
A BIM/CAD/3D model displayed in AR is not automatically a digital twin. The claimed DT level must be supported by data linkage, directionality, synchronization, and operational evidence.
