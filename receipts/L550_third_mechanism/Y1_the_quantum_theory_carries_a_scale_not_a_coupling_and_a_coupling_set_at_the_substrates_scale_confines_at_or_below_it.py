"""Y1 -- the quantum Yang--Mills theory carries a SCALE and no free coupling, and a coupling set at
the substrate's own scale confines at or below it.

P14's dimensional sentence was classical: the action int F^2/g^2 carries a dimensionless g, which a
single length cannot build.  Quantised, the coupling runs and pure Yang--Mills trades it for one
scale (dimensional transmutation, witnessed by a non-zero trace of the stress tensor).  That theory
is now constructed -- a Wightman QFT as a scaling limit of 4D Wilson lattice gauge theory for any
simple compact group, the bare coupling fixed by the lattice spacing at slope 11 C_g / 24 pi^2, the
running g^2(r) log(1/r) -> 1/(2 b0), a non-zero trace; no uniqueness of the infinite-volume limit
and no mass gap (Yang--Mills group assessment, 10 Nov 2026, github.com/yang-mills-group/YM at
b379615f5596, Theorems 4.1, 7.1, 7.2).

So the question the substrate faces is where the one scale sits.

  (1) The construction's slope is twice b0: 11 C_g/24 pi^2 = 2 * 11 C_g/48 pi^2, so its two
      theorems are one running law.
  (2) At one loop Lambda = mu exp(-1/(2 b0 g^2(mu))) < mu for EVERY g^2 > 0: a coupling set at mu,
      of any strength, confines at or below mu.
  (3) On the corpus's alpha the observed scales stand 41.29 (pure-gauge Lambda_MSbar) and 42.15
      (lightest glueball) decades above hbar c / alpha, stable across the observed range of Lambda.
  (4) The descent: a 5D coupling of length alpha over a reduction length of order alpha gives a 4D
      coupling of order one at hbar c / alpha, which by (2) confines at or below hbar c / alpha.

CONTROL -- the instrument can say yes: the same one-loop relation with the coupling set far on the
ultraviolet side (mu = hbar c / l_P, 1/g^2 = 6.32) returns a confinement scale ABOVE hbar c/alpha,
at the observed value it was solved from; so (2)'s verdict is a property of where the coupling is
set and not of the formula.

P14 pins: the rewritten dimensional sentence and the quantum paragraph are read live.

Bound: not that no mechanism can set the coupling in the ultraviolet -- it says where one must;
not a derivation of Lambda_YM; one-loop running only (two-loop moves the exponent by a logarithm,
not the sign of Lambda - mu); the glueball and Lambda_MSbar values are standard lattice inputs
quoted, not computed here; the large-number coincidence between 10^41 and (alpha/l_P)^(2/3) is not
used and not claimed.

Written by the chat seat.  Stated for reversal.
"""
import math
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []

HBAR_C_GEV_M = 1.9732698e-16   # GeV m
L_P = 1.616255e-35             # m
R0 = 0.5e-15                   # m, Sommer scale
R0_LAMBDA = 0.602              # r0 * Lambda_MSbar, pure SU(3) (quenched lattice)
GLUEBALL = 1.73                # GeV, lightest 0++ glueball, pure SU(3) lattice


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    s = open(path, encoding='utf-8', errors='replace').read()
    return re.sub(r'\s+', ' ', s)


def lam_over_mu(g2, b0):
    return math.exp(-1.0 / (2.0 * b0 * g2))


def main():
    print()
    print('  Y1 -- the quantum theory carries a scale, not a coupling')
    print()
    C = 3.0                                   # SU(3)
    b0 = 11 * C / (48 * math.pi ** 2)
    slope = 11 * C / (24 * math.pi ** 2)
    check(f'(1) the construction\'s bare-coupling slope 11C/24pi^2 = {slope:.6f} is 2 b0 = {2*b0:.6f}: '
          'Theorem 4.1 and Theorem 7.2 are one running law', abs(slope - 2 * b0) < 1e-15)

    gs = [10 ** (k / 10) for k in range(-30, 31)]
    ratios = [lam_over_mu(g, b0) for g in gs]
    check(f'(2) Lambda/mu < 1 for all {len(gs)} couplings g^2 in [1e-3, 1e3]: max {max(ratios):.4f}',
          all(r < 1 for r in ratios))

    Lam_qcd = R0_LAMBDA * HBAR_C_GEV_M / R0
    for Lam in (1.0e-52, 1.1056e-52, 1.2e-52):
        al = math.sqrt(3 / Lam)
        E_al = HBAR_C_GEV_M / al
        d1 = math.log10(Lam_qcd / E_al)
        d2 = math.log10(GLUEBALL / E_al)
        check(f'(3) Lambda = {Lam:.4g} m^-2: Lambda_MSbar = {Lam_qcd*1e3:.0f} MeV at {d1:.2f} decades and the '
              f'glueball at {d2:.2f} above hbar c/alpha', 41.0 < d1 < 41.6 and 41.9 < d2 < 42.4)

    Lam = 1.1056e-52
    al = math.sqrt(3 / Lam)
    for L_red, name in ((al, 'alpha'), (2 * math.pi * al, '2 pi alpha'), (al / (2 * math.pi), 'alpha/2pi')):
        g4 = al / L_red
        r = lam_over_mu(g4, b0)
        check(f'(4) descent over {name}: g4^2 = {g4:.3f} at hbar c/alpha, Lambda/mu = {r:.3e} <= 1',
              r < 1)

    E_P = HBAR_C_GEV_M / L_P
    inv_g2 = 2 * b0 * math.log(E_P / Lam_qcd)
    back = E_P * lam_over_mu(1 / inv_g2, b0)
    E_al = HBAR_C_GEV_M / al
    check(f'CONTROL: coupling set at hbar c/l_P with 1/g^2 = {inv_g2:.2f} returns Lambda = {back*1e3:.0f} MeV, '
          f'{math.log10(back/E_al):.2f} decades ABOVE hbar c/alpha -- the instrument can say yes',
          abs(back / Lam_qcd - 1) < 1e-9 and back > E_al)

    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    check('P14 carries the rewritten dimensional sentence: "what a single length cannot build for a '
          'Yang--Mills term in four dimensions is its scale"',
          'what a single length cannot build for a Yang--Mills term in four dimensions is its scale' in p14)
    check('P14 carries the quantum reason: "It is the scale and not a coupling, because the quantum '
          'theory has no free coupling to supply"',
          'It is the scale and not a coupling, because the quantum theory has no free coupling to supply' in p14)
    check('P14 carries the bound: "puts the confinement scale at or below $\\hbar c/\\alpha$"',
          'puts the confinement scale at or below $\\hbar c/\\alpha$' in p14)
    # the printed figure is computed at the corpus's own alpha (P7: alpha/sqrt3 = 3009.892488 Mpc)
    al0 = 3009.892488 * math.sqrt(3) * 3.085677581e22
    E0 = HBAR_C_GEV_M / al0
    f1 = f'{math.log10(Lam_qcd / E0):.1f}'
    g = math.log10(GLUEBALL / E0) - math.log10(Lam_qcd / E0)
    check(f'P14 prints the figure this file computes at the corpus alpha: $10^{{{f1}}}$ for Lambda_MSbar, and the '
          f'glueball {g:.2f} decades higher ("nearly a decade higher still")',
          abs(math.log10(Lam_qcd / E0) - 41.3) < 0.05 and 'stands $10^{41.3}$ above it' in p14 and 0.8 < g < 1.0
          and 'nearly a decade higher still' in p14)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
