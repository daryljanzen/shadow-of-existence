# -*- coding: utf-8 -*-
"""r7882+60 gate Ⓠ⓸ — THE MASSLESS LIMIT, measured and not trusted.

`PREDICTION.md`: *"at `Sigma -> 0` the hierarchy's spectra must agree with the landed massless
hierarchy to the fit's own resolution ... the massive hierarchy reduces to the massless one when the
mass vanishes; if it does not, it is not the same object continued."*  And it is the gate that runs
BEFORE any validation number is read, because the massless limit is the one place the answer is
already known independently -- it is where a sign or a normalisation error shows.

⛔ *The switch refuses a zero sum by design, so the limit is APPROACHED: the comparison is at a sum
  small enough that the species is ultra-relativistic over the whole range the spectrum is built
  from, against the SAME sum with the hierarchy off.  The approach is itself measured, at two sums a
  decade apart, so a residual that is the mass rather than a defect shows as one by shrinking.*

⌗ NOT RETYPED: the leg runner and the array comparison are `r7878`'s own, imported.

    NODE=60 python3 limit.py
"""
import io
import json
import os
import sys
import tempfile

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
_R7878 = os.path.join(_BTW, 'r7878_60_the_three_changes_decomposed_and_the_exact_adiabatic'
                            '_sound_speed')
sys.path.insert(0, _R7878)
from switch_arms import one                                                     # noqa: E402

CUR = os.path.join(_BTW, 'ACOUSTIC_two_arm.py')
SUMS = ('1e-3', '1e-4')          # a decade apart, both far inside the relativistic regime


def main():
    print(__doc__)
    print('=' * 100)
    rec = {'sums': {}}
    tmp = tempfile.mkdtemp(prefix='r7882_limit_')
    for sm in SUMS:
        for tag, extra in (('off', dict(MNU=sm)), ('on', dict(MNU=sm, NUHIER='1'))):
            rc, out = one(CUR, os.path.join(tmp, '%s_%s' % (sm, tag)), extra)
            if rc != 0:
                raise SystemExit('  ⛔ %s/%s failed rc=%d:\n%s' % (sm, tag, rc, out[-1500:]))
        row = {}
        for which in ('tt', 'pol'):
            a = np.load(os.path.join(tmp, '%s_off_%s.npz' % (sm, which)), allow_pickle=True)
            b = np.load(os.path.join(tmp, '%s_on_%s.npz' % (sm, which)), allow_pickle=True)
            for key in [k for k in a.files if k != 'config' and a[k].dtype.kind == 'f']:
                x, y = np.asarray(a[key], float), np.asarray(b[key], float)
                if x.shape != y.shape or x.size == 0:
                    continue
                den = np.maximum(np.abs(x), 1e-300)
                row['%s/%s' % (which, key)] = float(np.abs(y - x).max() / den.max()
                                                    if np.abs(x).max() > 0 else
                                                    np.abs(y - x).max())
        rec['sums'][sm] = row
        print('\n  Sigma = %s eV, hierarchy on against off, worst relative difference per array:'
              % sm)
        for k in sorted(row):
            print('    %-14s %.3e' % (k, row[k]))
    #: the two statements the gate makes, computed rather than eyeballed
    _k = [k for k in rec['sums'][SUMS[0]] if k in rec['sums'][SUMS[1]]]
    rec['worst'] = dict((sm, max(rec['sums'][sm][k] for k in _k)) for sm in SUMS)
    rec['shrinks'] = bool(rec['worst'][SUMS[1]] < rec['worst'][SUMS[0]])
    rec['ratio'] = (rec['worst'][SUMS[0]] / rec['worst'][SUMS[1]]
                    if rec['worst'][SUMS[1]] else None)
    print('\n  worst over every array: %.3e at Sigma = %s, %.3e at %s'
          % (rec['worst'][SUMS[0]], SUMS[0], rec['worst'][SUMS[1]], SUMS[1]))
    print('  ⇒ the residual %s as the sum falls by a decade%s'
          % ('SHRINKS' if rec['shrinks'] else '** DOES NOT SHRINK **',
             ', by a factor %.1f' % rec['ratio'] if rec['ratio'] else ''))
    print('  ⇒ %s' % ('GATE Ⓠ⓸ MET: the hierarchy reduces to the landed massless one, and what is '
                      'left is the MASS -- it shrinks with it'
                      if rec['shrinks'] and rec['worst'][SUMS[1]] < 1e-02 else
                      '** GATE Ⓠ⓸ NOT MET -- the limit is not the landed one, and no validation '
                      'number is readable **'))
    rec['met'] = bool(rec['shrinks'] and rec['worst'][SUMS[1]] < 1e-02)
    json.dump(rec, io.open(os.path.join(_HERE, 'limit.json'), 'w', encoding='utf-8'),
              indent=1, sort_keys=True)
    print('  wrote limit.json')
    return 0 if rec['met'] else 1


if __name__ == '__main__':
    sys.exit(main())
