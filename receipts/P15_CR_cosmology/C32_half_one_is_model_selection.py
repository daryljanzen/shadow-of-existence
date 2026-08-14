#!/usr/bin/env python3
"""C32 -- `PO-10`'s half ① IS an information-criterion comparison, the corpus names it and never uses it,
and the penalty is computable now: $\\Delta$AIC $=10$, $\\Delta$BIC $=26.9$ in CR's favour before any
$\\chi^2$ is scored.

** WHERE THIS CAME FROM. **  r2708 established that "a parameter refit" is not defined between a
one-parameter arm and a six-parameter one, and stopped at "the row owes a RULE".  *** Daryl named the
rule in one line: that is an AIC/BIC-type comparison.  It is, and the standard machinery answers it. ***

** ⛔ ⓵ AND THE CORPUS NAMES THE TARGET WITHOUT EVER USING THE TOOL. **  P15 lists among its reaches
"** the likelihood-level MODEL SELECTION **: the parameter-free ratio comparison above is joined by the
exact low-multipole cosmic-variance likelihood".  ** But across all seventeen papers and every receipt: **

      *** AIC 0 · BIC 0 · Akaike 0 · Occam 0 · Bayes factor 0  (word-boundary matched) ***

  ⇒ *** The programme has been asking "does the likelihood arbitrate?" while never writing down the
      criterion that arbitrates between models of different size.  `L-147` answered a RATIO question and
      was right to; the SELECTION question needs a penalty term and there is none in the corpus. ***

** ⛭⛭ ⓶ AND THE PENALTY IS ALREADY DETERMINED BY NUMBERS THE CORPUS HAS. **  `L-147`'s banked setup is
** 215 TT bins **; P15 states CR fits on "** the single CMB-calibrated $\\Omega_m\\simeq0.31$ **" while
flat $\\Lambda$CDM analyses carry six:

      *** AIC = chi^2 + 2k          k=1: +2.0        k=6: +12.0     -> Delta AIC = 10.0
          BIC = chi^2 + k ln N      k=1: +5.4        k=6: +32.2     -> Delta BIC = 26.9   (ln 215 = 5.371) ***

  ⇒⇒ *** So CR may score up to $10$ worse in $\\chi^2$ (AIC) or $26.9$ worse (BIC) and still be the
      PREFERRED model.  That is the matched-freedom rule half ① was missing, it is standard rather than
      bespoke, and it can be stated before any refit is run. ***

** ⓷ WHICH CHANGES WHAT THE ROW OWES. **  *** Not "decide how to compare" -- that is decided, and by the
ordinary tool.  What remains is the $\\chi^2$ at CR's best $\\Omega_m$, scored on the same bins, which is a
one-parameter scan against a likelihood that is already wired (`L-147` reproduces CAMB's flat-$\\Lambda$CDM
$\\chi^2=206.4$ over those 215 bins). ***
  ⌗ ** And the row acquires a stated threshold: ** *** CR is preferred on BIC unless its best-fit $\\chi^2$
    exceeds $\\Lambda$CDM's by more than $26.9$. ***

WHAT IS NOT CLAIMED.  ** Not that $k=6$ is the right count for the $\\Lambda$CDM arm ** -- *** it is the
standard six for a flat-$\\Lambda$CDM CMB fit, and if the comparison is run against a different
parametrisation the penalty moves with it; the count must be stated with the result. ***  ** Not that CR's
$k=1$ is settled ** -- P15's three statements support it, but a refit that touches $A_s$ or $n_s$ would
raise it.  ** Not that the $\\chi^2$ is known ** -- it is not, and it is what remains.  ** Not that AIC and
BIC agree in general ** -- here they point the same way, which is worth saying because they often do not.

Written r2709.  Stated for reversal.
"""
import glob
import os
import re

import numpy as np

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
    print("  C32 -- is half ① an information-criterion comparison?")
    print()
    papers = ' '.join(body(f) for f in glob.glob(os.path.join(ROOT, 'corpus', '*.tex'))
                      if not os.path.basename(f).startswith('appendix_receipts'))
    # ** exclude THIS file: it names AIC/BIC throughout, so counting itself would report the
    # absence it exists to establish as already ended.  *** A survey must not be in its own
    # sample -- the same class as r2697's citation-marker blindness, one turn later. ***
    recs = ' '.join(open(f, encoding='utf-8', errors='replace').read()
                    for f in glob.glob(os.path.join(ROOT, 'receipts', '**', '*.py'),
                                       recursive=True)
                    if os.path.abspath(f) != os.path.abspath(__file__))
    both = papers + ' ' + recs

    # ⓵ the corpus names the target
    check('⓵ P15 names the target: "the likelihood-level model selection"',
          'likelihood-level model selection' in re.sub(r'\s+', ' ', papers))
    for term in ('AIC', 'BIC', 'Akaike', 'Occam', 'Bayes factor'):
        check(f'⛔ but "{term}" appears ZERO times across all papers and receipts (word-boundary)',
              len(re.findall(r'\b' + re.escape(term) + r'\b', both)) == 0)

    # ⓶ the penalty
    N = 215
    check(f'⛭⛭ ⓶ and L-147 banks the bin count: "chi^2 = 206.4 over {N} TT bins"',
          f'over {N} TT bins' in recs)
    dAIC = 2*(6 - 1)
    dBIC = (6 - 1)*np.log(N)
    check(f'so $\\Delta$AIC $=2(6-1)={dAIC:.1f}$ and $\\Delta$BIC $=5\\ln{N}={dBIC:.1f}$ in CR\'s favour '
          'before any $\\chi^2$ is scored',
          abs(dAIC - 10.0) < 1e-9 and abs(dBIC - 26.9) < 0.1)

    check('⓷ with CR\'s single parameter stated by P15: "the single CMB-calibrated $\\Omega_{m}"',
          'single CMB-calibrated' in re.sub(r'\s+', ' ', papers))

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** half ① is an information-criterion comparison, and the penalty is computable')
    print('  now. **')
    print('  ⛔ ⓵ ** The corpus NAMES the target and never uses the tool: ** P15 lists "the')
    print('     likelihood-level ** model selection **" among its reaches, while ** AIC, BIC, Akaike,')
    print('     Occam and Bayes factor appear ZERO times ** across all seventeen papers and every')
    print('     receipt.')
    print('     ⇒ *** The programme has asked "does the likelihood arbitrate?" without ever writing the')
    print('       criterion that arbitrates between models of different SIZE. ***')
    print('  ⛭⛭ ⓶ ** And the penalty follows from numbers already banked ** — 215 TT bins, CR at k=1,')
    print('     flat ΛCDM at k=6:')
    print(f'       ΔAIC = 2(6−1) = {dAIC:.1f}          ΔBIC = 5·ln 215 = {dBIC:.1f}')
    print('     ⇒⇒ *** CR may score up to 10 worse in χ² (AIC) or 26.9 worse (BIC) and still be the')
    print('       PREFERRED model.  That is the matched-freedom rule half ① was missing — standard,')
    print('       not bespoke, and statable before any refit runs. ***')
    print('  ⓷ ** So the row no longer owes a RULE.  It owes a NUMBER: ** the χ² at CR\'s best Ω_m on')
    print('     the same bins — a one-parameter scan against a likelihood already wired.')
    print('     ⌗ ** With a stated threshold: CR is preferred on BIC unless its best-fit χ² exceeds')
    print('       ΛCDM\'s by more than 26.9. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
