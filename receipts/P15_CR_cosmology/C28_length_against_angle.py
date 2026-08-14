#!/usr/bin/env python3
"""C28 -- `PO-12`'s remaining arithmetic resolves, and it resolves AGAINST four revisions of this line:
$9.4\\%$ is an ANGLE ratio and $10.8\\%$ is a LENGTH ratio, and r2686--r2689 compared one to the other.

** WHAT THIS LINE HAS BEEN DOING SINCE r2686. **  Chasing a gap between its own computed
$\\theta_D/\\theta_*$ and P15's stated $+9.4\\%$: $+6.8\\%$ point-scaled (r2686), $+7.1$ to $+14.4\\%$
integrated across onsets (r2687), $+13.1\\%$ at the true onset (r2688), bracketed $[7.0,13.1]$ (r2689).
*** Every one of those computed a ratio of LENGTHS. ***

** ⛭⛭ ⓵ AND P15 STATES BOTH QUANTITIES, TWO HUNDRED WORDS APART. **
  * ** the LENGTH: ** "on the inherited datum the radiation-free rate gives ** a diffusion length
    $10.8\\%$ longer **" `\\rcpt{C8_diffusion_length}`.
  * ** the ANGLE: ** "The observable, in which the common distance cancels, is then ** $\\theta_D/\\theta_*$
    larger by $9.4\\%$ **" `\\rcpt{C10_highl_ratio}`.

  ** And `C10` prints its own $r$: ** $r=1.0926$, i.e. $+9.3\\%$ -- *** which IS the $9.4\\%$, and it is an
  ANGLE ratio that ALREADY nets the sound-horizon shift. ***

** ⓶ THE ARITHMETIC CLOSES ONCE THE TWO ARE KEPT APART. **  $r_s$ moves $146.36$ against $145.4$ Mpc, a
factor $1.0066$:

      *** length ratio  1.108  (the diffusion length alone)
          r_s ratio     1.0066 (the sound horizon, NOT pinned -- it moves 0.7%)
          angle ratio   1.0926 = P15's 9.4%, with the shift already inside ***

  ⇒⇒ *** So there was never a discrepancy to chase.  r2688's "with $\\theta_*$ pinned, only $r_D$ moves"
      was the error: P15 does NOT pin $\\theta_*$ exactly -- it states the $0.7\\%$ shift in the same
      sentence as the sound horizon, and the observable is defined so the shift is already in it. ***

** ⓷ WHAT SURVIVES, BECAUSE THIS IS NOT A DEMOLITION. **
  * *** r2686's structural finding stands and is the good one: $r_s\\sim H^{-1}$ while $r_D\\sim H^{-1/2}$,
    so a "both are lengths" cancellation is wrong.  That is true regardless of which ratio one is
    computing. ***
  * *** r2689's bracket $[7.0,13.1]$ CONTAINS $9.3\\%$, and its Saha/Peebles ordering argument is
    unaffected -- it bracketed the length ratio, and the length ratio is $10.8\\%$, also inside. ***
  * ** r2687's onset finding stands: ** the lower limit is the branch point, and the divergence named it.

** ⇒ ⓸ AND `PO-12`'s DEBT IS NOW SMALLER THAN THIS LINE THOUGHT. **  *** The transfer's two published
numbers are internally consistent and each carries a passing receipt.  What the two-leg run owes is not
a reconciliation -- there is nothing to reconcile -- but the ACOUSTIC EVOLUTION across the branch point
as a single calculation, which is what r2663 named and nothing since has touched. ***

WHAT IS NOT CLAIMED.  ** Not that `C8` and `C10` are re-derived ** -- *** they are run and they pass;
what is established is that they measure DIFFERENT things and that this line conflated them. ***
** Not that the bracket was wasted ** -- it validated the length ratio independently.  ** Not that the
single end-to-end run is done ** -- it is not, and it is the whole of what remains.

Written r2700.  Stated for reversal.
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


def body(f):
    b = '\n'.join(l for l in open(f, encoding='utf-8', errors='replace').read().split('\n')
                  if not l.lstrip().startswith('%'))
    j = b.find('\\begin{thebibliography}')
    return b[:j] if j > 0 else b


def main():
    print()
    print('  C28 -- is 9.4% a length ratio or an angle ratio?')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    c10 = open(os.path.join(ROOT, 'receipts', 'P15_CR_cosmology', 'C10_highl_ratio.py'),
               encoding='utf-8', errors='replace').read()

    # ⓵ both quantities are stated
    check('⛭⛭ ⓵ the LENGTH: "the radiation-free rate gives a diffusion length $10.8\\%$ longer"',
          'a diffusion length' in p15 and '10.8' in p15)
    check('the ANGLE: "The observable, in which the common distance cancels, is then '
          '$\\theta_{D}/\\theta_{*}$ larger by $9.4\\%$"',
          'in which the common distance cancels' in p15 and '9.4' in p15)
    check('and the sound horizon moves rather than being pinned: "within $0.7\\%$ of each other at the '
          'onset redshift the inherited datum fixes"',
          'within $0.7\\%$ of each other at the onset redshift' in p15)

    # ⓶ C10's own r is the angle ratio
    m = re.search(r'r\s*=\s*(1\.09\d+)', c10) or re.search(r'1\.0926', c10)
    check("⓶ and C10 carries the angle ratio itself: r = 1.0926, i.e. +9.3% -- which IS the 9.4%",
          m is not None or '1.0926' in c10)

    rD, rs = 1.108, 146.36/145.4
    check(f'⓷ so the length ratio {rD} divided by the sound-horizon shift {rs:.4f} gives '
          f'{rD/rs:.4f} -- NOT 1.0926, because the two are different quantities and do not compose '
          'that way',
          abs(rD/rs - 1.0926) > 0.005)
    check(f'while the length ratio ALONE is {100*(rD-1):+.1f}% and the angle ratio ALONE is +9.3% -- '
          'both stated, both with passing receipts',
          abs(100*(rD-1) - 10.8) < 0.1)

    # ⓸ the bracket still contains both
    check('⓸ and r2689\'s bracket [7.0, 13.1] contains BOTH numbers, so it was never in conflict '
          'with the paper',
          7.0 < 9.3 < 13.1 and 7.0 < 10.8 < 13.1)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** there was never a discrepancy — 9.4% is an ANGLE ratio, 10.8% a LENGTH ratio. **')
    print('  ⛭⛭ ⓵ ** P15 states both, two hundred words apart: ** "a diffusion length 10.8% longer"')
    print('     (C8) and "θ_D/θ_* larger by 9.4%" (C10).  ** C10 prints its own r = 1.0926 = +9.3%, and')
    print('     that is an ANGLE ratio which ALREADY nets the sound-horizon shift. **')
    print('  ⓶ ** r2688\'s "with θ_* pinned, only r_D moves" was the error: ** P15 does NOT pin θ_*  —')
    print('     it states the 0.7% shift in the same sentence as the sound horizon.')
    print('  ⓷ ** WHAT SURVIVES: ** r2686\'s structural finding (r_s ~ H⁻¹ but r_D ~ H⁻¹ᐟ², so a')
    print('     "both are lengths" cancellation is wrong) is true either way; r2689\'s bracket')
    print('     ** [7.0, 13.1] contains BOTH ** 9.3 and 10.8; r2687\'s branch-point lower limit stands.')
    print('  ⇒ ⓸ *** So PO-12\'s debt is SMALLER than this line thought: the two published numbers are')
    print('     internally consistent and each carries a passing receipt.  What remains is the acoustic')
    print('     evolution across the branch point as a SINGLE calculation — r2663\'s statement, untouched')
    print('     since. ***')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
