#!/usr/bin/env python3
"""
THE P14 CHECK — does "three generations fix the cut's dimension at four" survive
contact with P3's ACTUAL derivation of the three-ness?

c54.7 asserted the chain

    horizon polynomial degree = D-1  =>  three roots <=> D = 4
    P3/P14 tie hinge <-> root, P14 ties wall <-> generation
    => three generations fix D = 4.

The middle link had not been checked at source.  It has now, and P3 does NOT get
its three-ness from the bare degree of the polynomial.  P3 sec:family, in its own
words:

    "the cubic r0 - r0^3 is the cubic in sin w that the TRIPLE-ANGLE IDENTITY
     collapses to sin 3w, and the slicing scale 2/sqrt3 is THE ONE SCALE REMOVING
     THE RESIDUAL HARMONIC ... three sky angles 120 degrees apart carry the same
     mass while cycling which root is the designated offset through all three ...
     Read on a fermion sector this three-fold is the generation multiplicity --
     FORCED TO THREE BY THE SINGLE TRIPLE-ANGLE AT THE GNOMONIC-FIXED SCALE."

So the load-bearing step is not "degree D-1" but "the mass relation collapses to a
SINGLE harmonic under one scale choice".  That is a far stronger condition, and it
is what this script tests in D dimensions.

SETUP.  D-dimensional Schwarzschild-de Sitter with alpha = 1:

    f(r) = 1 - 2M/r^{D-3} - r^2        =>        2M = r^{D-3} - r^{D-1}

Substitute the slicing offset r = c*sin(w) and expand in the multiple-angle basis.
The top harmonic is k = D-1.  ASK: is there a scale c > 0 killing every harmonic
below it?  (An additive constant is allowed: it shifts 2M without changing the
fold of the level sets, which is what counts the hinges.)

CALIBRATION.  At D=4 this must return the corpus's own answer -- c = 2/sqrt(3) and
2M = (2/(3 sqrt3)) sin 3w -- or the test is not measuring P3's step.

Run: python3 p14_generations_fix_dimension.py     (sympy)
"""

import sympy as sp

w, c = sp.symbols('w c', positive=True)
I = sp.I


def harmonics(n_lo, n_hi, scale):
    """
    Expand  scale**n_lo * sin(w)**n_lo - scale**n_hi * sin(w)**n_hi
    in the basis exp(i k w), returning {k: coeff} for k >= 0.
    """
    z = sp.exp(I * w)
    s = (z - 1 / z) / (2 * I)
    e = sp.expand(scale**n_lo * s**n_lo - scale**n_hi * s**n_hi)
    e = sp.expand(sp.powsimp(e, force=True))
    out = {}
    for k in range(0, n_hi + 1):
        co = e.coeff(z, k)
        if k == 0:
            co = e.subs(z, 1) - sum(e.coeff(z, j) for j in range(1, n_hi + 1)) \
                - sum(e.coeff(z, -j) for j in range(1, n_hi + 1))
        if sp.simplify(co) != 0:
            out[k] = sp.simplify(co)
    return out


print(__doc__.split("Run:")[0])
print("=" * 78)
print("THE COLLAPSE TEST — for which D does ONE scale remove every residual harmonic?")
print("=" * 78)
print(f"{'D':>3} {'top k':>6} {'lower harmonics to kill':>26} {'#eqns':>6} "
      f"{'collapses?':>11} {'scale c':>12}")

results = {}
for D in range(4, 11):
    n_lo, n_hi = D - 3, D - 1
    h = harmonics(n_lo, n_hi, c)
    lower = sorted(k for k in h if 0 < k < n_hi)
    eqs = [sp.Eq(sp.simplify(h[k]), 0) for k in lower]
    sols = []
    if eqs:
        raw = sp.solve(eqs, c, dict=True)
        for s in raw:
            v = s.get(c)
            if v is None:
                continue
            v = sp.nsimplify(sp.simplify(v))
            if v.is_real and v.is_positive:
                sols.append(v)
    else:
        sols = ['(unconstrained)']
    ok = bool(sols)
    scale = sols[0] if ok else None
    results[D] = (ok, scale, lower)
    print(f"{D:>3} {n_hi:>6} {str(lower):>26} {len(eqs):>6} "
          f"{('YES' if ok else 'no'):>11} {str(sp.radsimp(scale) if ok else '-'):>12}")

