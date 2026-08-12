#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE WAVENUMBER TRUNCATION WAS 78% OF THE CONTROL'S REMAINING chi^2, AND REMOVING
IT TAKES THE CONTROL TO chi^2/dof = 1.18 OVER THE FULL RANGE AGAINST A REFERENCE LambdaCDM'S 1.01 --
SO FRONT #2's TARGET IS MET AND NO NAMED SECTOR REMAINS.  ACROSS FOUR INSTRUMENT STATES THE CR ARM
DID NOT MOVE, AND `L-147`'s PRE-REGISTERED F4 FIRES WITH THE ABSOLUTE COMPANION ITS OWN F6
CORRECTION DEMANDED. **

Built r2441+c54.186, front #2, lead `L-500`.

===================================================================================================
** WHY THIS EXISTS: THE CONDITION c54.172 WROTE FOR REOPENING `L-147` HAS BEEN MET. **
===================================================================================================

`L-147` was answered at c54.172 with "the likelihood CANNOT ARBITRATE", and the reason was stated in
that file's own F6: ** F4 is a RATIO test and never asks whether the instrument's floor F2 is small
in ABSOLUTE terms.  It was not -- the control arm sat at chi^2/dof ~ 100. **  The row's closing line
named what would change it: *"a transfer with sub-per-cent-height control -- front #2's work."*

** FRONT #2 HAS NOW DELIVERED THAT, AND THIS FILE IS THE MEASUREMENT. **  *The reopening condition
was written before the answer was known, which is the only footing on which a result this
consequential may be read at all.*

  PART 1  ** WHERE THE CONTROL'S REMAINING chi^2 ACTUALLY LIVES, AND IT IS NOT SPREAD. **  After
          c54.183's derived lensing the control sits at 989 over 185 bins.  ** 726 of that 989 --
          73% -- is in the 30 bins above ell = 1500, which is 16% of the bins. **  *So c54.184's
          "53% in neither template set" is not a mystery shape distributed over the spectrum.*
  PART 2  ** AND IT IS THE WAVENUMBER TRUNCATION -- WHICH IS SHOWN BY REMOVING IT RATHER THAN BY
          ARGUING FOR IT. **  The instrument builds its k-grid as k = ell/D_M with ell <= LMAXL, so
          the HIGHEST output multipole has no k-headroom at all -- while C_ell draws on every k with
          k D_M >= ell.  ** Re-run at LMAXL = 3000 with the k-SPACING HELD FIXED and scored on the
          SAME bins, the control goes 989 -> 218, chi^2/dof 5.34 -> 1.18, and the last band's ratio
          to the reference goes 0.42 -> 0.99. **  *c54.178 named the starvation and reported a
          restricted-range number for it; what is new here is that it was the whole of the tail.*
          ⇒ ***FRONT #2's TARGET IS MET: the control is within 17% of a true LambdaCDM fit's chi^2
          over ell = 100-1996, and the last item on the front's own list is struck as numerical.***
  PART 3  ** THE CR ARM'S k-LADDER, WAIVED BY THE ALIAS GATE ON A CLAIM SINCE c54.178, IS CHECKED
          IN chi^2 HERE FOR THE FIRST TIME -- AND THE WAIVER WAS RIGHT. **  The gate demands 4
          samples per Bessel period and the CR ladder has 2.3; it passes itself with the note *"this
          is not aliasing -- but it is only not aliasing if the answer does not depend on it. Run
          KCONT=1 to check."*  ** Run at KCONT=1 (1800 continuum modes, 5.7 per period, against the
          ladder's ~725) the spectra agree to better than 0.7% everywhere and the chi^2 to 2.1 in
          51817. **  *That check had been run for the PEAK POSITION and never for the statistic this
          file reads.*
  PART 4  ** THE INSTRUMENT WAS IMPROVED FOUR TIMES.  THE CONTROL FOLLOWED THE SKY BY A FACTOR OF
          EIGHTEEN AND THE CR ARM MOVED BY 5%. **  Over the full range, both arms carrying the same
          lensing operator: the control 21.2 -> 27.7 -> 5.34 -> 1.18 across c54.175 (fluid, 8/9),
          c54.177 (fluid, derived 16/15), c54.178 (the polarised hierarchy) and c54.186 (the same
          with the wavenumber range opened); the CR arm 290.7 -> 304.2 -> 298.9 -> 302.1.  ** That
          is the signature F4's second clause is written to detect, and it is stronger than any
          single build's number. **
  PART 5  ** SO F4 FIRES, AND BY THREE ORDERS OF MAGNITUDE RATHER THAN THE ONE IT ASKS FOR. **  F2 = chi^2(arm) - chi^2(CAMB) and F3 = chi^2(CR) - chi^2(arm), both as `L-147`
          defines them, and both arms carried at the SAME wavenumber range so that the construction
          is not charged for the instrument's truncation -- which is the mistake F3 exists to avoid.

