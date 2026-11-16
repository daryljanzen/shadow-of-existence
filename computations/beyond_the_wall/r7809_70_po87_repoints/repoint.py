"""r7809 (69) ③: PO-87's 14 repoints, MEASURED before anything in the tree changes.
For each receipt: a temporary copy beside it with every namesake load pointed at its leaf-rate twin (`X.npz` ->
`X_leafrec1.npz` for the 7 candidates' banks; `grid_*` -> `grid_*_leafrec1` for the 7 namesake-grid readers), both run
from the receipt's own directory, and every printed number compared in order.  Output: out/<receipt>.{orig,rep}.txt and
out/SUMMARY.json.  The copy is deleted after its run; the receipt itself is not touched here."""
import os, re, sys, json, subprocess, difflib
ROOT = '/home/user/shadow-of-existence'; RCP = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology')
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out'); os.makedirs(OUT, exist_ok=True)
BANKS = ['r6919_geometry', 'r6919_noop', 'r6929_geometry', 'c54.178_cr', 'c54.186_cr_KCONT', 'c54.186_cr_L3000',
         'r6885_los_cr', 'r6885_losdp0_cr', 'r6885_lossw0_cr', 'r6893_switch_screen_cr', 'r6897_fields', 'r6897_noop',
         'cc66_r185_verify_cr']
GRIDS = ['grid_oneclock', 'grid_licensed', 'refit_grid185']
ITEMS = {
 '01': 'P15_a_source_with_no_physics_reproduces_the_contrast',
 '05': 'P15_the_contrast_excess_is_symmetric_about_the_envelope',
 '06': 'P15_the_control_entered_the_regime_and_the_arm_did_not_move',
 '17': 'P15_the_model_difference_is_an_acoustic_contrast_difference',
 '18': 'P15_the_monopole_zero_point_is_not_the_channel',
 '30': 'P15_there_is_no_phase_residual_and_the_fourth_peak',
 '31': 'P15_three_quarters_of_the_arms_residual_is_the_controls',
 'g1': 'P15_the_controls_base_log_is_banked_beside_the_grids',
 'g2': 'P15_the_fit_has_the_controls_freedom',
 'g3': 'P15_the_kernels_phase_difference_between_the_arms',
 'g4': 'P15_the_peak_plane_survives_the_merge',
 'g5': 'P15_the_selection_does_not_truncate',
 'g6': 'P15_the_skys_own_fourth_peak_cannot_tell_the_arms_apart',
 'g7': 'P15_the_spacing_drift_is_made_in_the_projection'}
NUM = re.compile(r'[-+]?\d+\.\d+(?:[eE][-+]?\d+)?|[-+]?\d+(?:[eE][-+]?\d+)')
def repoint(src):
    n = 0
    for b in BANKS:
        src, k = re.subn(rf"(?<![A-Za-z0-9_.]){re.escape(b)}(?=\.npz|['\"])(?!_leafrec1)", b + '_leafrec1', src); n += k
    for g in GRIDS:
        src, k = re.subn(rf"(?<![A-Za-z0-9_]){g}(?=['\"/])(?!_leafrec1)", g + '_leafrec1', src); n += k
    return src, n
def run(path):
    p = subprocess.run([sys.executable, os.path.basename(path)], cwd=os.path.dirname(path), capture_output=True,
                       text=True, timeout=3000)
    return p.returncode, p.stdout + p.stderr
only = sys.argv[1:] or list(ITEMS)
summ = json.load(open(os.path.join(OUT, 'SUMMARY.json'))) if os.path.exists(os.path.join(OUT, 'SUMMARY.json')) else {}
for k in only:
    f = next(x for x in sorted(os.listdir(RCP)) if x.startswith(ITEMS[k]) and x.endswith('.py'))
    src = open(os.path.join(RCP, f)).read(); rsrc, nsub = repoint(src)
    tmp = os.path.join(RCP, '_tmp_r7809_repoint_' + f)
    open(tmp, 'w').write(rsrc)
    try:
        rc0, o0 = run(os.path.join(RCP, f)); rc1, o1 = run(tmp)
    finally:
        os.remove(tmp)
    o1 = o1.replace('_tmp_r7809_repoint_', '')
    open(os.path.join(OUT, f'{k}.orig.txt'), 'w').write(o0); open(os.path.join(OUT, f'{k}.rep.txt'), 'w').write(o1)
    n0, n1 = NUM.findall(o0), NUM.findall(o1)
    moved = [(a, b) for a, b in zip(n0, n1) if a != b]
    summ[k] = dict(receipt=f, substitutions=nsub, rc_orig=rc0, rc_rep=rc1, numbers=[len(n0), len(n1)],
                   moved=len(moved), first_moved=moved[:40])
    print(f'[{k}] {f[:70]}  subs={nsub} rc {rc0}->{rc1} numbers {len(n0)}/{len(n1)} moved {len(moved)}', flush=True)
    json.dump(summ, open(os.path.join(OUT, 'SUMMARY.json'), 'w'), indent=1)
