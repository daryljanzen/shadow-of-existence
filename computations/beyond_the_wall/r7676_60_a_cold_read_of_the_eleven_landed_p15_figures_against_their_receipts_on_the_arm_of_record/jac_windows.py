#!/usr/bin/env python3
"""r7676 (60) -- MEASURE the Jacobian over the window the SENTENCE names and the one the BANK uses.

`l.1889-1890` says the Jacobian `runs 0.788 to 0.911 across +-3 HALF-WIDTHS of the visibility`.  The
bank that carries those two numbers builds its grid in `computations/beyond_the_wall/r6919_directions
/geom.py` as `linspace(ETA_LS - 3*w, ETA_LS + 3*w, 201)` with `w = M.ETA_LS_W`, and
`ACOUSTIC_two_arm.py:600` defines `ETA_LS_W` as *its FWHM in conformal time*.

⌗ So the question is a MEASUREMENT, not a reading of words: evaluate the same `Jac_of` over both
windows at the same parameters and print both.  The arm's parameters are `geom.py`'s own `ENV['cr']`,
used verbatim so this script cannot choose them.
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BTW = os.path.dirname(HERE)          # computations/beyond_the_wall, where ACOUSTIC_two_arm lives

CODE = '''
import numpy as np, json, ACOUSTIC_two_arm as M
w = M.ETA_LS_W                      # the FWHM in conformal time (ACOUSTIC_two_arm.py:600)
out = {}
for name, half in (('pm3_FWHM', 3.0 * w),            # geom.py's own grid: the bank's window
                   ('pm3_halfwidths', 3.0 * w / 2),  # the window l.1890 names
                   ('pm1p5_FWHM', 1.5 * w)):         # the same thing, named the other way
    e = np.linspace(M.ETA_LS - half, M.ETA_LS + half, 201)
    J = M.Jac_of(e)
    out[name] = (float(J.min()), float(J.max()))
print("__W__" + json.dumps(dict(arm=str(M.ARM), fwhm=float(w), eta_ls=float(M.ETA_LS),
                                windows=out)))
'''
# geom.py's ENV['cr'], verbatim
ENV = dict(ARM='cr', CRH0='68.581133', CROM='0.297209', ZSTART='3e7', LEAFSCALES='1',
           WBH2='0.021524', NS='0.997952', NODE='60', PYTHONPATH=BTW)
r = subprocess.run([sys.executable, '-c', CODE], cwd=BTW, env={**os.environ, **ENV},
                   capture_output=True, text=True, timeout=600)
line = [ln for ln in r.stdout.splitlines() if ln.startswith('__W__')]
if not line:
    sys.exit(f'no geometry line\n{r.stdout[-1200:]}\n{r.stderr[-1200:]}')
d = json.loads(line[0][5:])
for nm, (lo, hi) in d['windows'].items():
    print(f"  {nm:<18} Jac {lo:.6f} - {hi:.6f}   spread {100 * (hi - lo):.2f} pp")
json.dump(d, open(os.path.join(HERE, 'jac_windows.json'), 'w'), indent=1)
print(f"  FWHM = {d['fwhm']:.4f},  eta_LS = {d['eta_ls']:.4f}   -> jac_windows.json")
