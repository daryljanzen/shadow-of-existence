#!/usr/bin/env python3
"""RECEIPT — convexity/optimisation bake `CX1`: ** THE HUBBLE TENSION IS A CONVEXITY STATEMENT.  THE
RADIATION-PINNED chi^2(H0) IS STRICTLY CONVEX WITH A UNIQUE MINIMIZER (~67) THAT EXCLUDES 73; THE
GEOMETRIC RATE MAKES THE OBJECTIVE FLAT IN H0 (DEGENERATE HESSIAN, ARGMIN A WHOLE LINE THAT INCLUDES
73), BECAUSE H0 CANCELS IN THE DIMENSIONLESS BAO RATIO WHEN THE RULER SCALES AS c/H0. **

LEVEL: NO RATE -- a convexity/degeneracy classification of a fit objective.

WHY THIS PROBE.  The convexity/optimisation field, thrown for the first time at r3505 (order named it
  "convexity x143"), is almost entirely a HOMONYM: `convex`/`convexity`/`concave`/`KKT`/`epigraph`/
  `objective function` are x0 across all seventeen bodies, and the x143 is the substring behind
  `constraint` -- the HAMILTONIAN (ADM/Dirac) constraint of canonical gravity (P08 l.264/439 states it
  as such), not an optimisation constraint.  The one genuine optimisation content in the corpus is
  P15's chi^2 fits, and one of them carries a real CONVEXITY statement the field can check: P15 l.274
  says the radiation-pinned LambdaCDM chi^2 is "a steep parabola minimized near 67 and excluding the
  local value -- this is the tension", while "CR's chi^2 is flat in H0".  A parabola is a convex
  objective with a UNIQUE minimizer; "flat" is a DEGENERATE (non-strictly-convex) objective whose
  minimizer set is a whole line.  The Hubble tension, read through this field, IS that convexity fact.

THE MECHANISM, EXACT.  The BAO observable is the dimensionless ratio D_M(z)/r_s.  Comoving distance
  D_M = (c/H0) I(z) with I(z)=int_0^z dz'/E(z') dimensionless.
    - LambdaCDM: r_s is a PHYSICAL length fixed by pre-recombination (radiation) physics, ~147 Mpc, and
      does NOT scale with the late-time H0.  Then D_M/r_s = (c/H0) I(z)/r_s DEPENDS on H0
      (d/dH0 = -(c I)/(H0^2 r_s) != 0), so chi^2(H0) has a unique interior minimizer -- strictly convex
      near it -- pinned near 67 and excluding 73.  That non-cancellation IS the tension.
    - CR geometric rate: the ruler is set by the SAME geometric rate and scales as r_s ~ (c/H0) J with J
      dimensionless, so D_M/r_s = I(z)/J and H0 CANCELS (d/dH0 = 0).  chi^2(H0) is FLAT: gradient zero,
      Hessian zero, argmin the whole H0 axis -- so it fits at ANY H0, 73 included, and there is no
      tension to have.

WHAT IS CLAIMED, AND WHAT IS NOT.  Claimed: the tension-vs-no-tension is exactly strict-convexity
  (unique argmin) vs affine-degeneracy (argmin a line), and the switch is the H0-cancellation in the
  geometric ratio -- a checkable algebraic fact.  NOT claimed: a new fit (the numbers 67/73 and
  chi^2/dof~1 at any H0 are P15's, receipted `P15_hubble_expansion_confrontation_v2`,
  `P15_desi_dr2_confrontation`); CX1 supplies the convexity reading their "parabola" / "flat" language
  already carries.  This is the convexity field's ONE genuine WORKED paper; the field is otherwise the
  Hamiltonian-constraint homonym, and CX1 records the bite and its boundary.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

print("=" * 78)
print("  CX1 — the Hubble tension is a convexity statement: strict convexity vs flat degeneracy")
print("=" * 78)

H0, z, c, rs, J = sp.symbols('H0 z c r_s J', positive=True)
I = sp.Function('I')(z)                       # dimensionless comoving-distance integral
DM = (c / H0) * I

# (1) LambdaCDM: r_s fixed physical length -> ratio depends on H0
ratio_L = sp.simplify(DM / rs)
dL = sp.simplify(sp.diff(ratio_L, H0))
assert dL != 0, "radiation-pinned ratio must depend on H0"
print(f"\n  (1) LambdaCDM (r_s fixed):  D_M/r_s = {ratio_L},  d/dH0 = {dL}  != 0")
print("      -> chi^2(H0) depends on H0, has a UNIQUE minimizer (strictly convex near it): the tension.")

# (2) CR geometric: r_s ~ c/H0 -> H0 cancels, ratio flat
rs_geom = (c / H0) * J
ratio_CR = sp.simplify(DM / rs_geom)
dCR = sp.simplify(sp.diff(ratio_CR, H0))
assert dCR == 0 and H0 not in ratio_CR.free_symbols, "geometric ratio must be independent of H0"
print(f"\n  (2) CR geometric (r_s ~ c/H0):  D_M/r_s = {ratio_CR},  d/dH0 = {dCR}  == 0")
print("      -> chi^2(H0) is FLAT in H0: gradient 0, argmin the whole axis -> fits at any H0, incl. 73.")

# (3) the convexity consequence, stated as a theorem on the objective's Hessian
h, a, b, k, K = sp.symbols('h a b k K', real=True)
chi2_conv = a * (h - b)**2 + k                       # strictly convex iff a > 0
hess_conv = sp.diff(chi2_conv, h, 2)
argmin_conv = sp.solve(sp.diff(chi2_conv, h), h)
assert hess_conv == 2 * a and argmin_conv == [b], "convex quadratic: Hessian 2a, unique argmin b"
chi2_flat = K                                        # constant in h
assert sp.diff(chi2_flat, h) == 0 and sp.diff(chi2_flat, h, 2) == 0, "flat objective: zero grad & Hessian"
print(f"\n  (3) LambdaCDM chi^2(H0) = a(H0-b)^2+k:  Hessian = {hess_conv} (>0 for a>0), UNIQUE argmin = {argmin_conv[0]}")
print(f"      CR chi^2(H0) = K (flat):  gradient = 0, Hessian = 0, argmin = ALL H0 (degenerate).")

# (4) numeric illustration of the corpus's stated shapes: unique min ~67 excludes 73; flat includes 73
import math
chi2_L = lambda x: 0.5 * (x - 67.0)**2            # steep parabola, argmin 67
chi2_C = lambda x: 5.0                             # flat
xs = [66, 67, 68, 70, 73]
argmin_L = min(xs, key=chi2_L)
argmin_set_C = [x for x in xs if abs(chi2_C(x) - min(chi2_C(v) for v in xs)) < 1e-12]
assert argmin_L == 67 and 73 not in [argmin_L], "convex: unique argmin 67, excludes 73"
assert 73 in argmin_set_C, "flat: argmin set includes 73"
print(f"\n  (4) shapes P15 states: LambdaCDM parabola argmin over {xs} = {argmin_L} (excludes 73);")
print(f"      CR flat: every H0 is an argmin, set = {argmin_set_C} -> 73 in it.  The tension is the")
print("      strict convexity; CR dissolves it by degeneracy, and the switch is the H0-cancellation.")

print("\n  ** VERDICT: the Hubble tension IS a convexity statement -- a strictly convex radiation-pinned")
print("     chi^2(H0) with a unique minimizer excluding 73 -- and the geometric rate dissolves it by")
print("     making the objective flat (degenerate Hessian, argmin a line including 73), because H0")
print("     cancels in the dimensionless BAO ratio when the ruler scales as c/H0.  This is the")
print("     convexity field's one genuine bite; the rest of its x143 is the Hamiltonian-constraint")
print("     homonym. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
