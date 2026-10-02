# Build and Reproducibility Audit

## Architecture decision

Each upstream method receives its own environment. A common evaluator consumes standardized outputs.

This avoids forcing legacy ROS/C++ systems and modern Python/C++ localization pipelines into one brittle environment.

## Verified upstream facts

### ORB-SLAM3
Canonical upstream: UZ-SLAMLab/ORB_SLAM3. The project documents GPLv3 licensing, C++11, Pangolin, OpenCV, Eigen3, and bundled modified DBoW2/g2o dependencies. EuRoC and TUM-VI examples are provided.

### VINS-Mono
Canonical upstream is HKUST-Aerial-Robotics/VINS-Mono. The project is GPLv3 and provides Docker support in addition to its ROS/catkin workflow. Ceres, DBoW2 and a generic camera model are core dependencies.

### OpenVINS
The canonical rpng/open_vins repository remains in the baseline set. Its exact supported environment and immutable commit must be frozen before a build claim is made.

### LaMAR
The official microsoft/lamar-benchmark installation documents Ubuntu 22.04 testing, Python 3.9/3.10, Ceres Solver 2.1, COLMAP 3.8, HLoc 1.4, and editable installation of the LaMAR package.

## Current evidence state

No benchmark execution is claimed in this repository yet.

Current status:
- provenance architecture: established;
- environment separation: established;
- manifest validation: implemented;
- dataset integrity checker: implemented;
- CI integrity workflow: implemented;
- exact upstream commit pins: pending;
- container builds: pending;
- dataset acquisition: pending;
- smoke runs: pending;
- scientific benchmark runs: pending.

## Next action

Freeze exact canonical commits and dependency/container versions, then create the first minimal EuRoC smoke-test adapters. Full experiments remain blocked until smoke-test evidence is present.
