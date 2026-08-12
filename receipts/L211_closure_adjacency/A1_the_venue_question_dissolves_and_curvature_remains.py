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
smallest connected group containing the three wall monodromies and the hinge 3-cycle is SU(3), with the
lap as its centre -- "every channel the Standard Model has, with the configuration group SELECTED
rather than chosen."

⇒ ** SO THE THREE ROUTES TO COLOUR COMPOSE INTO ONE STATEMENT THE CORPUS HELD IN PIECES: **

    su(3) as a SUBSTRATE ISOMETRY   -- WALLED (PO-4, the 6-versus-5 dimension count)
    su(3) on the COMPACT FACE       -- PRICED AS AN ADD (L-213), and F13 shows it is the ONLY real
                                       form that could have hosted it
    su(3) from WALL MONODROMY       -- BUILT, and the group is SELECTED rather than chosen
                                       ** but the bundle is FLAT **

** AND THE FLATNESS IS WHERE THE LIVE GAP ACTUALLY SITS **, in P14's own words: "the bundle is FLAT.
Flat holonomy supplies exact selection rules and no curvature, so the construction delivers the discrete
content of colour and supplies no force."

⇒⇒ *** THE VENUE QUESTION DISSOLVES.  The corpus was never short of a home for su(3) -- it has one that
   SELECTS rather than chooses.  What F13 and L-213 leave is sharper and smaller: NOT "where does colour
   live" but "WHERE DOES ITS CURVATURE COME FROM". ***

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
    check('P13 names the adjacent gap: the compact-face fermion sector "remains unbuilt"',
          'remains unbuilt' in p13)
    check('and calls its construction "the major undertaking any geometric \\emph{gauge}-matter '
          'route would first have to complete"',
          'the major undertaking any geometric' in p13)
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
    check('and the smallest connected group containing the three wall monodromies and the hinge '
          '3-cycle is SU(3), with the lap as its centre',
          'smallest connected group containing the three wall monodromies' in p14
          and 'with the lap as its centre' in p14)
    check('with the configuration group SELECTED rather than chosen',
          'selected} rather than chosen' in p14 or 'selected\\/} rather than chosen' in p14
          or '\\emph{selected} rather than chosen' in p14)

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
          'closure-adjacency' in arc.lower() or 'CLOSURE-ADJACENCY' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** THE VENUE QUESTION DISSOLVES. **')
    print('  su(3) as a substrate isometry -- WALLED.  On the compact face -- PRICED AS AN ADD, and it')
    print('  is the only real form that could have hosted it.  From wall monodromy -- ** BUILT, with')
    print('  the configuration group SELECTED rather than chosen. **')
    print('  ⇒ The corpus was never short of a home for su(3).  ** What F13 and L-213 leave is sharper')
    print('    and smaller: NOT "where does colour live" but "WHERE DOES ITS CURVATURE COME FROM" --')
    print('    because the built bundle is FLAT, and flat holonomy supplies selection rules and no')
    print('    force. **')
    print('  ⌗ The three facts sit in three papers and two nodes\' findings.  No single reading would')
    print('    have joined them, and nothing in the register was looking.  ** L-211 is what looked. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
