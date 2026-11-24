# -*- coding: utf-8 -*-
"""Ⓒ③ BOTH LIMITS RE-READ ON THE **RE-SOLVED** BANK, and the precondition answered from the other
side.

`r7864` read both limits on the LANDED bank with the ruler repaired, and proved from the bank's
own recorded config that those spectra could not say which background solved them -- the switch
key was ABSENT, so the bank predated the repair and could not even say `false`.  Item ③ of order
`r7865` asks for the bank itself re-solved.  It is, at all thirty-two points, and now the
precondition runs the other way: the key is PRESENT at every node where there is anything to say.

⌗ *The machinery is `r7864`'s own -- its `Ruler`, its `attach`, its `profile` with the same
convergence discipline -- imported rather than retyped, with one thing changed: the bank the model
reads.  So a difference between this file's numbers and `r7864`'s is the SPECTRA and not the
method.*

⚠ ** A SCOPE LIMIT, DECLARED RATHER THAN DISCOVERED BY A READER: the CMB bandpower bank is
re-solved and the LENSING-POTENTIAL bank is not. ** The lensing grid was solved on the old
background and this revision does not re-solve it, so the lensing term in both limits still rides
spectra from before the repair.  That is named here and in the record, and it bounds what these
two numbers are.

    NODE=60 python3 limits_resolved.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7864 = os.path.join(_BTW, 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_density_and_both_limits_re_read')
sys.path.insert(0, R7864)
import limits as L7864                                                      # noqa: E402

#: ⛭ THE ONE CHANGE: the bank the model reads.  `limits` set this to the landed grid at import.
NEWBANK = os.path.join(BANK, 'pol_grid_bvel1_nufd_dneff')
os.environ['POL_DIR'] = NEWBANK

REF_RULER = 54.00                   # the reference's minimised limit, the order's comparison
REF_CALIB = 30.56                   # the reference's calibrated limit
R7864_MINIMISED = 69.97             # what the landed bank gave, with the ruler repaired
R7864_CALIBRATED = 81.94
BAND_OF_54 = 8.0                    # ⛭ REGISTERED Ⓒ③ᵈ: within 8 meV of 54.00


def precondition():
    """Ⓒ③ᵇ -- the re-solved bank's own config, and what it can now say that the old one could not"""
    pol = sorted(f for f in os.listdir(NEWBANK)
                 if f.endswith('.npz') and not f.endswith('_tt.npz'))
    cfgs = {}
    for f in pol:
        z = np.load(os.path.join(NEWBANK, f), allow_pickle=True)
        cfgs[f[:-4]] = json.loads(str(np.atleast_1d(z['config'])[0]))
    lc = {k: v for k, v in cfgs.items() if v.get('ARM') == 'lcdm'}
    cr = {k: v for k, v in cfgs.items() if v.get('ARM') == 'cr'}
    #: the repair is conditioned on a NONZERO sum, so a zero-sum node reads `false` TRUTHFULLY --
    #: at zero mass the two backgrounds are the same program, which r7864 measured to the bit
    nonzero_on = all(v.get('NUFD') is True for v in cfgs.values() if float(v.get('MNU') or 0) != 0)
    zero_off = all(v.get('NUFD') is False for v in cfgs.values()
                   if float(v.get('MNU') or 0) == 0)
    dneff_split = (all(abs(float(v.get('DNEFF') or 0) - 0.0293) < 1e-12 for v in lc.values())
                   and all(v.get('DNEFF') is None for v in cr.values()))
    pp = [f for f in os.listdir(os.environ['PPGRID'])
          if f.endswith('.json') and f.startswith('lcdm_')]
    ok = dict(cmb_points=len(pol), lcdm_points=len(lc), cr_points=len(cr),
              lensing_points_lcdm=len(pp),
              nufd_key_present=all('NUFD' in v for v in cfgs.values()),
              nufd_true_at_every_nonzero_sum=bool(nonzero_on),
              nufd_false_at_zero_sum=bool(zero_off),
              dneff_on_control_only=bool(dneff_split),
              lensing_bank_resolved=False,
              blob=cfgs['lcdm_S000'].get('instrument_blob'))
    ok['holds'] = bool(len(pol) == 32 and len(lc) == 16 and len(cr) == 16
                       and ok['nufd_key_present'] and nonzero_on and zero_off and dneff_split
                       and len(pp) >= 16)
    return ok


