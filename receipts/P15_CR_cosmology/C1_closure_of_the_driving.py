"""C1-CLOSURE — DOES THE ACOUSTIC OSCILLATOR CLOSE IN ELEMENTARY TERMS ON CR's DRIVING LEG?
WHICH background.  The driving lives on the leaf's local rate, ordinary Friedmann with radiation
  gravitating normally -- the cooling leg, re-expanding from the branch point, on which P16 runs a
  standard nucleosynthesis.  Every mode leaves the branch point frozen (P15 Prop. subhorizon) and
  re-enters on this leg, so the driving background is a STANDARD radiation-dominated Friedmann leg,
  expanding.  NOT the sinh^{2/3} law -- that is the stacking rate.  The closed form found below is
  EVEN in x, so a contracting radiation leg would carry it identically.
ORIGIN: storyboard_receipts/C1_closure_of_the_driving.py -- registered r2376 (c54); edit the origin, not this copy."""
import sympy as sp
print("="*80); print("C1 — THE MODE EQUATION ON L2"); print("="*80)
eta,k,x=sp.symbols('eta k x', positive=True)
print("""
STEP 1 — WHERE ON THE LEG DOES THE DRIVING HAPPEN?  This decides the background.
  P15: every mode is outside the horizon at the branch point and back inside it by the seam, where
  rho_r/rho_m ~ 2.  The driving is the re-entry between the two -- early on the re-expanding leg,
  near the branch point, where the radiation term is constant while the others vanish (C3).
  *** THERE RADIATION DOMINATES OVERWHELMINGLY. ***
  So the driving background is a RADIATION-DOMINATED Friedmann leg, expanding from the branch point.
""")
print("STEP 2 — AND THE RADIATION-ERA POTENTIAL IS ELEMENTARY. Derive it, do not quote it.")
Psi=sp.Function('Psi')
# radiation era, conformal time: a ~ eta ; the potential obeys
#   Psi'' + (4/eta) Psi' + (k^2/3) Psi = 0
ode=sp.Eq(sp.diff(Psi(eta),eta,2) + (4/eta)*sp.diff(Psi(eta),eta) + k**2*Psi(eta)/3, 0)
sol=sp.dsolve(ode, Psi(eta))
print("   radiation-era potential equation:  Psi'' + (4/eta) Psi' + (k^2/3) Psi = 0")
print("   sympy solves it:")
print("    ", sp.simplify(sol.rhs))
print()
print("   -> spherical Bessel of order one, which IS elementary:")
j1=sp.simplify(sp.sin(x)/x**2 - sp.cos(x)/x)
print(f"      j_1(x) = sin(x)/x^2 - cos(x)/x = {j1}")
print("   and the standard regular solution Psi = 3 Psi_i (sin x - x cos x)/x^3 with x = k eta/sqrt3:")
Psii=sp.Symbol('Psi_i')
P=3*Psii*(sp.sin(x)-x*sp.cos(x))/x**3
chk=sp.simplify(sp.expand(( sp.diff(P.subs(x,k*eta/sp.sqrt(3)),eta,2)
      + (4/eta)*sp.diff(P.subs(x,k*eta/sp.sqrt(3)),eta)
      + k**2*P.subs(x,k*eta/sp.sqrt(3))/3 )))
print(f"      substituted into the ODE it returns: {chk}   <- exact solution, verified")
print(f"      and the limit x->0: {sp.limit(P,x,0)}  (regular, = Psi_i)")
print("""
  *** SO THE RADIATION-ERA DRIVING POTENTIAL IS ELEMENTARY IN CLOSED FORM: sin x - x cos x over x^3.
      No Boltzmann integration is needed to have it. ***
""")
print("STEP 3 — AND THE TIME-REVERSED LEG CARRIES THE SAME FUNCTION.")
print("   A contracting radiation leg differs from an expanding one ONLY BY THE SIGN OF adot.")
print("   Under eta -> -eta the equation Psi'' + (4/eta) Psi' + (k^2/3) Psi = 0 is INVARIANT:")
Pm=P.subs(x,-x)
print(f"     Psi(-x) = {sp.simplify(Pm)}")
print(f"     and Psi(-x) - Psi(x) = {sp.simplify(Pm - P)}   <- the solution is EVEN in x")
print("   *** SO THE POTENTIAL IS LITERALLY THE SAME FUNCTION ON EITHER LEG. Not merely")
print("       equal in Fourier magnitude at omega=1 -- the SAME CLOSED FORM, pointwise. ***")

print("\n" + "="*80)
print("STEP 4 — WHAT IS SETTLED AND WHAT IS LEFT TO THE LIMITS.")
print("="*80)
print("""
  The function is settled: on a radiation-dominated Friedmann leg the driving potential is
  Psi = 3 Psi_i (sin x - x cos x)/x^3, x = k eta / sqrt3, exact and regular, taking the frozen value
  Psi_i at the branch point; and it is EVEN in x, so either leg carries the same closed form pointwise
  -- stronger than the Fourier-magnitude equality P15 states at omega = 1, and consistent with it.
  What each mode samples of it is set by its horizon-crossing history: exit on the infall, where
  aH -> infinity at the branch point, and re-entry on the re-expanding leg.  Those limits are C2's
  and the map is C3's; C4 assembles the envelope.
""")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  Added because this receipt printed its whole argument and asserted
# nothing: its OK certified only that Python exited zero.  Each check below is one of C1's own
# claims, and each is written so that a change to the derivation makes it FAIL.
#   (1) EXACTNESS — the printed "substituted into the ODE it returns: 0" is now a gate;
#   (2) REGULARITY — the x -> 0 limit is Psi_i, not a divergence;
#   (3) EVENNESS — Psi(-x) - Psi(x) = 0, which is the claim CR_cosmology.tex sec:envelope cites
#       this receipt for ("which is EVEN in x -- so a contracting radiation leg would carry the
#       same closed form pointwise").
#   (4) PIN — the closed form evaluated at x = 1/sqrt3, the horizon-entry phase.  C4 carries this
#       same number into the driving amplitude Psi(1/sqrt3)/2, which the paper quotes.  Pinning it
#       here means a change to C1's closed form breaks this gate before it can move C4 silently.
# ============================================================================================
assert sp.simplify(chk) == 0, f"Psi is NOT an exact solution of the radiation-era ODE: got {chk}"
assert sp.simplify(sp.limit(P, x, 0) - Psii) == 0, "Psi is not regular at x->0 with limit Psi_i"
assert sp.simplify(Pm - P) == 0, f"Psi is NOT even in x: Psi(-x)-Psi(x) = {sp.simplify(Pm - P)}"
_psi_entry = float(P.subs([(Psii, 1), (x, 1/sp.sqrt(3))]))
assert abs(_psi_entry - 0.967061) < 1.0e-5, \
    f"Psi(1/sqrt3)/Psi_i = {_psi_entry:.6f}, receipt/paper value 0.967061"
assert abs(_psi_entry/2 - 0.483531) < 1.0e-5, \
    f"driving amplitude Psi(1/sqrt3)/2 = {_psi_entry/2:.6f}, C4/paper value 0.483531"
print("GATE C1 (r2376+c54.160): exact, regular, EVEN; Psi(1/sqrt3) = "
      f"{_psi_entry:.6f}, amplitude {_psi_entry/2:.6f} -- all pinned.")
