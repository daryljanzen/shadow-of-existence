#!/usr/bin/env python3
"""r7679+70 (r7677 item 2): fold the band-RMS sweep on the arm of record, score it as the receipt does, and bank it.

  * Each of the 44 configurations is folded by `r7041_directions/fold.load` from `launch_band_rms.sh`'s slices, which
    checks that the declared slice ranges tile [0, modes) exactly.
  * The twelve sequences, their last steps and verdicts come from the receipt's own code:
    `P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting`'s `env_a`, `osc`, `verdict`, `SEQ`, `FLOOR`,
    `LO`, `HI`, `NG` and `INERT_ON_ARM`, lifted by `ast`. Its `ratio` is restated here only to read this bank instead
    of `/tmp/n66`, with the same arithmetic.
  * Banked as `spectra/r7041_band_rms_leafrec1.npz` (an addition): `ls__<tag>`, `Dl__<tag>`, `l_A__<tag>` for every
    folded configuration, plus `config` and `manifest`. A reader computes the ratio from it exactly as `from_bank` does.
Writes `band_rms.json`.
"""
import ast
import json
import os
import subprocess
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.join(HERE, '..')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
SP = os.path.join(BW, 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/r7677/inj')
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_band_rms_ratio_does_not_move_with_any_numerical_setting.py')
sys.path.insert(0, os.path.join(BW, 'r7041_directions'))
import fold  # noqa: E402

tree = ast.parse(open(RECEIPT, encoding='utf-8').read())
WANT_F = {'env_a', 'osc', 'verdict'}
WANT_A = {'FLOOR', 'LO', 'HI', 'NG', 'SEQ', 'INERT_ON_ARM', 'INJ', 'BANKED', 'R6919'}
keep = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))
        or (isinstance(n, ast.FunctionDef) and n.name in WANT_F)
        or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in WANT_A for t in n.targets))
        or (isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Tuple)
            and {e.id for e in n.targets[0].elts if isinstance(e, ast.Name)} & WANT_A)]
R = {'__name__': 'band_rms_lift'}
exec(compile(ast.Module(body=keep, type_ignores=[]), RECEIPT + '[lift]', 'exec'), R)
missing = (WANT_F | WANT_A) - set(R)
assert not missing, f'the receipt no longer defines {missing}'

loaded, bank = {}, {}


def load(inj, arm, s):
    if arm == 'cr' and s in R['INERT_ON_ARM']:
        s = 'base'
    tag = f'inj_{inj}_{arm}_{s}'
    if tag not in loaded:
        r = fold.load(D, tag)
        if r is None:
            sys.exit(f'{tag}: not complete (fold.load returned None) -- {fold.status(D, tag)}')
        ls, Dl, l_A, form = r
        loaded[tag] = (ls, Dl, l_A, form)
        bank[f'ls__{tag}'], bank[f'Dl__{tag}'], bank[f'l_A__{tag}'] = ls, Dl, np.array(l_A)
    ls, Dl, l_A, _ = loaded[tag]
    return ls / l_A, Dl


def ratio(inj, s):
    a, b = load(inj, 'cr', s), load(inj, 'lcdm', s)
    x = np.linspace(R['LO'], R['HI'], R['NG'])
    A, B = np.interp(x, a[0], R['osc'](*a)), np.interp(x, b[0], R['osc'](*b))
    return float(np.sum(A * B) / np.sum(B * B))


seqs = {(inj, name): [ratio(inj, s) for s in seq] for inj in R['INJ'] for name, seq in R['SEQ'].items()}
steps = {k: 100.0 * abs(v[-1] - v[-2]) / abs(v[-2]) for k, v in seqs.items()}
verds = {k: R['verdict'](v, steps[k] / 100.0) for k, v in seqs.items()}
worst_k = max(steps, key=steps.get)
counts = {c: sum(1 for v in verds.values() if v == c) for c in ('converged', 'not-turned-over', 'two-points-only',
                                                                  'unconverged')}
res = {
    'base': {inj: seqs[(inj, 'KFAC')][0] for inj in R['INJ']},
    'base_namesake': {inj: R['BANKED'][(inj, 'KFAC')][0] for inj in R['INJ']},
    'range': {inj: [min(x for (i, _), v in seqs.items() if i == inj for x in v),
                    max(x for (i, _), v in seqs.items() if i == inj for x in v)] for inj in R['INJ']},
    'sequences': {f'{i}/{n}': v for (i, n), v in seqs.items()},
    'last_step_pct': {f'{i}/{n}': s for (i, n), s in steps.items()},
    'worst_last_step_pct': [f'{worst_k[0]}/{worst_k[1]}', steps[worst_k]],
    'verdicts': {f'{i}/{n}': v for (i, n), v in verds.items()},
    'verdict_counts': counts,
    'verdict_counts_namesake': {'converged': 1, 'not-turned-over': 7, 'two-points-only': 4, 'unconverged': 0},
    'converged': sorted(f'{i}/{n}' for (i, n), v in verds.items() if v == 'converged'),
    'folded': {t: v[3] for t, v in sorted(loaded.items())},
    'floor_pct': 100 * R['FLOOR'],
}
cfg = subprocess.run([sys.executable, '-c', 'import ACOUSTIC_two_arm as M; print("__C__" + str(M._resolved_config()))'],
                     cwd=BW, capture_output=True, text=True,
                     env={**os.environ, 'ARM': 'cr', 'CRH0': '68.570730', 'CROM': '0.291246', 'ZSTART': '3e7',
                          'LEAFSCALES': '1', 'WBH2': '0.021643', 'NS': '1.015066', 'LEAFREC': '1',
                          'OMP_NUM_THREADS': '1'}).stdout
cfg = next(l[5:] for l in cfg.splitlines() if l.startswith('__C__'))
assert json.loads(cfg).get('LEAFREC') is True
bank['config'] = np.array(cfg)
bank['manifest'] = np.array(json.dumps(dict(
    stem='r7041_band_rms_leafrec1', namesake='r7041 injection sweep (/tmp/n66/r7041/inj, never banked)', LEAFREC=1,
    point=dict(CRH0=68.57073, CROM=0.291246, WBH2=0.021643, NS=1.015066, LEAFREC=1, ZSTART=3e7, LEAFSCALES=1),
    control=dict(LH0=67.410309, LOM=0.309826, WBH2=0.021966, NS=0.954248, LEAFREC=1),
    switches='HIER=1 LSTEP=8 LMAXL=2000 + SRCINJ=fixed | SRCINJ=sweep SRCINJRS=own + the setting; KSLICE 250 wide',
    settings='base kfac26 kfac32 kfac40 nk15 nk20 nlos1120 nlos2240 nlosw9 nlosw12 nlosf90 lstep4 '
             '(r7041_directions/launch_sliced.sh); cr nk15/nk20 are base by construction and not built',
    held='r7041 launch_sliced inj set; only the CR point and LEAFREC moved; the control rebuilt at LEAFREC=1, '
         'which equals the namesake control (r7669)',
    note_r7679='folded by r7041_directions/fold.load; keys ls__/Dl__/l_A__<tag>, tag = inj_<inj>_<arm>_<setting>')))
np.savez_compressed(os.path.join(SP, 'r7041_band_rms_leafrec1.npz'), **bank)
res['banked'] = 'spectra/r7041_band_rms_leafrec1.npz'
json.dump(res, open(os.path.join(HERE, 'band_rms.json'), 'w'), indent=1)
print(json.dumps({k: v for k, v in res.items() if k not in ('sequences', 'folded')}, indent=1))
