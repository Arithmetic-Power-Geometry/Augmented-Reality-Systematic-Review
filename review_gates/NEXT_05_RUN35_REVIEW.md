# NEXT-05 Adversarial Reviewer — Run 35

CRITICAL — Formal database searches remain unexecuted.
Status: OPEN. No counts fabricated.

HIGH — Raw exports could be silently edited.
Fix: registry SHA-256 must match bytes before ingestion.
Resolution: CONTROL IMPLEMENTED; awaits real exports.

HIGH — Deduplication could delete unique studies.
Fix: fuzzy matches are MANUAL_REVIEW only; no fuzzy auto-delete.
Resolution: CONTROL IMPLEMENTED.

HIGH — Conference/preprint/journal versions could be collapsed as duplicates.
Fix: importer never auto-merges study families.
Resolution: CONTROL IMPLEMENTED.

HIGH — Parsed count could drift from database export count.
Fix: fail closed when declared exported_count differs from parsed count.
Resolution: CONTROL IMPLEMENTED.

HIGH — Tool code might be described as tested without execution evidence.
Fix: self-test is committed as test-ready; no PASS claim without runtime/CI record.
Resolution: RESOLVED.

Verdict: CONTINUE. Critical next action is actual database execution/export provenance, then run importer and screening ledgers.
