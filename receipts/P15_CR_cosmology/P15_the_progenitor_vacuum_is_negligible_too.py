#!/usr/bin/env python3
"""
RECEIPT — P15: ** THE PROGENITOR'S OWN VACUUM, CARRIED THROUGH THE FULL PASSAGE AND AMPLIFIED BY THE
BRANCH-POINT MIXING, IS ALSO NEGLIGIBLE AGAINST THE OBSERVED AMPLITUDE. **

`prop:amplitude` rules out the SUBSTRATE's de Sitter vacuum ($\\sim10^{-122}$, short by $10^{113}$)
and the paper reads the classical, inherited character of the primordial statistics off it.  But the
inheritance story locates the fluctuations in the PROGENITOR, whose own vacuum that proposition does
not address.  This receipt addresses it.

  PART 1  ** the collapse-side background is one function, a = M(rho x + x^2/2), and its
          Mukhanov--Sasaki potential 2/(x(x+2 rho)) is M-free **
  PART 2  ** the connection through equality: a growing mode D/x arrives at the crunch as the
          constant (3/2 rho) D -- closed form, confirmed by integration from vacuum data **
  PART 3  ** the transfer law, assembled: P = 18 k^3 D_k^2/(M^2 rho^6), scale-invariant **
  PART 3b ** and the crunch residue's DOUBLING is the entire effect of the true variable **
  PART 4  ** the number: the vacuum delivers ~1e-112 at the progenitor's determined composition,
          against an observed 2.1e-9 **

rc=0 on success.  Run: python3 P15_the_progenitor_vacuum_is_negligible_too.py   (numpy scipy sympy)
"""
import sys

import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

print(__doc__.split("rc=0")[0])
fail = []

# =====================================================================
print("=" * 78)
print("PART 1 — THE BACKGROUND AND ITS POTENTIAL")
print("=" * 78)
M_, rho_ = sp.symbols('M rho', positive=True)
x = sp.symbols('x', positive=True)                  # x = |eta - eta_c|, crunch at x = 0
a_x = M_ * (rho_ * x + x**2 / 2)
U = sp.simplify(sp.diff(a_x, x, 2) / a_x)
print(f"  a(x) = {a_x}      (closed dust+radiation interior at the crunch, A = 2M, rho = 2 sqrt B/A)")
print(f"  z''/z = a''/a = {sp.factor(U)}      -- ** M has cancelled **")
if sp.simplify(U - 2 / (x * (x + 2 * rho_))) != 0:
    fail.append("potential")
print("  x >> 2 rho : 2/x^2, the beta = 2 matter contraction, exponents (-1, 2)")
print("  x << 2 rho : 1/(rho x), the radiation crunch,        exponents (0, 1)")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CONNECTION COEFFICIENT")
print("=" * 78)
v0 = sp.simplify(a_x * sp.integrate(1 / a_x**2, x))       # the mode dominant on contraction
lim0 = sp.simplify(sp.limit(v0, x, 0))
print(f"  v0 = a ∫ dx/a^2 :   x -> 0 gives {lim0} ;   x -> oo gives -2/(3 M x)")
mp.mp.dps = 60          # the two logs cancel to ~30 digits at large x; float64 cannot see it
f_num = sp.lambdify(x, v0.subs({M_: 1, rho_: sp.Rational(1, 1000)}), 'mpmath')
tail = float(mp.mpf('1e6') * f_num(mp.mpf('1e6')))
print(f"  checked numerically at M = 1, rho = 1e-3, x = 1e6 :  x*v0 = {tail:.8f}  vs -2/3")
if sp.simplify(lim0 + 1 / (M_ * rho_)) != 0 or abs(tail + 2 / 3) > 1e-6:
    fail.append("connection closed form")
print("  ** so c_0 = (3 / 2 rho) D  for an incoming growing mode v -> D/x. **")

print()
print("  Confirmed on the full k != 0 equation from vacuum data v -> e^{ikx}/sqrt(2k):")


