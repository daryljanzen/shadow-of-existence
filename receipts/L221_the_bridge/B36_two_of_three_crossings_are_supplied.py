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


def _r7283b7():
    """`r7283` ② batch seven: a short EXTENSION of the row's own named function, on demand.

    *`EXTEND` means the function alone does not reach the quantity and a short extension of it
    does.  The extension lives in the computations directory, not here, and this loads it.*"""
    import sys as _s
    _p = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7267_cc66_reach_the_71')
    if _p not in _s.path:
        _s.path.insert(0, _p)
    import extensions as _E
    return _E

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
    #   ⛭ ** AND 61 MADE THE SAME REPAIR INDEPENDENTLY AT `r4125`, from the other side: 60 found
    #   the mismatch by reading, 61 found it by the check going red under its own reach pass. **
    #   *Two lines, one defect, the same diagnosis and the same fix -- which is as good a
    #   confirmation that the label was the correct half as this kind of finding admits.*
    slicing = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'SdS-slicing-curve_v2.tex')))
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the metric
    check('⛭⛭ ⓵ the METRIC crosses: the slicing paper carries the continuation "$C^{\\infty}$ across '
          'the locus the chart labels $r=0$ ... a branch point and not a barrier"',
          'a branch point and not a barrier' in slicing
          and 'across the locus the chart labels' in slicing)
    check('and the framework paper "establishes that closure as a theorem"',
          'establishes that closure as a theorem, of which the circle exhibited here is the $\\Lambda=0' in circle)

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
    _E = _r7283b7()
    check("⛭ `r7283` ② COMPUTED, not cited: `bead_contour`s `M2` is EXACTLY `2/(3 sqrt 3)`, the "
          "Nariai value, so the horizon is a DOUBLE root -- `f` and its first derivative "
          "BOTH vanish there while the second does not. `1/f` therefore has a DOUBLE "
          "pole and the tortoise integral diverges as `1/eps` rather than as "
          "`log(1/eps)`, with `eps*I` converging to `2/f_rr(r_h)` across four decades. "
          "Walked toward a point of the same kind that `f` does not vanish at, the same "
          "predicate comes back FALSE",
          _E.tortoise_diverges(_E.the_horizon())
          and not _E.tortoise_diverges(_E.a_point_that_is_not_a_root())
          and _E.is_at_the_nariai_value()
          and _E.coefficient_matches_the_closed_form())

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
