"""D4 — IS NARIAI A SADDLE-NODE, AND WHAT SCALING DOES THAT FORCE?
CONFIRMATION 4 — and the collision guards the wording: the corpus's 'bifurcation' x23 is ALL the GR
BIFURCATION SPHERE of a Killing horizon, and P7's guard leans on 'the degenerate horizon carries NO
bifurcation sphere'.  So nothing below may be written as 'the bifurcation at Nariai' bare.
BASELINE (base r1838): saddle-node x0 · pitchfork x0 · transcritical x0 · normal form x0 ·
phase portrait x0 · structural stability x0.  And no near-Nariai scaling law of any kind."""
import sympy as sp, numpy as np
r,M,eps=sp.symbols('r M epsilon', real=True)
print("="*80); print("D4 — THE FOLD AT NARIAI, AND THE SQUARE-ROOT LAW IT FORCES"); print("="*80)
h=r**3-r+2*M                      # gauge alpha = 1
print(f"\n  horizon cubic (alpha=1):  h(r) = {h}")
Mc=sp.Rational(1,2)*2/(3*sp.sqrt(3)); rc=1/sp.sqrt(3)
print(f"  Nariai:  2M_c = {sp.nsimplify(2*Mc)} = {float(2*Mc):.6f},  double root r_c = 1/sqrt3 = {float(rc):.6f}")
print(f"    check h(r_c) = {sp.simplify(h.subs([(M,Mc),(r,rc)]))} ,  h'(r_c) = {sp.simplify(sp.diff(h,r).subs([(M,Mc),(r,rc)]))}")
print("""
STEP 1 — CLASSIFY IT.  h(r_c)=0 and h'(r_c)=0 with h''(r_c) != 0, and the parameter enters h
  additively at first order.  That is the FOLD (saddle-node): two simple roots collide and
  annihilate, leaving none real, as one parameter passes a critical value.
""")
print(f"    h''(r_c) = {sp.simplify(sp.diff(h,r,2).subs(r,rc))}  (nonzero)")
print(f"    dh/d(2M) = {sp.diff(h,M)/2}  (nonzero, and r-independent -- the additive unfolding)")
print("""
STEP 2 — THE NORMAL FORM, and the scaling it forces.
  Near a fold, h(r) ~ (1/2) h''(r_c) (r - r_c)^2 + (dh/dmu) (mu - mu_c), so the two roots sit at
      r - r_c = ± sqrt( -2 (dh/dmu)(mu - mu_c) / h''(r_c) ) ,
  i.e. *** THEY SEPARATE AS THE SQUARE ROOT OF THE DISTANCE FROM THE CRITICAL VALUE. ***
""")
print("  VERIFY numerically on the exact cubic:")
def roots(m2):
    rr=np.roots([1,0,-1,m2]); return np.sort([x.real for x in rr if abs(x.imag)<1e-10])
m2c=float(2*Mc)
print("     delta = 2M_c - 2M      root gap        gap / sqrt(delta)")
for d in [1e-2,1e-3,1e-4,1e-5,1e-6]:
    rts=roots(m2c-d)
    inner=[x for x in rts if x>0]
    gap=max(inner)-min(inner)
    print(f"     {d:<10.1e}          {gap:<14.8f}  {gap/np.sqrt(d):.6f}")
print("  -> the ratio converges: the gap IS c.sqrt(delta).  The fold's law, confirmed on the exact cubic.")
print("""
STEP 3 — AND THE CONSEQUENCE THE CORPUS CARES ABOUT: HOW FAST DOES kappa VANISH?
  O5 established kappa = f'(r_h)/2 -> 0 at the forced member.  The fold says HOW FAST.
""")
al=sp.Symbol('alpha', positive=True)
f=1-2*M/r-r**2/al**2
kap=sp.simplify(sp.diff(f,r)/2)
print("  kappa = f'(r_h)/2, and f'(r_h) is proportional to h'(r_h) up to a positive factor;")
print("  at a fold h'(r) ~ h''(r_c)(r - r_c) ~ sqrt(delta).")
print("  VERIFY on the exact f:")
for d in [1e-2,1e-3,1e-4,1e-5,1e-6]:
    m2=m2c-d; rts=roots(m2); inner=sorted([x for x in rts if x>0])
    rh=inner[0]   # black-hole horizon
    Mv=m2/2
    kv=float(sp.diff(f,r).subs([(M,Mv),(al,1),(r,rh)]))/2
    print(f"     delta={d:<9.1e}  r_h={rh:.8f}  kappa={kv:+.8f}   kappa/sqrt(delta)={kv/np.sqrt(d):+.6f}")
