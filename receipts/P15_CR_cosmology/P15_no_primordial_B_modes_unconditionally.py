#!/usr/bin/env python3
"""
RECEIPT — P15: ** THE TENSOR SECTOR IS WHERE THE COLLAPSE-TRANSFER MACHINE RUNS WITH NO IDEALISATION
AT ALL, AND IT RETURNS P_T ~ 5e-111 — ONE HUNDRED ORDERS BELOW THE OBSERVATIONAL BOUND. **

The scalar transfer (`P15_the_progenitor_vacuum_is_negligible_too`) needs $z\\propto a$, which for a
fluid holds only when $w$ and $c_s$ are constant.  ** For tensors $z_T=aM_{\\rm Pl}/2$ EXACTLY, for
any content, so $z_T''/z_T=a''/a$ identically and the entire passage — background, connection,
monodromy — applies verbatim with nothing assumed. **

  PART 1  ** z_T/a is a pure number for every equation of state; z_S/a is not **
  PART 2  ** P_T = 144 pi (l_P/M)^2 rho^(-6), scale-invariant, and the number **
  PART 3  ** the ratio: the crossing multiplies the tensor-to-scalar ratio by a CONSTANT, so the
          observed absence of B-modes bounds the PARENT's own ratio **

rc=0 on success.  Run: python3 P15_no_primordial_B_modes_unconditionally.py      (numpy sympy)
"""
import sys

import numpy as np
import sympy as sp

print(__doc__.split("rc=0")[0])
fail = []

LAM, LP, MPC = 1.1056e-52, 1.616255e-35, 3.0857e22
AS_OBS, R_BOUND = 2.1e-9, 0.032
alpha = np.sqrt(3.0 / LAM)
M_nar = alpha / (3 * np.sqrt(3))
RHO_HI = 0.0539                     # the progenitor's determined composition (c54.143)

# =====================================================================
print("=" * 78)
print("PART 1 — WHICH SECTOR CARRIES A HYPOTHESIS")
print("=" * 78)
print(f"  {'variable':>12} {'z':>30} {'z/a constant?':>26}")
for nm, z, note in [("scalar", "a sqrt(3(1+w)) M_Pl / c_s", "only if w AND c_s are"),
                    ("tensor", "a M_Pl / 2", "** for every content **")]:
    print(f"  {nm:>12} {z:>30} {note:>26}")
# ** r2376+c54.153: PART 1 used to PRINT the two z's as string literals, so "for every content"
#    was asserted in prose inside a receipt that could not fail.  It is now a symbolic identity
#    on an ARBITRARY a(eta), which is what "unconditionally" has to mean. **
_e = sp.symbols('eta')
_Mp = sp.symbols('M_Pl', positive=True)
_a = sp.Function('a')(_e)
_zT = _a * _Mp / 2
if sp.simplify(sp.diff(_zT, _e, 2) / _zT - sp.diff(_a, _e, 2) / _a) != 0:
    fail.append("z_T''/z_T = a''/a for arbitrary a")
print("  ** SYMBOLIC CHECK on an ARBITRARY a(eta): z_T = a M_Pl/2 gives z_T''/z_T - a''/a = "
      f"{sp.simplify(sp.diff(_zT,_e,2)/_zT - sp.diff(_a,_e,2)/_a)} identically -- no content, no")
print("     equation of state, no sound speed enters. **")
print("  Across the progenitor's equality (1+w) runs 1 -> 4/3 and c_s runs 0 -> 1/sqrt3, so z_S/a")
print("  moves and z_T/a does not.  ** The tensor potential IS a''/a, unconditionally. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE TENSOR POWER")
print("=" * 78)
k, rho, M, hbar, Mpl = sp.symbols('k rho M hbar M_Pl', positive=True)
D = sp.sqrt(hbar / 2) * k**sp.Rational(-3, 2)              # vacuum, per polarisation
C = (2 * sp.pi / rho) * (sp.Rational(3, 2) / rho) * D      # connection (3/2rho) then monodromy
PT = sp.simplify(2 * k**3 / (2 * sp.pi**2) * (C / (M * rho * Mpl / 2))**2)
print(f"  h_out = C/(a M_Pl/2) at the crunch, a = M rho |sigma|   =>   P_T = {PT}")
if sp.simplify(sp.diff(PT, k)) != 0:
    fail.append("P_T not scale-invariant")
