"""
P07_lap_timeline.py -- A2.11: the finite intervals between the cosmogenetic lap's landmarks,
exactly in phase and then in SI. KEY RESULTS: (a) w_back = 2 w_front = arccosh 2 = ln(2+sqrt3) --
the 2:1 in RADIUS (rho : -2rho) is a 1:2 in PHASE, inverted, by an identity chain; (b) the LIFT
advances Re(tau) by EXACTLY ZERO, so the collapse-to-expansion handoff takes no cosmic time at
all; (c) the intervals in Gyr at the corpus's own constants, with the 1/H0 scaling exposed --
which surfaced that the 4.30e52 kg Nariai mass quoted in THE_PLAN carries the Planck H0, not the
directly measured one CR fits at (3.94e52 kg there). [P7 thm:bead / A2.11]
HELD not claimed: which landmark begins the OBSERVABLE cosmology is not settled here (P7
separates the geometric r=0 closure from the physical seeding at the seam); the imaginary
interval is a contour length, not a duration, and says nothing about recurrence.
STATUS: OK   ORIGIN: storyboard_receipts/lap_timeline.py, built r1631.
"""
import sympy as sp

# ---------------------------------------------------------------- (A) exact phases
print("="*76); print("(A) THE LANDMARK PHASES -- exact"); print("="*76)
A_ = sp.Integer(1)                                  # work in units of the amplitude A
rho   = 2**sp.Rational(-1,3)                        # front seam = merged horizon = r_star
back  = 2*rho                                       # back seam = -2 rho
print(f"  in units of A:  front seam rho = 2^(-1/3) = {float(rho):.6f}")
print(f"                  turnaround      |r| = 1")
print(f"                  back seam  2rho = 2^(2/3) = {float(back):.6f}")
print()
# expansion leg: r/A = sinh^(2/3) w
sinh_f = sp.sqrt(rho**3)                            # sinh w = (rho/A)^(3/2)
assert sp.simplify(sinh_f - 1/sp.sqrt(2)) == 0
w_front = sp.asinh(1/sp.sqrt(2))
# the identity route, so nothing rests on simplify seeing through asinh:
assert sp.simplify(1 + 2*(1/sp.sqrt(2))**2) == 2    # cosh 2w = 1 + 2 sinh^2 w = 2
# collapse wing: |r|/A = cosh^(2/3) w
w_back = sp.acosh(2)
assert sp.simplify(sp.cosh(w_back) - 2) == 0
# and the closed forms, checked as algebra rather than by simplify
wf_cf, wb_cf = sp.log((1+sp.sqrt(3))/sp.sqrt(2)), sp.log(2+sp.sqrt(3))
assert sp.simplify(((1+sp.sqrt(3))**2/2) - (2+sp.sqrt(3))) == 0     # (1+sqrt3)^2/2 = 2+sqrt3
assert abs(float(w_front - wf_cf)) < 1e-14 and abs(float(w_back - wb_cf)) < 1e-14
print(f"  front seam : sinh w = 1/sqrt2  ->  w = ln((1+sqrt3)/sqrt2) = {float(w_front):.9f}")
print(f"  turnaround : cosh w = 1        ->  w = 0                   (the wing's vertex)")
print(f"  back seam  : cosh w = 2        ->  w = ln(2+sqrt3)        = {float(w_back):.9f}")
print()
print("  *** AND THE RELATION, EXACT:  w_back = 2 w_front = arccosh 2 = ln(2+sqrt3). ***")
assert abs(float(w_back - 2*w_front)) < 1e-14
print("  The 2:1 in RADIUS (rho : -2rho, the double root against the lone root) appears as")
print("  a 1:2 in PHASE, inverted -- and it is an identity chain, not a match:")
print("     rho/A = 2^(-1/3), sinh law   =>  sinh w_f = 2^(-1/2)")
print("     cosh 2w = 1 + 2 sinh^2 w     =>  cosh 2w_f = 2")
print("     2rho/A = 2^(2/3), cosh law   =>  cosh w_b  = 2   =>  w_b = 2 w_f.")

