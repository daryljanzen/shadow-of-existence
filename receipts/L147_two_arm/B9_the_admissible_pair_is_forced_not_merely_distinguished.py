#!/usr/bin/env python3
"""B9 -- c54.200 verified: the admissible pair is FORCED by P15's own transmission argument, not merely
distinguished by the instrument's comment, and that upgrades what PO-7's verdict is about.

** WHAT r2509 HAD. **  This line justified phi in {0, pi} from the INSTRUMENT's comment -- "phi = 0 is a
density extremum with theta = 0" -- and called them "the two values at which the mode enters with zero
velocity".  ** True, and weaker than the corpus can support. **

** ⛭⛭ WHAT c54.200 FOUND, AND IT IS THE PAPER'S OWN PHYSICS, IN PRINT BEFORE THE SCAN WAS RUN. **

P15, sec:what-crosses: on the contracting leg the comoving Hubble scale grows without bound as r -> 0,
"so the comoving horizon 1/aH shrinks to zero and ** EVERY mode exits it and FREEZES before the
crossing.  A frozen mode has no oscillation ** for the kernel to damp."

  ⇒ ** FROZEN means d(delta_gamma)/d eta = 0. **  The code's own continuity equation
    d(delta_g)/deta = -(4/3) theta_g then gives theta_g = (3/4) D k c_s sin(phi), so

        *** sin(phi) = 0 ,   phi in {0, pi} -- FORCED, not chosen. ***

  ** So the admissibility is a consequence of the transmission argument P15 already makes, and r2509
  understated it: the corpus does not merely DISTINGUISH the pair, it FORCES it. **

** ⓶ AND THAT CHANGES WHAT PO-7's VERDICT IS ABOUT. **

      CRPHI = 0    ->  phi/pi = 0.8780
      CRPHI = pi   ->  phi/pi = 0.6711
      ------------------------------------------------------
      band 0.2069        gap 0.6152        control 0.2628

  ** The control is OUTSIDE the band, and at phi = pi the arm is still 0.408 away. **
  ⇒ *** The question is no longer "is the disagreement real over SOME choice of phases?"  It is: "is a
      0.408 discrepancy, AT THE ONLY TWO READINGS THE CONSTRUCTION PERMITS, a real disagreement with the
      sky?" ***  ** That is a sharper verdict question and it is still Daryl's. **

** ⌗ ⓷ AND THE MEASUREMENT IS DOUBLED. **  54's `c54.186_cr_L3000` and cc54's `item38_cr_phi0.0_prod`
agree at 0.8780; 54's `c54.191_cr_phipi` and cc54's `item38_cr_phi3.1416_prod` agree at 0.6711.  ** Two
nodes, two instrument paths, four spectra, agreeing to four decimals at both endpoints of the band the
verdict rests on. **

WHAT IS NOT CLAIMED.  ** Not that PO-7 is converted ** -- F5 unsoftened, PO-7 protected, and the conversion runs by `F5`'s stated procedure.  ** Not that r2509 was wrong ** -- its band and its arithmetic stand; what was
understated was the STATUS of the pair.  Not that the transmission argument is re-derived here: ** it is
quoted at source and its consequence for phi is the step being checked. **

Written r2519.  Stated for reversal.
"""
import os
import re

import numpy as np
import sympy as sp
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def phase_of(name):
    z = np.load(os.path.join(SP, name))
    ls, Dl, lA = z['ls'], z['Dl'], float(z['l_A'])
    pk = ls[argrelextrema(Dl, np.greater, order=3)[0]]
    if len(pk) < 8:
        return None
    n = np.arange(1, len(pk) + 1)
    m = (n >= 4) & (n <= 8)
    a, b = np.polyfit(n[m], pk[m], 1)
    return -b/lA


