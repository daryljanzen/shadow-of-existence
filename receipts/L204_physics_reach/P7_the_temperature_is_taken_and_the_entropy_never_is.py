#!/usr/bin/env python3
"""P7 -- R-P station ⑦ walked: the corpus takes the de Sitter horizon's TEMPERATURE as the channel
through which the quantum of action enters, and never takes its ENTROPY -- and the entropy is exactly
where alpha and the Planck length meet, which is PO-6's own open question.

** THE STATION. **  R-P's ⑦: "thermodynamics / statistical mechanics --- the Gibbons--Hawking state at
kappa = 1/alpha, BH mechanics".  Optics ✔ at r1857--1863; thermo was the open half.

** ⓵ THE MEASUREMENT. **  Across the seventeen papers: ** temperature 59, surface gravity 30,
Gibbons--Hawking 11, entropy 10, Hartle--Hawking 9, equilibrium 6, Euclidean action 5, area law 3,
Bekenstein--Hawking 2 ** -- and

      *** second law 0 · generalized second law 0 · Smarr 0 · heat capacity 0 ·
          thermodynamic stability 0 · de Sitter entropy 0 ***

** ⓶ BUT THE BLACK-HOLE HALF IS DECLINED, EXPLICITLY AND IN PRINT, AND THE DECLINE IS CORRECT. **  P1:
"the horizon-thermodynamic apparatus, ** area law and entropy alike **, has on a finite layer ** no
realised horizon to be defined on **, exactly as its temperature has none.  The layered ontology thus
reads black-hole thermodynamics as ** the thermodynamics of an idealisation **."  And it scopes its own
non-claim: what survives "for a perpetually collapsing ultra-compact body … ** is not settled by this
reading and is not claimed here **."
  ⇒ ** So the absence of black-hole entropy is a DECLINE, properly scoped.  It covers the COLLAPSE
    horizon, which never completes. **

** ⛭⛭ ⓷ AND THE COSMOLOGICAL HORIZON IS THE OPPOSITE CASE -- AND IT IS LOAD-BEARING. **  P13/P14:
"** The quantum of action enters through the de Sitter horizon's Gibbons--Hawking thermal state, a
Euclidean continuation of period beta = 2 pi alpha **".

  ⇒ *** hbar ENTERS THE FRAMEWORK THROUGH THAT HORIZON'S TEMPERATURE.  It is not incidental. ***  And
    r2527 verified the same number from the metric: kappa = 1/alpha, T = kappa/2pi = 1/(2 pi alpha),
    matching beta = 2 pi alpha exactly.

  ** AND ITS ENTROPY IS NEVER TAKEN. **  Same horizon, same continuation:

      A = 4 pi alpha^2   ⇒   *** S = A/4 = pi alpha^2   (Planck units)
                                 = pi alpha^2 c^3/(G hbar) = pi (alpha/l_P)^2 ***

** ⓸ AND THAT IS WHY IT MATTERS RATHER THAN BEING A TIDINESS POINT. **

      *** T = 1/(2 pi alpha)      -- depends on alpha ALONE
          S = pi (alpha/l_P)^2    -- depends on the RATIO of alpha to the Planck length ***

  And PO-6's dark half asks ** "whether ONE dimensionful constant can regulate" **.
  ⇒ *** SO THE CORPUS TAKES THE THERMODYNAMIC QUANTITY THAT LEAVES ITS OWN OPEN QUESTION UNTOUCHED, AND
      NEVER TAKES THE ONE THAT FORCES IT -- on the same horizon, by the same Euclidean continuation, with
      alpha the sole dimensionful constant it admits. ***
  ⌗ ** The entropy is where alpha and l_P meet, and it is the only place in the corpus's thermodynamics
    where they would have to. **

WHAT IS NOT CLAIMED.  ** Not that the corpus should assert a de Sitter entropy ** -- whether S = A/4
applies to a cosmological horizon on this reading is exactly what would have to be argued, and the
one-constant theorem may well forbid what the entropy would require.  ** Not that the black-hole decline
is wrong ** -- it is correct and properly scoped, and this receipt says so.  ** Not that pi (alpha/l_P)^2
is a prediction ** -- it is the standard formula evaluated, and its status here is precisely what is
unasked.  Not that the second law's absence is a defect: ** with no realised black-hole horizon the
generalized second law reduces to the ordinary one, which is unremarkable -- the cosmological side is
where the question lives. **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT e4e2d75** *(retro-pinned r2802: the commit
that ADDED this receipt is the tree its absence was measured against — **a git lookup, not a
guess**. c54.220's rule, r2776.)*

Written r2536.  Stated for reversal.
"""
import glob
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


