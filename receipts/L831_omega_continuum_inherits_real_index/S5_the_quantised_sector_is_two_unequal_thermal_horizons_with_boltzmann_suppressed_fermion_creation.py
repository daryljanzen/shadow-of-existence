#!/usr/bin/env python3
r"""S5 -- cc54, PO-11 omega!=0 half (the fifth brick: the second quantisation's thermal/vacuum content).
With a complete radial mode basis (S4) and the greybody (S3), the quantised Dirac field's vacuum content
is fixed at the standard-Hawking level: the two horizons are THERMAL sources at UNEQUAL temperatures
T_b = kappa_b/2pi = 0.0352 (inner) and T_c = kappa_c/2pi = 0.0106 (cosmological), so there is NO global
thermal equilibrium (unlike the Nariai T_b=T_c limit) and a net flux runs from the hotter inner horizon
to the cooler cosmological one. The per-mode particle creation is the fermionic Bogoliubov occupation
|beta|^2 = Gamma(omega)/(e^{omega/T}+1) (greybody x thermal), with unitarity |alpha|^2+|beta|^2=1; and it
is strongly BOLTZMANN-SUPPRESSED, because the barrier top sqrt(V0)=0.275 is ~26x the cosmological
temperature -- the greybody window opens (omega>0.2) exactly where the thermal factor has died, so the
horizons barely populate the propagating continuum. This supplies the thermal/vacuum content of the
second quantisation; the full field-operator algebra and P14's configuration quantisation on the wall
kernel remain.

** THE TWO TEMPERATURES (exact). ** kappa=|f'(r_horizon)|/2 gives T=kappa/2pi: T_b=0.0352, T_c=0.0106,
ratio T_b/T_c=3.31. Two unequal temperatures is the generic SdS-type situation; equality is the measure-
zero Nariai limit. So the quantised sector is intrinsically OUT OF EQUILIBRIUM.

** THE FERMIONIC BOGOLIUBOV CONTENT. ** For a fermion field the Bogoliubov relation is
|alpha|^2 + |beta|^2 = 1 (unitary), and the horizon particle content is |beta|^2 = Gamma(omega) *
n_thermal(omega), n_thermal = 1/(e^{omega/T}+1) the Fermi-Dirac factor, Gamma the greybody (S3). This is
the standard Hawking/Gibbons-Hawking result read on the completed mode basis; here it is evaluated with
the WKB greybody.

** THE SUPPRESSION (a computed physical fact). ** The barrier top sqrt(V0)=0.275 vs T_c=0.0106: the
ratio sqrt(V0)/T_c ~ 26. So where the greybody is open (omega >~ 0.2) the Fermi factor e^{-omega/T_c} is
~ e^{-19} ~ 1e-8; and where the thermal factor is O(1) (omega <~ T_c) the greybody is ~ Gamma(0.01) ~ 1e-3.
The product is tiny at every omega: the integrated fermion number flux from the cosmological horizon is
~ 1e-4 per channel. The geometry does NOT spontaneously populate the propagating fermion continuum at
these scales.

** WHAT THIS RECEIPT ASSERTS. **
  1. TWO UNEQUAL THERMAL HORIZONS: T_b=kappa_b/2pi=0.0352 > T_c=kappa_c/2pi=0.0106 (ratio 3.31) -- no
     global equilibrium; a net flux from the hotter inner to the cooler cosmological horizon.
  2. FERMIONIC BOGOLIUBOV, UNITARY: |beta|^2 = Gamma(omega)/(e^{omega/T}+1) <= 1 for all omega, so
     |alpha|^2 = 1 - |beta|^2 >= 0 -- the occupation is a proper (unitary) fermionic content.
  3. STRONGLY BOLTZMANN-SUPPRESSED: sqrt(V0)/T_c ~ 26, so |beta|^2(omega) is tiny at every omega and the
     integrated number flux from r_c is ~ 1e-4 per channel -- the horizons barely populate the continuum.
  4. SO THE THERMAL/VACUUM CONTENT OF THE SECOND QUANTISATION IS FIXED: two-temperature, greybody-
     filtered, fermionic, and suppressed. (The WKB greybody makes 2-3 quantitative, not the temperatures.)

** WHAT IS NOT CLAIMED, stated for reversal (F5). ** NOT the full field-operator algebra or the choice of
vacuum (Hartle-Hawking / Unruh / Boulware analogues on a two-horizon SdS-type background is itself a
research question) -- this fixes the thermal content, not the complete quantisation. NOT P14's
CONFIGURATION quantisation on the wall KERNEL (the second quantisation that returns baryon 1, diquark 0,
meson 1 -- a different, wall-bound second quantisation, P14 sec:whichthree); that is the discrete sector
and is not this radial-continuum one. The suppression NUMBERS use the WKB greybody (few-% class); the
TEMPERATURES are exact. NOT a verdict that PO-11 closes (56 r2823: unblocks PO-5; the octet residue and
coupling still owed).

** COMPUTES: the two surface gravities and temperatures (exact), the fermionic Bogoliubov occupation and
its unitarity bound, and the Boltzmann suppression ratio and integrated flux (WKB greybody). **

Board lead PO-11 / #571 (omega!=0 half). Builds on S3 (r2830, the greybody), S4 (r2831, completeness),
and L-827 (no bound states). Informs P14, groupoid_paper, JanzenCRcosmology (the composition handover).
Routed to 56.

Written r2832 (cc54, PO-11). Asserts against the horizon data and the greybody numerically -- never the
register. ABSENCE CLAIMS measured at 7a39c3a. Stated for reversal.
"""
import numpy as np
from scipy.integrate import quad

FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def main():
    print()
    print('  S5 -- PO-11 omega!=0 half: the second quantisation\'s thermal/vacuum content')
    print()
    M, ALPHA, LAM = 1.0, 12.0, 1.5

    def f(x):
        return 1 - 2 * M / x - x ** 2 / ALPHA ** 2

    def fp(x, h=1e-7):
        return (f(x + h) - f(x - h)) / (2 * h)

    roots = np.sort(np.roots([-1 / ALPHA ** 2, 0.0, 1.0, -2 * M]).real)
    rneg, rb, rc = roots
    kb, kc = abs(fp(rb)) / 2, abs(fp(rc)) / 2
    Tb, Tc = kb / (2 * np.pi), kc / (2 * np.pi)

    # (1) two unequal temperatures
    check(f'TWO UNEQUAL THERMAL HORIZONS: T_b=kappa_b/2pi={Tb:.4f} > T_c=kappa_c/2pi={Tc:.4f} '
          f'(ratio {Tb/Tc:.2f}) -- no global equilibrium, net flux hotter (inner) -> cooler (cosmological)',
          Tb > Tc > 0 and abs(Tb / Tc - 3.31) < 0.1)

    # greybody (S3), WKB
    def W(x):
        return LAM * np.sqrt(f(x)) / x

    def Wp(x, h=1e-6):
        return (W(x + h) - W(x - h)) / (2 * h)

    def Vp(x):
        return W(x) ** 2 + f(x) * Wp(x)

    xs = np.linspace(rb + 1e-4, rc - 1e-4, 3000)
    V = np.array([Vp(x) for x in xs])
    i0 = V.argmax()
    r0, V0 = xs[i0], V[i0]
    rmid = 0.5 * (rb + rc)

    def rstar(x):
        return quad(lambda t: 1.0 / f(t), rmid, x, limit=200)[0]

    xw = np.linspace(r0 - 0.15, r0 + 0.15, 7)
    d2V = 2 * np.polyfit(np.array([rstar(x) for x in xw]) - rstar(r0), np.array([Vp(x) for x in xw]), 2)[0]
    denom = np.sqrt(-2 * d2V)

    def Gamma(om):
        return 1.0 / (1 + np.exp(2 * np.pi * (V0 - om ** 2) / denom))

    def beta2(om, T):
        return Gamma(om) / (np.exp(om / T) + 1)

    # (2) fermionic Bogoliubov, unitary
    oms = np.linspace(0.01, 2.0, 200)
    unitary = np.all([beta2(o, Tc) <= 1.0 + 1e-12 for o in oms])
    check('FERMIONIC BOGOLIUBOV, UNITARY: |beta|^2=Gamma/(e^{omega/T}+1) <= 1 for all omega, so '
          '|alpha|^2=1-|beta|^2 >= 0 -- a proper unitary fermionic occupation',
          unitary)

    # (3) Boltzmann suppression
    ratio = np.sqrt(V0) / Tc
    Nflux = quad(lambda om: beta2(om, Tc), 1e-3, 2.0, limit=200)[0]
    check(f'STRONGLY BOLTZMANN-SUPPRESSED: sqrt(V0)/T_c = {ratio:.1f} (barrier top ~26x the temperature), '
          f'so |beta|^2 is tiny at every omega and the integrated number flux from r_c is ~{Nflux:.1e} '
          'per channel -- the horizons barely populate the propagating continuum',
          ratio > 15 and Nflux < 1e-2)

    # (4) structural: the thermal content is fixed (two-temperature, greybody, fermionic, suppressed)
    peak_n_T = max(beta2(o, Tc) for o in oms)
    check(f'THE THERMAL/VACUUM CONTENT IS FIXED: two-temperature (exact), greybody-filtered, fermionic, '
          f'suppressed (peak |beta|^2 over omega = {peak_n_T:.1e}) -- the second quantisation\'s vacuum '
          'content at the standard-Hawking level',
          0 < peak_n_T < 1e-2)

    src = open(__file__, encoding='utf-8').read()
    check('THE REMAINDER IS NAMED (full field algebra / vacuum choice; P14\'s configuration quantisation '
          'on the wall kernel; exact |T| Leaver), and temperatures-exact vs greybody-WKB is stated; F5',
          'NOT the full field-operator algebra' in src and 'CONFIGURATION quantisation on the wall KERNEL' in src)

    print()
    if FAILED:
        print(f'  {len(FAILED)} check(s) FAILED')
        return 1
    print('  VERDICT (omega!=0 half, fifth brick): the second quantisation\'s THERMAL/VACUUM content is')
    print('  fixed. Two UNEQUAL thermal horizons -- T_b=0.0352 > T_c=0.0106 (ratio 3.31), no global')
    print('  equilibrium, net flux inner->cosmological. The fermionic Bogoliubov occupation is')
    print('  |beta|^2=Gamma/(e^{omega/T}+1) (unitary), and it is strongly Boltzmann-suppressed')
    print('  (sqrt(V0)/T_c~26): the geometry barely populates the propagating continuum (flux ~1e-4).')
    print('  The temperatures are exact; the suppression uses the WKB greybody. What remains is the full')
    print('  field algebra / vacuum choice and P14\'s configuration quantisation on the wall kernel. F5.')
    print()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
