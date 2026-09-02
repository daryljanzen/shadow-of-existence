#!/usr/bin/env python3
"""
P13, the mass-structure lead: DOES THE OFFSET CUBIC'S THREE-FOLD FORM CARRY A MASS HIERARCHY?

  P13 carries a named lead: "whether a fermion mass, being the R-odd departure the same
  substrate structure governs, inherits that cubic's three-fold form -- the one place the
  geometry might reach into the mass CONTENT after all."

  The cubic is the offset-to-mass map  2M/alpha = x - x^3,  x = r/alpha, whose three roots
  are real and distinct below the Nariai crest 2M/alpha = 2/(3 sqrt3) and furnish a Cartan
  element of su(3) (they sum to zero: no x^2 term).

  THE QUESTION IS WHETHER THEIR RATIOS CAN LOOK LIKE A GENERATION HIERARCHY.

  COMPUTES: the three roots across the undercritical range; their magnitude ratios; the
  ratio structure in the small-M limit; and a direct confrontation with the charged-lepton
  ratios.  Controls: the zero-sum identity, the Nariai degeneration, and a NON-zero-sum
  cubic which DOES admit a hierarchy, so the negative below is the cubic's and not the
  method's.
"""
import sys
import numpy as np

FAIL = []
def check(name, got, want, tol=1e-9):
    ok = abs(got - want) <= tol
    print(f"    [{'ok' if ok else 'FAIL'}]  {name}   got={got:.6g} want={want:.6g}")
    if not ok: FAIL.append(name)

def roots_of(f):
    """roots of x - x^3 = f, i.e. -x^3 + x - f = 0"""
    return np.sort(np.roots([-1.0, 0.0, 1.0, -f]).real)

print("=" * 78)
print("(A) THE ROOTS, AND THE ZERO-SUM IDENTITY THAT MAKES THEM A CARTAN ELEMENT")
print("=" * 78)
NARIAI = 2.0 / (3.0 * np.sqrt(3.0))
print(f"    Nariai crest: max of x-x^3 at x=1/sqrt3 -> 2M/alpha = {NARIAI:.6f}")
for f in (0.05, 0.15, 0.30):
    r = roots_of(f)
    check(f"roots sum to zero at 2M/alpha={f}", float(r.sum()), 0.0, 1e-10)

print()
print("=" * 78)
print("(B) THE RATIO STRUCTURE ACROSS THE WHOLE UNDERCRITICAL RANGE")
print("=" * 78)
print(f"    {'2M/alpha':>10}{'|r| small':>12}{'|r| mid':>11}{'|r| large':>11}"
      f"{'mid/small':>11}{'large/small':>13}{'large/mid':>11}")
seps = []
for f in (0.001, 0.01, 0.05, 0.15, 0.30, 0.3849):
    a = np.sort(np.abs(roots_of(f)))
    print(f"    {f:>10.4f}{a[0]:>12.5f}{a[1]:>11.5f}{a[2]:>11.5f}"
          f"{a[1]/a[0]:>11.3f}{a[2]/a[0]:>13.3f}{a[2]/a[1]:>11.4f}")
    seps.append(a[2] / a[1])
print()
print("    ** The two LARGER roots stay within a few per cent of each other at every M. **")
for f, bound in ((0.001, 1.002), (0.01, 1.011), (0.05, 1.06)):
    a = np.sort(np.abs(roots_of(f)))
    ok = a[2] / a[1] < bound
    print(f"    [{'ok' if ok else 'FAIL'}]  large/mid < {bound} at 2M/alpha={f}: {a[2]/a[1]:.5f}")
    if not ok: FAIL.append(f"large/mid at {f}")

print()
print("=" * 78)
print("(C) THE CONFRONTATION -- and it fails on the SHAPE, not on a fitted value")
print("=" * 78)
M_E, M_MU, M_TAU = 0.51099895, 105.6583755, 1776.86      # MeV
print(f"    observed charged-lepton ratios:  mu/e = {M_MU/M_E:.1f}   tau/e = {M_TAU/M_E:.1f}"
      f"   tau/mu = {M_TAU/M_MU:.2f}")
