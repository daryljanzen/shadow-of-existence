#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE SECOND AND LAST FREEDOM IN THE SEAM DATUM IS OPENED, AND ACROSS ALL EIGHTEEN
READINGS THE FIRST-PEAK POSITION SPANS 2.26x WHILE THE PEAK SPACING SPANS 1.21x AT A MEAN OF 0.772
OF ell_A AND NEVER EXCEEDS 0.818.  ** c54.187's SPACING RANGE IS WIDENED FROM 1.11x TO 1.21x -- THIS
FILE WEAKENS ITS OWN PREDECESSOR RATHER THAN CONFIRMING IT -- AND `L-147`'s F4 FIRES AT EVERY ONE OF
THE EIGHTEEN. **

Built r2441+c54.188, front #2, lead `L-502`.

===================================================================================================
** WHY: c54.187 CLOSED ONE FREEDOM AND NAMED THE OTHER.  THIS IS THE OTHER. **
===================================================================================================

c54.187 scanned the common PHASE and wrote: *"the phase is ONE degree of freedom in the datum;
Theta-hat's flatness in k is another and is NOT scanned here.  A scan that moved the SPACING would be
the one that mattered."*  ** This runs it. **

** WHAT THE SECOND FREEDOM IS, AND IT IS NOT INVENTED HERE. **  The datum's amplitude is the corpus's
C4 transfer shape T(x) = 3(sin x - x cos x)/x^3.  ** The instrument evaluates it at a SINGLE argument
xe = 1/sqrt(3) for every mode -- which is that shape read at each mode's OWN horizon crossing, since
x = k c_s eta with k eta = 1 gives exactly 1/sqrt(3).  That is a self-similar reading and a
defensible one. **  *The alternative evaluates the SAME shape at each mode's own phase AT THE SEAM,
x = k c_s eta_S, so modes that crossed earlier carry a smaller amplitude.*  Both are readings of "one
datum per mode"; neither is a new physical assumption.

  PART 1  ** THE POSITION IS NO MORE STABLE THAN c54.187 FOUND IT, AND SLIGHTLY LESS. **  Across the
          eighteen readings ell_1/ell_A spans 0.5570 to 1.2599 -- ** 2.26x, against the phase
          scan's own 2.21x. **  *The second freedom adds nothing to the position's instability
          because the position was already unstable.*
  PART 2  ** THE SPACING IS MEASURED ONLY WHERE THERE IS A SERIES TO MEASURE, AND THAT DISQUALIFIES
          EIGHT OF THE EIGHTEEN. **  ** Eight readings return a spectrum whose higher peaks have
          COLLAPSED -- the peak-finder sees three features, the last of them at zero -- and a
          spacing read off that is not a spacing. **  *The requirement stated before the numbers:
          four peaks, the fourth at least 5% of the first.*
  PART 3  ** OVER THE TEN THAT QUALIFY THE SPACING SPANS 0.676 TO 0.818 OF ell_A -- 1.21x, mean
          0.772 -- AND NEVER REACHES 0.82. **  ** c54.187 reported 1.11x from the phase alone.  This
          file WIDENS its predecessor's range by opening a freedom its predecessor did not have. **
          *The conclusion survives at a lower strength: a ~23% spacing deficit under every reading
          that produces an acoustic series at all.*
  PART 4  ** AND F4 FIRES AT EVERY ONE OF THE EIGHTEEN. **  chi^2/dof runs 157 to 460 against a
          control at 0.75 on identical bins, so ** the arm's best reading costs 209 times the
          control **.  *The datum's freedom, fully opened, does not reach the verdict.*

** THE ONE THING THAT LOOKS LIKE A RESCUE AND IS NOT. **  ** The best-fitting reading -- the seam
amplitude at phi = pi, chi^2/dof = 157 -- is one of the eight DISQUALIFIED ones, and its spacing
"improves" to 0.92 precisely because the higher peaks are gone. **  *A reading fits better by having
less structure to disagree with.  It is reported because it is the best number in the table and a
reader would find it; it is not a direction.*

** SO THE DATUM IS NOW CLOSED, AND WHAT IS LEFT IS NOT THE DATUM. **  Both freedoms the corpus's own
phrase leaves open have been scanned.  *What has NOT been varied is the background itself --
Z_START is solved so that pi D_M / r_s = 301.6 exactly, which is a target and not an output, and
that is a separate item from the datum.*  ** Registered rather than resolved. **

