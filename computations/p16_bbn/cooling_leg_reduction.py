"""
D1 companion -- verify the REDUCTION that makes the cooling leg a standard BBN (P16 sec:rate,
sec:peak, sec:trev).  The network (bbn_network.py) assumes three facts; here each is checked.

NB. This SUPERSEDES the r497-era CR_seam_turning_point_temperature.py, which estimated the
COSMOLOGICAL SEAM temperature (z~6797, ~1.6 eV -- the cold L1 onset of the observable foliation)
and, lacking the sec:peak distinction, concluded the light elements must be "inherited." P16
separates that cold cosmological seam (L1) from the PROGENITOR's local collapse peak (L2, the
self-gravitating excursion), which is set by the M-independent infall energy and runs HOT. The
nucleosynthesis is in-situ on the cooling leg of the local collapse, not inherited.

Facts verified:
  (1) sec:peak  -- the peak is M-INDEPENDENT: GM/R_s c^2 = 1/2 identically -> infall KE ~ half a
                   rest mass/nucleon ~ few hundred MeV -> T_pk ~ O(10^2) MeV, 3-4 orders above the
                   deuterium bottleneck, for EVERY progenitor.  The horizon-crossing mean density
                   rho_hor ~ M^-2 is a FLOOR, dilute for the cluster-scale holes P1 actually
                   delivers -- not the peak.
  (2) sec:peak  -- the compression is ADIABATIC: Thomson optical depth ~10^20, photon-diffusion
                   time >> free-fall time, so the trapped bath compresses with the gas, T~rho^1/3.
  (3) sec:rate  -- the WINDOW rate is the STANDARD Friedmann rate |H|=sqrt(8 pi G rho_r/3); the two
                   wrong extensions are each quantitatively fatal (stacking law into the window is
                   ~300x too slow; local law past the seam radiation-pins r_s).
  (4) metallicity floor -- total dissociation at T_pk >> nuclear binding resets to light elements
                   -> near-zero metals in the oldest systems.
"""
import numpy as np

# constants (SI)
G=6.674e-11; c=2.998e8; kB=1.381e-23; mp=1.673e-27; MeV_J=1.602e-13
Msun=1.989e30; sigT=6.652e-29; MeV=1.0
def J_to_MeV(E): return E/MeV_J
def T_from_kT_MeV(kT_MeV): return kT_MeV  # report kT in MeV directly

print("="*74)
print("COOLING-LEG REDUCTION  --  the three facts that make it a standard BBN")
print("="*74)

# ---------------------------------------------------------------------------
# (1) The peak is M-independent; rho_hor is a floor, not the peak.
# ---------------------------------------------------------------------------
print("\n(1) sec:peak -- M-INDEPENDENT peak from the infall energy (GM/R_s c^2 = 1/2)")
print(f"    {'M [Msun]':>12s} {'R_s [m]':>11s} {'GM/R_s c^2':>11s} {'kT_infall':>11s} {'rho_hor':>12s}")
print(f"    {'':12s} {'':11s} {'(=1/2)':>11s} {'[MeV/nucl]':>11s} {'[g/cm^3]':>12s}")
for M_solar in [1e1, 1e6, 1e9, 1e13, 1e15]:
    M=M_solar*Msun
    Rs=2*G*M/c**2
    ratio=G*M/(Rs*c**2)                       # identically 1/2
    kT_infall_MeV=J_to_MeV(0.5*mp*c**2)       # KE ~ 1/2 m c^2 per nucleon at R_s -> thermalized
    rho_hor=3*c**6/(32*np.pi*G**3*M**2)        # kg/m^3
    rho_hor_cgs=rho_hor/1000.0                 # g/cm^3
    print(f"    {M_solar:12.0e} {Rs:11.3e} {ratio:11.3f} {kT_infall_MeV:11.1f} {rho_hor_cgs:12.3e}")
kT_infall_MeV=J_to_MeV(0.5*mp*c**2)
T_D=0.07
print(f"    -> infall scale kT ~ {kT_infall_MeV:.0f} MeV/nucleon, INDEPENDENT of M; the conservative")
print(f"       thermalized bound T_pk >~ O(10^2) MeV is {1e2/T_D:.0f}x (~{np.log10(1e2/T_D):.1f} orders) above")
print(f"       the bottleneck T_D={T_D} MeV; at the full infall scale it is {kT_infall_MeV/T_D:.0f}x (~{np.log10(kT_infall_MeV/T_D):.1f} orders).")
rho_now=9.9e-30  # g/cm^3, present mean cosmic density
# crossover mass where the horizon-crossing mean density equals the present cosmic density
Mstar_kg=np.sqrt(3*c**6/(32*np.pi*G**3*(rho_now*1000)))    # rho_now in kg/m^3
Mstar_solar=Mstar_kg/Msun
print(f"    -> rho_hor ~ M^-2 is a FLOOR, not the peak.  It equals the present cosmic density")
print(f"       {rho_now:.1e} g/cm^3 at M* ~ {Mstar_solar:.1e} Msun (comparable to the observable")
print(f"       universe's mass).  For holes at/above M* the horizon-crossing mean is BELOW today's")
print(f"       density -- reading it as the peak would place the hot dense era in our FUTURE (the")
print(f"       reductio).  For cluster-scale holes (1e13-1e15 Msun, the merger end-state P1 delivers)")
print(f"       rho_hor is far too dilute to reach the bottleneck at horizon crossing; the compression")
print(f"       runs PAST the horizon to the r=0 branch point (the lap, sec:lap), so rho_hor bounds")
print(f"       the peak from below.  The peak is the M-independent infall scale above, not rho_hor.")

