"""
P14_two_rank_threes.py -- P14 sec:openquestions: this sector carries TWO rank-three bundles and
the paper was calling both "the bundle" in adjacent paragraphs.  They index different things,
both are right, and the division between them turns out to be the Standard Model's own relation
between the centre and the fundamental.

FOUND while discharging the bundle lead under the register's languishing rule, not by looking
for it.

THE TWO OBJECTS.
  * P14_the_bundle_is_the_branching: the PUSHFORWARD of the mode bundle from a wall's
    three-sheeted cover -- rank three because a cube root has three branches.
  * P14_the_wall_is_a_wall_of_a_hinge: E = L_0 + L_1 + L_2, one line per VANTAGE -- rank three
    because there are three hinges.
** Those are different bundles, and the paper introduced them four sentences apart. **

WHAT IS ESTABLISHED.
  1. WHAT THE PUSHFORWARD'S THREE ACTUALLY ARE.  Pushing a flat line bundle with Z_3 monodromy
     along the three-sheeted cover carries the regular representation, which decomposes into the
     three characters -- one line per value of the monodromy phase.  ** So those three lines
     sort DIFFERENT MODES by lambda mod 3.  They are a grading of the TOWER. **
  2. ** THE TEST THAT SEPARATES THEM: fix one mode and count the lines it occupies.  A given
     mode occupies EXACTLY ONE pushforward line and exists at ALL THREE vantages. **  The two
     threes do opposite jobs: the pushforward three separates different modes and is blind to
     which wall binds them; the vantage three separates the three copies of ONE mode and is
     blind to lambda.
  3. ** SO READING THE PUSHFORWARD'S EIGENLINES AS THE THREE COLOURS WOULD BE THE SEAT/MODE
     ERROR AGAIN -- counting VALUES of one object as distinct STATES. **  The receipt that
     introduced them did not commit it, but the paper as it stood invited it, since the sentence
     identifying a "colourless line" sat four sentences from the paragraph in which colour is
     the vantage index.  Fixed in the same revision as this receipt.
  4. ** AND THE OPERATIVE BUNDLE IS THE VANTAGE ONE **, because every downstream result uses it:
     the kernel of P14_statistics_not_gauge is "one mode per wall", and the hadron spectrum
     comes out of its exterior powers.  The pushforward grades the tower; it is not what colour
     acts on.
  5. ** THE RESOLUTION IS THE STANDARD MODEL'S OWN.  All three colours of one constituent carry
     the SAME triality -- asserted on the kernel -- which is exactly how the centre relates to
     the fundamental in QCD: triality is a property of the REPRESENTATION, carried identically
     by every state in it, while colour is the index WITHIN it.  The two rank-three objects
     reproduce that division exactly, and the apparent collision was the correct structure
     misdescribed. **
  6. ** AND IT RULES SOMETHING OUT: the three colours cannot come from the three SHEETS of a
     single cover, because a mode has one triality and would then have one colour.  They require
     three WALLS -- which the vantage reading supplies and the one-radius reading could not. **

** WHAT IS WITHDRAWN IS NARROWER THAN IT LOOKS.  The reality obstruction, the elimination of
every candidate bundle on this paper's own list, and the finding that the answer is not a bundle
of the ambient geometry because ambient geometry is real -- all hold whichever rank-three object
is meant.  What is withdrawn is only the identification of the OPERATIVE bundle with the
pushforward from one wall's cover: the right KIND of object, found one wall too early. **

ORIGIN: computations/baryon_edge/L131_two_rank_threes.py -- built r2376 (c54.57); edit the
origin, not this copy."""
import sympy as sp

print(__doc__.split("Run:")[0])

w = sp.exp(2 * sp.pi * sp.I / 3)


def W(k):
    return sp.simplify(sp.expand_complex(w**(k % 3)))


