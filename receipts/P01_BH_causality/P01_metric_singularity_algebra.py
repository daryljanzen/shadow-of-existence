"""
P01_metric_singularity_algebra.py -- verifies: the algebraic half of the metric-singularity argument
  -- along a generator of H+ the surviving time-coefficient is FORCED to vanish at r=r_h in every chart,
  and the two invariant separations (Killing norm |zeta|^2, areal-gradient |grad r|^2=g^rr) vanish there.
  [P1 BH_causality_v2 sec:3]
STATUS: ✔✔   RUN: python3 P01_metric_singularity_algebra.py   RUNTIME: ~3s
COMPUTES: from the Schwarzschild (t,r) metric it (i) INVERTS to get g^{rr}; (ii) TRANSFORMS to ingoing
  Eddington-Finkelstein (v=t+r*, dr*=dr/f) and to Painleve-Gullstrand (dt=dT - sqrt(r_h/r)/f dr) by
  substitution+expansion, deriving g_vv and g_TT (NOT asserting them); (iii) forms |zeta|^2=g(d_t,d_t).
  Checks each derived coefficient vanishes at r_h. CONTROL: each is nonzero at r=2 r_h, and the EF/PG
  cross terms are the standard 2 dv dr / 2 sqrt(r_h/r) dT dr (so the transform is real, not rigged).
BOUND: verifies only the ALGEBRAIC forcing (sec:3). The metric-singularity THEOREM and the causal-
  alignment PROPOSITION/LEMMA (sec:5) are analytic proofs, not computational claims -- out of receipt scope.
ORIGIN: built new r1334 (P1 cited no receipts).
"""
import sympy as sp
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
r, rh = sp.symbols('r r_h', positive=True)
f = 1 - rh/r
dt,dv,dT,dr = sp.symbols('dt dv dT dr', real=True)
print("="*72); print("P01 metric-singularity algebra -- coefficients DERIVED, not asserted"); print("="*72)

# (i) invert the (t,r) block g=diag(-f, 1/f): g^{rr} = 1/g_rr
g_static = sp.diag(-f, 1/sp.Rational(1)*  (1/f))
grr_up = sp.simplify((g_static.inv())[1,1])      # = f, by inversion
ok&=check("INVERT g: g^{rr} = 1/g_rr = f = (1-r_h/r)", sp.simplify(grr_up - f)==0)
ok&=check("|grad r|^2 = g^{rr} vanishes at r_h", sp.simplify(grr_up.subs(r,rh))==0)
ok&=check("  CONTROL g^{rr} != 0 at 2 r_h", sp.simplify(grr_up.subs(r,2*rh))!=0)

# (ii) EF: v = t + r*, dr*=dr/f => dt = dv - dr/f. Substitute into ds^2 = -f dt^2 + dr^2/f.
dt_EF = dv - dr/f
ds2_EF = sp.expand(-f*dt_EF**2 + dr**2/f)
g_vv = sp.simplify(ds2_EF.coeff(dv,2)); cross_EF = sp.simplify(ds2_EF.coeff(dv,1).coeff(dr,1)); drr_EF = sp.simplify(ds2_EF.coeff(dr,2))
ok&=check("EF transform -> g_vv = -f (derived), cross = 2 dv dr, dr^2 cancels",
          sp.simplify(g_vv+f)==0 and sp.simplify(cross_EF-2)==0 and sp.simplify(drr_EF)==0)
ok&=check("EF g_vv vanishes at r_h", sp.simplify(g_vv.subs(r,rh))==0)

# (iii) PG: dt = dT - sqrt(r_h/r)/f dr. Substitute.
dt_PG = dT - sp.sqrt(rh/r)/f*dr
ds2_PG = sp.expand(-f*dt_PG**2 + dr**2/f)
g_TT = sp.simplify(ds2_PG.coeff(dT,2)); cross_PG = sp.simplify(ds2_PG.coeff(dT,1).coeff(dr,1)); drr_PG = sp.simplify(ds2_PG.coeff(dr,2))
ok&=check("PG transform -> g_TT = -f (derived), cross = 2 sqrt(r_h/r), g_rr = 1",
          sp.simplify(g_TT+f)==0 and sp.simplify(cross_PG-2*sp.sqrt(rh/r))==0 and sp.simplify(drr_PG-1)==0)
ok&=check("PG g_TT vanishes at r_h (finite Delta T annihilated)", sp.simplify(g_TT.subs(r,rh))==0)

# Killing norm and the forcing
zeta_norm = g_static[0,0]                          # |zeta|^2 = g(d_t,d_t) = -f
ok&=check("Killing norm |zeta|^2 = -f vanishes at r_h", sp.simplify(zeta_norm.subs(r,rh))==0)
ok&=check("  CONTROL |zeta|^2 != 0 at 2 r_h", sp.simplify(zeta_norm.subs(r,2*rh))!=0)
dtv=sp.symbols('dt_nz', nonzero=True)
ok&=check("null-generator reduction: ds^2 = |zeta|^2(r_h) dt^2 = 0 with dt!=0 => coefficient forced 0",
          sp.simplify(zeta_norm.subs(r,rh)*dtv**2)==0)
print("="*72)
print("RESULT:", "ALL PASS -- g^{rr} (inversion), g_vv (EF), g_TT (PG) DERIVED and each vanishes at r_h;\n         cross terms are the standard ones (transform genuine); |zeta|^2 and |grad r|^2 vanish; controls\n         nonzero at 2 r_h." if ok else "SOME FAILED")
print("="*72)

# --- ASSERTIONS (added r2376+c54.158) --------------------------------------------------------
# sec:3's claim is an EXACT algebraic forcing (the file prints no numeric figure), so these are
# exact zeros: every derived time-coefficient vanishes at r_h, in all three charts, and the
# controls at r=2 r_h are not merely nonzero but the definite values +-1/2.
# (a) the file's own PASS/FAIL boolean.
assert ok, "P01 metric-singularity algebra: at least one derived coefficient check FAILED"
# (b) the forcing: g^rr (inversion), g_vv (EF), g_TT (PG) and |zeta|^2 all vanish at r=r_h.
assert sp.simplify(grr_up.subs(r, rh)) == 0
assert sp.simplify(g_vv.subs(r, rh)) == 0
assert sp.simplify(g_TT.subs(r, rh)) == 0
assert sp.simplify(zeta_norm.subs(r, rh)) == 0
# (c) CONTROL at r=2 r_h: f=1/2, so g^rr=+1/2 and |zeta|^2=-1/2 -- nonzero, and pinned.
assert sp.simplify(grr_up.subs(r, 2*rh) - sp.Rational(1, 2)) == 0
assert sp.simplify(zeta_norm.subs(r, 2*rh) + sp.Rational(1, 2)) == 0
# (d) the transforms are genuine, not rigged: EF cross term 2 dv dr with dr^2 cancelling, and
#     PG cross term 2 sqrt(r_h/r) with g_rr = 1.
assert sp.simplify(cross_EF - 2) == 0 and sp.simplify(drr_EF) == 0
assert sp.simplify(cross_PG - 2*sp.sqrt(rh/r)) == 0 and sp.simplify(drr_PG - 1) == 0
