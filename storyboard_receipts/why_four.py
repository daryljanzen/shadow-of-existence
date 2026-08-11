"""
WHY FOUR (r1108). The last open joint. Worked, not asserted.

WHERE WE ARE:
  * the hinge at 2a           -- FORCED (the Thales circle, which is the hole moved onto
                                 its own edge, ends there)
  * the 3 hinges at 0/120/240 -- FORCED (the triple angle; three roots of one cubic)
  * the dial has a Z4         -- FOUND (its axis and the axis's perpendicular; and
                                 perpendicularity is not a choice)
  * a hinge transpose by delta IS a dial turn by -delta -- VERIFIED (the physics depends
                                 only on theta - chi), and the map is an isometry.
  * STILL OPEN: nothing yet forces the STAMP to be 4 rather than n. thirty_degrees.py:
    "every n coprime to 3 closes evenly; the geometry does not prefer 4."

THE CANDIDATE FORCING, and it is Daryl's own shape ("all the symmetries that collapse
equivalent descriptions"):

  ** THE FIGURE MUST BE CLOSED UNDER THE GROUP THAT ACTS ON ITS OWN SLICING. **

  Not a new principle -- a coherence demand. Each hinge carries a dial. The dial has a Z4.
  By the isometry, that Z4 IS a Z4 of HINGE TRANSPOSES. So a figure with a hinge but
  without that hinge's Z4-orbit is a figure whose own slicing structure names positions it
  does not contain. It is incomplete BY ITS OWN LIGHTS.

TEST IT. It either picks 4 or it does not, and it can return "n is free" -- which would
confirm thirty_degrees.py and kill the conjecture.
"""
import numpy as np
from math import gcd

