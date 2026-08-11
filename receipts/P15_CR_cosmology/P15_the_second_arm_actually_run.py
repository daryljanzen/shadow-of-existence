#!/usr/bin/env python3
"""
RECEIPT — P15: ** THE SECOND BOLTZMANN ARM, ACTUALLY RUN.  THE SHAPE CROSS-VALIDATES; THE DEPTH
QUARTET THE CORPUS QUOTED DOES NOT REPRODUCE, AND IS WITHDRAWN. **

Built r2376+c54.153.  ** WHY IT EXISTS. **  P15 claimed that the low-multipole deficit had been
run a second time "on the photon hierarchy built for this programme", returning 0.42, 0.35, 0.29
and 0.52 at l = 2,3,4,5, and concluded that "two independent Boltzmann treatments cross-validate
the shape".  The receipt cited for that, `P15_the_low_ell_minimum_is_at_ell_four`, does not run
the hierarchy: it reads arm A out of the likelihood receipt's stored dict and ** reads arm B out
of the paper's own figure caption, by regular expression **.  So the cross-validation compared a
stored table against the citing paper's typography, and the quartet was banked nowhere.

** THIS FILE DRIVES THE HIERARCHY ITSELF. **  It evolves `HIER_photon_hierarchy` on a k-grid that
contains the discrete closed-S^3 ladder k_L = sqrt(L(L+2)) * stretch / D_M together with a dense
continuum grid, projects the module's own source terms to get Delta_l(k) for l = 2..44, and forms
the same two measures the CAMB arm forms: the discrete sum with the Harrison-Zel'dovich closed-S^3
weight w_L = (L+1)/(L(L+2)) against the continuum integral in dln k, each normalised to its own
l = 25-40 plateau.

  PART 1  ** the run: Delta_l(k) from the programme's own hierarchy, both measures **
  PART 2  ** THE SHAPE CROSS-VALIDATES: the minimum sits at l = 4 and recovery is by l ~ 7-8,
          independently of the CAMB arm and of the caption. **
  PART 3  ** THE DEPTHS DO NOT: this arm returns ~0.49/0.24/0.18/0.61 against CAMB's
          0.473/0.410/0.356/0.676, so the two treatments differ by up to a factor 1.9 at l = 3-4
          -- not the "uniformly 10-25% deeper" the corpus asserted.  ** The quartet 0.42/0.35/
          0.29/0.52 is reproduced by neither arm and is withdrawn. **

** WHAT THIS RECEIPT DOES AND DOES NOT SETTLE. **  It settles that the SHAPE claim is real and now
has a computation behind it, and that the DEPTH claim did not.  It does not settle which depth
table is right: the two treatments differ in the late-time ISW handling and in D_M (13864 here
against the projection's 13927), and this file makes no attempt to reconcile them.  ** The corpus
therefore has one converged depth table (the CAMB arm) and a second arm that agrees on shape and
not on depth, and that is what the paper now says. **

rc=0 on success.  Run: python3 P15_the_second_arm_actually_run.py   (numpy scipy; ~2 min)
"""
import os
import sys
import time

import numpy as np
from scipy.interpolate import interp1d
from scipy.special import spherical_jn

print(__doc__.split("rc=0")[0])
fail = []

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'storyboard_receipts'))
os.environ.setdefault('KMAXL', '700')

# =====================================================================
print("=" * 78)
print("PART 1 — THE RUN")
print("=" * 78)
t0 = time.time()
import HIER_photon_hierarchy as H              # noqa: E402  (env must be set first)

STRETCH = 2.75
Ls = np.arange(2, 260)
kL = np.sqrt(Ls * (Ls + 2)) * STRETCH / H.DM
kd = np.exp(np.linspace(np.log(kL[0] * 0.5), np.log(kL[-1]), 320))
kk = np.unique(np.concatenate([kL, kd]))
print(f"  modes: {len(kk)}   k = {kk[0]:.3e} .. {kk[-1]:.3e} /Mpc   D_M = {H.DM:.1f} Mpc")

E, Y, e_sw = H.evolve(kk)
m = E > max(e_sw, H.eta_rec - 160.0)
ee, Yv = E[m], Y[m]
g = np.array([float(H.g_of(e)) for e in ee])
tau = np.array([float(H.tau_of(e)) for e in ee])
Sm, Sd, Si, Sq = H.source_terms(ee, Yv, kk, g, tau)
has_q = Sq is not None
print(f"  hierarchy evolved and sources assembled in {time.time()-t0:.0f} s"
      f"   (quadrupole source: {has_q})")

x0m = H.eta_0 - ee
NS = 0.965
lnk = np.log(kk)
_u, _ix = np.unique(lnk, return_index=True)


