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
"""TC9 — THE TWO-COMPONENT SYSTEM.  A.33's step, coded as reasoned.
No effective fluid: delta_gamma and delta_c evolve separately, and Psi comes from the CONSTRAINT.
  delta_c'    = -theta_c + 3 Psi'
  theta_c'    = -H theta_c + k^2 Psi
  delta_gamma'= -(4/3) theta_gb + 4 Psi'
  theta_gb'   = -(H Rb/(1+Rb)) theta_gb + (k^2/(1+Rb)) delta_gamma/4 + k^2 Psi
  Psi'        = -H Psi - k^2 Psi/(3H) - (H/2) SUM_i Omega_i delta_i        [Poisson, Phi=Psi]
Adiabatic super-horizon ICs: delta_g=-2Psi, delta_c=-(3/2)Psi, theta=k^2 eta Psi/2, so
Theta_0 = delta_g/4 = -Psi/2, which is the condition TC2-TC8 used -- now derived rather than asserted.
CONTROL (r1960, sharpened by A.33): must return phi_1 ~ 0.27 AND P1/P2 ~ 2.2 on LambdaCDM."""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
c=299792.458
H0=67.4; Om=0.307; z_eq=3403.6; Or=Om/(1+z_eq); OL=1-Om
ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec); a_eq=1/(1+z_eq)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Hub=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)
ag=np.logspace(-8, np.log10(a_rec), 12000)
eg=np.concatenate([[0.],cumulative_trapezoid(c/(ag**2*Hub(ag)),ag)])
eta_rec=eg[-1]
a_of=CubicSpline(eg,ag); Hc_of=CubicSpline(eg, ag*Hub(ag)/c)
rho_tot=lambda a: Or/a**4+Om/a**3+OL
Og_of=CubicSpline(eg, (Or/ag**4)/rho_tot(ag))       # radiation fraction
Oc_of=CubicSpline(eg, (Om/ag**3)/rho_tot(ag))       # matter fraction
Rb_of=CubicSpline(eg, Rb_rec*(ag/a_rec))
DM=quad(lambda a: c/(a**2*Hub(a)), a_rec, 1.0, limit=250)[0]
rs=quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))), 1e-9, a_rec, limit=250)[0]
lA=np.pi*DM/rs
print("="*80); print("TC9 — TWO-COMPONENT SYSTEM, CONTROL"); print("="*80)
print(f"\n  eta_rec={eta_rec:.2f}  r_s={rs:.2f}  D_M={DM:.0f}  l_A={lA:.1f}")
def mode(k, eps=0.01):
    ei=eps/k
    def rhs(e,y):
        dc,tc,dg,tg,Ps=y
        Hc=Hc_of(e); Rb=Rb_of(e); Og=Og_of(e); Oc=Oc_of(e)
        Psp=-Hc*Ps - k**2*Ps/(3*Hc) - (Hc/2)*(Og*dg+Oc*dc)
        return [-tc+3*Psp,
                -Hc*tc+k**2*Ps,
                -(4/3)*tg+4*Psp,
                -(Hc*Rb/(1+Rb))*tg + (k**2/(1+Rb))*dg/4 + k**2*Ps,
                Psp]
    P0=1.0
    y0=[-1.5*P0, k**2*ei*P0/2, -2.0*P0, k**2*ei*P0/2, P0]
    s=solve_ivp(rhs,[ei,eta_rec],y0,method='RK45',rtol=1e-7,atol=1e-12,dense_output=True)
    dg,Ps=s.sol(eta_rec)[2],s.sol(eta_rec)[4]
    return dg/4+Ps, Ps
print("\n  super-horizon check (k tiny): Psi should decay 1 -> ~0.9 across equality")
v,P=mode(1e-4); print(f"    Psi(rec) = {P:.4f}")
ls=np.arange(120,1300,10.0)
res=np.array([mode(l/DM)[0] for l in ls])
rD=DM/1362.
Dl=(res*np.exp(-((ls/DM)*rD)**2))**2*ls**(0.965-1)
idx=[i for i in argrelextrema(Dl,np.greater,order=2)[0]]
print(f"\n  {'peak':>5s} {'l found':>9s} {'l meas':>8s} {'phi_n':>8s}")
meas=[220,536,813,1126]
for n,i in enumerate(idx[:4]):
    phi=(n+1)-ls[i]/lA
    print(f"  {n+1:>5d} {ls[i]:>9.0f} {meas[n] if n<4 else '-':>8} {phi:>8.3f}")
if len(idx)>=3:
    h=[Dl[i] for i in idx[:3]]
    print(f"\n  P1/P2 = {h[0]/h[1]:7.3f}   measured 2.212     phi_1 target 0.27")
