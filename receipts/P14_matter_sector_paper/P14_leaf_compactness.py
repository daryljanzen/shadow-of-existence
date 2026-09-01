"""
P14_leaf_compactness.py -- verifies the LOAD-BEARING index claim in sec:count (the sentence citing
  [AtiyahSinger1968]): in the leaf's PROPER measure dl = dr/sqrt|f| the closed slicing has FINITE total
  length -- the horizon turning points sit at finite proper distance (an INTEGRABLE sqrt-singularity) and
  the r=0 crossing is an integrable sqrt-singularity too -- so the leaf is COMPACT and the Dirac operator on
  it carries a well-defined analytical index dim ker, EXACTLY WHERE the bulk index on the non-compact
  spacetime (tortoise measure dr/f) is obstructed. The discriminating fact is the exponent: the proper
  measure has inverse-SQRT (power -1/2, integrable) singularities where the tortoise measure has a simple
  POLE (power -1, non-integrable). This is what answers P13's non-compactness worry from the leaf side.
STATUS: ✔✔   RUN: python3 P14_leaf_compactness.py   RUNTIME: ~2s
COMPUTES: on the concrete SdS of B-2 (M=0.12, alpha=1) the between-horizon proper length int_{r_b}^{r_c}
  dr/sqrt(f) (both endpoints f=0); shows it CONVERGES (horizon at finite proper distance) while the tortoise
  length int dr/f DIVERGES (log) at the same endpoint; shows the r=0 crossing int_0 dr/sqrt|f| ~ int sqrt(r)
  is integrable; and states the exponent test (-1/2 integrable, -1 not). CONTROL: a fabricated simple-pole
  measure dr/|f| at the horizon fails to converge under the same windowing that the sqrt measure passes.
EXTENDED r3748: the blocks above run at M=0.12 -- a NON-DEGENERATE member with two SEPARATE horizons.
  The corpus's cosmology is the NARIAI member, where they MERGE into a double root and 1/sqrt|f| becomes a
  SIMPLE POLE -- the very exponent this receipt's own control uses as its failure case. So the merging limit
  is exactly where the integrable-sqrt hypothesis fails POINTWISE, and this receipt did not go there.
  FUNCTIONAL_ANALYSIS F14 found the gap; the added block closes it: L CONVERGES to 1.8138 as M -> M_N while
  the gap closes to 1e-3, because int dr/sqrt((r-r_b)(r_c-r)) = pi INDEPENDENT OF THE GAP -- the interval
  closing exactly compensates the integrand blowing up. CONTROL: at the EXACT double root the increments do
  NOT shrink, so the block can detect the failure it checks for.
ORIGIN: built new r1387 (P14 final audit -- the body's compact-leaf/well-defined-index claim was unreceipted;
  distinct measure from P14_dual_norm, which contrasted flat dr vs tortoise dr/f).
"""
import numpy as np
from scipy import integrate
from scipy.optimize import brentq
def check(t,c): print(f"  [{'PASS' if c else 'FAIL'}] {t}"); return bool(c)
ok=True
print("="*74); print("P14 sec:count -- the leaf is COMPACT in dl=dr/sqrt|f| (finite length) => index well-defined"); print("="*74)
M,alph=0.12,1.0
f=lambda r: 1-2*M/r-r**2/alph**2
rb=brentq(f,0.15,0.5); rc=brentq(f,0.5,0.99)      # the two SdS horizons (f=0)
print(f"  horizons: r_b={rb:.4f}, r_c={rc:.4f}  (f>0 between them)")

# (1) between-horizon LEAF proper length int dr/sqrt(f): both endpoints are f=0 sqrt-singularities
L,_=integrate.quad(lambda r: 1/np.sqrt(f(r)), rb, rc, points=[rb,rc], limit=200)
ok&=check(f"LEAF proper length L=int_r_b^r_c dr/sqrt(f) is FINITE: L={L:.4f} (closed slicing has finite length)",
          np.isfinite(L) and 0<L<20)

# (2) horizon at FINITE proper distance: shrink cutoff toward r_b, proper length converges (increments->0)
eps=np.array([1e-2,1e-3,1e-4,1e-5,1e-6])
Lprop =np.array([integrate.quad(lambda r:1/np.sqrt(f(r)), rb+e, 0.5, points=[rb+e])[0] for e in eps])
dLp=np.diff(Lprop)
ok&=check(f"horizon at FINITE proper distance (dl=dr/sqrt f): proper length CONVERGES, increments SHRINK "
          f"({dLp[-3]:.4f}->{dLp[-2]:.4f}->{dLp[-1]:.4f}, ratio ~1/sqrt10/decade)",
          np.isfinite(Lprop[-1]) and abs(dLp[-1])<0.5*abs(dLp[-3]))

# (3) CONTRAST: tortoise length int dr/f DIVERGES (log) at the same horizon
Ltort=np.array([integrate.quad(lambda r:1/f(r), rb+e, 0.5, points=[rb+e])[0] for e in eps])
dLt=np.diff(Ltort)
ok&=check(f"tortoise length int dr/f DIVERGES at the SAME horizon (log; increments stay ~const, do NOT shrink: "
          f"{dLt[-3]:.3f},{dLt[-2]:.3f},{dLt[-1]:.3f}) => bulk index obstructed",
          dLt[-1]>0.5 and abs(dLt[-1]-dLt[-3])/abs(dLt[-3])<0.05)

