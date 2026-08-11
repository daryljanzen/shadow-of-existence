"""VALID4 — the RADIATION-DRIVING ENHANCEMENT against its EXACT radiation-era solution.

WHY.  With Silk damping off the hierarchy still gives P1/P3 = 3.016 vs a fully-damped sky value of
2.257, so the error is in the UNDAMPED acoustic amplitude.  The measured driving plateau was 1.71x
relative to our own lowest-k mode -- but that reference is not a clean Sachs-Wolfe limit, so 1.71 was
not yet a measurement of anything.  This benchmarks against a DERIVATION instead.

THE EXACT SYSTEM.  Pure radiation domination, photons only, no baryons (R=0), no anisotropic stress
(Psi = Phi), adiabatic.  With x = k eta / sqrt3 and Phi = 3 Phi_i (sin x - x cos x)/x^3 (exact), the
photon monopole obeys, for Xi = Theta_0 + Phi,
        Xi_xx + Xi = 2 Phi_xx ,       Xi(0) = Phi_i/2 ,  Xi_x(0) = 0 ,
since Theta_0(0) = -Phi_i/2 super-horizon (delta_gamma = -2 Psi).  The asymptotic oscillation
amplitude of Xi, divided by its undriven value Phi_i/2, IS the driving enhancement.

THE COMPARISON.  Our hierarchy is run and its high-k modes are read between horizon entry and equality
(eta_eq = 107 Mpc here), where the same limit holds.  Neutrinos (f_nu = 0.405) are present in ours and
absent from the exact solution; free-streaming is known to REDUCE the driving by O(10-20%), so the
exact value is an upper bound on what ours should show -- a small shortfall is expected, a large one is
the error we are hunting.
"""
import os, numpy as np
from scipy.integrate import solve_ivp

# ---------- the exact photons-only RD driven oscillator ----------
def Phi(x):    return np.where(x<1e-6, 1.0-x**2/10., 3.0*(np.sin(x)-x*np.cos(x))/x**3)
def Phi_xx(x, h=1e-5): return (Phi(x+h)-2*Phi(x)+Phi(x-h))/h**2
def rhs(x,y):  return [y[1], -y[0] + 2*Phi_xx(max(x,1e-4))]
s = solve_ivp(rhs, (1e-4, 400.0), [0.5, 0.0], rtol=1e-10, atol=1e-12, dense_output=True)
xs = np.linspace(200., 400., 20000); Xi = s.sol(xs)[0]
A_exact = (Xi.max()-Xi.min())/2.0
print("="*78)
print("EXACT pure-RD driven oscillator (photons only, Phi_i = 1)")
print("="*78)
print("  undriven amplitude   |Xi(0)| = Phi_i/2      = %.4f"%0.5)
print("  driven asymptotic amplitude of Theta_0+Phi  = %.4f"%A_exact)
print("  ==> EXACT DRIVING ENHANCEMENT               = %.3f x"%(A_exact/0.5))

# ---------- our hierarchy, read deep in RD ----------
os.environ.setdefault('NS1','3000'); os.environ.setdefault('NS2','600')
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['NODAMP']='1'
import HIER_photon_hierarchy as H
eta_eq = np.interp(1.0/(1+H.Om/H.Or_content), H.ag, H.eg)
kk = np.array([0.06,0.09,0.13,0.20,0.30])
E,Y,esw = H.evolve(kk)
print()
print("OUR HIERARCHY, read between horizon entry and equality (eta_eq = %.0f Mpc)"%eta_eq)
print("      k      x at eta_eq/2   enhancement (driven / undriven)")
m=(E>0.35*eta_eq)&(E<0.95*eta_eq)
Ph=Y[m][:,:,6]; sgn=Y[m][:,:,H.IN]/2
Hcv=np.array([H.Hc_of(e) for e in E[m]])[:,None]; Onv=np.array([H.On_of(e) for e in E[m]])[:,None]
Ps=Ph-6*Hcv**2*Onv*sgn/kk[None,:]**2
Xi_ours = Y[m][:,:,2]/4 + Ph          # Theta_0 + Phi, to match the exact variable
Psi_i = 1.0/(1.0+0.4*H.fnu)           # our Psi(0) with Phi(0) = 1
for i,k in enumerate(kk):
    xr = k*E[m]/np.sqrt(3)
    sel = xr > 8.0                     # well sub-horizon
    if sel.sum() < 20: print("  %6.3f     (too few sub-horizon samples in RD)"%k); continue
    A = (Xi_ours[sel,i].max()-Xi_ours[sel,i].min())/2.0
    print("  %6.3f   %8.1f        %8.3f x"%(k, k*0.5*eta_eq/np.sqrt(3), A/(0.5*Psi_i)))
print()
print("  (ours normalised to Psi_i/2, the same undriven reference, with Psi_i = Phi_i/(1+0.4 f_nu).)")
