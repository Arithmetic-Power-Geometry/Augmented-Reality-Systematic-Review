#!/usr/bin/env bash
set -euo pipefail
METHOD="${1:-}"
REF="${2:-}"
if [[ -z "$METHOD" || -z "$REF" ]]; then
  echo "usage: $0 {orbslam3|vinsmono|openvins|lamar} FULL_COMMIT_OR_TAG" >&2
  exit 64
fi
case "$METHOD" in
  orbslam3) FILE="containers/orbslam3/Dockerfile"; ARG="ORB_SLAM3_REF" ;;
  vinsmono) FILE="containers/vinsmono/Dockerfile"; ARG="VINS_MONO_REF" ;;
  openvins) FILE="containers/openvins/Dockerfile"; ARG="OPENVINS_REF" ;;
  lamar) FILE="containers/lamar/Dockerfile"; ARG="LAMAR_REF" ;;
  *) echo "unknown method: $METHOD" >&2; exit 64 ;;
esac
docker build -f "$FILE" --build-arg "$ARG=$REF" -t "ar-review-$METHOD:$REF" .
