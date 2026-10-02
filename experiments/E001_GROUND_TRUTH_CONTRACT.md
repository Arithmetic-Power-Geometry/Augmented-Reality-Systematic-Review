# E001 Ground-Truth Normalization Contract

The evaluator accepts ground truth only in the common CSV contract:

`timestamp,tx,ty,tz,qx,qy,qz,qw`

For E001 stereo-inertial evaluation, ground truth must represent the EuRoC IMU/body reference used by the visual-inertial trajectory convention. No scale fitting is permitted.

The ground-truth conversion step must:
1. preserve timestamps numerically;
2. preserve translation units in metres;
3. preserve quaternion orientation with an explicitly documented source ordering;
4. perform no smoothing or interpolation;
5. retain the source file checksum and normalized file checksum.

Until an audited converter for the official EuRoC ground-truth CSV is committed and tested, the one-command execution requires a pre-normalized ground-truth CSV and therefore remains **execution-gated**.
