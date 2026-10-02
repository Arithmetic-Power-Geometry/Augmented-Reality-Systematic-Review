#!/usr/bin/env python3
import json,platform,subprocess,sys
from pathlib import Path
def cmd(x):
    try:return subprocess.check_output(x,text=True,stderr=subprocess.STDOUT).strip()
    except Exception:return None
out={
 "platform":platform.platform(),"machine":platform.machine(),"processor":platform.processor(),
 "python":platform.python_version(),"cpu_count":__import__("os").cpu_count(),
 "lscpu":cmd(["lscpu"]),"memory":cmd(["bash","-lc","free -b"]),
 "gpu_nvidia_smi":cmd(["bash","-lc","command -v nvidia-smi >/dev/null && nvidia-smi -L || true"]),
 "docker":cmd(["bash","-lc","command -v docker >/dev/null && docker --version || true"])
}
Path(sys.argv[1]).write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print("HARDWARE_PROVENANCE_WRITTEN")
