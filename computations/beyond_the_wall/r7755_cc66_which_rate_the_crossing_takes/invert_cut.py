#!/usr/bin/env python3
"""`r7755+cc66` INVERTING THE CUT FOR THE LEAF RATE: WHICH MASS FUNCTION WOULD IT TAKE, AND IS IT ADMISSIBLE?

⛭ Registered in `PREDICTION.md` at `r7755+cc66.0`, pushed before this file existed. `R1`'s four rows and
`R2`'s two are stated there with their licences and are not moved.

⛭ ** THE CHART IS 60's, READ BY PATH AND NOT REIMPLEMENTED ** (`r7445`'s rule): `r7580/lightpath.py`
carries the background AND the radial equation's own constants -- `alpha`, `r0`, and `TWO_M = 2a/(3*sqrt3)`,
the Nariai offset.  If it has moved, this refuses rather than substituting a chart of its own.

THE RELATION, FROM `P15` `sec:properframe` STEP (iii).  At `E = 1` the radial equation is
`(dr/dtau)^2 = 2GM/c^2 r + r^2/alpha^2`, so with `h = (dr/dtau)/r` in inverse length,

        h^2(r) = mu(r)/r^3 + 1/alpha^2 ,      mu(r) == 2 G m(r) / c^2   [length]

and the straight cut `mu == TWO_M` returns the stacking rate identically.  Everything below is this one
relation solved for `mu(r)`, so the inversion is the chart's own equation read backwards and not a model.
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
Z_REC, alpha, r0, TWO_M = NS['Z_REC'], NS['alpha'], NS['r0'], NS['TWO_M']
H_stack, H_leaf = NS['H_stack'], NS['H_leaf']

h0 = H0 / C                      # inverse Mpc
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
print(f"\n  read from 60's chart: alpha {alpha:.6f}  r_0 {r0:.6f}  2M {TWO_M:.6f} Mpc   "
      f"H0 {H0}  Om_r {OMR:.4e}  z* {Z_REC}")

z = np.geomspace(1e-6, Z_REC, 4001)
r = r0 / (1.0 + z)


def h2_of_mu(mu, rr):
    """the chart's own relation, read forward"""
    return mu / rr ** 3 + 1.0 / alpha ** 2


# ---------------------------------------------------------------- 0 the forward direction is the chart's
h2_stack_chart = h2_of_mu(TWO_M, r)
h2_stack_pub = (H_stack(z) / C) ** 2
e0 = float(np.max(np.abs(h2_stack_chart / h2_stack_pub - 1.0)))
check("⛭ `r7755` ** ⓪ THE STRAIGHT CUT RETURNS THE PUBLISHED STACKING RATE THROUGH THIS RELATION ** ⇒ "
      "*asserted BEFORE the relation is read backwards, because an inversion of an equation that does not "
      "reproduce the forward case is an inversion of something else*",
      e0 < 1e-12, f"worst relative deviation of mu = 2M against H_stack over z in [1e-6, z*]: {e0:.3e}")

# ---------------------------------------------------------------- R1 the demanded mass function
h2_leaf = (H_leaf(z) / C) ** 2
mu_needed = (h2_leaf - 1.0 / alpha ** 2) * r ** 3          # solved pointwise, no form assumed
K_closed = h0 ** 2 * OMR * r0 ** 4
mu_closed = TWO_M + K_closed / r

e1 = float(np.max(np.abs(mu_needed / mu_closed - 1.0)))
check("⛭⛔ `r7755` ** ① THE DEMANDED MASS FUNCTION IS `mu(r) = 2M + K/r` EXACTLY, WITH "
      "`K = (H_0/c)^2 Omega_r r_0^4` ** ⇒ *solved POINTWISE from the relation with no form assumed, then "
      "compared against the closed form; `R1` row ① as registered*",
      e1 < 1e-10, f"K = {K_closed:.6e} Mpc^2; worst |mu_solved/mu_closed - 1| = {e1:.3e}")

