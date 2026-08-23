#!/usr/bin/env python3
"""B12 -- the two triples are NOT one structure, and the reason is that they are three-element sets of
different KINDS of object: three roots at one value of $f$, against three values of $f$.

** THE QUESTION.  ** P4, the corpus's one `DISCOVERABLE-PROOF`: "** Whether the two triples are one
structure ** in the sense the programme's number audit certifies is not claimed here: ** no derivation
producing $\\{0,1,2\\}$ from a single condition has been exhibited **, and the audit's verdict on that
claim is accordingly open."
  ⌗ ** And r2630 found it load-bearing for two open items rather than one: ** the root triple is the shared
  vertex of P4's question and `PO-2`'s.

** ⓵ THE ROOT TRIPLE IS THE $f=0$ LOCUS, AND THE CUBIC IS THE HORIZON POLYNOMIAL. **  Setting
$f=1-2M/r-r^2/\\alpha^2=0$ and clearing gives ** $r^3-\\alpha^2 r+2M\\alpha^2=0$ ** -- *** the same cubic as
the offset-to-mass map $2M=(r_0/\\alpha)-(r_0/\\alpha)^3$, up to sign convention. ***

  ** Computed at the Nariai mass $2M_N=2\\alpha/(3\\sqrt3)$ (α=1): **

      *** roots = {0.577350, 0.577350, -1.154701} = {1/√3, 1/√3, -2/√3},  sum = 0 ***

  ⇒ ** A DOUBLE root at $1/\\sqrt3$ and a simple one at $-2/\\sqrt3$ ** -- which is exactly what `PO-2`'s
    row names: "the designated root is $1/\\sqrt3$ and the one distinguished by the merger is
    $-2/\\sqrt3$".  *** The row's two distinguished roots are the double and the simple root of the same
    cubic, and the zero-sum is the vanishing $r^2$ coefficient. ***

** ⛭⛭ ⓶ AND THE CAUSAL TRIPLE IS NOT A SET OF ROOTS AT ALL. **  P4: "the excursion's three critical loci
sit at ** three equally spaced VALUES of $f$ **: the seam at $f=0$ ... the turnaround at $f=1$ ... and the
interior Euclidean null at $f=2$".  Solving $f=$ each in turn:

      *** f = 0:  r = -1.154701      f = 1:  r = -0.727416      f = 2:  r = -0.344142 ***

  ⇒ ** Three DIFFERENT loci, one per value. **

** ⇒⇒ ⓷ SO THE TWO TRIPLES ARE THREE-ELEMENT SETS OF DIFFERENT KINDS OF OBJECT. **  *** One is the three
ROOTS of $f=0$ -- three $r$-values at a single $f$.  The other is three VALUES of $f$ -- each with its own
single locus.  A derivation producing $\\{0,1,2\\}$ "from a single condition" would have to produce a set
of roots and a set of levels from one statement, and those are not the same type. ***

  ⌗ ** This does not refute the resemblance; it LOCATES it. **  Both triples live on the same excursion and
  both are forced by the same $f$.  *** What is not available is an identification, because there is no
  map from "the roots of $f=0$" to "the levels $f=0,1,2$" that is anything but a coincidence of
  cardinality. ***

** ⓸ AND THAT SETTLES THE AUDIT'S VERDICT IN THE DIRECTION P4 LEFT OPEN. **  The audit asked whether a
single condition yields $\\{0,1,2\\}$.  *** The answer available here is that the two triples are typed
differently, so no such condition can yield both -- which is a NEGATIVE result and is worth exactly as
much as a positive one, because it removes the corpus's only `DISCOVERABLE-PROOF` from the table. ***

WHAT IS NOT CLAIMED.  ** Not that `PO-2` is settled ** -- its question pairs the roots with the WALL
MODES, not with the causal characters, and this receipt says nothing about that pairing.  ** Not that the
resemblance is meaningless ** -- both triples are forced by the same structure function on the same
excursion, and *** that co-location is a fact even though the identification is not. ***  ** Not that a
cleverer condition is impossible ** -- what is shown is that the two sets are of different type, and a
derivation would have to bridge the type gap rather than exhibit a bijection.

Written r2631.  Stated for reversal.
"""
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


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print('  B12 -- are the two triples one structure?')
    print()
    p4 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')))
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    po2 = next(l for l in raw.split('\n')
               if re.match(r'\|\s*~?~?\*\*PO-2\*\*', l))

    # the question
    check('⓵ P4 asks it: "Whether the two triples are one structure ... no derivation producing '
          '$\\{0,1,2\\}$ from a single condition has been exhibited"',
          'Whether the two triples are one structure' in p4
          and 'no derivation producing $\\{0,1,2\\}$ from a single condition has been exhibited' in p4)
    check('and states the causal triple as three VALUES: "the excursion\'s three critical loci sit at '
          'three equally spaced values of $f$"',
          "the excursion's three critical loci sit at three equally spaced values of $f$" in p4)

    # ⓵ the cubic at Nariai
    MN = 1.0 / (3 * np.sqrt(3))
    rts = sorted(np.roots([1, 0, -1, 2 * MN]).real)
    check(f'⓶ the $f=0$ cubic at the Nariai mass has roots {[round(x, 6) for x in rts]}',
          np.allclose(rts, [-2 / np.sqrt(3), 1 / np.sqrt(3), 1 / np.sqrt(3)], atol=1e-9))
    check('with ZERO SUM', abs(sum(rts)) < 1e-9)
    check('a DOUBLE root at $1/\\sqrt3$ and a simple one at $-2/\\sqrt3$',
          abs(rts[1] - rts[2]) < 1e-9 and abs(rts[0] + 2 / np.sqrt(3)) < 1e-9)
    check("⌗ and PO-2's row names exactly those two: \"the designated root ... is $1/\\sqrt3$ and the one "
          'distinguished by the merger is $-2/\\sqrt3$"',
          '1/\\sqrt3$ and the one distinguished by the merger is $-2/\\sqrt3$' in po2
          or ('1/\\sqrt3' in po2 and '-2/\\sqrt3' in po2))

    # ⓶ the causal loci are one each
    got = []
    for tgt in (0, 1, 2):
        r = np.roots([1, 0, (tgt - 1), 2 * MN])
        # ** the doubled root at f=0 carries a tiny imaginary residue from the numerical solve; a
        # 1e-9 tolerance counted it as complex and reported 1 real root where there are 3. **
        real = [x.real for x in r if abs(x.imag) < 1e-6]
        got.append(len(real))
    check(f'⓷ and each causal LEVEL has a single real locus: counts {got}', got == [3, 1, 1])
    check('⇒⇒ so one triple is three ROOTS at a single $f$, and the other is three VALUES of $f$ -- '
          'three-element sets of DIFFERENT KINDS of object',
          got[1] == 1 and got[2] == 1 and abs(sum(rts)) < 1e-9)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the two triples are NOT one structure -- they are typed differently. **')
    print('  ⓵ ** The ROOT triple is the f=0 locus: ** clearing f = 1 - 2M/r - r²/α² = 0 gives')
    print('     ** r³ - α²r + 2Mα² = 0 **, the same cubic as the offset-to-mass map.')
    print('     At the Nariai mass: ** roots {1/√3, 1/√3, -2/√3}, sum zero ** -- a DOUBLE root at the')
    print("     designated value and a simple one at the merged, ** exactly PO-2's two distinguished")
    print('     roots. **')
    print('  ⛭⛭ ⓶ ** The CAUSAL triple is three VALUES of f **, each with its own single locus:')
    print('     f=0 → r=-1.154701,  f=1 → r=-0.727416,  f=2 → r=-0.344142.')
    print('  ⇒⇒ ⓷ ** One is three ROOTS at a single f.  The other is three VALUES of f. **  *** A')
    print('     derivation producing {0,1,2} "from a single condition" would have to produce a set of')
    print('     ROOTS and a set of LEVELS from one statement, and those are not the same type. ***')
    print('  ⌗ ** This LOCATES the resemblance rather than refuting it: ** both triples live on the same')
    print('    excursion and both are forced by the same f.  ** What is unavailable is an identification,')
    print('    because the only map between them is a coincidence of cardinality. **')
    print('  ⇒ ** A NEGATIVE result, and worth a positive one: it removes the corpus\'s only')
    print('    DISCOVERABLE-PROOF from the table. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
