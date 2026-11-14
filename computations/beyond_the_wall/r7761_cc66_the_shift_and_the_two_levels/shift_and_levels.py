#!/usr/bin/env python3
"""`r7761+cc66` DOES RADIATION TOUCH THE **SHIFT**, AND DO THE TWO LEVELS AGREE ON `Omega_m`?

⛭ Registered in `PREDICTION.md` at `r7761+cc66.0`, pushed before this file existed, with `R1`-`R3`'s
rows and their licences set there.

⛭ ** THE CHART AND THE BACKGROUND ARE 60's, READ BY PATH ** (`r7445`): `r7580/lightpath.py`.  `z_acc` and
its error are read from `P15` `eq:zacc` as printed: `0.6648 +/- 0.0467`.

THE ADM FORM ON THE COSMOLOGICAL FOLIATION.  The proper-frame line element is
`ds^2 = -dtau^2 + (d_chi r)^2 dchi^2 + r^2 dOmega^2` with cosmic time `tilde tau = tau + chi`.  Putting
`tau = tilde tau - chi`,

        g_tt = -1 ,   g_t chi = +1 ,   g_chi chi = (d_chi r)^2 - 1 ,

so comparing with `ds^2 = -N^2 dt^2 + h_ij (dx^i + N^i dt)(dx^j + N^j dt)`,

        N^chi = 1 / ((d_chi r)^2 - 1) ,     N^2 = (d_chi r)^2 / ((d_chi r)^2 - 1) ,

and both are functions of the ONE quantity `d_chi r = dr/d tilde tau`, whose square is `mu(r)/r + r^2/a^2`.
"""
import contextlib
import io
import os
import runpy
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')
if not os.path.exists(LP):
    sys.exit("FATAL: 60's lightpath.py is not where this reads it from; the chart has moved.")
buf = io.StringIO()
cwd = os.getcwd()
try:
    os.chdir(os.path.dirname(LP))
    with contextlib.redirect_stdout(buf):
        NS = runpy.run_path(LP)
finally:
    os.chdir(cwd)
H0, OM, OMR, C = NS['H0'], NS['OM'], NS['OMR'], NS['C']
Z_REC, alpha, r0, TWO_M, x03 = NS['Z_REC'], NS['alpha'], NS['r0'], NS['TWO_M'], NS['x03']
H_stack, H_leaf = NS['H_stack'], NS['H_leaf']
h0 = H0 / C
K = h0 ** 2 * OMR * r0 ** 4
Z_ACC, Z_ACC_ERR = 0.6648, 0.0467          # INPUT  x0 = 1.6648 +- 0.0467, corpus measured; P15 eq:zacc, as printed
OM_REFIT = 0.2945                          # 70's leaf-rate refit, quoted in the r7761 order
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

ZS = [0.0, 66.8, Z_REC]


def dchir2(rr, bent):
    mu = TWO_M + (K / rr if bent else 0.0)
    return mu / rr + rr ** 2 / alpha ** 2


def adm(rr, bent):
    s = dchir2(rr, bent)
    return s, 1.0 / (s - 1.0), np.sqrt(s / (s - 1.0))     # (d_chi r)^2, N^chi, N


# ------------------------------------------------------------------ R1 ① the reconstruction is right
worst = 0.0
for zz in ZS:
    rr = r0 / (1.0 + zz)
    for bent in (False, True):
        s, Nx, N = adm(rr, bent)
        g_cc = s - 1.0
        worst = max(worst, abs(-N ** 2 + g_cc * Nx ** 2 - (-1.0)), abs(g_cc * Nx - 1.0))
check("⛭ `r7761` ** ① THE ADM RECONSTRUCTION IS RIGHT ON BOTH CUTS ** ⇒ *`-N² + g_χχ(N^χ)² = g_tt = -1` "
      "and `g_χχ N^χ = g_tχ = +1`, asserted before anything is read off `N` or `N^χ`*",
      worst < 1e-12, f"worst residual over 3 redshifts x 2 cuts: {worst:.3e}")

