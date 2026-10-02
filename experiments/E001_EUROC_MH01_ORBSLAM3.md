# Experiment E001 — EuRoC MH_01_easy Baseline Reproduction

## Status
Pre-registered protocol. No scientific result is recorded by this document.

## Purpose
Establish the first controlled, provenance-complete execution path for the tracking/localization/SLAM workstream.

## Dataset
EuRoC MAV dataset, sequence `MH_01_easy`.

Dataset files are obtained from the official dataset source under its applicable terms. Dataset bytes are not committed to this repository.

## First method
ORB-SLAM3.

The initial smoke execution is not a method comparison. It validates the end-to-end evidence path.

## Mode
The exact ORB-SLAM3 sensor mode must match the selected EuRoC input contract and upstream example configuration. Mode, calibration and settings file are frozen in the run manifest before execution.

## Primary outputs
1. raw estimated trajectory;
2. normalized trajectory;
3. execution log;
4. run manifest;
5. dataset manifest/checksum record;
6. evaluator log;
7. machine-readable metric record.

## Primary accuracy metrics
- Absolute Trajectory Error (ATE), RMSE of translation after the preregistered alignment convention;
- Relative Pose Error (RPE), with delta and units explicitly stored.

Metric implementation/version must be frozen before the first scientific value is accepted.

## Secondary execution outcomes
- run success/failure;
- failure stage;
- wall-clock runtime;
- output pose count.

FPS, memory and energy are not primary metrics in E001 and must not be retroactively promoted because of favorable results.

## Failure rules
A run is a failure if any of the following occurs:
- process exits non-zero;
- required sensor stream cannot be consumed;
- initialization never completes;
- tracking terminates without producing the minimum evaluable trajectory defined by the evaluator;
- raw output is malformed;
- evaluator rejects temporal association or trajectory integrity.

A failed run remains evidence and is never silently removed.

## Repetitions
The smoke gate uses one execution to establish plumbing. The scientific reproduction phase uses at least three executions if nondeterminism is observed or plausible. All repetitions are retained.

## Tuning rule
No parameter is tuned against the sequence ground truth. The first run uses the canonical upstream EuRoC configuration. Any later parameter study is a separate experiment family.

## Ground-truth rule
Ground truth is used only by the evaluator after inference. It must not enter the method execution path.

## Acceptance gate
E001 becomes a scientific artifact only when:
- exact method commit is a full immutable SHA;
- environment/container digest is recorded;
- dataset provenance and integrity are recorded;
- raw trajectory checksum is recorded;
- evaluator revision is recorded;
- metric output can be regenerated from retained raw output.

## Extension
After ORB-SLAM3 passes the evidence path, compatible VINS-Mono and OpenVINS runs may be registered as E002/E003 under the same sequence and common evaluation contract.
