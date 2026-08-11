"""HANDOVER_band  (r2360)

THE PREDICTION TO TEST.  At r2353 the tight-coupling handover was measured to be worth ~1.7% at the
P2 mode, with a sign that made P2 WEAKER as the switch moves earlier.  Against the then-truncated
spectrum, where P2 was already too weak, that was the wrong direction and the finding was recorded
as such.  The k-range fix (r2356-r2358) reversed the sign of the residual: P1/P2 is now 2.123
against a target of 2.202, i.e. P2 is too STRONG by ~3.7%.  So the same handover correction now
points the right way, and should be worth roughly half the remaining gap.

WHY BAND POWERS RATHER THAN THE SPECTRUM.  Running the full spectrum at KMAXL=2500 with TPSW=3.0
puts far more of a 907-mode evolution through the full hierarchy and exceeds the compute budget.
But B_l = int dk k^{ns-2} |Delta_l(k)|^2 is proportional to C_l, so the RATIO B_221/B_537 is
P1/P2 up to the l(l+1) weighting -- and here the k-grid and the l-count are ours to choose, which
makes it perhaps a tenth of the cost.  This is the same measure that located the defect at r2355,
and it is phase-insensitive by construction.

WHAT WOULD FALSIFY IT.  If the handover moves the band ratio the wrong way, or by much less than
1.7%, the residual is something else and the r2353 measurement does not transfer to the corrected
spectrum.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('ESTORE', '0.5')
os.environ.setdefault('STRIDE', '2')
os.environ.setdefault('ETAEND', '760')

import numpy as np
from scipy.special import spherical_jn
import HIER_photon_hierarchy as H

NS = 0.965
LS = [221, 537, 815]
NK = int(os.environ.get('NK', '700'))
KMAX = float(os.environ.get('KMAX', '0.16'))
kk = np.linspace(0.002, KMAX, NK)   # NK/KMAX exposed so convergence in BOTH can be tested

E, Y, esw = H.evolve(kk)
m = E > max(esw, H.eta_rec - 160.0)
ee = E[m]
Yv = Y[m]
g = np.array([float(H.g_of(e)) for e in ee])
tau = np.array([float(H.tau_of(e)) for e in ee])
Sm, Sd, Si, Sq = H.source_terms(ee, Yv, kk, g, tau)

eta0 = 14144.4
B = {}
for l in LS:
    x = kk[None, :] * (eta0 - ee)[:, None]
    jl = spherical_jn(int(l), x)
    jlp = spherical_jn(int(l), x, derivative=True)
    xs = np.maximum(x, 1e-8)
    Kq = 2.0 * (-3.0 * jlp / xs + (3.0 * l * (l + 1) / (2.0 * xs ** 2) - 1.0) * jl)
    D = np.trapezoid(Sm * jl + Si * jl + Sd * jlp + (Sq * Kq if Sq is not None else 0.0),
                     ee, axis=0)
    B[l] = float(np.trapezoid(kk ** (NS - 2.0) * D ** 2, kk))

# D_l = l(l+1)C_l/2pi, so the peak-ratio analogue carries the l(l+1) weight
def dl(l):
    return B[l] * l * (l + 1)

print("  TPSW = %s   (switch at eta = %.1f Mpc)"
      % (os.environ.get('TPSW', '0.6'), esw))
for l in LS:
    print("     B_%d = %.6e" % (l, B[l]))
print("     P1/P2 (band) = %.4f     P1/P3 (band) = %.4f"
      % (dl(221) / dl(537), dl(221) / dl(815)))
