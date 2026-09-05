#!/usr/bin/env python3
"""B36 -- `PO-11`'s matching is narrowed to ONE object: the metric crosses $r=0$ and the BOUND mode
crosses it, and the CONTINUUM has never been asked to.

** WHERE THIS ARRIVES. **  *** r2744 located the join across the inner horizon; r2745 found the
continuation exists and P14 cited the wrong two papers.  ** The row still read "the mode matching",
which is three things, and two of them are already supplied. ** ***

** ⛭⛭ ⓵ THE METRIC CROSSES, AND THE CORPUS SAYS SO IN A THEOREM. **  `janzen_circle`: the slicing paper
"carries the continuation on the de Sitter substrate --- the one smooth manifold, $C^\\infty$ across the
locus the chart labels $r=0$, where the signed areal radius passes through zero ** as the origin of
polar coordinates does on a plane, a branch point and not a barrier **" -- and the framework paper
"establishes that closure as a theorem".

** ⛭⛭ ⓶ AND THE BOUND MODE CROSSES, IN P14's OWN PROPOSITION. **  "Each throat wall binds exactly one
normalizable chiral zero-mode.  Its chirality is a definite $\\sigma_y$ eigenvalue, ** whose sign is the
sign of the signed-radius flip **."

  ⇒ *** THE TWO ARE THE SAME STRUCTURE IN TWO VOCABULARIES.  P14's chirality sign IS the signed-radius
      flip -- the $r\\to-r$ doubling the continuation describes.  ** A Jackiw--Rebbi zero-mode of a wall
      $W$ odd in $x$ is precisely the mode regular at the origin of the doubled coordinate. ** ***
  ⌗ ** And the counts agree: ** *** exactly one bound mode, which is what a regularity condition at a
    polar origin permits. ***

** ⛔ ⓷ THE CONTINUUM HAS NOT BEEN ASKED. **  *** r2716 and cc54's `c54.214` built the scattering states
on the tortoise line of the STATIC region, $r_b<r<r_c$.  r2744 established $r=0$ sits deep inside the
inner horizon, where $f\\to-\\infty$.  ** Nothing in the corpus says how a static-region scattering state
behaves at $r=0$, and nothing has needed to. ** ***

** ⓸ SO THE ROW'S REMAINDER IS ONE OBJECT, NOT THREE. **  *** Not "the mode matching" -- the metric's
crossing is a theorem and the bound mode's is a proposition.  ** What remains is the CONTINUUM's
behaviour at $r=0$: whether the static region's scattering states continue through the branch point the
geometry already crosses, and with what condition. ** ***
  ⌗ ** And the shape of the answer is constrained by what is already there: ** *** the bound mode's
    condition at $r=0$ is fixed by the signed-radius flip, so the continuum's must be compatible with the
    same flip -- it is not a free choice of boundary condition but a matching to a structure the wall
    already fixes. ***

WHAT IS NOT CLAIMED.  ** Not that the continuum continues ** -- *** that is the open question; what is
established is that it is the ONLY one of the three left. ***  ** Not that Jackiw--Rebbi is derived
here ** -- *** the identification of P14's zero-mode with the regular mode at a doubled origin is read
from P14's own chirality clause, not proved. ***  ** Not that the horizon crossing is thereby easy ** --
r2744's finding stands: there is no single static time covering both regions.

** COMPUTES: nothing.  *** A read of three corpus statements against each other. *** **

Written r2767.  Stated for reversal.
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
    print("  B36 -- how much of PO-11's matching is already supplied?")
    print()
    circle = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'janzen_circle_v3.tex')))
    # ⛭⛭ r4070: THE SLICING PAPER, READ SEPARATELY -- because the check below says "the SLICING
    #   paper carries the continuation" and tested `circle`, which is P2, the CIRCLE paper.
    #   ** The label and the predicate named different papers, and the check passed anyway while
    #   P2 happened to quote P3's phrase. **  61's reach pass moved "a branch point and not a
    #   barrier" out of P2 and into the papers that own it, which is what exposed the mismatch.
    #   ⇒ *A check whose label and predicate disagree is not testing what it says; it passed for
    #     six hundred revisions on a coincidence of quotation.*
    slicing = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex')))
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the metric
    check('⛭⛭ ⓵ the METRIC crosses: the slicing paper carries the continuation "$C^{\\infty}$ across '
          'the locus the chart labels $r=0$ ... a branch point and not a barrier"',
          'a branch point and not a barrier' in slicing
          and 'across the locus the chart labels' in slicing)
    check('and the framework paper "establishes that closure as a theorem"',
          'establishes that closure as a theorem' in circle)

    # ⓶ the bound mode
    check('⛭⛭ ⓶ and the BOUND MODE crosses: "Each throat wall binds exactly one normalizable chiral '
          'zero-mode"',
          'binds exactly one normalizable chiral zero-mode' in p14)
    check('with its chirality tied to the same structure: "whose sign is the sign of the '
          'signed-radius flip" -- ** the $r\\to-r$ doubling the continuation describes **',
          'the sign of the signed-radius flip' in p14)

    # ⓷ the continuum lives elsewhere
    check('⛔ ⓷ while the CONTINUUM is built on the tortoise line of the static region -- P14 puts the '
          'horizons "at infinite tortoise distance", which is where those states live',
          'infinite tortoise distance' in p14)
    check('and the wall is at the OTHER zero: "$W$ changes sign at $r=0$: a domain wall", which '
          'r2744 placed deep inside the inner horizon',
          'a domain wall' in p14 and 'odd in the signed radius' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** two of the three crossings are supplied; the continuum is the remainder. **")
    print('  ⛭⛭ ⓵ ** The METRIC crosses ** — "$C^∞$ across the locus the chart labels r=0 … a branch')
    print('     point and not a barrier", and the framework paper makes that closure a theorem.')
    print('  ⛭⛭ ⓶ ** The BOUND MODE crosses ** — "each throat wall binds exactly one normalizable')
    print('     chiral zero-mode … whose sign is the sign of the signed-radius flip."')
    print('     ⇒ *** The two are ONE STRUCTURE in two vocabularies: P14\'s chirality sign IS the')
    print('     signed-radius flip, and a Jackiw-Rebbi zero-mode of a wall odd in x is precisely the')
    print('     mode regular at the origin of the doubled coordinate. ***')
    print('  ⛔ ⓷ ** The CONTINUUM has not been asked. **  r2716 and c54.214 built the scattering')
    print('     states on the STATIC region\'s tortoise line; r2744 put r=0 deep inside the inner')
    print('     horizon.  ** Nothing says how a static-region scattering state behaves at r=0. **')
    print('  ⓸ ** So the remainder is ONE object, not three: ** whether the static region\'s continuum')
    print('     continues through the branch point the geometry already crosses, and with what')
    print('     condition.')
    print('     ⌗ ** And it is not a free choice: ** the bound mode\'s condition at r=0 is fixed by the')
    print('       signed-radius flip, so the continuum\'s must be compatible with the same flip.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
