# E001 Methodological Readiness

Status: **execution-ready, data/build runner required**

Frozen before observing E001 performance:
- experiment question and failure rules;
- ORB-SLAM3 full source SHA;
- stereo-inertial EuRoC executable and canonical settings;
- dataset/sequence identity;
- raw-output contract;
- ORB-SLAM3 trajectory adapter;
- canonical EuRoC ground-truth adapter;
- 10 ms timestamp association;
- rigid SE(3) alignment, no scale correction;
- ATE/RPE definitions;
- synthetic evaluator tests;
- hardware and dataset provenance capture;
- one-command orchestration.

No scientific performance value has yet been generated.

The remaining work is operational rather than methodological: obtain the official sequence, build the pinned source, execute on recorded hardware, and freeze the resulting raw and derived artifacts.
