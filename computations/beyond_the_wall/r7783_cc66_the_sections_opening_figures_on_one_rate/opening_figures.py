#!/usr/bin/env python3
r"""r7783+cc66 item (3): the acoustic section's opening figures, read off the ONE-RATE arm through
the paper's OWN seven-window locator.

Registered in PREDICTION.md (r7783+cc66.7) before any figure was read.

⛭ THE LOCATOR IS NOT REIMPLEMENTED.  The comb receipt's own source is executed in a namespace here
and its `_matched` is called on the one-rate arm, so the sky, the arm of record and the one-rate arm
all go through ONE procedure -- the seven windows (40, 45, 50, 55, 60, 70, 80), the lensing ratio,
the binning and the parabola's vertex value, exactly as the paper's figures were made.

rc=0 if every row holds.  R4/R5 (the fourth feature) need a polarisation run and report their own
state rather than guessing.
"""
import io
import contextlib
import glob
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SPEC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'spectra')
COMB = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                    'P15_at_its_own_preferred_H0_the_crossing_arm_predicts_the_acoustic_comb_'
                    'with_no_fitted_number.py')
POL_OUT = os.path.join(SPEC, 'r7783_leafgeom_refit_pol_cr.npz')
ONE_RATE = 'r7749_leafgeom_nofit_L2000_cr.npz'
RECORD = 'cc66_cr_x_h686_L2000_leafrec1_distances.npz'
OK = []


def row(tag, good, text):
    OK.append((tag, good, text))
    print(f'{"PASS" if good else "FAIL"}  {tag}  {text}', flush=True)


print('=' * 99)
print('R0  THE CENSUS: WHICH POLARISATION BANKS EXIST, AND WHETHER ANY IS A LEAFGEOM=1 ARM')
print('=' * 99)
pol, lg_hits = [], []
for f in sorted(glob.glob(os.path.join(ROOT, 'computations', '**', '*.npz'), recursive=True)):
    try:
        z = np.load(f, allow_pickle=True)
    except Exception:
        continue
    if not ('Dl_EE' in z.files or 'Dl_TE' in z.files):
        continue
    rel = os.path.relpath(f, ROOT)
    lg = None
    if 'config' in z.files:
        c = z['config']
        try:
            c = c.item()
        except Exception:
            pass
        try:
            lg = json.loads(str(c)).get('LEAFGEOM')
        except Exception:
            lg = 'unparsed'
    sw = str(z['switches']) if 'switches' in z.files else ''
    pol.append((rel, lg))
    if lg is True or 'LEAFGEOM=1' in sw:
        lg_hits.append(rel)
    print(f'    {rel:70s} LEAFGEOM={lg}')
mine = os.path.relpath(POL_OUT, ROOT) in [p for p, _ in pol]
row('R0', len(pol) - (1 if mine else 0) == 4 and not [h for h in lg_hits
                                                      if h != os.path.relpath(POL_OUT, ROOT)],
    f'{len(pol)} npz file(s) in the tree carry Dl_EE or Dl_TE'
    + (f' (one of them this revision\'s own run)' if mine else '')
    + f'; pre-existing LEAFGEOM=1 polarisation arms: '
    + (', '.join(h for h in lg_hits if h != os.path.relpath(POL_OUT, ROOT)) or 'NONE')
    + ' -- so the fourth-feature comparison cannot be read off the bank, which is what R4 is for')

print()
print('=' * 99)
print("R1/R2/R3  THE OPENING FIGURES, THROUGH THE COMB RECEIPT'S OWN SEVEN-WINDOW LOCATOR")
print('=' * 99)
src = open(COMB, encoding='utf-8').read()
ns = {'__name__': '__r7783_comb__', '__file__': COMB}
buf = io.StringIO()
try:
    with contextlib.redirect_stdout(buf):
        exec(compile(src, COMB, 'exec'), ns)
except SystemExit:
    pass
except Exception as exc:
    sys.exit(f'FATAL: the comb receipt did not execute here: {type(exc).__name__}: {exc}')
for name in ('_matched', '_sweep', '_locate', '_WS', 'fit_comb'):
    if name not in ns:
        sys.exit(f'FATAL: the comb receipt no longer defines `{name}`; the locator has moved.')
print(f'    the locator\'s seven windows, from the receipt itself: {ns["_WS"]}')
with contextlib.redirect_stdout(io.StringIO()):
    rec = ns['_matched'](RECORD)
    one = ns['_matched'](ONE_RATE)

