"""C11 — THE EARLY ISW.  The last named piece.
CONFIRMATION 2/4 -- the corpus settles the input, in its own voice:
  'radiation, like matter, is inherited content read off that clock, NOT A TERM THAT SOURCES THE
   RATE, and there is no radiation-dominated era.  The objection that a perturbing radiation fluid
   "must gravitate and so alter the rate" is a CATEGORY ERROR against a construction that reads the
   rate LEFTWARD: the rate is set, and the fluid's energy is among the contents the set rate carries.'
So on L1 the background rate is matter + Lambda, full stop.  The ISW is INT (Phi' + Psi') d eta, and
the question is therefore entirely about whether Phi evolves on THAT background near recombination.
ORIGIN: storyboard_receipts/C11_early_isw.py -- registered r2376 (c54); edit the origin, not this copy."""
import sympy as sp, numpy as np
from scipy.integrate import quad, solve_ivp
print("="*80); print("C11 — DOES Phi EVOLVE NEAR RECOMBINATION?"); print("="*80)
a=sp.Symbol('a', positive=True)
print("""
STEP 1 — THE POTENTIAL ON A MATTER-DOMINATED BACKGROUND.  DERIVE, do not quote.
  In conformal time, for a fluid with w = c_s^2 = 0 (dust):
        Phi'' + 3 H (1+w) Phi' + [ ... w k^2 ... ] Phi = 0   ->   Phi'' + 3 H Phi' = 0
  with H = a'/a.  On a matter background a ~ eta^2, so H = 2/eta and
        Phi'' + (6/eta) Phi' = 0   =>   Phi = C1 + C2 eta^-5 .
""")
eta=sp.Symbol('eta', positive=True); Phi=sp.Function('Phi')
sol=sp.dsolve(sp.Eq(sp.diff(Phi(eta),eta,2) + (6/eta)*sp.diff(Phi(eta),eta), 0), Phi(eta))
print(f"   sympy: {sol}")
print("   *** THE GROWING MODE IS CONSTANT.  On a matter-dominated background Phi does not evolve,")
print("       so Phi' = 0 and THERE IS NO ISW CONTRIBUTION. ***")
print("""
STEP 2 — SO THE EARLY ISW EXISTS ONLY BECAUSE OF THE RADIATION TERM IN THE BACKGROUND.
  In LambdaCDM, rho_r/rho_m ~ 0.32 at recombination, so the background is not pure matter; Phi is
  still decaying from its radiation-era value, Phi' != 0, and the line-of-sight integral picks up
  power near the first peaks.  *** THAT IS THE EARLY ISW. ***
  On CR's L1 the background is matter + Lambda with NO radiation term -- the corpus's own sentence
  above -- and Lambda is utterly negligible at z ~ 1100:
""")
Om,OL=0.307,0.693; z_rec=1100.0; a_rec=1/(1+z_rec)
print(f"     at a_rec = {a_rec:.6f}:  Omega_m a^-3 = {Om*a_rec**-3:.4e},  Omega_L = {OL:.4f}")
print(f"     ratio Lambda/matter = {OL/(Om*a_rec**-3):.3e}  -- NINE orders down.")
print("   *** SO CR's L1 BACKGROUND AT RECOMBINATION IS PURE MATTER TO NINE DIGITS, Phi IS")
print("       CONSTANT, AND CR HAS NO EARLY ISW. ***")
print("""
STEP 3 — HOW BIG IS THE THING CR DOES NOT HAVE?  Estimate it from the LambdaCDM potential decay.
  On a matter+radiation background the growing-mode potential falls from its radiation-era value to
  9/10 of it deep in matter domination; the residual decay still running at recombination is what
  drives the early ISW.  Integrate the fractional decay across recombination:
""")
Or=Om*0.3214*a_rec
def Phi_of_a(av):
    # standard growing-mode interpolation across equality: Phi(y)/Phi_rad with y = a/a_eq
    y=av/(Or/Om)
    return (9/10)*( (16*np.sqrt(1+y)+9*y**3+2*y**2-8*y-16)/(10*y**3) )
y_rec=a_rec/(Or/Om)
print(f"   a_eq = Or/Om = {Or/Om:.4e},  y_rec = a_rec/a_eq = {y_rec:.3f}")
for lab,av in [("at equality", Or/Om), ("at recombination", a_rec), ("deep matter (y=100)", 100*Or/Om)]:
    print(f"     {lab:22s} Phi/Phi_rad = {Phi_of_a(av):.5f}")
d=(Phi_of_a(a_rec)-Phi_of_a(100*Or/Om))/Phi_of_a(100*Or/Om)
print(f"   -> at recombination Phi is still {100*d:+.2f}% above its asymptote: THAT residual decay")
print("      is what LambdaCDM's early ISW integrates and CR does not have.")
print("="*80)

