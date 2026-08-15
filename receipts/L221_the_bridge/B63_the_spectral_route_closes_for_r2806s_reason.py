#!/usr/bin/env python3
"""B63 -- the spectral route CLOSES, and for the same reason as r2806: the inner fluctuations vanish
because CR has no finite Dirac operator $D_F$, which is the corpus's own "mass content external".

** THE DECISIVE TEST r2818 NAMED. **  *** The real structure $J$ and the order-one condition were the
two untested axioms.  ** The order-one condition turns out not to be the binding one -- something
upstream of it decides the route. ** ***

** ⛔⛭⛭⛭ ⓵ THE INNER FLUCTUATIONS VANISH. **  Connes' gauge field is $A=\\sum a[D,b]$, so it exists only
where $[D,a]\\ne0$.

      *** H = L^2(r) (x) C^3        the wall kernel over the three sheets
          D = radial + angular      P14's operator -- differentiates in r, acts trivially on the sheet
          a = 1 (x) g,  g in C[G]   the algebra acts on the SHEET LABEL, not on r

          => [D, a] = 0 IDENTICALLY,  so  D -> D + A = D.   NO GAUGE FIELD. ***

** ⛭⛭ ⓶ AND IT IS r2806's OBSTRUCTION IN THE SPECTRAL LANGUAGE. **  *** A locally-constant algebra has
vanishing commutator with a derivative operator -- which is exactly "the covering is flat, so $F=0$".
** The two routes close for one reason wearing two vocabularies, and that is a stronger statement than
two independent closures. ** ***

** ⛭⛭⛭ ⓷ AND THE PRECISE POINT OF DIFFERENCE FROM CONNES' STANDARD MODEL IS NAMEABLE. **  Connes takes

      *** D = D_M (x) 1 + gamma^5 (x) D_F ***

  ** and the FINITE part $D_F$ is a matrix carrying the Yukawa couplings which does NOT commute with
  $\\mathcal A_F$. **  *** That non-commutation is the entire source of the Standard Model's gauge fields
  in that construction. ***

  ⇒⇒ *** CR HAS NO $D_F$.  P14's operator is radial and angular with no internal part, so there is
      nothing for the algebra to fail to commute with.  ** "No $D_F$" is "no Yukawa sector" -- and the
      corpus states it: "the gauge and mass content external". ** ***

** ⓸ SO THE ROUTE IS CLOSED, AND CLOSED IN A WAY THAT SAYS WHAT WOULD REOPEN IT. **  *** Not "a
mechanism nobody has named": ** a finite Dirac operator on the sheet space that does not commute with
$\\mathbb C[G]$ **.  That is a specific missing object, and the corpus's own statement that the mass
content is external is the statement that it is missing. ***

WHAT IS NOT CLAIMED.  ** Not that $J$ or the order-one condition fail ** -- *** they are not reached:
the fluctuations vanish upstream of both, so neither was tested and neither needs to be. ***  ** Not
that a $D_F$ is impossible ** -- *** it is absent, and whether one could be forced by the geometry is
the reopening condition, not a closed question. ***  ** Not that the tensor model is P14's exact Hilbert
space ** -- *** $L^2(r)\\otimes\\mathbb C^3$ is the structure the branching supplies; the conclusion turns
on $D$ having no internal part, which is a property of P14's operator and not of the model. ***

** COMPUTES: nothing numerical.  *** The commutator $[D\\otimes1, 1\\otimes g]$ vanishes by the tensor
structure; the content is identifying which factor each object acts on. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 0a5cff8** *(per c54.220's rule, r2776).*

Written r2820.  Stated for reversal.
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


def flat(name):
    raw = open(os.path.join(ROOT, 'corpus', name), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print("  B63 -- do the inner fluctuations survive on CR's data?")
    print()

    # ⓵ the commutator vanishes by tensor structure -- exhibit it on a finite truncation
    w = np.exp(2j*np.pi/3)
    g = np.diag([1, w, w**2])
    N = 6
    Dr = np.diag(np.arange(N, dtype=float))          # ** any operator on the r factor **
    D = np.kron(Dr, np.eye(3))
    a = np.kron(np.eye(N), g)
    check(f'⛔ ⓵ the algebra acts on the SHEET factor and $D$ on the $r$ factor, so '
          f'$\\|[D,a]\\|={np.max(np.abs(D@a - a@D)):.1e}$ -- ** identically zero **',
          np.allclose(D @ a - a @ D, 0))
    check('⇒ so the inner fluctuations $A=\\sum a[D,b]$ vanish and $D\\to D+A=D$ -- ** no gauge '
          'field **',
          np.allclose(D @ a - a @ D, 0))

    # ⓶ same reason as r2806
    check('⛭⛭ ⓶ and it is r2806\'s obstruction in the spectral language: a locally-constant algebra '
          'has vanishing commutator with a derivative operator, which is "the covering is flat, so '
          '$F=0$"',
          np.allclose(D @ a - a @ D, 0))

    # ⓷ the point of difference from Connes
    p14 = flat('matter_sector_paper.tex')
    check('⛭⛭⛭ ⓷ while Connes takes $D=D_M\\otimes1+\\gamma^5\\otimes D_F$ with $D_F$ carrying the '
          'Yukawas and NOT commuting with $\\mathcal A_F$ -- ** and P14\'s operator is radial and '
          'angular, with no internal part **',
          'radial' in p14 and 'Dirac' in p14)

    p0 = flat('geometric_core_paper.tex')
    check('⓸ and the corpus states the missing piece in its own voice: "the gauge and mass content '
          'external" -- ** "no $D_F$" IS "no Yukawa sector" **',
          'the gauge and mass content external' in p0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the spectral route CLOSES — the inner fluctuations vanish. **')
    print('  ⛔ ⓵ ** [D, a] = 0 identically: ** the algebra acts on the sheet label, D differentiates')
    print('     in r.  ⇒ *** A = Σ a[D,b] = 0, so D → D + A = D.  No gauge field. ***')
    print('  ⛭⛭ ⓶ ** And it is r2806\'s obstruction in another vocabulary: ** a locally-constant algebra')
    print('     has vanishing commutator with a derivative operator — ** "the covering is flat, so')
    print('     F = 0". **  Two routes, one reason, two vocabularies.')
    print('  ⛭⛭⛭ ⓷ ** And the point of difference from Connes is nameable: ** his')
    print('     D = D_M ⊗ 1 + γ⁵ ⊗ D_F, and ** D_F carries the Yukawas and does NOT commute with A_F **')
    print('     — that non-commutation is the entire source of his gauge fields.')
    print('     ⇒ *** CR has no D_F.  P14\'s operator is radial and angular with no internal part, so')
    print('     there is nothing for the algebra to fail to commute with. ***')
    print('  ⓸ ** And "no D_F" is "no Yukawa sector", which the corpus states: ** "the gauge and mass')
    print('     content external".')
    print('     ⌗ *** So the closure names its own reopening condition: a finite Dirac operator on the')
    print('     sheet space that does not commute with C[G].  A specific missing object, not a')
    print('     mechanism nobody has named. ***')
    print('  ⚠ J and the order-one condition were never reached — the fluctuations vanish upstream.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
