"""
The check stage 4 actually owed -- not a refuter, a source question:
DOES thm:bead ALREADY KNOW THIS?  If it does, "P7 under-states its own result" is
simply wrong, and the finding is not mine but the paper's.

My harvest (III.1) claimed:
  (a) "P7's thm:bead already says ... that the join is C^1. What it does not say is
       that the C^1-ness is PURCHASED by the imaginary excursion."
  (b) "a bead confined to real tau~ could not be smooth at r=0 at any M."
  (c) headline: "THE COSMOLOGICAL BEAD IS SMOOTH ONLY BECAUSE IT GOES THROUGH
       IMAGINARY TIME."

thm:bead, at source, says: "one continuous closed slicing curve"; "one closed object
on one smooth manifold"; and its PROOF says "for 0 > r > -(2M a^2)^(1/3) the radicand
is negative, so tau~ LEAVES THE REAL AXIS".

Three questions, and each can return against me.
"""
import numpy as np

alpha, M2 = 1.0, 0.3849001794597505
A = (M2*alpha**2)**(1/3)

print("="*78)
print("(Q1)  Does thm:bead CLAIM a continuous tangent (C^1) at r=0?")
print("="*78)
print("  Statement : 'one CONTINUOUS closed slicing curve' -> C^0.")
print("            : 'one closed object on one SMOOTH MANIFOLD' -> the SUBSTRATE is")
print("              smooth. That is a claim about the manifold, NOT about the")
print("              curve's join.")
print("  Proof     : 'the substrate is C^infty across the locus the chart so labels'")
print("              -- again the substrate.")
print("  => thm:bead claims CONTINUITY of the curve and SMOOTHNESS of the substrate.")
print("     It does NOT claim the join is C^1.")
print("  >> (a) IS WRONG. I attributed to P7 a claim it does not make, then credited")
print("     myself with explaining it.")

print()
print("="*78)
print("(Q2)  Does thm:bead already know r<0 requires imaginary tau~?")
print("="*78)
print("  Proof, verbatim: 'for 0 > r > -(2M a^2)^(1/3) the radicand is negative, so")
print("  tau~ leaves the real axis, its imaginary part reaching pi a/3 ...'")
print()
print("  And it is forced by the law itself. r^3 = 2M a^2 sinh^2(3 tau~/2a):")
for tt in (-1.2, -0.5, 0.5, 1.2):
    r3 = M2*alpha**2*np.sinh(1.5*tt/alpha)**2
    print(f"     tau~ = {tt:+.2f} (REAL)   ->  r^3 = {r3:+.5f}  ->  r = {np.sign(r3)*abs(r3)**(1/3):+.5f}   r >= 0")
print("  sinh^2 of a real argument is >= 0, so r^3 >= 0, so r >= 0 ALWAYS on real tau~.")
print("  >> THE LAP REQUIRES IMAGINARY TIME, AND P7'S OWN PROOF DERIVES IT.")
print("     So (c)'s content -- 'the lap is where tau~ leaves the real axis' -- is")
print("     ALREADY IN P7. My headline restates the paper and credits itself.")

print()
print("="*78)
print("(Q3)  Then what DOES the real-tau~ face do at r=0? Is (b) even a thing?")
print("="*78)
print("  On real tau~, r(tau~) = A |sinh(3 tau~/2a)|^(2/3) -- EVEN in tau~:")
for tt in (-0.6, -0.3, -0.05, 0.05, 0.3, 0.6):
    r = A*abs(np.sinh(1.5*tt/alpha))**(2/3)
    print(f"     tau~ = {tt:+.3f}  ->  r = {r:+.6f}")
print()
print("  It comes DOWN to 0 and goes back UP the same way. That is not a non-smooth")
print("  passage -- it is NO PASSAGE. A CUSP: the curve bounces off r=0 and returns")
print("  along the branch it came from. (Exactly the 'same sheet -> 180 reversal =")
print("  cusp' row of the nine-join enumeration.)")
print()
print("  >> (b) 'a bead confined to real tau~ could not be SMOOTH at r=0' is not false")
print("     so much as VACUOUS-AND-MIS-STATED: confined to real tau~ there is no join")
print("     to be smooth or unsmooth, because there is no r<0 to join TO.")

print()
print("="*78)
print("VERDICT ON III.1 -- refuted by me, at source, in ten minutes, no refuter needed")
print("="*78)
print("  DEAD: 'P7's thm:bead under-states its own result'; 'the C^1-ness is purchased")
print("        by the imaginary excursion'; 'the bead is smooth ONLY BECAUSE it goes")
print("        through imaginary time' -- as a claim about the OBJECT or about P7.")
print("        P7 does not claim C^1, and P7's proof already derives the imaginary")
print("        requirement. I inflated a shadow-fact into an object-fact and then")
print("        into a correction of the paper that already had it.")
print()
print("  ALIVE, and it is the storyboard's own claim at the storyboard's own weight:")
print("    * 180 mod 120 = 60: NOT ONE of the nine sheet-joins is smooth. The")
print("      three-fold ITSELF forbids smooth passage on the complex-r face.")
print("    * So the cosmological bead is NOT representable as a smooth curve on the")
print("      three-sheeted Riemann surface of r^3 = 2M sinh^2. THE SHEETS ARE NOT THE")
print("      BEAD'S HOME. (Modest, real, and it bears on C-AutA2: sheets-vs-generations")
print("      are two deformation rays -- this says the sheets are not where the bead")
print("      lives either.)")
print("    * 'One shadow breaks the very property the other exhibits' -- teeth for")
print("      'both are shadows, neither is the object', which is A3's whole warrant.")
print()
print("  WHAT I DID: took a true claim about two FACES and promoted it to a claim")
print("  about the OBJECT, then to a correction of a theorem that already knew it.")
print("  That is the over-correction-inside-a-concession's cousin: an over-reach")
print("  inside a synthesis. The synthesis was real; the promotion was not.")
