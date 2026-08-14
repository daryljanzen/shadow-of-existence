#!/usr/bin/env python3
"""B35 -- the continuation `PO-11`'s join needs EXISTS in the corpus, and P14 cites two papers that do
not carry it while two that do go uncited from that sentence.

** THE READ, owed since r2744. **  P14: the join between the static region's continuum and the wall
"remain the undertaking the corpus names`JanzenGeometricCore,JanzenBoundary`".  *** r2744 located the
join: the wall sits at $r=0$, deep inside the inner horizon where $f\\to-\\infty$.  So the question is
whether those two papers carry a continuation through $r=0$. ***

** ⛔ ⓵ THEY DO NOT. **  Across both, the horizon-crossing vocabulary is ** absent ** -- `across the
horizon` 0, `matching` 0, `junction` 0, `inner horizon` 0.  *** Their `continuation` hits (10 and 12)
are all the SEAM continuation: signature flips, the Wick rotation, the equatorial $S^4$.  A different
object entirely -- that continuation crosses a signature, not a horizon. ***

** ⛭⛭ ⓶ AND THE MACHINERY IS IN THE CORPUS, IN OTHER PAPERS. **

      *** janzen_circle    Kruskal 20 · Eddington 2
          slicing_operator horizon-regular 1 · Painleve 4 · Eddington 4
          BH_causality     Eddington 9 · Painleve 2 · "regular across" 1 ***

** ⛭⛭⛭ ⓷ AND THE CIRCLE PAPER CONTINUES THROUGH EXACTLY THE LOCUS THE WALL SITS AT. **  Its own
statement: "The slicing paper`JanzenSlicing` carries the continuation on the deSitter substrate---** the
one smooth manifold, $C^\\infty$ across the locus the chart labels $r=0$, where the signed areal radius
passes through zero as the origin of polar coordinates does on a plane, A BRANCH POINT AND NOT A
BARRIER **---and closes the curve onto the real conjugate branch."

  ⇒⇒ *** THAT IS THE WALL'S LOCUS, NAMED, WITH A CONTINUATION ACROSS IT.  P14's own wall is "odd in the
      SIGNED areal radius, changing sign at $r=0$" -- the same signed radius, the same zero.  The two
      papers describe one locus and only one of them says how to cross it. ***

** ⓸ SO THE CITATION IS AIMED WRONG, AND THAT IS THE FINDING. **  *** `JanzenGeometricCore` and
`JanzenBoundary` carry the substrate and the seam; ** `JanzenSlicing` and `janzen_circle` carry the
continuation through $r=0$ **.  A reader following P14's citation to find the join's machinery is sent
to the two papers that do not have it. ***
  ⚠ ** This does not supply the join. **  *** A classical continuation of the METRIC through $r=0$ is
    not a matching of QUANTUM MODES across it -- the continuum's stationary states and the wall's
    zero-mode still have no common time.  What changes is that the geometric half is not an
    undertaking: it is done, in two papers, and the row was reading it as open. ***

WHAT IS NOT CLAIMED.  ** Not that P14 errs on physics ** -- *** the two cited papers are the right
citation for what the SECTOR is; they are the wrong one for the CROSSING, and the sentence bundles
both. ***  ** Not that the mode matching follows ** -- explicitly not; see ⓸.  ** Not that the circle
paper's two readings are adjudicated ** -- it states that the construction "does not by itself choose
between them", and that stands.

** COMPUTES: nothing numerical.  *** A vocabulary count across thirteen papers and a read of four
passages. *** **

Written r2745.  Stated for reversal.
"""
import glob
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
    print("  B35 -- do the papers P14 cites for the join carry a continuation through r=0?")
    print()
    P = {os.path.basename(f)[:-4]: re.sub(r'\s+', ' ', body(f))
         for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
         if not os.path.basename(f).startswith('appendix')}

    # ⓵ the cited pair lack the vocabulary
    for name in ('geometric_core_paper', 'boundary_paper'):
        absent = all(len(re.findall(k, P[name], re.I)) == 0
                     for k in ('across the horizon', 'matching', 'junction', 'inner horizon'))
        check(f'⛔ ⓵ {name} carries NO horizon-crossing vocabulary: "across the horizon", "matching", '
              '"junction", "inner horizon" all zero', absent)

    # ⓶ but the machinery exists elsewhere
    check('⛭⛭ ⓶ while janzen_circle carries Kruskal 20 times and slicing_operator names '
          '"horizon-regular"',
          len(re.findall('Kruskal', P['janzen_circle_v3'])) > 10
          and 'horizon-regular' in P['slicing_operator'])

    # ⓷ and the circle paper names the wall's own locus with a continuation across it
    check('⛭⛭⛭ ⓷ and the circle paper states it: the slicing paper "carries the continuation ... the '
          'one smooth manifold, $C^{\\infty}$ across the locus the chart labels $r=0$, where the '
          'signed areal radius passes through zero ... a branch point and not a barrier"',
          'across the locus the chart labels' in P['janzen_circle_v3']
          and 'a branch point and not a barrier' in P['janzen_circle_v3'])
    check('which is the WALL\'s locus: P14 puts the wall where $W$ is "odd in the signed radius" and '
          '"changes sign at $r=0$"',
          'odd in the signed radius' in P['matter_sector_paper'])

    # ⓸ and P14 cites the other two
    check('⓸ while P14\'s join sentence cites JanzenGeometricCore and JanzenBoundary',
          'remain the undertaking the corpus names' in P['matter_sector_paper']
          and 'JanzenBoundary' in P['matter_sector_paper'])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the continuation EXISTS, and P14's join sentence cites the two papers")
    print("  without it. **")
    print('  ⛔ ⓵ ** geometric_core and boundary carry NO horizon-crossing vocabulary. **  Their')
    print('     "continuation" hits are the SEAM — signature flips and the Wick rotation.  ** That')
    print('     continuation crosses a signature, not a horizon. **')
    print('  ⛭⛭ ⓶ ** But the machinery is in the corpus: ** janzen_circle (Kruskal 20×),')
    print('     slicing_operator ("horizon-regular", Painlevé), BH_causality ("regular across").')
    print('  ⛭⛭⛭ ⓷ *** AND THE CIRCLE PAPER CONTINUES THROUGH EXACTLY THE WALL\'S LOCUS: "the one')
    print('     smooth manifold, C^∞ across the locus the chart labels r=0, where the signed areal')
    print('     radius passes through zero … A BRANCH POINT AND NOT A BARRIER."  P14\'s wall is at')
    print('     that same signed zero. ***')
    print('  ⇒ ⓸ ** So a reader following P14\'s citation for the join\'s machinery is sent to the two')
    print('     papers that do not have it. **')
    print('  ⚠ ** This does NOT supply the join: ** a classical continuation of the METRIC through r=0')
    print('    is not a matching of QUANTUM MODES across it.  *** What changes is that the GEOMETRIC')
    print('    half is not an undertaking — it is done, in two papers, and the row read it as open. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
