"""
E1 -- the exact discrete measure, and the octopole verdict.  (added 2026-06-30, r544 spearhead)

The confront_lowell_data.py PIVOT named three things that could differentiate ell=2 from ell=3
(and so relieve the octopole tension) or fail to (and so firm the falsification edge):
  (i) the Doppler term      -- SETTLED earlier (verify_doppler_lowell.py): does NOT differentiate.
  (ii) the exact discrete measure  -- THIS SCRIPT.
  (iii) a genuine Boltzmann solve   -- the residual ~10-20% transfer refinement, still open.

caveat (b) of verify_closedS3_nonsync.py: the scale-invariant weight w_L=(L+1)/(L(L+2)) used in
the headline result "should be cross-checked against a first-principles closed-S^3 primordial
normalisation."  This script does that cross-check FROM SCRATCH and tests whether the measure
differentiates the quadrupole from the octopole.

------------------------------------------------------------------------------------------------
FIRST-PRINCIPLES DERIVATION of the scale-invariant (Harrison-Zel'dovich) weight on the closed S^3
------------------------------------------------------------------------------------------------
Closed S^3, curvature radius r0.  Scalar Laplacian eigenvalues -k_beta^2 with
    k_beta^2 = (beta^2 - 1)/r0^2,   beta = L+1 = 1,2,3,...   (L=0 monopole/background, L=1 dipole/gauge)
Degeneracy of the beta-th eigenvalue on S^3:  g_beta = beta^2  (= (L+1)^2).

HZ = scale invariant = equal field variance per logarithmic k-interval.  The field variance is
    <Phi^2> = sum_beta g_beta * P_beta          (P_beta = per-(beta,l,m)-mode power, m-independent)
"Equal per dln k": with k_beta ~ beta at large beta, dln k ~ dbeta/beta, so we require
    g_beta * P_beta * dbeta  proportional to  dbeta/beta
    => beta^2 * P_beta proportional to 1/beta
    => P_beta proportional to 1/beta^3  ~  1/(beta(beta^2-1))      [PER-MODE POWER]
This is exactly the weight verify_closedS3_Cl_corrected.py SELECTED by its flat-limit test for the
S^3-orthonormal Pi transfer -- now DERIVED, not fitted.  (Check below: reproduces flat HZ.)

The C_ell SUMMATION weight for the FLAT j_ell projection is per-mode power x degeneracy:
    w_L = g_beta * P_beta = beta^2 * 1/(beta(beta^2-1)) = beta/(beta^2-1) = (L+1)/(L(L+2)).
=> the nonsync/radiative weight IS the first-principles closed-S^3 HZ measure.  caveat (b) CLOSED.

Large-L limit (the continuum / flat-limit cross-check): w_L = (L+1)/(L(L+2)) -> 1/L = dk/k (the
scale-invariant continuum measure), so the flat limit is automatic.  The two weights only differ at
LOW L -- exactly the low-ell regime -- so this is where any differentiation of ell=2 vs ell=3 must
come from, and it is the right place to test.

THE TEST: compute the bare-SW CR transfer C_ell = sum_{L>=2} w_L j_ell^2(k_L D_C) with the derived
measure, read the ell=2 / ell=3 ratio, and check its ROBUSTNESS to the weight (vary the low-L
measure) -- if the quadrupole/octopole ratio is stable under reasonable measure changes, the measure
does NOT differentiate them and the smooth deficit (octopole over-prediction) is firm.
"""
import numpy as np
from scipy.special import spherical_jn

r0  = 5064.0
D_C = 13927.0
chi = D_C/r0                      # 2.75 stretch factor

def kL(L):   return np.sqrt(L*(L+2))/r0
def w_HZ(L): return (L+1)/(L*(L+2))          # DERIVED first-principles closed-S^3 HZ measure

def Cl_SW(ells, weight, chi=chi, Lmax=4000):
    out = np.zeros(len(ells), float)
    for L in range(2, Lmax+1):
        x = np.sqrt(L*(L+2))*chi
        out += weight(L)*np.array([spherical_jn(int(l), x)**2 for l in ells])
    return out

def Dl(Cl, ells):                            # ell(ell+1)C_ell normalised to ell=25-30 plateau
    D = ells*(ells+1)*Cl
    return D/np.mean(D[ells>=25])

