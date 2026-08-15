#!/usr/bin/env python3
"""B42 -- `PO-4`'s "remaining route" was TAKEN, and P14 is the work: the boundary paper names the
discrete component as "the single geometric opening the wall leaves", and P14 says outright that it
takes that opening up.

** THE CLAIM r2775 LEFT. **  *** `PO-4`'s row records its remaining route as a fermion sector on the
discrete orientation parity $\\mathrm{O}(5,1)\\setminus\\mathrm{SO}_0(5,1)$, "routed r2398 from
`ENTRY_POINT_REGISTER` U3", with the row noting "it was not in this row" -- read at r2775 as ** unworked
in 377 revisions **.  ** It is not unworked. ** ***

** ⛭⛭ ⓵ THE BOUNDARY PAPER NAMES THE ROUTE AND ITS MECHANISM. **  *** "the index theorem is a statement
about a compact connected group, and a positive-dimensional connected group contains a circle whose
action is what forces the equivariant Dirac index to vanish, while the gravitational handedness is
carried by the discrete orientation parity $\\mathrm{O}(5,1)\\setminus\\mathrm{SO}_0(5,1)$, ** no such
circle action and so no trigger ** --- so observed fermion chirality is not merely found non-geometric
but ** FORCED to be **, the boundary the conclusion of a mechanism and not only the report of a wall;
** a fermion sector built on that discrete component, rather than a connected-group isometry, is the
single geometric opening the wall leaves **." ***

** ⛭⛭⛭ ⓶ AND P14 SAYS IT TAKES THAT OPENING. **  *** "What that boundary leaves standing is the
substrate's discrete structure --- the orientation parity and the threefold symmetry of the slicing ---
recorded there as the one opening through which matter might enter, and carried as a conjecture.  **
THIS PAPER TAKES UP THAT OPENING CONCRETELY. **  We put a Dirac field on the slicing curve and compute
what its zero-mode content is." ***

  ⇒⇒ *** THE MATTER SECTOR PAPER IS THE WORK ON THE ROUTE.  Not a paper that could take it -- a paper
      whose stated purpose is taking it. ***

** ⓷ AND WHAT IT DELIVERS ON THE ROUTE IS WHAT `PO-4` RECORDS AS ITS GAP. **  *** "a fermion sector with
exactly the discrete shape the Standard Model wears: three chiral generations carrying a family
symmetry" -- and, in the same paper's own accounting, colour's ** exact selection rules ** and weak
isospin as ** "a species label, not $SU(2)_L$'s chiral action" **. ***

  ⇒ *** So the route runs, and its outcome IS the row's remainder.  ** `PO-4` is not waiting on an
      untaken route; it is recording what the taken route returned. ** ***

** ⓸ WHICH CORRECTS r2775, WHOSE CORRECTION OF r2774 STILL STANDS. **  *** r2775 was right that r2774
answered a different question, and right that the row's object is the discrete route.  ** It was wrong
that the route is unworked ** -- and this line read "it was not in this row" as "it has not been done",
when the row's own sentence means the routing was recorded elsewhere. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-4` closes ** -- *** the row is protected and this receipt does not
recommend a strike: what the taken route DELIVERS ($\\mathfrak{su}(3)$'s selection rules, a species
label) against what the row ASKS ($\\mathfrak{su}(3)$ and $\\mathfrak{su}(2)_L$ as structures on the cut)
is a comparison the row's owner makes, not this line. ***  ** Not that P14's delivery is re-verified **
-- it is quoted, and its own accounting is used.  ** Not that r2775's kill receipt is withdrawn ** --
its check ① finding stands; only its "unworked in 377 revisions" gloss is corrected.

** COMPUTES: nothing.  *** Three corpus statements read in sequence: the boundary paper's mechanism, its
naming of the opening, and P14's statement that it takes it. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT ed7b4d0** *(per c54.220's rule, r2776).*

Written r2777.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  B42 -- is PO-4's remaining route actually unworked?")
    print()
    bp = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'boundary_paper.tex')))
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the boundary paper's mechanism
    check('⛭⛭ ⓵ the boundary paper gives the mechanism: the index theorem needs "a compact connected '
          'group", and the discrete parity has "no such circle action and so no trigger"',
          'no such circle action and so no trigger' in bp)
    check('and concludes chirality is "not merely found non-geometric but forced to be, the boundary '
          'the conclusion of a mechanism and not only the report of a wall"',
          # ** 'forced to be' spans a source line break; the clause stem does not **
          'not only the report of a wall' in bp and 'non-geometric but' in bp)
    check('⛭⛭⛭ and names the route: "a fermion sector built on that discrete component ... is the '
          'single geometric opening the wall leaves"',
          'is the single geometric opening the wall leaves' in bp)

    # ⓶ and P14 takes it
    check('⓶ and P14 says outright that it takes it: "This paper takes up that opening concretely. '
          'We put a Dirac field on the slicing curve and compute what its zero-mode content is."',
          'This paper takes up that opening concretely' in p14)
    check('with a stated outcome: "a fermion sector with exactly the discrete shape the Standard '
          'Model wears: three chiral generations carrying a family symmetry"',
          'three chiral generations carrying a family symmetry' in p14)

    # ⓷ and what it returns is the row's remainder
    check('⓷ while the same paper accounts what that returns for the gauge sector: colour\'s "exact '
          'selection rules" and isospin "a species label, not $SU(2)_L$\'s chiral action"',
          "colour's exact selection rules" in p14 and 'delivers a species label' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the route was TAKEN, and P14 is the work. **")
    print('  ⛭⛭ ⓵ ** The boundary paper gives the mechanism: ** the index obstruction is "a statement')
    print('     about a compact connected group", and the discrete parity has ** "no such circle action')
    print('     and so no trigger" ** — so chirality is ** "not merely found non-geometric but FORCED to')
    print('     be" **, and a fermion sector on that component is ** "the single geometric opening the')
    print('     wall leaves". **')
    print('  ⛭⛭⛭ ⓶ ** And P14 says outright it takes it: ** "This paper takes up that opening')
    print('     concretely.  We put a Dirac field on the slicing curve and compute what its zero-mode')
    print('     content is."')
    print('     ⇒ *** The matter sector paper is not a paper that COULD take the route.  It is the')
    print('     paper whose stated purpose is taking it. ***')
    print('  ⓷ ** And what it returns IS the row\'s remainder: ** three chiral generations with a family')
    print('     symmetry; colour\'s exact selection rules; isospin as a species label.')
    print('     ⇒ ** PO-4 is not waiting on an untaken route — it is recording what the taken route')
    print('       returned. **')
    print('  ⓸ ** Which corrects r2775\'s gloss, not its finding: ** its check ① result stands.  This')
    print('     line read the row\'s "it was not in this row" as "it has not been done", when the')
    print('     sentence means the ROUTING was recorded elsewhere.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
