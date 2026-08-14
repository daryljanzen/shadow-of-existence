#!/usr/bin/env python3
"""B32 -- `PO-5`'s two bounds COMPOSE, and cc54's is the tighter half: a third mechanism must supply a
non-flat connection AND a fixed pure number, and the corpus supplies neither.

** THE TWO STATEMENTS, and they came from opposite directions. **
  * ** r2729 (this line): ** the two walls are ONE wall -- *** a coupling IS the coefficient of an
    $F^2$ term, and where $F\\equiv0$ there is no term for any coefficient to sit in front of.  The
    question restates as "WHERE CAN A GAUGE CONNECTION FAIL TO BE FLAT?" ***
  * ** c54.216 (cc54): ** the sentence walling the holonomy route ** mentions no route ** -- checked
    mechanically against `holonomy`, `isometry`, `flat`, `bundle`, `monodromy`, `winding`.  *** So it
    constrains the TARGET: whatever produces the connection, it must end in a four-dimensional
    Yang--Mills term, and that term requires a dimensionless number the ledger does not carry. ***

** ⛭⛭ ⓵ THEY ARE THE SAME WALL FROM TWO SIDES, AND THEY COMPOSE. **

      *** r2729   there is no F^2 TERM to put a coefficient in front of
          c54.216 there is no NUMBER to be the coefficient ***

  ⇒ *** A third mechanism must supply BOTH.  Neither statement alone closes the route; together they
      leave a candidate nothing to be made of. ***

** ⛔ ⓶ AND MINE WAS THE WEAKER HALF, WHICH IS WORTH SAYING PLAINLY. **  *** "Where can $F$ fail to be
flat?" is still a SEARCH over the substrate's geometry.  "Deliver a fixed pure number" is ONE TEST
against ONE quantity.  r2729 removed the word UNBOUNDED; c54.216 replaced the search with a test. ***

** ⓷ AND THE PREMISE IS ANOTHER PAPER'S LEDGER POSITION, ALREADY SETTLED. **  p0: "The one physical
length is $\\alpha$, not $\\ell_P$; their ratio $\\alpha/\\ell_P\\sim10^{61}$ ... is the size of the
universe in gauge-units---** a number, not a tuning **."
  ⇒⇒ *** So the row and the constant ledger are ONE QUESTION.  If $\\ell_P$ is a gauge the ledger holds
      no free dimensionless parameter and no mechanism of any kind can deliver a free coupling; if
      $\\ell_P$ were a second scale, $\\alpha/\\ell_P$ is free and the bound evaporates.  ** One position
      decides two rows. ** ***

** ⓸ AND P14 ALREADY CARRIES IT. **  *** cc54 banked the finding into the paper: "what a third
mechanism must deliver is therefore a fixed pure number rather than a free parameter, and a candidate
is accordingly falsifiable against one quantity rather than searched for in an unbounded space."  **The
row's residue is a TEST, and the paper states it.** ***

WHAT IS NOT CLAIMED.  ** Not that a third mechanism is excluded ** -- *** the bound says what one must
deliver, not that nothing can; a candidate producing a fixed pure number from the substrate would meet
it. ***  ** Not that r2729 is superseded ** -- the $F^2$ half is independent and still holds; what is
corrected is this line's framing of the residue as a search.  ** Not that the ledger position is
re-derived ** -- it is p0's, with `JanzenCRcosmology`'s $\\Lambda\\ell_P^2\\sim3\\times10^{-122}$ behind
it.

** COMPUTES: nothing numerical.  *** The composition is read from two receipts and two papers; the one
number quoted, $\\alpha/\\ell_P\\sim10^{61}$, is p0's. *** **

Written r2741.  Stated for reversal.
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
    print("  B32 -- do PO-5's two bounds compose, and which is tighter?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))

    # ⓵ cc54's half, now in the paper
    check('⓵ P14 carries cc54\'s bound: it "constrains the target rather than the mechanism: whatever '
          'produces the connection, what it must end in is a four-dimensional Yang--Mills term"',
          'constrains the \\emph{target} rather than the mechanism' in p14)
    check('and states the residue as a TEST rather than a search: "a fixed pure number rather than a '
          'free parameter, and a candidate is accordingly falsifiable against one quantity rather '
          'than searched for in an unbounded space"',
          'a fixed pure number rather than a free parameter' in p14
          and 'rather than searched for in an unbounded space' in p14)

    # ⓶ the premise is p0's
    check('⛭⛭ ⓶ and the premise is p0\'s ledger position: "The one physical length is $\\alpha$, not '
          '$\\ell_{P}$; their ratio ... is the size of the universe in gauge-units---a number, not a '
          'tuning"',
          'the size of the universe in gauge-units' in p0 and 'a number, not a tuning' in p0)
    check('with the source number behind it -- p0 cites the cosmology paper for '
          '$\\Lambda\\ell_P^2\\sim3\\times10^{-122}$',
          'JanzenCRcosmology' in p0)

    # ⓷ and the two halves are different objects
    check('⓷ while r2729\'s half is about the TERM, not the number: the register records that a '
          'coupling is the coefficient of an $F^2$ term and that $F\\equiv0$ leaves nothing to '
          'multiply',
          'F^2' in open(os.path.join(ROOT, 'PROTECTED_OPEN.md'),
                        encoding='utf-8', errors='replace').read())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the two bounds compose, and cc54\'s is the tighter half. **')
    print('  ⛭⛭ ⓵ ** THE SAME WALL FROM TWO SIDES: **')
    print('       r2729    there is no F² TERM to put a coefficient in front of')
    print('       c54.216  there is no NUMBER to be the coefficient')
    print('     ⇒ *** A third mechanism must supply BOTH — a non-flat connection AND a fixed pure')
    print('       number — and the corpus supplies neither. ***')
    print('  ⛔ ⓶ ** And mine was the weaker half. **  "Where can F fail to be flat?" is still a')
    print('     SEARCH over the substrate.  ** "Deliver a fixed pure number" is ONE TEST against ONE')
    print('     quantity. **  r2729 removed the word UNBOUNDED; c54.216 replaced the search with a')
    print('     test.')
    print('  ⓷ ** And the premise is p0\'s ledger position, already settled: ** the one physical length')
    print('     is α, not ℓ_P, and their ratio is a number in gauge-units, not a tuning.')
    print('     ⇒ *** So this row and the constant ledger are ONE QUESTION.  One position decides two')
    print('       rows. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
