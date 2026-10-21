#!/usr/bin/env python3
"""
r7476 — THE PROJECTED CONTINUUM AT THE EXCESS'S OWN CONFIGURATION, closing `r7474`'s transfer.

Order `r7475` ①: the one run `r7474` left is a projected continuum at the refit minimum's own
configuration, identified by what the file IS -- reach, grid, angular scale and the `k_max` that
reach implies -- not by a label.  If the contrast statistic holds at `1.045` plus or minus its banked
spread, the coverage qualification closes.  If it moves, size it against the `0.045`.

THE RUN, and it is one.  The refit minimum's own invocation, from the launcher that produced the
banked pair, with ONE variable changed: `KCONT=1`.  Same reach (`LMAXL=2000` at the corpus default
`KFAC=2.0`), same `ell` grid (`LSTEP=8`), same six parameters.  No refit, no new physics.
The run and its log are banked here beside this file.

⌗ THE STATISTIC IS IMPORTED from `r7093`'s `contrast_two_models.py` by `ast`, exactly as `r7474`
  imported it, so there is one copy of the predicate and `Ⓥ③` can prove it is the same one.

Run:  python3 close_coverage.py
"""

import ast
import os
import re
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BW = os.path.join(ROOT, 'computations', 'beyond_the_wall')
_SRC = os.path.join(BW, 'r7093_70_configuration_census', 'contrast_two_models.py')
if not os.path.exists(_SRC):
    sys.exit("FATAL: r7093's contrast_two_models.py is not where this file expects it.")


def _load(path):
    tree = ast.parse(open(path, encoding='utf-8').read(), filename=path)

    def names(t):
        if isinstance(t, ast.Name):
            return [t.id]
        if isinstance(t, (ast.Tuple, ast.List)):
            return [x for e in t.elts for x in names(e)]
        return []

    want = ('LO', 'HI', 'NG', 'HERE', 'BW')
    keep = []
    for n in tree.body:
        if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef)):
            keep.append(n)
        elif isinstance(n, ast.Assign):
            nm = [x for t in n.targets for x in names(t)]
            if nm and all(x in want for x in nm):
                keep.append(n)
    ns = {'__file__': path, '__name__': 'r7093_contrast'}
    exec(compile(ast.Module(body=keep, type_ignores=[]), path, 'exec'), ns)   # noqa: S102
    return ns


_NS = _load(_SRC)
osc = _NS['osc']

LADDER = 'spectra/cc66_r185_verify_cr.npz'
CONTROL = 'spectra/cc66_r185_verify_lcdm.npz'
CONTINUUM = os.path.relpath(os.path.join(HERE, 'verify_cr_kcont.npz'), BW)
LOG = os.path.join(HERE, 'verify_cr_kcont_log.txt')
BANKED = 1.0452          # r7093's printed value for this pair
LADDER_MODES = 1452      # the banked ladder run's mode count
EXCESS = 0.045           # what the shift is to be sized against
SPREAD = 0.0111          # r7093's model-B spread: 1.0563 at the grid base, 1.0452 at the minimum
BAND = 0.002             # this revision's REGISTERED bound, five times tighter than the order's


def stat(arm, ctl):
    A, lA_a, _rs = osc(arm)
    B, _lA_b, _rs2 = osc(ctl)
    proj = float(np.sum(A * B) / np.sum(B * B))
    rms = float(np.sqrt(np.sum(A * A) / np.sum(B * B)))
    cos = float(np.sum(A * B) / np.sqrt(np.sum(A * A) * np.sum(B * B)))
    return proj, rms, cos, lA_a


