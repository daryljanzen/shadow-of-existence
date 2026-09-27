"""r6929's geometry scan -- the assignment as a CONTINUOUS parameter, not two settings.

*`r6929`'s order: the comb has been promoted to arbiter, so measure how sharply it discriminates.
Let the weighting on `tau` run from the stacking clock to the leaf's through a one-parameter family
-- `VISLEAF` as a FRACTION -- and report, against that parameter, `l_1/l_A` against the sky's 0.7312,
the retained fraction and its q-slope, and d r_s / d chi.*

  ⛭ ** THIS HALF IS A PROPERTY OF THE BACKGROUND AND COSTS ONE IMPORT PER POINT. **  `ETA_LS`, its
    FWHM, `r_D`, `R_S`, `l_A` and d r_s/d chi across the visibility are all module-level, so the
    fifteen-point scan on both arms is thirty imports and no solver.  ** The comb's half needs real
    spectra and is `launch.sh`'s. **
  ⚑ AND `l_A(f)` IS WHAT SEPARATES THE ORDER'S GUARD: if the comb moves only because the visibility
    peak relocates, `l_1` follows `l_A = pi D_M / r_s(ETA_LS)` and `l_1/l_A` is INVARIANT.  So the
    ratio the order asks for is already the peak-relocation part divided out.
"""
import json
import os
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.join(HERE, '..')
SP = os.path.join(BTW, 'spectra')

FS = [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.9, 1.0]
ENV = {'lcdm': dict(ARM='lcdm', LH0='67.410309', LOM='0.309826', WBH2='0.021966', NS='0.954248'),
       'cr': dict(ARM='cr', CRH0='68.581133', CROM='0.297209', ZSTART='3e7', LEAFSCALES='1',
                  WBH2='0.021524', NS='0.997952')}

CODE = '''
import numpy as np, json, ACOUSTIC_two_arm as M
w = M.ETA_LS_W
rs = M.rs_leaf_of if M.LEAFSCALES else M.rs_stack_of
lo, hi = M.ETA_LS - w / 2, M.ETA_LS + w / 2
print("__J__" + json.dumps(dict(
    arm=str(M.ARM), visleaf=float(M._VISLF), eta_ls=float(M.ETA_LS), fwhm=float(w),
    cs=float((rs(hi) - rs(lo)) / w), d_rs=float(rs(hi) - rs(lo)),
    rs_stack=float(M.rs_stack_of(M.ETA_LS)), rs_leaf=float(M.rs_leaf_of(M.ETA_LS)),
    rD=float(np.sqrt(M._kD2inv[M._gi])), R_S=float(M.R_S), l_A=float(M.L_A), D_M=float(M.D_M),
    tau_ls=float(M.tau_of(M.ETA_LS)), jac_ls=float(M.Jac_of(M.ETA_LS)))))
'''


def one(job):
    arm, f = job
    r = subprocess.run([sys.executable, '-c', CODE], cwd=BTW, capture_output=True, text=True,
                       env={**os.environ, **ENV[arm], 'VISLEAF': repr(f),
                            'OMP_NUM_THREADS': '1', 'OPENBLAS_NUM_THREADS': '1'})
    ln = [x for x in r.stdout.splitlines() if x.startswith('__J__')]
    if not ln:
        sys.exit(f'{arm} VISLEAF={f}: no geometry line\n{r.stdout[-400:]}\n{r.stderr[-800:]}')
    d = json.loads(ln[0][5:])
    # ⚠ the guard the launcher uses, applied here too: the switch must ARRIVE as the value asked for
    assert abs(d['visleaf'] - f) < 1e-12, f'{arm}: asked VISLEAF={f}, the instrument parsed {d["visleaf"]}'
    return arm, f, d


if __name__ == '__main__':
    jobs = [(a, f) for a in ENV for f in FS]
    with ProcessPoolExecutor(max_workers=4) as ex:
        res = list(ex.map(one, jobs))
    out = {}
    for arm in ENV:
        rows = [d for a, f, d in res if a == arm]
        fs = [f for a, f, d in res if a == arm]
        out[f'f__{arm}'] = np.array(fs, float)
        for k in rows[0]:
            if k == 'arm':
                continue
            out[f'{k}__{arm}'] = np.array([r[k] for r in rows], float)
    np.savez(os.path.join(SP, 'r6929_geometry.npz'), **out)
    print(f'  the geometry over {len(FS)} values of VISLEAF on both arms '
          f'-> spectra/r6929_geometry.npz')
    for arm in ENV:
        print(f'  {arm}:')
        print('    ' + '  '.join(f'{x:>9s}' for x in
                                 ('VISLEAF', 'eta_LS', 'FWHM', 'r_D', 'l_A', 'dr_s/dchi')))
        for i, f in enumerate(out[f'f__{arm}']):
            print('    ' + '  '.join(f'{v:9.4f}' for v in (
                f, out[f'eta_ls__{arm}'][i], out[f'fwhm__{arm}'][i], out[f'rD__{arm}'][i],
                out[f'l_A__{arm}'][i], out[f'cs__{arm}'][i])))
