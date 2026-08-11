"""
P03_cubic_factor_ellipse_locus.py -- verifies: the SdS horizon cubic factorises when the slicing
  parameter is one of its roots, the horizon locus g(r)=g(r0) is a line + a 45deg-tilted ellipse (the A2
  norm form), the three roots sum to zero, the root-exchange involution sigma, and the backward-radial
  reflection. [P3 SdS-slicing-curve_v2 prop:factor eq:factored, prop:locus eq:locusfactor, prop:involution, sec:ellipse]
STATUS: ✔✔   RUN: python3 P03_cubic_factor_ellipse_locus.py   RUNTIME: ~4s
COMPUTES: the factorisation identity; f = -(r-r0)(r^2+r r0+r0^2-1)/r at 2M=r0-r0^3; sum-of-roots=0; the
  ellipse quadratic-form eigenstructure (1/2 & 3/2, semi-axes sqrt2 & sqrt(2/3), 45deg); the involution
  sigma(r0)=1/2(-r0+sqrt(4-3r0^2)) (sigma o sigma=id, fixes 1/sqrt3, sigma(0)=1, sigma(1)=0, lands on the
  2nd root); the discriminant 4-3r0^2 regime counts; the reflection (r0,r)->(-r0,-r) with 2M->-2M.
  CONTROLS: the factorisation holds ONLY because 2M=r0-r0^3 (a generic 2M leaves r0 not a root); the
  discriminant sign predicts the real-root count on a numeric sweep.
ORIGIN: built new r1340 (P3's ellipse-locus claim was uncited).
"""
import sympy as sp, numpy as np
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r, r0, M = sp.symbols('r r_0 M', real=True)
print("="*74); print("P03 cubic factorisation + ellipse locus + involution"); print("="*74)
# (1) factorisation identity: (r-r0)(r^2+r r0+r0^2-1) == g(r)-g(r0), g=t^3-t
g=lambda t: t**3 - t
quad = r**2 + r*r0 + r0**2 - 1
ok&=check("factorisation (r-r0)(r^2+r r0+r0^2-1) = g(r)-g(r0)", sp.expand((r-r0)*quad - (g(r)-g(r0)))==0)
# (2) f = -(r-r0)*quad/r at 2M=r0-r0^3, alpha=1
twoM = r0 - r0**3
f = 1 - twoM/r - r**2
ok&=check("f = -(r-r0)(r^2+r r0+r0^2-1)/r  at 2M=r0-r0^3", sp.simplify(f + (r-r0)*quad/r)==0)
ok&=check("  at r0=0: f = 1-r^2 (de Sitter), roots of r^3-r are 0,±1", sp.simplify(f.subs(r0,0)-(1-r**2))==0)
# (3) three roots sum to zero (cubic r^3 - r + 2M, no r^2 term)
cub = sp.Poly(r**3 - r + twoM, r)
ok&=check("three roots sum to zero (no r^2 term)", cub.coeff_monomial(r**2)==0)
# (4) ellipse eigenstructure
A = sp.Matrix([[1, sp.Rational(1,2)],[sp.Rational(1,2),1]])
evs = A.eigenvects()
eigvals = sorted([ev[0] for ev in evs])
ok&=check("quadratic-form matrix [[1,1/2],[1/2,1]] eigenvalues = 1/2, 3/2", eigvals==[sp.Rational(1,2),sp.Rational(3,2)])
# semi-axis along eigvec = 1/sqrt(eigenvalue); 1/2->sqrt2 (anti-diagonal (1,-1)); 3/2->sqrt(2/3) (diagonal (1,1))
half = [ev for ev in evs if ev[0]==sp.Rational(1,2)][0]; three2=[ev for ev in evs if ev[0]==sp.Rational(3,2)][0]
vh=half[2][0]; vt=three2[2][0]
ok&=check("eigval 1/2 -> eigvec ∝ (1,-1) [anti-diagonal r=-r0], longer semi-axis sqrt2",
          sp.simplify(vh[0]+vh[1])==0 and sp.simplify(1/sp.sqrt(sp.Rational(1,2))-sp.sqrt(2))==0)
ok&=check("eigval 3/2 -> eigvec ∝ (1,1) [diagonal r=r0], shorter semi-axis sqrt(2/3)",
          sp.simplify(vt[0]-vt[1])==0 and sp.simplify(1/sp.sqrt(sp.Rational(3,2))-sp.sqrt(sp.Rational(2,3)))==0)
# ** r2376+c54.159: this line was `check(..., True)` -- a PASS certifying nothing.  Found by
#    the hollow-assertion lint once it was taught to read check() as well as assert. **
ok&=check("  tilt 45deg (eigenvectors along the diagonals)",
          sp.simplify(sp.Abs(sp.atan2(vh[1], vh[0]) % sp.pi) - 3*sp.pi/4) == 0
          and sp.simplify(sp.Abs(sp.atan2(vt[1], vt[0]) % sp.pi) - sp.pi/4) == 0)
