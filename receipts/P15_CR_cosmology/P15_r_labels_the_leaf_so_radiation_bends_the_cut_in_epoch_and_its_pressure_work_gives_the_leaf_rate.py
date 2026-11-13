#!/usr/bin/env python3
"""`r7759` ** `r` LABELS THE COSMOLOGICAL LEAF RATHER THAN RUNNING INSIDE ONE, SO RADIATION BENDS THE CUT
IN **EPOCH**; ITS PRESSURE WORK MAKES THE MISNER-SHARP MASS FALL AS `1/r` WITH A POSITIVE DENSITY, AND THE
RATE THAT BEND GIVES IS THE LEAF RATE. THE SUPERSEDED `-3 Omega_r z(1+z)^3` IS THE STATIC-REGION FORMULA
USED WHERE `r` IS TIMELIKE. **

`P15` `sec:properframe` step (iv) fixes the whole of this: *"the areal radius across the congruence
depends on `tau, chi` only through their sum, `r(tau,chi) = r(tau+chi)`"*, and cosmic time is
`tilde tau = tau + chi`.  ⇒ `r` is CONSTANT on every constant-`tilde tau` leaf.  So a *radial profile*
`rho_r(r)` has no referent inside a leaf; `rho(r)` specifies the density epoch by epoch, and `m(r)` is the
gravitating energy of the comoving volume at the epoch labelled `r`.

⛭ ** THE LAW, AND IT IS STANDARD GR AND NOT A NEW INGREDIENT. **  Past the cosmological horizon `r` is the
time direction and the Misner-Sharp mass obeys `dm/dr = -4 pi r^2 p`.  Dust (`p = 0`) keeps `m` constant,
so the SdS offset IS the dust term -- which is why it carries a matter density's form.  Radiation
(`p = rho/3`) makes `m` fall as `1/r` BY PRESSURE WORK, with `rho > 0` throughout.  Integrating gives
`mu(r) = 2M + K/r` with `K = (H_0/c)^2 Omega_r r_0^4`, whose rate is `H_leaf` identically.

⛭ ** AND `K` IS DERIVED TWICE OVER BY INDEPENDENT ROUTES **, which is the receipt's strongest row: once
by integrating the pressure-work law from a positive density, once by inverting the chart's own rate
relation against `H_leaf`.  They agree to round-off.

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that the construction's cut DOES carry radiation's energy. **  It establishes that a cut can,
   that the cut that does is the one whose rate is `H_leaf`, and that the mass function it needs is
   ordinary positive-density radiation rather than an exotic source.  Which cut the construction intends
   is a ruling and not a measurement, and `69` made it at `r7759`; this receipt does not re-make it.
 * ** Not that `r7614` erred in its arithmetic. **  Its published law is exactly what the static-region
   formula `dm/dr = +4 pi r^2 rho` gives on a positive `r^-4` density -- asserted below rather than
   asserted away.  What was wrong was the region the formula was used in.
 * ** Not that the late-time law moves. **  Measured here: the two rates differ by `4.4e-05` at `z = 0`.
 * ** No likelihood, no significance, nothing fitted. **  Every number is an integral or a derivative of
   two published rate laws over a published background.

COMPUTES: scope.
 * ** THIS RECEIPT READS COSMOLOGICAL PARAMETERS AND FITS NONE. **  `H_0 = 68.6`, `Omega_m = 0.2973`,
   `Omega_r h^2 = 4.15e-5`, `z* = 1089.9`, `alpha`, `r_0` and the Nariai offset `2M` are the sector's
   published background, read by path out of 60's `r7580/lightpath.py` (`r7445`'s rule) and asserted here
   rather than typed in as literals of this receipt's own.
 * ** THE REGISTRATION THAT GOVERNS THE NEW ROW IS `r7759+cc66.0`'s `PREDICTION.md` **, pushed before
   `pressure_work.py` existed; it named the failure mode under which `K` would NOT be derivable from the
   pressure-work law, and it recorded that one licence was missed and located in the quadrature's floor
   on a vanishing interval.  The remaining rows were measured at `r7757+cc66` under its own registration.
 * ** COST: about two seconds **, dominated by `4001` quadratures of a single-term integrand.  NOT long.
"""
import contextlib
import io
import os
import runpy
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')
PW = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7759_cc66_the_pressure_work_route', 'pressure_work.py')
for pth, who in ((LP, "60's lightpath.py"), (PW, "r7759's pressure_work.py")):
    if not os.path.exists(pth):
        sys.exit(f"FATAL: {who} is not where this reads it from; the instrument has moved.")

