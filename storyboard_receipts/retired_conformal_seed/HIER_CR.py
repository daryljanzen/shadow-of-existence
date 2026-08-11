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
"""HIER — THE PHOTON BOLTZMANN HIERARCHY.  LambdaCDM control.  NO DAMPING ENVELOPE ANYWHERE.  r2122.

WHY IT EXISTS, and the result that forced it (r2121).  A tight-coupled FLUID plus a Silk envelope
cannot represent Silk damping, because the damping is generated exactly where the fluid description
fails.  Measured, against the damping present at last scattering:
    fraction accumulated while the tight-coupling expansion is VALID (k*tau_c <= 0.1)
        P1 (l=220): 52.9%      P2 (l=536): 32.2%      P3 (l=813): 25.8%
so ~3/4 of the third peak's damping arises outside the regime that derives the envelope -- and the
shortfall is MODE-DEPENDENT, which is why no single envelope coefficient ever converged and why four
knobs (ISW strength, post-recombination coupling, damping scale, Doppler weight) each traded l_1
against P1/P2 against P1/P3 along a different line with the sky off all of them.
*** r_D IS NO LONGER AN INPUT TO ANYTHING.  The calculation produces its own damping. ***

STRUCTURE.  Tight coupling early (the photon equations are stiff: tau' ~ (1+z)^2), switching to the
full hierarchy at tau' = TPSW (default 0.6/Mpc, eta = 228.4 Mpc, z = 1394) -- late enough for an
explicit step to carry it, early enough that tight coupling is still good there.  At handover F_g2 is
seeded with its quasi-static tight-coupling value (16/27) theta_g / tau', higher multipoles zero.
Photon multipoles F_gl with Thomson terms, no polarisation (the 8/9 closure).  Source integrated along
the line of sight against g = tau' exp(-tau); Doppler uses the BARYON velocity.

*** CONVERGED IN MULTIPOLES: LG=LN=12, 20 and 32 give P1/P2 = 2.654 / 2.657 / 2.657. ***
Truncation is not an issue even though k*eta reaches ~18 at recombination.

*** WHERE IT STANDS, and the two problems are now SEPARATE. ***
                        l_1      P1/P2    P1/P3
    hierarchy, ISW on   213.2    2.657    3.193
    hierarchy, ISW off  231.4    1.919    2.463
    sky                 220      2.212    2.257
  (1) P1/P3 cannot reach 2.257 at ANY ISW strength -- its floor is 2.463 with the ISW off.  So there
      is ~9% genuine excess damping, independent of the ISW.  Much smaller than the 3.193 suggested.
  (2) The ISW is doing far too much work: switching it off swings P1/P2 by 38%, where in the fluid
      version it was modest.

*** THE DIAGNOSED CAUSE OF (2), and the named next build. ***
  BARYONS ARE LUMPED WITH CDM IN THE DENSITY SOURCE.  There is ONE matter perturbation `dc` weighted
  by the TOTAL Omega_m, while theta_b is evolved separately.  So before decoupling the baryons are
  treated as clustering like CDM when physically they are dragged by the photons and do NOT collapse.
  That over-builds the potentials through recombination and inflates both the driving and the ISW.
  FIX: carry delta_b as its own variable, delta_b' = -theta_b + 3 Phi' with the theta_b already here,
  and split the Poisson source into Omega_c delta_c + Omega_b delta_b.
  This is also the quantity the SECOND-PEAK question turns on (baryon loading), so it must be exact.
"""
import os
import numpy as np
from scipy.optimize import brentq
import numpy as np
_FSG=float(os.environ.get('FSG','1.0'))
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.special import spherical_jn

