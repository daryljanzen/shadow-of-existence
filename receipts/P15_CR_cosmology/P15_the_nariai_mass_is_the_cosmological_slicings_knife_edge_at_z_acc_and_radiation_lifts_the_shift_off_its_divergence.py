#!/usr/bin/env python3
"""`r7763` ** `-f` IS `g_chi chi` OF THE COSMOLOGICAL FOLIATION, SO `P15`'s PUBLISHED DOUBLE ROOT AT
`alpha/sqrt3` IS THE EPOCH AT WHICH THE CONSTANT-`tilde tau` SLICING DEGENERATES AND THE **SHIFT**
DIVERGES. THE NARIAI MASS IS THE KNIFE EDGE THAT PUTS IT THERE, `min (d_chi r)^2 = 3(M/alpha)^{2/3}`
BEING EXACTLY `1` AT THAT MASS AND MONOTONE IN IT; THE RADIUS IS `r_0/x_0`, SO THE LOCUS IS `z_acc`; AND
RADIATION LIFTS THE ROOT, SO ON THE CUT THE UNIVERSE HAS THE SHIFT PEAKS FINITE. **

⛔ ** WHAT IS CONFIRMATION OF PUBLISHED ALGEBRA AND WHAT IS NEW, SAID FIRST SO NO ROW BELOW CAN BE READ AS
MORE THAN IT IS. **  At `r7761` this seat reported to `69` that the corpus had not recorded the
cosmological slicing's degeneracy at this radius.  ** THAT WAS WRONG. **  `P15` `sec:scope`
`eq:chi-block-factored` prints

      `-f = (r - alpha/sqrt3)^2 (r + 2 alpha/sqrt3) / (alpha^2 r)`

and says under it: *"a double root at `r = +alpha/sqrt3` and a simple one at `r = -2alpha/sqrt3` --- which
are the lap's two seams, necessarily so, since `-f = 0` and `|d_chi r| = 1` are the same condition"*.
With `f = 1 - 2M/r - r^2/alpha^2`, `-f = 2M/r + r^2/alpha^2 - 1`, which IS `(d_chi r)^2 - 1`.  So the
corpus already carries, as exact algebra rather than as a numerical minimum, that the degeneracy sits at
`alpha/sqrt3`, that it is a DOUBLE root -- `r7761`'s `(10)`, "a minimum touching `1` and not a crossing"
-- and that `g_chi chi >= 0` away from it.  ** `(2)` and `(3)` below are therefore CONFIRMATIONS, and they
are run against the paper's own parsed expression rather than against a retyped one. **

** WHAT IS NEW IS FOUR THINGS, and they are `(4)`-`(8)`: **
 * ** the ADM identification. **  That `-f` is `g_chi chi` of the COSMOLOGICAL (constant-`tilde tau`)
   foliation, so what diverges at the double root is the ** shift ** `N^chi = 1/(-f)`.  `P15` reads the
   locus as a causal-character statement -- *"spacelike on both legs and Lorentzian through the whole
   interior of the lap"* -- and not as the shift's divergence.
 * ** the knife edge as a formula. **  `min (d_chi r)^2 = 3(M/alpha)^{2/3}`, stationary at
   `r = (M alpha^2)^{1/3}`, equal to `1` exactly when `M = alpha/(3 sqrt 3)` and monotone in `M`: a
   smaller offset puts the minimum below `1`, so `g_chi chi < 0` over a RANGE of epochs, and a larger one
   puts it above, with no degeneracy anywhere.
 * ** the locus is `z_acc`. **  The degenerate radius is `r_0/x_0` exactly, and that identity rearranges
   to `Omega_m = 2/(x_0^3 + 2)` -- the acceleration-epoch identity `P15` prints at `eq:zacc`.
 * ** radiation lifts it. **  With `mu = 2M + K/r` the minimum rises above `1`, so `g_chi chi > 0` at every
   epoch and the shift peaks finite instead of diverging.

⛔ ** WHAT THIS RECEIPT DOES NOT CLAIM. **
 * ** Not that `P15` derived the knife-edge characterization. **  `(4)` and `(5)` state it as a formula.
   Whether the corpus SELECTED the Nariai mass by this route is a ruling and is not asserted here.
 * ** Not that the degeneracy is physical. **  It is this chart's coordinate failure on the constant-
   `tilde tau` slicing; no claim is made that anything observable happens at `z_acc` on its account.
 * ** Not that the shift's divergence invalidates the published distance. **  `P15`'s own non-synchrony
   factor is finite there and the paper's `8787` against `14011` Mpc is untouched by anything here.
 * ** No likelihood, no significance, nothing fitted. **  Every number is algebra on two published rate
   laws over a published background, or a quantity parsed out of the paper's own text.

⛭ ** FAILABILITY, MEASURED AND NOT ASSERTED -- AND THE REGISTRATION NAMED TWO GATES WRONG. **
 * ** `2M` scaled by `1.01` reddens FOUR of the nine: `(2)`, `(4)`, `(5)`, `(7)` ** -- the geometric
   spine, including the pin on the paper's own sentence.
 * ⛔ ** `(3)` and `(6)` do NOT move, and my registration said they would. **  They cannot: `(3)` reads
   ONLY the expression parsed out of the paper, which carries no `2M`, and `(6)` depends on `alpha`, `r_0`
   and `x_0` alone.  Reported as an error in the registration's failability note rather than presented as
   a shortfall in the gates.
 * ** `Omega_r` scaled by `1.01` reddens `(1)` only, and that is by design: ** `(8)`'s claim is a SIGN,
   so a one-per-cent lift makes it more true, not less.  Probed the way it actually fails -- `K -> -K` --
   it reddens `(8)` and nothing else.

COMPUTES: scope.
 * ** THIS RECEIPT READS COSMOLOGICAL PARAMETERS AND FITS NONE. **  `H_0 = 68.6`, `Omega_m = 0.2973`,
   `Omega_r h^2 = 4.15e-5`, `z* = 1089.9`, `alpha`, `r_0` and the Nariai offset `2M` are the sector's
   published background, read by path out of 60's `r7580/lightpath.py` (`r7445`'s rule) rather than typed
   in as literals of this receipt's own.  `z_acc = 0.6648 +/- 0.0467` is `P15` `eq:zacc` as printed.
 * ** THE REGISTRATION THAT GOVERNS EVERY ROW IS `r7763+cc66.0`'s `PREDICTION.md` **, pushed before this
   file existed; it opens with the correction above, names which rows are confirmations, and sets each
   licence -- including that the GRID minimum is not the instrument for `(4)`, because at `r7761` that
   licence was missed by exactly the `(1/2) f'' dr^2` a grid node costs.
 * ** COST: under a second. **  No quadrature, no solver but one `brentq`.  NOT long.
"""
import contextlib
import io
import os
import re
import runpy
import subprocess
import sys

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
LP = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7580_60_whether_the_observers_readout_identification_forces_the_stacking_rate_distance',
                  'lightpath.py')
