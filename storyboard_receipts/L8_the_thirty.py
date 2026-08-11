#!/usr/bin/env python3
"""
L8.1-f · THE 30 / THE 60 — receipt.  Lane 8, the combinatorics ledger.
CLAIMS (written first, split per the indexing rule):
  A: "the hinge's subtended half-angle (30 deg) and the dial's fundamental domain (30 deg)
      are ONE 30."
  B: "the hole's 60 deg subtense at the hinge and the dial rotation w -> w+60 are ONE 60."
Either can return NO: A's two 30s have DIFFERENT derivations -- arcsin(1/2) from Euclid,
vs 120/4 from the sine's period.  If they merely agree numerically, that is the
"same numeral, two objects" NO (cf. L8.1-e).
SOURCE (P3, verbatim, and it names the trap): "the subtended half-angle is the sky angle,
  sin w = 1/2, whence sin 3w = 3(1/2) - 4(1/2)^3 = 1, its maximum -- so the tangent from
  the hinge is the Nariai cut NOT BECAUSE TWO ANGLES OF 30 DEG COINCIDE but because the
  identity peaks there of its own accord ONCE THE HOLE HAS PLACED THE HINGE."
"""
import numpy as np
a=1.0
def w_of_d(d): return np.rad2deg(np.arcsin(a/d))      # hole radius a seen from distance d
def s3(wdeg):  w=np.deg2rad(wdeg); return 3*np.sin(w)-4*np.sin(w)**3

print("== 1. the two 30s, each by ITS OWN route (no borrowing) ==")
w_geo = w_of_d(2*a)                                    # Euclid: hinge at 2a (prop:twoalpha, an OUTPUT)
print(f"   (i)  GEOMETRIC : hinge at d=2a -> sin w = a/2a = 1/2 -> w = arcsin(1/2) = {w_geo:.6f} deg")
per = 120.0                                            # period of sin(3w) in w
print(f"   (ii) SPECTRAL  : sin 3w has period {per:.0f} deg ; a sine peaks a QUARTER-period")
print(f"                    from its zero -> {per}/4 = {per/4:.6f} deg  (the fundamental domain [0,30])")
print(f"   equal: {np.isclose(w_geo, per/4)}   <- but agreement is NOT the test (L8.1-e)")

print("\n== 2. THE TEST for A: is it one object, or two that agree at one point? ==")
print("   P3's claim: the hole PLACES the hinge, sin w = 1/2 follows, and THEN the identity")
print("   peaks OF ITS OWN ACCORD.  So the weld is: geometry fixes sin w ; the identity does")
print("   the rest with NO new input.  Check the identity at the geometric value:")
print(f"     sin 3w at w = arcsin(1/2) : {s3(w_geo):.12f}   is it the maximum (=1)? {np.isclose(s3(w_geo),1)}")
print("   The identity 3s - 4s^3 attains its max at s = 1/2 -- verify by calculus, not by luck:")
print("     d/ds (3s - 4s^3) = 3 - 12 s^2 = 0  =>  s^2 = 1/4  =>  s = 1/2.")
print(f"     check: 3 - 12*(0.5)^2 = {3-12*0.25:.1f}  (stationary), and 3(1/2)-4(1/2)^3 = {s3(30):.1f}")
print("   => sin w = 1/2 is EXACTLY the stationary point of the triple-angle map.")
print("   The GEOMETRY delivers sin w = 1/2 ; the IDENTITY's peak is AT sin w = 1/2.")
print("   One object: the map s -> 3s - 4s^3, evaluated where the hole puts it.  VERDICT A: YES.")

print("\n== 3. CONTROL for A — move the hinge and BOTH 30s must die together ==")
print("   If the two 30s were independent, moving the hinge would break one and not the other.")
for d in (2.0, 2.5, 3.0, 1.5):
    w=w_of_d(d*a); print(f"   hinge at d={d:4.2f}a : sin w = {a/d:.4f}  w = {w:7.3f} deg   "
                         f"sin3w = {s3(w):+.6f}   Nariai? {np.isclose(s3(w),1)}")
print("   Only d=2a gives sin w = 1/2 -> sin 3w = 1.  Off 2a the geometric angle moves AND")
print("   the identity stops peaking -- TOGETHER, because it is one map evaluated at one point.")
print("   (The spectral 30 = 120/4 never moves: it is the map's own quarter-period.  What moves")
print("    is WHETHER THE HINGE SITS ON IT.  d=2a is what puts it there -- prop:twoalpha.)")

print("\n== 4. CLAIM B: the hole's 60 subtense vs the dial rotation w -> w+60 ==")
sub = 2*w_geo
print(f"   (i)  GEOMETRIC : full subtense = 2 * arcsin(1/2) = {sub:.6f} deg")
half = per/2
print(f"   (ii) SPECTRAL  : half-period of sin 3w = {per:.0f}/2 = {half:.6f} deg ; and w->w+60 flips 2M:")
for wt in (15.,42.,73.):
    print(f"        sin3({wt}+60) = {s3(wt+60):+.6f}   vs  -sin3({wt}) = {-s3(wt):+.6f}   "
          f"{np.isclose(s3(wt+60), -s3(wt))}")
print(f"   equal: {np.isclose(sub, half)}")
print("   THE TEST: the subtense is 2 x (quarter-period) ; the rotation is 1 x (half-period).")
print("   2*(P/4) = P/2 IDENTICALLY, for ANY P -- so the equality is an ARITHMETIC TRIVIALITY")
print("   GIVEN A.  It carries no content beyond A: the 60 is the 30 doubled, twice.")
print("   VERDICT B: YES, but DEPENDENT -- it is A's weld read twice, not a second result.")

print("\n== 5. CONTROL for B — is B independent of A?  (it must not be) ==")
for P in (120., 90., 200.):
    print(f"   period P={P:5.1f}: 2*(P/4) = {2*(P/4):6.2f} ; P/2 = {P/2:6.2f} ; equal={np.isclose(2*(P/4),P/2)}")
print("   True for every P => B tests nothing A did not.  Recorded as DEPENDENT, not as a")
print("   second merge.  A ledger counting it separately would be double-counting one weld.")

print("\n== VERDICT ==")
print("   A: YES, ONE 30.  Object: the triple-angle map s -> 3s - 4s^3, whose STATIONARY")
print("      POINT is exactly s = 1/2 -- and the hole, placing the hinge at 2a, delivers")
print("      sin w = 1/2.  Not two angles agreeing: the geometry hands the identity its")
print("      own extremum.  P3 says this in terms ('not because two angles of 30 coincide').")
print("   B: YES but DEPENDENT -- 2*(P/4) = P/2 for any P.  It is A doubled, and is recorded")
print("      as a corollary of A, NOT as a separate weld.")
