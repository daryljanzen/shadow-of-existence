#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE LAST FREE THING UPSTREAM IS THE CORPUS'S OWN ONE FITTED NUMBER, AND MOVING IT
BY 31% MOVES THE SPACING DEFICIT BY 7%.  ** z_onset IS SOLVED SO THAT ell_A HITS A TARGET; PINNING
THAT TARGET ANYWHERE FROM 260 TO 340 -- z_onset FROM 11009 TO 5066, r_s FROM 157 TO 120 Mpc -- LEAVES
THE PEAK SPACING AT 0.798 +- 0.028 OF ell_A AND NEVER ABOVE 0.821.  SO THE ~20% SPACING DEFICIT IS
NOT AN ARTEFACT OF WHERE THE PIN WAS PUT. **

Built r2441+c54.189, front #2, lead `L-504`.

===================================================================================================
** WHY: c54.188 CLOSED THE DATUM AND NAMED THE BACKGROUND.  THIS IS THE BACKGROUND. **
===================================================================================================

c54.188 closed both freedoms in the seam datum and wrote: *"What has NOT been varied is the
background: `Z_START` is solved so that pi D_M / r_s = 301.6 exactly, which is a TARGET and not an
output."*  ** This varies it. **

** AND THE FIRST THING TO SAY IS THAT THE PIN IS DECLARED, NOT HIDDEN. **  P15 sec:tensions states
it in its own words -- *"the measured acoustic scale is reproduced at the directly measured H_0 by a
single z_onset"* -- and names z_onset *"the one fitted number"*.  ** What had not happened is that
the number was a literal buried inside a `brentq` call, so nothing downstream could vary it and
nothing had. **  *The question a fitted parameter always owes is not whether it is fitted but what
survives it.*

  PART 1  ** MOVING THE PIN MOVES EVERYTHING IT SHOULD. **  Pinning ell_A at 260, 280, 301.6, 320
          and 340 drives z_onset from 11009 down to 5066 and the sound horizon from 157.1 to 120.2
          Mpc -- a 24% fall in r_s over a 31% swing in the target.
  PART 2  ** AND THE SPACING DEFICIT DOES NOT FOLLOW IT. **  The mean peak spacing stays between
          0.7647 and 0.8205 of ell_A across the whole range -- ** a spread of 1.07 against the pin's
          1.31 **.  *So the ~20% spacing deficit is a property of the construction and not of the
          value its one fitted parameter was fitted to.*
  PART 3  ** THE FIRST-PEAK POSITION IS TWICE AS SENSITIVE, AND STILL DOES NOT RESCUE ANYTHING. **
          ell_1/ell_A runs 0.5176 to 0.6308 -- 1.22x -- and never approaches the sky's 0.7312.
          ** Its drift is almost entirely ell_A's: the peak itself moves only 164 -> 176 while
          ell_A moves 260 -> 340. **
  PART 4  ** WHICH IS THE STRUCTURAL STATEMENT UNDER ALL OF IT. **  ** In ordinary acoustics the
          peak positions ARE set by the sound horizon, so a 24% fall in r_s should raise ell_1 by
          about 31%.  Here it raises it by 7%. **  *This construction's peaks are only weakly tied
          to its own sound horizon, and that -- rather than any one ratio -- is what the comparison
          with the sky is registering.*

** SO THE ACOUSTIC QUESTION ON THIS FRONT IS CLOSED AS FAR AS THE CONSTRUCTION'S FREEDOMS GO. **
c54.187 scanned the seam phase, c54.188 the amplitude reading, and this the fitted parameter.
** Across all of them the peak SPACING sits near 0.78-0.80 of ell_A and never reaches 0.9, while the
first-peak POSITION spans a factor of 2.26 and states nothing. **  *What is left is not a freedom
this file can scan: it is whether the construction's peaks SHOULD be tied to its sound horizon, which
is a question about the physics and not about a setting.*

** F5 IS NOT SOFTENED. **  A measurement discrepancy is not a framework verdict; `PO-7` is protected;
the conversion runs by `F5`'s stated procedure.  ** And one small inconsistency is recorded rather than fixed here: the
instrument pins ell_A = 301.6 while `P15_zonset_determinations` derives z_onset = 6797 by pinning the
MEASURED 301.76.  0.05%, and it is why this instrument returns 6761 where that receipt returns
6797. **  *Named so that the two numbers are not read as a disagreement.*

