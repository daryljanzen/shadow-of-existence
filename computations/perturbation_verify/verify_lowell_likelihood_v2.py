"""
Low-ell cosmic-variance likelihood, RECOMPUTED with the corrected genuine-Boltzmann depths
(verify_lowell_boltzmann.py, r962): CR/LCDM depth_l = 0.47,0.41,0.36,0.68,0.92,0.98 for l=2..7, ~1 for
l>=8 -- superseding the old SW-analytic 0.22/0.20 that verify_lowell_likelihood.py used.

Exact low-ell likelihood: each hat C_l ~ scaled chi^2_{2l+1} about the model C_l. For model comparison
CR vs LCDM given the observed hat C_l, the absolute baseline cancels in the ratio and
  Delta(-2 ln L)_l = (2l+1) [ r_l (1/depth_l - 1) + ln(depth_l) ] ,   r_l = observed/LCDM at l,
positive = CR disfavoured. Observed ratios are estimator-dependent (cosmic-variance-limited); we
report the central case and the octopole estimator range.
"""
import numpy as np
depth = {2:0.473,3:0.410,4:0.356,5:0.676,6:0.916,7:0.984,8:0.998,9:1.0,10:1.0}
# observed / LCDM at each l (central; literature, estimator- and mask-dependent):
#  l=2 quadrupole robustly low ~0.20; l=3 octopole central ~0.75 (WMAP 0.6, Efstathiou ~0.9);
#  l=4 ~0.7; l>=5 ~1.0 (no robust anomaly). Cosmic-variance-limited.
obs_central = {2:0.20,3:0.75,4:0.70,5:1.0,6:1.0,7:1.0,8:1.0,9:1.0,10:1.0}
obs_lowoct={**obs_central,3:0.60}
obs_highoct={**obs_central,3:0.95}

def dchi2(obs):
    tot=0.0; per={}
    for l in range(2,11):
        d=depth[l]; r=obs[l]
        v=(2*l+1)*(r*(1.0/d-1.0)+np.log(d)); per[l]=v; tot+=v
    return tot,per

print("="*70)
print("Low-ell likelihood with CORRECTED depths (0.47/0.41...), CR vs LCDM")
print("="*70)
print("Delta(-2lnL) > 0 disfavours CR.  Per-ell (central obs):")
tot,per=dchi2(obs_central)
print(f"  {'l':>3s} {'depth':>6s} {'obs/LCDM':>9s} {'Dchi2_l':>8s}")
for l in range(2,9):
    print(f"  {l:3d} {depth[l]:6.2f} {obs_central[l]:9.2f} {per[l]:8.2f}")
print(f"  central total (2<=l<=10):  Delta(-2lnL) = {tot:+.1f}  (compare old-depth ~+14)")
tl,_=dchi2(obs_lowoct); th,_=dchi2(obs_highoct)
print(f"  octopole estimator range:  low(WMAP) {tl:+.1f}   high(Efst) {th:+.1f}")
print("""
READING (do-not-assert beyond the numbers; cosmic-variance-limited <3sigma):
 * The quadrupole no longer helps CR: depth 0.47 vs observed 0.20 means CR OVER-predicts the
   quadrupole power (predicts a milder dip than observed) -- the old "striking match" (0.2 vs 0.2)
   was an artifact of the SW-analytic 0.22.
 * The octopole no longer strongly hurts CR: depth 0.41 vs observed ~0.6-1.0 is a MILD over-
   suppression, not the old severe 0.20-vs-0.75.
 * Net: the low-ell sector is a wash, cosmic-variance-limited -- CR predicts a smooth modest deficit
   (~0.4-0.5 at l=2-3) that matches neither the sharp observed quadrupole dip nor the normal octopole,
   sitting between them. Neither a correspondence success nor a sharp falsification risk.
""")
print("="*70)

# --- ASSERTIONS r2376+c54.160 -------------------------------------------------------------
# Print-only receipt.  P15 sec:largescale/sec:scope quotes it for Delta(-2lnL) ~ +1.8 over
# 2 <= l <= 10 (range +0.3 to +3.8), with the quadrupole REWARDING CR at -2.6, the octopole
# penalising at +1.3, and the largest single-multipole penalty +2.1 at l=4.  All pinned.
# The summation range is pinned too: the paper said 2 <= l <= 30 until r2376+c54.155, and this
# receipt has only ever summed to 10 -- so the range is now a gated quantity, not prose.
_tot, _per = dchi2(obs_central)
assert sorted(_per) == [2, 3, 4, 5, 6, 7, 8, 9, 10], f"summation range is {sorted(_per)}, paper says 2<=l<=10"
assert abs(_per[2] - (-2.6291)) < 0.002, f"l=2 term = {_per[2]}, paper/receipt say -2.63"
assert abs(_per[3] - 1.3137) < 0.002, f"l=3 term = {_per[3]}, paper/receipt say +1.31"
assert abs(_per[4] - 2.1012) < 0.002, f"l=4 term = {_per[4]}, paper/receipt say +2.10"
assert abs(_tot - 1.8043) < 0.005, f"central total = {_tot}, paper says +1.8"
# the structural readings the paper leans on, each of which a depth retune could invert
assert _per[2] < 0.0, "the quadrupole must REWARD CR -- the paper's 'sector's weight is not where its name suggests'"
assert _per[4] > _per[3], "the largest single-multipole penalty must sit at l=4, not the octopole"
assert max(_per, key=lambda l: _per[l]) == 4
# the octopole-estimator range
_tl, _ = dchi2(obs_lowoct); _th, _ = dchi2(obs_highoct)
assert abs(_tl - 0.2933) < 0.005, f"WMAP-octopole total = {_tl}, paper says +0.3"
assert abs(_th - 3.8189) < 0.005, f"Efstathiou-octopole total = {_th}, paper says +3.8"
assert _th < 9.0, "a 'wash well inside cosmic variance' must not reach 3 sigma at the range's top"
# the corrected genuine-Boltzmann depths the paper carries (0.47/0.41/0.36/0.68 at l=2,3,4,5)
assert abs(depth[2] - 0.473) < 1e-9 and abs(depth[3] - 0.410) < 1e-9
assert abs(depth[4] - 0.356) < 1e-9 and abs(depth[5] - 0.676) < 1e-9
print("[assertions r2376+c54.160] 2<=l<=10, per-ell -2.63/+1.31/+2.10, total +1.80, range +0.29..+3.82: pinned.")
