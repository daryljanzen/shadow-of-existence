#!/usr/bin/env python3
"""** ARM Ⓔ⑤: DOES `tau` ACQUIRE REACH ONCE THE LENSING BANDPOWERS ARE IN THE SCORE? **

Registered: *with the lensing term in, the score moves under a `tau` shift across `0.02`-`0.20` by
MORE than `1` in `chi^2` -- against the `<= 1.1e-12` that `r7844` measured without it.  Reachable
negative: a score that still does not move, which would mean the lensing term is not carrying the
absolute normalisation it was added for.*

** THE MECHANISM, WHICH `r7844` PREDICTED BEFORE THIS TERM EXISTED. **  `r7844` measured `tau` to
have no reach at all on a CMB-only score -- `chi^2` moved by at most `1.1e-12` across the whole
range -- because the score solves one overall amplitude exactly and `tau` enters the high-`l`
spectra only as `exp(-2 tau)` on that amplitude, so it cancels.  Its receipt said in terms: *"that
changes the moment the lensing bandpowers enter, which carry no fitted amplitude."*  This is that
claim under test.

    CMB    = AMP * exp(-2 tau) * shape_cmb      -> the fit determines `AMP * exp(-2 tau)`
    phiphi = AMP              * shape_phiphi    -> so the prediction is that number * exp(+2 tau)

⇒ `tau` moves the lensing prediction and cannot be absorbed, because nothing is fitted to the
lensing data.  ⌗ *The CMB half of the score is unchanged and still does not move with `tau`; the
whole of the reach is the lensing term's, which is why this is the arm that decides whether item ②
did what it was for.*

Writes `tau_reach_with_lensing.json`.
"""
import glob
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import lensing_like as LL                                                # noqa: E402

GRID = os.environ.get('PPGRID', '/tmp/claude-0/phiphi_grid_eta4000')
A_CMB = 1.078843e+04
T_CMB_UK = 2.7255e6


def main():
    p = os.path.join(GRID, 'lcdm_S000.json')
    if not os.path.exists(p):
        print('  the control\'s zero-sum point is not banked yet')
        return 2
    shape = np.asarray(json.load(open(p))['bandpowers'], float)
    base = A_CMB / T_CMB_UK ** 2

    taus = np.array([0.02, 0.04, 0.054, 0.08, 0.12, 0.16, 0.20])
    print('  the lensing term alone, at Sum = 0, with the amplitude from the CMB and exp(+2 tau):')
    print('      tau      exp(+2 tau)     chi2_lens      d chi2 vs tau = 0.02')
    rows = {}
    c0 = None
    for t in taus:
        m = base * np.exp(2.0 * t) * shape
        c2 = LL.chi2(m)
        if c0 is None:
            c0 = c2
        rows['%.3f' % t] = dict(tau=float(t), factor=float(np.exp(2 * t)), chi2=float(c2),
                                dchi2=float(c2 - c0))
        print('    %6.3f      %8.4f      %10.3f      %+10.3f'
              % (t, np.exp(2 * t), c2, c2 - c0), flush=True)
    spread = max(r['chi2'] for r in rows.values()) - min(r['chi2'] for r in rows.values())
    r7844 = 1.1368683772161603e-12
    holds = bool(spread > 1.0)
    print()
    print('  ⇒ chi^2 moves by %.3f across tau = 0.02 to 0.20, against r7844\'s %.3e without the '
          'lensing term' % (spread, r7844), flush=True)
    print('    a ratio of %.3e  ⇒ Ⓔ⑤ %s (registered: more than 1)'
          % (spread / r7844, 'HOLDS' if holds else 'FAILS'), flush=True)
    # and the tau the lensing data itself prefers, for the record
    def c2_of(t):
        return LL.chi2(base * np.exp(2.0 * t) * shape)
    tt = np.linspace(-0.05, 0.30, 701)
    cc = np.array([c2_of(t) for t in tt])
    tbest = float(tt[int(np.argmin(cc))])
    print('    ⌗ for the record, the lensing term alone prefers tau = %+.4f at Sum = 0, against '
          'the prior\'s %.3f +/- %.3f -- a %.1f sigma pull, and it is CONFOUNDED with the sum and '
          'with the shape systematic rather than a measurement of tau'
          % (tbest, LL.TAU_MEAN, LL.TAU_SIGMA,
             abs(tbest - LL.TAU_MEAN) / LL.TAU_SIGMA), flush=True)
    out = dict(rows=rows, spread=float(spread), r7844_without_lensing=r7844,
               ratio=float(spread / r7844), registered_threshold=1.0, holds=holds,
               tau_preferred_by_lensing_alone=tbest,
               tau_prior=dict(mean=LL.TAU_MEAN, sigma=LL.TAU_SIGMA),
               pull_sigma=float(abs(tbest - LL.TAU_MEAN) / LL.TAU_SIGMA),
               caveat=('the preferred tau is confounded with the sum and with the 50 per cent '
                       'shape systematic; it is not a measurement of tau'))
    with open(os.path.join(_HERE, 'tau_reach_with_lensing.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote tau_reach_with_lensing.json', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
