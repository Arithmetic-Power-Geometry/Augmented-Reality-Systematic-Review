# Gate 2 deterministic benchmark snapshot
BASE_SEED = 20261007
WORLD_SEED = lambda world_id: BASE_SEED + world_id * 7919
FAMILIES = [
("valid_local_claim",20),("valid_broad_claim",20),("unsupported_generalization",20),
("same_claim_conflict",20),("condition_split",20),("estimand_split",20),
("missing_obligation",20),("redundant_evidence",20),("fragile_vs_stable",20),
("dense_narrow_vs_sparse_diverse",20)
]
# Full generated CSV outputs and calculation trace are preserved in the execution record.
