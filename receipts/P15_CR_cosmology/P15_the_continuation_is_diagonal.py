#!/usr/bin/env python3
"""
RECEIPT — P15 `sec:predictions`: ** THE CONTINUATION THROUGH THE BRANCH POINT ACTS DIAGONALLY ON
THE TWO PERTURBATION MODES, SO THE SCALE-INVARIANT SPECTRUM DOES NOT REACH THE OBSERVER. **

The falsifier on the companion result (`P15_the_collapse_leg_is_scale_invariant`), named and run one
revision later.  Two independent arguments, and they agree.

  PART 1  the two modes and their spectra from vacuum data: dominant flat, survivor n_s - 1 = 6
  PART 2  ** the PARITY argument: sinh^(2/3) is EVEN in tau, so its correction enters at eta^6 and
          the Frobenius recursion steps in sixes past a resonance at three -- no logarithm **
  PART 3  ** the NUMERICAL argument: continue both modes around the branch point and measure the
          off-diagonal.  It falls as delta^(2/3); the diagonal entry goes to 1 **

rc=0 on success.  Run: python3 P15_the_continuation_is_diagonal.py   (sympy, numpy, scipy)
"""
import sys

import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp

print(__doc__.split("rc=0")[0])

# ---------------------------------------------------------------- PART 1
print("=" * 78)
print("PART 1 — THE TWO MODES AND THEIR SPECTRA")
print("=" * 78)
eta, k, s_ = sp.symbols('eta k s', positive=True), sp.symbols('k', positive=True), sp.symbols('s')
eta = sp.symbols('eta')
assert sorted(sp.solve(sp.Eq(s_ * (s_ - 1), 2), s_)) == [-1, 2]
v_ex = (1 - sp.I / (k * eta)) * sp.exp(-sp.I * k * eta) / sp.sqrt(2 * k)
ser = sp.series(v_ex, eta, 0, 3).removeO().expand()
cm, cp = sp.simplify(ser.coeff(eta, -1)), sp.simplify(ser.coeff(eta, 2))
assert sp.simplify(sp.log(sp.Abs(cm)).diff(k) * k + sp.Rational(3, 2)) == 0
assert sp.simplify(sp.log(sp.Abs(cp)).diff(k) * k - sp.Rational(3, 2)) == 0
print("  indicial exponents {-1, 2}; zeta = v/a goes as eta^-3 (dominant) or const (survivor)")
print("  vacuum data give |c-| ~ k^-3/2 and |c+| ~ k^+3/2, asserted, hence")
print("  ** dominant mode: P ~ k^0, scale-invariant.   surviving mode: P ~ k^6, n_s - 1 = 6. **")

# ---------------------------------------------------------------- PART 2
print()
print("=" * 78)
print("PART 2 — THE PARITY ARGUMENT")
print("=" * 78)
u = sp.symbols('u', positive=True)
corr = sp.simplify(sp.expand(sp.series(sp.sinh(u)**sp.Rational(2, 3), u, 0, 7).removeO()
                             / u**sp.Rational(2, 3)))
odd = [n for n in range(1, 7, 2) if sp.simplify(corr.coeff(u, n)) != 0]
print(f"  sinh^(2/3)(u)/u^(2/3) = {corr}")
print(f"  ** odd powers present: {odd}  -- NONE.  The correction is EVEN in tau. **")
assert not odd
print("  u ~ tau ~ eta^3, so the correction enters the potential at eta^6 and the Frobenius")
print("  series steps in SIXES from each root, while the resonance that would force a logarithm")
print("  sits at a step of THREE:")
visited = [-1 + 6 * n for n in range(5)]
print(f"     from s = -1 the series visits {visited}; the other root 2 is reached: {2 in visited}")
assert 2 not in visited
print("  ** no logarithm, so the two solutions stay pure powers and the continuation is diagonal. **")

# ---------------------------------------------------------------- PART 3
print()
print("=" * 78)
print("PART 3 — THE NUMERICAL ARGUMENT")
print("=" * 78)
A_, KK = 1.0, 1.0


def continue_dominant(delta):
    th0 = np.pi - 1e-9
    tau0 = delta * np.exp(1j * th0)
    y0 = [tau0 ** (-1 / 3), (-1 / 3) * tau0 ** (-4 / 3)]

    def rhs(th, y):
        tau = delta * np.exp(1j * th)
        b = 1.5
        S, C = np.sinh(b * tau), np.cosh(b * tau)
        a0 = A_ * np.power(S, 2.0 / 3.0)
        a1 = A_ * (2.0 / 3.0) * b * np.power(S, -1.0 / 3.0) * C
        a2 = A_ * b * b * ((2.0 / 3.0) * np.power(S, 2.0 / 3.0)
                           - (2.0 / 9.0) * np.power(S, -4.0 / 3.0) * C * C)
        v, vp = y
        vpp = -(a0 * a1 * vp + (KK ** 2 - a0 * a2 - a1 ** 2) * v) / a0 ** 2
        return [vp * 1j * tau, vpp * 1j * tau]

    sol = solve_ivp(rhs, [th0, 0.0], y0, rtol=1e-11, atol=1e-14)
    v, vp = sol.y[0, -1], sol.y[1, -1]
    t = delta + 0j
    b1, b1p = t ** (2 / 3), (2 / 3) * t ** (-1 / 3)
    b2, b2p = t ** (-1 / 3), (-1 / 3) * t ** (-4 / 3)
    det = b1 * b2p - b2 * b1p
    return (v * b2p - vp * b2) / det, (vp * b1 - v * b1p) / det


print(f"  {'delta':>9} {'diagonal':>12} {'LEAKAGE eps':>14} {'eps ratio':>11}  (expect 10^-2/3 = 0.2154)")
prev = None
for d in [1e-3, 1e-4, 1e-5, 1e-6]:
    c1, c2 = continue_dominant(d)
    eps = abs(c1) / abs(c2) * d
    rr = eps / prev if prev else float('nan')
    print(f"  {d:>9.0e} {abs(c2):>12.6f} {eps:>14.4e} {rr:>11.4f}")
    if prev:
        assert eps < prev
        assert abs(rr - 10 ** (-2 / 3)) < 0.02, (d, rr)
    prev = eps
assert abs(abs(c2) - 1.0) < 1e-3
print()
print("  ** the diagonal entry goes to 1 and the leakage falls as a CLEAN POWER delta^(2/3). **")
print("     The power law is itself the evidence against a logarithm: a log would leave a residual")
print("     no power of delta removes.  Two independent arguments, one verdict.")
print()
print("  BOUND: this settles the connection at the branch point for the SCALAR mode equation on")
print("  this background.  It does not settle what a background correction ODD in tau would do --")
print("  which is what mixing would require, and is the open route.")
print()
print("ALL PASS")
sys.exit(0)