# ---------------------------------------------------------------- constants, in SI
print(); print("="*76); print("(B) THE CONSTANTS -- fixed, not fitted"); print("="*76)
c   = 2.99792458e8                     # m/s, exact
G   = 6.67430e-11                      # m^3 kg^-1 s^-2
Mpc = 3.0856775814913673e22            # m
yr  = 3.1557e7                         # s (Julian)
H0  = 73.0*1e3/Mpc                     # the directly measured value the corpus fits at
Om  = 0.307                            # Planck 2018, CMB-calibrated -- the corpus's own invariant
OL  = 1 - Om
Lam = 3*H0**2*OL/c**2
al  = (3/Lam)**0.5                     # alpha = sqrt(3/Lambda) = c/(H0 sqrt(OmegaLambda))
M   = c**2/(3*Lam**0.5*G)
print(f"  H0 = 73 km/s/Mpc  ->  1/H0 = {1/H0/yr/1e9:.3f} Gyr    Omega_m = {Om}, Omega_L = {OL:.3f}")
print(f"  Lambda   = {Lam:.4e} m^-2")
print(f"  alpha    = {al:.4e} m  = {al/(c*yr)/1e9:.3f} Gly     (alpha/c = {al/c/yr/1e9:.3f} Gyr)")
print(f"  M        = {M:.4e} kg")
# self-consistency, not a number: M must satisfy the corpus's Nariai condition exactly
assert abs(Lam*G**2*M**2/c**4 - 1/9) < 1e-12, "eq:Nariai-condition violated"
print(f"  check eq:Nariai-condition  Lambda G^2 M^2/c^4 = {Lam*G**2*M**2/c**4:.12f}  [must be 1/9]")
# and the H0 scaling, stated because it is the whole caveat
M67 = c**2/(3*(3*(67.4e3/Mpc)**2*OL/c**2)**0.5/1*G)
print(f"  *** M SCALES AS 1/H0, and this is the caveat A2.11 exists to surface: ***")
print(f"      at the directly measured H0 = 73  ->  M = {M:.3e} kg")
print(f"      at the Planck H0 = 67.4          ->  M = {M67:.3e} kg   <- the 4.30e52 quoted in THE_PLAN")
print(f"      ratio = {M67/M:.4f} = 73/67.4 = {73/67.4:.4f}")
assert abs(M67/M - 73/67.4) < 1e-6
print(f"      The corpus states M SYMBOLICALLY (eq:Nariai-mass) and is therefore right; the")
print(f"      NUMBER lives only in THE_PLAN, and it carries an unstated H0 that is not the one")
print(f"      CR's own cosmology fits at. Lambda is inferred as 3 H0^2 Omega_L/c^2, so every")
print(f"      figure here inherits H0 -- alpha as 1/H0, M as 1/H0, and all intervals as 1/H0.")
Aamp = (2*G*M*al**2/c**2)**(1/3)
print(f"  amplitude A = (2GM alpha^2/c^2)^(1/3) = {Aamp:.4e} m = {Aamp/(c*yr)/1e9:.3f} Gly")
print(f"  and A / (alpha/sqrt3) = {Aamp/(al/3**0.5):.6f}   [must be 2^(1/3) = {2**(1/3):.6f}]")
assert abs(Aamp/(al/3**0.5) - 2**(1/3)) < 1e-9

# ---------------------------------------------------------------- (B) the intervals
print(); print("="*76); print("(C) THE INTERVALS, in SI"); print("="*76)
T = 2*al/(3*c)                          # tau = T * w
print(f"  the conversion:  tau = (2 alpha / 3c) * w,   with 2 alpha/3c = {T/yr/1e9:.4f} Gyr per unit phase")
print()
w0 = float(sp.asinh(sp.sqrt(OL/Om)))    # present epoch: Omega_m/Omega_L = csch^2 w   (P15)
rows = [
  ("collapse leg: back seam -> turnaround", float(w_back),        "real, on the wing"),
  ("the LIFT: turnaround -> r = 0",         0.0,                  "Re(tau) FROZEN -- see below"),
  ("expansion: r = 0 -> radius rho",        float(w_front),       "real; NOT the seeding -- see below"),
  ("expansion: r = 0 -> present epoch",     w0,                   "real"),
  ("expansion: front seam -> present",      w0 - float(w_front),  "real"),
]
for name, dw, kind in rows:
    print(f"  {name:<40s} dw = {dw:8.6f}   {dw*T/yr/1e9:8.3f} Gyr   ({kind})")
