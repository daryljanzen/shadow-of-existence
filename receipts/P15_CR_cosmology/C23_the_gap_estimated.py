#!/usr/bin/env python3
"""C23 -- an ESTIMATE for the gap r2664 named: the peak-region decay differs between CR and
$\\Lambda$CDM because the rate that drives it is $k^2/(3\\mathcal H)$ and $\\mathcal H$ is what differs.

** THE GAP. **  r2664 closed the end-to-end chain at both ends -- $7.5\\%$ low-$\\ell$ deficit, $0.843$ at
$\\ell_D$ -- and named the middle as unreached: "** the acoustic peaks, where $\\Phi$ decays by a factor of
order two and the decay is $k$-dependent through $k^2/(3\\mathcal H)$ **".

** ⓵ AND THE RATE THAT DRIVES IT IS BUILT FROM THE THING THAT DIFFERS. **  P15 names the rate as
$k^2/(3\\mathcal H)$, and separately: "** the geometric stacking rate near recombination is $13\\%$ below the
radiation-included one there **".

  ⇒ *** So the decay is not common to the two cosmologies.  At fixed $k$, CR's driving rate is larger by
      $1/0.87=1.149$ -- the potential decays about $15\\%$ FASTER. ***

** ⚠ ⓶ AND HERE IS THE ESTIMATE, WITH ITS MODEL STATED. **  Treating the decay as exponential in a
variable that scales inversely with $\\mathcal H$, a $\\Lambda$CDM decay of factor $2$ becomes
$2^{1/0.87}=2.22$ in CR:

      *** surviving Phi ratio  =  (1/2.22)/(1/2.00)  =  0.902
          power ratio at the peaks  =  0.902^2  =  0.813 ***

  ⛔ *** THIS IS AN ESTIMATE AND NOT A DERIVATION.  The compounding assumes a form for the decay that the
      paper does not state; what IS the paper's is the rate $k^2/(3\\mathcal H)$, the $13\\%$, and the
      factor of order two.  A run of the hierarchy would replace this number, and the point of computing
      it is to say what SIZE the gap is, not to fill it. ***

** ⚠⚠ ⓷ AND A SECOND NEAR-COINCIDENCE, NAMED AS r2663 NAMED THE FIRST. **  *** $0.813$ at the peaks sits
next to $0.843$ at $\\ell_D$ from damping (RE-PINNED c54.223 -- was $0.823$ at $r=1.093$).  DIFFERENT ORIGINS: the peak number comes from the potential's
$k^2/(3\\mathcal H)$ decay compounding over the observable leg; the damping number from
$\\exp[-(\\ell/\\ell_D)^2(r^2-1)]$ with $r=1.082$ (RE-PINNED c54.223 -- was 1.093).  They are not the same effect and must not be summed as
though independent nor conflated as though one. ***

** ⇒ ⓸ WHAT THIS BUYS. **  *** The gap between $7.5\\%$ at low $\\ell$ and $18\\%$ at $\\ell_D$ is not empty
and is not small: the estimate puts the peak region at ~$19\\%$ down as well.  So the predicted deviation
is BROAD rather than confined to the tail -- which is a statement about where a likelihood confrontation
would bite, and it is the first such statement the chain supports. ***

WHAT IS NOT CLAIMED.  ** Not that $0.813$ is a prediction ** -- *** it is an order-of-magnitude estimate
with a stated model, and it is labelled as one everywhere it appears. ***  ** Not that the effects
compose ** -- the damping ratio and the decay ratio act in overlapping $\\ell$ ranges and their
composition is not computed.  ** Not that the $13\\%$ applies across the peak range ** -- P15 states it
"near recombination", and the peaks span a range over which $\\mathcal H$ changes.

Written r2665.  Stated for reversal.
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


def main():
    print()
    print('  C23 -- how big is the gap at the acoustic peaks?')
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the paper's two inputs
    check('⓵ the rate is the paper\'s: "the rate responsible is $k^{2}/(3\\mathcal{H})$, which grows with '
          '$k$"',
          'the rate responsible is' in p15 and '3\\mathcal{H}' in p15)
    check('and the rate difference is the paper\'s: "the geometric stacking rate near recombination is '
          '$13\\%$ below the radiation-included one there"',
          'the geometric stacking rate near recombination is' in p15 and '13\\%$ below' in p15)
    check('and the decay size is the paper\'s: "by a factor of order two across the first few peaks"',
          'by a factor of order two across the first few peaks' in p15)

    # ⓶ the estimate
    h = 0.87
    faster = 1.0 / h
    check(f'⓶ so at fixed $k$ CR\'s driving rate is larger by {faster:.3f} -- the potential decays about '
          f'{100*(faster-1):.0f}% faster',
          abs(faster - 1.149) < 0.002)
    cr = 2.0 ** faster
    surv = (1/cr) / (1/2.0)
    check(f'and a LCDM decay of 2 becomes {cr:.2f} in CR, so surviving Phi ratio {surv:.3f} and power '
          f'ratio {surv**2:.3f}',
          abs(surv**2 - 0.813) < 0.004)

    # ⓷ the near-coincidence
    damp = float(np.exp(-(1.082**2 - 1)))   # ** RE-PINNED c54.223 (`L-557`) -- was 1.093 **
    # ** ⓷ RESTATED c54.223 (`L-557`), and the restatement is not a widened tolerance. **  At the
    # ** paper's old r = 1.093 the damping ratio was 0.823 and the gap to 0.813 was 0.010 -- close
    # ** enough that this receipt existed to say "different origins, do not conflate".  The corrected
    # ** r = 1.082 puts damping at 0.843, so the gap is 0.030: *** THE CORRECTION MOVED THEM APART. ***
    #   ⇒ ** The warning therefore stands on the ORIGINS argument and no longer needs the numbers to
    #     carry it -- which is the stronger position, and is asserted as such rather than by loosening
    #     the old bound to fit.  Widening a gate to accommodate a number is the r2727 failure. **
    _old_damp = float(np.exp(-(1.093**2 - 1)))        # the paper's r before r2755/c54.223
    check(f'⚠ ⓷ and {surv**2:.3f} sits near the damping ratio {damp:.3f} at $\\ell_D$ -- DIFFERENT '
          f'ORIGINS, named so they are not conflated',
          0.001 < abs(surv**2 - damp) < 0.05)
    check(f'⛭ and the correction WIDENED the coincidence rather than tightening it: the gap was '
          f'{abs(surv**2 - _old_damp):.3f} at r = 1.093 and is {abs(surv**2 - damp):.3f} at r = 1.082 '
          f'-- so the "do not conflate" warning no longer rests on the numbers being close',
          abs(surv**2 - _old_damp) < abs(surv**2 - damp)
          and abs(abs(surv**2 - _old_damp) - 0.010) < 0.002)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT: ** the gap is ~19% down at the peaks -- an ESTIMATE, with its model stated. **')
    print('  ⓵ ** The rate that drives the decay is built from the thing that differs: ** the paper gives')
    print('     k²/(3ℋ) as the rate and ** "the geometric stacking rate near recombination is 13% below the')
    print('     radiation-included one" ** as the difference.')
    print('     ⇒ ** So the decay is NOT common to the two cosmologies. **  At fixed k, CR decays ~15%')
    print('       faster.')
    print('  ⚠ ⓶ ** THE ESTIMATE: ** a ΛCDM decay of 2 becomes 2.22 in CR ⇒ surviving Φ ratio 0.902,')
    print('     ** power ratio 0.813. **')
    print('     ⛔ *** NOT A DERIVATION.  The compounding assumes a decay form the paper does not state.')
    print('       What IS the paper\'s: the rate, the 13%, the factor of two.  A run of the hierarchy')
    print('       would replace this number -- the point is to say what SIZE the gap is, not to fill')
    print('       it. ***')
    print('  ⚠⚠ ⓷ ** A SECOND NEAR-COINCIDENCE, named as r2663 named the first: ** 0.813 at the peaks')
    print('     sits next to ** 0.843 at ℓ_D ** from damping (RE-PINNED c54.223 — was 0.823).  ** Different origins ** -- the potential\'s')
    print('     k²/(3ℋ) decay against exp[-(ℓ/ℓ_D)²(r²-1)].  *** Not one effect; not to be summed as')
    print('     independent either. ***')
    print('  ⇒ ⓸ ** So the deviation is BROAD, not confined to the tail: ** ~7.5% down at low ℓ, ~19% at')
    print('     the peaks, 16% at ℓ_D, 50% at 2ℓ_D.  ** That is where a likelihood confrontation would')
    print('     bite, and it is the first such statement the chain supports. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