def Delta(l):
    X = kk[None, :] * x0m[:, None]
    jl = spherical_jn(int(l), X)
    jlp = spherical_jn(int(l), X, derivative=True)
    it = Sm * jl + Sd * jlp + Si * jl
    if has_q:
        Xs = np.maximum(X, 1e-8)
        it = it + Sq * 2.0 * (-3.0 * jlp / Xs
                              + (3.0 * l * (l + 1) / (2.0 * Xs**2) - 1.0) * jl)
    return np.trapezoid(it, ee, axis=0)


wL = (Ls + 1.0) / (Ls * (Ls + 2.0))
ls = np.arange(2, 45)
Cc = np.zeros(len(ls))
Cd = np.zeros(len(ls))
for i, l in enumerate(ls):
    D = Delta(l)
    Cc[i] = np.trapezoid(kk**(NS - 1.0) * D**2, lnk)
    f = interp1d(_u, D[_ix], kind='cubic', bounds_error=False, fill_value=0.0)
    Cd[i] = np.sum(wL * kL**(NS - 1.0) * f(np.log(kL))**2)


def plateau(C):
    d = C * ls * (ls + 1)
    return d / np.mean(d[(ls >= 25) & (ls <= 40)])


ratio = plateau(Cd) / plateau(Cc)
if not np.all(np.isfinite(ratio)):
    fail.append("non-finite ratio")

# =====================================================================
print()
print("=" * 78)
print("PART 2 — THE SHAPE CROSS-VALIDATES")
print("=" * 78)
CAMB = {2: 0.473, 3: 0.410, 4: 0.356, 5: 0.676, 6: 0.916, 7: 0.984, 8: 0.998}
CAPTION = {2: 0.42, 3: 0.35, 4: 0.29, 5: 0.52}
print(f"  {'ell':>5} {'this arm (hierarchy)':>22} {'CAMB arm (banked)':>20} "
      f"{'the quoted quartet':>20}")
for l in range(2, 13):
    i = l - 2
    print(f"  {l:>5} {ratio[i]:>22.3f} "
          f"{('-' if l not in CAMB else f'{CAMB[l]:.3f}'):>20} "
          f"{('-' if l not in CAPTION else f'{CAPTION[l]:.3f}'):>20}")
lo = ratio[:4]
argmin_l = int(ls[:4][np.argmin(lo)])
rec = [int(l) for i, l in enumerate(ls) if ratio[i] > 0.95]
rec_l = rec[0] if rec else None
print(f"\n  ** minimum over l = 2..5:  this arm at l = {argmin_l};  CAMB arm at l = 4 **")
print(f"  ** first l with ratio > 0.95:  this arm {rec_l};  CAMB arm 8 **")
print("  ⇒ ** THE SHAPE IS CROSS-VALIDATED BY A COMPUTATION AND NOT BY A CAPTION: a second,")
print("     independently written Boltzmann treatment puts the minimum at the same multipole and")
print("     recovers at the same place. **")
if argmin_l != 4:
    fail.append(f"minimum at l={argmin_l}, not 4")
if rec_l is None or not (6 <= rec_l <= 9):
    fail.append(f"recovery at l={rec_l}")

# =====================================================================
print()
print("=" * 78)
print("PART 3 — THE DEPTHS DO NOT, AND THE QUARTET IS WITHDRAWN")
print("=" * 78)
sp_ratio = [CAMB[l] / ratio[l - 2] for l in (2, 3, 4, 5)]
print(f"  {'ell':>5} {'CAMB / this arm':>18}")
for l, r in zip((2, 3, 4, 5), sp_ratio):
    print(f"  {l:>5} {r:>18.2f}")
print(f"\n  ** the two treatments differ by a factor {min(sp_ratio):.2f} to {max(sp_ratio):.2f} "
      f"at l = 2-5 **")
print("  ** THE CORPUS ASSERTED 'UNIFORMLY 10-25% DEEPER' AND A SPECIFIC QUARTET.  Neither holds:")
print("     the disagreement is not uniform (it is small at l = 2 and nearly a factor 2 at l = 3-4)")
print("     and the quartet 0.42/0.35/0.29/0.52 is returned by neither arm. **")
print("  *The two arms differ in their late-time ISW handling and in D_M (13864 here against the")
print("  projection's 13927); this receipt does not reconcile them, and says so rather than")
print("  quoting a spread it has not established.*")
if max(sp_ratio) < 1.4:
    fail.append("the depth disagreement should be large; it is not")

# =====================================================================
print()
print("=" * 78)
if fail:
    print("FAILED: " + "; ".join(fail))
    sys.exit(1)
print("ALL CHECKS PASS — the shape cross-validates on a real second run; the depth quartet does")
print("not, and is withdrawn.")
print("=" * 78)
