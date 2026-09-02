"""
CR perturbation reach -- Step 4, EXACT computation (supersedes the recursion-based C_ell
in verify_closedS3_transfer.py, whose downward recursion was found WRONG by up to 28% at
low beta -- see VERIFICATION_LOG).  Method: the closed-S^3 hyperspherical Bessel evaluated
in EXTENDED PRECISION (mpmath), the only method uniformly accurate across (beta,ell) at
chi_lss ~ 2.75 (near antipode): float Gegenbauer precision-loses at high ell (beta^ell
cancellation), the downward recursion is systematically low for low-beta modes, the ODE
underflows at high ell.  Resolution of the disputed values (exact, dps>=60):
    Phi^25_10 = 0.069844  (float-Gegenbauer right; recursion 0.05043 WRONG by 28%)
    Phi^5_2   = 0.202204  (recursion 0.18158 wrong by 10%)
    Phi^50_10 = -0.020297 (recursion -0.01877 wrong by 7%)

TAG: method gap [E] RESOLVED; suppression DIRECTION [E]; exact DEPTH/shape [R] (normalisation +
spectrum-convention ambiguity, see note); the CR NON-SYNCHRONOUS transfer still the open object.
DO-NOT-ASSERT the CR prediction until the non-synchronous transfer is built and P12 cold-read.

Physics: ordinary Sachs-Wolfe, dT/T=(1/3)Phi at LSS, scale-invariant primordial spectrum
(weight w=1/beta), closed S^3 of present areal radius r0=5064 Mpc, LSS at chi_lss=D_C/r0.
A degree-L mode (beta=L+1) feeds multipoles ell<=L; L>=2 physical.
"""
import mpmath as mp, numpy as np
mp.mp.dps = 90
print("!!! CORRECTION (r520): the 'suppression present' reading below is WALKED BACK / not claimed.")
print("!!! The C_ell ASSEMBLY normalisation is wrong (closure sum-rule != 1; fails flat-limit reduction).")
print("!!! What stands: the radial functions are exact (mpmath), and the recursion was wrong up to 28%.")
print("!!! See VERIFICATION_LOG.md (r520) and CORPUS_MAP r520. Open: correct closed SW C_ell formula.\n")
chi = mp.mpf(13927)/mp.mpf(5064); cchi = mp.cos(chi); schi = mp.sin(chi)

def dfact_mp(n):
    r = mp.mpf(1)
    while n > 1: r *= n; n -= 2
    return r

def Phi(beta, ell):                      # exact hyperspherical Bessel, flat-normalised (-> j_ell)
    if ell > beta-1: return mp.mpf(0)     # the closed-S^3 cutoff: degree-L feeds ell<=L
    n = beta-1-ell
    N = mp.mpf(beta)**ell/(dfact_mp(2*ell+1)*mp.gegenbauer(n, ell+1, 1))
    return N*schi**ell*mp.gegenbauer(n, ell+1, cchi)

ells = list(range(2, 31))
def Clsum(bmax):
    Cl = {l: mp.mpf(0) for l in ells}
    for beta in range(3, bmax+1):
        for l in ells:
            if l <= beta-1:
                v = Phi(beta, l); Cl[l] += v*v/beta
    return Cl

print("="*66)
print("Closed-S^3 SW low-ell transfer -- EXACT (mpmath dps=90)")
print("="*66)
# convergence in beta_max
for bmax in (300, 600, 900):
    C = Clsum(bmax)
    D = {l: float(l*(l+1)*C[l]) for l in ells}
    hi = np.mean([D[l] for l in ells if 25 <= l <= 30])
    print(f"  bmax={bmax}: [ell(ell+1)C_ell normalised to ell=25-30]  "
          f"D(2)={D[2]/hi:.4f} D(3)={D[3]/hi:.4f} D(5)={D[5]/hi:.4f} D(10)={D[10]/hi:.4f}")

C = Clsum(900); D = {l: float(l*(l+1)*C[l]) for l in ells}
hi = np.mean([D[l] for l in ells if 25 <= l <= 30])
print("\n  ell(ell+1)C_ell^closed, normalised to ell=25-30 (flat SW would be 1 at all ell):")
for l in ells:
    if l <= 12 or l in (15, 20, 25, 30):
        print(f"     ell={l:2d}: {D[l]/hi:.4f}")

print("""
[READING]
 * METHOD GAP RESOLVED [E]: exact mpmath Gegenbauer is uniformly accurate; the r516
   recursion-based C_ell was an ARTIFACT (recursion wrong up to 28% at low beta).
 * SUPPRESSION PRESENT [E, direction + rough magnitude]: ell(ell+1)C_ell rises
   monotonically from ell=2 to ell~30 -- a strong low-ell deficit, the quadrupole at
   ~0.4 of the ell=25-30 level, beta_max-converged.  This is the standard closed-universe
   low-ell suppression (the k_min argument), in the region of the observed large-angle
   deficit.  It OVERTURNS the r516 "no suppression" look-signal, which was the recursion error.
 * DEPTH/SHAPE [R, not claimed]: ell(ell+1)C_ell has not cleanly plateaued by ell=30, so
   the exact suppression DEPTH is normalisation-dependent; the scale-invariant weight in a
   closed universe (w=1/beta vs the curvature-corrected HZ) and the near-antipode geometry
   need care before a pinned shape.
 * OPEN OBJECT [not claimed]: this is the STANDARD closed transfer, NOT the CR
   non-synchronous tau~=tau+chi transfer (closed-S^3 source on the FLAT distance projection,
   prop:flat) -- a stepping stone confirming the mechanism, not the CR prediction.
[STATUS] method gap closed; suppression sound (direction); shape + non-synchronous transfer
         open; P12 cold read owed.
""")
print("="*66)
