"""Ⓔ⑤: does the initial-condition repair move the ABSOLUTE normalisation toward one?

`r7848` held `(A_cmb / T_CMB^2) e^{+2 tau} = 1.617967e-09` against the nine bandpowers' own
preferred `1.471643e-09`, a ratio of `0.909563`, with nothing fitted to them.  The held number comes
from the CMB fit and does NOT depend on which growth carries `Phi` forward, so the repair can only
move the PREFERRED one -- and `shape_sensitivity` measured that move directly, as the change in the
amplitude the nine bandpowers want for this instrument's vector.

The arm registered that the ratio moves TOWARD `1`, with the reachable negative that it moves away.

⌗ And CAMB is in the table beside it, because this revision found it installed: at a stated
`A_s` it wants an amplitude of `1.002494` with nothing fitted, which says the absolute normalisation
of these bandpowers is reachable to a quarter of a per cent by a pipeline that is not this one.

Run: python3 normalisation.py          (writes normalisation.json)
"""
import io
import json
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
R7846 = os.path.join(os.path.dirname(_HERE),
                     'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')


def j(p):
    return json.load(io.open(p, encoding='utf-8'))


def main():
    info = j(os.path.join(R7846, 'lensing_informative.json'))
    sens = j(os.path.join(_HERE, 'shape_sensitivity.json'))
    camb = j(os.path.join(_HERE, 'camb_reference.json'))

    held = float(info['amp_held'])
    pref_old = float(info['amp_preferred_by_bandpowers'])
    ratio_old = float(info['amp_ratio_preferred_over_cmb'])
    change = float(sens['difference']['amplitude_change_relative'])
    pref_new = pref_old * (1.0 + change)
    ratio_new = pref_new / held

    toward_one = abs(ratio_new - 1.0) < abs(ratio_old - 1.0)
    out = dict(held=held, preferred_r7848=pref_old, ratio_r7848=ratio_old,
               amplitude_change_relative=change, preferred_r7850=pref_new,
               ratio_r7850=ratio_new,
               miss_r7848_pc=100.0 * (1.0 - ratio_old), miss_r7850_pc=100.0 * (1.0 - ratio_new),
               moves_toward_one=bool(toward_one),
               held_does_not_depend_on_the_growth=True,
               camb_amplitude_with_nothing_fitted=float(camb['fitted_amplitude']),
               camb_As=float(camb['config']['As']),
               camb_chi2_nothing_fitted=float(camb['chi2_nothing_fitted']))
    print('\n  Ⓔ⑤: the absolute normalisation, held against what the bandpowers prefer\n')
    print('  held (from the CMB fit, independent of the growth):   %.6e' % held)
    print('  preferred, r7848 growth from the quadrature:          %.6e   ratio %.6f  (%.2f per '
          'cent low)' % (pref_old, ratio_old, out['miss_r7848_pc']))
    print('  preferred, r7850 growth from the instrument:          %.6e   ratio %.6f  (%.2f per '
          'cent low)' % (pref_new, ratio_new, out['miss_r7850_pc']))
    print('\n  ⇒ Ⓔ⑤ %s: the ratio moves %s one.'
          % ('HOLDS' if toward_one else 'FAILS', 'TOWARD' if toward_one else 'AWAY FROM'))
    print('\n  ⌗ and for scale, CAMB at a stated A_s = %.3e wants an amplitude of %.6f with nothing'
          '\n     fitted, at chi^2 %.4f on nine bins -- so this normalisation is reachable to a '
          'quarter\n     of a per cent by a pipeline that is not this one.'
          % (out['camb_As'], out['camb_amplitude_with_nothing_fitted'],
             out['camb_chi2_nothing_fitted']))
    with io.open(os.path.join(_HERE, 'normalisation.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote normalisation.json\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