** WHAT THIS IS AND IS NOT, AND F5 IS NOT SOFTENED HERE. **  `L-147`'s F5 says a negative is a
MEASUREMENT DISCREPANCY and not a framework verdict, and that `PO-7` is protected precisely here.
** This file reports a number and does not convert it.  the conversion runs by `F5`'s stated procedure. **  *And the
number is not new physics: the corpus has carried ell_1/ell_A = 0.5703 against the sky's 0.7312 --
a 22% deficit -- since c54.168, stated in P15's own text at 21.9%.  What is new is that there is now
a control good enough for that deficit to be read through a likelihood instead of through a ratio.*

** THE TWO THINGS THAT WOULD UNDO IT, WRITTEN DOWN SO THEY CAN BE TESTED RATHER THAN ARGUED. **
  (a) ** an unequal comparison. **  If the control were carried at a wavenumber range the CR arm was
      not, F3 would charge the construction for the instrument.  *Both arms are run at LMAXL = 3000
      here and scored on identical bins; PART 5 reports the restricted range as well, where the
      question does not arise because both arms have headroom.*
  (b) ** a defect the instrument's states SHARE. **  PART 3 removes the largest named candidate.
      What is NOT ruled out is something upstream of all of them -- and the honest form of that
      worry is that 0.5703 has never once moved across eight instrument states, which is evidence
      either of a robust prediction or of a shared upstream constant.  *This file cannot separate
      those and does not claim to.*

SETTINGS: mixed, and the mixture is the point.  PARTS 1 and 3-5 read the LMAXL=2000 banked
pair (reduced vs production 3000); PART 2 reads the LMAXL=3000 pair and is what SHOWS the 2000 runs
were starved.  AT PRODUCTION: every chi^2 quoted from the 2000 pair is 78% truncation artefact and
the file says so in PART 2 rather than leaving it to the reader -- ** the reduced numbers are
reported here as the THING BEING CORRECTED, not as measurements. **  *The one figure taken from the
2000 pair as a measurement is the SHELL LOCATION of the residual, which is what sent PART 2 looking
and does not depend on the tail being right.*

rc=0 on success.  Run: python3 P15_the_control_entered_the_regime_and_the_arm_did_not_move.py
                        (numpy scipy camb; ~60 s, mostly CAMB)
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


def grid(name):
    z = np.load(os.path.join(SP, name))
    ls = np.asarray(z['ls'], float)
    LF = np.arange(ls[0], ls[-1] + 1)
    return LF, np.interp(LF, ls, np.asarray(z['Dl'], float)), z


LFl, ARM, _zl = grid('c54.178_lcdm.npz')            # LMAXL = 2000
LFc, CRA, _zc = grid('c54.178_cr.npz')              # LMAXL = 2000
LF3, ARM3, _z3 = grid('c54.186_lcdm_L3000.npz')     # LMAXL = 3000, k-spacing held fixed
LFC3, CR3, _zc3 = grid('c54.186_cr_L3000.npz')      # LMAXL = 3000, the same for the CR arm

# --- CAMB's own LambdaCDM, lensed and unlensed, and the lensed/unlensed ratio c54.183 uses ---
import camb                                                                # noqa: E402
_p = camb.set_params(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9, tau=0.0544)
_p.set_for_lmax(3500, lens_potential_accuracy=1)
_pc = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK')
_Dlen, _Dunl = _pc['total'][:, 0], _pc['unlensed_total'][:, 0]
_Lc = np.arange(len(_Dlen))
_rat = np.ones_like(_Dlen)
_m = (_Lc >= 2) & (_Dunl > 0)
_rat[_m] = _Dlen[_m] / _Dunl[_m]


