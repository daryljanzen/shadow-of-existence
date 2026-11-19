"""Y12 -- the heavy right-handed neutrino must decay before nucleosynthesis, and that puts a floor on
the right-handed scale; the scale its mass is set at is the one the measured neutrino masses require.

Y11: the joint microwave-and-abundance N_eff points away from a light right-handed neutrino and to the
heavy case.  In the realisation the construction's breaking datum points to (Higgs doublets, no
bidoublet, no triplet; Y6, Y8) no neutrino mass is renormalisable.  The three lepton-number-violating
operators are all dimension five with one scale M:
    (L_L H_L)^2/M  ->  v_L^2/M,   (L_L H_L)(L_R H_R)/M  ->  m_D = v_L v_R/M,   (L_R H_R)^2/M  ->  m_N = v_R^2/M,
so with order-one coefficients the light mass is v_L^2/M (the seesaw term m_D^2/m_N is the same size)
and the mixing is theta = m_D/m_N = v_L/v_R, which is the seesaw relation theta^2 = m_nu/m_N exactly.

Computed here:
  (1) CONTROL: with M the reduced Planck mass the light mass is v_L^2/M = 2.5e-5 eV, two thousand times
      below the 0.05 eV the atmospheric splitting requires; so the measured masses fix M = v_L^2/m_nu
      = 1.2e15 GeV (at most, the heaviest light neutrino being at least that heavy).
  (2) the state is light at nucleosynthesis (m_N < 1 MeV) only for v_R < 1.1e6 GeV -- the case Y11
      finds disfavoured.
  (3) heavy, it is thermalized at the peak (Y9) and must reheat the plasma above 5.96 MeV (Barbieri et
      al. 2025, 95%).  Through its mixing it does so for v_R > 3.5e7 GeV (m_N = 1.0 GeV, entropy release
      S = 2.1), with no dilution above 4.8e7 GeV; through the right-handed W alone it would need
      v_R > 1.7e9 GeV and S = 6.9e3.
  (4) CONTROL: between the light case and the floor (v_R = 1e7 GeV) the reheating temperature is below
      0.1 MeV: heavy and long-lived, excluded.
  (5) with the doublets' strong-CP cap v_R < 2.4e13 GeV (Y6), the right-handed scale is confined to
      3.5e7 to 2.4e13 GeV with order-one coefficients, v_L/v_R between about 1e-11 and 1e-5, a window
      containing the minimal parity models' 1e10 +- 1 GeV (Hall--Harigaya).  The cap's operator is a
      colour operator; the neutrino scale is a lepton-number scale, which moves it only if the states
      at that scale carry colour.

Decay channels, Majorana (factor 2): through the right-handed W (G_R = G_F (M_W/M_WR)^2, g_R = g_L),
N -> e pi below 1 GeV (f_pi = 130.2 MeV) and N -> e q q' above with the open quark doublets counted;
through the mixing, the same pion mode, three-body W/Z modes below M_W (25 G_F^2 m^5 theta^2/192 pi^3),
two-body W, Z, h modes above (g^2 theta^2 m^3/16 pi M_W^2), and nu e e / three-nu below the pion.
T_RH = (Gamma M_Pl / 1.66 sqrt(10.75))^(1/2); S = 1.83 g*^(1/4) m Y/(Gamma M_Pl)^(1/2) (Scherrer--Turner).

Bound: order-one coefficients (the floor scales with them); m_nu = 0.05 eV; free-quark rates above 1 GeV
and one pion mode below; the heavy-neutral-lepton widths to a factor of order one; instantaneous decay.

So inside the window the state decays before nucleosynthesis, below it it is light or decays too late, and
P18 reads that as the sixteenth state not being the dark matter in the doublet realisation.

COMPUTES: closed forms and a bisection in v_R; P14, P15, P16 and P18 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
GF, MW, G, MSTAR, FPI, MPL, Z3, VL = 1.1664e-5, 80.38, 0.65, 2.435e18, 0.1302, 1.221e19, 1.2020569, 246.22
M_NU = 0.05e-9          # GeV, the atmospheric scale
MSCALE = VL ** 2 / M_NU  # the lepton-number scale the measured masses fix
MPI = 0.1396
T_RH_MIN = 5.96e-3


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def width(v, th2fn):
    m = v ** 2 / MSCALE
    gr = GF * (MW / (G * v / 2)) ** 2
    th2 = th2fn(v, m)
    w = 0.0
    if m > MPI:
        if m < 1.0:
            w = 2 * (gr ** 2 + th2 * GF ** 2) * FPI ** 2 * 0.974 ** 2 * m ** 3 / (16 * math.pi) * (1 - (MPI / m) ** 2) ** 2
        else:
            nch = 1 + (m > 2.0) + (m > 180.0)
            w = 2 * 3 * nch * gr ** 2 * m ** 5 / (192 * math.pi ** 3)
            w += th2 * 25 * GF ** 2 * m ** 5 / (192 * math.pi ** 3) if m < MW else th2 * G ** 2 * m ** 3 / (16 * math.pi * MW ** 2)
    elif m > 1.022e-3:
        w = th2 * 2 * GF ** 2 * m ** 5 / (192 * math.pi ** 3)
    return m, w


def relic(v):
    td = 1e-3 * (G * v / 2 / MW) ** (4 / 3)
    gd = 106.75 if td > 175 else 61.75 if td > 0.2 else 10.75
    return 3 * 0.75 * (Z3 / math.pi ** 2) * 2 / ((2 * math.pi ** 2 / 45) * gd)


def state(v, th2fn):
    m, w = width(v, th2fn)
    if w == 0:
        return m, 0.0, float('inf')
    trh = math.sqrt(w * MPL / 1.66 / math.sqrt(10.75))
    s = max(1.0, 1.83 * 10.75 ** 0.25 * m * relic(v) / math.sqrt(w * MPL))
    return m, trh, s


def floor(th2fn):
    lo, hi = 1e6, 1e15
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if state(mid, th2fn)[1] > T_RH_MIN:
            hi = mid
        else:
            lo = mid
    return hi


def nodil(th2fn, start):
    lo, hi = start, 1e15
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if state(mid, th2fn)[2] < 1.1:
            hi = mid
        else:
            lo = mid
    return hi


WR = lambda v, m: 0.0
DIM5 = lambda v, m: (VL / v) ** 2


def main():
    print()
    print('  Y12 -- the floor on the right-handed scale from the heavy state\'s decay')
    print()
    m_pl = VL ** 2 / MSTAR * 1e9
    check(f'CONTROL (1): at the reduced Planck mass the light mass is {m_pl:.1e} eV, {0.05 / m_pl:.0f} times short of 0.05 eV; '
          f'the measured masses fix the scale at {MSCALE:.2e} GeV',
          abs(m_pl - 2.5e-5) < 0.05e-5 and 1500 < 0.05 / m_pl < 2500 and abs(MSCALE - 1.2e15) / 1.2e15 < 0.02)
    check(f'(1) the mixing equals the seesaw relation: theta^2 m_N = {DIM5(1e9, 1e18 / MSCALE) * 1e18 / MSCALE * 1e9:.3f} eV',
          abs(DIM5(1e9, 1e18 / MSCALE) * 1e18 / MSCALE - M_NU) < 1e-15)
    v_light = math.sqrt(1e-3 * MSCALE)
    check(f'(2) light at nucleosynthesis only for v_R < {v_light:.2e} GeV', abs(v_light - 1.1e6) / 1.1e6 < 0.02)
    f2 = floor(DIM5)
    m2, _, s2 = state(f2, DIM5)
    n2 = nodil(DIM5, f2)
    check(f'(3) through the mixing: v_R > {f2:.2e} GeV (m_N {m2:.2f} GeV, S {s2:.1f}); S < 1.1 above {n2:.2e}',
          abs(f2 - 3.5e7) / 3.5e7 < 0.02 and abs(m2 - 1.0) < 0.05 and abs(s2 - 2.1) < 0.05 and abs(n2 - 4.8e7) / 4.8e7 < 0.02)
    f1 = floor(WR)
    m1, _, s1 = state(f1, WR)
    check(f'(3) through the right-handed W alone: v_R > {f1:.2e} GeV (m_N {m1:.2e} GeV, S {s1:.2e})',
          abs(f1 - 1.7e9) / 1.7e9 < 0.02 and abs(s1 - 6.9e3) / 6.9e3 < 0.03)
    t = [state(1e7, f)[1] for f in (WR, DIM5)]
    check(f'CONTROL (4): at v_R = 1e7 GeV, T_RH = {t[0]:.1e} and {t[1]:.1e} GeV: below 0.1 MeV',
          all(x < 1e-4 for x in t))
    check(f'(5) window: {f2:.1e} to 2.4e13 GeV contains 1e9 to 1e11', f2 < 1e9 and 1e11 < 2.4e13)
    p15_txt = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    check(f'P15 prints the reheating bound this file uses, {T_RH_MIN * 1e3:.2f} MeV, read from the paper; '
          f'the light mass this file takes is {M_NU * 1e9:.2f} eV',
          '$5.96$~MeV' in p15_txt and abs(T_RH_MIN * 1e3 - 5.96) < 0.005 and abs(M_NU * 1e9 - 0.05) < 0.005)
    r_lo, r_hi = VL / 2.4e13, VL / f2
    check(f'(5) the ratio of the vacuum values in that window: {r_lo:.1e} to {r_hi:.1e}, between about 1e-11 and 1e-5',
          abs(math.log10(r_lo) + 11) < 0.5 and abs(math.log10(r_hi) + 5) < 0.5)
    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('P14 carries the window: "The size is nonetheless bounded on both sides by what the construction carries"',
          'The size is nonetheless bounded on both sides by what the construction carries' in p14)
    p15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    p16 = flat(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
    check('P15 carries the floor: "Heavy, it must decay before nucleosynthesis"', 'Heavy, it must decay before nucleosynthesis' in p15)
    check('P16 carries the floor: "it must decay before nucleosynthesis"', 'it must decay before nucleosynthesis' in p16)
    p18 = flat(os.path.join(ROOT, 'corpus', 'CR_synthesis.tex'))
    check('P18 carries the window: "by the parity\'s own right-handed neutrino having to decay before nucleosynthesis"',
          "by the parity's own right-handed neutrino having to decay before nucleosynthesis" in p18)
    check('P18 carries the reading: "the sixteenth state is not the dark matter"', 'the sixteenth state is not the dark matter' in p18)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
