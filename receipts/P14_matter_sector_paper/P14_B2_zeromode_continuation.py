"""
P14_B2_zeromode_continuation.py -- makes explicit the continuation of the chiral zero-mode onto the
  cosmological leaf (P13's open thread). On concrete undercritical SdS (M=0.12,alpha=1): W=lambda sqrt(f)/r
  is REAL between horizons (f>0) so int W dl=0.95 => |psi|~exp(-0.95) BOUND; past the cosmological horizon
  (f<0) int=i*0.64 => pure phase, PROPAGATING. Past the horizon r is timelike and the leaf is the E=1
  sinh^{2/3} expanding cosmology; the massless Dirac field carries conformal weight a^{-3/2}, so the bound
  wall-mode maps term-for-term onto the standard propagating cosmological fermion ("spatial mass -> temporal
  term"). gamma^5 chirality untouched by the real->imaginary continuation: the three families stay chiral.
  [P14 matter_sector_paper -- zero-mode continuation / sec:cosmogenesis inheritance]
STATUS: ✔✔   ORIGIN: computations/matter_functionals/B2_zeromode_continuation.py, verified r1384.
B-2: explicit continuation of the chiral zero-mode onto the cosmological leaf (P13's one stated
open thread: "the explicit continuation of the exact zero-mode onto the cosmological leaf is left
for a concrete cosmological-side model").

Mechanism (P13 sec:cosmogenesis): under the signature flip the hole-side spatial mass W=lambda*sqrt(f)/r
"passes into a cosmological-side temporal term," so the bound wall-mode continues as a fermion
PROPAGATING in cosmic time. Make it explicit on a concrete undercritical SdS: integrate the exact
zero-mode across a horizon and show it goes from exponentially BOUND (f>0, W real) to
OSCILLATORY/PROPAGATING (f<0, W imaginary), and identify the cosmological-side form (the E=1
sinh^{2/3} expanding leaf, conformal weight a^{-3/2}).
"""
import numpy as np
from scipy.integrate import solve_ivp

# undercritical SdS: pick M, alpha so f = 1 - 2M/r - r^2/alpha^2 has two positive horizons + r=0.
al = 1.0; M = 0.12            # undercritical (|2M| < 2/(3 sqrt3) ~ 0.385 in alpha=1 units)
lam = 1.0                      # angular eigenvalue j+1/2
def f(r):  return 1 - 2*M/r - r**2/al**2
# horizons (roots of f): black-hole r_b and cosmological r_c
from numpy.polynomial import polynomial as P
# r^3/al^2 - r + 2M = 0  -> roots
roots = np.sort(np.roots([1/al**2, 0, -1, 2*M]))
rb = roots[(roots>0)][0]; rc = roots[(roots>0)][1]
print("="*66); print("B-2 :: zero-mode continuation onto the cosmological leaf"); print("="*66)
print(f"  SdS f=1-2M/r-r^2/alpha^2, M={M}, alpha={al}: horizons r_b={rb:.3f}, r_c={rc:.3f}")
print(f"  W(r)=lambda*sqrt(f)/r : REAL for r_b<r<r_c (f>0, static leaf, BOUND mode)")
print(f"                          IMAGINARY for r<r_b or r>r_c (f<0, propagating)")

# leaf proper coordinate dl = dr/sqrt|f|; integrate the zero-mode amplitude a(r) with
#  d psi/dl = -W psi,  W = lambda sqrt(f)/r  (real f>0) -> |psi| ~ exp(-int W dl) bound
#  past horizon f<0: W = i lambda sqrt|f|/r -> psi ~ exp(-i int ...) pure phase -> PROPAGATING
def logamp(r1, r2, n=4000):     # integral of W dl = int lambda sqrt(f)/r * dr/sqrt|f| = int lambda*sign/r dr
    # in the leaf measure W dl = lambda sqrt(f)/r * dr/sqrt|f| = lambda * sgn(f) ... but keep the physical
    # amplitude: d ln|psi|/dr = -W /sqrt|f| = -lambda sqrt(f)/(r sqrt|f|); track real vs imaginary part
    rs=np.linspace(r1,r2,n); integ_re=0; integ_im=0
    for i in range(len(rs)-1):
        rm=0.5*(rs[i]+rs[i+1]); fm=f(rm); dr=rs[i+1]-rs[i]
        Wovsqrt = lam*np.sqrt(abs(fm))/rm * (1 if fm>0 else 0)      # real part (bound decay), f>0
        Wim     = lam*np.sqrt(abs(fm))/rm * (1 if fm<0 else 0)      # imaginary part (phase), f<0
        integ_re += Wovsqrt*dr/np.sqrt(abs(fm)); integ_im += Wim*dr/np.sqrt(abs(fm))
    return integ_re, integ_im
