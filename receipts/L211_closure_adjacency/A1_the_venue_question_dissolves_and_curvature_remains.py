#!/usr/bin/env python3
"""A1 -- L-211 run on L-213's closure: the venue question dissolves; curvature is what remains.

** THE PROCEDURE (L-211): ** "when a gap closes, the corpus owes on the gaps in connected regions --
the adjacent dots become visible and connectable."  Deliverable: WHICH ADJACENT GAP THE CLOSURE JUST
MADE ANSWERABLE.  Run here on L-213's closure (r2448) together with F13 (r2442).

** THE CLOSURES: **
  * F13   -- so(6,C) has FOUR real forms and su(3) embeds in EXACTLY ONE, the compact one.
  * L-213 -- taking that compact face as physical, motivated by the SM as an external constraint,
             is an ADD by the base rate's discriminant, and requirement (2) is untouched: the face
             carries no clock.

** THE ADJACENT GAP P13 ADVERTISES, in its own words: ** "The compact-face fermion sector the
obstruction would act on REMAINS UNBUILT, and its construction is the major undertaking any geometric
GAUGE-matter route would first have to complete" -- and a coherent route must proceed "by some route
other than su(3) as a substrate isometry."

** WHAT THE ADJACENCY ANSWERS: THAT OTHER ROUTE EXISTS, IT IS ALREADY BUILT, AND IT IS NOT THE COMPACT
FACE. **  P14: "The bundle the operator acts on is not a bundle of the substrate: every ambient
candidate is real, and a real bundle's complexification carries a parallel conjugation, so its holonomy
lands in the real form and none can carry su(3).  ** THE MODULE IS THE BRANCHING ITSELF. **"  And the
three wall monodromies with the hinge 3-cycle generate a FINITE group of order 81 in U(3), each
monodromy carrying determinant omega, whose determinant-one part is Delta(27) and lies in SU(3), with
the lap as its centre -- "every channel the Standard Model has, with the configuration group SELECTED
rather than chosen."

** r6931+70.1: this paragraph previously said "the smallest connected group containing the three wall
monodromies and the hinge 3-cycle is SU(3)".  That was P14's wording at r2455 and it was an error the
corpus corrected at r6707 (3b921b95, the body) and r6719 (440623b6, the abstract): a single wall
monodromy has determinant omega, so the group they generate is finite, of order 81, in U(3), and only
its determinant-one part Delta(27) lies in SU(3).  The finding here never rested on the group being
SU(3) -- it rests on the route being BUILT, SELECTED and FLAT -- so it survives the correction intact. **

** r6931+70.1: AND THE ADJACENT GAP BELOW HAS SINCE BEEN DISCHARGED BY P13 ITSELF. **  At r6683
(73eb61ef) P13 stopped calling the compact-face fermion sector "unbuilt ... the major undertaking":
sec:open now SPECIFIES that sector (a fermion on the face is an SU(4) object, 4 -> 3 + 1) and finds it
OBSTRUCTED TWICE (no equivariant map to the cosmological three-sphere; no Dirac zero modes on the round
face, the squash and torsion evasions both excluded), "so what is definite is the emptiness of a
definite object" (receipts P13_boundary_paper/P13_the_construction_is_specifiable_and_colour_sits_in_
the_spin_group and P13_the_last_evasion_inside_the_premise_is_the_squash_and_it_is_excluded_twice).
That discharge STRENGTHENS this receipt's conclusion: the compact-face venue is now not merely priced
as an ADD but specified and empty, so the venue question is closed from that side too, and curvature
is still what remains.

⇒ ** SO THE THREE ROUTES TO COLOUR COMPOSE INTO ONE STATEMENT THE CORPUS HELD IN PIECES: **

    su(3) as a SUBSTRATE ISOMETRY   -- WALLED (PO-4, the 6-versus-5 dimension count)
    su(3) on the COMPACT FACE       -- PRICED AS AN ADD (L-213), and F13 shows it is the ONLY real
                                       form that could have hosted it
    colour from WALL MONODROMY      -- BUILT: a finite order-81 group in U(3) whose determinant-one
                                       part Delta(27) lies in SU(3), SELECTED rather than chosen
                                       ** but the bundle is FLAT **

** AND THE FLATNESS IS WHERE THE LIVE GAP ACTUALLY SITS **, in P14's own words: "the bundle is FLAT.
Flat holonomy supplies exact selection rules and no curvature, so the construction delivers the discrete
content of colour and supplies no force."

⇒⇒ *** THE VENUE QUESTION DISSOLVES.  The corpus was never short of a home for su(3) -- it has one that
   SELECTS rather than chooses.  What F13 and L-213 leave is sharper and smaller: NOT "where does colour
   live" but "WHERE DOES ITS CURVATURE COME FROM". ***  (r6931+70.1: "a home for su(3)" read here as a
   home for colour's DISCRETE content -- the finite holonomy above -- which is all P14 claims.)

⌗ WHY THIS IS THE ROW'S MECHANISM AND NOT A COINCIDENCE: the three facts sit in THREE PAPERS (P13's
frontier, P13's face-status, P14's discrete opening) and in two nodes' findings.  ** No single reading
would have joined them, and nothing in the register was looking; L-211's procedure is what looked. **

WHAT IS NOT CLAIMED.  Not that the curvature question is answerable, or close.  Not that the monodromy
route delivers colour as a FORCE -- P14 says plainly that it does not.  ** Only that the question the
corpus should now be asking about colour is about curvature and not about venue, and that this became
visible only when two closures in one paper were read against a third paper's built result. **

Written r2455.  Stated for reversal.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(f):
    return re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'corpus', f),
                                    encoding='utf-8', errors='replace').read())


def main():
    print()
    print("  A1 -- L-211 on L-213's closure: what did it make answerable?")
    print()
    p13, p14 = flat('boundary_paper.tex'), flat('matter_sector_paper.tex')

    # the gap P13 advertises next to the closure
    # ** r6931+70.1: class (b), DISCHARGED.  These two checks pinned P13's "The compact-face fermion
    #   sector the obstruction would act on remains unbuilt, and its construction is the major
    #   undertaking any geometric gauge-matter route would first have to complete".  r6683 (73eb61ef)
    #   replaced that sentence with "sec:open specifies that sector and finds it obstructed twice", and
    #   sec:open does the work: the sector is specified as an SU(4) object and shown empty by two
    #   independent obstructions, with its own receipts.  Re-pinning to the new wording alone would keep
    #   an "unbuilt" gap alive past its answer, so the checks are re-pointed at WHAT DISCHARGED IT: the
    #   specification, the two obstructions, the stated emptiness, and the receipt that carries them. **
    check('P13 names the adjacent gap and has since answered it: the compact-face sector "can be '
          'specified, and is obstructed twice" (discharged r6683)',
          'n} specifies that sector and finds it obstructed twice' in p13
          and 'that sector can be specified, and is obstructed twice' in p13)
    check('and what the specification returns is "the emptiness of a definite object", carried by '
          "P13's own receipt of the specification",
          't evade the positive-curvature obstruction, so what is definite is the emptiness of a definite object' in p13
          and 'P13_the_construction_is_specifiable_and_colour_sits_in_the_spin_group' in p13
          and os.path.exists(os.path.join(ROOT, 'receipts', 'P13_boundary_paper',
              'P13_the_construction_is_specifiable_and_colour_sits_in_the_spin_group.py')))
    check('and requires "some route other than $\\su(3)$ as a substrate isometry"',
          'other than $\\su(3)$ as a substrate isometry' in p13)

    # the other route, in P14, already built
    check('P14: the bundle is NOT a bundle of the substrate -- every ambient candidate is real',
          'not a bundle of the substrate' in p14 and 'every ambient candidate is real' in p14)
    check("and a real bundle's complexification carries a parallel conjugation, so none can "
          'carry su(3)',
          'parallel conjugation' in p14 and 'none can carry' in p14)
    check('⇒ "The module is the \\emph{branching} itself"',
          'The module is the \\emph{branching} itself' in p14)
    # ** r6931+70.1: class (a), FROZE AN ERROR.  This pinned "the smallest connected group containing
    #   the three wall monodromies and the hinge 3-cycle is SU(3)".  A single wall monodromy has
    #   determinant omega, so the monodromies generate a FINITE group of order 81 in U(3), not SU(3);
    #   corrected at r6707 (3b921b95) in the body and r6719 (440623b6) in the abstract.  What this check
    #   is about is that the monodromy route yields a definite, selected group with the lap as its centre;
    #   the pin follows the correction: order 81 in U(3), determinant-one part Delta(27) in SU(3). **
    check('and the three wall monodromies with the hinge 3-cycle generate a finite group of order 81 '
          'in U(3), whose determinant-one part Delta(27) lies in SU(3), with the lap as its centre',
          'generate a finite group of order $81$ in $U(3)$' in p14
          and 'whose determinant-one part is $\\Delta(27)$ and lies in $SU(3)$, with the lap as its centre' in p14)
    check('with the configuration group SELECTED rather than chosen',
          'y channel the Standard Model has, with the configuration group \\emph{selected} rather than chosen' in p14 or 'selected\\/} rather than chosen' in p14
          or 'y channel the Standard Model has, with the configuration group \\emph{selected} rather than chosen' in p14)

    # and the negative half, which is where the gap moves to
    check('⛭ AND THE BUNDLE IS FLAT: "Flat holonomy supplies exact selection rules and no curvature"',
          'the bundle is \\emph{flat}' in p14 and 'no curvature' in p14)
    check('so the construction "delivers the discrete content of colour and supplies no force"',
          'supplies no force' in p14)

    # the two closures this is run on
    arc = open(os.path.join(ROOT, 'THE_LIVE_ARC.md'), encoding='utf-8', errors='replace').read()
    check('L-213 was struck by pricing the compact-face motivation as an ADD',
          'made the argument an ADD' in arc or 'it is an ADD' in arc)
    check('and F13 established su(3) embeds in exactly one real form',
          'exactly one real form' in arc or 'embeds in **exactly one**' in arc
          or 'EXACTLY ONE' in arc)
    check("L-211's procedure is what joined three papers no single reading would have",
          'closure-adjacency' in arc.lower() or 'CLOSURE-ADJACENCY (L-211' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** THE VENUE QUESTION DISSOLVES. **')
    print('  su(3) as a substrate isometry -- WALLED.  On the compact face -- PRICED AS AN ADD, and it')
    print('  is the only real form that could have hosted it (and P13 has since specified that sector')
    print('  and found it obstructed twice).  From wall monodromy -- ** BUILT: a finite order-81 group in')
    print('  U(3) whose determinant-one part Delta(27) lies in SU(3), SELECTED rather than chosen. **')
    print("  ⇒ The corpus was never short of a home for colour's discrete content.  ** What F13 and")
    print('    L-213 leave is sharper')
    print('    and smaller: NOT "where does colour live" but "WHERE DOES ITS CURVATURE COME FROM" --')
    print('    because the built bundle is FLAT, and flat holonomy supplies selection rules and no')
    print('    force. **')
    print('  ⌗ The three facts sit in three papers and two nodes\' findings.  No single reading would')
    print('    have joined them, and nothing in the register was looking.  ** L-211 is what looked. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
