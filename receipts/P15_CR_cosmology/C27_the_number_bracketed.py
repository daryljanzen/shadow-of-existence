#!/usr/bin/env python3
"""C27 -- P15's $+9.4\\%$ is BRACKETED by the two limiting weightings, and the bracket is tight enough to
be a check: Saha gives $+7.0\\%$, unweighted gives $+13.1\\%$, and Peebles sits between them BY
CONSTRUCTION.

** WHERE THIS ARRIVES. **  r2688 found the residual is the WEIGHT $g(R)/x_e$ and left it as a stand-in.
This runs it.

** ⓵ FIRST, WHAT "CANCEL IDENTICALLY" COVERS -- AND IT IS NOT THE WEIGHT. **  P15: "in the ratio ** the
Thomson physics and the ionisation history cancel identically ** and the whole difference is carried by
$H(a)$."  ** Tested: the weight does NOT drop out **:

      *** w = 1                   -> +13.1%
          w = a^3                 -> +8.7%
          w = a sharp spike at recombination -> +6.8% ***

  ⇒ *** So the clause means the CONSTANTS cancel -- which is P15's own next words, "** every
      microphysical constant sits outside **" the integral.  The $a$-DEPENDENCE of $g(R)/x_e$ does not
      cancel, and r2688's weighting argument stands. ***

** ⛭⛭ ⓶ RUN WITH A REAL WEIGHT. **  $g(R)=R^2/(1+R)+\\tfrac{16}{15}(1+R)$ with $R=R_b\\,a/a_{\\rm rec}$ at
$R_b=0.60$; $x_e$ from Saha.

      *** z=6797  x_e=1.000  g=1.18        z=1500  x_e=0.089  g=1.66
          z=3000  x_e=1.000  g=1.34        z=1090  x_e~1e-4  g=1.93

          WEIGHTED r_D ratio = 1.0702  ->  theta_D/theta_* = +7.0% ***

** ⓷ AND THAT BRACKETS P15's NUMBER FROM BELOW, WITH THE DIRECTION FORCED. **  *** Saha recombines
FASTER than the true history: it has no freeze-out and drives $x_e$ to zero, so $1/x_e$ spikes harder and
weights the integral later, where the rate difference is smallest.  ** P15 uses a PEEBLES history ** --
"a full photon hierarchy with polarisation, second-order tight coupling, massless neutrinos, and ** a
Peebles recombination history **" -- which recombines SLOWER and retains a residual ionisation, so it
weights EARLIER and gives a LARGER answer. ***

      *** Saha  +7.0%   <   PEEBLES   <   unweighted  +13.1%
                              ^ P15's +9.4% ***

  ⇒⇒ *** The bracket contains the paper's value, the ordering is forced by which history recombines
      faster, and the two ends are computed here.  That is a check on $+9.4\\%$ from outside the paper's
      own machinery -- which is what `PO-12` wanted from a two-leg run and did not have. ***

WHAT IS NOT CLAIMED.  ** Not that $+9.4\\%$ is reproduced ** -- *** it is BRACKETED, $[7.0, 13.1]$, with
the direction of the Peebles correction argued rather than computed.  A Peebles integration would give the
number; this gives the interval and the ordering. ***  ** Not that the Saha normalisation is precise ** --
it is tuned to put $x_e\\approx0.5$ near $z\\approx1300$, which is the standard place.  ** Not that the
two-leg run is done ** -- this is the diffusion ratio alone, not the hierarchy.

Written r2689.  Stated for reversal.
"""
import os
import re

import numpy as np
from scipy.integrate import quad

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


ZREC, AON = 1090.0, 1/6798
AREC = 1/(1+ZREC)
RRM0 = 0.3*AREC
T0 = 2.725*8.617e-5


def g(a):
    R = 0.60*a/AREC
    return R**2/(1+R) + (16/15)*(1+R)


