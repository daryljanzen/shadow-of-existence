#!/usr/bin/env python3
"""r7703+70 item 2: bank FROZEN converged in NS3 (1800, 2400 and their h^2 extrapolation) on (L) at both points and on
the control background (one clock), with per-row numerics. Reads frozen_runs.json (this directory) and r7701's
ns3_frozen_followup.json (the distances point's rungs). Writes spectra/p15_lowell_depths_frozen_converged_leafrec1.npz
and bank_frozen.json (the comparisons against arm A (L), DECOUPLED and the banked NS3 900 rows)."""
import json, os, subprocess
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); BW = os.path.join(HERE, '..'); SP = os.path.join(BW, 'spectra')
ROOT = os.path.abspath(os.path.join(BW, '..', '..'))
ELLS = [2, 3, 4, 5, 6, 7, 8]
R = json.load(open(os.path.join(HERE, 'frozen_runs.json')))
F = json.load(open(os.path.join(BW, 'r7701_70_leafpert_convergence', 'ns3_frozen_followup.json')))
A = np.load(os.path.join(SP, 'p15_lowell_depths_armA_leafpert_leafrec1.npz'))
B = np.load(os.path.join(SP, 'p15_lowell_depths_leafpert_leafrec1.npz'))
C = np.load(os.path.join(SP, 'cc66_lowell_sweep.npz'))
FROZEN = dict(ZEND=0, NTAU=150000, KLO=0.1, NLOW=480)
LADDER = {'distances': {n: F[f'NS3_{n}'] for n in (1800, 2400)},
          'refit': {n: R[f'refit_L__NS3_{n}']['depths'] for n in (1800, 2400)},
          'control': {n: R[f'control__NS3_{n}']['depths'] for n in (900, 1800, 2400)}}
LAB = {'distances': 'L', 'refit': 'L', 'control': 'one_clock'}


def h2(a, b, n1=1800, n2=2400):
    return (n2 ** 2 * np.asarray(b, float) - n1 ** 2 * np.asarray(a, float)) / (n2 ** 2 - n1 ** 2)


out = {'ells': np.array(ELLS)}; numerics = {}; res = {}
for pt, lad in LADDER.items():
    for n, d in lad.items():
        k = f'{pt}__armB_frozen__{LAB[pt]}__NS3_{n}'
        out[k] = np.array(d, float); numerics[k] = dict(FROZEN, NS3=n)
    x = np.round(h2(lad[1800], lad[2400]), 4)
    k = f'{pt}__armB_frozen__{LAB[pt]}__h2'
    out[k] = x; numerics[k] = dict(FROZEN, NS3='h^2 extrapolation from 1800 and 2400 (h = (eta_0 - EFINE)/NS3)')
    if pt == 'control':
        dec = np.asarray(C['DECOUPLED_control_KLO_0_1_NS3_60000'][:7], float); base = np.asarray(lad[900], float)
        ref = None
    else:
        dec = np.asarray(B[f'{pt}__armB_decoupled__L'][:7], float); base = np.asarray(B[f'{pt}__armB_frozen__L'][:7], float)
        ref = np.asarray(A[f'{pt}__armA__L'][:7], float)
    r = dict(h2=x.tolist(), d2400_vs_h2_pct=np.round(100 * (np.asarray(lad[2400]) / x - 1), 2).tolist(),
             ns3_900_to_h2_pct=np.round(100 * (x / base - 1), 2).tolist(),
             vs_decoupled_pct=np.round(100 * (x / dec - 1), 2).tolist())
    if ref is not None:
        r['vs_armA_L_pct'] = np.round(100 * (x / ref - 1), 2).tolist()
    r['max_abs'] = {k2: max(abs(v) for v in r[k2]) for k2 in r if k2.endswith('_pct')}
    res[pt] = r
rows = [k for k in out if '__armB_' in k]
blob = subprocess.run(['git', 'rev-parse', 'HEAD:storyboard_receipts/HIER_photon_hierarchy.py'], cwd=ROOT,
                      capture_output=True, text=True).stdout.strip()
out['config'] = np.array(json.dumps(dict(
    instrument='storyboard_receipts/HIER_photon_hierarchy.py (arm B) through the receipt arm-B harness', HIER_blob=blob,
    points=dict(distances=dict(H0=68.60, Om=0.2973, WBH2=0.02237, radiation='4.1833e-5/h^2'),
                refit=dict(H0=68.570730, Om=0.291246, WBH2=0.021643, radiation='4.15e-5/h^2'),
                control=dict(H0=67.40, Om=0.3150, WBH2=0.02237, radiation='4.1833e-5/h^2')),
    SPLITCLOCK={k: ('L' if '__L__' in k else None) for k in rows},
    clock={k: ('(L): HIER SPLITCLOCK=L, as p15_lowell_depths_leafpert_leafrec1' if '__L__' in k
               else 'one clock (SPLITCLOCK unset), as cc66_lowell_sweep FROZEN_control_KLO_0_1') for k in rows},
    numerics=numerics,
    ARM="HIER with ARM unset; (L) rows the arm of record's construction, control rows one clock", LEAFREC=True,
    LEAFSCALES=None, ZSTART=None, STACKPERT=None, VISLEAF=None,
    note_defining='LEAFSCALES/ZSTART/STACKPERT/VISLEAF are ACOUSTIC_two_arm.py switches; HIER has none, so each is '
                  'written out as null. (L) mirrors STACKPERT unset (LEAFPERT) and VISLEAF=0.',
    note_ns3='NS3 >= ~3000 is NOT used: at 3600 the mode at the HKCAP edge (h*k = 0.079998) blows up finitely at '
             'k*eta ~ 250 and the harness returns r = 1 (r7703+70 item 1). Every run here printed max|Phi| <= 0.93.')))
out['manifest'] = np.array(json.dumps(dict(
    stem='p15_lowell_depths_frozen_converged_leafrec1', LEAFREC=1, rows=rows,
    held="the receipt's arm-B harness with FROZEN_adjudicated settings; NS3 the only knob changed",
    note_r7703='FROZEN converged in NS3 (69, r7703 item 2): (L) at both points and the control background')))
np.savez(os.path.join(SP, 'p15_lowell_depths_frozen_converged_leafrec1.npz'), **out)
res['banked'] = 'spectra/p15_lowell_depths_frozen_converged_leafrec1.npz'; res['rows'] = rows
json.dump(res, open(os.path.join(HERE, 'bank_frozen.json'), 'w'), indent=1)
print(json.dumps({k: (v['max_abs'] if isinstance(v, dict) and 'max_abs' in v else v) for k, v in res.items()}, indent=1))
