#!/usr/bin/env python3
"""E51 -- `PO-9`'s link (e) reproduced on three independent routes: the scale map's rank is 1, and the
one-parameter fibre follows by dimension count.

** WHERE `PO-9` STANDS. **  Its kill receipt's ④ does not clear: "The conclusion rests on ... ** (c) every
rung above the last being maximally symmetric; (d) the plane-section scale-only reduction; (e) the scale
map's rank being 1.  ⛔ (c), (d) and (e) are `L-533`'s own derivation and are reproduced NOWHERE
ELSE. **  `PO-7`'s ④ failed on ONE unreproduced link and cc54 closed it in a revision; ** this fails on
THREE. **"

  ⇒ *** So the discharge is not new physics.  It is a SECOND PATH to each of three steps -- and this
      receipt supplies it for (e), the one that is a pure computation. ***

** ⓵ THE MAP.  ** `L-533`/E50: a plane section of $dS_D$ at offset $c$ is $dS_{D-1}$ of radius
$\\sqrt{\\alpha^2-c^2}$, so the scale map is

      *** alpha_eff = sqrt(alpha_top^2 - c_2^2) :  TWO inputs, ONE output ***

** ⓶ THREE INDEPENDENT ROUTES TO RANK 1. **
  * ** SYMBOLIC (E50's own): ** the Jacobian is the $1\\times2$ row
    $[\\alpha_{\\rm top}/\\sqrt{\\cdot},\\; -c_2/\\sqrt{\\cdot}]$, ** rank 1 **.
  * ** LEVEL SETS: ** for a fixed $\\alpha_{\\rm eff}$, three distinct $(\\alpha_{\\rm top},c_2)$ pairs
    return it exactly.  *** The preimage is a CURVE, not a point -- which is rank deficiency exhibited
    rather than differentiated. ***
  * ** NUMERICAL: ** the Jacobian's rank over 200 random admissible points is ** {1} ** with no
    exceptions.

** ⓷ AND THE FIBRE FOLLOWS BY DIMENSION COUNT, not by a further claim. **  *** domain 2, image 1, rank 1
⇒ fibre dimension $2-1=1$. ***  ** So "the tower has a one-parameter fibre" is arithmetic once the rank is
established, and needs no separate reproduction. **

** ⇒⇒ WHAT THIS DOES AND DOES NOT DO FOR `PO-9`. **  *** (e) now has a second path, and the fibre claim
that rides on it is arithmetic.  (c) and (d) do NOT -- (c) is a statement about every rung of the tower
and (d) is the plane-section reduction itself, and both remain `L-533`'s alone. ***  ** The receipt's ④
still does not clear, and the honest count moves from THREE unreproduced links to TWO. **

WHAT IS NOT CLAIMED.  ** Not that `PO-9` closes ** -- `F5` reserves it and two links stand unreproduced.
** Not that the level-set and numerical routes are fully independent of the symbolic one ** -- *** all
three take the same map as given; what they are independent of is each other's METHOD, not the map's
derivation, and the map's derivation is (d). ***  ** Not that (c) or (d) is easy ** -- neither is
attempted here.

Written r2640.  Stated for reversal.
"""
import os
import re

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  E51 -- reproducing PO-9's link (e) independently")
    print()
    kill = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'kills', 'PO-9.md'),
                                    encoding='utf-8', errors='replace').read())

    # the receipt's own statement of the gap
    check("⓵ PO-9's ④ names the three: \"(c) every rung above the last being maximally symmetric; (d) "
          "the plane-section scale-only reduction; (e) the scale map's rank being 1\"",
          "the scale map's rank being 1" in kill
          and 'the plane-section' in kill)
    check('and says they are reproduced nowhere else',
          'reproduced NOWHERE ELSE' in kill or 'reproduced nowhere else' in kill.lower())

    # ⓶ route 1 -- symbolic
    a, c = sp.symbols('alpha_top c_2', positive=True)
    aeff = sp.sqrt(a**2 - c**2)
    J = sp.Matrix([[sp.diff(aeff, a), sp.diff(aeff, c)]])
    check(f'⓶ SYMBOLIC: the Jacobian of alpha_eff = sqrt(alpha_top^2 - c_2^2) has rank {J.rank()}',
          J.rank() == 1)

    # route 2 -- level sets are curves
    ok = True
    for target in (1.0, 2.0, 3.7):
        pts = [(target*k, float(np.sqrt((target*k)**2 - target**2))) for k in (1.2, 1.6, 2.5)]
        if len({round(p[0], 9) for p in pts}) != 3:
            ok = False
        for at, c2 in pts:
            if abs(np.sqrt(at**2 - c2**2) - target) > 1e-12:
                ok = False
    check('LEVEL SETS: for each of three targets, three DISTINCT (alpha_top, c_2) pairs return it '
          'exactly -- the preimage is a curve, not a point', ok)

    # route 3 -- numerical rank
    rng = np.random.default_rng(0)
    ranks = set()
    for _ in range(200):
        at = rng.uniform(1.5, 9.0)
        c2 = rng.uniform(0.0, at * 0.95)
        d = np.sqrt(at**2 - c2**2)
        ranks.add(int(np.linalg.matrix_rank(np.array([[at/d, -c2/d]]), tol=1e-12)))
    check(f'NUMERICAL: the Jacobian rank over 200 random admissible points is {ranks}', ranks == {1})

    # ⓷ the fibre by dimension count
    check('⓷ and the fibre follows by dimension count: domain 2, image 1, rank 1 => fibre dimension 1',
          2 - J.rank() == 1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** link (e) has a second path.  PO-9's unreproduced count goes THREE -> TWO. **")
    print('  ⓵ ** The map: ** a plane section of dS_D at offset c is dS_(D-1) of radius')
    print('     sqrt(alpha^2 - c^2) -- ** two inputs, one output. **')
    print('  ⓶ ** Three routes to rank 1: ** the symbolic Jacobian; the LEVEL SETS (three distinct pairs')
    print('     per target, so the preimage is a CURVE -- rank deficiency exhibited rather than')
    print('     differentiated); and the numerical rank over 200 random points, ** {1} with no')
    print('     exceptions. **')
    print('  ⓷ ** And the one-parameter fibre is ARITHMETIC once the rank is fixed: ** domain 2, image 1,')
    print('     rank 1 ⇒ fibre dimension 1.  ** No separate reproduction needed. **')
    print('  ⚠ ** (c) and (d) still stand alone. **  ⓸ is a statement about every rung of the tower; ⓹ is')
    print('    the plane-section reduction itself -- ** and all three routes above take that reduction as')
    print('    GIVEN, so they are independent of each other\'s method and not of (d). **')
    print('  ⇒ ** PO-9\'s ④ still does not clear. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
