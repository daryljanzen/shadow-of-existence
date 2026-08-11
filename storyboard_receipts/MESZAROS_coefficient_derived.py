"""DERIVE the Meszaros coefficient in our conventions.  Pure RD, H=1/eta, Phi=Psi given exactly by
   Phi(x) = 3 Phi_i [sin x - x cos x]/x^3 ,  x = k eta/sqrt3
CDM:  theta_c' = -H theta_c + k^2 Psi ;  delta_c' = -theta_c + 3 Phi'
Integrate and fit delta_c = A + B ln(eta).  No recalled numbers, no external code."""
import numpy as np
from scipy.integrate import solve_ivp
Phi_i=-1.0
def Phi(x):  return 3.0*Phi_i*(np.sin(x)-x*np.cos(x))/x**3 if x>1e-6 else Phi_i*(1-x*x/10)
def dPhi(x, h=1e-5): return (Phi(x+h)-Phi(x-h))/(2*h)
for k in (0.04,0.08,0.16,0.32):
    s3=np.sqrt(3.0)
    def rhs(e,y):
        dc,tc=y; x=k*e/s3
        return [-tc + 3*dPhi(x)*(k/s3), -tc/e + k*k*Phi(x)]
    e0=1e-3/k
    y0=[-1.5*Phi_i, 0.0]                      # super-horizon adiabatic: delta_c = -3/2 Phi
    s=solve_ivp(rhs,[e0,4000./k],y0,rtol=1e-10,atol=1e-14,dense_output=True)
    ee=np.exp(np.linspace(np.log(20./k),np.log(3000./k),400))
    dc=s.sol(ee)[0]
    B,A=np.polyfit(np.log(ee),dc,1)
    print("   k=%.2f :  DERIVED  delta_c = %.4f + %.4f ln(eta)     [check: k-independent B]"%(k,A,B))
