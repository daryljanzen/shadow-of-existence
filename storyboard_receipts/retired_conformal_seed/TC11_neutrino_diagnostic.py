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
"""TC10 — THE NEUTRINO HIERARCHY ADDED, per A.35's specification.
Photons+baryons (tightly coupled), CDM, and FREE-STREAMING NEUTRINOS with a multipole hierarchy.
Anisotropic stress separates the potentials: Phi != Psi, which is the skeleton assumption C6 flagged.
CONTROL: phi_1 ~ 0.27 AND P1/P2 ~ 2.2 on LambdaCDM.  Prediction from A.35: +0.077 to phi_1."""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
c=299792.458
H0=67.4; Om=0.307; z_eq=3403.6; Or=Om/(1+z_eq); OL=1-Om
ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
fnu=0.4052                                   # neutrino share of the radiation
Hub=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)
ag=np.logspace(-8, np.log10(a_rec), 12000)
eg=np.concatenate([[0.],cumulative_trapezoid(c/(ag**2*Hub(ag)),ag)])
eta_rec=eg[-1]
Hc_of=CubicSpline(eg, ag*Hub(ag)/c)
rt=Or/ag**4+Om/ag**3+OL
Og_of=CubicSpline(eg,(1-fnu)*(Or/ag**4)/rt); On_of=CubicSpline(eg,fnu*(Or/ag**4)/rt)
Oc_of=CubicSpline(eg,(Om/ag**3)/rt); Rb_of=CubicSpline(eg, Rb_rec*(ag/a_rec))
DM=quad(lambda a: c/(a**2*Hub(a)), a_rec, 1.0, limit=250)[0]
rs=quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))), 1e-9, a_rec, limit=250)[0]
lA=np.pi*DM/rs
print("="*80); print("TC10 — WITH FREE-STREAMING NEUTRINOS"); print("="*80)
print(f"\n  eta_rec={eta_rec:.2f}  r_s={rs:.2f}  D_M={DM:.0f}  l_A={lA:.1f}   f_nu={fnu}")
LMAX=20
def mode(k, eps=0.01):
    ei=eps/k
    def rhs(e,y):
        dc,tc,dg,tg,dn,tn = y[:6]; F=y[6:]        # F[0]=F2, F[1]=F3, ...
        Hc=Hc_of(e); Rb=Rb_of(e); Og=Og_of(e); On=On_of(e); Oc=Oc_of(e)
        sig=F[0]/2
        Ps_minus_Ph = 6*Hc**2*On*sig/k**2          # Psi = Phi - 6 H^2 On sig /k^2 ... sign below
        # constraint: Phi - Psi = -6 H^2 On sig / k^2   =>  Psi = Phi + 6 H^2 On sig /k^2
        # solve Phi from Poisson given Psi(Phi): do it explicitly
        # Poisson: Phi' = -Hc Psi - k^2 Phi/(3Hc) - (Hc/2) sum
        return None
    # explicit state: carry Phi as a variable, Psi algebraic from Phi and sigma
    def rhs2(e,y):
        dc,tc,dg,tg,dn,tn,Ph = y[0],y[1],y[2],y[3],y[4],y[5],y[6]
        F=y[7:]
        Hc=Hc_of(e); Rb=Rb_of(e); Og=Og_of(e); On=On_of(e); Oc=Oc_of(e)
        sig=F[0]/2
        Ps = Ph + 6*Hc**2*On*sig/k**2
        Php = -Hc*Ps - k**2*Ph/(3*Hc) - (Hc/2)*(Og*dg+On*dn+Oc*dc)
        d=[-tc+3*Php,
           -Hc*tc+k**2*Ps,
           -(4/3)*tg+4*Php,
           -(Hc*Rb/(1+Rb))*tg+(k**2/(1+Rb))*dg/4+k**2*Ps,
           -(4/3)*tn+4*Php,
           k**2*(dn/4-sig)+k**2*Ps,
           Php]
        dF=np.empty(LMAX-1)
        dF[0]=(8/15)*tn-(3/5)*k*F[1]                     # F2
        for i in range(1,LMAX-2):
            l=i+2
            dF[i]=k/(2*l+1)*(l*F[i-1]-(l+1)*F[i+1])
        l=LMAX; dF[-1]=k*F[-2]-(l+1)/e*F[-1]             # truncation
        return d+list(dF)
    Ph0=1.0; Ps0=Ph0/(1+2*fnu/5)
    y0=[-1.5*Ps0, k**2*ei*Ps0/2, -2*Ps0, k**2*ei*Ps0/2, -2*Ps0, k**2*ei*Ps0/2, Ph0]+[0.0]*(LMAX-1)
    s=solve_ivp(rhs2,[ei,eta_rec],y0,method='RK45',rtol=1e-6,atol=1e-11,dense_output=True)
    yr=s.sol(eta_rec); Ph=yr[6]; sig=yr[7]/2
    Ps=Ph+6*Hc_of(eta_rec)**2*On_of(eta_rec)*sig/k**2
    return yr[2]/4+Ps, Ps
