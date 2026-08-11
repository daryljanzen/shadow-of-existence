"""Q4 — is there a cross-ratio on the horizon roots invariant under the groupoid?
Roots of r^3 - r + 2M with 2M = r0 - r0^3: they are r0, and (-r0 +- sqrt(4-3r0^2))/2.
ORIGIN: storyboard_receipts/Q4_equianharmonic_vantages.py -- registered r2376 (c54); edit the origin, not this copy."""
import sympy as sp
r0 = sp.symbols('r0', real=True)
d  = sp.sqrt(4 - 3*r0**2)
rA = r0
rB = (-r0 + d)/2
rC = (-r0 - d)/2
print("="*78); print("Q4 — CROSS-RATIO ON THE HORIZON ROOTS"); print("="*78)
print("\nSTEP 0 — the three roots, and they sum to zero:")
print("   rA =", rA, "  rB =", sp.simplify(rB), "  rC =", sp.simplify(rC))
print("   sum =", sp.simplify(rA+rB+rC))

def CR(a,b,c,d_):
    return sp.simplify(((a-c)*(b-d_))/((b-c)*(a-d_)))

print("\nSTEP 1 — three roots need a FOURTH point.  The natural candidates in the corpus:")
print("   r = 0   (the branch point, R's fixed point)   |   r = infinity")
lam = CR(rA, rB, rC, sp.Integer(0))
lam = sp.simplify(sp.radsimp(lam))
print("\n   cross-ratio (rA, rB; rC, 0) =", lam)
print("   simplified                  =", sp.simplify(sp.expand(lam)))

print("\nSTEP 2 — is it CONSTANT in r0?  (i.e. the same for every member of the family)")
for val in [sp.Rational(1,5), sp.Rational(1,2), 1/sp.sqrt(3), sp.Rational(9,10)]:
    v = sp.nsimplify(sp.simplify(lam.subs(r0, val)))
    print(f"   r0 = {str(sp.nsimplify(val)):12s} ->  lambda = {v}   ~ {sp.N(v, 12)}")
    # r2376+c54.158 -- pins STEP 2's printed figures, and with them the receipt's NEGATIVE half:
    # on the r-line the cross-ratio is NOT invariant.  It reads 2.88606348806 at r0 = 1/5,
    # 1.19337524528 at r0 = 1/2 and 0.309345910933 at r0 = 9/10 -- and it DEGENERATES to exactly 1
    # at Nariai r0 = 1/sqrt(3), where two of the three roots merge.  That failure is what sends
    # the search for a groupoid-invariant cross-ratio to the SKY ANGLE in STEP 3.
    assert abs(float(sp.N(v, 20)) - {sp.Rational(1, 5): 2.88606348806,
                                     sp.Rational(1, 2): 1.19337524528,
                                     1/sp.sqrt(3):      1.0,
                                     sp.Rational(9, 10): 0.309345910933}[val]) < 1e-10, (val, v)
# r2376+c54.158 -- and the two halves of that negative, stated exactly: the r-line cross-ratio
# takes DIFFERENT values at r0 = 1/5 and r0 = 1/2 (so it is not a family invariant), and it is
# exactly 1 -- the degenerate cross-ratio -- at the Nariai value r0 = 1/sqrt(3).
assert sp.simplify(lam.subs(r0, 1/sp.sqrt(3)) - 1) == 0
assert sp.simplify(lam.subs(r0, sp.Rational(1, 5)) - lam.subs(r0, sp.Rational(1, 2))) != 0

print("\n" + "="*78)
print("STEP 3 — the 120-degree structure is in the SKY ANGLE, not the r-line.")
print("  P3: r0 = (2/sqrt3) sin w, and the three roots are the three preimages of 3w")
print("  under the sine -- i.e. w, w+120, w+240.  On the unit circle: three points 120 apart.")
w = sp.symbols('w', real=True)
z = [sp.exp(sp.I*(w + 2*sp.pi*k/3)) for k in range(3)]
lam3 = sp.simplify(((z[0]-z[2])*(z[1]-0))/((z[1]-z[2])*(z[0]-0)))
lam3 = sp.simplify(sp.expand_complex(sp.simplify(lam3)))
print("\n   cross-ratio (z0, z1; z2, 0)  =", sp.nsimplify(sp.simplify(lam3)))
for val in [0, sp.pi/7, sp.pi/5, sp.pi/3]:
    v=sp.simplify(lam3.subs(w,val))
    print(f"   w = {str(sp.nsimplify(val)):8s} -> {sp.nsimplify(sp.simplify(v))}   ~ {sp.N(v,10)}")
