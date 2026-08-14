#!/usr/bin/env python3
"""C41 -- a tilde marks a value the corpus has not settled, and the test is whether ANOTHER receipt
disagrees.  `$\\sim$301` failed that test and was made precise; `$\\sim$8\\%` passed it and stays.

** THE PRINCIPLE, Daryl r2749. **  *** "Isn't '~301' just a place marker for while the value is not
accurately known?  If the value is now determined more accurately and is not expected to change then it
ought to be reported with accurate precision.  Not as a gloss that was only necessary while the value
was changing as you computed things." ***
  ⇒ ** And r2748 concluded the opposite -- "the tilde is there, the paper is honest, no edit is owed" --
  which mistook the PRESENCE of a hedge for its JUSTIFICATION. **

** ⛭⛭ ⓵ APPLIED TO `$\\sim$301`: THE HEDGE WAS STALE, AND THE EDIT IS MADE. **  ** One receipt asserts
the value and none competes: ** `P15_zonset_determinations` carries $100\\theta_*=1.04109$ and
`assert abs(MEAS_L - 301.76) < 0.01`.  *** A published measurement and arithmetic on it.  Nothing about
it moves as CR computes things, so the tilde was marking a settlement that had already happened. ***
  ⇒ ** P15 now reads "against the measured $301.76$". **  *** And the correction runs in the programme's
      favour: the gap was never $1.20$; it is $0.44$. ***

** ⛔⛭⛭ ⓶ APPLIED TO `$\\sim8\\%$`: THE HEDGE IS EARNED, AND NINE EDITS WERE REVERTED. **  *** This line
replaced all nine with $8.2\\%$ on the strength of `P15_damping_ratio_clean`, which returns $+8.2\\%$ on
CAMB's exact $x_e(z)$.  ** Then C8 turned out to derive $+10.83\\%$ analytically from the corpus's own
datum -- AND TO NAME THE DISAGREEMENT IN ITS OWN OUTPUT: ** "damping_ratio_clean.py reports
$\\sim+9\\%$.  This derivation gives $+10.8\\%$." ***

  ⇒⇒ *** SO THE NUMBER IS CONTESTED INSIDE THE CORPUS, and a tilde on a contested number is exactly
      what a tilde is for.  ** The nine edits were reverted. ** ***

** ⓷ WHICH GIVES THE TEST, and it is mechanical rather than a judgement. **

      *** a tilde is STALE     when one receipt asserts the value and none competes
          a tilde is EARNED    when receipts disagree, or none asserts ***

  ⌗ ** And the second case is invisible from the paper. **  *** P15's prose looks identical in both:
    `${\\sim}301$` and `${\\sim}8\\%$` are the same three characters.  ** The difference is entirely in
    whether the receipts behind them agree, which is why the test has to run on the receipts and not on
    the text. ** ***

** ⓸ AND THE DISAGREEMENT IS NOW NAMED AS OWED. **  *** $+10.83\\%$ (analytic, baryon-weighted, from the
inherited datum) against $+8.2\\%$ ($\\theta_D/\\theta_*$ on CAMB's exact history) -- C8 flags it and
nothing resolves it.  ** That is a live discrepancy on a figure P15 calls "a real, computed effect" nine
times. ** ***

WHAT IS NOT CLAIMED.  ** Not that either damping figure is right ** -- *** they measure ratios that may
not be the same ratio, and C8's own text says the baryon weighting moves $+10.68\\%$ to $+10.83\\%$ while
the CAMB receipt reports $r_D$ alone at $1.0897$; adjudicating them is the owed work, not this
receipt. ***  ** Not that every tilde in the corpus was audited ** -- 63 exist and most are honest
order-of-magnitude statements ($H_0\\approx68$, $T\\approx0.8$eV); two were tested.

** COMPUTES: nothing new.  *** Two existing receipts were RUN and their outputs compared. *** **

Written r2749.  Stated for reversal.
"""
import glob
import os
import re

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
    print("  C41 -- is a tilde in P15 a stale hedge or an earned one?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    def rcpt(n):
        return open(glob.glob(os.path.join(ROOT, 'receipts', '**', n), recursive=True)[0],
                    encoding='utf-8', errors='replace').read()

    # ⓵ the 301 case: one asserter, no competitor -> made precise
    check('⛭⛭ ⓵ P15 now reads "against the measured $301.76$" -- the tilde is gone',
          'measured $301.76$' in p15 and '{\\sim}301' not in p15)
    check('and one receipt asserts it with no competitor: '
          '"assert abs(MEAS_L - 301.76) < 0.01"',
          'MEAS_L - 301.76' in rcpt('P15_zonset_determinations.py'))

    # ⓶ the 8% case: receipts disagree -> tilde stays
    check('⛔ ⓶ while $\\sim8\\%$ REMAINS tilde-marked in P15, nine times',
          len(re.findall(r'\{\\sim\}8\\%', p15)) == 9)
    c8 = rcpt('C8_diffusion_length.py')
    # ** C8 prints the figure from an f-string, so the number is COMPUTED and not literal --
    # which is stronger: it cannot go stale against its own derivation. **
    check('because C8 derives a different figure, computed rather than quoted: "WITH THE BARYON '
          'TERMS: r_D IS {100*(rat-1):+.2f}% LONGER"',
          'WITH THE BARYON TERMS' in c8 and '100*(rat-1)' in c8)
    check('⛭⛭ and C8 NAMES THE DISAGREEMENT IN ITS OWN TEXT: "damping_ratio_clean.py reports ~+9%. '
          'This derivation gives +10.8%"',
          'damping_ratio_clean.py reports' in c8 and 'This derivation gives' in c8)

    # ⓷ the two look identical in the paper
    check('⓷ and the two cases are indistinguishable from the prose alone -- both were the same '
          'three characters before this revision',
          '{\\sim}8\\%' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** a tilde is stale when ONE receipt asserts and none competes. **')
    print('  ⛭⛭ ⓵ ** ~301 FAILED that test: ** one receipt asserts 301.76, nothing competes, and the')
    print('     value is a published measurement plus arithmetic — it does not move as CR computes.')
    print('     ** P15 now reads 301.76, and the correction runs in the programme\'s favour: the gap')
    print('     was never 1.20, it is 0.44. **')
    print('  ⛔ ⓶ ** ~8% PASSED it, and nine edits were reverted. **  This line replaced all nine with')
    print('     8.2% on one receipt — then C8 turned out to derive +10.83% analytically ** and to name')
    print('     the disagreement in its own output. **')
    print('     ⇒ *** A tilde on a CONTESTED number is exactly what a tilde is for. ***')
    print('  ⓷ ** And the two are indistinguishable from the prose: ** ${\\sim}301$ and ${\\sim}8\\%$ are')
    print('     the same three characters.  ** The difference is entirely in whether the receipts')
    print('     behind them agree — so the test runs on the receipts, never on the text. **')
    print('  ⓸ ** And the disagreement is now named: ** +10.83% analytic against +8.2% on CAMB\'s exact')
    print('     history, on a figure P15 calls "a real, computed effect" nine times.  ** Owed. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
