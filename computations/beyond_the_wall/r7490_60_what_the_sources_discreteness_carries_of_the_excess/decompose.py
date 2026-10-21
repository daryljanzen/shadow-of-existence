#!/usr/bin/env python3
"""
r7490 — WHAT PART OF THE 0.045 EXCESS THE SOURCE'S DISCRETENESS CARRIES, amplitude and phase
read apart.  Order r7489 (1).

THE RULING THIS RESTS ON, and it is 69's: the closed S^3 source spectrum is discrete by
degree, one mode per L at k_L = sqrt(L(L+2))/r_0, and P15's own transfer is the L>=2-floored
sum over that ladder, which reaches k_max D_M ~ 4000 at one mode per degree.  So THE LADDER IS
THAT SPECTRUM and the continuum is the check -- which makes r7480's two component moves the
measured effect of the source's DISCRETENESS on the contrast, not a numerical artefact.

⌗ THE STATISTIC IS IMPORTED from r7093's contrast_two_models.py by ast, as r7474, r7476 and
  r7480 imported it.  One copy of the predicate in the tree (r7445's rule, promoted r7447).

Run:  python3 decompose.py
"""

import ast
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
_SRC = os.path.join(BW, 'r7093_70_configuration_census', 'contrast_two_models.py')
_R7476 = os.path.join(BW, 'r7476_60_the_projected_continuum_at_the_excesss_own_configuration')
_R7480 = os.path.join(BW, 'r7480_60_is_the_contrasts_amplitude_half_converged_in_the_wavenumber_sampling')
for _p in (_SRC, _R7476, _R7480):
    if not os.path.exists(_p):
        sys.exit(f'FATAL: {_p} is not where this file expects it.')


def _names(t):
    if isinstance(t, ast.Name):
        return [t.id]
    if isinstance(t, (ast.Tuple, ast.List)):
        return [x for e in t.elts for x in _names(e)]
    return []


def _load(path):
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)
    want = ('LO', 'HI', 'NG', 'HERE', 'BW')
    keep = []
    for n in tree.body:
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            keep.append(n)
        elif isinstance(n, ast.Assign):
            nm = [x for t in n.targets for x in _names(t)]
            if nm and all(x in want for x in nm):
                keep.append(n)
    ns = {'__file__': path, '__name__': 'r7093_contrast'}
    exec(compile(ast.Module(body=keep, type_ignores=[]), path, 'exec'), ns)   # noqa: S102
    return ns


_NS = _load(_SRC)
osc = _NS['osc']
LO, HI = _NS['LO'], _NS['HI']

LADDER = 'spectra/cc66_r185_verify_cr.npz'
CONTROL = 'spectra/cc66_r185_verify_lcdm.npz'
CONT4 = os.path.relpath(os.path.join(_R7476, 'verify_cr_kcont.npz'), BW)
CONT8 = os.path.relpath(os.path.join(_R7480, 'verify_cr_kcont_nk2.npz'), BW)
EXCESS = 0.045
PRINTED = {LADDER: (1.04520, 1.04552, 0.99969), CONT4: (1.04516, 1.04986, 0.99552)}


def three(arm, ctl):
    """proj, rms, cos from the imported oscillation, plus the raw sums."""
    A, lA, _rs = osc(arm)
    B, _lb, _rs2 = osc(ctl)
    sAB, sAA, sBB = float(np.sum(A * B)), float(np.sum(A * A)), float(np.sum(B * B))
    return (sAB / sBB, np.sqrt(sAA / sBB), sAB / np.sqrt(sAA * sBB)), (A, B), lA