SL = os.path.join(ROOT, 'computations', 'beyond_the_wall',
                  'r7761_cc66_the_shift_and_the_two_levels', 'shift_and_levels.py')
TEX = os.path.join(ROOT, 'corpus', 'CR_cosmology.tex')
for pth, who in ((LP, "60's lightpath.py"), (SL, "r7761's shift_and_levels.py"),
                 (TEX, "P15's CR_cosmology.tex")):
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
Z_REC, alpha, r0, TWO_M, x03 = NS['Z_REC'], NS['alpha'], NS['r0'], NS['TWO_M'], NS['x03']
h0 = H0 / C
K = h0 ** 2 * OMR * r0 ** 4
M_LEN = TWO_M / 2.0
R3 = np.sqrt(3.0)
Z_ACC, Z_ACC_ERR = 0.6648, 0.0467   # INPUT  x0 = 1.6648 +- 0.0467, corpus measured; P15 eq:zacc,
#   as printed, which itself carries the interval as an input "from DESI DR2 D_M/D_H".  NOTHING HERE
#   COMPUTES THE FIT -- `(6)` propagates the printed interval through an identity and no row rests on
#   its width.  ⌗ `r7765+cc66.1`: the declaration is what `L_probability/S1` `(iii)2` requires of every
#   file carrying `0.0467`, and this receipt was the one carrier without it.
TEXT = open(TEX, encoding='utf-8', errors='replace').read()
FAILS = []


