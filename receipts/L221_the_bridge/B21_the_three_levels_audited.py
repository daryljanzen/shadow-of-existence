#!/usr/bin/env python3
"""B21 -- `PO-2`'s hold has THREE NAMED LEVELS, and this session answered two of them without ever
checking against the naming: level (2) is passed, and level (3) is narrower than "walled".

** THE HOLD, as `PO-2` states it. **  "Held at ** do-not-assert on three separated levels **."  The
levels are named in `GEOMETRY_PHYSICS_TAXONOMY`: "** the three levels --- (1) skeleton grounded, (2)
resemblance do-not-assert, (3) identification walled --- stand exactly as r693 set them **."

** ⛔ ⓵ AND FOUR REVISIONS THIS SESSION ANSWERED AGAINST THEM WITHOUT NAMING THEM. **  All four notes are
in the row; *** none is filed against the level it answers, so the row reads as four independent findings
when it records a level-by-level state change. ***

      *** (1) skeleton grounded          r2631: the root triple IS the f=0 locus, roots
                                          {1/sqrt3, 1/sqrt3, -2/sqrt3}, sum zero.  COMPUTED.
          (2) resemblance do-not-assert  r2629: the resemblance is a CONSTRUCTION -- the three modes
                                          are one operator's kernel, the channel count is computed.
                                          r2633: and its REASON -- "the three carry one mass parameter
                                          and are identical in content".
          (3) identification walled      r2632: P14 EXHIBITS the map -- roots -> hinges -> walls ->
                                          modes, "the Weyl S_3 IS the relation among the three
                                          hinges". *** 

** ⛭⛭ ⓶ SO LEVEL (2) IS PASSED, AND SAYING SO IS THE POINT. **  *** A "resemblance do-not-assert" is a
hold against reading a similarity as a fact.  When the similarity becomes a construction -- identical
content by one $2M$, a bare label, a within-state index, $SU(3)$ generated -- the hold has nothing left to
guard.  It was calibrated to an object that no longer exists. ***

** ⓷ AND LEVEL (3) IS NARROWER THAN "WALLED". **  *** P14 exhibits the structural identification and
r2632 verified it.  What remains walled is the PHYSICAL one: that the roots ARE colour charge, as against
carrying a structure isomorphic to colour's. ***
  ⌗ ** Which is exactly what `PO-5`/`PO-4`独 established from the other side: ** *** the construction
    delivers a discrete label at the centre and no coupling -- so "these are colour" cannot be asserted
    while what colour DOES is absent. ***  ** The wall is not on the map; it is on the force. **

WHAT IS NOT CLAIMED.  ** Not that `PO-2` closes ** -- level (3) stands and `F5` reserves the strike.
** Not that the taxonomy is wrong ** -- *** r693 set three levels and all three were right; two have since
been answered and the catalogue was never told. ***  ** Not that the physical identification is
impossible ** -- it waits on the coupling, which `PO-5` walls on two routes and leaves a third unnamed.

Written r2683.  Stated for reversal.
"""
import os
import subprocess
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
    print("  B21 -- what do PO-2's three levels stand at now?")
    print()
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po2 = next(l for l in raw.split('\n') if l.startswith('| **PO-2**'))
    tax = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'GEOMETRY_PHYSICS_TAXONOMY.md'),
                                   encoding='utf-8', errors='replace').read())

    check('⓵ the row states the hold: "Held at do-not-assert on three separated levels"',
          'do-not-assert on three separated levels' in po2)
    check('and the taxonomy names them: "(1) skeleton grounded, (2) resemblance do-not-assert, '
          '(3) identification walled"',
          'skeleton grounded' in tax and 'resemblance do-not-assert' in tax
          and 'identification walled' in tax)
    # ** ⛭ AMENDED c54.230, CROSS-BAND AND ROUTED: this quoted a sentence r2803 CORRECTED, and the
    # ** correction is this receipt's own finding landing. **  `B21`'s ⓵ is that four revisions answered
    # ** against the three levels without naming them; r2803 read the same thing in the document
    # ** ("170 revisions stale") and rewrote it.
    #   ⇒ *** So the pin broke because the argument won.  Both ends are pinned: the wording at the
    #       commit where it stood, and the CURRENT sentence asserted separately. ***
    _BEFORE_R2803 = '4ab76d3~1'   # the commit before r2803
    _tax_then = subprocess.run(
        ['git', 'show', f'{_BEFORE_R2803}:GEOMETRY_PHYSICS_TAXONOMY.md'],
        cwd=ROOT, capture_output=True, text=True, errors='replace').stdout
    check(f'as set at r693 and still standing at {_BEFORE_R2803} (before r2803): "stand exactly as r693 set them"',
          'stand exactly as r693 set them' in _tax_then)
    check('⛭ AND r2803 CORRECTED IT, which is this receipt\'s own finding arriving in the document: '
          '"THE THREE LEVELS NO LONGER STAND AS r693 SET THEM"',
          'NO LONGER STAND AS r693 SET THEM' in tax
          and 'stand exactly as r693 set them' not in tax)

    # ⓶ this session's four answers are all in the row
    for rev, what in (('r2631', 'level (1): the root triple IS the f=0 locus'),
                      ('r2629', 'level (2): the resemblance became a CONSTRUCTION'),
                      ('r2633', 'level (2): and its reason, identical in content'),
                      ('r2632', 'level (3): P14 exhibits the structural map')):
        check(f'⓶ {rev} is in the row -- {what}', rev in po2)

        # ** r2722, cc54's c54.213: *** an absence receipt that FAILS because its finding was acted
        # on is a SUCCESS -- flipping the comparison would throw that away.  Converted to a
        # REGRESSION GUARD on the FILLING, naming the revision that did it. ***
    check('✔ FILLED r2683 -- the row now names the three levels, and the guard is that it keeps '
          'doing so',
          '(1) skeleton grounded' in po2 and '(2) resemblance do-not-assert' in po2
          and '(3) identification walled' in po2
          and 'THE STATE NOW' in po2.upper())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** level (2) is PASSED and level (3) is narrower than 'walled'. **")
    print('  ⓵ ** The hold has three NAMED levels ** -- (1) skeleton grounded, (2) resemblance')
    print('     do-not-assert, (3) identification walled -- ** and four revisions this session answered')
    print('     against them without naming them. **')
    print('  ⛭⛭ ⓶ ** LEVEL (2) IS PASSED. **  *** A "resemblance do-not-assert" guards against reading a')
    print('     similarity as a fact.  When the similarity becomes a CONSTRUCTION -- identical content by')
    print('     one 2M, a bare label, a within-state index, SU(3) generated -- the hold has nothing left')
    print('     to guard.  It was calibrated to an object that no longer exists. ***')
    print('  ⓷ ** LEVEL (3) IS NARROWER THAN "WALLED". **  P14 exhibits the STRUCTURAL identification and')
    print('     r2632 verified it.  ** What remains walled is the PHYSICAL one: that the roots ARE colour')
    print('     charge, as against carrying a structure isomorphic to colour\'s. **')
    print('     ⇒ *** Which PO-5 establishes from the other side: the construction delivers a label at')
    print('       the centre and NO coupling.  So "these are colour" cannot be asserted while what colour')
    print('       DOES is absent.  The wall is not on the map; it is on the FORCE. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
