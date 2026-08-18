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
import os
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn
from scipy.optimize import brentq
from scipy.signal import argrelextrema
c=299792.458
H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec); fnu=0.4052; LMAX=20
_SW=lambda n,d: float(os.environ.get('RAD_'+n,d))   # r3042: per-site radiation switches
_S_RATE=_SW('RATE',0.0)   # 0 = geometric (shipped) | 1 = radiation drives the rate
_S_TOT =_SW('TOT', 1.0)   # 1 = Omega denominator includes radiation (shipped) | 0 = rate's own total
_S_SRC =_SW('SRC', 1.0)   # 1 = photons+neutrinos source the potential (shipped) | 0 = they do not
_S_CS  =_SW('CS',  1.0)   # 1 = sound speed carries baryon loading (shipped) | 0 = pure 1/sqrt(3)
_S_NU  =_SW('NU',  1.0)   # 1 = neutrinos present (shipped) | 0 = photons only
_S_MAT =_SW('MAT', 1.0)   # 1 = matter fraction diluted by the same total (shipped) | 0 = vs rate's own
_S_LA  =_SW('LA',301.6)   # the acoustic-scale target the seam datum is solved to
_S_GRAV=_SW('GRAV',0.0)   # 0 = species enter via (3Hc^2/2)Omega (through the rate, shipped)
                          # 1 = every species by its own physical 4piG a^2 rho, symmetrically
Hub=lambda a: H0*np.sqrt(_S_RATE*Or_content/a**4+Om/a**3+OL)                    # *** NO RADIATION TERM ***
Or_content=4.15e-5/(H0/100)**2   # *** omega_r is FIXED by T_CMB; Omega_r = omega_r/h^2.  The old
                                 # form had BOTH scaling factors inverted, giving z_eq=2905 where
                                 # omega_m/omega_r gives 3936 -- 37% too much radiation (r1989). ***
# r2350: the conformal-time grid began at a=1e-5 with eg SEEDED AT ZERO, omitting the
# 4.596 Mpc already elapsed from a=0 (in radiation domination c/(a^2 H) is constant, so the
# missing piece is a/(H0 sqrt(Or))).  Negligible at eta_0 but 12% at z=1e4.  Grid extended and
# seeded; verified against CAMB to 0.01 Mpc across four decades of redshift.  [see r2349]
ag=np.logspace(-7,0,20000)
_eta_seed=float(quad(lambda a: c/(a**2*Hub(a)), 1e-14, ag[0], limit=200)[0])
eg=np.concatenate([[_eta_seed],_eta_seed+cumulative_trapezoid(c/(ag**2*Hub(ag)),ag)])
Hc_of=CubicSpline(eg, ag*Hub(ag)/c)
rt=_S_TOT*Or_content/ag**4+Om/ag**3+OL
Og_of=CubicSpline(eg,(1-_S_NU*fnu)*(Or_content/ag**4)/rt); On_of=CubicSpline(eg,_S_NU*fnu*(Or_content/ag**4)/rt)
Oc_of=CubicSpline(eg,(Om/ag**3)/(rt if _S_MAT else (Om/ag**3+OL))); Rb_of=CubicSpline(eg, Rb_rec*(ag/a_rec))
_H0c=H0/c
_Wr_of=CubicSpline(eg,(3.0/2.0)*(_H0c**2)*Or_content/ag**2)
_Wm_of=CubicSpline(eg,(3.0/2.0)*(_H0c**2)*Om/ag)
eta_rec=float(np.interp(a_rec,ag,eg)); eta_0=eg[-1]
rs_f=lambda zs: quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+_S_CS*Rb_rec*a/a_rec))), 1/(1+zs), a_rec, limit=250)[0]
DM=eta_0-eta_rec
zs=brentq(lambda z: np.pi*DM/rs_f(z)-_S_LA, 1500., 60000.)
a_onset=1/(1+zs); eta_onset=float(np.interp(a_onset,ag,eg)); rs=rs_f(zs); lA=np.pi*DM/rs
print("="*80); print("CRRUN19 — PHASE GATED FOR Psi AS WELL"); print("="*80)
print(f"\n  z_onset={zs:.0f}  eta_onset={eta_onset:.2f}  eta_rec={eta_rec:.1f}  D={DM:.0f}  r_s={rs:.2f}  l_A={lA:.1f}")
eta_end=float(np.interp(min(20*a_rec,1.0),ag,eg))
# ===================== r2372: THE THOMSON OPACITY, and with it the damping =====================
# The CR receipt evolved photons as a PERFECT FLUID: no sigma_gamma, so no Silk damping at all.
# The tight-coupling closure sigma_gamma = A theta/tau' needs only tau', and tau' = n_e sigma_T a is
# a function of the SCALE FACTOR alone -- it does not know which background it is being read on --
# so the same recombination history HIER uses transfers here directly.
# A = 16/45 with polarisation (the standard damping rate's 16/15 term includes it); the amplitude
# rate is half the friction coefficient, which is where the factor 2 comes from (r2361).
# ** r2376+c54.160: this import made the REGISTERED receipt unrunnable from its own directory --
#    RD_diffusion_direct lives only in storyboard_receipts/, so the file exited 1 on ImportError
#    before reaching any computation, and the assertion sweep had to run it from the ORIGIN
#    instead.  A receipt that cannot run where it is registered is not a receipt. **
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.dirname(
    _os.path.abspath(__file__)))), 'storyboard_receipts'))
