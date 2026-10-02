#!/usr/bin/env bash
set -euo pipefail
IMAGE="${1:?image tag required}"; OUT="${2:?output json required}"
DIGEST="$(docker image inspect "$IMAGE" --format '{{.Id}}')"
PKGS="$(docker run --rm "$IMAGE" bash -lc "dpkg-query -W -f='\${Package}=\${Version}\\n' | sort" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().splitlines()))')"
PROV="$(docker run --rm "$IMAGE" cat /opt/BUILD_PROVENANCE.txt | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().splitlines()))')"
python3 - "$OUT" "$IMAGE" "$DIGEST" "$PKGS" "$PROV" <<'PY'
import json,sys
out,image,digest,pkgs,prov=sys.argv[1:]
with open(out,"w") as f:
 json.dump({"image":image,"image_id":digest,"packages":json.loads(pkgs),"build_provenance":json.loads(prov)},f,indent=2)
 f.write("\n")
print("IMAGE_INVENTORY_WRITTEN",digest)
PY
