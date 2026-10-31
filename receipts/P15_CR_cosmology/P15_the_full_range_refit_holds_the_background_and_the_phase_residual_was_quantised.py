#!/usr/bin/env python3
r"""
RECEIPT -- P15 / `sec:refit-bound`: ** THE $185$-BIN FULL-RANGE REFIT, ON THE ARM OF RECORD -- AND
THE FINDING HALF INVERTS.  $H_0$ STILL HOLDS, MOVING $0.022\%$; BUT $\Omega_m$ MOVES $2.123\%$,
SIXTY-FOUR TIMES THE "THIRTIETH OF A PER CENT" THE CORPUS CARRIES, WHERE ON THE NAMESAKE ARM IT MOVED
$0.031\%$. **

** THIS FILE'S OWN NAME SAYS THE REFIT HOLDS THE BACKGROUND.  THE NAME IS LEFT AS IT STANDS BECAUSE
THE PAPER CITES IT, AND IT IS THE NAMESAKE ARM'S READING. **  *`r7645`+`cc66.68` re-pointed the ARM's
grid onto `refit_grid185_leafrec1_distances/` -- `refit_grid185/launch.sh` verbatim with `LEAFREC=1`:
the same distances' point $(68.60, 0.2973)$ with the built-in $\omega_b$ and $n_s$, the same nine runs,
the same launcher steps.  The CONTROL's grid does not move, and does not need to: r7641 measured
`LEAFREC`'s reach into the control at $3.6\times10^{-16}$.  The arm's own starting point does not move
either -- `refit_grid185_leafrec1_distances/cr_base` carries $D_M = 14011.4567$, $\ell_A = 302.8891$
and $r_s = 145.3281$ BIT-IDENTICALLY to the namesake's, because `LEAFREC` does not touch the
background.  What moves is the spectrum the fit is run on, and the minimum it finds.*
  ⇒ *So the half of the corpus sentence that is about $H_0$ survives and the half about $\Omega_m$
  fails.  `CR_framework.tex:1863` and `CR_synthesis.tex:1553` both say the arm's "expansion rate and
  matter density stay where the baryon-acoustic distances put them, to under a thirtieth of a per
  cent"; on the arm of record the expansion rate does and the matter density does not.  Routed to
  node 69 in `FOR_69.md` with the replacement figures, because the landing set is 69's to land as one
  unit.*

** ⇒ AND TWO FURTHER GATES OF THIS RECEIPT TURN, EACH A MEASUREMENT RATHER THAN A TOLERANCE. **
  ⓵ ** THE RESPONSE MODEL NO LONGER PREDICTS ITS OWN MINIMUM. **  It says $284.9$ and the real run at
  those parameters returns $297.7$ -- a miss of $+12.1$ where the namesake's was $-0.0$.  *The reason
  is nameable rather than mysterious: $n_s$ moves $+2.57$ grid steps on the arm of record against
  $+1.65$ on the namesake, and the stencil's quadratic is built on $\pm1$.  The gate is kept and
  INVERTED -- it now asserts the miss, two-sided, and asserts the step count that explains it, so a
  stencil rebuilt wide enough to recover agreement fails here and has to be read.*
  ⓶ ** AND ON THE RAW LOCATOR THE TWO ARMS NO LONGER RETURN THE SAME PHASE RESIDUAL **, the control's
  $4.5\%$ against the arm's $0.7\%$, because the arm of record's raw second peak falls in the $532$
  bin where the namesake's fell in $540$ -- the bracketing-bin coin flip measured at `cc66.68` in
  `P15_the_locator_is_good_to_three_hundredths_and_the_fourth_peaks_residual_is_the_controls_too`,
  where the $\ell_2$ bins agree to $0.011$ per cent against $\ell_3$'s $0.066$.  *** THE CLAIM
  SURVIVES AND THE ARGUMENT FORM DOES NOT. ***  *That `cc66.18`'s $4.5\%$ is the grid is now carried
  by the CONTROL alone, which goes $4.5\%$ raw to $1.6\%$ refined on one spectrum, and by the arm's
  own swing in the other direction, $0.7\%$ to $3.7\%$.  Two spectra each moving five-fold under a
  change of locator is the same evidence as two spectra agreeing; what is withdrawn is "both arms
  return the same number", not "the number measures the grid".*

** ⇒ AND ONE NUMBER THIS LINE LANDED AT `cc66.18` IS CORRECTED HERE. **  The $132$-bin receipt
reported the acoustic phase going "$2.3\%\to4.5\%$ out, WORSE".  *That $4.5\%$ was read from a peak
locator quantised to the spectrum's own $\ell$ sampling -- `LSTEP=8` -- and at that resolution ** the
CONTROL returns the same $4.5\%$ **, so the number could not distinguish the arms, the ranges, or
anything else.*  With the peaks refined sub-grid (validated below against an `LSTEP=1` spectrum to
$0.13$ in $\ell$) the crossing arm sits at ** $3.7\%$ on $185$ bins on the arm of record ($3.4\%$ on
the namesake) and $3.1\%$ on $132$ ** against ** the control's $1.6\%$ **.  *** The verdict survives -- freedom does not close the phase and the arm
carries about twice the control's residual -- but it survives on different numbers, and the ones the
corpus is carrying are quantisation. ***

Built r6825+cc66.25 (node 66, code seat), discharging order ① of the chat seat's `r6801`
("run the 185-bin refit ... whether the background still sits where the distances put it when the
damping tail is in the fit") and reporting the correction its follow-up forced.

===================================================================================================
** WHAT WAS RUN, AND WHAT IS READ RATHER THAN RUN **
===================================================================================================

An 18-run derivative grid at `LMAXL=2000`, `LSTEP=8`, `KFAC` at the corpus default $2.0$: a base and
two-sided steps in $H_0$, $\Omega_m$, $\omega_b$ and $n_s$ on each arm, giving the gradient and the
diagonal curvature, with the amplitude closed-form at every evaluation.  ** Each run carries $2547$
$k$-modes against the $132$-bin grid's $1656$ ** -- four hours of wall clock at four at a time.

  ** THE GRID AND THE VERIFICATION SPECTRA ARE READ, NOT PRODUCED. **  They are banked at
  `computations/beyond_the_wall/refit_grid185/` for the control (with the launcher, the fit driver
  and the verification script beside them), `computations/beyond_the_wall/
  refit_grid185_leafrec1_distances/` for the arm, and at `spectra/cc66_r185_verify_lcdm.npz` and
  `spectra/cc66_r185_verify_cr_leafrec1.npz`.
  ⛭ ** ARM KEYS READ: ** no key suffix is involved here -- the arm is selected by DIRECTORY and by
  FILE STEM, and both are named in `GRIDS` and `_VER` below, once each.  *The sibling banks that
  carry `__cr` and `__cr_leafrec1` side by side are the geometry family, not this one; `cc66.68`
  found that reading `__cr` out of one of those returns the namesake silently.*  *Every
  parameter is inside the `.npz`; this file re-does the fit, the scoring and the peak analysis on
  them, and asserts the numbers rather than quoting them.*

  ** tau IS NOT A DIRECTION OF THIS FIT AND THAT IS MEASURED, NOT ASSUMED. **  With no reionisation
  modelled, $e^{-2\tau}$ is a constant on $\ell\ge100$ and is exactly degenerate with $A_s$
  (r6760+cc66.14: $\chi^2$ identical to $10^{-6}$ across $\tau=0$--$0.15$).  *So the fit has four
  directions plus an amplitude, not the six the abstract counts.*

** COMPUTES: both arms refitted like-for-like on the same 185 bins, ell = 100-1996, with P15's
   derived CAMB lensing operator imposed on both; the minimum located on the response model and
   then VERIFIED by real LMAXL=2000 runs at the best-fit parameters; every parameter
   flatness-tested against a one-step excursion; and the two follow-ups recomputed with a peak
   locator whose resolution is measured rather than assumed.  *** Nothing is tuned: the steps are
   the same as the 132-bin grid's, the lensing operator is LCDM's and is imposed on both arms
   alike, and the amplitude is the only closed-form freedom. ***

STATUS: OK
rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~40 s -- reads the banked grid)
"""
import os
import re
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize
from scipy.signal import argrelextrema