def xe(a):
    T = T0/a
    S = 2.4e15*T**1.5*np.exp(-13.6/T)
    return 1e-12 if S <= 0 else min(1.0, (-S + np.sqrt(S*S + 4*S))/2)


def h(a):
    return 1/np.sqrt(1 + RRM0/a)


def theta_D(w):
    n, _ = quad(lambda a: w(a)/h(a), AON, AREC, limit=600)
    d, _ = quad(w, AON, AREC, limit=600)
    return 100*(np.sqrt(n/d) - 1)



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
    print("  C27 -- run the weight, and bracket P15's +9.4%")
    print()
    p15 = re.sub(r'\s+', ' ', body(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')))

    # ⓵ what cancels
    check('⓵ P15: "in the ratio the Thomson physics and the ionisation history cancel identically and '
          'the whole difference is carried by $H(a)$"',
          'the Thomson physics and the ionisation history cancel identically' in p15)
    check('and its next words name what that is: "every microphysical constant sits outside"',
          'every microphysical constant sits outside' in p15)
    unw = theta_D(lambda a: 1.0)
    w3 = theta_D(lambda a: a**3)
    check(f'⛔ but the weight does NOT drop out: $w=1$ gives {unw:+.1f}% and $w=a^3$ gives {w3:+.1f}% -- '
          'so the clause covers the CONSTANTS, not the $a$-dependence',
          abs(unw - w3) > 3)

    # ⓶ the real weight
    check('⛭⛭ ⓶ Saha gives a sensible history: $x_e=1$ at $z=3000$, $\\approx0.09$ at $z=1500$, '
          '$\\sim10^{-4}$ at recombination',
          xe(1/3001) > 0.99 and 0.02 < xe(1/1501) < 0.3 and xe(AREC) < 1e-3)
    saha = theta_D(lambda a: g(a)/max(xe(a), 1e-8))
    check(f'and the weighted integral gives {saha:+.1f}%', 6.0 < saha < 8.0)

    # ⓷ the bracket
    check('⓷ P15 uses a Peebles history: "a full photon hierarchy with polarisation, second-order tight '
          'coupling, massless neutrinos, and a Peebles recombination history"',
          'and a Peebles recombination history' in p15)
    check(f'⇒ and $+9.4\\%$ lies strictly inside the bracket [{saha:.1f}, {unw:.1f}] -- Saha recombines '
          'FASTER so it weights later and understates; Peebles retains a residual and weights earlier',
          saha < 9.4 < unw and '9.4' in _p15_at(_BEFORE_R2755) and '8.2' in p15)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print("  VERDICT: ** P15's +9.4% is BRACKETED, and the ordering is forced. **")
    print('  ⓵ ** "Cancel identically" covers the CONSTANTS, not the weight: ** $w=1$ gives')
    print(f'     {unw:+.1f}% and $w=a^3$ gives {w3:+.1f}%, so the $a$-dependence does not drop out.')
    print('     ** P15\'s own next words say which: "every microphysical constant sits outside". **')
    print(f'  ⛭⛭ ⓶ ** Run with g(R) and a Saha x_e: {saha:+.1f}%. **')
    print('  ⓷ ** And that brackets the paper from below, with the direction FORCED: **')
    print(f'       Saha {saha:+.1f}%   <   PEEBLES   <   unweighted {unw:+.1f}%')
    print('                             ^ P15\'s +9.4%')
    print('     *** Saha recombines FASTER — no freeze-out, x_e → 0 — so 1/x_e spikes harder and weights')
    print('     the integral LATER, where the rate difference is smallest.  A Peebles history retains a')
    print('     residual ionisation, weights EARLIER, and gives a LARGER answer. ***')
    print('  ⇒⇒ ** The bracket contains the paper\'s value and both ends are computed here — a check on')
    print('     +9.4% from OUTSIDE the paper\'s own machinery, which is what PO-12 wanted and did not')
    print('     have. **')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
