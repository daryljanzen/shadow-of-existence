"""Bank r6891's runs into computations/beyond_the_wall/spectra.

  r6893_switch_screen_{arm}.npz   the sweep, one key group per tag            (already banked)
  r6893_full_reach_nulls_lcdm.npz the nine off-path switches at LMAXL=2000
  r6893_fine_grid_{arm}.npz       fineA (LSTEP=2 LMAXL=900, whole) and fineB
                                  (LSTEP=4 LMAXL=2000, SUMMED over k-slices), plus the
                                  slice-additivity pair at the screen grid
"""
import os, glob, sys, numpy as np
SP='/home/user/shadow-of-existence/computations/beyond_the_wall/spectra'
D='/tmp/n66/r6893'
def rc(log):
    if not os.path.exists(log): return None
    for L in open(log):
        if L.startswith('__DONE__'): return int(L.split('rc=')[1])
    return None
def put(D_, key, p):
    d=np.load(p)
    D_[f"ls__{key}"]=d['ls'].astype(np.int32); D_[f"Dl__{key}"]=d['Dl'].astype(np.float64)
    D_[f"lA__{key}"]=np.float64(d['l_A']); D_[f"DM__{key}"]=np.float64(d['D_M'])
    D_[f"rs__{key}"]=np.float64(d['r_s'])

# ---- the full-reach nulls -----------------------------------------------------------------------
out={}; fail=[]
for p in sorted(glob.glob(f"{D}/full/*_lcdm.npz")):
    t=os.path.basename(p)[:-4]
    if t.startswith('junk'): continue
    put(out, t[:-5], p); out[f"rc__{t[:-5]}"]=np.int32(rc(f"{D}/full/{t}.log") or 0)
for lg in sorted(glob.glob(f"{D}/full/*_lcdm.log")):
    t=os.path.basename(lg)[:-4]
    if t.startswith('junk'): continue
    if rc(lg) not in (0,) or not os.path.exists(f"{D}/full/{t}.npz"): fail.append(f"{t}:rc={rc(lg)}")
if [k for k in out if k.startswith('ls__')]:
    out['failed']=np.array(fail, dtype=object)
    np.savez_compressed(os.path.join(SP,'r6893_full_reach_nulls_lcdm.npz'), **out)
    print(f"  r6893_full_reach_nulls_lcdm.npz: {len([k for k in out if k.startswith('ls__')])} spectra, "
          f"failed={fail}")
else:
    print("  full-reach nulls: nothing yet")

# ---- the fine grid -----------------------------------------------------------------------------
for arm in ('lcdm','cr'):
    F={}; miss=[]
    for v in ('base','nufs0'):
        p=f"{D}/fine/fineA_{v}_{arm}.npz"
        if os.path.exists(p): put(F, f"fineA_{v}", p)
        else: miss.append(f"fineA_{v}")
        sl=sorted(glob.glob(f"{D}/fine/fineB_{v}_{arm}_k*.npz"),
                  key=lambda q:int(q.split('_k')[-1][:-4]))
        if sl:
            tot=None; ls=None
            for q in sl:
                d=np.load(q)
                if ls is None: ls=d['ls'].astype(np.int32); tot=np.zeros(len(ls))
                assert len(d['ls'])==len(ls)
                tot=tot+d['Dl'].astype(np.float64)
            d0=np.load(sl[0])
            F[f"ls__fineB_{v}"]=ls; F[f"Dl__fineB_{v}"]=tot
            F[f"lA__fineB_{v}"]=np.float64(d0['l_A']); F[f"DM__fineB_{v}"]=np.float64(d0['D_M'])
            F[f"rs__fineB_{v}"]=np.float64(d0['r_s'])
            F[f"nsl__fineB_{v}"]=np.int32(len(sl))
        else: miss.append(f"fineB_{v}")
    # the slice-additivity pair, at the screen grid
    sp=sorted(glob.glob(f"{D}/slice/sl_{arm}_*.npz"))
    if len(sp)==2:
        tot=None; ls=None
        for q in sp:
            d=np.load(q)
            if ls is None: ls=d['ls'].astype(np.int32); tot=np.zeros(len(ls))
            tot=tot+d['Dl'].astype(np.float64)
        F['ls__slicesum']=ls; F['Dl__slicesum']=tot
        d0=np.load(sp[0]); F['lA__slicesum']=np.float64(d0['l_A'])
        F['DM__slicesum']=np.float64(d0['D_M']); F['rs__slicesum']=np.float64(d0['r_s'])
    else: miss.append('slicesum')
    if [k for k in F if k.startswith('ls__')]:
        F['missing']=np.array(miss, dtype=object)
        np.savez_compressed(os.path.join(SP,f'r6893_fine_grid_{arm}.npz'), **F)
        print(f"  r6893_fine_grid_{arm}.npz: "
              f"{sorted(k[4:] for k in F if k.startswith('ls__'))}  missing={miss}")
    else:
        print(f"  fine grid {arm}: nothing yet (missing {miss})")
