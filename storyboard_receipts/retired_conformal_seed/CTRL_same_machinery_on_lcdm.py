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
"""CTRL — THE IDENTICAL MACHINERY ON LambdaCDM.  The control that licenses reading the CR run.

Same integrator, same discrete source modes, same projection, same direct r_D -- only the background
is swapped to Planck-2018 LambdaCDM on BOTH rates (no stacking/foliation split).

WHY IT EXISTS (r2120).  The CR run's residual was being read against the SKY, which attributes every
deviation to CR.  Run on LambdaCDM, where the input physics is known correct, this machinery gives
    peaks 225/525/795   (sky: 220/536/813)
    P1/P2 = 2.265       (sky 2.212, +2.4%)
    P1/P3 = 2.545       (sky 2.257, +12.8%)
so the peak-position drift and most of the third-peak deficit are MACHINERY, not physics.  The CR run
must therefore be read CONTROL-RELATIVE:  CR/control gives -8.3% at P1/P2 and -4.0% at P1/P3, which
relocates the discrepancy from the third peak to the SECOND and shrinks it from 23% to ~8%.

*** THE MACHINERY'S OWN DEFECTS, to be fixed before any residual is interpreted: ***
  * peak positions: P2 low by 4.9%, P3 low by 2.2% ON LambdaCDM -- a phase error growing with k.
  * P1/P3 high by 12.8% on LambdaCDM.
  * LMAX=20 hierarchy truncation; discrete-mode stretch 2.75; no lensing, no reionisation.
"""
import os
import numpy as np
_FSG=float(os.environ.get('FSG','1.0'))
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn
from scipy.optimize import brentq
from scipy.signal import argrelextrema
c=299792.458
H0=67.40
Or_content=4.15e-5/(67.40/100)**2; Om=0.3150; OL=1-Om; ombh2=0.02237; z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec); fnu=0.4052; LMAX=int(os.environ.get('LMAX','20'))
Hub=lambda a: H0*np.sqrt(Or_content/a**4+Om/a**3+OL)   # LEAF rate: content-carrying (r2115)
   # *** omega_r is FIXED by T_CMB; Omega_r = omega_r/h^2.  The old
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
# D_M is the PROJECTION: measured across the foliation -> STACKING rate (radiation-free)
_x0=1.6648; _al=16.889*306.6
_Hfol=lambda z: Hub(1/(1+z))/c                              # control: one background
from scipy.integrate import quad as _q
DM=_q(lambda a: 1/(a**2*_Hfol(1/a-1)),a_rec,1.0,limit=400)[0]
DM_leaf=eta_0-eta_rec  # kept for reference
zs=1e6   # start deep in the radiation era, adiabatic growing mode; the pole is the LIMIT not a start point
a_onset=1/(1+zs)
from scipy.integrate import quad as _qq
eta_onset=_qq(lambda a: 1/(a**2*Hub(a)/c),1e-14,a_onset,limit=400)[0]  # computed, not interpolated
rs=rs_f(zs); lA=np.pi*DM/rs; rs=rs_f(zs); lA=np.pi*DM/rs
print("="*80); print("CONTROL — THE SAME MACHINERY ON LambdaCDM"); print("="*80)
print(f"\n  z_onset={zs:.0f}  eta_onset={eta_onset:.2f}  eta_rec={eta_rec:.1f}  D={DM:.0f}  r_s={rs:.2f}  l_A={lA:.1f}")
eta_end=float(np.interp(min(20*a_rec,1.0),ag,eg))
def modes_all(kk):
    """Solve every mode in ONE system.  State: (nk, 7+LMAX-1) flattened.
    The modes are independent, so this is the identical RHS applied to arrays over k --
    the 360 sequential solve_ivp calls were pure per-call overhead."""
    nk=len(kk); NV=7+(LMAX-1)
    Hcs=Hc_of(eta_onset); Ogs=Og_of(eta_onset); Ons=On_of(eta_onset); Ocs=Oc_of(eta_onset)
    S=(Ogs+Ons)+0.75*Ocs
    # Standard adiabatic growing mode.  (The retired seam-transmission scheme -- the leg horizon
    # wavenumber, the flat-in-k amplitude A_flat, the gated phase and the four Psi-readings -- was
    # removed at r2115 as an artifact of treating the lower boundary as a transmission surface.)
    Ph0=-np.ones_like(kk)   # scale-invariant potential, unit normalisation
    # ADIABATIC GROWING MODE, super-horizon in radiation domination.  The energy constraint with
    # k^2 phi negligible and phi'=0 gives 3 H^2 psi = -4 pi G a^2 d(rho), i.e. delta = -2 PSI; the
    # Euler equation then gives theta = k^2(delta_g/4 + psi) tau = (k^2 tau/2) PSI.  Both relations
    # are in PSI, not PHI -- and psi = phi/(1+2R_nu/5), so coding them in phi mis-sets the amplitude
    # of delta_g relative to the potentials by 1/(1+0.4 f_nu) = 1.162 (r2120).
    Ps0=Ph0/(1.0+0.4*fnu)
    dg0=-2.0*Ps0
    th0v=(kk**2*eta_onset/2.0)*Ps0
    y0=np.zeros((nk,NV))
    y0[:,0]=0.75*dg0; y0[:,1]=th0v; y0[:,2]=dg0; y0[:,3]=th0v
    y0[:,4]=dg0; y0[:,5]=th0v; y0[:,6]=Ph0
    # ADIABATIC GROWING MODE: psi/phi = 1/(1+2R_nu/5) from the outset (free-streaming neutrinos).
    # Inverting psi = phi - 6 H^2 Om_nu sigma/k^2 fixes sigma_nu; F_2 = 2 sigma.  Setting the
    # hierarchy to zero (as before) starts the mode at psi/phi = 1, which is not the growing mode.
    _fac=1.0-1.0/(1.0+0.4*fnu)
    y0[:,7]=2.0*(Ph0*_fac)*kk**2/(6.0*Hcs**2*Ons)
    def rhs(e,Y):
        y=Y.reshape(nk,NV)
        dc,tc,dg,tg,dn,tn,Ph=[y[:,j] for j in range(7)]
        F=y[:,7:]
        Hc=Hc_of(e); Rb=Rb_of(e); Ogv=Og_of(e); Onv=On_of(e); Ocv=Oc_of(e)
        if _FSG<1.0 and e>eta_rec: Ogv=Ogv*_FSG
        sig=F[:,0]/2
        Ps=Ph-6*Hc**2*Onv*sig/kk**2
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
    NS=int(os.environ.get('NSTEP','1400'))
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
    _OS=int(os.environ.get('OVERSAMPLE','1'))
    if _OS>1:   # CONTINUOUS control: same k range, _OS x finer sampling (no discrete-S^3 claim)
        lL=np.linspace(lL[0],lL[-1],len(lL)*_OS)
    kk = lL/DM
    keep = lL <= float(os.environ.get('KMAXL','900'))   # explicit stability cap: h k^2/(3H) < 2.8 fails above ~l=1000          # only modes the spectrum actually needs
    kk = kk[keep]; lL = lL[keep]
    nk = len(kk)
    print(f"  modes: {nk}, highest l_L = {lL[-1]:.0f} (requested lmax={lmax})")
    sol,nk,NV=modes_all(kk)
    yr=sol.sol(eta_rec).reshape(nk,NV)
    sig=yr[:,7]/2
    Psr=yr[:,6]-6*Hc_of(eta_rec)**2*On_of(eta_rec)*sig/kk**2
    SW=yr[:,2]/4+Psr; DP=float(os.environ.get('DPF','1.0'))*yr[:,3]/kk
    # log-spaced from eta_rec: resolves the EARLY ISW (first few hundred Mpc) as well as the late
    _NE=int(__import__('os').environ.get('NE','400'))
    ee=eta_rec*np.exp(np.linspace(0,np.log(eta_end/eta_rec),_NE))
    Yg=np.array([sol.sol(e).reshape(nk,NV) for e in ee])
    Phg=Yg[:,:,6]; sgg=Yg[:,:,7]/2
    Hcv=np.array([Hc_of(e) for e in ee])[:,None]; Onv=np.array([On_of(e) for e in ee])[:,None]
    Psg=Phg-6*Hcv**2*Onv*sgg/kk[None,:]**2
    IS=[np.gradient(Phg[:,i],ee)+np.gradient(Psg[:,i],ee) for i in range(nk)]
    # r_D COMPUTED DIRECTLY on the leaf rate, with the Thomson opacity carried explicitly and a
    # Peebles ionisation history (RD_diffusion_direct.py, control-validated on LambdaCDM).
    # Nothing anchored.  The old form rD=(D_LCDM/1362)sqrt(I/I_LCDM) used 1362 -- a POWER-spectrum
    # damping multipole -- as an AMPLITUDE scale, and so over-damped by ~1.55 (r2120).
    from RD_diffusion_direct import r_D as _rD_direct
    Yp_bbn = 0.2454
    rD=_rD_direct(lambda z: Hub(1/(1+z)), ombh2, Yp_bbn, z_rec, Rb_rec, "CR leaf rate") \
       *float(__import__('os').environ.get('RDF','1.0'))
    damp=np.exp(-(kk*rD)**2); SW*=damp; DP*=damp
    # discrete measure: dk_L between neighbours replaces dk
    dk = np.gradient(kk)
    import os as _o
    NS=float(_o.environ.get('NS','0.965'))
    P = kk**(NS-1)/kk * dk
    _DL=int(os.environ.get('DL','15'))
    ls=np.arange(120,lmax,_DL); Cl=np.empty(len(ls))
    for j,l in enumerate(ls):
        x=kk*DM
        D_=SW*spherical_jn(int(l),x)+DP*spherical_jn(int(l),x,derivative=True)
        add=np.array([np.trapezoid(IS[i]*spherical_jn(int(l),kk[i]*(eta_0-ee)),ee) for i in range(nk)])
        Cl[j]=np.sum(P*(D_+float(__import__('os').environ.get('ISWF','1.0'))*add)**2)
    return ls, Cl*ls*(ls+1), rD
