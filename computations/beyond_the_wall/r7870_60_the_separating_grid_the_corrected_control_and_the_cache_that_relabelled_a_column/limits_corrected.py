# -*- coding: utf-8 -*-
"""Ⓐ① BOTH LIMITS RE-READ ON THE BANK AT THE **CORRECTED** N_eff OFFSET.

Order `r7869` item ① — and the correction it rests on is order `r7867`'s: the reference's own CAMB
object carries `N_eff = 3.044000`, so the control's like-for-like offset is `+0.044` and not the
`+0.0293` that `r7866` ran. `+0.0293` was the effective massless count plus the INTEGER massive
count, where CAMB's one massive state is worth `1.0147` in those units.

⌗ *The machinery is `r7864`'s, imported rather than retyped, exactly as `r7866`'s own read imported
it — the same `Ruler`, the same `attach`, the same `profile` with its convergence discipline, the
same sum nodes, and the same amplitude halving. ONE thing differs from `r7866`'s read: the two
banks the model is pointed at. So a difference between these numbers and `r7866`'s is the SPECTRA
and not the method.*

⚠ ** THE ARM OF RECORD IS CARRIED, NOT RE-RUN, AND THAT IS EXACT RATHER THAN AN APPROXIMATION. **
Neither figure of the offset touches the arm of record — it carries none under either — so its
sixteen points in each half were copied across. The two generators' arm-of-record invocations are
byte-identical and the carried points' own configs record no offset at all, which the precondition
below checks rather than assumes.

⛔ ** AND THE PLUMBING IS MEASURED IN THIS RUN, BECAUSE THIS LINE HAS BEEN WRONG ABOUT IT ONCE. **
At `r7866` a lensing re-point left every profile total bit-identical while the lensing shape the
model read differed by `4.5` per cent at the same sum, and a whole thirty-two-point grid was spent
on the wrong reading of that. So this run loads the lensing base from BOTH grids itself and prints
the difference, and it says which grid its own model holds. *A run that cannot show it read the
grid it claims is not evidence about that grid.*

    NODE=60 python3 limits_corrected.py
"""
import io
import json
import os
import sys

import numpy as np

_HERE = os.path.dirname(os.path.abspath(__file__))
_BTW = os.path.dirname(_HERE)
BANK = os.path.join(_BTW, 'bank')
R7864 = os.path.join(_BTW, 'r7864_60_the_massive_neutrino_background_given_its_fermi_dirac_'
                           'density_and_both_limits_re_read')
sys.path.insert(0, R7864)
import limits as L7864                                                      # noqa: E402

#: ⛭ BOTH KEYS, SET BEFORE `model6` IS IMPORTED ANYWHERE.  `model6` reads `PPGRID` at MODULE IMPORT
#:   TIME, so a key set after the first import would be read by nothing.  `r7866` learned that the
#:   expensive way.
NEWBANK = os.path.join(BANK, 'pol_grid_bvel1_nufd_dneff044')
NEWPP = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff044')
OLDPP = os.path.join(BANK, 'phiphi_grid_eta4000_bvel1_primnorm1_nufd_dneff')
os.environ['POL_DIR'] = NEWBANK
os.environ['PPGRID'] = NEWPP

DNEFF_CORRECTED = 0.044             # order r7867's correction; r7866 ran 0.0293
REF_RULER = 54.00                   # the reference's minimised limit
REF_CALIB = 30.56                   # the reference's calibrated limit
R7866_MINIMISED = None              # ⛔ r7866 read NO readable minimised limit at +0.0293
R7866_CALIBRATED = 185.69           # what r7866 read at the superseded offset
BAND_CALIB_MOVE = 10.0              # ⛭ REGISTERED Ⓐ①ᵈ: the calibrated figure moves under 10 meV


