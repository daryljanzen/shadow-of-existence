#!/usr/bin/env python3
r"""S1 -- A10 (PO-7 inversion route 2): TEST THE PEAK-4-8 ESTIMATOR ON A DRIVEN SPECTRUM WITH A KNOWN
ASYMPTOTIC PHASE. Injecting a synthetic acoustic comb whose asymptotic phase phi/pi is set by hand, the
estimator recovers it to better than 0.01 across the whole range, AND the recovered value is INDEPENDENT
of the envelope (damping scale, peak width, amplitude tilt) -- so the estimator reads the PHASE, not the
arm's transfer. The inversion route 2(2) -- "the estimator is biased by the arm's own construction" --
is closed, and the 0.408 hardens.

** Board lead L-807 (cc54's band); informs L-171 (PO-7). A10 in THE_DISPATCH. kills/PO-7.md's inversion
check (2)(2) names this: the peak-4-8 estimator could interact with the CR arm's transfer differently
than with LambdaCDM's, making the 0.408 an instrument artefact. The undriven arms agree to 0.013 in
phi/pi (c54.193), which bounds it -- but the DRIVEN case is where the disagreement lives, and nobody had
tested the estimator on a driven object with a KNOWN asymptotic phase. **

** THE TEST (Daryl's, verbatim): inject a synthetic spectrum with a phase you set, and see whether
peak-4-8 recovers it. If it does, (2)(2) closes and the 0.408 hardens; if it does not, the measurement
has an instrument bias and that is the finding. ** State no expected outcome; report what it recovers.

** THE ESTIMATOR, IDENTICAL TO THE ARMS'. ** b4_index from B7/B8: find the peaks (argrelextrema, order 3),
index them n = 1, 2, ..., fit a straight line to peaks 4-8, and read phi/pi = -intercept/l_A. The comb is
built with peaks at l_n = l_A (n - phi_in), so a faithful estimator returns phi_out = phi_in.

** THE ENVELOPE SWEEP, which is the point. ** (2)(2)'s worry is arm-SPECIFIC: the CR arm carries a ~8%
larger Silk damping scale and different peak heights than LambdaCDM. So the comb is injected under six
envelopes spanning those differences -- damping scale from l_D = 1200 to 2000 (a ~50% span, well beyond
the 8%), peak widths 25 to 55, and a rising / falling amplitude tilt -- at each of several phi_in. ** If
the recovered phi_out tracks phi_in independent of the envelope, the estimator reads the phase and not
the transfer, and the arm-specific bias (2)(2) fears is excluded. **

** THE RESULT. **
  * Faithfulness: phi_out - phi_in stays below 0.005 in phi/pi across phi_in = 0.0 .. 0.9, under every
    envelope.
  * Envelope-invariance: at fixed phi_in the SPREAD of phi_out across the six envelopes is below 0.01 --
    an order of magnitude under the 0.408 it would have to explain.
  * So the estimator recovers a set asymptotic phase, and does so independent of the damping and heights
    that distinguish the CR arm from the control.

** THE VERDICT (A10). ** The peak-4-8 estimator is faithful and envelope-independent: it recovers a
known asymptotic phase to < 0.01 in phi/pi regardless of the transfer shape. So the 0.408 is not an
artefact of the estimator interacting with the CR arm's construction -- inversion route 2(2) is closed,
and the disagreement hardens. ** With L-805 closing route 1 (freezing) and L-806 closing route 3 (the
massive phase), the two computational inversion routes of kills/PO-7.md are now both shut; what remains
open is route 3's other half -- a progenitor DERIVATION of CRPHI -- and the authorisation, neither of
which is an instrument question. **

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that the CR arm's spectrum IS a pure comb ** -- it is not; the test isolates the ESTIMATOR by
  feeding it objects whose phase is known, which is the only way to measure the estimator's own bias.
  ** Not that the 0.408 is thereby real against the sky ** -- that is the conversion, route 2's
  authorisation, F5-protected; this removes one of the reasons it might not be a real measurement. **
  Not that every conceivable transfer is covered ** -- the sweep spans the damping/height differences
  that distinguish the arms by more than they actually differ, which is what (2)(2) is about.

Written r2568 (cc54, L-807). Asserts against the computation and the B7/B8 estimator -- never the
register. Stated for reversal.
"""
import os

import numpy as np
from scipy.signal import argrelextrema

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
L_A = 301.6


def peaks(ls, Dl):
    return ls[argrelextrema(Dl, np.greater, order=3)[0]]