ls,Dl,rD=spectrum(nk=260, lmax=1250)
print(f"  r_D(CR) = {rD:.2f} Mpc   ->  l_D = {DM/rD:.0f}")
from scipy.signal import argrelextrema as _ar
idx=[q for q in _ar(Dl,np.greater,order=2)[0]]
def _refine(q):
    if q<1 or q>=len(ls)-1: return float(ls[q]), float(Dl[q])
    y0,y1,y2=Dl[q-1],Dl[q],Dl[q+1]; d=y0-2*y1+y2
    if d==0: return float(ls[q]), float(y1)
    t=0.5*(y0-y2)/d                      # sub-grid offset in units of the step
    h=float(ls[1]-ls[0])
    return float(ls[q]+t*h), float(y1-0.25*(y0-y2)*t)
pk=[_refine(q) for q in idx[:4]]
print(f"\n  *** CR SPECTRUM ON THE DETERMINED DATUM ***")
print(f"    peaks at l = {[round(p[0],1) for p in pk]}")
if len(pk)>=3:
    print(f"    P1/P2 = {pk[0][1]/pk[1][1]:.3f}   P1/P3 = {pk[0][1]/pk[2][1]:.3f}")
print(f"    (A.100 on the flat-delta_g datum gave 150/360/585/840, P1/P2=1.471)")
print(f"    (sky: 220/536/813, P1/P2=2.212, P1/P3=2.257)")
Dn=Dl/Dl[int(np.argmin(np.abs(ls-210)))]
print(f"\n  CR spectrum, normalised at l=210 (l_A={lA:.1f}, l_2={np.sqrt(8)*2.75:.2f}):")
for j in range(0,len(ls),2):
    print(f"    l={ls[j]:>5d}  {Dn[j]:7.4f}  {'#'*max(0,int(30*Dn[j]))}")
