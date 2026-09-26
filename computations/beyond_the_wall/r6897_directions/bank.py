"""Bank r6897's runs into computations/beyond_the_wall/spectra."""
import os, glob, numpy as np
SP='/home/user/shadow-of-existence/computations/beyond_the_wall/spectra'
D='/tmp/n66/r6897'
def rc(lg):
    if not os.path.exists(lg): return None
    for L in open(lg):
        if L.startswith('__DONE__'): return int(L.split('rc=')[1])
    return None
# ---- the fields at the visibility peak -----------------------------------------------------------
F={}
for tag in ('lcdm','cr','wblo','wbhi'):
    p=f"{D}/zp/fields_{tag}.npz"
    if not os.path.exists(p): print(f"  fields {tag}: not ready"); continue
    d=np.load(p)
    for key in ('k','th0','psi','phi','tb'):
        F[f"{key}__{tag}"]=d[key].astype(np.float64)
    for key in ('eta','eta_ls','eta_ls_w','a_ls','R_eta','R_peak','rb_rec','a_rec','z_rec',
                'ombh2','r_s','D_M'):
        F[f"{key}__{tag}"]=np.float64(d[key])
    F[f"arm__{tag}"]=str(d['arm'])
if F:
    np.savez_compressed(os.path.join(SP,'r6897_fields.npz'), **F)
    print(f"  r6897_fields.npz: {sorted({k.split('__')[1] for k in F})}, "
          f"{os.path.getsize(os.path.join(SP,'r6897_fields.npz'))/1024:.0f} kB")
# ---- the no-op pair: the ZPSAVE edit with the switch unset ----------------------------------------
N={}
for arm in ('lcdm','cr'):
    p2=f"{D}/noop/noop_{arm}.npz"
    if not os.path.exists(p2): print(f"  noop {arm}: not ready"); continue
    d=np.load(p2)
    N[f"ls__{arm}"]=d['ls'].astype(np.int32); N[f"Dl__{arm}"]=d['Dl'].astype(np.float64)
    N[f"rc__{arm}"]=np.int32(rc(f"{D}/noop/noop_{arm}.log") or 0)
if len(N)>=4:
    np.savez_compressed(os.path.join(SP,'r6897_noop.npz'), **N)
    print("  r6897_noop.npz: both arms")

# ---- the control's omega_b response, summed over KSLICE pieces ------------------------------------
W={}; miss=[]
WB=['0.02020872','0.02108736','0.021966','0.02284464','0.02372328']
for w in WB:
    sl=sorted(glob.glob(f"{D}/wb/wb{w}_k*.npz"), key=lambda q:int(q.split('_k')[-1][:-4]))
    n_expected=len(range(0,2547,250))
    if len(sl)!=n_expected: miss.append(f"{w}:{len(sl)}/{n_expected}"); continue
    ls=None; tot=None
    for q in sl:
        d=np.load(q)
        if ls is None: ls=d['ls'].astype(np.int32); tot=np.zeros(len(ls))
        tot=tot+d['Dl'].astype(np.float64)
    d0=np.load(sl[0])
    W[f"ls__{w}"]=ls; W[f"Dl__{w}"]=tot; W[f"nsl__{w}"]=np.int32(len(sl))
    W[f"lA__{w}"]=np.float64(d0['l_A']); W[f"rs__{w}"]=np.float64(d0['r_s'])
    W[f"DM__{w}"]=np.float64(d0['D_M'])
if W:
    W['omega_b']=np.array([float(x) for x in WB if f"ls__{x}" in W])
    W['missing']=np.array(miss, dtype=object)
    np.savez_compressed(os.path.join(SP,'r6897_wb_response_lcdm.npz'), **W)
    print(f"  r6897_wb_response_lcdm.npz: {len(W['omega_b'])} of 5 omega_b, missing={miss}")
else:
    print(f"  wb response: nothing complete yet ({miss})")
