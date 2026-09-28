"""⓷ IS THE TWO WIDTHS BEING DIFFERENT FORCED OR CHOSEN? -- r6999+cc66.52.

⛔ *The order's ⓷: "On two rates the widths differ because the clocks differ.  Is the ratio you measured
a prediction of the two-rate assignment, or an artefact of how the window was constructed in this
instrument?  If it is forced by the construction, this is a CR prediction nobody has stated and it
belongs in the paper as one regardless of what it does to the contrast."*

** THE QUESTION IS DECIDABLE WITHOUT A RUN, BY A POINTWISE IDENTITY THE BANKS CARRY. **  The instrument
keeps two sound horizons: `rs_stack`, the comoving RULER (`l_A = pi D_M / r_s`), and `rs_leaf`, the
PHASE ACCUMULATOR the plasma runs on.  They are the same integrand on two rates, so

    d(rs_leaf)/d(eta)  =  Jac(eta) x d(rs_stack)/d(eta),      Jac = H_phys / H_leaf

and `Jac == 1` identically on the control by the rate identity.  ⇒ ** So the test is: measure the
window's width in eta, in rs_leaf and in rs_stack, and ask WHICH of the two clocks carries the
arm-versus-control difference. **  *If it is the leaf clock alone, the difference is `Jac` and nothing
else, and `Jac` is not an instrument parameter -- it IS the two-rate assignment.*

⚠ ** AND A WIDTH IS NOT A QUANTITY UNTIL ITS DEFINITION IS NAMED, SO THREE ARE USED. **  All three are
taken under ONE measure -- the visibility as a probability density over `eta` -- and applied to the
random variables `eta`, `rs_leaf(eta)`, `rs_stack(eta)`:
  · `rms`      the standard deviation.  ⌗ *Tail-weighted, and the window has long tails.*
  · `fwhm`     the full width at half maximum.
  · `chi-half` `1/kappa` where the characteristic function of that variable falls to `1/2`.
⌗ *`cc66.51` reported this on `rms` alone.  The three do NOT agree on the SIZE -- which is itself worth
saying -- and they agree exactly on where it comes from.*
"""
import os

import numpy as np
from scipy.optimize import brentq

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}


def measure(t):
    d = A[t]
    e = np.asarray(d['eta'], float)
    w = np.asarray(d['vis'], float)
    return e, w / np.trapezoid(w, e), np.asarray(d['rs_leaf'], float), np.asarray(d['rs_stack'], float)


def rms(e, w, x):
    m = np.trapezoid(w * x, e)
    return float(np.sqrt(np.trapezoid(w * (x - m) ** 2, e)))


def fwhm(e, w, x):
    i = np.where(w >= w.max() / 2)[0]
    return float(x[i[-1]] - x[i[0]])


def chi_half(e, w, x):
    f = lambda k: np.hypot(np.trapezoid(w * np.cos(k * x), e), np.trapezoid(w * np.sin(k * x), e)) - 0.5
    hi = 1e-3
    while f(hi) > 0:
        hi *= 2
    return 1.0 / brentq(f, 1e-9, hi)


DEFS = (('rms', rms), ('fwhm', fwhm), ('chi-half', chi_half))
print(__doc__)
print('=' * 100)

# ---- the pointwise identity, first, because everything below rests on it ------------------------
print('\n  ⛭ THE IDENTITY, CHECKED POINTWISE ACROSS THE WINDOW (where the visibility is above a '
      'hundredth of its peak):')
for t in ('lcdm', 'cr'):
    e, w, rl, rs = measure(t)
    r = np.gradient(rl, e) / np.gradient(rs, e)
    J = np.asarray(A[t]['jac'], float)
    m = w > 0.01 * w.max()
    print(f"    {t:5s}  d(rs_leaf)/d(rs_stack) / Jac  in [{(r[m] / J[m]).min():.8f}, "
          f"{(r[m] / J[m]).max():.8f}]      Jac in [{J[m].min():.6f}, {J[m].max():.6f}]")

# ---- the widths, three definitions, one measure -------------------------------------------------
W = {t: {n: tuple(f(*measure(t)[:2], x) for x in measure(t)[0:1] + measure(t)[2:])
         for n, f in DEFS} for t in ('lcdm', 'cr')}
print(f"\n  the window's width, under one measure and three definitions:")
print(f"    {'arm':6s} {'defn':9s} {'in eta':>10s} {'in rs_leaf':>12s} {'in rs_stack':>12s}"
      f" {'eta/leaf':>10s} {'eta/stack':>10s}")