def LR(l):
    return np.interp(np.asarray(l, float), _Lc, _rat, left=1.0, right=_rat[-1])


CAMBL = np.interp(LFl, _Lc, _Dlen)
ARML = ARM * LR(LFl)                          # the arm carrying c54.183's derived lensing
LMAX0 = float(LFl[-1])                        # every comparison is scored on THESE bins

# =====================================================================
print("=" * 78)
print("PART 1 — WHERE THE CONTROL'S REMAINING chi^2 LIVES, IN SHELLS OF MULTIPOLE")
print("=" * 78)
CUTS = (700, 900, 1100, 1300, 1500, 1700, int(LMAX0))
print(f"  {'ell <=':>7} {'bins':>5} {'shell bins':>10} | {'arm+lensing':>11} {'shell':>8} | "
      f"{'CAMB lensed':>11} {'shell':>7}")
pa = pc = 0.0
pn = 0
SHELL = {}
for lm in CUTS:
    ca, na = CS.chi2_of(LFl, ARML, lmax=lm)[:2]
    cc, _ = CS.chi2_of(LFl, CAMBL, lmax=lm)[:2]
    SHELL[lm] = (ca, na, cc)
    print(f"  {lm:>7} {na:>5} {na-pn:>10} | {ca:>11.1f} {ca-pa:>8.1f} | {cc:>11.1f} {cc-pc:>7.1f}")
    pa, pc, pn = ca, cc, na
TOT, NB, CAMB_TOT = SHELL[int(LMAX0)]
TAIL = TOT - SHELL[1500][0]
NTAIL = NB - SHELL[1500][1]
print(f"\n  ** {TAIL:.0f} OF THE {TOT:.0f} — {TAIL/TOT:.0%} — IS IN THE {NTAIL} BINS ABOVE ell = 1500, "
      f"WHICH IS {NTAIL/NB:.0%} OF THE BINS. **")
print(f"     *and below ell = 700 the control is at chi^2/dof = {SHELL[700][0]/SHELL[700][1]:.2f}, "
      f"against CAMB's lensed {SHELL[700][2]/SHELL[700][1]:.2f} on the same bins.*")
if TAIL / TOT < 0.6:
    fail.append(f"only {TAIL/TOT:.0%} of the residual is above ell=1500 -- PART 1's claim is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — AND IT IS THE WAVENUMBER TRUNCATION, SHOWN BY REMOVING IT")
print("=" * 78)
print("  the grid is k = ell/D_M with ell <= LMAXL, so the TOP output multipole has no k above it")
print("  left to integrate over -- while C_ell draws on every k with k D_M >= ell.")
print(f"  banked control: LMAXL = 2000, {len(_zl['ls'])} multipoles to {LFl[-1]:.0f}")
print(f"  the same run at LMAXL = 3000 (k-spacing held fixed): {len(_z3['ls'])} to {LF3[-1]:.0f}")
print()
ARM3L = ARM3 * LR(LF3)
CAMB3 = np.interp(LF3, _Lc, _Dlen)
print(f"  {'ell band':>13} {'LMAXL=2000 / CAMB':>19} {'LMAXL=3000 / CAMB':>19}")
BANDS = ((100, 400), (400, 700), (700, 1000), (1000, 1300), (1300, 1700), (1700, int(LMAX0)))
RB = {}
for lo, hi in BANDS:
    out = []
    for LF, D, C in ((LFl, ARML, CAMBL), (LF3, ARM3L, CAMB3)):
        A1 = CS.chi2_of(LF, D, lmax=LMAX0)[2]
        A2 = CS.chi2_of(LF, C, lmax=LMAX0)[2]
        s = (LF >= lo) & (LF < hi)
        out.append(float(np.mean((A1 * D)[s] / (A2 * C)[s])))
    RB[(lo, hi)] = out
    print(f"  {f'{lo}-{hi}':>13} {out[0]:>19.4f} {out[1]:>19.4f}")
