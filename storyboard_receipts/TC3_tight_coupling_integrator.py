"""TC2 — THE TIGHT-COUPLING INTEGRATOR, WITH EVERYTHING PRECOMPUTED ON AN ETA GRID.
Control-first per r1960: LambdaCDM must reproduce the measured peak ratios before CR means anything."""
import numpy as np
from scipy.integrate import solve_ivp, quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
c=299792.458
H0L=67.4; OmL=0.307; z_eq=3403.6; OrL=OmL/(1+z_eq); OLL=1-OmL
ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec); a_eq=1/(1+z_eq)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
HL=lambda a: H0L*np.sqrt(OrL/a**4+OmL/a**3+OLL)
def PsiL(a):
    y=np.asarray(a)/a_eq
    small=y<0.05
    out=np.empty_like(y,dtype=float)
    out[small]=(9/10)*(1-y[small]/16+7*y[small]**2/160)
    yy=y[~small]
    out[~small]=(9/10)*((16*np.sqrt(1+yy)+9*yy**3+2*yy**2-8*yy-16)/(10*yy**3))
    return out
print("="*80); print("TC2 — CONTROL FIRST"); print("="*80)
# grid in a, then eta by cumulative integration
ag=np.logspace(-8, np.log10(a_rec), 12000)
integ=c/(ag**2*HL(ag))
eg=np.concatenate([[0.],cumulative_trapezoid(integ,ag)])
Rg=Rb_rec*(ag/a_rec); Pg=PsiL(ag)
Rbs=CubicSpline(eg,Rg); Ps=CubicSpline(eg,Pg)
eta_rec=eg[-1]
print(f"  eta_rec = {eta_rec:.2f} Mpc   (quad gave 283.42)")
DM=quad(lambda a: c/(a**2*HL(a)), a_rec, 1.0, limit=250)[0]
rs=quad(lambda a: c/(a**2*HL(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))), 1e-9, a_rec, limit=250)[0]
lstar=np.pi*DM/rs
print(f"  r_s={rs:.2f}  D_M={DM:.0f}  l_*={lstar:.1f}")
def mode(k):
    def rhs(e,y):
        Rb=Rbs(e); Rbp=Rbs(e,1); cs2=1/(3*(1+Rb))
        P=Ps(e); Pp=Ps(e,1); Ppp=Ps(e,2)
        return [y[1], -(Rbp/(1+Rb))*y[1] - k**2*cs2*y[0] - (k**2/3)*P - Ppp - (Rbp/(1+Rb))*Pp]
    e0=eg[1]
    s=solve_ivp(rhs,[e0,eta_rec],[-Ps(e0)/2,0.0],method='RK45',rtol=1e-6,atol=1e-11,
                dense_output=True)
    return s.sol(eta_rec)[0]+Ps(eta_rec)
ls=np.arange(80,1400,12.0)
vals=np.array([mode(l/DM) for l in ls])
print(f"\n  scanning l=80..1400 for the oscillator's own extrema...")
from scipy.signal import argrelextrema
ab=np.abs(vals)
idx=argrelextrema(ab,np.greater,order=2)[0]
pk=[(ls[i],vals[i]) for i in idx]
print(f"  {'peak':>5s} {'l':>8s} {'Theta0+Psi':>12s} {'measured':>10s}")
meas=[220,536,813,1126]
for n,(l,v) in enumerate(pk[:4]):
    print(f"  {n+1:>5d} {l:>8.0f} {v:>12.5f} {meas[n] if n<4 else '-':>10}")
rD=DM/1362.
h=[(v*np.exp(-((l/DM)*rD)**2))**2 for l,v in pk[:4]]
print(f"\n  WITH damping:  P1/P2={h[0]/h[1]:.3f}   P1/P3={h[0]/h[2]:.3f}   P2/P3={h[1]/h[2]:.3f}")
print(f"  MEASURED:      P1/P2=2.212   P1/P3=2.257   P2/P3=1.020")
