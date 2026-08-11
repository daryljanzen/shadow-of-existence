"""STEP 1: derive B with NEUTRINOS included, so the comparison runs in the DEFAULT configuration
(equality where it belongs) with nothing perturbed.  Full RD system: photons (tightly coupled ->
delta_g oscillates freely), neutrinos with a hierarchy, CDM.  Adiabatic ICs.  Check: B must be
k-INDEPENDENT."""
import numpy as np
from scipy.integrate import solve_ivp
fnu=0.4089; fg=1.0-fnu; LN=24
def run(k, eta_max):
    s3=np.sqrt(3.0)
    # state: dg, tg, dn, tn, F2..F_LN, dc, tc, Phi   (RD: H=1/eta, Om_g=fg, Om_nu=fnu)
    NV=4+(LN-1)+3
    def rhs(e,y):
        dg,tg,dn,tn=y[0],y[1],y[2],y[3]; F=y[4:4+LN-1]; dc,tc,Ph=y[-3],y[-2],y[-1]
        H=1.0/e; sig=F[0]/2
        Ps=Ph-6*H*H*fnu*sig/k**2
        o=np.zeros(NV)
        o[0]=-(4/3)*tg+4*(-H*Ps-k*k*Ph/(3*H)-(H/2)*(fg*dg+fnu*dn))
        o[1]=k*k*(dg/4)+k*k*Ps                      # tightly coupled: no viscosity, no drag
        o[2]=-(4/3)*tn+4*o[-1] if False else -(4/3)*tn
        o[3]=k*k*(dn/4-sig)+k*k*Ps
        o[4]=(8/15)*tn-(3/5)*k*F[1]
        for i in range(1,LN-2):
            l=i+2; o[4+i]=k/(2*l+1)*(l*F[i-1]-(l+1)*F[i+1])
        o[4+LN-2]=k*F[LN-3]-(LN+1)/e*F[LN-2]
        Php=-H*Ps-k*k*Ph/(3*H)-(H/2)*(fg*dg+fnu*dn)
        o[0]=-(4/3)*tg+4*Php; o[2]=-(4/3)*tn+4*Php
        o[-3]=-tc+3*Php; o[-2]=-H*tc+k*k*Ps; o[-1]=Php
        return o
    e0=1e-4/k
    y0=np.zeros(NV); Ph0=-1.0; Ps0=Ph0/(1+0.4*fnu); dg0=-2*Ps0
    y0[0]=dg0; y0[2]=dg0; y0[1]=(k*k*e0/2)*Ps0; y0[3]=y0[1]
    y0[4]=2.0*(Ph0*(1-1/(1+0.4*fnu)))*k*k/(6*(1/e0)**2*fnu)
    y0[-3]=0.75*dg0; y0[-2]=y0[1]; y0[-1]=Ph0
    return solve_ivp(rhs,[e0,eta_max],y0,method='Radau',rtol=1e-7,atol=1e-11,dense_output=True)
print("   DERIVED with neutrinos (f_nu=%.4f).  Check: B must be k-INDEPENDENT."%fnu)
for k in (0.64,2.56):
    s=run(k, 2400./k)
    ee=np.exp(np.linspace(np.log(30./k),np.log(1200./k),200))
    dc=s.sol(ee)[-3]
    B,A=np.polyfit(np.log(ee),dc,1)
    print("      k=%5.2f :  B = %8.4f   A = %9.4f"%(k,B,A))
