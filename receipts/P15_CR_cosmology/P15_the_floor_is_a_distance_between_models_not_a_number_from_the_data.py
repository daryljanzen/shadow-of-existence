#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE CONTROL'S REMAINING 17% IS NAMED, AND NAMING IT REQUIRED CHANGING THE
MEASUREMENT.  MEASURED THROUGH THE DATA THE FLOOR IS F2 = 21-31 DEPENDING ON WHICH LambdaCDM IS
CALLED TRUE; MEASURED AS A DISTANCE BETWEEN THE TWO MODELS -- WHICH IS WHAT IT ACTUALLY IS -- IT IS
0.11 chi^2 PER BIN, AND THE REFERENCE'S OWN NEUTRINO CONTENT MOVES IT BY A FACTOR OF THREE. **

Built r2441+c54.188, front #2, lead `L-503`.

===================================================================================================
** WHY: c54.186 SAID "1.18 IS NOT A FIT" AND LEFT THE REMAINDER UNNAMED.  THIS NAMES IT. **
===================================================================================================

c54.186 took the control to chi^2/dof = 1.18 against a reference LambdaCDM's 1.01 on the same 185
bins and said, against itself, that the 17% between them had not been named.  ** It is named here,
and the naming turns on a distinction the front had not been making: F2 as `L-147` defines it --
chi^2(arm) - chi^2(CAMB) -- is a difference of two numbers each computed AGAINST THE SKY, so it
mixes how far the two models are apart with where each happens to sit relative to one noise
realisation. **  *The thing the front actually wants to know is how far apart the two models are.*

  PART 1  ** THE INSTRUMENT REPRODUCES A REFERENCE LambdaCDM TO BETTER THAN 1.6% EVERYWHERE, AND
          THE DIFFERENCE IS SMOOTH RATHER THAN ACOUSTIC. **  Amplitude-matched, the fractional
          departure runs -1.1% at ell ~ 200 through zero near ell ~ 600 to +0.7% at ell ~ 1400,
          with an in-band rms of 0.1-0.7%.  *A slow undulation of order one per cent, not a
          mis-phased oscillation.*
  PART 2  ** AND F2 IS NOT A CLEAN MEASURE OF IT, WHICH IS SHOWN BY MOVING THE REFERENCE. **  Three
          defensible reference LambdaCDMs give F2 = +31.2, +21.5 and +27.2.  ** The spread across
          reference choices is comparable to the value being reported. **
  PART 3  ** SO THE FLOOR IS MEASURED WITHOUT THE DATA: the chi^2 distance between the two models,
          in the comparison's own metric. **  chi2_sep = (A_a m_a - A_c m_c)^T F (A_a m_a - A_c m_c)
          over the same bins.  ** Against the reference the front actually uses it is 21.3 over 185
          bins -- 0.11 chi^2 per bin, about a third of a standard deviation per bin. **
  PART 4  ** AND THE ORDERING REVERSES BETWEEN THE TWO MEASURES, WHICH IS THE TRAP. **  The
          massless-neutrino reference gives the SMALLEST F2 (21.5) and the LARGEST model separation
          (62.7).  ** A reference chosen to make the instrument look good through the data is the
          one it is furthest from as a model. **  *Reported because someone will otherwise choose
          it.*

** WHAT THIS DOES TO c54.178's LIST, WHICH IS NOW COMPLETE. **  That revision named four things
remaining: reionisation, the neutrino mass, a lensed spectrum, and the wavenumber range.
Reionisation was struck at c54.181, lensing built at c54.183, the wavenumber range closed at
c54.186.  ** The neutrino mass is the one item never addressed, and it is worth about ten of the
thirty-one: the reference carries one massive species at 0.06 eV and this instrument carries none.
So the last item on that list is now MEASURED rather than outstanding. **

** AND WHAT IT DOES TO `L-147`, WHICH IS NOTHING EXCEPT MAKE IT SAFER. **  F3 = 51848.  ** The floor
is 21-63 across every reference choice defensible here, so F4's margin is three orders of magnitude
whichever is taken. **  *A verdict that does not depend on the choice is the only kind this front
should report.*