def main():
    print(__doc__)
    print('=' * 104)
    out = {}

    print('\n  Ⓒ③ᵃ+ᵇ THE PRECONDITION, RUN THE OTHER WAY -- what can the re-solved bank say?')
    print('  ' + '-' * 104)
    pre = precondition()
    print('    %d CMB point(s): %d control, %d arm of record; %d lensing point(s)'
          % (pre['cmb_points'], pre['lcdm_points'], pre['cr_points'],
             pre['lensing_points_lcdm']))
    print('    the switch key is present in every point\'s config: %s' % pre['nufd_key_present'])
    print('    it reads TRUE at every nonzero sum: %s' % pre['nufd_true_at_every_nonzero_sum'])
    print('    and FALSE at the zero-sum node: %s   ⌗ *which is the TRUTHFUL record: the repair is '
          'conditioned on a nonzero sum, so at zero mass the two backgrounds are one program*'
          % pre['nufd_false_at_zero_sum'])
    print('    the ruling\'s DNEFF is on the CONTROL only, the arm of record carrying none: %s'
          % pre['dneff_on_control_only'])
    print('    ⚠ the LENSING bank is NOT re-solved: declared, and it bounds both numbers below')
    out['precondition'] = pre
    if not pre['holds']:
        print('\n  ⛔ the precondition FAILS -- no limit is reported.\n')
        _save(out)
        return 1

    import model3 as M3
    import distances as DI
    import model6 as M6

    r_inst = L7864.Ruler(os.path.join(R7864, 'rd_grid_nufd.npz'), 'r_drag',
                         "this instrument's own drag epoch ON THE REPAIRED BACKGROUND",
                         'instrument')

    sums = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
    out['profiles'] = {}
    for which, free, ruler, label in (
            ('minimised', [0, 1, 2, 3], None,
             "Ⓒ③ᶜ THE RULER MINIMISED, on the RE-SOLVED bank -- against the reference's 54.00 meV"),
            ('calibrated', [0, 1, 2, 3], r_inst,
             "Ⓒ③ᶜ CALIBRATED on the repaired drag epoch, RE-SOLVED bank -- against 30.56 meV")):
        mod = M6.Model6('lcdm')
        raw = mod.amp_cmb
        mod.amp_cmb = lambda x4, s, _r=raw: _r(x4, s) / 2.0
        ss = [s for s in sums if mod.cmb.s_lo - 1e-9 <= s <= mod.cmb.s_hi + 1e-9]
        if ruler is not None:
            L7864.attach(mod, ruler, M3, DI)
        res = L7864.profile(mod, ss, label, free, ruler)
        res['clipped_calls'] = (0 if ruler is None else int(ruler.clipped))
        out['profiles'][which] = res

    mini, cal = out['profiles']['minimised'], out['profiles']['calibrated']
    print('\n  THE ADJUDICATION')
    print('  ' + '-' * 104)
    print('    minimised  %s meV on the re-solved bank, against the reference\'s %.2f  '
          '(r7864 read %.2f on the landed bank)'
          % (('%.2f' % mini['limit_meV']) if mini['limit_meV'] else 'NOT REPORTED',
             REF_RULER, R7864_MINIMISED))
    print('    calibrated %s meV against the ordered %.2f  (r7864 read %.2f)'
          % (('%.2f' % cal['limit_meV']) if cal['limit_meV'] else 'NOT REPORTED',
             REF_CALIB, R7864_CALIBRATED))
    moved_toward = (None if mini['limit_meV'] is None
                    else bool(abs(mini['limit_meV'] - REF_RULER)
                              < abs(R7864_MINIMISED - REF_RULER)))
    gap54 = None if mini['limit_meV'] is None else abs(mini['limit_meV'] - REF_RULER)
    in_band = bool(gap54 is not None and gap54 <= BAND_OF_54)
    out['adjudication'] = dict(
        limit_minimised=mini['limit_meV'], limit_calibrated=cal['limit_meV'],
        reference_minimised=REF_RULER, reference_calibrated=REF_CALIB,
        r7864_minimised=R7864_MINIMISED, r7864_calibrated=R7864_CALIBRATED,
        expectation_moved_toward_54=moved_toward,
        band_meV=BAND_OF_54, gap_to_54=gap54, band_holds=in_band,
        read_on='the RE-SOLVED bank, CMB only; the lensing bank is not re-solved and that is '
                'declared')
    print('    ⇒ the REGISTERED EXPECTATION was that the minimised limit moves TOWARDS 54.00 from '
          '%.2f: %s' % (R7864_MINIMISED,
                        'MET' if moved_toward else '** REFUTED **, reported with the number'))
    print('    ⇒ the REGISTERED BAND was within %.1f meV of 54.00; the gap is %s: %s'
          % (BAND_OF_54, ('%.2f' % gap54) if gap54 is not None else 'unreadable',
             'HOLDS' if in_band else '** FAILS **, reported as failed with the criterion unmoved'))
    _save(out)
    print('')
    return 0


def _save(out):
    with io.open(os.path.join(_HERE, 'limits_resolved.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))


if __name__ == '__main__':
    sys.exit(main())
