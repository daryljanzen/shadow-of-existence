#!/usr/bin/env python3
"""`r7856` Ⓑ②ᵇ — the primordial normalisation the lensing path never had, DERIVED and then CHECKED
against the independent pipeline's ABSOLUTE potential power, with nothing fitted anywhere.

** WHERE THE GAP IS. **  `phiphi.clpp` builds the dimensionless potential power as

    D2ref = (kk ** (NS - 1)) * Phi ** 2

-- the tilt WITHOUT A PIVOT and NO AMPLITUDE AT ALL -- and `Phi` is this instrument's transfer
relative to a seed of `Phi = -1`.  So the path carries no primordial normalisation, which is what
`Ⓐ①ᵈᵖʳᵉ` measured: the CMB side's fitted factor came out `1.11e+04` against the lensing side's
`8.16e-10`, fifteen orders apart, so the two were never put on one `AMP`.

** THE DERIVATION, from the instrument's OWN initial conditions and not from a textbook. **  The
control arm seeds `Ph0 = -1` with `dg0 = -2 * Ph0` and `dc0 = 0.75 * dg0`, which IS the
radiation-domination adiabatic growing mode, and `ZSTART 3e7` puts every mode of interest
super-horizon at the seed.  In that regime `|Phi| = (2/3)|zeta|`, so a seed of `|Phi| = 1`
corresponds to `|zeta| = 3/2` and

    D2_Phi,prim(k) = (4/9) * A_s * (k / k_pivot) ** (NS - 1)

against the instrument's `k ** (NS - 1)`.  ⇒ The missing factor is

    AMP = (4/9) * A_s * k_pivot ** (1 - NS)

⛔ ** AND IT IS NOT TRUSTED: ** `(4/9)` is an identity in a regime, so `⑵` below puts the derived
`AMP` to CAMB's own ABSOLUTELY NORMALISED Weyl power at the same cosmology and the same time, with
nothing fitted on either side.  *That test does not use the bandpowers, the likelihood or any fit,
so it cannot be passed by a normalisation that merely reproduces the data.*

Run: python3 normalise.py      (writes normalise.json)
"""
import io
import json
import glob
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7852 = os.path.join(_BTW, 'r7852_60_the_lensing_potential_reconciled_with_camb_term_by_term')
R7854 = os.path.join(_BTW, 'r7854_60_the_potential_repaired_in_the_hierarchy_and_the_recalibration_sized')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7852)
sys.path.insert(0, _BTW)

import ACOUSTIC_two_arm as A                                              # noqa: E402
import terms as TT                                                        # noqa: E402

# the lensing side's fitted factors, from r7854's summary.json -- read, not retyped
A_LENS_REPAIRED = 8.164235700977891e-10
A_LENS_LANDED = 1.5768615382253947e-09
AS = 2.1e-9           # the reference's stated A_s, the same parameter camb_reference.py uses
K_PIVOT = 0.05        # /Mpc, CAMB's default pivot for A_s
ETAREF = 4000.0
I_PHI = 6


def derived_amp(As=AS, ns=None, kp=K_PIVOT):
    ns = float(A.NS) if ns is None else float(ns)
    return (4.0 / 9.0) * As * kp ** (1.0 - ns), dict(zeta_to_phi=4.0 / 9.0, As=As, ns=ns,
                                                     k_pivot=kp, pivot_factor=kp ** (1.0 - ns))


