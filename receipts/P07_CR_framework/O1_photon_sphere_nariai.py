"""O1 — the photon sphere of the SdS family, and where it sits at Nariai.
f(r) = 1 - 2M/r - r^2/alpha^2.   Photon sphere: d/dr (f/r^2) = 0.   Impact parameter b^2 = r^2/f.
ORIGIN: storyboard_receipts/O1_photon_sphere_nariai.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np, sympy as sp
r,M,al = sp.symbols('r M alpha', positive=True)
f = 1 - 2*M/r - r**2/al**2

print("="*78); print("O1 — THE PHOTON SPHERE OF SdS, AND NARIAI"); print("="*78)
print("\nSTEP 1 — the photon sphere, derived (NOT assumed from Schwarzschild):")
cond = sp.simplify(sp.diff(f/r**2, r))
print("   d/dr (f/r^2) =", sp.simplify(cond))
sol = sp.solve(sp.Eq(cond,0), r)
print("   => r_ph =", sol, "   <- LAMBDA-INDEPENDENT: the alpha term drops out of the condition")

print("\nSTEP 2 — the Nariai member: Lambda G^2 M^2/c^4 = 1/9, i.e. in units alpha=1 (Lambda=3):")
Mn = sp.Rational(1,3)/sp.sqrt(3)
print(f"   M_Nariai = 1/(3.sqrt3) = {float(Mn):.10f} (alpha=1)")
print(f"   photon sphere r_ph = 3M = {float(3*Mn):.10f}")
print(f"   alpha/sqrt3        =      {float(1/sp.sqrt(3)):.10f}")
print(f"   EQUAL: {sp.simplify(3*Mn - 1/sp.sqrt(3))==0}")

print("\nSTEP 3 — and the merged horizon at Nariai is at alpha/sqrt3.  So:")
fN = f.subs({M:Mn, al:1})
print("   f(r) at Nariai =", sp.simplify(fN))
print("   f(alpha/sqrt3) =", sp.simplify(fN.subs(r, 1/sp.sqrt(3))), "   <- the horizon")
print("   f'(alpha/sqrt3)=", sp.simplify(sp.diff(fN,r).subs(r, 1/sp.sqrt(3))), "   <- DOUBLE root, degenerate")
print("\n   *** THE PHOTON SPHERE COINCIDES WITH THE MERGED HORIZON AT NARIAI. ***")

print("\nSTEP 4 — the impact parameter b^2 = r^2/f there:")
print("   b^2 = r_ph^2 / f(r_ph) = (1/3) / 0  ->  DIVERGES.")
print("   So the shadow's impact parameter is unbounded at the forced member: the photon")
print("   sphere is null-degenerate, sitting exactly on the horizon where f = f' = 0.")
print("\nSTEP 5 — is this generic or special?  Sweep M below Nariai:")
print(f"   {'M/M_Nariai':>12s} {'r_ph = 3M':>12s} {'inner horizon':>15s} {'f(r_ph)':>12s}")
for frac in [0.3,0.6,0.9,0.99,1.0]:
    Mv=float(Mn)*frac
    fn = sp.lambdify(r, f.subs({M:Mv, al:1}), 'numpy')
    roots=np.sort([x.real for x in np.roots([-1,0,1,-2*Mv]) if abs(x.imag)<1e-9])
    pos=[x for x in roots if x>0]
    print(f"   {frac:12.3f} {3*Mv:12.6f} {pos[0] if pos else float('nan'):15.6f} {float(fn(3*Mv)):12.6f}")

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  STEP 1's condition, STEP 2's "EQUAL: True" and STEP 3's two
# zeros were all printed.  Pinned here: the derived condition 2(3M-r)/r^4 and its single root
# r_ph = 3M, its Lambda-independence (alpha does not occur in it at all), and the Nariai
# coincidence r_ph = alpha/sqrt3 = the merged horizon with f = f' = 0 -- the last done for
# SYMBOLIC alpha, not only in the alpha = 1 units STEPS 2-5 run in.  The sweep is pinned by the
# closed form f(3M) = 1/3 - 9 M^2/alpha^2, which is what makes the table's approach to 0 a fact
# about the family rather than about the five fractions chosen.
assert sp.simplify(cond - 2*(3*M - r)/r**4) == 0
assert sol == [3*M]
assert al not in cond.free_symbols                       # LAMBDA-INDEPENDENT, identically
assert sp.simplify(3*Mn - 1/sp.sqrt(3)) == 0
assert abs(float(Mn) - 0.1924500897) < 1e-9 and abs(float(3*Mn) - 0.5773502692) < 1e-9
assert sp.simplify(fN.subs(r, 1/sp.sqrt(3))) == 0                    # ON the horizon
assert sp.simplify(sp.diff(fN, r).subs(r, 1/sp.sqrt(3))) == 0        # a DOUBLE root
assert sp.simplify(sp.diff(fN, r, 2).subs(r, 1/sp.sqrt(3)) + 6) == 0 # and not a triple one
M_gen, r_gen = al/(3*sp.sqrt(3)), al/sp.sqrt(3)          # the same at ARBITRARY alpha:
assert sp.simplify(sp.solve(sp.Eq(sp.diff(f/r**2, r), 0), r)[0] - 3*M) == 0
assert sp.simplify((3*M).subs(M, M_gen) - r_gen) == 0    # r_ph = 3M = alpha/sqrt3 = the horizon
assert sp.simplify(f.subs({M: M_gen, r: r_gen})) == 0
assert sp.simplify(sp.diff(f, r).subs({M: M_gen, r: r_gen})) == 0
assert sp.simplify(sp.diff(f, r, 2).subs({M: M_gen, r: r_gen}) + 6/al**2) == 0
assert sp.simplify(f.subs(r, 3*M) - (sp.Rational(1, 3) - 9*M**2/al**2)) == 0
for frac_a, f_expect in [(0.3, 0.303333), (0.6, 0.213333), (0.9, 0.063333), (0.99, 0.006633)]:
    assert abs(float(f.subs({M: float(Mn)*frac_a, al: 1, r: 3*float(Mn)*frac_a})) - f_expect) < 1e-6
assert abs(float(f.subs({M: float(Mn), al: 1, r: 3*float(Mn)}))) < 1e-12     # and 0 at Nariai
print("\n  [r2376+c54.161] asserted: d(f/r^2)/dr = 2(3M-r)/r^4 with the single root r_ph = 3M and")
print("  no alpha in it; at SYMBOLIC alpha the Nariai member has r_ph = alpha/sqrt3 with f = f' = 0")
print("  and f'' = -6/alpha^2; and the sweep column is pinned by f(3M) = 1/3 - 9M^2/alpha^2.")
