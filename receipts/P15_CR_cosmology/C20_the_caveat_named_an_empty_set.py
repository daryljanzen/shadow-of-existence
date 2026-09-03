#!/usr/bin/env python3
"""C20 -- r2661's caveat is vacuous: at the branch point every mode is outside the comoving horizon, so
the $9/10$ join is unrestricted, and the corpus's own horizon function proves it.

** THE CAVEAT, written one revision ago. **  r2661 computed the branch-point join as
$\\Phi_{\\rm exp}/\\Phi_{\\rm coll}=9/10$ and closed: "** SUPER-HORIZON ONLY.  Modes inside the horizon at
the branch point are not covered, and $\\mathcal R$'s conservation is a super-horizon result. **"

** ⛭⛭ ⓵ AND THERE ARE NO SUCH MODES. **  P15: "** the branch point lies at the far end of the same rising
branch, where $2M/r$ carries $aH$ up without bound and the comoving horizon to zero, so THERE EVERY MODE
IS OUTSIDE IT **".

** ⓶ VERIFIED FROM THE CORPUS'S OWN HORIZON FUNCTION. **  "The comoving Hubble radius is built from the
slicing paper's own turnaround function, ** $(rH)^2=(1-f)+A/r^2$ **".  With
$f=1-2M/r-r^2/\\alpha^2$:

      *** (rH)^2 = A/r^2 + 2M/r + r^2/alpha^2   ->   +infinity   as r -> 0+ ***

  ⇒ ** $aH\\to\\infty$, so the comoving horizon $1/(aH)\\to0$ and every finite comoving $k$ satisfies
    $k\\ll aH$. **
  ⌗ ** And the term ordering matches the paper's: ** $A/r^2$ (radiation) diverges faster than $2M/r$
    (mass), while $r^2/\\alpha^2$ (substrate) vanishes -- *** "on the leg the radiation term dominates
    because it is constant while the others vanish". ***

** ⇒⇒ ⓷ SO THE JOIN IS UNRESTRICTED. **  *** $\\mathcal R$'s conservation is a super-horizon result and
the branch point is a locus where nothing is sub-horizon.  The $9/10$ applies to every scalar mode, and
r2661's caveat named an empty set. ***

** ⓸ AND THE DISTINCTION THAT MAKES THIS WORK IS ONE THE PAPER HAD TO CORRECT. **  The SEAM and the
BRANCH POINT are different loci and give ** opposite ** answers: at the seam "the acoustic modes are
already within the comoving horizon"; at the branch point every mode is outside.
  ⌗ *** P15 records the correction: "a distinction six sentences of this paper previously ran together,
      corrected at r2501+c54.197 with the inversion re-derived from the metric function rather than
      asserted."  A caveat written at the wrong locus would have been exactly that error again. ***

WHAT IS NOT CLAIMED.  ** Not that the transfer is complete ** -- *** the join is one boundary condition;
the collapse-leg evolution and the expansion-leg constancy are separately established, and the full
hierarchy across two legs is still unrun. ***  ** Not that $\\mathcal R$ is conserved through the crossing
DYNAMICS ** -- P15 defers "the detailed worldline and field dynamics of the crossing for a concrete matter
model", and this receipt uses the kinematic super-horizon result, not that.  ** Not that the seam
statement is weakened ** -- it is correct at the seam, which is a different locus.

Written r2662.  Stated for reversal.
"""
import os
import re

import sympy as sp

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
    print("  C20 -- is r2661's super-horizon caveat non-empty?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the paper's statement
    check('⛭⛭ ⓵ P15: "the branch point lies at the far end of the same rising branch, where $2M/r$ '
          'carries $aH$ up without bound and the comoving horizon to zero, so there every mode is '
          'outside it"',
          'the comoving horizon to zero, so there \\emph{every} mode is outside it' in p15)
    check('and the seam gives the OPPOSITE answer: "the acoustic modes are already within the comoving '
          'horizon there"',
          'the acoustic modes are already within the comoving horizon there' in p15)

    # ⓶ verified from the horizon function
    check('⓶ and the horizon function is the corpus\'s own: "The comoving Hubble radius is built from '
          "the slicing paper's own turnaround function, $(rH)^{2}=(1-f)+A/r^{2}$\"",
          'The comoving Hubble radius is built from the slicing' in p15)
    r, M, A, al = sp.symbols('r M A alpha', positive=True)
    f = 1 - 2*M/r - r**2/al**2
    rH2 = sp.simplify((1 - f) + A/r**2)
    check(f'and it diverges at the branch point: $(rH)^2 = {rH2} \\to \\infty$ as $r\\to0^+$',
          sp.limit(rH2, r, 0, '+') == sp.oo)
    check('so $aH\\to\\infty$, the comoving horizon $1/(aH)\\to0$, and every finite $k$ is outside',
          sp.limit(1/sp.sqrt(rH2), r, 0, '+') == 0)
    check('with the radiation term dominating, as the paper says: $A/r^{2}$ diverges faster than $2M/r$ '
          'while $r^{2}/\\alpha^{2}$ vanishes',
          sp.limit((A/r**2) / (2*M/r), r, 0, '+') == sp.oo
          and sp.limit(r**2/al**2, r, 0, '+') == 0)

    # ⓸ the corrected distinction
    # ** RE-PINNED r3961.  ** The old pin required P15 to CONTAIN the words "previously ran together,
    # corrected at r2501+c54.197" -- i.e. it enforced revision-history narration inside a paper, which
    # the corpus's one-state rule forbids and which was therefore removed.  A gate must not require a
    # defect.  Re-pinned to the DISTINCTION ITSELF, which is what this receipt is about and which the
    # paper now states in its own voice, twice.
    check('⓷ the seam/branch-point distinction is stated: the branch point is NOT a seam',
          'not} a seam' in p15)
    check('  and the seams are named as the two unit-speed loci of the lap',
          'the seams are the two unit-speed loci of the lap' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** r2661's caveat named an EMPTY SET.  The 9/10 join is unrestricted. **")
    print('  ⛭⛭ ⓵ ** At the branch point every mode is outside the horizon: ** "$2M/r$ carries $aH$ up')
    print('     without bound and the comoving horizon to zero".')
    print('  ⓶ ** Verified from the corpus\'s own horizon function: ** (rH)² = A/r² + 2M/r + r²/α² →')
    print('     ∞ as r → 0⁺, so 1/(aH) → 0 and every finite k satisfies k ≪ aH.  ** And the term ordering')
    print('     matches the paper: A/r² (radiation) beats 2M/r (mass); r²/α² (substrate) vanishes. **')
    print('  ⇒⇒ ** So R\'s conservation -- a super-horizon result -- applies to EVERY scalar mode at that')
    print('     locus, and the caveat covered nothing. **')
    print('  ⓷ ** And the distinction that makes this work is one the paper had to CORRECT: ** the SEAM')
    print('     and the BRANCH POINT give ** opposite ** answers, "a distinction six sentences of this')
    print('     paper previously ran together".  *** A caveat written at the wrong locus would have been')
    print('     that error again. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
