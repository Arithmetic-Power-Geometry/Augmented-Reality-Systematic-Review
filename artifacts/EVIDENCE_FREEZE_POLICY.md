# Evidence Freeze Policy

A result is frozen when its raw inputs and provenance are immutable enough to reproduce the derived value.

## Freeze record
For each accepted run retain:
- experiment ID and run ID;
- complete upstream method SHA;
- configuration checksum;
- environment/container digest;
- hardware manifest;
- dataset ID/version/sequence;
- dataset integrity metadata;
- raw-output checksum;
- adapter revision;
- evaluator revision;
- metric record checksum.

## Corrections
A frozen result is never overwritten. If an error is found:
1. mark the old result invalid with a reason;
2. preserve it;
3. create a new run/result identifier;
4. document the correction.

## Paper-facing rule
Only frozen, valid results may populate generated paper figures/tables. Literature-reported values remain in a separate evidence layer.
