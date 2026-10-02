#!/usr/bin/env python3
import importlib.util,math,tempfile
from pathlib import Path
import numpy as np
p=Path(__file__).resolve().parents[1]/"evaluator"/"trajectory_metrics.py"
s=importlib.util.spec_from_file_location("ev",p); ev=importlib.util.module_from_spec(s); s.loader.exec_module(ev)

def traj(xs,offset=(0,0,0),yaw=0):
    c=math.cos(yaw/2); z=math.sin(yaw/2)
    rows=[]
    R=np.array([[math.cos(yaw),-math.sin(yaw),0],[math.sin(yaw),math.cos(yaw),0],[0,0,1]])
    off=np.array(offset,float)
    for i,x in enumerate(xs):
        pos=R@np.array([x,0,0],float)+off
        rows.append([float(i),*pos,0,0,z,c])
    return np.array(rows,float)

# Test 1: identical trajectories => all zero.
g=traj([0,1,2,3]); e=g.copy()
m=ev.evaluate(g,e,0.001)
assert m["ate_rmse_m"]<1e-12
assert m["rpe_translation_rmse_m"]<1e-12
assert m["rpe_rotation_rmse_deg"]<1e-9

# Test 2: global rigid transform must disappear under SE3 alignment.
e=traj([0,1,2,3],offset=(10,-4,2),yaw=0.7)
m=ev.evaluate(g,e,0.001)
assert m["ate_rmse_m"]<1e-10, m
assert m["rpe_translation_rmse_m"]<1e-10, m
assert m["rpe_rotation_rmse_deg"]<1e-6, m

# Test 3: scale drift must NOT disappear because scale correction is forbidden.
e=traj([0,2,4,6])
m=ev.evaluate(g,e,0.001)
assert m["ate_rmse_m"]>0.5, m
assert abs(m["rpe_translation_rmse_m"]-1.0)<1e-10, m

# Test 4: known timestamp offset inside tolerance associates; outside fails.
e=g.copy(); e[:,0]+=0.005
assert ev.evaluate(g,e,0.01)["associated_pose_count"]==4
try:
    ev.evaluate(g,e,0.001)
except ValueError:
    pass
else:
    raise AssertionError("association tolerance guard failed")
print("EVALUATOR_MATH_TESTS_OK")
