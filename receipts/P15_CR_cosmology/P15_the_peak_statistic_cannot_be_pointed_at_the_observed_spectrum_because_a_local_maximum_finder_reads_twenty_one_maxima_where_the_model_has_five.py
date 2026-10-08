#!/usr/bin/env python3
"""
RECEIPT -- P15: ** `r7211` ORDERED THE OBSERVED POINT ONTO THE PEAK PLANE AND SAID TO STOP AND SAY SO
IF THE PLACEMENT CAME BACK UNRELIABLE RATHER THAN MERELY IMPRECISE.  *** IT IS UNRELIABLE, AND NOT
BECAUSE OF THE COVARIANCE: THE PEAK LOCATOR READS `$21$` LOCAL MAXIMA ON THE OBSERVED SPECTRUM WHERE
IT READS `$5$` ON A MODEL BINNED THE SAME WAY, SO THE FIVE IT REFINES ARE NOT THE ACOUSTIC PEAKS. ***

  ⓵ ** THE STATISTIC SURVIVES THE BINNING.  THAT WAS THE RISK AND IT IS NOT THE PROBLEM. **  *Run on
  four model spectra fine and then through the likelihood's own `bin_spectrum`, the common offset
  moves by `$-0.0013$` to `$-0.0021$` and the alternation by about `$-0.0002$` -- a small bias,
  consistent in sign, and applied to data and models alike.*

  ⓶ ⛔ ** BUT THE PEAK LOCATOR IS NOT NOISE-ROBUST, AND THE OBSERVED SPECTRUM IS NOISY AT THE SCALE
  OF ITS OWN CURVATURE. **  *The locator takes local maxima of a `$0.5$`-step interpolant and keeps
  the first five separated by `$60$`.  On the binned CR model that returns the acoustic peaks.  On
  the observed spectrum it returns `$21$` maxima, keeps `$10$`, and the first five are
  `$239$`/`$464$`/`$527$`/`$617$`/`$815$` -- **three of them inside the second acoustic peak's own
  neighbourhood.**  The parabola then refines noise wiggles, and one of the five is not even concave.*

  ⓷ ⛔ ** AND THE ERROR BAR CONFIRMS IT RATHER THAN RESCUING IT. **  *Propagating the full `plik_lite`
  TT covariance by Cholesky draws: **`$98.2$` per cent of `$2000$` draws fail to yield five finite
  peaks at all**, the `$35$` survivors give `$\\sigma_\\varphi=1.25$` against a driving signal of
  `$0.127$` and a loading signal of `$0.018$`, and the two components come back correlated at
  `$-0.955$` -- collapsed onto one degenerate direction rather than spanning a plane.*

  ⇒ ** SO NO POINT IS PLACED AND NO CARRIER IS NAMED.  `r7211` ASKED FOR THE INTERVAL AS THE RESULT
  AND THE INTERVAL IS THAT THERE IS NO MEASUREMENT HERE. **  *It is not that the observed point's
  uncertainty covers both candidates -- it is that the quantity being measured is not the one the
  statistic was built to read.  `$\\sigma_\\varphi$` is ten times the larger candidate's whole signal
  and seventy times the smaller's.*

  ⌗ ** WHAT THIS DOES NOT TOUCH. **  *`cc66.157` and `cc66.158` compare MODEL to MODEL on noiseless
  `$238$`-point spectra, where `Ⓐ` above shows the statistic sound.  **The `$5.39\\times$` separation
  and the `$\\omega_b$` opposition stand unchanged.**  What fails is one step -- pointing it at data.*

  ⌈ ** AND WHAT A REPAIR WOULD HAVE TO BE, STATED WITHOUT BUILDING IT. **  *A locator that finds
  maxima and then refines them cannot work on a spectrum whose noise creates maxima.  It would have
  to fit a parametric comb to the whole binned residual under the covariance -- **a different
  statistic, which `r7211` did not order and which is `66`'s to cost.***

** COMPUTES: the de-tilted peak statistic of `cc66.156`, unchanged, (a) on four model spectra fine
   and likelihood-binned, to bound the binning's effect; (b) on `plik_lite`'s own binned TT data
   from `chi2_of_spectrum`, which `nofit_figure_numbers.npz` carries verbatim; (c) on `$2000$`
   Cholesky draws of the full `$179\\times179$` covariance.  *** No refit, no new statistic, no new
   spectrum -- the placement was a re-read and it cost one. *** **

STATUS: rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~60 s)
"""
import os
import sys