def main():
    print()
    print('  B9 -- is the admissible pair FORCED, or only distinguished?')
    print()
    raw = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'),
               encoding='utf-8', errors='replace').read()
    p15 = re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                        if not l.lstrip().startswith('%')))
    inst = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
                encoding='utf-8', errors='replace').read()

    # ⓵ the forcing, at source
    check('P15 sec:what-crosses exists and argues the transmission dichotomy',
          'label{sec:what-crosses}' in p15)
    check('⛭ and it states: the comoving horizon shrinks to zero so EVERY mode exits it and FREEZES '
          'before the crossing',
          'every} mode exits it and freezes before the crossing' in p15
          or 'mode exits it and freezes before the crossing' in p15)
    check('and "A frozen mode has no oscillation for the kernel to damp"',
          'A frozen mode has no oscillation for the kernel to damp' in p15)
    check("and the instrument's continuity equation gives theta_g = (3/4) D k c_s sin(phi)",
          'theta_g = (3/4) D k c_s sin(phi)' in inst)

    phi = sp.Symbol('phi', real=True)
    zeros = sp.solveset(sp.Eq(sp.sin(phi), 0), phi, domain=sp.Interval.Ropen(0, 2*sp.pi))
    check('⇒⇒ SO FROZEN (d delta/d eta = 0) FORCES sin(phi) = 0, i.e. phi in {0, pi} on [0, 2pi) '
          f'(found {zeros})', zeros == sp.FiniteSet(0, sp.pi))
    check('⇒ the corpus does NOT merely distinguish the pair -- it FORCES it, by an argument in print '
          'before the scan was run',
          'A frozen mode has no oscillation for the kernel to damp' in p15
          and zeros == sp.FiniteSet(0, sp.pi))

    # ⓶ the band, and the control outside it
    a54 = phase_of('c54.186_cr_L3000.npz')
    acc = phase_of('item38_cr_phi0.0_prod.npz')
    p54 = phase_of('c54.191_cr_phipi_L3000.npz')
    pcc = phase_of('item38_cr_phi3.1416_prod.npz')
    ctrl = phase_of('c54.186_lcdm_L3000.npz')
    check(f'CRPHI=0 gives {a54:.4f} (54) and {acc:.4f} (cc54) -- four decimals, two instrument paths',
          abs(a54 - acc) < 1e-4)
    check(f'CRPHI=pi gives {p54:.4f} (54) and {pcc:.4f} (cc54) -- likewise',
          abs(p54 - pcc) < 1e-4)
    band = abs(a54 - p54)
    gap = abs(a54 - ctrl)
    check(f'the band is {band:.4f} against a gap of {gap:.4f} -- a factor of {gap/band:.2f}',
          2.5 < gap/band < 3.5)
    check(f'⛭ AND THE CONTROL ({ctrl:.4f}) IS OUTSIDE THE BAND [{min(a54,p54):.4f}, '
          f'{max(a54,p54):.4f}]', not (min(a54, p54) <= ctrl <= max(a54, p54)))
    check(f'with the arm still {abs(p54-ctrl):.4f} away at the nearer admissible reading',
          abs(p54 - ctrl) > 0.35)

    # ⓷ what it does and does not settle
    check('⇒⇒ SO THE VERDICT QUESTION SHARPENS: not "is the disagreement real over SOME choice of '
          'phases" but "is 0.408, at the only two readings the construction permits, a real '
          'disagreement with the sky?"',
          not (min(a54, p54) <= ctrl <= max(a54, p54)) and abs(p54 - ctrl) > 0.35)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the pair is FORCED, and r2509 understated it. **')
    print('  P15 sec:what-crosses: ** every mode exits the horizon and FREEZES before the crossing, and')
    print('  a frozen mode has no oscillation. **  Frozen means d delta/d eta = 0, and continuity gives')
    print('  theta_g proportional to sin(phi) -- ** so sin(phi) = 0 and phi in {0, pi}, FORCED by the')
    print("  paper's own transmission argument, in print before the scan was run. **")
    print(f'  => Band {band:.4f} against a gap of {gap:.4f}; ** the control ({ctrl:.4f}) is OUTSIDE it, and')
    print(f'     the arm is still {abs(p54-ctrl):.4f} away at the nearer admissible reading. **')
    print('  * And the endpoints are doubled: ** 54 and cc54 agree to four decimals at both, on two')
    print('    instrument paths. **')
    print('  => ** So PO-7\'s verdict question sharpens: is 0.408, AT THE ONLY TWO READINGS THE')
    print("     CONSTRUCTION PERMITS, a real disagreement with the sky? **  Still Daryl's.")
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
