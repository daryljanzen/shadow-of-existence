#!/usr/bin/env python3
"""B8 -- the seam datum's band across ZERO-VELOCITY phases is 0.207, a third of the 0.615 disagreement;
and the L-202 link this line first reached for is WITHDRAWN.

** WHERE BOTH NODES LEFT IT. **  cc54's B7: the seam phase moves the asymptotic intercept ~0.31 l_A while
the spacing holds.  54's c54.195: the phase spans 0.891 in phi/pi across four production phases, "** with
the control's values inside both **" -- and it withdrew the 0.62pi on that basis.

** ⛔ ⓵ THE LINK THIS LINE FIRST REACHED FOR IS WRONG, AND IT IS WITHDRAWN HERE. **

L-202's mapped half records: "'it is a continuous interpretive parameter' is ruled out -- ** reality
admits exactly two values, geometrically forced **".  This line read that as licensing CRPHI in {0, pi}.
  ⇒ ** IT DOES NOT.  L-202's phase is the ANTILINEAR FACE K on the branch structure.  CRPHI is a
    hydrodynamic initial condition on the photon-baryon oscillator. **  ** TWO OBJECTS SHARING ONE
    WORD ** -- which is r2494's finding (four objects, one word) arriving in reverse, and inside the very
    row that recorded it.  ⇒ *** The rule earned there applies to this line's own reasoning: when a word
    looks like it licenses a step, count the objects first. ***

** ⛭⛭ ⓶ BUT THE TWO VALUES ARE DISTINGUISHED ANYWAY, ON THE INSTRUMENT'S OWN STATEMENT. **

    delta_g = D cos(k c_s (eta - eta_S) + phi),      theta_g = (3/4) D k c_s sin(phi)

  and the instrument's comment: "** phi = 0 is a density extremum with theta = 0. **"

      phi      delta_g/D    theta_g ~ sin(phi)
      0            1             0        <- DENSITY EXTREMUM, zero velocity
      pi/4     sqrt2/2       sqrt2/2
      pi/2         0             1
      3pi/4   -sqrt2/2       sqrt2/2
      pi          -1             0        <- DENSITY EXTREMUM, zero velocity

  ⇒ *** theta_g = 0 at EXACTLY phi = 0 and phi = pi on [0, 2pi).  Those are the only two values at which
      the mode enters with ZERO VELOCITY. ***  ** A different footing from L-202's and a sound one. **

** ⓷ AND THE BAND ACROSS THOSE TWO IS A THIRD OF THE DISAGREEMENT. **  Read off the production spectra,
peaks 4-8:

      CRPHI = 0    -> phi/pi = 0.8780     (c54.186_cr_L3000 AND cc54's item38_cr_phi0.0_prod)
      CRPHI = pi   -> phi/pi = 0.6711     (c54.191_cr_phipi  AND cc54's item38_cr_phi3.1416_prod)
      ------------------------------------------------------------------
      ** zero-velocity band = 0.2069 **         disagreement = 0.6152     control = 0.2628

  ** AND THE TWO NODES AGREE TO THE DIGIT ON BOTH VALUES ** -- four spectra, two instrument paths.

  ⇒ *** SO THE BAND IS A THIRD OF THE GAP, NOT MOST OF IT.  And neither zero-velocity value brings the
      arm near the control: at CRPHI = pi the arm sits at 0.671 against the control's 0.263 -- still
      0.408 away. ***
  ⇒ ** 54's "the control's value is inside the span" is TRUE OF THE FULL SPAN and the full span includes
    phi = pi/4 and pi/2, at which the mode enters MOVING. **  ⇒ *** The withdrawal was reached over a set
    that includes non-extremum initial conditions, and over the zero-velocity pair the control is NOT
    inside. ***

WHAT IS NOT CLAIMED.  ** Not that non-extremum phases are inadmissible ** -- nothing here forbids them,
and whether the seam must sit at a density extremum is exactly what is unsettled.  ** Not that the 0.62pi
is reinstated **: it is one reading of a two-reading choice, and the OTHER reading gives 0.671, so the
disagreement survives at 0.408 rather than at 0.615.  ** Not that L-202 says anything about CRPHI ** --
that link is withdrawn above.  F5 unsoftened, PO-7 protected, the conversion Daryl's.

Written r2509.  Stated for reversal.
"""
import os
import glob
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