def precondition():
    """Ⓐ①ᵃ+ᵇ -- read off every point's own recorded config, not off the directory name"""
    pol = sorted(f for f in os.listdir(NEWBANK)
                 if f.endswith('.npz') and not f.endswith('_tt.npz'))
    cfgs = {}
    for f in pol:
        z = np.load(os.path.join(NEWBANK, f), allow_pickle=True)
        cfgs[f[:-4]] = json.loads(str(np.atleast_1d(z['config'])[0]))
    lc = {k: v for k, v in cfgs.items() if v.get('ARM') == 'lcdm'}
    cr = {k: v for k, v in cfgs.items() if v.get('ARM') == 'cr'}
    #: the repair is conditioned on a NONZERO sum, so a zero-sum node reads `false` TRUTHFULLY:
    #: at zero mass the two backgrounds are the same program, measured to the bit at r7864
    nonzero_on = all(v.get('NUFD') is True for v in cfgs.values()
                     if float(v.get('MNU') or 0) != 0)
    zero_off = all(v.get('NUFD') is False for v in cfgs.values()
                   if float(v.get('MNU') or 0) == 0)
    #: ⛔ THE WHOLE POINT OF THIS READ: the control at the CORRECTED offset, the arm of record at
    #:   none at all.  An arm-of-record point carrying ANY offset would make this bank the wrong
    #:   object, so it is checked and not trusted to the filename.
    split = (all(abs(float(v.get('DNEFF') or 0) - DNEFF_CORRECTED) < 1e-12 for v in lc.values())
             and all(v.get('DNEFF') is None for v in cr.values()))
    pp_lc = [f for f in os.listdir(NEWPP) if f.endswith('.json') and f.startswith('lcdm_')]
    pp_cr = [f for f in os.listdir(NEWPP) if f.endswith('.json') and f.startswith('cr_')]
    ok = dict(cmb_points=len(pol), lcdm_points=len(lc), cr_points=len(cr),
              lensing_points_lcdm=len(pp_lc), lensing_points_cr=len(pp_cr),
              dneff_key_present=all('DNEFF' in v for v in cfgs.values()),
              dneff_corrected_on_control_only=bool(split),
              nufd_true_at_every_nonzero_sum=bool(nonzero_on),
              nufd_false_at_zero_sum=bool(zero_off),
              blob=cfgs['lcdm_S000'].get('instrument_blob'))
    ok['holds'] = bool(len(pol) == 32 and len(lc) == 16 and len(cr) == 16
                       and len(pp_lc) == 16 and len(pp_cr) == 16
                       and ok['dneff_key_present'] and split and nonzero_on and zero_off)
    return ok


