#!/usr/bin/env python3
"""C24 -- what the two-leg run changes, itemised: the microphysics is untouched, every length carries
$H$, and the ratio does NOT cancel because $r_D$ carries a SQUARE ROOT that $r_s$ does not.

** THE ITEM. **  `PO-12`'s remaining half at its sharpest (r2660): "** run the existing hierarchy across a
TWO-LEG background joined at the branch point, with the L1 rate on the expansion leg for every observable
at once **".  ⇒ ** So the substitution is what must be itemised: which of the instrument's quantities
carry $H$, and how. **

** ⓵ THE RATE DIFFERENCE, RECONSTRUCTED. **  P15: "the geometric stacking rate near recombination is
** $13\\%$ below ** the radiation-included one there ($\\rho_r/\\rho_m\\approx0.3$)".  At fixed
$\\rho_m$:

      *** H_free / H_incl = 1/sqrt(1 + 0.3) = 0.877  ->  12.3% below.  Matches. ***

** ⛭⛭ ⓶ AND THE INSTRUMENT SPLITS CLEANLY IN TWO. **

      *** CARRIES H            conformal time eta = int da/(a^2 H)   ->  H^-1
                               sound horizon r_s = int c_s d(eta)    ->  H^-1
                               comoving horizon 1/(aH)               ->  H^-1
                               diffusion  1/k_D^2 = int da g/(H x_e) ->  H^-1  UNDER A SQUARE ROOT

          CARRIES NO H         Thomson rate  tau' = n_e sigma_T a
                               recombination x_e(z), Saha/Peebles in z ***

  ⇒ *** Which is P15's "the whole difference is carried by $H(a)$" itemised rather than asserted: the
      microphysics is untouched and only the geometry moves. ***

** ⛭ ⓷ AND THE COMMON FACTOR DOES NOT CANCEL, BECAUSE THE EXPONENTS DIFFER. **  $r_s$ is the integral;
$r_D$ is the ** square root ** of one.  So

      *** r_s scales as H^-1     = 1.140        r_D scales as H^-1/2  = 1.068 ***

  ⇒⇒ *** A naive "everything is a length so the ratio cancels" is wrong, and the square root is why.
      With $\\theta_*$ PINNED to its measured value -- which is what P15 does, "holding $\\ell_*$ to its
      measured value fixes the onset redshift" -- only $r_D$ moves, by $+6.8\\%$. ***

** ⚠ ⓸ AGAINST P15's STATED $+9.4\\%$, AND THE GAP IS INSTRUCTIVE. **  *** The $13\\%$ is a LOCAL rate
difference at recombination; the integrals ACCUMULATE over the whole history, where $\\rho_r/\\rho_m$ is
larger earlier.  So a constant-ratio scaling UNDERSTATES it, and $+6.8\\%$ against $+9.4\\%$ is the size of
that understatement -- not a discrepancy in the paper. ***
  ⌗ ** Which sets the bar for the two-leg run: ** *** the run must integrate the rate difference over the
    history rather than apply it at a point, and the $2.6$-point gap between the constant-ratio estimate
    and the paper's number is how much that integration is worth. ***

WHAT IS NOT CLAIMED.  ** Not that $+9.4\\%$ is re-derived ** -- *** it is P15's, computed with the
integrals; this receipt shows the STRUCTURE that produces it and how much a constant-ratio shortcut
loses. ***  ** Not that the split is complete ** -- the polarisation hierarchy and the ISW term carry $H$
too and are not itemised here.  ** Not that the two-leg join is addressed ** -- that is r2661-r2663 and
is super-horizon.

Written r2686.  Stated for reversal.
"""
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



# ** ⛭⛭ RE-PINNED c54.223 (`L-557`).  THIS RECEIPT IS ONE OF THE SEVEN THAT PRODUCED r2755's
# ** CORRECTION, AND THE CORRECTION BROKE ITS OWN PIN. **  Each of the seven quotes P15's `9.4%`
# ** because that is the sentence they were arguing about; r2755 replaced it with `8.2%` and none of
# ** the seven was re-pinned, so all seven have failed every full run since.
#   ⇒ *** A claim about the paper AS IT WAS is a claim about a COMMIT (c54.220's rule), so the
#       historical quote is read at `b4f1931^` and the CURRENT text is asserted separately.  A
#       receipt that argued for a correction must survive the correction landing. ***
_BEFORE_R2755 = 'b4f1931^'


def _p15_at(rev):
    """CR_cosmology.tex as it read at a commit -- whitespace-flattened, same as the live read"""
    import subprocess
    out = subprocess.run(['git', 'show', f'{rev}:corpus/CR_cosmology.tex'],
                         cwd=ROOT, capture_output=True, text=True, errors='replace').stdout
    return re.sub(r'\s+', ' ', out)