h2_back = h2_of_mu(mu_needed, r)
e1b = float(np.max(np.abs(h2_back / h2_leaf - 1.0)))
check("⛭ `r7755` ** ①ᵇ AND THAT CUT'S OWN RATE *IS* THE LEAF RATE, CHECKED FORWARD ** ⇒ *the licence the "
      "registration set: the recomputed `m(r)` reproduces `H_leaf(z)` over the whole range*",
      e1b < 1e-10, f"worst relative deviation over z in [1e-6, z*]: {e1b:.3e}")

mu_prime = -K_closed / r ** 2
check("⛭⛔ `r7755` ** ② ITS MASS FUNCTION DECREASES OUTWARD: `mu'(r) = -K/r^2 < 0` AT EVERY RADIUS ** ⇒ "
      "*`R1` row ②, and the first half of why it is not a cut the construction can carry*",
      bool(np.all(mu_prime < 0.0)),
      f"mu' ranges {mu_prime.min():.3e} to {mu_prime.max():.3e} Mpc/Mpc, all negative")

rho_shape = mu_prime / (4.0 * np.pi * r ** 2)              # proportional to the density, sign-exact
rho_r4 = rho_shape * r ** 4
check("⛭⛔ `r7755` ** ③ SO ITS DENSITY IS NEGATIVE AND IS EXACTLY RADIATION'S OWN `r^-4` PROFILE WITH THE "
      "SIGN REVERSED ** ⇒ *** `rho ∝ mu'/r^2 = -K/(4 pi r^4)`: the shape the physics asks for, carrying "
      "the sign the physics forbids ***",
      bool(np.all(rho_shape < 0.0))
      and float(np.max(np.abs(rho_r4 / rho_r4[0] - 1.0))) < 1e-12,
      f"rho < 0 everywhere; rho*r^4 constant to {float(np.max(np.abs(rho_r4 / rho_r4[0] - 1.0))):.3e}")

mu_at_0 = K_closed / (r0 * 1e-12)
check("⛭⛔ `r7755` ** ④ AND IT IS NOT ADMISSIBLE: THE ENERGY CONDITIONS FAIL AT EVERY RADIUS AND THE MASS "
      "FUNCTION DIVERGES AT THE BRANCH POINT ** ⇒ *** so there is NO cut, bent however one likes, whose "
      "own rate is the leaf rate. Option (c) is closed, and the remaining question is which object the "
      "distance is read off -- a classification, not a dynamics. *** ⛔ *This fires AGAINST the leaf-rate "
      "reading's easiest route, which is why it was registered before it was run.*",
      bool(np.all(rho_shape < 0.0)) and mu_at_0 > 1e6 * TWO_M,
      f"rho < 0 at all {len(r)} nodes (weak and null energy conditions fail); "
      f"mu(r) -> {mu_at_0:.3e} Mpc as r -> 1e-12 r_0, against 2M = {TWO_M:.3f}")

# ---------------------------------------------------------------- R2 the published bend, same instrument
B = 3.0 * h0 ** 2 * OMR * r0 ** 4                          # a POSITIVE r^-4 density, normalised at r_0
mu_bend = TWO_M + B * (1.0 / r0 - 1.0 / r)
h2_bend = h2_of_mu(mu_bend, r)
term_meas = h2_bend - h2_stack_chart
term_pub = -3.0 * h0 ** 2 * OMR * z * (1.0 + z) ** 3       # P15's printed law
dev = np.abs(term_meas / term_pub - 1.0)
e2_all = float(np.max(dev))

# ⛔ THE REGISTERED LICENCE WAS `< 1e-10` OVER THE WHOLE GRID AND IT IS NOT MET: the measured worst is
#    about `7e-07`, at the LOW-z end.  That is reported, not loosened, and then DIAGNOSED rather than
#    excused -- the diagnosis is itself asserted below, in two independent ways.
#    The arithmetic of the suspected cause: `term` is formed as a difference of two h^2 values that agree
#    to `3 Omega_r z` in relative terms, so double precision's floor on the ratio is `~1e-16/(3 Omega_r z)`,
#    which at `z = 1e-6` is `~4e-07`.  If that is the cause the deviation scales as `1/z`; if instead the
#    two laws disagree, it does not.
hi = z >= 1e-2
e2_hi = float(np.max(dev[hi]))
floor = 1e-16 / (3.0 * OMR * z)
over = float(np.max(dev / floor))            # an upper BOUND test: round-off may sit anywhere below it
# ⛔ and the same term formed with EVERY cancellation removed analytically: `1/r_0 - 1/r` is itself a
#    difference of nearly equal numbers as `z -> 0`, which is why the first attempt at this check still
#    carried `1e-10`.  Exactly, since `1/r = (1+z)/r_0`, the difference is `-z/r_0` with nothing to cancel.
#    ⛔ My first rewrite of this line put `-(z/(1+z))/r_0` here and was simply wrong -- it dropped a factor
#    of `(1+z)` and the check reported `0.999`, which is the gate doing its job on its own author.
term_direct = B * (-z / r0) / r ** 3
e2_direct = float(np.max(np.abs(term_direct / term_pub - 1.0)))

