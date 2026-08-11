import sympy as sp

r, r0, x, y, M, t = sp.symbols('r r0 x y M t', real=True)
r1, r2, r3 = sp.symbols('r1 r2 r3', real=True)

print("="*70)
print("c17fork_1: the A2 root-system structure of the SdS solution space")
print("="*70)

# ---- 1. The horizon cubic (thesis Eq. horizon_eq / SdS_statical_pure), alpha=1
# N(r) = r^3 - r0^3 - (r - r0) = r^3 - r + 2M, with 2M = r0 - r0^3
twoM = r0 - r0**3
N = r**3 - r0**3 - (r - r0)
N_dep = sp.expand(N)
print("\n[1] Horizon cubic N(r) = r^3 - r0^3 - (r-r0) =", N_dep)
print("    with 2M = r0 - r0^3 ;  N(r) = r^3 - r + 2M :", sp.simplify(N_dep-(r**3 - r + twoM))==0)
# depressed: no r^2 term => sum of three roots = 0  (Cartan / traceless)
poly = sp.Poly(r**3 - r + (twoM.subs(r0, sp.Symbol('a'))), r)  # generic 2M
print("    coeff of r^2 :", sp.Poly(r**3 - r + sp.Symbol('m'), r).all_coeffs()[1],
      " => r1+r2+r3 = 0  (the traceless/Cartan condition)")

# ---- 2. Vieta: given one root r0, the OTHER two horizons lie on the ellipse
# divide N by (r - r0):
quotient, remainder = sp.div(r**3 - r + twoM, r - r0, r)
print("\n[2] N(r)/(r-r0):  quotient =", sp.expand(quotient), " remainder =", sp.simplify(remainder))
print("    => other two horizons satisfy:", sp.expand(quotient), "= 0")
# quotient should be r^2 + r0 r + (r0^2 - 1)  => r^2 + r r0 + r0^2 = 1  (the ellipse)
ellipse_check = sp.simplify(sp.expand(quotient) - (r**2 + r*r0 + r0**2 - 1))
print("    quotient - (r^2 + r*r0 + r0^2 - 1) =", ellipse_check,
      " => the two non-r0 horizons lie on r^2 + r*r0 + r0^2 = 1  (FUNDAMENTAL ELLIPSE) :", ellipse_check==0)

# ---- 3. The fundamental ellipse IS the A2 quadratic form
# A2 root space = the plane r1+r2+r3=0 in R^3, metric = restriction of sum r_i^2
r3sub = -(r1+r2)
form3 = r1**2 + r2**2 + r3**2
form2 = sp.expand(form3.subs(r3, r3sub))
print("\n[3] Restrict sum r_i^2 to the traceless plane r1+r2+r3=0:")
print("    sum r_i^2 | (r3=-(r1+r2)) =", form2, " = 2*(r1^2 + r1 r2 + r2^2)")
print("    => the A2 quadratic form is  x^2 + x y + y^2  == the fundamental ellipse form :",
      sp.simplify(form2/2 - (r1**2 + r1*r2 + r2**2))==0)
# Gram matrix of x^2+xy+y^2 and its eigenvalues (A2 signature 1:3)
G = sp.Matrix([[1, sp.Rational(1,2)],[sp.Rational(1,2), 1]])
print("    Gram matrix [[1,1/2],[1/2,1]] eigenvalues:", sorted(G.eigenvals().keys()),
      " ratio 3:1 (the A2 1:3)")

# ---- 4. S3 = Weyl(A2) permutes the three horizons, fixing the geometry (same M)
# elementary symmetric polynomials of the three roots are S3-invariant => same cubic => same M
e1 = r1+r2+r3
e2 = r1*r2+r1*r3+r2*r3
e3 = r1*r2*r3
import itertools
inv = True
for p in itertools.permutations([r1,r2,r3]):
    sub = {r1:p[0], r2:p[1], r3:p[2]}
    if sp.simplify(e1.subs(sub,simultaneous=True)-e1)!=0: inv=False
    if sp.simplify(e2.subs(sub,simultaneous=True)-e2)!=0: inv=False
    if sp.simplify(e3.subs(sub,simultaneous=True)-e3)!=0: inv=False
print("\n[4] S3 permutations leave (e1,e2,e3) invariant =>",
      "same cubic, same M, same rigid geometry :", inv)
print("    e1=0 (traceless) fixed; e2=-1 (=> ellipse=1) fixed; e3=-2M fixed.")
print("    => S3 = Weyl(A2) permutes the THREE HORIZONS as interchangeable")
print("       descriptions of ONE rigid geometry (thesis line 78).")

# ---- 5. Physical map of the three horizons for an under-critical M
import numpy as np
for Mval in [0.10, 0.18]:
    coeffs = [1,0,-1,2*Mval]
    roots = sorted(np.roots(coeffs).real)
    crit = 1/np.sqrt(27)
    label = "under-critical" if Mval<crit else "OVER-critical(complex pair)"
    print(f"\n[5] M={Mval}  ({'under' if Mval<crit else 'over'}-critical, 1/sqrt27={crit:.4f})")
    print(f"    roots of r^3 - r + 2M : {np.round(roots,4)}   sum={np.round(sum(roots),6)}")
    if Mval<crit:
        print(f"    inner/negative horizon r-={roots[0]:.4f} ; black-hole r_b={roots[1]:.4f} ; cosmological r_c={roots[2]:.4f}")
        print(f"    => S3-orbit connects (inner <-> black-hole <-> cosmological): ONE geometry, three horizon-faces")

# ---- 6. signature structure: g_tt = N(r)/r ; sign of N(r) = r spacelike/timelike
print("\n[6] g_tt = N(r)/r (thesis SdS_statical_pure); sign(N) flips at each horizon")
print("    => the (r,r0)-plane shaded/unshaded (r timelike/spacelike) is the A2-form sign chamber")
print("="*70)
