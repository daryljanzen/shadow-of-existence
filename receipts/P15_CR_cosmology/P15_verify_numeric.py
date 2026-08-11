"""
P15_verify_numeric.py -- verifies P15 numeric anchors, each derived from observational inputs (not hardcoded);
  the receipt marks [E] robust vs [R] leading-order per anchor.
  ANCHOR 5 (prop:amplitude): Lambda=3(H0/c)^2 OmegaL -> Lambda*lP^2=2.85e-122; dS vacuum power (hbar H_Lam/E_P)^2
     =9.5e-123 vs A_s=2.1e-9 -> substrate vacuum ~113 orders BELOW (robust to O(10) 2pi/reduced-MP prefactor). [E]
  ANCHOR 7 (prop:subhorizon): comoving Hubble k at onset H0 E(z_onset)/((1+z)c)=0.0104/Mpc vs first peak
     pi/r_s=0.0217/Mpc -> ratio 2.1x > 1, acoustic modes SUB-HORIZON at the onset. [E]
  (ANCHOR 6 low-ell location [R]: r_0=5064 Mpc, D_C=13927 Mpc, ell_2=7.8 -- leading-order only; the precise
   low-ell deficit is the separate exact-transfer receipts, so the paper does not overclaim from this.)
  Reproduces the paper's numbers exactly.
STATUS: ✔✔ (anchors 5 & 7 PASS [E], match paper; anchor 6 honest leading-order [R])   RUN: python3 P15_verify_numeric.py   RUNTIME: ~2s
ORIGIN: computations/perturbation_verify/verify_numeric.py, verified r1390.
"""
import numpy as np
from scipy.integrate import quad

# --- observational inputs (CR reads Omega_m0 as the epoch clock; H0 the directly-measured rate) ---
H0_kms=67.4; Om=0.3153; OL=1-Om; c=299792.458       # km/s, Mpc
DH=c/H0_kms                                          # Hubble distance, Mpc
# SI for the Planck-scale comparison
H0_si=H0_kms*1e3/3.0857e22                            # 1/s
c_si=2.99792458e8; lP=1.616e-35; hbar=1.0546e-34; G=6.674e-11
Lam_si=3*(H0_si/c_si)**2*OL                           # 1/m^2  (Lambda = 3 H0^2 OL / c^2)

print("="*68)
print("ANCHOR 5 — substrate vacuum amplitude floor vs observed A_s   [E (order); prefactor convention-flagged]")
print("-"*68)
Lam_planck=Lam_si*lP**2                                # Lambda in Planck units = cosmological-constant-problem number
H_Lam_si=c_si*np.sqrt(Lam_si/3)                        # de Sitter Hubble of the substrate, 1/s
MP=np.sqrt(hbar*c_si/G)                                # Planck mass, kg
# de Sitter vacuum metric-fluctuation power ~ (H_Lam_hbar / M_P c^2)^2  (natural-units order)
EP=np.sqrt(hbar*c_si**5/G)                             # Planck energy, J
H_Lam_E=hbar*H_Lam_si                                  # de Sitter Hubble in energy, J
Delta2_sub=(H_Lam_E/EP)**2                             # ~ (H_Lam/M_P)^2
As=2.1e-9
print(f"  Lambda in Planck units (Lam*lP^2)      = {Lam_planck:.2e}   (the cc-problem number)")
print(f"  substrate dS vacuum power ~(H_Lam/M_P)^2= {Delta2_sub:.2e}")
print(f"  observed A_s                           = {As:.2e}")
print(f"  ratio substrate/observed               = {Delta2_sub/As:.2e}  (~{np.log10(As/Delta2_sub):.0f} orders BELOW)")
# ** ANCHOR 5's PRINTED VERDICT HAD NOTHING BEHIND IT (routed by node 56, r2376+c54.166). **  The
# sub-horizon anchor gained a real check at c54.154; THIS one still printed PASS on a computation it
# never compared.  ** A printed verdict with nothing compared is a claim, not a check. **  The claim
# the paper cites this for is that the substrate's own vacuum is ~110-120 orders BELOW the observed
# A_s -- so the amplitude is inherited classical content and no inflationary consistency relation
# applies.  That gap is what is asserted, with the O(10) prefactor convention left loose deliberately.
_gap = np.log10(As / Delta2_sub)
assert 105.0 < _gap < 125.0, f"the substrate/observed gap is {_gap:.1f} orders, not the 110-120 claimed"
assert Delta2_sub < As, "the substrate vacuum must be BELOW the observed amplitude for the claim to hold"
print(f"  ** CHECK (c54.166): the gap is {_gap:.1f} orders; the paper's claim is 110-120. **")
print("  RESULT: PASS [E] — substrate vacuum is ~110-120 orders below A_s, robust to the O(10) prefactor")
print("          (6e-123 vs 3e-122 etc = 2pi / reduced-vs-full M_P convention). Conclusion: the amplitude")
print("          is INHERITED CLASSICAL content, not the substrate vacuum -> no inflationary consistency relation.")