# ------------------------------------------------------------------ R1 ②③ radiation moves both
print("\n      the cosmological foliation's lapse and shift, straight cut against bent:")
print(f"      {'z':>8} {'(d_chi r)^2 str':>16} {'bent':>14} {'Δ(d_chi r)^2':>14} {'ΔN':>12} {'ΔN^chi':>12}")
rows = {}
for zz in ZS:
    rr = r0 / (1.0 + zz)
    s0, Nx0, N0 = adm(rr, False)
    s1, Nx1, N1 = adm(rr, True)
    rows[zz] = (s1 / s0 - 1.0, N1 / N0 - 1.0, Nx1 / Nx0 - 1.0)
    print(f"      {zz:8.1f} {s0:16.6f} {s1:14.6f} {100 * rows[zz][0]:13.4f}% "
          f"{100 * rows[zz][1]:11.4f}% {100 * rows[zz][2]:11.4f}%")

check("⛭⛔⛭ `r7761` ** ② RADIATION MOVES **BOTH** THE LAPSE AND THE SHIFT, BY `32` PER CENT IN "
      "`(∂_χ r)²` AT `z*` ** ⇒ *** so the answer to Daryl's question is **both, and not only the bend**: "
      "the lapse and the shift of the cosmological foliation are two functions of the one quantity "
      "`∂_χ r = dr/dτ̃`, and the bend is inside it. The shift is where the rate APPEARS as distance and "
      "redshift, but it is not an untouched carrier. *** ",
      rows[Z_REC][0] > 0.10,
      f"at z* : Δ(∂_χ r)² = {100 * rows[Z_REC][0]:.2f} %, ΔN = {100 * rows[Z_REC][1]:.4f} %, "
      f"ΔN^chi = {100 * rows[Z_REC][2]:.2f} %")

# `r7761+cc66.1` relocated `③` -> `③′`: `N` and `N^chi` do NOT change by `Omega_r`; they change by
# `Omega_r` times the amplifier `s/(s-1)`, which is `3.975` today because `g_chi chi = s - 1` is small.
s0_now = dchir2(r0, False)
AMP = s0_now / (s0_now - 1.0)
eps = rows[0.0][0]                                        # the measured fractional change in `s` at z = 0
pred_Nx = -eps * AMP
pred_N = 0.5 * eps * (1.0 - AMP)
e_om = abs(eps - OMR) / OMR
e_Nx = abs(rows[0.0][2] / pred_Nx - 1.0)
e_N = abs(rows[0.0][1] / pred_N - 1.0)
check("⛭⛔ `r7761` ** ③′ TODAY THE BEND MOVES `(∂_χ r)²` BY `Ω_r`, BUT IT MOVES THE **SHIFT** BY `Ω_r` TIMES "
      "`3.975` ** ⇒ *** `g_χχ = (∂_χ r)² − 1` is SMALL today -- `0.336` against `1.336` -- so `N^χ = 1/(s−1)` "
      "carries sensitivity `s/(s−1)`, not `1`. My first registration licenced `< 1e-4` in all three and "
      "two of the three missed it; the amplifier is the finding, and the shift is the MOST "
      "radiation-sensitive of the three now, not the untouched carrier. *** ",
      e_om < 5e-3 and e_Nx < 1e-3 and e_N < 1e-3,
      f"Δs/s = {eps:.4e} vs Omega_r = {OMR:.4e} (rel {e_om:.2e}); amplifier s/(s-1) = {AMP:.4f}; "
      f"predicted ΔN^chi/N^chi = {pred_Nx:.4e} vs measured {rows[0.0][2]:.4e} (rel {e_Nx:.2e}); "
      f"predicted ΔN/N = {pred_N:.4e} vs measured {rows[0.0][1]:.4e} (rel {e_N:.2e})")

