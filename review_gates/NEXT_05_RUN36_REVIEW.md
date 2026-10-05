# NEXT-05 Adversarial Reviewer — Run 36

CRITICAL — 91 formal source-query executions are still unexecuted.
Status: OPEN. This blocks final corpus/PRISMA/Results, not all manuscript drafting.

HIGH — Search importer previously lacked execution-backed CI.
Fix: dedicated GitHub Actions integrity workflow committed.
Status: CONTROL IMPLEMENTED; no PASS claimed because no associated run was returned.

HIGH — Methods could lack authoritative methodological citations.
Fix: PRISMA 2020, PRISMA-S, PRESS, Bramer deduplication and database-combination references validated and added.
Resolution: RESOLVED.

HIGH — Waiting for 200 references could unnecessarily delay writing.
Fix: manuscript-start gate separates draftable framing/Methods from freeze-dependent Results.
Resolution: RESOLVED.

HIGH — Starting early could accidentally turn planned search into completed search.
Fix: claim-state gate mandates prospective wording until registry provenance supports executed wording.
Resolution: RESOLVED.

Verdict: START METHODS-FIRST DRAFTING while formal search execution proceeds; DO NOT write final Results or PRISMA counts.
