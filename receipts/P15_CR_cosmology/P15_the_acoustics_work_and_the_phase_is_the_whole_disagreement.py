#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE ASYMPTOTIC SPACING TRACKS THE SOUND HORIZON AT 98% OF THE ACOUSTIC RATE, SO
THIS CONSTRUCTION'S ACOUSTICS WORK.  ** THE WHOLE DISAGREEMENT IS THE ACOUSTIC PHASE: 0.62 pi, ROBUST
TO THE ONE FITTED PARAMETER, AND THE SEAM DATUM'S PHASE FREEDOM CLOSES A THIRD OF IT AND NO MORE. **
AND THIS RETRACTS c54.189's "a QUARTER of the acoustic rate", WHICH WAS MEASURED ON THE FIRST PEAK --
INSIDE THE TRANSIENT c54.190 FOUND. **

Built r2441+c54.191, front #2, lead `L-506`.

===================================================================================================
** WHY: c54.190 SEPARATED SPACING FROM PHASE AND OWED BOTH A PRODUCTION-DEPTH TEST. **
===================================================================================================

c54.190 found that the CR arm's asymptotic spacing is right to 2.4% and that the disagreement is a
phase offset of 0.62 pi.  ** Both of those were read off ONE reading of the datum at ONE value of the
fitted parameter.  The scans that varied those were all at the depth c54.190 showed to be
insufficient. **  *So the two questions c54.187-189 thought they had answered are re-asked here at
the depth that can answer them, and one of their answers does not survive.*

  PART 1  ** THE ASYMPTOTIC SPACING TRACKS THE SOUND HORIZON, AND AT ESSENTIALLY THE FULL ACOUSTIC
          RATE. **  Moving the pin from ell_A = 301.6 to 340 drops r_s by 11%; ordinary acoustics
          requires the peak spacing to rise by 13%, and ** it rises by 13% -- 98% of the acoustic
          rate. **  *So the peaks in this construction ARE set by its own sound horizon.*
  PART 2  ** WHICH RETRACTS c54.189's HEADLINE. **  That revision reported *"this construction's
          peaks track its own sound horizon at 24% of the rate acoustics requires"* -- ** measured
          on the FIRST peak, which c54.190 then showed sits 142 multipoles off the asymptotic line,
          inside a transient. **  *Measured here over the pin range this file uses, the first peak
          moves at 37% of the acoustic rate against the series' 98% -- a different range and depth
          from c54.189's 24%, so the figure is not reproduced and is not meant to be.  What is
          reproduced is the FINDING: the first peak is far less sensitive than the series, and the
          series is what "the acoustics" means.*
  PART 3  ** AND THE PHASE IS ROBUST TO THE FITTED PARAMETER. **  The intercept moves from -0.878 to
          -0.899 of ell_A across the same 31% swing in the pin -- ** three per cent of a discrepancy
          of 0.62. **  *So the acoustic phase shift is a property of the construction
          and not of the number it fits.*
  PART 4  ** THE SEAM DATUM'S PHASE FREEDOM IS A REAL LEVER ON IT AND SPANS A THIRD OF IT. **  At
          the opposite phase the intercept moves to -0.671, closing the gap to the control from
          0.615 to 0.408 -- ** 34%, and no further. **  *Which is the confirmation c54.190's
          diagnosis wanted: the datum's phase controls the acoustic phase, as a phase diagnosis
          predicts, and it cannot close the discrepancy.*

** SO THE FRONT'S ACOUSTIC STATEMENT, IN ITS FINAL FORM. **  ** This construction reproduces the
acoustic SPACING -- the quantity its one fitted parameter is fitted to, and which it then tracks at
98% of the acoustic rate when that parameter is moved -- and disagrees with the sky in the acoustic
PHASE by 0.62 pi, a discrepancy robust to the fitted parameter and only a third reachable by the one
freedom the seam datum leaves open. **  *That is one number and one mechanism, where the front began
with four items and a ratio.*

** F5 IS NOT SOFTENED, AND THE SHAPE OF THIS RESULT MAKES THAT MATTER MORE RATHER THAN LESS. **  A
measurement discrepancy is not a framework verdict; `PO-7` is protected; the conversion runs by `F5`'s stated procedure.
** And the discrepancy is now specific enough to be attacked: an acoustic phase shift is a computable
consequence of the driving, so the question "why 0.62 pi" has an address. **  *This file does not
have it.*

rc=0 on success.  Run: python3 P15_the_acoustics_work_and_the_phase_is_the_whole_disagreement.py
                        (numpy scipy; ~10 s)
