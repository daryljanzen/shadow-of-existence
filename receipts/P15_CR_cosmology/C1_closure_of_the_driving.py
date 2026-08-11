"""C1-CLOSURE — DOES THE ACOUSTIC OSCILLATOR CLOSE IN ELEMENTARY TERMS ON CR's COLLAPSE LEG?
CONFIRMATION 4 first — WHICH background.  The corpus is specific and I must not substitute:
  L2 (where the driving lives) = 'the leaf's local rate, ORDINARY FRIEDMANN, radiation GRAVITATING
  NORMALLY, on the progenitor's collapse excursion' -- and P16: on the cooling leg |H| = sqrt(8 pi G
  rho/3), 'identical to standard BBN at every temperature in the window, differing from an expanding
  radiation era ONLY BY THE SIGN OF adot'.
  So L2 is a STANDARD Friedmann background, contracting.  NOT the sinh^{2/3} law -- that is L1.
ORIGIN: storyboard_receipts/C1_closure_of_the_driving.py -- registered r2376 (c54); edit the origin, not this copy."""
import sympy as sp
print("="*80); print("C1 — THE MODE EQUATION ON L2"); print("="*80)
eta,k,x=sp.symbols('eta k x', positive=True)
print("""
STEP 1 — WHERE ON THE LEG DOES THE DRIVING HAPPEN?  This decides the background.
  P15: the modes are SUB-HORIZON AT THE SEAM and 'each mode's driving is COMPLETE on the collapse
  side'.  At the seam rho_r/rho_m ~ 2.  But the driving is not done AT the seam -- it is done BY
  then, i.e. DEEPER on the leg, hotter and earlier, where P16 puts the peak at ~10^2 MeV with total
  dissociation.  *** DEEP ON THE COLLAPSE LEG RADIATION DOMINATES OVERWHELMINGLY. ***
  So the driving background is a RADIATION-DOMINATED Friedmann leg, contracting.
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
print("STEP 3 — AND CR's LEG IS ITS TIME-REVERSE, WHICH IS THE SAME FUNCTION.")
print("   P16: the collapse leg differs from an expanding radiation era ONLY BY THE SIGN OF adot.")
print("   Under eta -> -eta the equation Psi'' + (4/eta) Psi' + (k^2/3) Psi = 0 is INVARIANT:")
Pm=P.subs(x,-x)
print(f"     Psi(-x) = {sp.simplify(Pm)}")
print(f"     and Psi(-x) - Psi(x) = {sp.simplify(Pm - P)}   <- the solution is EVEN in x")
print("   *** SO THE POTENTIAL IS LITERALLY THE SAME FUNCTION ON THE CONTRACTING LEG. Not merely")
print("       equal in Fourier magnitude at omega=1 -- the SAME CLOSED FORM, pointwise. ***")

print("\n" + "="*80)
print("STEP 4 — WHERE MY RESULT AND P15's CAUTION MEET.  Held carefully, not smoothed.")
print("="*80)
print("""
  P15 says two things that must both stand:
    (a) 'its driving does not live on an expanding radiation era... it lives on the CONTRACTING side
         --- the progenitor's radiation-comparable collapse phase, whose potential evolution is the
         Friedmann TIME-REVERSE of an expanding radiation era'  -- and
    (b) 'the same radiation-free rate that enlarges r_D also reshapes the high-ell driving envelope
         (removing the radiation-driving boost that sets the LambdaCDM peaks), so CR's high-ell
         spectrum is governed by SHORT-WAVELENGTH COLLAPSE-PHASE DRIVING THAT HAS NOT BEEN COMPUTED.'

  STEP 2-3 SETTLE THE FUNCTION AND NOT THE SAMPLING.  What is now established:
    * the driving potential on a radiation-dominated Friedmann leg is ELEMENTARY, verified exactly:
      Psi = 3 Psi_i (sin x - x cos x)/x^3, x = k eta / sqrt3 ;
    * that function is EVEN in x, so the contracting leg carries THE SAME CLOSED FORM POINTWISE --
      which is stronger than the Fourier-magnitude equality P15 buys at omega = 1, and consistent
      with it.
  *** SO THE FUNCTION IS NOT THE UNCOMPUTED THING. ***

  WHAT IS UNCOMPUTED IS WHICH PART OF IT EACH MODE SAMPLES.  A mode's driving is the stretch of
  Psi(x) it experiences while INSIDE the horizon, and the horizon history differs:
    - LambdaCDM: comoving Hubble radius GROWS through the radiation era; modes ENTER, high-ell first,
      and each is driven from its entry to equality.  The 'radiation-driving boost' is that entry-to-
      equality stretch.
    - CR's leg: the corpus's own sequence is INFALL (contracting) -> PEAK -> TURNAROUND -> COOLING
      LEG (re-expanding) -> seam.  So the comoving Hubble radius SHRINKS, reaches a minimum at
      turnaround, then GROWS again -- and a mode can EXIT and RE-ENTER on one leg.
  *** THAT is the uncomputed object, and it is not a transfer function: it is a HORIZON-CROSSING
      HISTORY on a non-monotonic Hubble radius, deciding the limits of an integral whose integrand
      is already in closed form. ***
""")
print("  AND IT SHARPENS THE OPEN ITEM RATHER THAN CLOSING IT:")
print("    before: 'the high-ell driving envelope has not been computed' -- shape unknown, and a")
print("            Boltzmann transfer implied.")
print("    after : the integrand is elementary and known; what is owed is the horizon-crossing")
print("            history across infall-peak-turnaround-cooling, which fixes each mode's limits.")
print("  *** A CLOSED-FORM INTEGRAND WITH UNKNOWN LIMITS IS A DIFFERENT AND MUCH SMALLER PROBLEM ***")
print("  *** THAN AN UNKNOWN TRANSFER FUNCTION -- and it is the corpus's own bead geometry that")
print("      supplies the limits, not a code. ***")
print("="*80)

# ============================================================================================
# GATE — r2376+c54.160.  Added because this receipt printed its whole argument and asserted
# nothing: its OK certified only that Python exited zero.  Each check below is one of C1's own
# claims, and each is written so that a change to the derivation makes it FAIL.
#   (1) EXACTNESS — the printed "substituted into the ODE it returns: 0" is now a gate;
#   (2) REGULARITY — the x -> 0 limit is Psi_i, not a divergence;
#   (3) EVENNESS — Psi(-x) - Psi(x) = 0, which is the claim CR_cosmology.tex sec:envelope cites
#       this receipt for ("which is EVEN in x -- so the contracting leg carries the same closed
#       form pointwise").
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
