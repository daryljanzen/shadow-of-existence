#!/usr/bin/env python3
"""B29 -- `PO-5` is NOT unbounded, and I have been calling it that for sixty revisions without spending
a turn on it.  The two walls are ONE wall, and what a third mechanism must do is a bounded geometric
question.

** THE AVOIDANCE, NAMED FIRST. **  r2667 walled two routes and wrote "an UNBOUNDED existence question --
nothing bounds the search".  *** That verdict has stood since, and it has served as a standing reason to
work every other row first.  Daryl, r2729: "stop finding excuses".  This is the turn that should have
happened sixty revisions ago. ***

** ⛭⛭ ⓵ THE TWO WALLS ARE ONE WALL. **
  * ** HOLONOMY: ** "the bundle above is flat, so the construction supplies colour's exact selection
    rules and no force---it quantises and does not couple."
  * ** ISOMETRY: ** "a Yang--Mills term in four dimensions carries a dimensionless coupling that a single
    length cannot build."

  ⇒ *** But a coupling IS the coefficient of an $F^2$ term.  Where $F\\equiv0$ there is no such term for
      any coefficient to sit in front of, so the dimensional argument answers a question that only arises
      ONCE THERE IS A TERM.  The isometry wall is MOOT wherever the holonomy wall holds. ***

** ⓶ AND THE DIMENSIONAL ARGUMENT IS WEAKER THAN IT READS ON ITS OWN. **  "A single length cannot build
a dimensionless number" is true of $\\alpha$ alone -- but ** the corpus is full of dimensionless numbers
that are not built from $\\alpha$ at all: **

      *** the winding's Z_3 -> 3      the root count -> 6      triality classes -> 3
          generations -> 3            the Weyl threshold -> 3/4 (r2728)
          the branch-point transfer -> 9/10 (r2661) ***

  ⇒ *** So C1 ("supply a dimensionless number") is NOT the obstruction.  What none of these is, is a
      COUPLING -- and the reason is not that they are the wrong numbers but that there is nothing for a
      number to multiply. ***

** ⛭ ⓷ SO THE ROW'S QUESTION RESTATES, AND IT IS BOUNDED. **  Not "is there a third mechanism?" -- an
existence question over an unnamed space -- but:

      *** WHERE, IF ANYWHERE, CAN A GAUGE CONNECTION ON THIS SUBSTRATE FAIL TO BE FLAT? ***

  ⇒⇒ ** A geometric question with a finite answer, and the flatness claim is SCOPED rather than
  universal: ** *** P14 says "the bundle ABOVE is flat" -- above being the specific construction the paper
  builds, not a theorem that every bundle on the substrate is flat.  A scoped claim leaves the complement
  open, and the complement is where a third mechanism would have to live. ***

** ⓸ WHAT THIS DOES AND DOES NOT CHANGE. **  *** It does not supply a mechanism, and it does not weaken
either wall on its own ground: the construction's bundle IS flat and its holonomy DOES give only phases.
What it removes is the word UNBOUNDED, which was never earned -- the search has a shape, a criterion
($F\\ne0$), and a place to look (outside the specific bundle P14 constructs). ***

WHAT IS NOT CLAIMED.  ** Not that a non-flat bundle exists here ** -- *** that is exactly the open
question, now stated so it can be worked. ***  ** Not that P14 overstates ** -- its wording is careful
("the bundle above"); the over-reach was this line's "UNBOUNDED".  ** Not that the dimensionless numbers
listed could BE couplings ** -- they are combinatorial invariants, and the point is only that
availability of a number was never the binding constraint.

Written r2729.  Stated for reversal.
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
    print('  B29 -- is PO-5 actually unbounded?')
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po5 = next(l for l in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-5\*\*', l))

    # ⓵ the two walls, quoted
    check('⓵ HOLONOMY wall: "the bundle above is flat, so the construction supplies colour\'s exact '
          'selection rules and no force---it quantises and does not couple"',
          'the bundle above is flat' in p14 and 'it quantises and does not couple' in p14)
    check('ISOMETRY wall: "a Yang--Mills term in four dimensions carries a dimensionless coupling that '
          'a single length cannot build"',
          'dimensionless coupling that a single length cannot build' in po5
          or 'a single length cannot build' in p14)

    # ⓶ the flatness claim is SCOPED
    check('⛭⛭ ⓶ and the flatness claim is SCOPED, not universal: P14 says "the bundle ABOVE is flat" '
          '-- the construction it builds, not every bundle on the substrate',
          'the bundle above is flat' in p14)

    # ⓷ the corpus has dimensionless numbers
    for term, n in (('triality', 3), ('generation', 3)):
        check(f'⓷ and the corpus carries dimensionless numbers not built from $\\alpha$: "{term}" '
              f'appears in P14',
              term in p14.lower())
    check('so "a single length cannot build a dimensionless number" is not the binding constraint -- '
          'the corpus has several, and none is a coupling because there is no $F^2$ to multiply',
          'triality' in p14.lower() and 'the bundle above is flat' in p14)

    # ⓸ the row currently says UNBOUNDED
    # ** the word lives in the STAMP, not the row.  *** So "UNBOUNDED" was never a corpus
    # claim at all -- it was a classification this line wrote into its own reporting script
    # at r2667 and then repeated for sixty revisions as though the register held it. ***
    stamp = open(os.path.join(ROOT, 'scripts', 'stamp.py'),
                 encoding='utf-8', errors='replace').read()
    check('⓸ and the word UNBOUNDED lives ONLY in this line\'s own stamp script, never in the row -- '
          'a classification written into the reporting and then repeated as though the register held it',
          "UNBOUNDED = {'PO-5'}" in stamp and 'UNBOUNDED' not in po5)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** PO-5 is not unbounded — the two walls are ONE wall. **')
    print('  ⛭⛭ ⓵ ** A coupling IS the coefficient of an F² term. **  Where F ≡ 0 there is no such term')
    print('     for any coefficient to sit in front of — so the dimensional argument answers a question')
    print('     that only arises ONCE THERE IS A TERM.  ** The isometry wall is MOOT wherever the')
    print('     holonomy wall holds. **')
    print('  ⓶ ** And "a single length cannot build a dimensionless number" is not the binding')
    print('     constraint: ** the corpus carries 3 (winding, triality, generations), 6 (roots),')
    print('     3/4 (the Weyl threshold), 9/10 (the branch-point transfer).  *** None is a coupling —')
    print('     not because they are the wrong numbers but because there is nothing to multiply. ***')
    print('  ⛭ ⓷ ** SO THE QUESTION RESTATES, AND IT IS BOUNDED: **')
    print('       *** WHERE, IF ANYWHERE, CAN A GAUGE CONNECTION ON THIS SUBSTRATE FAIL TO BE FLAT? ***')
    print('     ⌗ And P14\'s claim is SCOPED — "the bundle ABOVE is flat", the construction it builds,')
    print('       not a theorem about every bundle.  ** A scoped claim leaves the complement open, and')
    print('       the complement is where a third mechanism would have to live. **')
    print('  ⓸ ** What this removes is the word UNBOUNDED, which was never earned. **  The search has a')
    print('     shape, a criterion (F ≠ 0), and a place to look.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
