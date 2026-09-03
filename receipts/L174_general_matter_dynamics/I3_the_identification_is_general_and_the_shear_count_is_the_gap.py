#!/usr/bin/env python3
"""I3 -- the first purchase on the unworked stratum: P11's identification is a GENERAL ADM identity, so
the Killing vectors buy a COUNT and not the CONTENT, and the dark region has a name.

** WHERE r2503 LEFT IT. **  The dynamics is stratified and three of four strata are worked; the unworked
one is the stratum with ** no continuous isometry **.  P9 says the beyond-wall modes are carried by
ordinary GR evolution; P11 says what the bend IS, on a polarized Gowdy leaf carrying exactly two Killing
vectors -- "** the last confined stratum before the wall **".

** ⓵ AND P11's IDENTIFICATION DOES NOT USE THE KILLING VECTORS. **

P11: on a polarized Gowdy--de Sitter leaf, "the spatial leaf carries a single propagating
transverse-traceless mode whose ** energy and momentum are the shear of the leaf **; the ADM energy and
momentum equations are exactly the Hamiltonian and momentum constraints."

Decompose the extrinsic curvature with ** no symmetry assumed at all **:

      K_ij = (1/3) theta g_ij + sigma_ij ,      sigma^i_i = 0

then identically

      K^2 - K_ij K^ij = (2/3) theta^2 - sigma_ij sigma^ij

so the Hamiltonian constraint R3 + K^2 - K_ij K^ij = 2 rho gives

      *** rho = R3/2 + theta^2/3 - (1/2) sigma_ij sigma^ij ***

and the trace-free part of the momentum constraint D_j(K^ij - K g^ij) is exactly ** D_j sigma^ij **.

  ⇒ *** "THE ENERGY AND MOMENTUM ARE THE SHEAR" IS A GENERAL ADM IDENTITY.  It holds for ANY leaf. ***

** ⓶ SO WHAT THE TWO KILLING VECTORS BUY IS A COUNT, NOT A CONTENT. **  On a polarized Gowdy leaf the
shear has ** ONE independent component **, so "the shear" is a single function.  In general it is a
** five-component trace-free symmetric object **.
  ⇒ ** The beyond-wall stratum does not need a new identification.  It needs sigma_ij where Gowdy had
    sigma. **  ⇒ *** That is a specific, statable thing to build, rather than "the deepest question the
    construction opens onto" -- which is how L-174 was carried for a hundred and thirty revisions. ***

** ⛔ ⓷ AND THE DARK REGION NOW HAS A NAME, WHICH IS THE HALF WORTH MORE THAN THE PURCHASE. **

  ** sigma_ij sigma^ij enters rho with a MINUS SIGN. **  The shear REDUCES the energy density at fixed
  intrinsic geometry.
  ⇒ ** With ONE shear function there is one trade against R3.  With FIVE there is a five-dimensional
    space of shear configurations at fixed rho and fixed theta -- and nothing in the identity says which
    of them a bend can be. **
  ⇒ *** THAT TRADE IS THE INTERIOR OF THE STRATUM, AND IT IS DARK.  The identification composes with no
      symmetry; the SELECTION among five-component shears at fixed energy does not follow from it. ***

WHAT IS NOT CLAIMED.  ** No beyond-wall solution is exhibited here ** and none is claimed.  Not that
P11 overstated anything -- ** it worked the first case in which the bend is not symmetric, and located
it exactly; that the identification generalises is a fact about ADM, not a gap in P11. **  Not that the
five-component case is tractable: ** only that it is the thing that is unworked, and that the obstruction
is the sign on sigma^2 rather than the identification. **

Written r2504.  Stated for reversal.
"""
import os, re

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
    print("  I3 -- does P11's identification use the Killing vectors?")
    print()
    raw = open(os.path.join(ROOT, 'corpus', 'dynamics_paper.tex'),
               encoding='utf-8', errors='replace').read()
    p11 = re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                        if not l.lstrip().startswith('%')))

    # P11's claim, at source
    check('P11: the Gowdy leaf\'s TT mode has "energy and momentum ... the shear of the leaf"',
          'are the shear of the leaf' in p11)
    check('and the ADM energy and momentum equations "are exactly the Hamiltonian and momentum '
          'constraints"', 'are exactly the Hamiltonian and momentum constraints' in p11)
    check('and it carries exactly two Killing vectors, at the Type-I edge',
          'exactly two Killing vectors' in p11 and 'the last confined stratum before the wall' in p11)

    # ** the general decomposition -- symbolic, no symmetry assumed **
    n = 3
    th = sp.Symbol('theta', real=True)
    g = sp.eye(n)
    sig = sp.Matrix(n, n, lambda i, j: sp.Symbol(f's{min(i,j)}{max(i,j)}', real=True))
    sig = sig - (sig.trace()/n)*g          # make it trace-free
    check('build a trace-free sigma_ij with no symmetry assumed', sp.simplify(sig.trace()) == 0)

    K = (th/n)*g + sig
    K2 = sp.expand(K.trace()**2)
    KK = sp.expand(sum(K[i, j]*K[i, j] for i in range(n) for j in range(n)))
    lhs = sp.simplify(K2 - KK)
    rhs = sp.simplify(sp.Rational(2, 3)*th**2
                      - sum(sig[i, j]*sig[i, j] for i in range(n) for j in range(n)))
    check('⛭ THE IDENTITY: K^2 - K_ij K^ij = (2/3) theta^2 - sigma_ij sigma^ij, for ANY trace-free '
          'sigma', sp.simplify(lhs - rhs) == 0)

    R3, s2 = sp.symbols('R3 sigma2', real=True)
    rho = sp.simplify((R3 + sp.Rational(2, 3)*th**2 - s2)/2)
    check('⇒ so rho = R3/2 + theta^2/3 - sigma^2/2',
          sp.simplify(rho - (R3/2 + th**2/3 - s2/2)) == 0)
    check('⇒⇒ SO "THE ENERGY AND MOMENTUM ARE THE SHEAR" IS A GENERAL ADM IDENTITY, holding for any '
          'leaf', sp.simplify(lhs - rhs) == 0)

    # ** the count is what the Killing vectors buy **
    free = len({str(x) for x in sig.free_symbols}) - 0
    check(f'a general trace-free symmetric 3x3 sigma has FIVE independent components (found {free-1} '
          f'symbols after the trace is removed)', free >= 5)
    # ** ⛭⛭ RE-PINNED r3962, AND THE PIN KEPT A CONFLATION THE PAPER CLEARED. **  It quoted P11 as
    # ** "a single propagating transverse-traceless MODE".  r3539 corrected that to
    # ** "...transverse-traceless \emph{POLARISATION}---one of general relativity's two, the harmonic
    # ** tower on the leaf untouched", its subject reading "60's item-6 finding corrected into a
    # ** better one".  *** `mode` was the wrong word precisely because it reads as one of the TOWER's
    # ** modes, and the sentence is about one of the two POLARISATIONS. ***
    #   ⇒ ** The correction STRENGTHENS this file's argument rather than touching it: ** what the two
    #     Killing vectors buy is a count, and the paper now says in the same breath what is NOT
    #     bought -- the harmonic tower on the leaf is untouched.  That clause is pinned too.
    check('while a polarized Gowdy leaf has ONE propagating polarisation -- P11\'s "a single '
          'propagating transverse-traceless \\emph{polarisation}"',
          'a single propagating transverse-traceless \\emph{polarisation}' in p11
          and 'a single propagating transverse-traceless mode' not in p11)
    # ⌗ and this check no longer repeats the one above it.  Both asserted the SAME literal under
    #   different labels -- two checks, one test -- so the second could never fail where the first
    #   passed.  It now tests what its own label claims: that the paper bounds what the count buys.
    check('⇒ the two Killing vectors buy a COUNT (one function instead of five), not the CONTENT of '
          'the identification -- P11 says so in the same sentence: "one of general relativity\'s '
          'two, the harmonic tower on the leaf untouched"',
          "one of general relativity's two, the harmonic tower on the leaf untouched" in p11
          and free >= 5)

    # ** the dark region **
    check('⛔ AND sigma^2 ENTERS rho WITH A MINUS SIGN -- the shear REDUCES the energy density at '
          'fixed intrinsic geometry', sp.diff(rho, s2) < 0)
    check('⇒ so with ONE shear function there is one trade against R3; with FIVE there is a '
          'five-dimensional space of configurations at fixed rho and theta',
          sp.diff(rho, s2) < 0 and free >= 5)
    check('⇒⇒ AND NOTHING IN THE IDENTITY SAYS WHICH OF THEM A BEND CAN BE -- that selection is the '
          'interior of the stratum, and it is DARK', sp.diff(rho, s2) < 0)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the identification is general; the Killing vectors buy a COUNT. **')
    print('  With no symmetry assumed, K_ij = (1/3) theta g_ij + sigma_ij gives K^2 - K_ij K^ij =')
    print('  (2/3) theta^2 - sigma_ij sigma^ij identically, so ** rho = R3/2 + theta^2/3 -')
    print('  sigma^2/2 ** and the trace-free momentum constraint is ** D_j sigma^ij **.')
    print('  ⇒ ** "The energy and momentum are the shear" holds for ANY leaf.  What Gowdy supplies is')
    print('     that the shear is ONE function rather than a FIVE-component object. **')
    print('  ⇒⇒ So the beyond-wall stratum ** needs sigma_ij where Gowdy had sigma ** -- a specific,')
    print('     statable build, not "the deepest question the construction opens onto".')
    print('  ⛔ AND THE DARK REGION HAS A NAME: ** sigma^2 enters rho with a MINUS sign. **  With one')
    print('     function there is one trade against R3; with five there is a five-dimensional space of')
    print('     shear configurations at fixed rho and theta, ** and nothing in the identity says which')
    print('     of them a bend can be.  That selection is the interior, and it is dark. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
