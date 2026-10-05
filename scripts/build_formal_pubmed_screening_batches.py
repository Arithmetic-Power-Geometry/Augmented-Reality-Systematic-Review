#!/usr/bin/env python3
import csv, hashlib
from pathlib import Path

SRC=Path("evidence/search/derived/pubmed/PUBMED_Q00_DETERMINISTIC_PRESCREEN_2026-10-05.csv")
OUT=Path("evidence/screening/formal_pubmed_batches")
OUT.mkdir(parents=True,exist_ok=True)

with SRC.open(encoding="utf-8", newline="") as f:
    rows=list(csv.DictReader(f))

eligible=[r for r in rows if r.get("prescreen_decision")=="UNCERTAIN_REQUIRES_SCREENING" and r.get("prescreen_reason")=="TITLE_ABSTRACT_REVIEW_REQUIRED"]
if len(rows)!=10198:
    raise SystemExit(f"FAIL: expected 10198 prescreen rows, got {len(rows)}")
if len(eligible)!=7728:
    raise SystemExit(f"FAIL: expected 7728 TA rows, got {len(eligible)}")

base_fields=["screening_ordinal","batch_id"] + list(eligible[0].keys())
decision_fields=["ta_decision","ta_reason_code","ta_screener","ta_timestamp","ta_evidence_note","decision_version","second_verification_state","adjudication_state"]
fields=base_fields+[x for x in decision_fields if x not in base_fields]

manifest=[]
for idx in range(31):
    lo=idx*250
    chunk=eligible[lo:min(lo+250,len(eligible))]
    bid=f"TA-{idx+1:02d}"
    path=OUT/f"{bid}.csv"
    with path.open("w",encoding="utf-8",newline="") as f:
        w=csv.DictWriter(f,fieldnames=fields)
        w.writeheader()
        for j,r in enumerate(chunk,start=lo+1):
            x={"screening_ordinal":j,"batch_id":bid,**r}
            for k in decision_fields: x.setdefault(k,"")
            w.writerow(x)
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    manifest.append((bid,lo+1,lo+len(chunk),len(chunk),path.as_posix(),digest))

mp=OUT/"BATCH_CHECKSUMS.csv"
with mp.open("w",encoding="utf-8",newline="") as f:
    w=csv.writer(f); w.writerow(["batch_id","start_ordinal","end_ordinal","records","path","sha256"]); w.writerows(manifest)

all_ids=[r.get("pmid","") for r in eligible]
if len(all_ids)!=len(set(all_ids)):
    raise SystemExit("FAIL: duplicate PMID found within TA screening set")
if sum(x[3] for x in manifest)!=7728:
    raise SystemExit("FAIL: batch cardinality mismatch")

summary=OUT/"README.md"
summary.write_text(
    "# Formal PubMed title/abstract batches\n\n"
    "Generated deterministically from the checksum-frozen Q00 prescreen.\n\n"
    "- Input rows: 10,198\n"
    "- TITLE_ABSTRACT_REVIEW_REQUIRED: 7,728\n"
    "- Batches: 31 (30 x 250; TA-31 = 228)\n"
    "- Duplicate PMID within TA set: 0\n\n"
    "Blank decision fields are intentional. These files are screening work units, not completed screening decisions. "
    "No automated inclusion/exclusion is asserted.\n",
    encoding="utf-8"
)
print("PASS: generated 31 batches covering 7728 unique PMIDs")

# Run 54 trigger: repository-native generation of immutable screening work units.
