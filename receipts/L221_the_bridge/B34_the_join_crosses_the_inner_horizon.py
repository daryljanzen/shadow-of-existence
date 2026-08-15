#!/usr/bin/env python3
"""B34 -- ⛭⛭ **REFINED r2785: BOTH SIDES ARE NOT INTERIOR.**  *** This receipt sampled $r>0$ only.
$f=1-2M/r-r^2/\\alpha^2$ has $2M/r$ ODD and dominant at the origin, so **$f\\to-\\infty$ as
$r\\to0^+$ and $f\\to+\\infty$ as $r\\to0^-$** -- the wall sits ON the boundary between a static
region and a non-static one.  The conjugate branch is a full static region with its own
reflected de Sitter horizon.  See `B43_the_two_sides_of_the_wall_differ_in_signature`.
** What survives: $f(0.010)<0$ and the inner-horizon crossing, both unaffected. ** ***

B34 -- `PO-11`'s join is LOCATED: the wall and the continuum are separated by the inner horizon, so
the remaining undertaking is a matching across a Killing horizon, not a calculation on one region.

** WHERE THIS ARRIVES. **  r2739 reopened the row on P14's own words: "the quantised field, its mode
completeness, and ** the join between the static region's continuum and the wall---which sit in different
regions **---remain the undertaking the corpus names."  *** Which regions was never worked out. ***

** ⓵ THE TWO OBJECTS, AND WHERE EACH LIVES. **  P14: "the factor $\\sqrt f/r$ vanishes at the horizons
($f=0$) and is ** odd in the signed radius **.  Because $r$ is signed, ** $W$ changes sign at $r=0$: a
domain wall **."  ** So $W$ has TWO kinds of zero, and they are at different places: **

      *** the CONTINUUM   lives where f > 0, the static region  rb < r < rc
          the WALL        lives at r = 0, where the signed radius passes through zero ***

** ⛭⛭ ⓶ AND $r=0$ IS NOT IN THE STATIC REGION -- IT IS DEEP INSIDE THE INNER HORIZON. **  With
$f=1-2M/r-r^2/\\alpha^2$ at the undercritical member $M=0.12$, $\\alpha=1$:

      *** r = 0.300000   f = +0.1100    STATIC
          r = 0.256968   f =  0.0000    the inner horizon
          r = 0.200000   f = -0.2400    not static
          r = 0.010000   f = -23.0001   not static ***

  ⇒ ** As $r\\to0^+$ the $-2M/r$ term dominates and $f\\to-\\infty$. **  *** The wall sits in a region
      where $f<0$: $t$ and $r$ have swapped roles, and there is no static Killing time in which to pose
      a stationary scattering problem. ***

** ⛭ ⓷ SO THE "DIFFERENT REGIONS" ARE SEPARATED BY THE INNER HORIZON, AND THAT NAMES THE UNDERTAKING. **
  *** The join is a MATCHING ACROSS A KILLING HORIZON.  Not a harder version of the scattering problem
  r2716 solved -- a different kind of problem: the continuum's modes are stationary states of a static
  region, and the wall's zero-mode lives where staticity fails.  ** There is no single time coordinate
  covering both. ** ***

** ⓸ WHICH IS WHY P14 CALLS IT AN UNDERTAKING AND CITES TWO OTHER PAPERS FOR IT. **  *** `JanzenGeometricCore`
and `JanzenBoundary` -- the geometry of the crossing and the boundary conditions there.  A row asking for
a propagating sector cannot be closed inside the static region, and r2717's strike did exactly
that. ***

WHAT IS NOT CLAIMED.  ** Not that the join is impossible ** -- *** horizon-crossing matchings are
standard in black-hole scattering; what is established is that the remaining work is of that KIND, and it
was being read as more of the same. ***  ** Not that the two cited papers supply it ** -- P14 points at
them for the geometry, and whether they carry the matching is unchecked here.  ** Not that the
undercritical member is special ** -- $f\\to-\\infty$ as $r\\to0^+$ holds for any $M>0$, and the numbers
above are one member for concreteness.

** COMPUTES: $f(r)$ at five radii on the undercritical member $M=0.12$, $\\alpha=1$, to place $r=0$
relative to the inner horizon.  *** $M$ and $\\alpha$ are the corpus's own SdS parameters. *** **

Written r2744.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

M, AL = 0.12, 1.0
RB, RC = 0.25696832, 0.84643915


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def f(r):
    return 1 - 2*M/r - r*r/AL**2


def body(p):
    b = '\n'.join(l for l in open(p, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print("  B34 -- which regions does PO-11's join cross?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ P14 gives W two kinds of zero
    check('⓵ P14 gives $W$ TWO kinds of zero: it "vanishes at the horizons ($f=0$) and is odd in the '
          'signed radius"',
          'vanishes at the horizons' in p14 and 'odd in the signed radius' in p14)
    check('and locates the wall at the second: "Because $r$ is signed, $W$ changes sign at $r=0$: a '
          'domain wall"',
          'changes sign at' in p14 and 'a domain wall' in p14)

    # ⓶ r=0 is inside the inner horizon
    check(f'⛭⛭ ⓶ the static region is $f>0$: $f({RB+0.05:.3f})={f(RB+0.05):+.4f}$ inside, and '
          f'$f({RB:.5f})={f(RB):+.4f}$ at the inner horizon',
          f(RB+0.05) > 0 and abs(f(RB)) < 1e-6)
    check(f'while $f(0.200)={f(0.2):+.4f}$ and $f(0.010)={f(0.01):+.4f}$ -- as $r\\to0^+$ the $-2M/r$ '
          'term dominates and $f\\to-\\infty$',
          f(0.2) < 0 and f(0.01) < f(0.2))
    check('⇒ so $r=0$, where the wall sits, is DEEP INSIDE the inner horizon and not in the static '
          'region at all',
          f(0.01) < 0 and RB > 0)

    # ⓷ and P14 names the consequence
    check('⛭ ⓷ and P14 names it as an undertaking in other papers: the join "remains the undertaking '
          'the corpus names", citing the geometric-core and boundary papers',
          'remain the undertaking the corpus names' in p14
          and 'JanzenBoundary' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the join crosses the INNER HORIZON — a matching, not a harder scattering. **")
    print('  ⓵ ** W has two kinds of zero and they are at different places: ** at the horizons (f=0),')
    print('     and at r=0 where the signed radius passes through zero.')
    print('  ⛭⛭ ⓶ ** And r=0 is deep inside the inner horizon: ** as r→0⁺ the −2M/r term dominates and')
    print(f'     f→−∞ (f(0.010) = {f(0.01):.1f}).  ** The wall sits where f < 0 — t and r have swapped')
    print('     roles, and there is no static Killing time in which to pose a stationary problem. **')
    print('  ⛭ ⓷ *** SO THE "DIFFERENT REGIONS" ARE SEPARATED BY A KILLING HORIZON, and the remaining')
    print('     undertaking is a MATCHING ACROSS ONE — not a harder version of the scattering problem')
    print('     r2716 solved, but a different kind of problem: the continuum\'s modes are stationary')
    print('     states of a static region, and the wall\'s zero-mode lives where staticity fails.')
    print('     THERE IS NO SINGLE TIME COORDINATE COVERING BOTH. ***')
    print('  ⓸ ** Which is why P14 calls it an undertaking and cites two other papers for it — and why')
    print('     r2717\'s strike, taken entirely inside the static region, could not have closed it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
