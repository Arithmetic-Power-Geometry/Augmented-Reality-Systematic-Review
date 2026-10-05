# Algorithm — Manuscript Claim-State Gate

Input: candidate manuscript sentence c
Output: DRAFT_NOW, PROVISIONAL, or BLOCK_UNTIL_FREEZE

1. If c reports retrieved/screened/included/excluded counts -> BLOCK_UNTIL_FREEZE.
2. If c reports prevalence/frequency across the review corpus -> BLOCK_UNTIL_FREEZE.
3. If c reports final gap/contradiction strength derived from the corpus -> BLOCK_UNTIL_FREEZE.
4. If c describes a frozen protocol, planned search semantics, extraction schema, or dedup method -> DRAFT_NOW, but use prospective/planned wording until execution.
5. If c summarizes a fully validated external reference -> DRAFT_NOW with citation.
6. If c states novelty/contribution relative to the final corpus -> PROVISIONAL until closest-prior-work and corpus checks finish.
7. If c describes pilot/seed evidence -> PROVISIONAL and label it pilot/seed.
8. If c reports an experiment -> require immutable execution provenance; otherwise BLOCK.
9. Before final submission, convert every prospective Methods statement to executed wording only when the registry/ledgers support it.
