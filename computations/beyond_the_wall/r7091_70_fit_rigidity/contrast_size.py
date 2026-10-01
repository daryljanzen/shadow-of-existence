"""r7091 (70), post-hoc and declared so: the size and sign of the contrast change the data ask for, per arm --
the coefficient c on the contrast template once the five declared directions are fitted, i.e. the
oscillatory part of the spectrum scaled by (1 + c)."""
import sys
import numpy as np
sys.argv = [sys.argv[0], '--mc', '1']
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()):
    import rigidity as R
for arm in ('lcdm', 'cr'):
    B = R.build(arm)
    cols = [B['m0'] * 0.02] + [B['g'][k] * R.STEP[k] for k in R.STEP] + [B['contrast']]
    Jw = np.column_stack([R.W(B, c) for c in cols])
    y = R.W(B, B['d'] - B['m0'])
    x, *_ = np.linalg.lstsq(Jw, y, rcond=None)
    F = Jw.T @ Jw
    err = np.sqrt(np.diag(np.linalg.inv(F)))
    print(f'{arm:5s}  contrast scaled by (1 + c):  c = {x[-1]:+.4f} +- {err[-1]:.4f}  ({x[-1] / err[-1]:+.1f} sigma)')
