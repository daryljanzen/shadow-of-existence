import numpy as np
# ---- CR / cosmological parameters (from the corpus) ----
rs   = 147.0     # sound horizon at last scattering [Mpc]  (coherence-comb script)
D_C  = 13864.0   # CR comoving distance to LS [Mpc]        (banked)
kD   = 0.13      # Silk damping scale [1/Mpc]              (coherence-comb script)
z_ls = 1090.0
z_onset = 6801.0  # ρ_r/ρ_m ≈ 2 here  -> ρ_r=ρ_m (density) at z_eq
z_eq = (1.0+z_onset)/2.0 - 1.0            # ρ_r/ρ_m=2 at seam, ∝(1+z) -> =1 at z_eq
Rls  = 0.6       # baryon loading R=3ρ_b/4ρ_γ at LS (Ω_b h²≈0.022): standard value
print(f"CR density-equality z_eq = {z_eq:.0f} (ρ_r=ρ_m); seam z={z_onset:.0f}, ρ_r/ρ_m=2 there")
print(f"note: this is the standard z_eq≈3400 — CR's radiation DENSITY tracks standard,")
print(f"      but the geometric stacking RATE means no radiation-dominated EXPANSION epoch.\n")

ell = np.arange(2,1600); k = ell/D_C

# ---- the effective-temperature transfer at last scattering (tight coupling, Hu-Sugiyama form) ----
# [Θ0+Ψ](k) = [ (1+R) * B(k) * cos(k rs)  -  R ] * Ψ0(k) * D(k)
#   cos(k rs): the acoustic phase (coherent, single seam datum)
#   -R term: baryon loading -> boosts ODD (compression) peaks, the peak-height asymmetry
#   B(k): the DRIVING boost (potential decay for modes crossing near/before equality)
#   D(k): Silk damping
D = np.exp(-(k/kD)**2)

# DRIVING bracket. Standard Hu-Sugiyama driving envelope: modes crossing the horizon
# before equality are boosted by the potential decay; the boost saturates ~ a factor of a
# few for k >> k_eq. k_eq (comoving horizon at equality):
keq = 0.073 * (z_eq/3400.0)            # ~standard k_eq ≈ 0.073/Mpc for z_eq≈3400
def driving(kk, strength):
    # strength=1 : full ΛCDM-like driving (radiation gravitates normally at k>>k_eq)
    # strength=0 : NO driving (matter-like potential, Ψ const, the geometric stacking-rate extreme)
    boost_full = 1.0 + 4.0*(1.0 - 1.0/(1.0+(kk/keq)**2))   # ->1 at k<<keq, ->5 at k>>keq (HS ~5x)
    return 1.0 + strength*(boost_full-1.0)

def Theta_eff(strength):
    B = driving(k, strength)
    Psi0 = (k/keq)**0  # flat transfer for the amplitude comparison (isolate the acoustic physics)
    return ((1.0+Rls)*B*np.cos(k*rs) - Rls) * Psi0 * D

# Sachs-Wolfe plateau (large-scale, k rs << 1): (1/3)Ψ ; normalize plateau to 1
def Cl(strength):
    Th = Theta_eff(strength)
    C = Th**2
    # large-scale SW plateau level
    plateau = ( (1.0/3.0) )**2
    return C/plateau

# peak heights (first three) relative to the SW plateau, for the two brackets
def peak_heights(strength):
    C = Cl(strength)
    heights=[]
    for n in (1,2,3):
        kp = n*np.pi/rs
        ip = np.argmin(abs(k-kp))
        # local max near the analytic peak
        lo,hi=max(ip-8,0),min(ip+8,len(k))
        heights.append(C[lo:hi].max())
    return heights

for strength,label in [(1.0,"FULL driving (radiation gravitates normally)"),
                       (0.0,"NO driving (matter-like potential — geometric stacking-rate extreme)")]:
    h = peak_heights(strength)
    print(f"{label}")
    print(f"   peak heights / SW plateau:  P1={h[0]:.1f}  P2={h[1]:.1f}  P3={h[2]:.1f}   (P1/P2={h[0]/h[1]:.2f})")

# observed (Planck, ΔT² relative to SW plateau, rough): first peak ~ (5-6)x the plateau
print(f"\nObserved (Planck, rough): first-peak/plateau ~ 5–6 ;  P1/P2 ~ 2.0–2.3 (baryon loading)")
print("\n--- reading ---")
h1 = peak_heights(1.0); h0 = peak_heights(0.0)
print(f"CR bracket, first-peak/plateau:  [{h0[0]:.1f} (no driving) , {h1[0]:.1f} (full driving)]")
print(f"CR bracket, P1/P2 asymmetry:     [{h0[0]/h0[1]:.2f} , {h1[0]/h1[1]:.2f}]  (baryon loading, driving-robust)")