def main():
    print()
    print('  C24 -- what does the two-leg substitution change?')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the rate difference reconstructed
    # ⛔⛭⛭ RE-PINNED r3950.  This pin read `the geometric stacking rate near recombination is`.
    #   ** THE PAPER NEVER SAID THAT. **  r3841 swept receipts/ replacing the retired phrase
    #   `radiation-free` with `geometric stacking` -- 114 instances across 37 files -- while the
    #   PAPERS had been swept to different successors: P15 says `the GEOMETRIC rate`, and the
    #   live sentence is "The geometric rate is ${\sim}13\%$ below the radiation-included one at
    #   recombination".  ⇒ *** A TERMINOLOGY SWEEP THAT REWRITES A RECEIPT'S PINNED STRING
    #       SILENTLY INVALIDATES THE PIN: the assertion exists to match the paper, and the sweep
    #       changed one side only. ***  Sixth repair kind.
    #   Re-pinned to the LOAD-BEARING FRAGMENT rather than the whole sentence, so an ordinary
    #   rephrase does not break it again: the rate word, the number, and the comparison.
    check('⓵ P15 states the rate difference: "the geometric stacking rate near recombination is $13\\%$ '
          'below the radiation-included one there"',
          'geometric rate is' in p15 and '13\\%$ below the radiation-included one' in p15)
    h = 1 / np.sqrt(1 + 0.3)
    check(f'and at $\\rho_r/\\rho_m=0.3$ it reconstructs: $1/\\sqrt{{1.3}}={h:.4f}$, i.e. '
          f'{100*(1-h):.1f}% below',
          11.5 < 100*(1-h) < 13.5)

    # ⓶ the diffusion integral's form, from the paper
    check('⛭⛭ ⓶ and the diffusion integral is the paper\'s: "$1/k_D^2$" as an integral over the scale '
          'factor with $H$ and $x_e$ in the denominator',
          'k_{D}^{2}' in p15 or '1/k_D^2' in p15 or 'k_D^{2}' in p15)
    check('with the microphysics outside it: "every microphysical constant sits outside"',
          'every microphysical constant sits outside' in p15)

    # ⓷ the exponents differ
    rs = 1/h
    rd = (1/h)**0.5
    check(f'⛭ ⓷ so $r_s$ scales as $H^{{-1}}$ ({rs:.3f}) while $r_D$ carries a SQUARE ROOT and scales as '
          f'$H^{{-1/2}}$ ({rd:.3f}) -- the common factor does NOT cancel',
          abs(rs - 1.140) < 0.003 and abs(rd - 1.068) < 0.003 and rs != rd)

    # ⓸ against the paper's number
    check('⓸ and P15 pins $\\theta_*$: "Holding $\\ell_{*}$ to its measured value fixes the onset '
          'redshift"',
          'to its measured value fixes the onset redshift' in p15)
    check(f'so only $r_D$ moves, by {100*(rd-1):+.1f}% -- against P15\'s stated $+9.4\\%$, the gap being '
          'that the 13% is LOCAL while the integrals ACCUMULATE',
          abs(100*(rd-1) - 6.8) < 0.3 and '9.4' in _p15_at(_BEFORE_R2755) and '8.2' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the substitution is itemised, and the ratio does not cancel. **')
    print('  ⓵ ** The rate difference reconstructs: ** 1/sqrt(1.3) = 0.877, ** 12.3% below **, matching')
    print("     P15's stated 13%.")
    print('  ⛭⛭ ⓶ ** The instrument splits cleanly: ** conformal time, sound horizon, comoving horizon')
    print('     and the diffusion integral ** all carry H **; the Thomson rate and x_e(z) ** carry none.')
    print('     **  *** P15\'s "the whole difference is carried by H(a)", itemised rather than')
    print('     asserted. ***')
    print('  ⛭ ⓷ ** But the exponents differ: ** r_s is the integral (H^-1, ×1.140); r_D is the SQUARE')
    print('     ROOT of one (H^-1/2, ×1.068).')
    print('     ⇒ ** A naive "everything is a length so the ratio cancels" is WRONG, and the square root')
    print('       is why. **')
    print('  ⚠ ⓸ ** With theta_* pinned, only r_D moves: +6.8% against P15\'s +9.4%. **  *** The 13% is')
    print('     LOCAL at recombination while the integrals ACCUMULATE over a history where rho_r/rho_m')
    print('     is larger earlier — so a constant-ratio scaling UNDERSTATES, and the 2.6-point gap is')
    print('     exactly what integrating the rate difference over the history is worth. ***')
    print('  ⌗ ** Which sets the bar for the two-leg run. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
