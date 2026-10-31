"""r7647+70: fold the arm-of-record slice check (launch.sh) into spectra/r6893_slice_check_leafrec1.npz the way
r6893_directions/bank2.py's step 0b folds the namesake, ADDING `__cr_leafrec1` keys to the namesake's twelve
(unchanged).  An addition, not a re-key.  Gates: every run rc=0; the slices tile; rmax < 1e-14; config LEAFREC true."""
import glob
import json
import os
import shutil
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.join(HERE, '..', 'spectra')
D = os.environ.get('D', '/tmp/claude-0/-home-user-shadow-of-existence/4913e7eb-3c04-585c-bc52-ac1b69fc5eb8/scratchpad/bank6')
fail = []
os.makedirs(os.path.join(HERE, 'logs'), exist_ok=True)


def rc(log):
    return next((int(l.split('rc=')[1]) for l in open(log) if l.startswith('__DONE__')), None)


for q in sorted(glob.glob(f'{D}/*.log')):
    shutil.copy(q, os.path.join(HERE, 'logs'))
    if rc(q) != 0:
        fail.append(f'{os.path.basename(q)}: rc {rc(q)}')
w = f'{D}/whole_cr.npz'
sl = sorted(glob.glob(f'{D}/k*_cr.npz'), key=lambda q: int(os.path.basename(q)[1:].split('_')[0]))
if [int(os.path.basename(q)[1:].split('_')[0]) for q in sl] != list(range(0, 1452, 250)):
    fail.append(f'slices: {len(sl)}')
dw = np.load(w, allow_pickle=True)
ls = dw['ls'].astype(np.int32)
tot = np.zeros(len(ls))
for q in sl:
    d = np.load(q)
    assert len(d['ls']) == len(ls)
    tot = tot + d['Dl'].astype(np.float64)
a = float(np.max(np.abs(tot - dw['Dl'])))
r = a / float(np.max(np.abs(dw['Dl'])))
old = np.load(os.path.join(SP, 'r6893_slice_check.npz'), allow_pickle=True)
out = {k: old[k] for k in old.files}
out.update({'nsl__cr_leafrec1': np.int32(len(sl)), 'amax__cr_leafrec1': np.float64(a), 'rmax__cr_leafrec1': np.float64(r),
            'ls__cr_leafrec1': ls, 'Dl_whole__cr_leafrec1': dw['Dl'].astype(np.float64),
            'Dl_sliced__cr_leafrec1': tot, 'config': dw['config']})
if not json.loads(str(dw['config'])).get('LEAFREC'):
    fail.append('config LEAFREC not true')
if r >= 1e-14:
    fail.append(f'rmax {r:.3e} >= 1e-14')
sw = next((l.split(None, 1)[1].strip() for l in open(f'{D}/whole_cr.log') if l.startswith('__SWITCHES__ ')), '?')
man = dict(file='spectra/r6893_slice_check_leafrec1.npz', namesake='spectra/r6893_slice_check.npz', LEAFREC=1,
           form="ADDITION (r7647 convention): the namesake's twelve keys unchanged, `__cr_leafrec1` keys added",
           point=dict(CRH0=68.570730, CROM=0.291246, WBH2=0.021643, NS=1.015066, ZSTART=3e7, LEAFSCALES=1, LEAFREC=1),
           switches=sw, held="r6893_directions/step0b.sh verbatim, the cr half, $CR -> the arm of record, LEAFREC=1 set; "
                             "bank2.py step 0b's fold; the control not re-run (LEAFREC does not reach it)")
out['manifest'] = np.array(json.dumps(man))
np.savez_compressed(os.path.join(SP, 'r6893_slice_check_leafrec1.npz'), **out)
same_ls = np.array_equal(ls, old['ls__cr'])
dmove = float(np.max(np.abs(dw['Dl'] - old['Dl_whole__cr'])) / np.max(np.abs(old['Dl_whole__cr']))) if same_ls else float('nan')
print(f'arm of record: {len(sl)} slices summed against the whole, max |dD_l| = {a:.3e} ({r:.3e} relative)')
print(f"namesake cr:   {int(old['nsl__cr'])} slices, {float(old['amax__cr']):.3e} ({float(old['rmax__cr']):.3e} relative)")
print(f'whole spectrum moved from the namesake: same ls {same_ls}, max relative |d| = {dmove:.3e}')
if not (1e-3 <= dmove <= 1e-1):
    print('  (prediction band [1e-3, 1e-1] missed)')
print('\n'.join(['FAILS:'] + fail) if fail else 'all gates hold')
sys.exit(1 if fail else 0)
