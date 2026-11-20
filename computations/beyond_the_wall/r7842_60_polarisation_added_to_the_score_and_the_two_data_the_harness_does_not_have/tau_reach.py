"""r7842+60: WHAT A tau PRIOR CAN DO IN THIS HARNESS -- measured, not assumed.

On order r7841 (69) item ③, which asks for the low-`l` and optical-depth information "or a `tau`
prior equivalent to it, and say which".  The low-`l` half is a data question and is answered by the
repository: `use_low_ell_bins=True` reads a file that is not banked.  The `tau` half is NOT a data
question -- it is a question about this harness's reach, and it is answerable here.

** THE CLAIM TO BE TESTED, STATED BEFORE TESTING IT. **  A `tau` prior constrains NOTHING in this
harness, for two independent reasons:

  (a) the score solves ONE overall amplitude ANALYTICALLY at every point, so the uniform
      `exp(-2 tau)` suppression that `tau` applies to the whole spectrum is EXACTLY degenerate with
      it -- not approximately, exactly, because the amplitude is a closed-form quotient;
  (b) the instrument's visibility carries RECOMBINATION ONLY and no reionisation, so there is no
      low-`l` E-mode bump for `tau` to move, which is the one place `tau` is not degenerate with
      the amplitude in a real analysis.

Both are checked: (a) numerically, by scaling all three spectra by a constant and comparing chi^2
to the last bit; (b) by reading the instrument's own source for a reionisation term.

rc=0 on success.  Writes tau_reach.json.
"""
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
BW = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import score_ttteee as SC                                                  # noqa: E402

POL = os.environ.get('POL_DIR', '/tmp/claude-0/pol_grid')
OUT = os.path.join(HERE, 'tau_reach.json')


def main():
    z = np.load(os.path.join(POL, 'lcdm_S000.npz'), allow_pickle=True)
    ls = np.asarray(z['ls'], float)
    tt, te, ee = (np.asarray(z[k], float) for k in ('Dl', 'Dl_TE', 'Dl_EE'))
    base = SC.chi2_of(ls, tt, te, ee)
    rows = {}
    # (a) a uniform suppression is exactly what exp(-2 tau) is; tau = 0.02 .. 0.10 spans the
    #     published range and then some, and the factor is applied to all three spectra alike
    worst = 0.0
    for tau in (0.02, 0.0544, 0.10, 0.20):
        f = np.exp(-2.0 * tau) / np.exp(-2.0 * 0.054)
        c = SC.chi2_of(ls, tt * f, te * f, ee * f)
        rows[f'{tau:.4f}'] = dict(factor=float(f), chi2=c[0], amplitude=c[2],
                                  dchi2=c[0] - base[0])
        worst = max(worst, abs(c[0] - base[0]))
        print('  tau = %.4f -> factor %.6f : chi2 %.10f, amplitude %.6e, dchi2 %+.3e'
              % (tau, f, c[0], c[2], c[0] - base[0]), flush=True)
    # (b) the instrument's own source: is there a reionisation term in the visibility at all?
    src = io.open(os.path.join(BW, 'ACOUSTIC_two_arm.py'), encoding='utf-8').read()
    words = {w: src.lower().count(w) for w in ('reionis', 'reioniz', 'xe_reion', 'zreio', 'tau_reio')}
    print('\n  the instrument\'s source, counted: %s' % json.dumps(words))
    json.dump(dict(baseline=dict(chi2=base[0], nbins=base[1], amplitude=base[2]),
                   uniform_suppression=rows, worst_abs_dchi2=worst,
                   reionisation_words=words), open(OUT, 'w'), indent=1)
    print(f'\n  worst |dchi2| over the whole tau range: {worst:.3e}')
    print(f'  wrote {os.path.relpath(OUT, HERE)}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
