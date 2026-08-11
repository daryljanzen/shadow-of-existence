#!/usr/bin/env python3
"""
RECEIPT — P15 `sec:transmission` / `sec:predictions`:
** THE COLLAPSE LEG IS A SCALE-INVARIANT BACKGROUND, AND THE CORPUS SAYS IT HAS NONE. **

P15 lists as an established signature: *"the branch point carries the progenitor tilt and does not
drive $n_s\\to1$; CR has no inflationary scale-invariant attractor."*  The adjective carries the
sentence.  There are TWO backgrounds that freeze a scale-invariant spectrum -- the two roots of one
quadratic -- and only one of them is inflation.

  PART 1  the condition beta(beta-1) = 2 and its two roots: -1 (de Sitter) and +2 (matter contraction)
  PART 2  ** the corpus's own collapse leg is beta = 2 EXACTLY **
  PART 3  ** the spectrum integrated on it: flat to a part in 10^4 **

rc=0 on success.  Run: python3 P15_the_collapse_leg_is_scale_invariant.py   (sympy, numpy, scipy)
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("rc=0")[0])

# ---------------------------------------------------------------- PART 1
print("=" * 78)
print("PART 1 — THE CONDITION AND ITS TWO ROOTS")
print("=" * 78)
eta, beta = sp.symbols('eta beta', real=True)
zz = sp.simplify(sp.diff((-eta)**beta, eta, 2) / (-eta)**beta)
print(f"  a proportional to (-eta)^beta, z proportional to a  =>  z''/z = {zz}")
roots = sorted(sp.solve(sp.Eq(beta * (beta - 1), 2), beta))
print(f"  ** scale invariance needs 2/eta^2, so beta(beta-1) = 2, giving beta = {roots} **")
assert roots == [-1, 2], roots
print("     beta = -1 : de Sitter inflation, EXPANDING")
print("     beta = +2 : matter-dominated CONTRACTION")

# ---------------------------------------------------------------- PART 2
print()
print("=" * 78)
print("PART 2 — THE COLLAPSE LEG IS beta = 2")
print("=" * 78)
tau, M = sp.symbols('tau M', positive=True)
a_tau = (sp.Rational(9, 2) * M * tau**2)**sp.Rational(1, 3)     # P8 prop:cosmo, P14 receipt
assert sp.simplify(sp.log(a_tau).diff(tau) * tau - sp.Rational(2, 3)) == 0
eta_tau = sp.simplify(sp.integrate(1 / a_tau, tau))
assert sp.simplify(sp.log(eta_tau).diff(tau) * tau - sp.Rational(1, 3)) == 0
print("  the corpus's own near-branch-point law r^3 = (9/2) M tau^2, with a = |r|:")
print("     d ln a / d ln tau = 2/3          (asserted)")
print("     d ln eta / d ln tau = 1/3        (asserted)")
print("  ** so tau ~ eta^3 and a ~ eta^2 : beta = 2, the second root, exactly **")

# ---------------------------------------------------------------- PART 3
print()
print("=" * 78)
print("PART 3 — THE SPECTRUM, INTEGRATED")
print("=" * 78)


def spectrum(b, kk, eta_f=-1e-3):
    def rhs(e, y):
        pot = b * (b - 1) / e**2
        return [y[1], -(kk**2 - pot) * y[0], y[3], -(kk**2 - pot) * y[2]]
    ei = min(-4000.0, -200.0 / kk)
    n = np.sqrt(2 * kk)
    y0 = [np.cos(kk * ei) / n, kk * np.sin(kk * ei) / n,
          -np.sin(kk * ei) / n, kk * np.cos(kk * ei) / n]
    s = solve_ivp(rhs, [ei, eta_f], y0, rtol=1e-10, atol=1e-14)
    return kk**3 * (s.y[0, -1]**2 + s.y[2, -1]**2) / abs(eta_f)**(2 * b)


KS = np.array([0.05, 0.1, 0.2, 0.5, 1.0, 2.0])
for b, nm in [(2.0, "matter contraction"), (-1.0, "de Sitter inflation")]:
    P = np.array([spectrum(b, kk) for kk in KS])
    slope = np.polyfit(np.log(KS), np.log(P), 1)[0]
    print(f"  {nm:>22}:  d ln P / d ln k = {slope:+.5f}   =>  n_s = {1 + slope:.5f}")
    assert abs(slope) < 1e-3, (nm, slope)
print()
print("  ** BOTH FLAT.  The matter-dominated contraction freezes a scale-invariant spectrum")
print("     exactly as de Sitter inflation does, and the corpus's collapse leg is the contraction. **")
print()
print("  BOUND, and it is the whole caution: this is the STANDARD contraction result (Wands 1999;")
print("  Finelli-Brandenberger 2002) applied to a background the corpus DERIVES.  It inherits that")
print("  literature's known difficulty -- whether the matching across the bounce selects the")
print("  scale-invariant mode -- and here the bounce is a branch point with an analytic")
print("  continuation rather than a smooth bounce.  ** The mode-selection question is NOT settled")
print("  by this receipt and is registered separately. **")
print()
print("ALL PASS")
sys.exit(0)