SETTINGS: reduced -- LMAXL=1000 vs production 3000.  AT PRODUCTION: PART 4's sensitivity is
retracted -- at LMAXL=3000 the asymptotic series tracks r_s at 98% of the acoustic rate, not
the 24% read here off the FIRST peak, which sits inside a transient (c54.191).  The pin scan's
own robustness stands.  ** This is the second figure this depth cost, and both are declared
here rather than left to the reader. **

rc=0 on success.  Run: python3 P15_the_spacing_deficit_survives_the_one_fitted_parameter.py
                        (numpy scipy; ~10 s)
"""
# ** SCOPE NOTE (r2933). **
# *** This receipt measures MEAN PEAK SPACING framed as "the ~20% spacing deficit" — a figure `B4_the_intercept_is_a_phase` WITHDREW ("the ~21%/23% figure is withdrawn"; at production depth the asymptotic spacing is 0.975). Its 3%-under-31% stability is therefore measured on a mean over three or four peaks, i.e. THE TRANSIENT REGION, and B5 records that the scan cannot reach the asymptotic intercept. ***
# ⌗ The receipt's own computation is unaffected; this records WHAT IT MEASURES.
import os
import sys

import numpy as np
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

TARGETS = ('260', '280', '301.6', '320', '340')
LM = 500          # LMAXL = 1000 on these runs, so ell <= 500 carries 2x wavenumber headroom
SKY = 220.6 / 301.7

# =====================================================================
print("=" * 78)
print("PART 1/2/3 — THE ONE FITTED PARAMETER, MOVED")
print("=" * 78)
print("  *`z_onset` is solved so that l_A = pi D_M / r_s hits the target in the first column.  P15")
print("   sec:tensions calls it \"the one fitted number\"; LATARG = 301.6 is the value as coded.*")
print()
print(f"  {'l_A pinned':>11} {'r_s':>8} {'first four peaks':>26} {'l1/lA':>8} {'spacing/lA':>11} "
      f"{'chi^2/dof':>10}")
POS, SPA, RS, DOF = [], [], [], []
for t in TARGETS:
    z = np.load(os.path.join(SP, f'c54.189_cr_lA{t}.npz'))
    ls = np.asarray(z['ls'], float)
    D = np.asarray(z['Dl'], float)
    lA = float(z['l_A'])
    pk = argrelextrema(D, np.greater, order=3)[0][:4]
    if len(pk) < 4:
        fail.append(f"the pin at {t} returns fewer than four peaks -- the series is degenerate and "
                    "the spacing below is not a spacing")
        continue
    sp = float(np.mean(np.diff(ls[pk]))) / lA
    c = CS.chi2_of(ls, D, lmax=LM)
    POS.append(float(ls[pk[0]]) / lA)
    SPA.append(sp)
    RS.append(float(z['r_s']))
    DOF.append(c[0] / c[1])
    print(f"  {t:>11} {float(z['r_s']):>8.1f} {str([int(ls[q]) for q in pk]):>26} "
          f"{ls[pk[0]]/lA:>8.4f} {sp:>11.4f} {c[0]/c[1]:>10.1f}")
_pin = float(TARGETS[-1]) / float(TARGETS[0])
_sr = max(SPA) / min(SPA)
_pr = max(POS) / min(POS)
print(f"\n  ** THE PIN MOVES BY {_pin:.2f}x AND r_s BY {max(RS)/min(RS):.2f}x. **")
print(f"     the peak SPACING / l_A : {min(SPA):.4f} – {max(SPA):.4f}   spread {_sr:.2f}x   "
      f"mean {np.mean(SPA):.4f}")
print(f"     the first POSITION / l_A : {min(POS):.4f} – {max(POS):.4f}   spread {_pr:.2f}x   "
      f"(the sky: {SKY:.4f})")
print(f"\n  ⇒ ***THE ~{100*(1-np.mean(SPA)):.0f}% SPACING DEFICIT IS NOT AN ARTEFACT OF WHERE THE PIN "
      f"WAS PUT: a {100*(_pin-1):.0f}% swing in\n     the one fitted parameter moves it by "
      f"{100*(_sr-1):.0f}%.***")
if _sr > 1.20:
    fail.append(f"the spacing moves {_sr:.2f}x under the pin -- it IS an artefact of the fitted "
                "parameter and every conclusion resting on it must be withdrawn")
if max(SPA) > 0.90:
    fail.append(f"the spacing reaches {max(SPA):.3f} of l_A under some pin -- the deficit is not "
                "robust and this file's title is wrong")
if max(POS) > SKY:
    fail.append(f"the first-peak position reaches {max(POS):.4f}, at or past the sky's {SKY:.4f} -- "
                "PART 3's 'never approaches' is false")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND THE STRUCTURAL STATEMENT UNDER IT")
print("=" * 78)
# ** in ordinary acoustics ell_1 is proportional to D_M / r_s, so d ln ell_1 = -d ln r_s. **
_i, _j = int(np.argmax(RS)), int(np.argmin(RS))
L1 = [POS[k] * float(np.load(os.path.join(SP, f'c54.189_cr_lA{TARGETS[k]}.npz'))['l_A'])
      for k in range(len(POS))]
d_rs = RS[_j] / RS[_i] - 1.0
d_l1 = L1[_j] / L1[_i] - 1.0
print(f"  r_s falls {100*d_rs:+.0f}% between the widest pins ({RS[_i]:.1f} -> {RS[_j]:.1f} Mpc)")
print(f"  the first peak moves {100*d_l1:+.0f}% over the same range ({L1[_i]:.0f} -> {L1[_j]:.0f})")
print(f"  ** ordinary acoustics would give {100*(1/(1+d_rs)-1):+.0f}%, since ell_1 goes as D_M/r_s. **")
_sens = d_l1 / (1 / (1 + d_rs) - 1)
print(f"\n  ⇒ ***THIS CONSTRUCTION'S PEAKS ARE ONLY {_sens:.0%} AS SENSITIVE TO ITS OWN SOUND HORIZON")
print(f"     AS ACOUSTICS REQUIRES.***  *That -- rather than any one ratio -- is what the comparison")
print("     with the sky is registering, and it is a question about the physics rather than about a")
print("     setting, so this file registers it and does not scan it.*")
print()
print("  ⛔ ***F5 UNSOFTENED: a MEASUREMENT DISCREPANCY is not a framework verdict.  `PO-7` is")
print("     protected and the conversion runs by `F5`'s stated procedure.***")
if not (0.0 < _sens < 0.6):
    fail.append(f"the peaks track the sound horizon at {_sens:.0%} of the acoustic rate -- PART 4's "
                "reading is not what the scan shows")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — moving the corpus's one fitted number over a 31% range drives z_onset from")
print("11009 to 5066 and the sound horizon by 24%, and the peak spacing stays at 0.798 +- 0.028 of")
print("l_A throughout, never above 0.821.  The spacing deficit is not an artefact of the pin.  And")
print("the peaks track the sound horizon at about a quarter of the rate acoustics requires, which is")
print("the structural statement under the ratio.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.189, `L-504`.  This is the last upstream freedom the construction leaves, so
# the pins are on the survival AND on the point at which the survival claim would fail.
#   (1) the spacing's spread under the pin, and the ceiling past which it would be an ARTEFACT of
#       the fitted parameter and every conclusion resting on it withdrawn;
#   (2) the spacing's maximum, since a pin that took it near 1.0 would remove the deficit itself;
#   (3) that the first-peak position never reaches the sky's ratio at any pin, which is PART 3;
#   (4) the sensitivity of the peaks to r_s, which is PART 4's whole content -- if it ever reached
#       the acoustic rate, the disagreement would be about a NUMBER and not about a mechanism.
# ============================================================================================
assert _sr < 1.20, f"the spacing moves {_sr:.2f}x under the pin -- it is the pin's, not the model's"
assert max(SPA) < 0.90, f"the spacing reaches {max(SPA):.3f} of l_A under some pin"
assert 0.70 < np.mean(SPA) < 0.85, f"the mean spacing is {np.mean(SPA):.3f}, expected ~0.80"
assert max(POS) < SKY, f"the position reaches {max(POS):.4f}, at or past the sky's {SKY:.4f}"
assert len(SPA) == len(TARGETS), f"only {len(SPA)} of {len(TARGETS)} pins gave a four-peak series"
assert 0.0 < _sens < 0.6, f"the peaks track r_s at {_sens:.0%} of the acoustic rate"
assert abs(max(RS) / min(RS) - 1.31) < 0.05, \
    f"r_s swings {max(RS)/min(RS):.2f}x over the pin range, expected ~1.31"
print(f"GATE c54.189 (r2441), `L-504`: pinning l_A from {TARGETS[0]} to {TARGETS[-1]} drives r_s "
      f"{max(RS):.1f} -> {min(RS):.1f} Mpc ({max(RS)/min(RS):.2f}x) and leaves the peak spacing at "
      f"{min(SPA):.4f}–{max(SPA):.4f} of l_A ({_sr:.2f}x, mean {np.mean(SPA):.3f}); the first peak "
      f"never reaches the sky's {SKY:.4f}; and the peaks track r_s at {_sens:.0%} of the acoustic "
      f"rate — pinned against P15 sec:tensions's 'one fitted number', `L-502`, and `L-147` F5.")
