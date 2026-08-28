#!/usr/bin/env python3
"""RECEIPT — quadric bake `Q7`: ** P02'S INTERIOR ARC IS A CIRCLE, AND ITS ANALYTIC COMPLETION IS ONE
CONIC READ TWICE -- HYPERBOLA / CIRCLE / HYPERBOLA -- THE CIRCLE AND THE HYPERBOLA SHARING THE ONE
EQUATION (r-M)^2 -/+ s^2 = M^2 ACROSS THE SIGNATURE FLIP s -> i s. **

LEVEL: NO RATE -- a conic classification.

WHY THIS PROBE.  The r3500 reach pass read P02 (janzen_circle) for the quadric field for the first
  time.  Its whole conic content is one object -- the "hyperbola, circle, hyperbola" analytic
  completion of the Lemaitre-Tolman cycloid -- and it carried NO quadric receipt (the neighbouring
  P02 receipts cover the cycloid's critical points and the Kretschmann function-pole, not the conic).

WHAT P02 CLAIMS.  The interior arc r = M(1 + cos z) has r - M = M cos z obeying r'' = -(r - M) --
  simple harmonic motion about r = M -- so it is the projection onto the r-axis of uniform motion on
  the CIRCLE (r-M)^2 + s^2 = M^2, conjugate s = M sin z.  Continuing z into the complex plane at each
  critical point (z -> i rho) sends the circle to the HYPERBOLA (r-M)^2 - s^2 = M^2: "a single
  analytic curve, hyperbola-circle-hyperbola".

VERIFIED SYMBOLICALLY.
  (1) r = M(1+cos z) satisfies r'' = -(r-M) exactly (SHM about r=M).
  (2) (r-M)^2 + (M sin z)^2 = M^2 identically -- the interior arc lies on the CIRCLE of radius M.
  (3) z -> i rho gives r = M(1+cosh rho) and s = M sinh rho with (r-M)^2 - s^2 = M^2 identically --
      the exterior arms lie on the HYPERBOLA of the same semi-parameter M.
  (4) Circle and hyperbola are ONE conic in the (r-M, s) plane: the unit-discriminant conic
      (r-M)^2 + eps s^2 = M^2 with eps = +1 (Riemannian s real) and eps = -1 (Lorentzian s = i rho) --
      a signature flip of the transverse coordinate, not two curves.

WHAT IS NOT CLAIMED.  The Kruskal-extension reading, the back-seam continuation past z=pi, and the
  twelfth-order Kretschmann pole are P02's own (receipted separately); Q7 claims only the conic
  classification circle <-> hyperbola under s -> i s.

VERDICTS ARE ASSERTS.
"""
import sympy as sp

print("=" * 78)
print("  Q7 — P02's interior conic: circle and hyperbola, one curve across the signature flip")
print("=" * 78)

z, M, rho, s = sp.symbols('z M rho s', real=True)

r = M * (1 + sp.cos(z))
assert sp.simplify(sp.diff(r, z, 2) - (-(r - M))) == 0, "r'' = -(r-M): SHM about r=M"
print(f"\n  (1) r = M(1+cos z):  r'' = -(r-M)  -> simple harmonic motion about r = M.")

circle = sp.simplify((r - M)**2 + (M * sp.sin(z))**2 - M**2)
assert circle == 0, "interior arc on the circle (r-M)^2 + s^2 = M^2"
print(f"  (2) (r-M)^2 + (M sin z)^2 - M^2 = {circle}  -> the interior arc is the CIRCLE of radius M.")

rH = M * (1 + sp.cosh(rho))
sH = M * sp.sinh(rho)
hyp = sp.simplify((rH - M)**2 - sH**2 - M**2)
assert hyp == 0, "z -> i rho gives the hyperbola (r-M)^2 - s^2 = M^2"
print(f"  (3) z -> i rho:  (r-M)^2 - (M sinh rho)^2 - M^2 = {hyp}  -> the exterior arms are the")
print("      HYPERBOLA of the same semi-parameter M.")

# (4) one conic (r-M)^2 + eps s^2 = M^2, eps = +1 circle, eps = -1 hyperbola
eps = sp.symbols('eps')
conic = (r - M)**2 + eps * s**2 - M**2
circle_case = sp.simplify(conic.subs({eps: 1, s: M * sp.sin(z)}))
hyper_case = sp.simplify(conic.subs({eps: -1, s: sH, r: rH}))
assert circle_case == 0 and hyper_case == 0
# discriminant of A x^2 + C y^2: sign of A*C decides ellipse(+)/hyperbola(-); here A=1, C=eps
assert sp.sign(1 * 1) == 1 and sp.sign(1 * (-1)) == -1
print("  (4) one conic (r-M)^2 + eps*s^2 = M^2:  eps=+1 (s real) is the CIRCLE (AC>0, elliptic),")
print("      eps=-1 (s = i rho) is the HYPERBOLA (AC<0) -- a signature flip of the transverse")
print("      coordinate, ONE analytic curve read twice, not two curves.")

print("\n  ** VERDICTS: P02's interior arc IS a circle (SHM); its analytic completion is that one")
print("     conic continued across s -> i s into a hyperbola -- 'hyperbola, circle, hyperbola'. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