C2 = CS.chi2_of(LFl, ARML, lmax=LMAX0)
C3 = CS.chi2_of(LF3, ARM3L, lmax=LMAX0)
CC = CS.chi2_of(LFl, CAMBL, lmax=LMAX0)
print(f"\n  {'':>26} {'chi^2':>9} {'chi^2/dof':>11}   (the same {C2[1]} bins throughout)")
print(f"  {'control, LMAXL = 2000':>26} {C2[0]:>9.1f} {C2[0]/C2[1]:>11.2f}")
print(f"  {'control, LMAXL = 3000':>26} {C3[0]:>9.1f} {C3[0]/C3[1]:>11.2f}")
print(f"  {'CAMB lensed LambdaCDM':>26} {CC[0]:>9.1f} {CC[0]/CC[1]:>11.2f}")
_share = (C2[0] - C3[0]) / C2[0]
print(f"\n  ** THE TRUNCATION WAS {C2[0]-C3[0]:.0f} OF THE {C2[0]:.0f} — {_share:.0%} — AND THE LAST BAND'S "
      f"RATIO GOES {RB[(1700,int(LMAX0))][0]:.2f} -> {RB[(1700,int(LMAX0))][1]:.2f}. **")
print("     *A physical over-damping would not know where the grid ends.*")
print(f"  ⇒ ***FRONT #2's TARGET IS MET: the control is at chi^2/dof = {C3[0]/C3[1]:.2f} against a true "
      f"LambdaCDM fit's {CC[0]/CC[1]:.2f}\n     over ell = {LFl[0]:.0f}-{LMAX0:.0f}, and the last item on "
      f"the front's list is struck as NUMERICAL.***")
if _share < 0.5:
    fail.append(f"opening the wavenumber range recovers only {_share:.0%} -- PART 2's mechanism is "
                "not what the numbers show")
if C3[0] / C3[1] > 1.6:
    fail.append(f"the k-adequate control is at chi^2/dof = {C3[0]/C3[1]:.2f} -- front #2's target is "
                "NOT met and PART 2's closing line must be rewritten rather than patched")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE CR LADDER, WAIVED BY THE ALIAS GATE SINCE c54.178, CHECKED IN chi^2")
print("=" * 78)
LFk, CRK, _zk = grid('c54.186_cr_KCONT.npz')
print("  the gate demands 4 samples per Bessel period; the CR ladder has 2.3 and waives ITSELF with")
print("  \"this is not aliasing -- but it is only not aliasing if the answer does not depend on it\".")
print()
print(f"  {'':>26} {'l<700':>9} {'l<1300':>9} {'full':>9} {'peak1':>7} {'l1/lA':>8}")
_P = {}
for nm, LF, D, z in (('ladder (2.3 per period)', LFc, CRA, _zc),
                     ('continuum KCONT=1 (5.7)', LFk, CRK, _zk)):
    r = [CS.chi2_of(LF, D, lmax=lm) for lm in (700, 1300, None)]
    p1 = float(LF[argrelextrema(D, np.greater, order=3)[0][0]])
    _P[nm] = (r, p1 / float(z['l_A']))
    print(f"  {nm:>26} {r[0][0]/r[0][1]:>9.2f} {r[1][0]/r[1][1]:>9.2f} {r[2][0]/r[2][1]:>9.2f} "
          f"{int(p1):>7} {p1/float(z['l_A']):>8.4f}")
_dev = float(np.max(np.abs(np.interp(LFc, LFk, CRK) / CRA - 1.0)))
_dchi = abs(_P['continuum KCONT=1 (5.7)'][0][2][0] - _P['ladder (2.3 per period)'][0][2][0])
print(f"\n  ** THE TWO SPECTRA AGREE TO {100*_dev:.2f}% EVERYWHERE AND THE chi^2 TO {_dchi:.1f} IN "
      f"{_P['ladder (2.3 per period)'][0][2][0]:.0f}. **")
print("     ⇒ ***The waiver was right, and it is now checked on the statistic this file reads rather")
print("     than only on the peak position.***")
if _dev > 0.02 or _dchi > 20.0:
    fail.append(f"the ladder and the continuum differ by {100*_dev:.1f}% / {_dchi:.0f} in chi^2 -- "
                "the CR arm's projection depends on the discreteness and PART 5 is INADMISSIBLE")

