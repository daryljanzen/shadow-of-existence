#!/usr/bin/env python3
"""RECEIPT — statistics/inference bake `S3`: ** P04'S ISOTROPY EXCLUSION IS A LOWER BOUND AGAINST AN
UPPER LIMIT, NOT AN ESTIMATE AGAINST AN ESTIMATE — AND THAT STRUCTURE, NOT THE RATIO, IS WHAT MAKES IT
ROBUST. NEITHER THE PAPER NOR ITS OWN RECEIPT SAYS SO. **

LEVEL: NO RATE — inference structure on a stated comparison.

THE FIELD'S QUESTION.  P04 excludes matter-tracking expansion by "an exclusion by three orders of
  magnitude": a predicted scatter of ~1e-3 against an observed <~3e-6.  A statistician's first move is
  that a RATIO OF POINT ESTIMATES is not an exclusion -- it carries no error model and no direction.
  ** The probe was built as that attack.  It bounces, and the reason it bounces is the finding. **

WHAT P04 ACTUALLY DOES.  Its receipt establishes sigma_path = 2.77e-3 as a FLOOR and then checks two
  alternative estimate choices, BOTH OF WHICH RAISE IT -- sigma_8(0) = 0.8 without growth-weighting
  gives 7.78e-3, and correlations with a smaller effective N give 5.55e-3.  So the prediction is a
  LOWER BOUND.  And the observed side, <~3e-6, is an UPPER LIMIT.

  ** LOWER BOUND AGAINST UPPER LIMIT.  Every free choice in the calculation pushes the two FURTHER
  apart, so the exclusion cannot be weakened by a different estimate -- only by a different physical
  claim.  That is the strongest form an exclusion of this kind can take, and it is stronger than the
  ratio the paper quotes. **

AND THE TEST CAN FAIL.  The control -- isotropic expansion with no matter-tracking -- returns
  sigma_path = 0 EXACTLY, not a small number.  A test whose null returns zero is one that could have
  come out the other way, which is what makes the three orders informative rather than decorative.

WHAT IS OWED IS A SENTENCE, in the same shape S2 found: name the structure, and state the robustness
  factor.  The observed limit would have to be 9x larger to weaken the exclusion to two orders, 92x to
  one order, and 923x for it to vanish.

ROUTED, NOT APPLIED.

VERDICTS ARE ASSERTS.

⌗ AMENDED r3535 (node 60) — VERDICT 3 WAS HOLLOW, AND THE HOLE WAS IN THE PLACE THE RECEIPT MAKES ITS
  LOUDEST CLAIM.  The file read `control = 0.0` and then `assert control == 0.0`: a literal asserted
  against itself.  ** A statement that the null returns EXACTLY zero cannot be checked by writing the
  zero down. **  Nothing about the physics was being tested, and no change to P04, to the separate-
  universe deficit, or to the path-averaging could ever have made that line fail.  The claim was true;
  the instrument for it was not there.  Now the zero is PRODUCED, three ways, and each of the three is
  a way the old line could not fail and the new ones can:

  (1) THE COUPLING IS DIFFERENTIATED OUT OF THE LAW, not assigned.  Each expansion law is written as
      a_local(delta) and the response coefficient read off as d ln a_local / d delta at delta = 0.
      Mass conservation in the cell, rho (1+delta) a_local^3 = rho a^3, gives a_local = a (1+delta)^(-1/3)
      and hence -1/3, which is P04's separate-universe deficit RE-DERIVED here.  The isotropic law is
      a_local = a, delta absent, and sympy returns 0 for its derivative.  ** The control's zero is now
      the derivative of a law with no delta in it. **
  (2) THE SCATTER IS REALISED, not formula'd.  20,000 Monte-Carlo lines of sight through N ~ 1174
      cells of Gaussian delta are drawn once and BOTH laws are pushed through the SAME field -- so the
      two runs differ in the law and in nothing else.  The tracking law reproduces P04's analytic
      2.77e-3 to within the MC error of the mean; the isotropic law returns a std over a vector that
      is identically zero.
  (3) AND THE DISCRIMINATING LEG, which is what the old assert lacked entirely: a NEAR-isotropic law,
      a_local = a (1+delta)^(-eps) with eps = 1e-3, is run through the same field and returns 8.3e-6,
      NOT zero.  ** So the exact zero is a property of the isotropic law and not of the code's shape:
      perturb the law by one part in a thousand and VERDICT 3's assert fails. **  That is the condition
      the `\\rcpt` rail requires and the one the previous line could not meet.

  Nothing in the finding changes.  N and the floor are now computed from P04's own integral rather
  than transcribed, and cross-checked against the figures P04's receipt pins, so the two files can no
  longer drift apart silently -- which is the second thing a transcribed constant cannot do.
"""

import numpy as np
import sympy as sp