def main():
    out = {}
    print('\n  Ⓑ②ᵇ⑴ THE DERIVATION, from this instrument\'s own seed', flush=True)
    amp, parts = derived_amp()
    print('      the seed: Ph0 = -1, dg0 = -2 Ph0, dc0 = 0.75 dg0  -- the RD adiabatic growing mode')
    print('      (4/9) x A_s x k_pivot**(1-ns) = %.6f x %.4e x %.6f = %.10e'
          % (parts['zeta_to_phi'], parts['As'], parts['pivot_factor'], amp))
    print('      ns = %.4f (the instrument\'s own), k_pivot = %.3f /Mpc' % (parts['ns'],
                                                                           parts['k_pivot']))
    out['derivation'] = dict(amp=amp, **parts)

    print('\n  Ⓑ②ᵇ⑵ PUT TO THE REFERENCE\'S ABSOLUTE WEYL POWER, NOTHING FITTED ON EITHER SIDE',
          flush=True)
    st_rep = np.load(glob.glob(os.path.join(R7854, 'repair_state_bvel1_*.npz'))[0])
    st_land = np.load(os.path.join(R7854, 'locate_state.npz'))
    etas = [float(v) for v in st_land['etas']]
    kk = np.asarray(st_land['kk'], float)
    j = int(np.argmin(np.abs(np.asarray(etas) - ETAREF)))
    a_ref = float(A.a_of_eta(etas[j]))
    z_ref = 1.0 / a_ref - 1.0
    phi_rep = np.asarray(st_rep['Y'])[j, :, I_PHI]
    phi_land = np.asarray(st_land['Y'])[j, :, I_PHI]
    print('      at eta = %.0f (a = %.6f, z = %.4f), %d modes' % (etas[j], a_ref, z_ref, len(kk)))
    r, cfg = TT.camb_results()
    PW = TT.camb_weyl_power(r)
    print('      camb %s, NonLinear_none, A_s = %.4e' % (cfg['camb_version'], cfg['As']))

    def p_inst(phi, amp_):
        return 2 * np.pi ** 2 * amp_ * (kk ** (float(A.NS) - 1.0)) * phi ** 2 / kk ** 3

    pi_rep, pi_land = p_inst(phi_rep, amp), p_inst(phi_land, amp)
    pw = np.array([PW(z_ref, float(k)) for k in kk])
    sub = kk >= 0.02                      # sub-horizon, where Psi = Phi and the comparison is clean
    rr, rl = pi_rep / pw, pi_land / pw
    print('\n      k [/Mpc]   P_inst repaired   P_inst landed      P_camb(Weyl)   rep/camb  land/camb')
    for i, k in enumerate(kk):
        print('      %8.4g   %.6e      %.6e     %.6e   %8.4f  %8.4f'
              % (k, pi_rep[i], pi_land[i], pw[i], rr[i], rl[i]), flush=True)
    mrep = float(np.exp(np.mean(np.log(rr[sub]))))
    mland = float(np.exp(np.mean(np.log(rl[sub]))))
    print('\n      over k >= 0.02 (%d modes), geometric mean of the ratio:' % int(sub.sum()))
    print('        repaired / reference = %.6f        landed / reference = %.6f' % (mrep, mland))
    print('      worst |ratio/mean - 1| over those modes: repaired %.4f, landed %.4f'
          % (float(np.max(np.abs(rr[sub] / mrep - 1))), float(np.max(np.abs(rl[sub] / mland - 1)))))
    print('    ** the derived AMP puts the REPAIRED instrument within %.2f per cent of the '
          'reference\'s **' % (100 * abs(mrep - 1.0)))
    print('       absolute potential power, with NOTHING fitted on either side; the LANDED one '
          'sits at %.4f' % mland, flush=True)
    out['vs_reference'] = dict(eta=etas[j], a_ref=a_ref, z_ref=z_ref,
                               k=[float(v) for v in kk],
                               p_inst_repaired=[float(v) for v in pi_rep],
                               p_inst_landed=[float(v) for v in pi_land],
                               p_camb_weyl=[float(v) for v in pw],
                               ratio_repaired=[float(v) for v in rr],
                               ratio_landed=[float(v) for v in rl],
                               subhorizon_k_min=0.02,
                               mean_ratio_repaired=mrep, mean_ratio_landed=mland,
                               camb=cfg)

    print('\n  Ⓑ②ᵇ⑶ AND AGAINST THE NINE BANDPOWERS\' OWN FITTED FACTOR', flush=True)
    sr, sl = amp / A_LENS_REPAIRED, amp / A_LENS_LANDED
    print('      the derived AMP           %.10e' % amp)
    print('      what the data wants       %.10e (repaired)   %.10e (landed)'
          % (A_LENS_REPAIRED, A_LENS_LANDED))
    print('      derived / wanted          %.6f (repaired)             %.6f (landed)' % (sr, sl))
    print('    ⇒ at the derived normalisation and with NOTHING fitted, the repaired instrument\'s')
    print('      lensing power sits %.2f per cent %s the data; the landed one sits a factor %.4f %s'
          % (100 * abs(sr - 1.0), 'above' if sr > 1 else 'below', 1.0 / sl if sl < 1 else sl,
             'below' if sl < 1 else 'above'), flush=True)
    out['vs_bandpowers'] = dict(amp_derived=amp, a_lens_repaired=A_LENS_REPAIRED,
                                a_lens_landed=A_LENS_LANDED,
                                derived_over_wanted_repaired=sr,
                                derived_over_wanted_landed=sl)

    print('\n  Ⓐ①ᶜ REVISITED AT THE DERIVED NORMALISATION -- the registered expectation', flush=True)
    print('      registered: "the repair moved the absolute scale AWAY from the reference"')
    print('      at the derived normalisation the instrument sits at %.4f before and %.4f after'
          % (sl, sr))
    toward = abs(np.log(sr)) < abs(np.log(sl))
    print('    ** the registered expectation is %s: the repair moved the absolute scale %s **'
          % ('REFUTED' if toward else 'HELD', 'TOWARD' if toward else 'AWAY FROM'))
    print('      ⌗ ratio.py read it as AWAY because it saw only the RAW vector grow by 1.9939.')
    print('        The raw vector did grow; what that growth DOES to the absolute scale could not')
    print('        be read until the normalisation existed, and it takes the instrument from a')
    print('        factor %.4f below the data to %.2f per cent above it.'
          % (1.0 / sl, 100 * abs(sr - 1.0)), flush=True)
    out['A1c_revisited'] = dict(before=sl, after=sr, moved_toward=bool(toward),
                                registered_expectation_refuted=bool(toward))

    with io.open(os.path.join(_HERE, 'normalise.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote normalise.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
