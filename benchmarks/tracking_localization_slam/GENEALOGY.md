# Algorithm Genealogy and Comparison Logic

## Why genealogy precedes benchmarking

Method names conceal different computational contracts. The tracking/localization family contains at least four distinct branches:

1. **online keyframe SLAM** — PTAM → ORB-SLAM → ORB-SLAM2 → ORB-SLAM3;
2. **visual-inertial state estimation** — optimization-based systems such as VINS-Mono and filter-based systems such as OpenVINS;
3. **direct odometry** — systems such as DSO that optimize photometric error rather than feature correspondences;
4. **map-based absolute localization** — hierarchical retrieval/matching systems such as HLoc and AR-native benchmark pipelines such as LaMAR.

The project will not collapse these branches into one leaderboard.

## Historical path

### PTAM
PTAM is retained as a foundational AR-oriented ancestor because it separated tracking and mapping into parallel processes and demonstrated keyframe-based monocular mapping for augmented reality. It is primarily a genealogy reference rather than the default modern executable baseline.

### ORB-SLAM lineage
ORB-SLAM established a unified ORB-feature pipeline for tracking, mapping, relocalization and loop closing. ORB-SLAM2 expanded the sensor modes. ORB-SLAM3 further integrated visual-inertial estimation and multi-map operation.

### VIO split
VINS-Mono represents tightly coupled nonlinear optimization with IMU preintegration and visual features. OpenVINS provides a contrasting filter/MSCKF research platform. This creates a scientifically meaningful optimization-versus-filter comparison when sensor inputs and protocols are harmonized.

### Direct methods
DSO is retained because direct photometric optimization represents a materially different mechanism. Its canonical formulation is odometry, so global loop-closing claims must not be compared as though its system contract were identical to full SLAM.

### Absolute localization
HLoc narrows a reference database through image retrieval, matches local features, and estimates query pose geometrically. This is an absolute localization contract rather than continuous online SLAM.

### AR-native localization and mapping
LaMAR explicitly targets localization and mapping for AR devices under realistic conditions, including heterogeneous devices, multi-session capture, and multi-sensor streams. It therefore forms the bridge between computer-vision localization and actual AR deployment evidence.

## Comparison principle

A method pair is compared only after answering:

- Are they solving the same task?
- Do they receive the same information?
- Is a prebuilt map allowed?
- Is temporal history allowed?
- Is IMU/radio/depth allowed?
- Are metrics semantically identical?
- Is failure defined identically?
- Are resource budgets disclosed?

If any answer materially changes the problem contract, the comparison is stratified or marked contextual rather than used as a direct ranking.

## First mechanism-level experimental contrasts

### Contrast A — optimization VIO vs filter VIO
VINS-Mono vs OpenVINS on matched camera+IMU sequences.

### Contrast B — visual vs visual-inertial within a common SLAM family
ORB-SLAM3 visual vs inertial modes where datasets support both.

### Contrast C — controlled benchmark vs AR-native deployment
Compare robustness/ranking patterns across controlled VIO/SLAM datasets and LaMAR-compatible localization experiments only where task mappings are defensible.

### Contrast D — retrieval/matching choices within absolute localization
Use the modular HLoc/LaMAR-style pipeline to vary retrieval, local features, matchers, sequence/multicamera cues and measure recall–latency–resource trade-offs.

Contrast D is particularly attractive for later new-method development because components can be changed under a stable AR-native evaluation contract.

## Current gap hypothesis

A candidate gap is **benchmark-transfer instability**: conclusions drawn from controlled robotics/vision datasets may not preserve method ranking or failure behavior under heterogeneous, multi-session AR conditions.

This remains a hypothesis until executable evidence exists.

## Next gate

Before running experiments:
1. pin exact upstream commits;
2. verify licenses;
3. construct build manifests;
4. select a small legal/downloadable benchmark subset;
5. implement dataset-integrity checks;
6. implement common result adapters;
7. run smoke tests;
8. only then launch full benchmark workflows.
