# Smoke-Test Gate

No numerical benchmark result is accepted until the corresponding method passes this gate.

## S1 — Source provenance
- canonical upstream identified;
- immutable commit pinned;
- license recorded;
- submodules/dependency revisions recorded.

## S2 — Build
- clean environment build succeeds;
- build log retained;
- container image/digest retained;
- no undocumented manual patch.

## S3 — Dataset integrity
- dataset version recorded;
- required files validated;
- calibration/configuration recorded;
- no benchmark ground truth is exposed to the method during inference unless the protocol explicitly permits it.

## S4 — Minimal execution
- one small sequence/query set completes;
- raw prediction/trajectory retained;
- failure exit codes are propagated;
- timing boundary is observable.

## S5 — Evaluation
- common adapter parses output;
- evaluator produces a machine-readable record;
- manifest validation succeeds;
- result can be regenerated from raw output.

## S6 — Repeatability
- at least three smoke repetitions when nondeterminism is plausible;
- any variation is retained rather than silently selecting the best run.

Passing a smoke test establishes executability, not scientific superiority.
