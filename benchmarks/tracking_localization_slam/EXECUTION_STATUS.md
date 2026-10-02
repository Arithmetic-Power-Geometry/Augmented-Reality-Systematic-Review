# Execution Readiness Status

Date: 2026-10-02

## Completed

- canonical upstream repositories identified;
- method-specific environment architecture defined;
- upstream dependency constraints recorded;
- candidate stable refs identified where publicly verifiable;
- common run-manifest contract implemented;
- dataset integrity checker implemented;
- trajectory normalization adapter implemented;
- synthetic adapter smoke test implemented;
- CI can validate repository infrastructure without downloading scientific datasets.

## Deliberately not claimed

- ORB-SLAM3 build success;
- VINS-Mono build success;
- OpenVINS build success;
- LaMAR build success;
- EuRoC dataset acquisition;
- LaMAR dataset acquisition;
- any scientific run;
- any reproduced ATE/RPE/recall value;
- any method ranking.

## Pinning policy

Short SHAs discovered through public metadata are candidate identifiers only. Before a scientific run, each selected upstream reference must be resolved to the complete commit SHA and recorded in the run manifest.

For actively maintained upstreams, a stable release may be preferable to a moving branch when it provides a reproducible environment contract. The selection must be documented and cannot be changed after benchmark freeze without creating a new experiment version.

## Next executable gate

1. Resolve full immutable SHAs.
2. Add method-specific container definitions.
3. Build each container.
4. Acquire one EuRoC smoke sequence under its original terms.
5. Record checksums locally/within permitted metadata.
6. Execute one baseline at a time.
7. Normalize raw trajectories.
8. Evaluate only after raw-output provenance passes validation.