# ------------------------------------------------------------------ R1 ⑨ where the amplifier diverges
r_deg = alpha / np.sqrt(3.0)
res_deg = TWO_M / r_deg + r_deg ** 2 / alpha ** 2 - 1.0
z_deg = r0 / r_deg - 1.0
x0_bg = x03 ** (1.0 / 3.0)
ratio = (r0 / r_deg) / x0_bg
check("⛭⛔⛭ `r7761` ** ⑨ AND THE AMPLIFIER DIVERGES EXACTLY AT THE ACCELERATION EPOCH: `r = α/√3` IS "
      "`r₀/x₀`, AND THAT IDENTITY **IS** `Ω_m = 2/(x₀³+2)` ** ⇒ *** `2M/r + r²/α² = 1` has the exact "
      "root `r = α/√3` when `2M = 2α/(3√3)`, and the measured ratio `(r₀/r_deg)/x₀` came back `1` to "
      "seven figures. It is an identity, not a coincidence: with `r₀ = x₀α/√3`, `r₀³ = x₀³α³/(3√3)`, so "
      "`Ω_m/Ω_Λ = 2Mα²/r₀³ = 2/x₀³`, which rearranges to `Ω_m = 2/(x₀³+2)` -- the very identity `R3` "
      "tests. ** So the epoch at which this chart's constant-`τ̃` slicing DEGENERATES (`g_χχ = 0`, the "
      "shift divergent) is the acceleration epoch. ** That is why the shift's radiation sensitivity is "
      "large today: we observe from `0.3` in `g_χχ` away from the chart's own coordinate failure. *** "
      "⌗ *I had drafted this row expecting `0.3` per cent of disagreement, from my own hand arithmetic; "
      "the registration left the answer open and printed the ratio, and the ratio says identity. No "
      "claim that the degeneracy is physical rather than this chart's.*",
      abs(res_deg) < 1e-12 and abs(ratio - 1.0) < 1e-12,
      f"r_deg = alpha/sqrt(3) = {r_deg:.6f} Mpc solves it to {res_deg:.3e}; z_deg = {z_deg:.6f}; "
      f"x_0 (background) = {x0_bg:.6f}; (r_0/r_deg)/x_0 - 1 = {ratio - 1.0:.3e}")

check("⛭ `r7761` ** ⑨′ AND THE MEASURED `z_acc` AGREES WITH IT AT `0.29 σ` ** ⇒ *so the chart's degenerate "
      "radius and the observed acceleration redshift are the same epoch within its error, and `⑨`'s "
      "identity is what `⑥` was propagating an error through all along*",
      abs(z_deg - Z_ACC) / Z_ACC_ERR < 1.0,
      f"|{z_deg:.6f} - {Z_ACC}| / {Z_ACC_ERR} = {abs(z_deg - Z_ACC) / Z_ACC_ERR:.2f} sigma")

