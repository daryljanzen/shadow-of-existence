#!/usr/bin/env python3
"""MEASURES which of the receipt's nine rows redden under three perturbations of its INPUTS.
Nothing is asserted here: the point is that the rows reading the measured legs move, the row
identifying the comb build from its own switches moves only when those switches move, and the rows
reading the inherited guards and this file's scope do not."""
import json, os, re, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                 'P15_the_frozen_build_measured_on_the_one_rate_is_3_3_not_the_carried_3_4_and_'
                 'theta_star_at_the_combs_own_point_is_plus_4_8_sigma.py')
src = open(R, encoding='utf-8').read()
HERE = os.path.dirname(R)
ANCHORS = (("HERE = os.path.dirname(os.path.abspath(__file__))", f'HERE = {HERE!r}'),
           ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", f'ROOT = {ROOT!r}'))

PROBES = [
    ("P1  the measured h2 leg stretched by 1 per cent -- every measured figure and the carry "
     "comparison must move, and nothing about theta* may",
     "D2400 = np.asarray(runs['distances_one_clock__NS3_2400']['depths'], float)",
     "D2400 = 1.01 * np.asarray(runs['distances_one_clock__NS3_2400']['depths'], float)"),
    ("P2  the comb build's switches rewritten to the refit minimum -- the premise row must lose its "
     "identification, and only that row",
     "_sw = COMB['switches']",
     "_sw = COMB['switches'].replace('CRH0=68.60', 'CRH0=68.585672').replace('CROM=0.2973', 'CROM=0.294463')"),
    ("P3  one rung's max|Phi| pushed past the inherited 0.93 ceiling -- the guard row must fire",
     "_phis = [runs[k]['phimax'] for k in runs]",
     "_phis = [0.97 for k in runs]"),
]


def run(text):
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