from scipy.signal import argrelextrema
c=299792.458
H0=69.316                                    # CR: from x0 and alpha, not fitted to the CMB
_x0=1.6648                                   # DESI DR2
# omega_r = omega_gamma (1 + 0.2271 N_eff), N_eff = 3.046 -- was 4.15e-5, 0.8% low (r2138)
Or_content=4.1833e-5/(69.316/100)**2; Om=2/(_x0**3+2); OL=1-Om
ombh2=0.02218; z_rec=1092.0; a_rec=1/(1+z_rec)   # omega_b from BBN deuterium
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec); fnu=float(os.environ.get('FNU','0.4089')); LMAX=int(os.environ.get('LMAX','20'))
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
_Ob0=ombh2/(H0/100.)**2                                   # baryons, from omega_b h^2
Ob_of=CubicSpline(eg,(_Ob0/ag**3)/rt); Ocdm_of=CubicSpline(eg,((Om-_Ob0)/ag**3)/rt)
eta_rec=float(np.interp(a_rec,ag,eg)); eta_0=eg[-1]
rs_f=lambda zs: quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))), 1/(1+zs), a_rec, limit=250)[0]
# D_M is the PROJECTION: measured across the foliation -> STACKING rate (radiation-free)
_x0=1.6648; _al=16.889*306.6
_al=16.889*306.6                             # alpha in Mpc, from stellar ages
_Hfol=lambda z: np.sqrt(1+2*(1+z)**3/_x0**3)/_al   # STACKING rate, 1/Mpc, RADIATION-FREE
from scipy.integrate import quad as _q
DM=_q(lambda a: 1/(a**2*_Hfol(1/a-1)),a_rec,1.0,limit=400)[0]
# L3: content evolves on the LEAF (eta), but the ANGULAR projection distance is measured ACROSS the
# foliation, i.e. on the stacking rate.  D_of(eta) is built by mapping leaf-time -> z -> stacking
# distance, and is used for BOTH the source and the ISW (LEAF used DM for one and eta_0-eta for the
# other, which is inconsistent).
_zg_d=np.concatenate([[0.],np.logspace(-4,np.log10(3000.),4000)])
_Dg=np.concatenate([[0.],cumulative_trapezoid(1.0/_Hfol(_zg_d),_zg_d)])
_D_of_z=CubicSpline(_zg_d,_Dg)
D_of=lambda e: _D_of_z(np.clip(1.0/np.interp(e,eg,ag)-1.0,0.,3000.))

DM_leaf=eta_0-eta_rec  # kept for reference
zs=1e6   # start deep in the radiation era, adiabatic growing mode; the pole is the LIMIT not a start point
a_onset=1/(1+zs)
from scipy.integrate import quad as _qq
eta_onset=_qq(lambda a: 1/(a**2*Hub(a)/c),1e-14,a_onset,limit=400)[0]  # computed, not interpolated
rs=rs_f(zs); lA=np.pi*DM/rs; rs=rs_f(zs); lA=np.pi*DM/rs
print("="*80); print("CR — THE PHOTON HIERARCHY ON THE TWO-RATE BACKGROUND"); print("="*80)
print(f"\n  Om={Om:.4f} (from x0={_x0})  z_onset={zs:.0f}  eta_rec={eta_rec:.1f}  D_stack={DM:.0f}  D_leaf={eta_0-eta_rec:.0f}  r_s={rs:.2f}  l_A={lA:.1f}")
eta_end=float(os.environ.get('ETAEND', np.interp(min(20*a_rec,1.0),ag,eg)))
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


# ================= the ionisation history (shared with r_D and the visibility) =================
from RD_diffusion_direct import xe_history, n_H0_of, sigT, Mpc_m, xe_total
_Yp = 0.2470
_zg, _xeg = xe_history(lambda z: Hub(1/(1+z))*1e3/Mpc_m, ombh2, _Yp, z_hi=3000.0, z_lo=80.0, n=6000)
_nH0 = n_H0_of(ombh2, _Yp)
_XEF = float(os.environ.get('XEF','1.0'))   # scale the frozen-out residual tail (test r2124)
_HE = os.environ.get('NOHE','0') != '1'
def _xe(a):
    """n_e / n_H -- the quantity the Thomson opacity needs, INCLUDING helium (r2133)."""
    z = 1.0/a - 1.0
    if z >= _zg[0]: xH = 1.0
    else:
        xH = _xeg[-1] if z <= _zg[-1] else float(np.interp(z, _zg[::-1], _xeg[::-1]))
        if xH < 1e-3: xH = xH*_XEF          # frozen-out residual tail (tested r2124: negligible)
    return xe_total(z, xH, _nH0, _Yp, helium=_HE)
