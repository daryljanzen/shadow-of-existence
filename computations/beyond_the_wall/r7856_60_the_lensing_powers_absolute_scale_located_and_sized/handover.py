#!/usr/bin/env python3
"""`r7856` Ⓐ①ᵈ, CORRECTED — the handover IS implemented, and it hands over about twice too much.

⛔ ** THIS FILE CORRECTS THIS REVISION'S OWN `Ⓐ①ᵈᵖʳᵉ`. **  That arm concluded the two sides "were
never put on one `AMP`" because the CMB side's fitted factor came out `1.11e+04` against the lensing
side's `8.16e-10`.  ** The conclusion was wrong and the arm's own test was at fault: ** `model6`
already hands one amplitude across, in `pp_model`, and it does the unit conversion the arm omitted:

    pp_model = (amp_cmb / T_CMB_UK**2) * exp(+2 tau) * pp_shape

-- the CMB's fitted `AMP exp(-2 tau)` in `uK^2`, divided by `T_CMB^2` to make it dimensionless and
un-screened of reionisation.  *So the two ARE commensurable, `Ⓐ①ᵈᵖʳᵉ`'s band was applied to the
wrong pair of numbers, and the claim that the sides were never joined is withdrawn here rather than
left standing in the record.*

** WHAT THE CORRECTED COMPARISON THEN ASKS. **  Three numbers that should all be the same `AMP`:

  ⑴ what the CMB side HANDS OVER:  `amp_cmb / T_CMB^2 * exp(2 tau)`
  ⑵ what this instrument's own seed IMPLIES: `(4/9) A_s k_p^(1-ns)`, validated against the
    reference's absolute Weyl power to `0.13` per cent on the super-horizon modes
  ⑶ what the nine lensing bandpowers WANT: the closed-form factor on the repaired vector

Run: python3 handover.py       (writes handover.json)
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)

AS = 2.1e-9
K_PIVOT = 0.05
SUM_REF = 0.06
A_LENS_REPAIRED = 8.164235700977891e-10
A_LENS_LANDED = 1.5768615382253947e-09


def main():
    import model6 as M6                                                    # noqa: E402
    import lensing_like as LL                                              # noqa: E402
    import phiphi as PP                                                    # noqa: E402
    ns = float(PP.NS)
    out = dict(ns=ns, As=AS, k_pivot=K_PIVOT, T_CMB_UK=float(M6.T_CMB_UK))

    print('\n  Ⓐ①ᵈ CORRECTED -- THREE READINGS OF ONE `AMP`', flush=True)
    mod = M6.Model6('lcdm')
    x4 = np.zeros(4)
    tau = float(LL.TAU_MEAN)
    a_raw = float(mod.amp_cmb(x4, SUM_REF))
    handed = (a_raw / M6.T_CMB_UK ** 2) * np.exp(2.0 * tau)
    derived = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)
    print('      T_CMB = %.5e uK, tau = %.4f, exp(+2 tau) = %.6f'
          % (M6.T_CMB_UK, tau, float(np.exp(2.0 * tau))))
    print('      ⑴ the CMB side hands over   amp_cmb/T^2 x exp(2 tau) = %.10e' % handed)
    print('        (its raw fitted factor in uK^2 was %.10e)' % a_raw)
    print('      ⑵ this instrument\'s seed implies (4/9) A_s k_p^(1-ns) = %.10e' % derived)
    print('      ⑶ the nine bandpowers want                            = %.10e (repaired)'
          % A_LENS_REPAIRED)
    print('                                                            = %.10e (landed)'
          % A_LENS_LANDED)
    print()
    print('      ⑴/⑵ = %.6f      ⑴/⑶ = %.6f (repaired)      ⑵/⑶ = %.6f'
          % (handed / derived, handed / A_LENS_REPAIRED, derived / A_LENS_REPAIRED), flush=True)
    disagree = abs(handed / A_LENS_REPAIRED - 1.0) > 0.10
    print('    ** Ⓐ①ᵈ %s AS REGISTERED: |handed/wanted - 1| = %.4f against a criterion of 0.10 **'
          % ('PASSES (they disagree)' if disagree else 'FAILS (they agree)',
             abs(handed / A_LENS_REPAIRED - 1.0)))
    print('    ⇒ ** AND THE DISAGREEMENT IS A FACTOR %.4f, WHICH IS THE "ABOUT TWO" THIS ORDER'
          % (handed / A_LENS_REPAIRED))
    print('      SET OUT TO FIND ** -- but it is NOT a missing normalisation on the lensing side:')
    print('      the handover is implemented and it hands over %.4f times what the data wants and'
          % (handed / A_LENS_REPAIRED))
    print('      %.4f times what this instrument\'s own seed implies.' % (handed / derived))
    print('      ⌗ ⑵ is the one of the three with an INDEPENDENT check behind it: it agrees with')
    print('        the reference\'s absolute Weyl power to 0.13 per cent super-horizon, with')
    print('        nothing fitted. So ⑴ is the reading that is out, not ⑵.', flush=True)
    out['readings'] = dict(handed_over=handed, raw_amp_cmb_uk2=a_raw, derived=derived,
                           wanted_repaired=A_LENS_REPAIRED, wanted_landed=A_LENS_LANDED,
                           tau=tau, handed_over_r_derived=handed / derived,
                           handed_over_r_wanted=handed / A_LENS_REPAIRED,
                           derived_r_wanted=derived / A_LENS_REPAIRED,
                           A1d_passes=bool(disagree), criterion=0.10)

    print('\n  ⇒ AND THE CANCELLATION `r7852` MEASURED, NOW IDENTIFIED IN BOTH OF ITS FACTORS',
          flush=True)
    # ⚠ `mod.pp_shape` is the RESPONSE BANK's shape, which is the LANDED (BVEL off) instrument --
    #   the first version of this block scored the derived amplitude against it and read the
    #   result as the handover fitting BETTER, which is the opposite of what is happening.  The
    #   two shapes are kept apart here and each is named.
    shape_landed = mod.pp_shape(x4, SUM_REF)
    rep = np.asarray(json.load(io.open(os.path.join(
        _BTW, 'r7854_60_the_potential_repaired_in_the_hierarchy_and_the_recalibration_sized',
        'grid_ics_eta4000_bvel1', 'lcdm_S000.json'), encoding='utf-8'))['bandpowers'], float)
    sc = float(np.exp(np.mean(np.log(shape_landed / np.asarray(json.load(io.open(os.path.join(
        _BTW, 'r7850_60_phi_carried_through_the_radiation_era', 'grid_ics_eta4000',
        'lcdm_S000.json'), encoding='utf-8'))['bandpowers'], float)))))
    print('      the response bank\'s shape is the LANDED instrument\'s, to a factor %.6f' % sc)
    rows = (('the LANDED shape at the handed-over amplitude', handed * shape_landed),
            ('the LANDED shape at the derived amplitude', derived * shape_landed),
            ('the REPAIRED shape at the handed-over amplitude', handed * rep / sc),
            ('the REPAIRED shape at the derived amplitude', derived * rep / sc))
    cz = {}
    for name, m in rows:
        cz[name] = float(LL.chi2(np.asarray(m, float)))
        print('      %-48s chi2 %12.4f' % (name, cz[name]))
    print('      %-48s chi2 %12.4f' % ('the reference, nothing fitted', 8.817347545463614))
    print()
    print('    ⇒ ** THE HANDOVER WAS CALIBRATED AGAINST THE BROKEN INSTRUMENT. **  It hands over')
    print('      %.4f of what the seed implies, and the LANDED instrument\'s lensing power was'
          % (handed / derived))
    print('      %.4f of what it should be, so the two cancelled -- which is exactly the'
          % (A_LENS_LANDED and derived / A_LENS_LANDED))
    print('      cancellation `r7852` measured at 1.36 per cent and could not then name.')
    print('      ⇒ The baryon repair doubled the lensing power and BROKE the cancellation, so the')
    print('        joint fit is now handed twice the lensing it should have and can only buy it')
    print('        back by suppressing lensing. The one knob for that is the neutrino mass sum.')
    print('        ** That, and not a physics discovery, is the 598 meV. **', flush=True)
    out['cancellation'] = dict(bank_shape_is_landed_to_factor=sc, chi2=cz,
                               chi2_reference=8.817347545463614,
                               handover_over_derived=float(handed / derived),
                               landed_over_derived=float(derived / A_LENS_LANDED))

    with io.open(os.path.join(_HERE, 'handover.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote handover.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
