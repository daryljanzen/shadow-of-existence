"""TC4 — THE INTEGRATOR WITH Psi(k,eta) FROM C1.  Control first.
THE FIX (r1965): TC2/TC3 used the SUPER-HORIZON growing mode Psi(a) for modes deep inside the
horizon.  C1 gives the correct law: inside the horizon during radiation domination the potential
decays as 3(sin x - x cos x)/x^3 with x = k eta/sqrt3, and it FREEZES once matter dominates.
That is k-DEPENDENT, and it is the whole reason the odd/even asymmetry washes out at high l."""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
c=299792.458
H0=67.4; Om=0.307; z_eq=3403.6; Or=Om/(1+z_eq); OL=1-Om
ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec); a_eq=1/(1+z_eq)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
H=lambda a: H0*np.sqrt(Or/a**4+Om/a**3+OL)
ag=np.logspace(-8, np.log10(a_rec), 12000)
eg=np.concatenate([[0.],cumulative_trapezoid(c/(ag**2*H(ag)),ag)])
eta_rec=eg[-1]; eta_eq=float(np.interp(a_eq,ag,eg))
Rbs=CubicSpline(eg, Rb_rec*(ag/a_rec))
DM=quad(lambda a: c/(a**2*H(a)), a_rec, 1.0, limit=250)[0]
rs=quad(lambda a: c/(a**2*H(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))), 1e-9, a_rec, limit=250)[0]
lstar=np.pi*DM/rs
print("="*80); print("TC6 — PER-MODE INITIAL TIMES"); print("="*80)
print(f"\n  eta_eq={eta_eq:.2f}  eta_rec={eta_rec:.2f}  r_s={rs:.2f}  D_M={DM:.0f}  l_*={lstar:.1f}")
def Psi_k(k):
    """C1's radiation-era decay, frozen at equality."""
    def f(e):
        x=k*min(e,eta_eq)/np.sqrt(3)
        return 1.0 if x<1e-8 else 3*(np.sin(x)-x*np.cos(x))/x**3
    return f
def mode(k, eps=0.01):
    """START EACH MODE AT A FIXED NUMBER OF e-FOLDS OUTSIDE ITS OWN HORIZON: k eta_i = eps.
    Starting every mode at a common eta -> 0 (the r1965 fault) integrates decades of super-horizon
    evolution for low k and destabilises them."""
    P=Psi_k(k)
    eta_i=eps/k
    egr=np.linspace(eta_i,eta_rec,3000); Pg=np.array([P(e) for e in egr])
    Ps=CubicSpline(egr,Pg)
    def rhs(e,y):
        Rb=Rbs(e); Rbp=Rbs(e,1); cs2=1/(3*(1+Rb))
        return [y[1], -(Rbp/(1+Rb))*y[1] - k**2*cs2*y[0] - (k**2/3)*Ps(e) - Ps(e,2) - (Rbp/(1+Rb))*Ps(e,1)]
    s=solve_ivp(rhs,[eta_i,eta_rec],[-Ps(eta_i)/2,0.0],method='RK45',rtol=1e-7,atol=1e-12,dense_output=True)
    return s.sol(eta_rec)[0]+Ps(eta_rec)
ls=np.arange(120,1300,10.0)
vals=np.array([mode(l/DM) for l in ls])
rD=DM/1362.
Dl=(vals*np.exp(-((ls/DM)*rD)**2))**2*ls**(0.965-1)
idx=[i for i in argrelextrema(Dl,np.greater,order=2)[0]]
print(f"\n  {'peak':>5s} {'l (found)':>10s} {'l (measured)':>13s} {'D_l':>12s}")
meas=[220,536,813,1126]
for n,i in enumerate(idx[:4]):
    print(f"  {n+1:>5d} {ls[i]:>10.0f} {meas[n] if n<4 else '-':>13} {Dl[i]:>12.4e}")
if len(idx)>=3:
    h=[Dl[i] for i in idx[:3]]
    print(f"\n  P1/P2 = {h[0]/h[1]:7.3f}   measured 2.212")
    print(f"  P1/P3 = {h[0]/h[2]:7.3f}   measured 2.257")