from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m, xe_total
_Yp = 0.2454
_zg, _xeg = xe_history(lambda z: Hub(1/(1+z))*1e3/Mpc_m, ombh2, _Yp, z_hi=3000.0, z_lo=80.0, n=6000)
_nH0 = n_H0_of(ombh2, _Yp)
def _xe(a):
    z = 1.0/a - 1.0
    xH = float(np.interp(z, _zg[::-1], _xeg[::-1])) if (z <= _zg[0] and z >= _zg[-1]) else (1.0 if z > _zg[0] else float(_xeg[-1]))
    return xe_total(z, xH, _nH0, _Yp, helium=True)
_aa = np.logspace(np.log10(1/(1+3e4)), 0.0, 4000)
_ea = np.array([float(np.interp(x, ag, eg)) for x in _aa])
_tpa = np.array([_xe(x)*_nH0/x**3*sigT*x*Mpc_m for x in _aa])
taup_of = CubicSpline(_ea, _tpa)
_VISC = float(os.environ.get('VISCF','1.0'))*(16.0/45.0)
_NODAMP_CR = os.environ.get('NODAMP','0') == '1'

def modes_all(kk):
    """Solve every mode in ONE system.  State: (nk, 7+LMAX-1) flattened.
    The modes are independent, so this is the identical RHS applied to arrays over k --
    the 360 sequential solve_ivp calls were pure per-call overhead."""
    nk=len(kk); NV=7+(LMAX-1)
    Hcs=Hc_of(eta_onset); Ogs=Og_of(eta_onset); Ons=On_of(eta_onset); Ocs=Oc_of(eta_onset)
    S=(Ogs+Ons)+0.75*Ocs
    # Psi transmits (C1's leg residual); delta_g derived from L1's constraint
    xe=1/np.sqrt(3)
    rr=(Ogs+Ons)/Ocs                      # rho_r/rho_m at the seam
    ksm=Hcs*np.sqrt(1.0+rr)               # THE LEG's horizon wavenumber (r2056)
    xs=(kk/ksm)/np.sqrt(3)
    # ENVELOPE of C1's Psi, not its instantaneous value: 3(sin x - x cos x)/x^3 -> 3/x^2 at large x,
    # matched smoothly to 1 at x->0.  Amplitude transmits, phase gated (A.126) -- for Psi as well.
    Pl=1.0/(1.0+xs**2/3.0)
    Ph0=-Pl                                   # potential a well
    # C4: Theta_hat oscillates freely on the leg from entry at x_e, amplitude flat in k
    A_flat=-(3*(np.sin(xe)-xe*np.cos(xe))/xe**3)/2
    # PHASE RESET (A.126): unbounded tortoise phase leaves nothing to inherit
    That=A_flat*np.ones_like(kk)
    dThat=np.zeros_like(kk)
    Cc=(4.0/3.0)*(Ogs+Ons)+Ocs
    hh=1e-4
    dPl=np.where(xs<1e-6, 0.0,
        (3*(np.sin(xs+hh)-(xs+hh)*np.cos(xs+hh))/np.maximum(np.abs(xs+hh),1e-12)**3
        -3*(np.sin(xs-hh)-(xs-hh)*np.cos(xs-hh))/np.maximum(np.abs(xs-hh),1e-12)**3)/(2*hh))
    dPh0=-dPl*(kk/np.sqrt(3))                       # d Psi/d eta from C1
    # delta_g = 4(Theta_hat - Psi) directly from the leg (C1 + C4), and theta from continuity:
    #   delta_g' = 4(That' - Psi') = -(4/3)theta + 4 Psi'  =>  theta = -3 That' + 6 Psi'
    dg0=4*(That-Ph0)
    th0v=-3*dThat+6*dPh0
    y0=np.zeros((nk,NV))
    y0[:,0]=0.75*dg0; y0[:,1]=th0v; y0[:,2]=dg0; y0[:,3]=th0v
    y0[:,4]=dg0; y0[:,5]=th0v; y0[:,6]=Ph0
    def rhs(e,Y):
        y=Y.reshape(nk,NV)
        dc,tc,dg,tg,dn,tn,Ph=[y[:,j] for j in range(7)]
        F=y[:,7:]
        Hc=Hc_of(e); Rb=Rb_of(e); Ogv=Og_of(e); Onv=On_of(e); Ocv=Oc_of(e)
        sig=F[:,0]/2
        # r2371: SIGN CORRECTED.  The standard relation is k^2(Phi - Psi) = 12 pi G a^2 (rho+p)
        # sigma, i.e. Psi = Phi - (positive) sigma.  This file carried a PLUS.  The neutrino
        # hierarchy here is byte-identical to HIER's -- out[:,7]=(8/15)*tn-(3/5)*kk*F[:,1] -- so
        # sigma has the same sign in both, and HIER pairs it with a MINUS while reproducing
        # CAMB's peak ratios to 0.42%.  Not a compensating convention.  Worth +20% on P1/P2 and
        # +13% on P1/P3, both toward the sky.
        # r2372b: Psi carries the anisotropic stress of BOTH free-streaming species.  HIER has
        # (Onv*sgn + Ogv*sgg); this file had only the neutrino term, because it had no sigma_gamma
        # at all.  The closure above supplies one, so the photon quadrupole enters Psi here too --
        # Omega_gamma is still ~15% of the total at z~1000, exactly where the driving is set.
        _tp = float(taup_of(e))
        _on = (not _NODAMP_CR) and (_tp > float(os.environ.get("TPGATE","0.6")))
        _sgg = (_VISC*tg/_tp) if _on else 0.0
        _slip = (kk**2*Rb**2/(3.0*(1+Rb)**2*_tp)) if _on else 0.0
        _PSG = 0.0 if os.environ.get("NOPSG","0")=="1" else Ogv*_sgg
        Ps=Ph-6*Hc**2*(Onv*sig + _PSG)/kk**2
        Php=((-Hc*Ps-kk**2*Ph/(3*Hc)-(_Wr_of(e)*_S_SRC*((1-_S_NU*fnu)*dg+_S_NU*fnu*dn)+_Wm_of(e)*dc)/(3*Hc)) if _S_GRAV else (-Hc*Ps-kk**2*Ph/(3*Hc)-(Hc/2)*(_S_SRC*(Ogv*dg+Onv*dn)+Ocv*dc)))
        out=np.empty_like(y)
        out[:,0]=-tc+3*Php
        out[:,1]=-Hc*tc+kk**2*Ps
        out[:,2]=-(4/3)*tg+4*Php
        out[:,3]=-(Hc*Rb/(1+Rb))*tg+(kk**2/(1+Rb))*dg/4+kk**2*Ps-kk**2*_sgg/(1+Rb)-_slip*tg
        out[:,4]=-(4/3)*tn+4*Php
        out[:,5]=kk**2*(dn/4-sig)+kk**2*Ps
        out[:,6]=Php
        out[:,7]=(8/15)*tn-(3/5)*kk*F[:,1]
        for i in range(1,LMAX-2):
            l=i+2; out[:,7+i]=kk/(2*l+1)*(l*F[:,i-1]-(l+1)*F[:,i+1])
        out[:,7+LMAX-2]=kk*F[:,LMAX-3]-(LMAX+1)/e*F[:,LMAX-2]
        return out.ravel()
    NS=int(os.environ.get('NS_CR','1400'))
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
    # r2369: the cap is a STEP-SIZE limit (h k^2/(3H) < 2.8), not a modelling choice, so it moves
    # with NS.  Exposed so the pair can be raised together; the truncation at 900 leaves only two
    # genuine peaks above the first and makes the low-l structure unreadable.
    keep = lL <= float(os.environ.get('LCAP','900.0'))
    kk = kk[keep]; lL = lL[keep]
    nk = len(kk)
    print(f"  modes: {nk}, highest l_L = {lL[-1]:.0f} (requested lmax={lmax})")
    sol,nk,NV=modes_all(kk)
    yr=sol.sol(eta_rec).reshape(nk,NV)
    sig=yr[:,7]/2
    Psr=yr[:,6]-6*Hc_of(eta_rec)**2*On_of(eta_rec)*sig/kk**2   # r2371: sign corrected, see above
    SW=yr[:,2]/4+Psr; DP=yr[:,3]/kk
    if os.environ.get('SRCDIAG','0')=='1':
        from scipy.signal import argrelextrema as _are
        _i=_are(np.abs(SW),np.greater,order=6)[0]
        _rs=rs_f(zs)
        print('  SRCDIAG: source SW(k) extrema')
        print('     k         k*r_s/pi      l = k*DM')
        for _q in _i[:7]: print('    %.5f     %7.4f     %8.1f'%(kk[_q],kk[_q]*_rs/np.pi,kk[_q]*DM))
        _d=np.diff(kk[_i][:7])
        print('     spacing in k: %s'%'  '.join('%.5f'%x for x in _d))
        print('     acoustic pi/r_s = %.5f ; ratio = %.4f'%(np.pi/_rs, np.mean(_d)/(np.pi/_rs)))
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
    rD=(Dl_/1362.)*np.sqrt(I/Il)*float(__import__('os').environ.get('RDF','1.0'))
    damp=np.exp(-(kk*rD)**2); SW*=damp; DP*=damp
    # discrete measure: dk_L between neighbours replaces dk
    dk = np.gradient(kk)
    import os as _o
    NS=float(_o.environ.get('NS','0.965'))
    P = kk**(NS-1)/kk * dk
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