_ea = np.linspace(eg[1], eta_end, 20000)
_aa = np.interp(_ea, eg, ag)
_tpa = np.array([_xe(x)*_nH0/x**3*sigT*x*Mpc_m for x in _aa])
taup_of = CubicSpline(_ea, _tpa)
_seg = (_tpa[:-1]+_tpa[1:])/2*np.diff(_ea)
_tau = np.concatenate([np.cumsum(_seg[::-1])[::-1], [0.0]])
tau_of = CubicSpline(_ea, _tau)
g_of   = CubicSpline(_ea, _tpa*np.exp(-_tau))

_NODAMP = os.environ.get('NODAMP','0')=='1'
_NODAMPTH = os.environ.get('NODAMPTH','0')=='1'   # damping off in theta ONLY; Psi untouched
LG = int(os.environ.get('LG','12'))     # photon multipoles kept
LN = int(os.environ.get('LN','12'))     # neutrino multipoles kept
# state: 0 dc 1 tc 2 dg 3 tg 4 dn 5 tn 6 Ph 7 tb  then Fg2..FgLG then Fn2..FnLN
_POL = os.environ.get('POL','0') == '1'          # photon polarisation (E-mode hierarchy G_l)
LGP = LG if _POL else 0
NV = 9 + (LG-1) + (LN-1) + (LGP+1 if _POL else 0)
IG = 9; IN = 9 + (LG-1); IP = 9 + (LG-1) + (LN-1)   # G_0 .. G_LGP at IP..

