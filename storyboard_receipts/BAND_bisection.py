"""BAND_bisection  (r2355)

THE QUESTION.  The instrument's peak amplitudes run low against CAMB by 9.4% at P2 and 32% at P3,
and the excess scales as k^3.3 rather than k^2 -- which excludes a mis-set diffusion scale and a
too-wide visibility, both of which give exactly k^2.  The remaining split is:

    source assembly   ->   projection onto j_l

WHY THE PREVIOUS ATTEMPTS FAILED.  The sources oscillate in eta and Delta_l(k) oscillates in k, so
comparing at a single k or a single eta is phase-sensitive: two calculations agreeing perfectly can
differ by any factor at a chosen point.  r2354 produced sign-alternating ratios this way and then a
non-monotone 1.47/1.74/1.68 that measured nothing interpretable.

THE FIX.  Integrate over a k-band, exactly as the envelope measure does when it compares at extrema.
The band power

    B_l  =  int dk  k^{ns-2}  |Delta_l(k)|^2

is what actually enters C_l (up to constants), and it is phase-insensitive by construction: the
oscillations are squared and integrated over.  Forming it for OURS and for CAMB, on the SAME k-grid
and the SAME eta-grid and with the SAME projection code, isolates the two stages cleanly:

    B_l(ours)/B_l(CAMB) tracks the peak deficit   ->  the defect is in the SOURCE
    B_l ratios flat while the peaks differ        ->  the defect is in the PROJECTION or downstream

NORMALISATION.  Our source carries a per-mode normalisation (Phi_0 = -1 for every k) while CAMB's
carries the primordial spectrum.  That is a k-dependent factor and it must be divided out, not
absorbed into one constant.  We take it from the sources themselves in a regime where both are
monopole-dominated and non-oscillatory -- deep super-horizon at the visibility peak -- and then
apply the SAME k-dependent factor at every l.  If that factor is right, the l=221 band ratio should
come out near unity, because P1 is the peak both calculations agree on.  That is the test's own
control, and it is checked before anything else is read.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('ESTORE', '0.5')
os.environ.setdefault('STRIDE', '2')
os.environ.setdefault('ETAEND', '760')

import numpy as np
from scipy.special import spherical_jn
import camb
import HIER_photon_hierarchy as H

NS = 0.965
LS = [221, 537, 815]
KLO, KHI, NK = 0.002, 0.10, 900

kk = np.linspace(KLO, KHI, NK)

print("=" * 92)
print("BAND-INTEGRATED BISECTION -- source vs projection, phase-insensitive")
print("=" * 92)

# ---------- our side ----------
E, Y, esw = H.evolve(kk)
m = E > max(esw, H.eta_rec - 160.0)
ee = E[m]
Yv = Y[m]
g = np.array([float(H.g_of(e)) for e in ee])
tau = np.array([float(H.tau_of(e)) for e in ee])
Sm, Sd, Si, Sq = H.source_terms(ee, Yv, kk, g, tau)
# r2355 control caught this: CAMB's T_source is the FULL source, so ours must be too --
# each term with ITS OWN kernel (Doppler with j_l', quadrupole with j_l + 3 j_l''), exactly as
# the spectrum code projects them.  Comparing Sm+Si alone against CAMB's full source gave a
# l=221 control ratio of 1.605 with 47% normalisation scatter -- correctly unreadable.
S_ours = Sm + Si   # monopole + ISW; Sd and Sq are projected separately below

# ---------- CAMB's side, same k and eta ----------
p = camb.CAMBparams()
p.set_cosmology(H0=67.40, ombh2=0.02237, omch2=0.3150 * 0.674**2 - 0.02237,
                mnu=0.0, omk=0, tau=0.0544)
p.InitPower.set_params(As=2.1e-9, ns=NS)
p.set_for_lmax(1600, lens_potential_accuracy=0)
res = camb.get_results(p)
eta0 = res.conformal_time(0.0)
S_camb = res.get_time_evolution(kk, ee, ['T_source'])[:, :, 0].T

print()
print("  grid: %d k in [%.3f, %.3f] ; %d eta in [%.1f, %.1f] ; eta_0 = %.1f"
      % (NK, KLO, KHI, len(ee), ee[0], ee[-1], eta0))

# ---------- the per-mode normalisation, taken from the sources ----------
# visibility-weighted RMS is phase-insensitive and monopole-dominated at the peak
sel = g > 0.02 * g.max()
w = g[sel]


def rms(S):
    return np.sqrt(np.trapezoid((S[sel] ** 2) * w, ee[sel]) / np.trapezoid(w, ee[sel]))


# The per-mode normalisation is KNOWN, not fitted.  Ours sets Phi_0 = -1 for every k; CAMB's
# source carries the primordial curvature perturbation with P_zeta = A_s (k/k_piv)^{ns-1}, so
# |zeta| ~ sqrt(A_s) (k/k_piv)^{(ns-1)/2}.  Fitting it from RMS of oscillating sources gave 47%
# scatter and a failed control; the analytic factor has no such freedom.  One overall constant
# remains (our Phi_0 vs zeta normalisation) and is fixed by the l=221 control.
kpiv = 0.05
prim = np.sqrt(2.1e-9) * (kk / kpiv) ** ((NS - 1.0) / 2.0)
nrm = 1.0 / prim
print('  per-mode normalisation: analytic, sqrt(A_s)(k/k_piv)^{(ns-1)/2} -- no fitted scatter')

S_ours_n = S_ours / nrm[None, :]
Sd_n = Sd / nrm[None, :]
Sq_n = (Sq / nrm[None, :]) if Sq is not None else None

# ---------- band powers ----------
print()
print("  BAND POWER  B_l = int dk k^{ns-2} |Delta_l(k)|^2, same projection code both sides")
print("     %5s %14s %14s %10s   %s" % ("l", "ours", "CAMB", "ratio", "peak deficit to explain"))
targets = {221: 1.000, 537: 0.906, 815: 0.679}
for l in LS:
    x = kk[None, :] * (eta0 - ee)[:, None]
    jl = spherical_jn(int(l), x)
    jlp = spherical_jn(int(l), x, derivative=True)
    xs = np.maximum(x, 1e-8)
    Kq = 2.0 * (-3.0 * jlp / xs + (3.0 * l * (l + 1) / (2.0 * xs ** 2) - 1.0) * jl)
    Do = np.trapezoid(S_ours_n * jl + Sd_n * jlp + (Sq_n * Kq if Sq is not None else 0.0), ee, axis=0)
    Dc = np.trapezoid(S_camb * jl, ee, axis=0)
    wgt = kk ** (NS - 2.0)
    Bo = np.trapezoid(wgt * Do ** 2, kk)
    Bc = np.trapezoid(wgt * Dc ** 2, kk)
    print("     %5d %14.6e %14.6e %10.4f   %.3f"
          % (l, Bo, Bc, Bo / Bc if Bc else float('nan'), targets[l]))

print()
print("  CONTROL: the l=221 ratio must come out near 1 -- P1 is the peak both agree on.")
print("  If it does not, the per-mode normalisation is wrong and nothing below it is readable.")
print()
print("  READ: ratio tracking the deficit column  -> the defect is in the SOURCE")
print("        ratio flat near 1 while peaks differ -> the defect is DOWNSTREAM of the source")