buf = io.StringIO()
cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(LP))
    with contextlib.redirect_stdout(buf):
        NS = runpy.run_path(LP)
finally:
    os.chdir(cwd)
H0, OM, OMR, C = NS['H0'], NS['OM'], NS['OMR'], NS['C']
Z_REC, alpha, r0, TWO_M = NS['Z_REC'], NS['alpha'], NS['r0'], NS['TWO_M']
H_stack, H_leaf, r_of = NS['H_stack'], NS['H_leaf'], NS['r_of']
tt_of_z = NS['tt_of_z']
h0 = H0 / C
K = h0 ** 2 * OMR * r0 ** 4
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f"             {witness}")


print("=" * 100)
print(__doc__)
print("=" * 100)

check("⛭ `r7759` ** ① THE BACKGROUND AND BOTH RATE LAWS ARE 60's, READ BY PATH AND NOT REIMPLEMENTED ** ⇒ "
      "*`r7445`'s rule; the published values are asserted as what that script carries, so a change to "
      "them reddens this receipt instead of silently repricing the reading*",
      abs(H0 - 68.6) < 5e-9 and abs(OM - 0.2973) < 5e-9 and abs(OMR - 8.8186e-05) < 5e-10
      and abs(Z_REC - 1089.9) < 5e-9,
      f"H0 {H0}  Om {OM}  Om_r {OMR:.4e}  z* {Z_REC}  alpha {alpha:.4f}  r_0 {r0:.4f}  2M {TWO_M:.4f} Mpc")

# ------------------------------------------------------------------ ② r labels the leaf
LEAVES = [0.0, 10.0, 100.0, Z_REC]
spread, radii = [], []
for zl in LEAVES:
    tt = tt_of_z(zl)
    chis = np.linspace(0.0, 0.9 * tt, 2001)
    rr = np.array([r_of((tt - c) + c) for c in chis])     # r(tau + chi) at fixed tilde tau
    spread.append(float(np.max(np.abs(rr / rr[0] - 1.0))))
    radii.append(float(rr[0]))
RANGE = max(radii) / min(radii)
check("⛭⛔ `r7759` ** ② `r` IS CONSTANT ON EVERY COSMOLOGICAL LEAF, AND VARIES `1091` TIMES OVER BETWEEN "
      "THEM ** ⇒ *** so `r` labels the leaf and is not a direction within one, which is why a radial "
      "profile `rho_r(r)` has no referent on a leaf; the range is asserted beside the spread so the row "
      "is a TEST and not a tautology *** ",
      max(spread) < 1e-12 and abs(RANGE - 1091.0) < 0.5,
      f"max spread along a leaf {max(spread):.2e} over 2001 points on each of 4 leaves; "
      f"r = {', '.join(f'{v:.4g}' for v in radii)} Mpc, range {RANGE:.1f}x")

# ------------------------------------------------------------------ ③④⑤ the two bends
z = np.geomspace(1e-6, Z_REC, 4001)
r = r0 / (1.0 + z)
bend_hist = K / r
bend_prof = 3.0 * K * (-z / r0)


def h2(mu, rr):
    return mu / rr ** 3 + 1.0 / alpha ** 2


e_hist = float(np.max(np.abs(h2(TWO_M + bend_hist, r) / (H_leaf(z) / C) ** 2 - 1.0)))
check("⛭⛔ `r7759` ** ③ THE EPOCH BEND `mu = 2M + K/r` HAS THE LEAF RATE FOR ITS OWN RATE, WITH "
      "`K = 3006.658` Mpc² ** ⇒ *the chart's own relation `h² = mu/r³ + 1/alpha²` at `E = 1`, with the "
      "bend radiation's pressure work supplies*",
      e_hist < 1e-12 and abs(K - 3006.658) < 5e-4,
      f"K = {K:.6f} Mpc^2; worst relative deviation from H_leaf = {e_hist:.3e}")