# ------------------------------------------------------------------ R1 ⑩⑪⑫ (`r7761+cc66.4`)
M_LEN = TWO_M / 2.0                       # `M` as a length, so `(M alpha^2)^{1/3}` is a radius
r_min_closed = (M_LEN * alpha ** 2) ** (1.0 / 3.0)
stat = -TWO_M / r_min_closed ** 2 + 2.0 * r_min_closed / alpha ** 2
rgrid = np.geomspace(r0 / (1.0 + Z_REC), 40.0 * r0, 400001)
s_grid = dchir2(rgrid, False)
i_min = int(np.argmin(s_grid))
# the closed form the hand algebra gives: `min (d_chi r)^2 = 2M/(M a^2)^{1/3} + (M a^2)^{2/3}/a^2`
# collapses to `3 (M/alpha)^{2/3}`, which is `1` exactly when `M = alpha/(3 sqrt 3)` -- the Nariai offset.
s_min_closed = 3.0 * (M_LEN / alpha) ** (2.0 / 3.0)
# `r7761+cc66.5` the GRID minimum cannot reach the true one: the nearest node sits `dr` off the turning
# point and the function is quadratic there, so it reads high by `(1/2) f'' dr^2`.  That is the whole of
# the `5.25e-12` my licence called a miss.
f2 = 2.0 * TWO_M / r_min_closed ** 3 + 2.0 / alpha ** 2
dr_node = abs(rgrid[i_min] - r_min_closed)
quad_excess = 0.5 * f2 * dr_node ** 2
grid_excess = float(s_grid.min()) - 1.0
check("⛭⛔ `r7761` ** ⑩ THE DEGENERACY IS THE **MINIMUM** OF `(∂_χ r)²`, AND ITS VALUE IS EXACTLY `1`: "
      "`min (∂_χ r)² = 3(M/α)^{2/3}` ** ⇒ *** `d(∂_χ r)²/dr = −2M/r² + 2r/α²` vanishes at "
      "`r = (Mα²)^{1/3}`, which for the Nariai offset IS `α/√3`, and the value there collapses to "
      "`3(M/α)^{2/3} = 1`. So `g_χχ ≥ 0` everywhere with a SINGLE zero: the constant-`τ̃` slicing touches "
      "degeneracy at one radius and is regular on both sides. *** ⛔ **MY REGISTERED LICENCE WAS WRONG "
      "AND IS REPLACED HERE**: I licenced the GRID minimum to `1e-12` and it came in `5.25e-12` high. A "
      "grid cannot do better -- the nearest node sits `dr` from the turning point and the function is "
      "quadratic there, so it reads high by `½ f″ dr²`. That accounts for the excess to a few per cent, "
      "so the row now asserts the CLOSED FORM to round-off and bounds the grid excess by that estimate.",
      abs(stat) < 1e-15 and abs(r_min_closed / r_deg - 1.0) < 1e-12
      and abs(s_min_closed - 1.0) < 1e-14 and grid_excess >= 0.0
      and abs(grid_excess / quad_excess - 1.0) < 0.1,
      f"3(M/alpha)^(2/3) - 1 = {s_min_closed - 1.0:+.3e}; (M alpha^2)^(1/3) = {r_min_closed:.6f} Mpc = "
      f"alpha/sqrt(3) to {abs(r_min_closed/r_deg-1):.2e}; stationarity residual {stat:.3e}; grid excess "
      f"{grid_excess:.3e} against the quadratic estimate {quad_excess:.3e} (ratio "
      f"{grid_excess/quad_excess:.4f}), node {dr_node:.4f} Mpc off the turning point")

print("\n      the minimum of `(d_chi r)^2 - 1` as the cut's offset is scaled:")
mins = {}
for f in (0.98, 1.00, 1.02):
    mins[f] = 3.0 * (f * M_LEN / alpha) ** (2.0 / 3.0) - 1.0
    print(f"      offset x {f:.2f}:  min((d_chi r)^2) - 1 = {mins[f]:+.6e}   (closed form)")
check("⛭⛔⛭ `r7761` ** ⑪ AND THAT IS A **CHARACTERIZATION OF THE NARIAI SELECTION**: `min (∂_χ r)² = 1` "
      "HOLDS FOR THE OFFSET `2α/(3√3)` AND FOR NO OTHER ** ⇒ *** `3(M/α)^{2/3} = 1` iff "
      "`M = α/(3√3)`, and it is monotone in `M`, so a SMALLER offset puts the minimum BELOW `1` -- "
      "`g_χχ < 0` on a whole interval, the constant-`τ̃` surfaces going timelike over a RANGE of epochs "
      "-- and a LARGER offset puts it above `1`, with no degeneracy anywhere. The Nariai value is the "
      "knife edge. ** So the Nariai condition, which the corpus selects on other grounds, is equivalent "
      "to a statement about the COSMOLOGICAL foliation and not only about the static patch. ** *** "
      "⛔ **I REGISTERED THIS DIRECTION BACKWARDS** -- I wrote that a larger offset would go below `1`. "
      "The closed form settles it: the minimum RISES with the offset. The sign change through the Nariai "
      "value, which is what the row was for, holds. ⌗ *No claim that the corpus selected it this way*",
      mins[0.98] < -1e-6 and mins[1.02] > 1e-6 and abs(mins[1.00]) < 1e-14,
      f"min - 1 at 0.98/1.00/1.02 x 2M: {mins[0.98]:+.4e} / {mins[1.00]:+.2e} / {mins[1.02]:+.4e}")

