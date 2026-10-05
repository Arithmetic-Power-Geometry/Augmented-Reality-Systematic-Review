#!/usr/bin/env bash
set -euo pipefail
# One-command E001 orchestration. Does not download data or install ORB-SLAM3.
# Usage: execute_E001.sh ORB_ROOT EUROC_MH01_ROOT TIMESTAMPS_FILE GT_RAW_EUROC_CSV RUN_ROOT
ORB_ROOT="${1:?ORB root}"; DATA="${2:?EuRoC MH_01_easy root}"; TIMES="${3:?timestamps file}"
GT_RAW="${4:?official EuRoC state_groundtruth_estimate0/data.csv}"; ROOT="${5:?run root}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
RUN="$ROOT/E001/E001-R01"
mkdir -p "$RUN"/{raw,normalized,evaluation,provenance}
python "$HERE/benchmarks/tracking_localization_slam/adapters/euroc_groundtruth_to_common.py" "$GT_RAW" "$RUN/normalized/groundtruth.csv"
sha256sum "$GT_RAW" "$RUN/normalized/groundtruth.csv" > "$RUN/provenance/groundtruth.sha256"

python "$HERE/benchmarks/tracking_localization_slam/scripts/capture_hardware.py" "$RUN/provenance/hardware.json"
python "$HERE/benchmarks/tracking_localization_slam/scripts/validate_euroc_structure.py" "$DATA"
sha256sum "$ORB_ROOT/Examples/Stereo-Inertial/EuRoC.yaml" > "$RUN/provenance/config.sha256"
cp "$HERE/benchmarks/tracking_localization_slam/manifests/E001_R01_planned.json" "$RUN/manifest.planned.json"

"$HERE/experiments/runners/run_E001.sh" "$ORB_ROOT" "$DATA" "$TIMES" "$RUN"

python "$HERE/benchmarks/tracking_localization_slam/adapters/euroc_orbslam_to_common.py"   "$RUN/raw/f_E001_R01.txt" "$RUN/normalized/trajectory.csv"
python "$HERE/benchmarks/tracking_localization_slam/scripts/validate_common_trajectory.py"   "$RUN/normalized/trajectory.csv"

python "$HERE/benchmarks/tracking_localization_slam/evaluator/trajectory_metrics.py"   "$RUN/normalized/groundtruth.csv" "$RUN/normalized/trajectory.csv" --tolerance 0.01 --run-id E001-R01   --output "$RUN/evaluation/metrics.json"

sha256sum "$RUN/normalized/trajectory.csv" "$RUN/evaluation/metrics.json" > "$RUN/evaluation/SHA256SUMS.txt"
echo "E001_PIPELINE_COMPLETE: $RUN"