print("="*80)
print("(1)  THE FIGURE'S HINGE SET, for a stamp of order n")
print("="*80)
def hinges(n):
    return sorted({(120*i + (360//n)*k) % 360 for i in range(3) for k in range(n)}) if 360 % n == 0 else None
print(f"  {'n':>3} {'#hinges':>8} {'spacing':>8}  the set is the multiples of...")
for n in (1,2,3,4,5,6,8,12):
    h = hinges(n)
    if h is None: continue
    g = gcd(120, 360//n)
    print(f"  {n:>3} {len(h):>8} {360//len(h) if len(h) else 0:>8}  gcd(120, 360/n) = {g:>3}"
          f"{'   (3 and n share a factor: copies collide)' if gcd(3,n)>1 else ''}")
print()
print("  >> the hinge set is the multiples of  g(n) = gcd(120, 360/n).")

print()
print("="*80)
print("(2)  THE CLOSURE TEST — is the figure closed under a 90-degree hinge transpose?")
print("="*80)
print("  (which, BY THE ISOMETRY, is the dial's own quarter-turn)")
print()
print(f"  {'n':>3} {'#hinges':>8} {'spacing':>8} {'0+90 in the set?':>18}  closed under the dial's Z4?")
ok_n = []
for n in (1,2,3,4,5,6,8,9,10,12,15,16,20):
    if 360 % n: continue
    h = hinges(n)
    closed = all(((x+90) % 360) in h for x in h)
    if closed and gcd(3,n)==1: ok_n.append(n)
    print(f"  {n:>3} {len(h):>8} {360//len(h):>8} {str(90 in h):>18}  "
          f"{'YES' if closed else 'no '}"
          f"{'   <- and coprime to 3' if closed and gcd(3,n)==1 else ('   (collides)' if closed else '')}")
print()
print("  >> ** THE CLOSURE CONDITION IS NOT VACUOUS. It kills n = 5, 9, 10, 15. **")
print(f"     n that pass BOTH (closed under the dial's Z4, and coprime to 3): {ok_n}")
print(f"  ** MINIMAL: n = {min(ok_n)}. **")

print()
print("="*80)
print("(3)  THE ARITHMETIC OF IT — why the condition IS '4 divides n'")
print("="*80)
print("  the hinge set = multiples of g = gcd(120, 360/n).")
print("  closed under +90  <=>  g | 90.")
print("  and g | 120 always. So g | gcd(120,90) = 30. The set must be multiples of a")
print("  divisor of 30 -- i.e. the spacing must divide 30.")
for n in (4,5,8):
    g = gcd(120, 360//n)
    print(f"     n={n:>2}: g = {g:>3}   g | 90 ? {90 % g == 0}   -> {'CLOSED' if 90%g==0 else 'NOT closed'}")
print()
print("  With gcd(3,n)=1: g = gcd(120, 360/n) = 120/gcd(120, n)... check directly instead:")
for n in range(1, 25):
    if 360 % n: continue
    if gcd(3,n) != 1: continue
    g = gcd(120, 360//n)
    if 90 % g == 0:
        print(f"     n={n:>2}  spacing={g:>3}  4|n? {n%4==0}")
print()
print("  >> ** THE CONDITION IS EXACTLY: 4 | n (with gcd(n,3)=1). **")
print("     Because the dial's Z4 needs a quarter-turn in the figure, and the figure's")
print("     spacing is gcd(120, 360/n); that divides 90 only when n brings a factor of 4.")

print()
print("="*80)
print("(4)  SO WHY 4 AND NOT 8, 16, 20?")
print("="*80)
print("  All of {4, 8, 16, 20, ...} are closed and coprime to 3. The condition gives a")
print("  FAMILY, and 4 is its MINIMUM. Is minimality a reason, or a preference?")
print()
print("  ** IT IS THE CORPUS'S OWN RULE 2 (least arbitrariness), AND IT IS THE ONLY PLACE")
print("     IN THIS ARGUMENT WHERE A PRINCIPLE IS DOING WORK: **")
print("     n=8 is closed under the dial's Z4 -- but it is closed under MORE than the dial")
print("     asks. Its extra Z2 answers to nothing in the construction. That extra factor is")
print("     an UNFIXED ARBITRARY MODULUS -- exactly what Rule 2 rules INADMISSIBLE, not")
print("     merely disfavoured (P14 uses the identical move to force 3 generations).")
print("     n=4 is closed under the dial's Z4 AND NOTHING MORE. It is the CLOSURE, not a")
print("     closure.")
print()
print(f"  >> ** n = 4 IS THE MINIMAL CLOSURE OF THE FIGURE UNDER ITS OWN DIAL. **")
print(f"     3 hinges x 4 = {len(hinges(4))} hinges at {360//len(hinges(4))} degrees.")

print()
print("="*80)
print("(5)  AND THEN — ARE THE TWO 30s THE SAME 30?")
print("="*80)
print("  the kaleidoscope's 30 : 360/12 = 360/(3 x 4)")
print("                          the 3 = the triple angle. the 4 = the dial's quadrants.")
print("  the Nariai dial's 30  : arcsin(a/2a) -- the hole's half-angle at the hinge,")
print(f"                          = {np.degrees(np.arcsin(0.5)):.1f} deg, forced by the hinge at 2a.")
print()
print("  ** THEY ARE STILL NOT THE SAME 30, AND I AM NOT GOING TO SAY THEY ARE. **")
print("  One is 360/(3x4) -- a COMBINATORIAL closure in the azimuth.")
print("  The other is arcsin(1/2) -- a METRIC angle in the sky.")
print("  Both are now FORCED, and both are alpha re-read, and they are EQUAL. That is more")
print("  than thirty_degrees.py had (where the 4 was a bare choice, so the equality was a")
print("  coincidence of a choice). But EQUAL AND BOTH FORCED IS NOT THE SAME NUMBER: they")
print("  are computed by different routes from the same input, and nothing here shows the")
print("  routes are one route.")
print()
print("  ** WHAT WOULD SHOW IT: a derivation of 360/(3x4) FROM arcsin(1/2), or the reverse.")
print("     The suggestive shape: the hole subtends 60 at the hinge, and 60 = 2 x 30 =")
print("     360/6; the hinges are 120 apart and 120 = 2 x 60. Everything is a doubling of")
print("     the hole's half-angle. THAT is checkable and I have not done it. **")

print()
print("="*80)
print("VERDICT — what moved, and what did not")
print("="*80)
print("  ** MOVED: thirty_degrees.py's 'the geometry does not prefer 4' IS NOW FALSE. **")
print("  The geometry prefers 4, and the preference is not aesthetic: the figure must be")
print("  closed under the group acting on its own slicing; that group is the dial's Z4; the")
print("  closure condition is exactly 4 | n; and n=4 is the minimal closure, with anything")
print("  larger carrying a factor that answers to nothing (Rule 2).")
print("  ** So 12 = 3 x 4 has both factors forced -- the 3 by the triple angle, the 4 by")
print("     the dial -- and Daryl's conjecture is CONFIRMED at the level he pitched it. **")
print()
print("  DID NOT MOVE, and this is the honest residue:")
print("   * the closure demand is a COHERENCE PRINCIPLE, not a computation. It is a good")
print("     one and it is the corpus's own, but it is not a theorem. A construction that")
print("     declined it would read the single-hinge index -- and P14 makes exactly this")
print("     move and marks it exactly this way.")
print("   * the two 30s are EQUAL and BOTH FORCED. They are not yet ONE.")
