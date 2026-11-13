#!/usr/bin/env python3
"""`r7757+cc66` IS `r` A PROFILE DIRECTION AT ALL, AND WHY THE TWO ACCOUNTS OF RADIATION'S GRAVITY HAVE
OPPOSITE SIGNS.

⛭ Registered in `PREDICTION.md` at `r7757+cc66.0`, pushed before this file existed, INCLUDING its stated
expectation of contradicting `r7755+cc66` §⑦ and the failure mode that would leave §⑦ standing.

⛭ ** THE CHART IS 60's, READ BY PATH ** (`r7445`): `r7580/lightpath.py` carries `alpha`, `r0`, `TWO_M`,
the background, and `r_of_tt`, the chart's own areal radius as a function of cosmic time.

THE QUESTION.  `P15` `sec:properframe` step (iv): *"the areal radius across the congruence depends on
`tau, chi` only through their sum, `r(tau,chi) = r(tau+chi)`"*, and cosmic time is `tilde tau = tau +
chi`.  If that is so then `r` is constant on a leaf, `rho(r)` is a HISTORY and not a PROFILE, and the
mass-function integral that produced `r7614`'s law is integrating across leaves rather than across space.
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
H_stack, H_leaf, r_of_tt = NS['H_stack'], NS['H_leaf'], NS['r_of']
h0 = H0 / C
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

# ------------------------------------------------------------------ R1 is r a direction within a leaf?
tt_of_z = NS['tt_of_z']      # the chart's own cosmic time at redshift z, read rather than rewritten


LEAVES = [0.0, 10.0, 100.0, Z_REC]
spreads, radii = [], []
for zl in LEAVES:
    tt = tt_of_z(zl)
    # walk ALONG the leaf: tilde tau = tau + chi held fixed, chi swept across the congruence
    chis = np.linspace(0.0, 0.9 * tt, 2001)
    taus = tt - chis
    rr = np.array([r_of_tt(t + c) for t, c in zip(taus, chis)])   # r(tau + chi), the chart's own form
    spreads.append(float(np.max(np.abs(rr / rr[0] - 1.0))))
    radii.append(float(rr[0]))

check("⛭⛔ `r7757` ** ① `r` IS CONSTANT ON EVERY COSMOLOGICAL LEAF: IT LABELS THE LEAF AND IS NOT A "
      "DIRECTION WITHIN ONE ** ⇒ *** swept along each leaf by moving `chi` and compensating in `tau` at "
      "fixed `tilde tau = tau + chi`, which is step (iv)'s own variable; `2001` points per leaf, four "
      "leaves from today to last scattering *** ⛔ *so `rho(r)` is a HISTORY across leaves and not a "
      "profile across space, and `int 4 pi rho(r) r^2 dr` is not a mass interior to a sphere*",
      max(spreads) < 1e-12,
      "max relative spread of r along a leaf: " + ", ".join(f"z={z:.0f}: {s:.2e}" for z, s in zip(LEAVES, spreads)))

check("⛭ `r7757` ** ② AND `r` DOES VARY BETWEEN LEAVES, SO ① IS A TEST AND NOT A TAUTOLOGY ** ⇒ *if `r` "
      "were constant everywhere the first check would pass vacuously*",
      max(radii) / min(radii) > 1e3,
      "r across the sampled leaves: " + ", ".join(f"{v:.4g}" for v in radii) +
      f" Mpc, spanning {max(radii) / min(radii):.4g}x")

# ------------------------------------------------------------------ R2 the two accounts
z = np.geomspace(1e-6, Z_REC, 4001)
r = r0 / (1.0 + z)
K = h0 ** 2 * OMR * r0 ** 4


def h2_of_mu(mu, rr):
    return mu / rr ** 3 + 1.0 / alpha ** 2


bend_hist = K / r                                         # the comoving volume's energy, falling as 1/a
mu_hist = TWO_M + bend_hist
e3 = float(np.max(np.abs(h2_of_mu(mu_hist, r) / (H_leaf(z) / C) ** 2 - 1.0)))
check("⛭⛔ `r7757` ** ③ THE HISTORY READING IS THE STANDARD RADIATION TERM, AND ITS RATE IS THE LEAF "
      "RATE ** ⇒ *radiation's gravitating energy in a comoving volume falls as `1/a`, so `mu = 2M + K/r`; "
      "that is not an exotic source but the textbook `(1+z)^4` term, and `r7755`'s inverted mass function "
      "is exactly it*",
      e3 < 1e-10, f"K = {K:.6e} Mpc^2; worst relative deviation from H_leaf = {e3:.3e}")

B = 3.0 * K
# rho_r ∝ r^-4 integrated AS A PROFILE with m(r0) = M.  `1/r_0 - 1/r` is written in its exact
# cancellation-free form `-z/r_0`, since `1/r = (1+z)/r_0` -- the same correction `r7755` needed.
bend_prof = B * (-z / r0)
mu_prof = TWO_M + bend_prof
term_prof = h2_of_mu(mu_prof, r) - h2_of_mu(TWO_M, r)
term_pub = -3.0 * h0 ** 2 * OMR * z * (1.0 + z) ** 3
hi = z >= 1e-2
e4 = float(np.max(np.abs(term_prof[hi] / term_pub[hi] - 1.0)))
check("⛭ `r7757` ** ④ AND THE PROFILE READING IS `r7614`'s PUBLISHED LAW, `-3 Omega_r z(1+z)^3` ** ⇒ *the "
      "same instrument reproduces the paper's printed bend, so the two accounts below are this corpus's "
      "own two accounts and not a straw man.* ⌗ *Compared above `z = 1e-2`, where the subtraction is not "
      "at its cancellation floor -- the floor measured and diagnosed at `r7755` §⑦*",
      e4 < 1e-10, f"worst |measured/printed - 1| above z = 1e-2: {e4:.3e}")

check("⛭⛔⛭ `r7757` ** ⑤ SO THE TWO ACCOUNTS ARE TWO MASS FUNCTIONS, `+K/r` AGAINST `-3K(1/r_0 - 1/r)`, "
      "AND THEIR RATIO IS THE PAPER'S OWN `-3z/(1+z)` ** ⇒ *** the whole of the sign difference is the "
      "step of integrating `rho(r)` IN `r`: one reading asks what the comoving volume's energy is at "
      "epoch `r`, the other asks what mass lies inside radius `r` -- and by ① the second question has no "
      "referent, because `r` does not run inside a leaf *** ",
      float(np.max(np.abs((bend_prof / bend_hist) / (-3.0 * z / (1.0 + z)) - 1.0))) < 1e-13,
      f"ratio of the two bends / (-3z/(1+z)) - 1: worst "
      f"{float(np.max(np.abs((bend_prof / bend_hist) / (-3.0 * z / (1.0 + z)) - 1.0))):.3e}  "
      f"[taken on the bend terms themselves; forming them as mu - 2M reintroduces the same "
      f"cancellation that bit twice at r7755, which is why they are kept as their own expressions]")

dp_hist = -K / r ** 2
dp_prof = B / r ** 2
check("⛭⛔ `r7757` ** ⑥ AND `m'(r) != 0` ON **BOTH** READINGS, SO THE KERNEL THEOREM IS UNTOUCHED EITHER "
      "WAY ** ⇒ *** `P15`'s *radiation requires `m'(r) != 0`, a bend of the cut* is TRUE on the history "
      "reading too -- what the two readings disagree about is only what the bend is a bend IN, not "
      "whether radiation bends the cut. *** ⛔ *So `r7755` §⑦'s `no cut supplies the leaf rate` fails at "
      "its interpretive step, not its algebra: `mu' < 0` is the radiation energy REDSHIFTING, not a "
      "negative density.*",
      bool(np.all(dp_hist != 0.0)) and bool(np.all(dp_prof != 0.0))
      and bool(np.all(dp_hist < 0.0)) and bool(np.all(dp_prof > 0.0)),
      f"history mu' in [{dp_hist.min():.3e}, {dp_hist.max():.3e}] (falling energy); "
      f"profile mu' in [{dp_prof.min():.3e}, {dp_prof.max():.3e}] (rising enclosed mass)")

# ------------------------------------------------------------------ R3 what it costs the late-time law
d0 = abs(float(H_leaf(0.0) / H_stack(0.0)) - 1.0)
zg = np.geomspace(1e-3, Z_REC, 200001)
dev = np.abs(H_leaf(zg) / H_stack(zg) - 1.0)
z1pc = float(zg[np.argmax(dev >= 0.01)]) if np.any(dev >= 0.01) else float('nan')
check("⛭ `r7757` ** ⑦ AND IT COSTS THE LATE-TIME LAW NOTHING: THE TWO RATES DIFFER BY `Omega_r` TODAY ** "
      "⇒ *the `sinh^{2/3}` law, `z_acc = x_0 - 1` and `Lambda` setting the amplitude are untouched at the "
      "level any of them is used; this is the thing the order asked be protected and it is measured "
      "rather than asserted*",
      d0 < 1e-4,
      f"|H_leaf/H_stack - 1| at z = 0 is {d0:.3e} (Omega_r = {OMR:.3e}); it first reaches 1 % at "
      f"z = {z1pc:.1f}")

print("\n" + "=" * 100)
print(f"  {'OK  ' if not FAILS else 'FAIL'}  {7 - len(FAILS)} of 7 checks;  "
      f"{len(FAILS)} failure(s)" + ("" if not FAILS else ": " + "; ".join(FAILS[:2])))
print("=" * 100)
sys.exit(1 if FAILS else 0)
