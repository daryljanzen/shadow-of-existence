"""
P14_L8_the_three.py -- verifies THE 3 (sec:family): the three HINGES and the three ROOTS are ONE 3, not two
  that coincidentally agree -- both solve the SAME horizon cubic (the sky-angle "designation" is the sine
  r0=(2/sqrt3)sin w), so the count is forced, not a choice. CONTROL at wrong scale (2/sqrt3->1) BREAKS
  (max|diff|=0.5), so the test can return NO. [P14 matter_sector_paper sec:family]
STATUS: ✔✔   ORIGIN: storyboard_receipts/L8_the_three.py, verified r1385.L8.1-a — THE 3: are the three HINGES and the three ROOTS one 3, or two that agree?

Daryl (r1146): "I don't think there's any choice. I think we've already established that."
UNDER TEST — his claim. This receipt must be able to return NO.

P3 (gauge alpha=1):  r0 = (2/sqrt3) sin w        [prop:gnomonic — the sky angle]
                     2M = (2/(3 sqrt3)) sin 3w   [prop:triple]
                     cubic: r^3 - r + 2M = 0     [the horizon cubic]
Hinges: three, 120 deg apart in the swing  [prop:twoalpha, sec:ontology]

CLAIM: the three hinges' own r0 values ARE the three roots of the cubic at that 2M.
If TRUE  -> one object (the dial w), two projections (w and 3w): a DERIVATION -> one 3.
If FALSE -> two triples that agree in count only.
"""
import numpy as np
s3 = np.sqrt(3.0)

def r0_of(w):  return (2.0/s3)*np.sin(w)
def twoM_of(w): return (2.0/(3.0*s3))*np.sin(3.0*w)

rng = np.random.default_rng(8)
worst = 0.0
for w in rng.uniform(-np.pi, np.pi, 4000):
    # the three hinges: 120 deg apart on the SAME dial
    hinge_r0 = np.array([r0_of(w + k*2*np.pi/3) for k in range(3)])
    # the cubic at the 2M this dial position sets
    twoM = twoM_of(w)
    roots = np.sort_complex(np.roots([1.0, 0.0, -1.0, twoM]))
    assert np.max(np.abs(roots.imag)) < 1e-9, "roots must be real on this dial"
    worst = max(worst, np.max(np.abs(np.sort(roots.real) - np.sort(hinge_r0))))
print(f"  [1] hinge r0 triple  vs  cubic roots : max|diff| = {worst:.3e}   -> {'MATCH' if worst<1e-9 else 'FAIL'}")

# --- the guard: could this have returned NO? Break the forced scale 2/sqrt3 -> 1. ---
def r0_bad(w): return 1.0*np.sin(w)
def twoM_bad(w): return r0_bad(w) - r0_bad(w)**3
bad = 0.0
for w in rng.uniform(-np.pi, np.pi, 400):
    h = np.array([r0_bad(w + k*2*np.pi/3) for k in range(3)])
    rt = np.roots([1.0, 0.0, -1.0, twoM_bad(w)])
    if np.max(np.abs(rt.imag)) > 1e-9: continue
    bad = max(bad, np.max(np.abs(np.sort(rt.real) - np.sort(h))))
print(f"  [2] CONTROL, wrong scale (2/sqrt3->1): max|diff| = {bad:.3e}   -> {'MATCH (test is vacuous!)' if bad<1e-9 else 'BREAKS — the test can return NO'}")

# --- and WHY: the identity behind it ---
w = 0.37
lhs = (lambda r: r**3 - r)(r0_of(w))
rhs = -(2.0/(3.0*s3))*np.sin(3*w)
print(f"  [3] identity  r0^3 - r0 == -(2/3sqrt3) sin 3w : {abs(lhs-rhs):.2e}")
print("      => sin(3(w+120k)) = sin(3w) for k=0,1,2, so the three dial positions")
print("         SOLVE THE SAME CUBIC. The 'designation' is the sine. Not a choice.")
