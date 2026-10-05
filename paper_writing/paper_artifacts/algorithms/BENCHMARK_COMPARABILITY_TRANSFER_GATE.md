# Algorithm — Benchmark Comparability and Transfer Gate

Input: studies a,b and proposed comparative claim c
Output: C0, C1, C2, or C3 plus transfer tier T0-T5

1. Match task definition.
2. Match or characterize dataset/environment difference.
3. Compare sensor stack and device class.
4. Compare motion regime and scale.
5. Verify ground-truth source and accuracy.
6. Align metric definition, units, thresholds and aggregation.
7. Align initialization, failure handling, tuning and sequence split.
8. Distinguish reported from reproduced values.
9. If human outcomes are invoked, require aligned user/task/exposure evidence.
10. If field superiority is invoked, require intended-user operational evidence.
11. Assign:
   C0 = non-comparable;
   C1 = qualitative only;
   C2 = partially comparable with explicit caveats;
   C3 = directly comparable under aligned protocol.
12. Assign transfer tier T0-T5.
13. Permit quantitative ranking only at C3.
14. Permit cross-setting directional synthesis at C2 only with explicit moderators.
15. HOLD any universal-superiority claim based only on T0-T2 evidence.
