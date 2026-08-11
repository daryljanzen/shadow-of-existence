"""VALID — does the photon hierarchy reproduce the ANALYTIC Silk damping?

The hierarchy (HIER_photon_hierarchy.py) generates its own damping with no envelope.  That damping has
never been checked against anything.  This is the check, and it is the same move that caught the
anisotropic-stress sign: compare against a derivation, not against the sky.

METHOD.  Run the identical hierarchy twice -- once normally, once with the photon anisotropic stress
forced to zero (NODAMP: perfect coupling, hence NO Silk damping, everything else identical).  For each
mode take the acoustic oscillator amplitude of x = Theta_0 + Psi,
        A = sqrt( x^2 + (dx/d eta)^2 / omega^2 ),      omega = k c_s = k / sqrt(3(1+R)),
which is smooth through zero-crossings.  Then
        -ln( A_damped / A_undamped )  should equal  k^2 / k_D^2(eta)
with 1/k_D^2 the analytic integral used by RD_diffusion_direct.py.  A linear fit in k^2 gives the
hierarchy's OWN diffusion length; the ratio to the analytic one is the answer.
"""
import os, numpy as np
os.environ.setdefault('NS1','2400'); os.environ.setdefault('NS2','3000')
import HIER_photon_hierarchy as H

kk = np.linspace(0.008, 0.060, 14)

def run(nodamp):
    H._NODAMP = nodamp
    E, Y, e_sw = H.evolve(kk)
    return E, Y, e_sw

E1,Y1,e_sw = run(False)
E0,Y0,_    = run(True)
assert np.allclose(E1,E0)

def amp(E, Y, e_target):
    j = int(np.argmin(abs(E-e_target)))
    j = max(1, min(j, len(E)-2))
    def xof(i):
        Ph=Y[i,:,6]; sgn=Y[i,:,H.IN]/2
        Ps=Ph-6*H.Hc_of(E[i])**2*H.On_of(E[i])*sgn/kk**2
        return Y[i,:,2]/4+Ps
    x=xof(j); dx=(xof(j+1)-xof(j-1))/(E[j+1]-E[j-1])
    R=H.Rb_of(E[j]); w=kk/np.sqrt(3*(1+R))
    return np.sqrt(x**2+(dx/w)**2), E[j]

print("="*78)
print("HIERARCHY DAMPING vs THE ANALYTIC SILK FORMULA   (switch at eta=%.1f Mpc)"%e_sw)
print("="*78)
from scipy.integrate import quad
def invkD2_analytic(e_hi):
    f=lambda e:(H.Rb_of(e)**2/(1+H.Rb_of(e))+8/9)/(6*(1+H.Rb_of(e))*float(H.taup_of(e)))
    return quad(f, H.eg[1], e_hi, limit=300)[0]

for e_t in (245.0, 260.0, 272.0):
    A1,ea = amp(E1,Y1,e_t); A0,_ = amp(E0,Y0,e_t)
    y = -np.log(np.clip(A1/A0, 1e-12, None))
    good = np.isfinite(y) & (y>0)
    slope = np.polyfit(kk[good]**2, y[good], 1)[0]          # = 1/k_D^2 as the hierarchy has it
    ana = invkD2_analytic(ea)
    print("  eta=%6.1f Mpc (z=%5.0f):  hierarchy 1/k_D^2 = %7.2f Mpc^2   analytic = %7.2f Mpc^2"
          % (ea, 1/np.interp(ea,H.eg,H.ag)-1, slope, ana))
    print("      r_D  hierarchy %.2f Mpc  vs analytic %.2f Mpc   ->  RATIO %.3f"
          % (np.sqrt(slope), np.sqrt(ana), np.sqrt(slope/ana)))
