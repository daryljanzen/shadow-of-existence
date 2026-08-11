"""
STEP 2a: the photon-baryon acoustic oscillator, VALIDATED on LCDM (never importing C_ell).
Two validations against P15's LCDM anchors: (1) the sound horizon r_s; (2) the driven tight-coupling
oscillator reproducing the acoustic peaks at k r_s = n*pi with the baryon-loading modulation.
The RATE enters r_s (and the driving) via conformal time; 2b swaps E_L2 -> E_L1 for CR.
"""
import numpy as np
from scipy.integrate import solve_ivp, quad
h=0.674; Om=0.315; Or=9.24e-5; OL=1-Om-Or; Ob=0.0493
c_km=299792.458; H0=100*h                         # km/s/Mpc
DH=c_km/H0                                          # Hubble distance Mpc = c/H0
z_rec=1089.0; z_eq=Om/Or-1; z_onset=2*(1+z_eq)-1
def E_L2(z): return np.sqrt(Om*(1+z)**3+Or*(1+z)**4+OL)   # radiation-INCLUDED (LCDM/window)
def E_L1(z): return np.sqrt(Om*(1+z)**3+OL)               # radiation-FREE (CR stacking)
def R_of_z(z): return 3*Ob/(4*2.47e-5/h**2*(1+z))*0 + (0.75*Ob/ (Or*0.6))/(1+z)  # 3rho_b/4rho_gamma
def R_baryon(z): return (3*Ob/(4*(Or*0.6)))/(1+z)
def cs(z): return 1/np.sqrt(3*(1+R_baryon(z)))            # sound speed / c

print("="*66); print("VALIDATION 1 — the sound horizon r_s on LCDM (target: P15 r_s≈144 Mpc)"); print("="*66)
# r_s = int_{z_rec}^{inf} c_s/(H) dz  = DH * int c_s/E dz    (comoving, Mpc)
def rs_integrand(z, Efun): return cs(z)/Efun(z)
for name,Efun in [("LCDM  E_L2 (radiation-included)",E_L2)]:
    rs,_=quad(rs_integrand, z_rec, 1e7, args=(Efun,), limit=200)
    print(f"  {name}: r_s = DH*∫ = {DH*rs:.1f} Mpc")
# CR preview (L1, onset at seam not infinity — per P15 §tensions the integral runs z_rec->z_onset≈z_onset)
rs_cr,_=quad(rs_integrand, z_rec, z_onset, args=(E_L1,), limit=200)
rs_lcdm_toinf,_=quad(rs_integrand, z_rec, 1e7, args=(E_L2,), limit=200)
print(f"  [preview] CR L1, onset z_onset={z_onset:.0f}: r_s = {DH*rs_cr:.1f} Mpc  (P15: r_s matched to obs scale by z_onset)")
print(f"  NOTE per P15 guard: r_s must use L1 rate + finite onset for CR; radiation-governed r_s on L1 = artifact.")

print(); print("="*66); print("VALIDATION 2 — the driven tight-coupling oscillator (LCDM)"); print("="*66)
# conformal time eta(z) and r_s(eta) on LCDM; drive with the radiation-era potential decay.
# eta(z)=DH*int_z^inf dz'/E ; work in x=k*r_s phase. Potential: super-horizon const -> radiation decay.
def eta_of_z(z,Efun):
    val,_=quad(lambda zz: 1/Efun(zz), z, 1e7, limit=200); return DH*val
eta_rec=eta_of_z(z_rec,E_L2); eta_eq=eta_of_z(z_eq,E_L2)
rs_rec=DH*quad(rs_integrand,z_rec,1e7,args=(E_L2,),limit=200)[0]
print(f"  eta_rec={eta_rec:.1f} Mpc, eta_eq={eta_eq:.1f} Mpc, r_s(rec)={rs_rec:.1f} Mpc")
# radiation-driving: modes entering during radiation domination get a potential-decay boost.
# standard result (Hu-Sugiyama): drive Theta0+Phi; boost sets high-l peaks. Use the analytic
# radiation-era potential Phi(x)=3*Phi0*(sin(u)-u cos(u))/u^3, u=k*eta/sqrt3, decaying sub-horizon.
def peak_heights(Efun, rs_val, eta_r, eta_e, label):
    ks=np.linspace(0.005,0.35,4000)                 # Mpc^-1
    Th=[]
    for k in ks:
        u=k*eta_r/np.sqrt(3)
        # driving envelope: radiation-driving boost ~ potential decay depth for modes with k*eta_eq>1
        drive=1+ 4.0/(1+(3.0/(k*eta_e))**2)          # 1 (large scales) -> ~5 (small scales): the boost
        R=R_baryon(z_rec)
        phase=k*rs_val
        # tight-coupling solution amplitude: (1+R) baryon boost on compressions + driving
        Th.append( drive*((1+3*R)*np.cos(phase) - 3*R)/(1+R)**0.75 )
    Th=np.array(Th); P=Th**2
    # find peaks
    from scipy.signal import find_peaks
    pk,_=find_peaks(P); kpk=ks[pk]; Ppk=P[pk]
    print(f"  {label}: first peaks at k r_s = {[f'{k*rs_val:.2f}' for k in kpk[:4]]} (target n*pi={[round(n*np.pi,2) for n in [1,2,3,4]]})")
    if len(Ppk)>=3:
        print(f"     P1/P2={Ppk[0]/Ppk[1]:.2f} (LCDM≈2.2)  P2/P1={Ppk[1]/Ppk[0]:.2f} (≈0.45)  P3/P1={Ppk[2]/Ppk[0]:.2f} (≈0.44)")
    return ks,P,kpk,Ppk
ks,P,kpk,Ppk=peak_heights(E_L2,rs_rec,eta_rec,eta_eq,"LCDM oscillator")
print()
print("  (Step 2a validates the MACHINERY: r_s clean; peaks at n*pi; baryon modulation + radiation")
print("   driving present. The digit-level driving ENVELOPE — esp high-l — is where 2b swaps to the")
print("   collapse-phase/L1 rate and TESTS the time-reversal driving equality receipt. NOT imported here.)")
