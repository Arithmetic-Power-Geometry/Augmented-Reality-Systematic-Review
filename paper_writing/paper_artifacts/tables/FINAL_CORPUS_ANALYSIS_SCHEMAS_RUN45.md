# Final Corpus Analysis Schemas — Run 45

## Primary study extraction
study_id,study_family_id,canonical_report_id,year,domain_D,technology_T,hardware_H,sensing_S,algorithm_A,metrics_M,environment_E,users_U,reproducibility_R,task,dataset,benchmark,baseline,protocol,statistics,reported_result,limitation,code,data,model,configuration,hardware_spec,seeds,evaluator,raw_outputs,provenance_report

## Comparability pair ledger
pair_id,study_a,study_b,task_match,dataset_match,hardware_match,environment_match,user_match,protocol_match,metric_semantics_match,baseline_match,comparability_level_C0_C3,reason,evidence_refs

## Reproducibility ledger
study_id,reporting,materials,data,code,environment,protocol,executability,reproduction,replication,provenance,R_level,notes

## Contradiction/failure ledger
cluster_id,claim_a,claim_b,study_a,study_b,apparent_direction,condition_difference,comparability_level,failure_regime,contradiction_status,explanation,evidence_refs

## Gap-promotion ledger
gap_id,description,reported_support,observed_support,persistence_check,contradiction_check,reproducibility_check,closest_prior_work,experimental_actionability,state,decision,evidence_refs

## Result integrity rule
Every final numeric table must be regenerable from a frozen ledger keyed to included study IDs. No manually typed prevalence percentage is authoritative.


## Stage-4 condition-normalized contradiction ledger
cluster_id,claim_id_a,claim_id_b,study_a,study_b,task_match,user_match,device_match,sensing_match,environment_match,metric_semantics_match,comparator_match,protocol_match,deployment_maturity_match,C_level,outcome_direction_a,outcome_direction_b,normalized_status,failure_regime,evidence_refs

Allowed normalized_status: VERIFIED_CONTRADICTION | CONDITION_DEPENDENT | INSUFFICIENT_EVIDENCE | NOT_COMPARABLE.

## Stage-4 failure-regime ledger
failure_id,study_id,method,baseline_condition,trigger_condition,outcome_metric,direction,magnitude,environment,device,sensing,user_task,C_level,R_level,replication_state,evidence_refs

## Stage-4 closest-prior-work ledger
candidate_id,task,method,condition,outcome,corpus_matches,companion_matches,review_library_matches,citation_chase_matches,closest_record_id,distinguishing_feature,novelty_gate,evidence_refs

## Stage-4 sensitivity matrix
analysis_id,claim_id,sensitivity_type,reference_specification,alternative_specification,reference_result,alternative_result,direction_preserved,interpretation_preserved,notes,evidence_refs

Prespecified sensitivity_type values: DATABASE_SET | CODER | THRESHOLD | UNRESOLVED_FIELD | STUDY_FAMILY | STUDY_QUALITY | COMPARABILITY.

## Stage-4 RQ answer ledger
rq_id,answer_status,answer_text,n_studies,n_reports,denominator_definition,robustness_status,key_evidence_refs,sensitivity_refs,limitations

answer_status: ANSWERED | PARTIALLY_ANSWERED | INSUFFICIENT_EVIDENCE.
robustness_status: ROBUST | SENSITIVITY_DEPENDENT | NOT_TESTABLE.

## Stage-4 integrity rule
No candidate contradiction becomes VERIFIED_CONTRADICTION without condition normalization and adequate comparability. No sparse cell becomes VERIFIED_OPPORTUNITY without persistence, evidence-quality/reproducibility, contradiction, closest-prior-work and actionability gates. No RQ answer is final unless its denominator resolves to the same frozen corpus checksum.
