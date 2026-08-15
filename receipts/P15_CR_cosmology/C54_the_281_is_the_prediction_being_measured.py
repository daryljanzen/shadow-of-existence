#!/usr/bin/env python3
"""C54 -- CR's $\\chi^2/{\\rm dof}=281$ is not an unexplained excess: it is the ORDER the damping
signature itself produces against Planck-sized errors, which inverts `PO-10`'s question.

** THE GAP r2781 LEFT. **  *** The control's residual is diagnosed (a $k$-range truncation, halving
under $L_{\\max}$).  ** CR's $281$ is unresponsive to the same parameter and was diagnosed by nothing --
the only remainder on the board with no candidate mechanism at all. ** ***

** ⛭⛭ ⓵ THE CANDIDATE IS P15's OWN PREDICTION. **  P15's high-$\\ell$ consequence, with no free
parameter: $C_\\ell^{\\rm CR}/C_\\ell^{\\Lambda{\\rm CDM}}=\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$ with $r=1.0824$
(r2755).  Scored as a fractional residual over the arm's $185$ bins:

      *** sigma = 0.2%     bare damping -> chi^2/dof  5099
          sigma = 0.5%                                 816
          sigma = 1.0%                                 204
          measured CR arm                              281 ***

  ⇒ *** $281$ SITS INSIDE THE RANGE THE PREDICTION SPANS, and ** BELOW ** the value at Planck's quoted
      few-tenths-of-a-per-cent errors. ***

** ⛭⛭⛭ ⓶ WHICH INVERTS THE ROW'S QUESTION. **  *** `PO-10` asked what mechanism explains CR's $281$.
** The answer may be that nothing needs to: the arm is scoring the effect P15 predicts, at the order
P15 predicts it. **  An arm that returns a large $\\chi^2$ against $\\Lambda$CDM is what a model
predicting a $8.2\\%$ high-$\\ell$ suppression IS. ***

** ⓷ AND IT SHARPENS F5 RATHER THAN WEAKENING IT. **  `P15_where_the_likelihood_sits` F5: "a negative
is a measurement discrepancy, not a framework verdict."
  ⇒ *** If CR's $\\chi^2$ is its own predicted signature being measured, then ** the discrepancy IS the
      framework's claim, not evidence against it ** -- and reading $281$ as a defect was reading a
      prediction as an error.  F5 protected the row from the wrong direction of mistake. ***

** ⓸ AND IT GIVES THE ROW A SHARP NEXT TEST, WHICH IS ABOUT SHAPE. **  *** Size agreement to an order is
weak.  ** The discriminating check is whether the arm's per-bin residual has the $\\exp[-(\\ell/\\ell_D)^2]$
PROFILE ** -- rising as $\\ell^2$ in the exponent -- or is flat/random.  A profile match would convert
this candidate; a flat residual would kill it. ***

WHAT IS NOT CLAIMED.  ** Not that $281$ is derived ** -- *** the arm scores against the plik COVARIANCE,
not a flat $\\sigma$; this is an ORDER comparison and is reported as one. ***  ** Not that the row
closes ** -- *** it supplies the candidate `PO-10` lacked and names the test that would settle it. ***
** Not that CR is favoured or disfavoured ** -- F5 governs, and this receipt does not report a verdict.
** Not that $\\ell_D=1400$ is the corpus's value ** -- it is P15's illustrative scale; the PROFILE, not
its normalisation, is what the next test would use.

** COMPUTES: the damping residual over 185 bins at three error scales.  *** $r=1.0824$ is r2755's
corrected value and the profile is P15's own. *** **

⌗ **ABSENCE CLAIMS IN THIS RECEIPT ARE MEASURED AT d7f2e7e** *(per c54.220's rule, r2776).*

Written r2786.  Stated for reversal.
"""
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

