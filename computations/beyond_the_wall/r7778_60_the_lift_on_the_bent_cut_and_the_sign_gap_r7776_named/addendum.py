#!/usr/bin/env python3
"""r7778 (60) -- ADDENDUM.  Three POST-HOC checks, declared as post-hoc and changing NO criterion.

  (i)   arm 7 is two imaginary accumulations recomputed at 50 digits with mpmath and with BOTH
        inverse-square-root endpoints the lift has at BOTH ends on the bent cut -- because arm 7's
        result reversed the registered DIRECTION and a reversed sign must not rest on one quadrature.
  (ii)  arm 4's control recomputed as the MAXIMUM over the samples.  The registered criterion took
        the MINIMUM, and the minimum is small for a reason unrelated to the question, so the arm
        FAILS as registered and stays failed; this number says what the control would have shown.
  (iii) arm 8's segment boundaries refined off the log grid, whose resolution reported them to four
        figures only.
"""
import numpy as np
import sympy as sp
import mpmath as mp
from scipy.optimize import brentq

CLIGHT = 299792.458
H0, OM = 68.6, 0.2973
OMR = 4.15e-5 / (H0 / 100.0) ** 2
OL = 1.0 - OM
hub = H0 / CLIGHT
X0 = (2 * OL / OM) ** (1 / 3)
ALPHA = 1.0 / (hub * np.sqrt(OL))
R0 = ALPHA * X0 / np.sqrt(3.0)
TWOM = 2 * R0 ** 3 / (ALPHA ** 2 * X0 ** 3)
KRAD = hub ** 2 * OMR * R0 ** 4
RT = (TWOM * ALPHA ** 2) ** (1 / 3)

mp.mp.dps = 50
A, M2, KK = mp.mpf(ALPHA), mp.mpf(TWOM), mp.mpf(KRAD)


def rad_mp(s, K):
    return -M2 / s + K / s ** 2 + s ** 2 / A ** 2


def drad_mp(s, K):
    return M2 / s ** 2 - 2 * K / s ** 3 + 2 * s / A ** 2


def half(lo, hi, sing_at_lo, K):
    """u^2 = |s - s_end| removes the inverse square root at a SIMPLE zero of the radicand exactly.

    ** The guard is on the VALUE of the radicand and not on u == 0: at 50 digits a quadrature node
       can be close enough to the endpoint that lo + u**2 rounds TO the endpoint, where the
       radicand is exactly 0 -- a u == 0 guard alone raises ZeroDivisionError there, as it did. **
    """
    L = mp.sqrt(hi - lo)
    end = lo if sing_at_lo else hi
    lim = 1 / mp.sqrt(abs(drad_mp(end, K)))

    def g(u):
        s = lo + u ** 2 if sing_at_lo else hi - u ** 2
        v = -rad_mp(s, K)
        return lim if v <= 0 else u / mp.sqrt(v)

    return 2 * mp.quad(g, [0, L])


print("=" * 100)
print("(i)  the two imaginary accumulations at 50 digits, endpoints substituted away")
target = mp.pi * A / 3
rtm = mp.findroot(lambda s: rad_mp(s, mp.mpf(0)), mp.mpf(RT))
mid_v = rtm / 2
im_vac = (mp.quad(lambda s: 1 / mp.sqrt(-rad_mp(s, mp.mpf(0))), [0, mid_v])
          + half(mid_v, rtm, False, mp.mpf(0)))
print(f"  vacuum r_t      = {mp.nstr(rtm, 20)} Mpc")
print(f"  vacuum |Im tau| = {mp.nstr(im_vac, 22)} Mpc")
print(f"  pi*alpha/3      = {mp.nstr(target, 22)} Mpc")
print(f"  relative        = {mp.nstr((im_vac - target) / target, 6)}"
      "   <= the printed bound reproduced; nothing of M in it")
s_in = mp.findroot(lambda s: rad_mp(s, KK), mp.mpf('1.4983879'))
s_out = mp.findroot(lambda s: rad_mp(s, KK), mp.mpf('3791.7273'))
mid = (s_in + s_out) / 2
im_bent = half(s_in, mid, True, KK) + half(mid, s_out, False, KK)
print(f"  the lift's ends : s_in = {mp.nstr(s_in, 20)}   s_out = {mp.nstr(s_out, 20)}")
print(f"  bent   |Im tau| = {mp.nstr(im_bent, 22)} Mpc")
print(f"  bent - bound    = {mp.nstr(im_bent - target, 12)} Mpc"
      f"  =  {mp.nstr((im_bent - target) / target, 8)} relative")
