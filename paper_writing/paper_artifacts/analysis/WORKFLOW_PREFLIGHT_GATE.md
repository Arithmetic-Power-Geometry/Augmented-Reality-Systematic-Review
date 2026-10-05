# Scientific Workflow Preflight Gate

Scientific benchmark workflows must not be triggered merely because a YAML file exists.

Before NEXT-20 or any scientific run:

```bash
bash scripts/preflight_repository.sh
```

A run is permitted only after `PREFLIGHT_PASS`.

The checker currently enforces:
1. required repository paths;
2. Bash syntax for scientific runner/build scripts;
3. queue/master-plan status consistency;
4. duplicate BibTeX-key and DOI detection;
5. YAML parsing when Ruby is available;
6. detection of the literal escaped-newline corruption previously found in E001.

This is a **static gate**, not evidence that a container builds or a scientific experiment succeeds. After static PASS, the next layer is build-smoke evidence; only after that may a scientific run proceed.

## Why prior workflows failed
The observed failures were heterogeneous rather than one recurring GitHub defect:
- generated shell text contained literal `\n` tokens;
- historical notes referenced a stale/wrong script path;
- execution-state files drifted out of agreement.

GitHub Actions is intentionally fail-fast, so these small repository inconsistencies surface as failed jobs rather than being silently ignored.
