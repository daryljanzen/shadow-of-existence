#!/usr/bin/env python3
"""
RECEIPT — P16 (the collapse excursion): ** THE MODE MIXING AT THE CRUNCH IS 2 pi / rho, WITH
rho = 2 sqrt(B)/A THE RADIATION-TO-DUST AMPLITUDE RATIO — AND IT IS DISCONTINUOUS AT ZERO
RADIATION, BECAUSE ANY RADIATION AT ALL CHANGES THE INDICIAL EXPONENTS. **

  PART 1  the crunch's two derivatives separate by species: slope = radiation, curvature = dust
  PART 2  ** exponents (-1,2) with pure dust; (0,1) with ANY radiation -- a discrete jump **
  PART 3  ** the monodromy off-diagonal is exactly 2 pi i p = -2 pi i / rho, verified **

rc=0 on success.  Run: python3 P16_the_mixing_is_two_pi_over_rho.py   (sympy, numpy, scipy)
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("rc=0")[0])
A, t = sp.symbols('A t', positive=True)          # t = rho = 2 sqrt(B) / A

print("=" * 78)
print("PART 1 — THE CRUNCH'S DERIVATIVES SEPARATE BY SPECIES")
print("=" * 78)
sin_c, cos_c = -2 * t / (1 + t**2), (1 - t**2) / (1 + t**2)
sqrtB = A * t / 2
ap = sp.simplify((A / 2) * sin_c + sqrtB * cos_c)
app = sp.simplify((A / 2) * cos_c - sqrtB * sin_c)
print("  a = (A/2)(1 - cos eta) + sqrt(B) sin eta vanishes at tan(eta_c/2) = -rho, and there")
print(f"     a'(eta_c)  = {ap}   = -sqrt(B)  ** the RADIATION amplitude **")
print(f"     a''(eta_c) = {app}   = A/2       ** the DUST amplitude **")
assert sp.simplify(ap + sqrtB) == 0 and sp.simplify(app - A / 2) == 0
p_expr = sp.simplify(app / ap)
print(f"  ** p := a''/a' = {p_expr} = -1/rho, the dust-to-radiation ratio and nothing else **")
assert sp.simplify(p_expr + 1 / t) == 0

print()
print("=" * 78)
print("PART 2 — THE EXPONENTS JUMP")
print("=" * 78)
s_ = sp.symbols('s')
d2 = sorted(sp.solve(sp.Eq(s_ * (s_ - 1), 2), s_))
d1 = sorted(sp.solve(sp.Eq(s_ * (s_ - 1), 0), s_))
print(f"  pure dust : a ~ sigma^2, potential 2/sigma^2  =>  exponents {d2}, difference 3")
print(f"  radiation : a ~ sigma  , potential p/sigma    =>  exponents {d1}, difference 1")
assert d2 == [-1, 2] and d1 == [0, 1]
print("  ** the pair is (0,1) for EVERY rho > 0 and (-1,2) at rho = 0 exactly.  A discrete jump in")
print("     the indicial pair is not something a small parameter smooths: the pure-dust background")
print("     is a measure-zero exception, not the leading term of a series in the radiation. **")

print()
print("=" * 78)
print("PART 3 — THE MONODROMY, PREDICTED AND MEASURED")
print("=" * 78)
print("  With v_0 = 1 + p sigma ln sigma, one circuit sends ln sigma -> ln sigma + 2 pi i, so")
print("  v_0 -> v_0 + 2 pi i p v_1.  ** Off-diagonal = 2 pi i p = -2 pi i / rho, no free constant. **")
A_v, k_v, cs2 = 2.0, 1.0, 1.0 / 3.0


def loop(rho_v, delta=1e-4):
    sB, etac, pex = A_v * rho_v / 2.0, 2 * np.pi - 2 * np.arctan(rho_v), -1.0 / rho_v

    def rhs(th, y):
        sig = delta * np.exp(1j * th)
        e = etac + sig
        aa = (A_v / 2) * (1 - np.cos(e)) + sB * np.sin(e)
        app_ = (A_v / 2) * np.cos(e) - sB * np.sin(e)
        v, vp = y
        return [vp * 1j * sig, (-(cs2 * k_v**2) + app_ / aa) * v * 1j * sig]

    ls = np.log(delta + 0j)
    y0 = [1.0 + pex * delta * ls, pex * (ls + 1.0)]
    sol = solve_ivp(rhs, [0.0, 2 * np.pi], y0, rtol=1e-12, atol=1e-15)
    return abs((sol.y[0, -1] - y0[0]) / delta), abs(2 * np.pi * pex)


print(f"\n  {'rho':>8} {'rho_r/rho_m at a_max':>21} {'measured':>12} {'2 pi / rho':>12} {'ratio':>8}")
for rv in [0.8, 0.4, 0.2, 0.1]:
    m, pr = loop(rv)
    r = m / pr
    print(f"  {rv:>8.3f} {rv**2/4.0:>21.5f} {m:>12.4f} {pr:>12.4f} {r:>8.4f}")
    assert 0.99 < r < 1.01, (rv, r)
print("\n  ** matched to better than one per cent at every radiation fraction, with no fitted")
print("     constant.  The mixing is 2 pi / rho. **")
print()
print("  READING: a progenitor with MORE radiation has a SMALLER p and mixes LESS.  The")
print("  scale-invariant spectrum frozen on the contracting side reaches the observer in inverse")
print("  proportion to the radiation the progenitor carried -- which is a constraint from the sky")
print("  on the composition, running backwards through the chain.")
print()
print("  BOUND: interior at leading order (closed FRW, dust + radiation, no anisotropy, no")
print("  dissipation); sound speed held at 1/3 rather than run through the mixture's own c_s(a).")
print("  ** What is exact is the indicial structure, the identification of p, and the 2 pi i p")
print("  monodromy -- none of which the bounds above can soften. **")
print()
print("ALL PASS")
sys.exit(0)