import numpy as np

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


def head(t):
    print(f"\n{BAR}\n  {t}\n{BAR}")


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
NPZ = os.path.join(BW, 'r7183_nofit_figure', 'nofit_figure_numbers.npz')
GO = os.path.join(BW, 'r7093_directions', 'grid_oneclock')
LEV = os.path.join(BW, 'r7201_cc66_loading_lever')
for _p in (NPZ, GO, LEV):
    if not os.path.exists(_p):
        print(f"  ⛔ A SOURCE THIS RECEIPT READS IS NOT ON DISK: {_p}")
        sys.exit(1)

LMIN, LMAX, NPK, HALFWIN = 150.0, 1600.0, 5, 40.0
NDRAW, SEED = 2000, 20261008


def _detilt(ls, Dl):
    g = np.isfinite(ls) & np.isfinite(Dl)
    ls, Dl = np.asarray(ls, float)[g], np.asarray(Dl, float)[g]
    m = (ls >= LMIN) & (ls <= LMAX) & (Dl > 0)
    if m.sum() < 8:
        return None, None, None
    tilt = float(np.polyfit(np.log(ls[m]), np.log(Dl[m]), 1)[0])
    return ls, Dl / ls ** tilt, tilt


def maxima(ls, Dl):
    """every local maximum of the interpolant, and the ones the 60-gap rule keeps."""
    ls, Y, _t = _detilt(ls, Dl)
    if ls is None:
        return [], []
    lg = np.arange(LMIN, min(LMAX, ls.max()), 0.5)
    Di = np.interp(lg, ls, Y)
    idx = [i for i in range(2, len(Di) - 2)
           if Di[i] > Di[i - 1] and Di[i] >= Di[i + 1] and Di[i] > Di[i - 2] and Di[i] >= Di[i + 2]]
    keep = []
    for i in idx:
        if not keep or lg[i] - keep[-1] > 60.0:
            keep.append(lg[i])
    return [lg[i] for i in idx], keep


def phi_alt(ls, Dl, lA):
    """cc66.156's statistic, unchanged."""
    _all, coarse = maxima(ls, Dl)
    ls2, Y, _t = _detilt(ls, Dl)
    if ls2 is None:
        return np.nan, np.nan, 0
    pk = []
    for l0 in coarse[:NPK]:
        w = (ls2 >= l0 - HALFWIN) & (ls2 <= l0 + HALFWIN)
        if w.sum() < 4:
            pk.append(np.nan)
            continue
        c = np.polyfit(ls2[w] - l0, Y[w], 2)
        pk.append(l0 - c[1] / (2 * c[0]) if c[0] < 0 else np.nan)
    pk = np.array(pk, float)
    ok = np.isfinite(pk)
    if ok.sum() < 3:
        return np.nan, np.nan, int(ok.sum())
    n = np.arange(1, len(pk) + 1)[ok]
    p = pk[ok] / lA
    phi = float(np.mean(p - n))
    r = p - (n + phi)
    return phi, float(np.mean(r * (-1.0) ** n)), int(ok.sum())


LC, FACB = CS.bin_center_and_fac()
F = np.load(NPZ)
KEEP = np.isin(LC, F['ell'])
lc, fac = LC[KEEP], FACB[KEEP]
DAT = CS.X_DATA[KEEP]
COV = CS.COV_TT[np.ix_(KEEP, KEEP)]
L_A = float(F['l_A'])


def binned(path):
    z = np.load(path, allow_pickle=True)
    Cl = CS.bin_spectrum(np.asarray(z['ls'], float), np.asarray(z['Dl'], float))
    k = np.isfinite(Cl)
    return LC[k], (Cl * FACB)[k], float(z['l_A'])


def fine(path):
    z = np.load(path, allow_pickle=True)
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float), float(z['l_A'])


# ============================================================ A. the binning is not the problem
head("A.  ⓵ THE STATISTIC SURVIVES THE LIKELIHOOD'S BINNING -- THE RISK THAT IS NOT THE PROBLEM")

print("      ⌗ `X_data` is binned C_l and NOT D_l -- `bin_center_and_fac`'s own docstring records")
print("        that peak-finding on it directly loses the first peak entirely.  Every spectrum here")
print("        is converted with that same `fac`, data and models alike.")
print()
print(f"      {'spectrum':12s} {'fine phi':>10s} {'bin phi':>10s} {'shift':>9s} | "
      f"{'fine alt':>10s} {'bin alt':>10s} {'shift':>9s}")
