# E001 Execution Checklist

## Frozen before execution
- [x] Experiment protocol
- [x] Primary metrics
- [x] Failure rules
- [x] ORB-SLAM3 canonical repository
- [x] Full ORB-SLAM3 commit SHA: `4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4`
- [x] Dataset/sequence identity: EuRoC `MH_01_easy`

## Must be completed on the execution runner
- [ ] Acquire the sequence from the official EuRoC source.
- [ ] Record source URL and applicable terms.
- [ ] Generate local SHA-256 provenance metadata.
- [ ] Freeze the exact ORB-SLAM3 EuRoC sensor mode/configuration.
- [ ] Record configuration SHA-256.
- [ ] Build the pinned container.
- [ ] Record image digest and build log.
- [ ] Record CPU/GPU/RAM/OS.
- [ ] Execute without access to ground-truth poses in the inference path.
- [ ] Preserve raw upstream trajectory and process log.
- [ ] Hash raw output.
- [ ] Normalize through the common adapter.
- [ ] Validate normalized trajectory.
- [ ] Run the frozen evaluator.
- [ ] Validate metric record.
- [ ] Freeze result provenance.

## Stop conditions
Stop and record a failed/blocked run rather than improvising if:
- the pinned source does not build;
- the official dataset cannot be acquired;
- the upstream example requires an undocumented patch;
- timestamps/calibration cannot be mapped unambiguously;
- evaluation requires changing the preregistered metric semantics.

Any correction creates a new protocol/run version.