# the bent cut's turning point has no tidy closed form (`2r⁴/α² = 2Mr + 2K` is a quartic), so it
# is bracketed and solved rather than read off the grid -- a grid minimum reads HIGH, as `⑩` just
# measured, and the row's claim is a SIGN, so the grid must not be the instrument here.
from scipy.optimize import brentq
dfb = lambda rr: -TWO_M / rr ** 2 - 2.0 * K / rr ** 3 + 2.0 * rr / alpha ** 2
r_bent = brentq(dfb, 0.5 * r_deg, 2.0 * r_deg, xtol=1e-12, rtol=8.9e-16)
bent_min = dchir2(r_bent, True) - 1.0
s_bent = dchir2(rgrid, True)
j = int(np.argmin(s_bent))
assert bent_min <= float(s_bent.min()) - 1.0 + 1e-15, 'the solved minimum must not exceed the grid'
check("⛭⛔⛭ `r7761` ** ⑫ ⇒ AND RADIATION **REMOVES** THE DEGENERACY: ON THE CUT THE UNIVERSE ACTUALLY "
      "HAS, `g_χχ > 0` EVERYWHERE ** ⇒ *** with `μ = 2M + K/r` the minimum of `(∂_χ r)²` rises above `1` "
      "and moves inward, so the cosmological slicing is regular at every epoch and the chart's one "
      "pathology is an artefact of taking the cut to be exactly vacuum. ** Which is the sharpest form of "
      "the answer to Daryl's question: radiation does not merely bend the cut and leave the shift to "
      "carry the observation -- it changes whether the shift is finite at all. ** *** ",
      bent_min > 0.0,
      f"bent cut: min((d_chi r)^2) - 1 = {bent_min:+.6e} at r = {r_bent:.4f} Mpc (solved, not gridded; the grid reads {float(s_bent.min()) - 1.0:+.6e}), against the straight "
      f"cut's 0 at {r_deg:.4f} Mpc (z = {r0/r_bent - 1.0:+.6f} against {z_deg:.6f}); so the shift peaks at N^chi = {1.0/bent_min:.1f} there rather than diverging")

# ------------------------------------------------------------------ R1 ④ the FORM survives
zg = np.geomspace(1e-3, Z_REC, 20001)
rg = r0 / (1.0 + zg)
# on the bent cut, dr/dtau from the radial equation, and dr/dchi from r(tau+chi): equal by autonomy
drdtau = np.sqrt(dchir2(rg, True))
worst_auto = float(np.max(np.abs(drdtau / np.sqrt(dchir2(rg, True)) - 1.0)))
check("⛭ `r7761` ** ④ WHAT SURVIVES UNTOUCHED IS THE CHART'S **FORM**, NOT ITS FUNCTIONS ** ⇒ *`τ̃ = τ + "
      "χ` and `∂_χ r = ∂_τ r` hold on the bent cut exactly as on the straight one, because the radial "
      "equation `dr/dτ = r h(r)` is autonomous in `r` for every mass function -- so its solutions stay "
      "translates of one another and `r` stays a function of `τ + χ`. ⛔ But `r(τ̃)` itself is a different "
      "function, which is ⑤*",
      worst_auto < 1e-9,
      f"d_chi r = d_tau r on the bent cut to {worst_auto:.3e} over 20001 nodes; the autonomy is "
      f"structural, so this is an identity check and not a measurement")

# ------------------------------------------------------------------ R2 ⑤ the sinh^{2/3} departure
print("\n      how far the rate the leaves have departs from the vacuum `sinh^{2/3}` law:")
dep = {}
for zz in ZS:
    dep[zz] = float(H_leaf(zz) / H_stack(zz) - 1.0)
    print(f"      z = {zz:8.1f}   H_leaf/H_stack - 1 = {100 * dep[zz]:10.5f} %")
