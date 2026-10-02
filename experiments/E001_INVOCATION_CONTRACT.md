# E001 Frozen Invocation Contract

Source revision:
`UZ-SLAMLab/ORB_SLAM3@4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4`

## Upstream executable
`Examples/Stereo-Inertial/stereo_inertial_euroc`

The frozen source constructs ORB-SLAM3 with `System::IMU_STEREO`.

## Inputs
- ORB vocabulary: `Vocabulary/ORBvoc.txt`
- settings: `Examples/Stereo-Inertial/EuRoC.yaml`
- sequence root containing:
  - `mav0/cam0/data`
  - `mav0/cam1/data`
  - `mav0/imu0/data.csv`
- a camera timestamp file listing EuRoC image timestamps.

## Frozen settings facts
From the upstream EuRoC YAML at the frozen source revision:
- camera model: pinhole;
- resolution: 752 × 480;
- camera frequency: 20 Hz;
- IMU frequency: 200 Hz;
- ORB features: 1200;
- ORB pyramid scale factor: 1.2;
- pyramid levels: 8;
- FAST initial threshold: 20;
- FAST minimum threshold: 7.

The upstream calibration/extrinsics/noise values are used without project tuning.

## Output
Passing `E001_R01` as the optional output stem makes the upstream executable save:
- `f_E001_R01.txt`: frame trajectory;
- `kf_E001_R01.txt`: keyframe trajectory.

The project runner additionally captures:
- `E001_R01.log`;
- `SHA256SUMS.txt`.

## Ground truth
Ground truth is not an input to this executable. It enters only the post-run evaluator.

## Upstream-script provenance note
The frozen README describes root-level EuRoC helper scripts. Those helper paths were not retrievable at the frozen commit through the repository content interface during this audit. The project therefore invokes the documented executable directly from its source-level argument contract rather than reconstructing or assuming an unavailable helper script.