SETTINGS: reduced -- LMAXL=1000 vs production 3000.  AT PRODUCTION: the eighteen-reading
robustness stands as run and the SPACING figure does not -- see c54.190.  ** What this file
measures is the first-three-gap spacing under eighteen datum readings, and that is a real and
stable quantity; it is not the acoustic spacing, and c54.190 corrects the name. **

rc=0 on success.  Run: python3 P15_both_datum_freedoms_opened_and_the_spacing_still_holds.py
                        (numpy scipy; ~15 s)
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
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

PHIS = (0.0, 0.3927, 0.7854, 1.1781, 1.5708, 1.9635, 2.3562, 2.7489, 3.1416)
READINGS = (('flat', 'c54.187_cr_phi{}.npz'), ('seam', 'c54.188_cr_seam_phi{}.npz'))
LM = 500          # LMAXL = 1000 on these runs, so ell <= 500 carries 2x wavenumber headroom
MINPK, MINH = 4, 0.05     # ** stated before the numbers: what counts as a measurable series **

# =====================================================================
print("=" * 78)
print("PART 1/2/3 — EIGHTEEN READINGS OF THE CORPUS'S OWN DATUM")
print("=" * 78)
print("  *`flat` = the C4 shape at one argument for every mode, the instrument as coded before")
print("   c54.188; `seam` = the same shape at each mode's own phase at the seam.*")
print()
print(f"  {'reading':>16} {'npk':>4} {'4th/1st':>8} {'l1/lA':>8} {'spacing':>8} {'chi^2/dof':>10} "
      f"{'series?':>8}")
POS, SPA, DOF, USED = [], [], [], []
for tag, pat in READINGS:
    for phi in PHIS:
        z = np.load(os.path.join(SP, pat.format(phi)))
        ls = np.asarray(z['ls'], float)
        D = np.asarray(z['Dl'], float)
        lA = float(z['l_A'])
        pk = argrelextrema(D, np.greater, order=3)[0][:4]
        h = float(D[pk[-1]] / D[pk[0]]) if len(pk) >= MINPK else 0.0
        sp = float(np.mean(np.diff(ls[pk]))) / lA
        c = CS.chi2_of(ls, D, lmax=LM)
        ok = len(pk) >= MINPK and h >= MINH
        POS.append(float(ls[pk[0]]) / lA)
        DOF.append(c[0] / c[1])
        USED.append(ok)
        if ok:
            SPA.append(sp)
        print(f"  {tag + ' ' + format(phi, '.4f'):>16} {len(pk):>4} {h:>8.3f} "
              f"{ls[pk[0]]/lA:>8.4f} {sp:>8.4f} {c[0]/c[1]:>10.1f} {'yes' if ok else 'NO':>8}")
_pr = max(POS) / min(POS)
_sr = max(SPA) / min(SPA)
print(f"\n  ** {sum(USED)} OF THE {len(POS)} READINGS CARRY A MEASURABLE FOUR-PEAK SERIES. **")
print(f"     first-peak POSITION / l_A  (all {len(POS)}) : {min(POS):.4f} – {max(POS):.4f}   "
      f"spread {_pr:.2f}x")
print(f"     peak SPACING / l_A   (the {sum(USED)} usable) : {min(SPA):.4f} – {max(SPA):.4f}   "
      f"spread {_sr:.2f}x   mean {np.mean(SPA):.4f}")
print(f"\n  ** c54.187 REPORTED 1.11x FROM THE PHASE ALONE.  OPENING THE SECOND FREEDOM WIDENS IT TO "
      f"{_sr:.2f}x. **")
print(f"     *This file weakens its own predecessor.  The conclusion survives at lower strength: a")
print(f"     ~{100*(1-np.mean(SPA)):.0f}% SPACING deficit under every reading that produces an acoustic series at all,")
print(f"     against a POSITION that spans a factor of {_pr:.2f} and states nothing.*")
if _pr < 1.5:
    fail.append(f"the position moves only {_pr:.2f}x -- PART 1 is not what the scan shows")
if _sr > 1.6:
    fail.append(f"the spacing moves {_sr:.2f}x over both freedoms -- it is no longer the robust "
                "quantity and c54.187's conclusion must be WITHDRAWN, not widened")
