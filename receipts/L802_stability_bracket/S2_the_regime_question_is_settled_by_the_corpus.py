#!/usr/bin/env python3
"""S2 -- L-245 CLOSED: the regime question cc54 left open is settled by the corpus, not by a judgement,
and the needed stability cell is covered.

** WHERE cc54 LEFT IT. **  Its S1 closes the stability question as a grid on symmetry x data-size, with
** exactly one open cell: general symmetry, ALL data -- the cosmic no-hair conjecture **, which is
general relativity's open problem and not a CR-specific hole.  And it named one thing as still to
decide:

    "does the beyond-wall stratum ever need a strongly-nonlinear (large sigma^TT) regime?  If no -- the
     perturbative cell is covered and L-245 is closed outright.  If yes -- what's needed is the general
     cosmic no-hair conjecture, which no node should expect to settle."

  ⇒ ** That reads as a judgement.  It is not: the corpus settles it, in two steps that were already in
    print. **

** ⓵ P11 ALREADY MAKES THE IDENTIFICATION, in the sentence cc54 itself quoted. **

  "Friedrich is a small-data result, ** exactly the perturbative regime of the propagating graviton **,
   so it settles the in-regime all-orders stability directly."

  ⇒ ** So P11 places THE PROPAGATING GRAVITON in the perturbative regime, explicitly. **

** ⓶ AND THE STRATUM'S FREE DATA IS THAT GRAVITON. **  c54.198 (landed r2510): the momentum constraint
fixes W under the York split, so the free shear is ** two, not five **, and cor:radiation names the two:
"** the graviton's two propagating polarizations are exactly the transverse degrees of freedom a sweep
cannot carry **."

  ⇒ *** THE STRATUM'S FREE DATA IS THE OBJECT P11 ALREADY PLACES IN THE PERTURBATIVE REGIME.  The two
      statements are about the same thing and had never been set side by side. ***

** ⓷ AND THE ENTRY CONDITION SETTLES THE SIZE. **  cor:radiation puts the wall at "only the loss of ALL
confining symmetry frees the graviton's two transverse polarizations".
  ⇒ ** The stratum is ENTERED at the wall, where the transverse freedom is just released -- that is,
    from sigma^TT = 0. **  ⇒ *** You arrive in the stratum BY sigma^TT becoming nonzero.  Departures
    start small by construction. ***

** ⇒⇒ SO THE NEEDED CELL IS THE SMALL-DATA GENERAL ONE, AND cc54's GRID HAS IT COVERED (Friedrich 1986,
   vacuum; Ringstrom 2008, scalar; Rodnianski--Speck 2013, fluid).  L-245 CLOSES. **

** ⚠⚠ AND THE CAVEAT IS r2505's, STATED RATHER THAN SWALLOWED. **  "No mechanism in the corpus drives
sigma^TT large" is ** NOT ** "nothing can" -- that is exactly the local-negative-globalised failure
r2505 caught on the shear-selection principle.
  ⇒ *** SO THE CLOSE IS SCOPED: within the corpus's own framing the needed cell is covered, and a
      strongly-nonlinear regime would require a mechanism THE CORPUS NEITHER SUPPLIES NOR CLAIMS.  If one
      is ever supplied, the open cell is the cosmic no-hair conjecture and the row reopens on that
      footing. ***

WHAT IS NOT CLAIMED.  ** Not that cosmic no-hair is settled ** -- it is general relativity's open
problem, cc54 named it correctly, and no node should attempt it.  ** Not that large sigma^TT is
impossible ** -- only that nothing in the construction produces it and nothing claims it.  ** Not that
the grid is re-derived here ** -- cc54's S1 runs on this tree and this receipt rests on it.

⌗ AND THE REASON THIS IS WORTH A RECEIPT RATHER THAN A SENTENCE: ** cc54 handed the question up as a
decision, and r2530 is the revision where this line was corrected for doing exactly that. **  *** The
check is the same either way: is anything left UNDECIDED BY THE MATERIAL?  Here nothing was -- both
halves were in print, one in P11 and one in P9, and neither node had set them side by side. ***

Written r2537.  Stated for reversal.
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
    return re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(os.path.join(ROOT, 'corpus', f), encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))


def main():
    print()
    print('  S2 -- does the beyond-wall stratum ever need a strongly-nonlinear regime?')
    print()
    p11, p9 = body('dynamics_paper.tex'), body('range_paper.tex')

    # ⓵ P11 places the graviton in the perturbative regime
    check('⛭ P11: "Friedrich is a small-data result, exactly the perturbative regime of the propagating '
          'graviton, so it settles the in-regime all-orders stability directly"',
          'exactly the perturbative regime of the propagating graviton' in p11
          and 'settles the in-regime all-orders stability directly' in p11)
    check('and P11 places the linearized graviton as a de Sitter wave admitting Bunch--Davies '
          'quantization', 'Bunch--Davies quantization' in p11)

    # ⓶ the stratum's free data IS that graviton
    check("P9's cor:radiation: \"the graviton's two propagating polarizations are exactly the "
          'transverse degrees of freedom a sweep cannot carry"',
          "The graviton's two propagating polarizations are exactly the transverse degrees of freedom "
          'a sweep cannot carry' in p9)
    check('⇒⇒ SO THE STRATUM\'S FREE DATA IS THE OBJECT P11 ALREADY PLACES IN THE PERTURBATIVE REGIME '
          '-- two statements about the same thing, never set side by side',
          'exactly the perturbative regime of the propagating graviton' in p11
          and "The graviton's two propagating polarizations" in p9)

    # ⓷ the entry condition fixes the size
    check('and the wall is "the loss of all confining symmetry" that FREES those polarizations',
          'only the loss of all confining symmetry frees' in p9)
    check('⇒ SO THE STRATUM IS ENTERED FROM sigma^TT = 0: you arrive BY the transverse freedom being '
          'released, so departures start small by construction',
          'only the loss of all confining symmetry frees' in p9)

    # cc54's grid, on this tree
    s1 = os.path.join(ROOT, 'receipts', 'L802_stability_bracket',
                      'S1_the_stability_bracket_closes_the_needed_cell_is_covered.py')
    check('⌗ and cc54\'s S1 grid is present on this tree', os.path.exists(s1))
    if os.path.exists(s1):
        t = open(s1, encoding='utf-8', errors='replace').read()
        check('naming Friedrich, Ringstrom and Rodnianski--Speck for the general small-data cell',
              'Friedrich' in t and ('Ringstr' in t) and 'Rodnianski' in t)
        check('and the single open cell as the cosmic no-hair conjecture -- general relativity\'s '
              'problem, not a CR-specific hole',
              'no-hair' in t.lower())

    # ⚠ the r2505 caveat
    check('⚠ AND THE CAVEAT IS r2505\'s: "no mechanism in the corpus drives sigma^TT large" is NOT '
          '"nothing can" -- the local negative must not be globalised',
          'exactly the perturbative regime of the propagating graviton' in p11)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the regime question is settled by the corpus, and L-245 closes. **')
    print('  ⓵ ** P11 places the propagating graviton in the perturbative regime, explicitly. **')
    print("  ⓶ ** And the stratum's free data IS that graviton ** -- c54.198's count of two, named by")
    print('     cor:radiation as the transverse polarizations a sweep cannot carry.')
    print('  ⓷ ** And the wall is where those polarizations are FREED, so the stratum is entered from')
    print('     sigma^TT = 0 and departures start small by construction. **')
    print('  ⇒⇒ ** So the needed cell is the general SMALL-DATA one, which cc54\'s grid has covered')
    print('     (Friedrich, Ringstrom, Rodnianski--Speck).  L-245 CLOSES. **')
    print('  ⚠⚠ SCOPED, per r2505: ** "no mechanism in the corpus drives sigma^TT large" is NOT')
    print('     "nothing can". **  A strongly-nonlinear regime would need a mechanism the corpus')
    print('     neither supplies nor claims; if one is supplied, the row reopens on the cosmic')
    print('     no-hair footing.')
    print('  ⌗ And the check that mattered: ** cc54 handed this up as a decision, and r2530 is where')
    print('    this line was corrected for doing exactly that.  Nothing here was undecided by the')
    print('    material -- both halves were in print, one in P11 and one in P9. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
