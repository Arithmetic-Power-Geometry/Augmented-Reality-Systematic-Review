#!/usr/bin/env python3
"""Dependency-light trajectory evaluator for the AR review benchmark.

CSV input columns:
timestamp,tx,ty,tz,qx,qy,qz,qw

ATE: translation RMSE after rigid SE(3) Horn/Kabsch alignment (no scale).
RPE: consecutive associated-pose relative translation and rotation RMSE.
"""
import argparse,csv,json,math
from pathlib import Path
import numpy as np

COLS=["timestamp","tx","ty","tz","qx","qy","qz","qw"]

def load_csv(path):
    with Path(path).open(newline="",encoding="utf-8") as f:
        r=csv.DictReader(f)
        if r.fieldnames!=COLS: raise ValueError(f"expected header {COLS}")
        a=np.array([[float(row[k]) for k in COLS] for row in r],dtype=float)
    if len(a)<2: raise ValueError("trajectory needs at least two poses")
    if np.any(np.diff(a[:,0])<=0): raise ValueError("timestamps must increase")
    return a

def qrot(q):
    x,y,z,w=q
    n=math.sqrt(x*x+y*y+z*z+w*w)
    if n==0: raise ValueError("zero quaternion")
    x,y,z,w=x/n,y/n,z/n,w/n
    return np.array([
      [1-2*(y*y+z*z),2*(x*y-z*w),2*(x*z+y*w)],
      [2*(x*y+z*w),1-2*(x*x+z*z),2*(y*z-x*w)],
      [2*(x*z-y*w),2*(y*z+x*w),1-2*(x*x+y*y)]
    ])

def associate(gt,est,tol):
    pairs=[]; j=0
    for i in range(len(gt)):
        while j+1<len(est) and abs(est[j+1,0]-gt[i,0])<=abs(est[j,0]-gt[i,0]): j+=1
        if abs(est[j,0]-gt[i,0])<=tol: pairs.append((i,j))
    # enforce one-to-one estimated indices
    out=[]; used=set()
    for p in pairs:
        if p[1] not in used: out.append(p); used.add(p[1])
    if len(out)<2: raise ValueError("fewer than two timestamp associations")
    return out

def align_se3(P,Q):
    # Find R,t mapping estimate Q to ground truth P, no scale.
    pm=P.mean(0); qm=Q.mean(0)
    H=(Q-qm).T@(P-pm)
    U,_,Vt=np.linalg.svd(H)
    R=Vt.T@U.T
    if np.linalg.det(R)<0:
        Vt[-1,:]*=-1; R=Vt.T@U.T
    t=pm-R@qm
    return R,t

def angle_deg(R):
    c=max(-1.0,min(1.0,(np.trace(R)-1)/2))
    return math.degrees(math.acos(c))

def evaluate(gt,est,tol):
    pairs=associate(gt,est,tol)
    gi=np.array([i for i,_ in pairs]); ei=np.array([j for _,j in pairs])
    Pg=gt[gi,1:4]; Pe=est[ei,1:4]
    A,t=align_se3(Pg,Pe)
    PeA=(A@Pe.T).T+t
    ate=np.sqrt(np.mean(np.sum((PeA-Pg)**2,axis=1)))
    Rg=[qrot(gt[i,4:8]) for i in gi]
    Re=[A@qrot(est[j,4:8]) for j in ei]
    terr=[]; rerr=[]
    for k in range(len(pairs)-1):
        dg=Rg[k].T@(Pg[k+1]-Pg[k]); de=Re[k].T@(PeA[k+1]-PeA[k])
        terr.append(np.linalg.norm(de-dg))
        Rrelg=Rg[k].T@Rg[k+1]; Rrele=Re[k].T@Re[k+1]
        rerr.append(angle_deg(Rrelg.T@Rrele))
    return {
      "associated_pose_count":len(pairs),
      "ate_rmse_m":float(ate),
      "rpe_translation_rmse_m":float(np.sqrt(np.mean(np.square(terr)))),
      "rpe_rotation_rmse_deg":float(np.sqrt(np.mean(np.square(rerr))))
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("ground_truth"); ap.add_argument("estimate")
    ap.add_argument("--tolerance",type=float,default=0.01)
    ap.add_argument("--run-id",required=True); ap.add_argument("--output",required=True)
    a=ap.parse_args()
    m=evaluate(load_csv(a.ground_truth),load_csv(a.estimate),a.tolerance)
    rec={"run_id":a.run_id,"evaluator":"project-se3-evaluator-v1",
         "evaluator_commit":"PROJECT_COMMIT_AT_RUN",
         "alignment":{"type":"SE3_rigid","scale_correction":False},
         "association":{"method":"nearest_timestamp_one_to_one","tolerance_seconds":a.tolerance},
         "metrics":m,"valid":True,"invalid_reason":None}
    Path(a.output).write_text(json.dumps(rec,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(rec,indent=2))
if __name__=="__main__": main()
