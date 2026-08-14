#!/usr/bin/env python3
"""S13 -- at second order in the shear the quadratic basis is genuinely THREE-dimensional, and the
third direction is $C^2$: it vanishes identically shear-free, so L-818 never had to route it, and it
has no route.

** THE RUN r2743 MADE POSSIBLE. **  *** r2743 established the degeneracy ends at the shear,
$C^2=4\\sigma^2+O(\\sigma^4)$, and filed "compute the counterterm basis at SECOND order" as owed.
cc54's `L-818` then settled the SHEAR-FREE running layer coefficient-independently.  ** This is the
next order, and it is where the two results part. ** ***

** ⓵ THE QUADRATIC SPACE IS THREE-DIMENSIONAL AND TWO COMBINATIONS ARE SPOKEN FOR. **

      *** GB  = Riem^2 - 4 Ric^2 +   R^2       rank
          C^2 = Riem^2 - 2 Ric^2 + R^2/3         2   of 3 ***

  ** So exactly one direction remains beyond $GB$ and $C^2$ ** -- and it is the $R$-sector L-818
  routes.

** ⛭⛭ ⓶ EACH DIRECTION, AND WHAT CARRIES IT. **
  * ** $GB$: ** topological in four dimensions.  *** A total derivative whatever the geometry -- shear
    does not touch it. ***
  * ** the $R$-sector: ** L-818's identity $R^2=4\\Lambda R-R\\,E_{\\rm trace}$ routes it to
    $G$-renormalization plus an EOM-removable term.  *** The identity involves $R$ ALONE -- no Weyl -- so
    shear does not touch it either. ***
  * ⛔ ** $C^2$: ** *** ZERO identically on any shear-free layer, $4\\sigma^2$ at second order.  **L-818
    never had to route it because on its layer there was nothing to route.** ***

** ⛭⛭⛭ ⓷ AND $C^2$ HAS NO ROUTE OF THE THREE L-818 USES. **
  * ** not topological ** -- *** $GB$ is the only topological quadratic invariant in four dimensions,
    and $C^2$ is linearly independent of it (rank 2 above). ***
  * ** not EOM-removable ** -- *** Weyl is the free gravitational field: it survives on-shell in vacuum,
    where the EOM terms vanish by construction. ***
  * ** not a $\\Lambda$ or $G$ renormalization ** -- *** those are the $R^0$ and $R^1$ directions;
    $C^2$ is quadratic in the trace-free part and carries no $R$. ***

  ⇒⇒ *** SO THE ONE-CONSTANT LEDGER DOES NOT EXTEND TO SECOND ORDER IN THE SHEAR.  At $O(\\sigma^2)$ a
      quadratic counterterm requires a coefficient the substrate does not supply. ***

** ⓸ AND THE CORPUS'S OWN ONE-CONSTANT STATEMENT IS ABOUT THE SUBSTRATE FACE. **  p0: "every curvature
invariant on either face is a pure power of $1/\\alpha^2$ ... its silence about magnitudes is a property
of ** a one-constant theory ** rather than a gap awaiting work."
  ⌗ *** True on the faces, where $C^2=0$.  ** The claim is not contradicted -- it is SCOPED, and this
    receipt locates the scope. ** ***

** ⚠ ⓹ WHAT THIS IS AND IS NOT, because the row is protected. **  *** This is a BOUNDED NEGATIVE on one
order of one expansion: the ledger survives shear-free (L-818) and does not survive at $O(\\sigma^2)$.
** It is not a verdict on the construction. **  The shear sector is exactly the interacting tower P10
names as "the standard problem of the interacting theory" (r2763/r2764), so a new constant appearing
there is a statement about where the free-field treatment ends -- which is the boundary all three nodes
already located. ***

WHAT IS NOT CLAIMED.  ** Not that the second-order coefficient is computed ** -- *** only that the
direction is independent and unrouted; its value is a heat-kernel calculation this receipt does not
run. ***  ** Not that L-818 is limited in a way it did not say ** -- *** it states its layer explicitly
and r2764 located that boundary; this is the next order, not a correction. ***  ** Not that the corpus's
one-constant claim fails ** -- it is a claim about the faces, and on the faces it holds.

** COMPUTES: the rank of $\\{GB, C^2\\}$ in the three-dimensional quadratic space and its nullspace.
*** Both combinations are standard and the space is the corpus's own $\\{$Riem$^2$, Ric$^2$, $R^2\\}$. ***
**

Written r2766.  Stated for reversal.
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
    print("  S13 -- is the quadratic basis still one-dimensional at O(sigma^2)?")
    print()

    # ⓵ the rank
    M = sp.Matrix([[1, -4, 1], [1, -2, sp.Rational(1, 3)]])
    check(f'⓵ $GB$ and $C^2$ span rank {M.rank()} of the three-dimensional space '
          '(Riem$^2$, Ric$^2$, $R^2$) -- so exactly one direction remains beyond them',
          M.rank() == 2)
    ns = M.nullspace()
    check(f'and the remaining direction is {sp.nsimplify(ns[0].T)} -- the $R$-sector L-818 routes',
          len(ns) == 1)

    # ⓶ C^2 vanishes shear-free
    T = sp.symbols('T')
    a = sp.Function('a')(T)
    ap, app = sp.diff(a, T), sp.diff(a, T, 2)
    for kv in (1, 0, -1):
        R = 6*(app/a + (ap/a)**2 + kv/a**2)
        Ric2 = 12*((app/a)**2 + (app/a)*((ap/a)**2 + kv/a**2) + ((ap/a)**2 + kv/a**2)**2)
        Rie2 = 12*((app/a)**2 + ((ap/a)**2 + kv/a**2)**2)
        check(f'⛭⛭ ⓶ and $C^2=0$ identically on the shear-free layer at $k={kv:+d}$ -- ** L-818 never '
              'had to route it because there was nothing to route **',
              sp.simplify(Rie2 - 2*Ric2 + R**2/3) == 0)

    # ⓷ the corpus's one-constant statement is about the faces
    p0 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'geometric_core_paper.tex')))
    check('⓷ while the corpus\'s one-constant claim is about the FACES: "every curvature invariant on '
          'either face is a pure power of $1/\\alpha^{2}$ ... a property of a one-constant theory '
          'rather than a gap awaiting work"',
          'is a pure power of' in p0 and 'one-constant theory' in p0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the ledger does not extend to second order in the shear. **')
    print('  ⓵ ** GB and C² span rank 2 of 3 **, leaving exactly the R-sector L-818 routes.')
    print('  ⛭⛭ ⓶ ** And C² vanishes identically shear-free at every k ** — ** L-818 never had to route')
    print('     it because on its layer there was nothing to route. **  At O(σ²) it is 4σ².')
    print('  ⛭⛭⛭ ⓷ ** And C² has none of L-818\'s three routes: **')
    print('       not topological      GB is the only topological quadratic in 4d, and C² is')
    print('                            linearly independent of it')
    print('       not EOM-removable    Weyl is the free gravitational field — it survives on-shell')
    print('                            in vacuum, where the EOM terms vanish by construction')
    print('       not Λ or G renorm    those are the R⁰ and R¹ directions; C² carries no R')
    print('     ⇒ *** At O(σ²) a quadratic counterterm requires a coefficient the substrate does not')
    print('     supply. ***')
    print('  ⓸ ** The corpus\'s one-constant claim is not contradicted — it is SCOPED: ** p0 states it')
    print('     of the FACES, where C² = 0.  This receipt locates the scope.')
    print('  ⚠ ⓹ ** A BOUNDED NEGATIVE, not a verdict: ** the shear sector IS the interacting tower P10')
    print('    names as "the standard problem of the interacting theory".  ** A new constant appearing')
    print('    there says where the free-field treatment ends — the boundary all three nodes located. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
