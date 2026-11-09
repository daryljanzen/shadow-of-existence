#!/usr/bin/env python3
"""`r7719+cc66` CAN THE NAMED BUILD EVEN WORK? — measured before it is named.

The step fails because one side of it rests on half an independent window.  The obvious replacement is
to stop using a step and fit the two mechanisms as TEMPLATES to the whole curve, which uses every band
centre instead of two group means.

⛔ BUT A TEMPLATE FIT SEPARATES TWO MECHANISMS ONLY IF THEIR TEMPLATES ARE NOT PARALLEL.  If the
   kernel-held and source-held difference curves are nearly collinear, no estimator whatever separates
   them, and the route is closed for a GEOMETRIC reason rather than a statistical one -- which is a
   stronger and more useful finding than "not resolved".  So that is measured here, before the build is
   named, and the naming follows the number instead of preceding it.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', 'r7717_cc66_the_calibrated_estimator')))
import calibrate_and_read as C                                               # noqa: E402

real = C.load_real()
rep = {}
print("\n  ⛭ THE TWO MECHANISMS' TEMPLATES, AND WHETHER THEY ARE PARALLEL")
print("     templates in q on the control's own grid, each the log-ratio of a single swap:")
qd, yd = real['lcdm|lcdm']
on = lambda k: np.interp(qd, real[k][0], real[k][1])
t_ker = np.log(on('cr|lcdm') / yd)        # kernel swapped, source held
t_src = np.log(on('lcdm|cr') / yd)        # source swapped, kernel held
t_own = np.log(on('cr|cr') / yd)          # both
for nm, t in (('kernel-held', t_ker), ('source-held', t_src), ('own x own', t_own)):
    print(f"       {nm:12s}  mean {t.mean():+.5f}  sd {t.std(ddof=1):.5f}  "
          f"range {t.min():+.4f} .. {t.max():+.4f}")
# the overlap after removing each template's mean -- a mean offset separates trivially and is not
# what the discrimination turns on
a, b = t_ker - t_ker.mean(), t_src - t_src.mean()
corr = float(np.corrcoef(a, b)[0, 1])
cos = float(a @ b / np.sqrt((a @ a) * (b @ b)))
# the condition number of the 2x2 design matrix: how ill-posed the two-amplitude fit is
X = np.column_stack([a, b])
sv = np.linalg.svd(X, compute_uv=False)
cond = float(sv[0] / sv[-1])
print(f"\n       correlation of the two templates (means removed): {corr:+.4f}")
print(f"       cosine of the angle between them:                 {cos:+.4f}")
print(f"       condition number of the two-amplitude design:     {cond:.2f}")
print(f"       ⇒ variance inflation of each amplitude: {1.0 / (1.0 - cos ** 2):.2f}x")
rep.update(corr=corr, cos=cos, cond=cond, vif=1.0 / (1.0 - cos ** 2))
# and what the fit would give on the measured contrast
coef, *_ = np.linalg.lstsq(X, t_own - t_own.mean(), rcond=None)
print(f"\n       the two amplitudes the fit returns on the measured contrast: "
      f"kernel {coef[0]:+.4f}, source {coef[1]:+.4f}")
print(f"       (an exact linear decomposition would give 1 and 1; the departure is the interaction)")
rep['amplitudes'] = [float(coef[0]), float(coef[1])]
near_parallel = abs(cos) > 0.9
print(f"\n  ⇒ the templates are {'⛔ NEARLY PARALLEL' if near_parallel else 'WELL SEPARATED'}, so a "
      f"two-amplitude fit {'CANNOT' if near_parallel else 'CAN'} separate them")
rep['near_parallel'] = bool(near_parallel)
json.dump(rep, open(os.path.join(HERE, 'can_a_template_fit_separate_them.json'), 'w'), indent=1)
