#!/usr/bin/env python3
"""
RECEIPT -- P15: ** BEFORE BUILDING EITHER OF THE TWO THINGS FRONT #2 NAMED NEXT, BOTH ARE MEASURED --
AND ONE OF THEM IS WORTH EXACTLY NOTHING.  REIONISATION IS ALGEBRAICALLY DEGENERATE WITH THE FITTED
AMPLITUDE ON THIS STATISTIC; LENSING IS WORTH ABOUT 400 OF THE REMAINING 1320, AND THE ell-DEPENDENCE
OF THE SMOOTHING IT WANTS IS LENSING'S OWN. **

Built r2376+c54.181, front #2.

===================================================================================================
** WHY THIS EXISTS: I NAMED TWO NEXT STEPS AND ONE OF THEM CANNOT PAY. **
===================================================================================================

c54.178 closed with "what remains is accuracy: reionisation, neutrino mass, a lensed spectrum, and
the wavenumber range".  ** Two of those are now measured rather than assumed, and the measurement
cost minutes against builds that would have cost revisions. **  *This is the c54.176 discipline
applied before the work instead of after it: establish what the statistic can resolve, then spend.*

  PART 1  ** REIONISATION IS EXACTLY DEGENERATE WITH THE AMPLITUDE, AND THE PROOF IS ALGEBRA RATHER
          THAN A SCAN. **  Above ell ~ 40 reionisation's whole effect on TT is the constant screening
          exp(-2 tau) -- the second visibility bump contributes only below ell ~ 30, outside this
          instrument's range entirely.  ** And the amplitude here is fitted in CLOSED FORM,
          A = (m F d)/(m F m), which is homogeneous of degree -1 in m: under m -> s m it returns
          A/s, and the residual d - A m is IDENTICAL. **  So d(chi^2) = 0 exactly, for any s.
          *Demonstrated at tau = 0.054, 0.10 and 0.30: zero to machine precision at all three,
          including a tau five times the measured one.*
  PART 2  ** LENSING IS WORTH ABOUT 400 OF THE 1320, WHICH IS REAL AND IS NOT THE BULK. **  A
          Gaussian smoothing in ell, scanned in width, minimises at chi^2 = 921 against 1320.
  PART 3  ** AND THE SHAPE IT WANTS IS LENSING'S, NOT A GENERIC BLUR. **  A smoothing whose width
          GROWS with ell beats a constant-width one by a factor of two in d(chi^2), each compared at
          its OWN optimum so that the comparison is of shape and not of size.  ** Lensing smooths
          more at high ell -- the deflection subtends a larger fraction of an acoustic wavelength --
          and that is the signature the data select. **
  PART 4  ** WHAT THIS IS NOT: A RESULT ABOUT THE SKY. **  The width is FITTED, so the 400 is an
          estimate of what a DERIVED lensing calculation has to play for, not a measurement of the
          lensing amplitude and not a claim that the control improves.  *A derived calculation has
          no free width and could return more or less.*  ** The number that matters is the one it
          leaves: even at its own optimum, ~900 of the 1320 is still unaccounted for, so lensing is
          the next build and is NOT the last one. **

** WHAT THIS DOES TO THE FRONT'S LIST. **  Reionisation is struck from it -- not deferred, struck,
because on this statistic it cannot pay at any tau.  *It would return the moment the comparison
gained ell < 30, or a second spectrum, or a fixed amplitude -- and that condition is written here so
the strike can be undone by a change of statistic rather than by a change of mind.*

rc=0 on success.  Run: python3 P15_what_is_left_is_lensing_and_not_reionisation.py  (numpy scipy)
"""
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

_z = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra', 'c54.178_lcdm.npz'))
LS, DL = np.asarray(_z['ls'], float), np.asarray(_z['Dl'], float)
LF = np.arange(LS[0], LS[-1] + 1)
DF = np.interp(LF, LS, DL)
BASE, NB = CS.chi2_of(LS, DL)[:2]

# =====================================================================
print("=" * 78)
print("PART 1 — REIONISATION IS EXACTLY DEGENERATE, AND IT IS ALGEBRA AND NOT A SCAN")
print("=" * 78)
print(f"  {'tau':>8} {'exp(-2 tau)':>13} {'chi^2':>10} {'fitted A':>12} {'d(chi^2)':>12}")
print(f"  {'—':>8} {1.0:>13.4f} {BASE:>10.1f} {CS.chi2_of(LS, DL)[2]:>12.4e} {0.0:>12.2e}")
_worst = 0.0
for tau in (0.054, 0.10, 0.30):
    s = float(np.exp(-2 * tau))
    c, n, A, lo, hi = CS.chi2_of(LS, DL * s)
    _worst = max(_worst, abs(c - BASE))
    print(f"  {tau:>8.3f} {s:>13.4f} {c:>10.1f} {A:>12.4e} {c-BASE:>12.2e}")
print(f"\n  ** ZERO TO MACHINE PRECISION AT EVERY tau, INCLUDING ONE FIVE TIMES THE MEASURED VALUE. **")
print("     *A = (m F d)/(m F m) is homogeneous of degree -1 in m, so m -> s m gives A -> A/s and")
print("     the residual d - A m does not move.  ** The degeneracy is exact, not approximate, and it")
print("     is a property of the STATISTIC rather than of the size of tau. **")
if _worst > 1e-6 * BASE:
    fail.append(f"the reionisation screening moved chi^2 by {_worst:.2e} -- it is not exact")


