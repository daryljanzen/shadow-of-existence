"""
P14_the_axis_vantage_is_a_pair
==============================
TWO THINGS, one a correction of my own previous receipt.

(1) P14R63 scored the axis vantage against the seat's five properties and marked
    TRIALITY-NEUTRAL as MET, with the reason: "Z_3 fixes it, so the deck acts
    trivially: lambda = 0 mod 3."

    ** That conflates the two threes the corpus proves unrelated. **  The Z_3 that
    FIXES the axis is the rotation acting on the hinges.  Triality is graded by the
    TURNAROUND's deck Z_3.  P14R4 shows the two are not related by ANY covering
    construction -- "strictly stronger than by no affine one" -- so fixity under one
    says nothing whatever about the action of the other.  The score is withdrawn.

(2) The open property P14R63 named as next: what would make ONE fixed locus a TRIPLE.
    The axis vantage is reached by a square root, X_0 = sqrt(pow) with pow = -alpha^2,
    and a square root on a negative argument is where branch structure lives.  This
    computes how many branches, and asks whether three is among the answers.

WHAT WOULD FALSIFY THE HEADLINE.  A cube-root structure at the axis, or any reason the
height's branches number three.
"""
import sympy as sp

a = sp.Symbol('alpha', positive=True)

print("=" * 78)
print("PART 1 — THE CORRECTION: WHICH Z_3 FIXES THE AXIS")
print("=" * 78)
print("  the ROTATION Z_3     : permutes the three hinges; FIXES the axis (that is what")
print("                         'the Z_3-fixed axis' names)")
print("  the TURNAROUND DECK  : permutes the three sheets of the signed radius r;")
print("                         GRADES triality as lambda mod 3")
print()
print("  P14R4: these two are not related by ANY covering-space construction over the")
print("  2M-plane -- (omega r)^3 - omega r + 2M vanishes only at r = 0.")
print()
print("  ** So 'the rotation fixes the axis' does NOT give 'the deck acts trivially')")
print("  there. **  P14R63's triality-neutral score used the wrong Z_3 and is WITHDRAWN;")
print("  the property reverts to OPEN.")

print()
print("=" * 78)
print("PART 2 — HOW MANY BRANCHES THE AXIS VANTAGE HAS")
print("=" * 78)
pow_axis = -a**2
roots = sp.solve(sp.Eq(sp.Symbol('X0')**2, pow_axis), sp.Symbol('X0'))
print(f"  pow(axis) = {pow_axis}")
print(f"  X_0^2 = pow  ->  X_0 in {roots}")
print(f"  number of branches: {len(roots)}")
print()
print("  ** TWO, not three. **  The height is fixed by a SQUARE root, so the axis")
print("  vantage is a PAIR: +i alpha and -i alpha.")
print()
print("  Checked for a cube-root structure at the axis, since that is what would give")
print("  three: the lap's three-ness comes from r being a cube root of an invariant")
print("  (P14R4's r^3 - r + 2M), and r is the AREAL radius, not the height.  The height")
print("  rule X_0 = sqrt(pow) is quadratic wherever it is applied -- at the hinge it")
print("  gives +/- sqrt3 alpha just as it gives +/- i alpha here.")
print(f"  hinge branches: {sp.solve(sp.Eq(sp.Symbol('X0')**2, 3*a**2), sp.Symbol('X0'))}")
print("  ** So two is not an accident of the axis; it is what the height rule gives")
print("  everywhere, and at a hinge those two branches are the two HORNS. **")

print()
print("=" * 78)
print("PART 3 — SO THE THREE-NESS PROPERTY FAILS, AND FAILS INFORMATIVELY")
print("=" * 78)
print("  The axis vantage is a pair, and the seat needs a triple.  ** That is a clean")
print("  failure of the property P14R63 named as next. **")
print()
print("  AND THE FAILURE HAS A SHAPE WORTH KEEPING.  S3's colourless triple is not")
print("  three symmetric objects: it is 2 LEFT + 1 RIGHT -- a doublet and a singlet.")
print("  The axis vantage supplies a PAIR exchanged by the height's sign, which is the")
print("  horn structure at every other vantage.  ** So what the axis offers is the 2,")
print("  and what is missing is the 1. **")
print()
print("  ⇒ RESTATED DEMAND: not 'find a triple', but 'find the singlet that completes")
print("    the axis pair'.  That is a strictly smaller object than the one the previous")
print("    three revisions were looking for.")
print()
print("  NOT CLAIMED: that the axis pair IS the lepton doublet.  The correspondence of")
print("  a sign-exchanged height pair with a weak doublet is a shape, and shapes have")
print("  been wrong twice in this arc already (P14R57's 2+1 on the generations, and")
print("  this receipt's own PART 1).  What is established is the COUNT: two, not three.")

print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print("  WITHDRAWN: P14R63's triality-neutral score, which conflated the rotation Z_3")
print("  with the turnaround deck.  Of the seat's five properties the axis vantage now")
print("  meets ONE by construction -- no hinge index -- with three-ness FAILED and")
print("  triality, R's action, and fermion content all OPEN.")
print()
print("  ESTABLISHED: the axis vantage is a PAIR, because the height rule is a square")
print("  root wherever it is applied; at a hinge the same two branches are the horns.")
print()
print("  WHAT IT LEAVES: the demand is now for a singlet to complete a pair, not a")
print("  triple to fill a hole -- smaller, and stated against an object that exists.")
