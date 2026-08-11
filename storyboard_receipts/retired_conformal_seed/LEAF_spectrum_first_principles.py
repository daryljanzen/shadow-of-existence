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
"""LEAF — THE CR SPECTRUM ON THE LEAF RATE, FROM FIRST PRINCIPLES.

THE TWO RATES, and every quantity is placed on one of them (r2115):
  * LEAF rate  Hub(a) = H0 sqrt(Or/a^4 + Om/a^3 + OL)   -- CONTENT-CARRYING, radiation included.
    Carries r_s, recombination, the perturbations and the diffusion integral: these are content
    riding on the leaf, and the leaf is the existent.
  * STACKING rate  _Hfol(z) = sqrt(1 + 2(1+z)^3/x0^3)/alpha  -- RADIATION-FREE, from CR's own two
    numbers.  Carries D_M alone, which is measured ACROSS the foliation.
  Putting content physics on the stacking rate is the reification P7's remark forbids.

BACKGROUND: Om = 2/(x0^3+2) with x0 = 1.6648 from DESI DR2; alpha = 16.889 Gly from stellar ages;
  omega_b = 0.02218 from BBN deuterium.  No CMB-derived quantity except n_s (see below).

INITIAL DATA: standard adiabatic growing mode set deep in radiation domination, z = 1e6
  (Phi = const, delta_g = -2 Phi, delta_c = (3/4) delta_g, theta = (k^2 eta/2) Phi).
  The lower limit is a LIMIT, not a transmission surface.

SOURCE MODES ARE DISCRETE: k_L = sqrt(L(L+2))/r_0 for L >= 2 (sec:largescale, A.58), projected to
  l_L = sqrt(L(L+2)) * 2.75, the stretch fixed parameter-free by Lambda.  No source below l_2 = 7.78.

*** THE ONE UNSECURED NUMBER, AND IT IS THE ONE THAT MATTERS (r2120). ***
  r_D is computed here by ANCHORING to LambdaCDM: rD = (D_LCDM/1362) sqrt(I/I_LCDM).  The anchoring
  supplies the Thomson opacity, which the integral I does not carry -- I is
  int da [R^2/(1+R) + 8/9] / [6(1+R)] / H, with no n_e sigma_T a in it.  A direct computation needs
  an ionisation history this file does not contain.
  Anchored, this gives r_D = 10.20 Mpc and P1/P2 = 2.560, P1/P3 = 3.582.
  The ledger's A.154 reports a DIRECT value r_D = 7.987 Mpc, which reproduces its headline exactly
  (verified r2120 by rescaling: P1/P2 = 2.233, P1/P3 = 2.787) -- but that derivation is not in this
  file or anywhere in the bundle.  *** WRITING IT IS THE NAMED NEXT JOB. ***
  Env hook RDF rescales r_D for exactly this test; RDF=0.783 reproduces A.154.

*** AND THE RESIDUAL SITS ON TOP OF IT. *** P1/P2 lands to 0.9% and P1/P3 is 23% low -- a MONOTONIC
  deficit growing with l, the same functional shape as the only k-rising term in the calculation,
  damp = exp[-(k r_D)^2].  The deficit and the diffusion length are one open question.

n_s = 0.965 is a Planck-fitted input, worth a factor 0.957 over l = 225 -> 795 (4%, not the 23%).
  It is the last impure input and should be sourced or marginalised.
CONTROL: the LambdaCDM run at r1975 -- peaks 225/510/810, P1/P2 = 2.299.
"""
import os
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn
from scipy.optimize import brentq
from scipy.signal import argrelextrema
c=299792.458
H0=69.316
Or_content=4.15e-5/(69.316/100)**2; Om=2/(1.6648**3+2); OL=1-Om; ombh2=0.02218; z_rec=1092.0; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec); fnu=0.4052; LMAX=20
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
_Hfol=lambda z: np.sqrt(1+2*(1+z)**3/_x0**3)/_al          # 1/Mpc
from scipy.integrate import quad as _q
DM=_q(lambda a: 1/(a**2*_Hfol(1/a-1)),a_rec,1.0,limit=400)[0]
DM_leaf=eta_0-eta_rec  # kept for reference
zs=1e6   # start deep in the radiation era, adiabatic growing mode; the pole is the LIMIT not a start point
a_onset=1/(1+zs)
from scipy.integrate import quad as _qq
eta_onset=_qq(lambda a: 1/(a**2*Hub(a)/c),1e-14,a_onset,limit=400)[0]  # computed, not interpolated
rs=rs_f(zs); lA=np.pi*DM/rs; rs=rs_f(zs); lA=np.pi*DM/rs
print("="*80); print("LEAF — THE CR SPECTRUM ON THE LEAF RATE"); print("="*80)
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
    Psr=yr[:,6]-6*Hc_of(eta_rec)**2*On_of(eta_rec)*sig/kk**2
    SW=yr[:,2]/4+Psr; DP=yr[:,3]/kk
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
    Yp_bbn = 0.2470
    rD=_rD_direct(lambda z: Hub(1/(1+z)), ombh2, Yp_bbn, z_rec, Rb_rec, "CR leaf rate") \
       *float(__import__('os').environ.get('RDF','1.0'))
    damp=np.exp(-(kk*rD)**2); SW*=damp; DP*=damp
    # discrete measure: dk_L between neighbours replaces dk
    dk = np.gradient(kk)
    import os as _o
    NS=float(_o.environ.get('NS','0.965'))
    P = kk**(NS-1)/kk * dk
    _DL=int(os.environ.get('DL','5'))   # 15 quantised the peaks; 2 over-resolves the mode graininess
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
    """Parabolic sub-grid peak position and height: reading heights at grid points
    undershoots, and undershoots MORE for the narrower high-l peaks, inflating P1/P3."""
    if q<1 or q>=len(ls)-1: return float(ls[q]), float(Dl[q])
    y0,y1,y2=Dl[q-1],Dl[q],Dl[q+1]; d=y0-2*y1+y2
    if d==0: return float(ls[q]), float(y1)
    t=0.5*(y0-y2)/d; h=float(ls[1]-ls[0])
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