print(__doc__.split("STATUS:")[0])
BAR = "=" * 104
fail = []


def check(label, ok):
    print(f"    {'OK  ' if ok else 'FAIL'}  {label}")
    if not ok:
        fail.append(label)


ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
# ** THE ARM'S GRID MOVES TO THE ARM OF RECORD; THE CONTROL'S DOES NOT MOVE (r7645+cc66.68). **
#   *`refit_grid185_leafrec1_distances/` is `refit_grid185/launch.sh` verbatim with `LEAFREC=1`: the
#   same distances' point (68.60, 0.2973, built-in omega_b and n_s), the same nine runs, the same
#   launcher steps.  Its `cr_base` carries D_M 14011.4567, l_A 302.8891 and r_s 145.3281 BIT-IDENTICALLY
#   to the namesake's, because LEAFREC does not reach the background -- so what moves here is the
#   spectrum, not the point the fit starts from.  The control stays in the namesake directory, which is
#   70's `r7639` rule and which r7641 measured at 3.6e-16.*
GRIDS = {'lcdm': os.path.join(_BW, 'refit_grid185'),
         'cr': os.path.join(_BW, 'refit_grid185_leafrec1_distances')}
GRID = GRIDS['lcdm']                      # kept for the control-side reads only
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SKY = np.array([220.4, 537.7, 817.3, 1123.9])
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.020)
TH0 = {'lcdm': dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965),
       'cr': dict(H0=68.60, OM=0.2973, WB=0.0224, NS=0.965)}
NAME = {'lcdm': 'control (LCDM)', 'cr': 'CR, crossing'}

# ** THE LENSING OPERATOR IS P15's OWN: CAMB's lensed/unlensed ratio at the control's parameters. **
# Imposed on BOTH arms alike, so it cannot favour either.
_LR = np.load(os.path.join(SPEC, 'cc66_lens_ratio.npz')) if os.path.exists(
    os.path.join(SPEC, 'cc66_lens_ratio.npz')) else None
if _LR is None:
    import camb                                                            # noqa: E402
    _p = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                         mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    _cl = camb.get_results(_p).get_cmb_power_spectra(_p, CMB_unit='muK', lmax=3000)
    _le, _un = _cl['total'][:, 0], _cl['unlensed_scalar'][:, 0]
    LG = np.arange(len(_le), dtype=float)
    RATIO = np.ones_like(_le)
    _m = _un > 0
    RATIO[_m] = _le[_m] / _un[_m]
else:
    LG, RATIO = np.asarray(_LR['lg'], float), np.asarray(_LR['ratio'], float)


def binned(ls, Dl, lens=True):
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO) if lens else Dl)


