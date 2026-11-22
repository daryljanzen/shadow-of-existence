#!/usr/bin/env python3
"""`r7856` Ⓓ④ᵃ — WHICH SIDE carries the factor two, measured against the reference and not by
elimination.

`handover.py` established that the amplitude the CMB side hands the lensing side is `1.9829` times
what this instrument's own seed implies, and that the seed's figure is the one with an independent
check behind it.  ⇒ By elimination the factor sits on the CMB side.  **Elimination is not a
measurement**, so this file puts the CMB side itself to the reference.

** THE TEST. **  `model6.amp_cmb` fits `AMP exp(-2 tau)` on the instrument's own binned TT/TE/EE
against `plik_lite`.  If the CMB bank's vector is built from the same `Phi = -1` seed and carries no
normalisation, that fitted number -- converted as `pp_model` converts it -- must equal the derived
`AMP`.  It does not.  So either the bank's vector is low by that factor, or the conversion is.
Both are checkable against CAMB's own TT at the same cosmology:

  ⑴ CAMB's `D_l^TT` at `A_s = 2.1e-9`, binned through the harness's own `plik_lite` windows
  ⑵ the instrument's binned TT at the control's centre, times the DERIVED `AMP` and `T_CMB^2` and
    `exp(-2 tau)` -- i.e. what the bank predicts absolutely if the seed's normalisation is right

⇒ If `⑵/⑴` comes out near `0.5`, the CMB BANK is low by two and the lensing side is sound.
  If it comes out near `1`, the bank is right and the factor is in the conversion.

⌗ ** TT ONLY, and only over the bins the bank covers **, because the question is a normalisation and
TT is where the data is strongest; the polarisation blocks share the same one amplitude by
construction and cannot answer a different question.

Run: python3 cmb_side.py        (writes cmb_side.json)
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
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
sys.path.insert(0, R7842)

import camb                                                               # noqa: E402
from camb import model as camb_model                                      # noqa: E402

AS = 2.1e-9
K_PIVOT = 0.05
SUM_REF = 0.06
H0, OM, WB, NS_P, TAU = 67.40, 0.3150, 0.0224, 0.965, 0.054


def main():
    import model6 as M6                                                    # noqa: E402
    import score_ttteee as SC                                              # noqa: E402
    import phiphi as PP                                                    # noqa: E402
    ns = float(PP.NS)
    AMP = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)
    out = dict(amp_derived=AMP, ns=ns, As=AS)

    print('\n  Ⓓ④ᵃ WHICH SIDE CARRIES THE FACTOR TWO -- measured, not inferred', flush=True)
    mod = M6.Model6('lcdm')
    x4 = np.zeros(4)
    m_bank = np.asarray(mod.cmb.binned(x4, SUM_REF), float)
    a_raw = float(mod.amp_cmb(x4, SUM_REF))

    h = H0 / 100.0
    omch2 = (OM - WB / h ** 2) * h ** 2 - SUM_REF / 93.14
    p = camb.set_params(H0=H0, ombh2=WB, omch2=omch2, mnu=SUM_REF, tau=TAU, ns=ns, As=AS,
                        lmax=2600, WantTransfer=True)
    p.NonLinear = camb_model.NonLinear_none
    r = camb.get_results(p)
    # ⚠ `total` is the LENSED spectrum, which is what plik_lite measures; `unlensed_total` is not.
    cl = r.get_cmb_power_spectra(p, CMB_unit='muK', spectra=['total'])['total']
    ls = np.arange(cl.shape[0])
    with np.errstate(divide='ignore', invalid='ignore'):
        Dl_tt = cl[:, 0]            # already D_l = l(l+1)C_l/2pi in uK^2 with CMB_unit='muK'
    print('      camb %s, A_s = %.4e, lmax 2600, lensed `total`' % (camb.__version__, AS))

    # bin CAMB through the harness's own windows, TT block only
    lsx = np.arange(2, 2601)
    dl = np.interp(lsx, ls, np.nan_to_num(Dl_tt))
    b_camb = SC.bin_three(lsx, dl, np.zeros_like(dl), np.zeros_like(dl))
    tt = (SC.BLOCK == 0) & mod.cmb.ok
    keep = tt[mod.cmb.ok] if b_camb.shape[0] == SC.BLOCK.shape[0] else None
    bc = np.asarray(b_camb, float)[tt]
    # the bank's own TT bins, in the same order
    mb_full = np.full(SC.BLOCK.shape[0], np.nan)
    mb_full[mod.cmb.ok] = m_bank
    mbank_tt = mb_full[tt]
    good = np.isfinite(bc) & np.isfinite(mbank_tt) & (bc != 0)
    pred = AMP * (M6.T_CMB_UK ** 2) * np.exp(-2.0 * TAU) * mbank_tt[good]
    ratio = pred / bc[good]
    gm = float(np.exp(np.mean(np.log(np.abs(ratio)))))
    print('      %d TT bins compared' % int(good.sum()))
    print('      the bank x derived AMP x T^2 x exp(-2 tau), over CAMB\'s own binned TT:')
    print('        geometric mean %.6f, range %.6f .. %.6f' % (gm, float(np.min(ratio)),
                                                               float(np.max(ratio))))
    print('      the handover\'s own reading was %.6f of the derived AMP'
          % (a_raw / (M6.T_CMB_UK ** 2) * np.exp(2.0 * TAU) / AMP), flush=True)
    near_half = abs(gm - 0.5) < 0.15
    near_one = abs(gm - 1.0) < 0.15
    print()
    if near_half:
        print('    ** THE CMB BANK IS LOW BY ABOUT TWO, and the lensing side is sound. **')
    elif near_one:
        print('    ** THE CMB BANK IS RIGHT, so the factor is in the CONVERSION and not the bank. **')
    else:
        print('    ** NEITHER: the ratio is %.4f, which is not near a half or a one, so this file'
              % gm)
        print('       does NOT name the carrier and says so rather than picking the nearer. **')
    out['tt_absolute'] = dict(n_bins=int(good.sum()), geometric_mean=gm,
                              ratio_min=float(np.min(ratio)), ratio_max=float(np.max(ratio)),
                              handover_over_derived=float(a_raw / (M6.T_CMB_UK ** 2)
                                                          * np.exp(2.0 * TAU) / AMP),
                              bank_low_by_about_two=bool(near_half),
                              bank_is_right=bool(near_one),
                              carrier_named=bool(near_half or near_one),
                              camb_version=camb.__version__, lensed='total')

    with io.open(os.path.join(_HERE, 'cmb_side.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote cmb_side.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
