"""Y13 -- the lepton-number scale is completed most simply by gauge-singlet fermions, which carry no
colour; one per generation leaves the light neutrinos exactly massless, and the measured splittings
need at least five.

Y12: in the doublet realisation the three neutrino mass operators are dimension five with one scale M,
fixed by the measured masses at about 1.2e15 GeV.  The strong-CP cap on the right-handed scale (Y6)
bounds a COLOUR operator suppressed by the Planck mass; it moves to M only if the states at M carry
colour.  In the Pati--Salam reading (P14) lepton number is the fourth colour, so the question is whether
the states that complete the lepton-number operators sit in SU(4) multiplets that carry colour.

The operators are (F chi)^2 / M with F = (4,2,1) + (4bar,1,2) the fermion generation and chi the Higgs
doublets embedded as (4bar,2,1) + (4,1,2).  A tree-level completion exchanges a state in one of the
channels the product decomposes into.

Computed here:
  (1) the SU(4) channels, by the quadratic Casimir on explicit tensor-product representations:
      4 x 4bar = 1 + 15 (C2 = 0 and 4) -- the fermion-exchange channel F chi; 4 x 4 = 6 + 10
      (C2 = 5/2 and 9/2) -- the scalar-exchange channel F F.  So a fermion completion is either a total
      singlet or an SU(4) adjoint, which carries colour; a scalar completion is the (10,1,3)+(10,3,1),
      whose SU(2) triplet is the triplet the construction's breaking datum excludes (Y6, Y8).  CONTROL:
      the Casimirs of the fundamental and the adjoint are 15/8 and 4 in this normalisation.
  (2) with gauge-singlet fermions S (mass M_S) the full neutral mass matrix [[0, D], [D^T, M_S]], D the
      6 x n_S Yukawa-times-vev block, has exactly max(0, 6 - n_S) massless states: over random
      draws n_S = 3, 4, 5, 6 give 3, 2, 1, 0 exact zeros.  So one singlet per generation leaves all
      three light neutrinos massless to all orders at tree level, and the two measured splittings need
      n_S >= 5.  CONTROL: independent coefficients for the three operators give no zero.
  (3) the cap: the doublets' operator (|H_L|^2 - |H_R|^2) G Gtilde / Lambda^2 with Lambda the reduced
      Planck mass gives v_R < 2.4e13 GeV (Y6); with Lambda = M = 1.2e15 GeV it gives v_R < 1.2e10 GeV.
      So the window is 3.5e7 to 2.4e13 GeV with singlet completion, 3.5e7 to 1.2e10 GeV with an
      SU(4)-adjoint completion; the minimal parity models' 1e10 sits inside both.

So the Pati--Salam reading does not force the lepton-number scale to be a colour scale: the minimal
completion is colourless, and it is the singlets' number, not their charges, that the data constrain.

Bound: tree level; the adjoint completion's feed into G Gtilde is taken at its maximal, operator-level
size (c = 1); the singlets' masses are taken generic and of one order; v_L/v_R = 1e-2 in the rank draws
(the rank does not depend on it).

COMPUTES: explicit su(4) generators, tensor-product Casimir spectra, 400 random neutral mass matrices,
closed-form caps; P14 and P15 sentences read live.

Written by the chat seat.  Stated for reversal.
"""
import itertools
import math
import os
import re

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
FAILED = []
RNG = np.random.default_rng(20261118)
M_RED_PLANCK = 2.435e18
M_LEP = 246.22 ** 2 / 0.05e-9
THETA_BOUND = 1e-10
FLOOR = 3.5e7


def check(label, cond):
    print(f"    {'OK  ' if cond else 'FAIL'}  {label}")
    if not cond:
        FAILED.append(label)


def flat(path):
    return re.sub(r'\s+', ' ', open(path, encoding='utf-8', errors='replace').read())


def su4():
    gens = []
    for i, j in itertools.combinations(range(4), 2):
        a = np.zeros((4, 4), complex); a[i, j] = a[j, i] = 0.5; gens.append(a)
        b = np.zeros((4, 4), complex); b[i, j] = -0.5j; b[j, i] = 0.5j; gens.append(b)
    for k in range(1, 4):
        d = np.zeros((4, 4), complex)
        d[:k, :k] = np.eye(k); d[k, k] = -k
        gens.append(d / math.sqrt(2 * k * (k + 1)))
    return gens