def _rhs(e, y, kk, tight):
    dc,tc,dg,tg,dn,tn,Ph,tb,db = [y[:,j] for j in range(9)]
    Fg = y[:,IG:IG+LG-1]; Fn = y[:,IN:IN+LN-1]
    Hc=Hc_of(e); Rb=Rb_of(e); Ogv=Og_of(e); Onv=On_of(e); tp=float(taup_of(e))
    Ocv=Ocdm_of(e); Obv=Ob_of(e)
    sgn = Fn[:,0]/2
    # sigma_gamma = A theta/tau' with A DERIVED from the standard Silk formula:
    #   r_D^2 = Int deta/[6(1+R)tau'] [R^2/(1+R) + 16/15]  ->  for R->0, Int deta (8/45)/tau'
    # and theta' contains -k^2 sigma_gamma, giving Int k^2 A deta/tau'.  Hence A = 8/45.
    # The old 16/45 was exactly TWICE this -- a factor-2 excess in the tight-coupling
    # viscosity, where most of the damping accumulates (r2163).
    _visc = float(os.environ.get('VISCF','1.0'))*((8.0/45.0) if _POL else (4.0/27.0))
    # r2198: NODAMP zeroes sigma_gamma EVERYWHERE -- including in Psi, where it changes the
    # POTENTIALS, not just the damping.  So it is not a clean undamped reference and the
    # r_D^2 extracted from it (r2197) was measuring two effects at once.  NODAMPTH removes
    # sigma_gamma ONLY from the theta equation, leaving Psi's anisotropic stress intact.
    sgg = np.zeros_like(tg) if _NODAMP else np.where(tight, _visc*tg/max(tp,1e-30), Fg[:,0]/2)
    sgg_th = np.zeros_like(sgg) if _NODAMPTH else sgg     # what the theta equation sees
    # Psi carries the anisotropic stress of BOTH free-streaming species.  Before decoupling
    # sigma_gamma is negligible; after it the photons free-stream and Omega_gamma is still ~15% of
    # the total at z~1000 -- exactly the epoch the early ISW integrates over (r2133).
    _PSG = 0.0 if os.environ.get('NOPSG','0')=='1' else Ogv*sgg
    Ps = Ph - 6*Hc**2*(Onv*sgn + _PSG)/kk**2
    # BARYONS ARE NOT CDM.  Before decoupling theta_b = theta_gamma, so delta_b is dragged by the
    # photons and does NOT collapse; lumping it with delta_c over-builds the potentials (r2122).
    Php = -Hc*Ps - kk**2*Ph/(3*Hc) - (Hc/2)*(Ogv*dg+Onv*dn+Ocv*dc+Obv*db)
    out = np.zeros_like(y)
    out[:,0] = -tc + 3*Php
    out[:,1] = -Hc*tc + kk**2*Ps
    # SECOND-ORDER TIGHT COUPLING (r2150).  Setting theta_b = theta_g is FIRST order and leaves the
    # slip identically zero (verified r2149: S/S_closed-form = 0.00 through tight coupling).  Here tg
    # is the COMBINED velocity, (1+R)theta = theta_g + R theta_b, and the slip is quasi-static:
    #     S = theta_b - theta_g = (tau_c R/(1+R)) ( -H theta - k^2 delta_g/4 ),
    # so theta_g = theta - R S/(1+R) and theta_b = theta + S/(1+R).
    if tight and not _NODAMP:
        _S = (R_SLIP := (Rb/((1+Rb)*max(tp,1e-30)))) * (-Hc*tg - kk**2*dg/4)
        _tg_ph = tg - Rb*_S/(1+Rb)
    else:
        _S = np.zeros_like(tg); _tg_ph = tg
    out[:,2] = -(4/3)*_tg_ph + 4*Php
    out[:,4] = -(4/3)*tn + 4*Php
    out[:,5] = kk**2*(dn/4 - sgn) + kk**2*Ps
    out[:,6] = Php
    out[:,8] = -tb + 3*Php          # delta_b' = -theta_b + 3 Phi'
    if tight:
        # one-fluid: photons and baryons share a velocity; drag carried exactly
        # Combined photon-baryon momentum with theta_g = theta_b:
        #   (1+R) theta' = k^2 dg/4 - k^2 sigma_g + (1+R) k^2 Psi - H R theta
        # so the VISCOSITY term carries 1/(1+R) like the pressure term.  It did not (r2126) --
        # a factor (1+R) of excess damping through tight coupling: 1.4x at the switch, 1.6x at
        # recombination.
        # THE BARYON-PHOTON SLIP (second-order tight coupling).  Setting theta_b = theta_g exactly
        # is FIRST order and omits the slip, which supplies the R^2/(1+R) term of the standard
        # damping rate Gamma = (k^2/6(1+R)tau')[R^2/(1+R) + 16/15].  The viscosity term above
        # reproduces the 16/15 part exactly; this adds the missing R^2/(1+R) part.  The amplitude
        # damping rate is half the friction coefficient, hence the factor 2.
        _slip = 0.0 if _NODAMP else (kk**2*Rb**2/(3.0*(1+Rb)**2*max(tp,1e-30)))
        out[:,3] = -(Hc*Rb/(1+Rb))*tg + (kk**2/(1+Rb))*dg/4 + kk**2*Ps - kk**2*sgg_th/(1+Rb) - _slip*tg
        out[:,7] = out[:,3]
    else:
        out[:,3] = kk**2*(dg/4 - sgg_th) + kk**2*Ps + tp*(tb - tg)
        out[:,7] = -Hc*tb + kk**2*Ps + (tp/Rb)*(tg - tb)
        if _POL:
            G = y[:,IP:IP+LGP+1]
            Pi = Fg[:,0] + G[:,0] + G[:,2]                       # Pi = F_g2 + G_0 + G_2
            out[:,IG] = (8/15)*tg - (3/5)*kk*Fg[:,1] + tp*(-Fg[:,0] + Pi/10.)
            out[:,IP]   = -kk*G[:,1] + tp*(-G[:,0] + Pi/2.)
            out[:,IP+1] = (kk/3)*(G[:,0] - 2*G[:,2]) - tp*G[:,1]
            out[:,IP+2] = (kk/5)*(2*G[:,1] - 3*G[:,3]) + tp*(-G[:,2] + Pi/10.)
            for l in range(3, LGP):
                out[:,IP+l] = kk/(2*l+1)*(l*G[:,l-1] - (l+1)*G[:,l+1]) - tp*G[:,l]
            out[:,IP+LGP] = kk*G[:,LGP-1] - (LGP+1)/e*G[:,LGP] - tp*G[:,LGP]
        else:
            out[:,IG] = (8/15)*tg - (3/5)*kk*Fg[:,1] - 0.9*tp*Fg[:,0]
        for i in range(1, LG-2):
            l = i+2
            out[:,IG+i] = kk/(2*l+1)*(l*Fg[:,i-1] - (l+1)*Fg[:,i+1]) - tp*Fg[:,i]
        out[:,IG+LG-2] = kk*Fg[:,LG-3] - (LG+1)/e*Fg[:,LG-2] - tp*Fg[:,LG-2]
    out[:,IN] = (8/15)*tn - (3/5)*kk*Fn[:,1]
    for i in range(1, LN-2):
        l = i+2
        out[:,IN+i] = kk/(2*l+1)*(l*Fn[:,i-1] - (l+1)*Fn[:,i+1])
    out[:,IN+LN-2] = kk*Fn[:,LN-3] - (LN+1)/e*Fn[:,LN-2]
    return out

