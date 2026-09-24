#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE DRIVING SUBTRACTION ON THE ADJUDICATED ARM IS 0.96x THE CONTROL'S, WHERE
`sec:refit-bound`'s PINNED ARM WAS 2.48x. ** THE ANOMALOUS DRIVING BELONGED TO THE PIN AND NOT TO
THE CONSTRUCTION. **

** ⇒ AND IT IS PATH-PROOF: the two instrument paths agree to four decimals (0.1717 both), unlike
the heights. **  *That matters because it is the one thing in this family that has been
path-dependent, and this quantity is not.*

Built r6760+cc66.15 (node 66, code seat), on `PO-13`, at node 66 (chat seat)'s routed item in
`FOR_CC66`: "removing every coupling to the potential on the crossing arm at (68.60, 0.2973), both
paths, reporting the first peak, ell_1/ell_A and the shift against the control's."

===================================================================================================
** WHAT THE PARAGRAPH SAID, AND WHY ITS NUMBERS ARE OUT **
===================================================================================================

`sec:refit-bound`'s driving-subtraction paragraph carried the PINNED arm: first peak 206 -> 340,
ell_1/ell_A 0.6830 -> 1.1273, ** 2.4 times the control's shift **.  *That configuration is the one
r6760+cc66.7 retired -- the pin and the crossing are disjoint by ordering -- so the paragraph now
points at a measurement the corpus does not have.*  ** This is that measurement. **

** THE CONVENTION, STATED BECAUSE IT IS EASY TO GET WRONG AND THE ANSWER MOVES WITH IT. **
ell_1/ell_A here is the first peak over the arm's ** REPORTED ** l_A = pi D_M / r_s, which is what
the instrument's own header prints -- NOT over the comb fitted to the spectrum's peaks.  *On this
arm those are 302.9 and 298.0, so the two conventions give 0.7329 and 0.7450 for the same run.*
** The chat seat's control figure reproduces on the reported-l_A convention and not on the other,
which is how it was identified. **

  PART 1  ** THE FOUR ROWS. **
  PART 2  ** THE RATIO, WHICH IS WHAT THE PARAGRAPH IS ABOUT. **
  PART 3  ** BOTH PATHS. **
  PART 4  ** AND A TWO-MULTIPOLE DIFFERENCE FROM THE QUOTED CONTROL, PRICED. **

** COMPUTES: nothing.  *** It reads spectra already produced and locates their peaks.  The runs are
   `ARM=cr CRH0=68.60 CROM=0.2973 ZSTART=3e7 LEAFSCALES=1 [NODRIVE=1] LSTEP=2 LMAXL=1300` with
   `HIER=1` for the polarisation path and absent for the fluid, and `ARM=lcdm [NODRIVE=1]` for the
   control.  `NODRIVE=1` sets DRC = DRE = 0, which is every coupling of the potential into the
   fluid; Phi's own evolution is never switched, since removing it would change the background
   rather than the driving. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~5 s; reads spectra/cc66_*.npz)
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')

# sec:refit-bound's pinned-arm row, quoted so the comparison is against the paper and not a memory
PIN_DRIVEN, PIN_UNDRIVEN = 206.0, 340.0
PIN_RATIO_D, PIN_RATIO_U = 0.6830, 1.1273
CHAT_CONTROL_UNDRIVEN, CHAT_CONTROL_SHIFT = 276.0, 0.1858


def peak1(tag):
    z = np.load(os.path.join(SPEC, f'cc66_{tag}.npz'))
    ls, Dl = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    q = argrelextrema(Dl, np.greater, order=3)[0]
    return float(ls[q[0]]), float(z['l_A'])


ROWS = [
    ('control (LCDM), POLARISATION', 'lcdm', 'lcdm_nodrive_pol'),
    ('CR arm 68.60, POLARISATION', 'cr_x_h686_pol', 'cr_x_h686_nodrive_pol'),
    ('CR arm 68.60, FLUID', 'cr_x_h686_fluid', 'cr_x_h686_nodrive_fluid'),
]

print("=" * 104)
print("  PART 1 -- ** THE FOUR ROWS **   (ell_1/l_A on the REPORTED l_A, the instrument's own)")
print("=" * 104)
print(f"  {'configuration':>30} {'l_A rep':>8} {'l_1 driven':>11} {'undriven':>9} {'shift':>6} "
      f"{'l1/lA driven':>13} {'undriven':>9} {'d(l1/lA)':>9}")
R = {}
for nm, td, tu in ROWS:
    p_d, lA = peak1(td)
    p_u, lA_u = peak1(tu)
    if abs(lA - lA_u) > 0.2:
        fail.append(f"{nm}: driven and undriven report different l_A ({lA} vs {lA_u})")
    a, b = p_d / lA, p_u / lA
    R[nm] = dict(lA=lA, d=p_d, u=p_u, ra=a, rb=b, shift=b - a)
    print(f"  {nm:>30} {lA:>8.1f} {p_d:>11.0f} {p_u:>9.0f} {p_u - p_d:>6.0f} "
          f"{a:>13.4f} {b:>9.4f} {b - a:>9.4f}")
