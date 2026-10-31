#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE PARAMETER REFIT, ON THE ARM OF RECORD.  GIVEN FOUR FREE PARAMETERS THE
CROSSING ARM MOVES $H_0$ BY $-0.0009$ -- A THOUSANDTH OF A PER CENT, STAYING WHERE THE
BARYON-ACOUSTIC DATA PUT IT -- AND Omega_m BY $-0.0064$, WHICH IS $2.16\%$ AND DOES NOT. **

** ⛔⛔ SO THE CLAIM SPLITS RATHER THAN MOVING. **  *On the NAMESAKE arm both were inside a
thirtieth of a per cent, at $0.001\%$ and $0.20\%$, and the corpus carries that as "the spectrum,
given the freedom to go anywhere, stays there".  On the arm of record the EXPANSION RATE stays and
the MATTER DENSITY is pulled two per cent off -- four tenths of one grid step, and the only one of
the four parameters the distance data themselves constrain.  The 185-bin range says the same thing
with $0.022\%$ and $2.123\%$ (`cc66.68`), so it is not a property of this range.*

** AND IT STILL DOES NOT CLOSE THE TWO RESIDUALS, THOUGH THE EVIDENCE HAD TO BE REBUILT: the
acoustic phase goes $1.32\%\to3.69\%$ out and the fourth peak $0.47\%\to0.51\%$, both read with a
locator whose resolution is measured. **
  ⛭⛭⛭ *The figures this file carried, $2.3\%\to4.5\%$ and $0.9\%\to0.7\%$, were a COMPUTED
  "after" on raw `argrelextrema` peaks against a TYPED-IN "before" -- and the raw locator is the one
  `cc66.18`'s $4.5\%$ was withdrawn as.  On the arm of record that locator returns a BIT-IDENTICAL
  peak set before and after the refit, $220/532/812/1132$ both times, so its phase is $0.72\%$ on two
  spectra separated by $146$ in $\chi^{2}$.  **No argument about locators is needed: the locator
  reports the same number for two different spectra.**  Both columns are now computed, on both
  locators, from the two spectra this receipt already reads.*

** ⇒ SO THE RESIDUALS ARE PROPERTIES OF THE CONSTRUCTION AND NOT BACKGROUND CHOICES, ** which is
the question node 66 (chat seat) asked of this run in as many words: *"if a refit removes them they
are a background choice rather than a property of the construction."*  It does not remove them.

** chi^2 AT THE VERIFIED MINIMUM: control 118.3 (0.90/bin), arm 181.7 (1.38/bin) over 132 bins --
a ratio of 1.54, against 2.35 as-computed. **  *Freedom closes 60 per cent of the excess over one and
leaves the rest.*  ⌗ *On the namesake arm these were 171.1, 1.45 and 2.22, and "about a third of
the gap" was that arm's arithmetic.*

Built r6788+cc66.18 (node 66, code seat), on `PO-13`, at the chat seat's standing refit order and
its ruling of r6788 (take the 132-bin configuration; the control refitted like-for-like).

===================================================================================================
** WHAT WAS RUN, AND THE THREE THINGS THAT MAKE IT A FIT RATHER THAN AN EXTRAPOLATION **
===================================================================================================

  ** 1  A MEASURED RESPONSE, NOT A SEARCH. **  Each likelihood call is a full spectrum, so a search
  is thousands of them.  Instead: 18 runs -- a base and two-sided steps in H0, Omega_m, omega_b and
  n_s, per arm -- giving the gradient AND the diagonal curvature, so the model is quadratic along
  each axis.  *The amplitude is fitted in closed form at every evaluation and costs nothing.*

  ** 2  THE MINIMUM IS VERIFIED BY A REAL RUN. **  The response model says where to go; a run at
  the best-fit parameters says what is there.  ** Predicted 118.2 and 170.8; measured 118.3 and
  181.7 -- $+0.2$ on the control and $+10.9$ on the arm. **
  ⛔⛔ *On the namesake both were inside half a unit.  On the arm of record the ARM's stencil
  misses by eleven while the control's -- same code, same steps -- is good to two tenths, because
  $n_s$ moves $+2.39$ grid steps here and the quadratic is built on $\pm1$.  So the model's
  PARAMETERS are still the licence (PART 2 reads them, PART 5 scores the real run at them) and the
  model's $\chi^{2}$ is not.  The 185-bin range does the same at $+12.8$ and $2.57$ steps.*
  ⌗ *The verification file is banked at the FULL-RANGE minimum; this range's own minimum agrees
  with it to a quarter of a grid step, measured before the re-point was made and gated in PART 1.*

  ** 3  EVERY PARAMETER IS TESTED FOR FLATNESS. **  A one-step excursion from the minimum must cost
  chi^2 or the 'best fit' is not a measurement.  *This is not decoration: it is what caught a dead
  knob.  Before r6788+cc66.17 the tilt returned d(chi^2) = 0.00 on BOTH arms, because `NS` was
  shadowed by two more copies of the literal 0.965 on the path the grid runs.*

