# -*- coding: utf-8 -*-
"""r7873+cc66 item ⑪ -- THE TWO-START BASIN TEST, as 60 routed it.

At `Sigma = 0.400` eV, the reference profiler on BOTH rulers from two `H0` starts -- 60's own basin
figures `65.29` and `68.59` -- with the other four parameters at this reference's own banked best
fit for that ruler.  Report the `chi2` each lands at and the `H0` each converges to.

⌗ 60 is right that `r7869`'s record held each ruler's BEST FIT and no branch scan, so "one branch to
0.60 eV" claimed more than it showed.  This is the scan that claim needed.  The verdict is therefore
a REGISTERED CRITERION and not an expectation:

    same branch  iff |dH0| < 0.5  AND |dchi2| < 0.01
    two branches iff |dH0| > 2.0  AND |dchi2| > 0.01
    anything else is 60's third outcome, and is reported as neither.

    NODE=cc66 python3 two_start.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
ROOT = os.path.dirname(os.path.dirname(_BTW))
assert os.path.isdir(os.path.join(ROOT, 'receipts')), ROOT
R7853 = os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_reference')
sys.path.insert(0, R7853)
import profile_likeforlike as PL                                            # noqa: E402

BANK = os.path.join(R7853, 'out5')
SUM = 0.400
H0_STARTS = (65.29, 68.59)          # 60's own basin figures, not chosen here
MODES = ('rd_camb', 'rd_min')
SAME_DH0, SAME_DCHI = 0.5, 0.01     # registered criterion
TWO_DH0, TWO_DCHI = 2.0, 0.01
OUT = os.path.join(_HERE, 'two_start.json')
NAMES = ('H0', 'Om', 'ombh2', 'ns', 'tau')


def banked(mode, s):
    f = os.path.join(BANK, '%s_%.3f.json' % (mode, s))
    if not os.path.exists(f):
        sys.exit('FATAL: %s is not where this reads it from.' % f)
    return json.load(io.open(f, encoding='utf-8'))


def interior(x):
    return all(lo < v < hi for v, (lo, hi) in zip(x, PL.BOX))


def main():
    print(__doc__)
    print('=' * 100)
    out = {'sum': SUM, 'h0_starts': list(H0_STARTS), 'box': [list(b) for b in PL.BOX],
           'criterion': dict(same_dh0=SAME_DH0, same_dchi2=SAME_DCHI,
                             two_dh0=TWO_DH0, two_dchi2=TWO_DCHI),
           'modes': {}}

    for mode in MODES:
        b = banked(mode, SUM)
        base = [b['H0'], b['Om'], b['ombh2'], b['ns'], b['tau']]
        print('\n  === %s ===' % mode)
        print('      Ⓐ① banked Sigma = %.3f best fit, READ from the record: %s'
              % (SUM, dict(zip(NAMES, ['%.8f' % v for v in base]))))
        print('          its banked chi2 %.8f' % b['total'])
        rec = {'banked': dict(zip(NAMES, base)), 'banked_chi2': float(b['total']), 'runs': {}}

        for h0 in H0_STARTS:
            start = [h0] + base[1:]        # everything else at its own best fit
            det = PL.profile(SUM, mode, start)
            chi2 = float(det['total'])
            x = [float(det[k]) for k in NAMES]
            rec['runs']['%.2f' % h0] = dict(
                start=list(start), chi2=float(chi2),
                params=dict(zip(NAMES, [float(v) for v in x])),
                interior=bool(interior(x)))
            print('      start H0 %.2f  ->  chi2 %.8f   H0 %.8f   interior %s'
                  % (h0, chi2, x[0], interior(x)))

        a, c = rec['runs']['%.2f' % H0_STARTS[0]], rec['runs']['%.2f' % H0_STARTS[1]]
        dh0 = abs(a['params']['H0'] - c['params']['H0'])
        dchi = abs(a['chi2'] - c['chi2'])
        if dh0 < SAME_DH0 and dchi < SAME_DCHI:
            verdict = 'ONE BRANCH'
        elif dh0 > TWO_DH0 and dchi > TWO_DCHI:
            verdict = 'TWO BRANCHES'
        else:
            verdict = 'THE THIRD OUTCOME'
        lower = a if a['chi2'] <= c['chi2'] else c
        rel = abs(lower['chi2'] - b['total']) / max(abs(b['total']), 1e-30)
        rec.update(dh0=float(dh0), dchi2=float(dchi), verdict=verdict,
                   both_interior=bool(a['interior'] and c['interior']),
                   lower_chi2=float(lower['chi2']),
                   reproduces_banked_rel=float(rel))
        print('      ⇒ |dH0| %.8f   |dchi2| %.8f   ⇒ %s' % (dh0, dchi, verdict))
        print('        Ⓒ③ the lower start reproduces the banked chi2 to %.3e relative' % rel)
        print('        Ⓑ② both interior: %s' % rec['both_interior'])
        out['modes'][mode] = rec

    v = {m: out['modes'][m]['verdict'] for m in MODES}
    out['rulers_agree'] = bool(len(set(v.values())) == 1)
    print('\n  Ⓔ⑤ the two rulers: %s  ⇒ they %s'
          % (v, 'AGREE' if out['rulers_agree'] else 'DISAGREE, which is itself the finding'))
    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
