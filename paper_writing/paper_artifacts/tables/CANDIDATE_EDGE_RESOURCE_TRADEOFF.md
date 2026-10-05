# Candidate Result — Mobile AR Edge/Resource Tradeoff Structure

**Pre-freeze synthesis.**

The validated edge/resource studies indicate that mobile AR resource management is inherently multi-objective rather than a single latency-minimization problem.

| Study | Main decision variables | Explicit outcomes/tradeoffs |
|---|---|---|
| Ahn et al. 2020 | image resolution + transmit power | energy, latency constraint, recognition accuracy |
| Hao et al. 2024 | subtask offloading + edge-server selection | end-to-end delay under heterogeneous runtime environments |
| Na & Lee 2024 | MEC resource/offloading with generative-AI-enabled framework | energy efficiency and AR service requirements |

## Candidate implication
A future AR orchestration method should not optimize latency alone. At minimum, the evidence supports considering **latency × energy × task/recognition quality**, with hardware/network state as context.

This is relevant to the project's previously proposed adaptive multi-objective orchestration direction, but it is **not evidence of novelty**. A novelty claim requires a dedicated closest-prior-work audit after corpus freeze.