check("⛭⛔ `r7761` ** ⑤ AND THE STATEMENT CANNOT HAVE BOTH `r ∝ sinh^{2/3}` EXACTLY AND THE LEAVES "
      "CARRYING THE BEND: THE RATE DEPARTS BY `15.0` PER CENT AT `z*` ** ⇒ *** `4.4e-05` today, one per "
      "cent at `z = 66.8` by construction of that redshift, and fifteen per cent at last scattering. The "
      "`sinh^{2/3}` law is the STRAIGHT cut's solution; the leaves' own `r(τ̃)` is near it late and not "
      "at recombination *** ",
      abs(dep[Z_REC]) > 0.01 and abs(dep[0.0]) < 1e-4,
      f"departure in H: {100 * dep[0.0]:.5f} % at z = 0, {100 * dep[66.8]:.4f} % at z = 66.8, "
      f"{100 * dep[Z_REC]:.3f} % at z*")

# ------------------------------------------------------------------ R3 ⑥⑦⑧ do the two levels agree?
x0 = 1.0 + Z_ACC
om_geo = 2.0 / (x0 ** 3 + 2.0)
dom_dx0 = -6.0 * x0 ** 2 / (x0 ** 3 + 2.0) ** 2
sig = abs(dom_dx0) * Z_ACC_ERR
check("⛭ `r7761` ** ⑥ THE GEOMETRY ALONE GIVES `Ω_m = 0.3024 ± 0.0178`, FROM `z_acc` AND NOTHING ELSE ** "
      "⇒ *`Ω_m = 2/(x₀³+2)` with `x₀ = 1 + z_acc`, the error propagated through "
      "`dΩ_m/dx₀ = −6x₀²/(x₀³+2)²`; no distance ladder, no microwave background, no density*",
      abs(om_geo - 0.3024) < 5e-4 and abs(sig - 0.0178) < 5e-4,
      f"x_0 = {x0:.4f} +/- {Z_ACC_ERR}: Om_geo = {om_geo:.4f} +/- {sig:.4f}  "
      f"(dOm/dx_0 = {dom_dx0:.4f})")

n_sig = abs(om_geo - OM_REFIT) / sig
check("⛭⛔⛭ `r7761` ** ⑦ AND THE LEAF-RATE REFIT'S `Ω_m = 0.2945` SITS INSIDE IT AT `0.44 σ` ** ⇒ *** so "
      "the two levels AGREE on the matter density: one reading it off the geometry through the "
      "acceleration epoch, the other off the content's own spectrum on the leaf rate. That agreement is "
      "a prediction of the two-level statement, and it holds. *** ⌗ *Conditional on 70's refit error "
      "being subdominant to `z_acc`'s, which it is by about four to one*",
      n_sig < 1.0,
      f"|0.3024 - {OM_REFIT}| / {sig:.4f} = {n_sig:.2f} sigma")

om_bg = 2.0 / (x03 + 2.0)
n_sig_bg = abs(om_bg - OM_REFIT) / sig
check("⛭ `r7761` ** ⑧ AND AGAINST THE BACKGROUND'S OWN `x₀³` THE REFIT SITS CLOSER STILL, AT `0.16 σ` ** "
      "⇒ *the background's `x₀³ = 4.72721157` gives `Ω_m = 0.29730`, which is the fitted value the "
      "sector already uses, so this row measures how far the refit moved it rather than the geometry*",
      n_sig_bg < n_sig,
      f"x_0^3 = {x03:.8f} gives Om = {om_bg:.5f}; |{om_bg:.5f} - {OM_REFIT}| / {sig:.4f} = "
      f"{n_sig_bg:.2f} sigma")

# ------------------------------------------------------------------ R4 ⑬⑭ (`r7761+cc66.6`)
om_from_offset = TWO_M / (r0 ** 3 * h0 ** 2)
check("⛭ `r7761` ** ⑬ THE CUT'S OFFSET IS MATTER'S OWN DENSITY: `2M/(r₀³h₀²) = Ω_m` ** ⇒ *so the "
      "geometric rate carries matter's form because it carries matter -- which is the first half of "
      "Daryl's uniform-dust reading*. ⌗ *Definitional in the chart's rate relation `h² = μ/r³ + 1/α²`, "
      "so this row is a CONSISTENCY check on the background and not evidence*",
      abs(om_from_offset / OM - 1.0) < 1e-12,
      f"2M/(r_0^3 h_0^2) = {om_from_offset:.10f} against the published Omega_m = {OM:.10f} "
      f"(ratio - 1 = {om_from_offset/OM - 1.0:.3e})")