def papers():
    return [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
            if not os.path.basename(f).startswith('appendix_receipts')]


def body(f):
    return re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%')))


def main():
    print()
    print('  P7 -- station ⑦: what does the corpus take from the horizon it grants is real?')
    print()
    P = papers()
    allp = ' '.join(body(f) for f in P)
    rp = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'THE_PHYSICS_REACH.md'),
                                  encoding='utf-8', errors='replace').read())
    # ** PO-6's dark half lives in BOARD.md's vein summary, not the register -- located by grep after
    # the first run failed against THE_LIVE_ARC.  Same lesson as r2515's N1. **
    arc = re.sub(r'\s+', ' ', open(os.path.join(ROOT, 'BOARD.md'),
                                   encoding='utf-8', errors='replace').read())

    check('R-P names ⑦ as thermodynamics: "the Gibbons--Hawking state at $\\kappa=1/\\alpha$, BH '
          'mechanics"',
          # ** the R-P row uses an EN-DASH, not '--'.  Matched at source rather than by habit. **
          'thermodynamics / statistical mechanics' in rp
          and 'Gibbons\u2013Hawking state at $\\kappa=1/\\alpha$' in rp)

    # ⓵ the measurement
    have = {k: len(re.findall(re.escape(k), allp, re.I))
            for k in ('temperature', 'Gibbons--Hawking', 'entropy', 'Hartle--Hawking',
                      'area law', 'Bekenstein--Hawking')}
    check(f'the thermodynamic vocabulary is present: temperature {have["temperature"]}, '
          f'Gibbons--Hawking {have["Gibbons--Hawking"]}, entropy {have["entropy"]}, area law '
          f'{have["area law"]}',
          have['temperature'] > 20 and have['Gibbons--Hawking'] > 5 and have['entropy'] > 5)
    for k in ('second law', 'Smarr', 'heat capacity', 'de Sitter entropy'):
        n = len(re.findall(re.escape(k), allp, re.I))
        check(f'⛔ and "{k}" appears ZERO times', n == 0)

    # ⓶ the decline, and it is correct
    check('⌗ but the BLACK-HOLE half is declined in print: "area law and entropy alike, has on a '
          'finite layer no realised horizon to be defined on"',
          'area law and entropy alike, has on a finite layer no realised horizon to be defined on'
          in allp)
    # ** RE-PINNED r3107.  The pinned sentence was removed from P7 at r3059, and what replaced it is
    #    SHARPER, not weaker: the non-claim is now scoped to the subsection that makes it rather than
    #    to "this reading", and the sentence goes on to say what the collapse DOES produce and where
    #    that is established.  So the receipt's thesis -- the temperature is taken and the entropy is
    #    never taken -- is unchanged, and the scoping it pins is stronger.  Pinning the OLD wording
    #    punished the edit that improved it, which is this class's rule. **
    check('and it scopes its own non-claim to the subsection making it: what survives for a '
          'perpetually collapsing ultra-compact body "is not settled by the horizon-thermodynamic '
          'reading of this subsection"',
          'is not settled by the horizon-thermodynamic reading of this subsection' in allp)
    check('and it says where what the collapse DOES produce is established, rather than leaving the '
          'non-claim bare',
          'what the collapse does produce is the subject of the central theorem below' in allp)
    check('⇒ so THAT absence is a properly scoped DECLINE, covering the COLLAPSE horizon',
          'thermodynamics of an idealisation' in allp)

    # ⓷ the cosmological horizon, and it is load-bearing
    check('⛭⛭ AND THE COSMOLOGICAL HORIZON IS THE OPPOSITE CASE, AND LOAD-BEARING: "The quantum of '
          "action enters through the de Sitter horizon's Gibbons--Hawking thermal state, a Euclidean "
          'continuation of period $\\beta=2\\pi\\alpha$"',
          "The quantum of action enters through the de Sitter horizon's Gibbons--Hawking thermal "
          'state' in allp and '\\beta=2\\pi\\alpha' in allp)

    al = sp.Symbol('alpha', positive=True)
    beta = 2*sp.pi*al
    T = 1/beta
    kappa = 1/al
    check(f'and the number matches r2527\'s independent derivation: kappa = 1/alpha gives '
          f'T = kappa/2pi = {sp.simplify(kappa/(2*sp.pi))}, equal to 1/beta',
          sp.simplify(T - kappa/(2*sp.pi)) == 0)

    # ⓸ the entropy, and what each carries
    A = 4*sp.pi*al**2
    S = sp.simplify(A/4)
    check(f'⛭ the same horizon has area A = 4 pi alpha^2, so S = A/4 = {S} in Planck units',
          sp.simplify(S - sp.pi*al**2) == 0)
    G, hbar, c = sp.symbols('G hbar c', positive=True)
    S_full = sp.simplify(A*c**3/(4*G*hbar))
    check(f'restored: S = A c^3/(4 G hbar) = pi (alpha/l_P)^2',
          sp.simplify(S_full - sp.pi*al**2*c**3/(G*hbar)) == 0)
    check('⇒⇒ SO T DEPENDS ON alpha ALONE WHILE S DEPENDS ON THE RATIO alpha/l_P',
          len(T.free_symbols) == 1 and len(S_full.free_symbols) == 4)
    check("and PO-6's dark half asks whether ONE dimensionful constant can regulate",
          'one dimensionful constant' in arc.lower())
    check('⇒ SO THE CORPUS TAKES THE QUANTITY THAT LEAVES ITS OWN OPEN QUESTION UNTOUCHED AND NEVER '
          'TAKES THE ONE THAT FORCES IT',
          len(re.findall('de Sitter entropy', allp, re.I)) == 0
          and 'one dimensionful constant' in arc.lower())

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the corpus takes the temperature and never the entropy, from the same horizon. **')
    print('  ⓵ ** second law 0 · Smarr 0 · heat capacity 0 · de Sitter entropy 0 ** -- against')
    print(f'     temperature {have["temperature"]}, Gibbons--Hawking {have["Gibbons--Hawking"]}, '
          f'entropy {have["entropy"]}.')
    print('  ⓶ ** The BLACK-HOLE half is declined in print and the decline is correct: ** "area law and')
    print('     entropy alike, has on a finite layer no realised horizon to be defined on."')
    print('  ⓷ ** But the de Sitter horizon is the opposite case AND load-bearing: the quantum of action')
    print('     ENTERS through its Gibbons--Hawking state, beta = 2 pi alpha. **')
    print('  ⓸ ** T = 1/(2 pi alpha) depends on alpha ALONE.  S = pi (alpha/l_P)^2 depends on the RATIO.')
    print("     And PO-6 asks whether ONE dimensionful constant can regulate. **")
    print('  ⇒⇒ ** So the corpus takes the thermodynamic quantity that leaves its own open question')
    print('     untouched, and never takes the one that forces it -- same horizon, same continuation. **')
    print('  ⚠ NOT claimed: that a de Sitter entropy SHOULD be asserted.  ** Whether S = A/4 applies on')
    print('    this reading is exactly what would have to be argued, and the one-constant theorem may')
    print('    well forbid what it would require. **  The finding is that it is UNASKED.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
