"""Bank the screen (and, when present, the full-reach null re-runs and the fine-grid spectra) into
computations/beyond_the_wall/spectra as one npz per arm per stage, keyed by tag."""
import os, sys, glob, numpy as np
SP='/home/user/shadow-of-existence/computations/beyond_the_wall/spectra'
def rc(log):
    if not os.path.exists(log): return None
    for L in open(log):
        if L.startswith('__DONE__'): return int(L.split('rc=')[1])
    return None
def bank(srcdir, out, arm, strip):
    D={}
    for p in sorted(glob.glob(f"{srcdir}/*_{arm}.npz")):
        t=os.path.basename(p)[:-4]
        if t.startswith('junk'): continue
        k=t[:-(len(arm)+1)] if strip else t
        d=np.load(p)
        D[f"ls__{k}"]=d['ls'].astype(np.int32); D[f"Dl__{k}"]=d['Dl'].astype(np.float64)
        D[f"lA__{k}"]=np.float64(d['l_A']); D[f"DM__{k}"]=np.float64(d['D_M'])
        D[f"rs__{k}"]=np.float64(d['r_s'])
        D[f"rc__{k}"]=np.int32(rc(f"{srcdir}/{t}.log") if rc(f"{srcdir}/{t}.log") is not None else -1)
    fail=[]
    for lg in sorted(glob.glob(f"{srcdir}/*_{arm}.log")):
        t=os.path.basename(lg)[:-4]
        if t.startswith('junk'): continue
        r=rc(lg)
        if r not in (0,None) or not os.path.exists(f"{srcdir}/{t}.npz"):
            fail.append(f"{t}:rc={r}")
    D['failed']=np.array(fail, dtype=object)
    if len([k for k in D if k.startswith('ls__')])==0: return None
    np.savez_compressed(os.path.join(SP,out), **D)
    n=len([k for k in D if k.startswith('ls__')])
    print(f"  {out}: {n} spectra, {os.path.getsize(os.path.join(SP,out))/1024:.0f} kB")
    return n
for arm in ('lcdm','cr'):
    bank('/tmp/n66/r6891/screen', f'r6891_switch_screen_{arm}.npz', arm, True)
    bank('/tmp/n66/r6891/full',   f'r6891_full_reach_nulls_{arm}.npz', arm, True)
    bank('/tmp/n66/r6891/fine',   f'r6891_fine_grid_{arm}.npz', arm, True)