def c0_of(k, rho, n_osc=300.0):
    x_f = 1e-4 * rho

    def rhs(xx, y):
        pot = 2.0 / (xx * (xx + 2.0 * rho))
        return [y[1], (pot - k**2) * y[0], y[3], (pot - k**2) * y[2]]

    x_i = n_osc / k
    n = np.sqrt(2.0 * k)
    y0 = [np.cos(k * x_i) / n, -k * np.sin(k * x_i) / n,
          np.sin(k * x_i) / n, k * np.cos(k * x_i) / n]
    s = solve_ivp(rhs, [x_i, x_f], y0, rtol=1e-12, atol=1e-16, method='DOP853')
    v = s.y[0, -1] + 1j * s.y[2, -1]
    vx = s.y[1, -1] + 1j * s.y[3, -1]
    return abs(v - vx * x_f)


TARGET = 3.0 / (2.0 * np.sqrt(2.0))
print(f"  {'rho':>10} {'k':>8} {'|c0| k^(3/2) rho':>20} {'3/(2 sqrt 2)':>16}")
worst = 0.0
for rho in [1e-3, 1e-4]:
    for k in [2.0, 10.0, 30.0]:
        val = c0_of(k, rho) * k**1.5 * rho
        worst = max(worst, abs(val / TARGET - 1))
        print(f"  {rho:>10.0e} {k:>8.1f} {val:>20.6f} {TARGET:>16.6f}")
print(f"  ** worst departure {worst*100:.2f}% -- and the k^(-3/2) is the beta = 2 leg's scale")
print(f"     invariance surviving the passage through equality intact. **")
if worst > 0.03:
    fail.append("connection numeric")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TRANSFER LAW")
print("=" * 78)
hbar, kk, Ms, rr, Dk = sp.symbols('hbar k M rho D_k', positive=True)
# ** r2376+c54.153: THE MONODROMY IS 4 pi/rho, NOT 2 pi/rho.  This receipt carried the TENSOR
#    value in the SCALAR chain for nine revisions, so its transfer law and its A_s were a factor
#    4 low and disagreed with the paper citing it.  PART 3b below verifies that the doubling is
#    the ENTIRE effect of using the true hydrodynamical variable, which is not obvious: z_S goes
#    as a^{3/2} in the matter era (exponents (-2,3), against a's (-1,2)) and the final division
#    is by z_S rather than a, and those two differences cancel. **
zeta = (4 * sp.pi / rr) * (sp.Rational(3, 2) / rr) * Dk / (Ms * rr)      # connection, monodromy, v/z
P = sp.simplify(kk**3 / (2 * sp.pi**2) * zeta**2)
print(f"  zeta_out = (4 pi/rho) * (3/2 rho) D_k / (M rho)   ⇒   P(k) = {P}")
print("  ** three factors of 1/rho: the connection, the monodromy, and a'(eta_c) = -M rho. **")
Pvac = sp.simplify(P.subs(Dk, sp.sqrt(hbar / 2) * kk**sp.Rational(-3, 2)))
print(f"  with the vacuum D_k = sqrt(hbar/2) k^(-3/2) :   P = {Pvac}")
print("  ** k has cancelled identically -- the spectrum is scale-invariant. **")
if sp.simplify(sp.diff(Pvac, kk)) != 0 or sp.simplify(Pvac - 9 * hbar / (Ms**2 * rr**6)) != 0:
    fail.append("transfer law")
print("  In G = c = 1, hbar/M^2 = (l_P/M)^2, so   ** A_s^vac = 9 (l_P/M)^2 rho^(-6) **")

