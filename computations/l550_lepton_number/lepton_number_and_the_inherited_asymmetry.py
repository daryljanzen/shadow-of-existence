"""What the lepton-number violation the measured neutrino masses require does to an inherited B-L,
and whether the singlets that complete the operators leave any other trace.

Working computation (L550 thread, after Y13/Y14); to be promoted to a receipt with the corpus edits.

(1) the singlets: a singlet S of mass M_S coupled to a lepton doublet with Yukawa y gives the light
    neutrinos m = y^2 v^2 / M_S; its decay parameter K = Gamma/H(T = M_S) = m / m_*, with
    m_* = 16 pi^(5/2) sqrt(g*) v^2 / (3 sqrt5 M_Pl) -- independent of M_S and y (the seesaw's scale
    freedom).  At the atmospheric mass K ~ 47: the singlets decay as fast as they are made, at
    T ~ M_S, leaving no relic and no entropy release.  CONTROL: int_0^inf z^3 K1(z)/4 dz = 3 pi/8.
(2) the dimension-five lepton-number violation is in equilibrium above
    T_eq = 1.66 sqrt(g*) pi^3 v^4 / (3 mbar^2 M_Pl), mbar^2 = sum of the light masses squared:
    about 5e12 GeV (hep-ph/9503335's coefficient gives 1.7e13).  Sphalerons are in equilibrium
    below about 7e11 GeV down to 131.7 GeV.
(3) a plasma that passes above T_eq in equilibrium -- on the infall to the regulated peak and again
    on the expanding leg -- has its lepton number driven to zero; with Pati-Salam unbroken there
    (v_PS = v_R, inside the window) B and L are not separate charges and B-L goes with it.
    The washout exponent integral_T_eq^T_max (Gamma/H) dT/T = T_max/T_eq - 1.
(4) below v_R, the right-handed neutrinos' inverse decays (K = m_nu/m_* at each mass) wash out B-L
    while the sphalerons run: survival exp(-K int_0^{m_N/131.7} z^3 K1(z)/4 dz).  Half survives at
    m_N ~ 80-150 GeV (K = 47 .. 8), a thousandth at 190-570 GeV: v_R ~ 3-4e8 GeV and 5-8e8 GeV at
    M = 1.2e15 GeV.
(5) Dirac masses (lepton number exact) avoid (3) and (4) but make the right-handed neutrinos light:
    Delta N_eff >= 0.141 (Y11), 2.7 sigma above the joint ACT value.
"""
import math

from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import k1

MPL, V, GS = 1.221e19, 174.10, 106.75
M_ATM, M_SOL = 0.0500e-9, 0.0086e-9
MSCALE = 246.22 ** 2 / M_ATM
T_SPH_OFF = 131.7
FAILED = []


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def hub(t):
    return 1.66 * math.sqrt(GS) * t ** 2 / MPL


def w(z):
    return z ** 3 * k1(z) / 4


def survival(m_n, k):
    return math.exp(-k * quad(w, 0, m_n / T_SPH_OFF, limit=200)[0])


def main():
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
          f'the washout exponent from there is {t_gauge / t_eq - 1:.0f}', t_gauge / t_eq > 50)

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
    print()
    print('  all checks pass' if not FAILED else f'  {len(FAILED)} FAILED')
    return 1 if FAILED else 0


if __name__ == '__main__':
    raise SystemExit(main())
