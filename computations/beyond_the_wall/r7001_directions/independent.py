"""⓷ IS THE WIDTH PREDICTION OBSERVABLE IN ITS OWN RIGHT? -- r7001+cc66.53.

⛔ *The order's ⓷: "You established a ratio that the two-rate assignment forces and one-rate cosmology
cannot produce.  That belongs in the paper as a prediction whatever it does to the contrast, and it is
currently landed inside a passage about a channel that failed.  So: is it observable in its own right?
...  If yes, that is a new observational handle for this construction and it outranks the row it was
found in.  If no, say so and I will keep it where it is."*

** THE QUESTION SPLITS IN TWO AND THEY HAVE DIFFERENT ANSWERS, WHICH IS THE POINT. **
  ⓐ *Is its CONTENT independent of what the corpus already reads off `Jac`?*  -- the comb.
  ⓑ *Is there a MEASUREMENT that reaches it?*
"""
import os

import numpy as np

SP = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'spectra')
A = {t: np.load(os.path.join(SP, f'r6959_eta_{t}.npz')) for t in ('lcdm', 'cr')}


def chi_half(e, w, x):
    from scipy.optimize import brentq

    def f(k):
        return np.hypot(np.trapezoid(w * np.cos(k * x), e), np.trapezoid(w * np.sin(k * x), e)) - 0.5
    hi = 1e-3
    while f(hi) > 0:
        hi *= 2
    return 1.0 / brentq(f, 1e-9, hi)


def mk(t):
    d = A[t]
    e = np.asarray(d['eta'], float)
    w = np.asarray(d['vis'], float)
    return e, w / np.trapezoid(w, e), np.asarray(d['rs_leaf'], float), \
        np.asarray(d['rs_stack'], float), np.asarray(d['jac'], float)


print(__doc__)
print('=' * 100)

e, w, rl, rs, J = mk('cr')
d = A['cr']
ils = int(np.argmax(np.asarray(d['vis'], float)))
CUM = float(rl[ils] / rs[ils])
WIN = float(np.trapezoid(w * J, e))

print('\n  ⓐ ** TWO DIFFERENT FUNCTIONALS OF THE SAME `Jac`, AND THE CORPUS ONLY READS ONE. **')
print(f"     the COMB reads the CUMULATIVE ratio, rs_leaf/rs_stack at last scattering : {CUM:.5f}")
print(f"       -- pi D_M / rs_leaf  = {np.pi * float(d['D_M']) / rl[ils]:8.3f}   against the banked "
      f"l_A = {float(d['l_A']):.3f}")
print(f"       -- pi D_M / rs_stack = {np.pi * float(d['D_M']) / rs[ils]:8.3f}   which is not close, "
      f"and that is why the comb is said to ride the leaf accumulation")
print(f"     the WIDTHS read the WINDOW-LOCAL average,  <Jac> over the visibility      : {WIN:.5f}")
print(f"       -- and Jac at the visibility peak itself is {float(J[ils]):.5f}")
print(f"\n     ⇒ ** THEY DIFFER BY {100 * (CUM / WIN - 1):+.0f} PER CENT. **  *An integral of `Jac` from "
      f"the start of the leg is not an average of `Jac` across last scattering, and nothing in the comb "
      f"constrains the second.*  ⌗ Both are 1 on one rate, and neither carries a free coefficient.")
print('     ⇒ *** SO THE WIDTH RATIO IS AN INDEPENDENT READING OF THE TWO-RATE ASSIGNMENT AND NOT A '
      'RESTATEMENT OF THE COMB.  A construction tuned to match the comb still has to produce the '
      'right LOCAL Jacobian to match the widths. ***')

print('\n  ⓑ ** BUT NO MEASUREMENT REACHES IT, AND THE TWO READERS ARE WHY. **')
WL = {t: chi_half(*mk(t)[:2], mk(t)[2]) for t in ('lcdm', 'cr')}
WE = {t: chi_half(*mk(t)[:2], mk(t)[0]) for t in ('lcdm', 'cr')}
print(f"     the PHASE width -- what the window's Landau damping of the acoustic oscillation reads --")
print(f"       control {WL['lcdm']:.5f}   arm {WL['cr']:.5f}   -> "
      f"{100 * (WL['cr'] / WL['lcdm'] - 1):+.2f} per cent.  ** That reader is effectively blind. **")
print(f"     the CONFORMAL width -- what the projection reads --")
print(f"       control {WE['lcdm']:.5f}   arm {WE['cr']:.5f}   -> "
      f"{100 * (WE['cr'] / WE['lcdm'] - 1):+.2f} per cent, and `cc66.52` bounded what that does to the "
      f"contrast at 2 per cent with its sign undetermined.")
print('\n     ⇒ *** THE PREDICTION IS A RATIO OF TWO WIDTHS, AND EVERY OBSERVABLE IDENTIFIED READS ONE '
      'OF THEM AND NOT THE RATIO.  The one that sees a difference sees 13 per cent of a quantity whose '
      'effect is bounded at 2; the one whose effect is large sees a difference of under 1 per cent. ***')

print('\n' + '=' * 100)
print("""
  ⛔ THE ANSWER, IN THE ORDER'S OWN TERMS: ** NO, IT IS NOT OBSERVABLE IN ITS OWN RIGHT -- AND THE
    REASON IT SHOULD STILL MOVE IS ⓐ AND NOT ⓑ. **

    *The order says "if no, say so and I will keep it where it is."  The answer to the observational
    question is no, and it is said plainly.*  ⌗ **But ⓐ is a separate finding and it was not in hand
    when that passage was written**: the width ratio and the comb are different functionals of `Jac`,
    differing by a third, so the prediction's CONTENT does not belong to the channel it was found
    while chasing.  ⇒ *That is a reason to move it that does not depend on it being measurable, and
    the choice is the chat seat's.*

  ⚠ AND WHAT WOULD MAKE IT OBSERVABLE, STATED SO IT IS NOT MISTAKEN FOR A CHANNEL.  *An observable
    that reads the visibility's width in CONFORMAL TIME while being insensitive to its width in
    acoustic phase would separate them.  The polarisation source is the natural candidate -- the
    quadrupole is generated across a scattering time rather than across an acoustic phase -- but this
    instrument banks polarisation only as its contribution to the TEMPERATURE decomposition
    (`w2pol`, the `sw*pol` and `dp*pol` cross terms), not as an E-mode spectrum, so the question
    cannot be asked of it as it stands.*  ⛔ **Not proposed as a channel: the order's ⓸ closes the
    list, and this is a note about what the instrument does not carry.**
""")
