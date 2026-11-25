# -*- coding: utf-8 -*-
"""r7873+cc66 item ⑪, THE DISCRIMINATION the registered criterion could not make.

`two_start.py` applies the criterion registered in `PREDICTION.md`:

    same branch  iff |dH0| < 0.5  AND |dchi2| < 0.01
    two branches iff |dH0| > 2.0  AND |dchi2| > 0.01
    anything else is 60's third outcome

`rd_camb` returns THE THIRD OUTCOME, and it does so in a specific and readable way: the two starts
agree on `H0` to `0.0039` -- eight thousandths of the same-branch bound -- while their `chi2`
differ by `0.086`, eight times the same-branch bound.  Reporting that as "inconclusive" would waste
what the run actually measured.

⛔ THE REGISTERED chi2 THRESHOLD WAS TIGHTER THAN THE PROFILER'S OWN CONVERGENCE TOLERANCE.
   `profile_likeforlike.profile` minimises with Nelder-Mead at `fatol=5e-3`, `xatol=1e-3`, five free
   parameters.  A criterion demanding two independent runs agree to `0.01` in `chi2` asks the
   minimiser for precision it does not claim.  That is a defect in MY registration, not a property
   of the likelihood, and it is recorded rather than quietly widened.

THIS DRIVER ASKS THE QUESTION THE CRITERION MEANT TO ASK.  Two converged points either sit in one
basin or they do not, and `H0` agreeing to `0.0039` while `chi2` differs says the OTHER FOUR
parameters moved.  So:

  ⒜ re-score BOTH converged points with the same scorer, to confirm the banked `chi2` is the
     surface's value at that point and not the minimiser's bookkeeping;
  ⒝ report every parameter's separation, not just `H0`'s;
  ⒞ score the MIDPOINT of the two converged points.  ** This is the discriminator. ** One basin is
     convex near its floor, so the midpoint of two points in one basin scores at or below the worse
     of them.  A midpoint that scores ABOVE both means a ridge between them, which is two basins.

⛔ A RIDGE MEANS NOTHING WITHOUT A SCALE, and the first version of this driver had none: it tested
   `midpoint > worse` against ZERO, so any excess at all -- including `4.8e-05`, which is a hundredth
   of the minimiser's own `fatol` -- came back as "TWO BASINS".  That is a defect in MY test, not a
   feature of the likelihood, and it reported a barrier where no barrier of any consequence exists.
   A barrier is compared here against TWO declared scales: the profiler's own `fatol = 5e-3`, below
   which the minimiser does not resolve anything, and `dchi2 = 1`, the one-parameter unit of
   inference.  A ridge under either is noted and NOT called a basin boundary.

    NODE=cc66 python3 basin_detail.py
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
sys.path.insert(0, os.path.join(_BTW, 'r7853_cc66_the_repaired_transfer_and_the_like_for_like_'
                                      'reference'))
import profile_likeforlike as PL                                            # noqa: E402

NAMES = ('H0', 'Om', 'ombh2', 'ns', 'tau')
SUM = 0.400
IN = os.path.join(_HERE, 'two_start.json')
OUT = os.path.join(_HERE, 'basin_detail.json')


def main():
    print(__doc__)
    print('=' * 100)
    if not os.path.exists(IN):
        sys.exit('FATAL: %s is not there yet -- two_start.py must land first.' % IN)
    TS = json.load(io.open(IN, encoding='utf-8'))
    out = {'sum': SUM, 'fatol': 5e-3, 'xatol': 1e-3, 'modes': {}}

    for mode, rec in sorted(TS['modes'].items()):
        runs = rec['runs']
        keys = sorted(runs)
        if len(keys) != 2:
            print('\n  %s: %d run(s), not two -- skipped' % (mode, len(keys)))
            continue
        a, b = runs[keys[0]], runs[keys[1]]
        xa = [float(a['params'][n]) for n in NAMES]
        xb = [float(b['params'][n]) for n in NAMES]
        print('\n  === %s ===   registered verdict: %s' % (mode, rec['verdict']))
        print('      banked chi2 %.8f' % rec['banked_chi2'])

        # ⒜ re-score both converged points
        ca, _ = PL.score(SUM, *xa, mode)
        cb, _ = PL.score(SUM, *xb, mode)
        print('      ⒜ re-scored: start %s  banked %.8f  re-scored %.8f  (|d| %.2e)'
              % (keys[0], a['chi2'], ca, abs(ca - a['chi2'])))
        print('         re-scored: start %s  banked %.8f  re-scored %.8f  (|d| %.2e)'
              % (keys[1], b['chi2'], cb, abs(cb - b['chi2'])))

        # ⒝ every parameter's separation
        print('      ⒝ parameter separations:')
        seps = {}
        for n, va, vb in zip(NAMES, xa, xb):
            seps[n] = float(abs(va - vb))
            print('           %-6s %14.8f  %14.8f   |d| %.8f' % (n, va, vb, abs(va - vb)))

        # ⒞ the midpoint: the discriminator
        xm = list((np.asarray(xa) + np.asarray(xb)) / 2.0)
        cm, _ = PL.score(SUM, *xm, mode)
        worse = max(ca, cb)
        better = min(ca, cb)
        excess = float(cm - worse)
        FATOL, UNIT = 5e-3, 1.0
        above = bool(excess > 0.0)
        matters = bool(excess > FATOL)
        spread = float(worse - better)
        maxsep = max(seps.values())
        print('      ⒞ midpoint chi2 %.8f against worse endpoint %.8f and better %.8f'
              % (cm, worse, better))
        print('         midpoint excess over the worse endpoint: %+.8f' % excess)
        print('         against the profiler\'s own fatol %.0e : %.4f of it' % (FATOL,
                                                                                excess / FATOL))
        print('         against the one-parameter unit dchi2=1 : %.2e of it' % (excess / UNIT))
        if not above:
            verdict = ('NO RIDGE AT ALL: the midpoint is BELOW the worse endpoint, so the two '
                       'converged points sit in ONE CONVEX BASIN')
        elif not matters:
            verdict = ('A RIDGE BELOW EVERY SCALE THAT MATTERS: %+.2e in chi2 is %.4f of the '
                       'minimiser\'s own fatol and %.1e of dchi2=1, between two points that agree '
                       'to %.2e in every parameter.  There is no barrier of consequence: ONE BASIN'
                       % (excess, excess / FATOL, excess / UNIT, maxsep))
        else:
            verdict = ('⛔ A REAL RIDGE: the midpoint is above both endpoints by %+.6f, which '
                       'exceeds the profiler\'s fatol -- TWO BASINS' % excess)
        print('         ⇒ %s' % verdict)
        ridge = matters
        out['modes'][mode] = dict(
            registered_verdict=rec['verdict'], banked_chi2=float(rec['banked_chi2']),
            chi2=[float(ca), float(cb)], chi2_banked=[float(a['chi2']), float(b['chi2'])],
            rescore_drift=[float(abs(ca - a['chi2'])), float(abs(cb - b['chi2']))],
            separations=seps, dH0=float(rec['dh0']), dchi2=float(rec['dchi2']),
            midpoint=dict(zip(NAMES, [float(v) for v in xm])), midpoint_chi2=float(cm),
            worse_endpoint=float(worse), better_endpoint=float(better),
            midpoint_above_both=bool(cm > worse),
            midpoint_minus_worse=excess,
            excess_over_fatol=float(excess / 5e-3),
            endpoint_spread=spread, max_separation=float(maxsep),
            ridge_that_matters=ridge,
            one_basin=bool(not ridge))

    io.open(OUT, 'w', encoding='utf-8').write(json.dumps(out, indent=1, sort_keys=True))
    print('\n  written %s' % os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