def check(label, ok, witness=''):
    if not ok:
        FAILS.append(label.split('**')[0].strip()[:60])
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if witness:
        print(f"             {witness}")


def dchir2(rr, bent=False):
    """`(d_chi r)^2 = mu(r)/r + r^2/alpha^2`, with `mu = 2M` straight and `2M + K/r` bent"""
    mu = TWO_M + (K / rr if bent else 0.0)
    return mu / rr + rr ** 2 / alpha ** 2


print("=" * 100)
print(__doc__)
print("=" * 100)

check("⛭ `r7763` ** ① THE BACKGROUND IS 60's, READ BY PATH AND NOT REIMPLEMENTED ** ⇒ *`r7445`'s rule; "
      "the published values are asserted as what that script carries, so a change to them reddens this "
      "receipt instead of silently repricing the reading*",
      abs(H0 - 68.6) < 5e-9 and abs(OM - 0.2973) < 5e-9 and abs(OMR - 8.8186e-05) < 5e-10
      and abs(Z_REC - 1089.9) < 5e-9,
      f"H0 {H0}  Om {OM}  Om_r {OMR:.4e}  z* {Z_REC}  alpha {alpha:.4f}  r_0 {r0:.4f}  "
      f"2M {TWO_M:.4f} Mpc  x_0^3 {x03:.8f}")

# ------------------------------------------------------------------ ② the paper's own -f IS g_chi chi
# `r7763+cc66.5` SPAN SHORTENED to the minimum that carries the claim, per the grain clause
# (`r7253` ruling 2): `\begin{equation}` was surplus -- the `-f=` form plus the LABEL is what the
# claim needs, and the label is load-bearing because the receipt cites this equation by name.
_EQ = re.search(r'-f=\\frac\{\(r-\\alpha/\\sqrt3\)\^(\d)\\,'
                r'\(r\+(\d)\\alpha/\\sqrt3\)\}\{\\alpha\^(\d) r\}\s*,\s*'
                r'\\label\{eq:chi-block-factored\}', TEXT)
if _EQ:
    POW, COEF, APOW = int(_EQ.group(1)), int(_EQ.group(2)), int(_EQ.group(3))
else:
    POW = COEF = APOW = -1


def minus_f_paper(rr):
    """`P15`'s `eq:chi-block-factored` RHS, built from the exponents and coefficient PARSED out of it"""
    return (rr - alpha / R3) ** POW * (rr + COEF * alpha / R3) / (alpha ** APOW * rr)


rgrid = np.geomspace(r0 / (1.0 + Z_REC), 40.0 * r0, 400001)
g_chi = dchir2(rgrid) - 1.0
paper = minus_f_paper(rgrid)
# `r7763+cc66.1` BOTH SIDES VANISH AT THE DOUBLE ROOT, so a RELATIVE comparison divides by a near-zero
# and reports the arithmetic's floor rather than the algebra.  My own side is `2M/r + r^2/alpha^2 - 1`, a
# difference of `O(1)` terms whose value is `O((r - alpha/sqrt3)^2)`, so it carries an absolute error of
# order `eps` there.  The licence is therefore an ABSOLUTE bound in units of `eps` times the largest
# term.  ⌗ The relative form was my registered licence and it missed at `8.4e-06`; see `PREDICTION.md`.
terms = TWO_M / rgrid + rgrid ** 2 / alpha ** 2 + 1.0
EPS = float(np.finfo(float).eps)
res = np.abs(paper - g_chi)
floor_ratio = float(np.max(res / (EPS * terms)))
check("⛭⛔⛭ `r7763` ** ② `P15`'s OWN `eq:chi-block-factored` IS `g_χχ = (∂_χ r)² − 1`, TO `4` TIMES THE "
      "ROUND-OFF FLOOR OVER FOUR DECADES IN `r` ** ⇒ *** so the paper's `−f` **is** the metric component "
      "of the cosmological foliation, and its published double root is that foliation's degeneracy. "
      "Expanding the paper's numerator gives `r³ − 3a²r + 2a³` over `α²r` with `a = α/√3`, which is "
      "`r²/α² − 1 + 2M/r` term by term, and `2M` is bit-identical to `2α/(3√3)`. The equation's "
      "exponents and its coefficient are **parsed out of `CR_cosmology.tex` and used**, not retyped: a "
      "change to the printed equation either fails the parse or moves this number. *** ⌗ *A "
      "CONFIRMATION of published algebra, not a discovery — see the docstring. And the licence is "
      "absolute, in units of `ε` times the largest term, because both sides vanish at the root*",
      POW == 2 and COEF == 2 and APOW == 2 and floor_ratio < 10.0,
      f"parsed from the paper: exponent {POW}, coefficient {COEF}, alpha power {APOW}; max absolute "
      f"residual {float(res.max()):.3e} over {rgrid.size} nodes spanning {rgrid[0]:.2f}-{rgrid[-1]:.0f} "
      f"Mpc, which is {floor_ratio:.2f} x eps x (2M/r + r^2/alpha^2 + 1); 2M - 2alpha/(3sqrt3) = "
      f"{TWO_M - 2.0 * alpha / (3.0 * R3):.3e}")