print(f"  ** the bend {'EXCEEDS' if im_bent > target else 'undershoots'} the printed bound -- the"
      " REGISTERED DIRECTION WAS THE OTHER ONE **")
print(f"  and the mechanism: the lift is SHORTER in r by"
      f" {mp.nstr((rtm - s_out) + s_in, 10)} Mpc, while the EVEN term K/s^2")
print(f"  reduces |radicand| across the interior, so 1/sqrt(|.|) rises:  at the midpoint"
      f" s = {mp.nstr(mid, 10)},")
print(f"  |rad| vacuum = {mp.nstr(-rad_mp(mid, mp.mpf(0)), 10)}   bent ="
      f" {mp.nstr(-rad_mp(mid, KK), 10)}   ({mp.nstr((rad_mp(mid, KK) - rad_mp(mid, mp.mpf(0))) / rad_mp(mid, mp.mpf(0)), 6)} relative)")
print("  the integrand's rise beats the interval's shortening, and the net is the +3.05e-4 above")

print("=" * 100)
print("(ii) arm 4's control, as the MAXIMUM instead of the registered minimum")
tau = sp.Symbol('tau', real=True)
als, TwoMs = sp.symbols('alpha twoM', positive=True)
r_conj = -(TwoMs * als ** 2) ** sp.Rational(1, 3) * sp.cosh(3 * tau / (2 * als)) ** sp.Rational(2, 3)
sub = {TwoMs: TWOM, als: ALPHA}
F = sp.lambdify(tau, (sp.diff(r_conj, tau) ** 2).subs(sub), 'numpy')
Gp = sp.lambdify(tau, (TwoMs / r_conj + r_conj ** 2 / als ** 2).subs(sub), 'numpy')
Gm = sp.lambdify(tau, (-TwoMs / r_conj + r_conj ** 2 / als ** 2).subs(sub), 'numpy')
samples = np.linspace(0.05, 4.0, 9) * ALPHA
rel_p = [abs(F(t) - Gp(t)) / abs(Gp(t)) for t in samples]
rel_m = [abs(F(t) - Gm(t)) / abs(Gm(t)) for t in samples]
print(f"  2M positive : max {max(rel_p):.3e}   min {min(rel_p):.3e}")
print(f"  2M flipped  : max {max(rel_m):.3e}   min {min(rel_m):.3e}  <-- the registered criterion read")
_t = samples[int(np.argmin(rel_m))]
_rc = sp.lambdify(tau, r_conj.subs(sub), 'numpy')
_r = abs(float(_rc(_t)))
_mass, _vac = TWOM / _r, _r ** 2 / ALPHA ** 2
print(f"                the MIN, which falls at tau = {_t / ALPHA:.2f} alpha, where |r| = {_r:.1f} Mpc")
print(f"                and the two terms are  2M/|r| = {_mass:.6e}  against  r^2/alpha^2 ="
      f" {_vac:.6e},")
print(f"                so the term the control was meant to discriminate carries"
      f" {_mass / (_mass + _vac):.3e} of the sum there.")
print("  ** A CONTROL EVALUATED WHERE THE DISCRIMINATING TERM IS NEGLIGIBLE DISCRIMINATES NOTHING. **")

print("=" * 100)
print("(iii) arm 8's segment boundaries, off the grid")


def rad(s, K):
    return -TWOM / s + K / s ** 2 + s ** 2 / ALPHA ** 2


b_vac = brentq(lambda s: rad(s, 0.0), 1.0, 5e4, xtol=1e-12)
print(f"  vacuum: NEGATIVE on (0, {b_vac:.9f}), POSITIVE above.  2 segments; r_t = {RT:.9f}")
print(f"  bent:   POSITIVE on (0, {float(s_in):.9f}), NEGATIVE on ({float(s_in):.9f}, "
      f"{float(s_out):.9f}), POSITIVE above.  3 segments")
print("=" * 100)
