#!/usr/bin/env python3
"""** WHERE THE GROWTH EQUATION IS VALID, AND WHY THE EARLIER CARRY IS NOT JUSTIFIED AFTER ALL. **

`r7846` measured two things that both argued for starting the growth carry earlier than the ordered
`z = 12.8`: the ordered interval carries only `44.4` per cent of the post-non-relativistic neutrino
suppression, and it leaves the lensing shape at `chi^2/dof = 2.05` against the nine banked
bandpowers where a carry from `z = 188` gives `1.07`.  **This seat decided the fork on that evidence
and routed the decision.  This script is the measurement that reverses it.**

** THE TEST. **  If the growth truly links two reference times, then the lensing potential cannot
care which one it is carried from:  `Phi(k, a_1)` taken DIRECTLY from the instrument's solve must
equal `Phi(k, a_2) * g(k, a_1)/g(k, a_2)`.  That is a closed comparison with no free constant.

** WHAT IT SAYS. **  The ratio is not `1`, and it is not a constant either:

      k = 2e-4 /Mpc   0.964
      k = 2e-3        0.936
      k = 7e-3        0.839
      k = 2e-2        0.754
      k = 7e-1        0.739

*`k`-dependent, flat at small scales, approaching `1` only at the largest.*  That is the signature
of sub-horizon `Phi` DECAY through the residual radiation era: a mode that is inside the horizon
while radiation still contributes loses potential in a way no matter-only growth equation carries.
At `z = 188` radiation is about `5` per cent of matter on this background; at `z = 12.8` it is about
`0.4` per cent.

⇒ ** SO THE GROWTH EQUATION WAS BEING APPLIED OUTSIDE ITS OWN RANGE, AND THE "BETTER SHAPE" AT THE
EARLIER CARRY WAS TWO ERRORS PARTLY CANCELLING: ** the truncation that loses high-`z` contributions,
against a growth that over-predicts them by up to `26` per cent in a `k`-dependent way.  A lower
`chi^2` obtained that way is not a better model.

⇒ ** THE ORDERED CARRY AT `z = 12.8` IS THE CORRECT ONE and `r7845`'s wording was right. **  The
`44.4` per cent of missing suppression and the `2.05` of shape error are both still real, and
neither is fixed by moving the start: fixing them needs a treatment that carries `Phi` through the
radiation era, which is a larger instrument change than this revision's order asks for.

⌗ *The guard this seat already carries says it: before an identity is treated as an obstruction,
establish what it RANGES OVER.  The growth equation ranges over matter domination.  I read its
limits off its own derivation and then started it where they do not hold.*

Writes `carry_validity.json`.
"""
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')

import phiphi as PP                                                      # noqa: E402
import growth_kdep as GK                                                 # noqa: E402
A = GK.A


def radiation_share(a):
    """the radiation-to-matter ratio on this instrument's own background at a"""
    om = GK.om_tot(a)
    h, h0 = GK._h_of(a), GK._h_of(1.0)
    orad = 1.0 - om - (1.0 - float(A.OM)) * (h0 / h) ** 2
    return float(orad / max(om, 1e-300))


def main():
    eta1, eta2 = 4000.0, 914.0
    a1, a2 = float(A.a_of_eta(eta1)), float(A.a_of_eta(eta2))
    k1, P1 = PP.phi_shape(eta1)
    k2, P2 = PP.phi_shape(eta2)
    assert np.allclose(k1, k2), 'the two solves must share their k grid'
    g = GK.GrowthKDep(0.0, kk=np.logspace(np.log10(PP.KMIN), np.log10(PP.KMAX), 48), a_start=a2)
    r = g.g_of(k1, np.array([a1]))[:, 0] / g.g_of(k1, np.array([a2]))[:, 0]
    ratio = P1 / (P2 * r)
    ok = np.isfinite(ratio)

    out = dict(
        eta=[eta1, eta2], a=[a1, a2], z=[1 / a1 - 1, 1 / a2 - 1],
        radiation_over_matter={'z_%.1f' % (1 / a1 - 1): radiation_share(a1),
                               'z_%.1f' % (1 / a2 - 1): radiation_share(a2)},
        k=[float(v) for v in k1], ratio=[float(v) for v in ratio],
        ratio_min=float(np.min(ratio[ok])), ratio_max=float(np.max(ratio[ok])),
        ratio_median=float(np.median(ratio[ok])),
        k_dependent=bool((np.max(ratio[ok]) - np.min(ratio[ok])) > 0.05),
        verdict=dict(
            growth_links_the_two_times=bool(np.allclose(ratio[ok], 1.0, atol=0.01)),
            reading=('the ratio is k-dependent, 0.96 at the largest scales and 0.74 at small ones, '
                     'which is sub-horizon Phi decay through the residual radiation era that a '
                     'matter-only growth equation does not carry'),
            decision=('the ORDERED carry at z = 12.8 is correct and r7845 was right; this seat\'s '
                      'own earlier decision to start at z = 188 is REVERSED, because the lower '
                      'chi^2 there was the truncation error partly cancelled by a growth error '
                      'rather than a better model'),
            what_is_still_owed=('the 44.4 per cent of missing neutrino suppression and the 2.05 of '
                                'shape error are both real and neither is fixed by moving the '
                                'start: that needs Phi carried through the radiation era, a larger '
                                'instrument change than this order asks for')))
    print('  a(eta=%.0f) = %.6f (z = %.2f), radiation/matter = %.4f'
          % (eta1, a1, 1 / a1 - 1, radiation_share(a1)), flush=True)
    print('  a(eta=%.0f) = %.6f (z = %.1f), radiation/matter = %.4f'
          % (eta2, a2, 1 / a2 - 1, radiation_share(a2)), flush=True)
    print('  the ratio Phi(a1) / [Phi(a2) g(a1)/g(a2)] runs %.4f to %.4f, median %.4f'
          % (out['ratio_min'], out['ratio_max'], out['ratio_median']), flush=True)
    print('  k-dependent: %s   ⇒ %s' % (out['k_dependent'], out['verdict']['decision']), flush=True)
    with open(os.path.join(_HERE, 'carry_validity.json'), 'w') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('  wrote carry_validity.json', flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
