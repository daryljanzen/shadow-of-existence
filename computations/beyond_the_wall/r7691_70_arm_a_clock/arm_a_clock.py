#!/usr/bin/env python3
"""r7691+70 item 1: which clock arm A runs, measured rather than read off a manifest.

Arm A is the low-l receipt's `armA`: stock CAMB, `set_cosmology(H0, ombh2, omch2, mnu=0.06, tau)` and nothing else.
This script (i) lifts `armA`'s CAMBparams construction from the receipt by ast and checks it calls no background or
recombination hook; (ii) builds those params at the distances point and the refit point and compares CAMB's own H(z)
with the two clocks of the arm of record -- the LEAF rate H0 sqrt(Or/a^4+Om/a^3+OL) (Or = 4.1833e-5/h^2) and the
STACKING rate H0 sqrt(Om/a^3+OL) -- at z in [10, 1e5]; (iii) lists what CAMB's python layer offers for the background
and recombination (its model classes and dark-energy classes). Writes `arm_a_clock.json`. Nothing is banked.
"""
import ast
import json
import os

import camb
import camb.dark_energy as de
import camb.recombination as rc
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
RECEIPT = os.path.join(ROOT, 'receipts', 'P15_CR_cosmology',
                       'P15_the_low_multipole_depth_gap_closes_and_two_defects_were_cancelling.py')

fn = next(n for n in ast.parse(open(RECEIPT, encoding='utf-8').read()).body
          if isinstance(n, ast.FunctionDef) and n.name == 'armA')
calls = sorted({ast.unparse(c.func) for c in ast.walk(fn) if isinstance(c, ast.Call)})
attrs = sorted({ast.unparse(t) for a in ast.walk(fn) if isinstance(a, ast.Assign) for t in a.targets
                if isinstance(t, ast.Attribute)})
HOOKS = ('Recomb', 'DarkEnergy', 'Reion', 'set_dark_energy', 'num_nu_massless', 'set_classes', 'recombination_model')
res = {'armA_calls': calls, 'armA_attribute_assignments': attrs,
       'armA_touches_background_or_recombination': [h for h in HOOKS if any(h in s for s in calls + attrs)]}

ZS = [10, 100, 1100, 3000, 1e4, 1e5]
for label, (H0, Om, wb) in (('distances', (68.60, 0.2973, 0.02237)), ('refit', (68.57073, 0.291246, 0.021643))):
    h = H0 / 100
    p = camb.CAMBparams()
    p.set_cosmology(H0=H0, ombh2=wb, omch2=Om * h * h - wb - 0.06 / 93.14, mnu=0.06, tau=0.0544)
    bg = camb.get_background(p)
    Or, OL = 4.1833e-5 / h ** 2, 1 - Om
    rows = []
    for z in ZS:
        Hc = float(bg.hubble_parameter(z))
        Hl = H0 * np.sqrt(Or * (1 + z) ** 4 + Om * (1 + z) ** 3 + OL)
        Hs = H0 * np.sqrt(Om * (1 + z) ** 3 + OL)
        rows.append(dict(z=z, camb_over_leaf=round(Hc / Hl, 5), camb_over_stacking=round(Hc / Hs, 5)))
    res[label] = dict(rows=rows, recombination_model=type(p.Recomb).__name__,
                      dark_energy_model=type(p.DarkEnergy).__name__)
res['camb_version'] = camb.__version__
res['camb_recombination_classes'] = sorted(n for n in dir(rc) if isinstance(getattr(rc, n), type)
                                           and issubclass(getattr(rc, n), rc.RecombinationModel))
res['camb_dark_energy_classes'] = sorted(n for n in dir(de) if isinstance(getattr(de, n), type)
                                         and issubclass(getattr(de, n), de.DarkEnergyModel))
json.dump(res, open(os.path.join(HERE, 'arm_a_clock.json'), 'w'), indent=1)
print(json.dumps(res, indent=1))
