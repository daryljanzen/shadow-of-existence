#!/usr/bin/env python3
"""MEASURES which of the receipt's ten rows redden under three perturbations of its INPUTS.
Nothing is asserted here: the point is to show the rows that read a depth set are the ones that
move, and that the rows reading the paper, the law's structure and this file's scope do not."""
import os, re, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                 'P15_the_low_ell_scoring_on_the_one_rate_improves_to_1_57_and_the_cited_receipt_'
                 'scores_different_depths_than_the_paper_prints.py')
src = open(R, encoding='utf-8').read()
HERE = os.path.dirname(R)
ANCHORS = (("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {HERE!r}'),
           ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}'))

PROBES = [
    ("P1  the ONE-RATE depths stretched by 1 per cent -- every one-rate figure moves, nothing the "
     "paper says does",
     "A_L, A_1 = AA['distances__armA__L'], AA['distances__armA__one_clock_gate']",
     "A_L, A_1 = AA['distances__armA__L'], 1.01 * AA['distances__armA__one_clock_gate']"),
    ("P2  the ARM-OF-RECORD depths stretched by 1 per cent -- the rows that reproduce the paper's "
     "own printed figures must lose them",
     "A_L, A_1 = AA['distances__armA__L'], AA['distances__armA__one_clock_gate']",
     "A_L, A_1 = 1.01 * AA['distances__armA__L'], AA['distances__armA__one_clock_gate']"),
    ("P3  the converged frozen leg replaced by the unconverged one -- item 3's baseline and its "
     "carry must both go, and only those",
     "F_L_h2, F_L_18 = FC['distances__armB_frozen__L__h2'], FC['distances__armB_frozen__L__NS3_1800']",
     "F_L_h2, F_L_18 = LP['distances__armB_frozen__L'], FC['distances__armB_frozen__L__NS3_1800']"),
]


def run(text):
    # FIRST occurrence only where an anchor could appear twice; each is asserted singular here so a
    # future edit that duplicates one is caught rather than silently half-rewritten.
    for old, new in ANCHORS:
        assert text.count(old) == 1, (old, text.count(old))
        text = text.replace(old, new, 1)
    with tempfile.TemporaryDirectory() as td:
        q = os.path.join(td, 'probe.py')
        open(q, 'w', encoding='utf-8').write(text)
        pr = subprocess.run([sys.executable, '-I', q], capture_output=True, text=True,
                            cwd=HERE, timeout=3600)
    rows = []
    for ln in pr.stdout.splitlines():
        m = re.match(r'\s*\[(PASS|FAIL)\].*?\*\* (.)', ln)
        if m:
            rows.append((m.group(2), m.group(1)))
    return pr.returncode, rows


rc0, base = run(src)
print(f'unperturbed: rc={rc0}  ' + ' '.join(f'{g}:{s}' for g, s in base))
for label, old, new in PROBES:
    assert src.count(old) == 1, (label, src.count(old))
    rc, rows = run(src.replace(old, new))
    red = [g for g, s in rows if s == 'FAIL']
    green = [g for g, s in rows if s == 'PASS']
    print(f'\n{label}\n    rc={rc}\n    REDDENS: {" ".join(red) or "(none)"}'
          f'\n    HOLDS:   {" ".join(green) or "(none)"}')
