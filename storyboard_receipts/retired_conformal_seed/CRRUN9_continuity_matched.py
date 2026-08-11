"""
=== RETIRED r2350 --- CARRIES THE CONFORMAL-TIME SEEDING DEFECT (r2349) ===

This file builds its background as
    ag = np.logspace(-5, 0, ...)
    eg = np.concatenate([[0.], cumulative_trapezoid(c/(ag**2*Hub(ag)), ag)])
which SEEDS THE CONFORMAL TIME AT ZERO where a = 1e-5, omitting the 4.596 Mpc already
elapsed from a = 0.  (In radiation domination H ~ a^-2 makes c/(a^2 H) constant, so the
missing piece is a/(H0 sqrt(Omega_r)) = 4.635 Mpc; the exact integral is 4.59615.)

CONSEQUENCE: eta is short by 4.596 Mpc at every epoch.  That is 0.03% of eta_0 but 12% at
z = 1e4, so LATE-TIME results here (l_A, peak positions, P1/P2) are unaffected while any
EARLY-TIME quantity or any comparison against another code is distorted.  This is what
produced the "4.4% T(k) deficit" that was chased as physics from r2197 to r2348.

NOT RETROACTIVELY CORRECTED, deliberately: this file is stored as it was built and used, so
the record of what was run stays honest.  The defect is recorded here instead.  The two
CITED files carrying it (C11TEST_radiation_zeroed, ROBUST_p1p2_scan) and the live instrument
(HIER_photon_hierarchy) WERE fixed at r2349-r2350.
=========================================================================================
"""
"""CRRUN — THE SAME INTEGRATOR ON CR.  The control passed at r1975, so this may now be run.
WHAT CHANGES, and each from the corpus not from me:
  * BACKGROUND: H^2 = H0^2(Om a^-3 + OL) at H0=73, Om=0.3066 -- radiation is content, not a source.
  * LOWER LIMIT: the SEAM, not eta->0 (C9: there is no observable expansion below it).
  * INITIAL DATA: the seam is NULL, so CHARACTERISTIC -- P15 sec:coherence, ONE datum per mode and a
    COMMON phase.  The modes are already sub-horizon there (prop:subhorizon), so the super-horizon
    adiabatic ICs used for LambdaCDM do NOT apply.  The one datum is the amplitude, C4 gives it FLAT
    in k, and the common phase is taken at an extremum (velocities zero).
  * SPECIES: adiabatically related, as the transmission argument requires.
CONTROL REFERENCE: the LambdaCDM run at r1975 -- peaks 225/510/810, phi_1=0.254, P1/P2=2.299."""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn
from scipy.optimize import brentq
from scipy.signal import argrelextrema
c=299792.458
H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec); fnu=0.4052; LMAX=20
Hub=lambda a: H0*np.sqrt(Om/a**3+OL)                    # *** NO RADIATION TERM ***
Or_content=4.15e-5/(H0/100)**2   # *** omega_r is FIXED by T_CMB; Omega_r = omega_r/h^2.  The old
                                 # form had BOTH scaling factors inverted, giving z_eq=2905 where
                                 # omega_m/omega_r gives 3936 -- 37% too much radiation (r1989). ***
