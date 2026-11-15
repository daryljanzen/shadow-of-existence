#!/usr/bin/env python3
"""MEASURES which of the receipt's nine rows redden under two perturbations.  Nothing is asserted
here: the point is to show the rows that read the fit are the ones that move, and that the rows
reading the paper, the window and this file's scope do not."""
import os, re, subprocess, sys, tempfile
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
R = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                 'P15_the_papers_1_06_and_the_joint_fits_1_4967_are_one_curve_in_l_D_and_'
                 'the_one_rate_sizes_are_1_0815_and_1_5238.py')
src = open(R, encoding='utf-8').read()
HERE = os.path.dirname(R)

PROBES = [
    ("P1  the faithful route priced on the HEADER l_D = 1951.9 instead of l_eff -- i.e. the very "
     "mistake the receipt exists to stop",
     "LEFF = (_ldh / _alp ** 0.5) if _m else float('nan')",
     "LEFF = (_ldh) if _m else float('nan')"),
    ("P2  the one-rate move scaled tenfold, leaving every published figure untouched",
     "MV = dm('r7749_leafgeom_nofit_L2000_cr') / dm('cc66_cr_x_h686_L2000_leafrec1_distances') - 1.0",
     "MV = 10.0 * (dm('r7749_leafgeom_nofit_L2000_cr') / dm('cc66_cr_x_h686_L2000_leafrec1_distances') - 1.0)"),
]

ANCHORS = (("HERE = os.path.dirname(os.path.abspath(__file__))", "HERE = %r" % HERE),
           ("ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))", "ROOT = %r" % ROOT))


def run(text):
    # the copy runs from a temp path, so its own HERE/ROOT must be pinned or it resolves nowhere --
    # the defect that killed the r7779 probe, repeated here and fixed the same way
    # FIRST occurrence only: each anchor appears twice in the receipt -- once as its own
    # definition and once inside the rewrite table it applies to the joint-fit source.  A global
    # replace clobbers that table, which is the defect that broke the r7783 probe.
    for old, new in ANCHORS:
        assert text.count(old) == 2, (old, text.count(old))
        text = text.replace(old, new, 1)
    with tempfile.TemporaryDirectory() as td:
        q = os.path.join(td, 'probe.py')
        open(q, 'w', encoding='utf-8').write(text)
        pr = subprocess.run([sys.executable, '-I', q], capture_output=True, text=True,
                            cwd=HERE, timeout=1800)
    out = []
    for ln in pr.stdout.splitlines():
        m = re.match(r'\s*\[(PASS|FAIL)\].*?\*\* (.)', ln)
        if m:
            out.append((m.group(2), m.group(1)))
    return pr.returncode, out

rc0, base = run(src)
print(f'unperturbed: rc={rc0}  ' + ' '.join(f'{g}:{s}' for g, s in base))
for label, old, new in PROBES:
    assert src.count(old) == 1, (label, src.count(old))
    rc, rows = run(src.replace(old, new))
    red = [g for g, s in rows if s == 'FAIL']
    green = [g for g, s in rows if s == 'PASS']
    print(f'\n{label}\n    rc={rc}\n    REDDENS: {" ".join(red) or "(none)"}'
          f'\n    HOLDS:   {" ".join(green) or "(none)"}')
