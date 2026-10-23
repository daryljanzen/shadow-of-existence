#!/usr/bin/env python3
"""RECEIPT — statistics/inference bake `S3`: ** P04'S ISOTROPY EXCLUSION IS A LOWER BOUND AGAINST AN
UPPER LIMIT, NOT AN ESTIMATE AGAINST AN ESTIMATE — AND THAT STRUCTURE, NOT THE RATIO, IS WHAT MAKES IT
ROBUST. **

LEVEL: NO RATE — inference structure on a stated comparison.

THE FIELD'S QUESTION.  P04 excludes a matter-tracking expansion rate: light crossing independent cells
  of uniform density, each expanding at its own rate, accumulates a redshift scatter of ~8.8e-3, against
  a whole measured CMB anisotropy of 4.1e-5.  A statistician's first move is that a RATIO OF POINT
  ESTIMATES is not an exclusion -- it carries no error model and no direction.
  ** The probe is that attack.  It bounces, and the reason it bounces is the finding. **

WHAT P04 ACTUALLY DOES.  Its receipt establishes the uncorrelated value as a FLOOR and computes two
  alternative estimate choices, BOTH OF WHICH RAISE IT -- the correlations of the matter field along the
  ray (1.6e-2) and holding the contrast at its present value along the path (8.5e-2).  So the prediction
  is a LOWER BOUND.  And the measured side bounds the redshift scatter from ABOVE: whatever scatter the
  sky carries must fit inside the whole measured anisotropy together with everything else on the sky.

  ** LOWER BOUND AGAINST UPPER LIMIT.  Every free choice in the calculation pushes the two FURTHER
  apart, so the exclusion cannot be weakened by a different estimate -- only by a different physical
  claim.  That is the strongest form an exclusion of this kind can take. **  The paper says so, with the
  robustness factor: the sky would have to be some 210 times more anisotropic for the floor to reach it.

AND THE TEST CAN FAIL.  The null is PRODUCED, three ways:
  (1) THE COUPLING IS DIFFERENTIATED OUT OF THE LAW, not assigned.  Each expansion law is written as
      a_local(delta) and its response read off as d ln a_local / d delta at delta = 0: mass conservation
      gives -1/3, P04's separate-universe deficit re-derived; the isotropic law a_local = a has no delta,
      and sympy returns 0.
  (2) THE SCATTER IS REALISED, not formula'd.  20,000 Monte-Carlo lines of sight through the cells P04
      integrates over -- each cell of comoving length R carrying a Gaussian contrast sigma_R(z) and the
      weight g = a H f / 3 of P04's line integral -- are drawn once and every law is pushed through the
      SAME field, so the runs differ in the law and in nothing else.  The tracking law reproduces P04's
      floor within the MC error; the isotropic law returns a std over a vector that is identically zero.
  (3) THE DISCRIMINATING LEG: a NEAR-isotropic law, a (1+delta)^(-1e-3), through the same field returns
      a small number and NOT zero.  ** So the exact zero is a property of the isotropic law and not of
      the code's shape. **

  The floor, its alternatives, the measured rms and the cells are taken from P04's own receipt by
  running it, not transcribed, so the two files cannot drift apart silently.
"""

import os
import runpy
import contextlib
import io
import numpy as np
import sympy as sp

print("=" * 78)
print("  S3 — the structure of P04's isotropy exclusion")
print("=" * 78)

# ── the prediction side, computed by P04's own receipt ──────────────────────────────────────
HERE = os.path.dirname(os.path.abspath(__file__))
P04 = os.path.join(HERE, "..", "P04_modern_parallax", "P04_redshift_isotropy_floor.py")
with contextlib.redirect_stdout(io.StringIO()):
    G = runpy.run_path(P04)
floor, corr, rms, nogrowth = G["u8"], G["c8"], G["rms"], G["u8_const"]
chi, g, s2R, h = G["chi"], G["g"], G["s2R8"], G["h"]
R = 8 / h                                          # Mpc
assert G["ok"], "P04's own receipt must pass"

print(f"\n  floor (uncorrelated cells, R = 8 h^-1 Mpc)  : {floor:.2e}")
alts = {"the correlations of the matter field along the ray": corr,
        "the contrast held at its present value along the path": nogrowth}
for k, v in alts.items():
    print(f"      alternative choice           : {v:.2e}   ({v/floor:.1f}x LARGER)   <- {k}")
    assert v > floor, "every alternative estimate must RAISE the prediction"
print("  ** VERDICT 1: every alternative estimate choice raises it, so the computed value is a")
print("     LOWER BOUND on the predicted scatter, not a point estimate. **")

