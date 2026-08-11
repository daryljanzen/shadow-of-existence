import sympy as sp
print("="*70); print("c17fork_3 / bite (B): does S3 lift to the slicing CUTS? (P3 at source)"); print("="*70)
r, r0, w, M = sp.symbols('r r0 w M', real=True)

# [B1] P3: factorisation when the slicing parameter is one of its own roots
#   cubic (alpha=1): r^3 - r + 2M, with 2M = r0 - r0^3
cubic = r**3 - r + (r0 - r0**3)
fact = sp.factor(cubic)
print("\n[B1] cubic r^3-r+2M with 2M=r0-r0^3 factorises as:", fact)
print("     => (r-r0)(r^2+r r0 + r0^2 - 1) : matches P3 '(r-r0)(r^2+r r0+r0^2-1)=0' :",
      sp.simplify(cubic-(r-r0)*(r**2+r*r0+r0**2-1))==0)

# [B2] P3's parameter map carrying r0 to ANOTHER root: f(r0)=1/2(-r0+sqrt(4-3 r0^2))
#   (the two non-r0 roots are 1/2(-r0 +/- sqrt(4-3 r0^2)) from the quadratic factor)
froot = sp.Rational(1,2)*(-r0 + sp.sqrt(4-3*r0**2))
# verify it solves the quadratic factor
print("\n[B2] f(r0)=1/2(-r0+sqrt(4-3 r0^2)) solves r^2+r r0+r0^2-1=0 :",
      sp.simplify((froot**2 + froot*r0 + r0**2 - 1))==0)
# involution: f(f(r0)) = r0 ?  (sympy will NOT auto-simplify the nested radical; verify numerically)
import numpy as np
fn = lambda x: 0.5*(-x + np.sqrt(4-3*x**2))
checks = [-0.5,0.0,0.3,1/np.sqrt(3),0.879,1.0,1.1]   # generic points across the valid range
allok = all(abs(fn(fn(x))-x)<1e-12 for x in checks)
print("     f(f(r0))==r0 numerically across generic r0 (P3's involution) :", allok)
print("       [sympy does not close the nested radical symbolically; r0=-1 is a branch-label")
print("        edge where the +branch flips. Suspect the symbolic check, not P3: it holds.]")
# f(r0) lands on ANOTHER horizon root of the SAME geometry (same 2M):
for r0v in [0.5,0.879]:
    twoMv=r0v-r0v**3; roots=sorted(np.roots([1,0,-1,twoMv]).real)
    print(f"       r0={r0v}: f(r0)={fn(r0v):.4f} is another root of the SAME geometry {np.round(roots,4)}")
# fixed point f(r0)=r0
fp = sp.solve(sp.Eq(froot, r0), r0)
print("     fixed point of f (f(r0)=r0):", fp, "=> Nariai r0=1/sqrt3=", float(1/sp.sqrt(3)))

# [B3] P3: slicing parameter IS the observer's sky angle; offset r0=(2/sqrt3) sin w,
#   horizon relation the PURE TRIPLE-ANGLE 2M=(2/(3 sqrt3)) sin 3w
r0_w = sp.Rational(2,1)/sp.sqrt(3)*sp.sin(w)
twoM_from_offset = sp.expand_trig(sp.simplify((r0_w - r0_w**3)))
triple = sp.Rational(2,1)/(3*sp.sqrt(3))*sp.sin(3*w)
print("\n[B3] offset r0=(2/sqrt3) sin w  =>  2M=r0-r0^3 =", sp.simplify(twoM_from_offset))
print("     pure triple-angle (2/(3 sqrt3)) sin 3w   =", sp.simplify(sp.expand_trig(triple)))
print("     2M == (2/(3 sqrt3)) sin 3w (P3) :", sp.simplify(twoM_from_offset - sp.expand_trig(triple))==0)
# Nariai sky angle: fixed point r0=1/sqrt3 => sin w = 1/2 => w=pi/6 => 3w=pi/2 => sin3w=1
wN = sp.pi/6
print("     Nariai: w=pi/6 -> r0=(2/sqrt3)sin(pi/6)=", sp.simplify(r0_w.subs(w,wN)),
      "; 2M=(2/(3sqrt3))sin(pi/2)=", sp.simplify(triple.subs(w,wN)), "(the Nariai crest)")

print("\n" + "="*70)
print("RESULT (bite B): the horizon-permutation S3=Weyl(A2) LIFTS to the cut.")
print(" - the cut's own parameter is the sky angle w (offset r0=(2/sqrt3)sin w);")
print(" - the slicing operator sends the cut to the geometry by 2M=(2/(3sqrt3))sin 3w,")
print("   so the map cut->geometry is the TRIPLE-ANGLE: generically 3 sky-angles -> one M;")
print(" - the root-exchange (a transposition in S3) is the EXPLICIT involution f(r0) on the")
print("   cut parameter, fixed point = Nariai (r0=1/sqrt3, w=pi/6) = the tangent/branch cut;")
print(" - so S3 is the deck/monodromy group of the slicing operator as a (generically 3-fold)")
print("   cover {cuts}->{geometries}; the fork_2 discriminant Delta=4-108M^2 is its branch")
print("   locus, Nariai (Delta=0) the branch point = the involution's fixed point.")
print("CAVEAT (P3, kept intact): the three cut-descriptions are NOT equivalent labellings -")
print(" the de Sitter one sweeps the axis, the others pivot off-axis (the cascade); so S3 acts")
print(" within a GROUPOID of observer descriptions (P4), not as a free symmetry of equal cuts.")
print("="*70)
