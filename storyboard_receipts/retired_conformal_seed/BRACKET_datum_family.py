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
print("="*80); print("CRRUN13 — BRACKETING TEST"); print("="*80)
print(f"\n  z_onset={zs:.0f}  eta_onset={eta_onset:.2f}  eta_rec={eta_rec:.1f}  D={DM:.0f}  r_s={rs:.2f}  l_A={lA:.1f}")
eta_end=float(np.interp(min(20*a_rec,1.0),ag,eg))
def modes_all(kk):
    """Solve every mode in ONE system.  State: (nk, 7+LMAX-1) flattened.
    The modes are independent, so this is the identical RHS applied to arrays over k --
    the 360 sequential solve_ivp calls were pure per-call overhead."""
    nk=len(kk); NV=7+(LMAX-1)
    Hcs=Hc_of(eta_onset); Ogs=Og_of(eta_onset); Ons=On_of(eta_onset); Ocs=Oc_of(eta_onset)
    S=(Ogs+Ons)+0.75*Ocs
    # Psi transmits (C1's leg residual); delta_g derived from L1's constraint
    xe=1/np.sqrt(3); ksm=Hcs
    xs=(kk/ksm)/np.sqrt(3)
    Pl=np.where(xs<1e-8,1.0,3*(np.sin(xs)-xs*np.cos(xs))/np.maximum(np.abs(xs),1e-12)**3)
    Ph0=-Pl                                   # potential a well
    import os
    W=float(os.environ.get('JOIN','1.0'))     # join scale in units of H_seam
    u=(kk/(W*Hcs))**2
    # smooth interpolation: -2 Psi at u<<1, -(2/3)k^2 Psi/(H^2 S) at u>>1
    dg0=Ph0*(-2.0 - (2.0/3.0)*kk**2/(Hcs**2*S))*0 + Ph0*(-2.0 - (2.0/3.0)*(kk**2/(Hcs**2*S))*u/(1+u))
    y0=np.zeros((nk,NV))
    y0[:,0]=0.75*dg0; y0[:,2]=dg0; y0[:,4]=dg0; y0[:,6]=Ph0
    def rhs(e,Y):
        y=Y.reshape(nk,NV)
        dc,tc,dg,tg,dn,tn,Ph=[y[:,j] for j in range(7)]
        F=y[:,7:]
        Hc=Hc_of(e); Rb=Rb_of(e); Ogv=Og_of(e); Onv=On_of(e); Ocv=Oc_of(e)
        sig=F[:,0]/2
        Ps=Ph+6*Hc**2*Onv*sig/kk**2
        Php=-Hc*Ps-kk**2*Ph/(3*Hc)-(Hc/2)*(Ogv*dg+Onv*dn+Ocv*dc)
        out=np.empty_like(y)
        out[:,0]=-tc+3*Php
        out[:,1]=-Hc*tc+kk**2*Ps
        out[:,2]=-(4/3)*tg+4*Php
        out[:,3]=-(Hc*Rb/(1+Rb))*tg+(kk**2/(1+Rb))*dg/4+kk**2*Ps
        out[:,4]=-(4/3)*tn+4*Php
        out[:,5]=kk**2*(dn/4-sig)+kk**2*Ps
        out[:,6]=Php
        out[:,7]=(8/15)*tn-(3/5)*kk*F[:,1]
        for i in range(1,LMAX-2):
            l=i+2; out[:,7+i]=kk/(2*l+1)*(l*F[:,i-1]-(l+1)*F[:,i+1])
        out[:,7+LMAX-2]=kk*F[:,LMAX-3]-(LMAX+1)/e*F[:,LMAX-2]
        return out.ravel()
    NS=1400
    eg2=np.linspace(eta_onset,eta_end,NS+1); h=eg2[1]-eg2[0]
    Y=y0.ravel().copy(); store=np.empty((NS+1,Y.size)); store[0]=Y
    for n in range(NS):
        e=eg2[n]
        k1=rhs(e,Y); k2=rhs(e+h/2,Y+h/2*k1); k3=rhs(e+h/2,Y+h/2*k2); k4=rhs(e+h,Y+h*k3)
        Y=Y+h/6*(k1+2*k2+2*k3+k4); store[n+1]=Y
    class _S:
        def __init__(self,g,st): self.g=g; self.st=st
        def sol(self,e):
            j=np.searchsorted(self.g,e); j=min(max(j,1),len(self.g)-1)
            w=(e-self.g[j-1])/(self.g[j]-self.g[j-1])
            return self.st[j-1]*(1-w)+self.st[j]*w
    return _S(eg2,store),nk,NV

