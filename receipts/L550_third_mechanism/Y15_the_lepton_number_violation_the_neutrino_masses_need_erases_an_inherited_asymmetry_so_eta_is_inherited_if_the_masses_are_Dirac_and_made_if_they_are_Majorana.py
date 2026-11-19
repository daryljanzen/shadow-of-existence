"""Y15 -- the lepton-number violation Majorana neutrino masses need erases an inherited asymmetry, so eta
is inherited if the masses are Dirac and made on the expanding leg if they are Majorana.

Y13/Y14: the lepton-number operators are completed by gauge singlets the construction does not supply.
The lead was whether the singlets leave a trace.  They leave none of their own; what they share with
the operators they complete -- lepton-number violation -- reaches the baryon-to-photon ratio, which P16
carries through the lap by a conservation law.  Above the electroweak crossover sphalerons change baryon
number, so the charge that carries eta there is B - L.

Computed here:
  (1) a singlet of mass M_S coupled to a lepton doublet with Yukawa y gives the light neutrinos
      m = y^2 v^2/M_S, and its decay parameter K = Gamma/H(T = M_S) = m/m_*, with
      m_* = 16 pi^(5/2) sqrt(g*) v^2/(3 sqrt5 M_Pl) = 1.07e-3 eV, whatever M_S and y: K = 47 at the
      atmospheric mass, 8 at the solar.  So the singlets decay as fast as they are made, at T ~ M_S,
      with no relic and no entropy release.  CONTROL: int_0^inf z^3 K1(z)/4 dz = 3 pi/8.
  (2) the dimension-five lepton-number violation is in equilibrium above
      T_eq = 1.66 sqrt(g*) pi^3 v^4/(3 mbar^2 M_Pl) = 5e12 GeV (1.7e13 on the single-flavour rate of
      hep-ph/9503335); sphalerons run from about 7e11 GeV down to 131.7 GeV.
  (3) a plasma in equilibrium (below alpha^2 M_Pl/1.66 sqrt(g*) = 4.4e14 GeV, 86 T_eq) that passes T_eq
      -- on the infall to the regulated peak and again on the expanding leg -- has its lepton number
      driven to zero with exponent T/T_eq - 1 = 85; with lepton number the fourth colour, unbroken
      there (v_PS = v_R in the window), baryon and lepton number are not separate charges, so B - L goes.
  (4) the right-handed neutrinos' inverse decays (K = m_nu/m_*) wash B - L out while the sphalerons
      run: survival exp(-K int_0^{m_N/131.7} z^3 K1/4).  Half survives at m_N = 78 to 153 GeV (K = 47
      to 8), v_R = 3.1e8 to 4.3e8 GeV at M = 1.2e15 GeV.
  (5) made instead by the right-handed neutrinos' own decays: the CP asymmetry is bounded by
      3 m_N m_atm/(16 pi v^2) and the efficiency at K = 47 is 5.2e-3 (the standard fit), so
      eta = 0.96e-2 eps kappa = 6.1e-10 needs m_N > 1.2e11 GeV, v_R > 1.2e13 GeV -- inside the window
      below the strong-CP cap 2.4e13.
  (6) Dirac masses (lepton number exact) conserve B - L throughout, and make the right-handed neutrinos
      light: Delta N_eff >= 0.141, 2.7 sigma above the joint ACT value (Y11).

Bound: unflavoured, hierarchical, order-one coefficients; inverse decays only in (4) (scatterings add
washout); g* = 106.75; the Davidson--Ibarra bound and the Buchmueller--Di Bari--Pluemacher efficiency
fit in (5); the regulated peak read as thermal plasma, as P15 reads it.

COMPUTES: closed forms, quadrature and root-finding; P16 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import k1

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
MPL, V, GS = 1.221e19, 174.10, 106.75
M_ATM, M_SOL = 0.0500e-9, 0.0086e-9
MSCALE = 246.22 ** 2 / M_ATM
T_SPH_OFF = 131.7
ETA_OBS = 6.1e-10
CAP = 2.4e13


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def hub(t):
    return 1.66 * math.sqrt(GS) * t ** 2 / MPL


def w(z):
    return z ** 3 * k1(z) / 4


def survival(m_n, k):
    return math.exp(-k * quad(w, 0, m_n / T_SPH_OFF, limit=200)[0])


def main():
    print()
    print('  Y15 -- lepton-number violation and the inherited asymmetry')
    print()
    mstar = 16 * math.pi ** 2.5 * math.sqrt(GS) * V ** 2 / (3 * math.sqrt(5) * MPL)
    k_atm, k_sol = M_ATM / mstar, M_SOL / mstar
    check(f'(1) m_* = {mstar * 1e9:.2e} eV; K = {k_atm:.0f} (atmospheric), {k_sol:.1f} (solar)',
          abs(mstar * 1e9 - 1.07e-3) < 0.02e-3 and round(k_atm) == 47 and abs(k_sol - 8.0) < 0.1)
    for y in (0.1, 1.0, 3.0):
        ms = y ** 2 * V ** 2 / M_ATM
        g = y ** 2 * ms / (8 * math.pi)
        check(f'(1) y = {y}: M_S = {ms:.1e} GeV, Gamma/H(M_S) = {g / hub(ms):.1f}, lifetime {6.582e-25 / g:.1e} s',
              abs(g / hub(ms) - k_atm) / k_atm < 0.01)
    check(f'CONTROL (1): int z^3 K1/4 = {quad(w, 0, 80)[0]:.6f} = 3 pi/8 = {3 * math.pi / 8:.6f}',
          abs(quad(w, 0, 80)[0] - 3 * math.pi / 8) < 1e-8)

    mbar2 = M_ATM ** 2 + M_SOL ** 2
    t_eq = 1.66 * math.sqrt(GS) * math.pi ** 3 * V ** 4 / (3 * mbar2 * MPL)
    t_cko = 17 * math.pi ** 5 * V ** 4 / (9 * M_ATM ** 2 * MPL)
    t_sph = 25 * (1 / 30) ** 5 * MPL / (1.66 * math.sqrt(GS))
    check(f'(2) lepton-number violation in equilibrium above {t_eq:.1e} GeV ({t_cko:.1e} on the single-flavour rate); '
          f'sphalerons below {t_sph:.1e} GeV', 3e12 < t_eq < 8e12 and 1e13 < t_cko < 3e13 and 5e11 < t_sph < 1e12)
    t_gauge = (1 / 40) ** 2 * MPL / (1.66 * math.sqrt(GS))
    check(f'(3) the plasma is in equilibrium below {t_gauge:.1e} GeV, {t_gauge / t_eq:.0f} times T_eq: '
          f'washout exponent {t_gauge / t_eq - 1:.0f}', t_gauge / t_eq > 50)

    for k in (k_atm, k_atm / 3, k_sol):
        half = brentq(lambda m: survival(m, k) - 0.5, 1, 1e4)
        milli = brentq(lambda m: survival(m, k) - 1e-3, 1, 1e5)
        print(f'      K = {k:5.1f}: half survives at m_N = {half:5.0f} GeV (v_R = {math.sqrt(half * MSCALE):.1e}); '
              f'a thousandth at {milli:5.0f} GeV (v_R = {math.sqrt(milli * MSCALE):.1e}); '
              f'at v_R = 1e10, {survival(1e20 / MSCALE, k):.0e}')
    lo = brentq(lambda m: survival(m, k_atm) - 0.5, 1, 1e4)
    hi = brentq(lambda m: survival(m, k_sol) - 0.5, 1, 1e4)
    check(f'(4) half survives at m_N = {lo:.0f} to {hi:.0f} GeV: v_R = {math.sqrt(lo * MSCALE):.1e} to {math.sqrt(hi * MSCALE):.1e} GeV',
          70 < lo < 90 and 140 < hi < 160)

    zb = 2 + 4 * k_atm ** 0.13 * math.exp(-2.5 / k_atm)
    kappa = 2 / (zb * k_atm) * (1 - math.exp(-zb * k_atm / 2))
    eps_needed = ETA_OBS / (0.96e-2 * kappa)
    m_min = eps_needed / (3 * M_ATM / (16 * math.pi * V ** 2))
    v_min = math.sqrt(m_min * MSCALE)
    check(f'(5) efficiency {kappa:.2e} at K = {k_atm:.0f}; eps > {eps_needed:.1e} needs m_N > {m_min:.1e} GeV, '
          f'v_R > {v_min:.1e} GeV, below the cap {CAP:.1e}', 1.0e11 < m_min < 1.5e11 and 1.1e13 < v_min < 1.4e13 < CAP)
    check('(6) Dirac: Delta N_eff floor 0.141 against 2.89 +- 0.11 is 2.7 sigma (Y11)',
          abs((3.044 + 3 * (10.75 / 106.75) ** (4 / 3) - 2.89) / 0.11 - 2.7) < 0.05)

    p16 = flat(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
    check('P16 carries the charge: "what carries $\\eta$ through that stretch is $B-L$"',
          'what carries $\\eta$ through that stretch is $B-L$' in p16)
    check('P16 carries the reading: "with Majorana masses $\\eta$ is not inherited but made on the expanding leg"',
          'with Majorana masses $\\eta$ is not inherited but made on the expanding leg' in p16)
    check('P16 carries where it is fixed: "fixed by neutrinoless double-beta decay"',
          'fixed by neutrinoless double-beta decay' in p16)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
