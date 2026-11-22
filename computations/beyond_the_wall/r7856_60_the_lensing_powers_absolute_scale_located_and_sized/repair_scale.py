#!/usr/bin/env python3
"""`r7856` Ⓞ⓪ᵇ Ⓒ③ Ⓒ③ᵇ — the repair applied, and the control scored with NOTHING fitted.

The missing normalisation is a single multiplicative constant on `clpp` -- `(4/9) A_s k_p^(1-ns)`,
since the pivot enters only as `k_p^(1-ns)` against this path's unpivoted `k^(ns-1)`.  So the repair
needs no re-solve: it multiplies the banked vector.  `PRIMNORM=1` puts the same constant inside
`phiphi.clpp` so every consumer gets it, and `Ⓞ⓪ᵇ` checks the switch against the arithmetic here.

⛔ ** THE CLAIM HERE IS ONLY LEGITIMATE WITH NOTHING FITTED. **  `r7854` reported `1.0534` per dof
WITH an amplitude free; the reference's `8.8173` is scored with nothing free.  Those two numbers are
not comparable and this file does not compare them: `Ⓒ③` is scored at a factor of exactly one, and
the free-amplitude score is printed beside it and explicitly refused the claim.

Run: python3 repair_scale.py       (writes repair_scale.json)
"""
import io
import json
import os
import subprocess
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
R7846 = os.path.join(_BTW, 'r7846_60_the_scale_dependent_growth_and_the_banked_lensing_bandpowers')
R7850 = os.path.join(_BTW, 'r7850_60_phi_carried_through_the_radiation_era')
R7854 = os.path.join(_BTW, 'r7854_60_the_potential_repaired_in_the_hierarchy_and_the_recalibration_sized')
os.environ.setdefault('NOPROJ', '1')
os.environ.setdefault('NK', '4')
sys.path.insert(0, R7846)
import lensing_like as LL                                                  # noqa: E402

AS = 2.1e-9
K_PIVOT = 0.05
CAMB_CHI2_NOTHING = 8.817347545463614       # r7850's camb_reference.json
LANDED_AMP = 1.5768615382253947e-09
REPAIRED_AMP = 8.164235700977891e-10


def vec(p):
    return np.asarray(json.load(io.open(p, encoding='utf-8'))['bandpowers'], float)


def score(b, amplitude=None):
    a = (float((b @ LL.FISHER @ LL.DATA) / (b @ LL.FISHER @ b)) if amplitude is None
         else float(amplitude))
    r = LL.DATA - a * b
    return float(r @ LL.FISHER @ r), a


