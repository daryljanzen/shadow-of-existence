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
"""LOS — THE VISIBILITY-WEIGHTED LINE-OF-SIGHT CONTROL.  LambdaCDM background.  r2121.

WHAT IT DOES.  Instantaneous recombination is gone.  The source is integrated along the line of sight
against the visibility g(eta) = tau' exp(-tau), built from the same Peebles ionisation history that
RD_diffusion_direct.py uses for r_D:
    Delta_l(k) = int d eta [ g (Theta_0+Psi) D(k,eta) j_l(x) + g (theta_b/k) D(k,eta) j_l'(x)
                           + exp(-tau) (Phi'+Psi') j_l(x) ],     x = k(eta_0 - eta),
with the diffusion envelope D(k,eta) = exp[-k^2/k_D^2(eta)] ACCUMULATED along the leg (knob DAMPF).

*** THE VISIBILITY IS VALIDATED (r2121). ***
    peak   eta = 276.0 Mpc,  z = 1090       (Planck z_* = 1089.9)
    FWHM   38.1 Mpc -> sigma = 16.2 Mpc     (standard ~19; 15% narrow, NOT wide)
    x_e    z=1090: 0.131 (std ~0.13) | z=900: 0.0124 (std ~0.008) | freeze-out 6.5e-4 (std ~2e-4)
  The freeze-out tail runs ~3x high -- the known limit of bare Peebles without helium.  It inflates a
  VARIANCE of g (51 Mpc) without widening the window; the FWHM is the honest measure.

*** THE OPEN TENSION, AND IT IS NOT TO BE SETTLED BY WHICHEVER FITS. ***
  DAMPF=1 (Silk envelope + finite-thickness smearing):  peaks 216.8/523.6/784.6, P1/P2=2.981, P1/P3=3.528
  DAMPF=0 (smearing only):                              peaks 220.1/524.8/777.6, P1/P2=2.269, P1/P3=2.205
  sky:                                                  peaks 220 /536 /813  , P1/P2=2.212, P1/P3=2.257
  A tight-coupled FLUID carries no viscosity and therefore no Silk damping of its own, so physically
  BOTH effects are real and both belong -- yet including both over-damps by ~25% in power at P3.
  THE CANDIDATE RESOLUTION, to be DERIVED not fitted: the standard k_D^2 envelope is derived for the
  tight-coupling solution evaluated AT last scattering, and its integral already runs THROUGH the
  recombination window.  Smearing that same solution over g re-applies part of the same suppression.
  If so the correct scheme accumulates the envelope only up to the START of the window and lets the
  smearing carry the window's own contribution -- a testable prediction, not a preference.

CONTEXT (r2120-r2121).  Four knobs -- ISW strength, post-recombination photon coupling, damping scale,
Doppler weight -- each trade l_1 against P1/P2 against P1/P3 along a DIFFERENT line, and the sky lies
off all of them.  No coefficient reaches the data, so a term was missing rather than miscalibrated.
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


# ================= the visibility function, from the same ionisation history as r_D =================
from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m
_Yp = 0.2454
_zg, _xeg = xe_history(lambda z: Hub(1/(1+z))*1e3/Mpc_m, ombh2, _Yp, z_hi=3000.0, z_lo=80.0, n=6000)
_nH0 = n_H0_of(ombh2, _Yp)
def _xe_of_a(a):
    z = 1.0/a - 1.0
    return np.where(z >= _zg[0], 1.0, np.where(z <= _zg[-1], _xeg[-1],
                    np.interp(z, _zg[::-1], _xeg[::-1])))
def _taup_of_eta(e):
    """Thomson opacity tau' = n_e sigma_T a, in Mpc^-1."""
    a = np.interp(e, eg, ag)
    return float(_xe_of_a(a))*_nH0/a**3 * sigT * a * Mpc_m

