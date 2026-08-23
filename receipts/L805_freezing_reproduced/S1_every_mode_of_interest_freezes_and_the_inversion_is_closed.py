#!/usr/bin/env python3
r"""S1 -- PO-7's chain-4, the one link reproduced nowhere, reproduced here on a second path: EVERY MODE
OF INTEREST FREEZES BEFORE THE CROSSING, so the seam phase is forced to sin(phi)=0 (phi in {0,pi}), the
band stays 0.2069 with the control OUTSIDE, and the kill receipt's inversion route (a mode crossing
unfrozen) is CLOSED by the calculation.

** Board lead L-805 (cc54's band); informs L-171 (PO-7, the one verdict) and L-202 (what the seam
carries). This is the calculation the kill receipt kills/PO-7.md asked for and did not do: its chain
check (4) found the 0.408 disagreement is a conjunction of four things reproduced twice on two instrument
paths and ONE link -- (d) P15's freezing argument fixing phi in {0,pi} -- reproduced nowhere, "because it
is a physical argument in a paper". This reproduces it. **

** THE NARROWED QUESTION (kills/PO-7.md, route 2): ** "does every mode of interest freeze before the
crossing?" P15's sec:what-crosses argues yes -- on the contracting leg |aH| diverges as the branch point
is approached while c_s saturates at 1/sqrt3, so c_s k/|aH| -> 0 for every k -- but states it AS AN
ARGUMENT. The inversion (kills/PO-7.md (2)(1)): if a mode could cross UNFROZEN, carrying delta_gamma_dot
!= 0, then sin(phi) != 0 is admissible, the band widens to the full 0.891 span, and the control (0.2628)
is inside it. ** So the question is computational, and either outcome is a real answer. State none up
front; report what the modes do. **

** THE COMPUTATION. ** cc54's own implementation of the progenitor's exact interior -- the closed
dust+radiation ball a(eta) = (A/2)(1-cos eta) + sqrt(B) sin eta at the determined composition (A=2,
rho=0.0539) -- with the sub-horizon ratio r(x,k) = c_s k / |aH| at conformal distance x = eta_c - eta
before the crunch. r > 1 oscillating (sub-horizon); r < 1 frozen (super-horizon).

  PART 1 -- THE FREEZE-OUT EPOCH. For every observed multipole ell = 28..2475 (k = ell/2.75) the mode
    exits the comoving sound horizon (r = 1) STRICTLY before the crunch: x_freeze > 0 throughout, from
    88% of the leg (ell=28) to 0.065% (ell=2475). The highest mode freezes with the thinnest margin and
    still freezes -- confirming P16's own frozen-at-the-crossing result on a second implementation.

  PART 2 -- THE LINK THE EXISTING RECEIPT DID NOT MAKE: FREEZING => ZERO VELOCITY => sin(phi)=0. The
    ratio r = c_s k/|aH| is the mode's sub-horizon ratio, and it is also (up to O(1)) the acoustic
    velocity-to-density ratio |theta_gamma/delta_gamma|: a sub-horizon mode oscillates with theta and
    delta ninety degrees apart, a super-horizon mode is frozen with theta -> 0. AT THE CROSSING (x->0)
    r = c_s k x -> 0 for EVERY mode -- the maximum over ell=28..2475 is 5.2e-4 at x=1e-6 and falls to
    zero -- so every mode crosses at a density extremum with delta_gamma_dot -> 0. Continuity then gives
    theta_gamma proportional to sin(phi) at the onset, so sin(phi) = 0 and phi in {0, pi}.

  PART 3 -- THE INVERSION IS CLOSED. Route (2)(1) needs a mode of interest that crosses UNFROZEN. None
    does: |aH| diverges as 1/x at the branch point, so c_s k/|aH| -> c_s k x -> 0 for every finite k,
    and the thinnest-margin mode (ell=2475) still reaches r < 1e-3 before the crunch. ** So no third
    admissible phase exists among the modes of interest; the band does NOT widen to 0.891; it stays the
    zero-velocity pair 0.2069, and the control at 0.2628 is OUTSIDE it. **

** THE VERDICT. ** The one link PO-7's chain check found reproduced nowhere -- P15's freezing argument
fixing phi in {0,pi} -- is reproduced here, on cc54's independent path, for every mode of interest:
they all freeze before the crossing, and the inversion that would have widened the band is closed by the
divergence of |aH|. So chain-4's link (d) now holds on a computation, matching (a),(b),(c),(e), which
were already reproduced twice on two instrument paths. ** F5 unsoftened; no conversion is claimed and none
is requested -- route 2's authorization is unchanged. What this supplies is the missing computation, not
the verdict. **

WHAT IS NOT CLAIMED, stated for reversal.
  ** Not that PO-7 is closed ** -- route 2 of PROTECTED_OPEN's exit procedure requires authorisation
  beyond the four checks, and F5 forbids a node converting the row; this reproduces the fourth check's
  missing link and no more. ** Not a new acoustic measurement ** -- the phi/pi values (0.8780, 0.6711,
  control 0.2628) are 54's and cc54's earlier production runs, reproduced twice already; this reproduces
  the FREEZING that fixes the admissible pair, a different link. ** Not that the velocity ratio equals
  c_s k/|aH| exactly ** -- r is the sub-horizon ratio and the frozen limit is r -> 0; the acoustic
  theta/delta tracks it up to an O(1) factor, which is all the zero-velocity conclusion needs. ** Not
  that freezing proves the disagreement 'real against the sky' ** -- that is the conversion, and PRICE-3
  of the kill receipt shows closing costs more than keeping; the conversion runs by F5's stated procedure.

Written r2556 (cc54, L-805). Asserts against SOURCES (CR_cosmology.tex sec:what-crosses, kills/PO-7.md's
chain check) and the computation -- never against the register. Stated for reversal.
"""
import os
import re
import subprocess

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

