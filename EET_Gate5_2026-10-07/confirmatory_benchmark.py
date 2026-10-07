# Gate 5 confirmatory benchmark snapshot
BASE_CONFIRMATORY_SEED = 31000000
WORLD_SEED = lambda world_id: BASE_CONFIRMATORY_SEED + world_id * 104729
FAMILIES = [
("valid_local_claim",20),("valid_broad_claim",20),("unsupported_generalization",20),
("same_claim_conflict",20),("condition_split",20),("estimand_split",20),
("missing_obligation",20),("redundant_evidence",20),("fragile_vs_stable",20),
("dense_narrow_vs_sparse_diverse",20)
]
PRIMARY_METRICS = ["OEE","UEE","macro_F1_claim_state","condition_split_F1"]
# EET V2 changes: obstruction explanatory-only; stability secondary; local missingness relaxation only.
