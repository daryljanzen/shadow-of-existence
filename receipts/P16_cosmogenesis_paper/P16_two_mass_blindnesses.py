"""
P16_two_mass_blindnesses.py -- the corpus's TWO mass-independence results at the collapse
seam (the perspectival Kretschmann scalar at fixed proper interval; the infall energy per
nucleon at the horizon) share their STRUCTURE and not their derivation. Both are readings
referred to a marker the collapse itself defines, both lose the blindness at fixed areal
radius. Held not claimed: neither implies the other. [P16 cosmogenesis_paper sec:peak]
STATUS: OK   ORIGIN: storyboard_receipts/two_mass_blindnesses.py, built r1616.
"""
import sympy as sp

M, al, tt, r, mN = sp.symbols('M alpha tautilde r m_N', positive=True)

print("="*74)
print("(A) CURVATURE, at the collapse's own marker vs an external one")
print("="*74)
# the bead's outward law (P8 prop:cosmo / P7): r^3 = 2 M alpha^2 sinh^2(3 tau/2 alpha)
r_of_tau = (2*M*al**2)**sp.Rational(1,3) * sp.sinh(3*tt/(2*al))**sp.Rational(2,3)
K_persp = 48*M**2/r_of_tau**6
K_near = sp.simplify(sp.limit(K_persp*tt**4, tt, 0))
print(f"  at fixed proper interval:  K*tau^4 -> {K_near}   (M absent: {M not in K_near.free_symbols})")
print(f"                             alpha absent: {al not in K_near.free_symbols}")
K_at_r = sp.simplify(48*M**2/r**6)
print(f"  at fixed areal radius r :  K = {K_at_r}   (M present: {M in K_at_r.free_symbols})")
assert M not in K_near.free_symbols and al not in K_near.free_symbols
assert M in K_at_r.free_symbols
# and the bookkeeping that buys it
expo = sp.simplify(sp.log(r_of_tau.subs(tt,1)/ (2*al**2)**sp.Rational(1,3) / sp.sinh(sp.Rational(3,2)/al)**sp.Rational(2,3), M))
print(f"  the exponent that buys it: r ~ M^(1/3), so r^6 ~ M^(6/3) = M^2, cancelling 48M^2 exactly")

print()
print("="*74)
print("(B) THERMAL, at the collapse's own marker vs an external one")
print("="*74)
G, c = sp.symbols('G c', positive=True)
R_s = 2*G*M/c**2
# specific infall energy (Newtonian readout of the convergence, as P16 uses it): GM/R
E_at_horizon = sp.simplify(G*M/(R_s*c**2))          # in units of c^2 per unit mass
E_at_r       = sp.simplify(G*M/(r*c**2))
print(f"  at the horizon R_s      :  GM/(R_s c^2) = {E_at_horizon}   (M absent: {M not in E_at_horizon.free_symbols})")
print(f"  at fixed areal radius r :  GM/(r c^2)   = {E_at_r}   (M present: {M in E_at_r.free_symbols})")
assert M not in E_at_horizon.free_symbols
assert M in E_at_r.free_symbols
print(f"  -> energy per nucleon at the horizon = {E_at_horizon} m_N c^2, a pure number: no M, no alpha")

print()
print("="*74)
print("THE COMPARISON")
print("="*74)
print("  Both quantities are M-BLIND when referred to a marker the collapse itself defines")
print("  (proper interval from the origin; the horizon), and M-DEPENDENT when referred to a")
print("  fixed areal radius. The mass sets a scale and the marker carries it. => STRUCTURAL.")
print()
print("  BUT THE MECHANISMS DIFFER, and the receipt does not claim otherwise:")
print("    (A) is the amplitude exponent  : r ~ M^(1/3) and 6 x (1/3) = 2.")
print("    (B) is the horizon's definition: R_s = 2GM/c^2 makes GM/(R_s c^2) = 1/2 an identity.")
print("  So: two independent derivations of one structural pattern, not one derivation twice.")
print()
print("  WHAT THIS DOES NOT SHOW (held, not claimed): that either result implies the other,")
print("  or that the pattern extends to any third quantity. Two instances are two instances.")
print()
print("VERIFIED: the shared structure is the scaling behaviour and its failure at fixed r;")
print("the derivations remain distinct.")

# ---------------------------------------------------------------------------
# (C) ADDED r1619: a THIRD instance, and it regroups the other two.
# P7 sec:cosmogenesis: the lap closes at tau~ = -i.pi.alpha/3, "fixed by the exponent and
# independent of M". Mechanism: M enters r^3 = 2 M alpha^2 sinh^2(3 tau/2 alpha) as a pure
# AMPLITUDE factor and never in the argument, so any condition stated on the PHASE is M-free
# while the radius at which it is met, r = -(2 M alpha^2)^(1/3), carries M^(1/3).
# ---------------------------------------------------------------------------
t = sp.symbols('t')
r3 = 2*M*al**2*sp.sinh(3*t/(2*al))**2
t0 = -sp.I*sp.pi*al/3
assert sp.simplify(r3.subs(t, t0) - (-2*M*al**2)) == 0
assert M not in sp.simplify(t0).free_symbols
print()
print("="*74)
print("(C) THE LAP'S CLOSURE PHASE  (added r1619)")
print("="*74)
print(f"  r^3 at tau~ = -i.pi.alpha/3 : {sp.simplify(r3.subs(t,t0))}  -> r = -(2 M alpha^2)^(1/3)")
print(f"  the closure time itself     : tau~ = -i.pi.alpha/3, M absent: {M not in sp.simplify(t0).free_symbols}")
print("  mechanism: M is a pure amplitude factor, absent from the argument of sinh.")
print()
print("  => THE REGROUPING. (A) and (C) share a MECHANISM, not merely a structure: both are")
print("     amplitude factorisation, M scaling out of anything read in the phase variable.")
print("     (B), the horizon identity GM/(R_s c^2) = 1/2, is genuinely independent of both.")
print("     So the corpus's mass-blindnesses are 2 of one kind and 1 of another, not 3 alike")
print("     and not 2 -- which is what this file claimed before r1619.")