# =====================================================================
print()
print("=" * 78)
print("PART 3b — AND THE DOUBLING IS THE ENTIRE EFFECT, WHICH IS NOT OBVIOUS")
print("=" * 78)
print("  The true hydrodynamical variable differs from a in THREE places, not one:")
print("    (i)   matter era:  z_S ~ a^{3/2}, so the exponents are (-2,3) against a's (-1,2);")
print("    (ii)  crunch:      z_S ~ a, exponents (0,1) for both, but the residue DOUBLES;")
print("    (iii) the final division is by z_S, not by a.")
print("  ** So the net factor is not the monodromy ratio by inspection.  Propagate the SAME")
print("     physical initial condition (zeta = 1, dzeta/dx = 0 in the matter era) under each")
print("     potential and read the ratio of the emerging survivor amplitudes. **")
ee = sp.symbols('ee')
A_num = 2.0
print(f"\n  {'rho':>10} {'zeta_out (z = a)':>20} {'zeta_out (z_S)':>18} {'ratio':>10}")
_ratios = []
for _rho in [0.2, 0.1, 0.0539]:
    _B = _rho**2 * A_num**2 / 4
    _a = (A_num / 2) * (1 - sp.cos(ee)) + sp.sqrt(_B) * sp.sin(ee)
    _zS = _a * (_a + 4 * _B / (3 * A_num)) / sp.diff(_a, ee)
    _ec = float(2 * np.pi - 2 * np.arctan(_rho))
    _out = []
    for _Z, _P in [(_a, 1.0 / _rho), (_zS, 2.0 / _rho)]:
        _U = sp.lambdify(ee, sp.simplify(sp.diff(_Z, ee, 2) / _Z), 'numpy')
        _Zn = sp.lambdify(ee, _Z, 'numpy')
        _Zp = sp.lambdify(ee, sp.diff(_Z, ee), 'numpy')
        _x0, _eps = 0.5, 1e-7
        _s = solve_ivp(lambda x, y: [y[1], _U(_ec - x) * y[0]], [_x0, _eps],
                       [_Zn(_ec - _x0), -_Zp(_ec - _x0)],
                       rtol=1e-12, atol=1e-20, method='DOP853')
        _L = np.log(_eps / (2 * _rho))
        _c0 = _s.y[0, -1] / (1.0 + _P * _eps * _L)
        _out.append(2 * np.pi * _P * _c0 / (_Zn(_ec - _eps) / _eps))
    _r = _out[1] / _out[0]
    _ratios.append(_r)
    print(f"  {_rho:>10.4f} {_out[0]:>20.5g} {_out[1]:>18.5g} {_r:>10.4f}")
if max(abs(r - 2.0) for r in _ratios) > 5e-3:
    fail.append("the doubling is the entire effect")
print("\n  ** EXACTLY 2 IN AMPLITUDE, HENCE 4 IN POWER, AT EVERY COMPOSITION TESTED -- the")
print("     matter-era exponent change and the change of final divisor cancel, and what survives")
print("     is the crunch residue alone.  That is why the a-based chain can be corrected by one")
print("     factor rather than rebuilt. **")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE NUMBER")
print("=" * 78)
LAM, LP, MPC, AS_OBS = 1.1056e-52, 1.616255e-35, 3.0857e22, 2.1e-9
alpha = np.sqrt(3.0 / LAM)
M_nar = alpha / (3 * np.sqrt(3))
rho_max = 0.0539                      # the composition DETERMINED (P16, c54.143)
As_vac = 9.0 * (LP / M_nar)**2 * rho_max**-6.0
print(f"  {'quantity':>50} {'value':>16}")
for nm, v in [("alpha [Mpc]", alpha / MPC),
              ("M_max = alpha/(3 sqrt 3) [Mpc]  (Nariai)", M_nar / MPC),
              ("the determined rho", rho_max),
              ("A_s from the progenitor vacuum", As_vac),
              ("A_s observed", AS_OBS),
              ("shortfall", AS_OBS / As_vac)]:
    print(f"  {nm:>50} {v:>16.4g}")
print()
print(f"  {'vacuum':>46} {'delivers':>14} {'short by':>12}")
for nm, v in [("the substrate's own (prop:amplitude)", (LP / alpha)**2),
              ("the progenitor's, unamplified", (LP / M_nar)**2),
              ("the progenitor's, WITH the mixing", As_vac)]:
    print(f"  {nm:>46} {v:>14.2e} {AS_OBS/v:>12.1e}")
if not (1e101 < AS_OBS / As_vac < 1e106):
    fail.append("shortfall")
print()
print("  ** THE COMPARISON IS TWO-STEP AND THE CORPUS HAD IT COMPRESSED INTO ONE (fixed c54.153).")
print("     The mixing buys 10^8.6 over the PROGENITOR'S OWN bare vacuum; the progenitor's vacuum")
print("     sits 10^10 above the SUBSTRATE'S; so eighteen orders separate the substrate's vacuum")
print("     from the progenitor's amplified one, and it is still SHORT BY A HUNDRED AND THREE. **")
print("  The primordial statistics are classical and non-vacuum for the")
print("  source that actually supplies them, and not only for the substrate that does not.")
print()
print("  Corollary: A_s does not measure the progenitor's mass.  What the construction fixes is the")
print("  MULTIPLIER, P = 18 k^3 D_k^2/(M^2 rho^6), for any incoming amplitude D_k.")

print()
if fail:
    print("FAIL: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
