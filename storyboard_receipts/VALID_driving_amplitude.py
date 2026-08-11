"""VALID3 — the RADIATION-DRIVING ENHANCEMENT of the acoustic amplitude, vs k.

WHY.  With Silk damping forced off the hierarchy still gives P1/P3 = 3.016 against a sky value of 2.257
that ALREADY includes full damping -- so the error is in the UNDAMPED acoustic amplitudes, not in any
suppression.  The mechanism that sets exactly that, mode by mode, is radiation driving: a mode entering
the horizon before equality is resonantly boosted by the decaying potential; one entering after is not.

THE BENCHMARK.  Radiation domination carries NO SCALE, so the enhancement must be
  * k-INDEPENDENT (a plateau) for k >> k_eq,
  * absent for k << k_eq,
with the transition at k_eq and a plateau height of the standard size.  Measured against the
Sachs-Wolfe value at k -> 0, the driven amplitude of Theta_0 + Psi should plateau near ~4-5x.
A plateau at the wrong HEIGHT, or a transition at the wrong k, is the error we are looking for.

The oscillator amplitude A = sqrt(x^2 + (dx/d eta)^2 / omega^2), x = Theta_0 + Psi, omega = k c_s, is
smooth through zero-crossings and is what sets peak heights.
"""
import os, numpy as np
os.environ.setdefault('NS1','2400'); os.environ.setdefault('NS2','1600')
os.environ['ESTORE']='0.5'; os.environ['STRIDE']='1'; os.environ['NODAMP']='1'
import HIER_photon_hierarchy as H

k_eq = 1.0/np.interp(1.0/(1+H.Om/H.Or_content), H.ag, H.eg)
kk = np.array([0.0012,0.0025,0.005,0.0080,0.0110,0.0159,0.024,0.032,0.0386,0.048,0.0586,0.075,0.095])
E,Y,esw = H.evolve(kk)

def amp_at(e_t):
    j=int(np.argmin(abs(E-e_t))); j=max(1,min(j,len(E)-2))
    def xof(i):
        Ph=Y[i,:,6]; sgn=Y[i,:,H.IN]/2
        Ps=Ph-6*H.Hc_of(E[i])**2*H.On_of(E[i])*sgn/kk**2
        return Y[i,:,2]/4+Ps
    x=xof(j); dx=(xof(j+1)-xof(j-1))/(E[j+1]-E[j-1])
    R=H.Rb_of(E[j]); w=kk/np.sqrt(3*(1+R))
    return np.sqrt(x**2+(dx/w)**2)

A = amp_at(H.eta_rec)
A0 = A[0]                               # the k->0 (Sachs-Wolfe) end of our own grid
print("="*76)
print("RADIATION-DRIVING ENHANCEMENT at recombination   (Silk damping OFF)")
print("  z_eq = %.0f   eta_eq = %.1f Mpc   k_eq = %.5f /Mpc"%(H.Om/H.Or_content, 1/k_eq, k_eq))
print("="*76)
print("     k        k/k_eq    |Theta_0+Psi|      relative to k->0")
for i,k in enumerate(kk):
    mark = "  <- P1" if abs(k-0.0159)<1e-6 else ("  <- P2" if abs(k-0.0386)<1e-6 else ("  <- P3" if abs(k-0.0586)<1e-6 else ""))
    print("  %8.5f   %7.2f   %12.5f   %12.3f%s"%(k, k/k_eq, A[i], A[i]/A0, mark))
print()
print("  EXPECTED: a rise through k ~ k_eq to a FLAT plateau for k >> k_eq (radiation")
print("  domination has no scale), plateau height ~4-5x the k->0 Sachs-Wolfe value.")
hi = A[kk/k_eq > 6]/A0
if len(hi) > 2:
    print("  MEASURED plateau: mean %.2f, spread %.1f%% over the k>>k_eq modes"
          %(hi.mean(), 100*(hi.max()-hi.min())/hi.mean()))