PT_c = sp.simplify(PT.subs({hbar: 1, Mpl: 1 / sp.sqrt(8 * sp.pi)}))
print(f"  in G = c = hbar = 1 :  P_T = {PT_c}     ** = 144 pi (l_P/M)^2 rho^(-6) **")
if sp.simplify(PT_c - 144 * sp.pi / (M**2 * rho**6)) != 0:
    fail.append("P_T coefficient")


def P_T_of(r_, M_=M_nar):
    return 144 * np.pi * (LP / M_)**2 * r_**-6.0


bound = R_BOUND * AS_OBS
print()
print(f"  {'quantity':>46} {'value':>16}")
for nm, v in [("M_max = alpha/(3 sqrt 3)  [Mpc]", M_nar / MPC),
              ("rho, determined", RHO_HI),
              ("P_T predicted", P_T_of(RHO_HI)),
              ("P_T observational ceiling (r < 0.032)", bound),
              ("below the ceiling by", bound / P_T_of(RHO_HI)),
              ("r predicted", P_T_of(RHO_HI) / AS_OBS)]:
    print(f"  {nm:>46} {v:>16.4g}")
if not bound / P_T_of(RHO_HI) > 1e95:
    fail.append("shortfall")
print()
print("  ** SO THERE ARE NO PRIMORDIAL B-MODES AT ANY CONCEIVABLE SENSITIVITY, AND THE STATEMENT NO")
print("     LONGER RESTS ON THE SUBSTRATE'S OWN TENSOR FLOOR -- it now covers the progenitor's")
print("     vacuum, carried through the mixing, which is the source the inheritance story names. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT THE ABSENCE OF B-MODES MEASURES")
print("=" * 78)
# ** r2376+c54.153: THE SCALAR LEG CARRIES 4 pi/rho, NOT 2 pi/rho (c54.146).  This receipt used
#    the tensor constant C for BOTH sectors, which made the scalar power a factor 4 too small and
#    the crossing ratio 24 instead of 6.  The INDEX row and both papers already carried 6; the
#    file did not. **
C_S = 2 * C                                                    # 4 pi/rho against the tensor's 2 pi/rho
PS = sp.simplify(k**3 / (2 * sp.pi**2) * (C_S / (M * rho * sp.sqrt(3) * Mpl))**2)   # w=0, c_s=1
r_cross = sp.simplify(PT / PS)
print(f"  Every k-dependent factor of the passage is shared by the two sectors, and the one factor")
print(f"  that is NOT -- the crunch residue, 4 pi/rho for scalars against 2 pi/rho for tensors --")
print(f"  is also k-free, so the crossing multiplies the ratio by a constant:")
print(f"  ** r_out = {r_cross} x r_in **   (24 with the tensor residue used for both, which is the")
print(f"  error this file carried until c54.153; the doubling divides it by four)")
if sp.simplify(r_cross - 6) != 0:
    fail.append("crossing ratio")
print()
print(f"  {'reading':>40} {'consequence':>34}")
for a_, b_ in [("parent's tensors at its own vacuum", f"r = {P_T_of(RHO_HI)/AS_OBS:.0e}"),
               ("parent's tensors enhanced like its scalars", "r = 6, excluded by 2 orders"),
               ("** what the sky permits of the parent **", f"** r_in <= {R_BOUND/6:.1e} **")]:
    print(f"  {a_:>40} {b_:>34}")

print()
if fail:
    print("FAIL: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