# ------------------------------------------------------------------ ③ the double root, from that expression
r_deg = alpha / R3
i0 = int(np.argmin(np.abs(paper)))
left = float(np.min(paper[rgrid < 0.95 * r_deg]))
right = float(np.min(paper[rgrid > 1.05 * r_deg]))
check("⛭ `r7763` ** ③ AND THAT EXPRESSION IS `≥ 0` ON `r > 0` WITH ITS ONLY ZERO AT `α/√3` — THE "
      "PUBLISHED DOUBLE ROOT ** ⇒ *the squared factor cannot change sign and `(r + 2α/√3)/(α²r) > 0` for "
      "`r > 0`, so the slicing touches degeneracy once and is spacelike on both sides, which is the "
      "paper's own reading of the same factorization*",
      float(np.min(paper)) > -1e-12 and abs(rgrid[i0] / r_deg - 1.0) < 1e-5
      and left > 1e-6 and right > 1e-6,
      f"min over the grid {float(np.min(paper)):+.3e}; nearest zero at r = {rgrid[i0]:.4f} Mpc against "
      f"alpha/sqrt3 = {r_deg:.4f}; strictly positive either side ({left:.3e} left, {right:.3e} right)")

# ------------------------------------------------------------------ ④ the closed form, and the grid is not the instrument
r_min_closed = (M_LEN * alpha ** 2) ** (1.0 / 3.0)
stat = -TWO_M / r_min_closed ** 2 + 2.0 * r_min_closed / alpha ** 2
s_min_closed = 3.0 * (M_LEN / alpha) ** (2.0 / 3.0)
f2 = 2.0 * TWO_M / r_min_closed ** 3 + 2.0 / alpha ** 2
i_min = int(np.argmin(dchir2(rgrid)))
quad_excess = 0.5 * f2 * (rgrid[i_min] - r_min_closed) ** 2
grid_excess = float(np.min(dchir2(rgrid))) - 1.0
check("⛭⛔ `r7763` ** ④ `min (∂_χ r)² = 3(M/α)^{2/3}`, STATIONARY AT `r = (Mα²)^{1/3} = α/√3`, AND "
      "EXACTLY `1` AT THE NARIAI MASS ** ⇒ *** `d(∂_χ r)²/dr = −2M/r² + 2r/α²` vanishes at `(Mα²)^{1/3}`, "
      "and the value there collapses to `3(M/α)^{2/3}`, which is `1` iff `M = α/(3√3)`. *** ⌗ **The grid "
      "minimum is NOT the instrument here.** At `r7761` I licenced it to `1e-12` and it read `5.25e-12` "
      "high — the nearest node sits off the turning point and the function is quadratic there, so a grid "
      "reads high by `½f″dr²`. The closed form is asserted and the grid excess is bounded by that "
      "estimate instead.",
      abs(stat) < 1e-15 and abs(r_min_closed / r_deg - 1.0) < 1e-12
      and abs(s_min_closed - 1.0) < 1e-14 and grid_excess >= 0.0
      and abs(grid_excess / quad_excess - 1.0) < 0.1,
      f"3(M/alpha)^(2/3) - 1 = {s_min_closed - 1.0:+.3e}; (M alpha^2)^(1/3) = {r_min_closed:.6f} Mpc "
      f"= alpha/sqrt3 to {abs(r_min_closed / r_deg - 1.0):.2e}; stationarity residual {stat:.3e}; grid "
      f"excess {grid_excess:.3e} against the quadratic estimate {quad_excess:.3e} "
      f"(ratio {grid_excess / quad_excess:.4f})")