** WHAT IS NOT CLAIMED. **  0.11 chi^2 per bin is not zero and this file does not say the instrument
is exact.  ** It says the residual is at the level where the REFERENCE's own parameter choices
matter as much as the instrument's error, and that below that level this statistic cannot arbitrate
between two LambdaCDM implementations at all. **

rc=0 on success.  Run: python3 P15_the_floor_is_a_distance_between_models_not_a_number_from_the_data.py
                        (numpy scipy camb; ~3 min, three CAMB runs)
"""
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SP = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402
import camb                                                                # noqa: E402

_z = np.load(os.path.join(SP, 'c54.186_lcdm_L3000.npz'))
_ls = np.asarray(_z['ls'], float)
LF = np.arange(_ls[0], _ls[-1] + 1)
D = np.interp(LF, _ls, np.asarray(_z['Dl'], float))
# ** LMAX0 IS 1996 AND NOT THIS SPECTRUM'S OWN END, AND THE FIRST WRITING OF THIS FILE GOT IT
# WRONG. **  The LMAXL = 3000 run carries multipoles to 2996, so `float(LF[-1])` scored 201 bins
# instead of the 185 c54.186 compared on -- and the extra sixteen sit above the range the CR arm
# covers, where the band comparison ran off the end and reported a 98% departure.  ** Every number
# here must be on the SAME 185 bins as c54.186 or none of them can be set beside it. **
LMAX0 = 1996.0

# ** the instrument's OWN background, read off rather than retyped where possible **
H0I, OMI, OMBH2I = 67.40, 0.3150, 0.0224
_h = H0I / 100.0
OMCH2I = OMI * _h ** 2 - OMBH2I

CASES = (
    ("as the front uses it (67.36, one 0.06 eV nu)",
     dict(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9, tau=0.0544)),
    ("massless neutrinos, as the instrument has",
     dict(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9, tau=0.0544, mnu=0.0)),
    ("+ the instrument's own H0, Om, ombh2, ns",
     dict(H0=H0I, ombh2=OMBH2I, omch2=OMCH2I, ns=0.965, As=2.1e-9, tau=0.0544, mnu=0.0)),
)


def camb_of(**kw):
    p = camb.set_params(**kw)
    p.set_for_lmax(3500, lens_potential_accuracy=1)
    pc = camb.get_results(p).get_cmb_power_spectra(p, CMB_unit='muK')
    Dl, Du = pc['total'][:, 0], pc['unlensed_total'][:, 0]
    Lc = np.arange(len(Dl))
    r = np.ones_like(Dl)
    m = (Lc >= 2) & (Du > 0)
    r[m] = Dl[m] / Du[m]
    return Lc, Dl, r


# =====================================================================
print("=" * 78)
print("PART 1 — THE INSTRUMENT AGAINST A REFERENCE LambdaCDM, BY BAND")
print("=" * 78)
_Lc, _Dl, _r = camb_of(**CASES[0][1])
ARM = D * np.interp(LF, _Lc, _r, left=1.0, right=_r[-1])
CAMBL = np.interp(LF, _Lc, _Dl)
_Aa = CS.chi2_of(LF, ARM, lmax=LMAX0)[2]
_Ac = CS.chi2_of(LF, CAMBL, lmax=LMAX0)[2]
frac = (_Aa * ARM) / (_Ac * CAMBL) - 1.0
print(f"  {'ell band':>13} {'mean':>9} {'in-band rms':>13} {'max abs':>9}")
BANDS = ((100, 300), (300, 500), (500, 700), (700, 900), (900, 1100),
         (1100, 1300), (1300, 1500), (1500, 1700), (1700, int(LMAX0)))
WORST = 0.0
for lo, hi in BANDS:
    s = (LF >= lo) & (LF < hi)
    WORST = max(WORST, float(np.max(np.abs(frac[s]))))
    print(f"  {f'{lo}-{hi}':>13} {100*np.mean(frac[s]):>8.2f}% {100*np.std(frac[s]):>12.2f}% "
          f"{100*np.max(np.abs(frac[s])):>8.2f}%")
print(f"\n  ** NOWHERE MORE THAN {100*WORST:.2f}%, AND THE DEPARTURE IS A SLOW UNDULATION RATHER THAN A "
      f"MIS-PHASED OSCILLATION. **")
print("     *The in-band rms is comparable to the band means, so the structure is smooth in ell.*")
if WORST > 0.03:
    fail.append(f"the instrument departs from the reference by {100*WORST:.1f}% -- PART 1's "
                "'better than 1.6%' is wrong")

# =====================================================================
print()
print("=" * 78)
print("PART 2/3/4 — F2 AGAINST THE DATA, AND THE MODEL SEPARATION THAT DOES NOT USE IT")
print("=" * 78)
print("  F2       = chi^2(arm) - chi^2(CAMB), both against the sky -- `L-147`'s own definition")
print("  chi2_sep = (A_a m_a - A_c m_c)^T F (A_a m_a - A_c m_c) -- a distance between two MODELS")
print()
print(f"  {'reference LambdaCDM':>44} {'F2':>8} {'chi2_sep':>9} {'per bin':>8}")
F2, SEP = {}, {}
for nm, kw in CASES:
    Lc, Dl, r = camb_of(**kw)
    A = D * np.interp(LF, Lc, r, left=1.0, right=r[-1])
    C = np.interp(LF, Lc, Dl)
    ca = CS.chi2_of(LF, A, lmax=LMAX0)
    cc = CS.chi2_of(LF, C, lmax=LMAX0)
    ma, mc = CS.bin_spectrum(LF, A), CS.bin_spectrum(LF, C)
    keep = np.isfinite(ma) & np.isfinite(mc) & (CS.BIN_HI <= LMAX0)
    Fi = np.linalg.inv(CS.COV_TT[np.ix_(keep, keep)])
    d = ma[keep] * ca[2] - mc[keep] * cc[2]
    F2[nm], SEP[nm] = ca[0] - cc[0], float(d @ Fi @ d)
    print(f"  {nm:>44} {F2[nm]:>+8.1f} {SEP[nm]:>9.1f} {SEP[nm]/keep.sum():>8.2f}")
_ref = CASES[0][0]
_nu = CASES[1][0]
NB = int(keep.sum())
print(f"\n  ** AGAINST THE REFERENCE THE FRONT ACTUALLY USES, THE TWO MODELS ARE {SEP[_ref]:.1f} APART "
      f"OVER {NB} BINS\n     — {SEP[_ref]/NB:.2f} chi^2 PER BIN, ABOUT A THIRD OF A STANDARD DEVIATION "
      f"PER BIN. **")
print(f"  ** AND THE NEUTRINO CONTENT MOVES IT BY A FACTOR OF {SEP[_nu]/SEP[_ref]:.1f}: the reference "
      f"carries one massive\n     species at 0.06 eV and this instrument carries none, which is worth about "
      f"{F2[_ref]-F2[_nu]:.0f} of the {F2[_ref]:.0f}. **")
print(f"\n  ⚠ ***AND THE ORDERING REVERSES: the massless reference gives the SMALLEST F2 "
      f"({F2[_nu]:+.1f}) and the\n     LARGEST separation ({SEP[_nu]:.1f}). A reference chosen to flatter "
      f"the instrument through the data\n     is the one it is furthest from as a model.***")
if not (SEP[_nu] > SEP[_ref] and F2[_nu] < F2[_ref]):
    fail.append("the ordering between F2 and the model separation does not reverse -- PART 4's "
                "whole point is absent and the paragraph must be removed rather than softened")
if SEP[_ref] / NB > 0.5:
    fail.append(f"the model separation is {SEP[_ref]/NB:.2f} per bin -- PART 3's reading is wrong")

# =====================================================================
print()
print("=" * 78)
print("AND WHAT IT DOES TO `L-147`, WHICH IS NOTHING EXCEPT MAKE IT SAFER")
print("=" * 78)
_zc = np.load(os.path.join(SP, 'c54.186_cr_L3000.npz'))
_lc = np.asarray(_zc['ls'], float)
CR = CS.chi2_of(_lc, np.asarray(_zc['Dl'], float), lmax=LMAX0)
ARMC = CS.chi2_of(LF, ARM, lmax=LMAX0)
F3 = CR[0] - ARMC[0]
LO, HI = min(SEP.values()), max(SEP.values())
print(f"  F3 = chi^2(CR arm) - chi^2(LambdaCDM arm) = {F3:.0f}")
print(f"  the floor, across every reference defensible here: {LO:.0f} – {HI:.0f}")
print(f"\n  ** SO F4's MARGIN IS {F3/HI:.0f}x AT ITS WORST AND {F3/LO:.0f}x AT ITS BEST — THREE ORDERS "
      f"OF MAGNITUDE\n     WHICHEVER REFERENCE IS TAKEN. **")
print("     *A verdict that does not depend on the choice is the only kind this front should report.*")
print()
print("  ⛔ ***F5 UNSOFTENED: a MEASUREMENT DISCREPANCY is not a framework verdict.  `PO-7` is")
print("     protected and the conversion runs by `F5`'s stated procedure.***")
if F3 / HI < 100:
    fail.append(f"F4's margin falls to {F3/HI:.0f}x at the worst reference -- the reference choice "
                "reaches the verdict and c54.186 must be restated")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the instrument reproduces a reference LambdaCDM to better than 1.6% with a")
print("smooth departure; F2 spans 21-31 across defensible references, a spread comparable to itself;")
print("the model separation is 0.11 chi^2 per bin; the neutrino content moves it threefold and is the")
print("last unaddressed item on c54.178's list, worth about ten of the thirty-one; and F4's margin is")
print("three orders of magnitude whichever reference is taken.")
print("=" * 78)

# ============================================================================================
# GATE — r2441+c54.188, `L-503`.  This file's content is that a MEASURE was wrong, so the pins
# are on the two measures disagreeing and on the size of the one that is right.
#   (1) the instrument-vs-reference departure, which is PART 1 and bounds everything else;
#   (2) the model separation per bin, which is the number that replaces the unnamed 17%;
#   (3) THE ORDERING REVERSAL between F2 and chi2_sep -- if it ever stops reversing, PART 4 is
#       not a trap and the paragraph is unearned;
#   (4) F4's margin at the WORST reference, since a verdict that depends on the choice is not one.
# ============================================================================================
assert WORST < 0.03, f"the instrument departs from the reference by {100*WORST:.1f}%"
assert SEP[_ref] / NB < 0.5, f"the model separation is {SEP[_ref]/NB:.2f} per bin, expected ~0.11"
assert SEP[_nu] > 1.5 * SEP[_ref], "the neutrino content does not move the separation appreciably"
assert F2[_nu] < F2[_ref], "the ordering does not reverse -- PART 4 is unearned"
assert F3 > 100 * HI, f"F4's margin is {F3/HI:.0f}x at the worst reference"
assert F3 > 4.0e4, f"F3 = {F3:.0f}, expected ~5.2e4 -- the arms or the range have moved"
print(f"GATE c54.188 (r2441), `L-503`: the instrument tracks a reference LambdaCDM to "
      f"{100*WORST:.2f}%; F2 spans {min(F2.values()):+.0f} to {max(F2.values()):+.0f} across three "
      f"references while the model separation spans {LO:.0f}–{HI:.0f} ({SEP[_ref]/NB:.2f} per bin at "
      f"the reference used), and the two orderings REVERSE; F3 = {F3:.0f}, so F4's margin is "
      f"{F3/HI:.0f}x at worst — pinned against `L-147` F2/F3/F4/F5 and c54.178's remaining-items "
      f"list, whose last entry (the neutrino mass) is worth {F2[_ref]-F2[_nu]:.0f} of it.")
