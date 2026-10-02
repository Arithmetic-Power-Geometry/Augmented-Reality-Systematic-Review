# Benchmark Output Contract

Each run uses:

```
runs/<experiment>/<run_id>/
  manifest.json
  raw/
    <upstream predictions>
    <process log>
    SHA256SUMS.txt
  normalized/
    trajectory.csv
  evaluation/
    metrics.json
    evaluator.log
  provenance/
    dataset.json
    hardware.json
    environment.json
```

## Immutability
Files under `raw/` are immutable after process completion. Normalization and evaluation never rewrite them.

## Invalid runs
Invalid/failed runs retain logs and any partial raw output. Their manifest is updated to `failed` or `invalid` with a reason; directories are not deleted.

## Publication artifacts
Generated figures/tables consume only validated records under `evaluation/` whose manifests have complete provenance.
