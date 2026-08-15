#!/usr/bin/env python3
"""B54 -- cc54's retraction of $r^{\\pm i\\lambda}$ is LOAD-BEARING FOR r2800's verdict, not against it:
imaginary indices would have given the extension freedom the verdict denies.

** WHY THIS EXISTS. **  *** cc54 retracted a probe result: "the $r^{\\pm i\\lambda}$ I got is my error,
not a real tension.  P14 derives $|r|^{\\pm\\lambda}$ (real indices)."  ** A retraction on the row whose
verdict this line supplied at r2800 needs checking against that verdict, not filed as someone else's
housekeeping. ** ***

** ⓵ r2800's VERDICT RESTS ON THREE STEPS AND ONLY ONE IS EXPOSED. **
  * *** the field is DIRAC -- read from the row's own object column, ** independent of any index
    value **; ***
  * ** the indices are $\\pm\\lambda$, NON-DEGENERATE ** -- *** this is the exposed step; ***
  * *** a non-degenerate pair has no one-parameter family, so the condition is determined. ***

** ⛭⛭⛭ ⓶ AND THE RETRACTION MOVES THE EXPOSED STEP IN THE DIRECTION THAT SUPPORTS IT. **

      *** REAL      r^{+lambda} decays, r^{-lambda} grows
                    -> normalisability picks one.  NO FREEDOM.

          IMAGINARY r^{+i lambda}, r^{-i lambda} BOTH have modulus 1
                    -> log-periodic oscillation, neither decays
                    -> the LIMIT-CIRCLE case, which HAS a one-parameter family ***

  ⇒⇒ *** IF $r^{\\pm i\\lambda}$ HAD BEEN BANKED, r2800's VERDICT WOULD HAVE BEEN WRONG.  ** Imaginary
      indices give exactly the extension freedom the verdict says the geometry does not leave open. **
      The retraction is load-bearing FOR the verdict. ***

** ⓷ AND P14's $\\lambda$ IS REAL BY ITS OWN DEFINITION. **  *** "$\\lambda=j+\\tfrac12$ labels partial
waves ... each contributes exactly one bound mode."  ** An angular quantum number is real by
construction, so $\\pm\\lambda$ is a real non-degenerate pair for every $j$. ** ***

** ⓸ AND cc54's DIAGNOSIS OF ITS OWN ERROR IS THE USEFUL PART. **  *** "the naive second-order $V_\\pm$
gave index 2, the naive first-order gave imaginary --- neither is the operator whose near-wall indices
are the correct $\\pm\\lambda$."  ** Two wrong operators giving two wrong answers is a stronger statement
than one wrong answer: it locates the gap at the OPERATOR, which is what `#556` now says it needs. ** ***

WHAT IS NOT CLAIMED.  ** Not that the transmission amplitude follows ** -- *** it needs the correct
radial operator carried across the horizon in a regular chart, and that is `#556`. ***  ** Not that
P14's indices are re-derived ** -- *** its $\\lambda=j+\\tfrac12$ is quoted and its reality follows from
being an angular label. ***  ** Not that r2800 needed rescuing ** -- *** it cited the real form; what
this receipt establishes is that the citation was load-bearing and the retracted form would have
overturned it. ***

** COMPUTES: $r^{\\pm\\lambda}$ and $r^{\\pm i\\lambda}$ at three radii, showing decay-versus-growth against
unit-modulus oscillation.  *** $\\lambda$ is P14's angular label. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT 264fb33** *(per c54.220's rule, r2776).*

Written r2808.  Stated for reversal.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

LAM = 1.5


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
    print("  B54 -- does cc54's retraction threaten r2800's verdict?")
    print()
    p14 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex')))

    check('⓵ P14 defines $\\lambda$ as an angular label: "$\\lambda=j+\\tfrac12$ labels partial waves ... '
          'each contributes exactly one bound mode" -- ** real by construction **',
          'labels partial' in p14 and 'each contributes exactly one bound mode' in p14)

    # ⓶ real indices: one decays, one grows
    rs = np.array([0.5, 0.1, 0.01])
    up, dn = rs**LAM, rs**(-LAM)
    check(f'⛭⛭⛭ ⓶ REAL indices separate: $r^{{+\\lambda}}$ decays to {up[-1]:.5f} while '
          f'$r^{{-\\lambda}}$ grows to {dn[-1]:.0f} -- ** normalisability picks one, NO freedom **',
          up[-1] < 0.01 and dn[-1] > 100)

    # and imaginary indices do not
    mods = [abs(np.exp(1j*LAM*np.log(r))) for r in rs]
    check(f'while IMAGINARY indices do not: $|r^{{\\pm i\\lambda}}|$ = {[round(m, 4) for m in mods]} -- '
          '** both unit modulus, log-periodic, neither decays **',
          all(abs(m - 1) < 1e-9 for m in mods))
    check('⇒ so imaginary indices are the LIMIT-CIRCLE case, which HAS a one-parameter family -- '
          '** exactly the freedom r2800 says the geometry does not leave open **',
          all(abs(m - 1) < 1e-9 for m in mods) and up[-1] < dn[-1])

    # ⓷ and the verdict's first step is index-independent
    raw = open(os.path.join(ROOT, 'PROTECTED_OPEN.md'), encoding='utf-8', errors='replace').read()
    row = next(x for x in raw.split('\n') if re.match(r'\|\s*~*\*\*PO-11\*\*', x))
    check('⓷ while r2800\'s first step is index-independent: the field is read as DIRAC from the row\'s '
          'own object column',
          'propagating Dirac sector' in row)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the retraction is load-bearing FOR r2800, not against it. **")
    print('  ⓵ ** P14\'s λ is an angular label — real by construction, ** so ±λ is a real')
    print('     non-degenerate pair for every j.')
    print('  ⛭⛭⛭ ⓶ ** And the two forms behave oppositely: **')
    print(f'       REAL       r^(+λ) → {up[-1]:.5f},  r^(−λ) → {dn[-1]:.0f}   one decays, one grows')
    print(f'       IMAGINARY  |r^(±iλ)| = 1 at every radius     log-periodic, neither decays')
    print('     ⇒ *** Imaginary indices are the LIMIT-CIRCLE case, which HAS a one-parameter family.')
    print('     If r^(±iλ) had been banked, r2800\'s verdict would have been WRONG — imaginary indices')
    print('     give exactly the extension freedom the verdict denies. ***')
    print('  ⓷ ** And the verdict\'s first step is index-independent ** — the field is Dirac by the')
    print('     row\'s object column, whatever the indices turn out to be.')
    print('  ⓸ ** And cc54\'s diagnosis is the useful part: ** "the naive second-order V± gave index 2,')
    print('     the naive first-order gave imaginary — neither is the operator."  ** Two wrong')
    print('     operators giving two wrong answers locates the gap at the OPERATOR **, which is what')
    print('     #556 now says it needs.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
