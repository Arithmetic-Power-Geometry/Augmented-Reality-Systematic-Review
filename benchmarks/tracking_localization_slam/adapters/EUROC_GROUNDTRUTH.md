# EuRoC Ground-Truth Adapter

## Accepted input
Canonical EuRoC `state_groundtruth_estimate0/data.csv` pose fields:

- `#timestamp [ns]`
- `p_RS_R_x [m]`, `p_RS_R_y [m]`, `p_RS_R_z [m]`
- `q_RS_w []`, `q_RS_x []`, `q_RS_y []`, `q_RS_z []`

Additional canonical columns such as velocity and IMU biases may be present and are ignored by the pose converter.

## Output
`timestamp,tx,ty,tz,qx,qy,qz,qw`

Conversion is deliberately limited to:
- nanoseconds → seconds;
- quaternion storage order `w,x,y,z` → common `x,y,z,w`.

It does not interpolate, smooth, align, rescale, or transform the pose.

## Fail-closed behavior
The converter rejects files missing the named canonical pose columns, non-finite values, strongly non-unit quaternions, non-increasing timestamps, or fewer than two poses.

## Reference-frame rationale
E001 is stereo-inertial. The frozen ORB-SLAM3 README states that visual-inertial EuRoC trajectories use dataset ground truth, while pure-visual trajectories require ground truth transformed to the left-camera frame. Accordingly, E001 uses the body/IMU-aligned EuRoC state ground truth without a camera-frame transformation.
