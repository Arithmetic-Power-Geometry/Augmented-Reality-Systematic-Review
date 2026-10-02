#!/usr/bin/env bash
set -euo pipefail

# E001 frozen runner: ORB-SLAM3 stereo-inertial on EuRoC MH_01_easy.
# Usage:
#   run_E001.sh ORB_SLAM3_ROOT EUROC_SEQUENCE_ROOT TIMESTAMPS_FILE OUTPUT_DIR
ORB_ROOT="${1:?ORB_SLAM3 root required}"
SEQ_ROOT="${2:?EuRoC MH_01_easy root required}"
TIMES="${3:?camera timestamp file required}"
OUT="${4:?output directory required}"

EXE="$ORB_ROOT/Examples/Stereo-Inertial/stereo_inertial_euroc"
VOCAB="$ORB_ROOT/Vocabulary/ORBvoc.txt"
SETTINGS="$ORB_ROOT/Examples/Stereo-Inertial/EuRoC.yaml"

for p in "$EXE" "$VOCAB" "$SETTINGS" "$TIMES" "$SEQ_ROOT/mav0/cam0/data" "$SEQ_ROOT/mav0/cam1/data" "$SEQ_ROOT/mav0/imu0/data.csv"; do
  [[ -e "$p" ]] || { echo "E001 missing required input: $p" >&2; exit 66; }
done

mkdir -p "$OUT/raw"
cd "$OUT/raw"

# The final positional token is an output stem supported by the frozen
# upstream executable. It causes f_E001_R01.txt and kf_E001_R01.txt.
"$EXE" "$VOCAB" "$SETTINGS" "$SEQ_ROOT" "$TIMES" E001_R01 2>&1 | tee E001_R01.log

test -s f_E001_R01.txt
sha256sum f_E001_R01.txt kf_E001_R01.txt E001_R01.log > SHA256SUMS.txt
echo "E001_RAW_OUTPUT_READY"
