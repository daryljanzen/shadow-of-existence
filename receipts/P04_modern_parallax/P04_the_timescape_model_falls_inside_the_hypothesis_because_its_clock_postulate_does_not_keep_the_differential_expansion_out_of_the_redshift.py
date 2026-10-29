#!/usr/bin/env python3
"""P4 sec:timescape -- THE TIMESCAPE MODEL FALLS INSIDE THE HYPOTHESIS THE FLOOR TESTS: its walls and voids expand at
different rates in the volume-average time, and its clock postulate does not keep that difference out of the
redshift.  A photon gains the local rate per unit of local proper time, so per unit of volume-average time it gains
the region's own rate, H_v or H_w; the clock rates enter only at the ends of the path.

WHAT IS CHECKED (the computation the chat seat 72 supplied at r7623, on Daryl's direction, from Wiltshire 2009,
PRD 80, 123512, eqs. 10, 11, 14, 15, 38, 39):
  * the tracker identities (f_v, abar, Hbar normalised today; the volume average f_v H_v + (1-f_v) H_w = Hbar);
  * the backreaction computed two ways, Q = 6 f_v (1-f_v)(H_v-H_w)^2 = 2 fdot^2 / (3 f_v (1-f_v));
  * the mean of the accumulation reproducing the model's own redshift relation, eq. 38;
  * the rms of ln(1+z) across directions for independent void/wall cells of 10, 30 and 50 h^-1 Mpc
    (2.4e-2, 4.2e-2, 5.4e-2), against the whole measured anisotropy 4.1e-5 (600 to 1300 times);
  * the analytic variance against a Monte Carlo of 4000 rays (30 h^-1 Mpc cells, within 5 per cent).
"""

import numpy as np
from scipy.integrate import quad
f0 = 0.762; b = 2*(1-f0)*(2+f0)/(9*f0); t0 = (2+f0)/3
fv   = lambda t: 2*t/(2*t+3*b)
fdot = lambda t: 6*b/(2*t+3*b)**2
abar = lambda t: 3*t*f0**(1/3)*fv(t)**(-1/3)/(2+f0)
Hbar = lambda t: 2/(3*t) + 2/(3*(2*t+3*b))
assert abs(fv(t0)-f0) < 1e-12 and abs(abar(t0)-1) < 1e-12 and abs(Hbar(t0)-1) < 1e-12
# h_r from the tracker: gamma_w(eq.38 ratio) = (2+f_v)/2 -> h_r = 2/3; check Q two ways
hr = 2/3
Hv = lambda t: Hbar(t)*3/(2+fv(t)); Hw = lambda t: hr*Hv(t)
for t in [0.1, 0.5, t0]:
    assert abs(fv(t)*Hv(t)+(1-fv(t))*Hw(t) - Hbar(t)) < 1e-12          # volume average
    Q1 = 6*fv(t)*(1-fv(t))*(Hv(t)-Hw(t))**2; Q2 = 2*fdot(t)**2/(3*fv(t)*(1-fv(t)))
    assert abs(Q1/Q2-1) < 1e-10, (Q1, Q2)
H0_dressed = (4*f0**2+f0+4)/(2*(2+f0))          # in units of Hbar0
print(f"gamma_w0 = {(2+f0)/2:.3f}, H_w/H_v = {hr:.3f}, Hbar0/H0 = {1/H0_dressed:.4f}")
RMS = {}
for Lh in [10, 30, 50]:                          # comoving cell, h^-1 Mpc (dressed h)
    L = Lh/2997.9 * H0_dressed                  # in c/Hbar0
    zdec_t = 1e-6
    s2 = quad(lambda t: (2*fdot(t)**2/(3*fv(t)*(1-fv(t))))/6 * abar(t)*L, zdec_t, t0, limit=400)[0]
    print(f"cell {Lh:3d} h^-1 Mpc: rms of ln(1+z) across directions = {np.sqrt(s2):.2e}")
    RMS[Lh] = np.sqrt(s2)

# (i) the mean of the accumulation is timescape's own redshift, eq. (38): exp(int_t^t0 Hbar) * gamma_w(t)/gamma_w0
gw = lambda t: (2+fv(t))/2
for t in [0.05, 0.3, 0.8]:
    mean = np.exp(quad(Hbar, t, t0)[0]) * gw(t)/gw(t0)
    eq38 = (2+fv(t))*fv(t)**(1/3)/(3*f0**(1/3)*t)
    assert abs(mean/eq38-1) < 1e-8, (mean, eq38)
print("mean accumulation reproduces timescape eq. (38): OK")

# (ii) Monte Carlo rays through random void/wall cells confirm the variance formula (30 h^-1 Mpc cells)
rng = np.random.default_rng(1)
L = 30/2997.9*H0_dressed
# march backward from t0: each cell takes dt = abar(t) L of volume-average time
ts = [t0]
while ts[-1] > 1e-4:
    ts.append(ts[-1] - abar(ts[-1])*L)
ts = np.array(ts[:-1]); dts = abar(ts)*L
dH = (Hv(ts)-Hw(ts))*dts
var_an = np.sum(fv(ts)*(1-fv(ts))*dH**2)
nray = 4000
draws = (rng.random((nray, ts.size)) < fv(ts)).astype(float)
dev = ((draws - fv(ts)) * dH).sum(axis=1)
print(f"cells per ray {ts.size}; rms analytic {np.sqrt(var_an):.3e}, Monte Carlo {dev.std():.3e}")
assert abs(dev.std()/np.sqrt(var_an)-1) < 0.05
# (iii) PINNED: the figures P4 sec:timescape quotes, against the whole measured anisotropy (P4 sec:floor, Planck 2018)
for Lh, quoted in [(10, 2.4e-2), (30, 4.2e-2), (50, 5.4e-2)]:
    assert abs(RMS[Lh] - quoted) < 0.05e-2, (Lh, RMS[Lh], quoted)
ANISO = 4.1e-5
ratios = [RMS[Lh]/ANISO for Lh in (10, 50)]
print(f"against the whole measured anisotropy {ANISO:.1e}: {ratios[0]:.0f} to {ratios[1]:.0f} times")
assert 550 < ratios[0] < 650 and 1250 < ratios[1] < 1400, ratios
assert abs((2+f0)/2 - 1.381) < 1e-3 and abs(hr - 2/3) < 1e-12      # wall clocks 38 per cent slow; H_w/H_v = 2/3
print(f"wall clocks against void clocks today: gamma_w0 - 1 = {100*((2+f0)/2-1):.0f} per cent")
assert round(100*((2+f0)/2-1)) == 38
print("ALL PASS")