"""Y12 -- the heavy right-handed neutrino must decay before nucleosynthesis, and that puts a floor on
the right-handed scale.

Y11: the joint microwave-and-abundance N_eff points away from a light right-handed neutrino and to
the heavy case, a mass above an MeV.  In the realisation the construction's breaking datum points to
(Higgs doublets, no triplet; Y6, Y8) the Majorana mass is dimension five, m_N = y v_R^2 / M_*.  The
state is thermalized at the peak in every case (Y9), so heavy it must decay before the plasma falls
to the last reheating temperature the abundances and the microwave background allow,
T_RH > 5.96 MeV (Barbieri et al. 2025, 95%).  This file finds the v_R at which it does.

Decay channels, Majorana (factor 2), y = 1, M_W(R) = g v_(L,R)/2 with g_R = g_L:
  * through the right-handed W: N -> e pi below 1 GeV (f_pi = 130.2 MeV), N -> e q q' above, the
    open quark doublets counted (u d; c s above 2 GeV; t b above 180 GeV); G_R = G_F (M_W/M_WR)^2.
  * through mixing with the left-handed neutrino, angle theta: the same pion mode, three-body W/Z
    modes below M_W (25 G_F^2 m^5 theta^2 / 192 pi^3), two-body W, Z, h modes above
    (g^2 theta^2 m^3 / 16 pi M_W^2), and nu e e / three-nu below the pion.
  Two mixings are carried: the dimension-five operators' own, theta = v_L/v_R; and the type-I
  seesaw relation for the measured scale, theta^2 = m_nu / m_N with m_nu = 0.05 eV.
The reheating temperature is T_RH = (Gamma M_Pl / 1.66 sqrt(10.75))^(1/2); the entropy release when
the state dominates is S = 1.83 g*^(1/4) m Y / (Gamma M_Pl)^(1/2) (Scherrer--Turner), with Y the
three states' relic n/s at their decoupling.

Computed here:
  (1) through the right-handed W alone the floor is v_R = 9.8e11 GeV (m_N = 3.9e5 GeV), where the
      state has dominated and releases S = 1.1e6.
  (2) with the dimension-five mixing the floor is v_R = 3.7e9 GeV (m_N = 5.8 GeV, S = 16), and the
      decay dilutes nothing (S < 1.1) above 1.4e10 GeV.
  (3) with the seesaw mixing the floor is v_R = 1.6e9 GeV (m_N = 1.0 GeV, S = 2.1), S < 1.1 above 2.1e9.
  (4) below the floor and above the light case (v_R from 4.9e7 GeV, Y11) the state is heavy and decays
      too late or not at all -- CONTROL: at v_R = 1e8 GeV the reheating temperature is below 0.1 MeV
      on every mixing, and with no mixing the state is stable below the pion threshold.
  (5) with the strong-CP bound on the doublet route, v_R < 2.4e13 GeV (Y6), the right-handed scale is
      confined to about 2e9 to 2.4e13 GeV with order-one couplings, a window that contains the
      1e10 +- 1 GeV of the minimal parity models (Hall--Harigaya).

Bound: y = 1 and order-one operator coefficients (the floors scale with them); free-quark rates above
1 GeV and the single pion mode below; instantaneous decay; the Scherrer--Turner dilution formula; the
mixing-mediated rates are the standard heavy-neutral-lepton forms to a factor of order one; the 0.05 eV
seesaw mass is the atmospheric scale.

COMPUTES: closed forms and a bisection in v_R; P15 and P16 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
GF, MW, G, MSTAR, FPI, MPL, Z3, VL = 1.1664e-5, 80.38, 0.65, 2.435e18, 0.1302, 1.221e19, 1.2020569, 246.22
MPI = 0.1396
T_RH_MIN = 5.96e-3


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def width(v, th2fn):
    m = v ** 2 / MSTAR
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
    lo, hi = 1e7, 1e15
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
SEE = lambda v, m: 0.05e-9 / m


def main():
    print()
    print('  Y12 -- the floor on the right-handed scale from the heavy state\'s decay')
    print()
    f1 = floor(WR)
    m1, _, s1 = state(f1, WR)
    check(f'(1) right-handed W alone: v_R > {f1:.2e} GeV (m_N {m1:.2e} GeV, S {s1:.2e})',
          abs(f1 - 9.8e11) / 9.8e11 < 0.01 and abs(m1 - 3.9e5) / 3.9e5 < 0.02 and abs(s1 - 1.1e6) / 1.1e6 < 0.05)
    f2 = floor(DIM5)
    m2, _, s2 = state(f2, DIM5)
    n2 = nodil(DIM5, f2)
    check(f'(2) dimension-five mixing: v_R > {f2:.2e} GeV (m_N {m2:.2f} GeV, S {s2:.1f}); S < 1.1 above {n2:.2e}',
          abs(f2 - 3.7e9) / 3.7e9 < 0.02 and abs(m2 - 5.8) < 0.05 and abs(s2 - 16) < 0.5 and abs(n2 - 1.4e10) / 1.4e10 < 0.02)
    f3 = floor(SEE)
    m3, _, s3 = state(f3, SEE)
    n3 = nodil(SEE, f3)
    check(f'(3) seesaw mixing: v_R > {f3:.2e} GeV (m_N {m3:.2f} GeV, S {s3:.1f}); S < 1.1 above {n3:.2e}',
          abs(f3 - 1.6e9) / 1.6e9 < 0.03 and abs(m3 - 1.0) < 0.05 and abs(s3 - 2.1) < 0.05 and abs(n3 - 2.1e9) / 2.1e9 < 0.03)
    t = [state(1e8, f)[1] for f in (WR, DIM5, SEE)]
    check(f'CONTROL (4): at v_R = 1e8 GeV, T_RH = {t[0]:.1e}, {t[1]:.1e}, {t[2]:.1e} GeV (W_R, dim-5, seesaw): all below 0.1 MeV',
          all(x < 1e-4 for x in t) and width(1e8, WR)[1] == 0.0)
    check(f'(5) window: {min(f2, f3):.1e} to 2.4e13 GeV contains 1e10 (and its 1e9 to 1e11 range in part)',
          min(f2, f3) < 1e10 < 2.4e13 and min(f2, f3) < 1e11)
    p15_txt = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    m_nu_ev = SEE(1.0, 1.0) * 1e9
    check(f'P15 prints the reheating bound this file uses, {T_RH_MIN * 1e3:.2f} MeV, read from the paper; '
          f'the seesaw mass this file assumes is {m_nu_ev:.2f} eV',
          '$5.96$~MeV' in p15_txt and abs(T_RH_MIN * 1e3 - 5.96) < 0.005 and abs(m_nu_ev - 0.05) < 0.005)
    r_lo, r_hi = VL / 2.4e13, VL / min(f2, f3)
    check(f'(5) the ratio of the vacuum values in that window: {r_lo:.1e} to {r_hi:.1e}, between about 1e-11 and 1e-7',
          abs(math.log10(r_lo) + 11) < 0.5 and abs(math.log10(r_hi) + 7) < 0.5)
    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('P14 carries the window: "The size is nonetheless bounded on both sides by what the construction carries"',
          'The size is nonetheless bounded on both sides by what the construction carries' in p14)
    p15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    p16 = flat(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
    check('P15 carries the floor: "Heavy, it must decay before nucleosynthesis"', 'Heavy, it must decay before nucleosynthesis' in p15)
    check('P16 carries the floor: "it must decay before nucleosynthesis"', 'it must decay before nucleosynthesis' in p16)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
