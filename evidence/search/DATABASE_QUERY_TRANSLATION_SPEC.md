# Database Query Translation Specification — Frozen V1 Semantics

**Status:** execution aid; does not amend the frozen search concepts and does not claim execution.

## Canonical Boolean payload

AR core:
`("augmented reality" OR "mixed reality" OR "extended reality" OR "AR system" OR "AR application")`

Specialist blocks are copied verbatim from `protocol/PRIMARY_STUDY_SEARCH_STRATEGY.md`.

For Q00 use AR core only. For Q01–Q12 use:
`(AR core) AND (specialist block)`.

## Platform translation policy

| Source | Search surface to prefer | Allowed adaptation | Prohibited silent change |
|---|---|---|---|
| IEEE Xplore | metadata/all-metadata search supported by platform | field wrappers, quote syntax, query splitting if platform limit requires it | deleting semantic terms or adding relevance filters |
| ACM Digital Library | advanced search / full bibliographic search | field syntax and platform quoting | restricting to one ACM venue unless recorded |
| Scopus | TITLE-ABS-KEY when supported | field wrapper and platform operators | adding subject-area filters silently |
| Web of Science Core Collection | Topic/TS when supported | TS field wrapper and platform operators | silently changing database collection |
| ScienceDirect | advanced search | platform field/length adaptation; split long query if necessary | treating ScienceDirect as equivalent to Scopus |
| SpringerLink | advanced/broad search supported by platform | quote/Boolean/query-length adaptation | undocumented content-type filtering |
| PubMed | title/abstract or broad text-word translation appropriate to platform | PubMed field tags and phrase handling | MeSH-only replacement of frozen free-text concepts |

## Query splitting
If a platform cannot accept a complete Qxx string:
1. split only for mechanical length/platform limits;
2. preserve the union of all frozen terms;
3. assign subruns such as `Q02a`, `Q02b`;
4. record every exact subquery in the registry;
5. combine exported records before cross-query deduplication;
6. document the limitation.

## Date handling
No lower publication bound. Upper frozen window: 2026-10-05 inclusive. If a platform only supports year-level publication filters, record that limitation and preserve the exact execution date so post-export eligibility can enforce the frozen date.

## Verification before each execution
- source/platform identity confirmed;
- Q ID and specialist block confirmed;
- semantic term set unchanged;
- date/filter behavior recorded;
- export format chosen;
- destination path prepared;
- registry row ID reserved.

**Never backfill an “exact executed query” from memory. Copy it from the platform at execution time.**
