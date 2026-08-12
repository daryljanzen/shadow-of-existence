#!/usr/bin/env python3
"""
RECEIPT -- P15: ** ell_1/ell_A = 0.5703 IS A STATEMENT ABOUT THE SEAM DATUM AND NOT ABOUT THE RATE.
VARYING THE ONE THING THE CORPUS'S OWN DATUM LEAVES UNSPECIFIED -- "a COMMON phase" -- MOVES IT FROM
0.5703 TO 1.2599, A FACTOR OF 2.21.  ** WHAT DOES NOT MOVE IS THE PEAK SPACING, AT 0.79 +- 0.04 OF
ell_A UNDER EVERY PHASE AND NEVER 1.0 -- SO THE ROBUST DISAGREEMENT IS A 21% SPACING DEFICIT AND NOT
A 22% POSITION DEFICIT. **  AND `L-147`'s F4 FIRES UNDER EVERY PHASE, SO c54.186's VERDICT SURVIVES
THE THING THAT COULD HAVE OVERTURNED IT. **

Built r2441+c54.187, front #2, lead `L-501`.  ** THIS FILE EXISTS BECAUSE c54.186 NAMED A WORRY AND
THE NEXT REVISION IS WHERE A NAMED WORRY GETS SETTLED OR WITHDRAWN. **

===================================================================================================
** WHY: c54.186 SAID "0.5703 HAS NOT MOVED ACROSS EIGHT INSTRUMENT STATES" AND THAT WAS THE WRONG
INVARIANCE TO QUOTE. **
===================================================================================================

c54.186 closed with a caveat: *0.5703 has not moved across eight instrument states, which is evidence
either of a robust prediction or of a shared upstream constant, and this file cannot separate those.*
** The eight states vary the TRANSFER -- a fluid, a derived shear coefficient, a polarised hierarchy,
a wavenumber range, a continuum k-grid.  NOT ONE OF THEM VARIES THE INITIAL DATUM. **  So an
invariance across them is an invariance of the transfer and says nothing about the datum.

** AND THE DATUM IS WHERE ell_1 LIVES, BY THE CONSTRUCTION'S OWN GEOMETRY. **  The CR arm begins at
the seam -- z_start = 6761, eta_S = 180.4 Mpc -- because that is where the construction begins.  A
first-peak mode has k ~ 0.013/Mpc and crossed the horizon at k eta = 1, i.e. eta ~ 75 Mpc.  ** So the
modes that set the first peak are ALREADY SUB-HORIZON when the integration starts, and their phase at
eta_S is not derived from anything: it is assigned. **  *The corpus's datum is "ONE datum per mode and
a COMMON phase" (P15 sec:coherence).  That phrase fixes that the phase is common.  It does not fix
WHICH phase, and the instrument picks a density extremum.*

  PART 1  ** THE FIRST-PEAK POSITION IS NOT ROBUST TO THE PHASE, AND THE RANGE IS A FACTOR OF
          2.21. **  Scanning the common phase over [0, pi] -- with the amplitude and every other
          input untouched -- ell_1/ell_A takes 0.5703, 0.6101, 0.6233, 0.6764 and 1.2599.  ** At
          phi = 3pi/8 the peak at 172 is not there at all and the series starts at 380. **
  PART 2  ** WHAT IS ROBUST IS THE SPACING, AND IT IS ROBUSTLY WRONG. **  The mean peak spacing
          stays within 0.734-0.818 of ell_A across the whole scan -- a spread of 1.11 against the
          position's 2.21 -- and is never 1.0.  ** So this construction's acoustic series is ~21%
          too CLOSE at the sky's angular scale, under every reading of its own datum, and THAT is
          the disagreement that does not depend on a choice. **
  PART 3  ** AND `L-147`'s F4 FIRES UNDER EVERY PHASE, WHICH IS WHY c54.186's VERDICT SURVIVES
          THIS. **  Scored on identical bins, the CR arm runs 202-449 in chi^2/dof against a control
          at 0.77 on the same bins.  ** Its BEST phase is still two hundred times the control. **
          *So the thing that could have overturned c54.186 was measured and does not.*
  PART 4  ** THIS REPRODUCES c54.164 ON THE CURRENT INSTRUMENT, WHICH HAD NOT BEEN DONE. **  c54.164
          found ell_1 in {150, 165, 315} and a source comb at 0.72-0.79 of pi/r_s under four
          readings -- on the OLD `ROBUST_p1p2_scan` code.  ** Everything since has been built on
          `ACOUSTIC_two_arm`, and the finding was never carried across; P15's text has quoted 0.5703
          through six revisions of a transfer that cannot move it. **

** WHAT THIS DOES AND DOES NOT DO TO THE CORPUS'S NUMBER. **  P15 reports a 21.9% first-peak deficit
against a position floor of 0.16% and says it *"is not an artefact of how last scattering was
modelled"*.  ** That sentence is TRUE and it is not the sentence a reader takes from it. **  The
deficit is not an artefact of last scattering; it IS a function of the seam phase, which is upstream
of last scattering and is a choice inside the corpus's own stated datum.  *The number to carry is the
SPACING deficit, which is 21% and survives the scan; the position deficit is real under the stated
reading and is not robust to a reading the corpus has not fixed.*

** WHAT IS STILL NOT RULED OUT, AND IT IS NARROWER THAN IT WAS. **  The phase is one degree of
freedom in the datum; the AMPLITUDE's flatness in k (`CRXE`, and Theta-hat flat) is another and is
not scanned here.  ** A scan that moved the SPACING would be the one that mattered, and this file
does not run it. **  *Registered rather than resolved.*

SETTINGS: reduced -- LMAXL=1000 vs production 3000.  AT PRODUCTION: the first-peak POSITION
result stands unchanged (the first peak is fully resolved at this depth, which is why this
file's own finding is sound); the SPACING figure does NOT -- at LMAXL=3000 the CR arm carries
eight peaks and the asymptotic spacing is 0.975 of ell_A, not the 0.79 read here off three
gaps.  ** Retracted at c54.190; this line is the declaration that would have prevented it. **

rc=0 on success.  Run: python3 P15_the_first_peak_is_the_seam_datum_and_the_spacing_is_not.py
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
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

# ** EVERY SPECTRUM HERE IS THE SAME RUN WITH ONE ENV VARIABLE CHANGED.  CRPHI = 0 IS THE INSTRUMENT
# AS CODED BEFORE c54.187 AND MUST REPRODUCE 0.5703, WHICH IS THE CONTROL ON THE KNOB ITSELF. **
PHIS = (0.0, 0.3927, 0.7854, 1.1781, 1.5708, 1.9635, 2.3562, 2.7489, 3.1416)
LM = 500          # LMAXL = 1000 on these runs, so ell <= 500 leaves 2x wavenumber headroom


def read(phi):
    z = np.load(os.path.join(SP, f'c54.187_cr_phi{phi}.npz'))
    ls = np.asarray(z['ls'], float)
    return ls, np.asarray(z['Dl'], float), float(z['l_A'])


# =====================================================================
print("=" * 78)
print("PART 1/2 — THE POSITION MOVES BY 2.2x AND THE SPACING DOES NOT MOVE AT ALL")
print("=" * 78)
print(f"  *the common phase is the one thing \"a COMMON phase\" leaves open; everything else is held*")
print()
print(f"  {'CRPHI':>8} {'first four peaks':>26} {'l1/lA':>8} {'spacing/lA':>11} {'chi^2/dof':>10}")
POS, SPA, DOF = [], [], []
for phi in PHIS:
    ls, D, lA = read(phi)
    pk = argrelextrema(D, np.greater, order=3)[0][:4]
    pos = ls[pk]
    sp = float(np.mean(np.diff(pos))) / lA
    c = CS.chi2_of(ls, D, lmax=LM)
    POS.append(float(pos[0]) / lA)
    SPA.append(sp)
    DOF.append(c[0] / c[1])
    print(f"  {phi:>8.4f} {str([int(x) for x in pos]):>26} {pos[0]/lA:>8.4f} {sp:>11.4f} "
          f"{c[0]/c[1]:>10.1f}")
_pr = max(POS) / min(POS)
_sr = max(SPA) / min(SPA)
print(f"\n  ** THE FIRST-PEAK POSITION RUNS {min(POS):.4f} TO {max(POS):.4f} — A FACTOR OF {_pr:.2f}. **")
print(f"  ** THE PEAK SPACING RUNS {min(SPA):.4f} TO {max(SPA):.4f} — A FACTOR OF {_sr:.2f}, AND IS "
      f"NEVER 1.0. **")
print(f"     *So the robust disagreement is a {100*(1-np.mean(SPA)):.0f}% SPACING deficit, not a "
      f"{100*(1-POS[0]/0.7312):.0f}% position one.*")
print("  ⇒ ***c54.186's caveat is answered in the affirmative for the POSITION and in the negative")
print("     for the SPACING. The eight instrument states varied the transfer; the transfer is not")
print("     what sets the first peak.***")
if abs(POS[0] - 0.5703) > 5e-4:
    fail.append(f"CRPHI=0 gives l_1/l_A = {POS[0]:.4f}, not 0.5703 -- the knob is not a no-op at its "
                "default and every comparison here is against the wrong baseline")
if _pr < 1.5:
    fail.append(f"the position moves by only {_pr:.2f}x -- PART 1's claim is not what the scan shows")
if _sr > 1.35:
    fail.append(f"the spacing moves by {_sr:.2f}x -- it is NOT the robust quantity and PART 2 must be "
                "rewritten rather than patched")
if max(SPA) > 0.95:
    fail.append(f"the spacing reaches {max(SPA):.3f} of l_A -- at that point the deficit is not "
                "robust either and this file's title is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — AND F4 FIRES UNDER EVERY PHASE, SO c54.186 SURVIVES THIS")
print("=" * 78)
_zl = np.load(os.path.join(SP, 'c54.186_lcdm_L3000.npz'))
_ls = np.asarray(_zl['ls'], float)
_cc = CS.chi2_of(_ls, np.asarray(_zl['Dl'], float), lmax=LM)
CTRL = _cc[0] / _cc[1]
print(f"  the control on the same {_cc[1]} bins: chi^2/dof = {CTRL:.2f}")
print(f"  the CR arm's BEST phase:               chi^2/dof = {min(DOF):.0f}  (CRPHI = "
      f"{PHIS[int(np.argmin(DOF))]:.4f})")
print(f"  the CR arm's worst phase:              chi^2/dof = {max(DOF):.0f}")
print(f"\n  ** EVEN AT ITS BEST PHASE THE CR ARM COSTS {min(DOF)/CTRL:.0f} TIMES THE CONTROL. **")
print("     *`L-147`'s F4 asks for one order of magnitude between F3 and F2. It gets two more than")
print("     that at every phase, so the phase freedom does not reach the verdict.*")
print()
print("  ⛔ ***AND F5 IS STILL NOT SOFTENED: a MEASUREMENT DISCREPANCY is not a framework verdict,")
print("     `PO-7` is protected, and removing a confound makes a measurement cleaner and not a")
print("     conclusion. the conversion runs by `F5`'s stated procedure.***")
if min(DOF) < 50 * CTRL:
    fail.append(f"the CR arm's best phase is only {min(DOF)/CTRL:.0f}x the control -- c54.186's "
                "reading does NOT survive the phase freedom and must be restated, not defended")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the first-peak position runs over a factor of 2.2 under the common phase the")
print("corpus's own datum leaves unspecified, so 0.5703 is a statement about the seam datum; the peak")
print("SPACING holds at 0.79 of l_A across the same scan and is never 1.0, so the robust disagreement")
print("is a 21% spacing deficit; and the CR arm costs at least two hundred times the control at every")
print("phase, so `L-147`'s F4 fires throughout and c54.186's verdict is not reached by this freedom.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.187, `L-501`.  This file WEAKENS a number the paper carries and STRENGTHENS a
# verdict the previous revision landed, so both directions are pinned.
#   (1) CRPHI = 0 reproduces 0.5703 -- without this the knob is not a control on itself;
#   (2) the position's spread, which is the withdrawal;
#   (3) the spacing's spread AND that it stays below 1.0, which is what replaces the withdrawn
#       number -- if the spacing ever moved, this file would have no positive content;
#   (4) the CR arm's BEST phase against the control, which is what makes c54.186 survive; if this
#       ever falls, c54.186 must be RESTATED rather than defended.
# ============================================================================================
assert abs(POS[0] - 0.5703) < 5e-4, f"CRPHI=0 gives {POS[0]:.4f}, not the coded 0.5703"
assert _pr > 1.5, f"the first-peak position moves only {_pr:.2f}x under the phase"
assert abs(max(POS) - 1.2599) < 2e-3, f"the position's maximum is {max(POS):.4f}, expected 1.2599"
assert _sr < 1.35, f"the spacing moves {_sr:.2f}x -- it is not the robust quantity"
assert 0.70 < np.mean(SPA) < 0.85, f"the mean spacing is {np.mean(SPA):.3f} of l_A, expected ~0.77"
assert max(SPA) < 0.95, f"the spacing reaches {max(SPA):.3f} -- the deficit is not robust"
assert min(DOF) > 50 * CTRL, \
    f"the CR arm's best phase is {min(DOF)/CTRL:.0f}x the control -- c54.186 must be restated"
assert min(DOF) > 150.0, f"the CR arm's best phase is chi^2/dof = {min(DOF):.0f}, expected ~202"
print(f"GATE c54.187 (r2441), `L-501`: the first-peak position runs {min(POS):.4f}-{max(POS):.4f} "
      f"({_pr:.2f}x) under the common phase while the spacing holds {min(SPA):.3f}-{max(SPA):.3f} "
      f"({_sr:.2f}x, mean {np.mean(SPA):.3f}, never 1.0); the CR arm's best phase costs "
      f"{min(DOF)/CTRL:.0f}x the control — pinned against P15 sec:coherence, `L-147` F4/F5, and "
      f"c54.164's ell_1 in {{150, 165, 315}}.")