print(f"  {'the PINNED arm (sec:refit-bound)':>30} {301.6:>8.1f} {PIN_DRIVEN:>11.0f} "
      f"{PIN_UNDRIVEN:>9.0f} {PIN_UNDRIVEN - PIN_DRIVEN:>6.0f} {PIN_RATIO_D:>13.4f} "
      f"{PIN_RATIO_U:>9.4f} {PIN_RATIO_U - PIN_RATIO_D:>9.4f}")

CTL = R['control (LCDM), POLARISATION']
ARM = R['CR arm 68.60, POLARISATION']
ARMF = R['CR arm 68.60, FLUID']

print()
print("=" * 104)
print("  PART 2 -- ** THE RATIO, WHICH IS WHAT THE PARAGRAPH IS ABOUT **")
print("=" * 104)
r_arm = ARM['shift'] / CTL['shift']
r_pin = (PIN_RATIO_U - PIN_RATIO_D) / CTL['shift']
print(f"  {'':>36} {'shift':>9} {'vs the control':>16}")
print(f"  {'the control itself':>36} {CTL['shift']:>9.4f} {1.0:>15.2f}x")
print(f"  {'the ADJUDICATED arm (crossing, 68.60)':>36} {ARM['shift']:>9.4f} {r_arm:>15.2f}x")
print(f"  {'the PINNED arm (the paragraph)':>36} {PIN_RATIO_U - PIN_RATIO_D:>9.4f} {r_pin:>15.2f}x")
print(f"""
  ⇒ *** THE ANOMALOUS DRIVING BELONGED TO THE PIN. ***  On the adjudicated arm the potential's grip
  on the oscillator is within {abs(r_arm - 1) * 100:.0f}% of the control's, and SLIGHTLY WEAKER rather than
  stronger.  *`sec:refit-bound`'s paragraph was reporting a property of the pinned configuration,
  not of the construction, and its 2.4x does not survive the configuration change.*

  ⚠ ** WHAT THIS DOES NOT SAY. **  A smaller driving shift is not evidence the arm is RIGHT -- it
  says the arm's driving now behaves like the control's, which REMOVES a discrepancy rather than
  adding a confirmation.  *The phase residual this is to be read against is still 2.3%
  (r6760+cc66.7), and nothing here touches it.*""")
if r_arm > 1.15 or r_arm < 0.85:
    fail.append(f"the adjudicated arm's shift is {r_arm:.2f}x the control's, not near parity")
if r_pin < 2.0:
    fail.append(f"the pinned arm's shift is {r_pin:.2f}x here, not the ~2.4x sec:refit-bound quotes")

print()
print("=" * 104)
print("  PART 3 -- ** BOTH PATHS, AND THIS ONE IS PATH-PROOF **")
print("=" * 104)
print(f"  {'polarisation':>16} {ARM['shift']:>9.4f}")
print(f"  {'fluid':>16} {ARMF['shift']:>9.4f}")
print(f"  {'difference':>16} {abs(ARM['shift'] - ARMF['shift']):>9.4f}")
print(f"""
  ⇒ ** The two paths agree to {abs(ARM['shift'] - ARMF['shift']):.4f}. **  *That is worth stating because the HEIGHTS on
  this instrument are path-dependent and have had to be reported as polarisation-path specific
  throughout (r6760+cc66.7, r6760+cc66.10).  **This quantity is not: the driving shift is the
  construction's and not the path's.***""")
if abs(ARM['shift'] - ARMF['shift']) > 0.005:
    fail.append("the two paths do not agree -- PART 3's claim is wrong")

print()
print("=" * 104)
print("  PART 4 -- ** THE QUOTED CONTROL AND THIS ONE DIFFER BY TWO MULTIPOLES **")
print("=" * 104)
print(f"  the chat seat's control:  l_1 undriven {CHAT_CONTROL_UNDRIVEN:.0f}, "
      f"shift {CHAT_CONTROL_SHIFT:.4f}")
print(f"  this tree's control:      l_1 undriven {CTL['u']:.0f}, shift {CTL['shift']:.4f}")
print(f"""
  ** {abs(CTL['u'] - CHAT_CONTROL_UNDRIVEN):.0f} multipoles, which is ONE GRID STEP at LSTEP=2 -- so it is resolution and
  not substance. **  *But it moves the quoted shift {CHAT_CONTROL_SHIFT:.4f} -> {CTL['shift']:.4f}, and with it the
  arm's ratio from {(PIN_RATIO_U - PIN_RATIO_D) / CHAT_CONTROL_SHIFT:.2f}x -> {r_pin:.2f}x for the pinned arm and
  {ARM['shift'] / CHAT_CONTROL_SHIFT:.2f}x -> {r_arm:.2f}x for the adjudicated one.*
  ⇒ *** Both are reported so the size of the difference is visible, and the ratios above are on
  THIS tree's control throughout rather than mixing a measured shift against a quoted one. ***""")
if abs(CTL['u'] - CHAT_CONTROL_UNDRIVEN) > 4:
    fail.append(f"this control's undriven peak is {CTL['u']:.0f} against the quoted "
                f"{CHAT_CONTROL_UNDRIVEN:.0f} -- more than a grid step, so not resolution")

print()
print("=" * 104)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 104)
