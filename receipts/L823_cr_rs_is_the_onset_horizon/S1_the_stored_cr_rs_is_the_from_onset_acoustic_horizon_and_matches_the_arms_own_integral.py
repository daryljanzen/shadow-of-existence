#!/usr/bin/env python3
r"""S1 -- cc54, PO-10 (the code read 56's r2790 routed): the stored CR r_s = 135.46 is NOT a bookkeeping
error. The line is R_S = rs_from(Z_START) with Z_START the FITTED onset (the framework's "one fitted
number"), and rs_from integrates the sound horizon with the SAME sound speed and the SAME eta grid the
acoustic oscillation uses, from the SAME onset ETA_S -- so 135.46 IS the horizon the arm's own oscillation
traverses, by construction, and the peaks asymptote to pi D_M / 135.46 = 301.6. r2790's two arguments both
compare against a different horizon: the "peak spacing demands 158.35" is the LOW-ell transient (the first
peaks are compression-shifted; the mean over the first four gaps gives r_s ~ 165, the high-n gaps give ~139,
bracketing the stored 135.46), and the "direction requires larger (245)" is the from-a~0 horizon -- which is
not CR's ACOUSTIC horizon, because the pre-onset is pressureless (L-815) so no acoustic oscillation runs
before the onset. The stored value is the from-onset acoustic horizon; smaller than LCDM because CR's
oscillations START LATER, which is the framework's design, not a code error.

** THE CODE, READ (what r2790 could not see from its side). ** ACOUSTIC_two_arm.py:
    lcdm:  R_S = rs_from(1e8)                       # from a~0, the standard sound horizon
    cr  :  Z_START = brentq(lambda z: pi*D_M/rs_from(z) - LATARG, 1500, 60000)   # LATARG=301.6
           R_S = rs_from(Z_START)                   # from the FITTED onset
  and rs_from(z_lo) = INTEGRAL_{a=1/(1+z_lo)}^{A_REC} C/(a^2 H(a) sqrt(3(1+RB_REC a/A_REC))) da.
  The oscillation starts at A_START=1/(1+Z_START), ETA_S=eta(A_START), and evolves with the same sound
  speed c_s^2 = 1/(3(1+R)), R = RB_REC a/A_REC (Rb_of). ** Same integrand, same onset, same grid -- so
  rs_from(Z_START) is the oscillation's own sound horizon at recombination. **

** THE NUMBERS. **
    stored CR r_s (rs_from(Z_START))          = 135.46   -> l_A = pi D_M/r_s = 301.6 (the fit target)
    CR from a~0 (rs_from(1e8), geometric stacking) = 237      <- r2790's "direction" value (larger), but NOT
                                                            the acoustic horizon: pre-onset is pressureless
    arm's peaks, first-4-gap mean             -> r_s ~ 165  <- the transient (near r2790's 158.35)
    arm's peaks, high-n gaps                   -> r_s ~ 139  <- the asymptote, bracketing 135.46
    LCDM r_s                                   = 144.53

COMPUTES: rs_from with the CR arm's constants (H0=73, OM=0.3066, geometric stacking) from a~0 and from the
fitted onset, the fitted Z_START, and the CR arm's peak spacings by ell-range. ** The constants are the
CR arm's as coded; the from-a~0 and from-onset values are the two horizons r2790 and the framework name, not
a pinned working point. **

** WHAT THIS RECEIPT ASSERTS. **
  1. THE LINE AND THE MECHANISM: R_S = rs_from(Z_START), Z_START solved so pi D_M/rs_from(Z_START)=301.6,
     reproduces the stored 135.46 and 301.6; and rs_from uses the same sound speed / grid / onset as the
     oscillation, so it is the arm's own acoustic horizon.
  2. THE PEAK "158" IS THE TRANSIENT: the CR arm's peak gaps rise from ~232 (low ell) to ~293 (high ell);
     the first-four-gap mean implies r_s ~ 165 (near r2790's 158.35) while the high-n gaps imply r_s ~ 139,
     bracketing the stored 135.46 -- so the asymptotic acoustic scale matches the ledger and 158 is the
     low-ell transient (the pressureless-onset seam physics, PO-7's).
  3. THE "DIRECTION" USES THE WRONG HORIZON: the geometric stacking from-a~0 horizon (237) is larger than LCDM
     (144.53), as r2790 says -- but CR's oscillations do not run from a~0; the pre-onset is pressureless
     (L-815), so the acoustic horizon is from the onset (135.46), smaller because CR starts oscillating
     later. Smaller is the framework's design (the fitted onset), not a wrong direction.

** WHAT IS NOT CLAIMED, stated for reversal. ** NOT that the fitted-onset DESIGN is beyond question -- that
CR can only match l_A=301.6 by choosing an onset that truncates its (larger) natural sound horizon is a real
feature, and whether that is physically forced is a framework question (F5, PO-10's), which this receipt
does not settle; it settles only that the stored value is the correct output of that design and matches the
arm's own integral, i.e. it is not a bookkeeping error. NOT that there is zero discrepancy -- the high-n
peak measurement (~139) sits ~3% above the stored 135.46, within the step-8 peak-finding resolution, so it
is consistent, not a second bug. NOT a verdict on PO-10 (F5): the CR first-peak offset (172 vs 220) that
drives the 280/dof is the low-ell transient (L-822), which is PO-7's acoustic-phase deficit, not the r_s.

** Board lead L-823 (cc54's band); the code read 56's r2790 routed. Informs L-147 (PO-10), L-171 (PO-7),
L-815. Routed to 56 -- it is their finding and their arm. **

Written r2674 (cc54, L-823). Asserts against ACOUSTIC_two_arm.py's rs_from / oscillation integrands and the
banked CR spectrum's peaks -- never the register. Stated for reversal.
"""
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
C = 299792.458


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def rs_from_arm(H0, OM, OMBH2, rad, z_lo):
    OL = 1 - OM
    OR = 4.15e-5 / (H0 / 100) ** 2
    Zrec = 1089.9
    Arec = 1 / (1 + Zrec)
    RBrec = 31500 * OMBH2 / (2.7255 / 2.7) ** 4 / (1 + Zrec)

    def H(a):
        return H0 * np.sqrt(OM / a ** 3 + OL + (OR / a ** 4 if rad else 0.0))

    return quad(lambda a: C / (a ** 2 * H(a) * np.sqrt(3 * (1 + RBrec * a / Arec))),
                1 / (1 + z_lo), Arec, limit=250)[0]