def build(tag, lens=True):
    z = np.load(os.path.join(GRIDS[tag], f'{tag}_base.npz'))
    ls = np.asarray(z['ls'], float)
    m0 = binned(ls, np.asarray(z['Dl'], float), lens)
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                               np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    mb = m0[ok]
    g, h = {}, {}
    for k in STEP:
        zp = np.load(os.path.join(GRIDS[tag], f'{tag}_{k}p.npz'))
        zm = np.load(os.path.join(GRIDS[tag], f'{tag}_{k}m.npz'))
        mp = binned(np.asarray(zp['ls'], float), np.asarray(zp['Dl'], float), lens)[ok]
        mm = binned(np.asarray(zm['ls'], float), np.asarray(zm['Dl'], float), lens)[ok]
        g[k] = (mp - mm) / (2 * STEP[k])
        h[k] = (mp - 2 * mb + mm) / STEP[k] ** 2
    return dict(m0=mb, ok=ok, F=F, d=CS.X_DATA[ok], g=g, h=h, th0=TH0[tag])


def chi2_at(B, x):
    m = B['m0'].copy()
    for k, v in zip(STEP, x):
        m = m + B['g'][k] * v + 0.5 * B['h'][k] * v * v
    if np.any(m <= 0):
        return 1e12
    A = float((m @ B['F'] @ B['d']) / (m @ B['F'] @ m))
    r = B['d'] - A * m
    return float(r @ B['F'] @ r)


# =================================================================================================
print(BAR)
print("  PART 1 -- ** THE GRID, AND THE FIT ON IT **")
print(BAR)
need = [f'{t}_{s}' for t in ('lcdm', 'cr')
        for s in ['base'] + [f'{k}{sg}' for k in STEP for sg in 'pm']]
have = [n for n in need if os.path.exists(os.path.join(GRIDS[n.split('_')[0]], f'{n}.npz'))]
check(f"all 18 grid runs are banked ({len(have)} of {len(need)})", len(have) == len(need))
_z = np.load(os.path.join(GRIDS['cr'], 'cr_base.npz'))
_ls = np.asarray(_z['ls'], float)
_nb = int(np.isfinite(CS.bin_spectrum(_ls, np.asarray(_z['Dl'], float))).sum())
print(f"  the grid reaches ell = {_ls[0]:.0f} to {_ls[-1]:.0f} and covers {_nb} bins, "
      f"ell {int(CS.BIN_LO[np.isfinite(CS.bin_spectrum(_ls, np.asarray(_z['Dl'], float)))][0])}"
      f"-{int(CS.BIN_HI[np.isfinite(CS.bin_spectrum(_ls, np.asarray(_z['Dl'], float)))][-1])}")
check("** the range is the 185-bin full one the order asked for, asserted not assumed **", _nb == 185)
print()
R = {}
for tag in ('lcdm', 'cr'):
    B = build(tag)
    n = int(B['ok'].sum())
    c0 = chi2_at(B, np.zeros(4))
    r = minimize(lambda x: chi2_at(B, x), np.zeros(4), method='Nelder-Mead',
                 options=dict(xatol=1e-4, fatol=1e-3, maxiter=4000))
    R[tag] = (B, r, n, c0)
    th = {k: B['th0'][k] + v for k, v in zip(STEP, r.x)}
    print(f"  {NAME[tag]}   ({n} bins)")
    print(f"    {'':>6} {'start':>10} {'best fit':>10} {'moved':>11} {'in steps':>9} {'%':>9}")
    for i, k in enumerate(STEP):
        print(f"    {k:>6} {B['th0'][k]:>10.4f} {th[k]:>10.4f} {r.x[i]:>+11.4f} "
              f"{r.x[i] / STEP[k]:>+8.2f}s {100 * r.x[i] / B['th0'][k]:>+8.3f}%")
    print(f"    chi^2  as-computed {c0:>8.1f} ({c0 / n:.2f}/bin)   "
          f"refitted {r.fun:>8.1f} ({r.fun / n:.2f}/bin)   d = {r.fun - c0:+.1f}\n")

# =================================================================================================
print(BAR)
print("  PART 2 -- ** THE MINIMUM, VERIFIED BY REAL RUNS **")
print(BAR)
print("  The response model says WHERE to go; only a full run says what is there.  Two runs at the")
print("  best-fit parameters, at the same LMAXL, LSTEP and k-reach as the grid.")
print()
print(f"  {'':>24} {'bins':>5} {'predicted':>10} {'measured':>10} {'d':>8}")
_VER = {'lcdm': 'cc66_r185_verify_lcdm.npz',
        'cr': 'cc66_r185_verify_cr_leafrec1.npz'}
VER = {}
for tag in ('lcdm', 'cr'):
    z = np.load(os.path.join(SPEC, _VER[tag]))
    ls = np.asarray(z['ls'], float)
    Dl = np.asarray(z['Dl'], float)
    c, nb, _A, _lo, _hi = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))
    VER[tag] = (c, nb, ls, Dl, z)
    print(f"  {NAME[tag]:>24} {nb:>5d} {R[tag][1].fun:>10.1f} {c:>10.1f} {c - R[tag][1].fun:>+8.1f}")
_MISS = {t: VER[t][0] - R[t][1].fun for t in ('lcdm', 'cr')}
_NSTEP = R['cr'][1].x[3] / STEP['NS']
check(f"control (LCDM): the real run lands within 2 in chi^2 of the model's prediction "
      f"({_MISS['lcdm']:+.2f})", abs(_MISS['lcdm']) < 2.0)