def evolve(kk):
    nk = len(kk); kk2 = kk[:,None] if False else kk
    Hcs=Hc_of(eta_onset); Ogs=Og_of(eta_onset); Ons=On_of(eta_onset)
    Ph0 = -np.ones(nk)
    Ps0 = Ph0/(1.0+0.4*fnu)
    dg0 = -2.0*Ps0
    th0 = (kk**2*eta_onset/2.0)*Ps0
    y = np.zeros((nk,NV))
    y[:,0]=0.75*dg0; y[:,1]=th0; y[:,2]=dg0; y[:,3]=th0
    y[:,4]=dg0; y[:,5]=th0; y[:,6]=Ph0; y[:,7]=th0; y[:,8]=0.75*dg0
    y[:,IN]=2.0*(Ph0*(1.0-1.0/(1.0+0.4*fnu)))*kk**2/(6.0*Hcs**2*Ons)
    # switch where the explicit step can carry the hierarchy AND tight coupling is still good
    TPS = float(os.environ.get('TPSW','0.6'))
    e_sw = float(brentq(lambda e: float(taup_of(e))-TPS, eg[1]+1e-6, eta_rec+60))
    NS1 = int(os.environ.get('NS1','3000')); NS2 = int(os.environ.get('NS2','5000'))
    g1 = np.linspace(eta_onset, e_sw, NS1+1)
    # TWO-STAGE GRID (r2154).  A single uniform grid to eta_0 gives h~5 Mpc against a 16 Mpc
    # visibility width -- three points across last scattering.  Fine through the visibility and
    # the early ISW, coarse for the late ISW, which varies on ~1000 Mpc scales.
    _EFINE = min(float(os.environ.get('EFINE','900')), eta_end)
    g2 = np.linspace(e_sw, _EFINE, NS2+1)
    g3 = (np.linspace(_EFINE, eta_end, int(os.environ.get('NS3','900'))+1)
          if eta_end > _EFINE + 1 else None)
    e_sw_marker=[1e9]
    store_e=[]; store_y=[]; _ESTORE=float(os.environ.get('ESTORE', eta_rec-160.0)); _STRIDE=int(os.environ.get('STRIDE','3'))
    # PER-MODE INTEGRATION WINDOW (r2136).  The free-streaming hierarchy is only stable while
    # LG > k*eta; past that the truncation reflects and the mode blows up.  But a mode that far
    # sub-horizon has had its potential decay to nothing and contributes no ISW, so it can simply
    # be FROZEN.  This lets the low-k modes -- the only ones that carry the ISW at the l we report
    # -- run on to late times, instead of a global ETAEND cutting off an ongoing Phi decay at z=362.
    # 0.7 was too generous: at KMAXL=3400 a mode went non-finite at k*eta = 0.62*LG,
    # BEFORE its freeze.  The truncation destabilises below the cap (r2141).
    # r2193: the step-size hypothesis (freeze on h*k) is FALSIFIED -- HKCAP at 2.0, 1.0, 0.5
    # and 0.35 all blow up where KETACAP=0.4 is stable.  The k*eta criterion is retained as
    # the DEFAULT and its mechanism is NOT understood; HKCAP is left available but inert.
    # r2194: the STEP-SIZE criterion is correct after all -- r2193 falsified it prematurely by
    # scanning only to HKCAP=0.35 and stopping one step above the working range.  Isolation:
    #   single-stage NS2=1800 -> all stable;  NS2=1300 -> k=0.19 blows at eta=751 (FINE step);
    #   two-stage added       -> k=0.05/0.10/0.19 blow just past EFINE (COARSE step).
    # Both are step-size failures.  h*k < 0.08 covers both and is now the DEFAULT criterion;
    # the legacy k*eta cap is off by default (KETACAP>=9 disables it).
    _CAP = float(os.environ.get('KETACAP','9.9'))
    _HK  = float(os.environ.get('HKCAP','0.08'))     # RK4 step-size limit: freeze when h*k > HKCAP
    def march(grid, tight):
        nonlocal y
        h = grid[1]-grid[0]
        for n in range(len(grid)-1):
            e=grid[n]
            # r2193: the freeze criterion was k*eta < CAP*min(LG,LN), read as "past the
            # truncation's reach".  IT IS NOT ABOUT THE TRUNCATION.  With a SINGLE-stage grid the
            # hierarchy runs stably to k*eta/LG = 2.85 for every mode to k=0.19 (freeze fully off);
            # the blow-ups occur only with the COARSE second stage, i.e. it is an explicit-RK4
            # STEP-SIZE limit, h*lambda < ~2.8 with lambda ~ k the multipole-advection rate.
            # So the criterion is on h*k, not on k*eta/LG -- which is why one global k*eta cap was
            # simultaneously 7x too tight for the fine stage and load-bearing for the coarse one.
            live = (kk*h) < _HK
            if _CAP < 9.0:                     # legacy behaviour retained under KETACAP<9
                live = live & ((kk*e) < _CAP*min(LG,LN))
            if not live.any(): break
            k1=_rhs(e,y,kk,tight); k2=_rhs(e+h/2,y+h/2*k1,kk,tight)
            k3=_rhs(e+h/2,y+h/2*k2,kk,tight); k4=_rhs(e+h,y+h*k3,kk,tight)
            dy = h/6*(k1+2*k2+2*k3+k4)
            dy[~live,:] = 0.0                      # frozen: past the truncation's reach
            y = y + dy
            if grid[n+1] > _ESTORE and (n % _STRIDE)==0:
                # STORE ONLY WHAT THE SOURCE NEEDS (r2142).  In the line-of-sight formalism the
                # high photon multipoles never enter the spectrum -- the projection j_l generates
                # them.  The source needs Theta_0, theta_b, Phi, sigma_nu, sigma_gamma and Pi: six
                # numbers, not NV~700.  This is what lets LG run high enough to be stable.
                store_e.append(grid[n+1])
                _Pi = (y[:,IG]+y[:,IP]+y[:,IP+2]) if _POL else y[:,IG]
                _Rb_s=Rb_of(grid[n+1]); _tp_s=max(float(taup_of(grid[n+1])),1e-30)
                _Ss=(_Rb_s/((1+_Rb_s)*_tp_s))*(-Hc_of(grid[n+1])*y[:,3]-kk**2*y[:,2]/4) \
                    if grid[n+1] <= e_sw_marker[0] else np.zeros_like(y[:,3])
                # sigma_gamma: during TIGHT COUPLING F_2 is not evolved -- it is computed on the
                # fly as _visc*theta/tau' -- so storing y[:,IG]/2 recorded ZERO there (r2169).
                # Store the value actually in use in each phase.
                _vs = float(os.environ.get('VISCF','1.0'))*((8.0/45.0) if _POL else (4.0/27.0))
                _sg_s = ((_vs*y[:,3]/max(float(taup_of(grid[n+1])),1e-30))
                         if (tight and not _NODAMP) else y[:,IG]/2)
                # r2202: column 6 = delta_c.  The store kept 6 columns (r2142) and delta_c was not
                # among them, so the CDM transfer could not be compared like-for-like across
                # redshift -- Phi ~ delta_c/k^2 holds only in matter domination, which invalidated
                # every high-z localisation of the T(k) slope error.
                store_y.append(np.stack([y[:,2]/4, y[:,7]+_Ss/(1+_Rb_s), y[:,6],
                                         y[:,IN]/2, _sg_s, _Pi, y[:,0]], axis=1).astype(np.float32))
    e_sw_marker[0]=e_sw
    march(g1, True)
    # hand over: seed F_g2 with its tight-coupling value, AND the higher multipoles with their
    # quasi-static tight-coupling values F_l = [l/(2l+1)](k/tau') F_{l-1} (r2163).  Setting them to
    # ZERO leaves F_2 undrained, so sigma_gamma and the viscosity are too large -- excess damping,
    # and the error is LINEAR IN k because the seed is.  This is the k-dependent omission at the
    # handover that r2162 localised.
    _tp_sw = float(taup_of(e_sw))
    if _POL:
        # F_2 = 2 sigma_gamma, and the tight-coupling phase runs sigma_gamma = (16/45) theta/tau'
        # (_visc above), so the seed must be (32/45), not (64/45): the old value DOUBLED
        # sigma_gamma across the handover and hence doubled the viscosity (r2163).
        # r2198: F_2 = 2 sigma_gamma and the phase runs sigma_gamma = _visc*theta/tau' with
        # _visc = 8/45 (r2163), so the seed is 16/45 -- NOT 32/45.  r2163 set 32/45 assuming
        # _visc = 16/45 and then halved _visc in the SAME revision without re-deriving the
        # seed; r2169 flagged it and the test that dismissed it was convention-blocked.
        y[:,IG] = float(os.environ.get('F2SEED','16.0'))/45.0*y[:,3]/_tp_sw
        _Pi = 2.5*y[:,IG]                            # Pi = F_2 + G_0 + G_2 with G_0=Pi/2, G_2=Pi/10
        y[:,IP] = _Pi/2.0; y[:,IP+2] = _Pi/10.0
    else:
        y[:,IG] = (16.0/27.0)*y[:,3]/_tp_sw
    _SEED = int(os.environ.get('SEEDHI','1'))
    if _SEED:
        for _i in range(1, LG-1):                      # F_3 .. up the tower
            _l = _i + 2
            y[:,IG+_i] = (_l/(2.0*_l+1.0))*(kk/_tp_sw)*y[:,IG+_i-1]
            if np.max(np.abs(y[:,IG+_i])) < 1e-30: break
        if _POL:
            for _i in range(3, LG):                    # G_3 .. (G_0,G_2 already set)
                _l = _i
                y[:,IP+_i] = (_l/(2.0*_l+1.0))*(kk/_tp_sw)*y[:,IP+_i-1]
                if np.max(np.abs(y[:,IP+_i])) < 1e-30: break
    march(g2, False)
    if g3 is not None: march(g3, False)
    print("  hierarchy switch at eta=%.1f Mpc (tau'=%.2f/Mpc, z=%.0f);  LG=%d LN=%d"
          % (e_sw, TPS, 1/np.interp(e_sw,eg,ag)-1, LG, LN))
    return np.array(store_e), np.array(store_y), e_sw