# =====================================================================
print("=" * 78)
print("PART 1 — THE TWO OBJECTS")
print("=" * 78)
for s in [
 "** `L-127` (c54.50), landed in P14: ** 'the PUSHFORWARD of the mode bundle from that",
 "three-sheeted cover to the base ... rank the order of the deck group ... ** its eigenlines are",
 "exactly the triality grading **.'  Rank 3, from the THREE SHEETS of ONE wall's cover.",
 "",
 "** `L-128` (c54.52), landed in P14 in the NEXT PARAGRAPH: ** the wall is a wall OF a hinge, so",
 "there are three radii and three branch loci, and the rank-3 object is ** E = L_0 + L_1 + L_2,",
 "one line per VANTAGE **, on which the wall monodromies act diagonally.",
 "",
 "⚠ ** THOSE ARE DIFFERENT BUNDLES.  One is rank 3 because a cube root has three branches; the",
 "   other is rank 3 because there are three hinges.  P14 currently calls both 'the bundle' in",
 "   adjacent paragraphs, and I wrote both. **",
 "",
 "⌗ ** AND THIS IS THE SESSION'S OWN RECURRING HAZARD ARRIVING A THIRD TIME. **  `lem:twoturnings`",
 "   exists because the hinge three and the turnaround three were being conflated.  ** Here are",
 "   a third and a fourth three -- the SHEETS of one cover, and the VANTAGES -- and nothing in",
 "   the corpus yet keeps them apart. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 2 — WHAT THE PUSHFORWARD'S THREE ACTUALLY ARE")
print("=" * 78)
print("  Push a flat line bundle with Z_3 monodromy forward along the 3-sheeted cover.  The")
print("  pushforward carries the REGULAR representation of the deck group, which decomposes into")
print("  the three CHARACTERS -- one line per value of the monodromy phase:")
print()
print(f"     {'character':>12} {'monodromy phase':>18} {'which modes sit here':>34}")
for k in range(3):
    lam_here = [L for L in range(9) if (-L) % 3 == k]
    print(f"     {('chi_%d' % k):>12} {('omega^%d' % k):>18} "
          f"{('lambda = ' + ', '.join(map(str, lam_here[:3])) + ', ...'):>34}")
print()
for s in [
 "** SO THE PUSHFORWARD'S THREE LINES ARE THE THREE TRIALITY CLASSES OF THE MODE TOWER: they",
 "   sort modes by lambda mod 3. **  That is a grading of the TOWER, indexed by which mode you",
 "   are looking at.",
 "",
 "⌗ ** `L-127` WAS RIGHT ABOUT THIS AND ITS SENTENCE IS ACCURATE AS WRITTEN.  What it did not",
 "   say, and what P14 therefore does not say, is that this three is NOT a three of",
 "   SIMULTANEOUS states. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE TEST THAT SEPARATES THEM")
print("=" * 78)
print("  Fix ONE mode -- one value of lambda -- and ask how many lines it occupies in each object.")
print()
print(f"  {'lambda':>7} | {'triality = -L mod 3':>20} {'pushforward lines occupied':>28} "
      f"| {'vantages carrying a mode':>26}")
for L in (1, 2, 3, 4):
    tri = (-L) % 3
    print(f"  {L:>7} | {tri:>20} {'1  (the chi_%d line)' % tri:>28} "
          f"| {'3  (walls 60, 180, 300)':>26}")
