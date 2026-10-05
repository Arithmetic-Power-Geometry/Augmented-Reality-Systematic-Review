# Formal Source Execution Outcome — Run 45

Execution was attempted from the currently available environment on 2026-10-05.

| Source | Planned cells | Source-native execution/export available here? | Run-45 outcome | Downstream status |
|---|---:|---|---|---|
| IEEE Xplore | 13 | No authenticated/source-native export channel exposed | ACCESS_LIMITATION | locked |
| ACM Digital Library | 13 | No source-native bulk export channel exposed | ACCESS_LIMITATION | locked |
| Scopus | 13 | No authenticated Scopus execution/export channel exposed | ACCESS_LIMITATION | locked |
| Web of Science Core Collection | 13 | No authenticated WoS execution/export channel exposed | ACCESS_LIMITATION | locked |
| ScienceDirect | 13 | Public article discovery available; no auditable source-native bulk search export | ACCESS_LIMITATION | locked |
| SpringerLink | 13 | Public article discovery available; no auditable source-native bulk search export | ACCESS_LIMITATION | locked |
| PubMed | 13 | Individual records/public discovery available; NCBI E-utilities execution endpoint inaccessible through current web interface | ACCESS_LIMITATION | locked |
| **Total** | **91** | **0 executable source-query cells with required raw export provenance** | **BLOCKED** | **formal corpus not frozen** |

## Important distinction
This is an environment/access outcome, not evidence that the databases themselves lack export capability. General web discovery is not substituted for a registered formal database execution.

## Minimum external input that unlocks the pipeline
For each executed source/query: exact query text, execution date, raw result count, exported count, raw CSV/RIS/BibTeX file, and source identity. The repository importer then verifies checksum/count provenance before pooling.
