# NOTE (r147): the COMPUTATION below stands (E=1 cosmology, checks 0) -- it is the flat
# comoving (E=1/PG) clock's dynamics = flat-LCDM, grounded in operator-paper sec:cosmology
# (prop:cosmo). Its FRAMING ("frozen constraint with an open deparametrization knot") is
# RETRACTED: the canonical content is the DISSOLUTION (cosmology paper Axiom-level remark;
# canonical_time.tex sec:two-readings / sec:selection) -- the deparametrization is standard,
# the move is the selection, there is no knot. See notebook v2 §3 (r147 rework).
import sympy as sp

print("="*78)
print("SdS canonical quantization — STEP 1: the cosmological member's canonical")
print("structure from the E=1 substrate congruence, computed IN the construction")
print("(SdS metric), not a flat-FLRW model with an added dust clock.")
print("="*78)

r, tau, M, al, E, pr, pt = sp.symbols('r tau M alpha E p_r p_t', positive=True)
f = 1 - 2*M/r - r**2/al**2     # the construction's f(r); alpha=sqrt(3/Lambda)

print("\n[0] The construction (Paper 3): f(r) = 1 - 2M/r - r^2/alpha^2,  alpha^2 = 3/Lambda.")
print("    Cosmological member: r timelike (Nariai). Fundamental observers = the E=1")
print("    marginally-bound radial geodesic congruence (= Painleve-Gullstrand comoving).")

# --- radial timelike geodesic in the SdS static chart, computed in the metric ---
# ds^2 = -f dt^2 + dr^2/f ; mass-shell g^{mn}p_m p_n = -1 ; p_t = -E conserved.
# g^{tt} = -1/f, g^{rr} = f.
print("\n[1] Radial timelike geodesic in SdS (mass-shell, computed in the metric):")
massshell = -pt**2/f + f*pr**2 + 1     # = 0 ; pt = -E
print("    -E^2/f + f p_r^2 + 1 = 0  =>  solve for (dr/dtau):")
# dr/dtau = dr/dproper = g^{rr} p_r = f p_r ; and from mass-shell solve p_r^2
pr2 = sp.solve(massshell.subs(pt,-E), pr**2)[0]
rdot2 = sp.simplify(f**2 * pr2)                    # (dr/dtau)^2 = (f p_r)^2 = f^2 p_r^2
print("    (dr/dtau)^2 =", sp.simplify(rdot2), "  = E^2 - f")
rdot2_E1 = sp.simplify(rdot2.subs(E,1))
print("    E=1 (marginally bound):  (dr/dtau)^2 =", rdot2_E1)
master = 2*M/r + r**2/al**2
print("    MASTER EQUATION check  (dr/dtau)^2 - (2M/r + r^2/alpha^2) =",
      sp.simplify(rdot2_E1 - master), "   (0 = matches ledger E=1 master eqn)")

# --- the reduced cosmological "energy" form: 1/2 rdot^2 + V(r) = 0 ---
print("\n[2] Reduced cosmological form (areal radius r = the scale, tau = cosmic time):")
V = -M/r - r**2/(2*al**2)
print("    Write (dr/dtau)^2 = 2M/r + r^2/alpha^2 as  (1/2)(dr/dtau)^2 + V(r) = 0,")
print("    V(r) = -M/r - r^2/(2 alpha^2)  [matter term -M/r, Lambda term -r^2/2alpha^2].")
print("    Check 2*(-V) - (2M/r + r^2/alpha^2) =", sp.simplify(2*(-V) - master))

# --- Hamiltonian constraint (the frozen / WDW form), p_r = dr/dtau ---
P = sp.Symbol('P', real=True)   # momentum conjugate to r in the reduced model
Hc = sp.Rational(1,2)*P**2 + V
print("\n[3] Reduced Hamiltonian CONSTRAINT (p_r=P conjugate to scale r):")
print("    H_c = (1/2)P^2 + V(r) = (1/2)P^2 - M/r - r^2/(2 alpha^2)  ~  0   (mass-shell)")
print("    Hamilton: dr/dtau = dH_c/dP = P  ;  on-shell H_c=0 => P^2 = 2M/r + r^2/alpha^2,")
print("    reproducing the master equation. This is the FROZEN (constraint) form.")

# --- verify the sinh^{2/3} trajectory solves the master equation ---
print("\n[4] Does r(tau) = (2 M alpha^2)^(1/3) sinh^{2/3}(3 tau / 2 alpha) solve it?")
A = (2*M*al**2)**sp.Rational(1,3)
rtau = A*sp.sinh(3*tau/(2*al))**sp.Rational(2,3)
lhs = sp.simplify(sp.diff(rtau,tau)**2)
rhs = sp.simplify((2*M/rtau + rtau**2/al**2))
print("    (dr/dtau)^2 - (2M/r + r^2/alpha^2) =", sp.simplify(lhs-rhs),
      "  (0 => exact)")

# --- Friedmann / flat-LCDM reading ---
print("\n[5] Friedmann reading:  H^2 = (rdot/r)^2 = 2M/r^3 + 1/alpha^2")
H2 = sp.simplify(master/r**2)
print("    (rdot/r)^2 =", H2, " = 2M/r^3 + Lambda/3   (1/alpha^2 = Lambda/3).")
print("    matter:  2M/r^3  (dust, ~ a^-3, the geometry's OWN M = the bend, not added dust)")
print("    dark energy:  1/alpha^2 = Lambda/3.   FLAT LCDM, no curvature term.")

print("\n" + "="*78)
print("WHERE THE FROZEN CONSTRAINT MEETS THE OPEN PART (stated, not papered over):")
print("="*78)
print("""
 - Established here, in the construction: the cosmological member's reduced
   canonical object is the constraint H_c = (1/2)P^2 - M/r - r^2/(2 alpha^2) ~ 0,
   whose Hamilton flow is exactly the E=1 master equation and whose solution is
   the sinh^{2/3} flat-LCDM law. Matter (2M/r^3) and Lambda (1/alpha^2) are the
   geometry's own; nothing is tuned (Nariai fixes M by alpha).

 - This is the FROZEN form (H_c ~ 0), the minisuperspace Wheeler-DeWitt object.
   ADM-7 turned it into a TRUE Hamiltonian by adding a Brown-Kuchar DUST clock
   (H_grav + H_dust ~ 0, solve for p_dust): right deparametrization STRUCTURE,
   but the dust clock and flat-FLRW were the 'wrong model' the ledger flags.

 - The SdS frontier (the [reach], ready-in-principle not done): CR's clock is
   NOT an added dust field but the SUBSTRATE'S E=1 congruence, which the corpus
   holds to be an ABSOLUTE foliation (ontologically fixed, not gauge). The exact
   technical task is to realise the deparametrization with THAT intrinsic clock:
   identify, within the construction, the variable conjugate to the absolute
   cosmic time that solves H_c for a true tau-Hamiltonian i d/dtau Psi = H_phys Psi,
   with no field added by hand. The frozen H_c above is the thing to deparametrize;
   the substrate clock is what must do it.

 - Held discipline: the within-geometry S_3 (description groupoid) is GAUGE, a
   symmetry any quantization must represent, not a spectrum (that route is dead).
   Operator ordering of P^2 and self-adjointness on r>0 are genuine, unsettled.
""")
