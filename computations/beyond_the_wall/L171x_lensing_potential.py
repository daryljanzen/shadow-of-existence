#!/usr/bin/env python3
"""L171x_lensing_potential.py -- ** THE LENSING POTENTIAL C_l^phiphi, ON THIS INSTRUMENT'S OWN Phi. **

Built r2376+c54.182, front #2.

** WHY IT IS A SEPARATE INSTRUMENT AND NOT A FLAG ON THE TRANSFER. **  The line-of-sight solve stops
at eta = 4000, which is z = 12.8, because that is where the visibility and the ISW have finished.
** The lensing kernel does not finish there: it peaks at chi = chi_*/2, which is z ~ 3.3, and runs
to z = 0. **  So the potential has to be carried a further ten thousand Mpc, and carrying the whole
perturbation system that far to obtain one scalar would be silly.

** HOW Phi IS CARRIED, AND IT IS EXACT RATHER THAN FITTED. **  On sub-horizon scales in a universe
of matter and Lambda the linear potential obeys Phi(k, a) = Phi(k, a_ref) * g(a)/g(a_ref) with
g(a) = D(a)/a, and the growth factor is a background quadrature,

    D(a)  proportional to  H(a) INT_0^a  da' / (a' H(a'))^3 ,

so nothing about the k-dependence enters and no transfer function is imported. ** The k-dependence
comes from this instrument's OWN solve at eta_ref = 4000, where the modes are long since sub-horizon
and matter-dominated. **  *That is the whole content of the extension: one background integral, and
the shape taken from the solve that produced the temperature spectrum.*

** THE NORMALISATION IS NOT FREE, AND THAT IS THE POINT. **  The same primordial amplitude sets the
temperature spectrum and the lensing potential.  The temperature comparison fits ONE amplitude A in
closed form; that A fixes the absolute normalisation of Phi, so ** lensing enters the transfer with
NO new parameter. **  *An imported lensing amplitude would be a fitted parameter wearing a
derivation's clothes -- which is the thing this programme keeps refusing.*

  Limber:  C_l^phiphi = INT dchi  W(chi)^2 / chi^2  P_Phi( k = (l+1/2)/chi ; chi ),
           W(chi) = -2 (chi_* - chi) / (chi_* chi),   P_Phi(k) = 2 pi^2 Delta^2_Phi(k) / k^3.

** THE CHECK IS A NUMBER THIS FILE DOES NOT SET. **  The rms deflection of a CMB photon is about
2.7 arcmin and [l(l+1)]^2 C_l^phiphi / 2pi peaks near 1e-7 around l ~ 40.  Neither is used as an
input anywhere here, so both are tests.

Env: NKP (k-modes for Phi, default 220), KMIN, KMAX, ETAREF (default 4000), LMAXPHI (default 2000).
Run:  python3 L171x_lensing_potential.py
"""
import os
import sys

import numpy as np
from scipy.integrate import quad
from scipy.interpolate import CubicSpline

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
import ACOUSTIC_two_arm as A                                              # noqa: E402

NKP = int(os.environ.get('NKP', '220'))
KMIN = float(os.environ.get('KMIN', '2e-4'))
KMAX = float(os.environ.get('KMAX', '1.0'))
ETAREF = float(os.environ.get('ETAREF', '4000'))
NS = 0.965


def growth_over_a():
    """g(a) = D(a)/a from the background alone, normalised to 1 deep in matter domination

    ** D(a) prop. H(a) INT_0^a da'/(a' H(a'))^3 is exact for matter + Lambda, and this background
    is exactly that after radiation stops mattering. **  It is evaluated from A.Hphys, so the two
    arms get their own growth rather than a shared one.
    """
    def integrand(x):
        return 1.0 / (x * A.Hphys(x)) ** 3
    ag = np.logspace(-4, 0, 600)
    D = np.array([A.Hphys(x) * quad(integrand, 1e-8, x, limit=200)[0] for x in ag])
    g = D / ag
    g /= g[0]                                    # 1 deep in matter domination
    return CubicSpline(np.log(ag), g)