# --- ASSERTIONS r2376+c54.160 -------------------------------------------------------------
# Print-only receipt.  P15 sec:refit-bound cites it for the two figures that were corrected at
# r2376+c54.155 -- "places it near ell=150, i.e. at half of ell_* rather than at 0.73" and
# "returns a first-to-second peak ratio of ~1.45 ... the instrument now returns 1.447".  Both
# are pinned here, so the next retune of the handover breaks this gate instead of the sentence
# (the ratio drifted 1.15 -> 1.347 -> 1.407 -> 1.447 while the paper carried 1.15).
_pk_l = [p[0] for p in pk]
assert len(pk) >= 4, f"only {len(pk)} peaks found -- the spectrum lost structure"
assert _pk_l == [150, 360, 555, 780], f"peaks at {_pk_l}, receipt prints [150, 360, 555, 780]"
_p1p2 = pk[0][1] / pk[1][1]; _p1p3 = pk[0][1] / pk[2][1]
assert abs(_p1p2 - 1.447) < 0.003, f"P1/P2 = {_p1p2}, paper and receipt say 1.447"
assert abs(_p1p2 - 1.45) < 0.01, "P15 sec:refit-bound quotes ~1.45 for this run"
assert abs(_p1p3 - 1.715) < 0.003, f"P1/P3 = {_p1p3}, receipt prints 1.715"
# the disagreement the paper RECORDS rather than resolves: 150 against the sky's 220, and the
# ratio well under the measured 2.21.  If either of these ever stopped holding the paragraph
# would be wrong in the other direction, so both bounds are gated.
assert pk[0][0] < 0.75 * 220, "the first peak no longer sits well below the measured 220"
assert abs(pk[0][0] / lA - 0.5) < 0.02, f"first peak / l_A = {pk[0][0]/lA}, paper says half of ell_* not 0.73"
assert _p1p2 < 2.21 * 0.8, "P1/P2 no longer disagrees with the measured 2.21 as the paper records"
# the background this run is built on, all printed and none previously checked
assert abs(zs - 6761.0) < 2.0, f"z_onset = {zs}, receipt prints 6761"
assert abs(lA - 301.6) < 0.1, f"l_A = {lA}, the pinned acoustic scale is 301.6"
assert abs(rs - 135.46) < 0.05, f"r_s = {rs}, receipt prints 135.46"
assert abs(DM - 13005.0) < 5.0, f"D = {DM}, receipt prints 13005"
assert abs(rD - 10.88) < 0.02, f"r_D(CR) = {rD}, receipt prints 10.88 Mpc"
print(f"\n  [assertions r2376+c54.160] peaks 150/360/555/780, P1/P2 1.447, P1/P3 1.715, z_onset 6761: pinned.")
