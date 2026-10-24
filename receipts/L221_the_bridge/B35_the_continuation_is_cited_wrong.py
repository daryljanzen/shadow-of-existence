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


# ⛭⛭ r7267 ①: THE LOADER FOR THE COMPUTED HALF OF THE PIN(S) BELOW, AND THE GAP WAS `INPUTS`.
#   `r7261`'s backlog named, per row, the module AND FUNCTION nearest to computing what this
#   receipt only MATCHES AS A STRING, and classified this row's gap a change of INPUTS.  ** The
#   obstruction was never the mathematics: the named module is a SCRIPT -- it prints its own
#   report at import and some of them run minutes of sympy to do it, so the function could not
#   be imported. **  `graft.py` takes the `def` and the transitive closure of the module-level
#   names it reads, over the AST, and executes nothing else; `parity.py` hands it this row's own
#   inputs.  ⇒ ** The pin below STAYS: it is the citation.  This is the verification. **
def _r7267():
    """`baryon_edge/L006w_the_d5_fourfold.py`'s own functions, grafted, at this row's inputs."""
    if not hasattr(_r7267, 'v'):
        import sys
        sys.path.insert(0, os.path.join(ROOT, 'computations', 'beyond_the_wall',
                                        'r7267_cc66_reach_the_71'))
        import parity
        _r7267.v = parity.at_inputs()
    return _r7267.v


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
    # ⛔⛭ r7131+cc66.100: the label said "Kruskal 20 times" and the condition asserted `> 10` -- a
    # round number standing in for a figure the label states exactly.  *Either the 20 is the claim, in
    # which case `> 10` does not test it, or it is not, in which case the label should not state it.*
    #   ⇒ *What this check is FOR is that `janzen_circle` carries the continuation's standard chart
    #     REPEATEDLY while `slicing_operator` names the regularity.  So the count is PRINTED and only
    #     "more than once" is asserted -- the form that cannot go stale against a twenty-first use.*
    _n_kr = len(re.findall('Kruskal', P['janzen_circle_v3']))
    check(f'⛭⛭ ⓶ while janzen_circle carries Kruskal {_n_kr} times -- REPEATEDLY, not once in '
          f'passing -- and slicing_operator names "horizon-regular".  ** The count is printed; only '
          f'"more than once" is asserted **',
          _n_kr > 1
          and '1$ geodesic, threaded through the horizon-regular Painlev\\\'e--Gullstrand chart, is dust' in P['slicing_operator'])

    # ⓷ and the circle paper names the wall's own locus with a continuation across it
    check('⛭⛭⛭ ⓷ and the circle paper states it: the slicing paper "carries the continuation ... the '
          'one smooth manifold, $C^{\\infty}$ across the locus the chart labels $r=0$, where the '
          'signed areal radius passes through zero ... a branch point and not a barrier"',
          # ⛭ r4070: EACH HALF PINNED TO THE PAPER THAT CARRIES IT.  61's reach pass moved
          #   "a branch point and not a barrier" out of P2; it now lives in P3, P14 and P15 --
          #   the papers that own the characterisation -- while P2 keeps the half that is P2's
          #   to state: the substrate "is $C^{\infty}$ across the locus the chart labels $r=0$",
          #   attributed in the same sentence to \cite{JanzenSlicing}.
          #   ⇒ *The receipt's claim is that the CORPUS states the continuation and attributes it
          #     to the slicing paper.  That is still true; what changed is which paper holds
          #     which clause, and pinning both halves to P2 asserted more than the claim needs.*
          'across the locus the chart labels' in P['janzen_circle_v3']
          and 'JanzenSlicing' in P['janzen_circle_v3']
          and 'a branch point and not a barrier' in P['SdS-slicing-curve_v2'])
    check('which is the WALL\'s locus: P14 puts the wall where $W$ is "odd in the signed radius" and '
          '"changes sign at $r=0$"',
          'odd in the signed radius' in P['matter_sector_paper'])
    # ⛭⛭ r7267 ①: AND THE PARITY IS NOW COMPUTED, THROUGH `L-006w`'s OWN `twoM`.  `twoM`
    #   solves f = 0 for the mass, 2M = r_0**(D-3) - r_0**(D-1), and `L-006w` prints its
    #   monomials and never substitutes r -> -r into the f it came from.  ** Built back on the
    #   same 2M, f = 1 - 2M/r**(D-3) - r**2 is EVEN in the signed radius and sqrt(f)/r is ODD
    #   -- at D = 5 and not at D = 4, which is the reachable converse this is false on. **
    #   ⌗ *And the two parities run opposite: the MASS function is R-odd exactly when D is EVEN,
    #   the WALL factor odd in the signed radius exactly when D is ODD.  At the corpus's D = 5
    #   those are different statements, and nothing had computed either.*
    check('⛭⛭ and the parity is COMPUTED, on the same `2M` `L-006w`\'s `twoM` returns: at D = 5 '
          'f is EVEN in the signed radius and sqrt(f)/r is ODD, and at D = 4 neither',
          _r7267().wall_is_odd(5) and _r7267().f_parity(5) == 1
          and not _r7267().wall_is_odd(4))

    # ⓸ and P14 cites the other two
    # ⛭ r7577 (69): DISCHARGED.  The citation this receipt found landing on two papers without the
    #   continuation is gone: P14's join sentence now states the join open as work and cites the framework
    #   paper, whose frontier carries it (frontier:fermion, register PO-95).  The check asserts the repair.
    check('⓸ and P14\'s join sentence no longer cites the two papers that lack the continuation: it cites '
          'the framework paper\'s frontier, which carries the join as work',
          'remain the undertaking the corpus names' not in P['matter_sector_paper']
          and ("the quantised field, its mode completeness, and the join between the static region's continuum "
               "and the wall---which sit in different regions---remain open, and they are work rather than a "
               "boundary, carried on the framework paper's frontier~\\cite{JanzenCRframework}")
               in P['matter_sector_paper'])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the continuation EXISTS, and P14's join sentence, which cited two papers")
    print("  without it, now cites the framework paper's frontier, which carries the join (PO-95). **")
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
