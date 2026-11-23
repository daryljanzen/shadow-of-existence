#!/usr/bin/env python3
"""** CAN THE NINE BANDPOWERS CONSTRAIN THE SUM AT ALL, GIVEN THE SHAPE SYSTEMATIC THEY CARRY? **

This is the question that decides whether item ③'s limit would be a measurement or a restatement of
a known error, and it is asked BEFORE the six-parameter chain is built rather than after.

** THE TWO NUMBERS IT WEIGHS. **
  ⓵ The SIGNAL.  `growth_kdep` measured the sum's effect on the matter power at high `k` as about
    `5` per cent on the ordered carry.  Here it is measured where it actually acts: on the nine
    bandpowers, as `chi^2_lens` moves from `Sum = 0` to the banked sums, **with the amplitude held
    at what the CMB fit determined** -- `A_cmb / T_CMB^2`, which is the whole mechanism, since no
    amplitude is fitted to the lensing data.
  ⓶ The SYSTEMATIC.  The same bandpowers scored against this instrument's own shape give
    `chi^2/dof = 2.05` with one best-fit normalisation, and the implied normalisation drifts
    MONOTONICALLY by `49.8` per cent across `L = 28` to `377`.  That is a `50` per cent error on a
    `5` per cent signal.

⇒ ** IF THE SUM'S OWN MOVEMENT IN `chi^2` IS SMALL AGAINST WHAT THE SHAPE ERROR ALREADY COSTS, THEN
A LIMIT FROM THIS TERM IS REPORTING THE SHAPE ERROR. **  Saying that, with the two numbers beside
each other, is then the honest deliverable for item ③ -- not a limit that happens to land in the
order's band because a systematic pushed it there.

⌗ *The amplitude is held and not fitted, deliberately.  Fitting one would absorb part of the shape
error AND part of the sum's effect, and the comparison would stop meaning anything.*

Writes `lensing_informative.json`.
"""
import glob
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
import lensing_like as LL                                                # noqa: E402

#: ⛔ ** THE BANK NO LONGER LIVES IN `/tmp`, AT `r7857`'s ORDER ③. **  *Three banks on this
#:   line were lost to a `/tmp` default -- the `555`-bin mask, the Phi bandpowers and this
#:   grid -- so what the scorers read is COMMITTED beside the instrument and this default
#:   points at it, computed from this file's own location rather than from an absolute path
#:   that would differ between containers.  The environment variable still overrides it.
_BANK = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     'bank', 'phiphi_grid_eta4000')
assert os.path.isdir(_BANK), _BANK      # two dirnames: this file sits one below `beyond_the_wall`
GRID = os.environ.get('PPGRID', _BANK)
A_CMB = 1.078843e+04              # the 555-bin control fit's own amplitude, r7844's run
T_CMB_UK = 2.7255e6
TAU = LL.TAU_MEAN


def amp_from_cmb(tau=TAU):
    """AMP = A_cmb / T_CMB^2 * exp(+2 tau): the CMB fixes AMP*exp(-2 tau), lensing wants AMP"""
    return A_CMB / T_CMB_UK ** 2 * np.exp(2.0 * tau)


def load(arm):
    out = {}
    for p in sorted(glob.glob(os.path.join(GRID, f'{arm}_*.json'))):
        j = json.load(open(p))
        out[j['tag']] = j
    return out


def main():
    g = load('lcdm')
    sums = {t: j for t, j in g.items() if t.startswith('S')}
    if not sums:
        print('  the grid has no sum points yet at %s' % GRID)
        return 2
    amp = amp_from_cmb()
    print('  AMP held at %.6e  (A_cmb = %.6e, T_CMB^2 = %.4e, exp(+2 tau) at tau = %.3f)'
          % (amp, A_CMB, T_CMB_UK ** 2, TAU), flush=True)
    print()
    print('    sum / eV    chi2_lens (AMP held)     d chi2 vs Sum = 0')
    base = None
    rows = {}
    for t in sorted(sums, key=lambda t: sums[t]['mnu']):
        j = sums[t]
        m = amp * np.asarray(j['bandpowers'], float)
        c2 = LL.chi2(m)
        if abs(j['mnu']) < 1e-12:
            base = c2
        rows[t] = dict(mnu=j['mnu'], chi2=float(c2), model=[float(v) for v in m])
    for t in sorted(rows, key=lambda t: rows[t]['mnu']):
        r = rows[t]
        r['dchi2'] = float(r['chi2'] - base)
        print('   %+8.3f     %12.3f            %+10.3f'
              % (r['mnu'], r['chi2'], r['dchi2']), flush=True)

    # the systematic, for scale: the same shape with its OWN best normalisation
    j0 = sums[[t for t in sums if abs(sums[t]['mnu']) < 1e-12][0]]
    m0 = np.asarray(j0['bandpowers'], float)
    Abest = float((m0 @ LL.FISHER @ LL.DATA) / (m0 @ LL.FISHER @ m0))
    c2_best = LL.chi2(Abest * m0)
    spread = max(r['dchi2'] for r in rows.values()) - min(r['dchi2'] for r in rows.values())
    print()
    print('  ⓶ the SYSTEMATIC, for scale: the same shape at its OWN best normalisation scores '
          '%.2f on 9 bandpowers (8 dof)' % c2_best, flush=True)
    print('     and the amplitude it prefers is %.6e against the CMB\'s %.6e, a ratio of %.3f'
          % (Abest, amp, Abest / amp), flush=True)
    print('  ⓵ the SIGNAL: the sum moves chi2_lens by %.2f across the banked range' % spread,
          flush=True)
    print()
    informative = bool(spread > 2.0 * abs(c2_best - 8.0) and spread > 4.0)
    print('  ⇒ the sum\'s movement is %s the shape error\'s cost: %s'
          % ('LARGER than' if informative else 'NOT large against',
             'the term can constrain the sum' if informative
             else 'a limit from this term would be reporting the shape error'), flush=True)
    out = dict(amp_held=float(amp), amp_from_cmb_components=dict(
        A_cmb=A_CMB, T_CMB_sq=T_CMB_UK ** 2, tau=TAU),
        rows={t: rows[t] for t in rows}, chi2_at_own_best_normalisation=float(c2_best),
        amp_preferred_by_bandpowers=float(Abest),
        amp_ratio_preferred_over_cmb=float(Abest / amp),
        sum_moves_chi2_by=float(spread), informative=informative)
    with open(os.path.join(_HERE, 'lensing_informative.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote lensing_informative.json', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