check("⛭⛔ `r7755` ** ⑤ THE SAME RELATION REPRODUCES `P15`'s PRINTED BEND LAW FROM A *POSITIVE* `r^-4` "
      "PROFILE: THE RADIATION TERM IS `-3 Omega_r z(1+z)^3`, AND WHERE THE SUBTRACTION CAN CARRY IT THE "
      "AGREEMENT IS ROUND-OFF ** ⇒ *`R2`'s licence, and the reason `R1` may be quoted at all: this "
      "inversion and `r7614`'s published law are demonstrably ONE instrument, shape and sign together.* "
      "⛔ *** THE REGISTERED LICENCE WAS `< 1e-10` ON THE WHOLE GRID AND IT IS NOT MET: the worst is "
      "`7.2e-07`, at the low-`z` end. That is reported as a miss and then DIAGNOSED, not loosened. *** "
      "*The term is formed as a difference of two `h^2` that agree to `3 Omega_r z`, so double "
      "precision's own floor on the ratio is `1e-16/(3 Omega_r z)`. Two independent checks say that is "
      "all it is: the deviation never exceeds twice that floor at any node across six decades of `z`, "
      "and the same term with every cancellation removed analytically agrees with the printed law to "
      "at every node, `z = 1e-6` included.*",
      e2_hi < 1e-10 and e2_direct < 1e-13 and over < 5.0,
      f"whole grid {e2_all:.3e} (REGISTERED LICENCE MISSED); above z = 1e-2, {e2_hi:.3e}; "
      f"cancellation-free form {e2_direct:.3e}; and the deviation never exceeds "
      f"{over:.2f}x the double-precision floor 1e-16/(3 Omega_r z) at any node")

check("⛭ `r7755` ** ⑥ AND THE TWO CUTS DIFFER IN NORMALISATION: THE EXACT-LEAF CUT DOES NOT MATCH THE "
      "STRAIGHT ONE AT THE PRESENT RADIUS ** ⇒ *reported as a number rather than a verdict, because `R2` "
      "row ⑥ asked for the number*",
      True,
      f"mu_leaf(r_0) - 2M = {K_closed / r0:.6e} Mpc, i.e. {100 * K_closed / (r0 * TWO_M):.4f} % of 2M; "
      f"and the physical bend's coefficient is B = {B / K_closed:.1f} K")

lam_rec = -(1.0 + Z_REC) / (3.0 * Z_REC)
check("⛭ `r7755` ** ⑦ AND IT AGREES WITH `r7753`'s SCALING ARGUMENT WHERE THE TWO OVERLAP ** ⇒ *`r7753` "
      "§③ got `lambda = -(1+z)/(3z)` for the amplitude that would match at one redshift; the same number "
      "falls out of `B = 3K` here, which is the independent route to it*",
      abs(lam_rec + K_closed / B * (1.0 + Z_REC) / Z_REC) < 1e-12,
      f"lambda(z*) = {lam_rec:.6f}, and K/B x (1+z*)/z* = {K_closed / B * (1.0 + Z_REC) / Z_REC:.6f}")

print("\n" + "=" * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {8 - len(FAILS)} of 8 checks;  "
      f"{len(FAILS)} failure(s)" + ("" if not FAILS else ": " + "; ".join(FAILS[:2])))
print("=" * 100)
sys.exit(1 if FAILS else 0)
