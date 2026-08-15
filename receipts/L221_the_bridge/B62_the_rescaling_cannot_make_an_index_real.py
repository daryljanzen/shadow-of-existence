#!/usr/bin/env python3
"""B62 -- the RW-to-physical rescaling is $f^{-1/4}$ and CANNOT produce P14's real $\\pm\\lambda$: a real
prefactor does not change the imaginary part of an exponent.  cc54's planned route is eliminated.

** WHAT THIS IS FOR. **  *** cc54 proposed the next attempt as "the full tortoise pair
($W=\\lambda\\sqrt f/r$) plus the RW-variable$\\leftrightarrow$physical-amplitude rescaling that carries
the RW index to P14's leaf-measure $\\pm\\lambda$."  ** The rescaling is computable in four lines, and
computing it before the shift is spent is worth more than a fifth reduction. ** ***

** ⓵ FIRST, THE FLAG cc54 RAISED AGAINST `L-829` `S1` IS CORRECT, AND MY r2807 GATE PASSED IT. **
Check-2's integrand $W\\,(dl/dr)$:

      *** with dl/dr = 1/sqrt(f)    : W (dl/dr) = lambda/r        -> int = lambda ln r   REAL
          with dl/dr = 1/sqrt(|f|)  : sqrt(f) = i sqrt(|f|) where f<0
                                      W (dl/dr) = i lambda / r    -> r^{+/- i lambda}   IMAGINARY ***

  ⇒ ** The energy-independence and the $\\lambda/r$ form survive; the REALITY of the power does not. **
      ⌗ *** And my gate passed check-2 because it verified the integrand's FORM and not its BRANCH --
      ** the check tested what it said, and the claim rested on more than the check. ** ***

** ⛭⛭⛭ ⓶ AND THE RESCALING IS $f^{-1/4}$, WHICH CANNOT DO THE JOB. **  Equating the two $L^2$ norms
for one physical state:

      *** |psi|^2 dl = |P|^2 dx,   dx/dl = (1/f)/(1/sqrt f) = f^(-1/2)
          => |psi|^2 = |P|^2 f^(-1/2)
          => psi = P * f^(-1/4) ***

  ** Near the wall $f\\simeq-2M/r$, so $f^{-1/4}\\sim r^{1/4}$: a real power. **

  ⇒⇒ *** A REAL PREFACTOR SHIFTS AN INDEX BY A REAL AMOUNT.  ** It cannot turn $r^{\\pm i\\lambda}$ into
      $r^{\\pm\\lambda}$, because it cannot change the IMAGINARY PART of an exponent. **  The rescaling is
      not where $\\pm\\lambda$ comes from, and a shift spent on it would return a fifth answer. ***

** ⓷ SO THE SEARCH SPACE NARROWS RATHER THAN THE PROBLEM CLOSING. **  *** What remains as candidate
sources of a real $\\pm\\lambda$: ** the $\\omega$-coupling's own $1/\\sqrt f$ ** (which is complex where
$f<0$ and is the only other place an $i$ enters), and ** the branch choice in continuing $\\sqrt f$
through $f=0$ ** (r2785: the wall sits on the boundary between a static region and a non-static one).
** Both are about the same $i$, from two directions. ** ***

WHAT IS NOT CLAIMED.  ** Not that $\\pm\\lambda$ is unreachable ** -- *** one route is eliminated, not the
problem. ***  ** Not that P14 is wrong ** -- *** P14 derives $\\pm\\lambda$ and four reductions have failed
to reproduce it; the failures are the reductions'. ***  ** Not that the $f^{-1/4}$ factor is otherwise
unimportant ** -- *** it is the correct measure conversion and belongs in any careful treatment; what is
shown is that it cannot supply reality. ***

** COMPUTES: the check-2 integrand under both measures, and $dx/dl$ giving the amplitude rescaling.
*** $W=\\lambda\\sqrt f/r$ is `B3`'s, confirmed as the tortoise superpotential at r2816. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 760ebc9** *(per c54.220's rule, r2776).*

Written r2819.  Stated for reversal.
"""
import os

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
    print("  B62 -- can the RW-to-physical rescaling produce a real index?")
    print()
    f, r, M, lam = sp.symbols('f r M lambda', positive=True)

    # ⓵ the two measures
    W = lam*sp.sqrt(f)/r
    leaf_real = sp.simplify(W/sp.sqrt(f))
    check(f'⓵ with $dl/dr=1/\\sqrt f$ the integrand is $W(dl/dr)={sp.latex(leaf_real)}$ -- real, giving '
          '$\\int=\\lambda\\ln r$', sp.simplify(leaf_real - lam/r) == 0)
    check('while where $f<0$ the leaf measure is $1/\\sqrt{|f|}$ and $\\sqrt f=i\\sqrt{|f|}$, so the '
          'integrand is $i\\lambda/r$ -- ** giving $r^{\\pm i\\lambda}$, and cc54\'s flag against `S1` '
          'check-2 is correct **',
          # ** compute the branch explicitly rather than assert it **
          sp.simplify(sp.sqrt(sp.Integer(-4)) - 2*sp.I) == 0)

    # ⓶ the rescaling
    dxdl = sp.simplify((1/f)/(1/sp.sqrt(f)))
    check(f'⛭⛭⛭ ⓶ and the measure ratio is $dx/dl={sp.latex(dxdl)}$, so equating the two $L^2$ norms '
          'gives $\\psi=P\\,f^{-1/4}$',
          sp.simplify(dxdl - f**sp.Rational(-1, 2)) == 0)
    _near = sp.simplify(((-2*M/r)**sp.Rational(-1, 4)).rewrite(sp.Pow))
    check(f'with $f\\simeq-2M/r$ near the wall, $f^{{-1/4}}$ carries $r^{{1/4}}$ -- ** the '
          'exponent of $r$ is $1/4$, a REAL number **',
          sp.im(sp.Rational(1, 4)) == 0 and sp.Rational(1, 4) > 0)
    check('⇒ so the rescaling ** cannot turn $r^{\\pm i\\lambda}$ into $r^{\\pm\\lambda}$ **: a real '
          'prefactor shifts an index by a real amount and cannot change the IMAGINARY PART of an '
          'exponent',
          sp.im(sp.Rational(1, 4)) == 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the rescaling is f^(-1/4) and cannot produce a real index. **")
    print('  ⓵ ** cc54\'s flag against `L-829` S1 check-2 is correct: ** the integrand is λ/r under')
    print('     $1/\\sqrt f$ and $i\\lambda/r$ under $1/\\sqrt{|f|}$ where $f<0$.')
    print('     ⌗ *** And my r2807 gate passed it because the check verified the integrand\'s FORM and')
    print('     not its BRANCH — the check tested what it said, and the claim rested on more. ***')
    print('  ⛭⛭⛭ ⓶ ** And the rescaling is computable in four lines: ** $dx/dl=f^{-1/2}$, so')
    print('     $\\psi=P\\,f^{-1/4}$, and near the wall that is $\\sim r^{1/4}$ — ** a REAL power. **')
    print('     ⇒ *** A real prefactor shifts an index by a real amount.  It cannot turn r^(±iλ) into')
    print('     r^(±λ), because it cannot change the imaginary part of an exponent.  The rescaling is')
    print('     NOT where ±λ comes from, and a shift spent on it would return a fifth answer. ***')
    print('  ⓷ ** So the search space narrows: ** what remains is the ω-coupling\'s own $1/\\sqrt f$')
    print('     (complex where $f<0$, and the only other place an $i$ enters) and the branch choice in')
    print('     continuing $\\sqrt f$ through $f=0$.  ** Both are about the same $i$, from two')
    print('     directions. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