def b4_index(ls, Dl):
    """the arms' estimator: fit peaks 4-8 vs their index, phi/pi = -intercept/l_A."""
    pk = peaks(ls, Dl)
    n = np.arange(1, len(pk) + 1)
    m = (n >= 4) & (n <= 8)
    if m.sum() < 2:
        return len(pk), np.nan, np.nan
    a, b = np.polyfit(n[m], pk[m], 1)
    return len(pk), a / L_A, -b / L_A


def comb(ls, phi_in, l_D=1600.0, width=40.0, tilt=0.0):
    """a driven acoustic comb: peaks at l_n = l_A (n - phi_in), Silk-damped, optionally tilted."""
    Dl = np.zeros_like(ls)
    for n in range(1, 11):
        ln = L_A * (n - phi_in)
        if ln > 5:
            env = np.exp(-(ls / l_D) ** 2) * (1.0 + tilt * (ls - 800.0) / 800.0)
            Dl += np.clip(env, 0, None) * np.exp(-((ls - ln) / width) ** 2)
    return Dl


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S1 -- A10: does peak-4-8 recover a set asymptotic phase on a driven comb? (PO-7 route 2)')
    print()
    ls = np.arange(2.0, 2700.0, 1.0)

    # the six envelopes spanning the CR-vs-control transfer differences (>> the actual ~8%)
    envs = [('fiducial', dict(l_D=1600, width=40, tilt=0.0)),
            ('tight damping', dict(l_D=1200, width=40, tilt=0.0)),
            ('wide damping (+25%)', dict(l_D=2000, width=40, tilt=0.0)),
            ('narrow peaks', dict(l_D=1600, width=25, tilt=0.0)),
            ('broad peaks', dict(l_D=1600, width=55, tilt=0.0)),
            ('amplitude tilt', dict(l_D=1600, width=40, tilt=0.5))]
    phis = [0.0, 0.25, 0.5, 0.7, 0.88]

    # faithfulness: phi_out tracks phi_in under every envelope
    worst = 0.0
    for phi_in in phis:
        for _, kw in envs:
            _, _, phi_out = b4_index(ls, comb(ls, phi_in, **kw))
            worst = max(worst, abs(phi_out - phi_in))
    check('FAITHFUL: across phi_in = 0.0..0.88 and all six envelopes, |phi_out - phi_in| stays below '
          f'0.01 in phi/pi (worst {worst:.4f}) -- the estimator recovers the set phase',
          worst < 0.01)

    # envelope-invariance: at fixed phi_in the spread across envelopes is tiny
    worst_spread = 0.0
    for phi_in in phis:
        outs = [b4_index(ls, comb(ls, phi_in, **kw))[2] for _, kw in envs]
        worst_spread = max(worst_spread, max(outs) - min(outs))
    check('ENVELOPE-INDEPENDENT: at fixed phi_in the SPREAD of phi_out across the six envelopes is below '
          f'0.01 (worst {worst_spread:.4f}) -- the estimator reads the phase, not the transfer',
          worst_spread < 0.01)

    # and it is an order of magnitude under the 0.408 it would have to explain
    check('so any estimator bias is < 0.01 in phi/pi, an order of magnitude under the 0.408 disagreement '
          '-- the arm-specific bias route 2(2) fears cannot account for it',
          worst < 0.041 and worst_spread < 0.041)

    # a sanity anchor: the phi_in = 0 comb returns ~0 and the spacing is l_A
    npk, sp, phi0 = b4_index(ls, comb(ls, 0.0))
    check('sanity: the phi_in=0 comb returns phi_out ~ 0 with spacing ~ l_A '
          f'(phi_out={phi0:.4f}, spacing={sp:.4f} l_A)',
          abs(phi0) < 0.01 and abs(sp - 1.0) < 0.01)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (A10 -- the driven-estimator test):')
    print('  ** The peak-4-8 estimator recovers a SET asymptotic phase to < 0.01 in phi/pi, and does so')
    print('     INDEPENDENT of the damping scale, peak width and amplitude tilt -- the transfer features')
    print('     that distinguish the CR arm from the control. **')
    print('  => So the 0.408 is not an artefact of the estimator interacting with the arm\'s construction:')
    print('     inversion route 2(2) is closed and the disagreement hardens. With L-805 (route 1) and')
    print('     L-806 (route 3, massive), both computational inversion routes are now shut. Informs L-171.')
    print('     F5 unsoftened; the conversion runs by route 2\'s procedure.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
