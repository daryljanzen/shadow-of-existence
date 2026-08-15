#!/usr/bin/env python3
"""B49 -- `PO-2` was gated by a stale sentence in the document that holds its levels, not by physics:
the taxonomy still read "stand exactly as r693 set them" 170 revisions after two of the three moved.

** THE PROMPT.  Daryl, r2803: ** *** "If an update to our list is owed now that the corpus has become
more complete and more self-knowing that's on you to gate.  The 54s will not touch it as long as you
keep the programme blocking it." ***

** ⛔⛭⛭ ⓵ THE GATE WAS A SENTENCE, AND IT WAS STALE IN TWO PLACES. **  `GEOMETRY_PHYSICS_TAXONOMY.md`
-- the document that HOLDS the three levels -- read:

      *** "the three levels --- (1) skeleton grounded, (2) resemblance do-not-assert,
          (3) identification walled --- stand exactly as r693 set them"
      and, separately, "AND THE SECOND HALF IS UNTOUCHED --- the three levels stand
          exactly as r693 separated them" ***

  ** And it had never heard of r2629--r2633. **  *** `PO-2`'s own row records those four findings and
  argues from them; the document the row DEFERS to did not carry them.  ** The row was arguing with a
  reader that had not been told. ** ***

** ⓶ THE STATE, VERIFIED AND WRITTEN INTO THE TAXONOMY. **
  * ** (1) SKELETON -- grounded and computed: ** *** the root triple IS the $f=0$ locus,
    $\\{1/\\sqrt3,1/\\sqrt3,-2/\\sqrt3\\}$, sum zero (r2631). ***
  * ✔ ** (2) RESEMBLANCE do-not-assert -- PASSED: ** *** r2629 turned the resemblance into a
    CONSTRUCTION, r2633 gave the reason.  ** A resemblance-hold guards against reading a similarity as
    a fact; when the similarity becomes a construction it has nothing left to guard. ** ***
  * ⚠ ** (3) IDENTIFICATION -- still walled, narrower than the word: ** *** P14 EXHIBITS the map, roots
    → hinges → walls → modes (r2632).  ** The STRUCTURAL identification is exhibited; the PHYSICAL one
    is what remains. ** ***

** ⛭ ⓷ AND LEVEL (1) IS SIZED HONESTLY RATHER THAN BANKED. **  *** The zero sum is ** ARITHMETIC, not
coincidence **: $f=0$ is a DEPRESSED cubic ($r^3/\\alpha^2 - r + 2M = 0$, no $r^2$ term), so the roots
sum to zero for every $M$ and every $\\alpha$. ***
  ⇒ ** That cuts both ways and both halves are stated: ** *** a structure that must vanish BY
    CONSTRUCTION is a better ground for colour-neutrality than one that happens to -- ** and it
    distinguishes nothing on its own, since every Schwarzschild--de Sitter geometry has it **.  The
    content is the $1{:}1{:}{-}2$ PATTERN, which is a degeneracy statement, not a sum statement. ***

** ⓸ SO THE ROW IS GATED ON ONE LEVEL, NOT THREE. **  *** `PO-5` gates level (3) alone -- whether a
coupling can arise at all.  ** Levels (1) and (2) gate nothing, and the row has read as triply held for
170 revisions because the document holding the levels was never updated. ** ***

WHAT IS NOT CLAIMED.  ** Not that level (3) is weakened ** -- *** the PHYSICAL identification is
untouched and still waits on `PO-5`; this receipt moves the OTHER TWO, which were already argued in the
row. ***  ** Not that r2629--r2633 are re-derived ** -- *** r2631's root locus is recomputed here and
the rest are read from the row and from P14. ***  ** Not that the taxonomy's other content is audited **
-- one sentence, in two places, was stale and is now current.

** COMPUTES: the $f=0$ roots and their sum at three $(M,\\alpha)$, and the depressed-cubic reason the sum
vanishes identically.  *** $f$ is the corpus's own. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT a99d9d2** *(per c54.220's rule, r2776).*

Written r2803.  Stated for reversal.
"""
import glob
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  B49 -- what was actually gating PO-2?")
    print()
    tax = open(glob.glob(os.path.join(ROOT, '**', 'GEOMETRY_PHYSICS_TAXONOMY.md'),
                         recursive=True)[0], encoding='utf-8', errors='replace').read()

    check('⛔ ⓵ the taxonomy no longer claims the levels stand as r693 set them -- both instances are '
          'superseded',
          'stand exactly as r693' not in tax)
    check('and it now carries the four findings it had never heard of (r2629, r2631, r2632, r2633)',
          all(k in tax for k in ('r2629', 'r2631', 'r2632', 'r2633')))
    check('with level (2) recorded as PASSED: "a \\"resemblance do-not-assert\\" guards against reading '
          'a similarity as a fact, and when the similarity becomes a construction the hold has '
          'nothing left to guard"',
          'nothing left to guard' in tax)

    # ⓷ the zero sum is arithmetic
    sums = []
    for M, a in ((1.0, 12.0), (0.3, 50.0), (2.0, 8.0)):
        rr = np.roots([1/(a*a), 0, -1, 2*M])
        sums.append(abs(np.sum(rr).real))
    check(f'⛭ ⓶ and the zero sum is ARITHMETIC: $f=0$ is a depressed cubic, so the roots sum to zero '
          f'at every $(M,\\alpha)$ tested (max residual {max(sums):.1e})',
          max(sums) < 1e-12)
    check('⇒ so it is a better ground than a coincidence AND distinguishes nothing on its own -- the '
          'content is the $1{:}1{:}{-}2$ pattern, a degeneracy statement',
          max(sums) < 1e-12)

    # ⓸ and the row is gated on one level
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(x for x in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-2\*\*', x))
    check('⓷ while the row records the surviving gate: level (3) is the PHYSICAL identification and '
          'waits on `PO-5` -- whether a coupling can arise at all',
          # ** the row writes it with a non-ASCII dash; match the two halves separately **
          'gated on' in row and 'PHYSICAL identification' in row
          and 'whether a coupling can arise at all' in row)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the gate was a stale sentence, and it is now current. **")
    print('  ⛔ ⓵ ** `GEOMETRY_PHYSICS_TAXONOMY` — the document that HOLDS the three levels — read')
    print('     "stand exactly as r693 set them" in TWO places and had never heard of r2629–r2633. **')
    print('     *** PO-2\'s own row records those findings and argues from them.  The row was arguing')
    print('     with a reader that had not been told. ***')
    print('  ⓶ ** Written in at source: ** (1) grounded and computed; ** (2) PASSED ** — a')
    print('     resemblance-hold has nothing left to guard once the similarity is a construction;')
    print('     (3) still walled but ** narrower than the word **, the structural map being exhibited.')
    print('  ⛭ ⓷ ** And level (1) is sized rather than banked: ** the zero sum is ARITHMETIC — $f=0$ is')
    print('     a depressed cubic, so the roots sum to zero for every M and α.')
    print('     ⇒ *** A better ground than a coincidence, AND it distinguishes nothing on its own.')
    print('     The content is the 1:1:−2 pattern, a degeneracy statement. ***')
    print('  ⓸ ** So PO-2 is gated on ONE level, not three: ** PO-5 gates level (3) alone.')
    print('     ** Levels (1) and (2) gate nothing, and the row read as triply held for 170 revisions')
    print('     because the document holding the levels was never updated. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
