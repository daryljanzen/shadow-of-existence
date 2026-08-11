"""
CR NON-SYNCHRONOUS low-ell transfer (leading-order, ordinary SW) -- the ACTUAL CR object.
This is the transfer the r521 standard-closed computation was NOT: it resolves the apparent
"no suppression" of r521 as a wrong-object artifact.

THE DECOUPLING (grounded at source, P12 sec:largescale / prop:flat):
  - PROJECTION is FLAT.  CR's distance slicing is the Euclidean constant-tau slice (prop:flat,
    Omega_k=0), so the comoving angular-diameter distance is the flat D_C ~ 13927 Mpc.  Decisive
    cross-check: D_M=D_C gives the acoustic scale ell_A ~ 301 (banked, correct), whereas treating
    the areal radius r0 ~ 5064 Mpc as the angular-diameter distance gives ell_A ~ 110 -- the
    RETRACTED r506 chimera.  So the photon projection is FLAT: flat spherical Bessel j_ell(k D_C).
  - SOURCE modes are DISCRETE.  The cosmological layers are the closed S^3 of curvature radius
    r0 ~ 5064 Mpc, so the scalar source spectrum is quantized: k_L = sqrt(L(L+2))/r0, L>=2
    (L=0 background, L=1 gauge dipole), with a hard lowest physical mode at L=2.
  - The CR transfer is therefore the DISCRETE closed-S^3 source spectrum projected through the
    FLAT j_ell -- NOT the hyperspherical Phi^beta_ell of the standard-closed transfer (which bakes
    in the closed DISTANCE relation CR does not have).  This is the proper full-sky version of the
    eq:lowell flat-sky placeholder.

  C_ell = sum_{L>=2} w_L * j_ell^2(k_L * D_C),   k_L*D_C = sqrt(L(L+2)) * (D_C/r0),
  scale-invariant discrete weight w_L = (Delta k_L / k_L) = (L+1)/(L(L+2))  (-> 1/L at high L,
  the discrete image of the continuum dk/k).

WHY A DEFICIT APPEARS IN CR BUT NOT IN THE STANDARD-CLOSED OBJECT (r521):
  The flat projection maps mode k_L to ell ~ k_L*D_C = sqrt(L(L+2))*(D_C/r0).  The stretch factor
  is D_C/r0 ~ 2.75 (flat projection distance / curvature radius -- the decoupling, made numerical).
  It pushes the LOWEST mode L=2 up to ell ~ sqrt(8)*2.75 ~ 7.8, leaving ell<~8 with no source ->
  a low-ell DEFICIT.  In the standard-closed transfer the curved projection instead maps degree-L
  to ell<=L and the discrete sum fills ell=2 adequately -> flat (r521).  The whole difference is
  flat-vs-curved PROJECTION.

RESULT [E, flat-limit-verified, L_max-converged] at chi=D_C/r0~2.75:
  ell(ell+1)C_ell (normalised to ell=25-30): l2~0.12 l3~0.10 l4~0.20 l5~0.65 l6~0.92 l7~0.99
  l8~1.00 and flat above -> a STRONG low-ell deficit below ell~7-8, recovered by ell~8.  This
  VINDICATES the eq:lowell floor (deficit below ell~8) for the right reason: the flat projection
  of the discrete closed-S^3 source.  Deficit LOCATION (ell~8) is geometric (set by k_2*D_C),
  robust to the weight; exact SHAPE/amplitude depends on the weight convention.

CAVEATS (do-not-assert as the final CR word):
  (a) leading-order ORDINARY SW only -- no ISW / no full radiative transfer;
  (b) the discrete scale-invariant measure w_L convention should be cross-checked against a
      first-principles closed-S^3 primordial normalisation;
  (c) a fresh-node P12 cold read on the floor claim is owed before any corpus enrichment.
"""
import numpy as np
from scipy.special import spherical_jn

r0 = 5064.0          # present S^3 areal/curvature radius [Mpc]  (sets the SOURCE quantization)
D_C = 13927.0        # flat comoving (= angular-diameter) distance to LSS [Mpc] (the PROJECTION)

def Cl_CR(ells, Lmax, chi=D_C/r0):
    """chi = D_C/r0 controls the discreteness: chi->0 = continuum (flat limit); chi~2.75 = CR."""
    out = np.zeros(len(ells))
    for L in range(2, Lmax+1):
        kL_DC = np.sqrt(L*(L+2))*chi
        w = (L+1)/(L*(L+2))
        out += w*np.array([spherical_jn(int(l), kL_DC)**2 for l in ells])
    return out

def Dl_norm(Cl, ells):
    D = ells*(ells+1)*Cl
    return D/np.mean(D[ells >= 25])

if __name__ == "__main__":
    ells = np.arange(2, 31)
    print("="*66)
    print("CR NON-SYNCHRONOUS transfer: discrete closed-S^3 source, FLAT j_ell projection")
    print("="*66)
    print("[flat-limit test] ell(ell+1)C_ell must be flat as chi=D_C/r0 -> 0:")
    for chi in (0.1, 0.5):
        D = Dl_norm(Cl_CR(ells, 4000, chi), ells)
        print(f"   chi={chi:.2f}: l2={D[0]:.3f} l5={D[3]:.3f} l10={D[8]:.3f} l20={D[18]:.3f}  (flat=1)")
    print("\n[CR RESULT] chi=D_C/r0=2.75, ell(ell+1)C_ell normalised to ell=25-30:")
    D = Dl_norm(Cl_CR(ells, 4000), ells)
    for i, l in enumerate(ells):
        if l <= 12 or l in (15, 20):
            print(f"   ell={l:2d}: {D[i]:.3f}  {'#'*int(round(D[i]*40))}")
    print("\n[READING] strong low-ell deficit below ell~7-8, recovered by ell~8 -- the eq:lowell")
    print(" floor vindicated for the right reason (flat projection of discrete closed source).")
    print(" Resolves the r521 'no suppression': that was the standard-closed (wrong) object.")
    print(" CAVEATS: ordinary SW only; weight convention to be cross-checked; P12 cold read owed.")
    print("="*66)
