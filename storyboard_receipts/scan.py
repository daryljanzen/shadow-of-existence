"""Scan z_onset: what does each value give for l_A (the high-l spacing) and l_1 (the first peak)?
One inherited datum, two observables -- this quantifies whether it can fit both."""
import numpy as np
from scipy.integrate import quad, cumulative_trapezoid
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
c=299792.458; H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec)
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Hub=lambda a: H0*np.sqrt(Om/a**3+OL)
ag=np.logspace(-7,0,20000)
seed=quad(lambda a: c/(a**2*Hub(a)),1e-14,ag[0],limit=200)[0]
eg=np.concatenate([[seed],seed+cumulative_trapezoid(c/(ag**2*Hub(ag)),ag)])
Hc_of=CubicSpline(eg, ag*Hub(ag)/c); Rb_of=CubicSpline(eg, Rb_rec*(ag/a_rec))
eta_rec=float(np.interp(a_rec,ag,eg)); DM=eg[-1]-eta_rec
rs_f=lambda zs: quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))),1/(1+zs),a_rec,limit=250)[0]
kk=np.linspace(0.004,0.06,600)
def first_peak(zs):
    eo=float(np.interp(1/(1+zs),ag,eg))
    def rhs(e,Y):
        y=Y.reshape(len(kk),3); dg,tg,Ph=[y[:,j] for j in range(3)]
        Hc=float(Hc_of(e)); Rb=float(Rb_of(e))
        Php=-Hc*Ph-kk**2*Ph/(3*Hc)
        o=np.empty_like(y)
        o[:,0]=-(4/3)*tg+4*Php
        o[:,1]=-(Hc*Rb/(1+Rb))*tg+(kk**2/(1+Rb))*dg/4+kk**2*Ph
        o[:,2]=Php
        return o.ravel()
    y0=np.zeros((len(kk),3)); y0[:,2]=-1.0; y0[:,0]=2.0
    NS=4000; g=np.linspace(eo,eta_rec,NS+1); h=g[1]-g[0]; Y=y0.ravel().copy()
    for n in range(NS):
        e=g[n]; k1=rhs(e,Y); k2=rhs(e+h/2,Y+h/2*k1); k3=rhs(e+h/2,Y+h/2*k2); k4=rhs(e+h,Y+h*k3)
        Y=Y+h/6*(k1+2*k2+2*k3+k4)
    y=Y.reshape(len(kk),3); S=y[:,0]/4+y[:,2]
    i=argrelextrema(np.abs(S),np.greater,order=6)[0]
    return (kk[i[0]]*DM if len(i) else np.nan), eta_rec-eo
print("   z_onset    span(Mpc)     r_s      l_A=piD/r_s    first source extremum l")
for zs in (6761.,10000.,20000.,50000.,2e5,1e6):
    l1,span=first_peak(zs); r=rs_f(zs)
    print("   %8.0f   %8.1f   %7.2f      %6.1f            %7.1f"%(zs,span,r,np.pi*DM/r,l1))
print()
print("   sky: l_A ~ 301.8, first peak 220  (ratio 0.73)")
