# Candidate Benchmark Validity and Transfer Model

Represent an evaluation as:
B = (Task, Dataset, SensorStack, Device, Environment, Motion, GroundTruth, Metric, Protocol, User, FieldTier)

## Benchmark dimensions
- task: localization, mapping, registration, tracking, reconstruction, interaction/user task;
- dataset provenance: benchmark, newly collected, synthetic, live;
- sensor stack: mono/stereo/RGB-D/IMU/radio/depth/hybrid;
- device: hand-held, HMD, robot/MAV, external rig;
- environment: indoor/outdoor, texture, lighting, scale, dynamics, clutter;
- motion: static, controlled, handheld, head-worn, unconstrained/mobile;
- ground truth: mocap, laser, survey, external tracker, pseudo-GT, annotation;
- metric: ATE/RPE/TRE/recall/latency/FPS/failure/user outcome;
- protocol: sequence split, initialization, failure handling, parameter tuning;
- user and field tier where human evaluation exists.

## Evidence-transfer classes
T0 Same benchmark/protocol.
T1 Same task/metric but different sequence or environment.
T2 Same algorithmic task but different device/sensor stack.
T3 AR-realistic transfer: head/hand-held, heterogeneous device, realistic environment.
T4 Human-task transfer: technical result connected to user/task outcome.
T5 Field transfer: intended users and operational environment.

A result at T0 cannot be promoted to T5 without intervening evidence.

## Evidence basis
- LaMAR: realistic multi-session, multi-sensor AR-device localization/mapping benchmark in three large indoor/outdoor locations.
- TUM-VI: synchronized VI benchmark with calibrated camera/IMU sensing and motion-capture ground truth.
- EuRoC: 11 stereo+IMU sequences with accurate ground truth in industrial and mocap environments.
- Guo et al. 2022: 87 HMD user-measurement papers across environmental conditions.
- Dey et al. 2018: 291 AR papers/369 user studies; methodological and display/application variation.
- Sadeghi-Niaraki & Choi 2020: markerless tracking/registration survey emphasizing application/environment-dependent localization requirements.
- Hu et al. 2025: standardized cross-device XR tracking evaluation showing substantial device/environment effects.

## Synthesis rule
No universal algorithm/device leaderboard unless Task, Dataset/Environment, SensorStack, GroundTruth, Metric and Protocol satisfy high comparability. Benchmark superiority is not automatically field superiority.
