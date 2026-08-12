#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE DERIVED LENSING BUILD c54.181 TEED UP, RUN WITH NO FREE WIDTH -- AND IT COMES IN
UNDER THE FITTED SMOOTHING'S UPPER BOUND, WHICH IS WHAT A DERIVATION MUST DO. **

Built r2376+c54.183, front #2, continuing `P15_what_is_left_is_lensing_and_not_reionisation` (c54.181).

===================================================================================================
** WHY THIS EXISTS: c54.181 BOUGHT ~400 WITH A FITTED WIDTH AND CALLED THE DERIVED CALCULATION THE
   NEXT BUILD.  THIS IS THAT CALCULATION. **
===================================================================================================

c54.181 fitted a Gaussian smoothing whose width GROWS with ell and bought d(chi^2) = 400 on the
LCDM arm (1320 -> 921), and said in as many words: the width is FITTED, so the 400 BOUNDS what a
derived lensing has to play for -- a derivation has no free width and may return more or less.  ** So
a derived lensing that came in ABOVE 400 would not be a triumph, it would be evidence the operation
had a free parameter hiding in it. **

  PART A  ** THE OPERATOR AND THE PIPELINE, VALIDATED ON A SPECTRUM WHERE THE ANSWER IS KNOWN. **
          CAMB's own LCDM through this instrument's likelihood goes chi^2 = 615 unlensed -> 186
          lensed (chi^2/dof ~ 1.0).  So on a TRUE LCDM spectrum the derived lensing is worth
          d(chi^2) ~ 429, and the lensed curve fits -- which is the check that the non-perturbative
          lensing operator (CAMB's lensed/unlensed ratio) and the pipeline are both wired right.
  PART B  ** THE DERIVED LENSING ON THE CR INSTRUMENT'S OWN LCDM ARM, NO FREE PARAMETER. **  Apply
          the SAME operator -- LCDM's lensed/unlensed ratio -- to the c54.178 LCDM arm: 1320 -> 989,
          d(chi^2) = 331.  ** Under the 400 the fitted smoothing bounded, as a derivation must be. **
          The gain is concentrated in the damping tail (ell 1100-1500), where lensing fills the
          troughs a fixed-angle deflection has smeared -- exactly the ell-dependence c54.181's
          growing width was picking up.
  PART C  ** THE PEAKS DO NOT MOVE, AND THE CORPUS'S OWN FIRST-ORDER KERNEL OVERSHOOTS. **  Lensing
          shifts the acoustic peak POSITIONS by 0.0% (a smoothing does not move a peak, it lowers
          it); the effect is a contrast reduction.  And the first-order Hu (2000) kernel -- the
          corpus's `LENS_correction.py`, run here on the SAME C^phiphi so only the ORDER differs --
          buys 508, ABOVE the fitted bound, because it BREAKS DOWN in the damping tail: it returns a
          spurious +13% ENHANCEMENT at ell = 1900 where the full operator gives +6.5%.  ** That is
          why the derived number is the full operator's 331 and not the first order's 508: 508 is a
          kernel artefact, not a result about the sky. **
  PART D  ** WHAT SURVIVES, AND THE c54.181 VERDICT CONFIRMED FROM THE DERIVED SIDE. **  ~989 of the
          1320 survives derived lensing on the arm.  Lensing is real -- 331, a quarter of the excess
          -- and it is NOT the last build, which is exactly what c54.181 said the fitted bound
          implied.  *The remaining ~800 is the instrument's own transfer inaccuracy: CAMB's UNLENSED
          LCDM already sits at 615 on these bins while the arm's unlensed sits at 1320, and that gap
          is not lensing's to close.*

** WHAT THIS IS NOT. **  Not a measurement of the lensing amplitude (the operator is LCDM's, imposed
not fitted) and not a claim the CR arm now fits -- it does not.  It measures how much of c54.181's
fitted-smoothing headroom a genuine, zero-parameter lensing recovers, and the answer is most but not
all of it, with the shortfall against the fit being the fit's free width.  `PO-7` stays protected.

rc=0 on success.  Run: python3 P15_derived_lensing_on_the_lcdm_arm.py   (numpy scipy camb)
"""
import os
import sys

import numpy as np

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

# --- the LCDM arm: the CR instrument's own unlensed reproduction of LCDM (c54.178) ---
_z = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra', 'c54.178_lcdm.npz'))
LS, DL = np.asarray(_z['ls'], float), np.asarray(_z['Dl'], float)
BASE, NB = CS.chi2_of(LS, DL)[:2]
LF = np.arange(int(LS[0]), int(LS[-1]) + 1)
DF = np.interp(LF, LS, DL)

# --- CAMB LCDM: lensed, unlensed, and the lensing potential (Planck 2018 base) ---
import camb                                                               # noqa: E402
_p = camb.set_params(H0=67.36, ombh2=0.02237, omch2=0.1200, ns=0.9649, As=2.1e-9, tau=0.0544)
_p.set_for_lmax(2600, lens_potential_accuracy=4)
_r = camb.get_results(_p)
_pc = _r.get_cmb_power_spectra(_p, CMB_unit='muK', raw_cl=False)
_Dl_lensed = _pc['total'][:, 0]
_Dl_unlens = _pc['unlensed_total'][:, 0]
_Lc = np.arange(_Dl_lensed.shape[0])
_ratio = np.ones_like(_Dl_lensed)
_m = (_Lc >= 2) & (_Dl_unlens > 0)
_ratio[_m] = _Dl_lensed[_m] / _Dl_unlens[_m]      # LCDM's non-perturbative lensed/unlensed operator
# C^phiphi = [L(L+1)]^2 C_L^phiphi / 2pi  (the PP convention), for the first-order kernel below
_lp = _r.get_lens_potential_cls(2600)[:, 0]
_Lpp = np.arange(_lp.shape[0])


def _lcdm_ratio(l):
    return np.interp(np.asarray(l, float), _Lc, _ratio, left=1.0, right=_ratio[-1])


# =====================================================================
print("=" * 78)
print("PART A — the operator and pipeline validated on CAMB's own LCDM")
print("=" * 78)
_Lg = np.arange(int(LS[0]), int(LS[-1]) + 1)
cu = CS.chi2_of(_Lg, np.interp(_Lg, _Lc, _Dl_unlens))[0]
cl = CS.chi2_of(_Lg, np.interp(_Lg, _Lc, _Dl_lensed))[0]
print(f"  CAMB LCDM through this likelihood:  unlensed chi^2 = {cu:.1f}   lensed chi^2 = {cl:.1f}"
      f"  (chi^2/dof = {cl/NB:.2f})")
print(f"  ** derived lensing is worth d(chi^2) = {cu-cl:+.1f} on a TRUE LCDM spectrum, and the lensed")
print(f"     curve fits -- the operator and the pipeline are wired right. **")
if not (0.75 < cl / NB < 1.25):
    fail.append(f"lensed CAMB LCDM sits at chi^2/dof = {cl/NB:.2f}, not ~1 -- the pipeline or the "
                "operator is mis-wired and PART A's validation does not hold")
if cu - cl < 350:
    fail.append(f"lensing is worth only {cu-cl:.0f} on true LCDM -- below what PART A reports")

# =====================================================================
print()
print("=" * 78)
print("PART B — the derived lensing on the CR instrument's LCDM arm, no free width")
print("=" * 78)
DL_full = DF * _lcdm_ratio(LF)
cB = CS.chi2_of(LF, DL_full)[0]
dB = BASE - cB
print(f"  arm unlensed chi^2 = {BASE:.1f}  ->  +derived lensing chi^2 = {cB:.1f}   d(chi^2) = {dB:+.1f}")
print(f"  ** {dB:.0f} against the {400} the c54.181 fitted smoothing bounded -- UNDER it, as a")
print(f"     zero-parameter derivation must be. **")
_bands = [(100, 600), (600, 1100), (1100, 1500), (1500, 1997)]
print("  gain by ell band (the tail is where lensing lives):")
for lo, hi in _bands:
    _D2 = DF.copy(); _mk = (LF >= lo) & (LF < hi); _D2[_mk] = DL_full[_mk]
    print(f"      l[{lo:4d},{hi:4d}): d(chi^2) = {BASE - CS.chi2_of(LF, _D2)[0]:+7.1f}")
if not (280 < dB < 385):
    fail.append(f"derived lensing on the arm buys {dB:.0f} -- outside the range PART B reports")
if dB >= 400:
    fail.append(f"derived lensing buys {dB:.0f} >= the 400 the fitted width bounded -- a derivation "
                "with no free width cannot beat the fit; a free parameter is hiding in the operator")

# =====================================================================
print()
print("=" * 78)
print("PART C — the peaks do not move, and the first-order kernel overshoots via a tail artefact")
print("=" * 78)
from scipy.signal import argrelextrema                                    # noqa: E402
_pu = [int(LF[i]) for i in argrelextrema(DF, np.greater, order=8)[0] if 150 < LF[i] < 1300][:4]
_pl = [int(LF[i]) for i in argrelextrema(DL_full, np.greater, order=8)[0] if 150 < LF[i] < 1300][:4]
_shift = max(abs(a - b) / a for a, b in zip(_pu, _pl)) if len(_pu) == len(_pl) and _pu else 1.0
print(f"  acoustic peaks unlensed {_pu}  ->  +lensing {_pl}   max |shift| = {100*_shift:.2f}%")


def _first_order_ratio(lvals, nlp=420, nth=192):
    """Hu (2000) first order in C^phiphi, on the SAME CAMB C^phiphi -- only the ORDER differs."""
    def _Cpp(l):
        l = np.maximum(np.asarray(l, float), 2.0)
        pp = np.interp(l, _Lpp, _lp, left=_lp[2], right=_lp[-1])
        hi = l > _Lpp[-1]
        if np.any(hi):
            pp = np.where(hi, _lp[-1] * (_Lpp[-1] / np.maximum(l, 1.)) ** 2, pp)
        return 2 * np.pi * pp / (l * (l + 1)) ** 2
    _cttv = 2 * np.pi * DF / (LF * (LF + 1))
    def _Ctt(l):
        return np.interp(np.asarray(l, float), LF, _cttv, left=_cttv[0], right=_cttv[-1])
    lp = np.exp(np.linspace(np.log(2.), np.log(3000.), nlp))
    th = np.linspace(0, 2 * np.pi, nth, endpoint=False)
    dlp = np.gradient(lp); dth = th[1] - th[0]; out = []
    for L in lvals:
        LP, TH = np.meshgrid(lp, th, indexing='ij')
        dot = LP * L * np.cos(TH) - LP ** 2
        Lm = np.sqrt(np.maximum(L ** 2 + LP ** 2 - 2 * L * LP * np.cos(TH), 1e-6))
        integ = (dot ** 2) * _Cpp(Lm) * (_Ctt(LP) - _Ctt(L)) * LP
        out.append(1.0 + np.sum(integ * dlp[:, None] * dth) / (2 * np.pi) ** 2 / _Ctt(L))
    return np.array(out)


_r1 = _first_order_ratio(LF)
cC = CS.chi2_of(LF, DF * _r1)[0]
dC = BASE - cC
_r1_1900 = float(np.interp(1900, LF, _r1))
_rf_1900 = float(_lcdm_ratio(1900))
print(f"  first-order Hu kernel:  chi^2 = {cC:.1f}   d(chi^2) = {dC:+.1f}   (ABOVE the fitted 400)")
print(f"  the tail breakdown:  at l=1900 first order = {_r1_1900:.3f} (+{100*(_r1_1900-1):.0f}%) "
      f"vs full = {_rf_1900:.3f} (+{100*(_rf_1900-1):.1f}%)")
print(f"  ** so the {dC:.0f} is the kernel breaking down, not the sky; the derived number is the")
print(f"     full operator's {dB:.0f}. **")
if _shift > 0.003:
    fail.append(f"lensing shifted a peak by {100*_shift:.1f}% -- a smoothing does not move peaks; "
                "PART C's position claim is wrong or the peak finder is")
if dC <= dB + 80:
    fail.append(f"the first-order kernel ({dC:.0f}) does not overshoot the full operator ({dB:.0f}) "
                "-- PART C's whole point (the tail artefact) is not reproduced")
if not (_r1_1900 > 1.10 and _rf_1900 < 1.10):
    fail.append(f"the tail artefact is not present as PART C describes: first order {_r1_1900:.3f}, "
                f"full {_rf_1900:.3f} at l=1900")

# =====================================================================
print()
print("=" * 78)
print("PART D — what survives, and c54.181's verdict confirmed from the derived side")
print("=" * 78)
print(f"  the arm control is at chi^2 = {BASE:.0f}; derived lensing leaves {cB:.0f} ({cB/NB:.2f}/dof)")
print(f"  ** ~{cB:.0f} of {BASE:.0f} survives -- lensing is real ({dB:.0f}) and NOT the last build. **")
print(f"  *the residual is transfer inaccuracy: CAMB's UNLENSED LCDM sits at {cu:.0f} on these bins")
print(f"   while the arm's unlensed sits at {BASE:.0f}; that ~{BASE-cu:.0f} gap is not lensing's.*")
if cB < 0.6 * BASE:
    fail.append(f"only {cB:.0f} of {BASE:.0f} survives -- PART D understates lensing and needs a "
                "rewrite rather than a patch")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print(f"ALL CHECKS PASS — derived lensing buys {dB:.0f} on the LCDM arm (under the fitted 400), the")
print(f"peaks do not move, the first-order kernel overshoots to {dC:.0f} via a tail artefact, and "
      f"~{cB:.0f} survives.")
print("=" * 78)

# ============================================================================================
# GATE — r2376+c54.183.  Each number front #2 rests on is pinned, with tolerances wide enough to
# survive a CAMB point release but narrow enough to fail on a wrong result.
#   (1) lensed CAMB LCDM fits (chi^2/dof ~ 1) -- the operator and pipeline are validated;
#   (2) the derived lensing on the arm is UNDER the c54.181 fitted bound of 400 -- the defining
#       property of a zero-parameter derivation against a fitted upper bound;
#   (3) the first-order kernel OVERSHOOTS it via the tail artefact -- the reason the derived number
#       is the full operator's, and a live check that the corpus's own LENS_correction is first order.
# ============================================================================================
assert 0.75 < cl / NB < 1.25, f"lensed CAMB LCDM at chi^2/dof = {cl/NB:.2f}, expected ~1"
assert cu - cl > 350, f"lensing worth only {cu-cl:.0f} on true LCDM, expected ~429"
assert 280 < dB < 385, f"derived lensing on the arm buys {dB:.1f}, expected ~331"
assert dB < 400, f"derived lensing {dB:.0f} is not under the c54.181 fitted bound of 400"
assert dC > dB + 80, f"first-order kernel {dC:.0f} does not overshoot the full operator {dB:.0f}"
assert _r1_1900 > 1.10 > _rf_1900, (f"tail artefact absent: first order {_r1_1900:.3f}, "
                                    f"full {_rf_1900:.3f} at l=1900")
assert _shift < 0.003, f"lensing shifted a peak by {100*_shift:.2f}%, expected ~0"
print(f"GATE c54.183 (r2376): lensed LCDM chi^2/dof = {cl/NB:.2f}; derived lensing on the arm "
      f"{BASE:.0f} -> {cB:.0f} (d = {dB:.0f}, under the fitted 400); first order overshoots to "
      f"{dC:.0f} via a +{100*(_r1_1900-1):.0f}% l=1900 tail artefact; peaks move {100*_shift:.2f}%. "
      f"Pinned against THE_WORK front #2.")
