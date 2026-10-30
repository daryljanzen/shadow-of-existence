#!/usr/bin/env python3
r"""r7639+cc66 -- ** WHAT A SWAP RE-RUN ON THE ARM OF RECORD WOULD NEED, AS A NUMBER RATHER THAN A
REQUEST. **

`P15_the_windows_phase_spread_...` re-points onto the arm of record and three of its gates go red.  All
three trace to ONE quantity that is not computed in the receipt at all: the swap coefficient
`SRCTAPER`, read out of the banked run as `T['swap']['taper']`.  That coefficient was SOLVED, before any
swap ran, to take the CONTROL's band-summed phase spread to the NAMESAKE arm's.  The arm of record's
window is a different width, so the banked coefficient is the wrong one for it, and no edit to the
receipt can make it the right one -- only a new instrument run can.

** SO THIS SCRIPT DOES THE SOLVE THE RE-RUN WOULD NEED, AND VALIDATES IT AGAINST A NUMBER COMPUTED
ELSEWHERE FIRST. **  `weight` and `spread` are lifted verbatim from the receipt (they depend on nothing
but `np` and the bank), and the lift is checked by reproducing the receipt's own printed figure --
`SRCTAPER=0.000110088` takes the control to `0.06424` -- before the solve is believed.  Then the same
bisection the original solve must have run is re-run against the arm of record's spread.

** AND IT SORTS THE RECEIPT'S THREE RED GATES, WHICH I HAD WRONG. **  My first reading was that all
three were bank-blocked on this coefficient.  Reading `alpha_for` says otherwise: PART 4's INVERSION
route solves its own coefficient from the arm's own narrowing and uses the banked pair only as the two
fit nodes of its response quadratic, which does not care whether `SRCTAPER` is arm-matched.  ⇒ So the
inversion's shares are the ARM OF RECORD's answer and wait on nothing: a seventh to a half, not a
quarter to a half.  Only the DIRECT-SWAP route, which reads the excess against the tapered control
itself, is blocked -- and its blockage has a sign fixed without any model.

⛔ ** WHAT IS NOT CHECKED HERE, AND IS SAID RATHER THAN LEFT TO BE FOUND. **  Two of the receipt's
PASSING gates are bank-affected in the same way and one of them sits close to its own threshold, so
they are no more readable than the FAILS: the two-routes gate (`0.18 < closed < 0.42`, predicted
`0.15`--`0.25` after the re-run) and the asymmetry gate's SIZE limb (`SH_H > 0.5`, the receipt's 72 per
cent of the peak-height excess, which falls with the coefficient).  The asymmetry gate's RATIO limb is
the paragraph's load-bearing claim and is the sturdier of the two, but it is not coefficient-free
either: the receipt's own two coefficients put it at 5.4-fold at 1.5 per cent narrowing and 2.25-fold
at 18.7, so the trend runs the favourable way and the re-run is what settles it.  *None of that is
computed here -- it needs the peak locator and the binning, which the re-run measures in one pass, so
building a projection for it would be waste.*

Exits 1 if the lift does not reproduce the receipt's printed figure, if the solve does not recover the
banked coefficient, if the solved coefficient does not land its target, if the response rows do not
reproduce the receipt's printed table, or if the monotonicity the sign argument rests on does not hold.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

NF = 3.0                       # the receipt's window cut, in FWHM of the visibility
NAMESAKE = 'r6959_eta_cr'      # the arm `cc66.46` measured and the banked taper was solved against
RECORD = 'r6959_eta_cr_leafrec1'   # the arm of record
CONTROL = 'r6959_eta_lcdm'

PRINTED_NAMESAKE = 0.06424     # the receipt's own PART 3 line, on the namesake arm
PRINTED_CONTROL = 0.06523      # the receipt's header, the control's own spread


def weight(d, key='w2md', nf=NF, taper=0.0, s0=None, nrm=False):
    """lifted VERBATIM from the receipt -- the amplitude weight across the window, abscissa r_s,leaf"""
    ee, els, w = d['eta'], float(d['eta_ls']), float(d['eta_ls_w'])
    m = (ee >= els - nf * w) & (ee <= els + nf * w)
    e, s = ee[m], d['rs_leaf'][m]
    a = np.sqrt(np.maximum(d[key][m], 0.0))
    if taper != 0.0:
        _s0 = float(d['rs_leaf'][int(np.argmin(np.abs(ee - els)))]) if s0 is None else s0
        _t = np.exp(-taper * (s - _s0) ** 2)
        if nrm:
            _g = d['vis'][m]
            _t = _t / (float(np.trapezoid(_g * _t, e)) / float(np.trapezoid(_g, e)))
        a = a * _t[:, None]
    return e, s, a


def spread(d, b=None, **kw):
    """lifted VERBATIM from the receipt"""
    e, s, a = weight(d, **kw)
    w = a.sum(axis=1) if b is None else a[:, b]
    t = float(np.trapezoid(w, e))
    mu = float(np.trapezoid(w * s, e)) / t
    return float(np.sqrt(max(np.trapezoid(w * (s - mu) ** 2, e) / t, 0.0)))


def sig(tag, **kw):
    d = np.load(os.path.join(SP, tag + '.npz'))
    return spread(d, **kw) / float(d['r_s'])


def solve(target, s0, lo=0.0, hi=1e-2, it=200):
    """bisect SRCTAPER so the tapered CONTROL's band-summed spread lands on `target`.  Monotone: a
    larger coefficient narrows the window, so the spread decreases in the coefficient."""
    d = np.load(os.path.join(SP, CONTROL + '.npz'))
    rs = float(d['r_s'])
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        if spread(d, taper=mid, s0=s0) / rs > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def main():
    fails = []
    T = np.load(os.path.join(SP, 'r6959_swap_lcdm.npz'))
    AL, S0 = float(T['taper']), float(T['taper_s0'])

    S_CTL = sig(CONTROL)
    S_NSK = sig(NAMESAKE)
    S_AOR = sig(RECORD)
    print(f"  the control's own band-summed spread        {S_CTL:.5f} of r_s "
          f"(receipt header {PRINTED_CONTROL})")
    print(f"  the namesake arm's                          {S_NSK:.5f} of r_s "
          f"(receipt header {PRINTED_NAMESAKE})")
    print(f"  the arm of record's                         {S_AOR:.5f} of r_s")

    # ---- ⓵ VALIDATE THE LIFT against a figure this script did not compute -----------------------
    BANKED = sig(CONTROL, taper=AL, s0=S0)
    print(f"\n  banked SRCTAPER={AL:.9g} takes the control to {BANKED:.5f}")
    if abs(BANKED - PRINTED_NAMESAKE) > 5e-5:
        fails.append(f"the lift does not reproduce the receipt's printed {PRINTED_NAMESAKE}: "
                     f"got {BANKED:.5f}")
    if abs(S_NSK - PRINTED_NAMESAKE) > 5e-5 or abs(S_CTL - PRINTED_CONTROL) > 5e-5:
        fails.append(f"the lifted spreads do not reproduce the receipt's header "
                     f"({S_CTL:.5f}, {S_NSK:.5f})")

    # ---- ⓶ AND RE-DERIVE THE BANKED COEFFICIENT, which shows the solve is the right solve -------
    RE = solve(S_NSK, S0)
    print(f"  re-solving for the NAMESAKE arm's spread gives SRCTAPER={RE:.9g} "
          f"-- the banked value to {abs(RE / AL - 1):.1e} relative")
    # ⛭ the bar is 1e-6 and not a per cent: perturbed, the recovery holds to better than 1e-9, so a
    # loose bar here would gate nothing.  It being EXACT is the whole point -- it says the lift is the
    # same operation the original solve ran, not merely a similar one.
    if abs(RE / AL - 1) > 1e-6:
        fails.append(f"the solve does not recover the banked coefficient: {RE:.6g} against {AL:.6g}")

    # ---- ⓷ WHAT THE RE-RUN WOULD NEED -----------------------------------------------------------
    NEW = solve(S_AOR, S0)
    LAND = sig(CONTROL, taper=NEW, s0=S0)
    print(f"\n  ⛭ THE ARM OF RECORD NEEDS SRCTAPER={NEW:.9g} (lands {LAND:.5f} against {S_AOR:.5f}), "
          f"which is {100 * (NEW / AL - 1):+.1f} per cent of the banked coefficient")
    print(f"     taper_s0 unchanged at {S0:.6g}.")
    # ⛔ AND THE LARGE COEFFICIENT DOES NOT MOVE, WHICH I CHECKED RATHER THAN ASSUMED.  My first
    # reading of this was that `SRCTAPERBIG` scales with the small one; measured, it does not, because
    # it was never arm-matched: it narrows the control by 18.7 per cent against the namesake arm's 1.5,
    # so it is the FAR probe point of a two-point response calibration and not a swap of any arm's
    # spread.  Only the small coefficient is solved from an arm.
    ABG = float(np.load(os.path.join(SP, 'r6959_big_lcdm.npz'))['taper'])
    NAR_BIG = 1.0 - sig(CONTROL, taper=ABG, s0=S0) / S_CTL
    print(f"     SRCTAPERBIG={ABG:.9g} stays as it is: it narrows the control by "
          f"{100 * NAR_BIG:.1f} per cent against the namesake arm's "
          f"{100 * (1 - S_NSK / S_CTL):.2f} and the arm of record's {100 * (1 - S_AOR / S_CTL):.2f}, "
          f"so it is the far probe point of the response calibration, not an arm-matched swap.")
    print(f"     ⛔ and that is the whole defect in one number: the banked swap imposes "
          f"{(1 - S_NSK / S_CTL) / (1 - S_AOR / S_CTL):.2f} times the narrowing the arm of record "
          f"has, which is why the direct-swap route overshoots the lowest band below unity.")
    if not NAR_BIG > 10 * (1 - S_NSK / S_CTL):
        fails.append("the large coefficient is arm-sized after all -- re-read the solve")
    if abs(LAND - S_AOR) > 2e-5:
        fails.append(f"the solved coefficient does not land the arm of record's spread: "
                     f"{LAND:.5f} against {S_AOR:.5f}")

    # ---- ⓸ AND HOW NARROW THE ASK IS, WHICH IS ALSO MEASURED AND NOT ASSUMED --------------------
    # The taper is applied to the CONTROL's source, so the six tapered banks are all control runs and
    # none of them reads an arm.  Only the three that carry the SMALL coefficient change.
    SMALL = [t for t in ('swap', 'big', 'swapall', 'bigall', 'nswap', 'nbig')
             if abs(float(np.load(os.path.join(SP, f'r6959_{t}_lcdm.npz'))['taper']) - AL) < 1e-12]
    print(f"\n  ⇒ THE ASK: re-run {len(SMALL)} of the six tapered controls -- {', '.join(SMALL)} -- with")
    print(f"     SRCTAPER={NEW:.9g}, SRCTAPERBIG and SRCTAPER_S0 unchanged, every other knob unchanged.")
    print(f"     The {6 - len(SMALL)} large-coefficient banks are untouched, and no arm is re-run: the")
    print("     taper acts on the control's source, and the arm enters only through the target spread.")
    if len(SMALL) != 3:
        fails.append(f"the small coefficient is carried by {len(SMALL)} banks, not 3 -- re-read TAP")

    # ---- ⓹ AND WHAT THE RE-RUN WOULD DO TO THE TWO GATES DOWNSTREAM OF THE COEFFICIENT ----------
    # ⛭ ONLY the DIRECT-SWAP route is coefficient-blocked.  PART 4's inversion route solves its OWN
    # coefficient from the arm's narrowing (`alpha_for`) and uses the banked pair only as the two fit
    # nodes of the response quadratic, which does not care whether `AL` is arm-matched -- so the
    # inversion's shares ARE the arm of record's answer and are not waiting on anything.  The direct
    # swap reads the excess against the tapered control itself, so it is.
    #
    # The sign of that blockage is fixed WITHOUT a model: the new coefficient is SMALLER, the tapered
    # control is therefore less narrowed, `R_nswap` is smaller, the excess read against it is LARGER,
    # and the closed fraction is SMALLER.  So the re-run can only move the lowest band FURTHER above
    # unity -- the overshoot the receipt asserts there cannot come back.  The SIZE needs the response
    # quadratic, which is the receipt's own instrument, so it is reported as a prediction.
    import numpy as _np

    def _env_a(x, y, win=1.0):
        e = _np.empty_like(y)
        for j, v in enumerate(x):
            m = (x >= v - win / 2) & (x <= v + win / 2)
            e[j] = _np.mean(y[m])
        return e

    def _osc(x, y, win=1.0):
        e = _env_a(x, y, win)
        return (y - e) / e

    ACTL = _np.load(os.path.join(SP, CONTROL + '.npz'))
    QE = _np.asarray(ACTL['q_edges'], float)

    def _band_std(q, o):
        return _np.array([float(_np.std(_np.interp(_np.linspace(a, b, 400), q, o)))
                          for a, b in zip(QE[:-1], QE[1:])])

    def _row(tag):
        d = _np.load(os.path.join(SP, tag + '.npz'))
        q = d['ls'].astype(float) / float(d['l_A'])
        return _band_std(q, _osc(q, _np.asarray(d['Dl'], float)))

    C0L = _row('r6941_fine_lcdm')
    RNS, RNB = _row('r6959_nswap_lcdm') / C0L, _row('r6959_nbig_lcdm') / C0L
    print("\n  the two weight-preserving runs, recomputed here rather than quoted:")
    print("    nswap " + "  ".join(f"{x:.5f}" for x in RNS))
    print("    nbig  " + "  ".join(f"{x:.5f}" for x in RNB))
    PR_NS = [1.02684, 1.01827, 1.01936, 1.01179, 1.01531, 1.01424, 1.01485]
    PR_NB = [1.25509, 1.27014, 1.28315, 1.20187, 1.26449, 1.24213, 1.29074]
    if not (_np.allclose(RNS, PR_NS, atol=5e-5) and _np.allclose(RNB, PR_NB, atol=5e-5)):
        fails.append("the response rows do not reproduce the receipt's printed PART 3 table")

    # the AOR excess row, measured at `r7639+cc66.23` and reproduced by `r7637+70` independently
    MEAS = _np.array([1.0295, 1.0595, 1.0610, 1.0639, 1.0777, 1.0728, 1.0795])
    PRED_NS, CLOSED_NOW, CLOSED_NEW = [], [], []
    for b in range(len(QE) - 1):
        Mx = _np.array([[AL, AL ** 2], [ABG, ABG ** 2]])
        c = _np.linalg.solve(Mx, [_np.log(RNS[b]), _np.log(RNB[b])])
        PRED_NS.append(float(_np.exp(c[0] * NEW + c[1] * NEW ** 2)))
        exc_now, exc_new = MEAS[b] / RNS[b], MEAS[b] / PRED_NS[-1]
        CLOSED_NOW.append((MEAS[b] - exc_now) / (MEAS[b] - 1.0))
        CLOSED_NEW.append((MEAS[b] - exc_new) / (MEAS[b] - 1.0))
    CLOSED_NOW, CLOSED_NEW = _np.array(CLOSED_NOW), _np.array(CLOSED_NEW)
    print("\n  the DIRECT-SWAP closure, as the banked (wrong-arm) coefficient gives it and as the")
    print("  receipt's own response quadratic predicts it at the arm-of-record coefficient:")
    print("    banked    " + "  ".join(f"{100 * x:5.0f}%" for x in CLOSED_NOW))
    print("    predicted " + "  ".join(f"{100 * x:5.0f}%" for x in CLOSED_NEW))
    print(f"    ⛔ the lowest band goes from {100 * CLOSED_NOW[0]:.0f} per cent closed to "
          f"{100 * CLOSED_NEW[0]:.0f}, so it does not overshoot on either -- and the re-run moves it "
          f"AWAY from the overshoot the receipt asserts, not towards it.")
    print(f"    ⛔ and above q=1.9 the closure goes from {100 * CLOSED_NOW[1:].min():.0f}-"
          f"{100 * CLOSED_NOW[1:].max():.0f} to {100 * CLOSED_NEW[1:].min():.0f}-"
          f"{100 * CLOSED_NEW[1:].max():.0f} per cent, so the PASS the banked coefficient gives the "
          f"two-routes gate is as unreadable as the three FAILS.")
    # ⛭ AND THE BANKED COLUMN IS VALIDATED, NOT JUST PRINTED: it must reproduce what the re-pointed
    # receipt itself computed through its own `EXC`/`CLOSED`.  Those closures are reproducible from
    # `windows_phase_spread_repoint.patch.txt` beside this file -- apply it and the receipt prints
    # `closed 32% 33% 19% 21% 21% 20%` with the lowest band at `0.913`.
    RCPT_CLOSED = [0.913, 0.32, 0.33, 0.19, 0.21, 0.21, 0.20]
    if not _np.allclose(CLOSED_NOW, RCPT_CLOSED, atol=5e-3):
        fails.append(f"the banked closures do not reproduce the re-pointed receipt's own: "
                     f"{'  '.join(f'{x:.3f}' for x in CLOSED_NOW)}")
    if not (CLOSED_NEW[0] < CLOSED_NOW[0] and bool(_np.all(CLOSED_NEW < CLOSED_NOW))):
        fails.append("the smaller coefficient does not reduce the closure in every band -- "
                     "the monotonicity argument above is wrong")

    print()
    if fails:
        print("FAILED:")
        for f in fails:
            print("  - " + f)
        return 1
    print("  OK -- the lift reproduces five figures computed elsewhere, the solve recovers the")
    print("  banked coefficient EXACTLY, and the new coefficient lands its target.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
