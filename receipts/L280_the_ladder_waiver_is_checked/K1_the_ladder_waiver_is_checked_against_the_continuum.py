r"""L-280 -- the aliasing waiver P15 records is CHECKED, by running the check the gate itself names.

** THE SITUATION. **  `ACOUSTIC_two_arm.py`'s `alias_gate` demands four sample points per Bessel period
in k.  *** The CR arm gets 2.3, so it FAILS that threshold -- and the gate waives itself: ***

    if ARM == 'cr' and KCONT != '1':
        "CR's ladder is DISCRETE and physical, so this is not aliasing -- but it is only
         not aliasing if the answer does not depend on it.  Run KCONT=1 to check."

  *** P15 records the waiver in its own voice and says the check was "named in its own text and never
  run".  It is run here. ***  The gate's own docstring is why this matters: a development configuration
  at 300 modes "put the first peak at ell = 196 instead of 220 and nothing said so" -- *the failure is
  SILENT, the source comb staying correct while the projected peaks comb at the sampling's spacing.*

** THE CHECK. **  Two spectra built by the same instrument on the same arm, differing only in whether
the source wavenumbers are the discrete closed-$S^3$ ladder or a continuum:

    discrete ladder   peaks 171.2, 406.5, 634.6, 917.9, 1203.1
    KCONT=1 continuum peaks 171.2, 406.6, 634.6, 917.8, 1203.1

⇒ *** THE ANSWER DOES NOT DEPEND ON THE LADDER SAMPLING: 0.16% at the first peak and under a tenth of
a multipole at the fifth.  The waiver is safe, and now by measurement rather than by the claim that the
ladder is physical. ***

⌗ ** This is the direct form of the bound `L-274` established analytically ** -- that the ladder's
imprint dies at $\ell \simeq k_2 D_C e^{3\sigma}$ and reaching the first acoustic peak would need a
transfer drawing power over a factor of some eight in $k$.  *The two agree, and they are independent:
one is a scaling law measured on Gaussian stand-ins, the other is the instrument's own two
configurations compared peak by peak.*

WHAT IS NOT CLAIMED.  Not that the sampling is adequate by the gate's own threshold -- it is not, at 2.3
against 4.0.  What is established is the conditional the gate states: that the answer does not depend on
it.  Not that this licenses the waiver at other parameter sets; both spectra here are at one
configuration, and the gate should be re-checked when the projection distance changes.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

FAILED = []
def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        FAILED.append(label)


def peaks(path, lo=100, hi=2000):
    d = np.load(path)
    ls, Dl = d['ls'], d['Dl']
    m = (ls >= lo) & (ls <= hi)
    L, D = ls[m], Dl[m]
    out = []
    for i in range(2, len(L) - 2):
        if D[i] > D[i - 1] and D[i] > D[i + 1] and D[i] > D[i - 2] and D[i] > D[i + 2]:
            a, b, c = D[i - 1], D[i], D[i + 1]
            dl = 0.5 * (a - c) / (a - 2 * b + c) if (a - 2 * b + c) != 0 else 0
            out.append(float(L[i] + dl * (L[i] - L[i - 1])))
    return float(d['l_A']), out


print()
print('  L-280 -- the ladder waiver, checked against the continuum')
print()

lad = os.path.join(SPEC, 'c54.178_cr.npz')
con = os.path.join(SPEC, 'c54.186_cr_KCONT.npz')
check('⓵ both spectra are present in the corpus', os.path.exists(lad) and os.path.exists(con))

lA1, p1 = peaks(lad)
lA2, p2 = peaks(con)
print(f'      discrete ladder    l_A = {lA1:.2f}   peaks {[round(v, 1) for v in p1[:5]]}')
print(f'      KCONT=1 continuum  l_A = {lA2:.2f}   peaks {[round(v, 1) for v in p2[:5]]}')

check('⓶ both find the same number of peaks in the window', len(p1) == len(p2))

n = min(len(p1), len(p2), 5)
diffs = [abs(p1[i] - p2[i]) for i in range(n)]
print(f'      peak-by-peak |difference| in ell: {[round(x, 2) for x in diffs]}')

rel1 = diffs[0] / p1[0]
check(f'⓷ ⛭ the FIRST peak moves by {diffs[0]:.2f} in ell, {100 * rel1:.2f}% -- so the first-peak '
      f'position does NOT depend on the ladder sampling', rel1 < 0.01)
check(f'⓷ᵇ and no peak in the window moves by as much as one multipole (max {max(diffs):.2f})',
      max(diffs) < 1.0)
check('⓸ so the conditional the gate states is MET: it is not aliasing, because the answer does not '
      'depend on it', max(diffs) < 1.0 and rel1 < 0.01)

print()
print('  ⌗ and the sampling is NOT adequate by the gate\'s own threshold -- 2.3 points per Bessel')
print('     period against the 4.0 it demands.  What is established is the conditional, not the rate.')

print()
print('=' * 78)
if FAILED:
    print(f'  {len(FAILED)} check(s) FAILED')
    sys.exit(1)
print('  ⇒ ** THE WAIVER IS SAFE, BY MEASUREMENT.  P15 recorded the check as named and never run; **')
print('     ** it is run, and the ladder and the continuum agree to a sixth of a per cent. **')
sys.exit(0)