def spectrum(lmax=900):
    stretch=2.75; Lmax=int(float(os.environ.get('KMAXL','900'))/stretch)+4
    Ls=np.arange(2,Lmax); lL=np.sqrt(Ls*(Ls+2))*stretch
    _OS=int(os.environ.get('OVERSAMPLE','1'))
    if _OS>1: lL=np.linspace(lL[0],lL[-1],len(lL)*_OS)   # continuous-limit test of the k-sum
    kk=lL/DM; keep=lL<=float(os.environ.get('KMAXL','900')); kk=kk[keep]; lL=lL[keep]
    print("  modes: %d, highest l_L = %.0f"%(len(kk),lL[-1]))
    E,Y,e_sw = evolve(kk)
    m = E > max(e_sw, eta_rec-160.0)
    ee = E[m]; Yv = Y[m]
    g = np.array([float(g_of(e)) for e in ee]); tau = np.array([float(tau_of(e)) for e in ee])
    # compact store columns: 0 Theta_0, 1 theta_b, 2 Phi, 3 sigma_nu, 4 sigma_gamma, 5 Pi
    Ph=Yv[:,:,2]; sgn=Yv[:,:,3]
    Hcv=np.array([Hc_of(e) for e in ee])[:,None]; Onv=np.array([On_of(e) for e in ee])[:,None]
    _sgg_s = Yv[:,:,4]
    Ogvv = np.array([Og_of(e) for e in ee])[:,None]
    Ps = Ph - 6*Hcv**2*(Onv*sgn + (0.0 if os.environ.get('NOPSG','0')=='1' else Ogvv*_sgg_s))/kk[None,:]**2
    MONO = Yv[:,:,0] + Ps
    if _POL:
        _Pi_s = Yv[:,:,5]
        # Seljak-Zaldarriaga source is g(Theta_0 + Psi + Pi_Theta/4) with Pi in THETA normalisation.
        # Our F,G are Ma-Bertschinger multipoles, 4x the Theta-normalised ones (Theta_l = F_l/4),
        # so Pi_Theta = Pi_F/4 and the term is Pi_F/16.
        # NOT added to MONO: a QUADRUPOLE source does not project with j_l.  Its kernel is
        # (3 j_l'' + j_l)/2, and by the Bessel equation j_l'' = -(2/x) j_l' + (l(l+1)/x^2 - 1) j_l,
        # so the kernel is  -3 j_l'/x + (3 l(l+1)/(2 x^2) - 1) j_l.   Using j_l for it is an
        # O(k tau_c) error -- LINEAR in k, which is the signature r2165 measured (r2166).
    DOPP = Yv[:,:,1]/kk[None,:]           # BARYON velocity, as it should be
    ISWs = np.gradient(Ph,ee,axis=0)+np.gradient(Ps,ee,axis=0)
    Sm = g[:,None]*MONO; Sd = g[:,None]*DOPP
    Sq = (g[:,None]*_Pi_s/16.0) if _POL else None      # quadrupole source, own kernel below
    Si = np.exp(-tau)[:,None]*ISWs*float(os.environ.get('ISWF','1.0'))
    NS_=float(os.environ.get('NS','0.965')); dk=np.gradient(kk); P=kk**(NS_-1)/kk*dk
    _DL=int(os.environ.get('DL','15')); ls=np.arange(int(os.environ.get('LMIN','120')),lmax,_DL); Cl=np.empty(len(ls))
    x0m = np.array([float(D_of(e)) for e in ee])   # stacking-rate distance, not eta_0-eta
    for j,l in enumerate(ls):
        X=kk[None,:]*x0m[:,None]
        jl=spherical_jn(int(l),X); jlp=spherical_jn(int(l),X,derivative=True)
        _int = Sm*jl + Sd*jlp + Si*jl
        if Sq is not None and int(os.environ.get('QKER','1')):
            Xs=np.maximum(X,1e-8)
            # SZ terms [2] g Pi/4 and [5] (3/4k^2)(g Pi)'' COMBINE: integrating [5] by parts
            # twice (d^2 j_l/deta^2 = k^2 j_l'') gives (3/4)(g Pi) j_l'', so the total Pi
            # contribution is (g Pi/4)(j_l + 3 j_l'') -- NOT half of it.  r2166 carried the
            # halved kernel; the factor is restored here (r2187).
            _QF = float(os.environ.get('QKF','2.0'))
            Kq = _QF*(-3.0*jlp/Xs + (3.0*l*(l+1)/(2.0*Xs**2) - 1.0)*jl)
            _int = _int + Sq*Kq
        elif Sq is not None:
            _int = _int + Sq*jl
        Dk=np.trapezoid(_int, ee, axis=0)
        Cl[j]=np.sum(P*Dk**2)
    return ls, Cl*ls*(ls+1)