# ------------------------------------------------------------------ ⑤ the knife edge
mins = {f: 3.0 * (f * M_LEN / alpha) ** (2.0 / 3.0) - 1.0 for f in (0.98, 1.00, 1.02)}
print("\n      the minimum of `(d_chi r)^2 - 1` as the cut's offset is scaled (closed form):")
for f in (0.98, 1.00, 1.02):
    print(f"      offset x {f:.2f}:  {mins[f]:+.6e}")
check("⛭⛔⛭ `r7763` ** ⑤ SO THE NARIAI MASS IS THE **KNIFE EDGE**: IT IS THE ONE OFFSET WHOSE "
      "COSMOLOGICAL SLICING DEGENERATES AT A SINGLE RADIUS ** ⇒ *** `3(M/α)^{2/3}` is monotone in `M`, so "
      "a SMALLER offset puts the minimum below `1` — `g_χχ < 0` on a whole interval, the constant-`τ̃` "
      "surfaces going timelike over a RANGE of epochs — and a LARGER offset puts it above `1`, with no "
      "degeneracy anywhere. ** The Nariai condition is therefore equivalent to a statement about the "
      "COSMOLOGICAL foliation, and not only about the static patch. ** *** ⌗ *Whether the corpus selected "
      "it by this route is 69's to rule and is not asserted*",
      mins[0.98] < -1e-6 and mins[1.02] > 1e-6 and abs(mins[1.00]) < 1e-14,
      f"min - 1 at 0.98/1.00/1.02 x 2M: {mins[0.98]:+.4e} / {mins[1.00]:+.2e} / {mins[1.02]:+.4e}")

# ------------------------------------------------------------------ ⑥ the locus is z_acc
x0_bg = x03 ** (1.0 / 3.0)
ratio = (r0 / r_deg) / x0_bg
z_deg = r0 / r_deg - 1.0
om_from_identity = 2.0 / ((r0 * R3 / alpha) ** 3 + 2.0)
n_sig = abs(z_deg - Z_ACC) / Z_ACC_ERR
check("⛭⛔⛭ `r7763` ** ⑥ AND THE DEGENERATE RADIUS IS `r₀/x₀` EXACTLY, SO THE LOCUS IS THE ACCELERATION "
      "EPOCH — AND THAT IDENTITY **IS** `Ω_m = 2/(x₀³+2)` ** ⇒ *** with `r₀ = x₀α/√3`, "
      "`r₀³ = x₀³α³/(3√3)`, so `Ω_m/Ω_Λ = 2Mα²/r₀³ = 2/x₀³`, which rearranges to `Ω_m = 2/(x₀³+2)` — the "
      "identity `P15` prints at `eq:zacc`. Recovering `Ω_m` from the degenerate radius ALONE returns the "
      "published value. ** So the epoch at which this chart's constant-`τ̃` slicing degenerates is the "
      "acceleration epoch, and the measured `z_acc` agrees with it. ** *** ",
      abs(ratio - 1.0) < 1e-12 and abs(om_from_identity / OM - 1.0) < 1e-12 and n_sig < 1.0,
      f"(r_0/r_deg)/x_0 - 1 = {ratio - 1.0:.3e}; Om recovered from r_0 sqrt3/alpha alone = "
      f"{om_from_identity:.10f} against the published {OM:.10f}; z_deg = {z_deg:.6f} against the measured "
      f"z_acc = {Z_ACC} +/- {Z_ACC_ERR}, i.e. {n_sig:.2f} sigma")

# ------------------------------------------------------------------ ⑦ the pin on sec:scope's own prose
# `r7763+cc66.5` SPAN SHORTENED likewise: `non-synchrony factor ` is surplus -- the FACTOR's own
# form is what identifies which quantity bottoms, and that is what this gate evaluates.
_NS = re.search(r'\$\\partial_\\chi r/\(1\+\\partial_\\chi r\)\$ epoch by epoch, '
                r'which bottoms at exactly \$\\tfrac(\d)(\d)\$ at the merged Nariai radius', TEXT)
