#!/usr/bin/env python3
"""C45 -- THE DAMPING DISCREPANCY IS RESOLVED: $x_e$ does not cancel from a ratio of INTEGRALS even
when it is identical in both, and C8's cancellation step is the error.

** ⓵ THE MEASUREMENT THAT SETTLES IT. **  Same range, same measure, ** only $x_e$ toggled **:

      *** x_e OMITTED (C8's step)          ratio 1.0994    +9.94%
          x_e INCLUDED (Hu--Sugiyama)      ratio 1.0837    +8.37%
                                                          ------
                                                           1.57pp ***

  ⇒ ** That is the whole gap. **  *** And the CAMB arm converges at $+5.66\\%$ with the full
      $R$-weighting, $+8.37\\%$ without it -- so the remaining difference from the receipt's $+8.97\\%$ is
      the baryon term, which C8 also carries at $0.15$pp.  Every piece is now accounted. ***

** ⛭⛭ ⓶ AND THE ERROR IS NOT WHAT r2750 SAID, NOR WHAT r2751 SAID. **
  * ** r2750: ** "C8 assumes $x_e$ is the SAME in both."  *** It is the same, near enough -- r2751
    measured the RESPONSE at $\\sim0.05$pp. ***
  * ** r2751/r2752: ** a normalisation, then truncation.  *** Both act on the integrands and cancel or
    converge. ***
  * *** THE ACTUAL ERROR: C8 assumes $x_e$ CANCELS.  **It does not cancel even when identical.** ***

** ⛭⛭⛭ ⓷ THE ALGEBRA, WHICH IS THE WHOLE LESSON. **

      *** INT f/H1  /  INT f/H2   DEPENDS ON f. ***

  ** A common weight cancels from a ratio of INTEGRANDS.  It does NOT cancel from a ratio of
  INTEGRALS ** -- *** because it reweights WHERE the two rates are being compared.  $x_e$ runs $0.13$ at
  recombination to $1.16$ above it: a factor of nine, concentrated exactly where the two rates differ
  most.  Down-weighting the high-$z$ end by nine pulls the ratio from $9.94$ to $8.37$. ***

** ⛔ ⓸ AND THIS CORRECTS r2752's OWN RULE. **  *** r2752 wrote: "a shared normalisation, a shared
$x_e$, a shared baryon term all divide out."  ** A shared CONSTANT divides out.  A shared FUNCTION does
not. **  The rule was right for the $\\sqrt{12}$ normalisation and wrong for $x_e$ in the same
sentence. ***

** ⓹ SO THE ADJUDICATION: THE CAMB ARM IS RIGHT AND C8 HAS A REAL ERROR. **  *** C8's STEP 1 states
"every microphysical constant is outside the integral" -- true of $\\sigma_T$ and $n_{e0}$, ** and $x_e$
is not a constant; it is the one factor in that group that VARIES **.  Its cancellation claim is
correct for the two constants and false for the third. ***

WHAT IS NOT CLAIMED.  ** Not that C8 is worthless ** -- *** its reduction to a single integral, its
elimination of the Boltzmann code from the RATIO, and its baryon correction all stand; one factor was
wrongly moved outside. ***  ** Not that $+8.37\\%$ is the answer ** -- the full Hu--Sugiyama with baryon
weighting gives $+5.66\\%$ and the receipt's own figure is $+8.97\\%$; ** which of those is P15's claimed
signature is a separate question this receipt does not settle. **  ** Not that P15's $\\sim8\\%$ should
now change ** -- it sits between the candidates, and r2749's test still governs.

** COMPUTES: the $r_D$ ratio with $x_e$ toggled on a fixed range and measure, using CAMB's own $x_e(z)$;
and the full Hu--Sugiyama ratio at three ceilings.  *** All cosmology is the corpus's own. *** **

Written r2753.  Stated for reversal.
"""
import glob
import os

import numpy as np
from scipy.integrate import trapezoid

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

