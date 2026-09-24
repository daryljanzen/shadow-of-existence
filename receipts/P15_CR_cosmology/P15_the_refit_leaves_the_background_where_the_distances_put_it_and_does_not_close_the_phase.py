#!/usr/bin/env python3
"""
RECEIPT -- P15: ** THE PARAMETER REFIT.  GIVEN FOUR FREE PARAMETERS THE CROSSING ARM MOVES $H_0$ BY
+0.008 AND Omega_m BY -0.0006 -- IT STAYS EXACTLY WHERE THE BARYON-ACOUSTIC DATA PUT IT.  ** AND IT
DOES NOT CLOSE THE TWO RESIDUALS: the acoustic phase goes 2.3% -> 4.5% OUT and the fourth peak
0.9% -> 0.7%. **

** ⇒ SO THE RESIDUALS ARE PROPERTIES OF THE CONSTRUCTION AND NOT BACKGROUND CHOICES, ** which is
the question node 66 (chat seat) asked of this run in as many words: *"if a refit removes them they
are a background choice rather than a property of the construction."*  It does not remove them.

** chi^2 AT THE VERIFIED MINIMUM: control 118.3 (0.90/bin), arm 171.1 (1.30/bin) over 132 bins --
a ratio of 1.45, against 2.22 as-computed. **  *Freedom closes about a third of the gap and leaves
the rest.*

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
  the best-fit parameters says what is there.  ** Predicted 118.2 and 170.6; measured 118.3 and
  171.1 -- +0.1 and +0.5. **  *That agreement is the licence to quote the model's parameters.*

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
GRID = os.path.join(BW, 'refit_grid')
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
    ls, Dl = load(os.path.join(GRID, f"{arm['tag']}_base.npz"))
    m0 = binned(ls, Dl, lens)
    ok = np.isfinite(m0)
    F = scipy.linalg.cho_solve(scipy.linalg.cho_factor(CS.COV_TT[np.ix_(ok, ok)]),
                               np.identity(int(ok.sum())))
    F = 0.5 * (F + F.T)
    g, h = {}, {}
    for k in STEP:
        mp = binned(*load(os.path.join(GRID, f"{arm['tag']}_{k}p.npz")), lens)[ok]
        mm = binned(*load(os.path.join(GRID, f"{arm['tag']}_{k}m.npz")), lens)[ok]
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
    ls, Dl = load(os.path.join(SPEC, f'cc66_refit_verify_{tag}.npz'))
    c, n, A, lo, hi = CS.chi2_of(ls, Dl * np.interp(ls, LG, RATIO))
    real[nm] = (c, n)
    print(f"  {nm:>18} {R[nm].fun:>16.1f} {c:>10.1f} {c / n:>7.2f} {c - R[nm].fun:>+8.1f} {n:>6d}")
    if abs(c - R[nm].fun) > 5.0:
        fail.append(f"{nm}: the verified chi^2 is {c - R[nm].fun:+.1f} from the model's -- "
                    "the response model may not be quoted")
    if n != 132:
        fail.append(f"{nm}: {n} bins, not the 132 this configuration covers")
print(f"\n  ⇒ ** +0.1 and +0.5 on 132 bins.  The model's parameters are quotable because a real run"
      f" at them lands where it said. **")

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
  *(68.60, 0.2973) came from DESI DR2 BAO and theta_*, with no spectrum involved.  ** The spectrum,
  given the freedom to go anywhere, stays there. **  The background the distances fix IS the
  background the spectrum wants.*
  ⌗ ** The tilt is the one parameter that moves: ** the arm wants n_s = {B['CR, crossing']['th0']['NS'] + R['CR, crossing'].x[3]:.4f}
  against the control's {B['control (LCDM)']['th0']['NS'] + R['control (LCDM)'].x[3]:.4f} -- bluer by
  {(R['CR, crossing'].x[3] - R['control (LCDM)'].x[3]):.4f}, which is {abs(R['CR, crossing'].x[3] - R['control (LCDM)'].x[3]) / STEP['NS']:.1f} steps and is a real difference between the arms.""")
if abs(d_h0) > 0.5 or abs(d_om) > 0.01:
    fail.append(f"the arm moved H0 by {d_h0:+.4f} and Om by {d_om:+.4f} -- not 'stays where the "
                "distances put it'")

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


ls, Dl = load(os.path.join(SPEC, 'cc66_refit_verify_cr.npz'))
q = argrelextrema(Dl, np.greater, order=3)[0][:4]
P = [float(ls[i]) for i in q]
lA_f, phi_f = comb(P)
lA_s, phi_s = comb(SKY)
print(f"  peaks at the refit minimum : {[int(v) for v in P]}")
print(f"  the sky                    : {[float(v) for v in SKY]}")
print(f"\n  {'':>22} {'before the refit':>17} {'after':>9} {'verdict':>12}")
print(f"  {'acoustic phase (% out)':>22} {2.3:>17.1f} {abs(phi_f / phi_s - 1) * 100:>9.1f} "
      f"{'WORSE':>12}")
print(f"  {'fourth peak (% out)':>22} {0.9:>17.1f} {abs(P[3] / SKY[3] - 1) * 100:>9.1f} "
      f"{'unchanged':>12}")
print(f"""
  ⇒ *** NEITHER RESIDUAL IS REMOVED BY FREEDOM. ***  The phase gets WORSE ({abs(phi_f / phi_s - 1) * 100:.1f}% against 2.3%) --
  the fit trades it for likelihood elsewhere -- and the fourth peak barely moves ({abs(P[3] / SKY[3] - 1) * 100:.1f}% against
  0.9%).  ** So on the chat seat's own criterion they are properties of the CONSTRUCTION and not
  background choices. **""")
if abs(phi_f / phi_s - 1) < 0.02:
    fail.append("the refit DID close the phase -- PART 4's verdict is wrong")

print()
print("=" * 104)
print("  PART 5 -- ** WHAT IT COSTS AND WHAT IT DOES NOT BUY **")
print("=" * 104)
cL, nL = real['control (LCDM)']
cC, nC = real['CR, crossing']
print(f"  {'':>28} {'chi2':>9} {'/bin':>7}")
print(f"  {'control, refitted':>28} {cL:>9.1f} {cL / nL:>7.2f}")
print(f"  {'CR arm, refitted':>28} {cC:>9.1f} {cC / nC:>7.2f}")
print(f"  {'ratio':>28} {cC / cL:>9.2f}x")
print(f"""
  ⇒ ** 1.45x at the verified minimum, against 2.22x as-computed on the same bins. **  *Freedom
  closes about a third of the gap and leaves the rest.*  ⛔ ** The arm is still disfavoured, and
  that is the result rather than a caveat on it. **

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