# ⛭⛭ r7645+cc66.68: ** AND ON THE ARM OF RECORD IT DOES NOT, WHICH IS THE READING AND NOT A
#   TOLERANCE. **  *The namesake's miss was -0.0 on the same gate.  Held two-sided at the measured
#   values, so a stencil rebuilt wide enough to recover agreement FAILS here and has to be read.*
check("\u26d4 ** AND THE ARM OF RECORD's REAL RUN DOES NOT: the model says "
      f"{R['cr'][1].fun:.1f} and the run returns {VER['cr'][0]:.1f}, a miss of {_MISS['cr']:+.1f} "
      "where the namesake's was -0.0 ** -- because n_s moves "
      f"{_NSTEP:+.2f} grid steps here against +1.65 on the namesake, and the stencil's quadratic is "
      "built on +-1",
      abs(VER['cr'][0] - 297.6683186940551) < 5e-3
      and abs(R['cr'][1].fun - 284.8548182477841) < 0.02
      and abs(_MISS['cr'] - 12.813500446271) < 0.02
      and abs(_NSTEP - 2.573397320610702) < 5e-4)
check("   \u2317 and the control's stencil is still good to 1.4, so the failure is the ARM's "
      "excursion and not the method: the two arms run the same code on the same steps",
      abs(_MISS['lcdm'] - 1.3815090359693545) < 0.02
      and abs(R['lcdm'][1].x[3] / STEP['NS']) < 1.0)
print()
print(f"  ** RATIO AT THE VERIFIED MINIMUM: {VER['cr'][0] / VER['lcdm'][0]:.2f}x ** "
      f"against {R['cr'][3] / R['lcdm'][3]:.2f}x as-computed on the same bins.")
check("the arm is still disfavoured at the verified minimum -- stated as the result, not a caveat",
      VER['cr'][0] > VER['lcdm'][0])

# =================================================================================================
print()
print(BAR)
print("  PART 3 -- ** THE QUESTION THE ORDER ASKED: DOES THE BACKGROUND STAY PUT WITH THE TAIL IN? **")
print(BAR)
d_h0 = R['cr'][1].x[0]
d_om = R['cr'][1].x[1]
print(f"  (68.60, 0.2973) came from DESI DR2 BAO and theta_* with no spectrum involved.  Given four")
print(f"  free parameters on the FULL range, the crossing arm moves")
print(f"      H0       {d_h0:+.4f}   ({100 * d_h0 / 68.60:+.3f}%)   against +0.011% on 132 bins")
print(f"      Omega_m  {d_om:+.4f}   ({100 * d_om / 0.2973:+.3f}%)   against  0.20%  on 132 bins")
print(f"      omega_b  {R['cr'][1].x[2]:+.4f}   ({100 * R['cr'][1].x[2] / 0.0224:+.2f}%)")
print(f"      n_s      {R['cr'][1].x[3]:+.4f}   ({100 * R['cr'][1].x[3] / 0.965:+.2f}%)")
print()
_PH0, _POM = 100 * d_h0 / 68.60, 100 * d_om / 0.2973
print("  \u21d2 \u26d4 ** THE EXPANSION RATE STAYS PINNED AND THE MATTER DENSITY DOES NOT. **  H0 "
      f"moves {abs(_PH0):.3f}%,")
print(f"  inside a thirtieth of a per cent; Omega_m moves {abs(_POM):.3f}%, which is "
      f"{abs(_POM) / (1 / 30.):.0f} times it.")
print("  *On the NAMESAKE arm both were inside: 0.028% and 0.031%.  So `the background stays pinned`")
print("  -- this file's own name, and the corpus sentence at CR_framework.tex:1863 and")
print("  CR_synthesis.tex:1553 -- is HALF the namesake arm's reading and half still true.  What the")
print("  two arms share is where the leverage lands: omega_b and n_s move further than on 132 bins")
print("  on both, and further still here, n_s by 2.57 steps against the namesake's 1.65.*")
check(f"** the crossing arm's H0 still moves by under 0.05% on the full range: {abs(_PH0):.3f}% **",
      abs(_PH0) < 0.05 and abs(_PH0 + 0.02162229341132475) < 5e-5)
# ⛭⛭⛭ r7645+cc66.68: ** THE GATE THAT SAID Omega_m IS HELD NOW ASSERTS THAT IT IS NOT. **
#   *Pinned two-sided at the measured per cent, not bounded, so BOTH directions fail it: a run that
#   returns the namesake's 0.031% fails, and so does one that returns something larger again.*
check("\u26d4 ** BUT Omega_m DOES NOT: it moves "
      f"{abs(_POM):.3f}%, {abs(_POM) / (1 / 30.):.0f} times the `thirtieth of a per cent` the corpus "
      "carries, where the namesake moved 0.031% **",
      abs(_POM + 2.123134312535325) < 5e-4)
check("   \u2317 and so the sentence splits rather than simply moving: the expansion rate half of it "
      "survives verbatim and the matter density half is withdrawn",
      abs(_PH0) < 1 / 30. < abs(_POM))
check(f"H0 moves FURTHER than on 132 bins ({abs(_PH0):.3f}% against 0.011%), stated not smoothed over",
      abs(_PH0) > 0.011)
check("omega_b and n_s move further than on 132 bins -- the tail's leverage, where predicted",
      abs(R['cr'][1].x[2] + 0.0007242802155514605) < 5e-7
      and abs(R['cr'][1].x[3] - 0.05146794641221404) < 5e-7)

