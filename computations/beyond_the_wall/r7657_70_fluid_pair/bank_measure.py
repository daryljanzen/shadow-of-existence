"""r7657+70: bank the four fluid-path runs as ADDITIONS (spectra/cc66_<tag>.npz, the namesake form ls/Dl/l_A/D_M/r_s/arm
plus config and manifest) and score them through `P15_at_its_own_preferred_H0_...`'s own `_matched` (lensed, matched
locator) and `score` (133-bin unlensed), lifted by executing the receipt up to its first matched read."""
import contextlib
import io
import json
import os
import shutil
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
SP = os.path.join(BW, 'spectra')
ROOT = os.path.dirname(os.path.dirname(BW))
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank8')
R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                 'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_with_no_fitted_number.py')
fail, out = [], []
os.makedirs(os.path.join(HERE, 'logs'), exist_ok=True)
RUNS = {'cr_x_h686_fluid_leafrec1_distances': ('cc66_cr_x_h686_fluid', 'the banked fluid arm\'s sibling at the distances\' point (68.60/0.2973), LEAFREC=1'),
        'cr_fluid_leafrec1': (None, 'the refitted arm of record (68.570730/0.291246/0.021643/1.015066), LEAFREC=1, LEAFGEOM unset'),
        'lcdm_fluid_refit': (None, 'the arm of record\'s own control (LH0=67.410309 LOM=0.309826 WBH2=0.021966 NS=0.954248)')}
for tag in list(RUNS) + ['lcdm_fluid_repro']:
    log = f'{D}/{tag}.log'
    shutil.copy(log, os.path.join(HERE, 'logs', tag + '.log'))
    if not any(l.startswith('__DONE__ rc=0') for l in open(log)):
        fail.append(f'{tag}: not rc=0')
# the reproduction gate
a, b = np.load(f'{D}/lcdm_fluid_repro.npz'), np.load(os.path.join(SP, 'cc66_lcdm_fluid.npz'))
rep = float(np.max(np.abs(a['Dl'] - b['Dl'])) / np.max(np.abs(b['Dl']))) if np.array_equal(a['ls'], b['ls']) else float('nan')
out.append(f'default control re-run against cc66_lcdm_fluid: same ls {np.array_equal(a["ls"], b["ls"])}, max |dD_l|/peak = {rep:.2e}')
if not rep < 1e-11:
    fail.append(f'control reproduction {rep:.2e}')
for tag, (ns_, what) in RUNS.items():
    d = np.load(f'{D}/{tag}.npz', allow_pickle=True)
    o = {k: d[k] for k in ('ls', 'Dl', 'l_A', 'D_M', 'r_s', 'arm')}
    o['config'] = d['config']
    sw = next((l.split(None, 1)[1].strip() for l in open(f'{D}/{tag}.log') if l.startswith('__SWITCHES__ ')), '')
    o['manifest'] = np.array(json.dumps(dict(
        file=f'spectra/cc66_{tag}.npz', namesake=(f'spectra/{ns_}.npz' if ns_ else None),
        form='ADDITION (r7647 convention): a new file; nothing existing moves', what=what,
        path='FLUID (HIER absent), r6760+cc66.7\'s recipe LSTEP=2 LMAXL=1300', switches=sw,
        reader='receipts/P15_CR_cosmology/P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_with_no_fitted_number.py (two-path block)')))
    if 'HIER=1' in sw:
        fail.append(f'{tag}: HIER set -- not the fluid path')
    np.savez(os.path.join(SP, f'cc66_{tag}.npz'), **o)
# score through the receipt's own functions
src = open(R).read()
ns = {'__file__': R, '__name__': 'lift'}
cwd = os.getcwd()
os.chdir(os.path.dirname(R))
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src[:src.index('_MSKY = _sweep(')], R, 'exec'), ns)
os.chdir(cwd)
M = {}
out.append(f"\n{'spectrum':42s} {'P1':>7} {'P2':>7} {'P3':>7} {'P4':>8} {'comb':>7} {'P1/P2':>6} {'P1/P3':>6} | 133-bin {'P1/P2':>6} {'P1/P3':>6} {'chi2':>7}")
for t in ('lcdm_fluid', 'cr_x_h686_fluid', 'cr_x_h686_fluid_leafrec1_distances', 'lcdm_fluid_refit', 'cr_fluid_leafrec1',
          'cr_x_h686_pol', 'cr_x_h686_pol_leafrec1_distances'):
    m, s = ns['_matched'](f'cc66_{t}.npz'), ns['score'](t)
    M[t] = (m, s)
    out.append(f"{t:42s} " + ' '.join(f'{x:7.2f}' for x in m['pk']) + f" {m['a4']:7.2f} {m['p12']:6.3f} {m['p13']:6.3f} |"
               f"         {s['p12']:6.3f} {s['p13']:6.3f} {s['chi2']:7.1f}")
pa = M['cr_x_h686_fluid_leafrec1_distances'][0]
P = dict(pk=(219.47, 528.26, 809.05, 1116.89), comb=297.31, p12=2.475, p13=2.995)
ok_a = (all(abs(x - y) <= 1.5 for x, y in zip(pa['pk'], P['pk'])) and abs(pa['a4'] - P['comb']) <= 1.0
        and abs(pa['p12'] - P['p12']) <= 0.03 and abs(pa['p13'] - P['p13']) <= 0.03)
over = pa['p12'] > M['lcdm_fluid'][0]['p12'] and pa['p13'] > M['lcdm_fluid'][0]['p13']
pb, cb, c0 = M['cr_fluid_leafrec1'][0], M['lcdm_fluid_refit'][0], M['lcdm_fluid'][0]
ok_b = (abs(pb['a4'] - pa['a4']) <= 2.0 and abs(pb['p12'] - pa['p12']) <= 0.06 and abs(pb['p13'] - pa['p13']) <= 0.06
        and abs(cb['p12'] - c0['p12']) <= 0.05 and abs(cb['p13'] - c0['p13']) <= 0.05)
out.append(f"\nprediction (a), the LEAFREC shift carried over: {'HOLDS' if ok_a else 'MISSED'}; the fluid arm overshoots its control in both: {over}")
out.append(f"prediction (b), the refitted arm and its own control: {'HOLDS' if ok_b else 'MISSED'}")
json.dump({t: dict(matched={k: (list(map(float, v)) if hasattr(v, '__len__') else float(v)) for k, v in m.items() if k in ('pk', 'a4', 'p12', 'p13')},
                   score133={k: float(s[k]) for k in ('p12', 'p13', 'chi2')}) for t, (m, s) in M.items()},
          open(os.path.join(HERE, 'measure.json'), 'w'), indent=1)
print('\n'.join(out))
print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold')
sys.exit(1 if fail else 0)