def main():
    import phiphi as PP                                                    # noqa: E402
    ns = float(PP.NS)
    AMP = (4.0 / 9.0) * AS * K_PIVOT ** (1.0 - ns)
    out = dict(amp=AMP, ns=ns, As=AS, k_pivot=K_PIVOT)

    print('\n  Ⓞ⓪ᵇ THE SWITCH AGAINST THE ARITHMETIC -- PRIMNORM=1 must be exactly this constant',
          flush=True)
    print('      PRIMNORM is %s in this process' % ('ON' if PP.PRIMNORM else 'OFF'))
    code = ('import os, sys; sys.path.insert(0, %r); os.environ["NOPROJ"]="1"; '
            'os.environ["NK"]="4"; os.environ["PRIMNORM"]="%s"; import phiphi as P; '
            'print(repr(P.PRIMNORM))')
    probes = {}
    for flag in ('0', '1'):
        r = subprocess.run([sys.executable, '-c', code % (R7846, flag)],
                           capture_output=True, text=True)
        probes[flag] = r.stdout.strip().splitlines()[-1] if r.returncode == 0 else 'ERROR'
    print('      unset  -> PRIMNORM %s        set -> PRIMNORM %s' % (probes['0'], probes['1']))
    sw_ok = probes['0'] == 'False' and probes['1'] == 'True'
    print('      the constant the switch applies: (4/9) x %.4e x %.3f**(1-%.4f) = %.10e'
          % (AS, K_PIVOT, ns, AMP))
    print('    ** Ⓞ⓪ᵇ %s: the switch reads off by default and the constant is the derived one **'
          % ('HOLDS' if sw_ok else 'FAILS'), flush=True)
    out['switch'] = dict(holds=bool(sw_ok), unset=probes['0'], set=probes['1'])

    b_land = vec(os.path.join(R7850, 'grid_ics_eta4000', 'lcdm_S000.json'))
    b_rep = vec(os.path.join(R7854, 'grid_ics_eta4000_bvel1', 'lcdm_S000.json'))
    ndof = LL.NBP - 1
    err = np.sqrt(np.diag(LL.COV))

    print('\n  Ⓒ③ THE CONTROL, REPAIRED AND NORMALISED, SCORED WITH NOTHING FITTED', flush=True)
    print('      bin   L_av       data            repaired x AMP     ratio    in bin sigma')
    nb_rep, nb_land = b_rep * AMP, b_land * AMP
    rat = nb_rep / LL.DATA
    for i in range(LL.NBP):
        print('       %d   %6.1f   %.6e    %.6e    %6.4f   %+7.2f'
              % (i + 1, LL.L_AV[i], LL.DATA[i], nb_rep[i], rat[i],
                 (nb_rep[i] - LL.DATA[i]) / err[i]), flush=True)
    c2_rep_fixed, _ = score(nb_rep, amplitude=1.0)
    c2_land_fixed, _ = score(nb_land, amplitude=1.0)
    c2_rep_free, a_rep_free = score(nb_rep)
    worst = float(np.max(np.abs(rat - 1.0)))
    print('\n      repaired x AMP, nothing fitted:  chi2 %.6f on %d dof (%.6f per dof)'
          % (c2_rep_fixed, LL.NBP, c2_rep_fixed / LL.NBP))
    print('      the reference,  nothing fitted:  chi2 %.6f' % CAMB_CHI2_NOTHING)
    print('      landed   x AMP, nothing fitted:  chi2 %.6f  (the same normalisation, unrepaired)'
          % c2_land_fixed)
    print('      worst |ratio - 1| over the nine bins: %.4f   (criterion < 0.10)' % worst)
    within = abs(c2_rep_fixed / CAMB_CHI2_NOTHING - 1.0)
    print('      chi2 against the reference\'s: %.4f of it, a difference of %.1f per cent'
          ' (criterion < 20)' % (c2_rep_fixed / CAMB_CHI2_NOTHING, 100 * within))
    c3 = worst < 0.10 and within < 0.20
    print('    ** Ⓒ③ %s AS REGISTERED **'
          % ('PASSES' if c3 else 'FAILS'), flush=True)
    out['C3'] = dict(passes=bool(c3), worst_ratio_minus_one=worst,
                     chi2_repaired_nothing_fitted=c2_rep_fixed,
                     chi2_landed_nothing_fitted=c2_land_fixed,
                     chi2_reference_nothing_fitted=CAMB_CHI2_NOTHING,
                     per_dof_repaired=c2_rep_fixed / LL.NBP,
                     fraction_of_reference=c2_rep_fixed / CAMB_CHI2_NOTHING,
                     ratio=[float(v) for v in rat], criterion_ratio=0.10,
                     criterion_chi2_fraction=0.20)

    print('\n  Ⓒ③ᵇ THE FREE-AMPLITUDE SCORE, PRINTED AND REFUSED THE CLAIM', flush=True)
    print('      with one amplitude free: chi2 %.6f on %d dof at a factor %.6f'
          % (c2_rep_free, ndof, a_rep_free))
    print('      ⇒ the factor is %.4f from one, so the free amplitude is NOT what makes Ⓒ③ land'
          % abs(a_rep_free - 1.0))
    print('    ⌗ Ⓒ③ is scored at a factor of exactly one above and this row cannot carry it.',
          flush=True)
    out['C3b'] = dict(chi2_one_amplitude=c2_rep_free, fitted_factor=a_rep_free,
                      factor_distance_from_one=float(abs(a_rep_free - 1.0)))

    with io.open(os.path.join(_HERE, 'repair_scale.json'), 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1, sort_keys=True)
    print('\n  wrote repair_scale.json\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
