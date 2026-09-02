"""nariai_welds_three_conditions.py (r1686) -- why the acceleration turnover sits at the seam
radius, and how that squares with the seam being the cosmogenesis.

DARYL'S QUESTION (r1685): the turnover is at r_HE = (M alpha^2)^{1/3}, which on Nariai IS the
seam radius alpha/sqrt3, and P16 owns the seam as the cosmogenesis. Is the coincidence a fact
about the Nariai member only, and how does it square with the seeding being a null boundary
rather than a dated event?

VERDICTS ARE ASSERTS, WRITTEN AFTER THE OUTPUT WAS READ.
"""
import sympy as sp
r, al, M = sp.symbols('r alpha M', positive=True)
f_gen  = 1 - 2*M/r - r**2/al**2
MN     = al/(3*sp.sqrt(3))                    # 27 M^2 = alpha^2
rho    = al/sp.sqrt(3)
f      = sp.simplify(f_gen.subs(M, MN))

print("(1) THREE CONDITIONS, AND WHAT EACH IS")
print("    f = 0        : a horizon (no static observers where f<0)")
print("    f' = 0       : the K_G zero = r_HE = the acceleration turnover")
print("    (dr/dtau)^2 = 1 - f, so dr/dtau = 1 exactly wherever f = 0")
print("    => unit rate tracks f=0 (a horizon property); the turnover tracks f'=0. Different.")

print()
print("(2) OFF NARIAI THEY SEPARATE")
Mg = sp.Symbol('M', positive=True)
hz = sp.solve(sp.Eq(f_gen, 0), r)
tp = sp.solve(sp.Eq(sp.diff(f_gen, r), 0), r)[0]
print("    f'=0 at r =", tp, " (M-dependent)")
print("    the horizons are the roots of f, which move with M independently.")
sub = {al: 1, M: sp.Rational(1,10)}          # an under-critical member
fh = [sp.nsimplify(x) for x in sp.Poly(sp.together(f_gen.subs(sub))*r, r).nroots()]
print("    at alpha=1, M=0.1 (under-critical): horizons", [sp.N(x,6) for x in fh if sp.im(x)==0 and sp.re(x)>0],
      " vs f'=0 at", sp.N(tp.subs(sub),6))

print()
print("(3) AT NARIAI THE DOUBLE ROOT WELDS THEM")
assert sp.simplify(f.subs(r, rho)) == 0,                    "f(rho) != 0"
assert sp.simplify(sp.diff(f, r).subs(r, rho)) == 0,        "f'(rho) != 0"
assert sp.simplify(sp.diff(f, r, 2).subs(r, rho)) == -6/al**2, "f''(rho) unexpected"
assert sp.simplify(tp.subs(M, MN) - rho) == 0,              "the turnover is not at rho"
print("    ASSERTED: f(rho) = f'(rho) = 0, f''(rho) = -6/alpha^2 < 0, and r_HE(M_N) = rho.")
print("    => rho is a MAXIMUM of f, so f <= 0 EVERYWHERE with equality only at rho:")
fa = sp.lambdify(r, f.subs(al,1))
assert all(fa(x) <= 1e-12 for x in [0.1,0.3,0.5,0.577,0.7,1.0,2.0,5.0]), "f>0 somewhere"
print("       the static region has collapsed to the single radius rho. There is no exterior.")

print()
print("(4) SO THE COMOVING WORLDLINE CROSSES IT -- it does not asymptote")
v2 = sp.simplify(1 - f.subs(r, rho))
assert v2 == 1, "the rate at rho is not 1"
print("    ASSERTED: (dr/dtau)^2 = 1 at rho, so dr/dtau = 1 exactly -- finite rate, finite time.")
print("    The 7.06 Gyr crossing is a crossing, not an approach.")

print()
print("(5) THE ANSWER TO THE QUESTION, in two parts")
print("  (a) The coincidence is NARIAI-ONLY, and the double root is what does it: f=0 and f'=0")
print("      are independent conditions that the degeneracy places at one radius. Off Nariai the")
print("      turnover sits between the two horizons and coincides with neither.")
print("  (b) The radius carries TWO DISTINCT THINGS and they must not be fused:")
print("      * the kappa=0 DEGENERACY -- a property of the geometry, not an event. This is what")
print("        the reassignment uses: a degenerating Killing field's freed null direction.")
print("      * the comoving CROSSING at 7.06 Gyr -- an event on our worldline, at unit rate.")
print("      The seeding is the first; the acceleration turnover is the second. One radius,")
print("      two readings at different levels -- the same distinction P7 draws between the")
print("      geometric closure and the physical seeding.")

print()
print("BOUND, not claimed:")
print("  * NOTHING here says the degeneracy CAUSES the turnover or vice versa. They are")
print("    co-located because the member is Nariai, and that is the whole of the claim.")
print("  * The 7.06 Gyr figure is the comoving crossing of the radius, at H0=73; it is not")
print("    a date for the seeding, which is a null-boundary property and not an event.")
