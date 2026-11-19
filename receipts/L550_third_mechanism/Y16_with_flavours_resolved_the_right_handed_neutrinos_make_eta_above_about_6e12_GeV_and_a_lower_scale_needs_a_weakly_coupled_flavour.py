"""Y16 -- with the lepton flavours resolved, the right-handed neutrinos make eta themselves above a
right-handed scale of about 6e12 GeV, and below it an asymmetry made by heavier states survives them
only through a weakly coupled flavour, which order-one coefficients give in a few per cent of cases.

Y15 (unflavoured): with Majorana masses an inherited asymmetry is erased on the hot leg and eta is made
on the expanding leg -- by the right-handed neutrinos themselves only above v_R ~ 1.2e13 GeV, and by
heavier states only if the right-handed neutrinos are lighter than ~100 GeV (v_R below ~3e8 GeV).  The
lead was whether flavour effects open the range between.  Below ~1e12 GeV the tau Yukawa, and below
~1e9 GeV the muon's, resolve the lepton flavours, and each flavour is washed out by its own strength
K_alpha = sum_i |m_D,alpha i|^2 / (m_N,i m_*).

Computed here:
  (1) the doublet realisation's three dimension-five operators with order-one complex Gaussian
      coefficient matrices (c_LL, c_RR symmetric; c_LR general), the right-handed masses by Takagi
      factorisation, the light mass matrix c_LL - c_LR c_RR^-1 c_LR^T normalised to m_3 = 0.05 eV, draws
      kept when the splitting ratio lies in 0.02-0.05 (measured 0.030), the charged-lepton basis a
      random unitary.  K_i alpha is then independent of v_R.  CONTROL: Takagi residual below 1e-12, and
      with c_LL = 0 (pure seesaw) the flavour-summed strength never below the light-mass sum over m_*.
  (2) made by the right-handed neutrinos with flavours resolved: eta = 0.96e-2 sum_alpha eps_alpha
      kappa(K_alpha), |eps_alpha| at most 3 m_N m_atm/(16 pi v^2); with two flavours at the median
      strengths the lightest needs m_N > 3e10 GeV, v_R > 6e12 GeV (unflavoured: 1.2e11 and 1.2e13).
  (3) made by heavier states (the singlets) without the operator washout of Y15 means at or below
      T_eq ~ 5e12 GeV, where the same bound and K = 47 give eta at most 2.5e-8; surviving the
      right-handed neutrinos' full washout exp(-3 pi K_alpha/8) then needs the least-washed flavour at
      K_alpha < 3.2.  Order-one draws give that in about 5% of cases with three flavours resolved
      (m_N below 1e9 GeV) and about 1.5% with two (1e9 to 1e12 GeV); unflavoured, never.

So with Majorana masses and order-one coefficients the right-handed scale sits at 3.5e7 to ~4e8 GeV or
~6e12 to 2.4e13 GeV, and between them only for a weakly coupled flavour, a few per cent of cases.

Bound: hierarchical right-handed masses (no resonance); the Buchmueller--Di Bari--Pluemacher efficiency
fit per flavour; the flavoured bound taken at its unflavoured size; the singlets' asymmetry carried into
B - L with an order-one factor taken as one; the anarchic measure is a convention for "order one".

COMPUTES: 40000 random coefficient sets, Takagi factorisation, closed-form efficiencies; P16 sentences
read live.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
RNG = np.random.default_rng(20261119)
MSTAR = 1.0702e-3          # eV (Y15)
M_ATM = 0.05               # eV
V = 174.10
MSCALE = 246.22 ** 2 / 0.05e-9
ETA = 6.1e-10
T_EQ = 5.2e12


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def cg(n, m):
    return (RNG.normal(size=(n, m)) + 1j * RNG.normal(size=(n, m))) / math.sqrt(2)


def takagi(a):
    u, s, _ = np.linalg.svd(a)
    w = u.conj().T @ a @ u.conj()
    up = u * np.exp(0.5j * np.angle(np.diag(w)))
    return s, up.conj()


def kappa(k):
    zb = 2 + 4 * k ** 0.13 * math.exp(-2.5 / k)
    return 2 / (zb * k) * (1 - math.exp(-zb * k / 2))


def eps_max(m):
    return 3 * m * M_ATM * 1e-9 / (16 * math.pi * V ** 2)


def main():
    print()
    print('  Y16 -- flavoured washout across the right-handed scale')
    print()
    res3, res2, sums, worst = [], [], [], 0.0
    for _ in range(40000):
        cll = cg(3, 3); cll = (cll + cll.T) / 2
        crr = cg(3, 3); crr = (crr + crr.T) / 2
        clr = cg(3, 3)
        mn, vv = takagi(crr)
        worst = max(worst, np.abs(vv.T @ crr @ vv - np.diag(mn)).max())
        d = clr @ vv
        light = cll - d @ np.diag(1 / mn) @ d.T
        ml = np.sort(np.linalg.svd(light, compute_uv=False))
        r = (ml[1] ** 2 - ml[0] ** 2) / (ml[2] ** 2 - ml[1] ** 2)
        if not 0.02 < r < 0.05:
            continue
        scale = M_ATM / ml[2]
        u, _, _ = np.linalg.svd(cg(3, 3))
        ka = (np.abs(u @ d) ** 2 / mn[None, :]).sum(axis=1) * scale / MSTAR
        res3.append(ka.min())
        res2.append(min(ka[2], ka[0] + ka[1]))
        sums.append((ka.sum(), ml.sum() * scale / MSTAR))
    res3, res2 = np.array(res3), np.array(res2)
    tot = np.array([s for s, _ in sums])
    ok = True
    for _ in range(2000):
        crr = cg(3, 3); crr = (crr + crr.T) / 2
        mn, vv = takagi(crr)
        d = cg(3, 3) @ vv
        light = -d @ np.diag(1 / mn) @ d.T
        ok &= bool((np.abs(d) ** 2 / mn[None, :]).sum() >= np.linalg.svd(light, compute_uv=False).sum() * (1 - 1e-9))
    check(f'CONTROL (1): {len(res3)} draws kept; Takagi residual {worst:.1e}; pure-seesaw sum rule holds on 2000 draws: {ok}; '
          f'flavour-summed strength median {np.median(tot):.0f}',
          worst < 1e-9 and ok and   # r7831 (69): the Takagi residual sits near 3e-13 and moves between builds; 1e-9 on O(1) entries keeps the control strict with headroom above 1e3
           50 < np.median(tot) < 70 and len(res3) > 5000)
    m3, m2 = np.median(res3), np.median(res2)
    print(f'      medians unrounded: {m3:.6f}, {m2:.6f}')
    check(f'(1) least-washed flavour strength, median: {m3:.1f} (three flavours), {m2:.1f} (two)', 8 < m3 < 12 and 14 < m2 < 21
          and round(m3, 1) == 9.6 and round(m2, 1) == 17.6)   # r7831 (69): the INDEX row prints 9.6 and 17.6

    k_other = np.median(tot) - m2
    ks = kappa(m2) + kappa(k_other)
    m_min = ETA / (0.96e-2 * eps_max(1.0) * ks)
    m_un = ETA / (0.96e-2 * eps_max(1.0) * kappa(47.0))
    check(f'(2) flavoured: m_N > {m_min:.1e} GeV, v_R > {math.sqrt(m_min * MSCALE):.1e} GeV; unflavoured {m_un:.1e}, {math.sqrt(m_un * MSCALE):.1e}',
          2e10 < m_min < 4e10 and 5e12 < math.sqrt(m_min * MSCALE) < 7e12 and 1.1e13 < math.sqrt(m_un * MSCALE) < 1.4e13)

    eta_max = 0.96e-2 * eps_max(T_EQ) * kappa(47.0)
    kstar = math.log(eta_max / ETA) / (3 * math.pi / 8)
    p3, p2 = np.mean(res3 < kstar), np.mean(res2 < kstar)
    check(f'(3) heavier states at T_eq make eta at most {eta_max:.1e}; survival needs K_alpha < {kstar:.2f}: '
          f'{100 * p3:.1f}% of draws (three flavours), {100 * p2:.1f}% (two)',
          2e-8 < eta_max < 3e-8 and 3.0 < kstar < 3.3 and 0.03 < p3 < 0.08 and 0.005 < p2 < 0.03)

    p16 = flat(os.path.join(ROOT, 'corpus', 'cosmogenesis_paper.tex'))
    check('P16 carries the flavoured edge: "a right-handed scale above about $6\\times10^{12}$~GeV"',
          'a right-handed scale above about $6\\times10^{12}$~GeV' in p16)
    check('P16 carries the weakly coupled flavour: "which order-one coefficients give in a few per cent of cases"',
          'which order-one coefficients give in a few per cent of cases' in p16)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