ag=np.logspace(-5,0,14000)
eg=np.concatenate([[0.],cumulative_trapezoid(c/(ag**2*Hub(ag)),ag)])
Hc_of=CubicSpline(eg, ag*Hub(ag)/c)
rt=Or_content/ag**4+Om/ag**3+OL
Og_of=CubicSpline(eg,(1-fnu)*(Or_content/ag**4)/rt); On_of=CubicSpline(eg,fnu*(Or_content/ag**4)/rt)
Oc_of=CubicSpline(eg,(Om/ag**3)/rt); Rb_of=CubicSpline(eg, Rb_rec*(ag/a_rec))
eta_rec=float(np.interp(a_rec,ag,eg)); eta_0=eg[-1]
rs_f=lambda zs: quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))), 1/(1+zs), a_rec, limit=250)[0]
DM=eta_0-eta_rec
zs=brentq(lambda z: np.pi*DM/rs_f(z)-301.6, 1500., 60000.)
a_onset=1/(1+zs); eta_onset=float(np.interp(a_onset,ag,eg)); rs=rs_f(zs); lA=np.pi*DM/rs
print("="*80); print("CRRUN9 — TWO BRANCHES MATCHED BY CONTINUITY"); print("="*80)
print(f"\n  z_onset={zs:.0f}  eta_onset={eta_onset:.2f}  eta_rec={eta_rec:.1f}  D={DM:.0f}  r_s={rs:.2f}  l_A={lA:.1f}")
eta_end=float(np.interp(min(20*a_rec,1.0),ag,eg))
def mode(k):
    def rhs(e,y):
        dc,tc,dg,tg,dn,tn,Ph=y[:7]; F=y[7:]
        Hc=Hc_of(e); Rb=Rb_of(e); Og=Og_of(e); On=On_of(e); Oc=Oc_of(e); sig=F[0]/2
        Ps=Ph+6*Hc**2*On*sig/k**2
        Php=-Hc*Ps-k**2*Ph/(3*Hc)-(Hc/2)*(Og*dg+On*dn+Oc*dc)
        d=[-tc+3*Php,-Hc*tc+k**2*Ps,-(4/3)*tg+4*Php,
           -(Hc*Rb/(1+Rb))*tg+(k**2/(1+Rb))*dg/4+k**2*Ps,
           -(4/3)*tn+4*Php,k**2*(dn/4-sig)+k**2*Ps,Php]
        dF=np.empty(LMAX-1); dF[0]=(8/15)*tn-(3/5)*k*F[1]
        for i in range(1,LMAX-2):
            l=i+2; dF[i]=k/(2*l+1)*(l*F[i-1]-(l+1)*F[i+1])
        dF[-1]=k*F[-2]-(LMAX+1)/e*F[-1]
        return d+list(dF)
    # CHARACTERISTIC DATA AT THE SEAM: one amplitude, flat in k (C4), common phase (velocities zero)
    # *** ONE DATUM PER MODE, AND REGULARITY FIXES THE REST (P15 sec:coherence; the primordial
    # scalar spectrum IS the characteristic data of the seam).  So the datum is the ACOUSTIC
    # AMPLITUDE -- flat in k by C4 -- with a COMMON phase (velocities zero), the species related
    # adiabatically, and *** Phi DETERMINED BY THE POISSON CONSTRAINT, NOT SET. ***
    # *** ONE FREE FUNCTION PER MODE.  The datum is the PRIMORDIAL SPECTRUM -- delta_g, equivalently
    # the curvature perturbation -- and everything else, INCLUDING the effective temperature at the
    # seam, is DERIVED from it via the constraint.  C4's flat envelope describes what the LEG DID; it
    # is not a second boundary condition to impose here.  Imposing both put a POLE at l~337. ***
    Hcs=Hc_of(eta_onset); Ogs=Og_of(eta_onset); Ons=On_of(eta_onset); Ocs=Oc_of(eta_onset)
    # sub-horizon constraint: k^2 Phi = -(3/2) H^2 sum Omega_i delta_i, with delta_c=(3/4)delta_g
    # and Theta_0+Psi = A  =>  delta_g/4 + Psi = A.  Solve the pair for delta_g and Phi(=Psi here,
    # sigma_nu = 0 at the seam by the same one-datum condition).
    # delta_g = 4(A - Psi);  Psi = -(3/2)(H/k)^2 [ (Og+On) delta_g + Oc (3/4) delta_g ]
    # *** THE FULL CONSTRAINT, not its sub-horizon limit.  For modes SUPER-horizon at the seam
    # (l < H D = 144) the sub-horizon form gives Phi = -71 delta_g, which is nonsense.  The full
    # relativistic Poisson, with theta = 0 at the seam, is
    #     (k^2 + (9/2) H^2 [Om_r + (3/4)Om_m]) Phi = -(3/2) H^2 [Om_r + (3/4)Om_m] delta_g ... no:
    # k^2 Phi + 3H(Phi' + H Psi) = -(3/2)H^2 sum, and on super-horizon scales Phi -> the adiabatic
    # value.  Interpolate correctly by keeping the 3H^2 term: (k^2 + 3H^2) Phi = -(3/2)H^2 S delta_g
    # *** TWO BRANCHES, MATCHED BY CONTINUITY AT k = H_seam (A.51-A.53). ***
    #   below: ordinary adiabatic super-horizon data (the validated LCDM form) -- A.50
    #   above: the leg handover, amplitude FLAT in k (C4), Phi from the constraint
    #   and A_eff is fixed by DEMANDING CONTINUITY at the boundary, not chosen.
    S = (Ogs+Ons) + 0.75*Ocs
    Ps_sh = 1.0/(1+2*fnu/5); dg_sh = -2*Ps_sh
    coef_b = -(1.5)*S/4.0                      # coef at k = H_s exactly
    A_eff = dg_sh*(1+4*coef_b)/4.0             # continuity condition
    if k < Hcs:
        Ph0 = 1.0
        y0=[-1.5*Ps_sh, k**2*eta_onset*Ps_sh/2, dg_sh, k**2*eta_onset*Ps_sh/2,
            dg_sh, k**2*eta_onset*Ps_sh/2, Ph0]+[0.0]*(LMAX-1)
    else:
        coef = -(1.5)*Hcs**2*S/(k**2 + 3*Hcs**2)
        dg0 = 4*A_eff/(1+4*coef)
        Ph0 = coef*dg0
        y0=[0.75*dg0, 0.0, dg0, 0.0, dg0, 0.0, Ph0]+[0.0]*(LMAX-1)
    s=solve_ivp(rhs,[eta_onset,eta_end],y0,method='RK45',rtol=1e-6,atol=1e-11,dense_output=True)
    yr=s.sol(eta_rec); sig=yr[7]/2
    Psr=yr[6]+6*Hc_of(eta_rec)**2*On_of(eta_rec)*sig/k**2
    ee=np.linspace(eta_rec,eta_end,60); Y=s.sol(ee); Ph=Y[6]; sg=Y[7]/2
    Ps=Ph+6*np.array([Hc_of(e) for e in ee])**2*np.array([On_of(e) for e in ee])*sg/k**2
    return yr[2]/4+Psr, yr[3]/k, ee, np.gradient(Ph,ee)+np.gradient(Ps,ee)
