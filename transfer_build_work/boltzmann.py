import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
Om=0.315; Or=9.24e-5; OL=1-Om-Or; Ob=0.0493; Oc=Om-Ob; h=0.674; H0=1.0
a_eq=Or/Om; a_rec=1/1090.0
def Ea(a): return np.sqrt(Om*a**-3+Or*a**-4+OL)
# background a(eta) via eta(a)=int da/(a^2 H0 Ea)
ag=np.logspace(-7,0.02,6000)
etag=np.concatenate([[0],cumulative_trapezoid(1/(ag**2*H0*Ea(ag)),ag)])
def a_of(eta): return np.interp(eta,etag,ag)
eta_rec=np.interp(a_rec,ag,etag); eta0=np.interp(1e-6,ag,etag)
def Hc_of(eta): a=a_of(eta); return a*H0*Ea(a)
def R_of(a): return 0.75*Ob/Or*a
print(f"  eta0={eta0:.4f}, eta_rec={eta_rec:.4f} (1/H0);  a_eq={a_eq:.2e}")
def derivs(eta,y,k):
    dg,tg,dc,tc,db=y; a=a_of(eta); H=a*H0*Ea(a); R=R_of(a); fac=1.5*H0**2*a**2
    drho=fac*(Or*a**-4*dg+Oc*a**-3*dc+Ob*a**-3*db)
    rpt =fac*((4./3)*Or*a**-4*tg+Oc*a**-3*tc+Ob*a**-3*tg)/k
    Phi=-(drho+3*H*rpt)/k**2; Psi=Phi; Phip=-H*Psi-rpt*k
    ddg=-4./3*tg+4*Phip
    dtg=(k**2*dg/4.+k**2*Psi*(1+R)-H*R*tg)/(1+R)
    ddc=-tc+3*Phip; dtc=-H*tc+k**2*Psi; ddb=-tg+3*Phip
    return [ddg,dtg,ddc,dtc,ddb]
def solve_k(k):
    Psi0=1.0; dg0=-2*Psi0; dc0=db0=0.75*dg0
    s=solve_ivp(derivs,[eta0,eta_rec],[dg0,0,dc0,0,db0],args=(k,),rtol=2e-6,atol=1e-8,max_step=eta_rec/250)
    dg,tg,dc,tc,db=s.y[:,-1]; a=a_rec
    Phi=-(1.5*H0**2*a**2*(Or*a**-4*dg+Oc*a**-3*dc+Ob*a**-3*db))/k**2
    return dg/4.+Phi
DH=299792.458/(100*h)
kk=np.linspace(3,320,240)
ic=np.array([solve_k(k) for k in kk]); P=ic**2
kD=0.14*DH; P=P*np.exp(-(kk/kD)**2)
from scipy.signal import find_peaks
pk,_=find_peaks(P); kpk=kk[pk]; Ppk=P[pk]; rs=144.4
print(f"  peaks k*r_s: {[f'{k/DH*rs:.2f}' for k in kpk[:5]]}  (target n*pi=3.14,6.28,9.42,12.57)")
if len(Ppk)>=3:
    print(f"  P1/P2={Ppk[0]/Ppk[1]:.2f} (≈2.2)  P2/P1={Ppk[1]/Ppk[0]:.3f} (≈0.45)  P3/P1={Ppk[2]/Ppk[0]:.3f} (≈0.44)")
np.save('lcdm_P.npy',np.c_[kk,P])
