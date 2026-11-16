"""r7813+70: sum each KFAC's KSLICE pieces into one bank, with the instrument's config.

Writes out/control_planck2018_kfac{2,3}.npz (ls, Dl, l_A, D_M, r_s, arm, config, n_slices).
Refuses to write if any slice is missing or did not finish rc=0.
"""
import glob
import json
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = '/tmp/n70/r7813'
OUT = os.path.join(HERE, 'out')
os.makedirs(OUT, exist_ok=True)

for kf in (2, 3):
    d = os.path.join(SRC, f'k{kf}')
    n = int(open(os.path.join(d, 'NMODES')).read().strip())
    starts = list(range(0, n, 250))
    Dl, ref, cfg = None, None, None
    for i in starts:
        log = os.path.join(d, f'k{kf}_s{i}.log')
        if not (os.path.exists(log) and re.search(r'^__DONE__ rc=0', open(log).read(), re.M)):
            sys.exit(f'KFAC={kf}: slice {i} not finished')
        with np.load(os.path.join(d, f'k{kf}_s{i}.npz'), allow_pickle=True) as z:
            if Dl is None:
                ref = {k: z[k] for k in ('ls', 'l_A', 'D_M', 'r_s', 'arm')}
                Dl = np.zeros_like(np.asarray(z['Dl'], float))
                cfg = json.loads(str(z['config']))
            assert np.array_equal(z['ls'], ref['ls'])
            Dl += np.asarray(z['Dl'], float)
    cfg.pop('KSLICE', None)
    assert cfg.get('KFAC') == float(kf), cfg.get('KFAC')
    fn = os.path.join(OUT, f'control_planck2018_kfac{kf}.npz')
    np.savez(fn, Dl=Dl, config=json.dumps(cfg, sort_keys=True), n_slices=len(starts), **ref)
    print(f'  KFAC={kf}: {len(starts)} slices of {n} modes -> {fn}')
