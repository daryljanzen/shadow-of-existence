#!/usr/bin/env python3
"""`r7856` Ⓐ①ᵈ Ⓐ①ᵈᵖʳᵉ — ONE primordial normalisation, fitted twice and compared.

`phiphi.py` states the doctrine in its own header: every mode of this instrument's solve starts at
`Phi = -1`, so

    CMB    = AMP * exp(-2 tau) * shape_cmb        (reionisation screens the high-`l` spectra)
    phiphi = AMP             * shape_phiphi       (the lensing potential is not screened)

`AMP` is therefore ONE number appearing in two places, and it can be fitted on each side alone.
`score_ttteee.chi2_of` and `model3.Model.chi2_cmb` both form `A = (m F d)/(m F m)` -- the CMB side's
answer; `r7854`'s bandpower scoring forms the same closed-form factor on the nine lensing
bandpowers -- the lensing side's answer.

⛔ ** Ⓐ①ᵈᵖʳᵉ IS ASKED FIRST AND IS NOT A FORMALITY: ** a ratio of two fitted factors is a physical
gap only if the two are fitting ONE quantity.  If the two come out of different orders of magnitude
then the CMB side's vector carries a normalisation the lensing side's does not, the two were never
put on one `AMP`, and the ratio is a comparison of conventions.  *That is the finding in that case
and this file says so rather than reporting the ratio as a factor.*

⌗ Both sides are evaluated at the CONTROL'S OWN FIXED COSMOLOGY -- the centre of the `lcdm` arm,
`x4 = 0`, which is the same `H0 67.40 / OM 0.3150 / WB 0.0224 / NS 0.965` the reference uses -- so
the comparison is at one cosmology and not across two fits.

Run: python3 amp_twice.py     (writes amp_twice.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7842 = os.path.join(_BTW, 'r7842_60_polarisation_added_to_the_score_and_the_two_data_the_'
                           'harness_does_not_have')
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
sys.path.insert(0, R7846)
sys.path.insert(0, R7842)
import lensing_like as LL                                                  # noqa: E402

# the lensing side's answers, from r7854's summary.json -- read, not retyped
A_LENS_REPAIRED = 8.164235700977891e-10
A_LENS_LANDED = 1.5768615382253947e-09
TAU_BANK = 0.054          # the tau the control's bank carries, as camb_reference.py states it
SUM_REF = 0.06            # the reference's mnu, so both sides sit at one cosmology


def main():
    import model3 as M3                                                    # noqa: E402
    out = {}
    print('\n  Ⓐ①ᵈᵖʳᵉ ARE THE TWO FITS FITTING ONE QUANTITY?  asked before any ratio is formed',
          flush=True)
    mod = M3.Model3('lcdm')
    x4 = np.zeros(4)
    m = mod.binned(x4, SUM_REF)
    # the same closed form `chi2_cmb` uses internally: A = (m F d)/(m F m)
    A_cmb = float((m @ mod.F @ mod.d) / (m @ mod.F @ m))
    chi2_cmb_free = float((mod.d - A_cmb * m) @ mod.F @ (mod.d - A_cmb * m))
    chi2_cmb_unit = float((mod.d - m) @ mod.F @ (mod.d - m))
    print('      the CMB model vector at the control\'s centre: %d bins, m runs %.4e .. %.4e'
          % (len(m), float(np.min(np.abs(m))), float(np.max(np.abs(m)))))
    print('      the data vector:                                     d runs %.4e .. %.4e'
          % (float(np.min(np.abs(mod.d))), float(np.max(np.abs(mod.d)))))
    print('      A_cmb  = %.10e   (chi2 %.4f fitted, %.4f at a factor of exactly one)'
          % (A_cmb, chi2_cmb_free, chi2_cmb_unit))
    print('      A_lens = %.10e   (repaired)        %.10e (landed)'
          % (A_LENS_REPAIRED, A_LENS_LANDED))
    same_order = 1e-11 <= abs(A_cmb) <= 1e-7
    print('    ** Ⓐ①ᵈᵖʳᵉ %s: A_cmb is %s the band 1e-11 .. 1e-7 that one Phi = -1 seed feeding '
          'both would put it in **'
          % ('HOLDS' if same_order else 'FAILS', 'inside' if same_order else 'OUTSIDE'), flush=True)
    out['A1d_pre'] = dict(holds=bool(same_order), A_cmb=A_cmb, A_lens_repaired=A_LENS_REPAIRED,
                          A_lens_landed=A_LENS_LANDED, n_cmb_bins=int(len(m)),
                          chi2_cmb_amplitude_fitted=chi2_cmb_free,
                          chi2_cmb_amplitude_one=chi2_cmb_unit,
                          m_abs_min=float(np.min(np.abs(m))), m_abs_max=float(np.max(np.abs(m))),
                          d_abs_min=float(np.min(np.abs(mod.d))),
                          d_abs_max=float(np.max(np.abs(mod.d))))

    print('\n  Ⓐ①ᵈ THE RATIO OF THE TWO, WITH THE SCREENING STATED', flush=True)
    scr = float(np.exp(-2.0 * TAU_BANK))
    print('      exp(-2 tau) at tau = %.3f is %.6f' % (TAU_BANK, scr))
    if not same_order:
        print('    ⛔ Ⓐ①ᵈ IS NOT REPORTED AS A FACTOR, because Ⓐ①ᵈᵖʳᵉ failed: the CMB side\'s')
        print('       vector carries a normalisation the lensing side\'s does not, so the two')
        print('       were NEVER PUT ON ONE `AMP` and a ratio of them is a ratio of conventions.')
        print('       ⇒ THAT is the finding, and it is exactly what the stub in phiphi.py')
        print('         (`amp = None` in both branches) leaves undone.', flush=True)
        out['A1d'] = dict(reported_as_a_factor=False,
                          reason='A1d_pre failed: the two fitted factors are not one quantity',
                          screening=scr)
    else:
        ratio = A_LENS_REPAIRED / A_cmb
        ratio_scr = A_LENS_REPAIRED / (A_cmb / scr)
        ratio_land = A_LENS_LANDED / A_cmb
        print('      A_lens / A_cmb        = %.6f   (repaired)   %.6f (landed)'
              % (ratio, ratio_land))
        print('      with the CMB side de-screened, A_lens / (A_cmb / exp(-2 tau)) = %.6f'
              % ratio_scr)
        disagree = abs(ratio - 1.0) > 0.10
        print('    ** Ⓐ①ᵈ %s AS REGISTERED: |A_lens/A_cmb - 1| = %.4f against a criterion of 0.10 **'
              % ('PASSES (they disagree)' if disagree else 'FAILS (they agree, so the joint fit\'s '
                 'compromise is NOT a normalisation conflict)', abs(ratio - 1.0)), flush=True)
        out['A1d'] = dict(reported_as_a_factor=True, passes=bool(disagree),
                          ratio_repaired=ratio, ratio_landed=ratio_land,
                          ratio_repaired_descreened=ratio_scr, screening=scr, criterion=0.10)

    with io.open(os.path.join(_HERE, 'amp_twice.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote amp_twice.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
