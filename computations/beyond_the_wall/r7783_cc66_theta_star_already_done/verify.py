#!/usr/bin/env python3
r"""r7783+cc66 item (5): theta_* on the corpus's own definition, on the one rate -- VERIFIED as
already landed by 70 at r7753, not recomputed into a competing number.

Registered in PREDICTION.md (r7783+cc66.14) before anything was re-run.

rc=0 if every row holds.
"""
import io
import contextlib
import json
import os
import runpy
import sys

OK = []


def row(tag, good, text):
    OK.append((tag, good, text))
    print(f'{"PASS" if good else "FAIL"}  {tag}  {text}', flush=True)


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SRC = os.path.join(ROOT, 'computations', 'beyond_the_wall', 'r7749_70_leafgeom_refit')
PROD = os.path.join(SRC, 'theta_corpus.py')
BANK = os.path.join(SRC, 'theta_corpus.json')
RES = os.path.join(SRC, 'RESULT.md')
for p in (PROD, BANK, RES):
    if not os.path.exists(p):
        sys.exit(f'FATAL: {p} is not where this reads it from.')

banked = json.load(open(BANK, encoding='utf-8'))
print('=' * 99)
print("R1  THE PRODUCER REPRODUCES ITS OWN BANK -- re-running 70's theta_corpus.py")
print('=' * 99)
_cwd = os.getcwd()
os.chdir(SRC)
try:
    with contextlib.redirect_stdout(io.StringIO()):
        runpy.run_path(PROD, run_name='__r7783_verify__')
finally:
    os.chdir(_cwd)
fresh = json.load(open(BANK, encoding='utf-8'))


def flat(d, pre=''):
    out = {}
    for k, v in d.items():
        if isinstance(v, dict):
            out.update(flat(v, pre + k + ' | '))
        else:
            out[pre + k] = v
    return out


fb, ff = flat(banked), flat(fresh)
moved = [k for k in fb if fb[k] != ff.get(k)]
print(f'    {len(fb)} stored value(s) compared; {len(moved)} moved')
for k in moved[:4]:
    print(f'      MOVED {k}: {fb[k]} -> {ff.get(k)}')
row('R1', not moved and set(fb) == set(ff),
    f"70's producer reproduces its bank exactly: {len(fb)} stored values, 0 moved -- so the landed "
    f'figure is not stale')

print()
print('=' * 99)
print('R2  THE FIGURE THE ORDER IS ASKING FOR, AND WHERE IT LIVES')
print('=' * 99)
WANT = {
    "distances' point": (1.03715, -11.9, 1.04235, +4.8),
    'arm of record refit point': (1.03684, -12.9, 1.04215, +4.2),
    'leaf-rate refit minimum': (1.03633, -14.6, 1.04157, +2.3),
}
print(f"      {'point':>28} {'arm of record':>22} {'THE ONE RATE':>22}")
bad = []
for label, (ta, pa, tl, pl) in WANT.items():
    key = next((k for k in banked if k.startswith(label)), None)
    if key is None:
        bad.append(f'{label}: no such point in the bank')
        continue
    rec = banked[key]['arm of record (D_M on stacking rate)']
    one = banked[key]['leaf-rate assignment (D_M on leaf rate)']
    gta, gpa = 100 * rec['theta_zstart'], rec['pull_zstart']
    gtl, gpl = 100 * one['theta_zstart'], one['pull_zstart']
    print(f'      {label:>28} {gta:>10.5f}, {gpa:>+7.1f}s {gtl:>10.5f}, {gpl:>+7.1f}s')
    for got, want, what in ((gta, ta, 'theta arm'), (gpa, pa, 'pull arm'),
                            (gtl, tl, 'theta one rate'), (gpl, pl, 'pull one rate')):
        if abs(got - want) > (0.000005 if 'theta' in what else 0.05):
            bad.append(f'{label}/{what}: {got} against {want}')
sentence = 'the leaf-rate refit sits at +2.3' in open(RES, encoding='utf-8').read()
print(f"    and r7749's RESULT.md already states the conclusion: {sentence}")
row('R2', not bad and sentence,
    'all six landed pairs reproduce and the conclusion sentence is already in the RESULT -- '
    'so the order asks for a figure the corpus has: +2.3 sigma at the leaf-rate refit minimum'
    if not bad and sentence else '; '.join(bad[:3]) or 'the RESULT sentence is missing')

print()
print('=' * 99)
print('R3  AND THE ASYMMETRY THAT IS THE SUBSTANCE: NO ONSET REACHES theta_obs ON THE ARM OF RECORD')
print('=' * 99)
pat = []
for key in banked:
    rec = banked[key]['arm of record (D_M on stacking rate)']['onset_matching']
    one = banked[key]['leaf-rate assignment (D_M on leaf rate)']['onset_matching']
    pat.append((key, rec, one))
    print(f'    {key[:52]:<54} arm {str(rec):>8}   one rate {one if one is None else f"{one:.3e}"}')
row('R3', all(r is None and o is not None for _, r, o in pat),
    f'at all {len(pat)} points: no onset redshift solves theta_* = theta_obs on the radiation-free '
    f'distance, while one does on the one rate -- the asymmetry, not the pull, is what the '
    f'definition shows')

print()
print('=' * 99)
row('R4', True, 'no new figure, no significance beyond the pulls the producer computes, and no '
                're-adjudication of z_rec, of c_s\'s baryon loading or of the omega_b choice -- all '
                "three are the DESI receipt's conventions and 70's to change")
bad2 = [t for t, g, _ in OK if not g]
print(f'{len(OK) - len(bad2)} of {len(OK)} rows hold' + (f'; RED: {bad2}' if bad2 else ''))
print('=' * 99)
raise SystemExit(1 if bad2 else 0)
