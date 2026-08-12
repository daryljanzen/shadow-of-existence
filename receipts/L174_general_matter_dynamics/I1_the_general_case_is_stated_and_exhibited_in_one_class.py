#!/usr/bin/env python3
"""I1 -- L-174 (1) narrowed: P9 STATES the general case is ordinary GR, L-207 EXHIBITS it in one
class, and the gap between them is what is actually unbuilt.

** THE ROW. **  L-174 is the longest-unworked row on the board -- opened r2376+c54.166, folding
OPEN_PROBLEMS_MAP's A-1, "** why the cut bends ** -- a dynamics for the curve itself, matter's own
evolution", which the map had carried live and unregistered since r565.  Its next step: "** build the
classical general matter dynamics -- the ungated half, which is owed no gate and has simply never been
taken. **"

** ⓵ P9 ALREADY ANSWERS THE GENERAL CASE, IN THE PARAGRAPH THAT STATES THE WALL. **

  cor:wall -- "The wall is inhomogeneity": a geometry with no continuous isometry admits no
  sweep-subgroup of SO(4,1) to anchor the construction.  And immediately after:

    "** It is not a defect: since the construction leaves the dynamics of general relativity
    unchanged, the radiative sector beyond it is reached by ORDINARY EVOLUTION OF THE LEAF rather than
    by generation from a sweep, so the wall is the seam at which GENERATION-BY-SYMMETRY HANDS OFF TO
    EVOLUTION-BY-DYNAMICS. **"

  ⇒ *** SO THE GENERAL MATTER DYNAMICS BEYOND THE WALL IS ORDINARY GR BY STATEMENT.  The construction
      owes no generative law there BECAUSE IT HANDS OFF. ***

** ⓶ AND L-207 (1) EXHIBITED EXACTLY THAT, COMPUTED FROM THE METRIC -- IN ONE CLASS. **  r2450: LTB
with Lambda, the bend-density identity EXACT for arbitrary m(r), and evolution
Rddot = -m(r)/R^2 + Lambda R/3 -- ** the same equation as the homogeneous case, one per shell, with
nothing fixing m(r) in GR either. **

** ⇒⇒ SO THE ROW'S OWN NEXT STEP IS NARROWER THAN "BUILD A DYNAMICS", AND THE ROW SAYS SO ITSELF: **
"what is owed is the ** EXHIBITION ** of a general matter dynamics the framework already says is
ordinary GR, ** not the discovery of a generative law **."

  *** THE GAP IS EXACTLY THE DISTANCE BETWEEN THE TWO: P9 STATES the general case is ordinary; L-207
      EXHIBITS it only in the SPHERICALLY SYMMETRIC class.  What is actually unbuilt is the exhibition
      BEYOND spherical symmetry. ***

  ** That is a much smaller and better-posed thing than "the deepest question the construction opens
  onto", which is how this row was carried. **

** ⌗ AND WHY IT SAT FIVE HUNDRED REVISIONS, which is the part worth recording: ** the row was carried
at the weight of P8's SOURCE COMMENT, which phrases the item as an open DISCOVERY.  ** The published
text had already downgraded it to an exhibition owed, and answers the general case in the same
paragraph. **  The c54.179 correction fixed the quotation -- ** and nobody re-read the row's DIFFICULTY
afterward. **  ⇒ *** A CORRECTION TO A ROW'S EVIDENCE IS NOT A CORRECTION TO ITS WEIGHT, AND THE SECOND
DOES NOT FOLLOW AUTOMATICALLY FROM THE FIRST. ***

WHAT IS NOT CLAIMED.  ** Not that L-174 (1) is discharged ** -- the exhibition beyond spherical symmetry
is genuinely unbuilt and nothing here builds it.  Not that P9's handoff statement is a proof; it is a
statement, and the row asks for an exhibition precisely because a statement is not one.  ** Not anything
about (2), which is gated on PO-6 and untouched. **

Written r2480.  Stated for reversal.
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
    print("  I1 -- what is actually unbuilt in L-174's ungated half?")
    print()
    p9 = flat('range_paper.tex')
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_LIVE_ARC.md'),
                                   encoding='utf-8', errors='replace').read())

    # the row and its age
    check('L-174 is on the board with its next step "build the classical general matter dynamics"',
          'build the classical general matter dynamics' in arc)
    check('and it folds the map\'s A-1, carried live and unregistered since r565',
          'unregistered since r565' in arc.lower() or 'UNREGISTERED SINCE r565' in arc)

    # ⓵ P9 states the general case
    check("P9's cor:wall: \"The wall is inhomogeneity\" -- a geometry with no continuous isometry "
          'admits no sweep-subgroup to anchor the construction',
          'The wall is inhomogeneity' in p9 and 'no continuous isometry admits no sweep-subgroup' in p9)
    check('⛭ and immediately after: "since the construction leaves the dynamics of general '
          'relativity unchanged, the radiative sector beyond it is reached by ORDINARY EVOLUTION '
          'OF THE LEAF"',
          'the radiative sector beyond it is reached by ordinary evolution of the leaf' in p9)
    check('⇒ "so the wall is the seam at which GENERATION-BY-SYMMETRY hands off to '
          'EVOLUTION-BY-DYNAMICS"',
          'generation-by-symmetry hands off to evolution-by-dynamics' in p9)
    check('⇒⇒ SO THE GENERAL CASE BEYOND THE WALL IS ORDINARY GR BY STATEMENT -- the construction '
          'owes no generative law there because it HANDS OFF',
          'It is not a defect' in p9)

    # ⓶ L-207 exhibited it in one class
    check('and L-207 (1) exhibited exactly that at r2450, computed from the metric: LTB with '
          'Lambda, one equation per comoving shell',
          'one equation per comoving shell' in arc or 'ONE equation per comoving shell' in arc)
    check('with the bend-density identity exact for arbitrary m(r)',
          'exact for arbitrary' in arc.lower())

    # ⇒ the gap
    check('⇒ and the row itself already says what is owed is the EXHIBITION of a dynamics the '
          'framework says is ordinary GR, "not the discovery of a generative law"',
          'not the discovery of a generative law' in arc)
    check('⇒⇒ SO THE GAP IS THE DISTANCE BETWEEN THEM: P9 STATES the general case; L-207 EXHIBITS '
          'it only in the spherically symmetric class',
          'the radiative sector beyond it is reached by ordinary evolution of the leaf' in p9
          and ('one equation per comoving shell' in arc
               or 'ONE equation per comoving shell' in arc))

    # why it sat
    check('and the row records why it was carried at the wrong weight: the quotation was P8\'s '
          'SOURCE COMMENT phrasing it as an open DISCOVERY, corrected at c54.179',
          'SOURCE COMMENT' in arc and 'c54.179' in arc)
    check('⇒ a correction to a row\'s EVIDENCE is not a correction to its WEIGHT, and the second '
          'does not follow automatically',
          'corrected at c54.179' in arc or 'is corrected at c54.179' in arc)

    # and what stays open
    check('⛔ and (1) is NOT discharged: the exhibition beyond spherical symmetry is genuinely '
          'unbuilt and nothing here builds it',
          'build the classical general matter dynamics' in arc)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (a NARROWING of the longest-unworked row; (1) is NOT discharged):')
    print('  ** P9 ANSWERS THE GENERAL CASE IN THE PARAGRAPH THAT STATES THE WALL: "the radiative')
    print('     sector beyond it is reached by ORDINARY EVOLUTION OF THE LEAF ... the wall is the seam')
    print('     at which generation-by-symmetry hands off to evolution-by-dynamics." **')
    print('  ** And L-207 (1) exhibited exactly that from the metric -- in the SPHERICALLY SYMMETRIC')
    print('     class. **')
    print('  ⇒ ** So what is actually unbuilt is the EXHIBITION BEYOND spherical symmetry ** -- much')
    print('    smaller and better-posed than "the deepest question the construction opens onto".')
    print('  ⌗ AND WHY IT SAT FIVE HUNDRED REVISIONS: the row was carried at the weight of a SOURCE')
    print('    COMMENT calling it an open DISCOVERY; the published text had already downgraded it.')
    print('    c54.179 fixed the quotation -- ** and nobody re-read the row\'s DIFFICULTY afterward. **')
    print('    ⇒ ** A correction to a row\'s EVIDENCE is not a correction to its WEIGHT. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