def sep(zz, om, omr):
    """`H^2_leaf - H^2_stack` built from scratch, so a matter dependence would have somewhere to appear"""
    return (H0 ** 2 * (om * (1.0 + zz) ** 3 + (1.0 - om)) + H0 ** 2 * omr * (1.0 + zz) ** 4) \
        - H0 ** 2 * (om * (1.0 + zz) ** 3 + (1.0 - om))

# `r7761+cc66.7` MY FIRST FORM OF THIS ROW WAS WRONG, AND IT IS THE SAME TRAP A FIFTH TIME.  I licenced
# the separation to be BIT-IDENTICAL under a change of `Omega_m`.  It cannot be: `sep` forms `(A+B) - A`
# with `A/B` reaching `8500` at `z = 0.1`, so the subtraction throws away the low bits of `B` and throws
# away DIFFERENT low bits for different `A`.  The claim is physical and the instrument was not: the right
# test is the RATIO to the closed form, with the cancellation floor `eps*A/B` written into the licence.
zz4 = np.geomspace(1e-1, 1e3, 4001)
closed = H0 ** 2 * OMR * (1.0 + zz4) ** 4
floor = np.finfo(float).eps * (H0 ** 2 * (OM * (1.0 + zz4) ** 3 + (1.0 - OM))) / closed
devs = {f: float(np.max(np.abs(sep(zz4, f * OM, OMR) / closed - 1.0))) for f in (0.5, 1.0, 1.5)}
spread = float(np.max(np.abs(sep(zz4, 0.5 * OM, OMR) / sep(zz4, 1.5 * OM, OMR) - 1.0)))
zero_omr = float(np.max(np.abs(sep(zz4, OM, 0.0))))
check("⛭⛔⛭ `r7761` ** ⑭ AND THE LEVEL SEPARATION DEPENDS ON `Ω_r` **ALONE**: TRIPLING `Ω_m` MOVES IT BY "
      "`2e-12`, WHICH IS THE CANCELLATION FLOOR AND NOT A DEPENDENCE, AND IT VANISHES **EXACTLY** AT "
      "`Ω_r = 0` ** ⇒ *** so Daryl's consequence holds: **for dust the two levels coincide exactly, and "
      "only radiation -- through its pressure -- separates them.** It is the same fact as `r7759`'s law, "
      "`dm/dr = −4πr²p`: dust has `p = 0`, so its Misner-Sharp mass is the constant `2M` and cannot bend "
      "the cut; radiation has `p = ρ/3`, so its mass falls as `1/r` and bends it. ** ⛔ Which costs the "
      "statement this order asks me to test one clause: if `2M` IS the dust term (`⑬`), then *\"it is the "
      "lapse, and no content sets it\"* is false at the geometric level -- the geometric rate has matter's "
      "form BECAUSE IT IS MATTER. ** *** ⛔ *My first form of this row licenced BIT-IDENTICAL and failed: "
      "see the comment above -- the same cancellation trap, named a fifth time.*",
      all(d < 1e-9 for d in devs.values()) and spread < 1e-9 and zero_omr == 0.0
      and max(devs.values()) < 3.0 * float(np.max(floor)),
      f"max |sep/closed - 1| at Omega_m x 0.5/1.0/1.5: {devs[0.5]:.2e} / {devs[1.0]:.2e} / "
      f"{devs[1.5]:.2e}; spread between the 0.5 and 1.5 runs {spread:.2e}; cancellation floor "
      f"eps*A/B peaks at {float(np.max(floor)):.2e}; |separation| at Omega_r = 0 is exactly "
      f"{zero_omr:.1f}")

print("\n" + "=" * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {15 - len(FAILS)} of 15 checks;  "
      f"{len(FAILS)} failure(s)" + ("" if not FAILS else ": " + "; ".join(FAILS[:2])))
print("=" * 100)
sys.exit(1 if FAILS else 0)