if __name__ == "__main__":
    ls,Dl = spectrum(lmax=1250)
    from scipy.signal import argrelextrema as _ar
    idx=[q for q in _ar(Dl,np.greater,order=2)[0]]
    def _refine(q):
        if q<1 or q>=len(ls)-1: return float(ls[q]),float(Dl[q])
        y0,y1,y2=Dl[q-1],Dl[q],Dl[q+1]; d=y0-2*y1+y2
        if d==0: return float(ls[q]),float(y1)
        t=0.5*(y0-y2)/d; h=float(ls[1]-ls[0])
        return float(ls[q]+t*h), float(y1-0.25*(y0-y2)*t)
    pk=[_refine(q) for q in idx[:4]]
    print("\n  *** CR — TWO-RATE BACKGROUND, NO DAMPING ENVELOPE ANYWHERE ***")
    print("    peaks at l =",[round(p[0],1) for p in pk])
    if len(pk)>=3: print("    P1/P2 = %.3f   P1/P3 = %.3f"%(pk[0][1]/pk[1][1],pk[0][1]/pk[2][1]))
    print("    (Planck 2018 Table 5, arXiv:1807.06205 -- SOURCED r2134:")
print("     peaks 220.6+-0.6 / 538.1+-1.3 / 809.8+-1.0 / 1147.8+-2.3;")
print("     D_l = 5733+-39 / 2586+-23 / 2518+-17 / 1227+-9 uK^2;")
print("     => P1/P2 = 2.2170,  P1/P3 = 2.2768,  P1/P4 = 4.6724)")
