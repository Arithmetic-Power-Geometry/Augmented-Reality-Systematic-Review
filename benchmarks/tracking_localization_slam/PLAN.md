# Tracking, Localization, and SLAM Benchmark Plan

## Objective

Establish the first executable comparison family for the project while preserving a strict separation among:
1. results reported by original papers;
2. results reported by third-party studies;
3. results reproduced by this repository.

Only category 3 will be used for repository-generated head-to-head benchmark claims.

## Benchmark hierarchy

### Tier A — AR-native
**LaMAR** is the primary benchmark for claims about realistic AR localization/mapping. It was designed around AR-device data, heterogeneous devices, multi-session capture, large indoor/outdoor spaces, and realistic trajectories.

### Tier B — controlled visual-inertial
**EuRoC MAV** and **TUM-VI** are used to test visual-inertial accuracy, robustness, initialization, and controlled repeatability.

### Tier C — controlled RGB-D / legacy
**TUM RGB-D** supports RGB-D trajectory evaluation and historical comparability.

Robotics benchmark performance will not be presented as equivalent to AR deployment performance.

## First baseline set

- ORB-SLAM3
- VINS-Mono
- OpenVINS
- LaMAR reference localization pipeline

Additional methods enter only after license, build feasibility, sensor compatibility, and benchmark compatibility checks.

## Reproduction protocol

Every run must record:
- repository URL;
- exact commit;
- license;
- build environment;
- dependency lock;
- CPU;
- GPU;
- RAM;
- operating system;
- dataset version;
- sequence/query IDs;
- sensor mode;
- calibration source;
- parameter file;
- random seed where applicable;
- warm-up policy;
- number of repetitions;
- timing boundary;
- success/failure rule;
- raw trajectory/prediction output;
- evaluation script version.

## Statistical protocol

Deterministic-looking systems are still run repeatedly when nondeterminism, thread scheduling, GPU operations, initialization, or stochastic components can alter outcomes.

Report:
- per-sequence values;
- median and dispersion across sequences/runs;
- failure counts;
- paired differences when methods share identical sequences;
- confidence intervals where meaningful;
- effect sizes rather than p-values alone.

## Fairness gates

A head-to-head comparison is prohibited when:
- sensor inputs differ materially and the difference defines the method;
- one method uses unavailable test ground truth;
- metric thresholds differ;
- one method is evaluated after manual recovery not allowed to others;
- preprocessing supplies privileged information;
- compute/resource boundaries differ without disclosure.

## First experimental question

**BQ1. Do method rankings and failure patterns observed on controlled SLAM/VIO benchmarks remain stable on an AR-native benchmark?**

This is a research question, not a presumed gap or result.

## Secondary questions

- BQ2. Which methods fail primarily at initialization versus sustained tracking/localization?
- BQ3. How sensitive are results to device type and sensor availability?
- BQ4. What accuracy–latency–memory trade-offs appear under a common environment?
- BQ5. How much of the published comparison landscape is reproducible from public artifacts?

## Novel-algorithm gate

No new SLAM/localization algorithm will be designed until:
1. the baseline reproduction matrix is populated;
2. failure modes are localized;
3. closest prior methods addressing those failure modes are audited;
4. a measurable hypothesis remains unresolved.

A new method must target a specific observed failure regime rather than aggregate unrelated improvements.