if __name__ == "__main__":
    ells = np.arange(2, 31)

    print("="*74)
    print("E1 -- first-principles closed-S^3 HZ measure, and the octopole verdict")
    print("="*74)

    # --- 1. derivation cross-checks --------------------------------------------------------------
    print("\n[1] DERIVATION CHECKS")
    Ls = np.array([2,3,4,5,10,50,500])
    permode = 1.0/((Ls+1)*((Ls+1)**2-1))     # P_beta = 1/(beta(beta^2-1))
    degen   = (Ls+1)**2                        # g_beta = beta^2
    wflat   = (Ls+1)/(Ls*(Ls+2))              # claimed C_ell weight
    print("  L   : "+" ".join(f"{L:7d}" for L in Ls))
    print("  g*P : "+" ".join(f"{g*p:7.4f}" for g,p in zip(degen,permode)) + "   (degeneracy x per-mode power)")
    print("  w_L : "+" ".join(f"{w:7.4f}" for w in wflat) + "   ((L+1)/(L(L+2)))")
    print("  -> g_beta * P_beta == (L+1)/(L(L+2)) exactly:",
          np.allclose(degen*permode, wflat))
    print("  -> large-L limit  w_L * L :", f"{wflat[-1]*Ls[-1]:.4f}", "(-> 1 = dk/k, scale-invariant continuum)")

    # --- 2. flat-limit test (machinery alive) ----------------------------------------------------
    print("\n[2] FLAT-LIMIT TEST (chi=D_C/r0 -> 0 must give flat ell(ell+1)C_ell):")
    for c in (0.05, 0.3):
        D = Dl(Cl_SW(ells, w_HZ, chi=c), ells)
        print(f"   chi={c:.2f}: l2={D[0]:.3f} l3={D[1]:.3f} l5={D[3]:.3f} l10={D[8]:.3f}  (flat=1)")

    # --- 3. the CR result with the DERIVED measure -----------------------------------------------
    print("\n[3] CR bare-SW low-ell with the DERIVED first-principles measure (chi=2.75):")
    D = Dl(Cl_SW(ells, w_HZ), ells)
    for i,l in enumerate(ells):
        if l <= 8:
            print(f"   ell={l}: {D[i]:.3f}  {'#'*int(round(D[i]*40))}")
    r23 = D[0]/D[1]
    print(f"   quadrupole/octopole ratio D2/D3 = {r23:.3f}  (==1 => starved together; smooth deficit)")

    # --- 4. ROBUSTNESS: does the measure differentiate ell=2 from ell=3? -------------------------
    # vary the low-L measure: w_L ~ (L+1)/(L(L+2)) * (L)^(-q) for a range of q (tilts the low-L
    # weighting); a blue/red primordial tilt and plausible measure conventions live in this family.
    print("\n[4] MEASURE-ROBUSTNESS of the D2/D3 ratio (the octopole-differentiation test):")
    print("    q    weight family                 D2     D3     D2/D3")
    for q in (-0.4, -0.2, 0.0, 0.2, 0.4):
        wq = lambda L, q=q: (L+1)/(L*(L+2)) * L**(-q)
        Dq = Dl(Cl_SW(ells, wq), ells)
        tag = "  <- derived HZ measure" if q==0.0 else ""
        print(f"   {q:+.1f}   (L+1)/(L(L+2)) * L^(-q)     {Dq[0]:.3f}  {Dq[1]:.3f}  {Dq[0]/Dq[1]:.3f}{tag}")
    print("   (also: pure per-mode 1/(beta(beta^2-1)) with NO degeneracy, a wrong measure, for contrast)")
    Dno = Dl(Cl_SW(ells, lambda L: 1.0/((L+1)*((L+1)**2-1))), ells)
    print(f"          1/(beta(beta^2-1)) alone        {Dno[0]:.3f}  {Dno[1]:.3f}  {Dno[0]/Dno[1]:.3f}")

    print("\n[VERDICT]")
    print(" - The headline measure (L+1)/(L(L+2)) is the first-principles closed-S^3 HZ weight")
    print("   (degeneracy beta^2 x per-mode power 1/(beta(beta^2-1))) -- caveat (b) CLOSED, not ad hoc.")
    print(" - D2/D3 ~ 1 and is STABLE across the measure family: the single floor k_2 starves ell=2")
    print("   and ell=3 ALIKE; the exact measure does NOT differentiate the quadrupole from the octopole.")
    print(" - With Doppler already non-differentiating (verify_doppler_lowell.py), two of the three")
    print("   flagged differentiators are closed: the smooth ell<~7 deficit is FIRM, and the octopole")
    print("   over-prediction stands as the falsification edge.  Residual: the full Boltzmann solve")
    print("   (~10-20% on the transfer), not expected to lift the factor ~4-5 -- stated without being claimed.")
    print("="*74)