print("\n   EQUIANHARMONIC test: lambda^2 - lambda + 1 = 0  (lambda = exp(+-i.pi/3))")
test = sp.simplify(lam3**2 - lam3 + 1)
print("   lambda^2 - lambda + 1 =", sp.nsimplify(sp.simplify(test)))
print("   |lambda| =", sp.simplify(sp.Abs(lam3)), "   arg(lambda)/pi =", sp.simplify(sp.arg(lam3)/sp.pi))
# r2376+c54.158 -- pins Q4's positive result, the figure receipts/INDEX.md quotes: on the sky angle
# the three roots taken with the centre give lambda = 1/2 + sqrt(3)i/2 = exp(i.pi/3) EXACTLY, and
# CONSTANT in w -- w does not appear in it at all, which is the invariance claim -- with modulus 1
# and argument pi/3.  That is the EQUIANHARMONIC value: lambda^2 - lambda + 1 = 0 identically.
assert sp.simplify(lam3 - (sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2)) == 0
assert w not in lam3.free_symbols                       # constant in w: the invariance
assert sp.simplify(test) == 0                           # equianharmonic: lambda^2 - lambda + 1 = 0
assert sp.simplify(sp.Abs(lam3)) == 1
assert sp.simplify(sp.arg(lam3)/sp.pi) == sp.Rational(1, 3)

print("\n" + "="*78)
print("STEP 4 — WHAT THE EQUIANHARMONIC VALUE MEANS, and the honest weight.")
print("="*78)
print("  (a) lambda = exp(i.pi/3) is the UNIQUE cross-ratio fixed by the FULL S_3 action on")
print("      cross-ratios.  Permuting four points sends lambda through the six-value orbit")
print("      {L, 1/L, 1-L, 1/(1-L), L/(L-1), (L-1)/L}; at the equianharmonic value that orbit")
print("      COLLAPSES to two points {exp(i.pi/3), exp(-i.pi/3)}, i.e. the value is invariant")
print("      up to conjugation under every permutation.  Check the orbit:")
L = sp.Rational(1,2) + sp.sqrt(3)*sp.I/2
orb = [L, 1/L, 1-L, 1/(1-L), L/(L-1), (L-1)/L]
vals = sorted({sp.nsimplify(sp.simplify(sp.expand_complex(x))) for x in orb}, key=str)
print("      orbit =", vals, " -> size", len(vals))
# r2376+c54.158 -- pins STEP 4(a): the six-element anharmonic orbit {L, 1/L, 1-L, 1/(1-L),
# L/(L-1), (L-1)/L} COLLAPSES to exactly TWO points at the equianharmonic value, and they are the
# conjugate pair exp(+-i.pi/3).  A generic cross-ratio has orbit size six; size two is what makes
# this value invariant under the full S_3 up to conjugation, which is the whole claim.
assert len(vals) == 2, vals
assert set(vals) == {sp.Rational(1, 2) + sp.sqrt(3)*sp.I/2,
                     sp.Rational(1, 2) - sp.sqrt(3)*sp.I/2}, vals
print("\n  (b) equianharmonic <=> j-invariant 0 <=> the associated elliptic curve has")
print("      COMPLEX MULTIPLICATION BY omega = exp(2.pi.i/3): the Z_3 the corpus carries.")
print("\n  (c) HONEST WEIGHT: three points 120 apart, taken with their centre, are")
print("      equianharmonic AUTOMATICALLY.  The mathematical content is not the value --")
print("      it is that CR's three vantages ARE at 120 degrees, which P3 forces by the")
print("      triple-angle identity.  So this NAMES a consequence of a forced fact; it does")
print("      not add one.  What it adds is the classical name and what the name carries.")
print("="*78)
