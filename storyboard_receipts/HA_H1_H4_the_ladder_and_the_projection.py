#!/usr/bin/env python3
"""RECEIPT — harmonic-analysis bake `H1`–`H4`: ** THE LADDER MEASURE IS THE SAME EXPRESSION BY TWO
INDEPENDENT DERIVATIONS; THE PROJECTION CONSERVES POWER; AND THE LOW-ELL DEFICIT IS TWO EFFECTS OF
OPPOSITE SIGN, OF WHICH P15 REPORTS ONE — WHILE QUOTING THE OTHER'S NUMBER. **

LEVEL: NO RATE — Sturm-Liouville on S^3 and the flat spherical-Bessel projection.

WHY THIS RECEIPT EXISTS.  The r3166 harmonic bake carries a real computation -- the split of the
  low-multipole deficit into a FLOOR and a DISCRETENESS part, the recovery multipole, and a measured
  bound on a gate P15 waives in its own voice -- and receipts none of it.

H1 — THE MEASURE, TWO WAYS.  w_L = (L+1)/(L(L+2)) is derived as degeneracy over per-mode power,
  (L+1)^2 / [(L+1)((L+1)^2-1)], and independently as d ln k_L / dL with k_L r_0 = sqrt(L(L+2)).
  ** Not merely equal at sampled L: sympy returns the SAME EXPRESSION from both routes. **

H2 — THE PROJECTION CONSERVES POWER.  sum_l (2l+1) j_l(x)^2 = 1 to ten figures at x = 1, 5, 20.  So
  nothing in the deficit is projection loss.

H3 — AND THE QUADRATURE IS NOT THE FINDING.  A fixed logarithmic grid reproduces the exact plateau
  int j_l^2 dln x = 1/(2 l (l+1)) to better than a part in 10^3 at l = 2, 5, 10.  ** This control
  matters: the ledger records that the FIRST form of its aliasing test, run with adaptive quadrature,
  reported an imprint that never died within l <= 40, and that redone on a checked fixed grid it dies
  at l = 32.  The direction survived and the number did not. **

H4 — THE BITE.  In the pure Sachs-Wolfe limit the suppression splits exactly into the FLOOR (the
  integral truncated below k_2) and the DISCRETENESS (ladder sum minus that truncated integral).  They
  have OPPOSITE SIGNS at some multipoles -- at l=4 the discreteness is negative while the floor is
  positive -- and near l=5-6 the discreteness contributes as much as the floor.  ** The ladder
  recovers to 99% at l=8; the floor alone does not recover until l=11.  P15 quotes "recovery by
  l ~ 8", which is the LADDER's number and not the floor's -- so the paper's quoted figure is the
  right one, and the mechanism behind it is not the one the text names. **

  NOTE ON THE PARAMETER: D_C/r_0 = 3.0 is chosen here, not taken from the corpus; the floor's exact
  recovery multipole moves with it (the r3166 ledger records 10).  The SPLIT and the ordering --
  ladder recovers before floor -- are what this receipt asserts, and they are robust.

VERDICTS ARE ASSERTS.
"""
import numpy as np
import sympy as sp
from scipy.special import spherical_jn

print("=" * 78)
print("  H1 / H2 / H3 / H4 — the S^3 ladder and the flat projection")
print("=" * 78)

# ---------------------------------------------------------------- H1
L = sp.symbols('L', positive=True)
w_power = sp.simplify((L + 1)**2 / ((L + 1) * ((L + 1)**2 - 1)))
w_dlnk = sp.simplify(sp.diff(sp.log(sp.sqrt(L * (L + 2))), L))
print(f"\n  H1  degeneracy / per-mode power = {w_power}")
print(f"      d ln k_L / dL               = {w_dlnk}")
assert sp.simplify(w_power - w_dlnk) == 0, "the two derivations must give one expression"
assert sp.simplify(w_power - (L + 1) / (L * (L + 2))) == 0
print("  ** VERDICT H1: sympy returns the SAME EXPRESSION from both routes, not merely equal")
print("     values at sampled L. **")

# ---------------------------------------------------------------- H2
print("\n  H2  spherical-Bessel completeness, sum_l (2l+1) j_l(x)^2 = 1:")
for x in (1.0, 5.0, 20.0):
    tot = sum((2 * l + 1) * spherical_jn(l, x)**2 for l in range(400))
    print(f"      x = {x:5.1f}   sum = {tot:.10f}")
    assert abs(tot - 1) < 1e-9, "the projection must conserve power"
print("  ** VERDICT H2: to ten figures.  Nothing in the deficit is projection loss. **")

# ---------------------------------------------------------------- H3
print("\n  H3  the fixed grid against the exact plateau int j_l^2 dln x = 1/(2 l (l+1)):")
xs = np.exp(np.linspace(np.log(1e-3), np.log(400), 200000))
for l in (2, 5, 10):
    val = np.trapezoid(spherical_jn(l, xs)**2, np.log(xs))
    exact = 1 / (2 * l * (l + 1))
    print(f"      l = {l:2d}   numeric {val:.8f}   exact {exact:.8f}   ratio {val/exact:.6f}")
    assert abs(val / exact - 1) < 1e-3, "the quadrature must not be the finding"
print("  ** VERDICT H3: better than a part in 10^3.  The ledger's own record of an adaptive-")
print("     quadrature artefact -- an imprint that 'never died within l <= 40' and dies at")
print("     l = 32 on a checked grid -- is why this control is run first. **")

# ---------------------------------------------------------------- H4
print("\n  H4  the deficit splits into FLOOR and DISCRETENESS  (D_C/r_0 = 3.0, chosen here)")
r0, DC = 1.0, 3.0
kL = lambda n: np.sqrt(n * (n + 2)) / r0
w = lambda n: (n + 1) / (n * (n + 2))
Ls = np.arange(2, 4000)
xg = np.exp(np.linspace(np.log(1e-4), np.log(4000), 120000))
cont = lambda l: np.trapezoid(spherical_jn(l, xg)**2, np.log(xg))
ladder = lambda l: sum(w(n) * spherical_jn(l, kL(n) * DC)**2 for n in Ls)
def trunc(l):
    m = xg >= kL(2) * DC
    return np.trapezoid(spherical_jn(l, xg[m])**2, np.log(xg[m]))

print(f"      {'l':>3} {'full':>8} {'floor':>8} {'discreteness':>13}")
rec_full = rec_floor = None
opposite = False
for l in range(2, 13):
    c = cont(l); f = ladder(l) / c; fl = trunc(l) / c
    if rec_full is None and f >= 0.99: rec_full = l
    if rec_floor is None and fl >= 0.99: rec_floor = l
    if (f - fl) < -0.01: opposite = True
    print(f"      {l:3d} {f:8.3f} {fl:8.3f} {f-fl:13.3f}")

assert opposite, "the two parts must take opposite signs somewhere"
assert rec_full is not None and rec_floor is not None
assert rec_full < rec_floor, "the ladder must recover BEFORE the floor alone"
print(f"\n      recovery to 99%:  ladder {rec_full}   floor alone {rec_floor}")
print("  ** VERDICT H4: the two parts take OPPOSITE signs at some multipoles, and the ladder")
print(f"     recovers at l={rec_full} where the floor alone does not until l={rec_floor}.  P15 quotes")
print("     'recovery by l ~ 8' -- the LADDER's number.  The paper's figure is right and the")
print("     mechanism behind it is not the one its text names. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
