"""
P13_kretschmann_bead.py -- verifies the Kretschmann scalar along the cosmogenetic bead: the MASS CANCELS.
  SdS K=48M^2/r^6+24/alpha^4; on the bead r^3=2M alpha^2 sinh^2(w) so r^6=4M^2 alpha^4 sinh^4(w), giving
  K=(12/alpha^4)(sinh^{-4}(3 tau~/2 alpha)+2) -- M-independent (verified across three M values at fixed w).
  [P13 boundary_paper]
STATUS: ✔✔   ORIGIN: storyboard_receipts/kretschmann_bead.py, verified r1382.The Kretschmann scalar along the bead: M CANCELS.

SdS:   K = 48 M^2 / r^6 + 24/alpha^4        (Lambda = 3/alpha^2)
Bead:  r^3 = 2M alpha^2 sinh^2(w),   w = 3 tau~ / 2 alpha        [thm:bead]

Then r^6 = (r^3)^2 = 4 M^2 alpha^4 sinh^4(w), so the mass cancels identically:

        K = (12/alpha^4) * ( sinh^{-4}(3 tau~/2 alpha) + 2 )

Along the comoving bead the curvature depends ONLY on alpha and cosmic time. The mass is invisible.

Near r=0 (s' the path length from r=0; sinh(3s'/2) ~ 3s'/2), one exponent gives both landmarks:
    r      ~  A (3s'/2)^{2/3}                ->  dr/ds ~ s'^{-1/3}  ->  VERTICAL TANGENT
    K      ~  12/(alpha^4 (3s'/2)^4)         ->  K     ~ s'^{-4}    ->  CURVATURE SINGULARITY
The vertical tangent of (F, flattened) and the r=0 curvature singularity are the SAME 2/3 power.
And the substrate is smooth there: (E)'s boing has X1 = -alpha, dX1/dr = 0 -- an ordinary minimum.
So the singularity is neither in the substrate nor in the mass: it is what the SO(3) sweep makes of a
smooth passage read through an areal radius shrinking to zero at infinite rate.
"""
import numpy as np, sympy as sp

M, al, w = sp.symbols('M alpha w', positive=True)
r3 = 2*M*al**2*sp.sinh(w)**2
K  = sp.simplify(48*M**2/r3**2 + 24/al**4)
assert sp.simplify(K - 12*(2 + sp.sinh(w)**-4)/al**4) == 0
print("K along the bead =", K, "   <- no M")

# numerical: same cosmic time, wildly different mass -> identical curvature
for twoM in (2e-3, 2/(3*np.sqrt(3)), 10.0):
    Mv = twoM/2
    for wv in (0.3, 1.0):
        r  = (2*Mv*np.sinh(wv)**2)**(1/3)
        Kv = 48*Mv**2/r**6 + 24
        assert abs(Kv - (12/np.sinh(wv)**4 + 24)) < 1e-9
        print(f"  2M={twoM:<8.4f} w={wv}:  r={r:.4f}  K={Kv:.6f}")
print("=> K identical at fixed w across 4 orders of magnitude in M, while r itself ranges 0.06..2.40.")

# the substrate is smooth at r=0: E's boing X1 = -alpha cos(2 pi r / sqrt3 alpha)
X1 = lambda r: -np.cos(2*np.pi*r/np.sqrt(3))
h  = 1e-5
d1 = (X1(h)-X1(-h))/(2*h); d2 = (X1(h)-2*X1(0)+X1(-h))/h**2
print(f"substrate at r=0:  X1={X1(0):+.4f}  dX1/dr={d1:+.2e}  d2X1/dr2={d2:+.4f}  -> ordinary smooth minimum")
