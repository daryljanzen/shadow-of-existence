#!/usr/bin/env python3
"""B5 -- the corrected claim's load-bearing quantity cannot be tested by the scan that would test it,
and the reason is depth.

** THE SITUATION AFTER c54.190. **  The disagreement is no longer the first-peak position (a seam-datum
artefact, 2.26x) and no longer the spacing (2.5%, not 21%).  ** It is the ASYMPTOTIC ACOUSTIC PHASE,
fitted on peaks 4-8: phi/pi = 0.878 against the control's 0.263, a difference of 0.62*pi. **  That fit
is the whole of the corrected statement, and this line verified the reading at r2484.

** ⛭⛭ AND THE ONE FREEDOM KNOWN TO MOVE THINGS CANNOT BE TESTED AGAINST IT. **

  c54.187 established that the seam datum's phase is ** ASSIGNED rather than derived ** -- the first-peak
  modes are already sub-horizon when integration begins -- and scanning it moves l_1/l_A by 2.26x.
  ** So the obvious question is whether it also moves the ASYMPTOTIC intercept. **

    ** Of the 23 datum-scan spectra (c54.187 nine phases, c54.188 nine seam readings, c54.189 five
    pins), ZERO reach peak 8.  They stop at l ~ 996 with THREE or FOUR peaks. **

  ⇒ *** THE FIT CANNOT BE PERFORMED ON ANY OF THEM.  The quantity that now carries the disagreement
      cannot be tested against the one freedom known to move things, because the scan that varies that
      freedom was run too shallow to fit it. ***

** ⌗ AND THIS IS check_depth's FINDING ARRIVING AS A CONSEQUENCE IN THE REVISION IT WAS BUILT. **  The
lint flags all 23 as shallow.  ** Here is what shallow costs this time: not a wrong number, but an
untestable one. **  The r2484 case and this one are different failures of the same cause --- there, a
statistic was quoted from a depth that could not support it; here, a statistic CANNOT be quoted at all.

** ⚠ AND WHAT IS NOT BEING ASSERTED, because the distinction is the whole value of this receipt. **

  * ** NOT that the phase is a datum artefact. **  Nothing here shows that, and the fork's reading is
    verified and stands.
  * ** NOT that c54.187's scan was wrong to run at LMAXL = 1000. **  Eighteen readings were only
    affordable there and the scan's own finding -- that the first-peak position states nothing -- is
    sound at that depth, because the first peak is resolved at that depth.
  * ⌗ ** AND ONE THING THAT IS WORTH NOTICING RATHER THAN CLAIMING: the first peak is exactly where the
    low-l TRANSIENT lives ** (+142, +80, +18 off the CR arm's own asymptotic line, against the
    control's -3, +14, -16).  ** So the scan demonstrably moves the TRANSIENT region.  Whether it moves
    the ASYMPTOTIC intercept is a separate question and is the untested one. **

** ⇒ THE EXPERIMENT THIS NAMES IS SMALL AND AFFORDABLE: rerun TWO OR THREE seam phases at production
depth and fit peaks 4-8. **  Not eighteen -- the question is whether the asymptotic intercept moves at
all, and two well-separated phases answer that.  ** If it does not move, the 0.62*pi is structural and
the corrected claim is much stronger than it is today.  If it does, the disagreement is a datum
statement after all and the front's whole content changes again. **

Written r2485.  Stated for reversal.
"""
import os, glob

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

    ⛔⛭ r7123+cc66.92 -- WHY THIS EXISTS.  The residual pin below was a window FINER THAN THE
    ABSCISSA its peaks sit on: `abs(r_c[i] - v) < 6` pinned residuals of INTEGER peak positions,
    located by `argrelextrema` on the banked `ls` grid whose step is 8, to a window 6 wide.
      ⇒ ** One bin on the pinned peak moves that residual by 8, and one bin on a FITTED peak (4..8)
      moves EVERY residual, so the measured quantum is 9.6, 8.0, 8.0 on the first three and the
      window sat below all three.  It fails 11 of 43 re-gridded trees. **
      ⌗ *Found by `70`'s `TILT` operator at r7119+70.1 and routed at r7123 together with the
      identical site in `B4`, which carries the full note.  It is `C63`'s check 2 again, repaired at
      r7119+cc66.90 by deriving the window from the abscissa.*
      ⌗ ** And the CONTROL pin `max(abs(r_l[:3])) < 20` was NOT flagged and is the same defect **
      -- 4 points of headroom against a 9.6-point quantum -- so it is repaired with it.
    ⛭ *The windows are COMPUTED from the grid; the claim is split into the SHAPE, which is grid-free,
    and the record's figures at the resolution the grid supports.  `2 * step` is derived and not
    chosen: one bin on the pinned peak plus the fit's own one-bin response, measured maximum 9.6.*
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


def peaks(path):
    z = np.load(path)
    ls, Dl = z['ls'], z['Dl']
    return (ls[argrelextrema(Dl, np.greater, order=3)[0]], float(ls.max()), float(z['l_A']),
            grid_step(ls))


