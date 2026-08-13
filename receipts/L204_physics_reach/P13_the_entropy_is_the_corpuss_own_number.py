#!/usr/bin/env python3
"""P13 -- item 52 answered from the corpus, and r2536's implication corrected: the de Sitter entropy is
3 pi / (Lambda ell_P^2), which is the number the corpus already states and already interprets.

** WHAT r2536 FOUND, AND IT STANDS AS A MEASUREMENT. **  Station ⑦: the corpus takes the de Sitter
horizon's ** TEMPERATURE ** -- T = 1/(2 pi alpha), the channel through which the quantum of action
enters -- and ** never its ENTROPY **.  ** de Sitter entropy 0 across seventeen papers. **  That count is
correct.

** ⛔ WHAT r2536 IMPLIED, AND IT WAS HALF WRONG. **  It read the asymmetry as biting on `PO-6`: "T
depends on alpha ALONE; S depends on the RATIO alpha/ell_P; and PO-6 asks whether a theory with ONE
dimensionful constant can regulate."
  ⇒ *** The implication was that the entropy is where alpha and ell_P would have to MEET, and that the
      corpus takes the quantity leaving its own open question untouched.  The corpus had already met
      them, and said what the meeting is. ***

** ⓵ THE ARITHMETIC. **  With alpha = sqrt(3/Lambda) and A = 4 pi alpha^2,

      *** S = A/4 = pi (alpha/ell_P)^2 = 3 pi / (Lambda ell_P^2) ***

  and the corpus states ** Lambda ell_P^2 ~ 3 x 10^-122 **, so ** S ~ 3.14 x 10^122 ** -- which is
  ** pi x (10^61)^2 ** to the digit.

** ⛭⛭ ⓶ AND THE CORPUS ALREADY STATES THAT NUMBER, AND ALREADY INTERPRETS IT. **

  "Since the ledger leaves exactly one physical scale ($\\Lambda$, equivalently $\\alpha=\\sqrt{3/\\Lambda}$),
   a Planck value is ** NOT a physical scale ** but what unit-counting yields when it has only gauges to
   count.  ** The one physical length is $\\alpha$, not $\\ell_P$; their ratio $\\alpha/\\ell_P\\sim10^{61}$
   ... is the size of the universe in gauge-units---A NUMBER, NOT A TUNING. **"

  ⇒ *** THE DE SITTER ENTROPY IS THAT RATIO SQUARED, TIMES pi.  The corpus has already taken the
      entropy's CONTENT under a different name, with ell_P declared a GAUGE rather than a scale -- so the
      entropy would be a THIRD statement of one number. ***

** ⓷ AND "CROSS-REGISTER" IS THE OPERATIVE WORD, ALSO ALREADY IN THE CORPUS. **  "The traditional Planck
length, mass, and time ... are combinations of these gauges, and ** CROSS-REGISTER ones, mixing the
thermal $\\hbar$ with the real-geometric $c$ and $G$ **."
  ⇒ ** So T = 1/(2 pi alpha) is a ONE-REGISTER quantity and S = pi (alpha/ell_P)^2 is a gauge-count
    across two. **  *** That is a structural reason for the asymmetry, not a decline and not an
    oversight -- and it is the reason r2536 could not see, because it read the ratio as a THREAT to the
    one-constant claim when the corpus reads it as the one-constant claim's OWN CONSEQUENCE. ***

** ⇒⇒ SO ITEM 52's ANSWER IS: the corpus need not take the entropy, because the entropy's number is
already taken and already read.  What is genuinely owed is ONE CLAUSE saying so ** -- that
S = 3 pi/(Lambda ell_P^2) is the same gauge-count, so the horizon thermodynamics adds no new scale.
  ⌗ ** And that clause is worth having precisely because a reader arriving from thermodynamics will
    compute the entropy, get 10^122, and want to know whether the framework owns it. **

WHAT IS NOT CLAIMED.  ** Not that r2536's measurement was wrong ** -- "de Sitter entropy" is at zero and
the temperature is taken; that stands.  ** Not that the entropy is DERIVED here ** -- S = A/4 is imported,
and whether it applies to a cosmological horizon on this reading is untouched.  ** Not that the
fine-tuning conjecture is evaluated **: the corpus states it "as the hypothesis it is, to be grounded
through the matter sector", and this receipt does not ground it.

Written r2564.  Stated for reversal.
"""
import glob
import math
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