def spectrum(nk=None, lmax=900):
    # *** THE SOURCE MODES ARE DISCRETE (sec:largescale, A.58). ***
    #   k_L = sqrt(L(L+2))/r_0,  L >= 2,  and the flat projection puts them at
    #   l_L = sqrt(L(L+2)) D_C/r_0 with the stretch D_C/r_0 = 2.75 fixed parameter-free by Lambda.
    #   No source below L=2, i.e. below l_2 = sqrt(8) x 2.75 = 7.78.
    stretch = 2.75
    Lmax = int(((lmax+400)/stretch)**1)+2
    Ls = np.arange(2, Lmax)
    lL = np.sqrt(Ls*(Ls+2))*stretch
    kk = lL/DM
    keep = lL <= 900.0   # explicit stability cap: h k^2/(3H) < 2.8 fails above ~l=1000          # only modes the spectrum actually needs
    kk = kk[keep]; lL = lL[keep]
    nk = len(kk)
    print(f"  modes: {nk}, highest l_L = {lL[-1]:.0f} (requested lmax={lmax})")
    sol,nk,NV=modes_all(kk)
    yr=sol.sol(eta_rec).reshape(nk,NV)
    sig=yr[:,7]/2
    Psr=yr[:,6]+6*Hc_of(eta_rec)**2*On_of(eta_rec)*sig/kk**2
    SW=yr[:,2]/4+Psr; DP=yr[:,3]/kk
    ee=np.linspace(eta_rec,eta_end,40)
    Yg=np.array([sol.sol(e).reshape(nk,NV) for e in ee])
    Phg=Yg[:,:,6]; sgg=Yg[:,:,7]/2
    Hcv=np.array([Hc_of(e) for e in ee])[:,None]; Onv=np.array([On_of(e) for e in ee])[:,None]
    Psg=Phg+6*Hcv**2*Onv*sgg/kk[None,:]**2
    IS=[np.gradient(Phg[:,i],ee)+np.gradient(Psg[:,i],ee) for i in range(nk)]
    # r_D on THIS rate (C8), anchored the same way as the control
    g=lambda a:(Rb_of(np.interp(a,ag,eg))**2/(1+Rb_of(np.interp(a,ag,eg)))+8/9)/(6*(1+Rb_of(np.interp(a,ag,eg))))
    I=quad(lambda a: ((Rb_rec*a/a_rec)**2/(1+Rb_rec*a/a_rec)+8/9)/(6*(1+Rb_rec*a/a_rec))/Hub(a), a_onset,a_rec,limit=250)[0]
    Hl=lambda a: 67.4*np.sqrt(0.307/(1+3403.6)/a**4+0.307/a**3+0.693)
    Il=quad(lambda a: ((Rb_rec*a/a_rec)**2/(1+Rb_rec*a/a_rec)+8/9)/(6*(1+Rb_rec*a/a_rec))/Hl(a),1e-9,a_rec,limit=250)[0]
    Dl_=quad(lambda a: c/(a**2*Hl(a)),a_rec,1.,limit=250)[0]
    rD=(Dl_/1362.)*np.sqrt(I/Il)
    damp=np.exp(-(kk*rD)**2); SW*=damp; DP*=damp
    # discrete measure: dk_L between neighbours replaces dk
    dk = np.gradient(kk)
    P = kk**(0.965-1)/kk * dk
    ls=np.arange(120,lmax,15); Cl=np.empty(len(ls))
    for j,l in enumerate(ls):
        x=kk*DM
        D_=SW*spherical_jn(int(l),x)+DP*spherical_jn(int(l),x,derivative=True)
        add=np.array([np.trapezoid(IS[i]*spherical_jn(int(l),kk[i]*(eta_0-ee)),ee) for i in range(nk)])
        Cl[j]=np.sum(P*(D_+add)**2)
    return ls, Cl*ls*(ls+1), rD
ls,Dl,rD=spectrum(nk=260, lmax=1250)
print(f"  r_D(CR) = {rD:.2f} Mpc   ->  l_D = {DM/rD:.0f}")
from scipy.signal import argrelextrema as _ar
idx=[q for q in _ar(Dl,np.greater,order=2)[0]]
pk=[(int(ls[q]),Dl[q]) for q in idx[:4]]
print(f"\n  *** CR SPECTRUM ON THE DETERMINED DATUM ***")
print(f"    peaks at l = {[p[0] for p in pk]}")
if len(pk)>=3:
    print(f"    P1/P2 = {pk[0][1]/pk[1][1]:.3f}   P1/P3 = {pk[0][1]/pk[2][1]:.3f}")
print(f"    (A.100 on the flat-delta_g datum gave 150/360/585/840, P1/P2=1.471)")
print(f"    (sky: 220/536/813, P1/P2=2.212, P1/P3=2.257)")
Dn=Dl/Dl[int(np.argmin(np.abs(ls-210)))]
print(f"\n  CR spectrum, normalised at l=210 (l_A={lA:.1f}, l_2={np.sqrt(8)*2.75:.2f}):")
for j in range(0,len(ls),2):
    print(f"    l={ls[j]:>5d}  {Dn[j]:7.4f}  {'#'*max(0,int(30*Dn[j]))}")
