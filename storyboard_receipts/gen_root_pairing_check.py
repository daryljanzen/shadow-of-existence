#!/usr/bin/env python3
"""
!! RETRACTED r1132 — THIS RECEIPT IS A STRAW MAN. KEPT AS THE RECORD, NOT AS A RESULT. !!

Its section (3) posits "if the three planes share the sky angle w" and kills the
generation<->root pairing on that premise. THE PREMISE IS NOT THE GEOMETRY.
The wall is defined RELATIVE TO ITS HINGE, and the other two hinges are distinct
relative to it: three vantages 120 deg apart at 2a on their common incircle,
distinct BY CONSTRUCTION (P3 sec:hinge-geometry). There is no degeneracy to find.
The construction is worked and coherent; this receipt manufactured a door in it.

THE LESSON, and it is the only thing here worth carrying:
  A RECEIPT INHERITS ITS PREMISE. A gate that writes the premise can rig the
  question without noticing -- the rigged-discriminator failure (THE_CODA
  "The source answers back"), committed in code, where the assert lends it
  authority it has not earned. Sections (1) and (2) are sound and reproduce
  P14's claims; section (3) tests a configuration the geometry does not have.
"""

import numpy as np
np.set_printoptions(precision=6, suppress=True)
a = 1.0                          # alpha gauge
print("== SOURCE FACTS (not assumed — quoted) ==")
print("P14 §count : hinges polar 0/120/240 at radius 2a; walls polar 180/300/60 on the throat, each ANTIPODAL to its hinge; Z_3-orbit.")
print("P3  §hinge : each hinge DESIGNATES one horizon root as its OWN black-hole horizon; Weyl S_3 = the relation among the three hinges.")
print("P14 §family: EACH PLANE CARRIES THE SAME THREE HORIZON VALUES.")
print("P3  §gnomonic: r_0 = (2/sqrt3) sin w ;  2M = (2/(3 sqrt3)) sin 3w")
print()

# (1) wall = hinge antipode?  Z_3 index preserved?
hinge = np.array([0.,120.,240.])
wall  = np.array([180.,300.,60.])
print("== (1) wall = hinge + 180 (mod 360), index-preserving? ==")
ok1 = np.allclose((hinge+180.)%360., wall%360.)
print("   (hinge+180)%360 =", (hinge+180.)%360., " vs walls =", wall, " ->", "PASS" if ok1 else "FAIL")

# (2) the three roots of ONE cubic at a given 2M — same for every plane (P14)
def roots(w_deg):
    w = np.deg2rad(w_deg)
    twoM = (2/(3*np.sqrt(3)))*np.sin(3*w)
    # horizon cubic r^3 - r + 2M = 0  (alpha=1 gauge, P12 §237)
    return np.sort(np.roots([1,0,-1,twoM]).real), twoM

for w in (30., 15., 22.5):
    R,twoM = roots(w)
    print(f"   w={w:5.1f}deg  2M={twoM:+.6f}  roots={R}  sum={R.sum():+.2e}")
print("   -> roots sum to zero (A_2), and the triple is a property of 2M ALONE:")
print("      every plane at the same 2M carries the SAME three values. (P14 confirmed)")
print()

# (3) THE TEST: does each hinge designate a DISTINCT root?
print("== (3) THE PAIRING — do three hinges designate three DISTINCT roots? ==")
print("   P3: r_0 IS the designated root, and r_0 = (2/sqrt3) sin w.")
print("   So the designation is fixed by the plane's OWN sky angle w, not by its hinge's polar angle.")
print("   Three planes on three hinges, all reading the SAME geometry, share one 2M (P14).")
w0 = 30.
R,twoM = roots(w0)
r0_from_w = (2/np.sqrt(3))*np.sin(np.deg2rad(w0))
print(f"   At w=30 (Nariai): r_0 from gnomonic = {r0_from_w:.6f}; roots = {R}")
print(f"   r_0 matches a root? {np.min(np.abs(R-r0_from_w)):.2e} -> {'YES' if np.min(np.abs(R-r0_from_w))<1e-9 else 'NO'}")
print()
print("== VERDICT ==")
print("   (1) PASS  — wall/hinge is an index-preserving Z_3 map; the four-way bijection's")
print("               wall<->hinge leg holds.")
print("   (2) PASS  — every plane carries the same three values (P14's claim reproduced).")
print("   (3) NOT ESTABLISHED — and this is the finding. The designation r_0 is fixed by the")
print("       plane's SKY ANGLE w, and NOTHING IN THE SOURCE SAYS the three hinges' planes")
print("       carry three DIFFERENT w. If they share w (one geometry, one 2M, three vantages),")
print("       they designate the SAME root, and the pairing generation<->root COLLAPSES to a")
print("       constant map — three generations, one designated root.")
print("   => The composed corollary DOES NOT FOLLOW from the sourced facts. P3's 'hop to a")
print("      neighbouring vantage' transposes roots ACROSS the S_3 orbit; whether the three")
print("      PHYSICAL walls sit at three different w is a separate claim NEITHER paper makes.")
