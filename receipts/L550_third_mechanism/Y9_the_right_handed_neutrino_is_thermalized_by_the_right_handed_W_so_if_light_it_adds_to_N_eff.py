"""Y9 -- the right-handed neutrino is thermalized by the right-handed W, so if it is light at
nucleosynthesis it adds to N_eff.

Y8: the sixteenth state an exact parity requires is a Standard-Model singlet with I3R = 1/2 and B-L = -1,
so it couples to W_R.  P15 had read it as never thermalized, contributing nothing to N_eff.  This file
computes what the W_R coupling does to that.

Computed here:
  (1) thermalization: the plasma reaches rho_Planck/6pi on the way to the branch point (P16's regulated
      peak); read as radiation at g* = 106.75 that is T ~ 2e18 GeV, far above every decoupling
      temperature below, so the state starts in equilibrium.
  (2) decoupling: W_R exchange is the Fermi rate scaled by (M_W/M_WR)^4, so T_dec = T_nuL (M_WR/M_W)^(4/3)
      with T_nuL = 1 MeV: 343 MeV at the ATLAS bound M_WR = 6.4 TeV (514 MeV at T_nuL = 1.5 MeV, the same
      g*s); and 1.4e7 GeV at v_R = 1e10 GeV (M_WR = g v_R/2).
  (3) Delta N_eff = 3 (10.75/g*s(T_dec))^(4/3) for three light states: g*s = 61.75 (u,d,s quarks and gluons
      free above the QCD crossover, with photons, e, mu, three nu_L) gives 0.29; g*s = 106.75 above the
      electroweak scale gives 0.14.  CONTROL: a state decoupling with the left-handed neutrinos
      (g*s = 10.75) gives exactly 1 per species.
  (4) against Planck's 2.99 +- 0.17 (P15, sec:coherence), N_eff = 3.044 + Delta = 3.18 to 3.34, i.e.
      1.1 to 2.0 sigma high; helium-4 moves by 0.013 Delta N_eff = 0.002 to 0.004 (P16's network, Y10).
  (5) 'light at nucleosynthesis' for the dimension-five Majorana mass v_R^2/M, with M = v_L^2/m_nu = 1.2e15 GeV the
      scale the measured neutrino masses fix (Y12) means
      m_N < 1 MeV, i.e. v_R < 1.1e6 GeV.  CONTROL: at the collider bound v_R = 19.7 TeV, m_N = 320 eV.

Bound: ideal-gas g*s with step thresholds (lattice corrections near the QCD crossover lower g*s by
about a tenth there and raise 0.29 accordingly, which is not carried); T_nuL = 1 MeV; W_R exchange only
(Z' exchange adds rate and lowers T_dec slightly); dY_p/dN_eff = 0.013 is P16's network's lever (Y10),
not a network run; y = 1; the peak is read as thermal radiation.

COMPUTES: closed-form numbers; the g*s step function; two P15 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
M_W = 80.38          # GeV
M_WR = 6400.0        # GeV, ATLAS 2023
G = 0.65
M_STAR = 246.22 ** 2 / 0.05e-9    # GeV, the lepton-number scale the measured neutrino masses fix (Y12)
M_PL = 1.221e19      # GeV
NEFF_SM = 3.044
NEFF_OBS, NEFF_SIG = 2.99, 0.17
DYP = 0.013   # P16's network returns 0.0131 per unit (L550 Y10)


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


# (mass GeV, entropy dof weight) -- fermions carry 7/8; QCD partons only above the crossover
SPECIES = [
    (0.0, 2.0),                 # photon
    (0.0, 3 * 2 * 7 / 8),       # three nu_L
    (0.000511, 4 * 7 / 8),      # e
    (0.1057, 4 * 7 / 8),        # mu
    (1.777, 4 * 7 / 8),         # tau
    (80.38, 6.0), (91.19, 3.0), (125.1, 1.0),   # W, Z, H
]
QUARKS = [(0.0022, 12 * 7 / 8), (0.0047, 12 * 7 / 8), (0.095, 12 * 7 / 8),
          (1.27, 12 * 7 / 8), (4.18, 12 * 7 / 8), (172.7, 12 * 7 / 8)]
T_QCD = 0.155


def gstar_s(T):
    g = sum(w for m, w in SPECIES if m < T)
    if T > T_QCD:
        g += 16.0 + sum(w for m, w in QUARKS if m < T)
    elif T > 0.14:
        g += 3.0
    return g


def t_dec(mwr, tnu=1e-3):
    return tnu * (mwr / M_W) ** (4 / 3)


def dneff(T):
    return 3 * (10.75 / gstar_s(T)) ** (4 / 3)


def main():
    print()
    print('  Y9 -- the sixteenth state and N_eff')
    print()
    rho = M_PL ** 4 / (6 * math.pi)
    t_peak = (30 * rho / (math.pi ** 2 * 106.75)) ** 0.25
    hh = t_dec(G * 1e10 / 2)
    check(f'(1) the peak rho_Pl/6pi read as radiation: T = {t_peak:.1e} GeV, above T_dec at v_R = 1e10 GeV ({hh:.1e} GeV)',
          t_peak > 1e18 and hh < t_peak and abs(hh - 1.4e7) / 1.4e7 < 0.05)

    td = t_dec(M_WR)
    td15 = t_dec(M_WR, 1.5e-3)
    check(f'(2) T_dec at M_WR = 6.4 TeV: {td * 1e3:.0f} MeV ({td15 * 1e3:.0f} MeV at T_nuL = 1.5 MeV), g*s = {gstar_s(td)} at both',
          round(td * 1e3) == 343 and gstar_s(td) == gstar_s(td15) == 61.75)

    lo, hi = dneff(300.0), dneff(td)
    check(f'(3) Delta N_eff = {hi:.3f} at the bound, {lo:.3f} with decoupling above the electroweak scale (g*s = {gstar_s(300.0)})',
          round(hi, 2) == 0.29 and round(lo, 2) == 0.14 and gstar_s(300.0) == 106.75)
    check(f'CONTROL (3): decoupling with nu_L, g*s(2 MeV) = {gstar_s(2e-3)}, gives {dneff(2e-3) / 3:.3f} per species',
          gstar_s(2e-3) == 10.75 and abs(dneff(2e-3) - 3) < 1e-12)
    mwr_ew = M_W * (172.7 / 1e-3) ** 0.75
    check(f'(3) decoupling passes the top mass for M_WR above {mwr_ew / 1e3:.0f} TeV', 500 < mwr_ew / 1e3 < 1000)

    n_lo, n_hi = NEFF_SM + lo, NEFF_SM + hi
    s_lo, s_hi = (n_lo - NEFF_OBS) / NEFF_SIG, (n_hi - NEFF_OBS) / NEFF_SIG
    y_lo, y_hi = DYP * lo, DYP * hi
    check(f'(4) N_eff = {n_lo:.2f} to {n_hi:.2f}, {s_lo:.1f} to {s_hi:.1f} sigma above 2.99 +- 0.17; Delta Y_p = {y_lo:.4f} to {y_hi:.4f}',
          f'{n_lo:.2f}' == '3.18' and f'{n_hi:.2f}' == '3.34' and f'{s_lo:.1f}' == '1.1' and f'{s_hi:.1f}' == '2.0'
          and round(y_lo, 3) == 0.002 and round(y_hi, 3) == 0.004 and abs(DYP - 0.013) < 0.0005)
    check(f'(4) pinned: Planck N_eff = {NEFF_OBS} +- {NEFF_SIG}; N_eff = {n_lo:.4f} and {n_hi:.4f}',
          abs(NEFF_OBS - 2.99) < 0.005 and abs(NEFF_SIG - 0.17) < 0.005
          and abs(n_lo - 3.18) < 0.005 and abs(n_hi - 3.34) < 0.005)

    v_mev = math.sqrt(1e-3 * M_STAR)
    v_bound = 2 * M_WR / G
    m_bound = v_bound ** 2 / M_STAR
    check(f'(5) m_N = v_R^2/M < 1 MeV for v_R < {v_mev:.1e} GeV (M = {M_STAR:.2e} GeV)', abs(v_mev - 1.1e6) / 1.1e6 < 0.02)
    check(f'CONTROL (5): at v_R = {v_bound:.3g} GeV, m_N = {m_bound * 1e9:.0f} eV', abs(m_bound * 1e9 - 320) < 5)

    p15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    check('P15 carries the reading: "turns on the state\'s mass, which the construction does not fix"',
          "turns on the state's mass, which the construction does not fix" in p15)
    check('P15 carries the numbers: "$0.29$ at the bound, falling to $0.14$"',
          '$0.29$ at the bound, falling to $0.14$' in p15)
    check('P15 no longer carries "a species that is never thermalized contributes nothing"',
          'a species that is never thermalized contributes nothing' not in p15)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