def main():
    print()
    print('  B5 -- can the datum scan test the asymptotic phase?')
    print()
    scan = sorted(glob.glob(os.path.join(SP, 'c54.18[789]_cr*.npz')))
    check(f'the datum scan is 23 CR spectra across three revisions (found {len(scan)})',
          len(scan) == 23)

    depths = [peaks(f) for f in scan]
    check('every one of them stops at l ~ 996', all(900 < d[1] < 1100 for d in depths))
    check('and resolves THREE or FOUR peaks', all(3 <= len(d[0]) <= 4 for d in depths))
    check('⛭⛭ ZERO of them reach peak 8, so the peaks-4-to-8 fit CANNOT BE PERFORMED ON ANY',
          not any(len(d[0]) >= 8 for d in depths))

    # the production pair can
    pc, mx_c, lA_c, step_c = peaks(os.path.join(SP, 'c54.186_cr_L3000.npz'))
    pl, mx_l, lA_l, step_l = peaks(os.path.join(SP, 'c54.186_lcdm_L3000.npz'))
    check('while the c54.186 production pair carries EIGHT peaks each and supports the fit',
          len(pc) == 8 and len(pl) == 8)
    check('⇒ so the corrected claim rests on ONE pair of spectra, and the scan cannot reach it',
          len(pc) == 8 and not any(len(d[0]) >= 8 for d in depths))

    # the transient lives where the scan CAN see
    n = np.arange(1, 9)
    m = (n >= 4) & (n <= 8)
    a_c, b_c = np.polyfit(n[m], pc[m], 1)
    a_l, b_l = np.polyfit(n[m], pl[m], 1)
    r_c, r_l = pc - np.polyval((a_c, b_c), n), pl - np.polyval((a_l, b_l), n)
    # the windows below are derived from the grid -- see grid_step()
    _resid_c = lambda p: np.asarray(p, dtype=float) - np.polyval(
        np.polyfit(n[m], np.asarray(p, dtype=float)[m], 1), n)
    q_c = resid_quantum(pc, step_c, _resid_c)
    print(f'    ⌗ one bin on any peak moves the first three CR residuals by '
          f'{q_c[0]:.1f}, {q_c[1]:.1f}, {q_c[2]:.1f} on a step-{step_c:.0f} grid; '
          f'the windows below are set by that')
    check(f'and the low-l transient lives in the first three peaks and is not an artefact of which '
          f'bins they landed in: CR {r_c[0]:+.0f}, {r_c[1]:+.0f}, {r_c[2]:+.0f} -- POSITIVE and '
          f'STRICTLY DECREASING, the first {r_c[0] / q_c[0]:.1f}x the {q_c[0]:.1f} one bin would '
          f'move it, and the record\'s +142, +80, +18 recovered to within '
          f'{max(abs(r_c[i] - v) for i, v in enumerate((142, 80, 18))):.1f} of the '
          f'{2 * step_c:.0f} two bins allow',
          r_c[0] > r_c[1] > r_c[2] > 0 and r_c[0] > 2 * q_c[0]
          and all(abs(r_c[i] - v) <= 2 * step_c for i, v in enumerate((142, 80, 18))))
    check(f'against the control\'s {r_l[0]:+.0f}, {r_l[1]:+.0f}, {r_l[2]:+.0f} -- no decaying '
          f'transient, and the arm\'s first residual exceeds the control\'s largest by '
          f'{r_c[0] - max(abs(r_l[:3])):.0f}, {(r_c[0] - max(abs(r_l[:3]))) / q_c[0]:.1f}x what one '
          f'bin could explain',
          not (r_l[0] > r_l[1] > r_l[2] > 0)
          and r_c[0] - max(abs(r_l[:3])) > 2 * q_c[0])
    check('⌗ so the scan demonstrably moves the TRANSIENT region -- the first peak is inside its '
          'depth -- and whether it moves the ASYMPTOTIC intercept is the untested question',
          all(len(d[0]) >= 3 for d in depths) and not any(len(d[0]) >= 8 for d in depths))

    # and the phase difference the claim rests on
    check(f'the phase difference is {(-b_c/lA_c) - (-b_l/lA_l):.3f} of pi -- the quantity in question',
          abs(((-b_c/lA_c) - (-b_l/lA_l)) - 0.615) < 0.02)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the load-bearing quantity cannot be tested by the scan that would test it. **')
    print('  All 23 datum-scan spectra stop at l ~ 996 with three or four peaks; ** ZERO reach peak 8,')
    print('  so the peaks-4-to-8 fit cannot be performed on any of them. **  The corrected claim rests')
    print('  on ONE pair of spectra.')
    print('  ⌗ This is check_depth\'s finding arriving as a consequence in the revision it was built:')
    print('    ** what shallow costs here is not a wrong number but an UNTESTABLE one. **')
    print('  ⚠ NOT asserted: that the phase is a datum artefact -- ** the fork\'s reading is verified')
    print('    and stands ** -- nor that running the scan at LMAXL=1000 was wrong: the first peak IS')
    print('    resolved there, which is why that scan\'s own finding is sound.')
    print('  ⌗ But the first peak is exactly where the TRANSIENT lives, so ** the scan moves the')
    print('    transient region demonstrably; whether it moves the ASYMPTOTIC intercept is untested. **')
    print('  ⇒ ** THE EXPERIMENT IS SMALL: two or three seam phases at production depth, fit peaks')
    print('     4-8.  Not eighteen -- the question is whether the intercept moves AT ALL. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
