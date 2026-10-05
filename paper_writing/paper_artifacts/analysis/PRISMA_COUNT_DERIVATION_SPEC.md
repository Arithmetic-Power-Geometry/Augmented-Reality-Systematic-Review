# PRISMA Count Derivation Specification — NEXT-05

**Rule:** every flow count is computed from frozen ledgers. No manuscript count is entered manually.

## Identification
- database_records_identified = sum exported records from EXECUTED formal-search registry rows, accounting for documented split-query union handling;
- other_records_identified = supplementary discovery/citation-search records tracked separately;
- duplicate_records_removed = count of dedup decisions whose noncanonical record is removed as bibliographic duplicate;
- records_after_dedup = unique canonical bibliographic records entering title/abstract screening.

## Screening
- records_screened = records with final title/abstract decision;
- records_excluded_ta = title/abstract exclusions grouped by controlled reason;
- reports_sought = records advancing to full text;
- reports_not_retrieved = full texts explicitly marked not retrieved;
- reports_assessed = retrieved reports with final full-text decision;
- reports_excluded_ft = full-text exclusions grouped by controlled protocol code.

## Included
- included_reports = canonical reports passing full-text eligibility;
- included_studies = unique study_family_id among included reports after family resolution.

## Assertions checked before freeze
1. every included report has a canonical_record_id;
2. every included report belongs to exactly one study family;
3. every exclusion has a controlled reason;
4. no duplicate canonical IDs enter screening twice;
5. no record after 2026-10-05 is included;
6. secondary reviews are not counted in the primary-study corpus;
7. raw exports/checksums remain immutable;
8. counts reconcile algebraically across stages.

## Reconciliation identities
`records_after_dedup = records_screened`

`records_screened = records_excluded_ta + reports_sought`

`reports_sought = reports_not_retrieved + reports_assessed`

`reports_assessed = reports_excluded_ft + included_reports`

Any failure blocks NEXT-05.