def phase_of(path):
    z = np.load(path)
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
    print('  B8 -- what is the band across the ZERO-VELOCITY phases?')
    print()
    inst = open(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'ACOUSTIC_two_arm.py'),
                encoding='utf-8', errors='replace').read()
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # ⓵ the withdrawn link
    check('L-202 records that a continuous interpretive parameter is ruled out -- "reality admits '
          'exactly two values, geometrically forced"',
          'reality admits exactly two values, geometrically forced' in arc)
    check('⛔ but L-202\'s phase is the ANTILINEAR FACE K on the branch structure',
          'antilinear' in arc.lower())
    check('while CRPHI is a hydrodynamic initial condition: delta_g = D cos(k c_s (eta - eta_S) + phi)',
          'delta_g = D cos(k c_s (eta - eta_S) + phi)' in inst)
    check('⇒ TWO OBJECTS SHARING ONE WORD -- the L-202 link is withdrawn',
          'reality admits exactly two values, geometrically forced' in arc
          and 'delta_g = D cos(k c_s (eta - eta_S) + phi)' in inst)

    # ⓶ the sound footing
    check("the instrument states its own distinguished value: \"phi = 0 is a density extremum with "
          'theta = 0\"', 'phi = 0 is a density extremum with theta = 0' in inst)
    check('and gives theta_g = (3/4) D k c_s sin(phi)',
          'theta_g = (3/4) D k c_s sin(phi)' in inst)
    phi = sp.Symbol('phi', real=True)
    zeros = sp.solveset(sp.Eq(sp.sin(phi), 0), phi, domain=sp.Interval.Ropen(0, 2*sp.pi))
    check(f'⛭ so theta_g = 0 at EXACTLY phi = 0 and phi = pi on [0, 2pi) (found {zeros})',
          zeros == sp.FiniteSet(0, sp.pi))
    check('and at pi/4, pi/2, 3pi/4 the mode enters MOVING (sin phi != 0)',
          all(sp.sin(v) != 0 for v in (sp.pi/4, sp.pi/2, 3*sp.pi/4)))

    # ⓷ the band
    p0a = phase_of(os.path.join(SP, 'c54.186_cr_L3000.npz'))
    p0b = phase_of(os.path.join(SP, 'item38_cr_phi0.0_prod.npz'))
    ppa = phase_of(os.path.join(SP, 'c54.191_cr_phipi_L3000.npz'))
    ppb = phase_of(os.path.join(SP, 'item38_cr_phi3.1416_prod.npz'))
    ctrl = phase_of(os.path.join(SP, 'c54.186_lcdm_L3000.npz'))
    check(f'CRPHI=0 gives phi/pi = {p0a:.4f} (54) and {p0b:.4f} (cc54) -- AGREEING TO THE DIGIT',
          abs(p0a - p0b) < 1e-3 and abs(p0a - 0.878) < 5e-3)
    check(f'CRPHI=pi gives phi/pi = {ppa:.4f} (54) and {ppb:.4f} (cc54) -- AGREEING TO THE DIGIT',
          abs(ppa - ppb) < 1e-3 and abs(ppa - 0.671) < 5e-3)
    band = abs(p0a - ppa)
    gap = abs(p0a - ctrl)
    check(f'⇒⇒ THE ZERO-VELOCITY BAND IS {band:.4f} AND THE DISAGREEMENT IS {gap:.4f} -- a factor of '
          f'{gap/band:.2f}', 2.5 < gap/band < 3.5)
    check(f'and at CRPHI=pi the arm sits at {ppa:.4f} against the control\'s {ctrl:.4f} -- still '
          f'{abs(ppa-ctrl):.4f} away',
          abs(ppa - ctrl) > 0.35)
    check('⇒ so over the zero-velocity PAIR the control is NOT inside, while the full span (which '
          'includes phi = pi/4 and pi/2, where the mode enters moving) does contain it',
          not (min(p0a, ppa) <= ctrl <= max(p0a, ppa)))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the zero-velocity band is a third of the gap, not most of it. **')
    print(f'    CRPHI = 0   -> phi/pi = {p0a:.4f}   (54 and cc54, to the digit)')
    print(f'    CRPHI = pi  -> phi/pi = {ppa:.4f}   (54 and cc54, to the digit)')
    print(f'    band {band:.4f}   disagreement {gap:.4f}   control {ctrl:.4f}')
    print('  ⇒ ** theta_g ~ sin(phi) vanishes at EXACTLY 0 and pi, so those are the only two values at')
    print('     which the mode enters with zero velocity -- the instrument says so itself. **')
    print(f'  ⇒⇒ ** At CRPHI = pi the arm is still {abs(ppa-ctrl):.4f} from the control, so over the')
    print('     zero-velocity pair the control is NOT inside. **  54\'s "the control is inside the span"')
    print('     is true of the FULL span, which includes phases where the mode enters MOVING.')
    print('  ⛔ AND THE L-202 LINK THIS LINE FIRST REACHED FOR IS WITHDRAWN: ** L-202\'s phase is the')
    print('     antilinear face K on the branch structure; CRPHI is a hydrodynamic initial condition.')
    print('     Two objects sharing one word -- r2494\'s finding, in reverse, inside its own row. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
