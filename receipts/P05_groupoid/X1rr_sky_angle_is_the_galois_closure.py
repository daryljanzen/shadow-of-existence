"""X1rr — the cover tower, CORRECTED AGAIN (r1881).  The r1874 correction had two errors of its own:
   (A) it called the dial's deck group D_6.  The deck group must PRESERVE 2M, and P3's D_6 generators
       (w -> w+60deg, w -> -w) NEGATE it.  D_6 is the dial's full symmetry INCLUDING the mass flip.
   (B) it called w -> w+pi the covering involution.  A covering involution must FIX the point below;
       w -> w+pi negates both 2M and r_0.  It IS R, but R is not a covering involution.
   Done correctly, the structure is the GALOIS one -- and it is exact.
ORIGIN: storyboard_receipts/X1rr_sky_angle_is_the_galois_closure.py -- registered r2376 (c54); edit the origin, not this copy."""
import numpy as np, sympy as sp
s, m = sp.symbols('s m')            # s = sin w ;  m = 2M
print("="*78); print("X1rr — THE SKY ANGLE IS THE GALOIS CLOSURE OF THE HORIZON CUBIC"); print("="*78)

print("\nSTEP 1 — the deck group of the dial, correctly: the maps PRESERVING 2M.")
f2M=lambda w: 2/(3*np.sqrt(3))*np.sin(3*w); fr0=lambda w: 2/np.sqrt(3)*np.sin(w)
for w in [0.31,1.07]:
    print(f"   w={w:.2f}:  tau: w+2pi/3 -> 2M {f2M(w+2*np.pi/3):+.6f}   sigma: pi/3-w -> 2M {f2M(np.pi/3-w):+.6f}"
          f"   (2M = {f2M(w):+.6f})")
    # r2376+c54.158 -- pins STEP 1, which is the r1881 correction itself: P5's own generators tau
    # (w -> w + 2pi/3) and sigma (w -> pi/3 - w) PRESERVE 2M -- printed +0.308544 at w=0.31 and
    # -0.026309 at w=1.07, the same value from all three -- and that is what qualifies them as
    # deck transformations of the dial over the mass plane.  P3's D_6 generators do NOT (STEP 6).
    assert abs(f2M(w + 2*np.pi/3) - f2M(w)) < 1e-12, w
    assert abs(f2M(np.pi/3 - w) - f2M(w)) < 1e-12, w
# and the printed figures themselves
assert abs(f2M(0.31) - 0.308544) < 5e-7
assert abs(f2M(1.07) - (-0.026309)) < 5e-7
print("   tau (order 3) and sigma (order 2) -- P5's OWN generators -- and P5 prop:tau: they generate S_3.")
print("   *** THE DIAL'S DECK GROUP OVER 2M IS S_3, ORDER 6 = the cover's degree: the cover is REGULAR. ***")

print("\nSTEP 2 — the field tower, computed.")
r0 = 2*s/sp.sqrt(3)
M2 = sp.simplify(sp.Rational(2,3)/sp.sqrt(3)*(3*s-4*s**3))     # (2/3sqrt3) sin 3w with sin3w=3s-4s^3
print("   with s = sin w :  r_0 =", sp.simplify(r0), " ,  2M =", sp.simplify(M2))
poly = sp.simplify(sp.expand(r0**3 - r0 + M2))
print("   check r_0 is a root:  r_0^3 - r_0 + 2M =", poly)
print("   so [Q(2M, s) : Q(2M)] = 3   (s satisfies the cubic 3s - 4s^3 = (3sqrt3/2).2M)")
# r2376+c54.158 -- pins STEP 2 as an EXACT identity in s = sin w, which is what the printed 0 on
# the line above means: r_0 = 2 sin(w)/sqrt(3) with 2M = (2/3sqrt3) sin 3w satisfies the horizon
# cubic r^3 - r + 2M = 0 identically -- the sky angle really does parametrise a root, so the dial
# sits over the mass plane by degree 3 and Q(2M, s) is a genuine cubic extension.
assert sp.simplify(poly) == 0
assert sp.simplify(r0**3 - r0 + M2) == 0
assert sp.degree(sp.Poly(sp.expand(3*s - 4*s**3), s)) == 3

print("\nSTEP 3 — but the OTHER two roots need cos w as well:")
w=sp.symbols('w')
for lab,a in [('w', w), ('pi/3 - w', sp.pi/3-w), ('-pi/3 - w', -sp.pi/3-w)]:
    e=sp.simplify(sp.expand_trig(2*sp.sin(a)/sp.sqrt(3)))
    print(f"     root at {lab:>10s} :  {e}")