print("  *** kappa VANISHES AS THE SQUARE ROOT OF THE DISTANCE FROM NARIAI, and the exponent is")
print("      FORCED BY THE FOLD -- it is not a feature of this cubic but of the collision type. ***")
print("="*80)

# =============================================================================================
# r2376+c54.161 -- ASSERTIONS.  The fold conditions and both scaling tables were printed and read
# by eye; "the ratio converges" was an invitation.  Pinned here: h(r_c) = h'(r_c) = 0 with
# h''(r_c) = 2 sqrt3 (the fold's three conditions, exactly), the additive unfolding dh/d(2M) = 1,
# and BOTH ratios at delta = 1e-6 against the numbers the table prints -- 1.519672 and 2.281510.
# Each is then checked against the coefficient the NORMAL FORM predicts, which is the content of
# the claim that the exponent is forced by the collision type and not by this cubic:
#     gap   -> 2 sqrt(2 delta / h''(r_c)) = 2 . 3^(-1/4) sqrt(delta) = 1.5196714 sqrt(delta)
#     kappa -> h''(r_c)|r_h - r_c| / r_c   / 2 = 3^(3/4) sqrt(delta) = 2.2795071 sqrt(delta)
assert sp.simplify(h.subs([(M, Mc), (r, rc)])) == 0
assert sp.simplify(sp.diff(h, r).subs([(M, Mc), (r, rc)])) == 0
assert sp.simplify(sp.diff(h, r, 2).subs(r, rc) - 2*sp.sqrt(3)) == 0        # fold, not cusp
assert sp.simplify(sp.diff(h, M)/2 - 1) == 0                               # additive unfolding
assert sp.simplify(sp.diff(sp.diff(h, M), r)) == 0                         # and r-independent
assert abs(d - 1e-6) < 1e-18                                               # the last table row
assert abs(gap/np.sqrt(d) - 1.519672) < 1e-5                               # the printed ratio
assert abs(gap/np.sqrt(d) - 2*3**(-0.25)) < 1e-5                           # = the normal form's
assert abs(kv/np.sqrt(d) - 2.281510) < 1e-5                                # the printed ratio
assert abs(kv/np.sqrt(d) - 3**0.75) < 5e-3                                 # -> 3^(3/4), from below
assert abs(rh - 1/np.sqrt(3)) < 1e-3 and rh < 1/np.sqrt(3)                 # approaching r_c
# the exponent itself, from two decades: halving is sqrt(10) apart, so the ratio must be flat
gap_a = (lambda rr: max(rr) - min(rr))([x for x in roots(m2c - 1e-4) if x > 0])
gap_b = (lambda rr: max(rr) - min(rr))([x for x in roots(m2c - 1e-8) if x > 0])
assert abs(gap_a/np.sqrt(1e-4) - gap_b/np.sqrt(1e-8)) < 1e-4               # exponent = 1/2 exactly
# CONTROL: past the fold (2M above 2M_c) the two positive roots are GONE -- the collision is a
# saddle-node annihilation, not a pitchfork or a transcritical crossing.
assert len([x for x in roots(m2c + 1e-3) if x > 0]) == 0
assert len([x for x in roots(m2c - 1e-3) if x > 0]) == 2
print("  [r2376+c54.161] asserted: h = h' = 0 with h'' = 2 sqrt3 at r_c, gap/sqrt(delta) =")
print("  1.519672 = 2.3^(-1/4) and kappa/sqrt(delta) = 2.281510 -> 3^(3/4), the exponent flat")
print("  across four decades, and no positive root above the fold.")
