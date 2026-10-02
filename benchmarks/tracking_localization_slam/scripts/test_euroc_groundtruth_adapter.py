#!/usr/bin/env python3
import csv,subprocess,sys,tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[3]
conv=root/"benchmarks/tracking_localization_slam/adapters/euroc_groundtruth_to_common.py"
with tempfile.TemporaryDirectory() as d:
 p=Path(d); src=p/"gt.csv"; out=p/"out.csv"
 src.write_text("#timestamp [ns],p_RS_R_x [m],p_RS_R_y [m],p_RS_R_z [m],q_RS_w [],q_RS_x [],q_RS_y [],q_RS_z [],v_RS_R_x [m s^-1]\n"
                "1000000000,1,2,3,0.5,0.5,0.5,0.5,9\n"
                "1500000000,4,5,6,1,0,0,0,8\n",encoding="utf-8")
 subprocess.check_call([sys.executable,str(conv),str(src),str(out)])
 rows=list(csv.DictReader(out.open()))
 assert rows[0]["timestamp"]=="1.0"
 assert [float(rows[0][k]) for k in ["tx","ty","tz"]]==[1,2,3]
 assert [float(rows[0][k]) for k in ["qx","qy","qz","qw"]]==[.5,.5,.5,.5]
 assert rows[1]["timestamp"]=="1.5"
 assert [float(rows[1][k]) for k in ["qx","qy","qz","qw"]]==[0,0,0,1]
 # Wrong semantic header must fail.
 bad=p/"bad.csv"; bad.write_text("timestamp,x,y,z,qx,qy,qz,qw\n1,0,0,0,0,0,0,1\n2,0,0,0,0,0,0,1\n")
 rc=subprocess.run([sys.executable,str(conv),str(bad),str(p/"badout.csv")]).returncode
 assert rc!=0
print("EUROC_GT_CONVERTER_TESTS_OK")
