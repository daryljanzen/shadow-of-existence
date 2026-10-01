#!/usr/bin/env python3
"""
RECEIPT — P16: ** IS THE LEADING-ORDER INTERIOR GOOD ENOUGH?  THE PERTURBATIONS STAY LINEAR BY SIX
ORDERS, AND THE ANISOTROPY THAT KILLS GENERIC BOUNCING MODELS IS EXCLUDED HERE BY THE SAME
ASSUMPTION THAT MAKES THE BRANCH POINT A NARIAI LOCUS. **

The collapse-side analysis is run on a closed FRW ball with dust and radiation, no anisotropy and no
dissipation.  That is stated in the paper as a bound and has never been tested.  Two threats:

  PART 1  ** NONLINEARITY.  zeta grows as |sigma|^{-3} on the beta = 2 leg, so the question is real.
          Normalised by the OBSERVED output, delta peaks at equality at ~1e-6. **
  PART 2  ** ANISOTROPY.  A Bianchi shear adds Sigma^2/a^2 to (da/deta)^2 and WINS at small a,
          turning the crunch into a ∝ |sigma|^{1/2} with a DEGENERATE indicial pair -- a different
          singular point, not a correction. **
  PART 3  ** what excludes it here, and what that leaves open **

rc=0 on success.  Run: python3 P16_the_leading_order_interior_is_adequate.py       (numpy sympy)
"""
import sys

import numpy as np
import sympy as sp

print(__doc__.split("rc=0")[0])
fail = []

AS_OBS, R_BOUND = 2.1e-9, 0.032
LAM, MPC = 1.1056e-52, 3.0857e22
alpha = np.sqrt(3.0 / LAM)
M_nar = alpha / (3 * np.sqrt(3))

# =====================================================================
print("=" * 78)
print("PART 1 — NONLINEARITY")
print("=" * 78)
print("  Run the transfer chain BACKWARDS from the observed amplitude rather than forwards from an")
print("  assumed one: zeta(sigma)/zeta_out = (2/3pi)(rho/|sigma|)^3, and in matter domination")
print("  delta = (2/3)(k/aH)^2 Phi with aH = 2/|sigma| and Phi = (3/5)zeta, so")
print("     ** delta(sigma) = (1/10) k^2 sigma^2 zeta(sigma) **, peaking where matter domination ends.")
zeta_out = np.sqrt(AS_OBS)
h_out = np.sqrt(R_BOUND * AS_OBS)
print()
print(f"  {'rho':>12} {'break mode k = 1/rho':>22} {'delta at equality':>20} {'h at equality':>18}")
for rv in [0.05451, 1e-3, 3.8e-6]:
    kb = 1.0 / rv
    d_eq = (1 / 10) * (2 / (3 * np.pi)) * kb**2 * rv**2 * zeta_out
    h_eq = (2 / (3 * np.pi)) * h_out
    print(f"  {rv:>12.2e} {kb:>22.0f} {d_eq:>20.3e} {h_eq:>18.3e}")
    if d_eq > 1e-4 or h_eq > 1e-4:
        fail.append("nonlinearity")
print()
print("  ** The column is CONSTANT because k^2 rho^2 = 1 at the break mode: the peak contrast is a")
print("     pure number times the observed amplitude and does not know the composition. **")
print("  Below equality the growth reverses -- in radiation domination aH = 1/|sigma| and Phi ∝")
print("  1/|sigma|, so delta ∝ |sigma| and falls to zero at the crunch.")
print("  ** SO LINEAR THEORY SURVIVES THE WHOLE PASSAGE WITH SIX ORDERS TO SPARE, and the margin is")
print("     read off the sky rather than assumed. **")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — ANISOTROPY")
print("=" * 78)
x = sp.Symbol('x', positive=True)
Sig = sp.Symbol('Sigma', positive=True)
s_ = sp.Symbol('s')
a_sh = sp.sqrt(2 * Sig * x)                       # a a' = Sigma  =>  a ∝ x^(1/2)
pot = sp.simplify(sp.diff(a_sh, x, 2) / a_sh)
roots = sp.solve(sp.Eq(s_ * (s_ - 1), sp.Rational(-1, 4)), s_)
print(f"  Shear enters (da/deta)^2 = B + A a - a^2 as + Sigma^2/a^2, which dominates as a -> 0.")
print(f"  Then a = {a_sh} ∝ x^(1/2) and a''/a = {pot}, with indicial roots {roots}.")
if roots != [sp.Rational(1, 2)]:
    fail.append("shear exponents")
print()
print(f"  {'crunch':>30} {'a ∝':>14} {'exponents':>14} {'monodromy':>18}")
for nm, ap, ex, mo in [("dust only", "sigma^2", "(-1, 2)", "diagonal"),
                       ("with radiation", "sigma", "(0, 1)", "2 pi/rho"),
                       ("** with ANY shear **", "sigma^(1/2)", "(1/2, 1/2)", "** degenerate **")]:
    print(f"  {nm:>30} {ap:>14} {ex:>14} {mo:>18}")
