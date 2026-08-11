#!/usr/bin/env python3
"""
P15 receipt — the two ranges of the one constant, and the fixed ratio between them.

P15 states that Lambda "governs both the global expansion and, per structure, the local
scale at which structure resists it -- the Hubble-Eddington radius -- one constant read at
two ranges."  That claim is qualitative.  This receipt supplies the quantitative relation.

  LOCAL RANGE   (P3, P8): the slicing surface's Gaussian curvature K_G = 1/alpha^2 - M/r^3
                 vanishes at the Hubble-Eddington radius
                      r_star = (M alpha^2)^(1/3)
                 -- where a structure's local bend exactly cancels the substrate's
                 cosmological curvature.

  GLOBAL RANGE  (P7 thm:bead, P8, P15): the bead's outward law
                      r(tau) = (2 M alpha^2)^(1/3) sinh^(2/3)(3 tau / 2 alpha)
                 has amplitude A = (2 M alpha^2)^(1/3).
                 From the Friedmann equation with (8 pi G/3) rho_Lambda = 1/alpha^2:
                      rho_m / rho_Lambda = csch^2(3 tau / 2 alpha)
                 so matter-Lambda equality is at sinh = 1, where r = A exactly.
                 ** The amplitude IS the matter-Lambda equality radius. **

  THE RATIO:
                      A / r_star = 2^(1/3)      exactly, for every M.

So the two ranges are not merely governed by the same constant: they are the same length
up to 2^(1/3).  The factor is the 2 of the Schwarzschild term 2M/r, against the M/r^3 of
the surface's Gaussian curvature -- nothing else enters.
"""
import sympy as sp

M, alpha, tau, r = sp.symbols('M alpha tau r', positive=True)

# --- local range: where K_G vanishes ---------------------------------------
K_G = 1/alpha**2 - M/r**3
r_star = sp.solve(sp.Eq(K_G, 0), r)[0]
assert sp.simplify(r_star - (M*alpha**2)**sp.Rational(1,3)) == 0

# --- global range: the bead amplitude --------------------------------------
A = (2*M*alpha**2)**sp.Rational(1,3)
a_of_t = A*sp.sinh(3*tau/(2*alpha))**sp.Rational(2,3)

# Friedmann check: rho_m/rho_Lambda = csch^2
H = sp.simplify(sp.diff(a_of_t, tau)/a_of_t)
ratio = sp.simplify(sp.trigsimp((H**2 - 1/alpha**2)*alpha**2))
assert sp.simplify(ratio - 1/sp.sinh(3*tau/(2*alpha))**2) == 0, "rho_m/rho_L must be csch^2"

# equality at sinh = 1  ->  a = A
a_eq = a_of_t.subs(sp.sinh(3*tau/(2*alpha)), 1)
assert sp.simplify(a_eq - A) == 0, "the amplitude must BE the equality radius"

# --- the ratio -------------------------------------------------------------
ratio_AR = sp.simplify(A/r_star)
assert sp.simplify(ratio_AR - 2**sp.Rational(1,3)) == 0
assert not ratio_AR.has(M) and not ratio_AR.has(alpha), "the ratio must be pure"

print("P15_two_ranges_ratio — PASS")
print(f"  local  : r_* = {r_star}      (K_G = 1/alpha^2 - M/r^3 vanishes)")
print(f"  global : A   = {A}   (= the matter-Lambda equality radius)")
print(f"  ratio  : A/r_* = {ratio_AR}  — pure, independent of M and alpha")
print("  rho_m/rho_Lambda = csch^2(3tau/2alpha), equality at sinh = 1, where r = A")
