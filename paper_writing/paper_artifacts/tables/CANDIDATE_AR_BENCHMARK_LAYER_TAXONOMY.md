# Candidate Result — AR Benchmarking Has Become Multi-Layer

**Pre-freeze synthesis.**

| Benchmark | AR-relevant layer | Ground truth / task scope |
|---|---|---|
| LaMAR | localization/mapping | persistent multi-session AR localization |
| Aria Digital Twin | 3D scene + object + human perception | device/object 6DoF, gaze, human pose, segmentation, depth, reconstruction/detection tasks |
| EgoObjects | fine-grained egocentric object understanding | instance/category detection + continual-learning tasks |
| CroCoDL | cross-device collaborative localization | robot + handheld + head-mounted devices across ten environments |
| Ego-HOIBench | human-object interaction understanding | fine-grained hand–verb–object triplets, >27K real images |
| ContrAR | semantic/security robustness | 312 real AR videos, contradictory virtual-content attacks, 11 VLMs |

## Candidate interpretation
A single AR “benchmark score” is structurally meaningless across these layers. The review should distinguish at least:

**localization → scene/object perception → interaction understanding → collaborative consistency → semantic/security robustness.**

Reproducibility should likewise be audited per layer: public data, split definition, calibration, annotation/ground truth, evaluator, baseline implementation and hardware/runtime context.