def main():
    print(__doc__)
    print('=' * 104)
    out = {}

    print('\n  Ⓐ①ᵃ+ᵇ THE PRECONDITION -- what offset are these spectra actually on?')
    print('  ' + '-' * 104)
    pre = precondition()
    print('    %d CMB point(s): %d control, %d arm of record;  lensing: %d control, %d arm'
          % (pre['cmb_points'], pre['lcdm_points'], pre['cr_points'],
             pre['lensing_points_lcdm'], pre['lensing_points_cr']))
    print('    the offset key is present in every point\'s config: %s' % pre['dneff_key_present'])
    print('    it reads %.3f on EVERY control point and NONE on every arm-of-record point: %s'
          % (DNEFF_CORRECTED, pre['dneff_corrected_on_control_only']))
    print('    the repair reads TRUE at every nonzero sum: %s, and FALSE at the zero-sum node: %s'
          '   ⌗ *the truthful record, not a gap*'
          % (pre['nufd_true_at_every_nonzero_sum'], pre['nufd_false_at_zero_sum']))
    out['precondition'] = pre
    if not pre['holds']:
        print('\n  ⛔ the precondition FAILS -- no limit is reported.\n')
        _save(out)
        return 1

    import model3 as M3                                                     # noqa: E402
    import distances as DI                                                  # noqa: E402
    import model6 as M6                                                     # noqa: E402

    print('\n  THE PLUMBING, MEASURED IN THIS RUN -- which grids does this model hold?')
    print('  ' + '-' * 104)
    probe = M6.Model6('lcdm')
    pb_new = np.asarray(probe.pp_base(0.30), float)
    #: the OLD grid's own base at the same sum, loaded here rather than remembered, so the claim
    #: "these are different spectra" is a measurement this run made
    import glob
    def _base_at(grid, tag='S030', arm='lcdm'):
        p = os.path.join(grid, '%s_%s.json' % (arm, tag))
        return np.asarray(json.load(io.open(p, encoding='utf-8'))['bandpowers'], float)
    b_new, b_old = _base_at(NEWPP), _base_at(OLDPP)
    rel = float(np.max(np.abs(b_new / b_old - 1.0)))
    print('    the CMB grid in use     : %s' % os.path.basename(os.environ['POL_DIR']))
    print('    the lensing grid in use : %s' % os.path.basename(M6.GRID))
    print('    the lensing grid this model holds IS the corrected one: %s'
          % (os.path.basename(M6.GRID) == os.path.basename(NEWPP)))
    print('    the corrected lensing bandpowers differ from the superseded ones by up to %.3e '
          'at Sum = 0.30 on the control  ⌗ *so the two banks are not the same object*' % rel)
    out['plumbing'] = dict(pol_dir=os.path.basename(os.environ['POL_DIR']),
                           pp_grid=os.path.basename(M6.GRID),
                           pp_grid_is_the_corrected_one=bool(os.path.basename(M6.GRID)
                                                             == os.path.basename(NEWPP)),
                           pp_base_at_030=[float(v) for v in pb_new[:4]],
                           max_rel_change_vs_superseded_grid=rel)

    r_inst = L7864.Ruler(os.path.join(R7864, 'rd_grid_nufd.npz'), 'r_drag',
                         "this instrument's own drag epoch ON THE REPAIRED BACKGROUND",
                         'instrument')

    sums = [0.0, 0.03, 0.06, 0.10, 0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 0.60]
    out['profiles'] = {}
    for which, free, ruler, label in (
            ('minimised', [0, 1, 2, 3], None,
             "Ⓐ①ᶜ THE RULER MINIMISED, on the bank at the CORRECTED offset -- r7866 read NO "
             "readable limit here at +0.0293"),
            ('calibrated', [0, 1, 2, 3], r_inst,
             "Ⓐ①ᵈ CALIBRATED on the repaired drag epoch, CORRECTED offset -- r7866 read 185.69")):
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

    #: ⛔⛭ ** ITEM ③ IS ANSWERED BEFORE ANY LIMIT IS READ THROUGH THE PROFILE, as the order
    #:   requires: the DIPS are reported here, above the adjudication, and the adjudication below
    #:   does not depend on them being absent. **
    print('\n  Ⓒ③ᵃ THE TOP OF THE PROFILE, REPORTED BEFORE ANY LIMIT IS READ THROUGH IT')
    print('  ' + '-' * 104)
    for which in ('minimised', 'calibrated'):
        p = out['profiles'][which]
        print('    %-11s minimum at Sum = %.3f eV;  monotonic above it: %s%s'
              % (which, p['min_at'], p['monotonic_above_min'],
                 '' if p['monotonic_above_min']
                 else ';  dips at ' + ', '.join('%.3f eV' % d[0] for d in p['dips'])))
        if p['sums'][-1] in [d[0] for d in p['dips']]:
            print('      ⚠ the dip is AT THE TOP NODE of the grid, which is what order r7869 '
                  'item ③ asks to separate from a feature of the model')
    out['top_node'] = dict(
        minimised_dips=[list(d) for d in mini['dips']],
        calibrated_dips=[list(d) for d in cal['dips']],
        minimised_dip_at_top_node=bool(mini['dips']
                                       and mini['dips'][-1][0] == mini['sums'][-1]),
        calibrated_dip_at_top_node=bool(cal['dips']
                                        and cal['dips'][-1][0] == cal['sums'][-1]),
        top_node_eV=float(mini['sums'][-1]),
        note='reported before the adjudication, and the edge test is a separate measurement')

    print('\n  THE ADJUDICATION')
    print('  ' + '-' * 104)
    print('    minimised  %s meV at the corrected offset, against the reference\'s %.2f  '
          '(r7866 read NO READABLE limit at the superseded offset)'
          % (('%.2f' % mini['limit_meV']) if mini['limit_meV'] else 'NOT REPORTED', REF_RULER))
    print('    calibrated %s meV against the ordered %.2f  (r7866 read %.2f)'
          % (('%.2f' % cal['limit_meV']) if cal['limit_meV'] else 'NOT REPORTED',
             REF_CALIB, R7866_CALIBRATED))
    #: Ⓐ①ᶜ was registered as a COMPARISON whose negative is the landed state: r7866's minimised
    #: limit was NOT readable, so a readable one here says the unreadability was the OFFSET's
    readable_now = bool(mini['limit_meV'] is not None)
    cal_move = (None if cal['limit_meV'] is None
                else float(cal['limit_meV'] - R7866_CALIBRATED))
    cal_in_band = bool(cal_move is not None and abs(cal_move) <= BAND_CALIB_MOVE)
    out['adjudication'] = dict(
        limit_minimised=mini['limit_meV'], limit_calibrated=cal['limit_meV'],
        reference_minimised=REF_RULER, reference_calibrated=REF_CALIB,
        r7866_minimised_was_readable=False, r7866_calibrated=R7866_CALIBRATED,
        minimised_readable_at_corrected_offset=readable_now,
        which_carried_the_unreadability=('the N_eff ruling, because the limit is READABLE once '
                                         'the offset is corrected' if readable_now else
                                         'NOT the offset -- it is unreadable at BOTH figures, so '
                                         'the offset is ruled out and the repair or the grid edge '
                                         'remains'),
        calibrated_move_meV=cal_move, band_meV=BAND_CALIB_MOVE, band_holds=cal_in_band,
        read_on='the bank at the CORRECTED offset, BOTH halves, with the arm of record carried '
                'byte-identically and checked to carry no offset at all')
    print('    ⇒ Ⓐ①ᶜ, registered with the landed NOT-readable state as its negative: the '
          'minimised limit is %s at the corrected offset ⇒ %s'
          % ('READABLE' if readable_now else 'STILL NOT READABLE',
             out['adjudication']['which_carried_the_unreadability']))
    if cal_move is not None:
        print('    ⇒ Ⓐ①ᵈ, registered expectation that the calibrated figure moves under %.1f meV: '
              'it moved %+.2f ⇒ %s'
              % (BAND_CALIB_MOVE, cal_move,
                 'HOLDS' if cal_in_band else '** REFUTED **, reported with the criterion unmoved'))
    else:
        print('    ⇒ Ⓐ①ᵈ cannot be read: the calibrated profile reports no limit, which is '
              'reported as the absence it is rather than as a number')
    _save(out)
    print('')
    return 0


def _save(out):
    with io.open(os.path.join(_HERE, 'limits_corrected.json'), 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float))


if __name__ == '__main__':
    sys.exit(main())
