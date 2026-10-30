"""r7641+70: r6929's geometry scan with the ARM OF RECORD's arm -- r6929_directions/geom.py's own probe (`CODE`,
`one`), lifted unchanged; only the arm's environment moves (LEAFREC=1 is the instrument default).  The control's
keys are the namesake's own.  -> spectra/r6929_geometry_leafrec1.npz"""
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'r6929_directions'))
import geom  # noqa: E402

geom.ENV['cr'] = dict(ARM='cr', CRH0='68.570730', CROM='0.291246', ZSTART='3e7', LEAFSCALES='1', LEAFREC='1',
                      WBH2='0.021643', NS='1.015066')
SP = os.path.join(HERE, '..', 'spectra')
if __name__ == '__main__':
    old = np.load(os.path.join(SP, 'r6929_geometry.npz'), allow_pickle=True)
    out = {k: old[k] for k in old.files if k.endswith('__lcdm')}
    with ProcessPoolExecutor(4) as ex:
        R = sorted(ex.map(geom.one, [('cr', f) for f in geom.FS]), key=lambda r: r[1])
    keys = [k[:-4] for k in old.files if k.endswith('__cr')]
    for k in keys:
        out[k + '__cr'] = np.array([r[1] if k == 'f' else r[2][k] for r in R])
    import subprocess
    r = subprocess.run([sys.executable, '-c', 'import ACOUSTIC_two_arm as M; print("__C__" + str(M._resolved_config()))'],
                       cwd=os.path.join(HERE, '..'), capture_output=True, text=True,
                       env={**os.environ, **geom.ENV['cr'], 'OMP_NUM_THREADS': '1'})
    out['config'] = np.array(next(l[5:] for l in r.stdout.splitlines() if l.startswith('__C__')))   # the arm's, VISLEAF scanned
    out['manifest'] = np.array(json.dumps(dict(file='spectra/r6929_geometry_leafrec1.npz', namesake='spectra/r6929_geometry.npz',
        LEAFREC=1, point=geom.ENV['cr'], held="r6929 geom.py's probe unchanged; the control's keys are the namesake's own")))
    np.savez(os.path.join(SP, 'r6929_geometry_leafrec1.npz'), **out)
    lA = out['l_A__cr']
    print(f"  arm of record: l_A over VISLEAF {lA.min():.6f}..{lA.max():.6f} (spread {lA.max()-lA.min():.2e}); "
          f"FWHM {out['fwhm__cr'].min():.3f}..{out['fwhm__cr'].max():.3f}; rD {out['rD__cr'][0]:.4f} -> {out['rD__cr'][-1]:.4f}")
    o = old
    print(f"  old arm      : l_A spread {o['l_A__cr'].max()-o['l_A__cr'].min():.2e}; FWHM {o['fwhm__cr'].min():.3f}..{o['fwhm__cr'].max():.3f}; "
          f"rD {o['rD__cr'][0]:.4f} -> {o['rD__cr'][-1]:.4f}")