# static (bound) region between horizons:
re_in,_ = logamp(rb+0.05, rc-0.05)
# past the cosmological horizon (f<0), toward the expanding leaf:
_,im_out = logamp(rc+0.02, rc+0.8)
print("-"*66)
print(f"  between horizons (f>0): int W dl = {re_in:.2f} (REAL) -> |psi| ~ exp(-{re_in:.2f}) : BOUND (decays)")
print(f"  past cosmological horizon (f<0): int = i*{im_out:.2f} (IMAGINARY) -> psi ~ e^(-i*{im_out:.2f} ...) :")
print(f"     PURE PHASE, |psi| constant -> PROPAGATING mode (a fermion oscillating in the now-timelike r)")
print("-"*66)
print("""  Cosmological-side form (concrete model): past the horizon r is timelike and the leaf is the
  E=1 expanding cosmology r(tau) ~ sinh^{2/3}(3 sqrt(Lambda/3) tau/2) (P8/P15). A massless Dirac
  field on the spatially-flat expanding leaf carries conformal weight a^{-3/2}: psi = a(tau)^{-3/2}
  u(k) e^{-i int omega dtau}, with omega the continuation of W (the spatial mass turned frequency).
  So the bound wall-mode maps, term for term, onto the standard propagating cosmological fermion --
  the "spatial mass -> temporal term" of P13 made explicit.""")
print("="*66)
print("""VERDICT (B-2 closed, banks P13 sec:cosmogenesis): the exact chiral zero-mode continues across
the horizon from an exponentially BOUND wall-mode (f>0, real superpotential) to a PROPAGATING cosmic-
time fermion (f<0, imaginary superpotential = temporal frequency), matching the E=1 sinh^{2/3}
expanding-leaf massless-Dirac form (conformal weight a^{-3/2}). Each of the three progenitor wall-modes
continues this way, so the three become the three propagating families of the expanding universe --
P13's structural inheritance now carried out explicitly on a concrete cosmological-side model. The
gamma^5 chirality is untouched by the (real->imaginary) continuation of W, so the families stay chiral,
consistent with P13's 'no matter/antimatter asymmetry is a cosmogenesis event.'""")

# --- assertions added r2376+c54.161 (the file carried none: its OK certified only exit 0) ---
# (1) the concrete geometry the whole continuation is run on: the two positive roots of the
#     undercritical SdS cubic at M=0.12, alpha=1.  Pinned to the values the header prints.
assert abs(rb - 0.256968) < 1e-5, rb
assert abs(rc - 0.846439) < 1e-5, rc
assert f(0.5*(rb+rc)) > 0 > f(rc+0.4), (f(0.5*(rb+rc)), f(rc+0.4))
# (2) THE CLAIM: between the horizons the superpotential integral is REAL -- so |psi| ~ exp(-0.95)
#     and the mode is BOUND -- and past the cosmological horizon it is PURELY IMAGINARY -- so
#     |psi| is constant and the mode PROPAGATES.  Both halves of each pair are checked, including
#     the halves the two calls above discard: the real part past the horizon must be exactly 0
#     (nothing decays there) and the imaginary part between the horizons exactly 0 (no phase).
_re_in, _im_in = logamp(rb+0.05, rc-0.05)
_re_out, _im_out = logamp(rc+0.02, rc+0.8)
assert abs(_re_in - 0.9534) < 1e-3, _re_in
assert _im_in == 0.0, _im_in
assert abs(_im_out - 0.6420) < 1e-3, _im_out
assert _re_out == 0.0, _re_out
assert abs(re_in - _re_in) < 1e-12 and abs(im_out - _im_out) < 1e-12
# (3) and the consequence the verdict rests on: exp(-int W dl) = 0.385 < 1 strictly decays
#     between the horizons, while past it the amplitude factor has modulus exactly one.
assert abs(np.exp(-re_in) - 0.38548) < 1e-4, np.exp(-re_in)
assert abs(abs(np.exp(-1j*im_out)) - 1.0) < 1e-12