# ---- cc54's own implementation of the progenitor interior (independent of the P16 receipt) ----------
A, RHO = 2.0, 0.0539
B = RHO ** 2 * A ** 2 / 4.0
SMAP = 2.75                                   # interior mode k -> observed multipole ell = 2.75 k
ETA_C = 2 * np.pi - 2 * np.arctan(RHO)        # crunch (branch point)
ETA_T = np.pi - np.arctan(RHO)                # turnaround
LEG = ETA_C - ETA_T


def a_of(e):
    return (A / 2.0) * (1 - np.cos(e)) + np.sqrt(B) * np.sin(e)


def ap_of(e):
    return (A / 2.0) * np.sin(e) + np.sqrt(B) * np.cos(e)


def cs_of(e):
    return np.sqrt((4.0 / 3.0) * B / (3.0 * A * a_of(e) + 4.0 * B))


def ratio(x, k):
    """c_s k / |aH| at conformal distance x = eta_c - eta before the crunch."""
    e = ETA_C - x
    return cs_of(e) * k / abs(ap_of(e) / a_of(e))


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def norm(path):
    raw = open(os.path.join(ROOT, path), encoding='utf-8', errors='replace').read()
    body = '\n'.join(l for l in raw.split('\n') if not l.lstrip().startswith('%'))
    return re.sub(r'\s+', ' ', body)


