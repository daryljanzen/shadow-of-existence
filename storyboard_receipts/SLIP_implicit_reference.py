"""An INDEPENDENT reference for the slip: the same tight-coupling pair, integrated implicitly at
high accuracy with our own conventions throughout.  No external definitions, so nothing to mis-pin.
Compare our explicit RK4 slip against it.

System (Newtonian gauge, Ma-Bertschinger), the two stiff variables only, with delta_g and the
potentials taken from the evolved run as given drivers:
    theta_g' = k^2(delta_g/4 - sigma_g) + k^2 Psi + tau'(theta_b - theta_g)
    theta_b' = -H theta_b + k^2 Psi + (tau'/R)(theta_g - theta_b)
"""
import os, numpy as np
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['ETAEND']='500'
import HIER_photon_hierarchy as H
from scipy.integrate import solve_ivp
K=np.array([0.015,0.030])
E,Y,esw=H.evolve(K)
sel=(E>200.)&(E<330.)
ee=E[sel]
print("  independent implicit reference vs our explicit RK4, for the SLIP theta_g - theta_b")
print("     eta      k=0.015                        k=0.030")
print("            explicit    implicit   ratio    explicit    implicit   ratio")
out={}
for i,k in enumerate(K):
    # drivers from the evolved run
    dg=np.interp(ee,E,Y[:,i,0])*4.0            # delta_g = 4 Theta_0
    Ph=np.interp(ee,E,Y[:,i,2]); sg=np.interp(ee,E,Y[:,i,4])
    f_dg=lambda e: np.interp(e,ee,dg); f_Ph=lambda e: np.interp(e,ee,Ph); f_sg=lambda e: np.interp(e,ee,sg)
    def rhs(e,y):
        tg,tb=y; tp=float(H.taup_of(e)); R=float(H.Rb_of(e)); Hc=float(H.Hc_of(e))
        return [k*k*(f_dg(e)/4-f_sg(e))+k*k*f_Ph(e)+tp*(tb-tg),
                -Hc*tb+k*k*f_Ph(e)+(tp/R)*(tg-tb)]
    q0=int(np.argmin(abs(E-ee[0])))
    dTh=(Y[q0+1,i,0]-Y[q0-1,i,0])/(E[q0+1]-E[q0-1]); dPh0=(Y[q0+1,i,2]-Y[q0-1,i,2])/(E[q0+1]-E[q0-1])
    tg0=-3*dTh+3*dPh0; tb0=Y[q0,i,1]
    s=solve_ivp(rhs,[ee[0],ee[-1]],[tg0,tb0],method='Radau',rtol=1e-10,atol=1e-16,dense_output=True)
    out[i]=s
for e in (240.,265.,277.,290.,305.):
    row=""
    for i,k in enumerate(K):
        q=int(np.argmin(abs(E-e)))
        dTh=(Y[q+1,i,0]-Y[q-1,i,0])/(E[q+1]-E[q-1]); dPh=(Y[q+1,i,2]-Y[q-1,i,2])/(E[q+1]-E[q-1])
        s_exp=(-3*dTh+3*dPh)-Y[q,i,1]
        yy=out[i].sol(e); s_imp=yy[0]-yy[1]
        row+="  %+10.3e %+10.3e %7.3f"%(s_exp,s_imp,s_exp/s_imp if abs(s_imp)>1e-30 else np.nan)
    print("   %6.0f %s"%(e,row))
