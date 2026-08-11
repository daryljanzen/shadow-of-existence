#!/usr/bin/env python3
"""
L8.1-e · THE 120 — receipt.  Lane 8, the combinatorics ledger.
CLAIM UNDER TEST (written first):
    "the bead's 120:240 arc split and the Z_3's 120 deg (three hinges at 0/120/240,
     the dial's w -> w+120) are ONE 120."
It can return YES: both are 360/3 and both live on the same cubic.
SOURCES (verbatim):
  §0 : "the lap's flattened map X1 = -a cos(2 pi r / sqrt3 a) is LINEAR in r, so the arc
        ratio IS the root ratio (verified: +a/sqrt3 -> 120.00 deg, -2a/sqrt3 -> -240.00 deg)"
        ... "Daryl's 'the asymmetry -- Nariai, 1/3 vs 2/3' is THIS 2, and it is forced."
  P3 : r_0 = (2/sqrt3) sin w      (prop:gnomonic)
  P7 : "Each bead splits its wrap 120 deg before its turn at r=0 and 240 deg after."
"""
import numpy as np
a=1.0; D=np.deg2rad
rho   = a/np.sqrt(3)          # the DOUBLE root at Nariai
back  = -2*a/np.sqrt(3)       # the single root
phase = lambda r: np.rad2deg(2*np.pi*r/(np.sqrt(3)*a))   # the lap's flattened map, LINEAR in r
r0    = lambda w: (2/np.sqrt(3))*a*np.sin(D(w))          # the dial, SINUSOIDAL in w

print("== 1. the arc split, recomputed from the lap map ==")
for n,r in (("seam  +a/sqrt3",rho),("r = 0        ",0.0),("back -2a/sqrt3",back)):
    print(f"   {n}: r={r:+.6f}  arc phase = {phase(r):+8.3f} deg")
print(f"   seam->0 = {phase(rho)-phase(0):+.2f} deg ;  0->back = {phase(0)-phase(back):+.2f} deg")
print(f"   => the split is {abs(phase(rho)):.0f} : {abs(phase(back)):.0f}  = 1 : 2   (sums to 360)")
print(f"   root span rho-(-2rho) = 3rho = {3*rho:.6f} = sqrt3*a = the map's PERIOD: "
      f"{np.isclose(3*rho, np.sqrt(3)*a)}")

print("\n== 2. the Z_3, on the dial ==")
nar=[30.,150.,270.]
print("   Nariai <=> sin3w = 1 -> 3w = 90 + 360k -> w = 30,150,270 (spacing 120 deg)")
for w in nar:
    print(f"     w={w:5.1f}  r0={r0(w):+.6f}   arc phase of that r0 = {phase(r0(w)):+8.3f} deg")

print("\n== 3. THE TEST: does the dial's Z_3 push forward to a Z_3 on the arc? ==")
ph=[round(phase(r0(w)),6) for w in nar]
print(f"   dial positions   {nar}   spacing 120,120,120  -> a free Z_3")
print(f"   their arc phases {ph}")
print(f"   distinct arc phases: {len(set(ph))} of 3  <-- THE WITNESS")
print("   w=30 and w=150 are DISTINCT dial positions with the SAME arc phase (+120).")
print("   The double root's two branches are SEPARATED on the dial and IDENTIFIED on the arc.")
print("   => the map dial->arc is 2:1 there; a free Z_3 cannot push forward to a free Z_3.")
print("   VERDICT: NO -- the two 120s are not one 120.  PROVED by exhibited collapse.")

print("\n== 4. WHAT THE ARC'S 120 ACTUALLY IS — and it is a 2, not a 3 ==")
print("   The arc split is 120:240 = 1:2 -- an ASYMMETRIC two-part ratio, NOT 1:1:1.")
print(f"   It is 360 * rho/(3rho) = 360 * {rho/(3*rho):.4f} = {360*rho/(3*rho):.0f} deg :")
print("   the 1/3 is the DOUBLE ROOT'S SHARE OF THE ZERO-SUM SPAN, not a threefold symmetry.")
print("   §0 says so in its own words: \"Daryl's 'the asymmetry -- Nariai, 1/3 vs 2/3' is")
print("   THIS 2, and it is forced.\"   The 120:240 belongs to the 2 FAMILY.")
print("   The Z_3's 120 is 360/3 with 3 = the NUMBER OF ROOTS (L8.1-a, the dial).")
print("   Same numeral, two different objects: a LENGTH RATIO vs a COUNT.")

print("\n== 5. CONTROL — the collapse is bought by the DOUBLE root; off Nariai it lifts ==")
for w0 in (30.0, 20.0):
    ws=[w0,w0+120,w0+240]
    rs=[r0(w) for w in ws]; ps=[round(phase(r),4) for r in rs]
    twoM=(2/(3*np.sqrt(3)))*np.sin(3*D(w0))
    print(f"   w0={w0:5.1f} (2M={twoM:+.5f}): arc phases {ps}  distinct={len(set(ps))}")
print("   Off Nariai the three arc phases are DISTINCT (3 of 3) -- but they are NOT equally")
print("   spaced, so still no Z_3 on the arc.  At Nariai two collapse.  Either way the arc")
print("   carries no threefold symmetry: the test is not vacuous, and it fails for two")
print("   independent reasons.")

print("\n== VERDICT ==")
print("   NO -- the arc's 120 and the Z_3's 120 are NOT one 120.  PROVED:")
print("   (i) the dial's free Z_3 collapses 2:1 onto the arc at Nariai (w=30,150 -> +120);")
print("   (ii) the arc split is 1:2 (an asymmetry, a LENGTH RATIO), the Z_3 is 1:1:1 (a COUNT).")
print("   The arc's 120:240 is §0's forced 2 -- 'the asymmetry, 1/3 vs 2/3' -- wearing a 3's")
print("   clothes because 360*(1/3) and 360/3 are the same numeral.")
