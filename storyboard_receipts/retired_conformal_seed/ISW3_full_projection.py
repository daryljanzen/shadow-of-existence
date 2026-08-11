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
"""ISW2 — THE ISW TERM ADDED TO THE PROJECTION.  A.38's third source term, the last one.
Structurally different from SW and Doppler: those are thin-source (visibility sharply peaked at
recombination); THIS is integrated along the line of sight from recombination forward.
So: background extended past a_rec, modes continued, Phi'+Psi' sampled over the stretch.
APPROXIMATION STATED: after recombination the photons decouple and my tight-coupling theta_gb is
invalid there -- but the ISW needs only the POTENTIALS, which are CDM-dominated by then
(Omega_r/Omega_m = 0.32 at a_rec and falling as 1/a).  That is why it is safe."""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn
from scipy.signal import argrelextrema
c=299792.458
H0=67.4; Om=0.307; z_eq=3403.6; Or=Om/(1+z_eq); OL=1-Om
ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec); Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
fnu=0.4052; LMAX=20
Hub=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)
# *** background now runs to a=1 ***
ag=np.concatenate([np.logspace(-8,np.log10(a_rec),9000), np.logspace(np.log10(a_rec*1.001),0,3000)])
eg=np.concatenate([[0.],cumulative_trapezoid(c/(ag**2*Hub(ag)),ag)])
eta_rec=float(np.interp(a_rec,ag,eg)); eta_0=eg[-1]
Hc_of=CubicSpline(eg, ag*Hub(ag)/c); rt=Or/ag**4+Om/ag**3+OL
Og_of=CubicSpline(eg,(1-fnu)*(Or/ag**4)/rt); On_of=CubicSpline(eg,fnu*(Or/ag**4)/rt)
Oc_of=CubicSpline(eg,(Om/ag**3)/rt); Rb_of=CubicSpline(eg, Rb_rec*(ag/a_rec))
D=eta_0-eta_rec
rs=quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))), 1e-9, a_rec, limit=250)[0]
lA=np.pi*D/rs
print("="*80); print("ISW2 — WITH THE LINE-OF-SIGHT TERM"); print("="*80)
print(f"\n  eta_rec={eta_rec:.1f}  eta_0={eta_0:.0f}  D={D:.0f}  l_A={lA:.1f}")
eta_isw_end=float(np.interp(min(20*a_rec,1.0),ag,eg))
print(f"  ISW integrated from eta_rec to eta={eta_isw_end:.0f} (a = 20 a_rec, where Omega_r/Omega_m = "
      f"{(Or/(20*a_rec)**4)/(Om/(20*a_rec)**3):.4f})")
def mode(k, eps=0.01):
    ei=eps/k
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
    Ph0=1.0; Ps0=Ph0/(1+2*fnu/5); sig_i=(eps**2)*Ps0/15
    y0=[-1.5*Ps0,k**2*ei*Ps0/2,-2*Ps0,k**2*ei*Ps0/2,-2*Ps0,k**2*ei*Ps0/2,Ph0]+[2*sig_i]+[0.]*(LMAX-2)
    s=solve_ivp(rhs,[ei,eta_isw_end],y0,method='RK45',rtol=1e-6,atol=1e-11,dense_output=True)
    yr=s.sol(eta_rec); sig=yr[7]/2
    Psr=yr[6]+6*Hc_of(eta_rec)**2*On_of(eta_rec)*sig/k**2
    # ISW: sample Phi'+Psi' from eta_rec forward
    ee=np.linspace(eta_rec,eta_isw_end,60)
    Y=s.sol(ee); Ph=Y[6]; sg=Y[7]/2
    Ps=Ph+6*np.array([Hc_of(e) for e in ee])**2*np.array([On_of(e) for e in ee])*sg/k**2
    dPh=np.gradient(Ph,ee); dPs=np.gradient(Ps,ee)
    return yr[2]/4+Psr, yr[3]/k, ee, dPh+dPs
def spectrum(nk, lmax=1200, isw=True):
    kk=np.linspace(20/D,(lmax+400)/D,nk)
    SW=np.empty(nk); DP=np.empty(nk); ISWs=[]
    for i,k in enumerate(kk):
        a,b,ee,src=mode(k); SW[i]=a; DP[i]=b; ISWs.append(src)
    rD=D/1362.; damp=np.exp(-(kk*rD)**2)
    SW*=damp; DP*=damp
    P=kk**(0.965-1)/kk
    ls=np.arange(120,lmax,15); Cl=np.empty(len(ls))
    for j,l in enumerate(ls):
        x=kk*D
        Dl=SW*spherical_jn(int(l),x)+DP*spherical_jn(int(l),x,derivative=True)
        if isw:
            add=np.empty(nk)
            for i,k in enumerate(kk):
                add[i]=np.trapezoid(ISWs[i]*spherical_jn(int(l),k*(eta_0-ee)), ee)
            Dl=Dl+add
        Cl[j]=np.trapezoid(P*Dl**2, kk)
    return ls, Cl*ls*(ls+1)
for isw in [False,True]:
    ls,Dl=spectrum(220, lmax=950, isw=isw)
    idx=[i for i in argrelextrema(Dl,np.greater,order=2)[0]]
    pk=[int(ls[i]) for i in idx[:3]]
    lab="WITH ISW" if isw else "no ISW  "
    if len(idx)>=3:
        h=[Dl[i] for i in idx[:3]]
        print(f"  {lab}: peaks {pk}  phi_1={1-pk[0]/lA:.3f}  P1/P2={h[0]/h[1]:.3f}")
    else:
        print(f"  {lab}: peaks {pk}")
print(f"  measured: peaks [220, 536, 813]  phi_1=0.27  P1/P2=2.212")