def spectrum(nk=220, lmax=950):
    kk=np.linspace(20/DM,(lmax+400)/DM,nk)
    SW=np.empty(nk); DP=np.empty(nk); IS=[]
    for i,k in enumerate(kk):
        a,b,ee,src=mode(k); SW[i]=a; DP[i]=b; IS.append(src)
    # r_D on THIS rate (C8), anchored the same way as the control
    g=lambda a:(Rb_of(np.interp(a,ag,eg))**2/(1+Rb_of(np.interp(a,ag,eg)))+8/9)/(6*(1+Rb_of(np.interp(a,ag,eg))))
    I=quad(lambda a: ((Rb_rec*a/a_rec)**2/(1+Rb_rec*a/a_rec)+8/9)/(6*(1+Rb_rec*a/a_rec))/Hub(a), a_onset,a_rec,limit=250)[0]
    Hl=lambda a: 67.4*np.sqrt(0.307/(1+3403.6)/a**4+0.307/a**3+0.693)
    Il=quad(lambda a: ((Rb_rec*a/a_rec)**2/(1+Rb_rec*a/a_rec)+8/9)/(6*(1+Rb_rec*a/a_rec))/Hl(a),1e-9,a_rec,limit=250)[0]
    Dl_=quad(lambda a: c/(a**2*Hl(a)),a_rec,1.,limit=250)[0]
    rD=(Dl_/1362.)*np.sqrt(I/Il)
    damp=np.exp(-(kk*rD)**2); SW*=damp; DP*=damp
    P=kk**(0.965-1)/kk
    ls=np.arange(120,lmax,15); Cl=np.empty(len(ls))
    for j,l in enumerate(ls):
        x=kk*DM
        D_=SW*spherical_jn(int(l),x)+DP*spherical_jn(int(l),x,derivative=True)
        add=np.array([np.trapezoid(IS[i]*spherical_jn(int(l),kk[i]*(eta_0-ee)),ee) for i in range(nk)])
        Cl[j]=np.trapezoid(P*(D_+add)**2, kk)
    return ls, Cl*ls*(ls+1), rD
ls,Dl,rD=spectrum(nk=260, lmax=1250)
print(f"  r_D(CR) = {rD:.2f} Mpc   ->  l_D = {DM/rD:.0f}")
Dn=Dl/np.max(Dl)
lsm=Hc_of(eta_onset)*DM
print(f"\n  z_eq={Om/Or_content-1:.0f}  rho_r/rho_m(seam)={(1+zs)/(Om/Or_content):.3f}  l_seam={lsm:.0f}")
print(f"  A_eff (continuity) vs C4 x 1/3 = 0.1612 : see below")
print(f"\n  CR spectrum (l_A={lA:.1f}):")
for j in range(0,len(ls),3):
    mark=" <== l_seam" if abs(ls[j]-lsm)<10 else ""
    print(f"    l={ls[j]:>5d}  {Dn[j]:6.3f}  {'#'*int(52*Dn[j])}{mark}")
