#!/usr/bin/env bash
set -euo pipefail

fail(){ printf 'PREFLIGHT_FAIL: %s\n' "$*" >&2; exit 1; }
ok(){ printf 'PREFLIGHT_OK: %s\n' "$*"; }

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

required=(
  ".github/workflows/benchmark-integrity.yml"
  ".github/workflows/orbslam3-build-smoke.yml"
  "experiments/runners/execute_E001.sh"
  "containers/capture_image_inventory.sh"
  "benchmarks/tracking_localization_slam/adapters/euroc_groundtruth_to_common.py"
  "benchmarks/tracking_localization_slam/evaluator/trajectory_metrics.py"
  "paper_writing/EXECUTION_MASTER_PLAN.md"
  "paper_writing/EXECUTION_QUEUE.csv"
  "paper_writing/paper_artifacts/references/master.bib"
)
for p in "${required[@]}"; do [[ -f "$p" ]] || fail "missing required path: $p"; done
ok "required paths exist"

for s in experiments/runners/execute_E001.sh containers/capture_image_inventory.sh containers/build.sh; do
  [[ -f "$s" ]] || fail "missing shell script: $s"
  bash -n "$s" || fail "bash syntax: $s"
done
ok "shell syntax"

python3 - <<'PY'
from pathlib import Path
import csv, re, sys
q=Path("paper_writing/EXECUTION_QUEUE.csv")
rows=list(csv.DictReader(q.open(encoding="utf-8")))
if not rows: raise SystemExit("empty execution queue")
ids=[r["task_id"] for r in rows]
if len(ids)!=len(set(ids)): raise SystemExit("duplicate task_id in execution queue")
master=Path("paper_writing/EXECUTION_MASTER_PLAN.md").read_text(encoding="utf-8")
for r in rows:
    if r["status"]=="COMPLETE":
        line=next((x for x in master.splitlines() if f"| {r['task_id']} |" in x), None)
        if line is None: raise SystemExit(f"{r['task_id']} missing from master plan")
        if "COMPLETE" not in line: raise SystemExit(f"ledger drift: {r['task_id']} COMPLETE in queue but not master plan")
bib=Path("paper_writing/paper_artifacts/references/master.bib").read_text(encoding="utf-8")
keys=re.findall(r"@\w+\{([^,]+),",bib)
if len(keys)!=len(set(keys)): raise SystemExit("duplicate BibTeX key")
dois=[x.lower() for x in re.findall(r"doi\s*=\s*\{([^}]+)\}",bib,re.I)]
if len(dois)!=len(set(dois)): raise SystemExit("duplicate DOI in master.bib")
print("PREFLIGHT_OK: queue/master ledger and BibTeX key/DOI uniqueness")
PY

if command -v ruby >/dev/null 2>&1; then
  ruby -e 'require "yaml"; ARGV.each { |f| YAML.load_file(f, aliases: true); puts "PREFLIGHT_OK: YAML parse #{f}" }'     .github/workflows/benchmark-integrity.yml .github/workflows/orbslam3-build-smoke.yml
else
  printf 'PREFLIGHT_WARN: ruby unavailable; YAML parse not executed locally\n'
fi

if grep -RFn '\\npython ' experiments/runners benchmarks containers --include='*.sh'; then
  fail "literal escaped newline command sequence detected"
fi
ok "no known literal-newline corruption"

printf 'PREFLIGHT_PASS\n'