# =====================================================================
print()
print("=" * 78)
print("PART 4 — FOUR INSTRUMENT STATES: THE CONTROL FOLLOWED THE SKY AND THE ARM DID NOT")
print("=" * 78)
print(f"  scored on the same {C2[1]} bins throughout, both arms carrying c54.183's lensing operator")
print()
print(f"  {'state':>44} | {'control':>9} {'CR arm':>9}")
STATES = (('c54.175  fluid, C = 8/9', 'c54.175_lcdm.npz', 'c54.175_cr.npz'),
          ('c54.177  fluid, derived C = 16/15', 'c54.177_lcdm.npz', 'c54.177_cr.npz'),
          ('c54.178  the polarised photon hierarchy', 'c54.178_lcdm.npz', 'c54.178_cr.npz'),
          ('c54.186  the same, wavenumber range opened',
           'c54.186_lcdm_L3000.npz', 'c54.186_cr_L3000.npz'))
TR = {}
for nm, fl, fc in STATES:
    row = []
    for f in (fl, fc):
        LF, D, _ = grid(f)
        c = CS.chi2_of(LF, D * LR(LF), lmax=LMAX0)
        row.append(c[0] / c[1])
    TR[nm[:7]] = row
    print(f"  {nm:>44} | {row[0]:>9.2f} {row[1]:>9.2f}")
_fc = TR['c54.175'][0] / TR['c54.186'][0]
_arm = [TR[k][1] for k in TR]
_fa = max(_arm) / min(_arm) - 1.0
print(f"\n  ** THE CONTROL IMPROVED BY A FACTOR OF {_fc:.0f} AND THE CR ARM MOVED BY {100*_fa:.0f}%. **")
print("     *Each state is a different physics content or a different numerical adequacy, not a")
print("     different setting.*")
print("  ⇒ ***An error the INSTRUMENT carries moves both arms.  This moved one.***")
if _fc < 5.0:
    fail.append(f"the control improved by only {_fc:.1f}x -- PART 4's contrast is not there")
if _fa > 0.15:
    fail.append(f"the CR arm moved {100*_fa:.0f}% across the four states -- it is not the fixed "
                "point PART 4 reports")

# =====================================================================
print()
print("=" * 78)
print("PART 5 — `L-147`'s PRE-REGISTERED F2 AND F3, WITH BOTH ARMS AT THE SAME WAVENUMBER RANGE")
print("=" * 78)
print("  F2 = chi^2(this instrument's LambdaCDM arm) - chi^2(CAMB)   [the instrument's own floor]")
print("  F3 = chi^2(CR arm) - chi^2(LambdaCDM arm), BOTH on this instrument")
print("  F4 = if F3 exceeds F2 by an order of magnitude, the disagreement is in the PHYSICS.")
print()
print(f"  {'lmax':>6} {'bins':>5} {'CAMB':>8} {'arm':>9} {'/dof':>6} {'CR':>10} | {'F2':>7} "
      f"{'F3':>10} {'F3/F2':>8}")
F = {}
for lm in (500, 700, 900, 1100, 1300, 1500, int(LMAX0)):
    cc = CS.chi2_of(LF3, CAMB3, lmax=lm)
    ca = CS.chi2_of(LF3, ARM3L, lmax=lm)
    cr = CS.chi2_of(LFC3, CR3, lmax=lm)         # the CR arm UNLENSED — its own better number
    F2, F3 = ca[0] - cc[0], cr[0] - ca[0]
    F[lm] = (F2, F3, ca[0] / ca[1])
    _r = f"{F3/F2:>8.0f}" if F2 > 0.5 else f"{'—':>8}"
    print(f"  {lm:>6} {ca[1]:>5} {cc[0]:>8.1f} {ca[0]:>9.1f} {ca[0]/ca[1]:>6.2f} {cr[0]:>10.1f} | "
          f"{F2:>7.1f} {F3:>10.1f} {_r}")
FULL = F[int(LMAX0)]
print(f"\n  ** AT FULL RANGE, WITH BOTH ARMS k-ADEQUATE: F2 = {FULL[0]:.0f} AND F3 = {FULL[1]:.0f}, "
      f"SO F4's SECOND\n     CLAUSE FIRES BY {FULL[1]/FULL[0]:.0f}x WHERE IT ASKS FOR 10. **")
print(f"  ** AND BELOW ell = 700, WHERE THE TRUNCATION CANNOT REACH EITHER ARM AT ALL: "
      f"F2 = {F[700][0]:.1f},\n     F3 = {F[700][1]:.0f}. **")