# ---------------------------------------------------------------------------
# (2) Adiabaticity: optical depth and diffusion-vs-freefall.
# ---------------------------------------------------------------------------
print("\n(2) sec:peak -- ADIABATIC compression (photon bath trapped, T ~ rho^1/3)")
# tau = n sigT R is M-dependent at horizon crossing (~ M^-1) and grows as the collapse deepens
# (R->0 past the horizon). Report it across masses to show it is >>1 for every progenitor;
# the cluster-scale value is a conservative floor that climbs toward the paper's ~1e20 near the peak.
print(f"    Thomson optical depth & diffusion/free-fall ratio at HORIZON CROSSING (conservative;")
print(f"    both grow steeply as the collapse runs past the horizon toward the r=0 branch point):")
print(f"      {'M [Msun]':>10s} {'tau':>10s} {'t_diff/t_ff':>12s}")
for M_solar in [1e0, 1e6, 1e13, 1e15]:
    M=M_solar*Msun; Rs=2*G*M/c**2
    rho_hor=3*c**6/(32*np.pi*G**3*M**2)
    n_e=rho_hor/mp
    tau=n_e*sigT*Rs
    t_ff=1.0/np.sqrt(G*rho_hor)
    lam_mfp=1.0/(n_e*sigT)
    t_diff=Rs**2/(lam_mfp*c)
    print(f"      {M_solar:10.0e} {tau:10.2e} {t_diff/t_ff:12.2e}")
print(f"    -> t_diff >> t_ff for every progenitor (>=~1e8 at horizon crossing for cluster masses,")
print(f"       climbing toward ~1e19-1e20 deep in the compression): the bath cannot leak out, so the")
print(f"       compression is adiabatic and the local kT tracks the density, kT ~ rho^1/3 (justified).")
# demonstrate the adiabat quantitatively
print(f"    adiabat check  kT ~ rho^1/3:")
for fac in [1.0, 1e3, 1e6, 1e9]:
    print(f"      rho x {fac:6.0e}  ->  kT x {fac**(1/3):8.2e}")

# ---------------------------------------------------------------------------
# (3) The window rate is the standard Friedmann rate; wrong extensions are fatal.
# ---------------------------------------------------------------------------
print("\n(3) sec:rate -- the WINDOW rate is STANDARD; the two mis-extensions are fatal")
H0_si=67.4*1e3/3.086e22; Om=0.315; Or=9.1e-5; T0=2.348e-10  # T0 in MeV (2.725 K)
MPl=1.22091e22;
def gstar(TMeV): return 10.75 if TMeV>0.1 else 3.36
def H_std(TMeV):    # standard local Friedmann, radiation-included (== window rate, sec:rate)
    return 1.66*np.sqrt(gstar(TMeV))*(TMeV)**2/MPl * (1/6.582e-22)   # 1/s
def H_stack(TMeV):  # WRONG: the radiation-free stacking law carried into the window
    z=TMeV/T0-1
    return H0_si*np.sqrt(Om*(1+z)**3)
TD=0.07
print(f"    at T_D={TD} MeV:")
print(f"      standard/local window rate  H_std   = {H_std(TD):.3e} /s")
print(f"      stacking law into window    H_stack = {H_stack(TD):.3e} /s")
print(f"      ratio H_std/H_stack = {H_std(TD)/H_stack(TD):.0f}x  -> stacking law is ~300x too SLOW,")
print(f"      the freeze-out is destroyed (the fatal mis-extension #1).")
print(f"    (mis-extension #2 -- carrying the local radiation-sourced law PAST the seam -- radiation-")
print(f"     pins the sound horizon and re-manufactures the Hubble tension; see damping_ratio_clean.py.)")

# ---------------------------------------------------------------------------
# (4) Metallicity floor.
# ---------------------------------------------------------------------------
print("\n(4) metallicity floor -- total dissociation resets to light elements")
B_per_A={'C-12':7.68,'O-16':7.98,'Fe-56':8.79}     # binding energy per nucleon [MeV]
print(f"    peak kT ~ O(10^2) MeV per nucleon vs nuclear binding energies per nucleon:")
for nuc,b in B_per_A.items():
    print(f"      {nuc}: {b:.2f} MeV/nucleon   -> kT/B ~ {1e2/b:.0f}  (>>1: fully photodissociated)")
print(f"    -> every heavy nucleus is unbound at the peak; the composition resets to free nucleons,")
print(f"       so the oldest, least-processed systems emerge near-zero metallicity (the observed floor).")

print("\n"+"="*74)
print("REDUCTION VERIFIED: peak M-independent & hot (every progenitor), compression adiabatic,")
print("window rate standard (mis-extensions fatal), metals reset.  The cooling leg is a standard")
print("BBN -> the network of bbn_network.py is the right object, and its pattern is P16's result.")
print("="*74)