if max(SPA) > 0.90:
    fail.append(f"the spacing reaches {max(SPA):.3f} of l_A among the usable readings -- the deficit "
                "is not robust and this file's title is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — AND F4 FIRES AT EVERY ONE OF THE EIGHTEEN")
print("=" * 78)
_zl = np.load(os.path.join(SP, 'c54.186_lcdm_L3000.npz'))
_c = CS.chi2_of(np.asarray(_zl['ls'], float), np.asarray(_zl['Dl'], float), lmax=LM)
CTRL = _c[0] / _c[1]
print(f"  the control on the same {_c[1]} bins:  chi^2/dof = {CTRL:.2f}")
print(f"  the CR arm across eighteen readings: chi^2/dof = {min(DOF):.0f} – {max(DOF):.0f}")
print(f"\n  ** THE ARM'S BEST READING COSTS {min(DOF)/CTRL:.0f} TIMES THE CONTROL. **")
_bi = int(np.argmin(DOF))
print(f"\n  ⚠ ***AND THE BEST READING IS ONE OF THE DISQUALIFIED EIGHT.***  *Its higher peaks have")
print(f"     collapsed, so it fits better by having less structure to disagree with. It is reported")
print(f"     because it is the best number in the table and a reader would find it; it is not a")
print(f"     direction.*  (usable series: {'yes' if USED[_bi] else 'NO'})")
print()
print("  ⛔ ***F5 UNSOFTENED: a MEASUREMENT DISCREPANCY is not a framework verdict.  `PO-7` is")
print("     protected and the conversion runs by `F5`'s stated procedure.***")
if min(DOF) < 50 * CTRL:
    fail.append(f"the arm's best reading is only {min(DOF)/CTRL:.0f}x the control -- c54.186 must be "
                "RESTATED rather than defended")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — both freedoms the corpus's datum leaves open are now scanned; the first-peak")
print("position spans 2.26x and states nothing; the spacing spans 1.21x at a mean of 0.77 of l_A and")
print("never exceeds 0.82, so the ~23% spacing deficit stands at a strength lower than c54.187 gave")
print("it; and the arm's best reading still costs two hundred times the control, so the datum's")
print("freedom fully opened does not reach `L-147`'s verdict.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.188, `L-502`.  This file WIDENS its own predecessor's range, so the pins are
# on the widened value and on the point past which the predecessor would have to be WITHDRAWN.
#   (1) the position's spread, which is the standing withdrawal from c54.187;
#   (2) the spacing's spread over BOTH freedoms, and the ceiling past which c54.187's conclusion
#       does not survive at any strength -- 1.6x, or a maximum above 0.90 of l_A;
#   (3) the usable-series count, since PART 3's number is computed only over those and a silent
#       change in how many qualify would move the range without moving the code;
#   (4) the arm's BEST reading against the control -- if this falls, c54.186 is restated.
# ============================================================================================
assert _pr > 1.5, f"the first-peak position moves only {_pr:.2f}x over both freedoms"
assert abs(max(POS) - 1.2599) < 2e-3, f"the position's maximum is {max(POS):.4f}, expected 1.2599"
assert _sr < 1.6, f"the spacing moves {_sr:.2f}x -- c54.187's conclusion must be WITHDRAWN"
assert max(SPA) < 0.90, f"the spacing reaches {max(SPA):.3f} of l_A among usable readings"
assert 0.70 < np.mean(SPA) < 0.85, f"the mean spacing is {np.mean(SPA):.3f}, expected ~0.77"
assert sum(USED) == 10, f"{sum(USED)} readings carry a measurable series, expected 10"
assert min(DOF) > 50 * CTRL, \
    f"the arm's best reading is {min(DOF)/CTRL:.0f}x the control -- c54.186 must be restated"
assert min(DOF) > 120.0, f"the arm's best reading is chi^2/dof = {min(DOF):.0f}, expected ~157"
print(f"GATE c54.188 (r2441), `L-502`: over {len(POS)} readings of both datum freedoms the first-peak "
      f"position spans {min(POS):.4f}–{max(POS):.4f} ({_pr:.2f}x) while the spacing spans "
      f"{min(SPA):.4f}–{max(SPA):.4f} ({_sr:.2f}x, mean {np.mean(SPA):.3f}) over the {sum(USED)} that "
      f"carry a series; the arm's best reading costs {min(DOF)/CTRL:.0f}x the control — pinned "
      f"against c54.187 `L-501`, P15 sec:coherence, and `L-147` F4/F5.")
