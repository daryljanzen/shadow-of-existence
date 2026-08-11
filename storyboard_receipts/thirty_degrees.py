"""
[!] VERDICT RETRACTED r1108. THE COMPUTATION BELOW STANDS; ITS CONCLUSION DOES NOT.

    This receipt concluded: "the 30 RHYMES on its 3 and COINCIDES on its 4 ... the
    kaleidoscope's 4 is CHOSEN ... every n coprime to 3 closes evenly; the geometry does
    not prefer 4." ** ALL FALSE. ** See one_thirty.py and why_not_eight.py:
      * sin w = 1/2 (the hinge at 2a) FORCES sin 3w = 1 by the triple-angle identity, so
        the hole's half-angle and P3's Nariai dial angle are ONE EVENT, not two 30s;
      * the dial's physical period is 90 (the physics is invariant under {front/back} x
        {mirror} and under no quarter), so the stamp's step IS the period and n=4 is
        forced -- n=8 is redundant, not arbitrary;
      * hence 12 = 3 x 4 with both factors forced BY ONE ROUTE, and the two 30s are one.

    ** WHY IT WAS WRONG, and this is the reusable part: it asked "WHICH n CLOSES THE
       STAMP?" -- a question about the figure -- and never asked "WHAT DOES THE HINGE'S
       OWN SINE DO?" -- a question about the hole. ** It tested the construction's output
    and never interrogated its input. Every n coprime to 3 does close the stamp; that is
    true and it is beside the point, because the stamp is not free -- it must match the
    dial, and the dial is set by the sine at the hinge.

    KEPT, NOT DELETED (THE_CODA s"The negatives are the map"): the enumeration of the n's
    is correct and reusable, and the failure is the record of an instrument pointed at the
    wrong object. Daryl's instinct against it was right and this node's was not.
"""
"""
WALKING THE 30 DEGREES -- the branch I filed as a kept negative without walking it.
(Daryl's thread, r1086: "either the twelve-fold structure has something to do with the
dial's critical angle, or 30 shows up twice for unrelated reasons. That's exactly the
kind of thing the geometry can answer." -- It said GO ANSWER IT. I wrote "no shared
mechanism on the table" and never went. That is declaring the absence of structure
from the failure to have found it, CODA_FIELD_NOTE July 3.)

THE TWO 30s:
  (i)  the kaleidoscope : 3 hinges x 4 quarter-turns = 12 -> 360/12 = 30 deg
  (ii) the Nariai dial  : 2M = (2/3sqrt3) sin 3w peaks at 3w = 90 -> w = 30 deg

The storyboard says (i) arrives "from pure combinatorics, with no reference to the
slicing." So the question that decides it: IS THE FOUR FORCED, OR CHOSEN?
"""
import numpy as np

print("="*76)
print("(1)  Where does each 30 actually come from? Factor them.")
print("="*76)
print("  (ii) THE DIAL.  2M = (2/3sqrt3) sin(3w).  A sine peaks at a QUARTER PERIOD.")
print("       So Nariai (the maximal-mass member) sits at 3w = 90 = 360/4.")
print("            w_Nariai = (1/3) x (360/4) = 360/(3x4) = 360/12 = 30 deg")
print("       The 3 is the TRIPLE ANGLE. The 4 is the sine's quarter period --")
print("       i.e. that a maximum is a QUARTER TURN from a zero. Both forced.")
print()
print("  (i)  THE KALEIDOSCOPE.  3 hinges (120 apart) x 4 quarter-turns:")
print("            spacing = 360/(3x4) = 360/12 = 30 deg")
print("       The 3 is the hinge triangle. The 4 is ... the rotation that was chosen.")
print()
print("  >> BOTH ARE 360/(3x4). Same 3. The question is entirely whether it is the same 4.")