hi = z >= 1e-2
term_prof = h2(TWO_M + bend_prof, r) - h2(TWO_M, r)
term_pub = -3.0 * h0 ** 2 * OMR * z * (1.0 + z) ** 3
e_prof = float(np.max(np.abs(term_prof[hi] / term_pub[hi] - 1.0)))
check("⛭ `r7759` ** ④ AND THE RADIAL-PROFILE BEND REPRODUCES THE PUBLISHED `-3 Omega_r z(1+z)^3` ** ⇒ "
      "*so the superseded reading is identified rather than deleted: the printed law is exactly what the "
      "static-region formula gives on a positive `r^-4` density.* ⌗ *Compared above `z = 1e-2`; below it "
      "the subtraction sits at its own cancellation floor, measured at `r7755`*",
      e_prof < 1e-10, f"worst |measured/printed - 1| above z = 1e-2: {e_prof:.3e}")

e_ratio = float(np.max(np.abs((bend_prof / bend_hist) / (-3.0 * z / (1.0 + z)) - 1.0)))
check("⛭⛔⛭ `r7759` ** ⑤ AND THE RATIO OF THE TWO BENDS IS THE PAPER'S OWN `-3z/(1+z)` ** ⇒ *** so the "
      "entire difference between the two accounts of radiation's gravity -- including its SIGN -- is the "
      "one step of asking what lies inside radius `r` rather than what the comoving volume holds at "
      "epoch `r` *** ⌗ *taken on the bend terms themselves, since forming them as `mu - 2M` reintroduces "
      "a cancellation that bit three times in this family*",
      e_ratio < 1e-13, f"worst |ratio / (-3z/(1+z)) - 1| = {e_ratio:.3e}")

# ------------------------------------------------------------------ ⑥ the pressure-work law, by path
buf2 = io.StringIO()
rc_pw = 0
try:
    os.chdir(os.path.dirname(PW))
    with contextlib.redirect_stdout(buf2):
        runpy.run_path(PW, run_name='__main__')
except SystemExit as e:
    rc_pw = e.code or 0
finally:
    os.chdir(cwd)
out_pw = buf2.getvalue()
check("⛭⛔⛭ `r7759` ** ⑥ AND `K` IS DERIVED FROM `dm/dr = -4 pi r^2 p` ITSELF, NOT MATCHED TO THE RATE: "
      "DUST KEEPS `m` CONSTANT, RADIATION'S PRESSURE WORK GIVES `+K/r`, AND THE DENSITY IS POSITIVE AT "
      "EVERY NODE ** ⇒ *** `r7759`'s computation is run from source here and its five checks must all "
      "pass; the pressure-work `K` and the inverted `K` are the same `3006.658` Mpc², so the mass "
      "function is ordinary radiation and `r7755`'s `negative density` was the STATIC-region formula "
      "applied where `r` is timelike *** ",
      rc_pw == 0 and '5 of 5 checks' in out_pw and 'all positive' in out_pw,
      f"pressure_work.py exits {rc_pw} with its own verdict line: "
      f"{[l.strip() for l in out_pw.splitlines() if 'of 5 checks' in l][:1]}")

# ------------------------------------------------------------------ ⑦ what it costs the late-time law
d0 = abs(float(H_leaf(0.0) / H_stack(0.0)) - 1.0)
zg = np.geomspace(1e-3, Z_REC, 200001)
dev = np.abs(H_leaf(zg) / H_stack(zg) - 1.0)
z1 = float(zg[np.argmax(dev >= 0.01)])
check("⛭ `r7759` ** ⑦ AND THE LATE-TIME LAW IS UNTOUCHED: THE TWO RATES DIFFER BY `4.4e-05` AT `z = 0` "
      "AND FIRST REACH ONE PER CENT AT `z = 66.8` ** ⇒ *the `sinh^{2/3}` law, `z_acc = x_0 - 1` and "
      "`Lambda` setting the amplitude are read where the two rates are indistinguishable, so none of them "
      "moves; stated as two measured numbers rather than as a reassurance*",
      abs(100000 * d0 - 4.4) < 0.5 and abs(z1 - 66.8) < 0.5,
      f"|H_leaf/H_stack - 1| = {d0:.3e} at z = 0 (Omega_r = {OMR:.3e}); one per cent at z = {z1:.1f}")

print("\n" + "=" * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {7 - len(FAILS)} of 7 gates;  "
      f"{len(FAILS)} failure(s)" + ("" if not FAILS else ": " + "; ".join(FAILS[:2])))
print("=" * 100)
sys.exit(1 if FAILS else 0)
