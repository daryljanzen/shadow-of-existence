"""SOURCE_bisection  (r2354)

WHY THIS TEST.  The instrument's peak amplitudes run low relative to CAMB by 9.4% at P2 and 32% at
P3.  Converting to a scaling: ln(0.679)/ln(0.906) = 3.92 across a k-ratio whose square is 2.31, i.e.
the excess goes as k^3.3, NOT k^2.  A mis-set diffusion scale gives exactly k^2 (an error eps in k_D
puts ln(ratio) proportional to (k/k_D)^2 * 2 eps), and so does a too-wide visibility.  So the defect
is NOT in that class, and the stage whose ell-dependence is not constrained to k^2 is the PROJECTION.

THE BISECTION.  The peak amplitude is the end of three stages:
    source assembly  ->  visibility weighting  ->  projection onto j_l
CAMB exposes its own line-of-sight source as 'T_source' in get_time_evolution, so comparing sources
at matched k and eta splits the problem in one measurement:
    sources agree   -> the defect is in the projection (kernel, ell sampling, or the j_l integral)
    sources differ  -> the defect is upstream, and the difference's k/eta structure says where

CONVENTION DISCIPLINE.  Six convention errors this session say: establish a regime where the two
MUST agree trivially before reading any difference.  That regime is low k, where the source is
dominated by the monopole Theta_0 + Psi and the Doppler and ISW terms are small.  Only once the
comparison is calibrated there is the difference at the peak scales meaningful.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('ESTORE', '0.5')
os.environ.setdefault('STRIDE', '2')
os.environ.setdefault('ETAEND', '760')

import numpy as np
import camb
import HIER_photon_hierarchy as H

# k for l = 221, 537, 815 plus a low-k calibration mode
KK = np.array([0.0040, 0.0159, 0.0387, 0.0588])
LABELS = ['calib (low k)', 'P1', 'P2', 'P3']

print("=" * 92)
print("SOURCE vs PROJECTION -- where the peak-amplitude deficit enters")
print("=" * 92)

# ---- our side -------------------------------------------------------------
E, Y, esw = H.evolve(KK)
m = E > max(esw, H.eta_rec - 160.0)
ee = E[m]
Yv = Y[m]
g = np.array([float(H.g_of(e)) for e in ee])
tau = np.array([float(H.tau_of(e)) for e in ee])
Sm, Sd, Si, Sq = H.source_terms(ee, Yv, KK, g, tau)
S_ours = Sm + Si                      # the j_l-projected part; Sd and Sq have their own kernels

# ---- CAMB's side ----------------------------------------------------------
p = camb.CAMBparams()
p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674**2 - 0.02237,
                mnu=0.0, omk=0, tau=0.0544)
p.InitPower.set_params(As=2.1e-9, ns=0.965)
p.set_for_lmax(1600, lens_potential_accuracy=0)
res = camb.get_results(p)
ev = res.get_time_evolution(KK, ee, ['T_source'])     # (nk, neta, 1)
S_camb = ev[:, :, 0].T                                # -> (neta, nk)

print()
print("  visibility peak at eta = %.1f Mpc ; comparing over eta in [%.1f, %.1f]"
      % (ee[int(np.argmax(g))], ee[0], ee[-1]))
print()

# ---- calibrate on the low-k mode, where both must be monopole-dominated ----
iv = int(np.argmax(g))
cal = S_ours[iv, 0] / S_camb[iv, 0]
print("  CALIBRATION on the low-k mode at the visibility peak:")
print("     ours = %+.6e   CAMB = %+.6e   ratio = %.5f" % (S_ours[iv, 0], S_camb[iv, 0], cal))
print("     (one overall constant; it absorbs the primordial normalisation and sign convention)")
print()

print("  SOURCE ratio (ours/CAMB, after that single calibration), at the visibility peak:")
print("     %-16s %14s %14s %10s" % ("mode", "ours", "CAMB", "ratio"))
for j, lab in enumerate(LABELS):
    r = (S_ours[iv, j] / cal) / S_camb[iv, j]
    print("     %-16s %+14.6e %+14.6e %10.4f" % (lab, S_ours[iv, j] / cal, S_camb[iv, j], r))

print()
print("  and integrated over the visibility (the quantity the projection actually sees):")
w = g / np.trapezoid(g, ee)
print("     %-16s %10s" % ("mode", "ratio"))
for j, lab in enumerate(LABELS):
    a = np.trapezoid(S_ours[:, j] * w, ee) / cal
    b = np.trapezoid(S_camb[:, j] * w, ee)
    print("     %-16s %10.4f" % (lab, a / b if b != 0 else float('nan')))

print()
print("  READ:  ratios ~1 at P2/P3  ->  the sources agree and the defect is in the PROJECTION.")
print("         ratios ~0.91 and ~0.68  ->  the defect is upstream, in the source assembly.")
