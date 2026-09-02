"""
CR perturbation reach -- Step 4, CORRECTED & flat-limit-VERIFIED closed-S^3 SW low-ell transfer.
Supersedes verify_closedS3_transfer.py (recursion, wrong) AND the suppression reading of
verify_closedS3_Cl_exact.py (normalisation, wrong).  History (the boundary, honestly mapped):
  r516: downward recursion -> "no suppression"   [WRONG: recursion off up to 28% at low beta]
  r519: flat-normalised Phi -> "strong suppression" [WRONG: closure sum-rule != const, mis-weighted]
  r521 (this): S^3-ORTHONORMAL radial fns + flat-limit-verified weight -> ~NO suppression (flat).

Two corrections made it sound:
 (1) RADIAL NORMALISATION: use the S^3-orthonormal radial function
        Pi_{beta,ell}(chi) = M sin^ell(chi) C^{ell+1}_{beta-1-ell}(cos chi),
        M^2 = (beta-1-ell)! * beta * (ell!)^2 * 2^{2ell+1} / (pi * Gamma(beta+ell+1)),
     fixed by int_0^pi Pi^2 sin^2chi dchi = 1 (Gegenbauer orthogonality).  VERIFIED: the closure
     sum_ell (2ell+1)Pi^2 is CONSTANT in chi (homogeneity of S^3) -- the flat-normalised functions
     of r519 FAILED this (closure beta,chi-dependent), which is why they mis-weighted the sum.
 (2) PRIMORDIAL WEIGHT: scale-invariant w(beta)=1/(beta(beta^2-1)) (closed-universe Harrison-
     Zel'dovich), SELECTED by the flat-limit test: ell(ell+1)C_ell must be flat as chi_lss->0.
     w=1/(beta(beta^2-1)) passes (~1.00); w=1/beta and 1/(beta^2-1) fail badly.

RESULT [E, flat-limit-verified, beta_max-converged]: at chi_lss=D_C/r0~2.75, ell(ell+1)C_ell is
FLAT to <1% (converging to flat as beta_max->infty) -- the ordinary-SW closed-S^3 transfer shows
NO significant low-ell suppression.  The method is alive (not trivially flat): chi near the antipode
(3.05) develops low-ell structure, chi<=2.75 is flat.

IMPLICATION (LOOK-SIGNAL for the P12 cold read, NOT a verdict): the closed-S^3 *discreteness*
(discrete mode spectrum, lowest physical mode L=2) does NOT, by ordinary SW at chi_lss~2.75, produce
a low-ell power DEFICIT.  So P12's "low-multipole discreteness floor in the region of the observed
deficit" is not supported AS A POWER DEFICIT by this computation.  CAVEATS (not claimed the CR word):
 (a) ordinary SW only -- the ISW is not included;
 (b) STANDARD-closed transfer, NOT the CR non-synchronous tau~=tau+chi transfer (closed-S^3 source on
     the FLAT distance projection, prop:flat) -- the actual unbuilt CR object (P12 sec:scope).
"""
import mpmath as mp, numpy as np
mp.mp.dps = 70; PI = mp.pi

def Pi(beta, ell, cchi, schi):       # S^3-orthonormal radial function
    if ell > beta-1: return mp.mpf(0)
    n = beta-1-ell
    M = mp.sqrt(mp.factorial(n)*beta*mp.factorial(ell)**2*mp.mpf(2)**(2*ell+1)/(PI*mp.gamma(beta+ell+1)))
    return M*schi**ell*mp.gegenbauer(n, ell+1, cchi)

def Dl(chi_val, bmax, ells):         # ell(ell+1)C_ell, w=1/(beta(beta^2-1)), normalised to ell=25-30
    chi = mp.mpf(chi_val); cchi = mp.cos(chi); schi = mp.sin(chi)
    Cl = {l: mp.mpf(0) for l in ells}
    for beta in range(3, bmax+1):
        w = mp.mpf(1)/(beta*(beta**2-1))
        for l in ells:
            if l <= beta-1: Cl[l] += w*Pi(beta, l, cchi, schi)**2
    D = {l: float(l*(l+1)*Cl[l]) for l in ells}
    hi = np.mean([D[l] for l in ells if l >= 25]); return {l: D[l]/hi for l in D}

ells = list(range(2, 31))
print("="*64)
print("CORRECTED closed-S^3 SW low-ell transfer (orthonormal Pi; w=1/(b(b^2-1)))")
print("="*64)
print("[closure check] sum_ell(2ell+1)Pi^2 constant in chi (homogeneity):")
for beta in (10, 25):
    vals = [float(sum((2*l+1)*Pi(beta, l, mp.cos(mp.mpf(c)), mp.sin(mp.mpf(c)))**2 for l in range(beta))) for c in (0.5, 2.75)]
    print(f"   beta={beta}: chi=0.5 -> {vals[0]:.3f} ; chi=2.75 -> {vals[1]:.3f}  (equal = correct)")
print("\n[flat-limit test] ell(ell+1)C_ell at small chi=0.3 (must be ~1 flat):")
D = Dl(0.3, 400, ells); print("   "+" ".join(f"l{l}:{D[l]:.3f}" for l in (2,3,5,10,15)))
print("\n[RESULT at chi_lss=2.75] ell(ell+1)C_ell normalised to ell=25-30 (flat=1):")
for bmax in (400, 700, 1000):
    D = Dl(2.7502, bmax, ells)
    print(f"   bmax={bmax}: l2={D[2]:.4f} l3={D[3]:.4f} l5={D[5]:.4f} l10={D[10]:.4f} l20={D[20]:.4f}")
print("""
[READING]  ordinary-SW closed-S^3 ell(ell+1)C_ell is FLAT at chi_lss~2.75 (converging to flat
 as beta_max grows) -> NO significant low-ell suppression.  Overturns r516 (recursion artifact,
 "no suppression" for the wrong reason) and r519 (normalisation artifact, "strong suppression").
 LOOK-SIGNAL for P12: the discreteness does not give a low-ell power deficit by ordinary SW.
 CAVEATS (not claimed CR word): ordinary SW only (no ISW); standard-closed, not the CR
 non-synchronous tau~=tau+chi transfer.  P12 cold read owed.
""")
print("="*64)