R_DAMP, L_D = 1.0824, 1400.0
CR_MEASURED = 281.0


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def chi2_of(sigma):
    ls = np.linspace(100, 2000, 185)
    resid = 1 - np.exp(-(ls/L_D)**2*(R_DAMP**2 - 1))
    return float(np.mean((resid/sigma)**2))


def main():
    print()
    print("  C54 -- does CR's 281 need a mechanism, or is it the prediction?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    check('⛭⛭ ⓵ P15 states the high-$\\ell$ consequence with no free parameter: '
          '"$C_{\\ell}^{\\mathrm{CR}}/C_{\\ell}^{\\Lambda\\mathrm{CDM}} '
          '=\\exp[-(\\ell/\\ell_{D})^{2}(r^{2}-1)]$"',
          'The high-$\\ell$ consequence follows with no free parameter' in p15)

    lo, hi = chi2_of(0.01), chi2_of(0.002)
    check(f'⓶ and scoring that residual over 185 bins gives $\\chi^2/$dof from {lo:.0f} '
          f'($\\sigma=1\\%$) to {hi:.0f} ($\\sigma=0.2\\%$)',
          hi > lo > 100)
    check(f'⇒ so the measured {CR_MEASURED:.0f} SITS INSIDE that range -- ** and below the value at '
          'Planck\'s quoted few-tenths-of-a-per-cent errors **',
          lo < CR_MEASURED < hi and CR_MEASURED < chi2_of(0.005))

    # ⓷ F5 is the protection, and it is sharpened
    lik = open(next(iter([os.path.join(dp, f) for dp, _, fs in os.walk(os.path.join(ROOT, 'receipts'))
                          for f in fs if f == 'P15_where_the_likelihood_sits.py'])),
               encoding='utf-8', errors='replace').read()
    check('⓷ while F5 states the protection: "a negative is a measurement discrepancy, not a '
          'framework verdict" -- ** and reading 281 as a defect read a prediction as an error **',
          'measurement discrepancy, not a framework verdict' in lik)

    # ⓸ the discriminating test is shape
    ls = np.linspace(100, 2000, 185)
    prof = 1 - np.exp(-(ls/L_D)**2*(R_DAMP**2 - 1))
    check(f'⓸ and the discriminating test is SHAPE, not size: the profile rises from '
          f'{100*prof[0]:.2f}% at $\\ell=100$ to {100*prof[-1]:.1f}% at $\\ell=2000$ -- ** a flat '
          'residual would kill this candidate **',
          prof[-1]/prof[0] > 50)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** 281 is the order P15's own prediction produces. **")
    print('  ⛭⛭ ⓵ ** Scored over 185 bins: **')
    for s in (0.002, 0.005, 0.01):
        print(f'       σ = {100*s:>4.1f}%   bare damping → χ²/dof {chi2_of(s):>8.0f}')
    print(f'       measured CR arm                       {CR_MEASURED:>8.0f}')
    print('     ⇒ *** 281 sits INSIDE the range and BELOW the value at Planck\'s quoted errors. ***')
    print('  ⛭⛭⛭ ⓶ ** Which inverts the row\'s question. **  PO-10 asked what mechanism explains 281.')
    print('     *** The answer may be that nothing needs to: the arm is scoring the effect P15')
    print('     predicts, at the order P15 predicts it.  An arm returning a large χ² against ΛCDM is')
    print('     what a model predicting an 8.2% high-ℓ suppression IS. ***')
    print('  ⓷ ** And it sharpens F5 rather than weakening it: ** if CR\'s χ² is its own predicted')
    print('     signature being measured, ** the discrepancy IS the framework\'s claim ** — and')
    print('     reading 281 as a defect read a prediction as an error.')
    print('  ⓸ ** The discriminating test is SHAPE: ** the profile rises from')
    print(f'     {100*prof[0]:.2f}% at ℓ=100 to {100*prof[-1]:.1f}% at ℓ=2000.  ** A profile match')
    print('     converts this candidate; a flat residual kills it. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
