#!/usr/bin/env bash
set -euo pipefail
METHOD="${1:-}"; REF="${2:-}"; DEP_REF="${3:-}"
sha40(){ [[ "$1" =~ ^[0-9a-f]{40}$ ]]; }
if [[ -z "$METHOD" || -z "$REF" ]]; then
  echo "usage: $0 {orbslam3|vinsmono|openvins|lamar} FULL_40_HEX_COMMIT [DEPENDENCY_40_HEX_COMMIT]" >&2; exit 64
fi
sha40 "$REF" || { echo "scientific builds require a full 40-hex method commit" >&2; exit 64; }
case "$METHOD" in
 orbslam3)
   [[ -n "$DEP_REF" ]] && sha40 "$DEP_REF" || { echo "ORB-SLAM3 requires full Pangolin commit" >&2; exit 64; }
   docker build -f containers/orbslam3/Dockerfile --build-arg ORB_SLAM3_REF="$REF" --build-arg PANGOLIN_REF="$DEP_REF" -t "ar-review-orbslam3:$REF" .
   ;;
 vinsmono) docker build -f containers/vinsmono/Dockerfile --build-arg VINS_MONO_REF="$REF" -t "ar-review-vinsmono:$REF" . ;;
 openvins) docker build -f containers/openvins/Dockerfile --build-arg OPENVINS_REF="$REF" -t "ar-review-openvins:$REF" . ;;
 lamar) docker build -f containers/lamar/Dockerfile --build-arg LAMAR_REF="$REF" -t "ar-review-lamar:$REF" . ;;
 *) echo "unknown method: $METHOD" >&2; exit 64 ;;
esac