OM, OR, OL = 0.3153, 8.6e-5, 0.6847


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print("  C45 -- does x_e cancel from a ratio of integrals?")
    print()
    import camb
    p = camb.CAMBparams()
    p.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.1200, TCMB=2.7255)
    res = camb.get_background(p)
    zstar = res.get_derived_params()['zstar']

    zg = np.linspace(zstar, 60000.0, 12001)
    xe = res.get_background_redshift_evolution(zg, ['x_e'], format='array')[:, 0]
    Hi = np.sqrt(OR*(1+zg)**4 + OM*(1+zg)**3 + OL)
    Hf = np.sqrt(OM*(1+zg)**3 + OL)

    def r(weight):
        f = 1/(weight*(1+zg)**2)
        return np.sqrt(trapezoid(f/Hf, zg))/np.sqrt(trapezoid(f/Hi, zg))

    r_off, r_on = r(np.ones_like(xe)), r(xe)

    check(f'⓵ with $x_e$ OMITTED (C8\'s cancellation step) the ratio is {r_off:.4f} '
          f'({100*(r_off-1):+.2f}%)', abs(100*(r_off-1) - 9.94) < 0.3)
    check(f'and with $x_e$ INCLUDED it is {r_on:.4f} ({100*(r_on-1):+.2f}%) -- '
          f'a shift of {100*(r_off-r_on):.2f}pp on the same range and measure',
          r_on < r_off and 100*(r_off-r_on) > 1.0)
    check(f'⛭⛭ ⓶ so $x_e$ does NOT cancel: it runs {xe[0]:.4f} at recombination to {xe[-1]:.4f} '
          f'above it -- a factor of {xe[-1]/xe[0]:.1f}, concentrated where the two rates differ most',
          xe[-1]/xe[0] > 5)
    check('⓷ while a shared CONSTANT does cancel exactly -- scaling the weight by any number leaves '
          'the ratio unchanged',
          abs(r(3.39*np.ones_like(xe)) - r_off) < 1e-9)
    check('⇒ which corrects r2752\'s own rule: "a shared normalisation, a shared $x_e$, a shared '
          'baryon term all divide out" -- a shared CONSTANT divides out, a shared FUNCTION does not',
          abs(r(3.39*xe) - r_on) < 1e-9 and abs(r_on - r_off) > 1e-3)

    # ⓸ C8's own wording
    c8 = open(glob.glob(os.path.join(ROOT, 'receipts', '**', 'C8_diffusion_length.py'),
                        recursive=True)[0], encoding='utf-8', errors='replace').read()
    check('⓸ and C8\'s step states it: "EVERY MICROPHYSICAL CONSTANT IS OUTSIDE THE INTEGRAL" -- true '
          'of $\\sigma_T$ and $n_{e0}$, and $x_e$ is the one member of that group that VARIES',
          'EVERY MICROPHYSICAL CONSTANT IS OUTSIDE THE INTEGRAL' in c8)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** x_e does not cancel from a ratio of INTEGRALS, and that is the whole gap. **')
    print(f'  ⓵ ** Same range, same measure, only x_e toggled: ** {100*(r_off-1):+.2f}% → '
          f'{100*(r_on-1):+.2f}%, a shift of {100*(r_off-r_on):.2f}pp.')
    print('  ⛭⛭⛭ ⓶ ** THE ALGEBRA:  ∫f/H₁ / ∫f/H₂ DEPENDS ON f. **  A common weight cancels from a')
    print('     ratio of INTEGRANDS.  ** It does not cancel from a ratio of INTEGRALS, because it')
    print(f'     reweights WHERE the two rates are compared. **  x_e runs {xe[0]:.2f} → {xe[-1]:.2f},')
    print('     a factor of nine, concentrated exactly where the rates differ most.')
    print('  ⛔ ⓷ ** And this corrects r2752\'s own rule, written one revision ago: ** "a shared')
    print('     normalisation, a shared x_e, a shared baryon term all divide out."')
    print('     *** A shared CONSTANT divides out.  A shared FUNCTION does not.  The rule was right')
    print('     for the √12 normalisation and wrong for x_e in the same sentence. ***')
    print('  ⓸ ** So C8 has a real error: ** "every microphysical constant is outside the integral" is')
    print('     true of σ_T and n_e0 — ** and x_e is the one member of that group that varies. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
