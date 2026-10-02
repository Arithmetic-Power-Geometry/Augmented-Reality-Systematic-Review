# Containers

Method environments are intentionally isolated.

## Rules

1. Every scientific image is built from an immutable upstream reference.
2. A Dockerfile committed here is not evidence that the image built successfully.
3. A successful build is recorded only after a build log and image digest are retained.
4. Dataset bytes are not embedded in method images.
5. Raw predictions are written to mounted output directories.
6. Evaluation occurs through the common evaluator contract.

## Current state

- ORB-SLAM3: build-oriented Dockerfile added; immutable upstream ref required.
- VINS-Mono: source container added; dependency installation deliberately gated.
- OpenVINS: source-pin container added; ROS mode/environment selection remains gated.
- LaMAR: source-pin container added; exact Ceres/COLMAP/HLoc installer remains gated.

No scientific container build is claimed by the presence of these files.
