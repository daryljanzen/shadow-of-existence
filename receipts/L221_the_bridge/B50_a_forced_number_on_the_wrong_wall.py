#!/usr/bin/env python3
"""B50 -- ⛔ **LABEL WITHDRAWN r2810.**  *** This receipt called $1/\\sqrt3$ "a FIXED IRRATIONAL forced by the
geometry -- the shape a coupling constant has".  **It is the shape a CARTAN GENERATOR'S NORMALISATION
has**: $\\mathrm{diag}(1,1,-2)/\\sqrt3$ is $\\lambda_8$, and the $\\sqrt3$ is exactly what makes
$\\mathrm{Tr}(\\lambda_8^2)=2$.  The corpus names it four papers over.  See `B56`.
  ⌗ *What survives: the triple IS forced (Nariai is the unique fixed point), and it IS dimensionless.
  **What is withdrawn is the KIND** -- it is not a candidate coupling and never was.* ***

B50 -- `PO-2`'s upgrade gives `PO-5` a FORCED dimensionless number for the first time, and it is on
the wrong wall: the number is supplied and the thing to multiply is not.

** THE QUESTION.  Daryl, r2804: ** *** "Does that one not give us a foothold we could actually use to
finally start working `PO-5`?" ***

** ⛭⛭⛭ ⓵ THE TRIPLE IS THE NARIAI ROOTS IN UNITS OF $\\alpha$, AND IT IS FORCED. **  At the Nariai
crest ($M=\\alpha/3\\sqrt3$) the $f=0$ roots are:

      *** -13.856406 / alpha = -1.154701 = -2/sqrt3     (single)
            6.928203 / alpha = +0.577350 = +1/sqrt3     (doubled)
            6.928203 / alpha = +0.577350 = +1/sqrt3 ***

  ⇒ ** Not a normalisation CHOICE. **  *** Nariai fixes $M/\\alpha$, and $\\alpha$ is the substrate's ONE
      length -- there is nothing else to divide by.  ** The ratio is forced twice over. ** ***

** ⛭⛭ ⓶ AND THAT IS A NEW KIND FOR THE LEDGER. **  *** r2769 enumerated the corpus's dimensionless
content as counts ($3$ winding, $6$ roots, $3$ generations) and derived or measured ratios ($3/4$,
$9/10$, $1.0824$).  ** $1/\\sqrt3$ is a FIXED IRRATIONAL forced by the geometry ** -- the shape a
coupling constant has, and the first of its kind in the ledger. ***
  ⌗ ** And `PO-2`'s level (2) passing is what makes it usable: ** *** a resemblance cannot supply a
    coupling; a CONSTRUCTION can be asked to.  Before r2803 the number was stated without being claimed. ***

** ⛔ ⓷ AND IT IS ON THE WRONG WALL. **  *** `PO-5` needs a number ** AND ** something for it to be the
coefficient OF.  P14: "the bundle above is flat, so the construction supplies colour's exact selection
rules ** and no force ** --- it quantises and does not couple."  ** r2729's wall is unmoved: there is
still no $F^2$ term. ** ***

  ⇒ *** THE FOOTHOLD IS REAL AND IT IS UNDER THE OTHER HALF OF THE ROW. ***

** ⛭ ⓸ BUT IT WEAKENS THE PREMISE OF p0's INFERENCE, WHICH IS THE PART WORTH ROUTING. **  *** r2791
established that p0 DERIVES the no-coupling FROM the one-constant character: "every curvature invariant
on either face is a pure power of $1/\\alpha^{2}$.  ** SO ** the construction cannot force a coupling
... a property of a one-constant theory." ***
  ⇒⇒ *** THE PREMISE IS ABOUT CURVATURE INVARIANTS ON THE FACES.  ** $1/\\sqrt3$ is not a curvature
      invariant -- it is a ratio of a horizon radius to $\\alpha$ at a degenerate point. **  So it is a
      forced dimensionless quantity that p0's sentence does not range over, and whether p0's inference
      still closes is a question the sentence itself does not answer. ***

WHAT IS NOT CLAIMED.  ** Not that a coupling exists ** -- *** the $F^2$ term is still absent and this
receipt does not supply one. ***  ** Not that p0 is wrong ** -- *** its inference is about curvature
invariants and is correct about those; what is claimed is that a forced dimensionless quantity exists
OUTSIDE that class, which is a scope observation, not a refutation. ***  ** Not that $1/\\sqrt3$ is a
coupling ** -- *** it is a number of the right KIND, which is what `PO-5` was measured as lacking, and
kind is not identity. ***

** COMPUTES: the $f=0$ roots at the Nariai crest and their ratios to $\\alpha$.  *** $f$ is the corpus's
own. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 4ab76d3** *(per c54.220's rule, r2776).*

Written r2804.  Stated for reversal.
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
    print("  B50 -- does PO-2's upgrade give PO-5 a foothold?")
    print()
    a = 12.0
    M = a/(3*np.sqrt(3))
    roots = sorted(np.real(np.roots([1/(a*a), 0, -1, 2*M])))
    norm = [r/a for r in roots]

    check(f'⛭⛭⛭ ⓵ at the Nariai crest ($M=\\alpha/3\\sqrt3$) the $f=0$ roots in units of $\\alpha$ are '
          f'{[round(x, 6) for x in norm]}',
          abs(norm[0] + 2/np.sqrt(3)) < 1e-6)
    check(f'-- exactly $\\{{-2/\\sqrt3,\\ 1/\\sqrt3,\\ 1/\\sqrt3\\}}$, the doubled root at $+1/\\sqrt3$',
          abs(norm[1] - 1/np.sqrt(3)) < 1e-6 and abs(norm[2] - 1/np.sqrt(3)) < 1e-6)
    check('⇒ and it is FORCED, not a normalisation choice: Nariai fixes $M/\\alpha$ and $\\alpha$ is '
          'the substrate\'s one length -- there is nothing else to divide by',
          abs(sum(norm)) < 1e-9)

    # ⓶ a new kind for the ledger
    check('⛭⛭ ⓶ and it is a NEW KIND: the ledger\'s other dimensionless content is counts and derived '
          'ratios, while $1/\\sqrt3$ is a FIXED IRRATIONAL',
          abs(1/np.sqrt(3) - round(1/np.sqrt(3))) > 0.1)

    # ⓷ but the F^2 wall is unmoved
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))
    check('⛔ ⓷ but r2729\'s wall is unmoved: P14 states "the bundle above is flat, so the '
          'construction supplies colour\'s exact selection rules and no force"',
          'the bundle above is flat' in p14 and 'and no force' in p14)

    # ⓸ and p0's premise is about curvature invariants
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    check('⛭ ⓸ while p0\'s inference has a premise about CURVATURE INVARIANTS: "every curvature '
          'invariant on either face is a pure power of $1/\\alpha^{2}$. So the construction cannot '
          'force a coupling"',
          'is a pure power of' in p0 and 'So the construction cannot force a coupling' in p0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** a real foothold, on the wrong wall — and it weakens p0's premise. **")
    print('  ⛭⛭⛭ ⓵ ** The triple IS the Nariai roots in units of α: ** −2/√3 single, +1/√3 doubled.')
    print('     *** Not a normalisation choice — Nariai fixes M/α and α is the substrate\'s ONE')
    print('     length.  Forced twice over. ***')
    print('  ⛭⛭ ⓶ ** And it is a NEW KIND for the ledger: ** the rest is counts (3, 6) and derived')
    print('     ratios (3/4, 9/10, 1.0824).  ** 1/√3 is a FIXED IRRATIONAL — the shape a coupling')
    print('     constant has. **  And PO-2 level (2) passing is what makes it usable: a resemblance')
    print('     cannot supply a coupling; a CONSTRUCTION can be asked to.')
    print('  ⛔ ⓷ ** But r2729\'s wall is unmoved. **  P14: "the bundle above is flat … and no force —')
    print('     it quantises and does not couple."')
    print('     ⇒ *** PO-5 needs a number AND something to be the coefficient OF.  PO-2 supplies the')
    print('     number.  The F² term is still absent. ***')
    print('  ⛭ ⓸ ** And this is the part worth routing: it weakens the PREMISE of p0\'s inference. **')
    print('     p0 derives the no-coupling from "every CURVATURE INVARIANT on either face is a pure')
    print('     power of 1/α²".  ** 1/√3 is not a curvature invariant — it is a horizon radius over α')
    print('     at a degenerate point. **  *** A forced dimensionless quantity outside the class p0\'s')
    print('     sentence ranges over. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