# =================================================================================================
print()
print(BAR)
print("  PART 4 -- ** THE FLATNESS TEST: A BEST FIT THAT COSTS NOTHING TO LEAVE IS NOT A MEASUREMENT **")
print(BAR)
print(f"  {'':>8} " + " ".join(f"{NAME[t]:>22}" for t in ('lcdm', 'cr')))
FLAT = {}
for i, k in enumerate(STEP):
    row = []
    for tag in ('lcdm', 'cr'):
        B, r, n, _ = R[tag]
        e = np.zeros(4)
        e[i] = STEP[k]
        dd = min(chi2_at(B, r.x + e) - r.fun, chi2_at(B, r.x - e) - r.fun)
        FLAT[(tag, k)] = dd
        row.append(dd)
    print(f"  {k:>8} " + " ".join(f"{v:>22.1f}" for v in row))
print("\n  (the cheaper of the two one-step excursions, in chi^2)")
# ⛭⛭⛭ `r7647` ⑶ -- THE QUARTET THE PAPER PRINTS, PINNED FOR THE FIRST TIME.  Until now this part
#   computed all eight of these and gated them only as `all(v > 5.0)`, a floor no quartet of this
#   size could ever fail, while `sec:refit-bound` printed four of them as `2527, 740, 141 and 31`
#   and NO receipt asserted any of them.  They are captured from the paper and compared here.
# ⌗ AND THE PAPER'S FOUR ARE THE NAMESAKE GRID'S, measured rather than assumed: pointing
#   `GRIDS['cr']` at `refit_grid185` instead reproduces 2527.3900 / 739.6168 / 141.0245 / 31.2352,
#   which round to exactly what the paper prints.  That is a one-line change anyone can repeat; it
#   is recorded here in prose rather than pinned, because this file's business is the arm of record.
_TEX = open(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'), encoding='utf-8').read()
_mq = re.search(r"one-step excursions cost\s*\$([0-9]+)\$, \$([0-9]+)\$, \$([0-9]+)\$ and "
                r"\$([0-9]+)\$", _TEX)
check("⌗ `sec:refit-bound`'s printed quartet is still FOUND by this file's pattern -- a sentence "
      "reworded past it must redden this part rather than leave it comparing against nothing",
      _mq is not None)
if _mq:
    _PQ = dict(zip(('H0', 'OM', 'WB', 'NS'), (float(x) for x in _mq.groups())))
    _A = {k: float(FLAT[('cr', k)]) for k in ('H0', 'OM', 'WB', 'NS')}
    _C = {k: float(FLAT[('lcdm', k)]) for k in ('H0', 'OM', 'WB', 'NS')}
    print(f"\n      {'':>6} {'paper':>10} {'arm of record':>16} {'control':>12} {'arm vs paper':>14}")
    for k in ('H0', 'OM', 'WB', 'NS'):
        print(f"      {k:>6} {_PQ[k]:>10.0f} {_A[k]:>16.4f} {_C[k]:>12.4f} "
              f"{(_A[k] / _PQ[k] - 1) * 100:>+13.4f}%")
    check("⛔⛔ ** THE QUARTET MOVES ON THE ARM OF RECORD AND THREE OF THE FOUR GET STIFFER: ** "
          f"{_A['H0']:.1f}, {_A['OM']:.1f}, {_A['WB']:.1f} and {_A['NS']:.1f} against the printed "
          f"{_PQ['H0']:.0f}, {_PQ['OM']:.0f}, {_PQ['WB']:.0f} and {_PQ['NS']:.0f} -- "
          f"{(_A['H0'] / _PQ['H0'] - 1) * 100:+.2f}%, {(_A['OM'] / _PQ['OM'] - 1) * 100:+.2f}%, "
          f"{(_A['WB'] / _PQ['WB'] - 1) * 100:+.2f}% and {(_A['NS'] / _PQ['NS'] - 1) * 100:+.2f}%",
          2538.0 < _A['H0'] < 2540.5 and 812.0 < _A['OM'] < 814.0
          and 149.3 < _A['WB'] < 150.4 and 25.7 < _A['NS'] < 26.3)
    # ⛭⛭⛭ THIS CLAIM IS MADE AGAINST THE CONTROL AND NOT AGAINST THE PAPER'S PRINTED QUARTET, AND
    #   THAT IS DELIBERATE.  `check_quote_pins` named the capture above as a new quote-pin key and
    #   put the reason plainly: a gate that asserts another seat's sentence "fails on SUCCESS when
    #   the sentence said something was open".  The first form of this gate compared the measured
    #   quartet with the PRINTED one, so the day 69 lands the arm-of-record figures the comparison
    #   would invert and this receipt would go red on a correct landing.  ⇒ The content -- three
    #   directions stiffen, the tilt softens -- is control-relative, and the control does not move.
    check("⛔ ** AND THE TILT IS THE ONE DIRECTION THAT SOFTENS: ** it is the only one of the four on "
          f"which the arm of record is LESS constrained than the CONTROL ({_A['NS'] / _C['NS']:.4f} "
          f"of it) while the other three are MORE ({_A['H0'] / _C['H0']:.2f}, "
          f"{_A['OM'] / _C['OM']:.2f}, {_A['WB'] / _C['WB']:.2f} of it) ** -- so the re-point "
          "stiffens the background and loosens the tilt, the same direction `cc66.68` found the "
          "refit moving it in.  *Stated against the control because the control is the thing that "
          "does not move; comparing with the paper's printed quartet would make this gate fail the "
          "day 69 lands the new figures.*",
          _A['NS'] < _C['NS'] and all(_A[k] > _C[k] for k in ('H0', 'OM', 'WB')))
    _ns_pq = {k: _PQ[k] for k in ('H0', 'OM', 'WB', 'NS')}
    _is_namesake = (_ns_pq == {'H0': 2527.0, 'OM': 740.0, 'WB': 141.0, 'NS': 31.0})
    _is_aor = (_ns_pq == {'H0': 2539.0, 'OM': 813.0, 'WB': 150.0, 'NS': 26.0})
    check("⌗ ** AND THE PAPER'S PRINTED QUARTET IS ONE OF EXACTLY TWO LEGITIMATE STATES: ** the "
          "NAMESAKE grid's `2527 / 740 / 141 / 31`, which is what it carries now, or the arm of "
          "record's `2539 / 813 / 150 / 26`, which is what `cc66.74` proposes and 69 lands.  "
          f"*It currently reads {_PQ['H0']:.0f} / {_PQ['OM']:.0f} / {_PQ['WB']:.0f} / "
          f"{_PQ['NS']:.0f}, the "
          + ('NAMESAKE' if _is_namesake else 'ARM OF RECORD' if _is_aor else 'UNRECOGNISED')
          + " state.*  This is the disjunction `check_quote_pins` asks for: the gate passes in "
          "either state and fails only on a THIRD set, which would be a drift rather than a "
          "landing.",
          _is_namesake or _is_aor)
    check("⌗ and the CONTROL's four are untouched by the re-point, pinned here so the comparison's "
          f"other half is asserted too: {_C['H0']:.4f}, {_C['OM']:.4f}, {_C['WB']:.4f}, "
          f"{_C['NS']:.4f}",
          1774.0 < _C['H0'] < 1774.3 and 473.0 < _C['OM'] < 473.2
          and 98.2 < _C['WB'] < 98.4 and 32.2 < _C['NS'] < 32.4)
check("** every parameter is constrained on both arms: a one-step excursion costs chi^2 ** -- the "
      f"cheapest of all eight is {min(float(v) for v in FLAT.values()):.2f}, so the claim that "
      "these are sharp minima rather than unconstrained directions survives the re-point with room "
      "to spare.  ⌗ The old floor here was 5.0, which no quartet of this size could fail; it is "
      "raised to 20 and the four figures themselves are pinned above",
      all(float(v) > 20.0 for v in FLAT.values()))
check("and n_s is a live direction, which is what caught the knob shadow at cc66.17 -- still live "
      "on both arms, and now the only one of the four that the re-point made cheaper",
      FLAT[('cr', 'NS')] > 5.0 and FLAT[('lcdm', 'NS')] > 5.0)

# =================================================================================================
print()
print(BAR)
print("  PART 5 -- ** THE TWO FOLLOW-UPS, AND THE PEAK LOCATOR'S RESOLUTION MEASURED FIRST **")
print(BAR)
# ** THIS IS THE CORRECTION.  cc66.18 read the peaks with argrelextrema on the spectrum's OWN
#    LSTEP=8 grid, so every peak was quantised to 8 in ell -- and the phase residual it feeds is a
#    few per cent.  The consequence was not subtle: the CONTROL returned the same 4.5%. **


def comb(P, n=3):
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(P[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def peaks_raw(ls, Dl, n=4, order=3):
    return [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=order)[0][:n]]


def peaks_sub(ls, Dl, n=4, order=3):
    """the same locator, with the maximum refined by the parabola through its three samples."""
    out = []
    for i in argrelextrema(Dl, np.greater, order=order)[0][:n]:
        if i < 1 or i > len(ls) - 2:
            out.append(float(ls[i]))
            continue
        y0, y1, y2 = Dl[i - 1], Dl[i], Dl[i + 1]
        den = y0 - 2 * y1 + y2
        off = 0.5 * (y0 - y2) / den if den != 0 else 0.0
        out.append(float(ls[i] + off * (ls[i + 1] - ls[i])))
    return out


# ⛭⛭ RE-POINTED AT r7097+cc66.79, onto a substrate that is RE-DERIVABLE.
# *`70` established that this validation held on `cc66_cr_x_lstep1.npz` -- which **has no command
# anywhere in the repository**, so the substrate could not be rebuilt, and whose comb is the superseded
# STACKING ruler's ($\ell_A = 172.841$ against this cosmology's $301.8$).*  ** `r6941_fine_cr.npz` has a
# launcher, carries $\ell_A = 301.799$ at configuration B, and spans ell 100-1999 at spacing 1 -- a
# wider range at the same resolution. **
#   ⇒ *And the check is STRICTER there, not looser: `70` measured raw $3.90$ and refined $0.023$ on the
#   new substrate against raw $3.06$ and refined $0.133$ on the old, so the refined error it has to beat
#   falls by a factor of six while the raw error it has to exceed rises.  Measured in
#   `r7095_70_artefact_configuration/locator_substrate_log.txt`; this edit is the re-pointing only.*
#   ⌗ *`r7097` left this to this seat although it is mechanical, because re-pointing what a receipt
#   READS changes its subject and that is reserved to the receipt's author.  The threshold is unchanged.*
print("  (a) ** THE REFINEMENT IS VALIDATED BEFORE IT IS USED, on a banked LSTEP=1 spectrum that has "
      "a launcher and this cosmology's own comb. **")
_z1 = np.load(os.path.join(SPEC, 'r6941_fine_cr_leafrec1.npz'))
_l1 = np.asarray(_z1['ls'], float)
_D1 = np.asarray(_z1['Dl'], float)
_native = peaks_sub(_l1, _D1, order=20)
print(f"      at spacing {int(_l1[1] - _l1[0])}: peaks " + " / ".join(f"{v:.2f}" for v in _native))
_err_raw = _err_sub = 0.0
for st in (2, 4, 8):
    _ls, _Ds = _l1[::st], _D1[::st]
    _o = max(3, 20 // st)
    _r = peaks_raw(_ls, _Ds, order=_o)
    _s = peaks_sub(_ls, _Ds, order=_o)
    e_r = max(abs(a - b) for a, b in zip(_r, _native))
    e_s = max(abs(a - b) for a, b in zip(_s, _native))
    _err_raw = max(_err_raw, e_r)
    _err_sub = max(_err_sub, e_s)
    print(f"      subsampled to {st:>2}: raw locator errs by {e_r:5.2f} in ell, "
          f"refined by {e_s:5.2f}")
check("** at the grid the refit runs on, the RAW locator errs by 3 in ell and the refined one by "
      "0.15 **", _err_raw > 2.0 and _err_sub < 0.2)
print("      ⇒ *so a phase residual of a few per cent read from raw peaks is reading the grid.*")
# ⛭⛭ r7645+cc66.68: ** AND THE SUBSTRATE'S IDENTITY IS GATED, BECAUSE THE RESOLUTION TEST
#   CANNOT SEE IT. **  *I perturbed this re-point back to `r6941_fine_cr` and EVERY gate in the file
#   stayed green: the locator's error against its own LSTEP=1 reference is a property of the GRID,
#   not of the arm, so the test is blind to which spectrum it runs on.  A re-point nothing holds is
#   not a re-point, so the arm is pinned here by the substrate's own comb.*
check("\u26ed ** and the substrate is the ARM OF RECORD's, which the resolution test above cannot "
      f"see: l_A = {float(_z1['l_A']):.4f} against the namesake's 301.7986, peaks "
      f"{' / '.join(f'{v:.2f}' for v in _native)} against 221.96 / 536.10 / 815.40 / 1130.53 **",
      abs(float(_z1['l_A']) - 302.9430505935752) < 5e-7
      and abs(_native[0] - 222.04654943740528) < 5e-7
      and abs(_native[1] - 535.8455230993328) < 5e-7
      and abs(_native[3] - 1129.7415107014076) < 5e-7)

print()
print("  (b) ** THE FOLLOW-UPS, ON BOTH LOCATORS AND BOTH ARMS. **")
lA_s, phi_s = comb(SKY)
print(f"      {'':>26} {'peaks':>34} {'phase % out':>12} {'4th peak %':>11}")
PH = {}
for tag in ('lcdm', 'cr'):
    _, _, ls, Dl, _z = VER[tag]
    for lab, fn in (('raw (as cc66.18 read it)', peaks_raw), ('refined', peaks_sub)):
        P = fn(ls, Dl)
        lA_f, phi_f = comb(P)
        PH[(tag, lab)] = (abs(phi_f / phi_s - 1) * 100, abs(P[3] / SKY[3] - 1) * 100)
        print(f"      {NAME[tag] + ', ' + lab:>26} {' / '.join(f'{v:.1f}' for v in P):>34} "
              f"{PH[(tag, lab)][0]:>11.1f}% {PH[(tag, lab)][1]:>10.1f}%")
print()
_RAW = 'raw (as cc66.18 read it)'
_P2 = {t: peaks_raw(VER[t][2], VER[t][3])[1] for t in ('lcdm', 'cr')}
# ⛭⛭⛭ r7645+cc66.68: ** THE ARGUMENT FORM IS WITHDRAWN AND THE CLAIM IS NOT. **
#   *On the namesake arm both arms returned 4.5% raw, and that agreement WAS the evidence that the
#   number measures the grid.  On the arm of record the raw second peak falls in the 532 bin where
#   the namesake's fell in 540 -- the bracketing-bin coin flip measured at cc66.68 in the locator
#   receipt, where the l_2 bins agree to 0.011 per cent against l_3's 0.066 -- so the raw readings
#   separate, 4.5% against 0.7%.  The claim is now carried TWICE OVER instead: each arm on its own
#   swings about five-fold between the two locators, in OPPOSITE directions, which cannot be a
#   property of either spectrum and can only be the locator.*
check("\u26d4 ** THE RAW LOCATOR NO LONGER AGREES BETWEEN THE ARMS: the control's "
      f"{PH[('lcdm', _RAW)][0]:.1f}% against the arm of record's {PH[('cr', _RAW)][0]:.1f}% ** -- "
      f"because the arm's raw l_2 falls at {_P2['cr']:.0f} where the namesake's and the control's "
      f"fall at {_P2['lcdm']:.0f}, a whole bin",
      #: ⛔ r7645+cc66.68: the CONTROL's raw figure is pinned by its PEAK SET and not by a float.
      #: *`check_tilt_pins` flagged `abs(PH[('lcdm', _RAW)][0] - 4.4642...) < 5e-4` as DETACHED, and
      #: it is right: `peaks_raw` returns abscissa values straight off the `LSTEP=8` grid, so the
      #: control's raw residual is quantised at a quantum of 8 in ell and a smooth 5 per cent tilt
      #: cannot move it.  The float added nothing -- `comb()` is deterministic in the peak set, which
      #: this gate already pins -- so it is removed rather than adjudicated into a baseline.*
      #:   ⇒ *The ARM's raw float is NOT flagged, and that is the finding rather than an accident:
      #:   its `l_2` sits on the 0.011-per-cent coin flip, so the tilt DOES move it where it cannot
      #:   move the control's.  It stays pinned.  The refined floats below are parabola-refined and
      #:   tilt-reachable, which is the grid-free assertion standing beside the quantised set.*
      abs(PH[('cr', _RAW)][0] - 0.7177288761125111) < 5e-4
      and peaks_raw(VER['lcdm'][2], VER['lcdm'][3]) == [220.0, 540.0, 812.0, 1132.0]
      and peaks_raw(VER['cr'][2], VER['cr'][3]) == [220.0, 532.0, 812.0, 1132.0]
      and (_P2['cr'], _P2['lcdm']) == (532.0, 540.0))
check("   \u21d2 ** AND THE CLAIM SURVIVES ON A STRONGER FOOTING: each arm SEPARATELY swings about "
      f"five-fold between the two locators -- the control {PH[('lcdm', _RAW)][0]:.1f}% -> "
      f"{PH[('lcdm', 'refined')][0]:.1f}% and the arm {PH[('cr', _RAW)][0]:.1f}% -> "
      f"{PH[('cr', 'refined')][0]:.1f}%, in OPPOSITE directions ** -- so the number cannot be a "
      "property of either spectrum and is the locator's",
      PH[('lcdm', _RAW)][0] / PH[('lcdm', 'refined')][0] > 2.5
      and PH[('cr', 'refined')][0] / PH[('cr', _RAW)][0] > 2.5
      and abs(PH[('cr', 'refined')][0] - 3.6907637485920186) < 5e-4
      and abs(PH[('lcdm', 'refined')][0] - 1.5572746731141507) < 5e-4)
check("** and refined they separate: the arm carries about twice the control's **",
      PH[('cr', 'refined')][0] > 1.5 * PH[('lcdm', 'refined')][0])
print(f"  ⇒ *** THE VERDICT SURVIVES ON DIFFERENT NUMBERS. ***  The crossing arm's phase residual is")
print(f"     {PH[('cr', 'refined')][0]:.1f}% on the full range against the control's "
      f"{PH[('lcdm', 'refined')][0]:.1f}%, and the fourth peak is "
      f"{PH[('cr', 'refined')][1]:.1f}% out against {PH[('lcdm', 'refined')][1]:.1f}%.")
print(f"     ** cc66.18's quoted 4.5% is withdrawn: it is the LSTEP=8 grid, and the control shares it. **")
print("     *Freedom still does not close the phase -- that part of the reading stands.*")

# =================================================================================================
print()
print(BAR)
print("  WHAT THIS SETTLES")
print(BAR)
print(f"""
  ** THE ORDER'S QUESTION IS ANSWERED, AND ON THE ARM OF RECORD THE ANSWER IS HALF THE OTHER WAY. **
  With the damping tail inside the fit the crossing arm's background moves {abs(_PH0):.3f}% in $H_0$
  -- inside a thirtieth of a per cent, as the corpus says -- and {abs(_POM):.3f}% in
  $\\Omega_m$, which is {abs(_POM) / (1 / 30.):.0f} times it.  ** So the expansion rate stays where the
  distances put it and the matter density does not. **  *On the NAMESAKE arm both were inside, at
  0.028% and 0.031%, and that is the reading the corpus carries.  What the two arms share is where
  the leverage lands: omega_b and n_s move further than on 132 bins on both, and further still here.
  The worry the order named -- that the tail would prise the background off -- turns out to be half
  right, and the half it is right about is the one the baryon-acoustic data constrain least.*

  ** AND IT COSTS {VER['cr'][0] / VER['lcdm'][0]:.2f}x THE CONTROL ** ({VER['cr'][0] / VER['cr'][1]:.2f} per bin against {VER['lcdm'][0] / VER['lcdm'][1]:.2f}), against
  {R['cr'][3] / R['lcdm'][3]:.2f}x as-computed.  *Freedom closes about a third of the gap and leaves the rest; the arm is
  still disfavoured, and that is the result rather than a caveat on it.*

  ⛔ ** ONE LANDED NUMBER OF MINE IS WITHDRAWN. **  `cc66.18`'s "the acoustic phase goes 2.3% -> 4.5%
  out" was read from peaks quantised to the spectrum's own LSTEP=8 sampling.  *The tell was there to
  be seen and I did not look for it: the CONTROL returns the same 4.5%.*  Refined -- with the
  refinement validated against an LSTEP=1 spectrum to 0.13 in ell before use -- the arm sits at
  {PH[('cr', 'refined')][0]:.1f}% against the control's {PH[('lcdm', 'refined')][0]:.1f}%.  ** The verdict does not change and the numbers do. **
  \u26d4 *And on the arm of record the EVIDENCE changes too: the two arms no longer return the same
  raw number ({PH[('lcdm', _RAW)][0]:.1f}% against {PH[('cr', _RAW)][0]:.1f}%, the arm's raw l_2 falling a
  whole bin lower), so `both arms return 4.5%` is withdrawn as an argument.  Each arm swings about
  five-fold between the locators on its own, in opposite directions, which carries it further.*
""")

print(BAR)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print(BAR)