def casimir_spectrum(rep_a, rep_b):
    n = rep_a[0].shape[0] * rep_b[0].shape[0]
    c2 = np.zeros((n, n), complex)
    for ta, tb in zip(rep_a, rep_b):
        t = np.kron(ta, np.eye(tb.shape[0])) + np.kron(np.eye(ta.shape[0]), tb)
        c2 += t @ t
    ev = np.round(np.linalg.eigvalsh(c2).real, 6)
    vals, counts = np.unique(ev, return_counts=True)
    return dict(zip(vals.tolist(), counts.tolist()))


def zeros(n_s, draws=100):
    out = set()
    for _ in range(draws):
        y = RNG.normal(size=(6, n_s)) + 1j * RNG.normal(size=(6, n_s))
        d = np.diag([1e-2] * 3 + [1.0] * 3) @ y
        ms = np.diag(RNG.uniform(50, 200, n_s)).astype(complex)
        full = np.block([[np.zeros((6, 6)), d], [d.T, ms]])
        sv = np.linalg.svd(full, compute_uv=False)
        out.add(int(np.sum(sv < 1e-12 * sv.max())))
    return out


def main():
    print()
    print('  Y13 -- what completes the lepton-number scale')
    print()
    f = su4()
    fbar = [-t.conj() for t in f]
    c_f = np.round(np.linalg.eigvalsh(sum(t @ t for t in f)).real, 6)
    adj = casimir_spectrum(f, fbar)
    sym = casimir_spectrum(f, f)
    check(f'CONTROL (1): C2(4) = {c_f[0]} (15/8)', np.allclose(c_f, 15 / 8))
    check(f'(1) 4 x 4bar: Casimir {{value: multiplicity}} = {adj} -> 1 + 15 (singlet or colour-carrying adjoint)',
          adj == {0.0: 1, 4.0: 15})
    check(f'(1) 4 x 4: Casimir {{value: multiplicity}} = {sym} -> 6 + 10 (the scalar channel; its SU(2) triplet is the excluded triplet)',
          sym == {2.5: 6, 4.5: 10})

    z = {n: zeros(n) for n in (3, 4, 5, 6)}
    check(f'(2) exact massless states with n_S singlets: ' + ', '.join(f'{n} -> {sorted(v)}' for n, v in z.items()),
          z == {3: {3}, 4: {2}, 5: {1}, 6: {0}})
    gen = []
    for _ in range(100):
        c = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
        cw, cd, cn = c @ c.T, RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3)), (lambda a: a @ a.T)(RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3)))
        m = np.block([[1e-6 * cw, 1e-3 * cd], [1e-3 * cd.T, cn]])
        sv = np.linalg.svd(m, compute_uv=False)
        gen.append(int(np.sum(sv < 1e-12 * sv.max())))
    check(f'CONTROL (2): independent operator coefficients leave {max(gen)} massless states', max(gen) == 0)

    cap_pl = math.sqrt(THETA_BOUND) * M_RED_PLANCK
    cap_m = math.sqrt(THETA_BOUND) * M_LEP
    check(f'(3) cap with Lambda = reduced Planck mass: v_R < {cap_pl:.2e} GeV; with Lambda = M = {M_LEP:.2e} GeV: v_R < {cap_m:.2e} GeV',
          abs(cap_pl - 2.4e13) / 2.4e13 < 0.02 and abs(cap_m - 1.2e10) / 1.2e10 < 0.02)
    check(f'(3) windows: {FLOOR:.1e} to {cap_pl:.1e} (singlets), {FLOOR:.1e} to {cap_m:.1e} (adjoint); 1e10 inside both',
          FLOOR < 1e10 < cap_m < cap_pl)

    p14 = flat(os.path.join(ROOT, 'corpus', 'matter_sector_paper.tex'))
    p15 = flat(os.path.join(ROOT, 'corpus', 'CR_cosmology.tex'))
    check('P15 carries the count: "one per generation leaves the light neutrinos exactly massless"',
          'one per generation leaves the light neutrinos exactly massless' in p15)
    check('P14 carries the reading: "the minimal completion of the lepton-number scale carries no colour"',
          'the minimal completion of the lepton-number scale carries no colour' in p14)
    print()
    if FAILED:
        print(f'  {len(FAILED)} FAILED')
        return 1
    print('  all checks pass')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