print()
print("="*76)
print("(2)  Is the four-fold FORCED by the stamp's geometry?  Test it: try every n.")
print("="*76)
print("  Stamp the 3 hinges under Z_n (rotation by 360/n) and see what closes:")
print(f"  {'n':>3} {'gcd(3,n)':>9} {'hinges':>7} {'spacing':>9}   even?   note")
for n in range(1, 13):
    g = np.gcd(3, n)
    hinges = 3*n//g
    orbit = sorted({(120*i + (360//n)*k) % 360 for i in range(3) for k in range(n)})
    gaps = {round((orbit[(i+1) % len(orbit)] - orbit[i]) % 360, 6) for i in range(len(orbit))}
    even = len(gaps) == 1
    note = ""
    if n == 4: note = "<-- the chosen one: 30 deg"
    if g > 1:  note = "3 and n share a factor: copies collide"
    print(f"  {n:>3} {g:>9} {len(orbit):>7} {(360/len(orbit)) if even else float('nan'):>9.2f}   "
          f"{'yes' if even else 'NO ':>5}   {note}")
print()
print("  => EVERY n coprime to 3 closes evenly. n=2 -> 60 deg. n=4 -> 30. n=5 -> 24.")
print("     n=7 -> 17.14. There is NOTHING in the stamp that selects n=4.")
print("     The '3 and 4 are coprime, so it lands evenly' is TRUE and is NOT a forcing:")
print("     coprimality explains why 4 CLOSES, never why 4.")

print()
print("="*76)
print("(3)  So is there a four-fold anywhere in the stamp? Enumerate its angles.")
print("="*76)
ang = {
    "hinges":                 [0, 120, 240],
    "tangent pts (crossings)":[60, 180, 300],
    "hinge->pole hit (0.8,+-0.6)": [round(np.degrees(np.arctan2(0.6, 0.8)), 2),
                                    round(np.degrees(np.arctan2(-0.6, 0.8)) % 360, 2)],
    "poles (a diameter)":     [90, 270],
}
for k, v in ang.items():
    print(f"  {k:28s} {v}")
print()
print("  The RIGHT ANGLES the stamp genuinely contains:")
print("   * the Thales tangent at the hinge is VERTICAL (90 to the radius);")
print("   * the two 45-degree chords meet the back at (-1,0) ORTHOGONALLY;")
print("   * the poles (0,+-1) are a DIAMETER, and a diameter is seen at 90.")
print()
print("  These are ORTHOGONALITIES -- angles BETWEEN lines. NOT a Z4 rotational orbit")
print("  of the figure. An orthogonality does not generate a quarter-turn symmetry any")
print("  more than a rectangle's corners make it 4-fold symmetric about its centre.")
print("  The pole pair {90,270} IS a genuine Z2 -- and 3 x 2 = 6 gives 60 deg, NOT 30.")

print()
print("="*76)
print("VERDICT -- and it is not the one I filed")
print("="*76)
print("  I filed: 'two 30s until a mechanism links them; no shared mechanism on the")
print("  table.' WALKED, it is sharper and it cuts BOTH ways:")
print()
print("  * BOTH 30s ARE 360/(3x4), with the SAME 3 (the triple angle / three hinges).")
print("    That much is a real, shared factorisation -- MORE than I credited.")
print()
print("  * BUT THE FOURS ARE DIFFERENT ANIMALS, and this is the finding:")
print("      - the DIAL's 4 is FORCED: it is the quarter period of a sine, i.e. that a")
print("        maximum sits a quarter turn from a zero. Nothing chooses it.")
print("      - the KALEIDOSCOPE's 4 is a CHOSEN rotation. The stamp contains 3-fold")
print("        structure, 2-fold structure (the poles), and orthogonalities -- but no")
print("        4-fold ORBIT. Every n coprime to 3 closes evenly; the geometry does not")
print("        prefer 4.")
print()
print("  => The kaleidoscope's 30 is NOT 'produced by pure combinatorics'. It is")
print("     produced by 3 (forced) and 4 (chosen). Choose n=5 and the same construction")
print("     'produces' 24 degrees, and it would look exactly as suggestive.")
print()
print("  >> THE HONEST STATEMENT: the coincidence is REAL but it is ONE FACTOR DEEP,")
print("     not two. The 3 is genuinely shared -- the triple angle is the hinge triple,")
print("     and that IS the corpus's own three-fold. The 4 is shared only as a number.")
print("     The 30 therefore rhymes on its 3 and coincides on its 4.")
print()
print("  >> AND THE LIVE QUESTION THIS EXPOSES, which nobody has asked: the dial's 4 is")
print("     'a maximum is a quarter turn from a zero'. If the kaleidoscope's quarter")
print("     turn could be DERIVED from the same fact -- from the Thales VERTICAL tangent")
print("     at the hinge, which is exactly a 'quarter turn from' statement -- the two")
print("     30s would become one. That is a real, well-posed, unattempted geometric")
print("     question. NOT 'no mechanism on the table': a NAMED, UNRUN one.")
print("     (The uncertainty is the map of where to reach, not the excuse to stop.)")
