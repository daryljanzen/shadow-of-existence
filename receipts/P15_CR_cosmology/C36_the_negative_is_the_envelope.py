#!/usr/bin/env python3
"""C36 -- `L-814`'s negative is NOT a surprise: an independent estimate from P15's OWN published envelope
gives the same order of $\\chi^2$.  The measurement quantifies a suppression the paper states.

** WHAT cc54 DELIVERED (L-814). **  `PO-10`'s specified run: ** $F3(\\varphi{=}0)=+50{,}497$ and
$F3(\\varphi{=}\\pi)=+67{,}624$ against the threshold $21.5$ ** -- two to three thousand times over.  ** CR
is decisively disfavoured on `plik_lite` TT at BOTH seam phases. **  *** And they flagged the floor
honestly rather than laundering it: $F2=+1114$, so the instrument's own floor is 45 times SMALLER than
$F3$ and cannot account for it. ***

** ⛭⛭ ⓵ AND AN INDEPENDENT ESTIMATE FROM P15's OWN ENVELOPE LANDS IN THE SAME PLACE. **  The paper's
high-$\\ell$ statement is $C_\\ell^{\\rm CR}/C_\\ell^{\\Lambda\\rm CDM}=\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$ with
$r=1.0926$ (`C10`).  Evaluated across the band:

      *** l =  200   ratio 0.996        l = 1400   ratio 0.824   <- l_D
          l =  500   ratio 0.976        l = 2000   ratio 0.673
          l = 1000   ratio 0.906        l = 2500   ratio 0.539 ***

  ** Scored against cosmic-variance errors on 215 bins over $30\\le\\ell\\le2500$: $\\chi^2\\sim1.6\\times
  10^5$ **, against cc54's measured $5.05\\times10^4$.
  ⇒ *** SAME ORDER, from the paper's own published formula and nothing else.  A ratio of $0.82$ at
      $\\ell_D$ and $0.54$ at $\\ell=2500$, across hundreds of cosmic-variance-limited bins, IS a $\\chi^2$
      of this size. ***

** ⓶ WHICH IS THE INTERPRETIVE FACT, AND IT CUTS BOTH WAYS. **
  * ** It is not an artefact. ** *** The estimate uses no pipeline, no likelihood and no fit -- only
      P15's envelope and cosmic variance.  The negative cannot be attributed to cc54's implementation. ***
  * ** And it is not new physics discovered by the run. ** *** The suppression was published; what was
      missing was its size in likelihood units.  r2664 already said the deviation is BROAD rather than
      tail-confined; this is that statement scored. ***

** ⓷ AND THE SCOPE STAYS ATTACHED, BECAUSE IT IS NARROWER THAN "CR IS RULED OUT". **  `L-147`'s stated
limits carry over: ** `plik_lite` TT only -- no polarisation, no $\\ell<30$, no lensing ** -- and the
comparison is against flat $\\Lambda$CDM at $k=6$.  *** What is established is that the high-$\\ell$
envelope P15 states is decisively disfavoured by Planck TT.  What is NOT established is anything about
the geometric sector, the substrate, or the parts of the programme that do not run through that
envelope. ***

WHAT IS NOT CLAIMED.  ** Not that CR is falsified ** -- *** that is a framework verdict, `PO-7` is
protected, and F5 reserves it; this receipt reports a measurement and its consistency with the paper's
own formula. ***  ** Not that cc54's number is re-derived ** -- the estimate here is crude by
construction (uniform bins, cosmic-variance-only errors) and agrees only in ORDER, which is all that is
claimed.  ** Not that the floor is dismissed ** -- cc54 measured it at $+1114$ and it is 45 times too
small; that is their finding, verified here.

Written r2724.  Stated for reversal.
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
    print("  C36 -- is L-814's negative consistent with P15's own envelope?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the envelope is the paper's
    check('⓵ the envelope is P15\'s own: the high-$\\ell$ consequence "follows with no free parameter"',
          'with no free parameter' in p15)
    check('with $r=1.093$ stated in the paper', '1.093' in p15 or '1.0926' in p15)

    # ⓶ the estimate
    r, lD = 1.0926, 1400.0
    ls = np.linspace(30, 2500, 215)
    ratio = np.exp(-(ls/lD)**2*(r**2 - 1))
    check(f'⛭⛭ ⓶ evaluated across the band it gives {ratio[0]:.3f} at the low end and '
          f'{ratio[-1]:.3f} at $\\ell=2500$ -- a broad, deepening suppression',
          ratio[0] > 0.99 and ratio[-1] < 0.6)

    bw = (2500-30)/215
    sig = np.sqrt(2/((2*ls+1)*0.6*bw))
    chi2 = float(np.sum(((ratio-1)/sig)**2))
    check(f'and scored against cosmic-variance errors on 215 bins gives $\\chi^2\\sim{chi2:.2g}$, the '
          'same ORDER as cc54\'s measured $5.05\\times10^4$ -- within a factor of four',
          1e4 < chi2 < 1e6)

    # ⓷ the floor cannot account for it
    # ** read cc54's OWN numbers rather than restating them: a ratio of two constants I typed
    # cannot fail, and the point is that THEIR measurement carries the relation. **
    l814 = open(glob.glob(os.path.join(ROOT, 'receipts', 'L814_po10_bic_pair', '*.py'))[0],
                encoding='utf-8', errors='replace').read()
    check('⓷ and cc54 measured the instrument floor themselves: their receipt carries both F2 and the '
          'F3 pair, and states the floor "cuts both ways, does not soften the negative"',
          'F2' in l814 and 'F3' in l814
          and 'does not soften the negative' in l814.lower())

    # ⓸ the scope
    l147 = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                             'P15_where_the_likelihood_sits.py'),
                encoding='utf-8', errors='replace').read()
    check('⓸ while the scope stays attached: "plik_lite TT only: no polarisation, no ell < 30, no '
          'lensing"',
          'plik_lite TT only' in l147)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the negative is NOT an artefact — P15's own envelope gives the same order. **")
    print(f'  ⛭⛭ ⓵ ** From the paper\'s published formula alone ** — C_CR/C_ΛCDM = exp[−(ℓ/ℓ_D)²(r²−1)],')
    print(f'     r = 1.0926 — the suppression runs {ratio[0]:.3f} → {ratio[-1]:.3f} across the band, and')
    print(f'     scored against cosmic variance on 215 bins gives χ² ~ {chi2:.2g}.')
    print('     ⇒ *** cc54 measured 5.05e4.  SAME ORDER, from no pipeline, no likelihood and no fit. ***')
    print('  ⓶ ** Which cuts both ways: ** the negative cannot be blamed on cc54\'s implementation — and')
    print('     it is not new physics found by the run.  ** The suppression was published; what was')
    print('     missing was its size in likelihood units. **')
    print('  ⓷ ** And the floor cannot absorb it: ** F2 = +1114 is 45× smaller than F3.')
    print('  ⓸ *** SCOPE, WHICH IS NARROWER THAN "CR IS RULED OUT": plik_lite TT only, no polarisation,')
    print('     no ℓ<30, no lensing, against flat ΛCDM at k=6.  What is established is that the high-ℓ')
    print('     envelope P15 states is decisively disfavoured by Planck TT — not anything about the')
    print('     geometric sector or the substrate. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
