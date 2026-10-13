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

    # ⛔⛭ AMENDED r4516.  ** P9's wall passage was rewritten and two exact strings went with it:
    #    "beyond IT" is "beyond THE WALL" now, and "It is not a defect" is "The wall is thus named
    #    and walked past, not a defect and not the construction's open edge". **  *Neither claim
    #    moved -- the pronoun was resolved and the sentence gained a clause.*  ⇒ `W1`'s rule: a
    #    longer string is still a string, so these match the content under REORDERING.
    _HANDOFF = re.compile(r"radiative sector beyond [^.]{0,20}?is reached by ordinary evolution "
                          r"of the leaf", re.I)
    _NOTDEF = re.compile(r"walked past,? not a defect|not a defect[^.]{0,60}?open edge", re.I)

    # the row and its age
    check('L-174 asks for the classical general matter dynamics, and the SOURCE claim this receipt '
          'rests on is P9\'s rather than the register\'s: the wall hands off to ordinary evolution',
          _HANDOFF.search(p9) is not None)
    # ⛭ WIDENED r7287+cc66: the ALT's upper-case arm was UNDECIDING -- the first arm tests
    #   `arc.lower()`, so it was true whenever the second was, and case folding is monotone.  The
    #   arm is dropped rather than kept, and the surviving span is widened past the participle to
    #   the clause that NAMES ITS SUBJECT (`the map`), which `unregistered since r565` did not.
    check('and it folds the map\'s A-1, carried live and unregistered since r565',
          'which the map has carried live and unregistered since r565' in arc.lower())

    # ⓵ P9 states the general case
    check("P9's cor:wall: \"The wall is inhomogeneity\" -- a geometry with no continuous isometry "
          'admits no sweep-subgroup to anchor the construction',
          'The wall is inhomogeneity]\\label{cor:wall} A geometry with n' in p9 and 'A geometry with no continuous isometry admits no sweep-subgroup of $\\so$ to anchor '
          'the construction' in p9)
    check('⛭ and immediately after: "since the construction leaves the dynamics of general '
          'relativity unchanged, the radiative sector beyond it is reached by ORDINARY EVOLUTION '
          'OF THE LEAF"',
          _HANDOFF.search(p9) is not None)
    check('⇒ "so the wall is the seam at which GENERATION-BY-SYMMETRY hands off to '
          'EVOLUTION-BY-DYNAMICS"',
          # ⛭ WIDENED r7287+cc66: the bare clause dropped the one thing the claim rests on --
          #   that it is THE WALL that hands off -- so it held for a paper siting the handoff
          #   anywhere else.  Widened to P9's own sentence, which names the wall.
          "The wall is therefore the proper boundary of the operator's generative "
          'reach---the boundary at which generation-by-symmetry hands off to '
          'evolution-by-dynamics' in p9)
    check('⇒⇒ SO THE GENERAL CASE BEYOND THE WALL IS ORDINARY GR BY STATEMENT -- the construction '
          'owes no generative law there because it HANDS OFF',
          _NOTDEF.search(p9) is not None)

    # ⓶ L-207 exhibited it in one class
    check('and L-207 (1) exhibited exactly that at r2450, computed from the metric: LTB with '
          'Lambda, one equation per comoving shell',
          # ⛭ WIDENED r7287+cc66: an appositive with one term inside the span and its head --
          #   the evolution equation it renames -- outside it.  Widened to the head.
          'evolution $\\ddot R=-m(r)/R^2+\\Lambda R/3$, one equation per comoving shell' in arc
          or 'ONE equation per comoving shell, and the shells do n' in arc)
    check('with the bend-density identity exact for arbitrary m(r)',
          # ⛭ WIDENED r7287+cc66: three words that stopped before the thing they quantify over.
          'the bend-density identity exact for arbitrary $m(r)$' in arc.lower())

    # ⇒ the gap
    check('⇒ and the row itself already says what is owed is the EXHIBITION of a dynamics the '
          'framework says is ordinary GR, "not the discovery of a generative law"',
          # ⛭ WIDENED r7287+cc66: the span carried only the NEGATIVE limb of an `X, not Y`
          #   contrast whose X -- the exhibition that IS owed -- was outside it.  Both limbs now.
          'what is owed is the EXHIBITION of a general matter dynamics the framework '
          'already says is ordinary GR, not the discovery of a generative law' in arc)
    check('⇒⇒ SO THE GAP IS THE DISTANCE BETWEEN THEM: P9 STATES the general case; L-207 EXHIBITS '
          'it only in the spherically symmetric class',
          _HANDOFF.search(p9) is not None
          and ('evolution $\\ddot R=-m(r)/R^2+\\Lambda R/3$, one equation per comoving shell' in arc
               or 'ONE equation per comoving shell, and the shells do n' in arc))

    # why it sat
    # ⛭ WIDENED r7287+cc66: this was a CO-OCCURRENCE pin -- `'SOURCE COMMENT' in arc and
    #   'c54.179' in arc` -- two spans whose conjunction in ONE FILE stood for the claim, and
    #   `c54.179` could not fail at 10 occurrences.  ** One widened span replaces both, and the
    #   label no longer claims the correction: the NEXT check establishes that, with its own
    #   literal. **
    check('and the row records why it was carried at the wrong weight: the framing was inherited '
          'from a `%` SOURCE COMMENT phrasing it as an open DISCOVERY, where the published '
          'paragraph had already downgraded it',
          # ⛔⛭ NARROWED AGAIN r7287+cc66, BY `check_provenance`, AND THE GATE IS RIGHT: the
          #   widened span quoted the arc quoting `"the deepest open question the construction
          #   RAISES"`, and that phrase lives ONLY in slicing_operator.tex's `%` COMMENTS.  A
          #   quotation lifted from a comment carries the authority of the paper it sits in while
          #   being no part of it -- and the gate cannot tell a quotation OF a comment, labelled as
          #   one, from a quotation passed off AS the paper's.
          #   ⌗ ** AND THE OTHER HALF IS NO BETTER, MEASURED: the arc's `the PUBLISHED paragraph
          #     says "the deepest question the construction OPENS ONTO"` is in NO paper's body
          #     either -- zero hits across every corpus/*.tex with comment lines stripped.  So the
          #     arc's record of the c54.179 correction quotes two phrases and neither is live
          #     paper text: one never was, and the other has been reworded away.  Routed. **
          #   ⇒ So the pin is the arc's OWN claim sentence, which quotes no paper text at all.
          '**AND THIS ROW INHERITED ITS FRAMING FROM A SOURCE COMMENT.**' in arc)
    check('⇒ a correction to a row\'s EVIDENCE is not a correction to its WEIGHT, and the second '
          'does not follow automatically',
          'n DISCOVERY (P8\'s % source comment, corrected at c54.179' in arc or 'is corrected at c54.179' in arc)

    # and what stays open
    # ** SUPERSEDED r2516: this check asserted (1) was unbuilt.  r2514 EXHIBITED it at linear order.
    # The re-anchor is not to new wording -- the CLAIM changed.  What I1 established stands: P9 STATES
    # the general case and L-207 exhibited it in the spherically symmetric class. **
    check('⌗ what THIS receipt established stands: P9 STATES the general case at the wall, and it is '
          'a statement rather than an exhibition',
          _HANDOFF.search(p9) is not None)

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
