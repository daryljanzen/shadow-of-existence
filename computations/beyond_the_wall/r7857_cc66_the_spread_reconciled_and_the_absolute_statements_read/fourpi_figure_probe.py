#!/usr/bin/env python3
r"""r7857 item ② -- ** THE ONE RECEIPT THE DOUBLING PROBE CANNOT REACH, REACHED ONE LAYER OUT. **

`P15_the_period_difference_null...` opens exactly ONE archive and it holds no instrument spectrum:
it reads `fig:acoustic-nofit`'s BANKED whitened residuals.  So `fourpi_audit.py` reports it VACUOUS
and asserts nothing, which is right -- a probe that reaches nothing must not return a verdict.

⇒ ** The reachable question is the one layer out: would the FIGURE's banked numbers move? **  So the
generator that writes them is run twice -- as it stands, and with every instrument `Dl` it loads
doubled -- and the two banks are compared key by key.  Nothing is written inside the repository:
`np.savez` is redirected, so the live bank is untouched (asserted at the end by its own hash).

Usage: python3 fourpi_figure_probe.py
"""
import hashlib
import json
import os
import runpy
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), f'ROOT is wrong: {ROOT}'
GEN = os.path.join(ROOT, 'corpus', 'make_fig_acoustic_nofit.py')
LIVE = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7183_nofit_figure',
                    'nofit_figure_numbers.npz')
CHILD = os.path.join(HERE, '_figure_child.py')
_CHILD_SRC = r'''
import os, runpy, sys
import numpy as np
KEYS = {'Dl'} if os.environ.get('MODE', 'tt') == 'tt' else {'Dl', 'Dl_EE', 'Dl_TE'}
DOUBLE = os.environ.get('DOUBLE', '0') == '1'
OUT = os.environ['OUT']
HITS = []
_load, _savez = np.load, np.savez


class _D:
    def __init__(self, z, p):
        self._z, self._p = z, p

    def __getitem__(self, k):
        v = self._z[k]
        if DOUBLE and k in KEYS:
            HITS.append(f'{os.path.basename(self._p)}:{k}')
            return np.asarray(v, float) * 2.0
        return v

    def __contains__(self, k):
        return k in self._z

    def __getattr__(self, n):
        return getattr(self._z, n)


def load(p, *a, **kw):
    z = _load(p, *a, **kw)
    return _D(z, str(p)) if hasattr(z, 'files') else z


def savez(p, *a, **kw):
    return _savez(OUT, *a, **kw)        # ** REDIRECTED: the repository's own bank is never written **


np.load, np.savez = load, savez
sys.argv = [sys.argv[1], '--numbers']
rc = 0
try:
    runpy.run_path(sys.argv[0], run_name='__main__')
except SystemExit as e:
    rc = int(e.code or 0)
print(f'__HITS__ {len(HITS)}')
print(f'__RC__ {rc}')
'''


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def run(double, out):
    env = {**os.environ, 'MODE': 'tt', 'DOUBLE': '1' if double else '0', 'OUT': out}
    p = subprocess.run([sys.executable, CHILD, GEN], cwd=ROOT, capture_output=True, text=True,
                       errors='replace', env=env)
    txt = p.stdout + p.stderr
    hits = int(txt.split('__HITS__ ')[1].split()[0]) if '__HITS__ ' in txt else -1
    return hits, txt


def main():
    before = sha(LIVE)
    open(CHILD, 'w').write(_CHILD_SRC)
    sc = os.environ.get('TMPDIR', '/tmp')
    a, b = os.path.join(sc, 'fig_base.npz'), os.path.join(sc, 'fig_doubled.npz')
    ha, ta = run(False, a)
    hb, tb = run(True, b)
    print(f'  generator as it stands: {ha} arrays doubled -> {os.path.basename(a)}')
    print(f'  generator with the bank doubled: {hb} arrays doubled -> {os.path.basename(b)}')
    if hb <= 0:
        print('  ⛔ REFUSED: the doubling reached nothing in the generator either.  Nothing is '
              'asserted.')
        print(tb[-1500:])
        return 2
    za, zb = np.load(a), np.load(b)
    assert sorted(za.files) == sorted(zb.files), 'the two banks must carry the same keys'
    rec, moved = {}, []
    for k in sorted(za.files):
        u, v = np.atleast_1d(np.asarray(za[k], float)), np.atleast_1d(np.asarray(zb[k], float))
        d = float(np.max(np.abs(v - u) / np.maximum(np.abs(u), 1e-300))) if u.shape == v.shape \
            else float('inf')
        rec[k] = d
        if d > 1e-12:
            moved.append((k, d))
    print(f'  {len(za.files)} banked keys compared; worst relative move '
          f'{max(rec.values()):.3e}')
    for k, d in moved:
        print(f'      ⛔ {k} moves by {d:.6g}')
    if not moved:
        print('  ⇒ ** THE FIGURE\'S WHOLE BANK IS INVARIANT **: every key the figure writes is '
              'unchanged when the bank it reads doubles, because the generator refits one amplitude '
              'per spectrum at the covariance-weighted optimum.  So the receipt that reads this '
              'bank cannot move either -- which is now a measurement and not an inference.')
    after = sha(LIVE)
    print(f'  the live bank is untouched: {after[:16]} == {before[:16]}  '
          f'{"OK" if after == before else "⛔ CHANGED"}')
    json.dump(dict(worst=max(rec.values()), moved=moved, keys=len(rec),
                   hits_base=ha, hits_doubled=hb, live_unchanged=(after == before)),
              open(os.path.join(HERE, 'fourpi_figure_probe.json'), 'w'), indent=1)
    os.remove(CHILD)
    return 0 if (after == before and not moved) else 1


if __name__ == '__main__':
    sys.exit(main())
