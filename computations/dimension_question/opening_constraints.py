"""Two constraints that fix what a dimensional rise would have to BE, before any construction."""
import sympy as sp
print("="*78)
print(" (A)  HORIZON POLYNOMIAL DEGREE vs SPACETIME DIMENSION  (D-dim Schwarzschild-de Sitter)")
print("="*78)
r,al,M=sp.symbols('r alpha M',positive=True)
for n in range(4,9):                      # n = spacetime dimension
    f=1-2*M/r**(n-3)-r**2/al**2
    poly=sp.simplify(sp.together(f)*r**(n-3))
    p=sp.Poly(sp.numer(sp.simplify(poly)),r)
    print("   spacetime dim %d :  f = 1 - 2M/r^%d - r^2/a^2   ->  horizon polynomial degree %d  (=> %d roots)"
          %(n,n-3,p.degree(),p.degree()))
print("\n   => degree = (spacetime dim) - 1.  THREE roots <=> FOUR-dimensional spacetime.")
print("      P3/P14: each hinge designates one root; the three hinges ARE the three generations.")
print("      So within CR the observed generation count FIXES the spacetime dimension at 4.")
print()
print("="*78)
print(" (B)  MINIMAL LORENTZIAN SUBSTRATE WHOSE ISOTROPY CAN CARRY su(3)")
print("="*78)
print("   dS_D = SO(D,1)/SO(D-1,1);  isotropy so(D-1,1) acts on the tangent space, signature (1,D-1).")
print("   su(3) is COMPACT, so any embedding lands in a maximal compact subalgebra: so(D-1).")
print("   smallest faithful REAL rep of su(3) is 6-dimensional (C^3 = R^6)  =>  su(3) subset so(n) iff n>=6.")
for D in range(5,9):
    ok = (D-1)>=6
    print("     D=%d : isotropy so(%d,1), maximal compact so(%d)  ->  su(3) %s"
          %(D,D-1,D-1,"FITS" if ok else "does NOT fit"))
print("\n   => a LORENTZIAN substrate whose isotropy carries su(3) needs D >= 7, not 6.")
print("      (P13's 'su(3) subset so(6)' is about the COMPACT face S^5=SO(6)/SO(5) -- an isometry group,")
print("       not a six-dimensional Lorentzian substrate.  P12's 'a six-dimensional substrate would")
print("       permit one' is loose in exactly that way.)")