** WHAT IS NOT A FREE DIRECTION, AND THE ABSTRACT COUNTS IT AS ONE. **  tau is exactly degenerate
with the amplitude here: no reionisation is modelled, so exp(-2 tau) is a constant on ell >= 100 and
only A_s exp(-2 tau) is seen.  ** Measured at cc66.14: chi^2 identical to one part in 1e6 across
tau = 0 to 0.15. **  *So the fit has FOUR directions plus an amplitude, not six.*

  PART 1  ** THE VERIFICATION. **
  PART 2  ** THE PARAMETERS AT THE MINIMUM, AND HOW FAR EACH MOVED. **
  PART 3  ** THE FLATNESS TEST. **
  PART 4  ** THE TWO FOLLOW-UPS: the acoustic phase and the fourth peak. **
  PART 5  ** WHAT IT COSTS AND WHAT IT DOES NOT BUY. **

** COMPUTES: the grid is `LMAXL=1300`, `LSTEP=8`, `HIER=1`, `KFAC` at the corpus default 2.0 --
   132 bins, ell 100-1287.  Starting points: control (67.40, 0.3150, 0.0224, 0.965), arm
   (68.60, 0.2973, 0.0224, 0.965) with the handover at the crossing and one clock.  Steps: H0 2.0,
   Omega_m 0.0150, omega_b 0.0008, n_s 0.0200.  *** The 185-bin configuration the order first asked
   for is NOT produced: a run at LMAXL=2000 takes ~60 min against container windows that were 1-15
   min, and the cheaper k-reach is refused by the instrument's own truncation guard.  The chat seat
   ruled at r6788 to take this range with the cost stated. *** **