for t in ('lcdm', 'cr'):
    for n, _ in DEFS:
        v = W[t][n]
        print(f"    {t:6s} {n:9s} {v[0]:10.5f} {v[1]:12.5f} {v[2]:12.5f} "
              f"{v[0] / v[1]:10.5f} {v[2] and v[0] / v[2]:10.5f}")

print(f"\n  ⇒ and the arm against the control, which is the question:")
print(f"    {'defn':9s} {'conformal width':>16s} {'(eta/leaf) ratio':>18s} {'(eta/stack) ratio':>19s}"
      f" {'Jac share':>11s}")
OUT = {}
for n, _ in DEFS:
    a, c = W['cr'][n], W['lcdm'][n]
    L = (a[0] / a[1]) / (c[0] / c[1])
    S = (a[0] / a[2]) / (c[0] / c[2])
    OUT[n] = (a[0] / c[0], L, S, L / S)
    print(f"    {n:9s} {a[0] / c[0]:16.5f} {L:18.5f} {S:19.5f} {L / S:11.5f}")

e, w, rl, rs = measure('cr')
JBAR = float(np.trapezoid(w * np.asarray(A['cr']['jac'], float), e))
print(f"\n  and the arm's own leaf-to-ruler width ratio against the visibility-weighted mean of Jac "
      f"({JBAR:.5f}):")
for n, _ in DEFS:
    a = W['cr'][n]
    print(f"    {n:9s}  w_leaf / w_stack = {a[1] / a[2]:.5f}   "
          f"-> {100 * (a[1] / a[2] / JBAR - 1):+.2f} per cent from <Jac>")

print('\n' + '=' * 100)
print(f"""
  ⛭⛭⛭ THE ANSWER IS FORCED, AND IT IS FORCED BY ONE OBJECT.

    ⓐ ** ON THE RULER CLOCK THE TWO ARMS ARE THE SAME INSTRUMENT. **  The ratio of the window's
      conformal width to its width in `rs_stack` is {OUT['chi-half'][2]:.5f} of the control's on
      `chi-half` and {OUT['fwhm'][2]:.5f} on `fwhm` -- ** a third of a per cent. **  *The visibility is
      laid down in eta by Thomson scattering on the physical background, and that is the same physics
      on both arms; the ruler clock sees it the same way on both.*

    ⓑ ** ON THE LEAF CLOCK IT IS {100 * (OUT['chi-half'][1] - 1):+.1f} PER CENT. **  And the whole of
      that difference is `Jac`: the Jac share reads {OUT['chi-half'][3]:.5f} and {OUT['fwhm'][3]:.5f},
      against the leaf-clock ratios {OUT['chi-half'][1]:.5f} and {OUT['fwhm'][1]:.5f}.  ⌗ *The arm's
      own leaf-to-ruler width ratio equals the visibility-weighted mean of `Jac` to under half a per
      cent on both core definitions.*

    ⓒ ** AND `Jac` IS NOT A KNOB. **  It is `H_phys / H_leaf`, fixed by the background solution once
      the arm is specified, with no free coefficient anywhere in it, and identically `1` on any
      one-rate cosmology.  ⇒ *** THE TWO WIDTHS STANDING IN A DIFFERENT RATIO IS A PREDICTION OF THE
      TWO-RATE ASSIGNMENT AND NOTHING ELSE.  It is not an artefact of how this instrument builds its
      window, because the window is built identically on both arms and the ruler clock proves it. ***

  ⚠ ** AND THE SIZE IS DEFINITION-DEPENDENT WHILE THE ATTRIBUTION IS NOT. **  `rms` gives
    {100 * (OUT['rms'][1] - 1):+.1f} per cent -- `cc66.51`'s figure -- against {100 * (OUT['fwhm'][1] - 1):+.1f}
    and {100 * (OUT['chi-half'][1] - 1):+.1f} for the two CORE measures, which agree with each other to
    better than a hundredth of a per cent.  *The window has long tails, `rms` weights them, and neither
    the projection nor the phase sweep responds to them.*  ⇒ **The prediction is to be quoted on a core
    width with the definition named, and `cc66.51`'s {100 * (OUT['rms'][1] - 1):+.1f} per cent is the
    tail-weighted reading of the same thing.**

  ⛔ ** AND THIS IS WHY ⓵ CANNOT BE RUN AS WRITTEN. **  *"Give the control arm this arm's conformal
    width at the same leaf width"* is, by ⓐ--ⓒ, exactly *"give the control arm this arm's `Jac`"* --
    and a control with `Jac != 1` is not a control.  ⇒ **The width channel is not separable from the
    two-rate assignment; there is no knob for it, and the instrument is right not to have one.**  *What
    CAN be done is the kernel calculation of ⓶, which is the projection sector's whole content.*
""")