print("     *The CR arm is scored UNLENSED, which is its better number: c54.183's operator is")
print("     LambdaCDM's own lensed/unlensed ratio and applying it to the CR arm costs it rather")
print("     than helping.*")
print()
print("  ⛔ ***AND F5 IS NOT SOFTENED: this is a MEASUREMENT DISCREPANCY, not a framework verdict.")
print("     `PO-7` is protected precisely here, and the conversion runs by `F5`'s stated procedure.***")
if not (FULL[1] > 10 * max(FULL[0], 1e-9)):
    fail.append("F3 does not exceed F2 by an order of magnitude at full range -- F4 does NOT fire "
                "and this file's title is wrong")
if not (F[700][1] > 10 * max(F[700][0], 1e-9)):
    fail.append("F4 does not fire below ell=700 either")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — 73% of the control's residual was in the 16% of bins above ell = 1500, and")
print("opening the wavenumber range removes 78% of it: the control reaches chi^2/dof = 1.18 against a")
print("true LambdaCDM fit's 1.01 on the same bins, so front #2's target is met and its last item is")
print("struck as numerical.  The CR ladder's alias-gate waiver is checked in chi^2 and holds.  Four")
print("instrument states improved the control eighteenfold and moved the CR arm 5%.  And `L-147`'s F4")
print("fires by three orders of magnitude — as a MEASUREMENT DISCREPANCY, with `PO-7` protected and")
print("the conversion left where it belongs.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.186, `L-500`.  This file reopens `L-147`, so every load-bearing number is
# pinned and the two that could make the reading INADMISSIBLE fail loudly rather than degrade.
#   (1) the k-adequate control at full range -- if it is not ~1.2 there is no discriminating
#       regime and nothing below may be read;
#   (2) the share the truncation carried, which is PART 2's whole mechanism;
#   (3) F3/F2 at full range AND below ell = 700 -- F4's second clause, which is the reopening;
#   (4) the ladder/continuum agreement, WITHOUT which the CR arm's chi^2 is not admissible at all;
#   (5) the four-state contrast, which is what makes this a statement about physics rather than
#       about one build;
#   (6) and the tail share, since PART 1 is what sent PART 2 looking.
# ============================================================================================
_dof3 = C3[0] / C3[1]
assert abs(_dof3 - 1.18) < 0.12, f"the k-adequate control is at chi^2/dof = {_dof3:.2f}, expected 1.18"
assert _share > 0.6, f"the truncation carried only {_share:.0%} of the residual, expected ~78%"
assert FULL[1] / max(FULL[0], 1e-9) > 100.0, \
    f"F3/F2 at full range is {FULL[1]/FULL[0]:.0f}, expected >100"
assert F[700][1] / max(F[700][0], 1e-9) > 100.0, \
    f"F3/F2 below ell=700 is {F[700][1]/F[700][0]:.0f}, expected >100"
assert _dev < 0.02, f"the CR ladder and continuum differ by {100*_dev:.2f}% -- PART 5 inadmissible"
assert abs(_P['continuum KCONT=1 (5.7)'][1] - 0.5703) < 5e-4, \
    f"the continuum CR arm is at l_1/l_A = {_P['continuum KCONT=1 (5.7)'][1]:.4f}, expected 0.5703"
assert _fc > 5.0, f"the control improved only {_fc:.1f}x across the four states"
assert _fa < 0.15, f"the CR arm moved {100*_fa:.0f}% across the four states"
assert TAIL / TOT > 0.6, f"only {TAIL/TOT:.0%} of the residual is above ell=1500"
print(f"GATE c54.186 (r2441), `L-500`: opening the wavenumber range removes {_share:.0%} of the "
      f"control's residual and takes it to chi^2/dof = {_dof3:.2f} against CAMB's {CC[0]/CC[1]:.2f} on "
      f"{C3[1]} identical bins; F3 = {FULL[1]:.0f} against F2 = {FULL[0]:.0f} at full range and "
      f"{F[700][1]:.0f} against {F[700][0]:.1f} below ell=700, so F4 fires; the CR ladder waiver holds "
      f"to {100*_dev:.2f}%; four states improved the control {_fc:.0f}x while the CR arm moved "
      f"{100*_fa:.0f}% — pinned against `L-147` F2/F3/F4/F5 and THE_WORK front #2.")