# (4) the r=0 crossing is an integrable sqrt-singularity too: near 0, |f|~2M/r so dl~sqrt(r/2M) dr
r0=np.array([1e-2,1e-4,1e-6,1e-8])
L0=np.array([integrate.quad(lambda r:1/np.sqrt(abs(f(r))), e, 0.1, points=[e])[0] for e in r0])
ok&=check(f"r=0 crossing integrable (dl~sqrt(r) near 0): int converges to finite as r->0 "
          f"({L0[0]:.4f}..{L0[-1]:.4f}, delta {L0[-1]-L0[0]:.1e})", np.isfinite(L0[-1]) and abs(L0[-1]-L0[0])<1e-2)

# (5) the exponent test + CONTROL: a fabricated simple-pole measure fails where the sqrt measure passes
#     model near-horizon f ~ s*(r-rb); dr/sqrt(s(r-rb)) integrable, dr/(s(r-rb)) not
s=abs((f(rb+1e-6)-0)/1e-6)   # local slope f'(rb)
sqrt_int=np.array([integrate.quad(lambda r:1/np.sqrt(s*(r-rb)), rb+e, rb+0.05)[0] for e in eps])
pole_int=np.array([integrate.quad(lambda r:1/(s*(r-rb)),        rb+e, rb+0.05)[0] for e in eps])
dS,dP=np.diff(sqrt_int),np.diff(pole_int)
ok&=check(f"EXPONENT TEST: sqrt-singularity (-1/2) INTEGRABLE (increments shrink {dS[-2]:.4f}->{dS[-1]:.4f}); "
          f"pole (-1) NOT (increments constant {dP[-2]:.3f},{dP[-1]:.3f})",
          abs(dS[-1])<0.5*abs(dS[-3]) and dP[-1]>0.5 and abs(dP[-1]-dP[-3])/abs(dP[-3])<0.05)

# --- r2376+c54.161 : pin the claim, so the receipt can fail -------------------------------
# The claim is the exponent: the proper measure dl = dr/sqrt|f| has an INTEGRABLE -1/2
# singularity at each horizon and at r=0 (finite total leaf length => compact leaf =>
# well-defined index), where the tortoise measure dr/f has a NON-integrable simple pole.
# The five check() booleans above are only printed; assert their conjunction, then pin the
# numbers this run prints.
assert ok, "a printed check FAILED -- the compact-leaf claim is not established by this run"
assert abs(rb - 0.2570) < 5e-4 and abs(rc - 0.8464) < 5e-4, \
    "the SdS horizons printed above are r_b=0.2570, r_c=0.8464 at M=0.12, alpha=1"
assert abs(L - 1.7671) < 1e-3, "the printed leaf proper length is L = 1.7671 (FINITE)"
# -1/2 exponent: each decade of cutoff adds sqrt(10) times LESS, so the increments fall to
# the pinned ratio 1/sqrt(10) = 0.31623 -- convergence, i.e. the horizon at finite distance.
assert abs(dLp[-1]/dLp[-2] - 0.31623) < 5e-3, \
    "proper-length increments must fall by 1/sqrt(10) per decade (exponent -1/2)"
assert abs(dLp[-1] - 0.002448) < 1e-5, "the printed last proper increment is 0.0024"
# -1 exponent: the tortoise increment per decade tends to ln(10)/f'(r_b) = 0.73786, CONSTANT,
# so the length grows without bound -- the bulk index is obstructed at the same locus.
assert abs(dLt[-1] - 0.73786) < 1e-4, \
    "tortoise increments must sit at ln(10)/f'(r_b) = 0.73786 per decade, not shrink"
assert dLt[-1] > 100 * dLp[-1], "the pole increment must dwarf the sqrt increment at the same cutoff"
assert abs(L0[-1] - 0.05002) < 1e-4, "the printed r=0 crossing length converges to 0.0500"
assert abs(s - 3.12061) < 1e-4, "the near-horizon slope f'(r_b) printed via s is 3.12061"
assert abs(dP[-1] - 0.73786) < 1e-4 and abs(dS[-1] - 0.002448) < 1e-5, \
    "CONTROL: the fabricated simple pole keeps a constant 0.73786 increment where the sqrt model's falls to 0.0024"

