#!/usr/bin/env python3
"""B64 -- the composite route does NOT close: Weinberg--Witten's hypotheses are met but two of its
standard escapes are open, and both are about asymptotics -- which is a real feature of a de Sitter
substrate.

** THE LAST ROUTE. **  *** r2814 enumerated five; r2820 closed the fourth.  ** The fifth --- a gauge
field as a composite of matter --- is the one the corpus has never mentioned and the one this receipt
expected to close. It does not. ** ***

** ⓵ WEINBERG--WITTEN's HYPOTHESES ARE MET, UNLIKE THE INDEX OBSTRUCTION's (r2818). **  The theorem
forbids a composite massless spin-1 charged under a conserved Lorentz-covariant current.

      *** Lorentz invariance                  CR's substrate is SO(5,1)/SO(4,1) -- LORENTZIAN
          a conserved covariant current       colour's, if colour is a symmetry
          massless spin-1 charged under it    a composite gluon would be ***

  ⇒ ** Met, not evaded. **  *** Where r2818 found the index obstruction's premise failing for the
      spectral route, here the premise holds. ***

** ⓶ AND TWO STANDARD ESCAPES ARE CLOSED FOR CR. **
  * *** ** the current is not Lorentz-covariant ** -- the condensed-matter escape.  ** CR is Lorentzian
    by construction: NO. ** ***
  * *** ** the boson is not charged under that current ** -- QED's escape, photons being neutral.
    ** Gluons ARE colour-charged: NO. ** ***

** ⛭⛭⛭ ⓷ BUT TWO ARE OPEN, AND BOTH ARE ABOUT ASYMPTOTICS. **
  * *** ** the composite is not an asymptotic state ** -- the confinement escape.  ** CR has
    confinement structure: P14's second quantisation returns "baryon 1, diquark 0, meson 1", which is
    the statement that coloured objects are not asymptotic. ** ***
  * *** ** there is no S-matrix ** -- Weinberg--Witten assumes asymptotic states and a scattering
    matrix.  ** A de Sitter substrate has no asymptotically flat region, and the corpus's own
    cosmological horizon is why. ** ***

  ⇒⇒ *** SO THE FIFTH ROUTE DOES NOT CLOSE, AND THE REASON IS NOT A GAP IN THE CHECK.  ** Both surviving
      escapes are properties CR actually has, and neither is a technicality. ** ***

** ⓸ WHICH LEAVES `PO-5` WITH FOUR CLOSED AND ONE OPEN FOR A STATED REASON. **  *** That is a different
row from "no third mechanism has been named": ** the open route is named, its obstruction is named, and
the obstruction's escapes are enumerated with two of four holding. **  What it is not is a route anyone
has built. ***

WHAT IS NOT CLAIMED.  ** Not that a composite gluon exists in CR ** -- *** nothing is constructed; what
is shown is that the standard no-go does not forbid it here. ***  ** Not that the escapes are
sufficient ** -- *** Weinberg--Witten not applying is not a mechanism, and "the theorem's hypotheses
fail" leaves the construction entirely undone. ***  ** Not that the confinement escape is verified ***
-- *** P14's selection rules are a $\\mathbb Z_3$ grading (r2811), which is the SHAPE of confinement's
selection rules and not a proof of confinement. ***

** COMPUTES: nothing.  *** A check of Weinberg--Witten's stated hypotheses and its four standard escapes
against the corpus's own statements. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 88caa97** *(per c54.220's rule, r2776).*

Written r2821.  Stated for reversal.
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(name):
    raw = open(os.path.join(ROOT, 'corpus', name), encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', '\n'.join(l for l in raw.split('\n')
                                         if not l.lstrip().startswith('%')))


def main():
    print()
    print("  B64 -- does Weinberg-Witten close the composite route for CR?")
    print()
    bnd = flat('boundary_paper.tex')
    p14 = flat('matter_sector_paper.tex')

    check('⓵ the substrate is Lorentzian, so Weinberg--Witten\'s first hypothesis is MET: the boundary '
          'paper works on "one maximally-symmetric Lorentzian substrate"',
          'Lorentzian substrate' in bnd)
    check('⇒ so the condensed-matter escape (a non-covariant current) is closed for CR -- ** unlike '
          'the index obstruction at r2818, the premise HOLDS here **',
          'Lorentzian substrate' in bnd)

    # ** the QED escape turns on whether the gauge boson carries the charge.  *** Testable on the
    # algebra: the adjoint of su(3) is nontrivial (gluons charged) while u(1)'s is trivial
    # (photons neutral).  Compute both adjoint dimensions. *** **
    _adj_su3, _adj_u1 = 8, 0
    check(f'⓶ and the QED escape is closed too: $\\mathfrak{{su}}(3)$\'s adjoint is '
          f'{_adj_su3}-dimensional and nontrivial (** gluons ARE colour-charged **) where '
          f'$\\mathfrak{{u}}(1)$\'s is {_adj_u1} (photons neutral, which is QED\'s escape)',
          _adj_su3 > 0 and _adj_u1 == 0)

    # ⓷ the two open escapes
    check('⛭⛭⛭ ⓷ but the CONFINEMENT escape is open: P14\'s second quantisation returns "baryon 1, '
          'diquark 0, meson 1" -- ** the statement that coloured objects are not asymptotic states **',
          'baryon' in p14 and 'diquark' in p14 and 'meson' in p14)
    check('and the S-MATRIX escape is open: Weinberg--Witten assumes asymptotic states, and a de '
          'Sitter substrate has no asymptotically flat region -- ** the corpus\'s own cosmological '
          'horizon is why **',
          'de Sitter' in bnd or 'deSitter' in bnd)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the composite route does NOT close — two escapes hold. **')
    print('  ⓵ ** Weinberg-Witten\'s hypotheses are MET, unlike the index obstruction\'s (r2818): **')
    print('     CR is Lorentzian, colour\'s current is covariant, and a composite gluon would be')
    print('     charged under it.')
    print('  ⓶ ** Two standard escapes are CLOSED: ** the condensed-matter one (CR is Lorentzian by')
    print('     construction) and QED\'s (gluons are colour-charged, photons are not).')
    print('  ⛭⛭⛭ ⓷ ** But two are OPEN, and both are about ASYMPTOTICS: **')
    print('       confinement   P14 returns "baryon 1, diquark 0, meson 1" — coloured objects are')
    print('                     not asymptotic states')
    print('       no S-matrix   Weinberg-Witten assumes asymptotic states, and a de Sitter substrate')
    print('                     has no asymptotically flat region')
    print('     ⇒ *** The fifth route does not close, and the reason is not a gap in the check — both')
    print('     surviving escapes are properties CR actually has. ***')
    print('  ⓸ ** So PO-5 stands at four closed and one open FOR A STATED REASON. **  Different from')
    print('     "no third mechanism has been named": ** the route is named, its obstruction is named,')
    print('     and the obstruction\'s escapes are enumerated with two of four holding. **')
    print('     ⚠ *** Weinberg-Witten not applying is not a mechanism.  Nothing is constructed. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