print("=" * 78)
print("  S3 — the structure of P04's isotropy exclusion")
print("=" * 78)

# ── the prediction side, recomputed from P04's own integral rather than transcribed ──────────
Om, OL, z_lss, R = 0.315, 0.685, 1089.0, 8.0          # R in h^-1 Mpc
s8_eff, s8_0, obs = 0.285, 0.8, 3e-6
E = lambda z: np.sqrt(Om * (1 + z) ** 3 + OL)
zz = np.linspace(0, z_lss, 200000)
d_lss = 2998.0 * np.trapezoid(1 / E(zz), zz)
N_cells = d_lss / R

floor = s8_eff / (3 * np.sqrt(N_cells))
alts = {"sigma_8(0) = 0.8, no growth-weighting": s8_0 / (3 * np.sqrt(N_cells)),
        "correlations, smaller effective N": s8_eff / (3 * np.sqrt(N_cells / 4))}

# these are P04's pinned figures; recomputing rather than transcribing means a drift is caught here
assert abs(N_cells - 1173.81) < 0.05, "N must match P04's pinned cell count"
assert abs(floor - 2.7728e-3) < 1e-6, "the floor must match P04's pinned sigma_path"

print(f"\n  N = d_lss/R (recomputed from P04's integral) : {N_cells:.0f} cells")
print(f"  predicted scatter, as computed : {floor:.2e}")
for k, v in alts.items():
    print(f"      alternative choice           : {v:.2e}   ({v/floor:.1f}x LARGER)   <- {k}")
    assert v > floor, "every alternative estimate must RAISE the prediction"
print("  ** VERDICT 1: every alternative estimate choice raises it, so the computed value is a")
print("     LOWER BOUND on the predicted scatter, not a point estimate. **")

print(f"\n  observed scatter               : <= {obs:.1e}   (an UPPER LIMIT)")
ratio = floor / obs
print(f"  ratio                          : {ratio:.0f}   -- the paper's 'three orders of magnitude'")
assert 100 < ratio < 10000
print("  ** VERDICT 2: LOWER BOUND against UPPER LIMIT.  Every free choice pushes the two")
print("     further apart, so the exclusion cannot be weakened by a different estimate --")
print("     only by a different physical claim.  That is stronger than the quoted ratio. **")

# ── VERDICT 3, rebuilt: the null's zero is PRODUCED, not written down ────────────────────────
# (1) the response coefficient of each law, read off the law by differentiation.
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

# (2) one realised density field, both laws pushed through it, so only the law differs.
n_cells, n_paths = int(round(N_cells)), 20000
rng = np.random.default_rng(2718)
field = rng.normal(0.0, s8_eff, size=(n_paths, n_cells))
path_mean = field.mean(axis=1)


def sigma_path(coefficient):
    """the realised scatter in the path-averaged fractional redshift shift, for a given law."""
    return float((coefficient * path_mean).std())


s_track = sigma_path(c_track)
control = sigma_path(c_iso)
s_near = sigma_path(c_near)
mc_err = floor / np.sqrt(2 * n_paths)      # the MC error on a std from n_paths draws

print(f"\n  the SAME field ({n_paths} lines of sight x {n_cells} cells) pushed through each law:")
print(f"      matter-tracking : sigma_path = {s_track:.3e}   (analytic floor {floor:.3e}, MC err {mc_err:.1e})")
print(f"      near-isotropic  : sigma_path = {s_near:.3e}   -- SMALL, and NOT zero")
print(f"      the control: isotropic expansion, no matter-tracking : sigma_path = {control:.1f}")
assert abs(s_track - floor) < 6 * mc_err, "the MC must reproduce P04's analytic floor"
assert control == 0.0, "the null must return exactly zero, not a small number"
assert s_near > 0.0 and s_near < obs * 10, \
    "the near-isotropic law must return a SMALL NONZERO number -- this is what makes the zero above a test"
assert s_near / max(control, 1e-300) > 1e12, \
    "perturbing the law by one part in a thousand must break the exact zero"
print("  ** VERDICT 3: the null returns EXACTLY zero, so the test could have come out the")
print("     other way.  That is what makes the three orders informative.")
print(f"     AND IT IS A TEST: perturb the law to a(1+delta)^(-1e-3) and the same field returns")
print(f"     {s_near:.1e}, not zero.  The zero belongs to the isotropic LAW, not to the code. **")

print("\n  robustness factor, in the shape S2 established for P15:")
for tgt, lbl in [(100, "two orders"), (10, "one order"), (1, "no exclusion at all")]:
    need = floor / tgt
    print(f"      to weaken the ratio to {tgt:>4} ({lbl:19s}): observed limit must be {need/obs:>5.0f}x larger")
assert floor / 100 / obs > 1, "even two orders needs a factor above one"

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
