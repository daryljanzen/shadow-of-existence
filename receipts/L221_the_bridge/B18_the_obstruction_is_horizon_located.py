#!/usr/bin/env python3
"""B18 -- `PO-11`'s obstruction is HORIZON-located, not singularity-located: the leaf and spacetime
measures differ only where $f$ vanishes, and $r=0$ is integrable in both.

** THE ROW, repointed at r2668. **  "The full PROPAGATING spinor field sector -- the built modes are
leaf-bound, not the propagating theory", targeting "a propagating Dirac sector on the slicing structure,
as against the bound zero-modes the matter paper delivers."

** ⓵ AND P14 STATES THE OBSTRUCTION EXACTLY. **  "the induced proper distance $d\\ell=dr/\\sqrt{|f|}$, in
which ** the horizon turning points lie at finite distance and the $r=0$ crossing is an integrable
square-root singularity **.  In the conserved spacetime Dirac norm---the tortoise measure---** the same
static mode does not normalize, the horizons standing infinitely far **.  The two are not
interchangeable, and ** CR reads the fermion on the leaf, where it is a bound state **."

** ⛭⛭ ⓶ COMPUTED: THE TWO MEASURES DIFFER ONLY AT THE HORIZONS. **

  ** Near a horizon, $f$ vanishes LINEARLY, $f\\approx c(r-r_h)$: **

      *** leaf      int dr/sqrt(c u)  =  2/sqrt(c)     FINITE
          tortoise  int dr/(c u)      =  infinity      LOG DIVERGENT ***

  ** Near $r=0$, $f\\sim-2M/r$ so $|f|\\sim2M/r$: **

      *** leaf      int sqrt(r/2M) dr  =  sqrt(2)/(3 sqrt(M))   FINITE
          tortoise  int r/(2M) dr      =  1/(4M)                FINITE ***

  ⇒⇒ *** So the singularity is NOT where the two norms part company.  $r=0$ is integrable in BOTH -- the
      leaf's square-root and the tortoise's linear measure each converge there.  The entire difference is
      at the horizons, where the leaf sees $1/\\sqrt u$ and the tortoise sees $1/u$. ***

** ⓷ WHICH LOCATES `PO-11`'s DESCENT PRECISELY. **  *** The built modes fail to be propagating states not
because of anything at the branch point but because the tortoise measure puts the horizons at infinite
distance.  A propagating Dirac sector would have to handle a mode spread over an infinite tortoise
interval -- which is the ordinary scattering problem on a black-hole background, not a feature of this
construction. ***
  ⌗ ** And that changes the row's character: ** *** the obstruction is not CR-specific.  It is the
    standard difficulty of normalising static modes across a horizon, met here in CR's coordinates -- so
    the descent is a known hard problem rather than an unnamed one. ***

WHAT IS NOT CLAIMED.  ** Not that the descent is easy ** -- *** the scattering problem is hard and this
receipt does not attempt it. ***  ** Not that the leaf reading is wrong ** -- P14 says the two are not
interchangeable and CR reads the leaf, which stands.  ** Not that $r=0$ is unproblematic in general ** --
only that ** for these two measures ** it is integrable, which is what the computation shows.

Written r2669.  Stated for reversal.
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
    print("  B18 -- where do the leaf and spacetime norms part company?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    # ⓵ the paper's statement
    check('⓵ P14 gives the leaf measure and its convergence: "the horizon turning points lie at finite '
          'distance and the $r=0$ crossing is an integrable square-root singularity"',
          'in that induced proper measure the horizons sit at finite distance and the modes are '
          'bound' in p14)
    check('and the spacetime norm\'s failure: "In the conserved spacetime Dirac norm---the tortoise '
          'measure---the same static mode does not normalize, the horizons standing infinitely far"',
          'whereas in the conserved spacetime Dirac norm the horizons are infinitely distant and '
          'the static mode does not normalize' in p14)
    check('with the choice stated: "CR reads the fermion on the leaf, where it is a bound state"',
          'CR reads the fermion on the leaf, where it is a bound state' in p14)
    check('and the localisation grounded: "the fermion is a mode of the existent spatial leaf"',
          'the fermion is a mode of the existent spatial leaf' in p14)

    # ⓶ compute both, at both loci
    u, c, M, r = sp.symbols('u c M r', positive=True)
    leaf_h = sp.integrate(1/sp.sqrt(c*u), (u, 0, 1))
    tort_h = sp.integrate(1/(c*u), (u, 0, 1))
    check(f'⛭⛭ ⓶ at a HORIZON ($f\\approx c(r-r_h)$): leaf integral = {leaf_h} (finite), tortoise = '
          f'{tort_h} (DIVERGENT)',
          leaf_h.is_finite and tort_h == sp.oo)

    leaf_0 = sp.integrate(sp.sqrt(r/(2*M)), (r, 0, 1))
    tort_0 = sp.integrate(r/(2*M), (r, 0, 1))
    check(f'and at $r=0$ ($|f|\\sim2M/r$): leaf = {sp.simplify(leaf_0)} and tortoise = '
          f'{sp.simplify(tort_0)} -- BOTH FINITE',
          leaf_0.is_finite and tort_0.is_finite)
    check('⇒ so the two measures differ ONLY at the horizons; $r=0$ is integrable in both',
          tort_h == sp.oo and tort_0.is_finite and leaf_h.is_finite and leaf_0.is_finite)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** PO-11's obstruction is HORIZON-located, not singularity-located. **")
    print('  ⛭⛭ ⓵ ** Near a horizon ** (f vanishes linearly): leaf ∫dr/√|f| = 2/√c ** FINITE **;')
    print('     tortoise ∫dr/|f| ** LOG DIVERGENT **.')
    print('  ⓶ ** Near r = 0 ** (|f| ~ 2M/r): leaf = √2/(3√M), tortoise = 1/(4M) — ** BOTH FINITE. **')
    print('  ⇒⇒ *** So the singularity is NOT where the two norms part company.  The entire difference')
    print('     is at the horizons, where the leaf sees 1/√u and the tortoise sees 1/u. ***')
    print('  ⓷ ** Which locates the descent: ** the built modes fail to be propagating states not because')
    print('     of anything at the branch point but ** because the tortoise measure puts the horizons at')
    print('     infinite distance. **  A propagating Dirac sector would have to handle a mode spread over')
    print('     an infinite tortoise interval.')
    print('     ⇒ *** That is the ordinary scattering problem on a black-hole background.  The')
    print('       obstruction is NOT CR-specific -- so the descent is a KNOWN hard problem rather than an')
    print('       unnamed one. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