rc=0 on success.  Run: python3 <this file>   (numpy, scipy; ~30 s; reads refit_grid/ and spectra/)
"""
import os
import sys

import numpy as np
import scipy.linalg
from scipy.optimize import minimize
from scipy.signal import argrelextrema

print(__doc__.split("rc=0")[0])
fail = []
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
# ⛭⛭ r7645+cc66.69: ** THE ARM MOVES TO THE ARM OF RECORD; THE CONTROL DOES NOT MOVE. **
#   *`refit_grid_leafrec1_distances/` is `refit_grid/`'s own recipe with `LEAFREC=1` at the same
#   distances' point -- nine runs, the same launcher steps, LMAXL 1300.  The control stays in the
#   namesake directory (70's `r7639` rule; r7641 measured LEAFREC's reach into the control at
#   3.6e-16).*
#   ⇒ ** AND THE VERIFICATION FILE IS BANKED AT THE FULL-RANGE MINIMUM, WHICH THIS RANGE'S OWN
#       MINIMUM AGREES WITH TO A QUARTER OF A GRID STEP. **  *Measured before this re-point was made,
#       because a verification at the wrong point would have been invisible: fitting this stencil on
#       the 132 bins lands at 68.599120 / 0.290866 / 0.021839 / 1.012701, against the banked
#       68.570730 / 0.291246 / 0.021643 / 1.015066 -- 0.014, 0.025, 0.245 and 0.118 of a step.  The
#       namesake's two ranges agree to the same quarter step, so this is a property of the problem and
#       not of the arm.  Gated in PART 1.*
GRIDS = {'lcdm': os.path.join(BW, 'refit_grid'),
         'cr': os.path.join(BW, 'refit_grid_leafrec1_distances')}
GRID = GRIDS['lcdm']
_VER = {'lcdm': 'cc66_refit_verify_lcdm.npz', 'cr': 'cc66_refit_verify_cr_leafrec1.npz'}
SPEC = os.path.join(BW, 'spectra')
sys.path.insert(0, os.path.join(ROOT, 'computations', 'planck_tt_likelihood'))
import chi2_of_spectrum as CS                                              # noqa: E402

SKY = np.array([220.4, 537.7, 817.3, 1123.9])
STEP = dict(H0=2.0, OM=0.0150, WB=0.0008, NS=0.0200)
ARMS = {
    'control (LCDM)': dict(tag='lcdm', th0=dict(H0=67.40, OM=0.3150, WB=0.0224, NS=0.965)),
    'CR, crossing': dict(tag='cr', th0=dict(H0=68.60, OM=0.2973, WB=0.0224, NS=0.965)),
}


def lensing_ratio():
    """CAMB's lensed/unlensed ratio -- the non-perturbative operator, LCDM's, imposed on both."""
    import camb
    pars = camb.set_params(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674 ** 2 - 0.02237,
                           mnu=0.06, omk=0, tau=0.054, As=2.1e-9, ns=0.965, lmax=3000)
    cl = camb.get_results(pars).get_cmb_power_spectra(pars, CMB_unit='muK', lmax=3000)
    lensed, unlens = cl['total'][:, 0], cl['unlensed_scalar'][:, 0]
    lg = np.arange(len(lensed))
    r = np.ones_like(lensed)
    m = unlens > 0
    r[m] = lensed[m] / unlens[m]
    return lg, r


LG, RATIO = lensing_ratio()


def binned(ls, Dl, lens=True):
    return CS.bin_spectrum(ls, Dl * np.interp(ls, LG, RATIO) if lens else Dl)


def load(path):
    z = np.load(path)
    return np.asarray(z['ls'], float), np.asarray(z['Dl'], float)


def build(arm, lens=True):
    ls, Dl = load(os.path.join(GRIDS[arm['tag']], f"{arm['tag']}_base.npz"))
    m0 = binned(ls, Dl, lens)
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                               np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    g, h = {}, {}
    for k in STEP:
        mp = binned(*load(os.path.join(GRIDS[arm['tag']], f"{arm['tag']}_{k}p.npz")), lens)[ok]
        mm = binned(*load(os.path.join(GRIDS[arm['tag']], f"{arm['tag']}_{k}m.npz")), lens)[ok]
        mb = m0[ok]
        g[k] = (mp - mm) / (2 * STEP[k])
        h[k] = (mp - 2 * mb + mm) / STEP[k] ** 2
    return dict(m0=m0[ok], ok=ok, F=F, d=CS.X_DATA[ok], g=g, h=h, th0=arm['th0'])


def chi2_at(B, x):
    m = B['m0'].copy()
    for k, v in zip(STEP, x):
        m = m + B['g'][k] * v + 0.5 * B['h'][k] * v * v
    if np.any(m <= 0):
        return 1e12
    A = float((m @ B['F'] @ B['d']) / (m @ B['F'] @ m))
    r = B['d'] - A * m
    return float(r @ B['F'] @ r)


def best(B):
    return minimize(lambda x: chi2_at(B, x), np.zeros(4), method='Nelder-Mead',
                    options=dict(xatol=1e-4, fatol=1e-3, maxiter=6000))


print("=" * 104)
print("  PART 1 -- ** THE VERIFICATION: the model said where to go, these runs say what is there **")
print("=" * 104)
B = {nm: build(a) for nm, a in ARMS.items()}
R = {nm: best(b) for nm, b in B.items()}
print(f"  {'arm':>18} {'model predicted':>16} {'REAL RUN':>10} {'/bin':>7} {'diff':>8} {'bins':>6}")
real = {}
for nm, tag in (('control (LCDM)', 'lcdm'), ('CR, crossing', 'cr')):
    ls, Dl = load(os.path.join(SPEC, _VER[tag]))
    c, n, A, lo, hi = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))
    real[nm] = (c, n)
    print(f"  {nm:>18} {R[nm].fun:>16.1f} {c:>10.1f} {c / n:>7.2f} {c - R[nm].fun:>+8.1f} {n:>6d}")
    if n != 132:
        fail.append(f"{nm}: {n} bins, not the 132 this configuration covers")
_MISS = {nm: real[nm][0] - R[nm].fun for nm in real}
_NSTEP = R['CR, crossing'].x[3] / STEP['NS']
# ⛔⛔ r7645+cc66.69: ** THE ARM'S VERIFIED RUN NO LONGER LANDS WHERE THE MODEL SAID, AND THAT
#   IS THE READING RATHER THAN A TOLERANCE. **  *On the namesake the miss was +0.5 and the threshold
#   was 5.  On the arm of record it is +10.9, where the CONTROL -- the same code, the same steps -- is
#   good to +0.2.  The reason is nameable: `n_s` moves +2.39 grid steps here and the stencil's
#   quadratic is built on +-1.  The same thing happens on the 185-bin range at +12.8 and 2.57 steps
#   (`cc66.68`), so it is the excursion and not this range.*
#   ⇒ *** So the model's PARAMETERS are still quotable -- PART 2 reads them, and the real run
#       at them is what PART 5 scores -- but the model's CHI-SQUARED is not.  The gate is kept and
#       INVERTED: it asserts the miss two-sided and asserts the step count that explains it, so a
#       stencil rebuilt wide enough to recover agreement fails here and has to be read. ***
if abs(_MISS['control (LCDM)']) > 2.0:
    fail.append(f"control: the verified chi^2 is {_MISS['control (LCDM)']:+.1f} from the model's")
if not (abs(_MISS['CR, crossing'] - 10.932003) < 0.02 and abs(_NSTEP - 2.3850457) < 5e-4):
    fail.append(f"the arm's miss is {_MISS['CR, crossing']:+.3f} at {_NSTEP:+.4f} steps of n_s, "
                "not the +10.932 at +2.385 measured at cc66.69")
print(f"\n  ⇒ ⛔ ** THE CONTROL'S RUN LANDS WHERE THE MODEL SAID ({_MISS['control (LCDM)']:+.1f}) AND THE "
      f"ARM'S DOES NOT ({_MISS['CR, crossing']:+.1f}). **")
print(f"  *Because n_s moves {_NSTEP:+.2f} grid steps on the arm of record and the stencil's quadratic")
print("  is built on +-1.  So the model's PARAMETERS are quotable -- PART 2 reads them and PART 5")
print("  scores the real run at them -- and the model's chi^2 is not.*")
print("  ⌗ *The 185-bin range does the same at +12.8 and +2.57 steps (cc66.68), so this is the")
print("  excursion and not the range.*")

print()
print("=" * 104)
print("  PART 2 -- ** THE PARAMETERS AT THE MINIMUM **")
print("=" * 104)
for nm in ARMS:
    print(f"\n  {nm}")
    print(f"    {'':>8} {'start':>10} {'best fit':>10} {'moved':>10} {'in steps':>10}")
    for i, k in enumerate(STEP):
        th0 = B[nm]['th0'][k]
        print(f"    {k:>8} {th0:>10.4f} {th0 + R[nm].x[i]:>10.4f} {R[nm].x[i]:>+10.4f} "
              f"{R[nm].x[i] / STEP[k]:>+9.2f}s")
d_h0 = R['CR, crossing'].x[0]
d_om = R['CR, crossing'].x[1]
print(f"""
  ⇒ *** THE ANSWER TO THE QUESTION THE ORDER ASKED. ***  Given four free parameters the crossing arm
  moves H0 by {d_h0:+.4f} and Omega_m by {d_om:+.4f} -- ** {abs(d_h0 / 68.60) * 100:.3f}% and {abs(d_om / 0.2973) * 100:.2f}%. **
  *(68.60, 0.2973) came from DESI DR2 BAO and theta_*, with no spectrum involved.*  ⛔⛔ ** AND ON
  THE ARM OF RECORD THE ANSWER SPLITS: THE EXPANSION RATE STAYS THERE AND THE MATTER DENSITY DOES
  NOT. **  *H0 moves {abs(d_h0 / 68.60) * 100:.3f}% -- a thirtieth of a per cent is 0.033%, so it is
  inside by a factor of twenty-five.  Omega_m moves {abs(d_om / 0.2973) * 100:.2f}%, which is
  {abs(d_om / 0.2973) * 100 / (1 / 30.):.0f} times it.  On the NAMESAKE arm both were inside, at
  0.001% and 0.20%.  So `the spectrum, given the freedom to go anywhere, stays there` is HALF this
  range's reading and half the namesake's, and the 185-bin range says the same thing with
  0.022% and 2.123% (`cc66.68`).*
  ⌗ ** The tilt is the one parameter that moves: ** the arm wants n_s = {B['CR, crossing']['th0']['NS'] + R['CR, crossing'].x[3]:.4f}
  against the control's {B['control (LCDM)']['th0']['NS'] + R['control (LCDM)'].x[3]:.4f} -- bluer by
  {(R['CR, crossing'].x[3] - R['control (LCDM)'].x[3]):.4f}, which is {abs(R['CR, crossing'].x[3] - R['control (LCDM)'].x[3]) / STEP['NS']:.1f} steps and is a real difference between the arms.""")
# ⛔⛔⛔ r7645+cc66.69: ** AND THE GATE THAT WAS SUPPOSED TO HOLD THIS COULD NEVER HAVE FAILED
#   FOR IT. **  *As written it read `abs(d_om) > 0.01` -- an ABSOLUTE bound on Omega_m, which at
#   0.2973 is 3.4 PER CENT.  The claim beside it is "stays where the distances put it", i.e. inside a
#   thirtieth of a per cent.  The namesake's 0.20% passed it and so does the arm of record's 2.16%:
#   the bound is sixteen times the arm's actual move and a hundred times the claim.*
#   ⇒ *** A tolerance that cannot fail for the thing it names is worse than none, because it
#       reports. Replaced by two PER CENT gates, one per parameter, pinned two-sided at the measured
#       values, so H0's half asserts that it holds and Omega_m's asserts that it does NOT. ***
_PH0, _POM = 100 * d_h0 / 68.60, 100 * d_om / 0.2973
if not (abs(_PH0) < 1 / 30. and abs(_PH0 + 0.00128348) < 5e-6):
    fail.append(f"H0 moved {_PH0:+.5f}% -- not the -0.00128% inside a thirtieth of a per cent "
                "measured at cc66.69")
if not (abs(_POM) > 1 / 30. and abs(_POM + 2.164128) < 5e-4):
    fail.append(f"Omega_m moved {_POM:+.4f}% -- not the -2.1641%, 65 times a thirtieth of a per "
                "cent, measured at cc66.69; a run that returns the namesake's -0.20% fails here")
if not abs(_PH0) < 1 / 30. < abs(_POM):
    fail.append("the claim no longer SPLITS, which is this revision's whole reading")

print()
print("=" * 104)
print("  PART 3 -- ** THE FLATNESS TEST: is each 'best fit' a measurement? **")
print("=" * 104)
print(f"  {'arm':>16} {'param':>7} {'step':>9} {'d(chi2) +1':>12} {'-1':>10} {'verdict':>14}")
for nm in ARMS:
    for i, k in enumerate(STEP):
        xp, xm = R[nm].x.copy(), R[nm].x.copy()
        xp[i] += STEP[k]
        xm[i] -= STEP[k]
        dp, dm = chi2_at(B[nm], xp) - R[nm].fun, chi2_at(B[nm], xm) - R[nm].fun
        ok = min(dp, dm) > 1.0
        print(f"  {nm if i == 0 else '':>16} {k:>7} {STEP[k]:>9.4f} {dp:>12.2f} {dm:>10.2f} "
              f"{'CONSTRAINED' if ok else 'FLAT':>14}")
        if not ok:
            fail.append(f"{nm}: {k} is FLAT -- its best fit is not a measurement")
print(f"""
  ⇒ ** All four are constrained on both arms. **  *Which is why "H0 moved by {d_h0:+.4f}" means AT A
  SHARP MINIMUM and not UNCONSTRAINED -- a one-step move in H0 costs {min(chi2_at(B['CR, crossing'], R['CR, crossing'].x + np.array([STEP['H0'], 0, 0, 0])) - R['CR, crossing'].fun, chi2_at(B['CR, crossing'], R['CR, crossing'].x - np.array([STEP['H0'], 0, 0, 0])) - R['CR, crossing'].fun):.0f} in chi^2.*
  ⌗ *Before r6788+cc66.17 the n_s row read 0.00 and 0.00 on both arms: `NS` was shadowed by two more
  copies of the literal 0.965 on the hierarchy path, which is the path this grid runs.  **This table
  is what caught it.***""")

print()
print("=" * 104)
print("  PART 4 -- ** THE TWO FOLLOW-UPS **")
print("=" * 104)


def comb(P, n=3):
    nn = np.arange(1, n + 1, dtype=float)
    A = np.vstack([nn, np.ones_like(nn)]).T
    lA, b = np.linalg.lstsq(A, np.asarray(P[:n], float), rcond=None)[0]
    return float(lA), float(np.pi * b / lA)


def peaks_raw(ls, Dl, n=4, order=3):
    return [float(ls[i]) for i in argrelextrema(Dl, np.greater, order=order)[0][:n]]


def peaks_sub(ls, Dl, n=4, order=3):
    """the same locator, with the apex refined by the parabola through its three samples.

    *Validated in the 185-bin sibling against a banked `LSTEP=1` spectrum before use: at the grid
    this refit runs on, the raw locator errs by 3.8 in ell and this one by 0.02.*
    """
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


# ⛔⛔⛔ r7645+cc66.69: ** BOTH SIDES OF THIS COMPARISON WERE WRONG AND IN OPPOSITE WAYS. **
#   *As written, the "after" column was COMPUTED from raw `argrelextrema` peaks on the spectrum's own
#   `LSTEP=8` abscissa, and the "before" column was the LITERALS 2.3 and 0.9, typed in from
#   elsewhere.  So the table compared a measurement against a number nothing here measures, on a
#   locator quantised to 8 in ell.*
#   ⇒ *** And that is the quantity `cc66.18`'s 4.5 per cent was withdrawn as: the 185-bin sibling
#       measured the raw locator erring by 3.8 in ell where the parabolic refinement errs by 0.02, and
#       found the CONTROL returning the same 4.5 per cent.  This table was still built on it. ***
#   ⛭⛭⛭ ** THE RE-POINT MAKES THE CASE UNANSWERABLY: ON THE ARM OF RECORD THE RAW LOCATOR
#       RETURNS A BIT-IDENTICAL PEAK SET BEFORE AND AFTER THE REFIT. **  *A four-parameter fit that
#       moves chi^2 by 135 leaves 220 / 532 / 812 / 1132 unchanged, so the raw phase is 0.72 per cent
#       both times and cannot see the refit at all.  No argument about locators is needed; the
#       locator reports the same number for two different spectra.*
#   ⌗ *Both columns are now computed, on BOTH locators, from the two spectra this receipt already
#   reads: `cr_base` of the arm's own grid for "before" and the verified minimum for "after".*
lA_s, phi_s = comb(SKY)
_SPEC = {'before': load(os.path.join(GRIDS['cr'], 'cr_base.npz')),
         'after': load(os.path.join(SPEC, _VER['cr']))}
_T = {}
for _lab, _z in _SPEC.items():
    for _kind, _fn in (('raw', peaks_raw), ('refined', peaks_sub)):
        _P = _fn(*_z)
        _T[(_lab, _kind)] = (_P, abs(comb(_P)[1] / phi_s - 1) * 100,
                             abs(_P[3] / SKY[3] - 1) * 100)
print(f"  {'':>15} {'peaks':>38} {'phase % out':>12} {'4th peak %':>11}")
for _lab in ('before', 'after'):
    for _kind in ('raw', 'refined'):
        _P, _ph, _p4 = _T[(_lab, _kind)]
        print(f"  {_lab + ', ' + _kind:>15} {' / '.join(f'{v:8.2f}' for v in _P):>38} "
              f"{_ph:>11.2f}% {_p4:>10.2f}%")
print(f"  {'the sky':>15} {' / '.join(f'{v:8.2f}' for v in SKY):>38}")
_RB, _RA = _T[('before', 'raw')], _T[('after', 'raw')]
_FB, _FA = _T[('before', 'refined')], _T[('after', 'refined')]
print(f"""
  \u21d2 ⛭⛭⛭ *** THE RAW LOCATOR CANNOT SEE THE REFIT: it returns the SAME peak set before and
  after, {[int(v) for v in _RB[0]]}, so its phase is {_RB[1]:.2f} per cent both times *** -- across a
  fit that moves chi^2 by {R['CR, crossing'].fun - chi2_at(B['CR, crossing'], np.zeros(4)):+.0f}.
  *That is the whole case against the raw number, made by the number itself.*

  \u21d2 *** AND ON THE REFINED LOCATOR THE VERDICT STANDS: THE PHASE GETS WORSE. ***  {_FB[1]:.2f} per
  cent before against {_FA[1]:.2f} after -- it nearly TRIPLES -- and the fourth peak barely moves,
  {_FB[2]:.2f} against {_FA[2]:.2f}.  ** So neither residual is removed by freedom, and on the chat
  seat's own criterion they are properties of the CONSTRUCTION and not background choices. **
  \u2317 *This file's name says `does not close the phase`, and on the arm of record read with a
  locator whose resolution is measured, it does not: the name holds.  What changes is the evidence --
  the namesake's 2.3 -> 4.5 was the grid's number on both ends.*""")
if not (_RB[0] == _RA[0] == [220.0, 532.0, 812.0, 1132.0]
        and abs(_RB[1] - 0.7177288761125111) < 5e-6
        and abs(_RA[1] - 0.7177288761125111) < 5e-6):
    fail.append(f"the raw locator no longer returns one peak set across the refit: {_RB[0]} then "
                f"{_RA[0]} -- which is cc66.69's central reading here")
if not (abs(_FB[1] - 1.3176188962799817) < 5e-6 and abs(_FA[1] - 3.6935232121655726) < 5e-6
        and _FA[1] > 2.5 * _FB[1]):
    fail.append(f"the refined phase is {_FB[1]:.4f} -> {_FA[1]:.4f}, not the 1.3176 -> 3.6935 "
                "measured at cc66.69")
if not (abs(_FB[2] - 0.4653093973312483) < 5e-6 and abs(_FA[2] - 0.5140431738418938) < 5e-6
        and abs(_FA[2] / _FB[2] - 1) < 0.15):
    fail.append(f"the refined fourth peak is {_FB[2]:.4f} -> {_FA[2]:.4f}, not the 0.4653 -> 0.5140 "
                "measured at cc66.69")

print()
print("=" * 104)
print("  PART 5 -- ** WHAT IT COSTS AND WHAT IT DOES NOT BUY **")
print("=" * 104)
cL, nL = real['control (LCDM)']
cC, nC = real['CR, crossing']
_C0L = chi2_at(B['control (LCDM)'], np.zeros(4))
_C0C = chi2_at(B['CR, crossing'], np.zeros(4))
# ⛭ r7645+cc66.69: the as-computed ratio is now COMPUTED here rather than typed into the prose
#   below, where it read `2.22x` -- the namesake's.  *Pinned two-sided with the verified ratio.*
if not (abs(_C0C / _C0L - 2.349253) < 5e-5 and abs(cC / cL - 1.535305) < 5e-5):
    fail.append(f"the ratios are {_C0C / _C0L:.6f}x as-computed and {cC / cL:.6f}x verified, not "
                "the 2.349253 and 1.535305 measured at cc66.69")
print(f"  {'':>28} {'chi2':>9} {'/bin':>7}")
print(f"  {'control, refitted':>28} {cL:>9.1f} {cL / nL:>7.2f}")
print(f"  {'CR arm, refitted':>28} {cC:>9.1f} {cC / nC:>7.2f}")
print(f"  {'ratio':>28} {cC / cL:>9.2f}x")
print(f"""
  ⇒ ** {cC / cL:.2f}x at the verified minimum, against {_C0C / _C0L:.2f}x as-computed on the same
  bins. **  *Freedom closes {100 * (1 - (cC / cL - 1) / (_C0C / _C0L - 1)):.0f} per cent of the excess
  over one and leaves the rest.*  ⛔ ** The arm is still disfavoured, and that is the result rather
  than a caveat on it. **  ⌗ *On the NAMESAKE arm these were 1.45x and 2.22x, and `about a third of
  the gap` was that arm's arithmetic; here freedom closes rather more than a third.*

  ⚠ ** AND THE RANGE IS 132 BINS, ell 100-1287, NOT THE 185 THE ORDER FIRST ASKED FOR. **  *The
  damping tail is where omega_b and n_s carry most of their leverage, so those two are the loosest
  numbers here.  H0 and Omega_m are set by the peak positions and the comb, all inside this range,
  so the question the order actually asked is answered on it.*  ⌗ *The chat seat ruled at r6788 to
  take this configuration with the range stated as its cost.*
""")

print("=" * 104)
if fail:
    print("  FAILED:")
    for f in fail:
        print(f"    - {f}")
    sys.exit(1)
print("  ✓ ALL CHECKS PASSED")
print("=" * 104)
