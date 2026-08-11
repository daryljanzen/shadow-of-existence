"""
Semi-analytic acoustic peak-height transfer, in sound-horizon phase x=k*r_s.
VALIDATION GATE (arc discipline): must reproduce CAMB's LCDM pattern P1/P2=2.21, P2/P1=0.453,
P3/P1=0.443 before any CR number is trusted. Physics: driven photon-baryon oscillator (tight
coupling) with baryon loading R (odd/even asymmetry), radiation-driving boost from potential
decay, Silk damping, Doppler; projected to C_l via x=k r_s, l=x*D_M/r_s.
"""
import numpy as np
from scipy.integrate import solve_ivp

# --- plasma inputs (LCDM, = CR inherited) ---
R   = 0.60          # baryon loading at recombination, 3 rho_b/4 rho_gamma
cs  = 1/np.sqrt(3*(1+R))
ns  = 0.965
# Silk damping scale in sound-horizon-phase units (k_D r_s); tuned to CAMB damping tail
xD  = 9.0
# radiation-driving: potential Psi(u) decays after horizon entry; u = k*eta = sqrt3 * x (RD)
def Psi(u):
    u=np.maximum(np.abs(u),1e-8); return 3*(np.sin(u)-u*np.cos(u))/u**3

# effective temperature monopole M(x)=Theta0+Psi at recombination, per mode, via driven oscillator
# oscillator in phase s = k r_s(eta) ; d^2Theta0/ds^2 + Theta0 = -Psi(u(s)) with u=sqrt3 s (RD-like)
def Meff(xstar):
    # integrate to s=xstar; baryon loading shifts equilibrium by -R*Psi
    def rhs(s,y):
        u=np.sqrt(3)*s
        return [y[1], -(y[0]) - Psi(u)]
    s=solve_ivp(rhs,[1e-4,xstar],[-0.5,0.0],rtol=1e-8,atol=1e-10,max_step=0.02,dense_output=True)
    Th0=s.y[0,-1]; Th0d=s.y[1,-1]
    u=np.sqrt(3)*xstar; Pn=Psi(u)
    M = (Th0+Pn) - R*Pn        # baryon-loaded effective temperature (compression boost on odd peaks)
    D = cs*Th0d                # Doppler ~ velocity
    return M, D

xs=np.linspace(0.2, 12, 1400)
M=np.array([Meff(x)[0] for x in xs]); D=np.array([Meff(x)[1] for x in xs])
Cl = (M**2 + D**2) * np.exp(-2*(xs/xD)**2) * xs**(ns-1)   # power vs x (tilt in x proxy)
# peaks at x ~ n*pi
def peakval(n):
    c=n*np.pi; m=(xs>c-0.9)&(xs<c+0.9); return Cl[m].max()
P=[peakval(n) for n in (1,2,3)]
print("semi-analytic (validation vs CAMB LCDM):")
print(f"  P1/P2 = {P[0]/P[1]:.3f}   P2/P1 = {P[1]/P[0]:.3f}   P3/P1 = {P[2]/P[0]:.3f}")
print(f"  CAMB target:  P1/P2 = 2.210   P2/P1 = 0.453   P3/P1 = 0.443")
