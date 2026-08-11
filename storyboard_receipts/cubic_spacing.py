"""cubic_spacing.py (r1623) -- the r1412 spacing lock-in, the two pieces of it that were
genuinely unplaced: (a) WHY the horizon cubic can degenerate and the turnaround cubic cannot,
read off their discriminants; (b) where the four loci sit in the fig-E phase.

ALREADY PLACED, NOT RE-DERIVED HERE: that H-T = -alpha^2 r so the two cubics meet at r=0 and
nowhere else (P7 sec:twocritical), and the four loci with their derivative signatures (P7's
triptych figure, receipt F_triptych.py). This receipt covers only the remainder.
"""
import sympy as sp
r, M, al = sp.symbols('r'), sp.symbols('M', positive=True), sp.symbols('alpha', positive=True)
H = r**3 - al**2*r + 2*M*al**2
T = r**3 + 2*M*al**2

print("(a) THE DISCRIMINANT CONTRAST")
dH, dT = sp.factor(sp.discriminant(H, r)), sp.factor(sp.discriminant(T, r))
print("   disc H =", dH, "  -> vanishes at M =", sp.solve(sp.Eq(dH, 0), M))
print("   disc T =", dT, "  -> strictly negative for every M != 0: never vanishes")
assert sp.solve(sp.Eq(dH, 0), M) != []
assert sp.simplify(dT + 108*M**2*al**4) == 0
# H's double root at Nariai gives (rho, rho, -2rho)
MN = al/(3*sp.sqrt(3)); rho = al/sp.sqrt(3)
HN = sp.expand(H.subs(M, MN))
assert sp.simplify(HN - sp.expand((r-rho)**2*(r+2*rho))) == 0
print("   at M = alpha/3sqrt3 :  H factors as (r-rho)^2 (r+2rho), rho = alpha/sqrt3  -> the 2:1")
# T's roots are always an equilateral triple, never coincident
Troots = sp.solve(T.subs({M: sp.Rational(1,10), al: 1}), r)
mods = {sp.nsimplify(abs(z), rational=False) for z in Troots}
print(f"   T's roots (M=0.1, alpha=1): {len(Troots)} distinct, equal modulus:",
      len({round(float(abs(z)), 12) for z in Troots}) == 1)
assert len(Troots) == 3 and len({round(float(abs(z)), 12) for z in Troots}) == 1
print("   => the flat term -alpha^2 r does double duty: it fixes WHERE the cubics meet and")
print("      it decides WHICH of them can degenerate. Absent from T, T's disc cannot vanish.")

print()
print("(b) THE FIG-E PHASE POSITIONS,  phi = 2 pi r / (sqrt3 alpha),  alpha = 1")
phi = lambda x: 2*sp.pi*x/sp.sqrt(3)
loci = [("front seam  +rho", rho.subs(al,1)), ("r=0", sp.Integer(0)),
        ("turnaround -cbrt2 rho", -sp.root(2,3)*rho.subs(al,1)), ("back seam -2rho", -2*rho.subs(al,1))]
for name, x in loci:
    print(f"   {name:24s} phi = {sp.nsimplify(phi(x))!s:24s} = {float(phi(x)*180/sp.pi):+8.2f} deg")
assert sp.simplify(phi(rho.subs(al,1)) - 2*sp.pi/3) == 0
assert sp.simplify(phi(-2*rho.subs(al,1)) + 4*sp.pi/3) == 0
assert sp.simplify(phi(-sp.root(2,3)*rho.subs(al,1)) + 2*sp.pi*sp.root(2,3)/3) == 0
print("   => the three horizon roots sit on the clean 120/240 lattice; the turnaround sits at")
print("      -2 pi cbrt(2)/3 ~ -151.2 deg, OFF it by exactly the cbrt(2) signature of the other")
print("      cubic -- so it cannot be read as a fourth root of this one.")
print()
print("VERIFIED (a) and (b). Held: nothing here identifies the two cubics' root sets.")
