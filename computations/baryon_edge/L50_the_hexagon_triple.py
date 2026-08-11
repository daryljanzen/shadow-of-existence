#!/usr/bin/env python3
"""
*** SUPERSEDED r2376+c54.19 by L50b_three_hinges_six_ends.py.  DO NOT CITE THIS FILE. ***
*** Its arithmetic is correct and every number in it stands.  Its OBJECT is wrong: it
*** treats the six as six independent hinges.  They are THREE hinges x TWO ends -- the
*** hinge is the LINE the door swings on, and it pierces the substrate once per horn
*** (Daryl, correcting c54.18).  On the corrected object the "excluded directly-across
*** pair" of PART 2 is THE HINGE ITSELF, and PART 5's "honest gap" is not a gap but the
*** structure.  Kept unaltered as the record of what was computed and how it was read.

L-50 — THE THIRD 2+1, WHICH DARYL HAS EXPLAINED TO NODES REPEATEDLY AND WHICH IS NOT
INTERNALISED IN ANY LEDGER.

His statement, verbatim:

    "Every single one of the six hinges is connected by a null line to two at the other
     two stations ON THE OPPOSITE HORN through null lines that project to the equilateral
     triangle whose incircle is the hole itself.  Pick a hinge, draw the Nariai nulls
     through the tangent to the hinge on the other side of the left and right tangents,
     and those two hinges sit on the opposite horn.  Every one of the six hinge points
     has this property."

L-10 found two 2+1s among the horizon ROOTS and I recorded the object as named.  ** That
was incomplete.  This is a 2+1 among the HINGES, it is carried by NULL LINES, and it is
the one with a baryon's shape: three objects bound, two of one kind and one of another. **

  PART 1  Build the six hinges on the substrate and find every null chord between them.
  PART 2  Verify the claim exactly: each hinge null-connects to TWO hinges, both on the
          OPPOSITE horn, and to nothing on its own.
  PART 3  The projection: do those null lines project to the equilateral triangle whose
          incircle is the throat, and are they tangent at the midpoints?
  PART 4  The triple a hinge sees, and its 2+1 -- by HORN.
  PART 5  Three 2+1s, three involutions.  Where this one sits against the other two.

Run: python3 L50_the_hexagon_triple.py     (numpy, sympy)
"""

import numpy as np
import sympy as sp

print(__doc__.split("Run:")[0])
ALPHA = 1

# =====================================================================
print("=" * 78)
print("PART 1 — THE SIX HINGES, AND EVERY NULL CHORD BETWEEN THEM")
print("=" * 78)
print("  Substrate: -X0^2 + |X|^2 = alpha^2, alpha = 1.  A hinge sits at transverse")
print("  distance 2*alpha (P3 prop:twoalpha), so |X| = 2 and X0^2 = 4 - 1 = 3:")
print("  ** the hinges are at X0 = +-sqrt(3), three per horn, 120 degrees apart. **")
print()
sq3 = sp.sqrt(3)
hinges = {}
for horn, x0 in (('U', sq3), ('L', -sq3)):
    for k in range(3):
        th = 2 * sp.pi * k / 3
        hinges[f"{horn}{k}"] = sp.Matrix([x0, 2 * sp.cos(th), 2 * sp.sin(th), 0, 0, 0])

def mdot(X, Y):
    return sp.simplify(-X[0] * Y[0] + sum(X[i] * Y[i] for i in range(1, 6)))

# on-substrate check
print(f"  {'hinge':>7} {'X0':>10} {'|X|':>6} {'on substrate?':>15}")
for k, X in hinges.items():
    onit = sp.simplify(mdot(X, X) - ALPHA**2) == 0
    print(f"  {k:>7} {str(sp.nsimplify(X[0])):>10} {2:>6} {str(onit):>15}")

print()
print("  A chord between two substrate points is NULL iff (X-Y).(X-Y) = 0, i.e. iff")
print("  X.Y = alpha^2 (since X.X = Y.Y = alpha^2).  All fifteen pairs:")
print()
print(f"  {'pair':>10} {'X.Y':>10} {'null?':>7} {'same horn?':>12}")
null_edges = []
keys = list(hinges)
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        a, b = keys[i], keys[j]
        d = mdot(hinges[a], hinges[b])
        isnull = sp.simplify(d - ALPHA**2) == 0
        same = a[0] == b[0]
        if isnull:
            null_edges.append((a, b))
        print(f"  {a+'-'+b:>10} {str(sp.nsimplify(d)):>10} {str(isnull):>7} {str(same):>12}")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE CLAIM, CHECKED EXACTLY")