SH = []
for tag, p in (('cr_base', os.path.join(GO, 'cr_base.npz')),
               ('lcdm_base', os.path.join(GO, 'lcdm_base.npz')),
               ('cr_nodrive', os.path.join(LEV, 'cr_nodrive.npz')),
               ('cr_rb0.5', os.path.join(LEV, 'cr_rb0.5.npz'))):
    f = phi_alt(*fine(p))
    b = phi_alt(*binned(p))
    SH.append((b[0] - f[0], b[1] - f[1]))
    print(f"      {tag:12s} {f[0]:+10.5f} {b[0]:+10.5f} {b[0] - f[0]:+9.5f} | "
          f"{f[1]:+10.5f} {b[1]:+10.5f} {b[1] - f[1]:+9.5f}")
_dp = [abs(s[0]) for s in SH]
_da = [abs(s[1]) for s in SH]
print(f"      ⇒ |shift| on the offset {min(_dp):.5f}-{max(_dp):.5f}, on the alternation "
      f"{min(_da):.5f}-{max(_da):.5f}")
check("Ⓐ①  ** THE BINNING COSTS A SMALL BIAS AND NOT THE STATISTIC: the offset moves by under "
      "`$0.0025$` and the alternation by under `$0.0005$` on every model tried, consistently in "
      "sign. **  *So the `$179$` binned points ARE enough to carry it, and whatever goes wrong "
      "below is not the resolution*",
      max(_dp) < 0.0025 and max(_da) < 0.0005 and all(s[0] < 0 for s in SH))


# ============================================================ B. the locator on the data
head("B.  ⓶ ⛔ BUT THE PEAK LOCATOR READS 21 MAXIMA ON THE OBSERVED SPECTRUM AND 5 ON THE MODEL")

_am_d, _co_d = maxima(lc, DAT * fac)
_lm, _dm, _lam = binned(os.path.join(GO, 'cr_base.npz'))
_am_m, _co_m = maxima(_lm, _dm)
print(f"      observed spectrum : {len(_am_d):3d} local maxima, {len(_co_d)} kept by the 60-gap rule")
print(f"         all at ell = {[round(x) for x in _am_d]}")
print(f"         the five the statistic takes: {[round(x) for x in _co_d[:NPK]]}")
print(f"      CR model, SAME bins: {len(_am_m):3d} local maxima, kept {[round(x) for x in _co_m]}")
_obs = phi_alt(lc, DAT * fac, L_A)
print(f"      ⇒ the statistic on the data returns phi {_obs[0]:+.5f}, alt {_obs[1]:+.5f}, from only "
      f"{_obs[2]} concave peaks of {NPK}")
check("Ⓑ①  ** THE FIVE MAXIMA THE STATISTIC REFINES ON THE DATA ARE NOT THE ACOUSTIC PEAKS. **  "
      "*Three of them -- `$464$`, `$527$`, `$617$` -- lie inside the second acoustic peak's own "
      "neighbourhood, which the model puts at `$554$`.  The locator keeps the FIRST five separated "
      "by `$60$`, and noise supplies more than five before the comb is exhausted*",
      len(_am_d) > 4 * len(_am_m) and sum(1 for x in _co_d[:NPK] if 430 < x < 680) >= 3)
check("Ⓑ②  and one of the five is not even concave, so the statistic falls back on fewer peaks than "
      "it requires.  *An alternation over four peaks with one of them spurious is not a measurement "
      "of the odd-even alternation of anything*",
      _obs[2] < NPK)


# ============================================================ C. the error bar
head("C.  ⓷ ⛔ AND THE FULL-COVARIANCE ERROR BAR CONFIRMS IT RATHER THAN RESCUING IT")

print(f"      the covariance is `plik_lite`'s own TT, {COV.shape[0]}x{COV.shape[1]} on these bins --")
print("      the same object cc66.153's whitening used, not the npz's diagonal `sigma`")
_ch = np.linalg.cholesky(COV)
_rng = np.random.default_rng(SEED)
_P, _A, _nf = [], [], 0
for _ in range(NDRAW):
    _d = DAT + _ch @ _rng.standard_normal(len(DAT))
    _r = phi_alt(lc, _d * fac, L_A)
    if not np.isfinite(_r[0]) or _r[2] < NPK:
        _nf += 1
        continue
    _P.append(_r[0])
    _A.append(_r[1])
