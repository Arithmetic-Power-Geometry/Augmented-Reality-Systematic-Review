#!/usr/bin/env python3
"""Self-contained fixture test for ingest_search_exports.py; safe synthetic data only."""
import csv, hashlib, subprocess, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SCRIPT=ROOT/"scripts"/"ingest_search_exports.py"
with tempfile.TemporaryDirectory() as td:
    d=Path(td); raw=d/"fixture.csv"; reg=d/"registry.csv"; out=d/"out"
    rows=[
      {"Title":"AR Tracking Study","Authors":"Doe, Jane; Roe, John","Year":"2025","DOI":"https://doi.org/10.1000/ABC.1"},
      {"Title":"AR Tracking Study","Authors":"Doe, Jane; Roe, John","Year":"2025","DOI":"10.1000/abc.1"},
      {"Title":"AR Tracking Study Extended","Authors":"Doe, Jane","Year":"2025","DOI":""}]
    with raw.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    h=hashlib.sha256(raw.read_bytes()).hexdigest()
    fields=["search_run_id","source","query_id","concept_block","exact_executed_query","execution_date","date_from","date_to","filters","raw_result_count","exported_count","export_file","export_sha256","access_limitation","operator_or_tool","status","notes"]
    with reg.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerow({"search_run_id":"SRTEST","source":"TESTDB","query_id":"Q00","exported_count":"3","export_file":str(raw),"export_sha256":h,"status":"EXECUTED"})
    subprocess.run(["python3",str(SCRIPT),"--registry",str(reg),"--source","TESTDB","--search-run-id","SRTEST","--query-id","Q00","--input",str(raw),"--outdir",str(out)],check=True)
    pooled=list(csv.DictReader((out/"pooled_raw_index.csv").open()))
    cand=list(csv.DictReader((out/"dedup_candidates.csv").open()))
    assert len(pooled)==3
    assert pooled[0]["doi_normalized"]=="10.1000/abc.1"
    assert any(x["match_basis"]=="EXACT_DOI" for x in cand)
    print("SELF_TEST_PASS: 3 records parsed; DOI normalized; exact DOI duplicate candidate emitted")
