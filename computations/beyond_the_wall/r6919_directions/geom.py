"""bank the two arms' PROJECTION GEOMETRY across the visibility -- r6919+cc66.42.

What `r6919` ⓶ asks to swap one at a time are two geometric factors, and the numbers that say whether
they are separable are properties of the background rather than of any run.  This writes them once,
per arm, so the receipt reads them instead of re-importing the instrument twice.

  * `Jac = d eta_leaf / d eta_stack` across +-3 FWHM -- 1.000000 on the control by rate identity.
  * `d r_s` across the FWHM on the arm's OWN clock and on the stacking clock.
  * `d chi` across the FWHM, which is d eta exactly, because x0 = eta_0 - eta on both arms.
  * their ratio: the sound speed the KERNEL sees, d r_s / d chi.
"""
import os, subprocess, sys
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = '''
import numpy as np, json, ACOUSTIC_two_arm as M
w = M.ETA_LS_W
rs = M.rs_leaf_of if M.LEAFSCALES else M.rs_stack_of
lo, hi = M.ETA_LS - w / 2, M.ETA_LS + w / 2
e3 = np.linspace(M.ETA_LS - 3 * w, M.ETA_LS + 3 * w, 201)
J = M.Jac_of(e3)
print("__J__" + json.dumps(dict(
    arm=str(M.ARM), leafscales=bool(M.LEAFSCALES), eta_ls=float(M.ETA_LS), fwhm=float(w),
    jac_lo=float(J.min()), jac_hi=float(J.max()), jac_pk=float(M.Jac_of(M.ETA_LS)),
    d_rs_own=float(rs(hi) - rs(lo)), d_rs_stack=float(M.rs_stack_of(hi) - M.rs_stack_of(lo)),
    d_rs_leaf=float(M.rs_leaf_of(hi) - M.rs_leaf_of(lo)), d_chi=float(w),
    rs_ls_own=float(rs(M.ETA_LS)), R_S=float(M.R_S), D_M=float(M.D_M), l_A=float(M.L_A))))
'''
ENV = {'lcdm': dict(ARM='lcdm', LH0='67.410309', LOM='0.309826', WBH2='0.021966', NS='0.954248'),
       'cr': dict(ARM='cr', CRH0='68.581133', CROM='0.297209', ZSTART='3e7', LEAFSCALES='1',
                  WBH2='0.021524', NS='0.997952')}
out = {}
for arm, env in ENV.items():
    r = subprocess.run([sys.executable, '-c', CODE], cwd=os.path.join(HERE, '..'),
                       env={**os.environ, **env}, capture_output=True, text=True)
    line = [ln for ln in r.stdout.splitlines() if ln.startswith('__J__')]
    if not line:
        sys.exit(f'{arm}: no geometry line\n{r.stdout[-800:]}\n{r.stderr[-800:]}')
    import json
    d = json.loads(line[0][5:])
    for k, v in d.items():
        out[f'{k}__{arm}'] = np.array(v)
    print(f"  {arm}: Jac {d['jac_lo']:.6f}-{d['jac_hi']:.6f}, d r_s(own) {d['d_rs_own']:.4f}, "
          f"d chi {d['d_chi']:.3f}, d r_s / d chi {d['d_rs_own']/d['d_chi']:.6f}")
np.savez(os.path.join(HERE, '..', 'spectra', 'r6919_geometry.npz'), **out)
print('  -> spectra/r6919_geometry.npz')