# r2376+c54.158 -- pins STEP 3, the degree-2 step that makes the tower 3 x 2 = 6: the FIRST root
# is 2 sin(w)/sqrt(3), free of cos w, but the other two expand to cos(w) -+ sin(w)/sqrt(3) -- they
# genuinely CARRY cos w, so the splitting field needs the further square root cos w = sqrt(1 -
# sin^2 w).  If all three roots were expressible in sin w alone the tower would be degree 3 and
# the sky angle would not be the Galois closure, which is exactly what this receipt asserts it is.
assert not sp.simplify(sp.expand_trig(2*sp.sin(w)/sp.sqrt(3))).has(sp.cos(w))
assert sp.simplify(sp.expand_trig(2*sp.sin(sp.pi/3 - w)/sp.sqrt(3))
                   - (sp.cos(w) - sp.sin(w)/sp.sqrt(3))) == 0
assert sp.simplify(sp.expand_trig(2*sp.sin(-sp.pi/3 - w)/sp.sqrt(3))
                   - (-sp.cos(w) - sp.sin(w)/sp.sqrt(3))) == 0
print("   The second and third carry cos w. So the SPLITTING field is Q(2M, sin w, cos w),")
print("   and cos w = sqrt(1 - sin^2 w) is a further degree-2 step:  [split : Q(2M)] = 3 x 2 = 6.")

print("\nSTEP 4 — AND THAT IS THE DIAL.  Degree 6 over 2M, Galois group S_3.")
print("   *** SO THE SKY ANGLE IS THE GALOIS CLOSURE (the splitting cover) OF THE HORIZON CUBIC, ***")
print("   *** and the root cover -- 3 sheets, NOT Galois -- is the intermediate field Q(2M, r_0).  ***")

print("\nSTEP 5 — the covering involution of dial -> root cover, and what it is:")
for w0 in [0.31,1.07,2.2]:
    ok = np.isclose(f2M(np.pi-w0),f2M(w0)) and np.isclose(fr0(np.pi-w0),fr0(w0))
    print(f"     w={w0:.2f}: w -> pi-w fixes (2M, r_0)? {ok}   and cos w: {np.cos(w0):+.5f} -> {np.cos(np.pi-w0):+.5f}")
    # r2376+c54.158 -- rule 7: the receipt computes this PASS/FAIL and only PRINTS it.  Pin it,
    # and with it error (B) of the r1874 pass: w -> pi - w FIXES both 2M and r_0 (so it is a
    # covering involution) while NEGATING cos w by a nonzero amount -- printed +0.95233 ->
    # -0.95233 at w=0.31 -- which is what makes it the Galois involution of the final square root.
    assert ok, w0
    assert abs(np.cos(np.pi - w0) + np.cos(w0)) < 1e-12, w0
    assert abs(np.cos(w0)) > 0.4, w0        # cos w is genuinely moved, not accidentally at a zero
print("   w -> pi - w fixes sin w and negates cos w.")
print("   *** IT IS THE GALOIS INVOLUTION OF THE FINAL SQUARE ROOT, cos w = sqrt(1 - sin^2 w). ***")
print("   It is NOT R: R negates 2M and r_0, and a covering involution fixes them.")

print("\nSTEP 6 — where R actually sits.  R: w -> w + pi negates 2M and r_0 together.")
print("   It is not IN the deck group of w -> 2M (it moves 2M); it is the extra Z_2 by which")
print("   Aut(A_2) = S_3 x Z_2 = D_6 exceeds the Galois group, relating the two Nariai sign-halves.")
print("   *** So D_6 is NOT a Galois group of this tower: S_3 is, and R adjoins the mass sign. ***")
# r2376+c54.158 -- pins STEP 6, which is error (A) of the r1874 pass and the sentence STEP 6 states
# with no computation behind it: R (w -> w + pi) NEGATES both 2M and r_0, and so does P3's D_6
# rotation w -> w + pi/3.  Neither preserves the mass, so neither is in the deck group of w -> 2M
# and neither is the covering involution -- which is precisely why the dial's deck group is S_3
# and not D_6, and why R is the EXTRA Z_2 by which Aut(A_2) exceeds the Galois group.
for _w0 in [0.31, 1.07, 2.2]:
    assert abs(f2M(_w0 + np.pi) + f2M(_w0)) < 1e-12, _w0        # R negates 2M
    assert abs(fr0(_w0 + np.pi) + fr0(_w0)) < 1e-12, _w0        # R negates r_0
    assert abs(f2M(_w0 + np.pi/3) + f2M(_w0)) < 1e-12, _w0      # P3's D_6 rotation negates 2M too
    assert abs(f2M(_w0)) > 1e-3, _w0                            # and 2M is nonzero, so that is a real sign flip
print("="*78)
