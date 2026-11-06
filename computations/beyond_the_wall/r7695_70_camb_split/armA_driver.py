#!/usr/bin/env python3
"""r7695+70 step 2: run the low-l receipt's own `armA` (lifted by ast, unaltered) against a chosen CAMB build.

Usage: CAMB_DIR=<dir holding the camb package> python3 armA_driver.py H0 Om ombh2 [extra_json]
`extra_json` is a JSON object of CAMBparams attributes set after `set_cosmology` (for the fork's switch); `armA`
is wrapped so the attributes are applied inside it, at the same point in the construction for every build.
Prints one line: __A__ {"camb_file": ..., "ells": [...], "depths": [...], "H1100": ..., "chi_star": ...}
"""
import ast
import json
import os
import sys

sys.path.insert(0, os.environ['CAMB_DIR'])
import camb  # noqa: E402
import numpy as np  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')
H0, Om, wb = (float(x) for x in sys.argv[1:4])
EXTRA = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}

tree = ast.parse(open(RECEIPT, encoding='utf-8').read())
keep = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))
        or (isinstance(n, ast.FunctionDef) and n.name in ('armA', 'r0_of'))
        or (isinstance(n, ast.Assign) and any(getattr(t, 'id', None) in ('C', 'NS', 'LMAX') for t in n.targets))]
A = {'__name__': 'armA_lift', '__file__': RECEIPT}
exec(compile(ast.Module(body=keep, type_ignores=[]), RECEIPT + '[armA]', 'exec'), A)
assert A['camb'] is camb, 'the lifted armA must use the CAMB build on CAMB_DIR'

_orig = camb.CAMBparams.set_cosmology


def _set(self, *a, **k):
    r = _orig(self, *a, **k)
    for key, val in EXTRA.items():
        setattr(self, key, val)
    return r


camb.CAMBparams.set_cosmology = _set
e, r = A['armA'](H0, Om, ombh2=wb)
d = dict(zip((int(x) for x in e), (float(x) for x in r)))
h = H0 / 100
p = camb.CAMBparams()
p.set_cosmology(H0=H0, ombh2=wb, omch2=Om * h * h - wb - 0.06 / 93.14, mnu=0.06, tau=0.0544)
res = camb.get_results(p)
print('__A__' + json.dumps(dict(camb_file=camb.__file__, version=camb.__version__, ells=list(range(2, 9)),
                                depths=[d[l] for l in range(2, 9)],
                                H1100=float(res.hubble_parameter(1100.0)),
                                chi_star=float(res.comoving_radial_distance(res.get_derived_params()['zstar'])))))