def smooth(a, p):
    """a Gaussian smoothing in ell with width sigma(ell) = a (ell/1000)^p; p = 0 is constant width"""
    out = np.empty_like(DF)
    for i, l in enumerate(LF):
        s = a * (l / 1000.0) ** p
        if s < 0.5:
            out[i] = DF[i]
            continue
        n = int(np.ceil(4 * s))
        x = np.arange(-n, n + 1)
        k = np.exp(-0.5 * (x / s) ** 2)
        k /= k.sum()
        seg = np.take(DF, np.clip(np.arange(i - n, i + n + 1), 0, len(DF) - 1))
        out[i] = float(np.dot(seg, k))
    return out


# =====================================================================
print()
print("=" * 78)
print("PART 2/3 — LENSING IS WORTH ~400, AND THE SHAPE IT WANTS GROWS WITH ell")
print("=" * 78)
print(f"  {'sigma(ell)':>22} {'best a':>7} {'chi^2':>9} {'chi^2/dof':>10} {'d(chi^2)':>9}")
BEST = {}
for p, nm in ((0.0, 'a (constant width)'), (1.0, 'a (ell/1000)'), (2.0, 'a (ell/1000)^2')):
    cands = [(CS.chi2_of(LF, smooth(a, p))[0], a) for a in np.arange(4.0, 70.0, 2.0)]
    c, a = min(cands)
    BEST[p] = (c, a)
    print(f"  {nm:>22} {a:>7.1f} {c:>9.1f} {c/NB:>10.2f} {c-BASE:>+9.1f}")
d0 = BASE - BEST[0.0][0]
d1 = BASE - BEST[1.0][0]
print(f"\n  ** A GROWING WIDTH BEATS A CONSTANT ONE BY {d1/d0:.1f}x IN d(chi^2) — {d1:.0f} against "
      f"{d0:.0f} — **")
print("  ** and each is compared at its OWN optimum, so this is a statement about SHAPE. **")
print("     *Lensing smooths more at high ell because a deflection of fixed angle subtends a larger")
print("     fraction of an acoustic wavelength there.  That is the signature the data select, and a")
print("     generic blur is not it.*")
if d1 <= d0:
    fail.append("a growing width does not beat a constant one -- PART 3's claim is the reverse")
if not (250 < d1 < 600):
    fail.append(f"the growing-width optimum buys {d1:.0f} -- outside the range PART 2 reports")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND THE NUMBER THAT MATTERS IS THE ONE IT LEAVES")
print("=" * 78)
left = BEST[1.0][0]
print(f"  the control is at chi^2 = {BASE:.0f} ({BASE/NB:.2f} per degree of freedom)")
print(f"  the best fitted lensing-shaped smoothing leaves {left:.0f} ({left/NB:.2f})")
print(f"\n  ** SO EVEN AT ITS OWN OPTIMUM, WITH A FREE WIDTH, ~{left:.0f} OF THE {BASE:.0f} SURVIVES. **")
print("     ⇒ ***Lensing is the next build and it is NOT the last one. The width here is FITTED, so")
print("     the 400 bounds what a DERIVED calculation has to play for rather than measuring the")
print("     lensing amplitude — a derivation has no free width and may return more or less.***")
if left < 0.5 * BASE:
    fail.append("the smoothing accounts for more than half -- PART 4 understates it and should be "
                "rewritten rather than patched")
if left / NB < 2.0:
    fail.append(f"a fitted smoothing alone takes the control to chi^2/dof = {left/NB:.1f} -- at that "
                "level L-147 must be revisited, not this line printed")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — reionisation cannot pay on this statistic at any tau, lensing is worth about")
print("400 of the 1320 and the smoothing it wants grows with multipole, and about 900 survives it.")
print("=" * 78)

# ============================================================================================
# GATE — r2376+c54.181.  Front #2's list is edited on the strength of these three numbers, so
# each is pinned.
#   (1) the reionisation degeneracy is EXACT -- if it ever moves chi^2, the amplitude is no longer
#       being fitted in closed form and PART 1's algebra no longer describes the pipeline;
#   (2) the growing-width optimum, and that it BEATS the constant-width one at its own optimum --
#       which is the shape claim and the reason "lensing" rather than "some smoothing";
#   (3) what survives it, since PART 4's whole point is that lensing is not the last build.
# ============================================================================================
assert _worst < 1e-6 * BASE, f"the reionisation screening moved chi^2 by {_worst:.3e}"
assert abs(BEST[1.0][0] - 920.6) < 15.0, f"the growing-width optimum is {BEST[1.0][0]:.1f}, expected 921"
assert abs(BEST[0.0][0] - 1095.8) < 15.0, f"the constant-width optimum is {BEST[0.0][0]:.1f}"
assert d1 > 1.5 * d0, f"the growing width beats the constant one by only {d1/d0:.2f}x"
assert left > 0.6 * BASE, f"only {left:.0f} of {BASE:.0f} survives -- PART 4 needs rewriting"
print(f"GATE c54.181 (r2376): reionisation exact to {_worst:.1e} in chi^2 at tau up to 0.30; the "
      f"lensing-shaped smoothing optimum is {BEST[1.0][0]:.0f} against a constant width's "
      f"{BEST[0.0][0]:.0f} and a baseline {BASE:.0f}; {left/BASE:.0%} survives -- pinned against "
      f"THE_WORK front #2.")