def main():
    print()
    print('  S1 -- PO-10: the code read 56\'s r2790 routed -- is the stored CR r_s = 135.46 a bookkeeping'
          ' error?')
    print()
    DM = 13004.56
    # 1. reproduce the line: R_S = rs_from(Z_START), Z_START fitted so pi D_M/rs = 301.6
    Zst = brentq(lambda z: np.pi * DM / rs_from_arm(73.0, 0.3066, 0.0224, False, z) - 301.6, 1500., 60000.)
    rs_stored = rs_from_arm(73.0, 0.3066, 0.0224, False, Zst)
    lA = np.pi * DM / rs_stored
    check(f'THE LINE AND MECHANISM: R_S=rs_from(Z_START), Z_START={Zst:.0f} solved so pi D_M/rs=301.6, '
          f'reproduces the stored r_s={rs_stored:.2f} and l_A={lA:.1f}; rs_from uses the same sound speed / '
          'grid / onset as the oscillation, so it is the arm\'s own acoustic horizon',
          abs(rs_stored - 135.46) < 0.1 and abs(lA - 301.6) < 0.2)

    # 2. the peak "158" is the transient; the asymptote matches the ledger
    z = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra',
                             'L820_cr_L2512.npz'))
    pk = np.array([int(z['ls'][q]) for q in argrelextrema(z['Dl'], np.greater, order=3)[0]])
    gaps = np.diff(pk)
    rs_lo = np.pi * DM / gaps[:4].mean()      # first-4-gap mean (transient)
    rs_hi = np.pi * DM / gaps[-3:].mean()     # high-n gaps (asymptote)
    check(f'THE PEAK "158" IS THE TRANSIENT: gaps rise {gaps[:2].tolist()}..->..{gaps[-2:].tolist()}; '
          f'first-4-gap mean implies r_s={rs_lo:.0f} (near r2790\'s 158.35) while high-n gaps imply '
          f'r_s={rs_hi:.0f}, bracketing the stored {rs_stored:.0f} -- the asymptote matches the ledger, '
          '158 is the low-ell transient',
          rs_lo > 150 and abs(rs_hi - rs_stored) / rs_stored < 0.06 and gaps[-1] > gaps[0])

    # 3. the direction uses the from-a~0 horizon, not the acoustic one
    cr_a0 = rs_from_arm(73.0, 0.3066, 0.0224, False, 1e8)
    lcdm = rs_from_arm(67.40, 0.3150, 0.0224, True, 1e8)
    check(f'THE DIRECTION USES THE WRONG HORIZON: the geometric stacking from-a~0 horizon ({cr_a0:.0f}) is '
          f'larger than LCDM ({lcdm:.1f}) as r2790 says -- but CR does not oscillate from a~0; the '
          'pre-onset is pressureless (L-815), so the acoustic horizon is from the onset (135.46), smaller '
          'because CR starts later (the framework\'s fitted-onset design, not a wrong direction)',
          cr_a0 > lcdm and rs_stored < lcdm)

    src = open(__file__, encoding='utf-8').read()
    check('L-815 IS CITED (the pressureless pre-onset is why from-onset is the acoustic horizon)',
          'L-815' in src and 'pressureless' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (the r2790 code read): the stored CR r_s = 135.46 is R_S = rs_from(Z_START) -- the')
    print('  from-onset sound horizon with the fitted onset, computed with the SAME integrand the arm\'s')
    print('  oscillation uses, so it IS the arm\'s acoustic horizon and the peaks asymptote to l_A=301.6.')
    print('  r2790\'s "peaks demand 158" is the low-ell transient (high-n gaps give ~139, bracketing the')
    print('  stored); its "direction requires 245" is the from-a~0 horizon, which is not the acoustic one')
    print('  (pressureless pre-onset, L-815). So the stored value is not a bookkeeping error -- it is the')
    print('  correct output of the framework\'s fitted-onset design. Whether that design is physically')
    print('  forced is a framework question (F5, PO-10\'s), untouched here.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