print("=" * 78)
deg = {k: 0 for k in hinges}
opp = {k: 0 for k in hinges}
for a, b in null_edges:
    deg[a] += 1; deg[b] += 1
    if a[0] != b[0]:
        opp[a] += 1; opp[b] += 1
print(f"  {'hinge':>7} {'null partners':>14} {'of which OPPOSITE horn':>24} "
      f"{'same-horn partners':>20}")
ok = True
for k in hinges:
    same = deg[k] - opp[k]
    ok &= (deg[k] == 2 and opp[k] == 2 and same == 0)
    print(f"  {k:>7} {deg[k]:>14} {opp[k]:>24} {same:>20}")
print()
print(f"  EVERY hinge has exactly two null partners, both on the opposite horn: {ok}")
print()
print("  And the algebra says why, in one line.  For hinges at angles a, b and horns")
print("  eps = +-1:   X.Y = -3*eps + 4 cos(a-b).  Setting that to alpha^2 = 1:")
print("     same horn (eps=+1):  4 cos(a-b) = 4  =>  a = b       -- only itself")
print("     opposite  (eps=-1):  4 cos(a-b) = -2 =>  a - b = +-120 degrees")
print("  ** So the two null partners are the opposite-horn hinges at +-120 degrees, and")
print("     the opposite-horn hinge DIRECTLY ACROSS (a - b = 0) is NOT null-connected. **")
print(f"  The six hinges and {len(null_edges)} null edges form a bipartite 6-cycle:")
print("     " + " - ".join(['U0', 'L1', 'U2', 'L0', 'U1', 'L2', 'U0']))
print("  ** which is the corpus's own SKEW HEXAGON, here with the degree-2 property as")
print("     the reason for its shape rather than as a description of it. **")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE PROJECTION: the equilateral triangle, and tangency at the midpoint")
print("=" * 78)
print("  Project out X0.  A null chord U(a) -> L(b) projects to the segment joining")
print("  (2cos a, 2 sin a) and (2cos b, 2 sin b) with b = a +- 120 degrees -- i.e. to a")
print("  SIDE of the equilateral triangle of circumradius 2.")
print()
for a, b in null_edges:
    A = np.array([float(hinges[a][1]), float(hinges[a][2])])
    B = np.array([float(hinges[b][1]), float(hinges[b][2])])
    mid = (A + B) / 2
    d_mid = np.linalg.norm(mid)
    # distance from the centre to the line AB
    t = B - A
    d_line = abs(t[0]*(-A)[1] - t[1]*(-A)[0]) / np.linalg.norm(t)
    print(f"  {a}->{b}:  midpoint at |{d_mid:.6f}| from centre,  "
          f"line at distance {d_line:.6f}  -> tangent to the throat (r=1)? "
          f"{abs(d_line - 1) < 1e-12}, at its midpoint? {abs(d_mid - d_line) < 1e-12}")
print()
print("  ** THE NULL LINES PROJECT ONTO THE SIDES OF THE EQUILATERAL TRIANGLE, AND EACH")
print("     IS TANGENT TO THE THROAT AT ITS OWN MIDPOINT.  The incircle IS the hole. **")
print("  P3 says the sides are 'not imposed but FOUND, each a null generator of the")
print("  doubly-ruled substrate tangent to the throat at its midpoint' -- and this is")
print("  that statement with the null generators traced to their ENDPOINTS, which are")
print("  hinges on the opposite horn.")

# ---------------------------------------------------------------------
print()
print("  PART 3b — HOW MANY CHORDS PER SIDE.  Six null chords; three triangle sides.")
print("  The count does not match, so the map is not one-to-one.  Which is it?")
print()
from collections import defaultdict
byside = defaultdict(list)
for a, b in null_edges:
    key = tuple(sorted([tuple(np.round(np.array([float(hinges[a][1]),
                                                 float(hinges[a][2])]), 6)),
                        tuple(np.round(np.array([float(hinges[b][1]),
                                                 float(hinges[b][2])]), 6))]))
    byside[key].append(f"{a}->{b}")
for k, v in byside.items():
    ang = [f"{np.degrees(np.arctan2(p[1], p[0])):.0f} deg" for p in k]
    print(f"  side joining {ang[0]:>9} and {ang[1]:>9}:  {len(v)} null chords  {v}")