def phi_shape():
    """Phi(k) at eta_ref from THIS instrument's own solve -- the k-dependence, unnormalised"""
    kk = np.logspace(np.log10(KMIN), np.log10(KMAX), NKP)
    sol, nk, NV = A.evolve(kk, t_eval=np.array([ETAREF]), e_end=ETAREF)
    Y = sol.y.T.reshape(1, nk, NV)
    return kk, Y[0, :, 6]                        # Phi


def main():
    print()
    print("=" * 78)
    print("L171x — THE LENSING POTENTIAL, ON THIS INSTRUMENT'S OWN Phi")
    print("=" * 78)
    g = growth_over_a()
    a_ref = float(A.a_of_eta(ETAREF))
    print(f"  eta_ref = {ETAREF:.0f} (a = {a_ref:.5f}, z = {1/a_ref-1:.2f});  "
          f"eta_0 = {A.eta_0:.0f};  chi_* = {A.D_M:.0f} Mpc")
    print(f"  growth: g(a)/g(a_ref) runs {g(np.log(a_ref))/g(np.log(a_ref)):.3f} -> "
          f"{float(g(0.0))/float(g(np.log(a_ref))):.3f} between eta_ref and today")
    kk, Phi = phi_shape()
    print(f"  Phi shape from the solve: {len(kk)} modes, k = {kk[0]:.1e} to {kk[-1]:.1e} /Mpc")

    # ** Delta^2_Phi(k) at eta_ref.  Phi is dimensionless and the solve starts every mode at
    # Phi = -1, so the primordial tilt is put back here and the overall scale is carried by AMP. **
    D2 = (kk ** (NS - 1)) * Phi ** 2
    lnP = CubicSpline(np.log(kk), np.log(np.maximum(D2, 1e-300)))

    def D2_of(k, a):
        k = np.clip(k, kk[0], kk[-1])
        return np.exp(lnP(np.log(k))) * (float(g(np.log(a))) / float(g(np.log(a_ref)))) ** 2

    chis = A.D_M
    ls = np.unique(np.round(np.logspace(np.log10(2), np.log10(
        float(os.environ.get('LMAXPHI', '2000'))), 60)).astype(int))
    cl = np.empty(len(ls), float)
    for i, l in enumerate(ls):
        def integ(chi, l=l):
            if chi <= 1.0 or chi >= chis:
                return 0.0
            eta = A.eta_0 - chi
            if eta <= ETAREF:                    # inside the solve's own range: same scaling
                eta = ETAREF
            a = float(A.a_of_eta(min(max(eta, float(A.eg[0])), A.eta_0)))
            k = (l + 0.5) / chi
            W = -2.0 * (chis - chi) / (chis * chi)
            P = 2 * np.pi ** 2 * D2_of(k, a) / k ** 3
            return W ** 2 / chi ** 2 * P
        cl[i] = quad(integ, 1.0, chis, limit=300)[0]
    return ls, cl, kk, Phi


if __name__ == '__main__':
    ls, cl, kk, Phi = main()
    # AMP is the one thing not set here: it is the primordial normalisation, and it is fixed by the
    # SAME fitted amplitude the temperature comparison uses.  Reported as a shape plus the scaling.
    print()
    print(f"  {'l':>6} {'[l(l+1)]^2 C_l^phiphi / 2pi  (x AMP)':>40}")
    for i, l in enumerate(ls):
        if l in (2, 10, 40, 100, 400, 1000):
            print(f"  {l:>6} {(l*(l+1))**2*cl[i]/(2*np.pi):>40.4e}")
    j = int(np.argmax((ls * (ls + 1)) ** 2 * cl / (2 * np.pi)))
    print(f"\n  ** the deflection power peaks at l = {ls[j]} ** "
          f"(the standard result is l ~ 40-60)")
    d2 = np.trapezoid(ls * (ls + 1) * cl * (2 * ls + 1) / (4 * np.pi), ls)
    print(f"  rms deflection = {np.degrees(np.sqrt(d2))*60:.3f} arcmin x sqrt(AMP)  "
          f"(the standard result is ~2.7)")
    np.savez(os.environ.get('SAVEPHI', '/tmp/clpp.npz'), ls=ls, cl=cl, k=kk, Phi=Phi)
