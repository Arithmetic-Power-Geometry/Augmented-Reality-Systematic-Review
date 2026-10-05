# NEXT-05 Run 4 — Workflow Hardening + Tracking/SLAM Bibliography

## Workflow root-cause analysis
The historical workflow failures were not one repeated defect. Audited causes were:
1. literal escaped-newline corruption in a generated shell runner;
2. stale/wrong path assumptions in historical notes;
3. execution-ledger drift between queue and master plan.

GitHub Actions uses fail-fast shell behavior and repository-workspace path resolution, so each class can stop a job immediately.

## Permanent mitigation added
`scripts/preflight_repository.sh` is now the fail-closed static gate before scientific workflows. It checks:
- required repository paths;
- Bash syntax;
- execution queue/master-plan consistency;
- duplicate BibTeX keys/DOIs;
- YAML parsing when Ruby is available;
- the previously observed literal-newline corruption signature.

No new automatic Actions workflow was created in this run. The preflight is deliberately a standalone checker first, avoiding a new CI failure while CI is being hardened.

## Bibliography
Prior validated entries: 21
New validated entries: 5
Current master.bib: **26 validated entries**

New tracking/localization anchors:
- PTAM (ISMAR 2007)
- ORB-SLAM (TRO 2015)
- ORB-SLAM2 (TRO 2017)
- VINS-Mono (TRO 2018)
- ORB-SLAM3 (TRO 2021)

## 200+ trajectory
174+ additional validated references remain to reach the breadth target. This target remains subordinate to relevance and validation.

## Corpus freeze
NEXT-05 remains open because formal database-specific export/query evidence and final screening/exhaustion evidence are still incomplete.