# (5) involution sigma
sig = lambda x: (-x + sp.sqrt(4-3*x**2))/2
sig_n=lambda x:(-x+np.sqrt(4-3*x**2))/2
ok&=check("sigma o sigma = id on the positive-root half (sweep r0∈[0,1])", all(abs(sig_n(sig_n(x))-x)<1e-9 for x in np.linspace(0,1,21)))
ok&=check("sigma fixes 1/sqrt3 (Nariai); sigma(0)=1; sigma(1)=0",
          sp.simplify(sig(1/sp.sqrt(3))-1/sp.sqrt(3))==0 and sp.simplify(sig(sp.Integer(0))-1)==0 and sp.simplify(sig(sp.Integer(1)))==0)
ok&=check("sigma(r0) is a root of the quadratic factor r^2+r r0+r0^2-1", sp.simplify(quad.subs(r, sig(r0)))==0)
# (6) discriminant 4-3 r0^2 -> real-root count (numeric sweep)
def nreal(r0v):
    tm=r0v-r0v**3; rts=np.roots([1,0,-1,tm]); return int(np.sum(np.abs(rts.imag)<1e-9))
ok&=check("discriminant 4-3r0^2: r0=0.3 undercrit(>0)->3 real, r0=1.2 overcrit(<0)->1 real",
          (4-3*0.3**2>0 and nreal(0.3)==3) and (4-3*1.2**2<0 and nreal(1.2)==1))
ok&=check("  Nariai |r0|=2/sqrt3: discriminant = 0", abs(4-3*(2/np.sqrt(3))**2)<1e-12)
# (7) backward-radial reflection (r0,r)->(-r0,-r): ellipse invariant, 2M->-2M
ok&=check("ellipse r^2+r r0+r0^2=1 invariant under (r0,r)->(-r0,-r)", sp.expand((quad+1).subs({r:-r,r0:-r0}) - (quad+1))==0)
ok&=check("  and 2M=r0-r0^3 -> -2M under r0->-r0", sp.simplify(twoM.subs(r0,-r0) + twoM)==0)
# (8) CONTROL: factorisation needs 2M=r0-r0^3
g2M = sp.symbols('g2M')  # a generic mass
ok&=check("CONTROL: for generic 2M != r0-r0^3, r0 is NOT a root of r^3-r+2M",
          sp.simplify((r**3-r+g2M).subs(r,r0)) != 0)
# r2376+c54.159 -- (a) the receipt's own PASS/FAIL flag, which was only printed; and (b) an
# INDEPENDENT pin of the figures INDEX quotes for this row, so the file does not rest on the flag:
# the ellipse r^2 + r.r0 + r0^2 = 1 (the A_2 norm form) has quadratic-form eigenvalues EXACTLY
# 1/2 and 3/2, hence semi-axes sqrt2 = 1.4142135624 (along the anti-diagonal r = -r0) and
# sqrt(2/3) = 0.8164965809 (along the diagonal), a 45-degree tilt; sigma fixes 1/sqrt3 =
# 0.5773502692 and swaps 0 <-> 1; and the discriminant 4 - 3 r0^2 vanishes at the Nariai value
# |r0| = 2/sqrt3 = 1.1547005384, splitting three real roots (r0 = 0.3) from one (r0 = 1.2).
assert ok, "P03_cubic_factor_ellipse_locus: a check() line FAILED -- see the PASS/FAIL column above"
assert eigvals == [sp.Rational(1,2), sp.Rational(3,2)], eigvals
assert abs(float(1/sp.sqrt(eigvals[0])) - 1.4142135624) < 1e-9
assert abs(float(1/sp.sqrt(eigvals[1])) - 0.8164965809) < 1e-9
assert abs(float(sp.acos(abs(vh[0])/sp.sqrt(vh[0]**2+vh[1]**2))*180/sp.pi) - 45.0) < 1e-9   # tilt
assert abs(sig_n(1/np.sqrt(3)) - 0.5773502692) < 1e-9, sig_n(1/np.sqrt(3))
assert abs(2/np.sqrt(3) - 1.1547005384) < 1e-9 and abs(4 - 3*(2/np.sqrt(3))**2) < 1e-12
assert (nreal(0.3), nreal(1.2)) == (3, 1), (nreal(0.3), nreal(1.2))
assert abs(sum(np.roots([1, 0, -1, 0.3 - 0.3**3]))) < 1e-12          # the three roots sum to zero

print("="*74)
allpass = ok
print("RESULT:", "ALL PASS -- cubic factors on the ellipse (A2 norm form), 3 roots sum to zero, ellipse\n         eigenstructure 1/2 & 3/2 (semi-axes sqrt2 & sqrt(2/3), 45deg tilt), involution sigma correct,\n         discriminant predicts regimes, backward-radial reflection is the 2M->-2M symmetry." if ok else "SOME FAILED")
print("="*74)