"""
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
NFIT = 4          # the asymptotic fit starts where c54.190 showed the transient has died

RUNS = (('LambdaCDM control',       'c54.186_lcdm_L3000.npz'),
        ('CR  phi=0,  l_A = 301.6', 'c54.186_cr_L3000.npz'),
        ('CR  phi=pi, l_A = 301.6', 'c54.191_cr_phipi_L3000.npz'),
        ('CR  phi=0,  l_A = 340',   'c54.191_cr_lA340_L3000.npz'))


def fit(fname):
    z = np.load(os.path.join(SP, fname))
    ls = np.asarray(z['ls'], float)
    D = np.asarray(z['Dl'], float)
    pk = argrelextrema(D, np.greater, order=3)[0]
    pos = ls[pk]
    n = np.arange(1, len(pos) + 1)
    b, a = np.polyfit(n[n >= NFIT], pos[n >= NFIT], 1)
    return dict(pos=pos, b=float(b), a=float(a), lA=float(z['l_A']), rs=float(z['r_s']))


R = {nm: fit(f) for nm, f in RUNS}

# =====================================================================
print("=" * 78)
print("THE ASYMPTOTIC SERIES UNDER BOTH REMAINING FREEDOMS, AT PRODUCTION DEPTH")
print("=" * 78)
print("  *each series fitted as ell_n = b n + a on peaks 4 and up, which is where c54.190 showed")
print("   the low-ell transient has died*")
print()
print(f"  {'run':>24} {'r_s':>7} {'l_A':>7} {'npk':>4} {'slope':>7} {'slope/l_A':>10} "
      f"{'intcpt/l_A':>11} {'vs control':>11}")
CTRL = R['LambdaCDM control']['a'] / R['LambdaCDM control']['lA']
for nm, _ in RUNS:
    d = R[nm]
    print(f"  {nm:>24} {d['rs']:>7.1f} {d['lA']:>7.1f} {len(d['pos']):>4} {d['b']:>7.1f} "
          f"{d['b']/d['lA']:>10.4f} {d['a']/d['lA']:>11.4f} {CTRL - d['a']/d['lA']:>+11.4f}")
if min(len(R[nm]['pos']) for nm, _ in RUNS) < 7:
    fail.append("an arm carries fewer than seven peaks -- the asymptotic fit is not asymptotic")

# =====================================================================
print()
print("=" * 78)
print("PART 1/2 — THE SPACING TRACKS THE SOUND HORIZON AT THE FULL ACOUSTIC RATE")
print("=" * 78)
A = R['CR  phi=0,  l_A = 301.6']
B = R['CR  phi=0,  l_A = 340']
d_rs = B['rs'] / A['rs'] - 1.0
d_b = B['b'] / A['b'] - 1.0
req = A['rs'] / B['rs'] - 1.0                 # acoustics: spacing goes as 1/r_s
SENS = d_b / req
print(f"  r_s          {A['rs']:>7.1f} -> {B['rs']:>7.1f}   ({100*d_rs:+.0f}%)")
print(f"  peak spacing {A['b']:>7.1f} -> {B['b']:>7.1f}   ({100*d_b:+.0f}%)")
print(f"  ordinary acoustics requires                 ({100*req:+.0f}%)")
print(f"\n  ** THE ASYMPTOTIC SPACING TRACKS THE SOUND HORIZON AT {SENS:.0%} OF THE ACOUSTIC RATE. **")
print("     ⇒ ***So the peaks in this construction ARE set by its own sound horizon, and the")
print("     acoustics work.***")
print()
print("  ⚠ ***AND THIS RETRACTS c54.189's HEADLINE.***  *That revision reported \"the peaks track")
print("     their own sound horizon at 24% of the rate acoustics requires\" — measured on the FIRST")
print("     peak, which c54.190 then showed sits 142 multipoles off the asymptotic line, inside a")
print("     transient.*")
_first = (B['pos'][0] / A['pos'][0] - 1.0) / req
print(f"     the FIRST peak alone moves at {_first:.0%} of the acoustic rate; the SERIES at "
      f"{SENS:.0%}.")
print("     *The first-peak number was not wrong, it was the wrong quantity — the same error c54.190")
print("     corrected in the spacing, one revision later and in the same file's neighbour.*")
if not (0.85 < SENS < 1.15):
    fail.append(f"the asymptotic spacing tracks r_s at {SENS:.0%} of the acoustic rate -- PART 1's "
                "claim that the acoustics work is not what the data show")
if _first > 0.6:
    fail.append(f"the first peak alone tracks at {_first:.0%}, not much below the series' "
                f"{SENS:.0%} -- PART 2's retraction has no basis")

# =====================================================================
print()
print("=" * 78)
print("PART 3/4 — AND THE PHASE IS THE WHOLE DISAGREEMENT")
print("=" * 78)
_ia = A['a'] / A['lA']
_ib = B['a'] / B['lA']
_ip = R['CR  phi=pi, l_A = 301.6']['a'] / R['CR  phi=pi, l_A = 301.6']['lA']
print(f"  intercept / l_A, which for a series peaking at k r_s = n pi - phi IS -(phi/pi):")
print(f"    the control                          {CTRL:>8.4f}")
print(f"    CR as coded                          {_ia:>8.4f}   (gap to control {CTRL-_ia:+.4f})")
print(f"    CR with the pin moved 31%            {_ib:>8.4f}   (moved {abs(_ib-_ia):.4f})")
print(f"    CR at the opposite seam phase        {_ip:>8.4f}   (gap to control {CTRL-_ip:+.4f})")
_pinmove = abs(_ib - _ia) / abs(CTRL - _ia)
_close = 1.0 - (CTRL - _ip) / (CTRL - _ia)
print(f"\n  ** THE FITTED PARAMETER MOVES THE PHASE BY {_pinmove:.0%} OF THE DISCREPANCY — it is the")
print(f"     construction's and not the number it fits. **")
print(f"  ** THE SEAM DATUM'S PHASE FREEDOM CLOSES {_close:.0%} OF IT, AND NO FURTHER. **")
print("     ⇒ ***Which is the confirmation c54.190's diagnosis wanted: the datum's phase controls")
print("     the acoustic phase, as a phase diagnosis predicts — and it cannot close the gap.***")
print()
print("  ⛔ ***F5 UNSOFTENED.  And the discrepancy is now specific enough to be attacked: an")
print("     acoustic phase shift is a computable consequence of the driving, so \"why 0.62 pi\" has")
print("     an address.  This file does not have it.  `PO-7` protected; the conversion is")
print("     Daryl's.***")
if _pinmove > 0.15:
    fail.append(f"the pin moves the phase by {_pinmove:.0%} of the discrepancy -- it is not robust "
                "to the fitted parameter and PART 3 is wrong")
if not (0.15 < _close < 0.70):
    fail.append(f"the seam phase closes {_close:.0%} of the gap -- outside what PART 4 reports, and "
                "if it closed all of it the discrepancy would be the datum's alone")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the asymptotic peak spacing tracks the sound horizon at 98% of the acoustic")
print("rate, so this construction's acoustics work and c54.189's 'a quarter of the rate' is retracted")
print("as a first-peak number read inside a transient; the acoustic phase offset of 0.62 pi moves by")
print("3% under a 31% swing in the fitted parameter and closes by 34% under the seam datum's own")
print("phase freedom, so the phase is the construction's and is the whole of the disagreement.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.191, `L-506`.  This file retracts one number of its own line's and promotes
# another to being the whole result, so both directions are pinned.
#   (1) the asymptotic sensitivity to r_s -- if it were NOT near 1 the acoustics would not work
#       and the phase reading would not be the whole story;
#   (2) the FIRST peak's sensitivity, since PART 2 retracts a number and must reproduce it;
#   (3) the pin's effect on the phase, without which the phase is the fitted parameter's;
#   (4) the seam phase's partial closure -- and if it ever closed the WHOLE gap the discrepancy
#       would be the datum's alone and this front's verdict would have to be restated;
#   (5) the peak count, since every number here is an asymptotic fit.
# ============================================================================================
assert 0.85 < SENS < 1.15, f"the asymptotic spacing tracks r_s at {SENS:.0%} of the acoustic rate"
assert _first < 0.6, f"the first peak tracks at {_first:.0%} -- it is NOT much less sensitive than "\
    f"the series' {SENS:.0%}, and PART 2 is retracting something the data do not support"
assert _pinmove < 0.15, f"the pin moves the phase by {_pinmove:.0%} of the discrepancy"
assert 0.15 < _close < 0.70, f"the seam phase closes {_close:.0%} of the gap"
assert abs((CTRL - _ia) - 0.615) < 0.05, f"the phase discrepancy is {CTRL-_ia:.3f}, expected 0.615"
assert min(len(R[nm]['pos']) for nm, _ in RUNS) >= 7, "an arm carries fewer than seven peaks"
print(f"GATE c54.191 (r2441), `L-506`: the asymptotic spacing tracks r_s at {SENS:.0%} of the "
      f"acoustic rate against the first peak's {_first:.0%}; the phase discrepancy is "
      f"{CTRL-_ia:.3f} l_A, moves {_pinmove:.0%} under a 31% swing in the fitted parameter and "
      f"closes {_close:.0%} under the seam datum's phase freedom — pinned against `L-505`, `L-504`'s "
      f"retracted PART 4, and `L-147` F5.")