def spectrum(nk=None, lmax=900):
    stretch = 2.75
    Lmax = int(float(os.environ.get('KMAXL','900'))/stretch)+4
    Ls = np.arange(2, Lmax)
    lL = np.sqrt(Ls*(Ls+2))*stretch
    kk = lL/DM
    keep = lL <= float(os.environ.get('KMAXL','900'))
    kk = kk[keep]; lL = lL[keep]; nk = len(kk)
    print("  modes: %d, highest l_L = %.0f" % (nk, lL[-1]))
    sol,nk,NV = modes_all(kk)

    NW = int(os.environ.get('NW','900'))
    ew = np.linspace(max(eta_rec-150.0, eg[1]), eta_rec+260.0, NW)
    el = eta_rec*np.exp(np.linspace(np.log((eta_rec+260.0)/eta_rec), np.log(eta_end/eta_rec), 260))[1:]
    ee = np.concatenate([ew, el])

    tp = np.array([_taup_of_eta(e) for e in ee])
    # tau(eta) = integral from eta to eta_end of tau' d eta  (reionisation ignored)
    seg = (tp[:-1]+tp[1:])/2*np.diff(ee)
    tau = np.concatenate([np.cumsum(seg[::-1])[::-1], [0.0]])
    g = tp*np.exp(-tau)
    norm = np.trapezoid(g, ee)
    ipk = int(np.argmax(g)); ebar = np.trapezoid(g*ee,ee)/norm
    sig_e = np.sqrt(np.trapezoid(g*(ee-ebar)**2,ee)/norm)
    print("  visibility: peak eta=%.1f Mpc (z=%.0f), norm=%.4f, sigma=%.1f Mpc"
          % (ee[ipk], 1/np.interp(ee[ipk],eg,ag)-1, norm, sig_e))

    Rb_e = np.array([Rb_of(e) for e in ee])
    integ = (Rb_e**2/(1+Rb_e) + 8.0/9.0)/(6.0*(1+Rb_e)*tp)
    invkD2 = np.concatenate([[0.0], np.cumsum((integ[:-1]+integ[1:])/2*np.diff(ee))])

    Y = np.array([sol.sol(e).reshape(nk,NV) for e in ee])
    Ph = Y[:,:,6]; sg = Y[:,:,7]/2
    Hcv = np.array([Hc_of(e) for e in ee])[:,None]; Onv = np.array([On_of(e) for e in ee])[:,None]
    Ps = Ph - 6*Hcv**2*Onv*sg/kk[None,:]**2
    MONO = Y[:,:,2]/4 + Ps
    DOPP = Y[:,:,3]/kk[None,:]
    ISWs = np.gradient(Ph,ee,axis=0) + np.gradient(Ps,ee,axis=0)
    # *** THE TIGHT-COUPLING VALIDITY CUT (r2121). ***
    # The Silk envelope comes from the SECOND-ORDER tight-coupling expansion, valid only while
    # k*tau_c << 1 with tau_c = 1/tau'.  Through recombination tau' collapses, so 1/k_D^2 diverges
    # exactly where the visibility has its weight -- the envelope is then being applied outside the
    # regime that derives it.  Per mode, stop accumulating at k*tau_c = 1, i.e. tau'(eta) = k.
    _TC = os.environ.get('TCCUT','1') == '1'
    if _TC:
        inv2 = np.empty((len(ee), len(kk)))
        for _i,_k in enumerate(kk):
            ok = np.where(tp > _k)[0]                 # tight coupling holds while tau' > k
            jstop = ok[-1] if len(ok) else 0
            inv2[:,_i] = np.minimum(invkD2, invkD2[jstop])
        print("  tight-coupling cut: mode k=%.4f freezes at eta=%.1f Mpc; k=%.4f at eta=%.1f Mpc"
              % (kk[0], ee[min(np.where(tp>kk[0])[0][-1], len(ee)-1)],
                 kk[-1], ee[min(np.where(tp>kk[-1])[0][-1], len(ee)-1)]))
    else:
        inv2 = np.repeat(invkD2[:,None], len(kk), axis=1)
    D_k  = np.exp(-(kk[None,:]**2)*inv2*float(os.environ.get('DAMPF','1.0')))
    Sm = g[:,None]*MONO*D_k
    Sd = g[:,None]*DOPP*D_k
    Si = np.exp(-tau)[:,None]*ISWs*float(os.environ.get('ISWF','1.0'))

    NS_ = float(os.environ.get('NS','0.965'))
    dk = np.gradient(kk); P = kk**(NS_-1)/kk * dk
    _DL = int(os.environ.get('DL','5'))
    ls = np.arange(120, lmax, _DL); Cl = np.empty(len(ls))
    x0m = eta_0 - ee
    for j,l in enumerate(ls):
        X = kk[None,:]*x0m[:,None]
        jl  = spherical_jn(int(l), X); jlp = spherical_jn(int(l), X, derivative=True)
        Dl_k = np.trapezoid(Sm*jl + Sd*jlp + Si*jl, ee, axis=0)
        Cl[j] = np.sum(P*Dl_k**2)
    return ls, Cl*ls*(ls+1), np.sqrt(invkD2[ipk])

ls,Dl,rD = spectrum(nk=260, lmax=1250)
print("  r_D at the visibility peak = %.2f Mpc" % rD)
from scipy.signal import argrelextrema as _ar
idx=[q for q in _ar(Dl,np.greater,order=2)[0]]
def _refine(q):
    if q<1 or q>=len(ls)-1: return float(ls[q]), float(Dl[q])
    y0,y1,y2=Dl[q-1],Dl[q],Dl[q+1]; d=y0-2*y1+y2
    if d==0: return float(ls[q]), float(y1)
    t=0.5*(y0-y2)/d; h=float(ls[1]-ls[0])
    return float(ls[q]+t*h), float(y1-0.25*(y0-y2)*t)
pk=[_refine(q) for q in idx[:4]]
print("\n  *** LINE-OF-SIGHT CONTROL (LambdaCDM) ***")
print("    peaks at l =", [round(p[0],1) for p in pk])
if len(pk)>=3: print("    P1/P2 = %.3f   P1/P3 = %.3f" % (pk[0][1]/pk[1][1], pk[0][1]/pk[2][1]))
print("    (Planck 2018 Table 5, arXiv:1807.06205 -- SOURCED r2134:")
print("     peaks 220.6+-0.6 / 538.1+-1.3 / 809.8+-1.0 / 1147.8+-2.3;")
print("     D_l = 5733+-39 / 2586+-23 / 2518+-17 / 1227+-9 uK^2;")
print("     => P1/P2 = 2.2170,  P1/P3 = 2.2768,  P1/P4 = 4.6724)")