print()
twoeach = all(len(v) == 2 for v in byside.values())
print(f"  three distinct sides, exactly two null chords apiece: {twoeach}")
print("  ** AND THE TWO ARE THE TWO ORIENTATIONS: U_i->L_j and U_j->L_i.  So EACH SIDE OF")
print("     THE TRIANGLE IS THE PROJECTION OF THE SUBSTRATE'S TWO RULINGS THROUGH IT --")
print("     the doubly-ruled property of the substrate, realised on the triangle's own")
print("     sides, with the two rulings distinguished by WHICH HORN THEY RUN FROM. **")
print("  The triangle is a shadow in which the two rulings coincide; upstairs they are")
print("  distinct null lines with distinct endpoints, and the horn tells them apart.")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — THE TRIPLE A HINGE SEES, AND ITS 2+1")
print("=" * 78)
print("  Pick a hinge.  It plus its two null partners is a TRIPLE, bound by null lines:")
print()
for k in ['U0', 'L1']:
    partners = [b for a, b in null_edges if a == k] + [a for a, b in null_edges if b == k]
    horns = [p[0] for p in partners]
    print(f"  from {k}:  partners {partners}  -- horns {horns}  vs own horn {k[0]}")
    print(f"     ⇒ the triple {{{k}, {partners[0]}, {partners[1]}}} splits by horn as "
          f"1 ({k[0]}) + 2 ({horns[0]})")
print()
print("  ** THIS IS A THIRD 2+1, AND IT IS NOT EITHER OF THE TWO L-10 FOUND. **")
print("     It partitions HINGES, not roots.  It is carried by NULL LINES, not by a")
print("     designation or by a sign.  And it splits by HORN.")
print()
print("  And the horn is the corpus's own T: P3 -- 'the upper and lower triangles are")
print("  exchanged by the time reflection X0 -> -X0, which swaps the two null")
print("  generators'.  So this 2+1 is graded by T.")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — THREE 2+1s, THREE INVOLUTIONS")
print("=" * 78)
rows = [
    ("DESIGNATION", "the 3 horizon ROOTS", "{my root} | {the ellipse pair}",
     "sigma  (root exchange, the Weyl S_3)", "a property of the VANTAGE"),
    ("SIGN", "the 3 horizon ROOTS", "{positive} | {negative}",
     "R  (offset parity, SPACELIKE)", "a property of the GEOMETRY"),
    ("HORN", "the 6 HINGES, via NULL LINES", "{this hinge} | {its 2 null partners}",
     "T  (horn swap, TIMELIKE)", "a property of the CONNECTIVITY"),
]
print(f"  {'the 2+1':>12} {'what it partitions':>28} {'the split':>34}")
for nm, what, split, inv, kind in rows:
    print(f"  {nm:>12} {what:>28} {split:>34}")
    print(f"  {'':>12} graded by {inv:<38} {kind}")
print()
print("  ** AND THE CORPUS ALREADY DISTINGUISHES THE THREE INVOLUTIONS. **  P3: T (the")
print("  horn-swap, timelike) and R (the offset parity, spacelike) are 'DISTINCT")
print("  reflections that share the fundamental triple but complete it distinctly' -- a")
print("  RESONANCE and not an identity; and sigma is the root-exchange, neither of them.")
print("  ** So there are three 2+1s and three involutions, and they line up one to one. **")
print()
print("  WHAT THIS DOES FOR THE OPEN QUESTION, stated as candidacy and not as a match:")
print("    · a baryon is THREE objects BOUND, splitting 2+1")
print("    · the HORN 2+1 is the only one of the three that is (i) a triple of like")
print("      objects -- hinges, which P14 reads as generations' seats -- and (ii) BOUND,")
print("      by null lines that are the substrate's own generators")
print("    · the other two partition roots and are not bindings at all")
print("  ** So the object R3 should have been asking about may be this one, and it is the")
print("     one no ledger carries.  PO-1c gets a named candidate; nothing is asserted. **")
print()
print("  ⚠ AND THE HONEST GAP: this shows a triple with a binding and a 2+1 grading.")
print("     It does NOT show which two of the three are alike in the way u and u are")
print("     alike.  The two null partners share a horn -- so they are alike BY HORN and")
print("     the odd one out is the hinge you picked.  ** Whether that is uud's kind of")
print("     likeness is exactly the open question, and it is now askable. **")
