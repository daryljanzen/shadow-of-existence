#!/usr/bin/env python3
"""S6 -- `PO-6`'s TWO HALVES restated against seven revisions of this session: the condition half is
finished, and the satisfiability half has a determinate successor.

** THE ROW'S OWN STRUCTURE. **  `PO-6` declares "** this item's two halves are two halves rather than one
entangled question **", on D1's ground: the sub-threshold set's size is "** irrelevant to whether each of
its fibres receives a condition **", so a per-fibre condition cannot be broken by the number of fibres.

  ⇒ ** But the row never restates the two halves against what has since been established. **  *** Seven
    revisions of this session are in it and none is filed against a half -- the same defect r2683 found
    on `PO-2`, one row over. ***

** ⓵ HALF ONE -- THE CONDITION LIST -- IS FINISHED. **
      *** r2610: C1 and C2 are ONE condition, joined by "so" in P10.  Seven -> SIX.
          r2611: C6 is DERIVED from [Gamma-hat, radial] = 0, not a condition.  Six -> FIVE plus one
                 theorem, and the C6/C7 tension cannot arise. ***
  ⌗ ** And the row already says what that was: ** "*** Neither removal is a physics result; both were
    found by reading the passages that ARGUE the conditions. ***"

** ⛭⛭ ⓶ HALF TWO -- JOINT SATISFIABILITY -- HAS TURNED OVER COMPLETELY. **
      *** r2619: the open half is the FLOOR.
          r2651: the floor fails at cubic order.        ⛔ WITHDRAWN r2671.
          r2652: the state-fixer has its own threshold at Gamma = -1/4.
          r2671: THE FLOOR DOES SURVIVE -- P10 resums the cubic to pi^2/(1+lambda phi), positive on
                 non-degenerate metrics, and its receipt passes.  So r2652's sub-(-1/4) region is EMPTY.
          r2677: and the counterterm basis is ONE-DIMENSIONAL because the background family is -- but
                 the LAYER's Ricci scalar RUNS, so the degeneracy does not transfer without argument. ***

  ⇒⇒ *** So the satisfiability half is not "open".  It has a STATED SUCCESSOR: does the one-dimensional
      counterterm basis survive on a background whose curvature runs?  Stated object, known instrument
      (sub-leading heat-kernel coefficients), decidable answer -- registered `L-543`. ***

** ⓷ AND THE TWO HALVES ARE NOW ASYMMETRIC IN A WAY THE ROW DOES NOT SHOW. **  *** Half one is DONE and
was done by reading.  Half two is a CALCULATION nobody has run, and it belongs to 54.  A row that
declares "two halves" and reports neither state reads as one open item, which is what it has read as for
seven revisions. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-6` closes ** -- *** half two's successor is unrun and `F5` reserves
the strike. ***  ** Not that the five conditions are jointly satisfiable ** -- that IS half two, restated.
** Not that the successor is this line's ** -- it is a calculation, registered `L-543`, and 54 has the
live thread.

Written r2684.  Stated for reversal.
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


def main():
    print()
    print("  S6 -- what do PO-6's two halves stand at?")
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po6 = next(l for l in raw.split('\n') if l.startswith('| **PO-6**'))

    check('⓵ the row declares the structure: "this item\'s two halves are two halves rather than one '
          'entangled question"',
          "two halves are two halves rather than one entangled question" in po6)
    check("on D1's ground: the sub-threshold set's size is \"irrelevant to whether each of its fibres "
          'receives a condition"',
          'irrelevant to whether each of its fibres receives a condition' in po6)

    # ⓶ half one, finished
    for rev, what in (('r2610', 'C1 and C2 are ONE condition: seven -> six'),
                      ('r2611', 'C6 is derived, not a condition: six -> five plus one theorem')):
        check(f'⓶ HALF ONE, {rev}: {what}', rev in po6)
    check('and the row already names what that was: "Neither removal is a physics result; both were '
          'found by reading the passages that ARGUE the conditions"',
          'Neither removal is a physics result' in po6)

    # ⓷ half two, turned over
    for rev, what in (('r2619', 'the open half is the FLOOR'),
                      ('r2652', 'the state-fixer has its own threshold'),
                      ('r2671', 'THE FLOOR DOES SURVIVE -- P10 resums the cubic'),
                      ('r2677', 'the counterterm basis is one-dimensional; the LAYER runs')):
        check(f'⛭⛭ HALF TWO, {rev}: {what}', rev in po6)

        # ** r2722, cc54's c54.213: *** an absence receipt that FAILS because its finding was acted
        # on is a SUCCESS -- flipping the comparison would throw that away.  Converted to a
        # REGRESSION GUARD on the FILLING, naming the revision that did it. ***
    check('✔ FILLED r2684 -- the row now restates both halves, and the guard is that it keeps doing '
          'so: HALF ONE and HALF TWO are both named',
          ('HALF ONE' in po6 or 'HALF ①' in po6) and ('HALF TWO' in po6 or 'HALF ②' in po6))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** half one is FINISHED; half two has a STATED SUCCESSOR. **")
    print('  ⓵ ** HALF ONE -- the condition list -- is done, and was done by READING: ** C1=C2 are one')
    print('     condition (r2610, seven → six); C6 is derived from a commutator, not a condition (r2611,')
    print('     six → ** five plus one theorem **).  ** The row itself says "neither removal is a physics')
    print('     result". **')
    print('  ⛭⛭ ⓶ ** HALF TWO -- joint satisfiability -- has turned over completely: ** the floor was')
    print('     the open half (r2619), was said to fail (r2651), and ** DOES SURVIVE ** (r2671, P10')
    print('     resums the cubic) -- which empties r2652\'s sub-(-1/4) region.  And r2677 adds a')
    print('     ** one-dimensional counterterm basis ** whose transfer to the running LAYER is unproved.')
    print('     ⇒ ** So half two is not "open" but has a STATED SUCCESSOR: ** does the one-dimensional')
    print('       basis survive on a background whose curvature runs?  ** Registered L-543. **')
    print('  ⓷ *** And the two halves are now ASYMMETRIC in a way the row does not show: half one is DONE')
    print('     and was done by reading; half two is a CALCULATION nobody has run.  A row declaring "two')
    print('     halves" and reporting neither state reads as ONE open item -- which it has, for seven')
    print('     revisions. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