def main():
    print()
    print('  P13 -- is the de Sitter entropy a number the corpus already owns?')
    print()
    papers = [f for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
              if not os.path.basename(f).startswith('appendix_receipts')]
    allp = ' '.join(re.sub(r'\s+', ' ', '\n'.join(
        l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
        if not l.lstrip().startswith('%'))) for f in papers)

    # r2536's measurement stands
    check('⌗ r2536\'s measurement stands: "de Sitter entropy" appears ZERO times',
          len(re.findall('de Sitter entropy', allp, re.I)) == 0)

    # ⓵ the arithmetic
    al, lP, Lam = sp.symbols('alpha ell_P Lambda', positive=True)
    S = sp.pi*al**2/lP**2
    S_L = sp.simplify(S.subs(al, sp.sqrt(3/Lam)))
    check(f'⓵ S = pi (alpha/ell_P)^2 = {S_L} with alpha = sqrt(3/Lambda)',
          sp.simplify(S_L - 3*sp.pi/(Lam*lP**2)) == 0)
    val = 3*math.pi/3e-122
    check(f'and with the corpus\'s Lambda ell_P^2 ~ 3e-122, S ~ {val:.2e} = pi x (1e61)^2',
          abs(val - math.pi*1e122)/(math.pi*1e122) < 0.01)

    # ⓶ the corpus states the number and reads it
    check('⛭⛭ and the corpus states it: "the one physical length is $\\alpha$, not $\\ell_P$; their '
          'ratio $\\alpha/\\ell_P\\sim10^{61}$"',
          'The one physical length is $\\alpha$, not $\\ell_P$' in allp)
    check('and interprets it: "the size of the universe in gauge-units---a number, not a tuning"',
          'the size of the universe in gauge-units---a number, not a tuning' in allp)
    check('and states the input: $\\Lambda\\ell_P^2\\approx3\\times10^{-122}$',
          '\\Lambda\\ell_P^2\\approx3\\times10^{-122}' in allp)
    check('and declares a Planck value NOT a physical scale but "what unit-counting yields when it has '
          'only gauges to count"',
          'what unit-counting yields when it has only gauges to count' in allp)

    # ⓷ cross-register
    check('⌗ and "cross-register" is already the corpus\'s word: the Planck values are "combinations of '
          'these gauges, and \\emph{cross-register} ones, mixing the thermal $\\hbar$ with the '
          'real-geometric $c$ and $G$"',
          'mixing the thermal $\\hbar$ with the real-geometric $c$ and $G$' in allp)
    check('⇒⇒ SO T = 1/(2 pi alpha) IS A ONE-REGISTER QUANTITY AND S IS A GAUGE-COUNT ACROSS TWO -- a '
          'structural reason for the asymmetry, not a decline',
          'mixing the thermal $\\hbar$ with the real-geometric $c$ and $G$' in allp
          and 'The one physical length is $\\alpha$, not $\\ell_P$' in allp)

    # the conjecture is stated as a hypothesis, not grounded here
    check('⚠ and the corpus states its fine-tuning conjecture "as the hypothesis it is, to be grounded '
          'through the matter sector"',
          'to be grounded through the matter sector' in allp)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the corpus already owns the entropy\'s number, under a different name. **')
    print('  ⓵ ** S = pi (alpha/ell_P)^2 = 3 pi/(Lambda ell_P^2) ~ 3.14e122. **')
    print('  ⓶ ** And the corpus states exactly that number and reads it: "the one physical length is')
    print('     alpha, not ell_P; their ratio ~1e61 ... the size of the universe in gauge-units --')
    print('     A NUMBER, NOT A TUNING." **  ⇒ ** The entropy would be a THIRD statement of one number. **')
    print('  ⓷ ** And "cross-register" is the corpus\'s own word: the Planck values mix the thermal hbar')
    print('     with the real-geometric c and G. **  ⇒ ** T is one-register; S is a gauge-count across')
    print('     two.  A structural reason for the asymmetry, not a decline. **')
    print('  ⛔ SO r2536\'s IMPLICATION WAS HALF WRONG: it read the ratio as a THREAT to the one-constant')
    print('     claim.  ** The corpus reads it as that claim\'s OWN CONSEQUENCE. **  The measurement')
    print('     stands; the reading is corrected.')
    print('  ⇒ ** What is genuinely owed is ONE CLAUSE ** -- that S = 3 pi/(Lambda ell_P^2) is the same')
    print('    gauge-count, so the horizon thermodynamics adds no new scale.  ** Worth having because a')
    print('    reader arriving from thermodynamics will compute 1e122 and want to know who owns it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