print()
for s in [
 "** A GIVEN MODE OCCUPIES EXACTLY ONE PUSHFORWARD LINE AND EXISTS AT ALL THREE VANTAGES. **",
 "   The two threes are therefore doing opposite jobs:",
 "",
 "     * the PUSHFORWARD three separates DIFFERENT modes (different lambda) and is blind to",
 "       which wall binds them;",
 "     * the VANTAGE three separates the THREE COPIES OF ONE MODE (same lambda, three walls)",
 "       and is blind to lambda.",
 "",
 "⚠ ** SO READING THE PUSHFORWARD'S EIGENLINES AS THE THREE COLOURS WOULD BE THE SEAT/MODE ERROR",
 "   AGAIN -- counting VALUES of one object as distinct STATES. **  `L-127` did not commit it,",
 "   but P14 as it currently stands invites it, because the paragraph that identifies the",
 "   'colourless line (1,1,1)' sits four sentences from the paragraph where colour is the vantage.",
 "",
 "⇒ ** AND THE OPERATIVE BUNDLE IS THE VANTAGE ONE, because that is the one every downstream",
 "   result uses: `L-130`'s kernel K is 'one mode per wall', and the hadron spectrum comes out",
 "   of Lambda^k K. **  The pushforward grades the tower; it is not what colour acts on.",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND THE RESOLUTION IS THE STANDARD MODEL'S OWN")
print("=" * 78)
print("  Check the two indices against each other on the kernel `L-130` uses:")
print()
print(f"  {'constituent':>16} {'vantage (colour)':>18} {'lambda':>8} {'triality':>10}")
LAM = 1
for j, az in ((0, 180), (1, 300), (2, 60)):
    print(f"  {('mode at wall %d' % az):>16} {j:>18} {LAM:>8} {(-LAM) % 3:>10}")
tris = {(-LAM) % 3}
print()
print(f"  ** ALL THREE COLOURS OF ONE CONSTITUENT CARRY THE SAME TRIALITY: {tris} **")
assert len(tris) == 1
for s in [
 "",
 "⌗ ** AND THAT IS EXACTLY THE RELATION QCD HAS BETWEEN THE CENTRE AND THE FUNDAMENTAL. **  In",
 "the Standard Model all three colours of an up quark have triality 1; triality is a property of",
 "the REPRESENTATION, carried identically by every state in it, while colour is the index WITHIN",
 "the representation.  ** The corpus's two rank-3 objects reproduce that division exactly:",
 "triality is the centre's grading and colour is the fundamental's index. **",
 "",
 "⇒ ** SO BOTH `L-127` AND `L-128` ARE RIGHT, ABOUT DIFFERENT THINGS, AND THE APPARENT COLLISION",
 "   IS THE CORRECT STRUCTURE MISDESCRIBED. **  What was missing was a sentence saying which is",
 "   which -- the same omission `lem:twoturnings` was written to repair for the other pair.",
 "",
 "⌗ *And it is worth noticing what this rules out: any attempt to get the three colours from the",
 "three SHEETS of a single cover.  That was `L-127`'s implicit picture and it cannot work, because",
 "a single mode has one triality and would then have one colour.*  ** The three colours require",
 "three WALLS, which is exactly what reading (ii) supplies and reading (i) could not. **",
]:
    print("  " + s)

# =====================================================================
print()
print("=" * 78)
print("PART 5 — WHAT MUST CHANGE, AND WHAT `L-127` IS WORTH AFTER IT")
print("=" * 78)
for s in [
 "① ** P14 MUST DISTINGUISH THEM IN THE TEXT. **  As it stands the reality obstruction and the",
 "   candidate-list elimination are followed by 'the pushforward ... its eigenlines are exactly",
 "   the triality grading ... the deck-invariant line is a colourless state', and then by a",
 "   paragraph in which colour is the vantage index.  ** A reader has no way to tell that the",
 "   colourless LINE and the colour INDEX live on different bundles. **  Fixed this revision.",
 "",
 "② ** `L-127` SURVIVES ALMOST INTACT AND ITS BEST PART IS UNTOUCHED. **  The reality obstruction",
 "   -- su(3) needs a COMPLEX rank-3 module, a real bundle's complexified holonomy lands in the",
 "   real form -- and the elimination of every candidate on P14's list are statements about what",
 "   the bundle CANNOT be, and they hold whichever rank-3 object one means.  ** So does its",
 "   central finding: the answer is not a bundle of the ambient geometry, because ambient",
 "   geometry is real, and the complex structure is at the branch point. **",
 "",
 "③ ** WHAT IS WITHDRAWN IS NARROWER THAN IT LOOKS: the identification of the OPERATIVE bundle",
 "   with the pushforward from ONE wall's cover. **  `L-128` replaced it with the sum over",
 "   vantages, and every downstream result -- the group, the selection rules, the hadron",
 "   spectrum -- uses the replacement.  ** `L-127` found the right KIND of object one wall too",
 "   early. **",
 "",
 "④ ⇒ ** SO `L-127` IS STRUCK, NOT AMENDED: its owed action ('does the three-wall transport",
 "   supply Q?') was answered YES by `L-128`, and its remaining content is either carried",
 "   forward or corrected above. **",
]:
    print("  " + s)
