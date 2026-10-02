# E001 One-Command Bundle

`experiments/runners/execute_E001.sh` chains the frozen stages without making scientific choices during execution.

It requires five explicit inputs:
1. pinned ORB-SLAM3 checkout/build root;
2. official EuRoC `MH_01_easy` sequence root;
3. frozen camera timestamp list;
4. audited normalized EuRoC ground-truth CSV;
5. destination run root.

The command captures hardware, validates dataset structure, hashes the upstream configuration, executes ORB-SLAM3, normalizes the raw trajectory, validates it, evaluates it with the frozen 10 ms/SE(3) evaluator, and hashes derived outputs.

The bundle deliberately does **not** download datasets, guess ground-truth column ordering, install dependencies, or turn a failed run into a successful record.
