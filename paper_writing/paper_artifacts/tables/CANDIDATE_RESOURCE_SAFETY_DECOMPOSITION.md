# Candidate Resource–Safety Evidence Decomposition

| Source | Mechanism | Main optimization/evaluation axes | Evidence type |
|---|---|---|---|
| Ahn et al. 2020 | resolution + transmission-power control | energy, detection accuracy, latency | analytical/numerical MAR-MEC |
| Seo et al. 2021 | mobile cache + transmission-power management | energy, latency, cache size | analytical/numerical MAR-MEC |
| He et al. 2021 | multiagent DRL offloading/resource allocation | energy, latency, radio/computing resources | simulation |
| Na & Lee 2024 | offloading + generative-AI super-resolution control | energy, latency, detection/service satisfaction | empirical latency model + optimization |
| Sahu et al. 2025 | DQN offloading + adaptive quality scaling | energy, latency, task success, rendering quality | experimental/simulation framework |
| Chen et al. 2024 | AR + captioning/VQA/retrieval | safety-query accuracy/recall, feasibility | benchmark + real-world images + user feasibility |

## Candidate synthesis
Resource-aware AR is a **multiobjective control problem**, not a one-dimensional energy problem:

`policy = f(device state, network state, workload, cache, resolution/quality, compute placement, latency constraint, accuracy/task utility)`.

Results should therefore be compared only when task model, network assumptions, energy boundary, quality/accuracy metric and latency constraint are sufficiently aligned.

## Safety separation
Safety evidence must distinguish at least:
1. **human hazard awareness/detection under AR display conditions**;
2. **AR systems designed to improve safety information/querying**;
3. **navigation/environmental safety effects**;
4. **physical/ergonomic load**.

A safety-assistance system with high model accuracy does not prove that wearing AR universally improves hazard awareness.
