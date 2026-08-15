#!/usr/bin/env python3
"""B15 -- `PO-3`'s two clauses are answered in two different rows, and neither cites the other: the WHY at
r2627 on `PO-3`, the BRIDGE at r2626 on `PO-4`.

** THE OBJECT, in two clauses. **  "The $a_2$-meaning drill-site --- ** why does the SdS geometry produce a
zero-sum triple with a $\\mathbf3/\\bar{\\mathbf3}$ parity doubling **, ** and does that reason bridge to
$\\su(3)$? **"

** ⓵ CLAUSE ONE -- THE WHY -- ANSWERED AT r2627, ON THIS ROW. **  P14: "** The mass function is odd in the
signed offset exactly when $D$ is even **, so at $D=5$ the orientation parity $r_0\\mapsto-r_0$
*fixes* each geometry rather than exchanging it with its conjugate: there is no mass-reflection
$\\mathbb{Z}_2$, hence ** no $\\mathbf3\\oplus\\bar{\\mathbf3}$ Nariai hexad **".
  ⇒ ** Read forward: at $D=4$ the parity EXCHANGES conjugates, and that exchange IS the doubling. **

** ⛭⛭ ⓶ CLAUSE TWO -- THE BRIDGE -- ANSWERED AT r2626, ON `PO-4`. **  P14: "the smallest connected group
containing ** the three wall monodromies and the hinge $3$-cycle is $SU(3)$ **, with the lap as its
centre", the module being "** the branching ** rather than any bundle of the substrate".
  ⇒ *** So the reason DOES bridge to $\\su(3)$ -- and by generation rather than by reduction, which is the
      finding r2626 recorded against `PO-4`'s stale "what reduces $\\so(6)\\to\\su(3)$?" ***

** ⛔ ⇒⇒ ⓷ AND THIS RECEIPT'S FIRST DRAFT GOT THIS WRONG. **  It asserted the two halves were split across
`PO-3` and `PO-4`.  *** They are not.  `PO-3` carries BOTH, and has since c54.42--c54.62, in its own status
text: "The bridge was BUILT ... the smallest connected group containing the three wall monodromies and the
hinge $3$-cycle is $SU(3)$, with the lap as its centre". ***
  ⇒ ** So the row has held its own complete answer for hundreds of revisions and still reads OPEN. **
  *** That is worse than a split: nothing had to be assembled, only read. ***

** ⓸ SO `PO-3` IS ANSWERED, IN BOTH CLAUSES. **
  * ** why the doubling: ** the mass function's parity in the signed offset, odd exactly when $D$ is even;
  * ** does it bridge: ** yes -- the same three-fold, read through the wall monodromies with the hinge
    $3$-cycle, ** generates $SU(3)$ **.
  ⚠ ** And the answer is not that the bridge is a REDUCTION. **  *** The row's target says "the $A_2$
      skeleton and the parity doubling", and what the corpus delivers is a GENERATION from the skeleton --
      which is a stronger answer than the question's own framing anticipated. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-3` closes ** -- `PROTECTED_OPEN` reserves the strike, and this
receipt marks the question answered rather than striking the row.  ** Not that the $SU(3)$ so generated is
a FORCE ** -- "the bundle is flat.  Flat holonomy supplies exact selection rules and no curvature", which
is `PO-5`'s remaining half.  ** Not that the mass VALUES follow ** -- P13 marks that separately.

Written r2645.  Stated for reversal.
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
    print("  B15 -- are both of PO-3's clauses answered?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    # ** ⛭ AMENDED c54.224 (`L-558`): the row matcher required the OPEN form `| **PO-n**` and
    # ** `PO-4` was STRUCK at r2778, so this file died on `StopIteration`. **  It had gone on
    # ** passing only because `19139ed` duplicated the row and one copy came back UNSTRUCK --
    # *** so this receipt was reading a resurrected copy of an item the observer line closed. ***
    # ** A matcher that admits only the open form silently follows whichever copy is open. **
    _ROWPAT = (lambda t: re.compile(r'\|\s*(?:~~)?\s*\*\*' + re.escape(t) + r'\*\*'))
    po3 = next(l for l in raw.split('\n') if _ROWPAT('PO-3').match(l))
    po4 = next(l for l in raw.split('\n') if _ROWPAT('PO-4').match(l))

    # the object's two clauses
    check('⓵ the object has TWO clauses: "why does the SdS geometry produce a zero-sum triple with a '
          '$\\mathbf3/\\bar{\\mathbf3}$ parity doubling, and does that reason bridge to $\\su(3)$?"',
          'parity doubling, and does that reason bridge to $\\su(3)$' in po3)

    # ⓵ the why
    check('⓶ CLAUSE ONE answered: "The mass function is odd in the signed offset exactly when $D$ is '
          'even"',
          'The mass function is odd in the signed offset exactly when $D$ is even' in p14)
    check('and PO-3 carries it', 'odd in the signed offset' in po3)

    # ⓶ the bridge
    check('⛭⛭ ⓷ CLAUSE TWO answered: "the smallest connected group containing the three wall monodromies '
          'and the hinge $3$-cycle is $SU(3)$, with the lap as its centre"',
          'the smallest connected group containing the three wall monodromies and the hinge $3$-cycle '
          'is $SU(3)$' in p14)
    check('and PO-4 carries THAT', 'wall monodromies with the hinge' in po4
          or 'three wall monodromies and the hinge' in po4)

    # ⓷ neither row holds both
    # ** ⛔ AND THE FIRST DRAFT OF THIS RECEIPT WAS WRONG.  It asserted that PO-3 does not carry the
    # generation clause.  *** It does -- and has since c54.42-c54.62, in its own status text: "The
    # bridge was BUILT ... the smallest connected group containing the three wall monodromies and the
    # hinge 3-cycle is SU(3)". ***  So the halves were never split across rows; ** BOTH have been in
    # PO-3 the whole time, and the row still reads OPEN. **
    check('⛭⛭ ⓸ and PO-3 ALREADY CARRIES the generation clause -- "The bridge was BUILT at '
          'c54.42--c54.62 ... the smallest connected group containing the three wall monodromies and '
          'the hinge $3$-cycle is $SU(3)$"',
          'The bridge was BUILT' in po3 and 'smallest connected group' in po3)
    check('so BOTH clauses are in this one row, and it still reads OPEN',
          'odd in the signed offset' in po3 and 'smallest connected group' in po3
          and 'OPEN' in po3)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-3 is answered in BOTH clauses, and BOTH are already in its own row. **")
    print('  ⓵ ** WHY the doubling ** (r2627, on PO-3): the mass function is "odd in the signed offset')
    print('     ** exactly when D is even **" -- so at D=4 the parity EXCHANGES conjugates, and that')
    print('     exchange IS the doubling.')
    print('  ⛭⛭ ⓶ ** DOES IT BRIDGE ** (r2626, on PO-4): yes -- "the smallest connected group containing')
    print('     the three wall monodromies and the hinge 3-cycle is ** SU(3) **, with the lap as its')
    print('     centre".')
    print('')
    print("  ⛔ ⓷ ** And this receipt's first draft asserted the halves were split across PO-3 and")
    print('     PO-4.  They are not: PO-3 carries BOTH, and has since c54.42-c54.62 -- "The bridge was')
    print('     BUILT ... the smallest connected group ... is SU(3)". **')
    print('     ⇒ *** So the row has held its own complete answer for hundreds of revisions and still')
    print('       reads OPEN.  That is worse than a split: nothing had to be assembled, only read. ***')
    print('  ⚠ ** And the answer is STRONGER than the question anticipated: ** the bridge is not a')
    print('    REDUCTION but a ** GENERATION ** from the skeleton -- which is why PO-4\'s stale "what')
    print('    reduces so(6) to su(3)?" never matched it.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
