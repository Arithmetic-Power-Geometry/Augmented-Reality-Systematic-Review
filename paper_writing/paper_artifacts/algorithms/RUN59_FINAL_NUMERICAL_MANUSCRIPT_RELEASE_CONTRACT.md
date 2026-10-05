# Run 59 — Final Numerical Manuscript Release Contract

The following manuscript fields are generated only after the executable final-corpus gate returns PASS:

1. final numerical Abstract;
2. final PRISMA counts;
3. final included-report and included-study counts;
4. corpus-wide percentages;
5. verified-gap prevalence;
6. final Results;
7. final Conclusions.

## Denominator rule
Every percentage must name or mechanically inherit its denominator from a frozen included-study/report ledger. Pilot Corpus V1 is never a final denominator.

## PRISMA rule
Identification, screening, retrieval, full-text exclusion and inclusion counts are derived from versioned ledgers. No manually estimated count is accepted.

## Gap-prevalence rule
A gap contributes to final prevalence only when its state is promoted by the frozen gap-promotion logic after reported support, observed support, persistence, contradiction, reproducibility and closest-prior-work checks. Candidate/pilot gaps are excluded from the final numerator.

## Release rule
The generator exits BLOCKED unless the final corpus gate has passed. Thus a manuscript cannot accidentally acquire final-looking numbers before genuine selection and verification are complete.
