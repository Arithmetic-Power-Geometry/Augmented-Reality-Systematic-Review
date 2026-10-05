# NEXT-02 Adversarial IEEE/TVCG Review — Batch 1

## Initial reject-first assessment

### HIGH — Batch coverage is strongly uneven
The first parallel discovery is rich in accessibility, cognitive load and industrial AR but leaves several of the 25 workstreams empty. Treating this batch as the systematic corpus would produce severe topic-selection bias.

**Required correction:** label every record as discovery candidate; publish a workstream coverage matrix; explicitly carry empty streams into later discovery expansion.

**Resolution:** implemented. **RESOLVED.**

### HIGH — Search-engine discovery is not equivalent to the frozen multi-database systematic search
A web discovery batch cannot substitute for IEEE Xplore/ACM/Scopus/WoS/etc. query execution.

**Required correction:** preserve Batch 1 as seed/discovery evidence only; do not populate PRISMA database counts from it; future source-query runs must be logged verbatim in the frozen search registry.

**Resolution:** implemented. **RESOLVED.**

### HIGH — Primary/secondary contamination risk
Broad AR searches surface systematic reviews alongside primary studies.

**Required correction:** Batch 1 registry contains only records with an identifiable primary empirical/technical evaluation; reviews remain in the separate review-of-reviews layer. Formal screening remains NEXT-03.

**Resolution:** implemented. **RESOLVED.**

### HIGH — Premature manuscript statistics
Counts from a convenience discovery batch could be mistaken for prevalence estimates.

**Required correction:** manuscript-facing Batch-1 table explicitly prohibits prevalence/generalization claims until the frozen systematic corpus exists.

**Resolution:** implemented. **RESOLVED.**

### MEDIUM — Metadata completeness varies
Some candidates have DOI-quality metadata; others currently rely on stable identifiers/PMC records and need canonical metadata verification.

**Required correction:** NEXT-03 must canonicalize DOI/venue/year before inclusion.

**Status:** OPEN-MEDIUM; does not block seed discovery but blocks final corpus inclusion.

## Verdict

**PASS AS DISCOVERY BATCH ONLY.** Unresolved CRITICAL=0; unresolved HIGH=0.

NEXT-02 does not satisfy systematic-search exhaustion. It creates a defensible seed primary-study registry and exposes coverage targets for the next discovery expansion/screening work.