# DIAGNOSTIC: does sigma_nu grow to the right magnitude through horizon entry?
def diag(k, eps=0.01):
    ei=eps/k
    import types
    # rerun the integrator but keep the solution object
    out={}
    def run():
        nonlocal out
        ei2=ei
        # copy of mode() internals
        return None
    return None
# simpler: instrument mode() by re-solving and sampling
def mode_full(k, eps=0.01):
    ei=eps/k
    def rhs2(e,y):
        dc,tc,dg,tg,dn,tn,Ph = y[0],y[1],y[2],y[3],y[4],y[5],y[6]
        F=y[7:]
        Hc=Hc_of(e); Rb=Rb_of(e); Og=Og_of(e); On=On_of(e); Oc=Oc_of(e)
        sig=F[0]/2
        Ps = Ph + 6*Hc**2*On*sig/k**2
        Php = -Hc*Ps - k**2*Ph/(3*Hc) - (Hc/2)*(Og*dg+On*dn+Oc*dc)
        d=[-tc+3*Php, -Hc*tc+k**2*Ps, -(4/3)*tg+4*Php,
           -(Hc*Rb/(1+Rb))*tg+(k**2/(1+Rb))*dg/4+k**2*Ps,
           -(4/3)*tn+4*Php, k**2*(dn/4-sig)+k**2*Ps, Php]
        dF=np.empty(LMAX-1)
        dF[0]=(8/15)*tn-(3/5)*k*F[1]
        for i2 in range(1,LMAX-2):
            l=i2+2; dF[i2]=k/(2*l+1)*(l*F[i2-1]-(l+1)*F[i2+1])
        l=LMAX; dF[-1]=k*F[-2]-(l+1)/e*F[-1]
        return d+list(dF)
    Ph0=1.0; Ps0=Ph0/(1+2*fnu/5)
    sig_i=(eps**2)*Ps0/15
    y0=[-1.5*Ps0,k**2*ei*Ps0/2,-2*Ps0,k**2*ei*Ps0/2,-2*Ps0,k**2*ei*Ps0/2,Ph0]+[2*sig_i]+[0.0]*(LMAX-2)
    return solve_ivp(rhs2,[ei,eta_rec],y0,method='RK45',rtol=1e-6,atol=1e-11,dense_output=True)
k1=270/DM
sol=mode_full(k1)
print(f"\n  DIAGNOSTIC for the first-peak mode, k={k1:.5f} (l=270):")
print(f"  {'eta':>8s} {'k eta':>7s} {'delta_nu':>10s} {'sigma_nu':>10s} {'sig/(dn/4)':>11s} {'Phi':>8s} {'Psi':>8s}")
for e in [1.0,5.0,20.0,52.0,114.0,200.0,eta_rec]:
    y=sol.sol(e); sig=y[7]/2
    Ps=y[6]+6*Hc_of(e)**2*On_of(e)*sig/k1**2
    r=sig/(y[4]/4) if abs(y[4])>1e-30 else 0
    print(f"  {e:>8.1f} {k1*e:>7.2f} {y[4]:>10.4f} {sig:>10.5f} {r:>11.4f} {y[6]:>8.4f} {Ps:>8.4f}")
print(f"\n  (horizon entry at k eta = 1, i.e. eta = {1/k1:.1f} Mpc; equality at 114)")
v,P=mode(1e-4); print(f"\n  super-horizon Psi(rec) = {P:.4f}")
ls=np.arange(120,1300,10.0)
res=np.array([mode(l/DM)[0] for l in ls])
rD=DM/1362.
Dl=(res*np.exp(-((ls/DM)*rD)**2))**2*ls**(0.965-1)
idx=[i for i in argrelextrema(Dl,np.greater,order=2)[0]]
print(f"\n  {'peak':>5s} {'l found':>9s} {'l meas':>8s} {'phi_n':>8s}")
meas=[220,536,813,1126]
for n,i in enumerate(idx[:4]):
    print(f"  {n+1:>5d} {ls[i]:>9.0f} {meas[n] if n<4 else '-':>8} {(n+1)-ls[i]/lA:>8.3f}")
if len(idx)>=3:
    h=[Dl[i] for i in idx[:3]]
    print(f"\n  P1/P2 = {h[0]/h[1]:7.3f}   (measured 2.212)      phi_1 target 0.27")
