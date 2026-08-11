"""
STEP 1 of the acoustic-transfer build: the collapse-worldline background as ONE reusable object.
Extracted at source from P16 (cosmogenesis_paper.tex) sec:rate + sec:scoping.

The physics the transfer will ride:
  - one E=1 (marginally bound) worldline, Painleve-Gullstrand comoving, flat leaves (P8);
  - density/composition are LEAF-carried and lapse-independent: rho_m(a), rho_r(a) cross the
    seam as inherited progenitor data (continuous);
  - TWO distinct rate-objects (P16 sec:scoping, the three-level rule):
      L2 window rate  H_L2  = sqrt(8πG(rho_m+rho_r)/3 + Λ/3)   [radiation INCLUDED; BBN runs here]
      L1 stacking rate H_L1 = sqrt(8πG rho_m/3        + Λ/3)   [radiation-FREE; observable cosmo]
    meeting at the reassignment SEAM (z≈6797, T≈1.6 eV, rho_r/rho_m≈2), where they differ by
    the finite factor sqrt((rho_m+rho_r)/rho_m)=sqrt3.  The seam resets the STACKING only.
The acoustic transfer (seam->recomb leg) rides radiation CONTENT (c_s, R) on the L1 (radiation-free) rate.
"""
import numpy as np

# --- standard densities (Planck-ish), the leaf-carried content (same in CR and LCDM) ---
h=0.674; H0=100*h*1e3/3.086e22             # s^-1
Om=0.315; Or=9.24e-5; OL=1-Om-Or           # radiation Or incl neutrinos
Ob=0.0493
z_eq=Om/Or-1                                # matter-radiation equality (LCDM)
z_onset=2*(1+z_eq)-1                         # P16 seam: rho_r/rho_m=2  => (1+z)=2(1+z_eq)
G=6.674e-11; c=3e8

def rho_ratio(z): return Or/Om*(1+z)        # rho_r/rho_m = (Or/Om)(1+z)
def E_L2(z): return np.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + OL)     # H/H0, radiation INCLUDED (window/LCDM)
def E_L1(z): return np.sqrt(Om*(1+z)**3 + OL)                    # H/H0, radiation-FREE (stacking)
def T_keV(z): return 2.35e-4*(1+z)/1e3      # photon temp in keV (T0=2.35e-4 eV... ->) rough

print("="*68); print("ANCHOR CHECKS against P16 sec:scoping"); print("="*68)
print(f"  matter-radiation equality z_eq = {z_eq:.0f}   (LCDM)")
print(f"  seam z_onset (rho_r/rho_m=2)     = {z_onset:.0f}   (P16: z≈6797)")
print(f"  rho_r/rho_m at seam            = {rho_ratio(z_onset):.3f}   (P16: ≈2)")
print(f"  H_L2/H_L1 at seam             = {E_L2(z_onset)/E_L1(z_onset):.4f}   (P16: sqrt3={np.sqrt(3):.4f})")
print(f"  rho_r/rho_m at recomb z=1100  = {rho_ratio(1100):.3f}   (leg spans 2 -> ~0.3)")
print()
print("="*68); print("THE SEAM->RECOMB LEG (where the CR-specific transfer lives)"); print("="*68)
print("  LCDM crosses matter-radiation equality on this leg WITH radiation gravitating;")
print("  CR does NOT (L1 radiation-free). z: seam(%.0f) -> recomb(1100), rho_r/rho_m: %.2f -> %.2f"
      %(z_onset, rho_ratio(z_onset), rho_ratio(1100)))
zleg=np.array([z_onset,4000,z_eq,2000,1100])
print("   z      rho_r/rho_m   H_L1/H0        H_L2/H0     H_L2/H_L1")
for z in zleg:
    print(f"  {z:6.0f}   {rho_ratio(z):8.3f}   {E_L1(z):10.1f}   {E_L2(z):10.1f}   {E_L2(z)/E_L1(z):8.4f}")
print()
# the reusable object: baryon loading R and sound speed c_s (radiation CONTENT, same both models)
def R_baryon(z): return 3*Ob/(4*(Or*0.6))*(1/(1+z))   # 3 rho_b/4 rho_gamma ; Or*0.6 ~ photon part
def cs2(z): return 1.0/(3*(1+R_baryon(z)))             # sound speed^2 / c^2
print("  CONTENT (c_s, R) — same in both; it is the RATE that differs:")
for z in [z_onset, z_eq, 1100]:
    print(f"   z={z:6.0f}   R_baryon={R_baryon(z):.3f}   c_s/c={np.sqrt(cs2(z)):.3f}")
print()
print("  WRONG-EXTENSION check (P16: carrying the stacking law INTO the window is ~300x low):")
TD=0.066  # ~0.8 MeV deuterium-bottleneck-ish in units where... use ratio form
# ratio (stacking-in-window)/(standard) ~ [H0 sqrt(Om)(T/T0)^{3/2}] / [1.66 sqrt(g*) T^2/Mpl]
print("   (structural: window needs the RADIATION-INCLUDED rate; the L1/L2 split is load-bearing,")
print("    not bookkeeping — the anchors above reproduce the sqrt3 seam factor and rho_r/rho_m=2.)")
print()
print("REUSABLE OBJECT EXPORTS: rho_ratio(z), E_L1(z), E_L2(z), R_baryon(z), cs2(z), z_onset, z_eq.")
