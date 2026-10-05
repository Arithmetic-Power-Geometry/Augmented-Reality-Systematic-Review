# Candidate Result — Adaptation Must Be Compared Against Existing Context-Aware AR

**Pre-freeze novelty constraint.**

Seeliger, Weibel & Feuerriegel provide a concrete prior-art anchor for adaptive AR: HMD-derived task/user context is used by a neural network to decide when navigation cues should be shown. Their second user study compares the adaptive interface against an always-on baseline.

## Consequence for this project's potential new method
A future adaptive multi-objective AR orchestration method cannot claim novelty merely because it:
- senses context;
- predicts when to alter augmentation;
- hides/shows visual cues; or
- uses machine learning for adaptation.

A defensible novelty claim would need a materially different decision space and evidence, for example joint optimization across compute placement, sensing, model complexity, augmentation modality, latency, energy, privacy and task quality. Even that remains only a hypothesis until NEXT-27 closest-prior-work audit.

## Required comparison dimensions
context inputs | adaptation action | objective(s) | device/network state | user state | safety | privacy | latency | energy | task quality | learned vs rule-based policy
