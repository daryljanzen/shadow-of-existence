#!/usr/bin/env python3
r"""r7806 (60) -- the addendum: Ⓕ⑥'s first form was the defect, not the screen.

The probe's Ⓕ⑥ printed the screen's TOTAL overlap with the signature beside the fit's INCREMENTAL
gain over the tilt, and the two disagreed by 48.6, 31.9 and 10.1 points.  Read that way, r7804's
residual screen looked to fail on the first direction unlike a tilt it was applied to.

They are not the same object.  The fit's gain is what Y_He adds ON TOP OF a tilt that is already
free; the screen's `rem` is what Y_He would remove from the signature with NO tilt in the model,
and most of what it removes is the same part the tilt already took.  The screen's own prediction
for the fit's gain is the residual overlap SQUARED times the share of the signature the residual
is -- which is exactly the quantity r7804 minted and not the one the probe printed.

Formed on the same base, the difference does not survive.  ⇒ GUARD: a screen is compared with a
fit on the base the fit reports against, and a disagreement between a total and an increment is a
disagreement between two quantities, not a finding.
"""
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
d = np.load(os.path.join(HERE, 'runs', 'r7806_probe.npz'))
r_yh, c_st, rem = d['r_yh'], d['c_st'], d['rem']
gain = d['a3'] - d['a2']
LBL = ('100-1758', '700-1760', '1000-1760')

print("=" * 100)
print("r7806 (60) -- ADDENDUM: the screen against the fit, on the fit's own base")
print("=" * 100)

print("\n  [A] THE FORM THE PROBE PRINTED -- a TOTAL overlap beside an INCREMENT")
print(f"\n      {'window':>12}{'screen total':>15}{'fit gain':>12}{'ratio':>9}")
bad = []
for i, lbl in enumerate(LBL):
    bad.append(float(gain[i] / rem[i]))
    print(f"      {lbl:>12}{rem[i]:>14.2f}%{gain[i]:>11.2f}%{bad[-1]:>9.3f}")
print(f"      ⇒ the ratio scatters over a factor of {max(bad) / min(bad):.1f}. "
      f"Read this way the screen predicts nothing.")

print("\n  [B] THE SCREEN'S OWN PREDICTION, which is what r7804 minted:")
print("      predicted gain = corr(Y_He, residual)^2  x  (share of the signature the residual is)")
print(f"\n      {'window':>12}{'corr':>9}{'tilt takes':>12}{'residual is':>13}"
      f"{'PREDICTED':>11}{'MEASURED':>10}{'ratio':>8}")
good = []
ROWS = []
for i, lbl in enumerate(LBL):
    tilt_share = float(c_st[i]) ** 2
    resid_share = 1.0 - tilt_share
    pred = float(r_yh[i]) ** 2 * resid_share * 100.0
    good.append(float(gain[i]) / pred)
    ROWS.append((lbl, pred, float(gain[i]), good[-1]))
    print(f"      {lbl:>12}{r_yh[i]:>9.4f}{tilt_share * 100:>11.1f}%{resid_share * 100:>12.1f}%"
          f"{pred:>10.2f}%{gain[i]:>9.2f}%{good[-1]:>8.2f}")
print(f"      ⇒ the ratio is {min(good):.2f} to {max(good):.2f} -- a factor of "
      f"{max(good) / min(good):.2f} across three windows whose residual share runs 28 to 3 per cent,")
print(f"        against the factor of {max(bad) / min(bad):.1f} the wrong pairing gave.")

print("\n  [C] AND THE SIGN OF THE MISS IS THE RIGHT ONE, which is the check that it is not a fluke.")
print("      Every measured gain EXCEEDS the prediction, never falls short, because the fit")
print("      re-optimises the tilt while the projection holds it fixed -- so the projection is a")
print("      LOWER bound on what a free fit recovers, approached from below and not crossed.")
for lbl, pred, meas, rat in ROWS:
    print(f"        {lbl:>12}: predicted {pred:5.2f} %  <  measured {meas:5.2f} %   (x{rat:.2f})")
assert all(m > p for _, p, m, _ in ROWS), "the projection is not a lower bound after all"
print("      ⇒ asserted: the projection is a lower bound on every window.")

print("\n" + "=" * 100)
print("  WHAT THIS CHANGES AND WHAT IT DOES NOT")
print("=" * 100)
print("""
  r7804's screen GENERALISES to Y_He, a direction far less tilt-like than either parameter it was
  minted on: it predicts the fit's incremental gain to better than a factor of two on all three
  windows, with the right sign on every one.

  What it does NOT do is predict the TOTAL overlap's worth of absorption, because the tilt has
  already taken that.  The screen answers the question PO-24 asks -- how much does freeing this
  parameter cost the displacement -- and not the question of how much the parameter resembles the
  signature.  Y_He is the clearest case yet of the two coming apart: it removes 53.5 per cent of
  the signature on the published window and buys 4.9 points of absorbed share.

  ⌗ The first form of this comparison is kept above rather than deleted, because the defect is
    instructive: both numbers were correct and the sentence putting them side by side was not.
""")
