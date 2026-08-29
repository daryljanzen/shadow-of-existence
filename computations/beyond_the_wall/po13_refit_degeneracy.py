#!/usr/bin/env python3
"""KILL THE DEGENERACY between the phase drift and the acoustic scale, before any data.

A wrong l_A = a uniform comb stretch = a phase residual LINEAR in q.  So refit l_A to each arm's own comb
(the linear-in-q trend that minimises the residual across q=1..6) and recompute.  What survives the linear
refit -- the CURVATURE -- is genuine phase incoherence, independent of the ruler; what is absorbed was just
a wrong acoustic scale (the +7% position over-drive seen twice).

Report, both arms: fitted slope (= implied fractional l_A shift), residual spread BEFORE and AFTER the
linear refit, and the surviving curvature.  The control MUST stay flat under its own refit or the test is
void.
"""
import numpy as np

q = np.array([1., 2., 3., 4., 5., 6.])
cr = np.array([0.245, 0.581, 0.758, 0.858, 0.926, 0.995])   # r3545 residual/pi
ct = np.array([0.254, 0.196, 0.206, 0.204, 0.227, 0.235])


def refit(name, r):
    # 2-param linear refit: r ~ a*q + b  (a = l_A/ruler degeneracy, b = absolute-phase reference)
    a, b = np.polyfit(q, r, 1)
    after = r - (a * q + b)
    # curvature: quadratic term (l_A-independent, absolute-phase-independent shape)
    c2 = np.polyfit(q, r, 2)[0]
    print(f"  {name}:")
    print(f"    raw residual        = {[round(x,3) for x in r]}   spread {r.max()-r.min():.3f}pi")
    print(f"    fitted slope a      = {a:+.4f}pi/q   (implied uniform l_A/ruler shift ~ {a*100:+.1f}% of a peak-spacing per peak)")
    print(f"    after linear refit  = {[round(x,3) for x in after]}")
    print(f"    spread AFTER refit  = {after.max()-after.min():.3f}pi   RMS {np.sqrt(np.mean(after**2)):.3f}pi")
    print(f"    surviving curvature = {c2:+.4f}pi/q^2  (concave arch if <0)")
    return after, np.sqrt(np.mean(after**2))


print("=" * 82)
print("  DEGENERACY CHECK -- refit l_A (best linear-in-q) and see what survives")
print("=" * 82)
ac_cr, rms_cr = refit("CR ", cr)
print()
ac_ct, rms_ct = refit("CTL", ct)
print()
print("  VALIDITY: control flat under its own refit? spread_after_CTL = "
      f"{ac_ct.max()-ac_ct.min():.3f}pi  ({'OK (flat floor)' if ac_ct.max()-ac_ct.min()<0.1 else 'FAIL'})")
print(f"  DISCRIMINANT: CR surviving RMS {rms_cr:.3f}pi  vs  control floor RMS {rms_ct:.3f}pi  "
      f"-> ratio {rms_cr/rms_ct:.1f}x")
print()
if rms_cr > 2.5 * rms_ct:
    print("  => the drift SURVIVES the l_A refit: a genuine, ruler-independent phase incoherence remains")
    print(f"     (the CURVATURE, ~{ac_cr.max()-ac_cr.min():.2f}pi peak-to-peak). BUT most of the raw {cr.max()-cr.min():.2f}pi")
    print("     drift was the acoustic-scale degeneracy -- the testable NEW signal is the smaller curvature.")
else:
    print("  => the drift is ABSORBED by the l_A refit: it is a wrong acoustic scale, not incoherence")
    print("     -- the same thing as the +7% position over-drive. Nothing new to take to Planck.")
