#!/usr/bin/env python3
"""B47 -- the wall is EXACTLY CRITICAL: $V\\to-1/(4r_*^2)$, the indicial equation has a DOUBLE ROOT at
$s=1/2$, and the two solutions are $\\sqrt{x}$ and $\\sqrt{x}\\log x$.

** THE CALCULATION r2796 NAMED. **  *** Expand the radial equation about $r=0$ and read the two
Frobenius indices.  ** The answer is that there are not two -- they coincide. ** ***

** ⛭⛭ ⓵ THE POTENTIAL IS $-4M^2/r^4$ AT THE WALL. **  With $V=f(\\ell(\\ell+1)/r^2+f'/r)$ and
$f=1-2M/r-r^2/\\alpha^2$:

      *** V r^4 -> -4M^2   as r -> 0 ***

  ** Independent of $\\ell$ and of $\\alpha$ ** -- *** the angular term and the cosmological term are both
  subleading against $f'/r$ when $f$ diverges. ***

** ⛭⛭⛭ ⓶ AND IN THE TORTOISE COORDINATE THAT IS EXACTLY $-1/(4x^2)$. **  r2796 gave $dr_*/dr\\simeq
-r/2M$, so $x\\equiv r_*\\simeq-r^2/4M$ and $r\\simeq2\\sqrt{M|x|}$:

      *** V ~ -4M^2 / (2 sqrt(M|x|))^4  =  -1/(4 x^2) ***

  ⇒ *** $M$ DROPS OUT TOO.  ** The wall's inverse-square coefficient is $-1/4$ for every mass, every
      $\\ell$, every $\\alpha$ -- it is a property of the signed-radius geometry and not of a
      parameter. ** ***

** ⛭ ⓷ AND $-1/4$ IS THE CRITICAL COEFFICIENT, SO THE INDICES COINCIDE. **  For $\\psi\\sim x^s$ the
indicial equation is $s(s-1)+1/4=0$, i.e. $s^2-s+1/4=(s-\\tfrac12)^2=0$:

      *** a DOUBLE ROOT at s = 1/2 ***

  ⇒⇒ *** THE TWO SOLUTIONS ARE $\\sqrt{x}$ AND $\\sqrt{x}\\log x$ -- ** a power and a LOGARITHM, not two
      powers **.  That is the degenerate case of the inverse-square problem, and it is the case the
      geometry lands on exactly. ***

** ⓸ WHICH IS WHY THE ROW HAS A CONDITION TO IMPOSE AND NOT A CHOICE OF EXPONENT. **  *** With distinct
indices one selects a solution by its power.  ** With a double root both solutions vanish like
$\\sqrt{x}$ and are distinguished only by the $\\log$ ** -- so the matching condition at the wall is a
statement about the logarithm's coefficient, which is exactly the one-parameter freedom a
self-adjoint-extension choice fixes. ***
  ⌗ ** And the corpus already works this structure one level up: ** *** P10's scale-factor Hamiltonian
    "carries an inverse-square term $\\sim/x^2$ at the origin whose coefficient ... attain[s] $\\le1/4$
    across the natural ordering family, strictly below the essential-self-adjointness threshold $3/4$".
    ** Same operator class, same origin, same critical arithmetic. ** ***

WHAT IS NOT CLAIMED.  ** Not that the extension is selected ** -- *** which multiple of $\\sqrt x\\log x$
the physical continuum carries is the row's remaining content, and this receipt supplies the form, not
the choice. ***  ** Not that P10's $1/4$ and this $-1/4$ are the same number ** -- *** P10's is a
coefficient in a different operator with a different sign convention; what is claimed is the same
STRUCTURE (an inverse-square term at an origin, at its critical value), not an identity of
coefficients. ***  ** Not that subleading terms are harmless ** -- *** only the indicial equation is
computed; corrections shift the series, not the indices. ***

** COMPUTES: $\\lim_{r\\to0}Vr^4$ symbolically, the tortoise substitution, and the indicial roots.
*** $f$ and $V$ are the corpus's own. *** **

Written r2797.  Stated for reversal.
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
    print("  B47 -- what are the Frobenius indices at the wall?")
    print()
    r, M, a, l, x, s = sp.symbols('r M alpha l x s', positive=True)
    f = 1 - 2*M/r - r**2/a**2
    V = sp.simplify(f*(l*(l+1)/r**2 + sp.diff(f, r)/r))

    lead = sp.simplify(sp.limit(V*r**4, r, 0))
    check(f'⛭⛭ ⓵ the potential is $V\\to{sp.latex(lead)}/r^4$ at the wall -- ** independent of $\\ell$ '
          'and of $\\alpha$ **',
          sp.simplify(lead + 4*M**2) == 0)

    # ⓶ tortoise: x = -r^2/4M  =>  r = 2 sqrt(M|x|)
    Vx = sp.simplify(lead/(2*sp.sqrt(M*x))**4)
    check(f'⛭⛭⛭ ⓶ and in the tortoise coordinate ($x\\simeq-r^2/4M$, so $r\\simeq2\\sqrt{{M|x|}}$) it '
          f'becomes ${sp.latex(Vx)}$ -- ** $M$ drops out too **',
          sp.simplify(Vx + sp.Rational(1, 4)/x**2) == 0)

    # ⓷ the indicial equation
    roots = sp.roots(sp.Poly(s*(s-1) + sp.Rational(1, 4), s))
    check(f'⛭ ⓷ so the indicial equation $s(s-1)+1/4=0$ has roots {dict(roots)} -- '
          '** a DOUBLE root at $s=1/2$, the indices COINCIDE **',
          roots == {sp.Rational(1, 2): 2})
    check('⇒ and the two solutions are $\\sqrt{x}$ and $\\sqrt{x}\\log x$ -- ** a power and a LOGARITHM, '
          'not two powers **',
          len(roots) == 1)

    # ⓸ P10 works the same structure
    p10 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'canonical_time.tex')))
    check('⓸ while P10 works the same operator class one level up: its scale-factor Hamiltonian '
          '"carries an inverse-square term" at the origin, with a coefficient read against the '
          'essential-self-adjointness threshold',
          'inverse-square' in p10 and 'essential-self-adjointness threshold' in p10)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the wall is EXACTLY CRITICAL — a double root at s = 1/2. **')
    print(f'  ⛭⛭ ⓵ ** V → −4M²/r⁴ at the wall ** — independent of ℓ and of α, since the angular and')
    print('     cosmological terms are subleading against f\'/r when f diverges.')
    print('  ⛭⛭⛭ ⓶ ** And in the tortoise coordinate that is exactly −1/(4x²) — M drops out too. **')
    print('     *** The wall\'s inverse-square coefficient is −1/4 for every mass, every ℓ, every α:')
    print('     a property of the signed-radius geometry, not of a parameter. ***')
    print('  ⛭ ⓷ ** And −1/4 is the CRITICAL coefficient: ** s(s−1)+1/4 = (s−½)² = 0.')
    print('     ⇒ *** A double root.  The two solutions are √x and √x·log x — a power and a')
    print('     LOGARITHM, not two powers. ***')
    print('  ⓸ ** Which is why the row has a CONDITION to impose, not a choice of exponent: ** both')
    print('     solutions vanish like √x and are distinguished only by the log, ** so the matching')
    print('     condition is a statement about the logarithm\'s coefficient ** — the one-parameter')
    print('     freedom a self-adjoint extension fixes.')
    print('     ⌗ P10 works the same operator class one level up, at the same origin.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