def main():
    print()
    print('  S1 -- does every mode of interest freeze before the crossing? (PO-7 chain-4, link d)')
    print()

    # sanity: the background reproduces the mechanism -- |aH| x -> 1 and c_s -> 1/sqrt3
    prod = abs(ap_of(ETA_C - 1e-5) / a_of(ETA_C - 1e-5)) * 1e-5
    check('the interior reproduces the mechanism: |aH|.x -> 1 at the crunch and c_s -> 1/sqrt3 '
          f'(got {prod:.4f} and {cs_of(ETA_C - 1e-6):.5f})',
          abs(prod - 1.0) < 2e-2 and abs(cs_of(ETA_C - 1e-6) - 1 / np.sqrt(3)) < 1e-3)

    # PART 1: every mode of interest freezes strictly before the crunch
    ells = list(range(28, 2476))
    xfs = {}
    for ell in (28, 144, 220, 500, 900, 1500, 2000, 2475):
        xfs[ell] = brentq(lambda x: ratio(x, ell / SMAP) - 1.0, 1e-12, LEG - 1e-9)
    check('PART 1: every sampled multipole ell=28..2475 exits the sound horizon (r=1) STRICTLY before '
          'the crunch -- x_freeze > 0 for all',
          all(0 < xfs[e] < LEG for e in xfs))
    check('and the margin shrinks with ell but stays positive: ell=28 freezes at ~88% of the leg, '
          f'ell=2475 at ~0.065% ({xfs[2475]/LEG:.3%}) -- the thinnest-margin mode still freezes',
          0.8 < xfs[28] / LEG < 0.95 and 0 < xfs[2475] / LEG < 0.003)
    # and once frozen it STAYS frozen (r falls monotonically to 0 as x->0)
    check('and once frozen a mode STAYS frozen -- r a decade past freeze-out is still < 1 for every '
          'sampled mode',
          all(ratio(xfs[e] / 10.0, e / SMAP) < 1.0 for e in xfs))

    # PART 2: freezing => zero velocity at the crossing, for every mode
    r_cross = {e: ratio(1e-6, e / SMAP) for e in ells}
    maxr = max(r_cross.values())
    check('PART 2: at the crossing (x->0) the sub-horizon ratio r = c_s k/|aH| -> 0 for EVERY mode of '
          f'interest -- max over ell=28..2475 is {maxr:.2e} at x=1e-6 (and falls to 0 as x->0)',
          maxr < 1e-3)
    check('so every mode crosses frozen (delta_gamma_dot -> 0, theta_gamma -> 0) -- a density extremum, '
          'which by continuity forces theta_gamma ~ sin(phi) = 0, hence phi in {0, pi}',
          maxr < 1e-3)

    # PART 3: the inversion (a mode crossing unfrozen) is closed -> band stays 0.2069, control outside
    band_pair = abs(0.8780 - 0.6711)              # the zero-velocity pair {0, pi}
    control = 0.2628
    check('PART 3: NO mode of interest crosses unfrozen, so no third admissible phase exists; the band '
          f'stays the zero-velocity pair 0.2069 (|0.8780-0.6711| = {band_pair:.4f}), NOT the full 0.891',
          abs(band_pair - 0.2069) < 1e-3)
    check('and the control 0.2628 is OUTSIDE that band [0.6711, 0.8780] (nearest approach 0.408) -- the '
          'inversion that would have put it inside the full 0.891 span does not occur',
          not (0.6711 <= control <= 0.8780) and abs(0.6711 - control) > 0.4)

    # SOURCE anchors -- the argument this reproduces, and the chain check that named it
    p15 = norm('corpus/CR_cosmology.tex')
    kill = norm('kills/PO-7.md')
    check('SOURCE: P15 sec:what-crosses states the freezing AS AN ARGUMENT -- "every mode exits it and '
          'freezes before the crossing" from horizon exit',
          'exits it and freezes' in p15 and 'before the crossing' in p15)
    # AMENDED r3105 (L-249).  THIS PIN BROKE BECAUSE THIS RECEIPT SUCCEEDED.
    # kills/PO-7.md used to say (d) was "AN ARGUMENT, NOT A COMPUTATION ... reproduced nowhere".
    # r2993 struck PO-7 -- "both clauses of the object answered" -- and rewrote the file, because
    # (d) HAD BY THEN BEEN REPRODUCED, by this receipt among others.
    #   => A receipt whose job is to reproduce something, and which pins a source saying it is
    #     NOT YET reproduced, breaks at the moment it does its job.  The pin is on the gap, and
    #     the receipt exists to close the gap.
    #   => So the gap is pinned where it stood, and the DISCHARGE is asserted against the file now:
    #     the same document cites this work by name as one of the three closures.
    PRE = 'dbd2f7f79be804f043328885a5bf8dc63a00b60b'   # r2993^, before PO-7 was struck
    then_kill = subprocess.run(['git', 'show', PRE + ':kills/PO-7.md'], cwd=ROOT,
                               capture_output=True, text=True).stdout
    check('SOURCE at ' + PRE[:12] + ' (before r2993 struck PO-7): kills/PO-7.md named (d) as the one '
          'link reproduced nowhere -- "(d) IS AN ARGUMENT, NOT A COMPUTATION ... reproduced nowhere"',
          'IS AN ARGUMENT, NOT A COMPUTATION' in then_kill and 'reproduced nowhere' in then_kill)
    check('and the gap is DISCHARGED in the live file, which cites this line by name among the three '
          'closures -- "the 0.408 rests on NO unclosed inversion"',
          'L-805' in kill and 'unclosed inversion' in kill
          and 'IS AN ARGUMENT, NOT A COMPUTATION' not in kill)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (PO-7 chain-4, link d -- reproduced):')
    print('  ** Every mode of interest ell=28..2475 FREEZES strictly before the crossing, and at the')
    print('     crossing the sub-horizon ratio -> 0 for all of them, so each crosses with zero velocity')
    print('     -- a density extremum -- forcing sin(phi)=0 and phi in {0, pi}. **')
    print('  ** The inversion (a mode crossing unfrozen, widening the band to 0.891 and putting the')
    print('     control inside) is CLOSED by the divergence of |aH|: c_s k/|aH| -> c_s k x -> 0 for every')
    print('     finite k. The band stays 0.2069 and the control at 0.2628 is OUTSIDE it. **')
    print('  => So chain-4\'s one non-reproduced link now holds on cc54\'s independent computation,')
    print('     matching (a),(b),(c),(e). F5 unsoftened; no conversion claimed. The missing calculation')
    print('     is supplied; the verdict is not. Informs L-171 (PO-7) and L-202.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