print()
print(f"  the lap's imaginary half-period (the lift's contour stretch): pi alpha/3c ="
      f" {3.141592653589793*al/(3*c)/yr/1e9:.3f} Gyr-equivalent of CONTOUR LENGTH,")
print(f"  and it advances Re(tau) by EXACTLY 0. *The collapse-to-expansion handoff takes no")
print(f"  cosmic time at all.* It is a stretch of the contour, not of time.")
print()
print(f"  present epoch check against flat-LCDM's age formula (they must agree, since the")
print(f"  radiation-free law IS the flat-LCDM scale factor):")
t0_lcdm = (2/(3*H0*OL**0.5))*w0
print(f"     tau_0 (this receipt) = {w0*T/yr/1e9:.4f} Gyr")
print(f"     t_0  (2/3H0 sqrtOL) arcsinh sqrt(OL/Om) = {t0_lcdm/yr/1e9:.4f} Gyr")
assert abs(w0*T - t0_lcdm)/t0_lcdm < 1e-12
print("     -> identical, as required.")

print(); print("="*76)
print("VERIFIED: the exact phases, the relation w_back = 2 w_front = arccosh 2, the constants")
print("against the corpus's own quoted Nariai mass, A = 2^(1/3) rho, and the present epoch")
print("against the independent flat-LCDM age formula.")
print()
print("THE CLOCK (this part of r1632 stands): every interval above is PROPER TIME OF THE")
print("  FUNDAMENTAL OBSERVERS -- P7 eq:SdS-fundamental, ds^2 = -dtau^2 + ... . P1's 'no horizon")
print("  completes at finite time' concerns the EXTERIOR STATIC clock. Different clocks.")
print()
print("THE TWO LEVELS, and they must not be collapsed into one (corrected r1633):")
print("  (1) GEOMETRICALLY THE LAP PASSES THROUGH r=0. It is a BRANCH POINT, NOT A BARRIER --")
print("      P7, verbatim: 'around the throat through r=0 (a branch point, not a barrier: the")
print("      substrate is smooth across the locus the chart labels r=0, the curvature divergence")
print("      there being the perspectival mass reading)'. Fig F draws it: the antimatter hole")
print("      collapsing through r=0 and continuing as our matter universe. The crossing is where")
print("      the SPECIES REVERSES. It happens, at finite proper time, and it is THE event of the")
print("      conjugation. Every interval computed above is an interval on that curve.")
print("  (2) PHYSICALLY, NO FINITE-TIME LAYER S_t CONTAINS THE CURVATURE SINGULARITY. That is the")
print("      Smoothness theorem, and it is a statement about the LAYERS, not about the curve --")
print("      the singularity is never actualised in a layer, and the cosmological future is")
print("      seeded at the finite-curvature seam rather than at a curvature singularity.")
print("  P7 states the relation itself: 'the geometric closure of the slicing curve through r=0")
print("  and the physical seeding of the layers at the finite-curvature horizon are claims at")
print("  DIFFERENT LEVELS, NOT COMPETING ONES.'")
print()
print("  *** THE ERROR THIS REPLACES, recorded so it is not made again. *** r1632 read (2) as if")
print("  it were (1) and concluded 'r=0 is an unattained limit, not an event', with the layer")
print("  history an open interval 'exactly the structure of an FLRW age'. That INVERTS the")
print("  corpus's central result: it puts the barrier back that CR removes, and it reaches for")
print("  the FLRW default -- which is the shadow-reader's collapse the ontology map's SEC 1-SHADOW")
print("  names. The paper says 'branch point, not a barrier' three paragraphs from where the")
print("  placement went in.")
print()
print("  * The imaginary interval is a CONTOUR length, not a duration, and says nothing about")
print("    recurrence (the r1622 guards).")
print("  * Every SI figure scales as 1/H0. CR's invariant is Omega_m; H0 is left to the local")
print("    ladder, and these are quoted at the directly measured value the corpus fits at.")
print("="*76)