print()
print("  The structural reason is a COUNT, not luck: the two powers are D-3 and")
print("  D-1, so the harmonics present run k = D-1, D-3, ..., and the number of")
print("  them BELOW the top is exactly one when D = 4 or D = 5 and two or more")
print("  from D = 6 on.  The construction has exactly ONE scale to spend.")

# ------------------------------------------------------------------
# calibration against the corpus at D=4, and the explicit D=5 form
# ------------------------------------------------------------------
print()
print("=" * 78)
print("CALIBRATION AT D=4 — must reproduce P3 exactly")
print("=" * 78)
c4 = results[4][1]
expr4 = sp.simplify((c4**1 * sp.sin(w)**1 - c4**3 * sp.sin(w)**3))
print(f"  scale found          : c = {sp.radsimp(c4)}   (P3: 2/sqrt(3))")
print(f"  2M(w)                : {sp.simplify(sp.trigsimp(expr4))}")
target = sp.Rational(2, 3) / sp.sqrt(3) * sp.sin(3 * w)
print(f"  P3's eq:tripleangle  : {target}")
print(f"  identical            : "
      f"{sp.simplify(sp.trigsimp(expr4 - target)) == 0}")

print()
print("=" * 78)
print("THE ONLY OTHER SURVIVOR — D=5")
print("=" * 78)
c5 = results[5][1]
expr5 = sp.simplify(sp.trigsimp(c5**2 * sp.sin(w)**2 - c5**4 * sp.sin(w)**4))
print(f"  scale found          : c = {sp.radsimp(c5)}")
print(f"  2M(w)                : {expr5}")
print(f"  rewritten            : {sp.simplify(sp.trigsimp(sp.expand_trig(expr5)))}")
print("  -> a pure 4-fold: the level sets are invariant under w -> w + 2pi/4,")
print("     so a five-dimensional cut would carry FOUR hinges and FOUR generations.")

print()
print("=" * 78)
print("VERDICT ON THE c54.7 CLAIM")
print("=" * 78)
print("  UPHELD, and by a stronger route than the one asserted.")
print()
print("  The claim was argued from the DEGREE of the horizon polynomial.  The")
print("  degree is necessary but is not what P3 leans on; P3 leans on the")
print("  single-harmonic collapse at a forced scale.  Testing THAT gives more:")
print()
print("     D_cut >= 6 : no scale collapses the mass relation.  There is no single")
print("                  multiple-angle, hence no forced hinge-fold and no")
print("                  generation count to read.  THE CONSTRUCTION DOES NOT EXIST.")
print("     D_cut = 5  : collapses to a 4-fold  ->  FOUR generations.")
print("     D_cut = 4  : collapses to a 3-fold  ->  THREE generations.")
print()
print("  So the observed count does not merely satisfy D-1 = 3; it SELECTS between")
print("  the only two dimensions in which the generation-counting mechanism exists")
print("  at all.  Four-dimensional spacetime is derivable inside CR from the")
print("  generation count.")
print()
print("  ** TWO THINGS THIS DOES NOT SHOW, NAMED. **")
print()
print("  (a) THE CHART IS CARRIED OVER, NOT RE-DERIVED.  P3 fixes the slicing")
print("      parameter by the geometry of observation: the hole's image lies on the")
print("      observer's celestial sphere and obtaining a planar chart forces the")
print("      GNOMONIC projection, the orthographic being excluded.  That argument is")
print("      made in four dimensions.  Whether the same chart is forced on a")
print("      (D-2)-sphere of directions is NOT checked here -- r = c sin w is")
print("      assumed.  If the chart fails in higher D the D=5 column weakens and the")
print("      D=4 result is untouched, so the conclusion is robust in the direction")
print("      that matters; but the gap is real.")
print()
print("  (b) THE D-DIMENSIONAL METRIC FUNCTION IS THE STANDARD TANGHERLINI-dS ONE,")
print("      not one derived from CR's own operator in D dimensions.  The operator")
print("      is codimension-one by construction, so this is the natural extension --")
print("      but it is an extension, and it is assumed.")
print()
print("  SKETCH MATERIAL.  Not landed in P14.  What would earn the landing is (a):")
print("  the chart argument redone at general D.")
