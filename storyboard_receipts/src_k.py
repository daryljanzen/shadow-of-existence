"""Measure where the CR source S(k) = Theta_0 + Psi has its extrema in k at recombination.
If they sit at k r_s = n pi, the modes are right and the spectrum's l-axis is at fault.
If they sit 1.34x apart, the modes themselves oscillate at the wrong frequency."""
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline
from scipy.signal import argrelextrema
c=299792.458; H0=73.0; Om=0.3066; OL=1-Om; ombh2=0.0224; z_rec=1089.9; a_rec=1/(1+z_rec)
fnu=0.4052; Or_content=4.15e-5/(H0/100)**2
Rb_rec=31500*ombh2/(2.7255/2.7)**4/(1+z_rec)
Hub=lambda a: H0*np.sqrt(Om/a**3+OL)
ag=np.logspace(-7,0,20000)
seed=quad(lambda a: c/(a**2*Hub(a)),1e-14,ag[0],limit=200)[0]
from scipy.integrate import cumulative_trapezoid
eg=np.concatenate([[seed],seed+cumulative_trapezoid(c/(ag**2*Hub(ag)),ag)])
Hc_of=CubicSpline(eg, ag*Hub(ag)/c); Rb_of=CubicSpline(eg, Rb_rec*(ag/a_rec))
rt=Or_content/ag**4+Om/ag**3+OL
Og_of=CubicSpline(eg,(1-fnu)*(Or_content/ag**4)/rt); On_of=CubicSpline(eg,fnu*(Or_content/ag**4)/rt)
Oc_of=CubicSpline(eg,(Om/ag**3)/rt)
eta_rec=float(np.interp(a_rec,ag,eg)); zs=6761.; eta_o=float(np.interp(1/(1+zs),ag,eg))
rs=quad(lambda a: c/(a**2*Hub(a)*np.sqrt(3*(1+Rb_rec*a/a_rec))),1/(1+zs),a_rec,limit=250)[0]
DM=eg[-1]-eta_rec
kk=np.linspace(0.005,0.10,900)
# minimal 4-variable tight-coupled system: dg, tg, Ph, dc  (enough for the acoustic phase)
def rhs(e,Y):
    y=Y.reshape(len(kk),4); dg,tg,Ph,dc=[y[:,j] for j in range(4)]
    Hc=float(Hc_of(e)); Rb=float(Rb_of(e)); Ogv=float(Og_of(e)); Onv=float(On_of(e)); Ocv=float(Oc_of(e))
    Ps=Ph
    Php=-Hc*Ps-kk**2*Ph/(3*Hc)-(Hc/2)*(Ogv*dg+Onv*dg+Ocv*dc)
    o=np.empty_like(y)
    o[:,0]=-(4/3)*tg+4*Php
    o[:,1]=-(Hc*Rb/(1+Rb))*tg+(kk**2/(1+Rb))*dg/4+kk**2*Ps
    o[:,2]=Php
    o[:,3]=-tg*0+3*Php
    return o.ravel()
y0=np.zeros((len(kk),4)); y0[:,2]=-1.0; y0[:,0]=-2.0*(-1.0); y0[:,3]=0.75*y0[:,0]
NS=6000; g=np.linspace(eta_o,eta_rec,NS+1); h=g[1]-g[0]; Y=y0.ravel().copy()
for n in range(NS):
    e=g[n]; k1=rhs(e,Y); k2=rhs(e+h/2,Y+h/2*k1); k3=rhs(e+h/2,Y+h/2*k2); k4=rhs(e+h,Y+h*k3)
    Y=Y+h/6*(k1+2*k2+2*k3+k4)
y=Y.reshape(len(kk),4); S=y[:,0]/4+y[:,2]
idx=argrelextrema(np.abs(S),np.greater,order=8)[0]
kp=kk[idx][:6]
print("   source extrema in k (velocities zero at onset, common phase):")
print("      k          k*r_s/pi     implied l = k D_M")
for k in kp: print("     %.5f      %7.4f       %7.1f"%(k,k*rs/np.pi,k*DM))
if len(kp)>2:
    d=np.diff(kp); print("\n   spacing in k: %s"%'  '.join('%.5f'%x for x in d))
    print("   acoustic period pi/r_s = %.5f"%(np.pi/rs))
    print("   ratio measured/acoustic = %.4f"%(np.mean(d)/(np.pi/rs)))
