"""r7089 (70) -- the audit's three measurements, read from the scratch runs `launch.sh` wrote.

The statistic is the receipt's own, copied rather than re-derived: the oscillation (y - e)/e about a running
arithmetic mean over one unit of q = ell / l_A, interpolated onto q in [0.85, 5.75] at 1200 points, and the
ratio  sum(A*B) / sum(B*B).

  (1) CANCELLATION -- per arm, the SELF-RATIO of each refined run against that arm's own base, set beside the
      cross-arm ratio's step on the same axis.  If the arms move and the ratio does not, the ratio's stability
      is common-mode cancellation.
  (2) RESPONSIVENESS -- the cross-arm ratio with ONE arm grossly under-resolved on the eta grid and the other at
      base.  If a known integration defect on one arm does not move the ratio past the floor, a small step is
      evidence of insensitivity rather than of stability.
  (3) BAND-RESOLVED -- the same ratio restricted to each unit of q, so a scalar step that hides opposing band
      movements is seen.

Usage:  python3 analyse.py <scratch dir>
"""
import os
import sys

import numpy as np

LO, HI, NG = 0.85, 5.75, 1200
FLOOR = 0.006
AXES = ['kfac26', 'nlos1120', 'nlosw9', 'nlosf90', 'lstep4']
COARSE = ['coarse140', 'narrow3']
D = sys.argv[1]


def env_a(x, y, win=1.0):
    e = np.empty_like(y, dtype=float)
    for j, v in enumerate(x):
        m = (x >= v - win / 2) & (x <= v + win / 2)
        e[j] = np.mean(y[m])
    return e


def osc(x, y, win=1.0):
    y = np.asarray(y, float)
    e = env_a(x, y, win)
    return (y - e) / e


def load(arm, s):
    p = os.path.join(D, f'inj_fixed_{arm}_{s}.npz')
    log = p[:-4] + '.log'
    if not (os.path.exists(p) and os.path.exists(log) and '__DONE__ rc=0' in open(log).read()):
        return None
    d = np.load(p)
    q = d['ls'].astype(float) / float(d['l_A'])
    x = np.linspace(LO, HI, NG)
    return x, np.interp(x, q, osc(q, np.asarray(d['Dl'], float)))


def ratio(a, b, band=None):
    x, A = a
    _, B = b
    m = np.ones_like(x, bool) if band is None else (x >= band[0]) & (x < band[1])
    return float(np.sum(A[m] * B[m]) / np.sum(B[m] * B[m]))


BANDS = [(1 + j, 2 + j) for j in range(4)] + [(5.0, 5.75)]
base = {arm: load(arm, 'base') for arm in ('cr', 'lcdm')}
if any(v is None for v in base.values()):
    sys.exit('base runs incomplete')
R0 = ratio(base['cr'], base['lcdm'])
print(f'base cross-arm ratio  {R0:.10f}   (the receipt banks 1.058685304866 from cc66\'s run)')

print('\n(1) CANCELLATION -- relative step, per arm against its own base, and of the cross-arm ratio')
print(f'  {"axis":10s} {"cr self":>12s} {"lcdm self":>12s} {"cross step":>12s}  {"arms/cross":>10s}')
rows = []
for s in AXES:
    a, b = load('cr', s), load('lcdm', s)
    if a is None or b is None:
        print(f'  {s:10s} UNMEASURED')
        continue
    scr = ratio(a, base['cr']) - 1
    slc = ratio(b, base['lcdm']) - 1
    cross = ratio(a, b) / R0 - 1
    big = max(abs(scr), abs(slc))
    rows.append((s, scr, slc, cross))
    print(f'  {s:10s} {scr:+12.3e} {slc:+12.3e} {cross:+12.3e}  {big / abs(cross) if cross else float("inf"):10.1f}')

print('\n(2) RESPONSIVENESS -- the cross-arm ratio with ONE arm under-resolved, against the floor')
for s in COARSE:
    for arm, other in (('cr', 'lcdm'), ('lcdm', 'cr')):
        a = load(arm, s)
        if a is None:
            print(f'  {s:10s} on {arm:4s} UNMEASURED')
            continue
        own = ratio(a, base[arm]) - 1
        r = ratio(a, base[other]) if arm == 'cr' else ratio(base['cr'], a)
        mv = r / R0 - 1
        print(f'  {s:10s} on {arm:4s} only: that arm moves {own:+.3e} against its base; '
              f'cross ratio {r:.6f}, moved {100 * mv:+.4f}%  -> {"PAST" if abs(mv) > FLOOR else "inside"} the 0.6% floor')

print('\n(3) BAND-RESOLVED -- the cross-arm step per band of q, against the scalar step')
print('  ' + f'{"axis":10s}' + ''.join(f'{f"[{b[0]:.2g},{b[1]:.3g})":>13s}' for b in BANDS) + f'{"scalar":>12s}')
for s, _, _, cross in rows:
    a, b = load('cr', s), load('lcdm', s)
    st = [ratio(a, b, bd) / ratio(base['cr'], base['lcdm'], bd) - 1 for bd in BANDS]
    print('  ' + f'{s:10s}' + ''.join(f'{v:+13.2e}' for v in st) + f'{cross:+12.2e}'
          + f'   max/scalar {max(abs(v) for v in st) / abs(cross) if cross else float("inf"):.1f}')
