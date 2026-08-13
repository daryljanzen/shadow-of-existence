#!/usr/bin/env python3
"""B8 -- `PO-4`'s two targets have opposite verdicts, and its status line asks a question the corpus
answered by a different route.

** THE ITEM. **  `PO-4`, target column: "** $\\su(3)$ and $\\su(2)_L$ as structures on the cut **".  Status
line: "OPEN.  The obstruction moved at c54.8---from *cannot act internally at all* to ** *what reduces
$\\so(6)\\to\\su(3)$?* ** ---it did not close."

** ⛭⛭ ⓵ THE FIRST TARGET IS DELIVERED, AND NOT BY REDUCING ANYTHING. **  P14: "Because the wall is a wall
of a hinge, the construction carries three signed areal radii rather than one, so a wall crossing
branches only the vantage that owns it and the monodromy is diagonal in the vantage basis and non-abelian
across it; ** the smallest connected group containing the three wall monodromies and the hinge $3$-cycle
is $SU(3)$, with the lap as its centre **."

  ⇒ ⛔ *** The row asks what REDUCES $\\so(6)$ to $\\su(3)$.  P14 does not reduce anything: it GENERATES
      $SU(3)$ as the smallest connected group containing three monodromies and a $3$-cycle.  The status
      line has been asking after a route the corpus did not take. ***
  ⌗ ** And the module is named too: ** "the module the operator's colour structure acts on is ** the
    branching ** rather than any bundle of the substrate."

** ⛔ ⓶ THE SECOND TARGET IS EXPLICITLY NOT DELIVERED, AND P14 SAYS WHY IN ONE CLAUSE. **  "** Weak
isospin as a gauging: $T$ is a discrete horn swap and delivers a species label, not $SU(2)_L$'s chiral
action **, the two occupations differing on the right-handed pair."

  ⇒ ** So the two halves of one target column have OPPOSITE verdicts: ** *** $\\su(3)$ is built as a
    structure on the cut; $\\su(2)_L$ is not, and the reason is that what the geometry supplies is a
    DISCRETE SWAP where a gauging needs a CHIRAL ACTION. ***

** ⓷ AND THE ROW'S SCOPE IS WIDER THAN WHAT REMAINS. **  r2608 recorded P14's own reduction: "So the
undelivered content is ** two items and not three **.  What remains genuinely outstanding is ** the gauge
group and the multiplet structure **; hypercharge follows from them by a condition this construction
supplies."
  ⇒ *** Combined: of `PO-4`'s two named targets, one is delivered and one is not; and of the three
      correspondence items the sector lists, hypercharge is derived from the other two. ***

** ⇒⇒ WHAT `PO-4` ACTUALLY IS, AFTER THIS. **  *** Not "$\\su(3)$ and $\\su(2)_L$ as structures on the
cut" but "$\\su(2)_L$ AS A GAUGING -- a chiral action where the geometry currently supplies a discrete
swap." ***  ** One target, and its obstruction is named rather than open-ended. **

WHAT IS NOT CLAIMED.  ** Not that $SU(3)$ is delivered as a FORCE ** -- "the bundle above is flat, so the
construction supplies colour's exact selection rules and no force---it quantises and does not couple",
which is `PO-5`'s remaining half and not this one.  ** Not that the horn swap cannot become a gauging **
-- P14 says what it currently delivers, not what it forecloses.  ** Not that the $\\so(6)$ question is
meaningless ** -- only that ***the corpus reached $SU(3)$ without answering it***, so it is no longer the
route this row is waiting on.

Written r2626.  Stated for reversal.
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
    print("  B8 -- are PO-4's two targets in the same state?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(l for l in raw.split('\n') if l.startswith('| **PO-4**'))

    # the row
    check("⓵ PO-4's target: \"$\\su(3)$ and $\\su(2)_L$ as structures on the cut\"",
          '\\su(3)$ and $\\su(2)_L$ as structures on the cut' in row)
    check('and its status asks a REDUCTION question: "what reduces $\\so(6)\\to\\su(3)$?"',
          'what reduces $\\so(6)\\to\\su(3)$' in row)

    # ⓵ SU(3) is generated, not reduced
    check('⛭⛭ ⓶ and P14 GENERATES it instead: "the smallest connected group containing the three wall '
          'monodromies and the hinge $3$-cycle is $SU(3)$, with the lap as its centre"',
          'the smallest connected group containing the three wall monodromies and the hinge $3$-cycle '
          'is $SU(3)$' in p14 and 'with the lap as its centre' in p14)
    check('with the module named: "the module the operator\'s colour structure acts on is the branching '
          'rather than any bundle of the substrate"',
          "the module the operator's colour structure acts on is the branch" in p14)

    # ⓶ su(2)_L is not
    check('⛔ ⓷ and the SECOND target is explicitly not delivered: "Weak isospin as a gauging: $T$ is a '
          "discrete horn swap and delivers a species label, not $SU(2)_L$'s chiral action\"",
          'Weak isospin as a \\emph{gauging}' in p14 or 'a discrete horn swap and delivers a species '
          'label' in p14)
    check('with the difference located: "the two occupations differing on the right-handed pair"',
          'the two occupations differing on the right-handed pair' in p14)

    # ⓷ the scope reduction
    check('⓸ and the sector\'s own count is reduced: "So the undelivered content is two items and not '
          'three. What remains genuinely outstanding is the gauge group and the multiplet structure"',
          'the undelivered content is two items and not three' in p14
          and 'What remains genuinely outstanding is the gauge group and the multiplet structure' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-4's two targets have OPPOSITE verdicts, and its status line asks after a")
    print('  route the corpus did not take. **')
    print('  ⛭⛭ ⓵ ** $\\su(3)$ IS DELIVERED, and not by reducing anything: ** "the smallest connected')
    print('     group containing the three wall monodromies and the hinge 3-cycle is SU(3), with the lap')
    print('     as its centre".')
    print('     ⇒ ⛔ ** The row asks what REDUCES so(6) to su(3).  P14 GENERATES SU(3).  The status line')
    print('       has been waiting on a route the corpus did not take. **')
    print('  ⛔ ⓶ ** $\\su(2)_L$ IS NOT, and the reason is one clause: ** "T is a discrete horn swap and')
    print("     delivers a species label, ** not SU(2)_L's chiral action **\".")
    print('  ⓷ ** And the sector\'s own count is reduced: ** "the undelivered content is ** two items and')
    print('     not three **" -- hypercharge follows from the gauge group and the multiplet structure.')
    print('  ⇒⇒ ** So PO-4 is now ONE target with a NAMED obstruction: su(2)_L as a GAUGING -- a chiral')
    print('     action where the geometry currently supplies a discrete swap. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
