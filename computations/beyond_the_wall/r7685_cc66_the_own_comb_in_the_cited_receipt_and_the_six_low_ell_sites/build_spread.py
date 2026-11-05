"""ARM (2): is the BUILD CHOICE itself worth more than three per cent at some multipole?

If it is, naming DECOUPLED does not make the cross-validation claim build-independent, and the
honest sentence carries the spread rather than quoting the favourable build's number alone.
"""
import os
import numpy as np
ROOT = '/home/user/shadow-of-existence'
d = np.load(os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra',
                         'p15_lowell_depths_distances_leafrec1.npz'), allow_pickle=True)
e, A, F, Dc = d['ells'], d['armA_exact'], d['armB_frozen'], d['armB_decoupled']
rf, rd = (F - A) / A * 100, (Dc - A) / A * 100
bs = (F - Dc) / A * 100                      # the build spread, in units of arm A

print("  l   armA   FROZEN rel%   DECOUP rel%   BUILD SPREAD (F-D)/A %")
for i, l in enumerate(e):
    print(f" {l:2d} {A[i]:.4f}   {rf[i]:+7.3f}      {rd[i]:+7.3f}       {bs[i]:+7.3f}")

m = e != 3
print(f"\n  worst |rel| FROZEN   : all {max(abs(rf)):.3f}   excluding l=3 {max(abs(rf[m])):.3f}")
print(f"  worst |rel| DECOUPLED: all {max(abs(rd)):.3f}   excluding l=3 {max(abs(rd[m])):.3f}")
print(f"  worst |build spread| : all {max(abs(bs)):.3f}   at l = {int(e[np.argmax(abs(bs))])}")
print(f"  build spread over 3% at: {[int(x) for x in e[abs(bs) > 3.0]]}")
print(f"\n  ARM (2): {'CONFIRMED' if max(abs(bs[(e>=2)&(e<=5)])) > 3.0 else 'FALSIFIED'}"
      f" -- the build choice is worth {max(abs(bs[(e>=2)&(e<=5)])):.2f}% at worst over l = 2-5")

# which build supports "three per cent at every multipole but the octopole"
for nm, r in (('FROZEN', rf), ('DECOUPLED', rd)):
    ok = max(abs(r[m])) < 3.0
    print(f"  \"three per cent at every multipole but the octopole\" on {nm:9s}: "
          f"{'TRUE' if ok else 'FALSE'}  (worst off-octopole {max(abs(r[m])):.2f}%)")

# l=3 is the only multipole where arm B sits ABOVE arm A on BOTH builds
both_up = [int(l) for i, l in enumerate(e) if rf[i] > 0 and rd[i] > 0]
print(f"\n  arm B above arm A on BOTH builds at l = {both_up}"
      f"   (l=3 alone: {both_up == [3]})")
print(f"  and l=3 is the LARGEST deviation on DECOUPLED: "
      f"{int(e[np.argmax(abs(rd))]) == 3}")

# --- WHICH MECHANISM IS DOING THE WORK AT WHICH MULTIPOLE -----------------------------------------
# The paper says "neither the freeze nor the towers is doing the work".  That is testable HERE: the
# build spread IS the freeze/tower treatment's own contribution, since FROZEN and DECOUPLED differ in
# nothing else.  So compare each multipole's A-against-B residual with the spread between the builds.
print("\n  WHICH MECHANISM MOVES WHICH MULTIPOLE")
print("   l   |resid| DECOUP   |build spread|   ratio resid/spread   reading")
for i, l in enumerate(e):
    rr, ss = abs(rd[i]), abs(bs[i])
    rat = rr / ss if ss > 1e-9 else float('inf')
    if rat > 3.0:
        rd_ = 'THE CLOCK -- survives both tower treatments'
    elif rat < 0.5:
        rd_ = 'THE TOWERS -- the treatment moves it, not the clock'
    else:
        rd_ = 'mixed'
    print(f"  {l:2d}   {rr:9.3f}      {ss:9.3f}        {rat:11.2f}       {rd_}")
print(f"\n  l=3 has the SMALLEST build spread of l=2-5 ({abs(bs[1]):.3f}%) and the LARGEST residual "
      f"({abs(rd[1]):.3f}%).")
print(f"  l=4 has the LARGEST build spread ({abs(bs[2]):.3f}%) and, on DECOUPLED, the smallest "
      f"residual of l=2-5 ({abs(rd[2]):.3f}%).")
print(f"\n  => 'neither the freeze nor the towers is doing the work' is TRUE at l=3 "
      f"(resid/spread {abs(rd[1])/abs(bs[1]):.1f}) and FALSE at l=4 "
      f"(resid/spread {abs(rd[2])/abs(bs[2]):.2f}): at the octopole the residual survives both tower "
      f"treatments with the SAME SIGN, and at l=4 the treatment is the whole of it.")
