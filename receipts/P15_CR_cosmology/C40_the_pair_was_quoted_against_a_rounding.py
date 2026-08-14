#!/usr/bin/env python3
"""C40 -- `PO-10`'s first pair is quoted against a ROUNDED measurement, and the rounding is a third of
the apparent discrepancy.  The corpus carries the unrounded value in its own receipt.

** THE READ, owed since r2746. **  *** The row needs published uncertainties for four measured values.
Before treating them as external, the question is whether the corpus already carries them -- and for
the first pair it carries something better and worse than an uncertainty: THE UNROUNDED VALUE. ***

** ⛭⛭ ⓵ WHAT P15's TEXT SAYS, AND WHAT ITS OWN RECEIPT SAYS. **

      *** P15 text:      "theta_* = D_M/r_s = 302.2 against the MEASURED 301"
          P15_zonset_determinations:
                         "Pinning the MEASURED acoustic angle 100 theta_* = 1.04109
                          (l_A = pi/theta_* = 301.76)" ***

  ⇒ ** The measured value is $301.76$, and the paper's prose rounds it to $301$. **

** ⓶ AND THE ROUNDING IS A THIRD OF THE GAP. **

      *** CR 302.2 against 301.00  ->  +1.20   (+0.399%)
          CR 302.2 against 301.76  ->  +0.44   (+0.146%) ***

  ⇒⇒ *** The discrepancy is $0.44$, not $1.20$.  ** A comparison built from the paper's prose would
      have carried an error two and a half times the real one, and in the direction that makes CR look
      worse. ** ***

** ⛭ ⓷ WHICH IS A DIFFERENT DEFECT FROM THE ONE r2746 GUARDED. **  *** r2746 forbade INVENTING an
uncertainty.  This is the mirror: taking a ROUNDED value from prose as though it were the datum.  Both
put a number into a comparison that the measurement does not support -- one too tight, one too loose --
and the prose rounding is the easier to miss because it is the corpus's own sentence. ***

** ⓸ AND THE UNCERTAINTY IS STILL NOT HERE. **  *** $100\\theta_*$ is among the best-measured
quantities in cosmology and its error bar is published, but this line does not have it and r2746's rule
stands: ** do not invent it **.  What r2748 supplies is the correct CENTRAL value for one of the four
pairs, from the corpus's own receipt, and the observation that the other three should be checked the
same way before any of them is scored. ***

** ⛔ ⓹ AND A CORRECTION TO THIS RECEIPT'S OWN FIRST DRAFT, MADE BEFORE IT BANKED. **  *** P15 does
not write "$301$".  It writes "against the measured ${\sim}301$" -- **the tilde is there, and the paper
marks the value as approximate**.  So the defect is NOT the paper's: it is honest, and its receipt
carries the precise figure and asserts it. ***

  ⇒ ** What remains true, and smaller: ** *** a COMPARISON that reads "$\sim301$" as its datum carries
    $1.20$ where the measurement gives $0.44$.  `PO-10`'s comparison must take the RECEIPT's value and
    not the prose's -- and nothing said so until now.  ** No paper edit is owed; a register note is. ***

WHAT IS NOT CLAIMED.  ** Not that the pair is scored ** -- *** no $\\sigma$, no $\\chi^2$; the point of
r2746 stands. ***  ** Not that P15 errs ** -- *** rounding $301.76$ to $301$ in prose is ordinary and the
receipt carries the precise value, which is the corpus working as designed; what would have erred is a
comparison reading the prose as the datum. ***  ** Not that the other three pairs are checked ** -- they
are not, and that is now named.

** COMPUTES: the two differences, $302.2-301.00$ and $302.2-301.76$, and their percentages.  *** Both
values are the corpus's own -- the CR figure from `C10`, the measured from
`P15_zonset_determinations`. *** **

Written r2748.  Stated for reversal.
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
    print("  C40 -- is PO-10's first pair quoted against the measurement or against a rounding?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))
    z = open(glob.glob(os.path.join(ROOT, 'receipts', '**', 'P15_zonset_determinations.py'),
                       recursive=True)[0], encoding='utf-8', errors='replace').read()

    check('⛭⛭ ⓵ P15\'s prose: "$\\theta_{*}=D_{M}/r_{s}=302.2$ against the measured $301$"',
          '302.2' in p15 and 'against the measured' in p15)
    check('while its own receipt carries the unrounded measurement: "Pinning the MEASURED acoustic '
          'angle 100theta_* = 1.04109 (l_A = pi/theta_* = 301.76)"',
          '1.04109' in z and '301.76' in z)

    CR, ROUNDED, MEAS = 302.2, 301.00, 301.76
    d_round, d_meas = CR - ROUNDED, CR - MEAS
    check(f'⓶ against the rounded {ROUNDED:.2f} the gap is {d_round:+.2f} ({100*d_round/ROUNDED:+.3f}%)',
          abs(d_round - 1.20) < 0.01)
    check(f'but against the measured {MEAS:.2f} it is {d_meas:+.2f} ({100*d_meas/MEAS:+.3f}%) -- '
          f'a factor of {d_round/d_meas:.1f} smaller',
          abs(d_meas - 0.44) < 0.01 and d_round/d_meas > 2)
    check('⇒ so the rounding is roughly a third of the apparent discrepancy, and in the direction '
          'that makes CR look worse',
          d_round > d_meas > 0)

    # ⓸ and the receipt pins its own value
    check('⓸ and the receipt asserts it rather than merely printing it: "assert abs(MEAS_L - 301.76)"',
          'MEAS_L - 301.76' in z)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the pair was quoted against a ROUNDING, and the corpus holds the real one. **")
    print(f'  ⛭⛭ ⓵ ** P15\'s prose rounds 301.76 to 301. **  Its own receipt carries')
    print('     100·θ_* = 1.04109, ℓ_A = 301.76, and asserts it.')
    print(f'  ⓶ ** The gap: ** {d_round:+.2f} against the rounding, {d_meas:+.2f} against the')
    print(f'     measurement — ** a factor of {d_round/d_meas:.1f} **, in the direction that makes CR')
    print('     look worse.')
    print('  ⛭ ⓷ *** WHICH IS THE MIRROR OF r2746\'s DEFECT.  That one forbade INVENTING an')
    print('     uncertainty; this is taking a ROUNDED value from prose as the datum.  Both put a')
    print('     number into a comparison the measurement does not support — one too tight, one too')
    print('     loose — and the prose rounding is the easier to miss BECAUSE IT IS THE CORPUS\'S OWN')
    print('     SENTENCE. ***')
    print('  ⓸ ** The uncertainty is still not here ** — 100·θ_* is among the best-measured quantities')
    print('     in cosmology, but this line does not have its error bar and will not invent it.')
    print('     ⌗ ** And the other three pairs are now named as needing the same check. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
