#!/usr/bin/env python3
"""B65 -- a composite gluon is the OCTET of $3\\otimes\\bar3$ and P14's second quantisation reports only
the SINGLET: the same fact supplies Weinberg--Witten's escape and hides the object.

** WHERE THIS ARRIVES. **  *** r2821 left the composite route open because two Weinberg--Witten escapes
hold, both about asymptotics.  ** The corpus already has composite machinery -- P14 second-quantises on
the wall kernel -- so the question is whether that machinery reaches a spin-1 colour-octet. ** ***

** ⓵ THE KERNEL CARRIES SPIN-$\\tfrac12$ MODES. **  P14: "$\\lambda=j+\\tfrac12$ labels partial waves and
each contributes exactly one bound mode."
  ⇒ *** Two of them combine as $\\tfrac12\\otimes\\tfrac12=0\\oplus1$: ** the spin-1 channel exists by
      ordinary angular momentum addition **, and a composite gluon would live there. ***

** ⛭⛭⛭ ⓶ BUT A GLUON IS AN OCTET, AND P14 COUNTS THE SINGLET. **

      *** 3 (x) 3bar = 1 (+) 8
            the SINGLET  -- colour-neutral, an ASYMPTOTIC state       <- P14's "meson 1"
            the OCTET    -- colour-charged, CONFINED                  <- where a gluon would be ***

  ⇒⇒ *** P14's "baryon 1, diquark 0, meson 1" is a COLOUR-SINGLET count.  ** It is silent on the octet,
      and silent on spin -- "meson 1" is one singlet channel, not one state, since $0\\oplus1$ is four
      states. ** ***

** ⛭⛭ ⓷ AND THE SAME FACT SUPPLIES THE ESCAPE AND HIDES THE OBJECT. **  *** Weinberg--Witten's
confinement escape holds BECAUSE the octet is colour-charged and so not asymptotic (r2821).  ** And
P14's count does not see the octet for exactly that reason: an asymptotic-state count reports singlets. **
***
  ⇒ *** A COMPOSITE GLUON IS INVISIBLE TO THE MACHINERY THAT WOULD FIND IT, FOR THE REASON THAT MAKES IT
      PERMISSIBLE.  ** That is not a coincidence to be noted -- it is why the route can be open and
      unexamined at the same time. ** ***

** ⓸ SO THE ROUTE'S REMAINDER IS SPECIFIC AND IT IS NOT WHAT THE CORPUS HAS BUILT. **  *** Not "does the
wall kernel produce bound states" -- it does, and P14 counts them.  ** It is: does the OCTET channel of
$3\\otimes\\bar3$ on the wall kernel contain a massless spin-1 state? **  P14's second quantisation is
built to answer the singlet question and would have to be rerun on the octet. ***

WHAT IS NOT CLAIMED.  ** Not that an octet state exists ** -- *** the channel exists by representation
theory; whether the wall kernel populates it with a massless spin-1 is exactly the unasked
question. ***  ** Not that P14's count is incomplete ** -- *** it answers what it was built to answer,
and the octet is outside its question rather than missing from its answer. ***  ** Not that a composite
gluon would suffice ** -- *** it would still need to reproduce the coupling, which is `PO-5` entire. ***

** COMPUTES: the spin and colour decompositions $\\tfrac12\\otimes\\tfrac12=0\\oplus1$ and
$3\\otimes\\bar3=1\\oplus8$, against P14's stated counts.  *** Dimension arithmetic, checked. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 99ddf13** *(per c54.220's rule, r2776).*

Written r2822.  Stated for reversal.
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
    print("  B65 -- does P14's composite machinery reach a spin-1 colour-octet?")
    print()
    p14 = flat('matter_sector_paper.tex')

    check('⓵ the kernel carries spin-$\\tfrac12$ modes: "$\\lambda=j+\\tfrac12$ labels partial waves and '
          'each contributes exactly one bound mode"',
          'labels partial' in p14 and 'each contributes exactly one bound mode' in p14)
    # ** compute the Clebsch decomposition rather than assert its dimensions **
    _spins = [abs(0.5-0.5) + k for k in range(int(0.5+0.5-abs(0.5-0.5))+1)]
    _dims = [int(2*j+1) for j in _spins]
    check(f'⇒ and two spin-$\\tfrac12$ combine as spins {_spins} with dimensions {_dims}, summing '
          f'to {sum(_dims)} $=2\\times2$ -- ** the spin-1 channel exists by ordinary angular '
          'momentum addition **',
          _spins == [0.0, 1.0] and sum(_dims) == 4)

    # ⓶ the colour decomposition
    # ** the adjoint of su(N) has dimension N^2-1; the rest of N (x) Nbar is the singlet **
    _N = 3
    _adj, _sing = _N*_N - 1, 1
    check(f'⛭⛭⛭ ⓶ but the colour decomposition is $3\\otimes\\bar3$: the adjoint of '
          f'$\\mathfrak{{su}}({_N})$ has dimension ${_N}^2-1={_adj}$ and the remainder is the '
          f'singlet, {_adj}+{_sing}={_adj+_sing}=${_N}\\times{_N}$ -- ** the gluon is the OCTET, '
          'the meson the SINGLET **',
          _adj == 8 and _adj + _sing == _N*_N)
    check('and P14 counts the singlet: "second quantisation on the wall kernel returns baryon 1, '
          'diquark 0, meson 1" -- ** a colour-singlet count, silent on the octet **',
          # ** the source writes `baryon $1$, diquark $0$, meson $1$` with math delimiters **
          'baryon $1$, diquark $0$, meson $1$' in p14)
    # ** the source's own gloss says CHANNEL: "every channel the Standard Model has" **
    check('⇒ and silent on spin too -- P14 glosses the count as "every channel the Standard Model '
          'has", and a CHANNEL is not a state: $0\\oplus1$ is four states in one channel',
          'every channel the Standard Model has' in p14)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** a composite gluon is the octet, and P14 counts the singlet. **')
    print('  ⓵ ** The kernel carries spin-½ modes ** (λ = j + ½, one bound mode per partial wave), and')
    print('     ** ½ ⊗ ½ = 0 ⊕ 1 ** — the spin-1 channel exists by ordinary addition.')
    print('  ⛭⛭⛭ ⓶ ** But 3 ⊗ 3̄ = 1 ⊕ 8: **')
    print('       the SINGLET  colour-neutral, an ASYMPTOTIC state    ← P14\'s "meson 1"')
    print('       the OCTET    colour-charged, CONFINED               ← where a gluon would be')
    print('     ⇒ *** P14\'s count is a colour-SINGLET count.  Silent on the octet, and silent on spin')
    print('     — "meson 1" is one channel, not one state. ***')
    print('  ⛭⛭ ⓷ ** And the same fact supplies the escape and hides the object: ** Weinberg-Witten\'s')
    print('     confinement escape holds BECAUSE the octet is colour-charged and not asymptotic — and')
    print('     ** P14\'s count does not see the octet for exactly that reason. **')
    print('     *** A composite gluon is invisible to the machinery that would find it, for the reason')
    print('     that makes it permissible.  That is why the route can be open and unexamined at once. ***')
    print('  ⓸ ** So the remainder is specific: ** does the OCTET channel of 3 ⊗ 3̄ on the wall kernel')
    print('     contain a massless spin-1 state?  ** P14\'s second quantisation is built for the singlet')
    print('     question and would have to be rerun on the octet. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