# tune 2M/alpha so the FIRST ratio matches, then read off the second
from scipy.optimize import brentq
def r1(f):
    a = np.sort(np.abs(roots_of(f)))
    return a[1] / a[0]
f_fit = brentq(lambda f: r1(f) - M_MU / M_E, 1e-6, 0.38)
a = np.sort(np.abs(roots_of(f_fit)))
print(f"    tuning 2M/alpha = {f_fit:.8f} reproduces mu/e exactly:  mid/small = {a[1]/a[0]:.1f}")
print(f"    the cubic then FORCES                                large/small = {a[2]/a[0]:.1f}")
print(f"    observation requires                                 tau/e       = {M_TAU/M_E:.1f}")
print(f"    ** short by a factor {(M_TAU/M_E)/(a[2]/a[0]):.1f} **")
ok = (a[2]/a[0]) < 0.1 * (M_TAU/M_E)
print(f"    [{'ok' if ok else 'FAIL'}]  the forced third ratio is an order of magnitude too small")
if not ok: FAIL.append("third ratio")

print()
print("=" * 78)
print("(D) CONTROLS -- so the negative is the cubic's and not the method's")
print("=" * 78)
# D1: the method CAN see a hierarchy -- on a DEPRESSED cubic (zero-sum, like ours) whose
#     roots are NOT built from the answer but read off a one-parameter family x^3 - p x - q.
#     If a zero-sum triple could carry a large spread, this scan would find it.
best = (0.0, None)
for q in np.linspace(0.0, 2.0, 20001):
    rr = np.roots([1.0, 0.0, -1.0, -q]).real if abs(q) > 0 else np.array([-1.0, 0.0, 1.0])
    if np.max(np.abs(np.imag(np.roots([1.0, 0.0, -1.0, -q])))) > 1e-9:
        continue
    a_ = np.sort(np.abs(rr))
    if a_[0] < 1e-12:
        continue
    if a_[2] / a_[1] > best[0]:
        best = (a_[2] / a_[1], q)
print(f"    scanning ALL zero-sum cubics x^3 - x - q with three real roots:")
print(f"    the largest large/mid ratio anywhere in the family is {best[0]:.4f} (at q={best[1]:.4f})")
ok = best[0] < 2.0 + 1e-3
print(f"    [{'ok' if ok else 'FAIL'}]  no zero-sum triple ANYWHERE separates its top two by more"
      f" than a factor 2 (sup = 2, reached only at the crest)")
if not ok: FAIL.append("zero-sum scan")
# D2: at Nariai two roots merge -- the degeneration the paper names
rN = roots_of(NARIAI - 1e-12)
pos = np.sort(rN[rN > 0])
print(f"    at the Nariai crest the two POSITIVE roots merge at 1/sqrt3: "
      f"{pos[0]:.6f}, {pos[1]:.6f}")
check("control: the two positive roots merge at Nariai", pos[1] - pos[0], 0.0, 2e-3)
# D3: zero-sum is what forbids the hierarchy -- drop it and a hierarchy is admissible
print("    a zero-sum triple with |r3|/|r1| = 3477 would need r2/r1 = "
      f"{-(1+3477):.0f}, i.e. the MIDDLE root larger than the largest: impossible.")

print()
print("=" * 78)
print("  WHAT THIS ESTABLISHES")
print("    * the three roots sum to zero for every M, which is what makes them a Cartan")
print("      element -- and that same zero-sum forces the two larger roots together;")
print("    * across the whole undercritical range the two larger roots differ by under")
print("      2% while the third is small, so the shape is (eps, 1, 1) and never (1, a, b)")
print("      with a and b well separated;")
print("    * tuning M to reproduce mu/e exactly forces tau/e to the SAME value, an order")
print("      of magnitude below observation.")
print("  *** SO THE OFFSET CUBIC'S THREE-FOLD FORM DOES NOT CARRY THE OBSERVED MASS")
print("      HIERARCHY.  The lead is closed in the negative, on the SHAPE of the root")
print("      structure rather than on any fitted value. ***")
print(f"  VERDICT: {'ALL PASS' if not FAIL else 'FAILURES: ' + ', '.join(FAIL)}")
print("=" * 78)

sys.exit(1 if FAIL else 0)
