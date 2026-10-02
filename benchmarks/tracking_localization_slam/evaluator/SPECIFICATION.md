# Trajectory Evaluator V1

## Scope
The evaluator operates on normalized timestamped SE(3) trajectories. It is independent of ORB-SLAM3 and does not read method configuration or images.

## Association
Nearest timestamp, one-to-one, maximum absolute difference **0.01 s (10 ms)**.

This tolerance is frozen before E001 execution. Changing it requires a new evaluator/protocol version.

## Alignment
Rigid SE(3) alignment maps estimated positions into the ground-truth frame using a least-squares Kabsch/Horn-style rotation and translation.

**Scale correction is disabled.** E001 is stereo-inertial and is expected to produce metric-scale estimates.

## ATE
ATE is the RMSE of translational residuals after the frozen rigid alignment.

## RPE
V1 uses consecutive associated poses (delta = 1 associated pose).
- translational RPE: RMSE of relative translation-vector error in the preceding pose frame;
- rotational RPE: RMSE of the angle of the relative-rotation error, degrees.

## Synthetic validation
Before scientific data are accepted, CI verifies:
1. identical trajectories produce zero error;
2. a pure global rigid transform produces zero error after alignment;
3. scale distortion remains visible because scale correction is prohibited;
4. timestamp offsets inside 10 ms associate and offsets beyond the tested tighter tolerance are rejected.

## Versioning
Any change to association, alignment, delta definition, units or aggregation creates a new evaluator version. Existing frozen results are not overwritten.
