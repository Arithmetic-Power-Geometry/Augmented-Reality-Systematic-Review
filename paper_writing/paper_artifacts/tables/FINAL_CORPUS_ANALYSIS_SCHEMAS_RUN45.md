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