print()
print("  ** A shear-dominated crunch is a DIFFERENT SINGULAR POINT, with a logarithm at zeroth order")
print("     rather than at the first step -- so the whole mixing calculation would describe the")
print("     wrong background. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — WHAT EXCLUDES IT, AND WHAT REMAINS")
print("=" * 78)
print("  ** THE SHEAR IS NOT A FREE DATUM. **  At k = 0 the tensor equation is h'' + 2(a'/a)h' = 0,")
print("  so h' ∝ 1/a^2 and Sigma = a^2 h'/2 is CONSTANT: the Bianchi shear IS the long-wavelength")
print("  growing tensor mode, and bounding the tensor sector bounds it.")
print("  In the matter era h ∝ |sigma|^{-3}, so Sigma = (3/8) M^2 |sigma|^3 h, against a domination")
print("  threshold Sigma << M^2 rho^3/2 (where shear would beat radiation at equality):")
print()
# ** ⛭ THE 3/8 IS DERIVED HERE AND WAS PREVIOUSLY ONLY NARRATED (added r7083, node 66). **
#   `r7081+70.1`'s sentinel sweep classed this coefficient HELD: it sat in the print string above and
#   in the ratio below, and replacing it left this receipt exiting zero with nothing failing -- so the
#   paper stated a formula as the construction's own result and no receipt derived it.
#   ⇒ *** Derived from the corpus's OWN stated relations, each quoted here so a premise cannot move
#     silently: *** `A = 2M` (one bead, one integration constant); `a = A|sigma|^2/4` on the matter
#     leg, which is the relation `sec:composition` uses as `a_eq = A rho^2/4`; `Sigma = a^2 h'/2`,
#     constant at k = 0; and `h ∝ |sigma|^{-3}`, with the prime the derivative in the leg's own
#     variable -- consistent because `a ∝ sigma^2` is the marginally bound dust interior in conformal
#     time.  ** The coefficient is then forced: (1/4)^2 * 3 * (1/2) * 2^2 = 3/8. **
_s, _M, _C = sp.symbols('sigma M C', positive=True)
_A = 2 * _M                                   # A = 2M
_a = _A * _s**2 / 4                           # a = A sigma^2 / 4
_h = _C * _s**-3                              # h  ∝ |sigma|^-3
_Sigma = sp.simplify(_a**2 * sp.diff(_h, _s) / 2)
_want = -sp.Rational(3, 8) * _M**2 * _s**3 * _h          # the paper's form, signed by h' < 0
_ok38 = sp.simplify(_Sigma - _want) == 0
_coeff = sp.simplify(-_Sigma / (_M**2 * _s**3 * _h))
print(f"  DERIVED: Sigma = a^2 h'/2 with A = 2M, a = A|sigma|^2/4, h = C|sigma|^-3  ->  "
      f"coefficient {_coeff}, the stated 3/8: {_ok38}")
if not (_ok38 and _coeff == sp.Rational(3, 8)):
    fail.append("the 3/8 in Sigma = (3/8) M^2 |sigma|^3 h is not reproduced from A = 2M, "
                "a = A|sigma|^2/4, Sigma = a^2 h'/2 and h ∝ |sigma|^-3")
print()
P_T_pred = 4.722e-111                    # 144 pi (l_P/M_nariai)^2 rho^-6 on the CORRECTED
#   configuration (r6921): M_nariai = 4.17e52 kg and rho = 0.05451, both on the background the
#   distance data fix.  ** SCALED from the banked 4.796e-111 by the configuration's own ratio
#   (-1.53%), not recomputed from scratch: the banked value reproduces from its stated formula
#   only to ~0.5%, so it carries convention rounding a fresh evaluation would silently change. **
#   And the rho^-6 form OVERSTATES the sensitivity: rho^2 = 2 a_eq/M makes M^-2 rho^-6 =
#   M/(8 a_eq^3) identically, so P_T = 18 pi l_P^2 M / a_eq^3 with NO rho in it -- the 6x lever
#   on rho is cancelled by M^-2, and the amplitude is M/a_eq^3 alone.
print(f"  {'tensor amplitude granted':>46} {'h at equality':>16} {'Sigma / threshold':>20}")
for nm, hv in [("the OBSERVATIONAL CEILING (r < 0.032)", (2 / (3 * np.pi)) * np.sqrt(R_BOUND * AS_OBS)),
               ("** this construction's PREDICTED P_T **", (2 / (3 * np.pi)) * np.sqrt(P_T_pred))]:
    ratio = (3 / 8) * hv / 0.5
    print(f"  {nm:>46} {hv:>16.2e} {ratio:>20.2e}")
    if ratio > 1e-5:
        fail.append("shear bound")
print()
print("  ** SO EVEN GRANTING THE PROGENITOR THE LARGEST TENSOR AMPLITUDE THE SKY PERMITS, THE INDUCED")
print("     SHEAR IS SIX ORDERS BELOW TAKING OVER THE CRUNCH -- AND FIFTY-SIX ON THE PREDICTED ONE. **")
print()
print("  And a genuinely HOMOGENEOUS shear is not a perturbation of a closed ball at all: the S^3")
print("  tensor tower starts at L = 2 and has no k = 0 member, so it would be a change of background")
print("  class, FRW -> Bianchi IX.  The construction selects FRW by its matching -- the exterior is")
print("  Schwarzschild-de Sitter and the branch point IS its Nariai locus, spherically symmetric")
print("  throughout.  ** One may not drop the symmetry and keep the Nariai locus. **")
print()
print(f"  {'threat':>44} {'status':>32}")
for a_, b_ in [("nonlinearity, scalar", "CLOSED (1e-6)"),
               ("nonlinearity, tensor", "CLOSED (1e-6 at the ceiling)"),
               ("shear from the L >= 2 tensor tower", "CLOSED (1e-6 of threshold)"),
               ("homogeneous Bianchi shear", "not a perturbation at all")]:
    print(f"  {a_:>44} {b_:>32}")
print()
print("  ** WHAT REMAINS IS A SCOPE STATEMENT AND NOT AN OPEN QUESTION: the construction works in the")
print("     spherically symmetric class, and that class is selected by the exterior it matches to --")
print("     a premise of the construction rather than a gap in it. **")

print()
if fail:
    print("FAIL: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS")
sys.exit(0)