HALF = (int(_NS.group(1)) / int(_NS.group(2))) if _NS else -1.0
dchir = np.sqrt(dchir2(rgrid))
nonsync = dchir / (1.0 + dchir)
at_deg = float(np.sqrt(dchir2(r_deg)) / (1.0 + np.sqrt(dchir2(r_deg))))
j = int(np.argmin(nonsync))
check("⛭⛔⛭ `r7763` ** ⑦ THE PIN ON `sec:scope`'s OWN SENTENCE: THE NON-SYNCHRONY FACTOR `∂_χ r/(1+∂_χ r)` "
      "*\"BOTTOMS AT EXACTLY `½` AT THE MERGED NARIAI RADIUS\"* — AND IT DOES SO **BECAUSE** `∂_χ r` "
      "BOTTOMS AT `1` THERE ** ⇒ *** the `½` is parsed out of the paper's sentence and COMPARED against "
      "the factor evaluated at `α/√3`; and the factor's own minimum over four decades is LOCATED at "
      "`α/√3`, which is `④`'s minimum seen through a monotone function. ** So the paper's published `½` "
      "and this receipt's knife edge are one fact. ** *** ⌗ *A comparison, not a regex that finds the "
      "digits*",
      HALF == 0.5 and abs(at_deg - HALF) < 1e-15 and abs(rgrid[j] / r_deg - 1.0) < 1e-5,
      f"parsed from the paper: {HALF}; the factor at alpha/sqrt3 = {at_deg:.17f}; its grid minimum "
      f"{float(nonsync.min()):.17f} at r = {rgrid[j]:.4f} Mpc against alpha/sqrt3 = {r_deg:.4f}")

# ------------------------------------------------------------------ ⑧ radiation lifts the root
dfb = lambda rr: -TWO_M / rr ** 2 - 2.0 * K / rr ** 3 + 2.0 * rr / alpha ** 2
r_bent = brentq(dfb, 0.5 * r_deg, 2.0 * r_deg, xtol=1e-12, rtol=8.9e-16)
bent_min = dchir2(r_bent, True) - 1.0
check("⛭⛔⛭ `r7763` ** ⑧ AND RADIATION **LIFTS** THE DOUBLE ROOT: ON THE CUT THE UNIVERSE HAS, `g_χχ > 0` "
      "AT EVERY EPOCH AND THE SHIFT PEAKS AT `N^χ = 3014` INSTEAD OF DIVERGING ** ⇒ *** `μ = 2M + K/r` "
      "adds a positive `K/r²` to `(∂_χ r)²`, so the minimum rises to `+3.3e-04` and moves inward. ** The "
      "chart's one pathology is an artefact of taking the cut to be exactly vacuum. ** *** ⌗ *The "
      "turning point is SOLVED by `brentq` on the derivative, not read off the grid: a grid minimum reads "
      "high, as `④` measured, and this row's claim is a SIGN*",
      bent_min > 0.0 and r_bent > r_deg,
      f"bent cut: min((d_chi r)^2) - 1 = {bent_min:+.6e} at r = {r_bent:.4f} Mpc (solved), against the "
      f"straight cut's exact 0 at {r_deg:.4f}; z = {r0 / r_bent - 1.0:.6f} against {z_deg:.6f}; "
      f"peak N^chi = {1.0 / bent_min:.1f}")

# ------------------------------------------------------------------ ⑨ the registered computation reproduces
pr = subprocess.run([sys.executable, SL], capture_output=True, text=True)
check("⛭ `r7763` ** ⑨ AND `r7761`'s REGISTERED COMPUTATION REPRODUCES, RUN BY PATH ** ⇒ *its `15` rows "
      "carry the ADM reconstruction, the shift's amplifier, the two levels' `Ω_m` at `0.44 σ` and Daryl's "
      "uniform-dust test; this receipt does not restate them and asserts the run instead*",
      pr.returncode == 0 and '15 of 15 checks' in pr.stdout,
      f"shift_and_levels.py exits {pr.returncode} with its own verdict line: "
      f"{[l.strip() for l in pr.stdout.splitlines() if 'of 15 checks' in l][:1]}")

print("\n" + "=" * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {9 - len(FAILS)} of 9 gates;  "
      f"{len(FAILS)} failure(s)" + ("" if not FAILS else ": " + "; ".join(FAILS[:2])))
print("=" * 100)
sys.exit(1 if FAILS else 0)
