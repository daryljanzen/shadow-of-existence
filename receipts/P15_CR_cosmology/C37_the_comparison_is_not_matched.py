#!/usr/bin/env python3
"""C37 -- `L-814`'s comparison is NOT MATCHED and its number must not stand as a result: the CR arm was
held at $k=2$ with $n_s$ FIXED at $\\Lambda$CDM's value, and freeing the tilt alone removes ** 15.6x ** of
the $\\chi^2$.  The specification was this line's, at r2710.

** WHAT WAS REPORTED. **  cc54's `L-814`, run to this line's specification: $F3(\\varphi{=}0)=+50{,}497$
and $F3(\\varphi{=}\\pi)=+67{,}624$ against a threshold of $21.5$.  *** Reported here at r2724 as "the
paper's own envelope scored", with an independent estimate agreeing to the same order.  ** Both the run
and the check inherited the same defect. ** ***

** ⛔ ⓵ THE DEFECT: THE COMPARISON IS NOT MATCHED. **  *** The $\\Lambda$CDM arm carries six free
parameters.  The CR arm was given TWO -- $\\Omega_m$ and $A_s$ -- with $\\omega_b$, $\\omega_c$, $\\tau$ and
** $n_s$ HELD AT $\\Lambda$CDM's FITTED VALUES **.  So the CR arm is scored on a spectrum whose tilt was
fitted for a different model. ***

** ⛭⛭ ⓶ AND THE TILT ALONE IS WORTH A FACTOR OF FIFTEEN. **

      *** n_s HELD  (as run)  chi^2 = 1.55e5   threshold 21.5   ->  7200x over
          n_s FREE            chi^2 = 9.95e3   threshold 16.1   ->   622x over
          at dn_s = -0.245                                          15.6x removed ***

  ⇒ *** A number that moves by more than an order of magnitude under a parameter the comparison should
      have varied is not a measurement of the model.  It is a measurement of the CONSTRAINT. ***

** ⓷ AND THE DEEPER SCOPE PROBLEM, WHICH THE TILT DOES NOT TOUCH. **  P15's envelope
$\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$ is a ** damping-tail MODIFICATION FACTOR ** derived from a diffusion-length
ratio.  Scoring it bin-by-bin treats it as a complete prediction of the power spectrum.
  ⇒⇒ *** So what was actually tested is "$\\Lambda$CDM, multiplied by CR's damping correction, against the
      data" -- a fair test OF THE CORRECTION, and not a test of CR computing its own spectrum, which at
      this level of detail it does not do. ***

** ⓸ THE HONEST STATUS. **  *** `L-814`'s NUMBER is withdrawn as a model comparison.  What survives is:
(a) the machinery runs and is instrumented; (b) the instrument floor is measured at $F2=+1114$; (c) the
$\\varphi=\\pi$ branch scores WORSE than $\\varphi=0$, which is a RELATIVE statement between two CR
configurations on identical footing and is unaffected by the mismatch. ** The absolute verdict is not
established and is not to be cited. ** ***

WHAT IS NOT CLAIMED.  ** Not that cc54 erred ** -- *** they ran the specification this line wrote at
r2710--r2719 and flagged the floor rather than laundering it.  The $k=2$ choice is r2710's. ***  ** Not
that a matched comparison would pass ** -- *** the tilt-corrected residual is still $\\sim10^4$; what is
claimed is that the comparison as run cannot support a verdict either way, not that CR would survive
one. ***  ** Not that the envelope is wrong ** -- only that scoring a modification factor as a spectrum
is a category difference that must be stated with any result.

Written r2725.  Stated for reversal.
"""
import glob
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  C37 -- is L-814 a matched comparison?')
    print()
    r, lD = 1.0926, 1400.0
    ls = np.linspace(30, 2500, 215)
    bw = (2500-30)/215
    env = np.exp(-(ls/lD)**2*(r**2 - 1))
    sig = np.sqrt(2/((2*ls+1)*0.6*bw))
    chi_held = float(np.sum(((env-1)/sig)**2))

    best = None
    for dn in np.linspace(-0.30, 0.05, 141):
        for lA in np.linspace(-0.6, 0.1, 141):
            m = np.exp(lA)*(ls/500.0)**dn
            c = float(np.sum(((env-m)/sig)**2))
            if best is None or c < best[0]:
                best = (c, dn, lA)
    chi_free, dn, _ = best

    check(f'⛔ ⓵ with $n_s$ HELD (as run) the envelope scores $\\chi^2={chi_held:.3g}$',
          chi_held > 1e4)
    check(f'⛭⛭ ⓶ while freeing the tilt alone drops it to ${chi_free:.3g}$ at '
          f'$\\Delta n_s={dn:+.3f}$ -- a factor of {chi_held/chi_free:.1f}',
          chi_held/chi_free > 5)
    check('⇒ so the number moves by more than an order of magnitude under a parameter the comparison '
          'should have varied -- it measures the CONSTRAINT, not the model',
          chi_held/chi_free > 10)

    # the threshold moves only slightly
    t2 = (6-2)*np.log(215)
    t3 = (6-3)*np.log(215)
    check(f'⓷ and the threshold barely moves for the extra parameter: {t2:.1f} to {t3:.1f}, so the '
          'penalty does not offset the gain',
          abs(t2 - t3) < 6 and chi_held - chi_free > 100*(t2 - t3))

    # what survives is the relative statement
    # ** read cc54's own statement rather than restating their numbers: a comparison of two
    # constants I typed cannot fail, and the claim is that THEIR receipt carries the relation. **
    l814 = open(glob.glob(os.path.join(ROOT, 'receipts', 'L814_po10_bic_pair', '*.py'))[0],
                encoding='utf-8', errors='replace').read()
    check('⓸ what survives is RELATIVE: cc54\'s receipt states phi=pi is "WORSE, not better" than '
          'phi=0 -- two CR configurations on identical footing, which the mismatch does not affect',
          'WORSE, not better' in l814)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the comparison is NOT MATCHED — the number is withdrawn as a result. **')
    print(f'  ⛔ ⓵ ** The ΛCDM arm carries six free parameters; the CR arm was given TWO, ** with n_s')
    print("     held at ΛCDM's fitted value.  ** The CR arm is scored on a spectrum whose tilt was")
    print('     fitted for a different model. **')
    print(f'  ⛭⛭ ⓶ ** And the tilt alone is worth {chi_held/chi_free:.1f}×: ** χ² = {chi_held:.3g} held,')
    print(f'     {chi_free:.3g} free, at Δn_s = {dn:+.3f}.')
    print('     ⇒ *** A number that moves by more than an order of magnitude under a parameter the')
    print('       comparison should have varied is not a measurement of the model. ***')
    print('  ⓷ ** And the deeper scope problem the tilt does not touch: ** P15\'s envelope is a damping')
    print('     tail ** MODIFICATION FACTOR **, and scoring it bin-by-bin treats it as a complete')
    print('     spectrum.  *** What was tested is "ΛCDM × CR\'s damping correction" — a test OF THE')
    print('     CORRECTION, not of CR computing its own spectrum. ***')
    print('  ⓸ ** HONEST STATUS: the NUMBER is withdrawn as a model comparison. **  What survives:')
    print('     the machinery runs; the floor is measured at F2 = +1114; and φ=π scores worse than')
    print('     φ=0, a RELATIVE statement between two CR configurations on identical footing.')
    print('     ** The absolute verdict is not established and is not to be cited. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