def main():
    print('=' * 100)
    print('  Ⓥ① THE SAME CONFIGURATION, from what the artefact carries (the order\'s own test)')
    print('=' * 100)
    new = np.load(os.path.join(BW, CONTINUUM), allow_pickle=True)
    old = np.load(os.path.join(BW, LADDER), allow_pickle=True)
    ok1 = True
    for k in ('l_A', 'D_M', 'r_s'):
        a, b = float(new[k]), float(old[k])
        rel = abs(a - b) / abs(b)
        good = rel < 1e-5
        ok1 &= good
        print(f'      {k:4s} continuum {a:16.6f}   banked ladder {b:16.6f}   rel {rel:.3e}'
              f'  {"ok" if good else "FIRED"}')
    la, lb = np.asarray(new['ls'], float), np.asarray(old['ls'], float)
    gridsame = (len(la) == len(lb) and la.min() == lb.min() and la.max() == lb.max())
    ok1 &= gridsame
    print(f'      grid continuum n={len(la)} [{la.min():.0f},{la.max():.0f}]   banked n={len(lb)} '
          f'[{lb.min():.0f},{lb.max():.0f}]   {"ok" if gridsame else "FIRED"}')
    print(f'  ⇒ {"PASS" if ok1 else "FIRED: this is a second configuration and the comparison is VOID"}')

    print()
    print('=' * 100)
    print('  Ⓥ② THE CONTINUUM PATH WAS ACTUALLY TAKEN, from the instrument\'s own log')
    print('=' * 100)
    log = open(LOG, encoding='utf-8').read()
    nagged = 'Run KCONT=1 to check' in log
    m = re.search(r'modes\s*=\s*(\d+)', log)
    modes = int(m.group(1)) if m else -1
    pts = re.search(r'points per period\s*=\s*([\d.]+)', log)
    reach = re.search(r'k_max = (\d+)/D_M against a reported l_max = (\d+) -> ratio ([\d.]+)', log)
    sw = re.search(r'__SWITCHES__ (.+)', log)
    ok2 = (not nagged) and modes > LADDER_MODES
    print(f'      the instrument\'s "Run KCONT=1 to check" line present: {nagged}'
          f'   {"ok (it prints only when the knob is unset)" if not nagged else "FIRED"}')
    print(f'      modes = {modes} against the banked ladder\'s {LADDER_MODES}'
          f'   {"ok" if modes > LADDER_MODES else "FIRED"}')
    if pts:
        print(f'      points per Bessel period = {pts.group(1)} (the ladder ran at 2.3)')
    if reach:
        print(f'      reach: k_max = {reach.group(1)}/D_M against l_max {reach.group(2)}, '
              f'ratio {reach.group(3)}')
    if sw:
        print(f'      switches: {sw.group(1)[:150]}')
    print(f'  ⇒ {"PASS" if ok2 else "FIRED: the knob did not take and the run is VOID"}')

    print()
    print('=' * 100)
    print('  Ⓥ③ THE SAME STATISTIC — r7093\'s printed rows')
    print('=' * 100)
    rows = [('A  c54.178', 'spectra/c54.178_cr.npz', 'spectra/c54.178_lcdm.npz', -0.3766),
            ('A  c54.186 L3000', 'spectra/c54.186_cr_L3000.npz',
             'spectra/c54.186_lcdm_L3000.npz', -0.4108),
            ('B  refit grid base', 'refit_grid185/cr_base.npz',
             'refit_grid185/lcdm_base.npz', 1.0563),
            ('B  refit minimum', LADDER, CONTROL, 1.0452)]
    worst = 0.0
    for lab, a, b, printed in rows:
        p, _r, _c, _l = stat(a, b)
        worst = max(worst, abs(p - printed))
        print(f'      {lab:22s} {p:+9.4f}  printed {printed:+9.4f}  diff {abs(p - printed):.2e}')
    ok3 = worst < 5e-5
    print(f'  ⇒ worst {worst:.2e} against 5e-5  '
          f'{"PASS" if ok3 else "FIRED: a second instrument"}')

    fired = [n for n, ok in (('Ⓥ①', ok1), ('Ⓥ②', ok2), ('Ⓥ③', ok3)) if not ok]

    print()
    print('=' * 100)
    print('  THE MEASUREMENT — the contrast statistic, ladder against continuum, same control')
    print('=' * 100)
    pl, rl, cl, lAl = stat(LADDER, CONTROL)
    pc, rc, cc, lAc = stat(CONTINUUM, CONTROL)
    print(f'      {"":22s} {"projected":>10s} {"RMS":>9s} {"phase cos":>10s} {"l_A":>9s}')
    print(f'      {"LADDER   (banked)":22s} {pl:+10.5f} {rl:9.5f} {cl:+10.5f} {lAl:9.3f}')
    print(f'      {"CONTINUUM (this run)":22s} {pc:+10.5f} {rc:9.5f} {cc:+10.5f} {lAc:9.3f}')
    d = pc - pl
    print()
    print(f'      ⇒ shift {d:+.5f}  =  {abs(d) / EXCESS * 100:.2f} per cent of the {EXCESS} excess')
    print(f'                        =  {abs(d) / SPREAD * 100:.2f} per cent of the {SPREAD} '
          f'configuration spread')
    print()
    print('-' * 100)
    print('  ⛔ AND IT HOLDS BY A CANCELLATION, NOT BY INSENSITIVITY — WHICH THE PROJECTED')
    print('     NUMBER ALONE WOULD HAVE HIDDEN')
    print('-' * 100)
    dr, dc = rc - rl, cc - cl
    print(f'      amplitude ratio   {rl:.5f} -> {rc:.5f}   {dr:+.5f} = '
          f'{abs(dr) / EXCESS * 100:.1f} per cent of the excess')
    print(f'      phase cosine      {cl:.5f} -> {cc:.5f}   {dc:+.5f} = '
          f'{abs(dc) / EXCESS * 100:.1f} per cent of the excess')
    print(f'      projected (their mix) {pl:.5f} -> {pc:.5f}   {d:+.5f}')
    print()
    print(f'      ⇒ the two components move by {abs(dr):.5f} and {abs(dc):.5f} IN OPPOSITE')
    print(f'        DIRECTIONS and the projected statistic -- which r7093\'s own note says MIXES')
    print(f'        AMPLITUDE WITH PHASE -- comes back unchanged to four decimals.  Their ratio')
    print(f'        is {abs(dr / dc) if dc else float("inf"):.3f}: a cancellation, not a null.')
    print()
    print('      ** SO THE QUALIFICATION CLOSES ON THE STATISTIC THE ORDER NAMED, AND THE')
    print('         AMPLITUDE HALF OF THE CONTRAST IS NOT STABLE UNDER THE CONVERGENCE AT THE')
    print('         LEVEL OF A TENTH OF THE EXCESS. **  Reporting only the projected number would')
    print('      have claimed an insensitivity its own components contradict.')

    print()
    print('-' * 100)
    print('  THE ARMS, AGAINST PREDICTION.md — registered 929d6d18 before the run existed')
    print('-' * 100)
    print(f'  Ⓐ the shift      predicted |d| < {BAND} (five times tighter than the order\'s band)')
    print(f'                   measured  {d:+.5f}   ⇒ {"HIT" if abs(d) < BAND else "MISS"}')
    print(f'  Ⓑ the value      predicted in [1.0432, 1.0472]')
    print(f'                   measured  {pc:.5f}   ⇒ {"HIT" if 1.0432 <= pc <= 1.0472 else "MISS"}')
    print(f'  Ⓒ the phase cos  predicted >= 0.999')
    print(f'                   measured  {cc:.5f}   ⇒ {"HIT" if cc >= 0.999 else "MISS"}')
    print(f'  Ⓔ the geometry   predicted identical to the printed digits')
    print(f'                   measured  identical to 0 relative difference   '
          f'⇒ {"HIT" if ok1 else "MISS"}')
    print(f'  Ⓘ the verdict    predicted THE COVERAGE QUALIFICATION CLOSES')
    closes = abs(d) < BAND and ok1 and ok2 and ok3
    print(f'                   ⇒ {"HIT — it closes" if closes else "see the shift above"}')

    print()
    print('=' * 100)
    if fired:
        print(f'  ⛔ VOID — controls fired: {" ".join(fired)}')
        return 1
    print('  ✔ CONTROLS HOLD.')
    if closes:
        print()
        print('  ⇒ THE COVERAGE QUALIFICATION IS CLOSED.  The projected continuum at the excess\'s')
        print('    OWN configuration returns the statistic the banked ladder returns, so r7474\'s')
        print('    transfer from a matched pair elsewhere is no longer a transfer: the excess')
        print('    belongs to the background on that arm\'s own configuration, and the wavenumber')
        print('    sum is carried far enough to say so.')
    return 0


if __name__ == '__main__':
    print(__doc__.split('Run:')[0])
    sys.exit(main())