print()
print("="*68)
print("ANCHOR 6 — low-ell discreteness cutoff  ell_L = sqrt(L(L+2)) * D_C / r_0   [R — leading order, O(1)]")
print("-"*68)
# present epoch from Omega_m/Omega_L = csch^2(u), u=(1/2)sqrt(3 Lam) c tau~0   (P9 eq L542)
u=np.arcsinh(np.sqrt(OL/Om))                           # sinh(u)=sqrt(OL/Om)
# current cosmological S^3 areal radius r_0 = (2^{1/3}/sqrt(Lam)) sinh^{2/3}(u)   (Nariai amplitude, P9 eq:nariai-amplitude + eq:r-SdS-solution)
inv_sqrtLam=DH/np.sqrt(3*OL)                            # 1/sqrt(Lam) in Mpc = c/(H0 sqrt(3 OL))
r0=(2**(1/3))*inv_sqrtLam*np.sinh(u)**(2/3)            # Mpc
# comoving distance to last scattering (flat-LCDM, robust per P9; radiation-free integrand to z_rec)
zrec=1089.0
Ez=lambda z: np.sqrt(Om*(1+z)**3+OL)                   # CR radiation-free rate
DC=DH*quad(lambda z:1/Ez(z),0,zrec)[0]                 # Mpc
print(f"  present-epoch u=asinh(sqrt(OL/Om))     = {u:.3f}")
print(f"  1/sqrt(Lambda)                          = {inv_sqrtLam:.0f} Mpc")
print(f"  current S^3 areal radius r_0            = {r0:.0f} Mpc")
print(f"  comoving distance to last scattering D_C= {DC:.0f} Mpc  (flat-LCDM, radiation-free integrand)")
for L in [1,2,3,4,5,10,20]:
    ell=np.sqrt(L*(L+2))*DC/r0
    print(f"    L={L:2d} -> ell ~ {ell:5.1f}")
print("  RESULT: [R] leading-order kD projection. Robust content: a discreteness floor at ell ~ a few,")
print("          set PARAMETER-FREE by Lambda (via r_0) and the standard D_C; lowest physical mode L=2 -> ell~7-8;")
print("          quasi-continuous by L~20. NOT a pinned ell. O(1) ambiguity: S^3 areal vs curvature radius,")
print("          and the discrete-L -> continuous-ell projection. Matches observed low-ell deficit in order only.")

print()
print("="*68)
print("ANCHOR 7 — acoustic modes are SUB-HORIZON at the plasma onset   [E]")
print("-"*68)
z_onset=6797.0   # r2366: fitted to the measured 100theta_*=1.04109 (was 6850, +0.28%, ~10sigma)
# comoving Hubble wavenumber at onset (CR radiation-free rate): k_hor = a H / c = H0 E(z) / ((1+z) c)  [1/Mpc]
k_hor_onset=H0_kms*Ez(z_onset)/((1+z_onset)*c)
rs=145.0                                                # acoustic sound horizon (banked scale, P9 sec687-691), Mpc
k_peak1=np.pi/rs                                        # first acoustic peak comoving wavenumber, 1/Mpc
print(f"  comoving Hubble k at onset (z={z_onset:.0f})   = {k_hor_onset:.4f} 1/Mpc")
print(f"  first acoustic peak k ~ pi/r_s (r_s~{rs:.0f})= {k_peak1:.4f} 1/Mpc")
print(f"  acoustic peak / horizon                  = {k_peak1/k_hor_onset:.1f}x  (>1 => sub-horizon)")
print("  RESULT: PASS [E] — acoustic-scale modes are inside the horizon at the onset; the standard")
print("          horizon-crossing/inflationary-IC story does not apply; the onset handover gates them.")

# =====================================================================
# ** CHECKS, added r2376+c54.154.  Print-only until now, so its OK certified that Python exited
#    zero.  The claim P15 cites it for at prop:subhorizon is that the acoustic modes are INSIDE
#    the horizon at onset by a factor >~ 2; that factor is asserted here. **
_Ez = np.sqrt(Om * (1 + z_onset)**3 + OL)
_k_hor = H0_kms * _Ez / ((1 + z_onset) * c)
_k_ac = np.pi / rs
_fac = _k_ac / _k_hor
print()
print(f"  ** CHECK (c54.154): k_hor(onset) = {_k_hor:.4f}/Mpc against the acoustic "
      f"k = pi/r_s = {_k_ac:.4f}/Mpc,")
print(f"     so the acoustic modes sit inside the horizon by a factor {_fac:.2f}. "
      f"prop:subhorizon claims >= 2. **")
assert _fac >= 2.0, f"sub-horizon factor is {_fac:.3f}, below the claimed 2"
assert 0.005 < _k_hor < 0.02 and 0.015 < _k_ac < 0.03, "the two wavenumbers moved off their range"
print("  CHECKS PASS")
