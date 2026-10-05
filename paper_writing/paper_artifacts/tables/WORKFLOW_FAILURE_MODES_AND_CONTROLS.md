# Table — Workflow Failure Modes and Controls

| Observed failure mode | Why it failed | Permanent control | Status |
|---|---|---|---|
| Literal `\\n` embedded in shell runner | Generated text joined commands incorrectly | signature scan + `bash -n` | controlled |
| Wrong/stale repository path | Workflow/script expected a file at a historical location | required-path preflight | controlled |
| Queue/master-plan disagreement | Sequential state drifted across control files | ledger-consistency preflight | controlled |
| Malformed BibTeX escaping / duplicate citation risk | Manual/generated citation edits can corrupt LaTeX or duplicate DOI/key | Bib key/DOI uniqueness + validation ledger | controlled |
| Build/runtime dependency failure | Cannot be proven by static inspection | build-smoke required after static PASS | still requires NEXT-20 evidence |

**Scientific-run rule:** static preflight PASS → build-smoke PASS → provenance capture → scientific execution. A workflow file existing is never treated as successful execution.