print(f"\n  measured anisotropy, whole sky : {rms:.2e}   (an UPPER LIMIT on any redshift scatter)")
ratio = floor / rms
print(f"  ratio                          : {ratio:.0f}   -- the paper's 'some 210'")
assert 200 < ratio < 225
print("  ** VERDICT 2: LOWER BOUND against UPPER LIMIT.  Every free choice pushes the two")
print("     further apart, so the exclusion cannot be weakened by a different estimate --")
print("     only by a different physical claim. **")

# ── VERDICT 3: the null's zero is PRODUCED, not written down ────────────────────────────────
_a, _delta, _eps = sp.symbols("a delta epsilon", positive=True)


def response(a_local):
    """d ln a_local / d delta at delta = 0 — the fractional expansion response to a density contrast."""
    return sp.simplify(sp.diff(sp.log(a_local), _delta).subs(_delta, 0))


law_tracking = _a * (1 + _delta) ** sp.Rational(-1, 3)   # rho (1+delta) a_local^3 = rho a^3
law_isotropic = _a                                       # delta does not appear
law_near_iso = _a * (1 + _delta) ** (-_eps)              # the discriminating leg

c_track = float(response(law_tracking))
c_iso = float(response(law_isotropic))
c_near = float(response(law_near_iso).subs(_eps, sp.Rational(1, 1000)))

print("\n  the response coefficient d ln a_local / d delta, DIFFERENTIATED out of each law:")
print(f"      matter-tracking   a(1+delta)^(-1/3) : {c_track:+.6f}   (P04's separate-universe deficit)")
print(f"      isotropic         a                 : {c_iso:+.6f}   (delta does not appear in the law)")
print(f"      near-isotropic    a(1+delta)^(-1e-3): {c_near:+.6f}   (the leg that must NOT return zero)")
assert abs(c_track + 1 / 3) < 1e-12, "mass conservation must give exactly -1/3, re-derived here"
assert c_iso == 0.0, "the isotropic law has no delta, so its derivative must be exactly zero"

# one realised field of independent cells along the ray, every law pushed through it
n_cells, n_paths = int(chi[-1] // R), 20000
xc = (np.arange(n_cells) + 0.5) * R
w = np.interp(xc, chi, g) * R * np.sqrt(np.interp(xc, chi, s2R))     # g R sigma_R per cell
rng = np.random.default_rng(2718)
unit = rng.normal(0.0, 1.0, size=(n_paths, n_cells))
path_sum = unit @ w                                                   # sum_i g_i R delta_i / (-1)


def sigma_path(coefficient):
    """the realised scatter of the accumulated redshift for a law of the given response:
    the rate response is the time derivative of the deficit, so the response scales g by -3 c."""
    return float((-3 * coefficient * path_sum).std())


s_track = sigma_path(c_track)
control = sigma_path(c_iso)
s_near = sigma_path(c_near)
mc_err = floor / np.sqrt(2 * n_paths)

print(f"\n  the SAME field ({n_paths} lines of sight x {n_cells} cells) pushed through each law:")
print(f"      matter-tracking : sigma_path = {s_track:.3e}   (P04's floor {floor:.3e}, MC err {mc_err:.1e})")
print(f"      near-isotropic  : sigma_path = {s_near:.3e}   -- SMALL, and NOT zero")
print(f"      the control: isotropic expansion, no matter-tracking : sigma_path = {control:.1f}")
assert abs(s_track - floor) < 6 * mc_err + 0.01 * floor, "the MC must reproduce P04's floor"
assert control == 0.0, "the null must return exactly zero, not a small number"
assert 0.0 < s_near < rms * 10, \
    "the near-isotropic law must return a SMALL NONZERO number -- this is what makes the zero above a test"
assert s_near / max(control, 1e-300) > 1e12, \
    "perturbing the law by one part in a thousand must break the exact zero"
print("  ** VERDICT 3: the null returns EXACTLY zero, so the test could have come out the")
print("     other way.  AND IT IS A TEST: perturb the law to a(1+delta)^(-1e-3) and the same")
print(f"     field returns {s_near:.1e}, not zero.  The zero belongs to the isotropic LAW, not to the code. **")

print("\n  robustness factor:")
for tgt, lbl in [(100, "two orders"), (10, "one order"), (1, "no exclusion at all")]:
    need = floor / tgt
    print(f"      to weaken the ratio to {tgt:>4} ({lbl:19s}): the measured anisotropy must be {need/rms:>5.1f}x larger")
assert abs(floor / rms - 214) < 6, "the paper's 'some 210 times more anisotropic'"

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
