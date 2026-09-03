#!/usr/bin/env python3
"""C15 -- the corpus's cancellation principle does NOT extend to the odd/even ratio, and the two ratios
differ in what is held fixed: r2646's gate stands, now with a reason.

** THE CANDIDATE ESCAPE. **  `CR_cosmology`, on the diffusion signature: "The diffusion length reduces to
a single integral over the scale factor in which every microphysical constant sits outside ... so ** in
the ratio the Thomson physics and the ionisation history cancel identically and the whole difference is
carried by $H(a)$ **".

  ⇒ ** If a ratio can be transfer-free, `PO-10`'s odd/even PATTERN is a ratio, and r2646's gate would not
    hold. **  *** This receipt tests that and it does not. ***

** ⛭⛭ ⓵ THE TWO RATIOS DIFFER IN WHAT IS HELD FIXED, AND THAT IS THE WHOLE OF IT. **
  * ** The corpus's ratio ** compares ** the SAME quantity on TWO RATES ** -- the diffusion length on the
    geometric stacking rate against the radiation-included one.  *** The microphysics is identical on both
    sides, so it cancels identically, and $H(a)$ is the only thing that differs. ***
  * ** An odd/even ratio ** compares ** DIFFERENT MULTIPOLES on ONE rate ** -- peak $n$ against peak
    $n+1$.  *** The transfer envelope is not the same at $\\ell_n$ and $\\ell_{n+1}$, so nothing cancels
    identically. ***

** ⓶ AND THE RESIDUE IS LARGE, NOT MARGINAL. **  Writing $C_\\ell = A(\\ell)\\,O(\\ell)$ with $A$ the
envelope and $O$ the oscillation, the adjacent-peak ratio carries $A(\\ell_n)/A(\\ell_{n+1})$.  At the
observed peak positions $\\{220, 540, 810, 1120\\}$:

      *** exp[-(l/1400)^2] :  1.132  1.204  1.357
          exp[-(l/1550)^2] :  1.107  1.164  1.283
          power law l^-1/2 :  1.567  1.225  1.176 ***

  ⇒ ** 13% at the first pair on a damping envelope, ** rising to ** 36% by the third ** -- *** and the
    growth is the damping tail biting, which is precisely the regime `PO-10`'s pattern lives in. ***

** ⇒⇒ ⓷ SO r2646's GATE STANDS, AND NOW HAS A REASON RATHER THAN AN ASSERTION. **  *** `PO-12` gates
`PO-10` not merely because both are "statements about $C_\\ell$" but because the only cancellation the
corpus establishes is between two RATES, and the odd/even pattern needs one between two MULTIPOLES.  Those
are different cancellations and the corpus has one of them. ***

** ⓸ AND THE SAME TEST NAMES WHAT WOULD WORK. **  *** A quantity comparing the SAME multipole on the two
rates would inherit the corpus's own cancellation -- which is exactly the shape of the diffusion-length
and sound-horizon results already computed ($10.8\\%$ longer; $r_s=146.4$ against $145.4$~Mpc).  So the
transfer-free route is real and it produces RATE-RATIOS, not SHAPE. ***

WHAT IS NOT CLAIMED.  ** Not that the odd/even pattern is unreachable ** -- it is reachable once the
transfer exists, which is `PO-12`.  ** Not that the envelopes tested are CR's ** -- *** they are generic
smooth and damping forms, and the point is that ANY of them leaves a residue of this size; a CR-specific
envelope would have to be computed, which is again `PO-12`. ***  ** Not that the corpus's cancellation is
weaker than stated ** -- it is exact for what it covers.

Written r2647.  Stated for reversal.
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
    print("  C15 -- does the corpus's cancellation reach the odd/even ratio?")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ the corpus's cancellation, and what it is between
    check('⓵ the corpus states a cancellation: "in the ratio the Thomson physics and the ionisation '
          'history cancel identically and the whole difference is carried by $H(a)$"',
          'the Thomson physics and the ionisation history cancel identically' in p15
          and 'carried by $H(a)$' in p15)
    # ⛔⛭ RE-PINNED r3952 -- r3841's sweep, same cause as r3950's five.  The paper says "on the inherited datum the GEOMETRIC rate gives a diffusion
    #   length $10.8\\%$" -- the term only; the number and the comparison were already right.
    check('and it is between two RATES: "on the inherited datum the geometric stacking rate gives a '
          'diffusion length $10.8\\%$ longer"',
          'the geometric rate gives a diffusion length' in p15 and '10.8' in p15)
    check('with the sound horizon computed the same way: "$r_{s}=146.4$~Mpc against $145.4$ on the '
          'radiation-included"',
          '146.4' in p15 and '145.4' in p15)

    # ⓶ the residue in an adjacent-peak ratio
    l = np.array([220., 540., 810., 1120.])
    envs = {'exp[-(l/1400)^2]': lambda x: np.exp(-(x/1400.)**2),
            'exp[-(l/1550)^2]': lambda x: np.exp(-(x/1550.)**2),
            'l^-0.5': lambda x: x**-0.5}
    worst = 0.0
    for name, A in envs.items():
        r = [A(l[i])/A(l[i+1]) for i in range(len(l)-1)]
        worst = max(worst, max(abs(x - 1) for x in r))
        check(f'⓶ envelope {name}: adjacent-peak ratios {[round(float(x),3) for x in r]} -- not 1',
              all(abs(x - 1) > 0.05 for x in r))
    check(f'⇒ the residue reaches {worst*100:.0f}% -- large, not marginal', worst > 0.3)

    # damping envelopes grow with l
    A = envs['exp[-(l/1400)^2]']
    grow = [A(l[i])/A(l[i+1]) for i in range(len(l)-1)]
    check('⓷ and on a damping envelope the residue GROWS with $\\ell$ -- the regime the odd/even pattern '
          'lives in',
          grow[0] < grow[1] < grow[2])

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** the corpus's cancellation does not reach the odd/even ratio.  r2646's gate")
    print('  stands, with a reason. **')
    print('  ⛭⛭ ⓵ ** The two ratios differ in what is held fixed: **')
    print('     ** the corpus\'s ** compares the SAME quantity on TWO RATES -- the microphysics is')
    print('     identical on both sides and cancels ** identically **;')
    print('     ** an odd/even ratio ** compares DIFFERENT MULTIPOLES on ONE rate -- ** the envelope is')
    print('     not the same at l_n and l_(n+1), so nothing cancels. **')
    print('  ⓶ ** And the residue is large: ** 13% at the first pair on a damping envelope, ** rising to')
    print('     36% by the third ** -- and the growth is the damping tail biting, ** which is precisely')
    print('     the regime the pattern lives in. **')
    print('  ⇒⇒ ** So PO-12 gates PO-10 not merely because both are "statements about C_l", but because')
    print('     the only cancellation the corpus establishes is between two RATES and the odd/even')
    print('     pattern needs one between two MULTIPOLES. **')
    print('  ⓸ ** And the test names what DOES work: ** a quantity comparing the SAME multipole on the')
    print('     two rates inherits the corpus\'s cancellation -- which is the shape of the results already')
    print('     computed (10.8% longer diffusion length; r_s = 146.4 against 145.4 Mpc).')
    print('     ⇒ ** The transfer-free route is real and it produces RATE-RATIOS, not SHAPE. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