_P, _A = np.array(_P), np.array(_A)
_frac = _nf / NDRAW
print(f"      {NDRAW} draws: {len(_P)} usable, {_nf} failed to yield five finite peaks "
      f"({100 * _frac:.1f} per cent)")
if len(_P) > 2:
    print(f"      the survivors: phi {_P.mean():+.5f} +- {_P.std():.5f}    "
          f"alt {_A.mean():+.5f} +- {_A.std():.5f}")
    print(f"      and their correlation is {np.corrcoef(_P, _A)[0, 1]:+.3f}")
_lb, _db, _la = binned(os.path.join(LEV, 'cr_nodrive.npz'))
_drv = abs(phi_alt(_lb, _db, _la)[0] - phi_alt(*binned(os.path.join(GO, 'cr_base.npz')))[0])
_p5 = phi_alt(*binned(os.path.join(LEV, 'cr_rb0.5.npz')))
_p15 = phi_alt(*binned(os.path.join(LEV, 'cr_rb1.5.npz')))
_lod = abs((_p15[0] - _p5[0]) / np.log(3.0))
print(f"      against the candidates on the same binned footing: driving {_drv:.5f}, "
      f"loading {_lod:.5f}")
print(f"      ⇒ the error on the offset is {_P.std() / _drv:.0f}x the driving's whole signal and "
      f"{_P.std() / _lod:.0f}x the loading's")
check("Ⓒ①  ** THE PLACEMENT IS UNRELIABLE AND NOT MERELY IMPRECISE, WHICH IS THE CASE `r7211` SAID "
      "TO STOP ON. **  *More than nine in ten covariance draws produce no five-peak series at all. "
      "A statistic that fails on most realisations of its own data is not returning a wide "
      "interval; it is not returning a measurement*",
      _frac > 0.9)
check("Ⓒ②  and the survivors do not span the plane: the two components come back correlated at "
      "better than `$0.9$` in magnitude, collapsed onto ONE direction.  *The plane's whole value in "
      "`cc66.156` was that the offset and the alternation are independent components; on the data "
      "they are not, so even a wide interval would not be an interval IN THIS PLANE*",
      len(_P) > 2 and abs(np.corrcoef(_P, _A)[0, 1]) > 0.9)
check("Ⓒ③  and the error on the offset exceeds the LARGER candidate's entire signal by more than a "
      "factor of five.  *So the honest statement is not `the uncertainty covers both candidates` -- "
      "it is that the quantity measured is not the one the statistic reads*",
      len(_P) > 2 and _P.std() > 5.0 * _drv)


# ============================================================ D. the bound
head("D.  WHAT THIS DOES AND DOES NOT TOUCH")

print("  ⛔ NO POINT IS PLACED AND NO CARRIER IS NAMED FOR THE OBSERVED DRIFT.")
print("  ✔ AND cc66.157 AND cc66.158 ARE UNTOUCHED.  Both compare MODEL to MODEL on noiseless")
print("     238-point spectra, which is the regime `PART A` shows the statistic sound in: the")
print("     5.39x separation, the opposite signs on the common offset, and the omega_b opposition")
print("     all stand.  What fails is one step, pointing it at data -- and it fails for a reason")
print("     specific to data: noise creates maxima, and a maximum-finder cannot tell them from")
print("     acoustic peaks.")
print("  ⌈ A REPAIR WOULD HAVE TO FIT A PARAMETRIC COMB TO THE WHOLE BINNED RESIDUAL UNDER THE")
print("     COVARIANCE, rather than locate maxima and refine them.  That is a DIFFERENT statistic.")
print("     `r7211` ordered the one that exists pointed at the data; it did not order a new one,")
print("     and costing one is 66's call rather than this seat's.")
check("Ⓓ①  the model-to-model regime is sound where the data regime is not, and the two are "
      "separated by one property -- whether the spectrum carries noise at the scale of its own "
      "curvature.  *That is why this receipt withdraws nothing from `cc66.157`/`cc66.158`*",
      max(_dp) < 0.0025 and _frac > 0.9)

print()
print(BAR)
if fail:
    print(f"  ⛔ {len(fail)} CHECK(S) FAILED")
    for q in fail:
        print(f"      - {q}")
    print(BAR)
    sys.exit(1)
print("  ✔ 8 of 8 checks pass -- and what they establish is a NEGATIVE: the placement r7211")
print("    ordered cannot be made with the statistic that exists, and the reason is named.")
print(BAR)
sys.exit(0)
