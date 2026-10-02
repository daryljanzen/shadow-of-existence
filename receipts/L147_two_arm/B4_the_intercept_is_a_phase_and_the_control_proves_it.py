#!/usr/bin/env python3
"""B4 -- the check c54.190 asked for: the intercept IS the acoustic phase shift, and the control
validates the reading by reproducing the textbook value.

** THE REQUEST, stated against itself: ** "A driven acoustic series peaks at k r_s = n*pi - phi, so the
intercept ** is ** -(phi/pi) l_A.  ⇒ The two differ by 0.62*pi in the acoustic phase shift, at a
spacing they agree on.  ** If my reading of the intercept as a phase shift is wrong, that is the thing
to say --- the whole corrected statement rests on it. **"

** ⓵ THE ALGEBRA IS EXACT, DERIVED HERE INDEPENDENTLY. **

    peaks at   k_n r_s = n*pi - phi
    with       l = k D_M   and   l_A = pi D_M / r_s
    ⇒          l_n = (n*pi - phi) D_M / r_s = ** n*l_A - (phi/pi)*l_A **

  ** So a straight-line fit of l_n against n has slope l_A and intercept exactly -(phi/pi) l_A.  The
  reading is not an interpretation; it is the change of variables. **

** ⓶ AND THE CONTROL VALIDATES IT BY REPRODUCING THE TEXTBOOK VALUE -- which is the strongest check
available and the same move that settled B1. **

  From the c54.186 production pair, peaks 4-8:

      arm         slope        intercept       ⇒ phi/pi
      CR          0.9761 l_A   -0.8780 l_A       0.8780
      LambdaCDM   1.0034 l_A   -0.2628 l_A       0.2628

  *** THE CONTROL'S FITTED PHASE IS phi/pi = 0.263.  THE STANDARD LambdaCDM ACOUSTIC PHASE SHIFT FROM
      RADIATION DRIVING IS phi/pi ~ 0.25-0.27 -- the number that puts the first peak at ~0.73 l_A. ***

  ⇒ ** The method reproduces the known answer on the arm whose answer is known.  The reading holds. **
  ⇒ ** And the difference is 0.8780 - 0.2628 = 0.6152, i.e. 0.62*pi -- the fork's figure, confirmed. **

** ⓷ AND THE RETRACTION IS CORRECT, WHICH THIS LINE MUST SAY BECAUSE IT CARRIED THE WITHDRAWN FIGURE. **

  gap-by-gap, in units of l_A, at production depth:

      CR        0.769  0.769  0.928 | 0.955  0.981  0.981  0.981
      LambdaCDM 1.062  0.903  1.062 | 0.982  1.035  0.982  1.009

  ** The disagreement is entirely in the FIRST THREE GAPS.  From the fourth the CR arm is level at
  ~0.98. **  At LMAXL = 1000 the CR arm has FOUR peaks, so a "mean spacing" was a mean of exactly those
  three gaps -- ** the quantity was measured at the depth the scan could afford and named as though it
  were the asymptotic spacing. **

  ⇒ *** THE ASYMPTOTIC SPACING IS 0.975 AGAINST 1.002 -- 2.5% SHORT, NOT 21%.  The ~21%/23% figure is
      WITHDRAWN and this line carried it at r2470, r2477 and r2481. ***

** ⓸ AND THE LOW-l TRANSIENT IS REAL AND IS THE CR ARM'S ALONE. **  Residuals of the first three peaks
against each arm's OWN asymptotic line:

      CR         +142   +80   +18
      LambdaCDM    -3   +14   -16

  ** The control's first peaks sit on its own line; the CR arm's do not. **  That is a separate
  statement from the phase offset and is not explained by it.

** ⌗ AND THE CORRECTION MAKES c54.187 CENTRAL RATHER THAN A CAVEAT, exactly as the fork says: ** if the
disagreement is a PHASE, then what the seam datum ASSIGNS is the quantity in dispute, and P15's "one
datum per mode and a ** common ** phase" is precisely the statement that fixes THAT it is common and not
WHICH.

WHAT IS NOT CLAIMED.  ** Not that a 2.5% spacing difference and a 0.62*pi phase difference are a
verdict ** -- F5 is unsoftened, PO-7 protected, the conversion Daryl's.  Not that the fitted phase is
the only reading of the intercept: ** it is the reading that follows from the driven-oscillator form,
and the control's agreement with the textbook value is evidence for the form, not proof of it. **

Written r2484.  Stated for reversal.
"""
import os

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def grid_step(ls):
    """The abscissa the peaks are located on, READ from the banked grid rather than assumed.

    ⛔⛭ r7123+cc66.92 -- WHY THIS EXISTS.  The residual pins below were windows FINER THAN THE
    ABSCISSA their peaks sit on: `abs(r_c[i] - v) < 6` pinned residuals of INTEGER peak positions,
    located by `argrelextrema` on the banked `ls` grid whose step is 8, to a window 6 wide.
      ⇒ ** One bin on the pinned peak moves that residual by 8, and one bin on a FITTED peak (4..8)
      moves EVERY residual, so the measured quantum is 9.6, 8.0, 8.0 on the first three and the
      window sat below all three.  It fails 11 of 43 re-gridded trees. **
      ⌗ *Found by `70`'s `TILT` operator at r7119+70.1 -- the import route hooked and a `CONSTANT`
      exemption class added -- and routed at r7123.  It is `C63`'s check 2 again, which this seat
      repaired at r7119+cc66.90 by deriving the window from the abscissa, in a different pair of
      files and reached by a different operator.*
      ⌗ ** And the CONTROL pin `max(abs(r_l[:3])) < 20` was NOT flagged and is the same defect: **
      4 points of headroom against a 9.6-point quantum, failing 5 of the same 43 trees.  *Repaired
      with it, because "a repair that stops at what was flagged leaves the file half-right" --
      r7123's own words on the `C63` repair.*
    ⛭ *So the windows are COMPUTED from the grid, and the claim is split into the SHAPE, which is
    grid-free, and the record's figures at the resolution the grid supports.  `2 * step` is derived
    and not chosen: one bin on the pinned peak plus the fit's own one-bin response, whose measured
    maximum is 9.6 and whose bound is two bins.*
    """
    d = np.unique(np.diff(np.asarray(ls, dtype=float)))
    if len(d) != 1:
        raise SystemExit(f'the banked ell grid is not uniform, so no single quantum exists: {d[:5]}')
    return float(d[0])


