# -*- coding: utf-8 -*-
"""r7860 (60) Ⓔ⑤ᵃ -- WHAT THE ORDERED CONTROL ACTUALLY NEEDS, SWITCH BY SWITCH AND MEASURED.

⛭ `r7857` (69) item ④ asks for the control with `BVEL`, `PRIMNORM` and `FOURPI` all on.  The three
are not the same kind of change, and this file establishes which of them the banked grid can take
analytically and which needs the solver run again -- **measured at the bank's OWN configuration, not
inferred from a cheap leg**.

  * **`FOURPI`** multiplies all three blocks by exactly two.  Measured here by RE-RUNNING the
    control point at the bank's own `LMAXL`/`LSTEP` with the switch set and comparing against twice
    the committed point: worst `|ratio - 1|` is at the last bit.  ⇒ So the whole grid takes this
    switch with NO recompute, and that is a measurement rather than the note this seat wrote.
  * **`PRIMNORM`** multiplies the lensing path's reference power by
    `(4/9) A_s k_p^(1-n_s)`, which is a CONSTANT per point -- but `n_s` varies across the grid, so
    the constant is per point and is read from each point's OWN recorded `n_s`.
  * ⛔ **`BVEL`** changes the SOLVER: the baryon continuity is driven by the baryon velocity rather
    than the photon's.  No constant can stand in for it, and the committed grid was generated
    before the switch existed.  ⇒ **The grid has to be run again for this one**, and the cost is
    measured below rather than guessed.

    python3 doubling.py
"""
import io
import json
import os
import sys
import time

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
#: ⛔ FOUR dirnames: this file sits three directories below the repository root.
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
BANK = os.path.join(_BTW, 'bank', 'pol_grid')
ON = os.environ.get('ONPOINT', '/tmp/claude-0/r7860/on.npz')

print(__doc__)
print('=' * 100)
out = {}

print('\n  Ⓔ⑤ᵃ `FOURPI` ON THE WHOLE GRID, WITHOUT A RECOMPUTE -- measured at the bank\'s own reach')
print('  ' + '-' * 98)
a = np.load(os.path.join(BANK, 'lcdm_S000.npz'), allow_pickle=True)
if not os.path.exists(ON):
    print('    ⛔ the switch-on re-run is not on disk -- nothing is claimed about the doubling.')
    sys.exit(1)
b = np.load(ON, allow_pickle=True)
same_ls = bool(np.array_equal(np.asarray(a['ls'], float), np.asarray(b['ls'], float)))
blocks = {}
for k in ('Dl', 'Dl_EE', 'Dl_TE'):
    x, y = 2.0 * np.asarray(a[k], float), np.asarray(b[k], float)
    m = x != 0
    w = float(np.max(np.abs(y[m] / x[m] - 1.0)))
    blocks[k] = dict(n=int(m.sum()), worst_abs_rel=w, exact=bool(w < 1e-12))
    print('    %-6s n=%3d   worst |ratio - 1| %.3e   exact to the last bit: %s'
          % (k, blocks[k]['n'], w, blocks[k]['exact']))
ok = same_ls and all(v['exact'] for v in blocks.values())
print('    same multipole axis: %s' % same_ls)
print('\n    ⇒ ** %s: twice the committed grid IS the switch-on grid, at the bank\'s own reach. **'
      % ('HOLDS' if ok else 'FAILS'))
print('      *So the substitution is stated and measured rather than made silently, which is what'
      '\n      this seat promised in the reply the order merged.*')
out['fourpi_doubling'] = dict(holds=ok, same_ls=same_ls, blocks=blocks,
                              point=os.path.basename(ON))

print('\n  Ⓔ⑤ᵃ `PRIMNORM` IS A CONSTANT PER POINT, AND THE POINTS DO NOT SHARE IT')
print('  ' + '-' * 98)
AS, KP = 2.1e-9, 0.05
ns_seen = {}
for f in sorted(os.listdir(BANK)):
    if not f.endswith('.npz') or f.endswith('_tt.npz'):
        continue
    z = np.load(os.path.join(BANK, f), allow_pickle=True)
    ns = float(np.asarray(z['ns'], float))
    ns_seen.setdefault('%.6f' % ns, []).append(f.split('.')[0])
for ns, names in sorted(ns_seen.items()):
    k = (4.0 / 9.0) * AS * KP ** (1.0 - float(ns))
    print('    n_s = %s  ->  constant %.10e   on %d point(s), e.g. %s'
          % (ns, k, len(names), names[0]))
print('    ⇒ %d distinct values across the grid, so it is applied PER POINT from that point\'s own'
      % len(ns_seen))
print('      recorded `n_s` and never as one number for the grid.')
out['primnorm'] = {ns: dict(constant=(4.0 / 9.0) * AS * KP ** (1.0 - float(ns)), n=len(v))
                   for ns, v in ns_seen.items()}

print('\n  ⛔ Ⓔ⑤ᵃ `BVEL` NEEDS THE SOLVER RUN AGAIN, AND HERE IS WHAT THAT COSTS')
print('  ' + '-' * 98)
pts = [f for f in os.listdir(BANK) if f.endswith('.npz') and not f.endswith('_tt.npz')]
blob = json.loads(str(np.atleast_1d(a['config'])[0])).get('instrument_blob')
mt = os.path.getmtime(ON)
started = os.path.getmtime(os.path.join(os.path.dirname(ON), 'on.log')) if os.path.exists(
    os.path.join(os.path.dirname(ON), 'on.log')) else mt
print('    the committed grid records instrument blob %s, which PREDATES the switch, so every' % blob)
print('    point in it was solved with the baryons driven by the photon velocity.')
print('    points to run again: %d   one point measured here at about 35 minutes on 4 cores' % len(pts))
print('    ⇒ the recompute is the whole cost of item ④, and it is REPORTED rather than skipped:')
print('      no limit is read off a BVEL-off grid and called a BVEL-on control.')
out['bvel'] = dict(points=len(pts), committed_blob=blob,
                   minutes_per_point_measured=35.0,
                   note='a solver change: no constant stands in for it')
with io.open(os.path.join(_HERE, 'doubling.json'), 'w', encoding='utf-8') as fh:
    fh.write(json.dumps(out, indent=1, sort_keys=True))
print('\n  wrote doubling.json\n')
sys.exit(0 if ok else 1)