# the arm of record's figures as r7781 labelled them in the paper
PAPER = dict(peaks=(220.0, 536.3, 811.6, 1125.1), comb=299.1, phi=-0.2488, p12=2.291, p13=2.349)
print(f"\n      {'quantity':>22} {'arm of record':>16} {'one rate':>12} {'move':>12}")
for lab, key in (('peak 1', 0), ('peak 2', 1), ('peak 3', 2), ('peak 4', 3)):
    print(f"      {lab:>22} {rec['pk'][key]:>16.3f} {one['pk'][key]:>12.3f} "
          f"{one['pk'][key] - rec['pk'][key]:>+12.3f}")
for lab, key in (('comb (3 peaks)', 'a3'), ('phi/pi', 'f3'), ('P1/P2', 'p12'), ('P1/P3', 'p13')):
    print(f"      {lab:>22} {rec[key]:>16.4f} {one[key]:>12.4f} {one[key] - rec[key]:>+12.4f}")

d_pk = [abs(float(one['pk'][i]) - float(rec['pk'][i])) for i in range(4)]
paper_ok = all(abs(float(rec['pk'][i]) - PAPER['peaks'][i]) < 0.6 for i in range(4))
row('R1', paper_ok and all(d < 1.0 for d in d_pk),
    f"the arm of record reproduces the paper's four peaks {PAPER['peaks']} "
    f"({[round(float(x), 1) for x in rec['pk']]}), and on the one rate each peak moves by "
    f"{max(d_pk):.3f} multipoles at most -- under one, as registered")
row('R2', abs(one['f3'] - rec['f3']) < 0.002 and abs(rec['f3'] - PAPER['phi']) < 0.002,
    f"the phase intercept phi/pi is {rec['f3']:+.4f} on the arm of record against the paper's "
    f"{PAPER['phi']:+.4f}, and {one['f3']:+.4f} on the one rate -- a move of "
    f"{one['f3'] - rec['f3']:+.5f}")
row('R3', abs(one['p12'] - rec['p12']) < 0.01 and abs(one['p13'] - rec['p13']) < 0.01
    and abs(rec['p12'] - PAPER['p12']) < 0.01 and abs(rec['p13'] - PAPER['p13']) < 0.01,
    f"the height ratios are {rec['p12']:.3f} and {rec['p13']:.3f} on the arm of record against the "
    f"paper's {PAPER['p12']} and {PAPER['p13']}, and {one['p12']:.3f} and {one['p13']:.3f} on the "
    f"one rate -- moves of {one['p12'] - rec['p12']:+.4f} and {one['p13'] - rec['p13']:+.4f}")

print()
print('=' * 99)
print('R4  THE POLARISATION RUN THE FOURTH FEATURE NEEDS -- STATE, NOT A GUESS')
print('=' * 99)
if not os.path.exists(POL_OUT):
    row('R4', False, f'NOT YET AVAILABLE: {os.path.relpath(POL_OUT, ROOT)} does not exist. The '
                     f'launcher is idempotent and registered in PREDICTION.md R4; until it finishes '
                     f'there is no EE or TE on a LEAFGEOM=1 arm and R5 is WITHHELD, not guessed')
    row('R5', False, 'WITHHELD: conditional on R4, exactly as registered')
else:
    with np.load(POL_OUT, allow_pickle=True) as z:
        keys = list(z.files)
        ls_n, Dl_n = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    with np.load(os.path.join(SPEC, 'r7749_leafgeom_refit_verify_cr.npz'), allow_pickle=True) as z:
        ls_b, Dl_b = np.asarray(z['ls'], float), np.asarray(z['Dl'], float)
    sh = np.intersect1d(ls_n, ls_b)
    a = np.interp(sh, ls_n, Dl_n)
    b = np.interp(sh, ls_b, Dl_b)
    worst = float(np.max(np.abs(a / b - 1.0))) if sh.size else 1.0
    print(f'    keys: {keys}')
    print(f'    TT against the banked refit arm over {sh.size} shared multipoles: '
          f'max |new/banked - 1| = {worst:.3e}')
    row('R4', {'Dl_EE', 'Dl_TE'}.issubset(keys) and sh.size > 100 and worst < 1e-6,
        f'the run IS the same arm: EE and TE present, and its TT reproduces the banked refit arm to '
        f'{worst:.2e} over {sh.size} shared multipoles')
    row('R5', False, 'the fourth-feature SCORE is the next step and is not computed in this file: '
                     'it runs PO-47s locator through r7633s score.py, which needs the control and '
                     'ACT inputs; registered as a separate step rather than inlined here')

print()
print('=' * 99)
bad = [t for t, g, _ in OK if not g]
print(f'{len(OK) - len(bad)} of {len(OK)} rows hold' + (f'; open: {bad}' if bad else ''))
print('=' * 99)
raise SystemExit(1 if bad else 0)
