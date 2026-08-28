#!/usr/bin/env python3
"""RECEIPT — spectral-theory bake `S5`: ** P15'S EXACT/WKB DISCREPANCY IS NOT AN ADIABATIC ERROR.  IT
IS MONOTONE IN THE WRONG DIRECTION AND SATURATES AT A NONZERO OFFSET, AND THE TEXT PLACES AN
ADIABATICITY REMARK BESIDE IT. **

LEVEL: NO RATE — WKB accuracy on the branch-point filter.

WHY THIS PROBE.  P15 was estimated MEDIUM on `WKB` x3 and `discrete spectrum` x2.  The discrete-sum
  half is already covered -- the harmonic bake's H1 verified the measure w_L = (L+1)/(L(L+2)) two ways
  and showed it is exactly d ln k_L / dL, so the CR sum is a Riemann sum of the very integral
  LambdaCDM uses.  ** The WKB half is not covered, and it carries a checkable claim. **

WHAT P15 SAYS.  "The exponential-of-an-integral form e^{-int omega d-eta} is a WKB approximation whose
  adiabaticity parameter is of order unity at l <~ 5" -- and then, from composing exact
  constant-omega transfer matrices over the segment: "exact/WKB ratios of 0.926, 0.913, 0.901, 0.891
  and 0.889 at l = 2, 3, 5, 15, 40: the WKB form is accurate to 7-11% at every multipole from 2 to
  40."

WHAT THE NUMBERS SAY.

      l          2      3      5     15     40
      ratio  0.926  0.913  0.901  0.891  0.889
      error   7.4%   8.7%   9.9%  10.9%  11.1%

  ** The ratio DECREASES monotonically with l.  WKB is MOST accurate at l = 2, where the adiabaticity
  parameter is of order unity, and LEAST accurate at l = 40, where it is small. **

  ** AN ADIABATIC ERROR BEHAVES THE OPPOSITE WAY. **  The WKB expansion is an expansion in the
  adiabaticity parameter, so an error of adiabatic origin is largest where that parameter is O(1) --
  here l <~ 5 -- and VANISHES as it does.  This one grows slightly with l and then SATURATES:
  0.891 at l = 15 and 0.889 at l = 40, a change of 0.002.  ** It tends to a constant near 0.889, not
  to 1. **

WHAT FOLLOWS.  The 7-11% is a SYSTEMATIC OFFSET and not the adiabaticity the neighbouring sentence
  names.  ** P15's conclusion is unaffected and if anything strengthened -- it says "the exact
  transmission is slightly smaller, so the filter is marginally stronger than the approximation gives",
  and a saturating offset makes that statement uniform in l rather than an accident of low multipole.
  What is misplaced is the attribution. **

  ROUTED, NOT APPLIED.  The clause owed: that the residual is an offset, uniform across the range, and
  therefore not the adiabatic correction discussed in the preceding sentence.

VERDICTS ARE ASSERTS.
"""

print("=" * 78)
print("  S5 — P15's exact/WKB ratios are not an adiabatic error")
print("=" * 78)

ls = [2, 3, 5, 15, 40]
rat = [0.926, 0.913, 0.901, 0.891, 0.889]

print(f"\n  {'l':>5} {'exact/WKB':>11} {'error':>8}")
for l, r in zip(ls, rat):
    print(f"  {l:5d} {r:11.3f} {100*(1-r):7.1f}%")

assert all(rat[i] > rat[i + 1] for i in range(len(rat) - 1)), "the ratio must be monotone decreasing"
print("\n  ** VERDICT 1: the ratio DECREASES monotonically with l.  WKB is MOST accurate at")
print("     l = 2, where P15 says the adiabaticity parameter is of ORDER UNITY, and LEAST")
print("     accurate at l = 40, where it is small. **")

print("\n  an adiabatic error is an expansion in that parameter, so it is LARGEST where the")
print("  parameter is O(1) and VANISHES as the parameter does.  This one does the opposite.")
assert rat[0] > rat[-1], "an adiabatic error would give the reverse ordering"
print("  ** VERDICT 2: the ordering is reversed from an adiabatic error. **")

tail = abs(rat[-1] - rat[-2])
print(f"\n  and it SATURATES: l=15 gives {rat[-2]}, l=40 gives {rat[-1]}, a change of {tail:.3f}")
assert tail < 0.01, "the ratio must saturate"
assert abs(rat[-1] - 1.0) > 0.10, "and it must saturate away from unity"
print(f"  ** VERDICT 3: it tends to a constant near {rat[-1]}, NOT to 1.  An adiabatic error")
print("     tends to zero; this tends to a nonzero offset. **")

print("\n  ** VERDICT 4: so the 7-11% is a SYSTEMATIC OFFSET, not the adiabaticity the")
print("     neighbouring sentence names.  P15's conclusion is unaffected and if anything")
print("     STRENGTHENED -- it says 'the exact transmission is slightly smaller, so the")
print("     filter is marginally stronger than the approximation gives', and a saturating")
print("     offset makes that uniform in l rather than an accident of low multipole.")
print("     What is misplaced is the attribution. **")

print("\n" + "=" * 78)
print("  ALL PASS")
print("=" * 78)
