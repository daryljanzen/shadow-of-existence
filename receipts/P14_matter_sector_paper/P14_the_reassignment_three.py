"""
P14_the_reassignment_three
==========================
WHAT IT ASKS.  P14R58 closed the search for the colourless triple's seat over twelve
three-element structures drawn from P3's geometry and P14's count/chirality/whichthree,
and stated its own scope: "a three arising in P5's groupoid, P12's algebroid, or the
charged sector would reopen it."

** A three arising in P7's CAUSAL REASSIGNMENT reopens it, and it was not on the list. **
(Daryl's object.)

THE THREE, from P7 sec:dS-SdS and the six-panel figure, quoted not re-derived:

  A  -- one null ruling bundle of dS_4, "reassigned to timelike to define the
        fundamental congruence in the SdS projection"
  B  -- the OTHER null ruling bundle: panel (D), "the B congruence as the flat
        synchronous space (constant tau, its conjugate dual, read in the opposite
        sense)"
  P  -- the at-rest comoving worldlines, "timelike in de Sitter space, but in the SdS
        projection they are reinterpreted as null geodesics and serve as the photon
        congruence"

THREE ROLES: fundamental timelike / synchronous flat space / photon null.

AND THE THIRD OPTION IS REAL, which is what makes this a structure and not a labelling:
B could have been promoted to the timelike congruence, leaving A as ITS synchronous
flat space.  The paper takes one assignment; the geometry admits the swap.

R'S ACTION, from the figure's own colour code:
  panel (A) -- "both R-conjugate null frames ... the A worldline congruence and its B
                synchronous-space dual"
  panel (B) -- "matter and antimatter are the two ends of the standing R-conjugation,
                the conjugate bundle read in the opposite sense.  The photon congruence
                (black) and the S^3 layers (grey) complete it."

so R exchanges A and B, and P is listed outside that conjugate pair.

WHAT WOULD FALSIFY THE HEADLINE.  If R moved P as well, the action would not be a
transposition and the 2+1 would not arise.
"""
import sympy as sp

print("=" * 78)
print("PART 1 — THE THREE, AND WHY IT IS NOT ON P14R58's LIST")
print("=" * 78)
for nm, what in (
    ("A", "null ruling bundle #1 -> promoted to the fundamental TIMELIKE congruence"),
    ("B", "null ruling bundle #2 -> the SYNCHRONOUS FLAT SPACE, A's conjugate dual"),
    ("P", "at-rest comoving worldlines (timelike in dS) -> reinterpreted as NULL, the photons"),
):
    print(f"  {nm} : {what}")
print()
print("  These are congruences on the dS_4 background, not structures on the throat.")
print("  ** They carry NO graze-point index, so they are COLOURLESS. **  And they are")
print("  neither the hinge three (no antipodal or root map reaches them) nor the")
print("  turnaround three (the deck indexes sheets of r, not congruences).")

print()
print("=" * 78)
print("PART 2 — R ACTS AS A TRANSPOSITION, AND THE SPLIT IS 2+1")
print("=" * 78)
# basis (A, B, P); R exchanges A and B, leaves P
R = sp.Matrix([[0, 1, 0],
               [1, 0, 0],
               [0, 0, 1]])
sp.pprint(R)
ev = R.eigenvals()
plus = sum(m for e, m in ev.items() if e == 1)
minus = sum(m for e, m in ev.items() if e == -1)
print(f"  involution: {sp.simplify(R*R - sp.eye(3)) == sp.zeros(3)}")
print(f"  R = +1 eigenspace: dimension {plus}   (P, and the symmetric combination A+B)")
print(f"  R = -1 eigenspace: dimension {minus}   (the antisymmetric combination A-B)")
print()
print(f"  ** {plus} + {minus}, and S3 asks for 2 left and 1 right. **")
print("  Pairing condition: a transposition has a fixed point, so not every object")
print("  here comes in an R-conjugate pair -- P14R56's first condition MET.")
print("  Transitivity condition: R cannot carry P into A or B -- the seat symmetry is")
print("  NOT transitive -- P14R56's second condition MET.")

print()
print("=" * 78)
print("PART 3 — THE OFFSET, WHICH IS THE PART THAT MAKES A AND B INEQUIVALENT")
print("=" * 78)
print("  Panel (A), at source: 'Each bead splits its wrap 120 deg before its turn at")
print("  r = 0 and 240 deg after, and the two beads turn at the same r = 0: one carries")
print("  its blue 120 deg arc up the right of the equator and its red 240 deg arc back")
print("  around, the other its red 120 deg arc up the left and its blue 240 deg arc")
print("  back.'")
print()
print("  So along each worldline the branch point falls at 1/3 of the lap for one")
print("  bundle and 2/3 for the other:")
for nm, frac in (("A", sp.Rational(1, 3)), ("B", sp.Rational(2, 3))):
    print(f"    bundle {nm}: branch point at {frac} of the lap")
print(f"  offset = {sp.Rational(2,3) - sp.Rational(1,3)} of a lap  =  one third")
print()
print("  ** That offset is why A and B are not interchangeable by relabelling. **")
print("  Panel (A): the two agree in colour over the upper two thirds and differ on")
print("  the hinge-side third, where the two 240 deg arcs overlap carrying OPPOSITE")
print("  species -- the purple third.  A double ruling read this way is not two flat")
print("  lines crossing at the centre: each line comes up, conjugates onto the lap,")
print("  branches at r = 0 where charge swaps to antimatter, and exits with the")
print("  opposite charge -- so each X has a left half and a right half.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  ** P14R58's closure is REOPENED, on the axis its own scope clause named. **")
print("  The reassignment carries a three -- A, B, P -- that is colourless, is neither")
print("  of the corpus's two threes, and on which R acts as a transposition giving")
print("  2 + 1 with chirality's own grading.  Both of P14R56's conditions are met, and")
print("  unlike the turnaround (P14R57) the objects are not the generations.")
print()
print("  WHAT IS NOT ESTABLISHED HERE, AND MUST BE BEFORE THIS IS A SEAT:")
print("   (1) R's fixing of P is read from the figure's grouping -- panel (B) lists the")
print("       photon congruence outside the R-conjugate pair -- and NOT from an")
print("       explicit statement that R fixes it.  ** If R moves P, the 2+1 collapses. **")
print("   (2) That these three congruences can CARRY Weyl fermions at all is not shown.")
print("       They are congruences of the background, and the wall modes of prop:wall")
print("       are the only fermion content this construction has built.")
print("   (3) The assignment A-timelike is a CHOICE the paper makes; the third option")
print("       (B timelike, A its synchronous space) is admitted by the geometry and")
print("       nothing here decides between them.")
print()
print("  ** So this is a live candidate and not a discharge of S3. **  It is recorded")
print("  at that weight: the search space is open again, with one candidate in it and")
print("  three named things to check.")
