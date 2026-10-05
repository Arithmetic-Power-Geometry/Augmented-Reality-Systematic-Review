# Pre-Run Workflow Audit — 2026-10-05

## Purpose
No scientific workflow is run until static paths, shell syntax, workflow references and citation-library syntax are checked.

## Findings

### F1 — CRITICAL — E001 runner contained literal escaped newlines
`experiments/runners/execute_E001.sh` contained literal `\n` characters joining `mkdir`, ground-truth conversion and checksum commands.

**Action:** corrected to real shell newlines; usage text now says raw official EuRoC ground-truth CSV.

### F2 — HIGH — Historical path assumption for image inventory was wrong
The valid script is `containers/capture_image_inventory.sh`; there is no copy under `benchmarks/tracking_localization_slam/scripts/`.

**Action:** confirmed `.github/workflows/orbslam3-build-smoke.yml` already references the correct `containers/` path. No duplicate script created.

### F3 — HIGH — master.bib contained malformed umlaut escaping
The Lauer et al. entry encoded Brünken as `Br{"u}nken`.

**Action:** corrected to BibTeX-safe `Br{\"u}nken`.

### F4 — Workflow structure
`benchmark-integrity.yml` and `orbslam3-build-smoke.yml` are structurally coherent on static inspection. This is not a claim that Actions have passed.

## Run decision
**DO NOT trigger a scientific E001 run during NEXT-05.** Literature corpus work is independent, and E001 remains scheduled later. Before any future run, inspect the actual Actions status/logs and run the static integrity checks against the corrected commit.

## Integrity principle
A workflow file existing in GitHub is not evidence of successful execution.
