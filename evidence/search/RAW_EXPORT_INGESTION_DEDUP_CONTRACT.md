# Raw Export Ingestion and Deduplication Contract — NEXT-05

## Principle
Raw database exports are immutable evidence. All normalization, merging, deduplication and screening occur on derived files.

## Raw storage
`evidence/search/raw_exports/<source>/<search_run_id>_<query_id>_<date>.<ext>`

For every raw export:
- preserve original bytes;
- compute SHA-256;
- record raw result count and exported count separately;
- record partial-export/API/page limits;
- never edit the raw file to fix metadata.

## Canonical pooled schema
Each exported record becomes one row with:
`record_id, source, search_run_id, query_id, title_raw, title_normalized, authors_raw, first_author_normalized, year, doi_raw, doi_normalized, stable_id_type, stable_id, venue, abstract, url_or_locator, source_record_id, raw_export_file, raw_row_or_record, study_family_id, dedup_status, canonical_record_id`.

## Normalization
- DOI: lowercase; strip DOI URL/prefix and surrounding whitespace.
- Title: Unicode normalization; lowercase comparison copy; collapse whitespace; normalize punctuation for matching while preserving raw title.
- Author: preserve raw list; create normalized first-author comparison field.
- Year: preserve source value; conflicts are adjudicated, not silently overwritten.

## Deduplication order
1. exact normalized DOI;
2. exact stable identifier (PMID, database accession, etc.);
3. exact normalized title;
4. fuzzy normalized title + first author + year → **manual verification required**.

A fuzzy match never auto-deletes a record.

## Companion/study-family rule
Preprint, conference and journal reports may belong to one study family but are not automatically duplicates. The most complete peer-reviewed report is canonical unless another report contains materially distinct experiments, datasets, populations or outcomes.

## Audit outputs
Derived processing must produce:
- `pooled_raw_index.csv`;
- `dedup_decisions.csv`;
- `study_family_ledger.csv`;
- `screening_master.csv`;
- checksum manifest for each frozen stage.

## PRISMA arithmetic gate
Identification and screening totals are computed from frozen derived ledgers, never typed manually into the manuscript.