print("\n" + "="*80)
print("STEP 4 — AND WHERE DOES THAT MISSING EFFECT SIT?  This decides whether it matters.")
print("="*80)
print("""
  The early ISW adds power NEAR THE FIRST PEAKS -- it is a large-scale effect, concentrated around
  l ~ 200, and it dies away well before the damping tail begins.  The damping deficit computed in
  C10 is the opposite: negligible below l ~ l_D/2 and growing beyond it.
  *** SO THE TWO DIFFERENCES LIVE AT OPPOSITE ENDS OF THE SPECTRUM AND DO NOT INTERFERE. ***
""")
print("  AND THE FIRST PEAK IS WHERE THE NORMALISATION IS ANCHORED.")
print("   P15: A_s is INHERITED -- 'the progenitor supplies A_s, n_s, rho_r/rho_m, the abundances'.")
print("   The overall amplitude is therefore not predicted by the construction; it is measured, as")
print("   eta is in flat LambdaCDM.")
print("   *** A FEW-PERCENT DEFICIT AT THE FIRST PEAK IS ABSORBED BY A_s, WHICH IS INHERITED ANYWAY. ***")
print("   The damping deficit is NOT so absorbed: it is a SHAPE change at high l, and rescaling A_s")
print("   to fix the first peak would make the tail worse, not better.")
print("""
  *** SO THE LAST NAMED ESCAPE CLOSES, AND IT CLOSES WITHOUT RESCUING ANYTHING. ***
  CR has no early ISW; the effect it lacks is a few percent, sits at the first peak, and is degenerate
  with an amplitude the framework does not predict.  It therefore CANNOT offset the damping
  signature, which lives at high l and changes the SHAPE.
""")
print("="*80)
print("RESULT C11: the early ISW is absent on L1 -- Phi is constant on a pure-matter background and")
print("  the corpus's own leftward reading puts radiation in the CONTENT, not the rate.  The missing")
print("  effect is ~4% in the potential at recombination, concentrated at the first peak, and")
print("  degenerate with the inherited A_s.")
print("  *** THE DAMPING SIGNATURE STANDS AS THE FRAMEWORK'S ONE SHAPE-LEVEL EXPOSURE, and the last")
print("      named term that might have redistributed it does not. ***")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  This receipt printed a sympy solution, a nine-orders ratio and a
# potential-decay estimate, and asserted none of them.  CR_cosmology.tex
# sec:envelope-consequence cites it for exactly those three: "on a pure-matter background the
# growing mode is constant, Phi'' + 3 H Phi' = 0 giving Phi = const, and this cosmology's rate at
# z ~ 1100 is MATTER-DOMINATED TO NINE ORDERS, the substrate term being utterly negligible
# there ... in the latter the potential is still SOME FOUR PER CENT above its asymptote at
# recombination".
#   (1) the sympy solution really is C1 + C2 eta^-5 -- a constant growing mode and a mode that
#       decays as the fifth power, so Phi' = 0 and there is no ISW.  Asserted as: it solves the
#       ODE, its eta -> oo limit is eta-free, and the remainder times eta^5 is eta-free;
#   (2) the nine orders, pinned to the 1.6913e-09 the receipt prints;
#   (3) the residual decay LambdaCDM still carries at recombination, pinned to +3.80% -- the
#       paper's "some four per cent" -- together with the three Phi/Phi_rad values it is built
#       from, so a change to the interpolation formula fails here.
# ============================================================================================
_rhs = sol.rhs
assert sp.simplify(sp.diff(_rhs, eta, 2) + (6/eta)*sp.diff(_rhs, eta)) == 0, \
    "the sympy solution does not satisfy Phi'' + (6/eta) Phi' = 0"
_asym = sp.limit(_rhs, eta, sp.oo)
assert eta not in _asym.free_symbols, \
    f"the growing mode is NOT constant: its eta -> oo limit is {_asym}"
_decay = sp.simplify((_rhs - _asym)*eta**5)
assert eta not in _decay.free_symbols, \
    f"the second mode does not fall as eta^-5: (Phi - const) eta^5 = {_decay}"
# (2) nine orders down: the substrate term against matter at recombination.
_lam_over_mat = OL/(Om*a_rec**-3)
assert abs(_lam_over_mat - 1.6913e-09) < 1.0e-13, \
    f"Lambda/matter at recombination = {_lam_over_mat:.4e}, expected 1.6913e-09"
assert _lam_over_mat < 1.0e-8, \
    "the substrate term is no longer nine orders down -- 'pure matter at recombination' has drifted"
# (3) the LambdaCDM residual the early ISW integrates and this cosmology lacks.
assert abs(Phi_of_a(Or/Om) - 0.86647) < 1.0e-5, f"Phi/Phi_rad at equality = {Phi_of_a(Or/Om):.5f}"
assert abs(Phi_of_a(a_rec) - 0.84261) < 1.0e-5, f"Phi/Phi_rad at recombination = {Phi_of_a(a_rec):.5f}"
assert abs(Phi_of_a(100*Or/Om) - 0.81174) < 1.0e-5, \
    f"Phi/Phi_rad deep in matter = {Phi_of_a(100*Or/Om):.5f}, expected 0.81174"
assert abs(y_rec - 3.111) < 0.001, f"y_rec = a_rec/a_eq = {y_rec:.3f}, expected 3.111"
assert abs(100*d - 3.80) < 0.01, \
    (f"the LambdaCDM potential is {100*d:+.2f}% above its asymptote at recombination; "
     f"CR_cosmology.tex sec:envelope-consequence says 'some four per cent'")
assert 100*d > 0, "the potential no longer sits ABOVE its asymptote -- the residual decay reversed"
print(f"GATE C11 (r2376+c54.160): Phi = {_asym} + {_decay}/eta^5 (growing mode constant); "
      f"Lambda/matter = {_lam_over_mat:.4e}; LambdaCDM residual {100*d:+.2f}% -- all pinned.")