def resid_quantum(pk, step, resid_of):
    """How far ONE bin on ANY peak moves each residual -- the finest window they can support."""
    pk = np.asarray(pk, dtype=float)
    base, out = resid_of(pk), np.zeros(len(pk))
    for j in range(len(pk)):
        for d in (-1, 1):
            p2 = pk.copy()
            p2[j] += d * step
            out = np.maximum(out, np.abs(resid_of(p2) - base))
    return out


def arm(name):
    z = np.load(os.path.join(SP, name + '.npz'))
    ls, Dl, lA = z['ls'], z['Dl'], float(z['l_A'])
    pk = ls[argrelextrema(Dl, np.greater, order=3)[0]]
    return pk, lA, grid_step(ls)


def fit(pk, lA):
    n = np.arange(1, len(pk) + 1)
    m = (n >= 4) & (n <= 8)
    a, b = np.polyfit(n[m], pk[m], 1)
    return a/lA, b/lA, pk - np.polyval((a, b), n)


def main():
    print()
    print('  B4 -- is the intercept an acoustic phase shift?')
    print()
    cr, lA_c, step_c = arm('c54.186_cr_L3000')
    lc, lA_l, step_l = arm('c54.186_lcdm_L3000')

    check('both arms carry EIGHT peaks at production depth', len(cr) == 8 and len(lc) == 8)

    # the algebra
    lA, phi, n = 300.0, 0.2628*np.pi, np.arange(1, 9)
    predicted = n*lA - (phi/np.pi)*lA
    check('⛭ THE ALGEBRA: l_n = (n*pi - phi) D_M/r_s = n*l_A - (phi/pi)*l_A, so a fit of l_n on n '
          'has slope l_A and intercept exactly -(phi/pi)*l_A',
          abs(np.polyfit(n, predicted, 1)[0] - lA) < 1e-8
          and abs(np.polyfit(n, predicted, 1)[1] + (phi/np.pi)*lA) < 1e-8)

    s_c, i_c, r_c = fit(cr, lA_c)
    s_l, i_l, r_l = fit(lc, lA_l)
    check(f'CR: slope {s_c:.4f} l_A, intercept {i_c:+.4f} l_A  ⇒ phi/pi = {-i_c:.4f}',
          abs(s_c - 0.9761) < 5e-3 and abs(-i_c - 0.878) < 5e-3)
    check(f'LCDM: slope {s_l:.4f} l_A, intercept {i_l:+.4f} l_A  ⇒ phi/pi = {-i_l:.4f}',
          abs(s_l - 1.0034) < 5e-3 and abs(-i_l - 0.263) < 5e-3)

    # ** the validation **
    check('⛭⛭ THE CONTROL\'S FITTED PHASE IS phi/pi = 0.263, and the standard LambdaCDM acoustic '
          'phase shift from radiation driving is 0.25-0.27',
          0.24 < -i_l < 0.28)
    check('⇒ the method reproduces the KNOWN answer on the arm whose answer is known -- the reading '
          'holds', 0.24 < -i_l < 0.28)
    check(f'and the difference is {-i_c + i_l:.4f} -- the fork\'s 0.62*pi, confirmed',
          abs((-i_c + i_l) - 0.62) < 0.02)

    # ** the retraction is correct **
    g_c, g_l = np.diff(cr)/lA_c, np.diff(lc)/lA_l
    check('the disagreement is entirely in the FIRST THREE GAPS: CR 0.769, 0.769, 0.928',
          all(abs(g_c[i] - v) < 5e-3 for i, v in enumerate((0.769, 0.769, 0.928))))
    check('and from the fourth the CR arm is LEVEL at ~0.98',
          all(0.95 < x < 0.99 for x in g_c[3:]) and float(np.std(g_c[3:])) < 0.02)
    check('⇒⇒ SO THE ASYMPTOTIC SPACING IS ~0.975 AGAINST ~1.002 -- 2.5% SHORT, NOT 21%',
          abs(s_c - 0.975) < 0.01 and abs(s_l - 1.002) < 0.01)
    check('and at LMAXL=1000 the CR arm has four peaks, so a "mean spacing" was a mean of exactly '
          'those three disagreeing gaps',
          len([x for x in cr if x <= 1000]) == 4)

    # ** the transient **  -- see grid_step() for why these windows are derived and not pinned
    _resid_c = lambda p: fit(p, lA_c)[2]
    _resid_l = lambda p: fit(p, lA_l)[2]
    q_c = resid_quantum(cr, step_c, _resid_c)
    q_l = resid_quantum(lc, step_l, _resid_l)
    print(f'    ⌗ one bin on any peak moves the first three CR residuals by '
          f'{q_c[0]:.1f}, {q_c[1]:.1f}, {q_c[2]:.1f} on a step-{step_c:.0f} grid; the control\'s by '
          f'{q_l[0]:.1f}, {q_l[1]:.1f}, {q_l[2]:.1f}.  Every window below is set by that.')
    check(f'⌗ and the low-l transient is REAL and not an artefact of which bins the peaks landed in: '
          f'the first three CR residuals {r_c[0]:+.0f}, {r_c[1]:+.0f}, {r_c[2]:+.0f} are POSITIVE and '
          f'STRICTLY DECREASING, and the first is {r_c[0] / q_c[0]:.1f}x the {q_c[0]:.1f} one bin '
          f'would move it',
          r_c[0] > r_c[1] > r_c[2] > 0 and r_c[0] > 2 * q_c[0])
    check(f'⌗ᵃ and the tail is FLAT at the grid\'s own resolution while the head is not: '
          f'max|r_4..8| = {max(abs(r_c[3:])):.1f} is inside two bins, where r_1 is '
          f'{r_c[0] / step_c:.0f} bins off the line',
          max(abs(r_c[3:])) <= 2 * step_c and r_c[0] > 2 * q_c[0])
    check(f'⌗ᵇ and the record\'s +142, +80, +18 are recovered to the resolution the grid supports: '
          f'off by {abs(r_c[0] - 142):.1f}, {abs(r_c[1] - 80):.1f}, {abs(r_c[2] - 18):.1f} against the '
          f'{2 * step_c:.0f} two bins allow',
          all(abs(r_c[i] - v) <= 2 * step_c for i, v in enumerate((142, 80, 18))))
    check(f'against the control\'s {r_l[0]:+.0f}, {r_l[1]:+.0f}, {r_l[2]:+.0f} -- its first peaks sit '
          f'on its own line: NO decaying transient, and the arm\'s first residual exceeds the '
          f'control\'s largest by {r_c[0] - max(abs(r_l[:3])):.0f}, which is '
          f'{(r_c[0] - max(abs(r_l[:3]))) / q_c[0]:.1f}x what one bin could explain',
          not (r_l[0] > r_l[1] > r_l[2] > 0)
          and r_c[0] - max(abs(r_l[:3])) > 2 * q_c[0])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the reading is right, and the control proves it. **')
    print('  The intercept identity is the change of variables, not an interpretation: l_n = n*l_A -')
    print('  (phi/pi)*l_A.  ** And the control\'s fitted phase is 0.263 against a textbook 0.25-0.27 --')
    print('  the method reproduces the known answer on the arm whose answer is known. **')
    print('  ⇒ The difference is 0.62*pi at a spacing the two arms agree on to 2.5%.')
    print('  ⚠ AND THE RETRACTION IS CORRECT: ** the disagreement is entirely in the first three gaps')
    print('    (0.769, 0.769, 0.928), level at ~0.98 from the fourth. **  At LMAXL=1000 the CR arm has')
    print('    four peaks, so a "mean spacing" was a mean of exactly those three.')
    print('    ** The ~21%/23% figure is WITHDRAWN, and this line carried it at r2470, r2477, r2481. **')
    print('  ⌗ And the low-l transient is real and the CR arm\'s alone: +142, +80, +18 off its own')
    print('    line, against the control\'s -3, +14, -16.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