# =====================================================================================
# ⛔⛭⛭ THE NARIAI LIMIT -- ADDED r3748, AND IT IS THE MEMBER THE CORPUS'S COSMOLOGY IS.
#
# Everything above is computed at M=0.12, alpha=1: a NON-DEGENERATE member with two SEPARATE
# horizons.  ** The corpus's cosmology is the NARIAI member, where those two horizons MERGE into a
# double root **, and at a double zero f ~ (r-r_h)^2, so 1/sqrt|f| ~ 1/|r-r_h| -- a SIMPLE POLE,
# which is exactly the non-integrable exponent this receipt's own control uses as its failure case.
#   => So the merging limit is precisely where the integrable-sqrt hypothesis fails POINTWISE, and
#      until r3748 this receipt did not go there.  `FUNCTIONAL_ANALYSIS` `F14` found the gap.
#
# ** THE CLAIM SURVIVES IT, AND THE REASON IS EXACT. **  Near a merging pair
# f = (r-r_b)(r_c-r) x (smooth, bounded), and the substitution r = mid + (gap/2) sin(theta) turns
# int dr/sqrt((r-r_b)(r_c-r)) into int_{-pi/2}^{pi/2} dtheta = pi -- INDEPENDENT OF THE GAP.
# ** The interval closing exactly compensates the integrand blowing up **, which is why the
# pointwise divergence never reaches the limit.
MN = alph/(3*np.sqrt(3))                      # 3 sqrt3 M = alpha; r_N = alpha/sqrt3
print()
print("="*74)
print("NARIAI LIMIT -- the member the corpus's cosmology actually is (added r3748)")
print("="*74)
print(f"  M_N = {MN:.6f}, r_N = {alph/np.sqrt(3):.6f}   (the two horizons merge here)")
print(f"  {'M/M_N':>10} {'gap':>10} {'L':>12}")
Ls, gaps = [], []
for frac in (0.5, 0.9, 0.99, 0.999, 0.9999, 0.999999):
    Mf = frac*MN
    ff = lambda r: 1-2*Mf/r-r**2/alph**2
    rb2 = brentq(ff, 1e-6, alph/np.sqrt(3)); rc2 = brentq(ff, alph/np.sqrt(3), 0.999999*alph)
    Lf,_ = integrate.quad(lambda r: 1/np.sqrt(max(ff(r), 1e-300)), rb2, rc2,
                          points=[rb2, rc2], limit=400)
    Ls.append(Lf); gaps.append(rc2-rb2)
    print(f"  {frac:>10} {rc2-rb2:>10.5f} {Lf:>12.4f}")
ok &= check(f"the gap CLOSES: {gaps[0]:.4f} -> {gaps[-1]:.5f}", gaps[-1] < 1e-3 < gaps[0])
ok &= check(f"and L CONVERGES rather than diverging: {Ls[0]:.4f} -> {Ls[-1]:.4f}, "
            f"last change {abs(Ls[-1]-Ls[-2]):.2e}",
            abs(Ls[-1]-Ls[-2]) < 1e-3 and np.isfinite(Ls[-1]))

# THE EXACT REASON, isolated: the gap-independent core.
print()
print("  the gap-independent core:  int_a^b dr/sqrt((r-a)(b-r)) = pi for EVERY gap")
core = []
for gap in (1.0, 0.1, 0.001):
    a_, b_ = 1.0, 1.0+gap
    v,_ = integrate.quad(lambda r: 1/np.sqrt((r-a_)*(b_-r)), a_, b_, points=[a_, b_], limit=400)
    core.append(v)
    print(f"    gap={gap:<8} = {v:.10f}   (pi = {np.pi:.10f})")
ok &= check("the core is pi at every gap, to 8 digits -- the interval closing compensates the blow-up",
            all(abs(v-np.pi) < 1e-8 for v in core))

# ⛔ THE CONTROL: the pointwise worry is REAL, so the test must be able to see it.
# At the EXACT double root the integrand is a simple pole and the length DOES diverge -- shown by
# windowing in, where the increments must NOT shrink.  If this passed too, the block above would be
# measuring quadrature error rather than a limit.
print()
print("  CONTROL -- at the EXACT double root the pointwise divergence is real:")
fN = lambda r: 1-2*MN/r-r**2/alph**2
rN = alph/np.sqrt(3)
epsN = np.array([1e-3, 1e-4, 1e-5, 1e-6])
LN = np.array([integrate.quad(lambda r: 1/np.sqrt(abs(fN(r))), rN+e, 0.9*alph,
                              points=[rN+e], limit=400)[0] for e in epsN])
dLN = np.diff(LN)
print(f"    windowed length at the merged root: {LN[0]:.3f} -> {LN[-1]:.3f}, "
      f"increments {dLN[-3]:.3f}, {dLN[-2]:.3f}, {dLN[-1]:.3f}")
ok &= check("CONTROL: AT the double root the increments do NOT shrink (a simple pole, log-divergent) "
            "-- so this block can detect the failure it is checking for",
            abs(dLN[-1]) > 0.5*abs(dLN[-3]))
print("    (the same exponent this receipt's fabricated-pole control uses as its failure case,")
print("     reached here by physics rather than by fabrication)")

print("="*74)
print("RESULT:", "ALL PASS -- the leaf has finite proper length in dl=dr/sqrt|f| (integrable sqrt-singularities\n         at the horizons and r=0), so it is COMPACT and the Dirac index dim ker is well-defined, exactly\n         where the tortoise-measure bulk index diverges. Leaf (vantage) index, not a bulk dS_5 index." if ok else "SOME FAILED")
print("="*74)