def main():
    print('=' * 104)
    print('  Ⓥ① THE IMPORTED STATISTIC, AND ITS SOURCE\'S OWN FOUR PRINTED ROWS FIRST')
    print('=' * 104)
    rows = [('A  c54.178', 'spectra/c54.178_cr.npz', 'spectra/c54.178_lcdm.npz', -0.3766),
            ('A  c54.186 L3000', 'spectra/c54.186_cr_L3000.npz',
             'spectra/c54.186_lcdm_L3000.npz', -0.4108),
            ('B  refit grid base', 'refit_grid185/cr_base.npz',
             'refit_grid185/lcdm_base.npz', 1.0563),
            ('B  refit minimum', LADDER, CONTROL, 1.0452)]
    worst = 0.0
    for lab, a, b, printed in rows:
        (p, _r, _c), _ab, _l = three(a, b)
        worst = max(worst, abs(p - printed))
        print(f'      {lab:22s} {p:+9.4f}  printed {printed:+9.4f}  diff {abs(p - printed):.2e}')
    ok1 = worst < 5e-5
    print(f'  ⇒ worst {worst:.2e}  {"PASS" if ok1 else "FIRED"}   '
          f'⌗ window q in [{LO}, {HI}], the statistic\'s own')

    print()
    print('=' * 104)
    print('  Ⓐ THE IDENTITY THE DECOMPOSITION RESTS ON:  proj  ==  rms × cos')
    print('=' * 104)
    print('      It is the algebra of the three sums and nothing else:')
    print('        proj = S_AB/S_BB,   rms = sqrt(S_AA/S_BB),   cos = S_AB/sqrt(S_AA·S_BB)')
    print('        rms × cos = sqrt(S_AA/S_BB) · S_AB/sqrt(S_AA·S_BB) = S_AB/S_BB = proj')
    print('      ⇒ so it must hold to machine precision, and that is what is checked -- NOT the')
    print('        five printed decimals, which could agree by rounding.')
    print()
    print(f'      {"spectrum":26s} {"proj":>11s} {"rms × cos":>12s} {"|difference|":>14s}')
    keep, okA = {}, True
    for lab, rel in (('LADDER   (the arm)', LADDER), ('CONTINUUM 4.0 pts', CONT4),
                     ('CONTINUUM 8.0 pts', CONT8), ('CONTROL vs itself', CONTROL)):
        (p, r, cs), (A, B), lA = three(rel, CONTROL)
        keep[lab] = (p, r, cs, A, B, lA)
        d = abs(p - r * cs)
        okA &= d < 1e-12
        print(f'      {lab:26s} {p:+11.6f} {r * cs:+12.6f} {d:14.3e}')
    print(f'  ⇒ {"PASS — the identity is exact" if okA else "FIRED: no product decomposition"}')

    print()
    print('=' * 104)
    print('  Ⓑ/Ⓒ THE EXCESS DECOMPOSED — what the amplitude carries and what the phase carries')
    print('=' * 104)
    print('      proj − 1 = (rms − 1) + rms·(cos − 1)    exactly, by the identity above')
    print()
    print(f'      {"spectrum":26s} {"excess":>10s} {"amplitude":>12s} {"phase":>12s}'
          f' {"phase share":>12s}')
    parts = {}
    for lab in ('LADDER   (the arm)', 'CONTINUUM 4.0 pts', 'CONTINUUM 8.0 pts'):
        p, r, cs, _A, _B, _l = keep[lab]
        amp, pha = r - 1.0, r * (cs - 1.0)
        parts[lab] = (p - 1.0, amp, pha)
        assert abs((p - 1.0) - (amp + pha)) < 1e-12
        print(f'      {lab:26s} {p - 1:+10.5f} {amp:+12.5f} {pha:+12.5f}'
              f' {abs(pha) / abs(p - 1) * 100:11.2f}%')
    print()
    exL, aL, pL = parts['LADDER   (the arm)']
    exC, aC, pC = parts['CONTINUUM 4.0 pts']
    print(f'  ⇒ ON THE LADDER — the arm\'s own spectrum by the ruling — THE EXCESS IS ALMOST ALL')
    print(f'    AMPLITUDE: {aL:+.5f} of amplitude against {pL:+.5f} of phase, the phase carrying')
    print(f'    {abs(pL) / abs(exL) * 100:.2f} per cent of it.  On the continuum the phase part is')
    print(f'    {abs(pC / pL):.1f} times larger ({pC:+.5f}) while the amplitude part grows by only')
    print(f'    {abs(aC - aL) / abs(aL) * 100:.1f} per cent of itself.')

    print()
    print('=' * 104)
    print('  Ⓔ/Ⓕ WHAT THE DISCRETENESS CARRIES — the two moves, and the metric NAMED')
    print('=' * 104)
    d_amp = aC - aL                      # the amplitude part's move, ladder -> continuum
    d_pha = pC - pL                      # the phase part's move, in the SAME additive terms
    d_proj = exC - exL
    print(f'      the amplitude part moves  {d_amp:+.5f}   = {abs(d_amp) / EXCESS * 100:5.2f}'
          f' per cent of the {EXCESS} excess')
    print(f'      the phase part moves      {d_pha:+.5f}   = {abs(d_pha) / EXCESS * 100:5.2f}'
          f' per cent')
    print(f'      their SUM, the projected  {d_proj:+.5f}   = {abs(d_proj) / EXCESS * 100:5.2f}'
          f' per cent   ⌗ they cancel')
    print(f'      and they are opposite in sign, their magnitudes within '
          f'{abs(abs(d_amp) / abs(d_pha) - 1) * 100:.1f} per cent of each other')
    quad = float(np.hypot(d_amp, d_pha))
    absum = abs(d_amp) + abs(d_pha)
    print()
    print(f'  ⌈ Ⓥ③ THE METRIC, NAMED, AND ITS ARBITRARINESS STATED')
    print(f'      This seat has NO DATA COVARIANCE.  What is used is the metric the statistic')
    print(f'      itself induces -- the two additive parts taken as components of one residual')
    print(f'      over the same q window -- so the discreteness\'s size is their QUADRATURE sum.')
    print(f'      The L1 sum is printed beside it as the other obvious choice.')
    print(f'      ⛔ A REAL LIKELIHOOD WEIGHTS PER-l RESIDUALS BY A COVARIANCE THIS DOES NOT')
    print(f'        HAVE, AND WOULD GIVE A DIFFERENT NUMBER.  This is reported as what the')
    print(f'        decomposition gives in the statistic\'s own metric, NOT as a likelihood result.')
    print()
    print(f'  ⇒ ⚑ THE DISCRETENESS CARRIES {quad / EXCESS * 100:.1f} PER CENT OF THE {EXCESS} '
          f'EXCESS IN QUADRATURE')
    print(f'    ({quad:+.5f}), and {absum / EXCESS * 100:.1f} PER CENT IF THE TWO ARE SIMPLY ADDED '
          f'({absum:.5f}),')
    print(f'    AGAINST {abs(d_proj) / EXCESS * 100:.2f} PER CENT IN THE PROJECTED STATISTIC.')

    print()
    print('-' * 104)
    print('  Ⓥ④ WHERE IN q THE TWO PARTS LIVE — printed, so neither is taken on trust')
    print('-' * 104)
    _p, _r, _c, A_L, B, lA = keep['LADDER   (the arm)']
    _p2, _r2, _c2, A_C, _B2, _l2 = keep['CONTINUUM 4.0 pts']
    n = len(A_L)
    edges = np.linspace(0, n, 7).astype(int)
    print(f'      {"q band (index)":18s} {"ladder RMS":>12s} {"cont RMS":>12s}'
          f' {"corr ladder":>12s} {"corr cont":>12s}')
    for i in range(6):
        s = slice(edges[i], edges[i + 1])
        a1, a2, b = A_L[s], A_C[s], B[s]
        rl = np.sqrt(np.sum(a1 * a1) / np.sum(b * b))
        rc = np.sqrt(np.sum(a2 * a2) / np.sum(b * b))
        cl = np.sum(a1 * b) / np.sqrt(np.sum(a1 * a1) * np.sum(b * b))
        cc = np.sum(a2 * b) / np.sqrt(np.sum(a2 * a2) * np.sum(b * b))
        print(f'      [{edges[i]:4d},{edges[i + 1]:4d})      {rl:12.5f} {rc:12.5f}'
              f' {cl:12.5f} {cc:12.5f}')
    print(f'      ⌗ the window carries {n} samples; the bands are equal in index, not in q.')

    print()
    print('-' * 104)
    print('  ⌈ TWO THINGS THE BAND TABLE SHOWS THAT NO SCALAR DOES')
    print('-' * 104)
    print('      ⒜ THE DISCRETENESS\'S PHASE EFFECT IS CONCENTRATED AT HIGH q.  The ladder\'s')
    print('        correlation with the control is >= 0.9998 in every band; the continuum\'s falls')
    print('        monotonically to 0.985 in the top band.  ⇒ ** So the 13.7 per cent is an UPPER')
    print('        reading for a likelihood: the phase half of it lives where the damping tail')
    print('        gives a likelihood least weight, and a real covariance would discount it more')
    print('        than it discounts the amplitude half. **  That is a direction, not a number,')
    print('        and it is said because the metric caveat above would otherwise read as neutral.')
    print('      ⒝ THE TWO MOVES AGREE TO 0.9 PER CENT AND THIS FILE DOES NOT KNOW WHY.  A')
    print('        cancellation that close is either a coincidence of this configuration or a')
    print('        structure of the statistic, and nothing here distinguishes them.  ⌗ No')
    print('        mechanism is offered: the corpus has paid for invented ones before.  What can')
    print('        be said is that it is NOT forced by the identity -- the identity makes the')
    print('        projected number the product, not the two factors\' moves equal and opposite.')

    print()
    print('-' * 104)
    print('  THE ARMS, AGAINST PREDICTION.md — registered 744e5b6c, pinned 9962d71c')
    print('-' * 104)
    hB = abs(aL) > 100 * abs(pL)
    hC = abs(pC) > 5 * abs(pL) and abs(aC - aL) < 0.1 * abs(aL)
    hE = 10.0 <= quad / EXCESS * 100 <= 20.0
    hF = abs(abs(d_amp) / abs(d_pha) - 1) < 0.10 and d_amp * d_pha < 0
    print(f'  Ⓐ proj == rms × cos                     ⇒ {"HIT" if okA else "MISS"}')
    print(f'  Ⓑ the ladder excess is almost all       amplitude {aL:+.5f} vs phase {pL:+.5f},'
          f' ratio {abs(aL / pL):.0f}x   ⇒ {"HIT" if hB else "MISS"}')
    print(f'  Ⓒ the continuum phase part grows        {abs(pC / pL):.1f}x, amplitude by '
          f'{abs(aC - aL) / abs(aL) * 100:.1f}%   ⇒ {"HIT" if hC else "MISS"}')
    print(f'  Ⓔ 10 to 20 per cent in a metric that    measured '
          f'{quad / EXCESS * 100:.1f}%   ⇒ {"HIT" if hE else "MISS"}')
    print(f'    does not let them cancel')
    print(f'  Ⓕ opposite and near-equal within 10%    {abs(abs(d_amp) / abs(d_pha) - 1) * 100:.1f}%'
          f', signs opposite: {d_amp * d_pha < 0}   ⇒ {"HIT" if hF else "MISS"}')

    print()
    print('=' * 104)
    if not (ok1 and okA):
        print('  ⛔ VOID — a control fired.')
        return 1
    print('  ✔ CONTROLS HOLD.')
    print()
    print(f'  ⇒ THE ORDER IS ANSWERED: on the arm\'s own spectrum the {EXCESS} excess is carried')
    print(f'    almost entirely by AMPLITUDE ({aL:+.5f} of {exL:+.5f}, the phase {abs(pL) / abs(exL) * 100:.1f}'
          f' per cent of it),')
    print(f'    and the source\'s discreteness moves the two parts by {d_amp:+.5f} and {d_pha:+.5f}')
    print(f'    IN OPPOSITE DIRECTIONS and within {abs(abs(d_amp) / abs(d_pha) - 1) * 100:.0f} per cent'
          f' of each other -- so it carries')
    print(f'    {abs(d_proj) / EXCESS * 100:.2f} per cent of the excess in the projected statistic'
          f' and {quad / EXCESS * 100:.1f} per cent')
    print(f'    once they are read apart.  ** The projected number is a product of two factors')
    print(f'    that move oppositely, and reading it alone hides a tenth of the excess. **')
    print()
    print('  ** Nothing is applied to the register.  Supplied, not applied. **')
    return 0


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    sys.exit(main())
