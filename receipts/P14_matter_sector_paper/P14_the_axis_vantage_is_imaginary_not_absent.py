"""
P14_the_axis_vantage_is_imaginary_not_absent
============================================
WHAT IT CORRECTS.  P14R62 computed that the Z_3-fixed axis meets the substrate in zero
points (-X_0^2 = alpha^2 has no real solution) and concluded that the colourless seat
"is not anywhere in this manifold ... a successor must EXTEND the substrate."

** That conclusion over-claimed, and the corpus's own instrument is what it missed. **
(Daryl's question: "Is the vantage the one that the geometry selects that sits above
the hole on its axis?")

P17 fixes a vantage's height by the power of a point:

    pow(P) = |X|^2 - alpha^2 ,    and the vantage is "lifted to its own height
    X_0 = sqrt(pow)"     [P17, receipt O2_sightline_null_on_lift]

The zero-intersection computation asked where the AXIS meets the substrate.  The
power-of-a-point construction asks a different question: what height does the geometry
assign to a vantage sitting at that planar position?  ** For the axis the answer is not
'none'.  It is imaginary. **

WHAT WOULD FALSIFY THE HEADLINE.  If pow on the axis were not -alpha^2, or if the
corpus treated imaginary-height loci as unreal rather than as reached by continuation.
"""
import sympy as sp

a = sp.Symbol('alpha', positive=True)

print("=" * 78)
print("PART 1 — THE HEIGHT THE CONSTRUCTION ASSIGNS TO EACH PLANAR POSITION")
print("=" * 78)
def height(absX, label):
    pw = sp.simplify(absX**2 - a**2)
    h  = sp.sqrt(pw)
    print(f"  {label:>34}  |X| = {str(absX):>9}   pow = {str(pw):>12}   X_0 = {str(sp.simplify(h)):>12}")
    return pw, h

height(2*a,        "a hinge (circumradius 2 alpha)")
height(a,          "the throat itself")
height(0,          "the Z_3-fixed axis (the hole)")
print()
print("  check the hinge lands on the substrate:  -X_0^2 + |X|^2 = alpha^2 ?")
lhs = sp.simplify(-(sp.sqrt(3)*a)**2 + (2*a)**2)
print(f"     -(sqrt3 alpha)^2 + (2 alpha)^2 = {lhs}   -> {sp.simplify(lhs - a**2) == 0}")
print()
print("  ** On the axis pow = -alpha^2, so X_0 = i*alpha. **  Not undefined, not absent")
print("  -- IMAGINARY, and at exactly the one invariant the programme never sends to a")
print("  limit.")

print()
print("=" * 78)
print("PART 2 — SO WHAT P14R62 ESTABLISHED, AND WHAT IT DID NOT")
print("=" * 78)
print("  ESTABLISHED, and unchanged: the axis meets the substrate in no REAL point.")
print("  NOT ESTABLISHED, and wrongly concluded: that there is nothing there.")
print()
print("  ** The corpus does not treat imaginary-reached loci as unreal. **  Its whole")
print("  apparatus is built the other way: the equatorial seam is reached by")
print("  theta -> pi/2 + i psi; the lift occupies an imaginary stretch of cosmic time;")
print("  P17's own title is 'Reached through the imaginary, real by ...'.  An imaginary")
print("  height places the axis vantage in the class of things this construction")
print("  reaches BY CONTINUATION, not in the class of things it lacks.")
print()
print("  ⇒ The demand 'a successor must EXTEND the substrate' is withdrawn.  What the")
print("    zero-intersection result supports is narrower: ** the seat is not at any")
print("    real point of the manifold **, which leaves the continuation route open and")
print("    is the route this corpus uses everywhere else.")

print()
print("=" * 78)
print("PART 3 — AND THE AXIS VANTAGE HAS THE PROPERTIES THE SEAT NEEDS")
print("=" * 78)
props = [
 ("three objects",        "OPEN",
  "the axis is ONE locus; what would sit on it as a triple is not shown here"),
 ("no hinge index",       "YES",
  "it is the Z_3-FIXED locus -- fixed, not permuted, so it carries no hinge label"),
 ("triality-neutral",     "YES",
  "Z_3 fixes it, so the deck acts trivially: lambda = 0 mod 3, the colourless class"),
 ("R acts as a transposition", "OPEN",
  "R's action ON the axis vantage is not computed here"),
 ("fermion content",      "OPEN",
  "prop:wall binds at walls; whether an imaginary-height vantage carries a mode is untouched"),
]
print(f"  {'property':>28} {'status':>7}")
for nm, st, why in props:
    print(f"  {nm:>28} {st:>7}   {why}")
print()
print("  ** Two of the five are met by construction and three are open. **  That is a")
print("  live candidate, and it is a different one from the reassignment three: it")
print("  fails the 'no hinge index' test nowhere, which is exactly where that one")
print("  failed.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  CORRECTION LANDED: P14R62's conclusion is withdrawn.  The zero-intersection")
print("  computation stands; what it supports is 'no REAL point', not 'nothing there'.")
print("  The geometry assigns the axis vantage height X_0 = i*alpha by the same")
print("  power-of-a-point rule that puts a hinge at sqrt3*alpha.")
print()
print("  NOT CLAIMED: that the axis vantage seats the colourless triple.  Three of the")
print("  five properties are open, and the first -- what would make ONE fixed locus a")
print("  TRIPLE -- is the one to take next.")
print()
print("  AND THE ASSIGNMENT ITEM (3) IS ANSWERED IN PASSING: nothing distinguishes one")
print("  ruling from the other -- the hyperboloid is doubly ruled and the two rulings")
print("  are each other's opposite -- so the A-timelike choice is NOT forced, and that")
print("  it is unforced is the content of R being a symmetry of the pair rather than a")
print("  defect in the construction.")
